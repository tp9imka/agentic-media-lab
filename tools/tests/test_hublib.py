"""Unit tests for the validator subset, frontmatter, markdown helpers and the evidence badge."""
import unittest

import hubtest  # noqa: F401  (puts tools/ on sys.path)
import hublib as h


class ValidatorTest(unittest.TestCase):
    SCHEMA = {
        "type": "object", "required": ["kind", "name"], "additionalProperties": False,
        "properties": {
            "kind": {"type": "string", "enum": ["a", "b"]},
            "name": {"type": "string", "pattern": "^[a-z]+$"},
            "tags": {"type": "array", "items": {"type": "string", "enum": ["x", "y"]}},
            "maybe": {"type": ["string", "null"]},
            "n": {"type": "integer"},
            "extra_a": {"type": "string"},
        },
        "allOf": [{"if": {"required": ["kind"], "properties": {"kind": {"enum": ["a"]}}},
                   "then": {"required": ["extra_a"]}}],
    }

    def errs(self, value):
        return h.validate(value, self.SCHEMA)

    def test_valid(self):
        self.assertEqual(self.errs({"kind": "b", "name": "ok", "maybe": None, "tags": ["x"], "n": 3}), [])

    def test_each_keyword(self):
        self.assertIn(("name", "missing required field"), self.errs({"kind": "b"}))
        self.assertIn(("kind", "'c' is not one of: a, b"), self.errs({"kind": "c", "name": "ok"}))
        self.assertIn(("name", "'Bad' does not match ^[a-z]+$"), self.errs({"kind": "b", "name": "Bad"}))
        self.assertIn(("zzz", "unknown field"), self.errs({"kind": "b", "name": "ok", "zzz": 1}))
        self.assertIn(("tags[1]", "'q' is not one of: x, y"), self.errs({"kind": "b", "name": "ok", "tags": ["x", "q"]}))
        self.assertIn(("n", "expected integer, got boolean"), self.errs({"kind": "b", "name": "ok", "n": True}))
        self.assertIn(("maybe", "expected string or null, got integer"), self.errs({"kind": "b", "name": "ok", "maybe": 1}))

    def test_if_then_only_for_matching_kind(self):
        self.assertIn(("extra_a", "missing required field"), self.errs({"kind": "a", "name": "ok"}))
        self.assertEqual(self.errs({"kind": "a", "name": "ok", "extra_a": "v"}), [])

    def test_subset_guard(self):
        with self.assertRaises(h.HubError):
            h.check_schema_subset({"type": "array", "minItems": 1}, "t")

    def test_repo_schemas_stay_in_subset(self):
        schemas = h.load_schemas(hubtest.REPO)
        self.assertEqual(set(schemas), set(h.SCHEMA_FILES))
        self.assertEqual(set(h.kind_required(schemas["record"])), {"tool", "model", "source", "recipe"})


class PathAndBadgeTest(unittest.TestCase):
    def test_contract_page_path(self):
        self.assertEqual(h.page_path("tool:remotion-dev/remotion"), "catalog/tool/remotion-dev__remotion.md")

    def base(self, **kw):
        rec = {"claims": [{"text": "t", "quote": "q", "locator": "l", "url": "https://x", "retrieved": "2026-01-01"}],
               "checked": {"depth": "primary-read"}, "source_type": "primary", "corroboration": "single-source",
               "url_status": "live"}
        rec.update(kw)
        return rec

    def tier(self, rec):
        return h.derive_badge(rec, ["agent-run", "scripted-run", "static-read"])["tier"]

    def test_tiers(self):
        self.assertEqual(self.tier(self.base()), "quoted-primary")
        self.assertEqual(self.tier(self.base(measured={"rung": "agent-run", "command": "c", "input": "i", "commit": "x"})),
                         "measured")
        self.assertEqual(self.tier(self.base(checked={"depth": "skim"})), "quoted-secondary")
        self.assertEqual(self.tier(self.base(corroboration="contested")), "quoted-secondary")
        self.assertEqual(self.tier(self.base(source_type="aggregator")), "quoted-secondary")
        self.assertEqual(self.tier(self.base(checked={"depth": "not-checked"})), "unverified")
        self.assertEqual(self.tier(self.base(claims=[])), "unverified")

    def test_via_blocks_top_rung(self):
        rec = self.base()
        rec["claims"][0]["via"] = "https://secondary"
        badge = h.derive_badge(rec, [])
        self.assertEqual(badge["tier"], "quoted-secondary")
        self.assertIn("a claim is quoted via a secondary source", badge["reasons"])

    def test_downgrade_and_dead_link(self):
        badge = h.derive_badge(self.base(downgrade={"reason": "tiny-sample"}, url_status="dead"), [])
        self.assertEqual(badge["tier"], "quoted-secondary")
        self.assertIn("downgraded one step: tiny-sample", badge["reasons"])
        self.assertIn("link dead", badge["reasons"])

    def test_popularity(self):
        self.assertEqual(h.popularity_flag({"stars": 30000, "installs": 50}, 100), "disagree")
        self.assertIsNone(h.popularity_flag({"stars": 900, "installs": 400}, 100))
        self.assertIsNone(h.popularity_flag({"stars": 900}, 100))


class MarkdownTest(unittest.TestCase):
    def test_frontmatter(self):
        text = ("---\nid: guide:x   # stable\ntitle: \"A: B\"\nconcepts: [concept:a, concept:b]\n"
                "tags:\n  - one\n  - two\n---\n# Body\n")
        fm, body, probs = h.parse_frontmatter(text)
        self.assertEqual(probs, [])
        self.assertEqual(fm, {"id": "guide:x", "title": "A: B", "concepts": ["concept:a", "concept:b"],
                              "tags": ["one", "two"]})
        self.assertEqual(body, "# Body\n")

    def test_frontmatter_absent_or_open(self):
        self.assertIsNone(h.parse_frontmatter("# Title\n")[0])
        self.assertEqual(h.parse_frontmatter("---\nid: x\n")[2], ["frontmatter: no closing ---"])

    def test_anchors(self):
        text = ("# Top\n## Same\n## Same\n## Custom {#keep}\n"
                '## <a id="html-id"></a>Label\n```\n## not a heading\n```\n')
        anchors = h.anchors_of(text)
        for a in ("top", "same", "same-1", "keep", "html-id", "label"):
            self.assertIn(a, anchors)
        self.assertNotIn("not-a-heading", anchors)

    def test_chunks(self):
        body = "intro\n# A\ntext a\n## B\ntext b\n# C\n"
        ch = h.chunks(body)
        self.assertEqual([c["anchor"] for c in ch], ["", "a", "b"])
        self.assertEqual(ch[2]["heading_path"], ["A", "B"])


if __name__ == "__main__":
    unittest.main()
