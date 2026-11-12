# talking-head-editor

`tool:griffinwooldridge/talking-head-editor` - tool - <https://github.com/griffinwooldridge/talking-head-editor>

A Claude Code skill that turns one raw talking-head take into a finished video: DeepFilterNet voice cleanup and -14 LUFS, Whisper word timings, take selection, tight cuts, face reframing with optional LUT, word-timed captions and HyperFrames motion graphics.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: talking head editor skill

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It has the most concrete delivery check found for transcript cuts: re-transcribe the final file and diff it against the kept words.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | audio, captions, motion, review-loop, design |
| cost | free-local |

macOS or Linux with ffmpeg, Node 18+ and Python 3.9-3.12 (3.13 needs PYTHON= pointing at an older one). Setup builds a venv with whisper, DeepFilterNet and OpenCV and downloads GSAP under GSAP's own licence. Motion graphics render through HyperFrames, whose skill sends a usage beacon. Claude Code only as stated. Not run here.

## Claims

1. Before handover it re-transcribes the final video and diffs it against the kept word list.

   > Re-transcribe `out/final.mp4` and diff it against the keep list: no missing or doubled words.

   Locator: SKILL.md, section 8 Review before you hand it over. Source: <https://github.com/griffinwooldridge/talking-head-editor/blob/main/SKILL.md>, retrieved 2026-11-12.

2. It collapses every pause to about 0.09 seconds.

   > Every pause collapses to about 0.09 s.

   Locator: SKILL.md, section 3 Cut. Source: <https://github.com/griffinwooldridge/talking-head-editor/blob/main/SKILL.md>, retrieved 2026-11-12.

3. Setup downloads GSAP, which has its own licence.

   > GSAP is downloaded at setup under its own license.

   Locator: README.md, section License. Source: <https://github.com/griffinwooldridge/talking-head-editor/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and SKILL.md against the three claims; references/*.md not opened
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `9cf2d35bf0b1e724f5b4371f3e7b344febd67aeee3f1064d982f0694069bed46`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-08
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1
- installs: 6
- installs_by_skill: {"talking-head-editor": 6}
- last_activity: 2026-10-27
- licence: unknown
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/griffinwooldridge/talking-head-editor, https://skills.sh/api/search?q=talking-head-editor
- stars: 10

## Related

- depends_on: [HyperFrames](heygen-com__hyperframes.md)
- alternative_to: [video-use](browser-use__video-use.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
