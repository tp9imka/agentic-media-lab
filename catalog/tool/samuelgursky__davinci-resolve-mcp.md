# DaVinci Resolve MCP Server

`tool:samuelgursky/davinci-resolve-mcp` - tool - <https://github.com/samuelgursky/davinci-resolve-mcp>

An MCP server that drives a running DaVinci Resolve through its scripting API: media pool, timeline edits, markers, grading, Fusion, Fairlight and render queue. A second Node server edits .drp, .drt and .drx files with Resolve closed.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Review loop](../../docs/glossary.md#review-loop), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: davinci-resolve-mcp, Resolve MCP

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The most complete agent path into a desktop editor found in this lane, and it reports when an edit was not verified instead of calling it fine.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | claude-code, codex, cursor, any-mcp |
| levers | review-loop, audio, captions, delivery |
| cost | mixed |

Full external control needs Resolve Studio, the paid edition (price not checked here). The free edition works only through an in-app bridge script, which the README says Resolve 21.1 closed for Python; treat it as a 21.0.x path. The installer configures Claude Code, Codex CLI and Cursor among others. Output is a first-pass assembly by the README's own account, not a finished cut. The server contacts GitHub for update checks; ffmpeg and openai-whisper are optional extras for silence detection and word-level work.

## Claims

1. External scripting, which the MCP server needs, is limited to Resolve Studio; the free edition refuses an outside process.

   > Blackmagic gates *external* scripting to Studio: on the free edition `scriptapp("Resolve")` refuses a foreign process, whatever the preference says.

   Locator: README.md, section Free edition (in-app bridge). Source: <https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md>, retrieved 2026-11-12.

2. Every tool result carries a verification status, and 'unverified' means nothing was checked rather than a clean result.

   > `verification.status: "unverified"` means *no evidence was reported*, not "checked and clean".

   Locator: README.md, section Operation envelope. Source: <https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md>, retrieved 2026-11-12.

3. The installer and the server check GitHub releases for updates.

   > The installer and server check the latest GitHub release for MCP updates.

   Locator: README.md, section Quick Start. Source: <https://github.com/samuelgursky/davinci-resolve-mcp/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; install docs and api-coverage page not opened
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `7a84bb30ea6338d89845875cb9fe59a78da828c9edf5beba153e1746fd469efc`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-03-18
- default_branch: main
- fetched_at: 2026-11-12
- forks: 473
- installs: 56
- installs_by_skill: {"resolve-audio": 48, "resolve-color": 55, "resolve-delivery": 44, "resolve-edit": 47, "resolve-fusion": 46, "resolve-mcp": 56, "resolve-media-analysis": 48, "resolve-media-pool": 39, "resolve-rough-cut": 44, "resolve-session": 41}
- last_activity: 2026-11-11
- licence: MIT
- open_issues: 10
- registry: skills.sh
- sources: https://api.github.com/repos/samuelgursky/davinci-resolve-mcp, https://skills.sh/api/search?q=davinci-resolve-mcp
- stars: 4061

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
