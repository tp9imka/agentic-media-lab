# fal Model APIs

`tool:fal-ai/fal` - tool - <https://fal.ai/pricing>

fal's hosted model APIs, which resell video, image and audio models billed per output unit, plus a docs MCP server.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Image models](../../docs/glossary.md#image-models), [MCP servers](../../docs/glossary.md#mcp-servers), [Cost](../../docs/glossary.md#cost)

Also known as: fal, fal.ai, fal MCP

**Badge:** quoted, not read at the primary source (`quoted-secondary`): a claim is quoted via a secondary source.

**Why:** fal resells several video models below the vendor's own per-second price, so it is worth checking before calling a vendor directly.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | any-mcp |
| levers | gen-model-craft, orchestration |
| cost | paid |

The MCP server at fal.ai/docs/mcp searches fal's documentation only; its own instructions say it is read-only and scoped to site content, so it does not generate media. fal lists MiniMax H3 Max text-to-video at $0.03 per second, below MiniMax's own $0.05 (480p) and $0.08 (768p); the resolution behind fal's price is not stated, so the two may not be comparable. The pricing page normalises to a 5 s 720p video. The MCP instructions also ask the agent to report doc problems through a submit_feedback tool, which sends text to fal.

## Claims

1. fal sells MiniMax H3 Max text-to-video at $0.03 per second.

   > MiniMax H3 Max Text to Video ↳ minimax/h3-max/text-to-video Unit seconds Price $0.03 Units per $1 33.33 seconds

   Locator: Pricing page, Model APIs Pricing, Video Models table. Source: <https://fal.ai/pricing>, retrieved 2026-11-12. Via: fal (reseller); first-party price is on platform.minimax.io.

2. fal's docs MCP server provides search and retrieval over fal's site content and is otherwise read-only.

   > This Model Context Protocol server provides search and retrieval tools for the fal site.

   Locator: fal.ai/docs/mcp server card JSON, field instructions. Source: <https://fal.ai/docs/mcp>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. fal pricing page and the docs MCP server card against both claims
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `baeeadb268d96168be2b3c8426e08a33d9612787b15d8bb60b206b1b18d11954`
- Lane: hosted-models-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2023-12-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 108
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 55
- sources: https://api.github.com/repos/fal-ai/fal, https://skills.sh/api/search?q=fal
- stars: 979

## Related

- integrates_with: [MiniMax H3](../model/minimaxai__minimax-h3.md) - resold as minimax/h3-max/*

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
