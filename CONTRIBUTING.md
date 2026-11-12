# Contributing

Agentic Media Lab is a public knowledge hub about agent-made video and images. Every
record points to a primary source. This page says how to add to it.

## Propose a record

Open an issue with the **Propose a record** form. Give the kind (tool, model, source or
recipe), the canonical URL, why it fits the reader's job, and one verbatim quote with a
locator. Tick the box that says you opened the primary source.

## Report an error in a record

Open an issue with the **Error in a record** form. Give the record id, what is wrong, the
URL of the source that shows it, and a quote from that source.

## Ask a question the hub does not answer

Open an issue with the **Question not covered** form. Write the question in your own
words and say what you tried.

## Before a pull request

Run the gate from the repository root:

```sh
python3 tools/gate.py
```

It must print `GATE: PASS`. CI runs the same command. CI also fails if the gate changes
any tracked file. If that happens, run `python3 tools/build.py` and commit the result.

## Rules a contribution must meet

1. It fits the hub's scope (see the out-of-scope list below).
2. You opened the primary source yourself. A summary or a repost is not enough.
3. Every claim has a verbatim quote, a locator, a URL and a retrieval date.
4. Licences and star counts are never typed by hand. `tools/enrich.py` collects them.
5. A new record starts at `checked.depth: not-checked`. A maintainer raises it after
   checking.
6. Generated output is never edited by hand: `catalog/`, `index/`, `graph/`,
   `reports/`, `INDEX.md`, `llms.txt`. Change the source data and rebuild.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```text
feat(data): add record for <tool>
fix(data): correct licence locator in <record id>
docs: clarify recipe format
```

Common types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`.

## Out of scope

The hub does not accept records, recipes or tools for:

- likeness or voice cloning of real people
- watermark or provenance removal
- safety-filter bypass
- NSFW tooling
- multi-account farming
- ban evasion
- unofficial posting APIs

Issues and pull requests in these areas are closed.

## Licences

By contributing you agree that code is licensed under Apache-2.0 and docs and data under
CC BY 4.0. See [LICENSES/README.md](LICENSES/README.md) for the path map.

## Conduct and security

This project follows the [Code of Conduct](CODE_OF_CONDUCT.md). Report security issues
as described in [SECURITY.md](SECURITY.md), not in public issues.
