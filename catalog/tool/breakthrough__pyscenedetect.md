# PySceneDetect

`tool:breakthrough/pyscenedetect` - tool - <https://github.com/Breakthrough/PySceneDetect>

A Python library and CLI that finds shot boundaries in a video and can split it, save frames or write a cut list.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Review loop](../../docs/glossary.md#review-loop)

Tags: shot-detection, qc

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Run on a render, it gives detected cut times and shot lengths (they depend on detector thresholds and minimum scene length), so a review step can check pacing and catch accidental cuts or a missing transition.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | review-loop, motion |
| cost | free-local |

For a generated clip, run `scenedetect -i out.mp4 detect-adaptive list-scenes` and compare cut count and shot lengths with the shot list. The docs name detect-threshold, not the content detectors, for fades in/out; use it or ffmpeg blackdetect for those. Needs Python and a video backend (OpenCV by default; PyAV and MoviePy are also listed); not installed or run here.

## Claims

1. Use detect-adaptive or detect-content for hard cuts and detect-threshold for fades.

   > For [detector] use detect-adaptive or detect-content to find fast cuts, and detect-threshold for fades in/out.

   Locator: CLI docs, scenedetect command. Source: <https://www.scenedetect.com/docs/latest/cli.html>, retrieved 2026-11-12.

2. Scenes shorter than 0.6 s are not split off by default.

   > Minimum length of any scene. TIMECODE can be specified as number of frames (-m 10), time in seconds (-m 2.5), or timecode (-m 00:02:53.633). Default: 0.6s

   Locator: CLI docs, global option -m/--min-scene-len. Source: <https://www.scenedetect.com/docs/latest/cli.html>, retrieved 2026-11-12.

3. detect-content cuts when the frame difference score exceeds 27.0 by default.

   > Lower values are more sensitive to shot changes. Refers to “content_val” in stats file. Default: 27.0

   Locator: CLI docs, detect-content, option -t/--threshold. Source: <https://www.scenedetect.com/docs/latest/cli.html>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: BSD-3-Clause
- URL status: live
- Saved source sha256: `93a7b5bb24f4ac6fcc3e76c001bf04529ce8ecf83e22ca5cf5f0217cadfa9e5c`
- Lane: craft

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2014-06-04
- default_branch: main
- fetched_at: 2026-11-12
- forks: 567
- last_activity: 2026-11-10
- licence: BSD-3-Clause
- open_issues: 62
- sources: https://api.github.com/repos/Breakthrough/PySceneDetect, https://skills.sh/api/search?q=PySceneDetect
- stars: 5437

## Related

- alternative_to: [FFmpeg](ffmpeg__ffmpeg.md) - ffmpeg scdet gives a per-frame score without splitting

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
