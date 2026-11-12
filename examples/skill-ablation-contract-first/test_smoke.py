"""Smoke test: the with-skill clip passes the reference contract; its copy is in the source. Skips without ffmpeg."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe not on PATH")
class Ablation(unittest.TestCase):
    def test_with_skill_passes_reference_contract(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "r.json"
            run = subprocess.run([sys.executable, str(ROOT / "lab/clipcheck/clipcheck.py"), str(HERE / "results/with-skill.mp4"),
                                  "--contract", str(ROOT / "lab/clipcheck/contracts/quote-first.json"),
                                  "--source", str(HERE / "results/source"), "--quiet", "--json", str(out)],
                                 capture_output=True, text=True)
            result = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual((run.returncode, result["errors"]), (0, 0), run.stdout + run.stderr)
        self.assertIn("copy-source", [p["rule"] for p in result["passed"]])


if __name__ == "__main__":
    unittest.main()
