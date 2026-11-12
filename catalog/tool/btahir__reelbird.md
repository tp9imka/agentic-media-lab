# Reelbird

`tool:btahir/reelbird` - tool - <https://github.com/btahir/reelbird>

A native macOS screen recorder with auto-zoom, smooth cursor, on-device captions, pause and 'um' cleanup, blur and redaction, with a CLI and an MCP server for agents. Share links go to your own bucket or an optional paid host.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: reelbird

Tags: screen-recording, auto-zoom

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It covers recording and screen-recording polish from one CLI an agent can call, and its MCP tools let the agent read what a take contains without watching it.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex, cursor |
| levers | captions, audio, motion, review-loop |
| cost | free-local |

Free and local for recording, editing, captions and export; sharing uploads to a bucket you set up (for example R2) or to Reelbird Pro at $5 a month. macOS 15 or later. Captions use Apple's on-device recogniser. The `cleanup` command has --dry-run and --undo; use them before exporting. Not run here.

## Claims

1. Its CLI and MCP server state support for Claude Code, Codex and Cursor.

   > The `reelbird` command-line tool and its MCP server let Claude Code, Codex or Cursor list screens, record a demo of the change they just made, export it and hand you the link.

   Locator: README.md, Works with agents. Source: <https://github.com/btahir/reelbird/blob/main/README.md>, retrieved 2026-11-12.

2. A cleanup command shortens pauses and cuts 'um's, with a dry run and undo.

   > shorten pauses, cut ums, trim dead ends (--dry-run, --undo)

   Locator: README.md, section Command line, reelbird cleanup. Source: <https://github.com/btahir/reelbird/blob/main/README.md>, retrieved 2026-11-12.

3. An MCP tool summarises a take's steps, speech and markers for the agent without watching the video.

   > describe a recording without watching it (`describe_take`: its steps, what was said and markers, so an agent can follow what you showed it)

   Locator: README.md, section MCP server. Source: <https://github.com/btahir/reelbird/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `bebf30241def3c73dca13ab408af9e1e2f28de42a67f4ac39fded20e4628fe81`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-13
- default_branch: main
- fetched_at: 2026-11-12
- forks: 7
- last_activity: 2026-11-10
- licence: MIT
- open_issues: 0
- sources: https://api.github.com/repos/btahir/reelbird, https://skills.sh/api/search?q=reelbird
- stars: 49

## Related

- alternative_to: [screenstudio-alt](connerkward__screenstudio-alternative-skill.md)

## Referenced by

- [screenstudio-alt](connerkward__screenstudio-alternative-skill.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
