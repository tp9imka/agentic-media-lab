#!/usr/bin/env python3
"""Fail when a repo file holds a home path, an email not in tools/private_terms.allow, or a line from
the local deny list named by HUB_PRIVATE_TERMS_FILE; or when record text holds an agent-directed command.
Skips .git/, .ref/ and binary files. Exit 0 when clean, 1 on any finding."""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hublib as h  # noqa: E402

BINARY_PROBE = 8192
ALLOW_FILE = "tools/private_terms.allow"

# The character classes keep these patterns from matching their own source text.
HOME_PATHS = (
    ("macOS home path", re.compile(r"(?<![\w.-])/Users/[A-Za-z0-9._-]+/")),
    ("Linux home path", re.compile(r"(?<![\w.-])/home/[A-Za-z0-9._-]+/")),
    ("Windows home path", re.compile(r"[A-Za-z]:\\Users\\", re.I)),
)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")

# Agent-directed commands in record text. Records summarise third-party text and feed llms.txt.
AGENT_DIRECTED = (
    # attempts to replace the reader's instructions
    ("override instructions", re.compile(
        r"\b(ignore|disregard|forget)\s+(all\s+|any\s+)?(the\s+|your\s+)?(previous|prior|above|earlier|system)\s+"
        r"(instructions|prompts?|rules)", re.I)),
    # orders addressed to the reader
    ("you must run", re.compile(r"\byou\s+(must|should|need\s+to)\s+(now\s+)?(run|execute|install|download|delete)\b", re.I)),
    # download piped into an interpreter
    ("pipe to shell", re.compile(r"\b(curl|wget)\b[^\n|]*\|\s*(sudo\s+)?(sh|bash|zsh|python3?|node)\b", re.I)),
    # text that addresses an AI reader directly
    ("addresses an AI", re.compile(r"\b(dear|attention|note to)\s+(ai|llm|agent|assistant|model)s?\b", re.I)),
    ("prompt extraction", re.compile(r"\b(reveal|print|show)\s+(your\s+)?(system\s+prompt|hidden\s+instructions)", re.I)),
)


def load_allow(root: Path) -> tuple[set[str], set[str]]:
    """(exact addresses, @domains) from the allowlist; # starts a comment."""
    path = root / ALLOW_FILE
    if not path.exists():
        path = Path(__file__).resolve().parent / Path(ALLOW_FILE).name
    exact, domains = set(), set()
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            entry = line.split("#", 1)[0].strip().lower()
            if entry.startswith("@"):
                domains.add(entry[1:])
            elif entry:
                exact.add(entry)
    return exact, domains


def load_deny() -> list[str]:
    path = os.environ.get("HUB_PRIVATE_TERMS_FILE")
    if not path:
        return []
    p = Path(path)
    if not p.is_file():
        print("warning: HUB_PRIVATE_TERMS_FILE does not name a file; deny list skipped", file=sys.stderr)
        return []
    return [ln.strip().lower() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.strip().startswith("#")]


def read_text_file(path: Path) -> str | None:
    data = path.read_bytes()
    if b"\0" in data[:BINARY_PROBE]:
        return None
    return data.decode("utf-8", errors="replace")


def allowed(email: str, exact: set[str], domains: set[str]) -> bool:
    e = email.lower()
    return e in exact or e.rsplit("@", 1)[1] in domains


def scan_file(rel: str, text: str, exact, domains, deny) -> list[str]:
    out = []
    for n, line in enumerate(text.splitlines(), 1):
        for name, pat in HOME_PATHS:
            if pat.search(line):
                out.append(f"{rel}:{n}: {name}")
        for m in EMAIL.finditer(line):
            if not allowed(m.group(0), exact, domains):
                out.append(f"{rel}:{n}: email {m.group(0)} not in {ALLOW_FILE}")
        low = line.lower()
        # Report the deny-list line number, never the term, so the log does not leak it.
        out += [f"{rel}:{n}: deny-list entry {i + 1}" for i, term in enumerate(deny) if term in low]
    return out


def strings(value, path=""):
    if isinstance(value, str):
        yield path, value
    elif isinstance(value, list):
        for i, v in enumerate(value):
            yield from strings(v, f"{path}[{i}]")
    elif isinstance(value, dict):
        for k, v in value.items():
            yield from strings(v, f"{path}.{k}" if path else k)


def scan_records(root: Path, kinds: list[str]) -> list[str]:
    out = []
    files = [f for _, f in h.iter_data_files(root, kinds)]
    if (root / "data" / "concepts.json").exists():
        files.append(root / "data" / "concepts.json")
    for f in files:
        rel = f.relative_to(root).as_posix()
        try:
            obj = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue  # the build reports invalid JSON
        items = obj.get("records", []) if isinstance(obj, dict) else obj if isinstance(obj, list) else []
        for rec in items:
            rid = rec.get("id", "-") if isinstance(rec, dict) else "-"
            for field, text in strings(rec):
                out += [f"{rel}: {rid}: {field}: agent-directed text ({name})"
                        for name, pat in AGENT_DIRECTED if pat.search(text)]
    return out


def main(argv=None) -> int:
    root, _ = h.root_from_args("Scan repo files for private terms and record text for agent-directed commands.", argv)
    try:
        kinds = h.load_config(root)["kinds"]
    except h.HubError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    exact, domains = load_allow(root)
    deny = load_deny()
    findings, scanned = [], 0
    for f in h.repo_files(root):
        text = read_text_file(f)
        if text is None:
            continue
        scanned += 1
        findings += scan_file(f.relative_to(root).as_posix(), text, exact, domains, deny)
    findings += scan_records(root, kinds)
    print(f"files scanned: {scanned}, deny-list entries: {len(deny)}, findings: {len(findings)}")
    for x in findings:
        print(f"  {x}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
