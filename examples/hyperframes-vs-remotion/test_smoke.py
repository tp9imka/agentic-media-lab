"""Smoke test: the committed clips still measure the way results/*.json say. Skips without ffmpeg."""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent


@unittest.skipUnless(shutil.which("ffmpeg") and shutil.which("ffprobe"), "ffmpeg and ffprobe not on PATH")
class Measure(unittest.TestCase):
    def test_both_arms_reproduce(self):
        for arm in ("hyperframes", "remotion"):
            want = json.loads((HERE / "results" / f"{arm}.json").read_text(encoding="utf-8"))
            with tempfile.TemporaryDirectory() as tmp:
                out = Path(tmp) / "result.json"
                run = subprocess.run([sys.executable, str(HERE / "measure.py"), arm,
                                      str(HERE / "results" / f"{arm}.mp4"), "--out", str(out)],
                                     capture_output=True, text=True)
                got = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
            self.assertEqual(got["verdict"], "pass")
            # Stream facts are exact. Black and freeze segments can shift by a frame across ffmpeg builds.
            self.assertEqual(got["stream"], want["stream"])


if __name__ == "__main__":
    unittest.main()
