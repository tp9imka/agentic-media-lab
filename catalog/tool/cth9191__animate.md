# Animate (cth9191)

`tool:cth9191/animate` - tool - <https://github.com/cth9191/animate>

A Claude Code plugin that makes short procedural canvas animations in seven styles (cut paper, crosshatch, riso, sketchbook, math, isometric, pixel) and renders them to MP4 with Playwright and ffmpeg. It runs story, look and storyboard check-ins before any animation, then a scripted review.

Concepts: [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Visual design](../../docs/glossary.md#visual-design)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its storyboard panels are rendered by the video's own scene functions, so an approved board carries into the build, and its review tool reports numbers instead of an impression.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | claude-code |
| levers | story, motion, design, audio, review-loop |
| cost | free-local |

Borrow: kit/board.js, one file of about 30 lines that draws TIMELINE.board = [{t,title,sound,next}] as a numbered panel grid for thumbs up or down; and tools/beats.mjs, one Node file with only ffmpeg as a dependency (own FFT, spectral-flux onsets, autocorrelation tempo with a prior near 120 BPM, bar phase from low-band energy) that writes beats.json with beats, bars, hits, the loudest moment and drops. Both assume the piece exposes a pure renderFrame(t). tools/review.mjs checks cuts against the beat grid, text cut off or under the phone UI, loudness and dead stretches, but it reads this plugin's TIMELINE format, so lifting it is a few functions plus that format. The style contract in styles/README.md encodes a look as a code plug-in; the kits are canvas drawing code tied to kit/core.js and kit/morph.js. Voice word times come from faster-whisper locally; the optional ElevenLabs connector costs about one credit per character per the skill. MIT. The skill itself lists which formats and styles are proven and which are not. Not run here.

## Claims

1. Animation does not start until the user has approved the storyboard.

   > **No animating before the storyboard is approved.** The check-ins exist because a wrong story or look costs a full build.

   Locator: plugins/animate/skills/animate/SKILL.md, Non-negotiables, rule 1. Source: <https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/SKILL.md>, retrieved 2026-11-12.

2. Each storyboard panel is the real frame at the beat's key time, so approved panels are not redrawn later.

   > The panels ARE the piece: each one is renderFrame(t) at the beat's key time, so an approved board

   Locator: plugins/animate/skills/animate/kit/board.js, header comment. Source: <https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/kit/board.js>, retrieved 2026-11-12.

3. With a supplied track, a beat map is injected into the build and onBeat(t) snaps times to the song's 8th-note grid.

   > the starter head reads `BPM` and `GRID0` from it, and `onBeat(t)` snaps a time to the song's 8th grid.

   Locator: plugins/animate/skills/animate/SKILL.md, Music: the user's own track, step 3. Source: <https://github.com/cth9191/animate/blob/main/plugins/animate/skills/animate/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. plugins/animate/skills/animate/SKILL.md, kit/board.js, tools/beats.mjs, tools/review.mjs, styles/README.md, LICENSE and README.md against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `d04aa6470e31401778ea0f12a28bc06f74a3d73e144bca282db1a2789f055884`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-04
- default_branch: main
- fetched_at: 2026-11-12
- forks: 225
- last_activity: 2026-10-05
- licence: MIT
- open_issues: 5
- sources: https://api.github.com/repos/cth9191/animate, https://skills.sh/api/search?q=animate
- stars: 1780

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
