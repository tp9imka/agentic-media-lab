#!/usr/bin/env python3
"""Check the decoder against evals/decoder_cases.json. Stdlib only.

  decode_eval.py [--cases FILE] [--decoder FILE]
Each case: {"question": "...", "expect_row": "q07"}. Passes when the first decoded row is
expect_row. "expect_row": null passes when decode finds nothing (an off-topic control).
Exit 1 on any FAIL; "skip: no queries" and exit 0 when the file has no cases.
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import query  # noqa: E402
import search_core as core  # noqa: E402

DEFAULT_CASES = query.ROOT / "evals" / "decoder_cases.json"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--cases", default=str(DEFAULT_CASES))
    p.add_argument("--decoder", default=str(query.DEFAULT_DECODER))
    a = p.parse_args(argv)
    cases = json.loads(Path(a.cases).read_text(encoding="utf-8")) if Path(a.cases).is_file() else []
    if not cases:
        print("skip: no queries")
        return 0
    try:
        rows = query.load_decoder(a.decoder)
    except query.HubError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    ids = {r["id"] for r in rows}
    fails = 0
    for c in cases:
        want = c.get("expect_row")
        got = [r["id"] for r in core.decode(rows, c["question"])]
        if want is not None and want not in ids:
            ok, note = False, f"expected row {want} is not in the decoder"
        elif want is None:
            ok, note = not got, "nothing found" if not got else f"got {got}"
        else:
            ok, note = bool(got) and got[0] == want, f"got {got or 'nothing'}"
        fails += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {c['question']!r}: want {want}, {note}")
    print(f"decode_eval: {len(cases) - fails}/{len(cases)} PASS")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
