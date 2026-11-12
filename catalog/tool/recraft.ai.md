# Recraft API and MCP server

`tool:recraft.ai` - tool - <https://www.recraft.ai/docs/api-reference/pricing>

A hosted image API with raster and vector (SVG) output, editing tools and a hosted MCP server at mcp.recraft.ai with OAuth.

Concepts: [Image models](../../docs/glossary.md#image-models), [MCP servers](../../docs/glossary.md#mcp-servers), [Cost](../../docs/glossary.md#cost)

Also known as: Recraft, Recraft V4.1, mcp.recraft.ai

Tags: image-generation, vector, svg, pricing

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Vector output means an illustration or icon for an explainer scales to any resolution and can be animated in code, which raster models cannot give.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | claude-code, any-mcp |
| levers | asset, design |
| cost | mixed |

Two separate balances: the API is prepaid units ($1 = 1,000), while the MCP server spends the Studio subscription credits. Free-plan images are public, owned by Recraft and not licensed for commercial use, so the MCP route on a free plan is unfit for client work. Assets may not be used to train AI models on any plan. On Claude Code on the web, img.recraft.ai must be allowlisted to download results. The pricing page was read; per-credit rates of the Studio plan were not.

## Claims

1. V4.1 costs $0.035 per raster image and $0.08 per vector image through the API; V4.1 Flash is $0.007 raster only.

   > | [V4.1](https://www.recraft.ai/docs/api-reference/models/recraft-v4-1.md) and V4.1 Utility | \$0.035 | \$0.08 | \$0.21 | \$0.30 |

   Locator: API reference, Pricing, model table (Raster, Vector, Pro raster, Pro vector). Source: <https://www.recraft.ai/docs/api-reference/pricing>, retrieved 2026-11-12.

2. Free-plan images are public, stay Recraft's property and are not licensed for commercial use; paid-plan images carry full commercial rights.

   > Images generated under the **Free plan** are publicly visible in the community gallery and remain the property of Recraft. These images are not licensed for commercial use.

   Locator: Plans and billing, Commercial rights and ownership. Source: <https://www.recraft.ai/docs/plans-and-billing/commercial-rights-and-ownership>, retrieved 2026-11-12.

3. The MCP server draws on subscription credits, not on API units.

   > The MCP server consumes **subscription credits** from your Recraft plan — the same balance used by the Recraft Studio app.

   Locator: MCP reference, MCP server, Billing. Source: <https://www.recraft.ai/docs/mcp-reference/remote-server>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Recraft API pricing page (markdown), Commercial rights and ownership page and MCP server page against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `d61ebbdd96ea1768fb1a9b515750565de256b3ee987805c8f00f5c8a58bf2011`
- Lane: media-stages

## Observed

Nothing collected yet.

## Related

- alternative_to: [Nano Banana (Gemini image models)](../model/google__nano-banana.md)
- alternative_to: [GPT Image 2](../model/openai__gpt-image.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
