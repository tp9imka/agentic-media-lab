# MCP Bridge for Adobe Premiere Pro

`tool:hetpatel-11/adobe_premiere_pro_mcp` - tool - <https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP>

A local MCP server plus a CEP panel inside Premiere Pro that exposes timeline, effects, captions, markers, audio and export operations. Ships as a Codex plugin, a Claude Code plugin and an Agent Skill.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Plugins](../../docs/glossary.md#plugins), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: adobe-premiere-pro-mcp, premiere-pro-mcp, Premiere MCP

Tags: telemetry

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The path for a reader who already finishes in Premiere and wants the agent to assemble and razor inside the real project.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | claude-code, codex, any-mcp |
| levers | captions, audio, delivery |
| cost | paid |

Premiere Pro is a paid Adobe subscription, so this is not a no-cost path. The CEP install turns on Adobe's CEP debug setting. Anonymous telemetry is on by default: set PREMIERE_MCP_TELEMETRY=0 in the server entry. Its read-only check confirms the bridge, not the edit; the agent still has to export and look at the result.

## Claims

1. It exposes 283 Premiere tools through a search-then-invoke pattern to Codex, Claude Code and other MCP clients.

   > 283 Premiere tools behind `search_tools` / `invoke_tool`, 13 context resources, and 10 guided prompts for Codex, Claude Code, Claude Desktop, and other MCP clients.

   Locator: README.md, header. Source: <https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP/blob/main/README.md>, retrieved 2026-11-12.

2. Its session check confirms the bridge and reads the open project and active sequence without changing anything.

   > It confirms that the CEP bridge responded and returns the Premiere build, open project, and active sequence without modifying the project.

   Locator: README.md, section What You Get. Source: <https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP/blob/main/README.md>, retrieved 2026-11-12.

3. Anonymous usage telemetry is on by default.

   > Anonymous usage telemetry is on by default so we can see how many people run the server and when a tool fails.

   Locator: README.md, section Telemetry. Source: <https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; QUICKSTART.md and the bundled skill not opened
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `aaddd15fee9ce29d091e9aa3774d6c2594b28dc719b6a32537f57410bb1b2e90`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-07-07
- default_branch: main
- fetched_at: 2026-11-12
- forks: 158
- installs: 1001
- installs_by_skill: {"edit-premiere-project": 40, "premiere-pro-mcp": 1001}
- last_activity: 2026-11-02
- licence: MIT
- open_issues: 24
- registry: skills.sh
- sources: https://api.github.com/repos/hetpatel-11/Adobe_Premiere_Pro_MCP, https://skills.sh/api/search?q=Adobe_Premiere_Pro_MCP
- stars: 857

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
