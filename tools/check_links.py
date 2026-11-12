#!/usr/bin/env python3
"""Fail when a relative markdown link or anchor does not resolve, an llms.txt link does not map to a
file under base_url, or a record has no catalog page. Exit 0 when broken is 0, else 1; 2 on bad config."""
from __future__ import annotations

import os
import re
import sys
import urllib.parse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hublib as h  # noqa: E402

INLINE_LINK = re.compile(r"!?\[[^\]]*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
REF_LINK = re.compile(r"^\s{0,3}\[[^\]]+\]:\s*<?(\S+?)>?(?:\s+\"[^\"]*\")?\s*$", re.M)
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")
LLMS_FILES = ("llms.txt", "catalog/llms.txt")


def exists_exact_case(root: Path, path: Path) -> bool:
    """Path.exists() ignores case on macOS; the site host does not, so compare names exactly."""
    if not path.exists():
        return False
    try:
        rel = path.relative_to(root)
    except ValueError:
        return False
    cur = root
    for part in rel.parts:
        if part not in os.listdir(cur):
            return False
        cur = cur / part
    return True


class Anchors:
    def __init__(self):
        self.cache = {}

    def of(self, path: Path) -> set[str]:
        if path not in self.cache:
            self.cache[path] = h.anchors_of(path.read_text(encoding="utf-8", errors="replace"))
        return self.cache[path]


def links_in(text: str) -> list[str]:
    plain = h.strip_code(text)
    return INLINE_LINK.findall(plain) + REF_LINK.findall(plain)


def check_md(root: Path, f: Path, anchors: Anchors) -> tuple[int, list[str]]:
    rel = f.relative_to(root).as_posix()
    broken, total = [], 0
    for target in links_in(f.read_text(encoding="utf-8", errors="replace")):
        if SCHEME.match(target):
            continue
        total += 1
        if target.startswith("/"):
            broken.append(f"{rel}: {target}: root-relative link breaks under base_url")
            continue
        path_part, _, anchor = target.partition("#")
        dest = (f.parent / urllib.parse.unquote(path_part)).resolve() if path_part else f
        if not exists_exact_case(root, dest):
            broken.append(f"{rel}: {target}: no such file")
            continue
        if anchor and dest.suffix == ".md" and urllib.parse.unquote(anchor) not in anchors.of(dest):
            broken.append(f"{rel}: {target}: no anchor #{anchor}")
    return total, broken


def check_llms(root: Path, base: str) -> tuple[int, list[str]]:
    broken, total = [], 0
    if not (root / "llms.txt").exists():
        return 0, ["llms.txt: missing (run tools/build.py)"]
    for name in LLMS_FILES:
        f = root / name
        if not f.exists():
            continue
        for target in INLINE_LINK.findall(f.read_text(encoding="utf-8")):
            total += 1
            if not target.startswith(base):
                broken.append(f"{name}: {target}: not under base_url {base}")
                continue
            rel = urllib.parse.unquote(target[len(base):].split("#")[0])
            if not rel or not exists_exact_case(root, (root / rel).resolve()):
                broken.append(f"{name}: {target}: no file {rel or '(empty path)'}")
    return total, broken


def main(argv=None) -> int:
    root, _ = h.root_from_args("Check relative links, anchors, llms.txt links and catalog pages.", argv)
    try:
        cfg = h.load_config(root)
    except h.HubError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    anchors, broken, total = Anchors(), [], 0
    for f in h.repo_files(root):
        if f.suffix == ".md":
            n, b = check_md(root, f, anchors)
            total += n
            broken += b
    n_llms, b = check_llms(root, cfg["base_url"])
    broken += b
    records = h.read_records(root, cfg["kinds"])
    for file, rec in records:
        rid = rec.get("id")
        if isinstance(rid, str) and ":" in rid and not (root / h.page_path(rid)).exists():
            broken.append(f"{file}: {rid}: no catalog page {h.page_path(rid)} (run tools/build.py)")
    print(f"relative links: {total}, llms.txt links: {n_llms}, records: {len(records)}, broken: {len(broken)}")
    for x in broken:
        print(f"  {x}")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
