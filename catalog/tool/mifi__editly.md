# editly

`tool:mifi/editly` - tool - <https://github.com/mifi/editly>

A Node.js tool that builds a video from a JSON5 edit spec of clips, images, titles, audio and GL transitions, streaming through ffmpeg.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Editing real footage](../../docs/glossary.md#footage-editing), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: editly

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A declarative format an agent can write without a frame model, with a `--fast` flag for a low-cost preview render.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: dormant.

| field | value |
|---|---|
| tool_type | renderer |
| agents | none-stated |
| levers | motion, audio, captions |
| cost | free-local |

Needs ffmpeg and ffprobe on PATH and, on Linux, may need extra headless-gl setup; the README's troubleshooting is mostly native-module errors. Without `--fast`, every clip is converted to the first input's size and frame rate unless you set them, which surprises mixed inputs. The last push to the repo was 2025-05-12 (GitHub API, read 2026-11-12), so I marked it dormant. It is a single-maintainer project by its README.

## Claims

1. Its fast mode renders at low resolution and frame rate for a quick preview.

   > Fast mode (low resolution and FPS, useful for getting a quick preview ⏩)

   Locator: README.md, Edit spec options table, fast. Source: <https://github.com/mifi/editly/blob/master/README.md>, retrieved 2026-11-12.

2. Without fast mode, output size and frame rate default to those of the first input video unless set explicitly.

   > Without `--fast`, it will default to using the **width**, **height** and **frame rate** from the **first** input video.

   Locator: README.md, Usage: Command line video editor. Source: <https://github.com/mifi/editly/blob/master/README.md>, retrieved 2026-11-12.

3. It needs ffmpeg and ffprobe installed and on PATH.

   > `ffmpeg` (and `ffprobe`) [installed](http://ffmpeg.org/) and available in `PATH`

   Locator: README.md, Requirements. Source: <https://github.com/mifi/editly/blob/master/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `b1a8788f9066986c60a0160c338036c5302f06aa43cd537c6a47e96239aaafce`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-04-15
- default_branch: master
- fetched_at: 2026-11-12
- forks: 389
- last_activity: 2025-05-12
- licence: MIT
- open_issues: 80
- sources: https://api.github.com/repos/mifi/editly, https://skills.sh/api/search?q=editly
- stars: 5607

## Related

- depends_on: [FFmpeg](ffmpeg__ffmpeg.md)

## Referenced by

- [FFmpeg](ffmpeg__ffmpeg.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
