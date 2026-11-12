# Pexels MCP Server

`tool:garylab/pexels-mcp-server` - tool - <https://github.com/garylab/pexels-mcp-server>

An MCP server that searches the Pexels API for photos, videos and collections, run through uvx with a Pexels API key.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: pexels-mcp-server, Pexels MCP

Tags: b-roll, stock

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Gives the agent a b-roll search that returns stock footage the Pexels licence page says can be used in ads and social posts.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | any-mcp |
| levers | asset |
| cost | free-tier |

Needs a Pexels API key, which means a Pexels account (free terms of the API not opened here: the API docs and help pages returned 403). It searches only; downloading, placing and crediting the clip are left to the agent or another tool. The licence page text saved here lists allowed uses; its restrictions section did not load, so check it before client work.

## Claims

1. It needs a Pexels API key in the server environment.

   > "PEXELS_API_KEY": "<Your Pexels API key>"

   Locator: README.md, section Usage, Using uv. Source: <https://github.com/garylab/pexels-mcp-server/blob/main/README.md>, retrieved 2026-11-12.

2. It can search Pexels videos.

   > - `videos_search` – Search videos

   Locator: README.md, section Available Tools. Source: <https://github.com/garylab/pexels-mcp-server/blob/main/README.md>, retrieved 2026-11-12.

3. The Pexels licence page lists ads and marketing campaigns among allowed uses.

   > Create unique ads, banners and marketing campaigns with photos from Pexels and promote your product.

   Locator: pexels.com/license, use-case list, Promote your product. Source: <https://www.pexels.com/license/>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and the visible text of pexels.com/license against the three claims; the licence restrictions section and API terms were not retrieved
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `0492f83c4a2b6da582106b066127582bee85ec8665ffb79fba54f135774d3f45`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-08-18
- default_branch: main
- fetched_at: 2026-11-12
- forks: 3
- last_activity: 2025-11-02
- licence: unknown
- open_issues: 2
- sources: https://api.github.com/repos/garylab/pexels-mcp-server, https://skills.sh/api/search?q=pexels-mcp-server
- stars: 30

## Related

- alternative_to: [Pixabay API documentation](../source/pixabay.com__api__docs.md)

## Referenced by

- [Pixabay API documentation](../source/pixabay.com__api__docs.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
