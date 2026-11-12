# SynthCut

`tool:relo-video/synthcut` - tool - <https://github.com/Relo-video/SynthCut>

An Electron multi-track editor whose core is an MCP server: cut, trim, grade, captions from Whisper, reframe, ducking, transcript editing and export, all through local ffmpeg. The UI mirrors every agent edit live.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: SynthCut by Relo, ai-video-editor MCP

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the one open editor here that has filler-and-pause removal, colour, loudness presets and a frame-inspection tool for the agent in one MCP surface.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex, cursor, gemini-cli, any-mcp |
| levers | captions, audio, review-loop, delivery, design |
| cost | free-local |

On a Mac it runs from source only: the packaged build and its auto-update are Windows-only. The README gives two tool counts (85 and 94). Motion graphics go through Remotion, which has its own company licence. A hosted sibling (relo.video) is advertised in the README; the open editor itself is local. Not run here.

## Claims

1. Its transcript tools remove filler words and long pauses in one call and cut by word index.

   > `tighten_talk` strips filler words + long pauses in one call, `delete_transcript_ranges` cuts by word index, and `edit_by_transcript` assembles a cut from your edited script

   Locator: README.md, section Features, Text-based editing. Source: <https://github.com/Relo-video/SynthCut/blob/main/README.md>, retrieved 2026-11-12.

2. There is no packaged macOS build; Mac users run it from source.

   > There is **no packaged installer for macOS or Linux yet** — the current release build (and its auto-update) is Windows-only.

   Locator: README.md, section Run on macOS & Linux (from source). Source: <https://github.com/Relo-video/SynthCut/blob/main/README.md>, retrieved 2026-11-12.

3. Export presets include loudness normalisation to -14 or -16 LUFS and sidecar SRT or VTT captions.

   > platform export presets with loudness normalization (-14/-16 LUFS), and sidecar SRT/VTT caption export/import.

   Locator: README.md, section Features, Output. Source: <https://github.com/Relo-video/SynthCut/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; GETTING_STARTED.md and the skill installer not opened
- Next check due: 2027-02-10
- Licence: GPL-3.0
- URL status: live
- Saved source sha256: `963068ba9a37d7f044001b663180d41d03fbb745d234caf3b7786e68f53b31cd`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-07-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 10
- last_activity: 2026-07-21
- licence: GPL-3.0
- open_issues: 15
- sources: https://api.github.com/repos/Relo-video/SynthCut, https://skills.sh/api/search?q=SynthCut
- stars: 47

## Related

- integrates_with: [Remotion Agent Skills](remotion-dev__skills.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
