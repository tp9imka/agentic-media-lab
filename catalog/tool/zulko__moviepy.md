# MoviePy

`tool:zulko/moviepy` - tool - <https://github.com/Zulko/moviepy>

A Python library for cutting, compositing and titling video. It loads frames as numpy arrays and encodes the result through ffmpeg.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Code-driven video](../../docs/glossary.md#code-driven-video)

Also known as: moviepy

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Easy for an agent to script in Python, but agent training data is full of v1 code that v2 broke.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | captions, audio |
| cost | free-local |

Tell the agent to target MoviePy v2 and to read the v1-to-v2 guide: its README example uses v2 names such as `subclipped` and `with_volume_scaled`, and v2 brought major breaking changes, so code written against v1 docs may break. It is slower than ffmpeg alone, so use it for logic and let ffmpeg do heavy filters. TextClip takes a font file path, so ship the .ttf with the project. The README asks for maintainers. I did not check a still-frame API.

## Claims

1. Version 2.0 introduced major breaking changes and v1 is no longer maintained.

   > MoviePy recently upgraded to v2.0, introducing major breaking changes.

   Locator: README.md, note at top. Source: <https://github.com/Zulko/moviepy/blob/master/README.md>, retrieved 2026-11-12.

2. Its own README says it is slower than using ffmpeg directly.

   > albeit slower than using ffmpeg directly due to heavier data import/export operations

   Locator: README.md, How MoviePy works. Source: <https://github.com/Zulko/moviepy/blob/master/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `272feb3c45b86a09aa6266cdc3af1334eac34a6fb1abcb395805f0aaf540c02f`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2013-08-12
- default_branch: master
- fetched_at: 2026-11-12
- forks: 2148
- last_activity: 2026-08-26
- licence: MIT
- open_issues: 96
- sources: https://api.github.com/repos/Zulko/moviepy, https://skills.sh/api/search?q=moviepy
- stars: 15139

## Related

- depends_on: [FFmpeg](ffmpeg__ffmpeg.md)

## Referenced by

- [FFmpeg](ffmpeg__ffmpeg.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
