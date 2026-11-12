"""Helpers shared by the tool tests: fixture hubs in temp dirs and tool runs."""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
REPO = TOOLS.parent
FIXTURES = Path(__file__).resolve().parent / "fixtures"
RAW_DIR = FIXTURES / "raw"
DATE = "2026-11-12"
GENERATED = ("index", "catalog", "graph", "reports", "INDEX.md", "llms.txt", "docs/SCHEMA.md", "docs/glossary.md")
HUB_ENV = ("HUB_RAW_DIR", "HUB_PRIVATE_TERMS_FILE", "HUB_BUILD_DATE")
TOOL_TIMEOUT_S = 300

sys.path.insert(0, str(TOOLS))


def make_hub(tmp: Path, name: str = "hub", fixture: bool = True) -> Path:
    """A hub root in tmp: the fixture hub (or only its config) plus the repo's schema files."""
    root = Path(tmp) / name
    if fixture:
        shutil.copytree(FIXTURES / "hub", root)
    else:
        root.mkdir(parents=True)
        shutil.copy(FIXTURES / "hub" / "hub.config.json", root / "hub.config.json")
    shutil.copytree(REPO / "data" / "schema", root / "data" / "schema")
    return root


def run(tool: str, root: Path, env: dict | None = None, date: str | None = DATE, cwd: Path | None = None):
    clean = {k: v for k, v in os.environ.items() if k not in HUB_ENV}
    if date:
        clean["HUB_BUILD_DATE"] = date
    clean.update(env or {})
    return subprocess.run([sys.executable, str(TOOLS / f"{tool}.py"), "--root", str(root)], capture_output=True,
                          text=True, env=clean, cwd=cwd or root, timeout=TOOL_TIMEOUT_S)


def generated_bytes(root: Path) -> dict[str, bytes]:
    out = {}
    for g in GENERATED:
        p = root / g
        files = [p] if p.is_file() else sorted(x for x in p.rglob("*") if x.is_file()) if p.exists() else []
        out.update({f.relative_to(root).as_posix(): f.read_bytes() for f in files})
    return out


def load_json(path: Path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=1) + "\n", encoding="utf-8")


def jsonl(path: Path) -> list[dict]:
    return [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]


def fixture_record(root: Path, rid: str) -> dict:
    kind = rid.split(":", 1)[0]
    for r in load_json(root / "data" / kind / "fixture-lane.json")["records"]:
        if r["id"] == rid:
            return json.loads(json.dumps(r))
    raise KeyError(rid)


def edit_records(root: Path, kind: str, fn) -> None:
    """Apply fn(records) to data/<kind>/fixture-lane.json in place."""
    path = root / "data" / kind / "fixture-lane.json"
    obj = load_json(path)
    fn(obj["records"])
    write_json(path, obj)
