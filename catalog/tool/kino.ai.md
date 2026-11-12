# Kino

`tool:kino.ai` - tool - <https://kino.ai>

A desktop video editor and media library (Electron) where people and Claude Code or Codex edit one shared timeline over MCP. Every edit, motion graphic and comment is stored as code on top of Remotion, and footage is indexed and proxied to Kino's cloud.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Code-driven video](../../docs/glossary.md#code-driven-video), [MCP servers](../../docs/glossary.md#mcp-servers), [Cost](../../docs/glossary.md#cost)

Also known as: Kino AI

Tags: video-editor, timeline, remotion

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It puts the reader's agent on the same timeline as teammates, with review links whose notes the agent can act on, instead of screenshots in chat.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex, any-mcp |
| levers | review-loop, orchestration, motion |
| cost | mixed |

Kino uploads low-res proxies of your footage so teammates and cloud inference can see it; check that against client contracts. The free tier caps MCP calls weekly, and the cap applies even when you bring your own Claude or Codex. Price naming differs between the vendor's pages: the 2026-11-04 launch post says 'Pro is $25 per editor per month', the pricing page FAQ names plans Editor and Editor Plus, and the plan prices did not render in the page as fetched. Re-check before buying. Being built on Remotion, Remotion's company licence question is Kino's to answer; not checked. Not installed or run here.

## Claims

1. All edits, motion graphics, timeline moves, comments and 3D scenes are stored as code built on Remotion.

   > All editing, all motion graphics, all dragging of timeline items around, all teammate comments, and all 3D scenes are expressed as code, built on Remotion.

   Locator: Launch HN post 50368804 by the founder, paragraph 3. Source: <https://news.ycombinator.com/item?id=50368804>, retrieved 2026-11-12.

2. The launch post says the full editor with MCP access is free and Pro costs $25 per editor per month.

   > The full editor is free, including unlimited imports and exports, real-time collaboration and MCP access for your own agent. Pro is $25 per editor per month

   Locator: Launch HN post 50368804, last paragraphs. Source: <https://news.ycombinator.com/item?id=50368804>, retrieved 2026-11-12.

3. Connecting your own Claude or Codex bills through that provider, and Kino's MCP limit still applies.

   > Connecting your own Claude or Codex account uses that provider’s billing, and Kino’s MCP limit still applies.

   Locator: kino.ai/pricing, Common questions, What are AI credits?. Source: <https://kino.ai/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. founder's Launch HN post (via HN Algolia API) and the visible text of kino.ai/pricing against the record
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `14ae0b2b5d2b5e0d88c9e27a3fd5ee3e43d5782a12936c834f9525905659b0ba`
- Lane: radar-2026-11-12

## Observed

Nothing collected yet.

## Related

- depends_on: [Remotion](remotion-dev__remotion.md)
- alternative_to: [Uncut](blazejkustra__uncut.md)

## Referenced by

- [Uncut](blazejkustra__uncut.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
