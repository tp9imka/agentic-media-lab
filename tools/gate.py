#!/usr/bin/env python3
"""One command that says whether the repo is consistent. Runs, in order: build, check_links,
check_evidence, private_terms, page budgets, then the optional steps that exist. Offline.
Prints one line per step (PASS, FAIL or skip) and ends with GATE: PASS or GATE: FAIL.
Exit 0 on GATE: PASS, 1 on GATE: FAIL."""
from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import hublib as h  # noqa: E402

STEP_TIMEOUT_S = 900
CORE = ("build", "check_links", "check_evidence", "private_terms")
OPTIONAL_TOOLS = ("search_eval", "decode_eval", "test_mcp_server")
FAIL_TAIL_LINES = 40


class Gate:
    def __init__(self, root: Path):
        self.root = root
        self.failed = False

    def report(self, status: str, name: str, detail: str = "") -> None:
        print(f"{status}: {name}" + (f" ({detail})" if detail else ""), flush=True)
        if status == "FAIL":
            self.failed = True

    def run(self, name: str, cmd: list[str], cwd: Path | None = None) -> None:
        try:
            p = subprocess.run(cmd, cwd=cwd or self.root, capture_output=True, text=True, timeout=STEP_TIMEOUT_S)
        except subprocess.TimeoutExpired:
            self.report("FAIL", name, f"timed out after {STEP_TIMEOUT_S} s")
            return
        out = (p.stdout + p.stderr).strip().splitlines()
        last = p.stdout.strip().splitlines()[-1] if p.stdout.strip() else ""
        if p.returncode == 0:
            self.report("PASS", name, last)
            return
        self.report("FAIL", name, f"exit {p.returncode}")
        for line in out[-FAIL_TAIL_LINES:]:
            print(f"    {line}")

    def page_budgets(self, budget: int) -> None:
        files = [f for f in h.repo_files(self.root) if f.suffix == ".md"]
        files += [self.root / n for n in ("llms.txt", "catalog/llms.txt") if (self.root / n).exists()]
        over = []
        for f in sorted(set(files)):
            n = len(f.read_text(encoding="utf-8", errors="replace"))
            if n > budget:
                over.append(f"{f.relative_to(self.root).as_posix()}: {n} characters")
        if over:
            self.report("FAIL", "page budgets", f"{len(over)} over {budget} characters")
            for x in over:
                print(f"    {x}")
        else:
            self.report("PASS", "page budgets", f"{len(files)} files under {budget} characters")

    def optional(self) -> None:
        py = sys.executable
        for name in OPTIONAL_TOOLS:
            script = self.root / "tools" / f"{name}.py"
            if script.exists():
                self.run(name, [py, str(script)])
            else:
                self.report("skip", name, "not present")
        site = self.root / "site"
        py_tests = sorted(site.rglob("test_*.py")) if site.exists() else []
        js_tests = sorted(p for ext in ("*.js", "*.mjs") for p in site.rglob(ext)
                          if p.name.startswith("test_") or ".test." in p.name) if site.exists() else []
        if py_tests:
            # site/tests is not a package, so unittest discovery finds nothing there: run each file.
            for t in py_tests:
                self.run(f"site python tests ({t.name})", [py, str(t)])
        if js_tests:
            node = shutil.which("node")
            if node:
                self.run("site js tests", [node, "--test", *[str(p) for p in js_tests]])
            else:
                self.report("skip", "site js tests", "node not found")
        if not py_tests and not js_tests:
            self.report("skip", "site tests", "not present")
        smoke = sorted((self.root / "examples").glob("*/test_smoke.py")) if (self.root / "examples").exists() else []
        for t in smoke:
            self.run(t.relative_to(self.root).as_posix(), [py, t.name], cwd=t.parent)
        if not smoke:
            self.report("skip", "examples smoke tests", "not present")


def main(argv=None) -> int:
    root, _ = h.root_from_args("Run every check; print GATE: PASS or GATE: FAIL.", argv)
    gate = Gate(root)
    try:
        budget = h.load_config(root)["page_char_budget"]
    except h.HubError as e:
        print(f"error: {e}")
        print("GATE: FAIL")
        return 1
    for name in CORE:
        gate.run(name, [sys.executable, str(TOOLS / f"{name}.py"), "--root", str(root)])
    gate.page_budgets(budget)
    gate.optional()
    print("GATE: FAIL" if gate.failed else "GATE: PASS")
    return 1 if gate.failed else 0


if __name__ == "__main__":
    sys.exit(main())
