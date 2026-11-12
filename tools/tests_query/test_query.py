"""Tests for tools/search_core.py, tools/query.py and the eval scripts, on the fixture index."""
import contextlib
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parent
ROOT = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import decode_eval  # noqa: E402
import query  # noqa: E402
import search_core as core  # noqa: E402
import search_eval  # noqa: E402

FIX = HERE / "fixtures" / "index"
EMPTY = HERE / "fixtures" / "empty_index"
DECODER = ROOT / "evals" / "decoder.json"
CASES = ROOT / "evals" / "decoder_cases.json"
OFF_TOPIC = ("what is the weather in paris", "best pizza recipe in town", "how do I file my taxes",
             "write a python web server", "my cat video", "hello world")


def run(*argv, index=FIX):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = query.main(list(argv) + ["--index-dir", str(index), "--decoder", str(DECODER)])
    return code, out.getvalue(), err.getvalue()


def run_json(*argv, index=FIX):
    code, out, _ = run(*argv, "--json", index=index)
    return code, json.loads(out)


def fixture():
    ix = query.load_index(FIX)
    return ix, core.build_index(ix["records"], ix["concepts"], ix["pages"])


class Tokeniser(unittest.TestCase):
    def test_keeps_codes_with_digits(self):
        self.assertEqual(core.tokens("T2V i2v MP4 on an M3 Max"), ["t2v", "i2v", "mp4", "m3", "max"])

    def test_alias_pairs(self):
        self.assertEqual(core.tokens("text to video"), core.tokens("t2v"))
        self.assertEqual(core.tokens("Image-to-Video"), core.tokens("i2v"))
        self.assertEqual(core.tokens("mcp server"), core.tokens("mcp-server"))
        self.assertEqual(core.tokens("mcpserver"), core.tokens("MCP_server"))

    def test_plural_and_suffix_folding(self):
        self.assertEqual(core.stem("renders"), core.stem("rendering"))
        self.assertEqual(core.stem("skills"), core.stem("skill"))


class Search(unittest.TestCase):
    def test_ranks_expected_record_first(self):
        _, index = fixture()
        hits, _ = core.search(index, "mcp-server render upload")
        self.assertEqual(hits[0]["id"], "tool:example/clip-mcp")
        self.assertIn("mcp", hits[0]["matched"])

    def test_concept_alt_and_hidden_labels_are_indexed(self):
        _, index = fixture()
        ix, index = fixture()
        concepts = {r["id"]: r["concepts"] for r in ix["records"]}
        top = core.search(index, "programmatic video")[0][0]
        self.assertIn("concept:code-driven-video", concepts[top["id"]])
        top = core.search(index, "apple silicon")[0][0]  # a hidden label only
        self.assertIn("concept:local-video-models", concepts[top["id"]])

    def test_page_chunks_return_anchor(self):
        _, index = fixture()
        hits, _ = core.search(index, "ebur128 loudness")
        self.assertEqual(hits[0]["kind"], "page")
        self.assertEqual(hits[0]["anchor"], "loudness")

    def test_hidden_records_need_all(self):
        _, index = fixture()
        ids = [h["id"] for h in core.search(index, "captions library", limit=50)[0]]
        self.assertNotIn("tool:example/old-captioner", ids)
        ids = [h["id"] for h in core.search(index, "captions library", include_hidden=True, limit=50)[0]]
        self.assertIn("tool:example/old-captioner", ids)
        ids = [h["id"] for h in core.search(index, "gone video", limit=50)[0]]
        self.assertNotIn("model:example/gone-video", ids)

    def test_filters_apply_after_ranking(self):
        _, index = fixture()
        all_hits, _ = core.search(index, "video", limit=50)
        tools, _ = core.search(index, "video", {"kind": "tool"}, limit=50)
        self.assertTrue(tools and all(h["kind"] == "tool" for h in tools))
        scores = {h["id"]: h["score"] for h in all_hits}
        self.assertTrue(all(scores[h["id"]] == h["score"] for h in tools))

    def test_deterministic_tie_order(self):
        _, index = fixture()
        a = [h["id"] for h in core.search(index, "fixture", limit=50)[0]]
        b = [h["id"] for h in core.search(index, "fixture", limit=50)[0]]
        self.assertEqual(a, b)


class Cli(unittest.TestCase):
    def test_search_text_has_required_parts(self):
        code, out, _ = run("search", "renderer mp4")
        self.assertEqual(code, 0)
        for part in ("tool:example/framewright", "Framewright (fixture)", "badge: Measured by us",
                     "why: ", "path: catalog/tool/example__framewright.md", "matched: renderer, mp4"):
            self.assertIn(part, out)

    def test_default_limit_is_8_and_limit_flag(self):
        code, data = run_json("search", "fixture")
        self.assertEqual(code, 0)
        self.assertEqual(len(data["hits"]), 8)
        self.assertGreater(data["total"], 8)
        _, data = run_json("search", "fixture", "--limit", "2")
        self.assertEqual(len(data["hits"]), 2)

    def test_json_hit_shape(self):
        _, data = run_json("search", "text to video")
        h = data["hits"][0]
        self.assertEqual(set(h), {"id", "kind", "title", "badge", "why", "path", "anchor", "score", "matched",
                                  "excerpt", "checked_date", "hidden", "stale"})
        self.assertEqual(h["badge"]["label"], "Quoted, primary source read")

    def test_nothing_found(self):
        code, out, _ = run("search", "zzzqqq")
        self.assertEqual(code, 3)
        self.assertIn("searched, nothing found", out)
        code, data = run_json("search", "zzzqqq")
        self.assertEqual((code, data["nothing_found"], data["hits"]), (3, True, []))

    def test_nothing_found_points_at_hidden_matches(self):
        code, out, _ = run("search", "oldcaptioner")
        self.assertEqual(code, 3)
        self.assertIn("add --all", out)
        code, data = run_json("search", "oldcaptioner", "--all")
        self.assertEqual((code, data["hits"][0]["id"]), (0, "tool:example/old-captioner"))

    def test_status_filter_names_hidden_status(self):
        code, data = run_json("search", "", "--status", "archived")
        self.assertEqual(code, 0)
        self.assertEqual([h["id"] for h in data["hits"]], ["tool:example/old-captioner"])

    def test_every_filter(self):
        cases = {("--kind", "model"): "model:example/wavegen", ("--fit", "high"): "tool:example/framewright",
                 ("--level", "advanced"): "model:example/wavegen", ("--tool-type", "skill"): "tool:example/motion-skill",
                 ("--lever", "orchestration"): "tool:example/clip-mcp", ("--agent", "codex"): "tool:example/framewright",
                 ("--mode", "i2v"): "model:example/wavegen", ("--access", "api"): "model:example/cloudmotion",
                 ("--cost", "free-tier"): "tool:example/clip-mcp", ("--status", "current"): "tool:example/framewright"}
        for flag, want in cases.items():
            code, data = run_json("search", "", *flag, "--limit", "50")
            self.assertEqual(code, 0, flag)
            self.assertIn(want, [h["id"] for h in data["hits"]], flag)

    def test_bad_filter_value_is_usage_error(self):
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as cm:
            query.main(["search", "x", "--cost", "cheap"])
        self.assertEqual(cm.exception.code, 2)

    def test_missing_index_message_and_exit(self):
        with tempfile.TemporaryDirectory() as td:
            p = subprocess.run([sys.executable, str(TOOLS / "query.py"), "search", "x", "--index-dir", td],
                               capture_output=True, text=True)
        self.assertEqual(p.returncode, 2)
        self.assertIn("index missing: run python3 tools/build.py", p.stderr)

    def test_show_includes_referenced_by_and_popularity_warning(self):
        code, data = run_json("show", "tool:example/framewright")
        self.assertEqual(code, 0)
        self.assertIn({"id": "recipe:local-explainer", "rel": "stage"}, data["referenced_by"])
        code, out, _ = run("show", "tool:example/clip-mcp")
        self.assertIn("warning: stars and installs disagree", out)

    def test_show_unknown_id_gives_nearest(self):
        code, data = run_json("show", "tool:example/framewrite")
        self.assertEqual(code, 3)
        self.assertEqual(data["nearest"][0], "tool:example/framewright")

    def test_concept(self):
        code, data = run_json("concept", "concept:code-driven-video")
        self.assertEqual(code, 0)
        self.assertEqual(data["total"], 3)
        code, _ = run_json("concept", "review-loop")
        self.assertEqual(code, 0)
        code, data = run_json("concept", "concept:nope")
        self.assertEqual(code, 3)

    def test_neighbors_both_directions(self):
        code, data = run_json("neighbors", "recipe:product-demo-reel")
        self.assertEqual(code, 0)
        self.assertIn("model:example/cloudmotion", [n["id"] for n in data["out"]])
        _, data = run_json("neighbors", "model:example/cloudmotion")
        self.assertIn("recipe:product-demo-reel", [n["id"] for n in data["in"]])

    def test_stats(self):
        code, data = run_json("stats")
        self.assertEqual(code, 0)
        self.assertEqual(data["records"], 12)
        self.assertEqual(data["by_kind"], {"model": 3, "recipe": 2, "source": 3, "tool": 4})
        self.assertEqual((data["hidden"], data["popularity_disagree"]), (2, 1))

    def test_empty_index(self):
        code, out, _ = run("stats", index=EMPTY)
        self.assertEqual(code, 0)
        self.assertIn("the hub has no records yet", out)
        code, out, _ = run("search", "remotion", index=EMPTY)
        self.assertEqual(code, 3)
        self.assertIn("searched, nothing found", out)


class Decoder(unittest.TestCase):
    def setUp(self):
        self.rows = query.load_decoder(DECODER)

    def test_starter_file_shape(self):
        data = json.loads(DECODER.read_text())
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual([r["id"] for r in self.rows], [f"q{n:02d}" for n in range(1, 21)])
        for r in self.rows:
            self.assertEqual(r["status"], "not-covered")
            self.assertEqual((r["pages"], r["record_ids"]), ([], []))
            self.assertTrue(r["keywords"])
        cases = json.loads(CASES.read_text())
        self.assertEqual(sorted(c["expect_row"] for c in cases), [r["id"] for r in self.rows])

    def test_not_covered_rows_do_not_invent_a_route(self):
        code, data = run_json("decode", "Do I need an MCP server or is a skill enough?")
        self.assertEqual(code, 0)
        row = data["rows"][0]
        self.assertEqual((row["id"], row["answer"]), ("q05", "not covered yet"))
        self.assertEqual((row["approach"], row["pages"], row["record_ids"]), ("", [], []))
        _, out, _ = run("decode", "Do I need an MCP server or is a skill enough?")
        self.assertIn("not covered yet", out)
        self.assertNotIn("approach:", out)

    def test_nothing_found_lists_three_nearest(self):
        code, out, _ = run("decode", "best pizza recipe in town")
        self.assertEqual(code, 3)
        self.assertIn("searched, nothing found", out)
        code, data = run_json("decode", "best pizza recipe in town")
        self.assertEqual(len(data["nearest"]), 3)

    def test_off_topic_controls(self):
        for q in OFF_TOPIC:
            self.assertEqual(core.decode(self.rows, q), [], q)

    def test_covered_row_prints_route(self):
        rows = [dict(self.rows[0], status="covered", approach="Compare both renderers.",
                     pages=["docs/guides/x.md"], record_ids=["tool:a/b"])] + self.rows[1:]
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "decoder.json"
            p.write_text(json.dumps({"schema_version": 1, "rows": rows}))
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                code = query.main(["decode", "Remotion or HyperFrames?", "--decoder", str(p)])
        self.assertEqual(code, 0)
        self.assertIn("approach: Compare both renderers.", out.getvalue())


class Evals(unittest.TestCase):
    def quiet(self, fn, argv):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(io.StringIO()):
            code = fn(argv)
        return code, out.getvalue()

    def test_search_eval_skip_pass_fail(self):
        with tempfile.TemporaryDirectory() as td:
            q = Path(td) / "q.json"
            q.write_text("[]")
            self.assertEqual(self.quiet(search_eval.main, ["--queries", str(q), "--index-dir", str(FIX)]),
                             (0, "skip: no queries\n"))
            q.write_text(json.dumps([{"query": "text to video", "expect_any": ["model:example/cloudmotion"], "top": 1}]))
            code, out = self.quiet(search_eval.main, ["--queries", str(q), "--index-dir", str(FIX)])
            self.assertEqual(code, 0)
            self.assertIn("PASS", out)
            q.write_text(json.dumps([{"query": "text to video", "expect_any": ["tool:example/clip-mcp"], "top": 1}]))
            code, out = self.quiet(search_eval.main, ["--queries", str(q), "--index-dir", str(FIX)])
            self.assertEqual(code, 1)
            self.assertIn("FAIL", out)

    @unittest.skipUnless(shutil.which("node"), "node not on PATH")
    def test_parity_with_site_scorer(self):
        queries = ["text to video", "mcp-server", "review loop frames", "free local explainer", "fixture",
                   "subtitles voiceover", "m3 max image-to-video", "benchmark"]
        with tempfile.TemporaryDirectory() as td:
            q = Path(td) / "q.json"
            q.write_text(json.dumps([{"query": x, "expect_any": [], "top": 8} for x in queries]))
            code, out = self.quiet(search_eval.main, ["--parity", "--queries", str(q), "--index-dir", str(FIX)])
        self.assertIn(f"parity: {len(queries)}/{len(queries)}", out)

    def test_decode_eval_passes_on_starter(self):
        code, out = self.quiet(decode_eval.main, [])
        self.assertEqual(code, 0, out)
        self.assertIn("decode_eval: 20/20 PASS", out)

    def test_decode_eval_skip(self):
        with tempfile.TemporaryDirectory() as td:
            c = Path(td) / "c.json"
            c.write_text("[]")
            self.assertEqual(self.quiet(decode_eval.main, ["--cases", str(c)]), (0, "skip: no queries\n"))


if __name__ == "__main__":
    unittest.main()
