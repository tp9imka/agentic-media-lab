#!/usr/bin/env python3
"""Validate data/ and write every generated file: index/, catalog/, graph/, INDEX.md, llms.txt,
docs/SCHEMA.md, docs/glossary.md, reports/build.md. Stdlib only.

Exit 0 when built, 1 on validation errors (nothing is written), 2 on unusable config or schema."""
from __future__ import annotations

import json
import posixpath
import shutil
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hublib as h  # noqa: E402

CHARS_PER_TOKEN = 4
WHY_CHARS = 140  # one-line why in tables and llms.txt notes
GLOSSARY_RECORD_LINKS = 10  # record links per concept in the glossary before "and N more"
NESTED_LLMS = "catalog/llms.txt"  # cards move here when llms.txt passes page_char_budget


# ---------------------------------------------------------------- small helpers

def one_line(s) -> str:
    return " ".join(str(s or "").split())


def short(s, n: int = WHY_CHARS) -> str:
    s = one_line(s)
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(" ", 1)[0]
    return cut + " ..."


def cell(s) -> str:
    return one_line(s).replace("|", "\\|") or "-"


def prose(s: str) -> str:
    """Escape < so placeholders like <kind> survive markdown rendering."""
    return s.replace("<", "&lt;")


def rel_link(target: str, from_file: str) -> str:
    anchor = ""
    if "#" in target:
        target, anchor = target.split("#", 1)
        anchor = "#" + anchor
    return posixpath.relpath(target, posixpath.dirname(from_file) or ".") + anchor


def value_text(v) -> str:
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) or "-"
    if isinstance(v, (dict, bool)) or v is None:
        return json.dumps(v, ensure_ascii=False, sort_keys=True)
    return str(v)


def kind_heading(kind: str) -> str:
    return kind.capitalize() + "s"


def frontmatter(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            lines.append(f"{k}: [{', '.join(v)}]")
        else:
            lines.append(f'{k}: "{v}"' if ":" in str(v) or "#" in str(v) else f"{k}: {v}")
    return "\n".join(lines + ["---", ""])


# ---------------------------------------------------------------- build

class Build:
    def __init__(self, hub: h.Hub, built: date):
        self.hub = hub
        self.root = hub.root
        self.cfg = hub.config
        self.built = built
        self.base = self.cfg["base_url"]
        self.footer = f"Index of all pages: {self.base}llms.txt"
        self.recs = hub.records
        self.concept_by_id = {c["id"]: c for c in hub.concepts}
        self.members = defaultdict(list)
        for rid, rec in self.recs.items():
            for c in rec.get("concepts") or []:
                self.members[c].append(rid)
        self.back = defaultdict(set)
        for rid, rec in self.recs.items():
            for r in rec.get("related") or []:
                self.back[r["id"]].add((rid, r["rel"]))
            for s in rec.get("stages") or []:
                self.back[s["record_id"]].add((rid, f"stage {s['stage']}"))
            if rec.get("superseded_by"):
                self.back[rec["superseded_by"]].add((rid, "superseded_by"))
        ratio = self.cfg["popularity_disagreement_ratio"]
        self.extra = {}
        for rid, rec in self.recs.items():
            obs = hub.observed.get(rid, {})
            self.extra[rid] = {
                "path": h.page_path(rid),
                "observed": obs,
                "badge": h.derive_badge(rec, self.cfg["measured_rungs"]),
                "concept_labels": [self.concept_by_id[c]["label"] for c in rec.get("concepts") or []
                                   if c in self.concept_by_id],
                "stale": h.parse_date(rec["checked"]["next_due"]) < built,
                "popularity_flag": h.popularity_flag(obs, ratio),
            }
        self.md = {}  # rel path => text of every readable markdown page, for the hub size

    # ------------------------------------------------ links

    def rec_link(self, rid: str, from_file: str) -> str:
        rec = self.recs.get(rid)
        title = rec["title"] if rec else rid
        return f"[{title}]({rel_link(h.page_path(rid), from_file)})"

    def concept_link(self, cid: str, from_file: str) -> str:
        c = self.concept_by_id.get(cid)
        label = c["label"] if c else cid
        return f"[{label}]({rel_link('docs/glossary.md#' + h.concept_anchor(cid), from_file)})"

    def emit(self, rel: str, text: str, readable: bool = True) -> None:
        h.write_text(self.root, rel, text)
        if readable:
            self.md[rel] = text

    # ------------------------------------------------ record pages

    def record_page(self, rid: str) -> str:
        rec, ex = self.recs[rid], self.extra[rid]
        here = ex["path"]
        badge = ex["badge"]
        chk = rec["checked"]
        title = rec["title"] + (f" ({h.inactive_label(rec)})" if h.is_inactive(rec) else "")
        head = f"`{rid}` - {rec['kind']}" + (f" - <{rec['url']}>" if rec.get("url") else "")
        lines = [f"# {title}", "", head, ""]
        if h.is_inactive(rec):
            lines += [f"**Marked {h.inactive_label(rec)}.** {one_line(rec.get('status_note'))}".rstrip(), ""]
        lines += [one_line(rec["summary"]), ""]
        concepts = ", ".join(self.concept_link(c, here) for c in rec.get("concepts") or []) or "none"
        lines += [f"Concepts: {concepts}", ""]
        if rec.get("aliases"):
            lines += [f"Also known as: {', '.join(rec['aliases'])}", ""]
        if rec.get("tags"):
            lines += [f"Tags: {', '.join(rec['tags'])}", ""]
        reasons = "; ".join(badge["reasons"])
        lines += [f"**Badge:** {badge['label']} (`{badge['tier']}`){': ' + reasons if reasons else ''}.", ""]
        lines += [f"**Why:** {one_line(rec['why_it_matters'])}", ""]
        due = chk["next_due"] + (" (overdue at build date)" if ex["stale"] else "")
        lines += [f"**Last checked:** {chk['date']}, {chk['depth']}, by {chk['by']}. Next check due {due}.", ""]

        lines += ["## Fit notes", "",
                  f"Fit: {rec['fit']}. Level: {rec['level']}. Maturity: {rec.get('maturity', '-')}.", ""]
        facts = [f for f in h.kind_required(self.hub.schemas["record"]).get(rec["kind"], [])
                 if f not in ("url", "maturity", "stages")]
        if facts:
            lines += ["| field | value |", "|---|---|"] + [f"| {f} | {cell(value_text(rec.get(f)))} |" for f in facts]
            lines.append("")
        lines += [one_line(rec["fit_notes"]), ""]
        if rec.get("stages"):
            lines += ["Stages:", ""]
            for n, s in enumerate(rec["stages"], 1):
                note = f" - {one_line(s['note'])}" if s.get("note") else ""
                lines.append(f"{n}. {s['stage']}: {self.rec_link(s['record_id'], here)}{note}")
            lines.append("")

        lines += ["## Claims", ""]
        if not rec["claims"]:
            lines += ["No claims recorded.", ""]
        for n, c in enumerate(rec["claims"], 1):
            via = f" Via: {one_line(c['via'])}." if c.get("via") else ""
            lines += [f"{n}. {one_line(c['text'])}", "", f"   > {one_line(c['quote'])}", "",
                      f"   Locator: {one_line(c['locator'])}. Source: <{c['url']}>, retrieved {c['retrieved']}.{via}", ""]

        obs = ex["observed"]
        licence = rec.get("licence_override") or obs.get("licence") or "unknown"
        if rec.get("licence_override") and rec.get("licence_reason"):
            licence += f" (override: {one_line(rec['licence_reason'])})"
        lines += ["## Provenance", "",
                  f"- Source type: {rec['source_type']}",
                  f"- Corroboration: {rec['corroboration']}",
                  f"- Checked: {chk['date']} by {chk['by']}, depth {chk['depth']}"
                  + (f". {one_line(chk['what'])}" if chk.get("what") else ""),
                  f"- Next check due: {chk['next_due']}",
                  f"- Licence: {licence}",
                  f"- URL status: {rec['url_status']}"]
        if chk.get("source_sha256"):
            lines.append(f"- Saved source sha256: `{chk['source_sha256']}`")
        if rec.get("archive_url"):
            lines.append(f"- Archive copy: <{rec['archive_url']}>")
        if rec.get("measured"):
            m = rec["measured"]
            lines.append(f"- Measured by us: rung {m['rung']}, command `{one_line(m['command'])}`, "
                         f"input {one_line(m['input'])}, commit `{m['commit']}`"
                         + (f", result {one_line(m['result'])}" if m.get("result") else ""))
        if rec.get("downgrade"):
            d = rec["downgrade"]
            lines.append(f"- Badge downgraded: {d['reason']}" + (f" - {one_line(d['note'])}" if d.get("note") else ""))
        if rec.get("citation"):
            lines.append("- Citation: " + "; ".join(f"{k} {value_text(v)}" for k, v in rec["citation"].items()))
        if rec.get("lane"):
            lines.append(f"- Lane: {rec['lane']}")
        lines.append("")

        lines += ["## Observed", ""]
        if obs:
            lines += ["Collected by `tools/enrich.py`, not typed by hand.", ""]
            lines += [f"- {k}: {value_text(obs[k])}" for k in sorted(obs)]
            if ex["popularity_flag"]:
                lines.append(f"- Popularity: installs and stars differ by more than "
                             f"{self.cfg['popularity_disagreement_ratio']}x")
        else:
            lines.append("Nothing collected yet.")
        lines.append("")

        lines += ["## Related", ""]
        rel = rec.get("related") or []
        lines += [f"- {r['rel']}: {self.rec_link(r['id'], here)}" + (f" - {one_line(r['note'])}" if r.get("note") else "")
                  for r in rel] or ["None."]
        lines += ["", "## Referenced by", ""]
        lines += [f"- {self.rec_link(src, here)} ({why})" for src, why in sorted(self.back.get(rid, ()))] or ["None."]
        lines += ["", "## Status", "", f"Status: {rec['status']}."]
        if rec.get("status_note"):
            lines.append(f"Note: {one_line(rec['status_note'])}")
        if rec.get("superseded_by"):
            lines.append(f"Superseded by {self.rec_link(rec['superseded_by'], here)}.")
        lines += ["", self.footer]
        return "\n".join(lines) + "\n"

    def write_catalog(self) -> None:
        cat = self.root / "catalog"
        if cat.exists():
            shutil.rmtree(cat)
        for rid in self.recs:
            self.emit(self.extra[rid]["path"], self.record_page(rid))
        here = "catalog/README.md"
        lines = ["# Catalog", "", "Every record, by kind. Generated by `tools/build.py` from `data/`.", "",
                 "Counts: " + ", ".join(f"{k} {self.count(k)}" for k in self.cfg["kinds"]) + ".", ""]
        active = [r for r in self.recs if not h.is_inactive(self.recs[r])]
        inactive = [r for r in self.recs if h.is_inactive(self.recs[r])]
        for kind in self.cfg["kinds"]:
            ids = [r for r in active if self.recs[r]["kind"] == kind]
            lines += [f"## {kind_heading(kind)} ({len(ids)})", ""]
            if not ids:
                lines += ["None yet.", ""]
                continue
            lines += ["| Record | Fit | Badge | Why |", "|---|---|---|---|"]
            for r in ids:
                lines.append(f"| {self.rec_link(r, here)} | {self.recs[r]['fit']} | {self.extra[r]['badge']['tier']} | "
                             f"{cell(short(self.recs[r]['why_it_matters']))} |")
            lines.append("")
        lines += [f"## Archived, retracted and shut down ({len(inactive)})", ""]
        if inactive:
            lines += ["| Record | Kind | Marked | Note |", "|---|---|---|---|"]
            for r in inactive:
                rec = self.recs[r]
                lines.append(f"| {self.rec_link(r, here)} | {rec['kind']} | {h.inactive_label(rec)} | "
                             f"{cell(short(rec.get('status_note')))} |")
        else:
            lines.append("None.")
        lines += ["", self.footer]
        self.emit(here, "\n".join(lines) + "\n")

    def count(self, kind: str) -> int:
        return sum(1 for r in self.recs.values() if r["kind"] == kind)

    # ------------------------------------------------ generated docs

    def schema_rows(self, schema: dict, prefix: str = "") -> list[str]:
        rows, req = [], set(schema.get("required", []))
        for name, sub in schema.get("properties", {}).items():
            path = prefix + name
            types = sub.get("type", "")
            typ = " or ".join(types) if isinstance(types, list) else types
            target = sub
            if typ == "array" and "items" in sub:
                target = sub["items"]
                typ = f"array of {target.get('type', 'any')}"
            allowed = ", ".join(map(str, target.get("enum", []))) or (
                f"`{target['pattern']}`" if "pattern" in target else "")
            rows.append(f"| `{path}` | {typ} | {'yes' if name in req else ''} | {cell(allowed)} | "
                        f"{prose(cell(sub.get('description', '')))} |")
            if target.get("properties"):
                rows += self.schema_rows(target, path + ("[]." if target is not sub else "."))
        return rows

    def write_schema_doc(self) -> str:
        sch = self.hub.schemas
        fm = {"id": "guide:schema", "title": "Data schema", "summary": "Every field, enum and rule of the hub's data, "
              "generated from data/schema.", "use_when": "Use this page when you need the exact record fields, "
              "allowed values, id rules or how the evidence badge is derived.", "concepts": [],
              "last_reviewed": self.built.isoformat()}
        lines = [frontmatter(fm), "# Data schema", "",
                 "Reference for anyone who writes or reads records. Generated by `tools/build.py` from "
                 "`data/schema/*.schema.json`, which is normative. Edit the schema files, not this page.", "",
                 "## Contents", "", "- [Data files](#data-files)", "- [Ids and page paths](#ids-and-page-paths)"]
        lines += [f"- [{sch[n].get('title', n)}](#{h.gh_slug(sch[n].get('title', n))})" for n in h.SCHEMA_FILES]
        lines += ["- [Kind-specific fields](#kind-specific-fields)", "- [Evidence badge](#evidence-badge)", "",
                  "## Data files", "",
                  f"Each `data/<kind>/<lane>.json` and `data/concepts.json` is "
                  f"`{{\"schema_version\": {h.SCHEMA_VERSION}, \"lane\": \"<lane>\", \"records\": [...]}}`. "
                  "`data/observed.json` is keyed by record id and written only by `tools/enrich.py`.", "",
                  "## Ids and page paths", "",
                  f"An id is `<kind>:<slug>`. The slug matches `{h.SLUG_RE.pattern}` and has no `//`, no `__` "
                  "and no trailing `/`. The page path replaces `/` in the slug with `__`: "
                  "`tool:remotion-dev/remotion` => `catalog/tool/remotion-dev__remotion.md`.", ""]
        for n in h.SCHEMA_FILES:
            s = sch[n]
            lines += [f"## {s.get('title', n)}", "", f"File: `data/schema/{n}.schema.json`. {prose(s.get('description', ''))}", "",
                      "| Field | Type | Required | Allowed | Notes |", "|---|---|---|---|---|"]
            lines += self.schema_rows(s) + [""]
        lines += ["## Kind-specific fields", "", "Required on top of the shared fields, per `kind`:", "",
                  "| Kind | Also required |", "|---|---|"]
        for kind, fields in h.kind_required(sch["record"]).items():
            lines.append(f"| {kind} | {', '.join(f'`{f}`' for f in fields)} |")
        lines += ["", "A record is marked inactive when `status` is archived or retracted, or `maturity` or "
                  "`access` is shut-down. It keeps its page and is listed separately in the catalog.", "",
                  "## Evidence badge", "",
                  "One badge per record, derived in this order; the first row that applies wins.", "",
                  "| Tier | Label | When |", "|---|---|---|"]
        lines += [f"| `{t}` | {h.TIER_LABELS[t]} | {cell(rule)} |" for t, rule in h.BADGE_TABLE]
        lines += ["", "A `downgrade` with a named reason (" + ", ".join(
                  h.schema_enum(sch["record"], "downgrade.reason")) + ") moves the badge one tier down. "
                  "A dead or moved link adds a reason and keeps the tier.", "", self.footer]
        text = "\n".join(lines) + "\n"
        self.emit("docs/SCHEMA.md", text)
        return text

    def write_glossary(self) -> str:
        here = "docs/glossary.md"
        fm = {"id": "guide:glossary", "title": "Glossary", "summary": "Every concept of the hub vocabulary with "
              "its labels, scope and records.", "use_when": "Use this page when a term in the hub is unclear or "
              "you need a concept id.", "concepts": [], "last_reviewed": self.built.isoformat()}
        lines = [frontmatter(fm), "# Glossary", "",
                 f"The hub vocabulary, {len(self.hub.concepts)} concepts. Generated by `tools/build.py` from "
                 "`data/concepts.json`. Each concept id is stable; the label may change.", ""]
        if not self.hub.concepts:
            lines += ["The vocabulary is empty: `data/concepts.json` is missing or has no records.", ""]
        else:
            lines += ["## Contents", ""] + [f"- [{c['label']}](#{h.concept_anchor(c['id'])})" for c in self.hub.concepts]
            lines.append("")
        for c in self.hub.concepts:
            cid = c["id"]
            lines += [f'## <a id="{h.concept_anchor(cid)}"></a>{c["label"]}', "", f"`{cid}`", ""]
            if c.get("alt_labels"):
                lines += [f"Also called: {', '.join(c['alt_labels'])}", ""]
            if c.get("scope_note"):
                lines += [f"Scope: {one_line(c['scope_note'])}", ""]
            for field, name in (("broader", "Broader"), ("related", "Related")):
                if c.get(field):
                    lines += [f"{name}: " + ", ".join(self.concept_link(x, here) for x in c[field]), ""]
            if c.get("same_as"):
                lines += [f"Same as: <{c['same_as']}>", ""]
            ids = self.members.get(cid, [])
            shown = ", ".join(self.rec_link(r, here) for r in ids[:GLOSSARY_RECORD_LINKS])
            more = f", and {len(ids) - GLOSSARY_RECORD_LINKS} more in the [catalog](../catalog/README.md)" \
                if len(ids) > GLOSSARY_RECORD_LINKS else ""
            lines += [f"Records ({len(ids)}): {shown or 'none yet'}{more}", ""]
        lines.append(self.footer)
        text = "\n".join(lines) + "\n"
        self.emit(here, text)
        return text

    # ------------------------------------------------ index files

    def page_entries(self, generated: dict) -> list[dict]:
        """(path, page_id, title, concepts, last_reviewed, use_when, body) for docs and example READMEs."""
        out = []
        docs = [(p["path"], p["frontmatter"], p["body"]) for p in self.hub.pages]
        for rel, text in generated.items():
            fm, body, _ = h.parse_frontmatter(text)
            docs.append((rel, fm, body))
        for rel, fm, body in docs:
            out.append({"path": rel, "page_id": fm.get("id"), "title": fm.get("title") or first_title(body, rel),
                        "concepts": fm.get("concepts") or [], "last_reviewed": fm.get("last_reviewed"),
                        "use_when": fm.get("use_when", ""), "body": body})
        for ex in self.hub.examples:
            meta = ex["meta"]
            title = meta.get("title") or first_title(ex["body"], ex["path"])
            note = meta.get("summary") or meta.get("key_result") or ""
            out.append({"path": ex["path"], "page_id": f"example:{ex['name']}", "title": title,
                        "concepts": meta.get("concepts") or [], "last_reviewed": None,
                        "use_when": note, "body": ex["body"], "status": meta.get("status")})
        out.sort(key=lambda p: p["path"])
        for p in out:
            self.md[p["path"]] = p["body"]
        return out

    def write_index_files(self, pages: list[dict]) -> dict:
        lines = []
        for p in pages:
            for ch in h.chunks(p["body"]):
                lines.append(json.dumps({"page_id": p["page_id"], "title": p["title"], "path": p["path"],
                                         "anchor": ch["anchor"], "heading_path": ch["heading_path"],
                                         "concepts": p["concepts"], "text": ch["text"],
                                         "last_reviewed": p["last_reviewed"]}, ensure_ascii=False))
        h.write_text(self.root, "index/pages.jsonl", "".join(x + "\n" for x in lines))

        recs = [json.dumps({**rec, **self.extra[rid]}, ensure_ascii=False) for rid, rec in self.recs.items()]
        h.write_text(self.root, "index/records.jsonl", "".join(x + "\n" for x in recs))

        concepts = [{**c, "record_ids": self.members.get(c["id"], []), "count": len(self.members.get(c["id"], []))}
                    for c in self.hub.concepts]
        h.write_text(self.root, "index/concepts.json", json.dumps(
            {"schema_version": h.SCHEMA_VERSION, "lane": self.hub.concepts_lane, "records": concepts},
            ensure_ascii=False, indent=1) + "\n")

        chars = sum(len(t) for t in self.md.values())
        primary = sum(1 for r in self.recs.values() if r["checked"]["depth"] == "primary-read")
        meta = {"built": self.built.isoformat(),
                "counts": {k: self.count(k) for k in self.cfg["kinds"]},
                "primary_read_share": round(primary / len(self.recs), 3) if self.recs else 0.0,
                "chars_total": chars,
                "tokens_estimate": chars // CHARS_PER_TOKEN,
                "lifetime": self.cfg["lifetime"]}
        h.write_text(self.root, "index/meta.json", json.dumps(meta, indent=1) + "\n")
        return meta

    def write_graph(self) -> None:
        nodes = [{"id": rid, "kind": r["kind"], "label": r["title"], "path": self.extra[rid]["path"],
                  "status": r["status"], "inactive": h.is_inactive(r), "badge": self.extra[rid]["badge"]["tier"],
                  "concepts": r.get("concepts") or []} for rid, r in self.recs.items()]
        nodes += [{"id": c["id"], "kind": "concept", "label": c["label"],
                   "path": "docs/glossary.md#" + h.concept_anchor(c["id"])} for c in self.hub.concepts]
        edges = []
        for rid, r in self.recs.items():
            edges += [{"source": rid, "target": x["id"], "rel": x["rel"]} for x in r.get("related") or []]
            edges += [{"source": rid, "target": c, "rel": "about"} for c in r.get("concepts") or []]
        edges.sort(key=lambda e: (e["source"], e["target"], e["rel"]))
        h.write_text(self.root, "graph/graph.json", json.dumps({"nodes": nodes, "edges": edges},
                                                               ensure_ascii=False, indent=1) + "\n")

    def size_line(self, meta: dict) -> str:
        return (f"Hub size: {meta['chars_total']} characters, about {meta['tokens_estimate']} tokens "
                f"(estimate, characters / {CHARS_PER_TOKEN}).")

    def write_index_md(self, meta: dict, pages: list[dict]) -> None:
        here = "INDEX.md"
        children = defaultdict(list)
        ids = set(self.concept_by_id)
        for c in self.hub.concepts:
            for p in c.get("broader") or []:
                if p in ids:
                    children[p].append(c["id"])
        roots = [c["id"] for c in self.hub.concepts if not [p for p in c.get("broader") or [] if p in ids]]

        def subtree(cid, seen):
            found = set(self.members.get(cid, []))
            for k in children.get(cid, []):
                if k not in seen:
                    found |= subtree(k, seen | {k})
            return found

        lines = [f"# {self.cfg['title']} - index", "", one_line(self.cfg.get("tagline")), "",
                 "Generated by `tools/build.py`.", "",
                 "Records: " + ", ".join(f"{k} {meta['counts'][k]}" for k in self.cfg["kinds"])
                 + f". Concepts: {len(self.hub.concepts)}. Pages: {len(pages)}.", "",
                 self.size_line(meta), "",
                 "Start from the [catalog](catalog/README.md), the [glossary](docs/glossary.md), the "
                 "[schema](docs/SCHEMA.md) or [llms.txt](llms.txt).", "", "## Concept tree", ""]

        def emit(cid, depth, seen):
            direct, total = len(self.members.get(cid, [])), len(subtree(cid, seen))
            extra = f", {total} with narrower concepts" if total != direct else ""
            noun = "record" if direct == 1 else "records"
            lines.append(f"{'  ' * depth}- {self.concept_link(cid, here)} - {direct} {noun}{extra}")
            for k in children.get(cid, []):
                if k not in seen:
                    emit(k, depth + 1, seen | {k})

        for r in roots:
            emit(r, 0, {r})
        if not self.hub.concepts:
            lines.append("The vocabulary is empty: `data/concepts.json` is missing or has no records.")
        lines += ["", self.footer]
        self.emit(here, "\n".join(lines) + "\n", readable=False)

    def card_line(self, rid: str) -> str:
        rec = self.recs[rid]
        mark = f" ({h.inactive_label(rec)})" if h.is_inactive(rec) else ""
        return f"- [{rec['title']}]({self.base}{self.extra[rid]['path']}): {rec['kind']}{mark}, " \
               f"{self.extra[rid]['badge']['tier']}. {short(rec['why_it_matters'])}"

    def write_llms(self, meta: dict, pages: list[dict]) -> None:
        b = self.base
        counts = ", ".join(f"{meta['counts'][k]} {k}" for k in self.cfg["kinds"])
        lines = [f"# {self.cfg['title']}", "",
                 f"> {one_line(self.cfg.get('tagline'))} Records: {len(self.recs)} ({counts}). "
                 f"Concepts: {len(self.hub.concepts)}. Pages: {len(pages)}. "
                 f"Size: about {meta['tokens_estimate']} tokens (estimate, characters / {CHARS_PER_TOKEN}).", "",
                 "## Entry points", "",
                 f"- [Index]({b}INDEX.md): concept tree with counts and the hub size",
                 f"- [Catalog]({b}catalog/README.md): every record by kind, inactive records listed separately"]
        for p in pages:
            if p["path"] in h.GENERATED_DOCS:
                lines.append(f"- [{p['title']}]({b}{p['path']}): {one_line(p['use_when'])}")
        lines.append(f"- [All records as JSON lines]({b}index/records.jsonl): the full machine dump")
        for name, note in (("README.md", "what the hub is"), ("AGENTS.md", "how agents query and extend the hub")):
            if (self.root / name).exists():
                lines.append(f"- [{name}]({b}{name}): {note}")
        guides = [p for p in pages if p["path"].startswith("docs/") and p["path"] not in h.GENERATED_DOCS]
        examples = [p for p in pages if p["path"].startswith("examples/")]
        if guides:
            lines += ["", "## Guides", ""] + [f"- [{p['title']}]({b}{p['path']}): {one_line(p['use_when'])}"
                                              for p in guides]
        if examples:
            lines += ["", "## Examples", ""]
            for p in examples:
                status = f" ({p['status']})" if p.get("status") else ""
                lines.append(f"- [{p['title']}]({b}{p['path']}){status}: {short(p['use_when'])}".rstrip(": "))
        top = [r for r in self.recs if self.recs[r]["fit"] == "high" and not h.is_inactive(self.recs[r])]
        rest = [r for r in self.recs if r not in set(top)]
        cards = []
        if top:
            cards += ["", "## Records", ""] + [self.card_line(r) for r in top]
        optional = [self.card_line(r) for r in rest]
        text = "\n".join(lines + cards + (["", "## Optional", ""] + optional if optional else [])) + "\n"
        nested = self.root / NESTED_LLMS
        if len(text) > self.cfg["page_char_budget"] and self.recs:
            sub = [f"# {self.cfg['title']} - records", "",
                   f"> Every record card. Linked from {b}llms.txt because the cards did not fit there.", ""]
            sub += cards[1:] + (["", "## Optional", ""] + optional if optional else [])
            self.emit(NESTED_LLMS, "\n".join(sub) + "\n", readable=False)
            text = "\n".join(lines + ["", "## Optional", "",
                                      f"- [All record cards]({b}{NESTED_LLMS}): one line per record"]) + "\n"
        elif nested.exists():
            nested.unlink()
        self.emit("llms.txt", text, readable=False)

    def write_report(self, meta: dict) -> None:
        tags = Counter(t for r in self.recs.values() for t in r.get("tags") or [])
        stale = [r for r in self.recs if self.extra[r]["stale"]]
        flags = [r for r in self.recs if self.extra[r]["popularity_flag"]]
        unseen = [r for r in self.recs if self.recs[r]["checked"]["depth"] == "not-checked"]
        lines = ["# Build report", "", f"Built {meta['built']} by `tools/build.py`.", "", "## Counts", ""]
        lines += [f"- {k}: {meta['counts'][k]}" for k in self.cfg["kinds"]]
        lines += [f"- concepts: {len(self.hub.concepts)}", f"- primary-read share: {meta['primary_read_share']}",
                  f"- {self.size_line(meta)}", "",
                  "## Validation", "", "dangling: 0 bad concepts: 0 invalid: 0", ""]
        lines += [f"- warning: {w}" for w in self.hub.warnings] + ([""] if self.hub.warnings else [])

        def section(title, items):
            nonlocal lines
            lines += [f"## {title} ({len(items)})", ""] + (items or ["None."]) + [""]

        section("Stale records (next check due before the build date)",
                [f"- `{r}`: due {self.recs[r]['checked']['next_due']}" for r in stale])
        section("Tags used once", [f"- `{t}`" for t, n in sorted(tags.items()) if n == 1])
        section("Popularity disagreements",
                [f"- `{r}`: stars {self.extra[r]['observed'].get('stars')}, installs "
                 f"{self.extra[r]['observed'].get('installs')}" for r in flags])
        section("Seen, not reviewed (checked.depth not-checked)", [f"- `{r}`" for r in unseen])
        lines.append(self.footer)
        self.emit("reports/build.md", "\n".join(lines) + "\n", readable=False)

    def run(self) -> None:
        self.write_catalog()
        generated = {"docs/SCHEMA.md": self.write_schema_doc(), "docs/glossary.md": self.write_glossary()}
        pages = self.page_entries(generated)
        meta = self.write_index_files(pages)
        self.write_graph()
        self.write_index_md(meta, pages)
        self.write_llms(meta, pages)
        self.write_report(meta)


def first_title(body: str, rel: str) -> str:
    fallback = Path(rel).parent.name if rel.endswith("README.md") else Path(rel).stem
    return h.first_heading(body) or fallback


def main(argv=None) -> int:
    root, _ = h.root_from_args("Validate data/ and write all generated files.", argv)
    try:
        built = h.build_date()
        hub = h.load_hub(root)
    except h.HubError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    for w in hub.warnings:
        print(f"warning: {w}", file=sys.stderr)
    for _, msg in hub.problems:
        print(f"error: {msg}", file=sys.stderr)
    summary = (f"build {built.isoformat()}: {len(hub.records)} records, {len(hub.concepts)} concepts, "
               f"dangling: {hub.count(h.DANGLING)} bad concepts: {hub.count(h.BAD_CONCEPT)} "
               f"invalid: {hub.count(h.INVALID)}")
    if hub.problems:
        print(summary)
        return 1
    Build(hub, built).run()
    print(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
