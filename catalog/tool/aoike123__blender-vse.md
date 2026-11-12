# Blender VSE Control

`tool:aoike123/blender-vse` - tool - <https://github.com/Aoike123/blender-vse>

A local MCP server, CLI and skill that inspect, patch, render and verify Blender Video Sequence Editor timelines in a named .blend file, with revision checks so human edits are not overwritten.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Agent Skills](../../docs/glossary.md#agent-skills), [Review loop](../../docs/glossary.md#review-loop)

Also known as: blender-vse-mcp, Blender VSE MCP

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A free desktop editor an agent can drive through typed operations rather than arbitrary Python, with the .blend left editable for a person.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: experimental.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | codex, any-mcp |
| levers | review-loop, delivery |
| cost | free-local |

Alpha; Blender 5.1 is the verified target. Its verify step checks saved structure only, so the agent still has to render and look at frames. The one-line install downloads a remote script into the shell and installs uv if missing; read it first or install from source. A local Codex plugin is documented; Claude Code works as a generic MCP host. Blender is free. Not run here.

## Claims

1. Final verification reopens the .blend in a fresh Blender process and checks structure, not frames.

   > final verification reopens the canonical `.blend` in a fresh Blender process and checks saved structural facts. It does not inspect frames or judge visual or creative correctness.

   Locator: README.md, section Core guarantees, Persistence evidence. Source: <https://github.com/Aoike123/blender-vse/blob/main/README.md>, retrieved 2026-11-12.

2. Callers pick operations from a catalog and cannot send free-form Python.

   > callers select operations from the catalog; they can never submit free-form Python.

   Locator: README.md, section Core guarantees, Bounded surface. Source: <https://github.com/Aoike123/blender-vse/blob/main/README.md>, retrieved 2026-11-12.

3. The quick-install script also installs uv when it is missing.

   > The script installs [uv](https://docs.astral.sh/uv/) when it is missing, then installs the `blender-vse-mcp` command on uv's managed Python 3.12 and checks for Blender.

   Locator: README.md, section Install. Source: <https://github.com/Aoike123/blender-vse/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `002d04122f1ed7c6d1d2f96bb99087f524c44272055aa07259d9fa4d9e86fc4d`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 0
- last_activity: 2026-10-27
- licence: MIT
- open_issues: 0
- sources: https://api.github.com/repos/Aoike123/blender-vse, https://skills.sh/api/search?q=blender-vse
- stars: 4

## Related

- alternative_to: [MCP for Blender](ahujasid__mcp-for-blender.md) - that server runs arbitrary Python in Blender; this one exposes a fixed operation catalog for the VSE

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
