# motion-skills (iArt)

`tool:iart-ai/motion-skills` - tool - <https://github.com/iart-ai/motion-skills>

An index of 19 motion-graphics skill packs plus a small verify toolkit: seek-and-screenshot, a contact sheet of start, middle and end, and an MP4 spec probe.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Agent Skills](../../docs/glossary.md#agent-skills), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The verify scripts are a renderer-neutral review loop: look at three frames on one sheet, then assert resolution, codec, fps and duration of the file.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, any-skill |
| levers | review-loop, delivery, motion |
| cost | free-local |

The skills themselves live in 19 other repos; this record covers only the index and tools/verify. The README promotes the vendor's paid iArt agent and cites its own cost figures; I did not check them. The scripts need ffmpeg, and Playwright Chromium for HTML; I did not run them.

## Claims

1. After stills are tiled, the agent inspects the sheet against the brief for clipped or off-canvas text.

   > # inspect sheet.png: matches the brief? clipped text / off-canvas / FOUC?

   Locator: tools/verify/README.md, Usage by tier, Light. Source: <https://github.com/iart-ai/motion-skills/blob/HEAD/tools/verify/README.md>, retrieved 2026-11-12.

2. It asserts a vertical short's real resolution and frame rate from the encoded file.

   > scripts/probe-mp4.sh out/short.mp4 1080x1920 30 # vertical short contract

   Locator: tools/verify/README.md, Usage by tier, Heavy Remotion. Source: <https://github.com/iart-ai/motion-skills/blob/HEAD/tools/verify/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `10c9457e7f240309b77ab6042e402c64d0ae66ce4d06008d58c9a361d2541c96`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-06-22
- default_branch: master
- fetched_at: 2026-11-12
- forks: 122
- last_activity: 2026-11-11
- licence: MIT
- open_issues: 2
- sources: https://api.github.com/repos/iart-ai/motion-skills, https://skills.sh/api/search?q=motion-skills
- stars: 1389

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
