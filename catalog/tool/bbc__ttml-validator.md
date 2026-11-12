# ttml-validator (BBC)

`tool:bbc/ttml-validator` - tool - <https://github.com/bbc/ttml-validator>

A BBC command-line validator that checks EBU-TT-D subtitle files against the technical requirements of the BBC Subtitle Guidelines, and TTML2 files against the DAPT profile.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Review loop](../../docs/glossary.md#review-loop)

Tags: subtitles, validator, qc

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is a first-party linter for the BBC rules, so an agent can check a subtitle file without re-implementing the guidelines.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | none-stated |
| levers | captions, review-loop |
| cost | free-local |

Only TTML input (EBU-TT-D or DAPT); SRT and VTT need converting first, and most short-form tools emit SRT or VTT. It checks technical rules only, so reading rate and line breaks still need a separate check. Needs Python 3.14 with poetry or uv. Not installed or run here.

## Claims

1. It checks EBU-TT-D files against the BBC guidelines' technical rules, not the editorial ones.

   > EBU-TT-D meeting the technical (but not editorial) requirements of the

   Locator: README, intro list. Source: <https://github.com/bbc/ttml-validator/blob/main/README.md>, retrieved 2026-11-12.

2. Its authors say technical validation does not replace previewing subtitles against the video.

   > Note that technical validation of a standalone file is not a substitute for previewing the presented file against the media it relates to

   Locator: README, intro note. Source: <https://github.com/bbc/ttml-validator/blob/main/README.md>, retrieved 2026-11-12.

3. It targets Python 3.14.

   > Built with python 3.14, so you might want to make sure you have that version available.

   Locator: README, Usage. Source: <https://github.com/bbc/ttml-validator/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md via GitHub API against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `880f9bb484eb59874760c87f402e964d48586b7227d885bf08a73ba91bcf8ec1`
- Lane: craft

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2024-12-13
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1
- last_activity: 2026-11-09
- licence: unknown
- open_issues: 5
- sources: https://api.github.com/repos/bbc/ttml-validator, https://skills.sh/api/search?q=ttml-validator
- stars: 12

## Related

- depends_on: [BBC Subtitle Guidelines](../source/bbc.co.uk__accessibility__forproducts__guides__subtitles.md)

## Referenced by

- [BBC Subtitle Guidelines](../source/bbc.co.uk__accessibility__forproducts__guides__subtitles.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
