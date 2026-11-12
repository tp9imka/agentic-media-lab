# Runway Dev API

`tool:runwayml/runway-api` - tool - <https://docs.dev.runwayml.com/guides/pricing>

Runway's developer API, which sells Runway's own models and other vendors' video and image models (Kling, Wan, Seedance, Grok Imagine, MiniMax, Veo, Gemini, GPT Image) under one credit balance, with a hosted MCP server.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Image models](../../docs/glossary.md#image-models), [MCP servers](../../docs/glossary.md#mcp-servers), [Cost](../../docs/glossary.md#cost)

Also known as: Runway API, Runway MCP, mcp.runwayml.com, Runway Model Router

**Badge:** quoted, not read at the primary source (`quoted-secondary`): a claim is quoted via a secondary source.

**Why:** One key and one MCP connector reach most of the hosted video models in this hub, and the price table is in plain text.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | any-mcp, cursor |
| levers | gen-model-craft, orchestration |
| cost | paid |

Credits are $0.01. Runway's resale prices differ from first-party prices: wan3 1080p is 20 credits ($0.20/s), the Alibaba list price before its 30% discount; seedance2_5 1080p is 68 credits ($0.68/s) against BytePlus' worked $0.569/s. Kling 4 is listed (kling_4 720p 15.7 credits list) though Kling's own pricing page could not be read. The MCP server needs a Runway sign-in; the plugin install route was not opened. veo3.1 is still sold here although it left the Gemini API on 2026-10-22.

## Claims

1. Runway sells Wan 3.0 at 5, 10 and 20 credits per second for 480p, 720p and 1080p.

   > wan3 (480p) | 5 credits per second | wan3 (720p) | 10 credits per second | wan3 (1080p) | 20 credits per second

   Locator: API pricing page, Video Generation Pricing table. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12. Via: Runway Dev API (reseller); first-party price is on Alibaba Model Studio.

2. Seedance 2.5 at 1080p costs 68 credits per second of output on Runway, with an 80 credit minimum.

   > seedance2_5 (1080p) | 68 credits per second of output, plus 34 credits per second of input and reference video (combined video capped at 30 seconds); reference images and audio are free (80 credit minimum per generation)

   Locator: API pricing page, Video Generation Pricing table. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12. Via: Runway Dev API (reseller); first-party price is on BytePlus ModelArk.

3. Runway's hosted MCP server is at mcp.runwayml.com/mcp and works as a custom connector after a Runway sign-in.

   > To use it, add the URL above as a custom connector in claude.ai (Settings → Connectors), Cursor, or any other MCP client. You'll be prompted to sign in with your Runway account.

   Locator: mcp.runwayml.com landing page. Source: <https://mcp.runwayml.com>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Runway Dev API pricing page and mcp.runwayml.com page against all three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `73052299f920e75c5516296c46b14327fd4eee05a43d2cf31521ffe840c63f72`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- integrates_with: [Runway Gen-4.5](../model/runwayml__gen-4.5.md)
- integrates_with: [Runway Aleph 2.0](../model/runwayml__aleph.md)
- integrates_with: [Veo 3.1](../model/google__veo-3.1.md) - veo3.1 still on the Runway price list 2026-11-12

## Referenced by

- [Dreamina Seedance 2.5](../model/bytedance__seedance.md) (integrates_with)
- [Runway Aleph 2.0](../model/runwayml__aleph.md) (depends_on)
- [Runway Gen-4.5](../model/runwayml__gen-4.5.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
