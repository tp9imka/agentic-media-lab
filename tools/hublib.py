"""Shared library for the hub tools: config, data loading, the schema-subset validator,
reference checks, the evidence badge and markdown helpers. Stdlib only."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import date
from pathlib import Path

DEFAULT_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_VERSION = 1
SCHEMA_FILES = ("record", "concept", "page", "example")
GENERATED_DOCS = ("docs/SCHEMA.md", "docs/glossary.md")
SKIP_DIRS = {".git", ".ref", "__pycache__", "node_modules", ".venv", "venv"}
INACTIVE_STATUSES = ("archived", "retracted")
SHUT_DOWN = "shut-down"
MAX_BROADER = 2
DATE_FIELDS = ("checked.date", "checked.next_due", "citation.accessed")

SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9._/-]*$")
CONCEPT_PREFIX = "concept:"

# Validator subset. Annotation keywords are allowed and ignored; anything else is a schema bug.
KEYWORDS = {"type", "required", "enum", "pattern", "properties", "items", "additionalProperties", "allOf", "if", "then"}
ANNOTATIONS = {"$schema", "$id", "title", "description", "$comment"}

# Categories of problems; the build summary line counts them separately.
DANGLING, BAD_CONCEPT, INVALID = "dangling", "bad concept", "invalid"


class HubError(Exception):
    """Unusable config, schema or environment (not a data problem)."""


# ---------------------------------------------------------------- basics

def root_from_args(description: str, argv=None, extra=None) -> tuple[Path, argparse.Namespace]:
    ap = argparse.ArgumentParser(description=description)
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT, help="hub root (default: this repo)")
    if extra:
        extra(ap)
    args = ap.parse_args(argv)
    return args.root.resolve(), args


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_text(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def load_config(root: Path) -> dict:
    path = root / "hub.config.json"
    if not path.exists():
        raise HubError(f"{path}: missing")
    cfg = read_json(path)
    need = ("name", "title", "base_url", "kinds", "review_interval_days", "popularity_disagreement_ratio",
            "page_char_budget", "measured_rungs", "lifetime")
    missing = [k for k in need if k not in cfg]
    if missing:
        raise HubError(f"hub.config.json: missing {', '.join(missing)}")
    if not cfg["base_url"].endswith("/"):
        raise HubError("hub.config.json: base_url must end with /")
    return cfg


def load_schemas(root: Path) -> dict:
    out = {}
    for name in SCHEMA_FILES:
        path = root / "data" / "schema" / f"{name}.schema.json"
        if not path.exists():
            raise HubError(f"data/schema/{name}.schema.json: missing")
        out[name] = read_json(path)
        check_schema_subset(out[name], f"{name}.schema.json")
    return out


def build_date() -> date:
    raw = os.environ.get("HUB_BUILD_DATE")
    if not raw:
        return date.today()
    try:
        return parse_date(raw)
    except ValueError:
        raise HubError(f"HUB_BUILD_DATE={raw!r}: expected YYYY-MM-DD") from None


def parse_date(s: str) -> date:
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", s or ""):
        raise ValueError(s)
    return date.fromisoformat(s)


def slug_of(record_id: str) -> str:
    return record_id.split(":", 1)[1]


def page_path(record_id: str) -> str:
    kind, slug = record_id.split(":", 1)
    return f"catalog/{kind}/{slug.replace('/', '__')}.md"


def concept_anchor(concept_id: str) -> str:
    return concept_id[len(CONCEPT_PREFIX):]


def is_inactive(rec: dict) -> bool:
    return (rec.get("status") in INACTIVE_STATUSES or rec.get("maturity") == SHUT_DOWN
            or rec.get("access") == SHUT_DOWN)


def inactive_label(rec: dict) -> str:
    return rec["status"] if rec.get("status") in INACTIVE_STATUSES else "shut down"


def repo_files(root: Path) -> list[Path]:
    """Tracked plus untracked-but-not-ignored files; every file when root is not a git top level."""
    files = None
    try:
        top = subprocess.run(["git", "rev-parse", "--show-toplevel"], cwd=root, capture_output=True,
                             text=True, check=True).stdout.strip()
        if Path(top).resolve() == root.resolve():
            out = subprocess.run(["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
                                 cwd=root, capture_output=True, check=True).stdout
            files = sorted({root / p for p in out.decode("utf-8", "replace").split("\0") if p})
    except (OSError, subprocess.CalledProcessError):
        files = None
    if files is None:
        files = sorted(p for p in root.rglob("*") if p.is_file())
    return [p for p in files if p.is_file() and not (SKIP_DIRS & set(p.relative_to(root).parts))]


# ---------------------------------------------------------------- validator

def check_schema_subset(schema, where: str) -> None:
    if not isinstance(schema, dict):
        raise HubError(f"{where}: schema must be an object")
    unknown = set(schema) - KEYWORDS - ANNOTATIONS
    if unknown:
        raise HubError(f"{where}: keyword(s) outside the validator subset: {', '.join(sorted(unknown))}")
    for k, sub in schema.get("properties", {}).items():
        check_schema_subset(sub, f"{where}.properties.{k}")
    for key in ("items", "if", "then"):
        if key in schema:
            check_schema_subset(schema[key], f"{where}.{key}")
    for i, sub in enumerate(schema.get("allOf", [])):
        check_schema_subset(sub, f"{where}.allOf[{i}]")


def json_type(v) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "boolean"
    if isinstance(v, int):
        return "integer"
    if isinstance(v, float):
        return "number"
    if isinstance(v, str):
        return "string"
    if isinstance(v, list):
        return "array"
    return "object"


def type_ok(v, t: str) -> bool:
    actual = json_type(v)
    return actual == t or (t == "number" and actual == "integer")


def _join(where: str, key: str) -> str:
    return f"{where}.{key}" if where else key


def validate(value, schema: dict, where: str = "") -> list[tuple[str, str]]:
    """(field path, problem) pairs for the subset: type, required, enum, pattern, properties,
    items, additionalProperties: false, allOf, if/then."""
    if "type" in schema:
        types = schema["type"] if isinstance(schema["type"], list) else [schema["type"]]
        if not any(type_ok(value, t) for t in types):
            return [(where, f"expected {' or '.join(types)}, got {json_type(value)}")]
    errs = []
    if "enum" in schema and value not in schema["enum"]:
        errs.append((where, f"{value!r} is not one of: {', '.join(map(str, schema['enum']))}"))
    if "pattern" in schema and isinstance(value, str) and not re.search(schema["pattern"], value):
        errs.append((where, f"{value!r} does not match {schema['pattern']}"))
    if isinstance(value, dict):
        for req in schema.get("required", []):
            if req not in value:
                errs.append((_join(where, req), "missing required field"))
        props = schema.get("properties", {})
        for k, sub in props.items():
            if k in value:
                errs += validate(value[k], sub, _join(where, k))
        if schema.get("additionalProperties") is False:
            errs += [(_join(where, k), "unknown field") for k in value if k not in props]
    if isinstance(value, list) and "items" in schema:
        for i, item in enumerate(value):
            errs += validate(item, schema["items"], f"{where}[{i}]")
    for sub in schema.get("allOf", []):
        errs += validate(value, sub, where)
    if "if" in schema and not validate(value, schema["if"], where):
        errs += validate(value, schema.get("then", {}), where)
    return errs


def kind_required(record_schema: dict) -> dict[str, list[str]]:
    """kind => fields its allOf/if/then block requires."""
    out = {}
    for block in record_schema.get("allOf", []):
        kinds = block.get("if", {}).get("properties", {}).get("kind", {}).get("enum", [])
        for k in kinds:
            out.setdefault(k, []).extend(block.get("then", {}).get("required", []))
    return out


def schema_enum(schema: dict, dotted: str) -> list:
    node = schema
    for part in dotted.split("."):
        node = node["items"] if part == "[]" else node["properties"][part]
    return node.get("enum", [])


# ---------------------------------------------------------------- frontmatter

def _scalar(raw: str):
    raw = raw.strip()
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    return raw


def _strip_comment(raw: str) -> str:
    quote = None
    for i, ch in enumerate(raw):
        if ch in "\"'" and quote in (None, ch):
            quote = None if quote else ch
        elif ch == "#" and quote is None and (i == 0 or raw[i - 1] in " \t"):
            return raw[:i].rstrip()
    return raw.rstrip()


def parse_frontmatter(text: str) -> tuple[dict | None, str, list[str]]:
    """(fields or None when absent, body, problems). Supports `key: value`, `key: [a, b]`,
    quoted strings, block lists (`- item`) and trailing `# comments`."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text, []
    try:
        end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration:
        return None, text, ["frontmatter: no closing ---"]
    fields, problems, key = {}, [], None
    for n, line in enumerate(lines[1:end], start=2):
        stripped = _strip_comment(line).strip()
        if not stripped:
            continue
        if stripped.startswith("- ") and key and (fields.get(key) == "" or isinstance(fields.get(key), list)):
            if fields[key] == "":
                fields[key] = []
            fields[key].append(_scalar(stripped[2:]))
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
        if not m or line[:1].isspace():
            problems.append(f"frontmatter line {n}: cannot parse {line.strip()!r}")
            continue
        key, raw = m.group(1), m.group(2)
        if raw.startswith("[") and raw.endswith("]"):
            fields[key] = [_scalar(x) for x in raw[1:-1].split(",") if x.strip()]
        else:
            fields[key] = _scalar(raw)
    return fields, "\n".join(lines[end + 1:]), problems


# ---------------------------------------------------------------- markdown

FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
EXPLICIT_BRACE_RE = re.compile(r"\s*\{#([A-Za-z0-9_-]+)\}\s*$")
HTML_ANCHOR_RE = re.compile(r"""<a\s+(?:id|name)=["']([^"']+)["']\s*>\s*</a>""")


def gh_slug(text: str) -> str:
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    s = re.sub(r"[^\w\- ]", "", text.strip().lower())
    return s.replace(" ", "-")


def strip_code(text: str) -> str:
    """Blank fenced blocks and inline code so links inside them are not checked."""
    out, fenced = [], False
    for line in text.split("\n"):
        if FENCE_RE.match(line):
            fenced = not fenced
            out.append("")
            continue
        out.append("" if fenced else re.sub(r"`[^`\n]*`", "", line))
    return "\n".join(out)


def headings(text: str) -> list[tuple[int, int, str, str, list[str]]]:
    """(line index, level, title, anchor, all anchors) for ATX headings outside code fences."""
    out, seen, fenced = [], {}, False
    for i, line in enumerate(text.split("\n")):
        if FENCE_RE.match(line):
            fenced = not fenced
            continue
        m = None if fenced else HEADING_RE.match(line)
        if not m:
            continue
        raw = m.group(2)
        explicit = []
        brace = EXPLICIT_BRACE_RE.search(raw)
        if brace:
            explicit.append(brace.group(1))
            raw = raw[:brace.start()]
        explicit += HTML_ANCHOR_RE.findall(raw)
        title = HTML_ANCHOR_RE.sub("", raw).strip()
        base = gh_slug(raw)
        n = seen.get(base, 0)
        seen[base] = n + 1
        auto = base if n == 0 else f"{base}-{n}"
        anchors = explicit + [auto]
        out.append((i, len(m.group(1)), title, anchors[0], anchors))
    return out


def anchors_of(text: str) -> set[str]:
    found = set(HTML_ANCHOR_RE.findall(strip_code(text)))
    for h in headings(text):
        found.update(h[4])
    return found


def chunks(body: str) -> list[dict]:
    """Heading-level chunks: {anchor, heading_path, text}. Text before the first heading is a chunk
    with an empty anchor. Chunks with no text are dropped."""
    lines = body.split("\n")
    hs = headings(body)
    out, path = [], []
    starts = [(0, None)] + [(h[0], h) for h in hs]
    for n, (start, h) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        if h:
            path = [p for p in path if p[0] < h[1]] + [(h[1], h[2])]
            text_lines = lines[start + 1:end]
        else:
            text_lines = lines[start:end]
        text = HTML_ANCHOR_RE.sub("", "\n".join(text_lines)).strip()
        if text:
            out.append({"anchor": h[3] if h else "", "heading_path": [p[1] for p in path], "text": text})
    return out


def first_heading(text: str) -> str | None:
    for h in headings(text):
        if h[1] == 1:
            return h[2]
    return None


# ---------------------------------------------------------------- evidence badge

TIER_ORDER = ("measured", "quoted-primary", "quoted-secondary", "unverified")
TIER_LABELS = {"measured": "measured by us", "quoted-primary": "quoted, primary source read",
               "quoted-secondary": "quoted, not read at the primary source", "unverified": "unverified"}
PRIMARY_SOURCE_TYPES = ("primary", "independent-secondary", "vendor-or-author")
BADGE_TABLE = (
    ("measured", "`measured.rung` is one of `measured_rungs` in hub.config.json and `measured.command`, "
                 "`measured.input`, `measured.commit` are set"),
    ("quoted-primary", "at least one claim, `checked.depth` is primary-read, no claim has `via`, `source_type` is "
                       + ", ".join(PRIMARY_SOURCE_TYPES) + ", and `corroboration` is not contested"),
    ("quoted-secondary", "at least one claim and `checked.depth` is primary-read or skim, but a quoted-primary "
                         "condition fails; the reasons name which"),
    ("unverified", "everything else: no claims, or `checked.depth` is not-checked"),
)


def derive_badge(rec: dict, measured_rungs: list[str]) -> dict:
    reasons = []
    m = rec.get("measured") or {}
    claims = rec.get("claims") or []
    depth = (rec.get("checked") or {}).get("depth")
    if m.get("rung") in measured_rungs and all(m.get(k) for k in ("command", "input", "commit")):
        tier = "measured"
        reasons.append(f"rung {m['rung']}")
    elif not claims:
        tier = "unverified"
        reasons.append("no claims")
    elif depth not in ("primary-read", "skim"):
        tier = "unverified"
        reasons.append("not checked")
    else:
        blockers = []
        if depth != "primary-read":
            blockers.append("checked by skim")
        if any(c.get("via") for c in claims):
            blockers.append("a claim is quoted via a secondary source")
        if rec.get("source_type") not in PRIMARY_SOURCE_TYPES:
            blockers.append(f"source type {rec.get('source_type')}")
        if rec.get("corroboration") == "contested":
            blockers.append("contested")
        tier = "quoted-secondary" if blockers else "quoted-primary"
        reasons += blockers or ["primary source read"]
    down = rec.get("downgrade")
    if down and tier != "unverified":
        tier = TIER_ORDER[TIER_ORDER.index(tier) + 1]
        reasons.append(f"downgraded one step: {down.get('reason')}")
    if rec.get("url_status") in ("dead", "moved"):
        reasons.append(f"link {rec['url_status']}")
    label = TIER_LABELS[tier] + (f" ({m['rung']})" if tier == "measured" else "")
    return {"tier": tier, "label": label, "reasons": reasons}


def popularity_flag(observed: dict, ratio: float) -> str | None:
    stars, installs = observed.get("stars"), observed.get("installs")
    if json_type(stars) not in ("integer", "number") or json_type(installs) not in ("integer", "number"):
        return None
    hi, lo = max(stars, installs, 1), max(min(stars, installs), 1)
    return "disagree" if hi / lo > ratio else None


# ---------------------------------------------------------------- loading

class Hub:
    """Everything loaded and checked from one hub root."""

    def __init__(self, root: Path):
        self.root = root
        self.config = load_config(root)
        self.schemas = load_schemas(root)
        self.problems: list[tuple[str, str]] = []
        self.warnings: list[str] = []
        self.records: dict[str, dict] = {}
        self.record_file: dict[str, str] = {}
        self.concepts: list[dict] = []
        self.concepts_lane = "vocabulary"
        self.observed: dict = {}
        self.pages: list[dict] = []
        self.examples: list[dict] = []

    def problem(self, category: str, file: str, rid: str, field: str, msg: str) -> None:
        self.problems.append((category, f"{file}: {rid or '-'}: {field or '-'}: {msg}"))

    def count(self, category: str) -> int:
        return sum(1 for c, _ in self.problems if c == category)


def iter_data_files(root: Path, kinds: list[str]):
    for kind in kinds:
        for f in sorted((root / "data" / kind).glob("*.json")):
            yield kind, f


def read_records(root: Path, kinds: list[str]) -> list[tuple[str, dict]]:
    """(repo-relative file, record) without validation; unreadable files are skipped."""
    out = []
    for _, f in iter_data_files(root, kinds):
        try:
            obj = read_json(f)
        except (OSError, ValueError):
            continue
        recs = obj.get("records", []) if isinstance(obj, dict) else []
        out += [(f.relative_to(root).as_posix(), r) for r in recs if isinstance(r, dict)]
    return out


def _wrapper_problems(obj, rel: str) -> list[str]:
    if not isinstance(obj, dict):
        return ["file must be an object {schema_version, lane, records}"]
    out = []
    if obj.get("schema_version") != SCHEMA_VERSION:
        out.append(f"schema_version must be {SCHEMA_VERSION}")
    if not isinstance(obj.get("lane"), str) or not obj.get("lane"):
        out.append("lane must be a non-empty string")
    if not isinstance(obj.get("records"), list):
        out.append("records must be a list")
    extra = set(obj) - {"schema_version", "lane", "records"}
    if extra:
        out.append(f"unknown top-level key(s): {', '.join(sorted(extra))}")
    return out


def load_hub(root: Path) -> Hub:
    hub = Hub(root)
    _load_concepts(hub)
    _load_records(hub)
    _check_references(hub)
    _load_observed(hub)
    _load_pages(hub)
    _load_examples(hub)
    return hub


def _load_concepts(hub: Hub) -> None:
    path = hub.root / "data" / "concepts.json"
    rel = "data/concepts.json"
    if not path.exists():
        hub.warnings.append("data/concepts.json is missing: the vocabulary is empty")
        return
    try:
        obj = read_json(path)
    except ValueError as e:
        hub.problem(INVALID, rel, "", "", f"not valid JSON: {e}")
        return
    if isinstance(obj, list):
        hub.warnings.append("data/concepts.json is a bare list; expected {schema_version, lane, records}")
        items = obj
    else:
        for p in _wrapper_problems(obj, rel):
            hub.problem(INVALID, rel, "", "", p)
        items = obj.get("records", []) if isinstance(obj, dict) and isinstance(obj.get("records"), list) else []
        if isinstance(obj, dict) and isinstance(obj.get("lane"), str) and obj["lane"]:
            hub.concepts_lane = obj["lane"]
    seen = set()
    for c in items:
        cid = c.get("id", "") if isinstance(c, dict) else ""
        for field, msg in validate(c, hub.schemas["concept"]):
            hub.problem(INVALID, rel, cid, field, msg)
        if not isinstance(c, dict) or not isinstance(cid, str):
            continue
        if cid in seen:
            hub.problem(INVALID, rel, cid, "id", "duplicate concept id")
            continue
        seen.add(cid)
        if len(c.get("broader") or []) > MAX_BROADER:
            hub.problem(INVALID, rel, cid, "broader", f"at most {MAX_BROADER} parents")
        hub.concepts.append(c)
    hub.concepts.sort(key=lambda c: c["id"])
    ids = {c["id"] for c in hub.concepts}
    for c in hub.concepts:
        for field in ("broader", "related"):
            for ref in c.get(field) or []:
                if ref not in ids:
                    hub.problem(BAD_CONCEPT, rel, c["id"], field, f"unknown concept {ref}")
                elif ref == c["id"]:
                    hub.problem(INVALID, rel, c["id"], field, "refers to itself")
    _check_concept_cycles(hub)


def _check_concept_cycles(hub: Hub) -> None:
    parents = {c["id"]: [p for p in c.get("broader") or [] if p != c["id"]] for c in hub.concepts}
    for start in parents:
        stack, seen = list(parents[start]), set()
        while stack:
            cur = stack.pop()
            if cur == start:
                hub.problem(INVALID, "data/concepts.json", start, "broader", "cycle in broader chain")
                break
            if cur in seen:
                continue
            seen.add(cur)
            stack += parents.get(cur, [])


def _check_dates(hub: Hub, rel: str, rid: str, rec: dict) -> None:
    for dotted in DATE_FIELDS:
        head, tail = dotted.split(".")
        val = (rec.get(head) or {}).get(tail) if isinstance(rec.get(head), dict) else None
        if isinstance(val, str):
            try:
                parse_date(val)
            except ValueError:
                hub.problem(INVALID, rel, rid, dotted, f"{val!r} is not a calendar date")
    for i, c in enumerate(rec.get("claims") or []):
        val = c.get("retrieved") if isinstance(c, dict) else None
        if isinstance(val, str):
            try:
                parse_date(val)
            except ValueError:
                hub.problem(INVALID, rel, rid, f"claims[{i}].retrieved", f"{val!r} is not a calendar date")
    chk = rec.get("checked") if isinstance(rec.get("checked"), dict) else {}
    try:
        if parse_date(chk.get("next_due", "")) < parse_date(chk.get("date", "")):
            hub.problem(INVALID, rel, rid, "checked.next_due", "is before checked.date")
    except ValueError:
        pass


def _check_id(hub: Hub, rel: str, kind: str, rid) -> bool:
    if not isinstance(rid, str) or ":" not in rid:
        hub.problem(INVALID, rel, str(rid), "id", "must be <kind>:<slug>")
        return False
    prefix, slug = rid.split(":", 1)
    ok = True
    if prefix != kind:
        hub.problem(INVALID, rel, rid, "id", f"kind prefix {prefix!r} does not match folder data/{kind}/")
        ok = False
    if not SLUG_RE.match(slug):
        hub.problem(INVALID, rel, rid, "id", f"slug {slug!r} does not match {SLUG_RE.pattern}")
        ok = False
    elif "//" in slug or slug.endswith("/") or "__" in slug:
        hub.problem(INVALID, rel, rid, "id", "slug must not contain //, __ or end with /")
        ok = False
    return ok


def _load_records(hub: Hub) -> None:
    kinds = hub.config["kinds"]
    schema = hub.schemas["record"]
    known_kinds = schema_enum(schema, "kind")
    for k in kinds:
        if k not in known_kinds:
            raise HubError(f"hub.config.json kind {k!r} is not in record.schema.json kind enum")
    paths = {}
    for kind, f in iter_data_files(hub.root, kinds):
        rel = f.relative_to(hub.root).as_posix()
        try:
            obj = read_json(f)
        except ValueError as e:
            hub.problem(INVALID, rel, "", "", f"not valid JSON: {e}")
            continue
        wp = _wrapper_problems(obj, rel)
        for p in wp:
            hub.problem(INVALID, rel, "", "", p)
        if wp and not (isinstance(obj, dict) and isinstance(obj.get("records"), list)):
            continue
        for i, rec in enumerate(obj["records"]):
            rid = rec.get("id") if isinstance(rec, dict) else None
            label = rid if isinstance(rid, str) else f"records[{i}]"
            for field, msg in validate(rec, schema):
                hub.problem(INVALID, rel, label, field, msg)
            if not isinstance(rec, dict):
                continue
            if rec.get("kind") is not None and rec.get("kind") != kind:
                hub.problem(INVALID, rel, label, "kind", f"{rec.get('kind')!r} in folder data/{kind}/")
            if not _check_id(hub, rel, kind, rid):
                continue
            _check_dates(hub, rel, rid, rec)
            if rid in hub.records:
                hub.problem(INVALID, rel, rid, "id", f"duplicate id, first in {hub.record_file[rid]}")
                continue
            pp = page_path(rid)
            if pp in paths:
                hub.problem(INVALID, rel, rid, "id", f"page path {pp} collides with {paths[pp]}")
                continue
            paths[pp] = rid
            hub.records[rid] = rec
            hub.record_file[rid] = rel
    hub.records = dict(sorted(hub.records.items()))


def _check_references(hub: Hub) -> None:
    concept_ids = {c["id"] for c in hub.concepts}
    for rid, rec in hub.records.items():
        rel = hub.record_file[rid]
        for i, c in enumerate(rec.get("concepts") or []):
            if c not in concept_ids:
                hub.problem(BAD_CONCEPT, rel, rid, f"concepts[{i}]", f"unknown concept {c}")
        for i, r in enumerate(rec.get("related") or []):
            if isinstance(r, dict) and isinstance(r.get("id"), str) and r["id"] not in hub.records:
                hub.problem(DANGLING, rel, rid, f"related[{i}].id", f"no record {r['id']}")
        sup = rec.get("superseded_by")
        if isinstance(sup, str) and sup not in hub.records:
            hub.problem(DANGLING, rel, rid, "superseded_by", f"no record {sup}")
        for i, s in enumerate(rec.get("stages") or []):
            if isinstance(s, dict) and isinstance(s.get("record_id"), str) and s["record_id"] not in hub.records:
                hub.problem(DANGLING, rel, rid, f"stages[{i}].record_id", f"no record {s['record_id']}")


def _load_observed(hub: Hub) -> None:
    path = hub.root / "data" / "observed.json"
    if not path.exists():
        return
    try:
        obj = read_json(path)
    except ValueError as e:
        hub.problem(INVALID, "data/observed.json", "", "", f"not valid JSON: {e}")
        return
    if not isinstance(obj, dict):
        hub.problem(INVALID, "data/observed.json", "", "", "must be an object keyed by record id")
        return
    hub.observed = {k: v for k, v in obj.items() if isinstance(v, dict)}


def _check_page_concepts(hub: Hub, rel: str, pid: str, concepts) -> None:
    ids = {c["id"] for c in hub.concepts}
    for i, c in enumerate(concepts if isinstance(concepts, list) else []):
        if c not in ids:
            hub.problem(BAD_CONCEPT, rel, pid, f"concepts[{i}]", f"unknown concept {c}")


def _load_pages(hub: Hub) -> None:
    """docs/**/*.md except the pages the build generates."""
    seen = {}
    docs = hub.root / "docs"
    files = sorted(docs.rglob("*.md")) if docs.exists() else []
    for f in files:
        rel = f.relative_to(hub.root).as_posix()
        if rel in GENERATED_DOCS or SKIP_DIRS & set(f.relative_to(hub.root).parts):
            continue
        fm, body, probs = parse_frontmatter(f.read_text(encoding="utf-8"))
        for p in probs:
            hub.problem(INVALID, rel, "", "", p)
        if fm is None:
            hub.problem(INVALID, rel, "", "", "missing frontmatter")
            continue
        pid = fm.get("id", "") if isinstance(fm.get("id"), str) else ""
        for field, msg in validate(fm, hub.schemas["page"]):
            hub.problem(INVALID, rel, pid, field, msg)
        if isinstance(fm.get("last_reviewed"), str):
            try:
                parse_date(fm["last_reviewed"])
            except ValueError:
                hub.problem(INVALID, rel, pid, "last_reviewed", "not a calendar date")
        if pid in seen:
            hub.problem(INVALID, rel, pid, "id", f"duplicate page id, first in {seen[pid]}")
        seen[pid] = rel
        _check_page_concepts(hub, rel, pid, fm.get("concepts"))
        hub.pages.append({"path": rel, "frontmatter": fm, "body": body})


def _load_examples(hub: Hub) -> None:
    ex_dir = hub.root / "examples"
    if not ex_dir.exists():
        return
    for d in sorted(p for p in ex_dir.iterdir() if p.is_dir()):
        readme, meta_path = d / "README.md", d / "example.json"
        rel_meta = meta_path.relative_to(hub.root).as_posix()
        meta = {}
        if meta_path.exists():
            try:
                meta = read_json(meta_path)
            except ValueError as e:
                hub.problem(INVALID, rel_meta, "", "", f"not valid JSON: {e}")
                meta = {}
            for field, msg in validate(meta, hub.schemas["example"]):
                hub.problem(INVALID, rel_meta, f"example:{d.name}", field, msg)
            if isinstance(meta, dict):
                _check_page_concepts(hub, rel_meta, f"example:{d.name}", meta.get("concepts"))
        elif readme.exists():
            hub.warnings.append(f"examples/{d.name}/ has a README.md but no example.json")
        if readme.exists():
            hub.examples.append({"name": d.name, "path": readme.relative_to(hub.root).as_posix(),
                                 "meta": meta if isinstance(meta, dict) else {},
                                 "body": readme.read_text(encoding="utf-8")})
