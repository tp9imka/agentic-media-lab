# MCP for Blender

`tool:ahujasid/mcp-for-blender` - tool - <https://github.com/ahujasid/mcp-for-blender>

A third-party MCP server and Blender add-on that lets an agent run Python in a live Blender, look at viewport, camera and animation-strip views, and render. Blender itself renders headless with `blender -b file.blend -a`.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [MCP servers](../../docs/glossary.md#mcp-servers), [Review loop](../../docs/glossary.md#review-loop), [Popularity and trust](../../docs/glossary.md#popularity-and-trust)

Also known as: blender-mcp, mcp-for-blender, ahujasid/blender-mcp

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The working path for 3D shots driven by an agent, with a built-in way for the agent to see its own frames.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | claude-code, codex, cursor, any-mcp |
| levers | asset, review-loop, motion |
| cost | mixed |

The server runs any Python the agent writes inside Blender by default; set BLENDER_MCP_SAFE_MODE=1 and save your .blend first. The quick start pipes a remote script to sh; the manual setup avoids that. Some 3D-generation features are premium or need Sketchfab or Hyper3D keys. For the final video, the agent can call Blender's own CLI (`blender -b file.blend -a`, with -f N for one frame); put -o and format flags before -a.

## Claims

1. Its tool for running code executes arbitrary Python in Blender, and the README tells you to save your work first.

   > The `execute_blender_code` tool allows running arbitrary Python code in Blender, which can be powerful but potentially dangerous.

   Locator: README.md, Limitations & Security Considerations. Source: <https://github.com/ahujasid/mcp-for-blender/blob/main/README.md>, retrieved 2026-11-12.

2. A look tool returns viewport, camera, multi-angle or animation-strip views so the agent can check a frame.

   > See the result from the `viewport`, `camera`, `angles` (auto-framed multi-view sheet, any direction) or `frames` (animation strip)

   Locator: README.md, tools table, look. Source: <https://github.com/ahujasid/mcp-for-blender/blob/main/README.md>, retrieved 2026-11-12.

3. Blender's CLI renders without the UI, and argument order matters: -f or -a must come last.

   > Always position -f or -a as the last arguments.

   Locator: docs.blender.org, Rendering From The Command Line. Source: <https://docs.blender.org/manual/en/latest/advanced/command_line/render.html>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `3b99ca9b7295f88ca255a51a9245695f2e3812de1873cdc04a3a0583ea116588`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-03-07
- default_branch: main
- fetched_at: 2026-11-12
- forks: 3107
- last_activity: 2026-11-04
- licence: MIT
- open_issues: 58
- sources: https://api.github.com/repos/ahujasid/mcp-for-blender, https://skills.sh/api/search?q=mcp-for-blender
- stars: 34103

## Related

None.

## Referenced by

- [Blender VSE Control](aoike123__blender-vse.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
