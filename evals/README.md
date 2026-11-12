# Evals

Deterministic checks for search and the decoder. Stdlib Python; `node` only for the parity check.

| File | What it holds | Checked by |
|---|---|---|
| `decoder.json` | The decoder: reader questions => route | `python3 tools/query.py decode "<question>"` |
| `decoder_cases.json` | Paraphrased questions => the decoder row they must hit | `python3 tools/decode_eval.py` |
| `search_queries.json` | Queries => ids that must appear in the top N | `python3 tools/search_eval.py` |

## decoder.json

```json
{"schema_version": 1, "rows": [{"id": "q01", "question": "...", "keywords": ["..."],
  "approach": "...", "pages": ["docs/..."], "record_ids": ["tool:..."], "examples": ["..."],
  "risk": "...", "status": "covered | thin | not-covered"}]}
```

- `id` is stable: `q` and two digits. Never renumber; add new rows at the end.
- `question` is the reader's own words. `keywords` are the words to search with; they are
  also what `decode` matches on, so add synonyms here when a paraphrase misses.
- `status: not-covered` => `decode` answers "not covered yet" and prints no route. Fill
  `approach`, `pages` and `record_ids` before moving a row to `thin` or `covered`.
- The starter has the 20 questions from the hub shape, all `not-covered`.

## decoder_cases.json

`[{"question": "...", "expect_row": "q07"}]`. Passes when the first decoded row is
`expect_row`. `"expect_row": null` passes when `decode` finds nothing (an off-topic control).
Write each case in words that differ from the row's own question.

## search_queries.json

`[{"query": "...", "expect_any": ["tool:owner/name"], "top": 8}]`. Passes when any expected id
is in the top `top` results of default search (archived, retracted and shut-down records left
out). Page sections have ids `<page_id>#<anchor>`. Empty until lanes add records.

## Commands

```
python3 tools/search_eval.py                 # PASS/FAIL per query; "skip: no queries" when empty
python3 tools/search_eval.py --parity        # also compare with site/search_core.js under node
python3 tools/decode_eval.py
python3 -m unittest discover tools/tests_query
```

Both scripts exit 1 on any FAIL. `--index-dir`, `--queries`, `--cases` and `--decoder`
point them at other files.
