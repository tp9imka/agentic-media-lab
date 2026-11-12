"""Offline tests for tools/enrich.py with a fake fetch function. No network."""
import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import hubtest
import enrich

GH = "https://api.github.com/repos/"
SK = "https://skills.sh/api/search?q="
HF = "https://huggingface.co/api/models/"


def gh_body(full_name, **kw):
    body = {"full_name": full_name, "stargazers_count": 120, "license": {"spdx_id": "MIT"},
            "pushed_at": "2026-11-01T10:00:00Z", "archived": False, "created_at": "2025-01-02T03:04:05Z",
            "forks_count": 7, "open_issues_count": 3, "default_branch": "main"}
    body.update(kw)
    return body


class FakeFetch:
    """url => (status, body, headers, final url). Unknown urls raise like a dead host."""

    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    def __call__(self, url, headers, timeout):
        self.calls.append((url, headers))
        if url not in self.routes:
            raise OSError("connection refused")
        status, body, hdrs, final = (list(self.routes[url]) + [None, None, None])[:4]
        raw = body if isinstance(body, bytes) else json.dumps(body).encode()
        return enrich.Response(status, hdrs or {"x-ratelimit-remaining": "50"}, raw, final or url)


class EnrichTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = hubtest.make_hub(Path(self.tmp.name), fixture=False)
        self.env = mock.patch.dict(os.environ, {"HUB_BUILD_DATE": hubtest.DATE}, clear=False)
        self.env.start()
        os.environ.pop("GITHUB_TOKEN", None)

    def tearDown(self):
        self.env.stop()
        self.tmp.cleanup()

    def records(self, recs):
        by_kind = {}
        for r in recs:
            by_kind.setdefault(r["id"].split(":")[0], []).append(r)
        for kind, rs in by_kind.items():
            hubtest.write_json(self.root / "data" / kind / "lane.json",
                               {"schema_version": 1, "lane": "lane", "records": rs})

    def run_enrich(self, routes, *argv):
        fetch = FakeFetch(routes)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            code = enrich.main(["--root", str(self.root), *argv], fetch=fetch, sleep=lambda s: None)
        return code, out.getvalue(), fetch

    def observed(self):
        return hubtest.load_json(self.root / "data" / "observed.json")

    def gh_record(self, slug="acme/kit"):
        return {"id": f"tool:{slug}", "url": f"https://github.com/{slug}"}

    def test_github_mapping(self):
        self.records([self.gh_record()])
        code, out, _ = self.run_enrich({GH + "acme/kit": (200, gh_body("acme/kit")), SK + "kit": (200, {"skills": []})})
        self.assertEqual(code, 0, out)
        e = self.observed()["tool:acme/kit"]
        self.assertEqual((e["stars"], e["licence"], e["last_activity"], e["archived"], e["created"], e["forks"]),
                         (120, "MIT", "2026-11-01", False, "2025-01-02", 7))
        self.assertEqual(e["fetched_at"], hubtest.DATE)
        self.assertEqual(e["sources"], [GH + "acme/kit", SK + "kit"])
        self.assertNotIn("installs", e)
        self.assertNotIn("moved_to", e)
        self.assertIn("enriched: 1 unchanged: 0 failed: 0 skipped: 0", out)

    def test_moved_repo(self):
        self.records([self.gh_record("old/kit")])
        final = "https://api.github.com/repositories/42"
        code, _, _ = self.run_enrich({GH + "old/kit": (200, gh_body("new/kit2"), None, final),
                                      SK + "kit": (200, {"skills": [{"source": "New/Kit2", "name": "a",
                                                                     "installs": 5}]})})
        e = self.observed()["tool:old/kit"]
        self.assertEqual(e["moved_to"], "new/kit2")
        self.assertIn(final, e["sources"])
        self.assertEqual(e["installs"], 5)

    def test_noassertion_and_null_licence_are_unknown(self):
        self.records([self.gh_record("a/one"), self.gh_record("a/two")])
        self.run_enrich({GH + "a/one": (200, gh_body("a/one", license={"spdx_id": "NOASSERTION"})),
                         GH + "a/two": (200, gh_body("a/two", license=None)),
                         SK + "one": (200, {"skills": []}), SK + "two": (200, {"skills": []})})
        obs = self.observed()
        self.assertEqual(obs["tool:a/one"]["licence"], "unknown")
        self.assertEqual(obs["tool:a/two"]["licence"], "unknown")

    def test_skills_source_filter_and_max_not_sum(self):
        self.records([self.gh_record()])
        skills = [{"source": "ACME/kit", "name": "render", "installs": 900},
                  {"source": "acme/kit", "name": "edit", "installs": 300},
                  {"source": "other/kit", "name": "render", "installs": 99999},
                  {"source": "acme/kit-extra", "name": "x", "installs": 50000}]
        self.run_enrich({GH + "acme/kit": (200, gh_body("acme/kit")), SK + "kit": (200, {"skills": skills})})
        e = self.observed()["tool:acme/kit"]
        self.assertEqual(e["installs"], 900)
        self.assertEqual(e["installs_by_skill"], {"render": 900, "edit": 300})
        self.assertEqual(e["registry"], "skills.sh")

    def test_huggingface_mapping(self):
        self.records([{"id": "model:org/m1", "url": "https://huggingface.co/Org/M1"}])
        body = {"tags": ["video", "license:apache-2.0"], "lastModified": "2026-10-09T01:02:03.000Z",
                "createdAt": "2026-01-01T00:00:00.000Z", "downloads": 1234, "likes": 56, "gated": False}
        code, out, _ = self.run_enrich({HF + "Org/M1": (200, body)})
        self.assertEqual(code, 0, out)
        e = self.observed()["model:org/m1"]
        self.assertEqual((e["licence"], e["last_activity"], e["created"], e["hf_downloads"], e["hf_likes"], e["gated"]),
                         ("apache-2.0", "2026-10-09", "2026-01-01", 1234, 56, False))
        self.run_enrich({HF + "Org/M1": (200, {"tags": ["video"]})})
        self.assertEqual(self.observed()["model:org/m1"]["licence"], "unknown")

    def test_no_lookup_gets_no_entry(self):
        self.records([{"id": "source:example.org/page", "url": "https://example.org/page"}])
        code, out, fetch = self.run_enrich({})
        self.assertEqual(fetch.calls, [])
        self.assertEqual(self.observed(), {})
        self.assertIn("skipped: 1", out)

    def test_failed_lookup_keeps_previous_values(self):
        self.records([self.gh_record()])
        prev = {"tool:acme/kit": {"stars": 10, "licence": "MIT", "fetched_at": "2026-01-01"}}
        hubtest.write_json(self.root / "data" / "observed.json", prev)
        code, out, fetch = self.run_enrich({GH + "acme/kit": (503, b"down"), SK + "kit": (200, {"skills": []})})
        self.assertEqual(code, 1)
        e = self.observed()["tool:acme/kit"]
        self.assertEqual((e["stars"], e["licence"], e["fetched_at"]), (10, "MIT", "2026-01-01"))
        self.assertEqual(e["errors"], ["api.github.com: HTTP 503"])
        self.assertEqual([u for u, _ in fetch.calls].count(GH + "acme/kit"), 2)  # one retry on 5xx
        self.assertIn("failed: 1", out)

    def test_failed_lookup_without_previous_writes_nothing(self):
        self.records([self.gh_record()])
        self.run_enrich({SK + "kit": (200, {"skills": []})})
        self.assertEqual(self.observed(), {})

    def test_dry_run_writes_nothing(self):
        self.records([self.gh_record()])
        code, out, _ = self.run_enrich({GH + "acme/kit": (200, gh_body("acme/kit")), SK + "kit": (200, {"skills": []})},
                                       "--dry-run")
        self.assertFalse((self.root / "data" / "observed.json").exists())
        self.assertIn('+    "stars": 120', out)

    def test_deterministic_output(self):
        self.records([self.gh_record("b/two"), self.gh_record("a/one")])
        routes = {GH + "a/one": (200, gh_body("a/one")), GH + "b/two": (200, gh_body("b/two")),
                  SK + "one": (200, {"skills": []}), SK + "two": (200, {"skills": []})}
        self.run_enrich(routes)
        first = (self.root / "data" / "observed.json").read_bytes()
        code, out, _ = self.run_enrich(routes)
        self.assertEqual((self.root / "data" / "observed.json").read_bytes(), first)
        self.assertIn("enriched: 0 unchanged: 2", out)
        text = first.decode()
        self.assertTrue(text.endswith("}\n"))
        self.assertEqual(text, json.dumps(json.loads(text), indent=2, sort_keys=True) + "\n")

    def test_rate_limit_stops_run(self):
        self.records([self.gh_record("a/one"), self.gh_record("b/two")])
        code, out, fetch = self.run_enrich({
            GH + "a/one": (200, gh_body("a/one"), {"x-ratelimit-remaining": "0", "x-ratelimit-reset": "0"}),
            SK + "one": (200, {"skills": []}), GH + "b/two": (200, gh_body("b/two"))})
        self.assertEqual(code, 1)
        self.assertNotIn(GH + "b/two", [u for u, _ in fetch.calls])
        self.assertIn("stopped: GitHub rate limit reached", out)
        self.assertIn("enriched: 1 unchanged: 0 failed: 0 skipped: 1", out)
        self.assertEqual(list(self.observed()), ["tool:a/one"])

    def test_token_only_in_header(self):
        self.records([self.gh_record()])
        with mock.patch.dict(os.environ, {"GITHUB_TOKEN": "secret-token-value"}):
            _, out, fetch = self.run_enrich({GH + "acme/kit": (200, gh_body("acme/kit")),
                                             SK + "kit": (200, {"skills": []})})
        self.assertEqual(fetch.calls[0][1]["Authorization"], "Bearer secret-token-value")
        self.assertNotIn("Authorization", fetch.calls[1][1])
        self.assertNotIn("secret-token-value", out + (self.root / "data" / "observed.json").read_text())
        self.assertEqual(fetch.calls[0][1]["User-Agent"], enrich.USER_AGENT)

    def test_max_age_and_only(self):
        self.records([self.gh_record("a/one"), self.gh_record("b/two")])
        hubtest.write_json(self.root / "data" / "observed.json",
                           {"tool:a/one": {"stars": 1, "fetched_at": "2026-11-10"}})
        routes = {GH + "b/two": (200, gh_body("b/two")), SK + "two": (200, {"skills": []})}
        code, out, fetch = self.run_enrich(routes, "--max-age-days", "7")
        self.assertEqual(code, 0, out)
        self.assertIn("enriched: 1 unchanged: 0 failed: 0 skipped: 1", out)
        code, out, fetch = self.run_enrich(routes, "--only", "tool:b/two")
        self.assertEqual([u for u, _ in fetch.calls], [GH + "b/two", SK + "two"])
        self.assertEqual(self.observed()["tool:a/one"]["stars"], 1)

    def test_npm_and_pypi_hints(self):
        self.records([{"id": "tool:pkgs", "url": "https://example.org", "tags": ["npm:@x/cli", "pypi:xtool"]}])
        self.run_enrich({"https://api.npmjs.org/downloads/point/last-week/@x/cli": (200, {"downloads": 40}),
                         "https://pypistats.org/api/packages/xtool/recent": (200, {"data": {"last_week": 70}})})
        e = self.observed()["tool:pkgs"]
        self.assertEqual((e["downloads_week"], e["registry"]), (70, "npm, pypi"))


if __name__ == "__main__":
    unittest.main()
