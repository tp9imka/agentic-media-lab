"""Smoke test: clipcheck still fails the before clip and passes the after clip. Skips without ffmpeg."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
CHECK = ROOT / "lab" / "clipcheck" / "clipcheck.py"
CONTRACT = ROOT / "lab" / "clipcheck" / "contracts" / "quote-first.json"


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe not on PATH")
class FixLoop(unittest.TestCase):
    def check(self, clip):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "r.json"
            # No --ocr: tesseract is optional and its reading varies by version.
            run = subprocess.run([sys.executable, str(CHECK), str(HERE / "results" / clip), "--contract", str(CONTRACT),
                                  "--quiet", "--json", str(out)], capture_output=True, text=True)
            return run.returncode, json.loads(out.read_text(encoding="utf-8"))

    def test_before_fails_on_empty_frames(self):
        code, result = self.check("before.mp4")
        self.assertEqual(code, 1)
        empty = [f for f in result["findings"] if f["rule"] == "empty-frames"]
        self.assertEqual(len(empty), 1)
        self.assertEqual(len(empty[0]["where"]), 3)

    def test_after_passes(self):
        code, result = self.check("after.mp4")
        self.assertEqual((code, result["errors"]), (0, 0))

    def test_every_rule_names_a_hub_source(self):
        rules = json.loads((ROOT / "lab" / "clipcheck" / "rules.json").read_text(encoding="utf-8"))["rules"]
        index = {json.loads(l)["id"]: json.loads(l) for l in (ROOT / "index" / "records.jsonl").read_text(encoding="utf-8").splitlines() if l}
        for rule in rules:
            self.assertTrue(rule["provenance"], rule["id"])
            for ref in rule["provenance"]:
                if ref["record"].startswith("example:"):
                    continue
                rec = index.get(ref["record"])
                self.assertIsNotNone(rec, f"{rule['id']}: {ref['record']} is not a hub record")
                self.assertTrue(any(ref["match"] in c["quote"] for c in rec["claims"]),
                                f"{rule['id']}: no quote in {ref['record']} contains {ref['match']!r}")


if __name__ == "__main__":
    unittest.main()
