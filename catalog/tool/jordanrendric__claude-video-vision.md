# claude-video-vision

`tool:jordanrendric/claude-video-vision` - tool - <https://github.com/jordanrendric/claude-video-vision>

A Claude Code plugin with an MCP server that extracts frames with ffmpeg and transcribes audio, so Claude can look at a video file. A /watch-video command and a video-perception skill drive it.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [MCP servers](../../docs/glossary.md#mcp-servers), [Plugins](../../docs/glossary.md#plugins)

Also known as: video-perception, watch-video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives Claude eyes on a finished render, which any renderer's review loop can use when its own skill has no frame-inspection step.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | claude-code |
| levers | review-loop |
| cost | mixed |

It perceives, it does not judge: you still need a review checklist from another skill. The MCP server is fetched from npm by npx on first use, which runs remote code; pin a version or build from the repo if that matters. With the Gemini or OpenAI backend the audio leaves your machine; pick the local Whisper backend for client work. It also downloads YouTube videos with yt-dlp, which this lane did not assess.

## Claims

1. For a video over 30 s its command must run an analysis pass (scene changes, silence, transcription) before pulling frames.

   > 2. **REQUIRED for videos > 30s:** Call `video_analyze` BEFORE `video_watch`. This is NOT optional.

   Locator: commands/watch-video.md, workflow step 2. Source: <https://github.com/jordanrendric/claude-video-vision/blob/HEAD/commands/watch-video.md>, retrieved 2026-11-12.

2. The MCP server installs itself from npm through npx the first time it runs.

   > The MCP server will auto-install via `npx` from [npm](https://www.npmjs.com/package/claude-video-vision) on first use — no build step required.

   Locator: README.md, Quick Start, step 1. Source: <https://github.com/jordanrendric/claude-video-vision/blob/HEAD/README.md>, retrieved 2026-11-12.

3. With the Gemini backend the audio track is sent to Google.

   > - **Audio is sent to Google's Gemini API** via the endpoint `https://generativelanguage.googleapis.com`.

   Locator: PRIVACY.md, section Gemini API. Source: <https://github.com/jordanrendric/claude-video-vision/blob/HEAD/PRIVACY.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md, commands/watch-video.md and PRIVACY.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `d4036e74f419c93378a7833550b22eb60e7a280476f3d4a9ef8b8bd969c5c9a9`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-03-31
- default_branch: main
- fetched_at: 2026-11-12
- forks: 171
- installs: 453
- installs_by_skill: {"video-perception": 453}
- last_activity: 2026-10-14
- licence: MIT
- open_issues: 11
- registry: skills.sh
- sources: https://api.github.com/repos/jordanrendric/claude-video-vision, https://skills.sh/api/search?q=claude-video-vision
- stars: 1492

## Related

None.

## Referenced by

- [Video & Audio Editing MCP Server](misbahsy__video-audio-mcp.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
