# Uncut

`tool:blazejkustra/uncut` - tool - <https://github.com/blazejkustra/uncut>

A macOS video editor for Apple Silicon that runs the user's installed Claude Code or Codex as the editing agent on a real multi-track timeline, with a separate critic that reviews rendered frames. It also exposes its tools to an outside agent over a local MCP server.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Review loop](../../docs/glossary.md#review-loop), [MCP servers](../../docs/glossary.md#mcp-servers)

Tags: video-editor, timeline, macos

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is a way to edit real footage with the reader's own agent and keep a timeline they can cut by hand, export to Final Cut or Resolve, and lock against the agent.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex, any-mcp |
| levers | review-loop, captions, audio, delivery |
| cost | mixed |

Runs on the reader's machine class (Apple Silicon, macOS 13+). Agent usage is billed through your own Claude or OpenAI plan; generators (GPT Image, Veo, ElevenLabs) need your own keys. If you edit with Codex, the critic still needs Claude Code installed. The comparison lines about Palmier and video-use are the author's own. The outside-agent MCP server is off by default and binds to 127.0.0.1 with a token. Not installed or run here.

## Claims

1. Uncut runs the user's installed Claude Code or Codex, which edits on a real timeline.

   > An AI-first video editor for macOS: it runs your installed Claude Code or Codex, which edits with you on a real timeline.

   Locator: README, first line. Source: <https://github.com/blazejkustra/uncut>, retrieved 2026-11-12.

2. Reviews use an independent critic that runs through Claude Code, so it must be installed even when editing with Codex.

   > The independent critic runs through Claude Code, so reviews need it installed even when you edit with Codex.

   Locator: README, Download, first bullet. Source: <https://github.com/blazejkustra/uncut>, retrieved 2026-11-12.

3. Locked clips, ranges or tracks cannot be changed, moved or unlocked by the agent.

   > Lock a clip, a range or a track and the agent can't change, move or unlock it.

   Locator: README, What it does, Locked cuts. Source: <https://github.com/blazejkustra/uncut>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README (raw) against the record
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `208f90a0295639b59bd43466625bba326deef18c8f92d95ebe2e778ed7d37527`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1
- last_activity: 2026-11-09
- licence: MIT
- open_issues: 2
- sources: https://api.github.com/repos/blazejkustra/uncut, https://skills.sh/api/search?q=uncut
- stars: 20

## Related

- alternative_to: [video-use](browser-use__video-use.md) - The README says video-use returns a finished file with no timeline.
- alternative_to: [Kino](kino.ai.md) - Both put a coding agent on a shared timeline; Kino is cloud-backed and built on Remotion.

## Referenced by

- [Kino](kino.ai.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
