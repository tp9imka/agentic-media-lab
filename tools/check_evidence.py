#!/usr/bin/env python3
"""Check every claim: quote, locator, url and retrieved are present, and when HUB_RAW_DIR holds the
saved source whose sha256 equals checked.source_sha256, the quote occurs in it (whitespace-normalised).
A claim whose saved source is absent counts as quote-unchecked, not as a failure.
Writes reports/evidence.md. Exit 0 when nothing failed, 1 on a missing field or quote not found, 2 on bad config."""
from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import hublib as h  # noqa: E402

REQUIRED = ("quote", "locator", "url", "retrieved")
HASH_CHUNK = 1 << 20


def normalise(s: str) -> str:
    return " ".join(s.split())


def sha256_of(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(HASH_CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


def saved_sources(raw_dir: str | None) -> dict[str, Path]:
    if not raw_dir:
        return {}
    base = Path(raw_dir)
    if not base.is_dir():
        print(f"warning: HUB_RAW_DIR={raw_dir} is not a directory; every quote is unchecked", file=sys.stderr)
        return {}
    return {sha256_of(p): p for p in sorted(base.rglob("*")) if p.is_file()}


def main(argv=None) -> int:
    root, _ = h.root_from_args("Check claim fields and quotes against saved sources.", argv)
    try:
        cfg = h.load_config(root)
        built = h.build_date()
    except h.HubError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    sources = saved_sources(os.environ.get("HUB_RAW_DIR"))
    texts: dict[str, str] = {}
    counts = {"claims": 0, "missing-fields": 0, "quote-found": 0, "quote-not-found": 0, "quote-unchecked": 0}
    failures, unchecked = [], []
    for file, rec in h.read_records(root, cfg["kinds"]):
        rid = rec.get("id", "-")
        sha = (rec.get("checked") or {}).get("source_sha256")
        for i, claim in enumerate(rec.get("claims") or []):
            counts["claims"] += 1
            claim = claim if isinstance(claim, dict) else {}
            missing = [k for k in REQUIRED if not claim.get(k)]
            if missing:
                counts["missing-fields"] += 1
                failures.append(f"{file}: {rid}: claims[{i}]: missing {', '.join(missing)}")
                continue
            if sha not in sources:
                counts["quote-unchecked"] += 1
                unchecked.append(f"`{rid}` claims[{i}]")
                continue
            if sha not in texts:
                texts[sha] = normalise(sources[sha].read_text(encoding="utf-8", errors="replace"))
            if normalise(claim["quote"]) in texts[sha]:
                counts["quote-found"] += 1
            else:
                counts["quote-not-found"] += 1
                failures.append(f"{file}: {rid}: claims[{i}].quote: not in saved source {sha[:12]}")
    summary = " ".join(f"{k}: {v}" for k, v in counts.items())
    lines = ["# Evidence report", "", f"Run {built.isoformat()} by `tools/check_evidence.py`.", "",
             "Saved sources live outside the public repo, so this report is written by a maintainer run that has them. "
             "A run without them checks claim fields only and leaves this file as it is. A claim is quote-unchecked "
             "when no saved file has the sha256 in the record's `checked.source_sha256`.", "", "## Counts", ""]
    lines += [f"- {k}: {v}" for k, v in counts.items()]
    lines += ["", f"## Failures ({len(failures)})", ""] + ([f"- {x}" for x in failures] or ["None."])
    lines += ["", f"## Quote unchecked ({len(unchecked)})", ""] + ([f"- {x}" for x in unchecked] or ["None."])
    lines += ["", f"Index of all pages: {cfg['base_url']}llms.txt"]
    # Without the saved sources a run cannot reproduce the quote counts, so it must not overwrite them.
    has_sources = bool(sources) or not (root / "reports/evidence.md").exists()
    if has_sources:
        h.write_text(root, "reports/evidence.md", "\n".join(lines) + "\n")
    print(summary + ("" if has_sources else " (report kept: no saved sources in this run)"))
    for x in failures:
        print(f"  {x}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
