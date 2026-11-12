# MakeMyClip Editor

`tool:makemyclip/editor` - tool - <https://github.com/MakeMyClip/editor>

A local editor for agents that ships as a Claude Code skill and plugin, the `clip` CLI, an MCP server and a browser timeline. It removes silence and repeated takes, cuts by transcript words, burns in word-timed captions, checks cuts and exports MP4, FCPXML or Premiere XML.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [MCP servers](../../docs/glossary.md#mcp-servers), [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: @makemyclip/editor, clip CLI, makemyclip-editor

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The closest match to the whole question on a Mac with no paid service: ffmpeg plus local whisper.cpp, a cut check with a contact sheet, and a handoff to Final Cut, Resolve or Premiere.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, any-mcp |
| levers | captions, review-loop, audio, delivery |
| cost | free-local |

Needs Node 24+, ffmpeg with text drawing, and for transcript work `brew install whisper-cpp` plus a ggml model you download yourself; the editor does not fetch one. Run `npx -y @makemyclip/editor doctor` first. The cut check is a CLI and chat feature, not in the browser UI yet. A cut splits clips into pieces, so silence removal has to run per piece (the agent does this in chat). Not run here.

## Claims

1. It runs edits with ffmpeg and a local whisper.cpp on the user's machine.

   > You ask Claude to edit a recording; it calls the editor's tools, and FFmpeg and a local whisper.cpp do the work on your computer.

   Locator: README.md, introduction. Source: <https://github.com/MakeMyClip/editor/blob/main/README.md>, retrieved 2026-11-12.

2. Its cut check flags cuts that may clip a word and writes a contact sheet of the frames either side.

   > | **Cut check** | Flags cuts where a word may be clipped, with a contact sheet of the frames on each side | `clip timeline check` |

   Locator: README.md, section What it does, table. Source: <https://github.com/MakeMyClip/editor/blob/main/README.md>, retrieved 2026-11-12.

3. It exports an FCPXML 1.10 project for Final Cut Pro and DaVinci Resolve.

   > | **Export to Final Cut Pro and DaVinci Resolve** | FCPXML 1.10 project | `clip timeline export --format fcpxml` |

   Locator: README.md, section What it does, table. Source: <https://github.com/MakeMyClip/editor/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; skill file and tool list beyond the README not opened
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `7fca578bf6465a01bc54a6e22fb7eb0cb57519ad0d97b7f997710bb91c7a1b11`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-05-26
- default_branch: main
- fetched_at: 2026-11-12
- forks: 3
- last_activity: 2026-11-07
- licence: MIT
- open_issues: 0
- sources: https://api.github.com/repos/MakeMyClip/editor, https://skills.sh/api/search?q=editor
- stars: 8

## Related

- depends_on: [whisper.cpp](ggml-org__whisper.cpp.md)
- depends_on: [FFmpeg](ffmpeg__ffmpeg.md)
- alternative_to: [video-use](browser-use__video-use.md) - video-use transcribes with a paid ElevenLabs key; this uses local whisper.cpp
- integrates_with: [FCPXML Reference (Apple Developer)](../source/developer.apple.com__documentation__professional-video-applications__fcpxml-reference.md)

## Referenced by

- [FCPXML Reference (Apple Developer)](../source/developer.apple.com__documentation__professional-video-applications__fcpxml-reference.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
