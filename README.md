# Agentic Media Lab

A knowledge hub for developers who make video and images with a coding agent.

It answers three questions:

1. **Which stack?** Skill + renderer or model, for the clip you have to make.
2. **How do I make it look professional?** The specific instructions that move motion,
   design, audio, captions and review from "it rendered" to finished.
3. **How do I put it on a schedule?** Runtimes, approval gates, publishing APIs and the
   platform rules that apply.

Claude Code comes first, portable skills that also work in Codex second.

## Status

Early. The pipeline works end to end and the first records are in. Research lanes, worked
examples with measured results and the full site are in progress. Live counts are on the
[index](INDEX.md); this README does not repeat them.

The hub is **living**: prices, model versions and API availability change monthly, so every
record carries the date it was last checked and the date its next check is due.

## Use it

No installs. Python 3.10 or newer.

```sh
git clone https://github.com/tp9imka/agentic-media-lab
cd agentic-media-lab
python3 tools/query.py decode "my agent-made video looks amateur, which skills fix that?"
python3 tools/query.py search "exits shorter than entrances"
python3 tools/query.py show tool:heygen-com/hyperframes
python3 -m http.server 8000    # then open http://localhost:8000/site/
```

Coding agents: read [AGENTS.md](AGENTS.md), or start from [llms.txt](llms.txt).

## What makes a record

- Somebody opened the primary source: the skill file, the licence, the vendor's pricing page.
- Every claim has a verbatim quote, a locator, a URL and a retrieval date.
  `python3 tools/gate.py` checks the fields, and a maintainer run checks each quote against
  a saved copy of the source.
- Licences, stars and install counts are collected by a tool, never typed. Popularity
  signals that disagree are flagged, not averaged.
- Shut-down APIs and retracted claims stay visible and labelled.
- Unknown is a valid value. "Not measured" and "not checked" beat a guess.

## Layout

| Path | What |
|---|---|
| `data/` | Records and vocabulary. The source of truth |
| `catalog/`, `index/`, `graph/`, `reports/`, `INDEX.md`, `llms.txt` | Generated. Never hand-edited |
| `docs/` | Schema, glossary, and guides as they land |
| `tools/` | Build, query, checks and the gate. Stdlib Python |
| `site/` | Static site. No build step, no third-party code |
| `evals/` | Reader questions, search checks |

## Contribute

See [CONTRIBUTING.md](CONTRIBUTING.md). Found a wrong record? Use the "record error" issue
form: the fix is a source and a quote.

## Licence

Code: Apache-2.0. Docs and data: CC BY 4.0. Path map in [LICENSES/README.md](LICENSES/README.md).
Quotes from third-party sources are short, attributed, and remain under their own terms.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
