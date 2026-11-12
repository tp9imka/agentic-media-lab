#!/usr/bin/env python3
"""Query the hub index from a shell. Stdlib only. Reads index/*.json(l) and evals/decoder.json.

  query.py search "remotion skill"              ranked search over records and page sections
  query.py search "t2v" --kind model --access weights
  query.py show tool:owner/name                 one record, with what references it
  query.py concept concept:review-loop          a concept and its records
  query.py neighbors tool:owner/name            related records, both directions
  query.py decode "<question in your words>"    the decoder row for a question
  query.py stats                                counts from the index
Add --json to any command. Exit codes: 0 results, 3 nothing found, 2 usage or missing index.
"""
import argparse
import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import search_core as core  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_INDEX = ROOT / "index"
DEFAULT_DECODER = ROOT / "evals" / "decoder.json"
DEFAULT_LIMIT = 8
NEAREST_IDS = 3
EXIT_OK, EXIT_USAGE, EXIT_NONE = 0, 2, 3
INDEX_MISSING = "index missing: run python3 tools/build.py"
NOTHING = "searched, nothing found"
NOT_COVERED = "not covered yet"

KINDS = ("tool", "model", "source", "recipe", core.PAGE_KIND)
ENUMS = {
    "fit": ("high", "medium", "low"),
    "level": ("intro", "intermediate", "advanced"),
    "status": ("current", "disputed", "outdated", "archived", "retracted"),
    "tool_type": ("skill", "plugin", "mcp-server", "renderer", "library", "framework", "runtime",
                  "service", "app"),
    "lever": ("motion", "design", "story", "consistency", "audio", "captions", "review-loop", "delivery",
              "gen-model-craft", "asset", "orchestration", "publishing"),
    "agent": ("claude-code", "codex", "cursor", "gemini-cli", "hermes", "any-skill", "any-mcp",
              "none-stated"),
    "mode": ("t2v", "i2v", "v2v", "edit", "lipsync", "t2i", "i2i", "tts", "music", "stt", "upscale"),
    "access": ("api", "weights", "app-only", "shut-down"),
    "cost": ("free-local", "free-tier", "paid", "mixed", "not-checked"),
}
KIND_FACTS = {
    "tool": ("tool_type", "agents", "levers", "cost", "maturity"),
    "model": ("modes", "access", "apple_silicon", "licence_class", "maturity"),
    "source": ("source_type", "corroboration", "maturity"),
    "recipe": ("video_types", "maturity"),
}


class HubError(Exception):
    pass


def read_jsonl(path):
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise HubError(f"index unreadable: {path.name}:{n}: {exc.msg}; run python3 tools/build.py")
    return out


def load_index(index_dir):
    d = Path(index_dir)
    need = [d / "records.jsonl", d / "concepts.json", d / "meta.json"]
    if not all(p.is_file() for p in need):
        raise HubError(INDEX_MISSING)
    try:
        concepts = json.loads(need[1].read_text(encoding="utf-8")).get("concepts", [])
        meta = json.loads(need[2].read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise HubError(f"index unreadable: {exc.msg}; run python3 tools/build.py")
    pages_path = d / "pages.jsonl"
    return {"records": read_jsonl(need[0]), "concepts": concepts, "meta": meta,
            "pages": read_jsonl(pages_path) if pages_path.is_file() else []}


def load_decoder(path):
    p = Path(path)
    if not p.is_file():
        raise HubError(f"decoder missing: {p}")
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("rows", [])
    except json.JSONDecodeError as exc:
        raise HubError(f"decoder unreadable: {p}: {exc.msg}")


def filters_of(a):
    return {name: getattr(a, name) for name, _ in core.FILTERS if getattr(a, name, None)}


def emit(a, data, text):
    if a.json:
        print(json.dumps(data, indent=1, ensure_ascii=False))
    else:
        print(text)


def hit_lines(i, h):
    where = h["path"] + (f"#{h['anchor']}" if h["anchor"] else "")
    marks = [m for m, on in (("hidden", h["hidden"]), ("stale", h["stale"])) if on]
    badge = h["badge"]["label"] if h["badge"] else "page section"
    out = [f"{i}. {h['id']} - {h['title']}" + (f"  [{', '.join(marks)}]" if marks else ""),
           f"   badge: {badge}" + (f" | checked {h['checked_date']}" if h["checked_date"] else "")]
    if h["why"]:
        out.append(f"   why: {h['why']}")
    out.append(f"   path: {where or '-'}")
    if h["matched"]:
        out.append(f"   matched: {', '.join(h['matched'])}")
    return out


def nearest_ids(ids, want):
    return difflib.get_close_matches(want, ids, n=NEAREST_IDS, cutoff=0.0)


def cmd_search(a, ix):
    filters = filters_of(a)
    if not (a.arg or "").strip() and not filters:
        print('usage: query.py search "<query>" (or give at least one filter)', file=sys.stderr)
        return EXIT_USAGE
    index = core.build_index(ix["records"], ix["concepts"], ix["pages"])
    hits, total = core.search(index, a.arg or "", filters, a.all, a.limit)
    hidden = 0
    if not total and not a.all:
        hidden = core.search(index, a.arg or "", filters, True, 0)[1]
    data = {"query": a.arg or "", "filters": filters, "all": a.all, "total": total, "shown": len(hits),
            "hits": hits, "nothing_found": not hits, "hidden_matches": hidden}
    if not hits:
        lines = [NOTHING]
        if hidden:
            lines.append(f"{hidden} archived, retracted or shut-down records match; add --all to see them")
        lines.append('next: python3 tools/query.py decode "<your question>"')
        emit(a, data, "\n".join(lines))
        return EXIT_NONE
    lines = [f'searched "{a.arg or ""}": {len(hits)} of {total} shown']
    for i, h in enumerate(hits, 1):
        lines += hit_lines(i, h)
    emit(a, data, "\n".join(lines))
    return EXIT_OK


def by_id(ix):
    return {r["id"]: r for r in ix["records"]}


def not_found(a, what, want, ids):
    near = nearest_ids(ids, want)
    emit(a, {"error": f"{what} not found", "id": want, "nearest": near},
         f"{what} not found: {want}" + (f"\nnearest: {', '.join(near)}" if near else ""))
    return EXIT_NONE


def fmt_value(v):
    if isinstance(v, list):
        return ", ".join(str(x) for x in v) or "-"
    if isinstance(v, bool):
        return "yes" if v else "no"
    return "-" if v in (None, "") else str(v)


def cmd_show(a, ix):
    recs = by_id(ix)
    r = recs.get(a.arg or "")
    if r is None:
        return not_found(a, "record", a.arg or "", list(recs))
    refs = core.referenced_by(ix["records"], r["id"])
    data = {**r, "referenced_by": [{"id": i, "rel": rel} for i, rel in refs]}
    badge = (r.get("badge") or {}).get("label") or "Unverified"
    chk = r.get("checked") or {}
    lines = [f"{r['id']} - {r.get('title', '')}",
             f"badge: {badge}" + ("  [stale]" if r.get("stale") else "")
             + ("  [hidden from default search]" if core.is_hidden(r) else ""),
             f"status: {fmt_value(r.get('status'))}" + (f" ({r['status_note']})" if r.get("status_note") else ""),
             f"url: {fmt_value(r.get('url'))}", f"path: {fmt_value(r.get('path'))}",
             f"summary: {fmt_value(r.get('summary'))}", f"why: {fmt_value(r.get('why_it_matters'))}",
             f"fit: {fmt_value(r.get('fit'))} - {fmt_value(r.get('fit_notes'))}",
             f"level: {fmt_value(r.get('level'))}"]
    for k in KIND_FACTS.get(r.get("kind"), ()):
        lines.append(f"{k}: {fmt_value(r.get(k))}")
    for st in r.get("stages") or []:
        lines.append(f"stage {st.get('stage', '')}: {st.get('record_id', '')}"
                     + (f" - {st['note']}" if st.get("note") else ""))
    lines.append(f"checked: {fmt_value(chk.get('date'))} ({fmt_value(chk.get('depth'))}, "
                 f"by {fmt_value(chk.get('by'))}), next due {fmt_value(chk.get('next_due'))}")
    for c in r.get("claims") or []:
        lines.append(f"claim: {c.get('text', '')}")
        lines.append(f'  quote: "{c.get("quote", "")}" ({c.get("locator", "")}) {c.get("url", "")} '
                     f"retrieved {c.get('retrieved', '')}" + (f" via {c['via']}" if c.get("via") else ""))
    obs = r.get("observed") or {}
    if obs:
        lines.append("observed: " + ", ".join(f"{k} {fmt_value(v)}" for k, v in obs.items()))
    if r.get("popularity_flag") == "disagree":
        lines.append("warning: stars and installs disagree by more than the configured ratio")
    for rel in r.get("related") or []:
        lines.append(f"related: {rel.get('rel', '')} {rel.get('id', '')}")
    for i, rel in refs:
        lines.append(f"referenced by: {i} ({rel})")
    emit(a, data, "\n".join(lines))
    return EXIT_OK


def cmd_concept(a, ix):
    concepts = {c["id"]: c for c in ix["concepts"]}
    want = a.arg or ""
    cid = want if want in concepts else f"concept:{want}"
    c = concepts.get(cid)
    if c is None:
        return not_found(a, "concept", want, list(concepts))
    recs = by_id(ix)
    ids = set(c.get("record_ids") or []) | {r["id"] for r in ix["records"] if cid in (r.get("concepts") or [])}
    filters = filters_of(a)
    hits = []
    for rid in sorted(ids):
        r = recs.get(rid)
        if r is None:
            continue
        e = {"id": rid, "kind": r.get("kind", ""), "rec": r}
        if core.visible(e, filters, a.all):
            hits.append(core.hit_of(e, 0.0, []))
    shown = hits[:a.limit]
    data = {"concept": c, "total": len(hits), "records": shown}
    lines = [f"{cid} - {c.get('label', '')}", f"scope: {fmt_value(c.get('scope_note'))}",
             f"also called: {fmt_value((c.get('alt_labels') or []) + (c.get('hidden_labels') or []))}",
             f"broader: {fmt_value(c.get('broader'))}", f"related: {fmt_value(c.get('related'))}",
             f"records: {len(shown)} of {len(hits)} shown"]
    for i, h in enumerate(shown, 1):
        lines += hit_lines(i, h)
    if not hits:
        lines.append(NOTHING)
    emit(a, data, "\n".join(lines))
    return EXIT_OK if hits else EXIT_NONE


def cmd_neighbors(a, ix):
    recs = by_id(ix)
    r = recs.get(a.arg or "")
    if r is None:
        return not_found(a, "record", a.arg or "", list(recs))
    out = [(x.get("id"), x.get("rel") or "related") for x in r.get("related") or [] if isinstance(x, dict)]
    out += [(st.get("record_id"), "stage") for st in r.get("stages") or [] if isinstance(st, dict)]
    filters = filters_of(a)

    def rows(pairs):
        res = []
        for nid, rel in pairs:
            n = recs.get(nid)
            if n is not None and not core.filter_ok(n, filters):
                continue
            res.append({"id": nid, "rel": rel, "title": (n or {}).get("title", ""), "in_index": n is not None,
                        "hidden": bool(n) and core.is_hidden(n)})
        return res
    data = {"id": r["id"], "out": rows(out), "in": rows(core.referenced_by(ix["records"], r["id"]))}
    lines = [f"neighbors of {r['id']}"]
    for direction, label in (("out", "=>"), ("in", "<=")):
        for n in data[direction]:
            note = "" if n["in_index"] else "  [not in index]"
            note += "  [hidden]" if n["hidden"] else ""
            lines.append(f"  {label} {n['rel']}: {n['id']} {n['title']}{note}")
    found = bool(data["out"] or data["in"])
    if not found:
        lines.append(NOTHING)
    emit(a, data, "\n".join(lines))
    return EXIT_OK if found else EXIT_NONE


def row_lines(r):
    out = [f"{r['id']}: {r['question']}  (score {r['score']:.3f}, status {r['status']})"]
    if r["status"] == "not-covered":
        out.append(f"  {NOT_COVERED}: the hub has no route for this question.")
    else:
        if r["status"] == "thin":
            out.append("  thin: the route rests on few records so far.")
        out.append(f"  approach: {fmt_value(r['approach'])}")
        out.append(f"  pages:    {fmt_value(r['pages'])}")
        out.append(f"  records:  {fmt_value(r['record_ids'])}")
        out.append(f"  examples: {fmt_value(r['examples'])}")
        out.append(f"  risk:     {fmt_value(r['risk'])}")
    if r["keywords"]:
        out.append(f'  search:   python3 tools/query.py search "{" ".join(r["keywords"])}"')
    return out


def cmd_decode(a, decoder_rows):
    if not (a.arg or "").strip():
        print('usage: query.py decode "<question>"', file=sys.stderr)
        return EXIT_USAGE
    rows = core.decode(decoder_rows, a.arg, min(a.limit, core.DECODE_MAX_ROWS))
    for r in rows:
        if r["status"] == "not-covered":
            r["answer"] = NOT_COVERED
    data = {"question": a.arg, "rows": rows, "nothing_found": not rows}
    if rows:
        lines = []
        for r in rows:
            lines += row_lines(r)
        emit(a, data, "\n".join(lines))
        return EXIT_OK
    data["nearest"] = core.nearest_rows(decoder_rows, a.arg)
    lines = [NOTHING, "nearest decoder rows:"]
    lines += [f"  {r['id']}: {r['question']}  [{r['status']}]" for r in data["nearest"]]
    emit(a, data, "\n".join(lines))
    return EXIT_NONE


def cmd_stats(a, ix, decoder_rows):
    recs = ix["records"]
    kinds = {}
    for r in recs:
        kinds[r.get("kind", "")] = kinds.get(r.get("kind", ""), 0) + 1
    statuses = {}
    for row in decoder_rows:
        statuses[row.get("status", "")] = statuses.get(row.get("status", ""), 0) + 1
    meta = ix["meta"]
    data = {"records": len(recs), "by_kind": dict(sorted(kinds.items())),
            "hidden": sum(core.is_hidden(r) for r in recs), "stale": sum(bool(r.get("stale")) for r in recs),
            "popularity_disagree": sum(r.get("popularity_flag") == "disagree" for r in recs),
            "concepts": len(ix["concepts"]), "page_chunks": len(ix["pages"]),
            "decoder_rows": dict(sorted(statuses.items())), "built": meta.get("built"),
            "primary_read_share": meta.get("primary_read_share"), "tokens_estimate": meta.get("tokens_estimate"),
            "lifetime": meta.get("lifetime")}
    lines = ["the hub has no records yet" if not recs else f"records: {len(recs)}"]
    for k, v in data["by_kind"].items():
        lines.append(f"  {k}: {v}")
    for k in ("hidden", "stale", "popularity_disagree", "concepts", "page_chunks", "built",
              "primary_read_share", "tokens_estimate", "lifetime"):
        lines.append(f"{k}: {fmt_value(data[k])}")
    lines.append("decoder rows: " + (", ".join(f"{k} {v}" for k, v in data["decoder_rows"].items()) or "none"))
    emit(a, data, "\n".join(lines))
    return EXIT_OK


def parser():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["search", "show", "concept", "neighbors", "decode", "stats"])
    p.add_argument("arg", nargs="?", help="query, id or question")
    p.add_argument("--kind", choices=KINDS)
    for name, values in ENUMS.items():
        p.add_argument("--" + name.replace("_", "-"), dest=name, choices=values)
    p.add_argument("--all", action="store_true", help="include archived, retracted and shut-down records")
    p.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    p.add_argument("--json", action="store_true")
    p.add_argument("--index-dir", default=str(DEFAULT_INDEX))
    p.add_argument("--decoder", default=str(DEFAULT_DECODER))
    return p


def main(argv=None):
    a = parser().parse_args(argv)
    if a.limit < 1:
        print("--limit must be at least 1", file=sys.stderr)
        return EXIT_USAGE
    if a.cmd in ("show", "concept", "neighbors") and not a.arg:
        print(f"usage: query.py {a.cmd} <id>", file=sys.stderr)
        return EXIT_USAGE
    try:
        if a.cmd == "decode":
            return cmd_decode(a, load_decoder(a.decoder))
        ix = load_index(a.index_dir)
        if a.cmd == "stats":
            rows = load_decoder(a.decoder) if Path(a.decoder).is_file() else []
            return cmd_stats(a, ix, rows)
        return {"search": cmd_search, "show": cmd_show, "concept": cmd_concept,
                "neighbors": cmd_neighbors}[a.cmd](a, ix)
    except HubError as exc:
        if a.json:
            print(json.dumps({"error": str(exc)}))
        print(str(exc), file=sys.stderr)
        return EXIT_USAGE


if __name__ == "__main__":
    sys.exit(main())
