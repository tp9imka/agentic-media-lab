# Video & Audio Editing MCP Server

`tool:misbahsy/video-audio-mcp` - tool - <https://github.com/misbahsy/video-audio-mcp>

A Python MCP server of single-purpose ffmpeg tools: trim, concatenate with transitions, burn subtitles, text and image overlays, b-roll insertion, silence removal and format changes.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers)

Also known as: video-audio-mcp

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A small, local way to give any MCP client b-roll and silence removal without writing ffmpeg filter graphs.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | any-mcp, cursor |
| levers | captions, asset, audio |
| cost | free-local |

Needs Python and ffmpeg, nothing hosted. Each tool writes a new file; there is no timeline, undo or project export. Its only check is a server health check, so the agent has to extract frames and listen to the output itself (pair with a frame-inspection tool). Silence removal is by level, not by transcript. Not run here.

## Claims

1. It has a tool that removes silent segments.

   > - `remove_silence` - Automatically remove silent segments

   Locator: README.md, section Available Tools, Advanced Editing. Source: <https://github.com/misbahsy/video-audio-mcp/blob/main/README.md>, retrieved 2026-11-12.

2. It has a tool that inserts b-roll with transitions.

   > - `add_b_roll` - Insert B-roll footage with transitions

   Locator: README.md, section Available Tools, Creative Tools. Source: <https://github.com/misbahsy/video-audio-mcp/blob/main/README.md>, retrieved 2026-11-12.

3. Its only verification tool checks the server, not the output.

   > - `health_check` - Verify server status

   Locator: README.md, section Available Tools, Advanced Editing. Source: <https://github.com/misbahsy/video-audio-mcp/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) tool list against the three claims; server.py not read
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `fd1c800cdb42b7901d85c15da3ff25cc863bc29765c6b8134833b67f689acf94`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-05-24
- default_branch: main
- fetched_at: 2026-11-12
- forks: 15
- last_activity: 2025-05-24
- licence: MIT
- open_issues: 3
- sources: https://api.github.com/repos/misbahsy/video-audio-mcp, https://skills.sh/api/search?q=video-audio-mcp
- stars: 90

## Related

- depends_on: [FFmpeg](ffmpeg__ffmpeg.md)
- integrates_with: [claude-video-vision](jordanrendric__claude-video-vision.md) - adds the frame check this server lacks

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
