"""End-to-end tests of tools/build.py on fixture hubs in temp dirs."""
import re
import shutil
import tempfile
import unittest
from pathlib import Path

from hubtest import (DATE, FIXTURES, edit_records, fixture_record, generated_bytes, jsonl, load_json, make_hub, run,
                     write_json)

SUMMARY = re.compile(r"dangling: (\d+) bad concepts: (\d+) invalid: (\d+)")
CONTRACT_KEYS = ("path", "observed", "badge", "concept_labels", "stale", "popularity_flag")
FOOTER = "Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt"


class FixtureBuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.mkdtemp()
        cls.root = make_hub(Path(cls.tmp))
        cls.result = run("build", cls.root)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp)

    def test_summary_line(self):
        self.assertEqual(self.result.returncode, 0, self.result.stderr)
        self.assertIn("dangling: 0 bad concepts: 0 invalid: 0", self.result.stdout)

    def test_records_jsonl_contract(self):
        recs = jsonl(self.root / "index/records.jsonl")
        ids = [r["id"] for r in recs]
        self.assertEqual(ids, sorted(ids))
        self.assertEqual(len(ids), 7)
        by = {r["id"]: r for r in recs}
        for r in recs:
            for k in CONTRACT_KEYS:
                self.assertIn(k, r)
            self.assertEqual(set(r["badge"]), {"tier", "label", "reasons"})
            self.assertTrue((self.root / r["path"]).exists())
        rem = by["tool:remotion-dev/remotion"]
        self.assertEqual(rem["path"], "catalog/tool/remotion-dev__remotion.md")
        self.assertEqual(rem["popularity_flag"], "disagree")
        self.assertEqual(rem["observed"]["stars"], 30000)
        self.assertEqual(rem["concept_labels"], ["Code-driven video", "Agent skills"])
        self.assertEqual(rem["badge"]["tier"], "quoted-primary")
        self.assertIsNone(by["tool:heygen-com/hyperframes"]["popularity_flag"])
        self.assertTrue(by["tool:heygen-com/hyperframes"]["stale"])
        self.assertFalse(rem["stale"])
        self.assertEqual(by["model:example/wan-video"]["badge"]["tier"], "measured")
        self.assertEqual(by["source:example/agent-skills-spec"]["badge"]["tier"], "quoted-secondary")
        self.assertEqual(by["tool:example/old-skill"]["badge"]["tier"], "unverified")
        self.assertEqual(by["recipe:remotion-explainer"]["observed"], {})
        stored = fixture_record(self.root, "tool:remotion-dev/remotion")
        self.assertEqual({k: v for k, v in rem.items() if k not in CONTRACT_KEYS}, stored)

    def test_concepts_json(self):
        obj = load_json(self.root / "index/concepts.json")
        by = {c["id"]: c for c in obj["concepts"]}
        self.assertEqual(by["concept:code-driven-video"]["count"], 3)
        self.assertEqual(by["concept:code-driven-video"]["record_ids"],
                         ["recipe:remotion-explainer", "tool:heygen-com/hyperframes", "tool:remotion-dev/remotion"])
        self.assertEqual(by["concept:agent-surface"]["count"], 0)

    def test_pages_jsonl(self):
        pages = jsonl(self.root / "index/pages.jsonl")
        keys = {"page_id", "title", "path", "anchor", "heading_path", "concepts", "text", "last_reviewed"}
        for p in pages:
            self.assertEqual(set(p), keys)
        guide = [p for p in pages if p["path"] == "docs/first-video.md"]
        self.assertIn("pick", [p["anchor"] for p in guide])
        self.assertEqual(guide[0]["page_id"], "guide:first-video")
        self.assertEqual(guide[0]["last_reviewed"], "2026-11-01")
        self.assertEqual(guide[0]["concepts"], ["concept:code-driven-video", "concept:agent-skills"])
        example = [p for p in pages if p["path"] == "examples/demo/README.md"]
        self.assertEqual(example[0]["page_id"], "example:demo")
        self.assertNotIn("docs/glossary.md", {p["path"] for p in pages})

    def test_meta(self):
        meta = load_json(self.root / "index/meta.json")
        self.assertEqual(set(meta), {"built", "counts", "primary_read_share", "chars_total", "tokens_estimate", "lifetime"})
        self.assertEqual(meta["built"], DATE)
        self.assertEqual(meta["counts"], {"tool": 3, "model": 2, "source": 1, "recipe": 1})
        self.assertEqual(meta["tokens_estimate"], meta["chars_total"] // 4)
        self.assertAlmostEqual(meta["primary_read_share"], round(4 / 7, 3))

    def test_pages_and_inactive(self):
        for rec in jsonl(self.root / "index/records.jsonl"):
            text = (self.root / rec["path"]).read_text()
            self.assertEqual(text.rstrip("\n").splitlines()[-1], FOOTER)
        old = (self.root / "catalog/tool/example__old-skill.md").read_text()
        self.assertTrue(old.startswith("# Old video skill (archived)"))
        readme = (self.root / "catalog/README.md").read_text()
        active, inactive = readme.split("## Archived, retracted and shut down")
        self.assertIn("example__old-skill.md", inactive)
        self.assertIn("example__gone-video.md", inactive)
        self.assertNotIn("example__old-skill.md", active)
        self.assertIn("remotion-dev__remotion.md", active)

    def test_page_slots_in_order(self):
        text = (self.root / "catalog/recipe/remotion-explainer.md").read_text()
        marks = ["# ", "**Badge:**", "**Why:**", "**Last checked:**", "## Fit notes", "## Claims", "## Provenance",
                 "## Observed", "## Related", "## Referenced by", "## Status", FOOTER]
        pos = [text.index(m) for m in marks]
        self.assertEqual(pos, sorted(pos))

    def test_llms_txt(self):
        text = (self.root / "llms.txt").read_text()
        self.assertTrue(text.startswith("# Agentic Media Lab\n\n> "))
        self.assertIn("## Entry points", text)
        self.assertIn("## Optional", text)
        self.assertIn("estimate", text)
        links = re.findall(r"\]\(([^)]+)\)", text)
        self.assertTrue(links)
        for link in links:
            self.assertTrue(link.startswith("https://tp9imka.github.io/agentic-media-lab/"), link)
        self.assertIn("index/records.jsonl", text)
        self.assertIn("Use this page when you want one clip out of a coding agent today.", text)

    def test_graph_and_index(self):
        graph = load_json(self.root / "graph/graph.json")
        kinds = {n["kind"] for n in graph["nodes"]}
        self.assertEqual(kinds, {"tool", "model", "source", "recipe", "concept"})
        rels = {e["rel"] for e in graph["edges"]}
        self.assertEqual(rels, {"about", "alternative_to", "evaluated_on"})
        index = (self.root / "INDEX.md").read_text()
        self.assertIn("Hub size:", index)
        self.assertIn("  - [Code-driven video](docs/glossary.md#code-driven-video) - 3 records", index)

    def test_report(self):
        report = (self.root / "reports/build.md").read_text()
        for needle in ("`tool:heygen-com/hyperframes`: due", "`react`", "`tool:remotion-dev/remotion`: stars 30000",
                       "`recipe:remotion-explainer`"):
            self.assertIn(needle, report)

    def test_generated_docs(self):
        schema = (self.root / "docs/SCHEMA.md").read_text()
        self.assertIn("## Evidence badge", schema)
        self.assertIn("`quoted-primary`", schema)
        self.assertIn("| tool | `url`, `maturity`, `tool_type`", schema)
        glossary = (self.root / "docs/glossary.md").read_text()
        self.assertIn('<a id="code-driven-video"></a>Code-driven video', glossary)
        self.assertIn("Also called: programmatic video", glossary)
        self.assertNotIn("code video", glossary.replace("Code-driven video", ""))


class DeterminismTest(unittest.TestCase):
    def test_byte_identical(self):
        with tempfile.TemporaryDirectory() as tmp:
            a, b = make_hub(Path(tmp), "a"), make_hub(Path(tmp), "b")
            self.assertEqual(run("build", a).returncode, 0)
            self.assertEqual(run("build", b).returncode, 0)
            first = generated_bytes(a)
            self.assertEqual(first, generated_bytes(b))
            self.assertEqual(run("build", a).returncode, 0)
            self.assertEqual(first, generated_bytes(a))

    def test_build_date_moves_stale(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            self.assertEqual(run("build", root, date="2026-10-01").returncode, 0)
            by = {r["id"]: r for r in jsonl(root / "index/records.jsonl")}
            self.assertFalse(by["tool:heygen-com/hyperframes"]["stale"])
            self.assertEqual(load_json(root / "index/meta.json")["built"], "2026-10-01")

    def test_bad_build_date(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(run("build", make_hub(Path(tmp)), date="12/11/2026").returncode, 2)


class EmptyHubTest(unittest.TestCase):
    def test_zero_records_no_vocabulary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp), fixture=False)
            res = run("build", root)
            self.assertEqual(res.returncode, 0, res.stderr)
            self.assertIn("vocabulary is empty", res.stderr)
            self.assertIn("dangling: 0 bad concepts: 0 invalid: 0", res.stdout)
            self.assertEqual((root / "index/records.jsonl").read_text(), "")
            self.assertEqual(load_json(root / "index/concepts.json")["concepts"], [])
            self.assertTrue((root / "index/pages.jsonl").exists())
            self.assertEqual(run("check_links", root).returncode, 0)


class InvalidDataTest(unittest.TestCase):
    CATEGORY = {"dangling": 0, "bad concept": 1, "invalid": 2}

    def build_with(self, tmp, case):
        root = make_hub(Path(tmp), case["rule"].replace(" ", "-").replace("(", "").replace(")", ""))
        rec = fixture_record(root, case["base"])
        rec["id"] = rec["id"] + "-bad"
        for k, v in case.get("set", {}).items():
            rec[k] = v
        for k in case.get("unset", []):
            rec.pop(k, None)
        kind = case["base"].split(":", 1)[0]
        write_json(root / "data" / kind / "zz-bad.json", {"schema_version": 1, "lane": "bad", "records": [rec]})
        return root, run("build", root)

    def test_each_rule_fails(self):
        cases = load_json(FIXTURES / "bad_records.json")["cases"]
        with tempfile.TemporaryDirectory() as tmp:
            for case in cases:
                with self.subTest(rule=case["rule"]):
                    root, res = self.build_with(tmp, case)
                    self.assertEqual(res.returncode, 1, res.stdout)
                    self.assertIn(case["expect"], res.stderr)
                    counts = [int(x) for x in SUMMARY.search(res.stdout).groups()]
                    self.assertGreaterEqual(counts[self.CATEGORY[case["category"]]], 1)
                    self.assertFalse((root / "catalog").exists(), "nothing is written on validation errors")

    def test_error_format(self):
        case = {"rule": "fmt", "base": "tool:remotion-dev/remotion", "set": {"fit": "great"}}
        with tempfile.TemporaryDirectory() as tmp:
            _, res = self.build_with(tmp, case)
            self.assertIn("error: data/tool/zz-bad.json: tool:remotion-dev/remotion-bad: fit: 'great' is not one of",
                          res.stderr)

    def test_wrapper(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            write_json(root / "data/tool/zz.json", {"schema_version": 2, "records": []})
            res = run("build", root)
            self.assertEqual(res.returncode, 1)
            self.assertIn("schema_version must be 1", res.stderr)
            self.assertIn("lane must be a non-empty string", res.stderr)

    def test_concept_rules(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            obj = load_json(root / "data/concepts.json")
            obj["records"].append({"id": "concept:x", "label": "X", "broader": ["concept:nope"], "licence": "MIT"})
            write_json(root / "data/concepts.json", obj)
            res = run("build", root)
            self.assertEqual(res.returncode, 1)
            self.assertIn("concept:x: licence: unknown field", res.stderr)
            self.assertIn("concept:x: broader: unknown concept concept:nope", res.stderr)

    def test_docs_frontmatter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            (root / "docs/no-frontmatter.md").write_text("# Hi\n")
            text = (root / "docs/first-video.md").read_text().replace("concept:agent-skills]", "concept:ghost]")
            (root / "docs/first-video.md").write_text(text)
            res = run("build", root)
            self.assertEqual(res.returncode, 1)
            self.assertIn("docs/no-frontmatter.md: -: -: missing frontmatter", res.stderr)
            self.assertIn("guide:first-video: concepts[1]: unknown concept concept:ghost", res.stderr)

    def test_example_schema(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            ex = load_json(root / "examples/demo/example.json")
            ex["verdict"] = "great"
            write_json(root / "examples/demo/example.json", ex)
            res = run("build", root)
            self.assertEqual(res.returncode, 1)
            self.assertIn("example:demo: verdict: 'great' is not one of", res.stderr)

    def test_dangling_counted_in_summary(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = make_hub(Path(tmp))
            edit_records(root, "tool", lambda rs: rs[0]["related"].append({"id": "tool:x/y", "rel": "extends"}))
            res = run("build", root)
            self.assertIn("dangling: 1 bad concepts: 0 invalid: 0", res.stdout)


if __name__ == "__main__":
    unittest.main()
