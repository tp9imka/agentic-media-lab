#!/usr/bin/env python3
"""Collect facts a forge or registry reports (licence, stars, last activity, archived flag,
skill installs, package downloads, model-card licence tag) for every record and write them to
data/observed.json. The only networked command of the hub and the only writer of that file.
Never part of the gate. Prints `enriched: N unchanged: N failed: N skipped: N`.
Exit 0 ok, 1 when a lookup failed or the GitHub rate limit stopped the run, 2 unusable config."""
from __future__ import annotations

import difflib
import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hublib as h  # noqa: E402

OBSERVED = "data/observed.json"
USER_AGENT = "hub-enrich/1"
DEFAULT_TIMEOUT_S = 20
HOST_DELAY_S = 1.0
MAX_RETRIES = 1
TOP_SKILLS = 10
MAX_BODY_BYTES = 5_000_000
ERROR_CHARS = 200

GITHUB_API = "https://api.github.com/repos/"
SKILLS_API = "https://skills.sh/api/search?q="
HF_API = "https://huggingface.co/api/models/"
NPM_API = "https://api.npmjs.org/downloads/point/last-week/"
PYPI_API = "https://pypistats.org/api/packages/"

GITHUB_URL_RE = re.compile(r"^https?://(?:www\.)?github\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)")
HF_URL_RE = re.compile(r"^https?://(?:www\.)?huggingface\.co/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+)/?$")
TOOL_ID_RE = re.compile(r"^tool:([a-z0-9_.-]+)/([a-z0-9_.-]+)$")
HINT_RE = re.compile(r"^(npm|pypi):(\S+)$")


@dataclass
class Response:
    status: int
    headers: dict
    body: bytes
    url: str


class LookupError_(Exception):
    """One lookup failed; the message is the short error kept in `errors`."""


class RateLimited(Exception):
    pass


def http_get(url: str, headers: dict, timeout: float) -> Response:
    """The only place that touches the network. Default TLS context; HTTP errors are returned,
    transport errors raise OSError."""
    req = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return Response(r.status, {k.lower(): v for k, v in r.headers.items()}, r.read(MAX_BODY_BYTES), r.url)
    except urllib.error.HTTPError as e:
        hdrs = {k.lower(): v for k, v in (e.headers or {}).items()}
        return Response(e.code, hdrs, e.read(MAX_BODY_BYTES) if e.fp else b"", e.url or url)


def _is_timeout(e: OSError) -> bool:
    reason = getattr(e, "reason", e)
    return isinstance(reason, (socket.timeout, TimeoutError))


def short(msg) -> str:
    return " ".join(str(msg).split())[:ERROR_CHARS]


# ---------------------------------------------------------------- lookups from id and url

def github_repo(rec: dict) -> tuple[str, str] | None:
    m = GITHUB_URL_RE.match(rec.get("url") or "")
    if m:
        owner, repo = m.group(1), m.group(2)
        return owner, repo[:-4] if repo.endswith(".git") else repo
    m = TOOL_ID_RE.match(rec.get("id") or "")
    return (m.group(1), m.group(2)) if m else None


def hf_model(rec: dict) -> tuple[str, str] | None:
    m = HF_URL_RE.match(rec.get("url") or "")
    return (m.group(1), m.group(2)) if m else None


def package_hints(rec: dict) -> list[tuple[str, str]]:
    out = []
    for t in rec.get("tags") or []:
        m = HINT_RE.match(t) if isinstance(t, str) else None
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def has_lookup(rec: dict) -> bool:
    return bool(github_repo(rec) or hf_model(rec) or package_hints(rec))


def day(ts) -> str | None:
    return ts[:10] if isinstance(ts, str) and re.match(r"^\d{4}-\d{2}-\d{2}", ts) else None


def spdx(lic) -> str:
    sid = lic.get("spdx_id") if isinstance(lic, dict) else None
    return sid if isinstance(sid, str) and sid and sid != "NOASSERTION" else "unknown"


def put(out: dict, key: str, value) -> None:
    """Only facts that were reported; a missing value stays absent."""
    if value is not None:
        out[key] = value


# ---------------------------------------------------------------- the enricher

@dataclass
class Enricher:
    fetch: object = http_get
    timeout: float = DEFAULT_TIMEOUT_S
    token: str | None = None
    sleep: object = time.sleep
    clock: object = time.monotonic
    last_call: dict = field(default_factory=dict)
    github_exhausted: str | None = None

    def get(self, url: str, sources: list, extra: dict | None = None) -> Response:
        host = urllib.parse.urlsplit(url).hostname or ""
        headers = {"User-Agent": USER_AGENT, "Accept": "application/json", **(extra or {})}
        for attempt in range(MAX_RETRIES + 1):
            wait = self.last_call.get(host, -HOST_DELAY_S) + HOST_DELAY_S - self.clock()
            if wait > 0:
                self.sleep(wait)
            self.last_call[host] = self.clock()
            if attempt == 0:
                sources.append(url)
            try:
                resp = self.fetch(url, headers, self.timeout)
            except OSError as e:
                if _is_timeout(e) and attempt < MAX_RETRIES:
                    continue
                raise LookupError_(f"{host}: {short(getattr(e, 'reason', e))}") from None
            if resp.status >= 500 and attempt < MAX_RETRIES:
                continue
            if resp.url and resp.url != url and resp.url not in sources:
                sources.append(resp.url)
            return resp
        raise AssertionError("unreachable")

    @staticmethod
    def json_of(resp: Response, host: str):
        if resp.status != 200:
            raise LookupError_(f"{host}: HTTP {resp.status}")
        try:
            return json.loads(resp.body.decode("utf-8"))
        except (UnicodeDecodeError, ValueError):
            raise LookupError_(f"{host}: response is not JSON") from None

    def github(self, owner: str, repo: str, out: dict, sources: list) -> None:
        if self.github_exhausted:
            raise RateLimited(self.github_exhausted)
        extra = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
        if self.token:
            extra["Authorization"] = f"Bearer {self.token}"
        resp = self.get(f"{GITHUB_API}{owner}/{repo}", sources, extra)
        if resp.headers.get("x-ratelimit-remaining") == "0":
            reset = resp.headers.get("x-ratelimit-reset", "")
            when = time.strftime("%H:%M UTC", time.gmtime(int(reset))) if reset.isdigit() else "later"
            self.github_exhausted = f"GitHub rate limit reached (resets {when}); set GITHUB_TOKEN or wait"
            if resp.status in (403, 429):
                raise RateLimited(self.github_exhausted)
        data = self.json_of(resp, "api.github.com")
        if not isinstance(data, dict) or not isinstance(data.get("full_name"), str):
            raise LookupError_("api.github.com: no full_name in response")
        put(out, "stars", data.get("stargazers_count"))
        out["licence"] = spdx(data.get("license"))
        put(out, "last_activity", day(data.get("pushed_at")))
        put(out, "archived", data.get("archived"))
        put(out, "created", day(data.get("created_at")))
        put(out, "forks", data.get("forks_count"))
        put(out, "open_issues", data.get("open_issues_count"))
        put(out, "default_branch", data.get("default_branch"))
        if data["full_name"].lower() != f"{owner}/{repo}".lower():
            out["moved_to"] = data["full_name"]

    def skills(self, owner: str, repo: str, out: dict, sources: list) -> None:
        names = {f"{owner}/{repo}".lower()}
        if out.get("moved_to"):
            names.add(out["moved_to"].lower())
        resp = self.get(SKILLS_API + urllib.parse.quote(repo), sources)
        data = self.json_of(resp, "skills.sh")
        entries = data.get("skills") if isinstance(data, dict) else None
        if not isinstance(entries, list):
            raise LookupError_("skills.sh: no skills list in response")
        by_skill = {}
        for e in entries:
            if not isinstance(e, dict) or str(e.get("source", "")).lower() not in names:
                continue
            n = e.get("installs")
            name = e.get("name") or e.get("skillId")
            if h.json_type(n) == "integer" and isinstance(name, str):
                by_skill[name] = max(n, by_skill.get(name, 0))
        if by_skill:
            top = sorted(by_skill.items(), key=lambda kv: (-kv[1], kv[0]))[:TOP_SKILLS]
            out["installs"] = top[0][1]
            out["installs_by_skill"] = dict(top)
            out.setdefault("registry", []).append("skills.sh")

    def huggingface(self, org: str, name: str, out: dict, sources: list) -> None:
        resp = self.get(f"{HF_API}{org}/{name}", sources)
        data = self.json_of(resp, "huggingface.co")
        if not isinstance(data, dict):
            raise LookupError_("huggingface.co: unexpected response")
        tags = [t for t in data.get("tags") or [] if isinstance(t, str)]
        lic = next((t.split(":", 1)[1] for t in tags if t.startswith("license:")), "")
        out["licence"] = lic or "unknown"
        put(out, "last_activity", day(data.get("lastModified")))
        put(out, "created", day(data.get("createdAt")))
        put(out, "hf_downloads", data.get("downloads"))
        put(out, "hf_likes", data.get("likes"))
        put(out, "gated", data.get("gated"))

    def package(self, registry: str, pkg: str, out: dict, sources: list) -> None:
        if registry == "npm":
            data = self.json_of(self.get(NPM_API + urllib.parse.quote(pkg, safe="@/"), sources), "api.npmjs.org")
            n = data.get("downloads") if isinstance(data, dict) else None
        else:
            data = self.json_of(self.get(f"{PYPI_API}{urllib.parse.quote(pkg)}/recent", sources), "pypistats.org")
            n = (data.get("data") or {}).get("last_week") if isinstance(data, dict) else None
        if h.json_type(n) != "integer":
            raise LookupError_(f"{registry}: no weekly downloads in response")
        out["downloads_week"] = max(n, out.get("downloads_week", 0))
        out.setdefault("registry", []).append(registry)

    def lookup(self, rec: dict) -> tuple[dict, list[str], list[str]]:
        """(facts, sources, errors) for one record."""
        out, sources, errors = {}, [], []
        steps = []
        gh = github_repo(rec)
        if gh:
            steps += [(self.github, gh), (self.skills, gh)]
        hf = hf_model(rec)
        if hf:
            steps.append((self.huggingface, hf))
        steps += [(self.package, hint) for hint in package_hints(rec)]
        for fn, args in steps:
            try:
                fn(*args, out, sources)
            except LookupError_ as e:
                errors.append(str(e))
        if "registry" in out:
            out["registry"] = ", ".join(sorted(set(out["registry"])))
        return out, sources, errors


# ---------------------------------------------------------------- run

def dump(obj: dict) -> str:
    return json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n"


def _extra(ap) -> None:
    ap.add_argument("--only", action="append", default=[], metavar="ID", help="only this record id (repeatable)")
    ap.add_argument("--dry-run", action="store_true", help="print the diff, write nothing")
    ap.add_argument("--max-age-days", type=int, default=None, metavar="N",
                    help="skip records fetched less than N days ago")
    ap.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_S, metavar="S", help="seconds per request")


def main(argv=None, fetch=http_get, sleep=time.sleep) -> int:
    root, args = h.root_from_args(__doc__.split("\n")[0], argv, _extra)
    try:
        cfg = h.load_config(root)
        run_date = h.build_date()
    except h.HubError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    path = root / OBSERVED
    old_text = path.read_text(encoding="utf-8") if path.exists() else ""
    try:
        previous = json.loads(old_text) if old_text else {}
    except ValueError as e:
        print(f"error: {OBSERVED}: not valid JSON: {e}", file=sys.stderr)
        return 2
    if not isinstance(previous, dict):
        print(f"error: {OBSERVED}: must be an object keyed by record id", file=sys.stderr)
        return 2

    records = {r["id"]: r for _, r in h.read_records(root, cfg["kinds"]) if isinstance(r.get("id"), str)}
    unknown = [i for i in args.only if i not in records]
    if unknown:
        print(f"error: --only: no record {', '.join(unknown)}", file=sys.stderr)
        return 2
    selected = sorted(args.only and set(args.only) or records)
    observed = {k: v for k, v in previous.items() if k in records}
    en = Enricher(fetch=fetch, timeout=args.timeout, token=os.environ.get("GITHUB_TOKEN") or None, sleep=sleep)
    counts = dict.fromkeys(("enriched", "unchanged", "failed", "skipped"), 0)
    stopped = None
    for rid in selected:
        rec, prev = records[rid], previous.get(rid)
        if stopped or not has_lookup(rec):
            counts["skipped"] += 1
            if not stopped:
                observed.pop(rid, None)
            continue
        if args.max_age_days is not None and isinstance(prev, dict):
            try:
                if run_date - h.parse_date(prev.get("fetched_at", "")) < timedelta(days=args.max_age_days):
                    counts["skipped"] += 1
                    continue
            except ValueError:
                pass
        try:
            facts, sources, errors = en.lookup(rec)
        except RateLimited as e:
            stopped = str(e)
            counts["skipped"] += 1
            continue
        if errors:
            counts["failed"] += 1
            for err in errors:
                print(f"failed: {rid}: {err}")
            if isinstance(prev, dict):
                observed[rid] = {**prev, "errors": errors}
            continue
        entry = {**facts, "sources": sources, "fetched_at": run_date.isoformat()}
        same = isinstance(prev, dict) and {k: v for k, v in prev.items() if k != "fetched_at"} == \
            {k: v for k, v in entry.items() if k != "fetched_at"}
        counts["unchanged" if same else "enriched"] += 1
        observed[rid] = entry

    new_text = dump(dict(sorted(observed.items())))
    if args.dry_run:
        diff = difflib.unified_diff(old_text.splitlines(True), new_text.splitlines(True), OBSERVED, OBSERVED)
        sys.stdout.writelines(diff)
    elif new_text != old_text:
        h.write_text(root, OBSERVED, new_text)
    if stopped:
        print(f"stopped: {stopped}")
    print(" ".join(f"{k}: {v}" for k, v in counts.items()))
    return 1 if counts["failed"] or stopped else 0


if __name__ == "__main__":
    sys.exit(main())
