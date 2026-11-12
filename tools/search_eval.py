#!/usr/bin/env python3
"""Check search ranking against evals/search_queries.json. Stdlib only.

  search_eval.py                         PASS/FAIL per query, exit 1 on any FAIL
  search_eval.py --parity                also run the queries through site/search_core.js with node
                                         and fail on any rank difference in the top 8
  search_eval.py --index-dir DIR --queries FILE
Each query: {"query": "...", "expect_any": ["id", ...], "top": N}. Passes when any expected id
is in the top N (default 8).
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import query  # noqa: E402
import search_core as core  # noqa: E402

ROOT = query.ROOT
DEFAULT_QUERIES = ROOT / "evals" / "search_queries.json"
SITE_CORE = ROOT / "site" / "search_core.js"
DEFAULT_TOP = 8
PARITY_TOP = 8
SCORE_TOLERANCE = 1e-6

NODE_HARNESS = r"""
import { readFileSync, existsSync } from "node:fs";
import { pathToFileURL } from "node:url";
const [corePath, indexDir, queriesPath, top] = process.argv.slice(2);
const core = await import(pathToFileURL(corePath).href);
const read = name => readFileSync(indexDir + "/" + name, "utf8");
const records = core.parseJsonl(read("records.jsonl"));
const concepts = JSON.parse(read("concepts.json")).concepts || [];
const pages = existsSync(indexDir + "/pages.jsonl") ? core.parseJsonl(read("pages.jsonl")) : [];
const index = core.buildIndex(records, concepts, pages);
const out = {};
for (const q of JSON.parse(readFileSync(queriesPath, "utf8"))) {
  out[q] = core.search(index, q, {}, false, Number(top))[0].map(h => [h.id, h.score]);
}
process.stdout.write(JSON.stringify(out));
"""


def python_top(index, q, n):
    return [(h["id"], h["score"]) for h in core.search(index, q, {}, False, n)[0]]


def js_top(index_dir, queries, n):
    """{query: [(id, score)]} from site/search_core.js, or None when node is missing."""
    node = shutil.which("node")
    if not node:
        return None
    with tempfile.TemporaryDirectory() as td:
        harness, qfile = Path(td) / "harness.mjs", Path(td) / "queries.json"
        harness.write_text(NODE_HARNESS, encoding="utf-8")
        qfile.write_text(json.dumps(queries), encoding="utf-8")
        run = subprocess.run([node, str(harness), str(SITE_CORE), str(index_dir), str(qfile), str(n)],
                             capture_output=True, text=True, check=False)
    if run.returncode:
        raise RuntimeError(f"node harness failed: {run.stderr.strip()}")
    return {q: [tuple(x) for x in v] for q, v in json.loads(run.stdout).items()}


def parity(index, index_dir, queries):
    js = js_top(index_dir, queries, PARITY_TOP)
    if js is None:
        print("skip: node not found")
        return 0
    bad = 0
    worst = 0.0
    for q in queries:
        py = python_top(index, q, PARITY_TOP)
        jj = js.get(q, [])
        worst = max([worst] + [abs(a[1] - b[1]) for a, b in zip(py, jj)])
        if [i for i, _ in py] != [i for i, _ in jj]:
            bad += 1
            print(f"PARITY FAIL {q!r}\n  py: {py}\n  js: {jj}")
    print(f"parity: {len(queries) - bad}/{len(queries)} queries rank the same top {PARITY_TOP} "
          f"in Python and JS (largest score difference {worst:.2e})")
    return 1 if bad or worst > SCORE_TOLERANCE else 0


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--parity", action="store_true")
    p.add_argument("--index-dir", default=str(query.DEFAULT_INDEX))
    p.add_argument("--queries", default=str(DEFAULT_QUERIES))
    a = p.parse_args(argv)
    items = json.loads(Path(a.queries).read_text(encoding="utf-8")) if Path(a.queries).is_file() else []
    if not items:
        print("skip: no queries")
        return 0
    try:
        ix = query.load_index(a.index_dir)
    except query.HubError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    index = core.build_index(ix["records"], ix["concepts"], ix["pages"])
    known = {r["id"] for r in ix["records"]} | {e["id"] for e in (d["e"] for d in index.docs)}
    fails = 0
    for it in items:
        top = it.get("top") or DEFAULT_TOP
        ids = [i for i, _ in python_top(index, it["query"], top)]
        want = it.get("expect_any") or []
        for w in want:
            if w not in known and not w.startswith(("guide:", "example:")):
                print(f"warning: expected id not in index: {w}")
        # A page hit is `<page id>#<anchor>`; an expected page id matches any of its sections.
        rank = next((n for n, i in enumerate(ids, 1) if i in want or i.split("#")[0] in want), None)
        if rank:
            print(f"PASS  {it['query']!r}: {ids[rank - 1]} at rank {rank} (top {top})")
        else:
            fails += 1
            print(f"FAIL  {it['query']!r}: none of {want} in top {top}; got {ids}")
    print(f"search_eval: {len(items) - fails}/{len(items)} PASS")
    code = 1 if fails else 0
    if a.parity:
        try:
            code = max(code, parity(index, a.index_dir, [it["query"] for it in items]))
        except RuntimeError as exc:
            print(str(exc))
            code = 1
    return code


if __name__ == "__main__":
    sys.exit(main())
