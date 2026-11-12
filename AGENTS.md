# AGENTS.md

A knowledge hub on agent-made video and images: which skill, renderer and model to use, how
to raise the result to production quality, and how to automate it. Structured records in
`data/` are the source of truth. Pages, indexes and counts are generated from them.

For anything about this topic, read the hub's pages before answering from memory. The field
changes monthly and several well-known APIs have shut down.

## Given a question

1. `python3 tools/query.py decode "<the question>"` - matches it to a reader question and
   gives the route, or says "not covered yet".
2. `python3 tools/query.py search "<keywords>"` - records and page sections, ranked.
   Filters: `--kind`, `--tool-type`, `--lever`, `--agent`, `--mode`, `--access`, `--cost`.
   Add `--all` to include shut-down and archived records. Add `--json` for machine output.
3. `python3 tools/query.py show <id>` - one record with its quotes, locators and dates.
4. No shell? Start at `llms.txt`. Every page has a markdown URL.

"searched, nothing found" and "not covered yet" are answers. Say them. Do not fill the gap
from memory without saying that it is from memory.

## Reading a record

- Each claim carries a verbatim quote, a locator, a URL and the date it was retrieved.
- The badge says how far to trust it: measured by us, quoted from a primary source read,
  quoted second-hand, or unverified. `docs/SCHEMA.md` has the derivation table.
- `checked.next_due` in the past means the record is stale. Prices, limits, versions and
  API availability go stale in about 30 days.
- Stars and installs come from `data/observed.json`, collected by a tool. When the two
  disagree widely the record is flagged; do not rank by either alone.
- A record describing a third-party skill is not an endorsement. Read a skill before
  installing it.

## Changing the hub

- Gate, before any commit: `python3 tools/gate.py` must end `GATE: PASS`.
- Never hand-edit generated output: `catalog/`, `index/`, `graph/`, `reports/`, `INDEX.md`,
  `llms.txt`, `docs/SCHEMA.md`, `docs/glossary.md`. Run `python3 tools/build.py`.
- Never type a licence, star count, install count or last-commit date into a record.
  `python3 tools/enrich.py` collects them.
- Ids are `<kind>:<slug>`, lowercase, derived from the canonical URL. Never rename or reuse
  one. A retired record stays, marked `archived`.
- A new claim needs a quote copied from the source, not retyped. No quote => no claim.
- When a new source contradicts a record, keep both and link them with `contradicts`.
- Rules for contributions and the out-of-scope list: `CONTRIBUTING.md`.

## Scope

In: skills, plugins, MCP servers, renderers, models, pipelines, craft, automation and
publishing rules for agent-made video and images. Out: likeness or voice cloning of real
people, watermark or provenance removal, safety-filter bypass, NSFW tooling, multi-account
farming, ban evasion, unofficial posting APIs.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
