# Tools

Stdlib Python 3.10 to 3.14, no installs, no network. Every command takes `--root <dir>` (default: this repo). Exit 2 means unusable config, schema or `HUB_BUILD_DATE`.

- `python3 tools/build.py` - validate `data/`, then write every generated file; prints `dangling: N bad concepts: N invalid: N`. Exit 0 built, 1 validation errors (nothing written). `HUB_BUILD_DATE=YYYY-MM-DD` fixes the date.
- `python3 tools/check_links.py` - relative links and anchors in `.md` files, `llms.txt` links under `base_url`, one catalog page per record; prints `broken: N`. Exit 0 when N is 0, else 1.
- `python3 tools/check_evidence.py` - claim fields present; with `HUB_RAW_DIR` set, quotes found in the saved source whose sha256 matches `checked.source_sha256`; writes `reports/evidence.md`. Exit 0 ok, 1 missing field or quote not found.
- `python3 tools/private_terms.py` - home paths, emails not in `tools/private_terms.allow`, lines of the local deny list in `HUB_PRIVATE_TERMS_FILE`, agent-directed text in records. Exit 0 clean, 1 on any finding.
- `python3 tools/gate.py` - build, check_links, check_evidence, private_terms, page budgets, then optional steps that exist; ends `GATE: PASS` or `GATE: FAIL`. Exit 0 pass, 1 fail.
- `python3 -m unittest discover tools/tests` - tests on fixture hubs in temp dirs. Exit 0 pass, 1 fail.

`tools/hublib.py` is the shared library: config, loading, the schema-subset validator, reference checks, the evidence badge, markdown helpers.
- `python3 tools/enrich.py` - the only networked command and never part of the gate: asks GitHub, skills.sh, Hugging Face, npm and PyPI for stars, installs, licence, last activity and downloads, and writes `data/observed.json` (its only writer); a failed lookup keeps the previous values. Flags `--only ID`, `--dry-run`, `--max-age-days N`, `--timeout S`; uses `GITHUB_TOKEN` when set; prints `enriched: N unchanged: N failed: N skipped: N`. Exit 0 ok, 1 a lookup failed or the GitHub rate limit stopped the run.
