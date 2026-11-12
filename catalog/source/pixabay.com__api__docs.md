# Pixabay API documentation

`source:pixabay.com/api/docs` - source - <https://pixabay.com/api/docs/>

Pixabay's API documentation for searching images and videos under the Pixabay Content License, with its attribution, caching, rate-limit and hotlinking rules.

Concepts: [Licences and territory](../../docs/glossary.md#licences-and-territory), [Editing real footage](../../docs/glossary.md#footage-editing)

Tags: b-roll, stock

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An agent pulling b-roll from Pixabay has to follow these rules, and one of them restricts automated querying.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Free with an API key, 100 requests per 60 seconds by default. The rule that the API is for real human requests and bans systematic mass downloads sits uneasily with an agent fetching b-roll on its own: keep queries few, cache for 24 hours, download the clips you use, and show the source. The Content License page itself returned a challenge page and was not read, so reuse terms for the clips are not quoted here.

## Claims

1. Pixabay asks API users to show where images and videos come from whenever search results are displayed.

   > If you make use of the API, show your users where the images and videos are from, whenever search results are displayed.

   Locator: Pixabay API, introduction. Source: <https://pixabay.com/api/docs/>, retrieved 2026-11-12.

2. Requests must be cached for 24 hours, automated mass querying is discouraged and systematic mass downloads are not allowed.

   > To keep the Pixabay API fast for everyone, requests must be cached for 24 hours. Also, the API is made for real human requests; do not send lots of automated queries. Systematic mass downloads are not allowed.

   Locator: section Rate Limit. Source: <https://pixabay.com/api/docs/>, retrieved 2026-11-12.

3. Permanent hotlinking of returned image URLs is not allowed.

   > However, permanent hotlinking of images (using Pixabay URLs in your app) is not allowed.

   Locator: section Hotlinking. Source: <https://pixabay.com/api/docs/>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `75eeeb0a5ebc254a5dd84e939358b88155494a71ba2e2b9c196caaf2e046419d`
- Lane: footage-editing

## Observed

Nothing collected yet.

## Related

- alternative_to: [Pexels MCP Server](../tool/garylab__pexels-mcp-server.md)

## Referenced by

- [Pexels MCP Server](../tool/garylab__pexels-mcp-server.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
