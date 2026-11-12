# Replicate API and MCP server

`tool:replicate/replicate` - tool - <https://replicate.com/docs/reference/mcp>

Replicate's model hosting API, with a remote MCP server and an npm package that expose its whole HTTP API to an agent: search models, run predictions, fetch results.

Concepts: [MCP servers](../../docs/glossary.md#mcp-servers), [Hosted video models](../../docs/glossary.md#hosted-video-models), [Image models](../../docs/glossary.md#image-models)

Also known as: Replicate, replicate-mcp, mcp.replicate.com

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An agent in Claude Code can search Replicate's catalogue and run a model by name without hand-written client code.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | claude-code, cursor, any-mcp |
| levers | orchestration, gen-model-craft |
| cost | paid |

The remote server asks for a Replicate API key in a web sign-in flow; the local route runs npx -y replicate-mcp, which downloads and runs the package each time. Not run here. Replicate's per-model prices were not read in this lane, so no price is recorded. The page also links agent skills and an llms.txt, not opened.

## Claims

1. The MCP server supports all operations in Replicate's HTTP API, including running models.

   > The server supports all of the operations in Replicate’s HTTP API.

   Locator: MCP server reference page, section Replicate's MCP server. Source: <https://replicate.com/docs/reference/mcp>, retrieved 2026-11-12.

2. The remote server is recommended and takes a Replicate API key through a web authentication flow.

   > After installing the server, you’ll be directed to a web-based authentication flow where you can provide a Replicate API key for the server to use on your behalf.

   Locator: MCP server reference page, section Remote vs local servers. Source: <https://replicate.com/docs/reference/mcp>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Replicate MCP reference page against both claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `385439e2b4a90e977e5033d0ea3518ece8f0a41a3a8e2bbc1874486273d1031b`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
