# Postiz

`tool:gitroomhq/postiz-app` - tool - <https://github.com/gitroomhq/postiz-app>

An open-source social media scheduler with a hosted cloud edition. The self-hosted edition posts through developer apps you register on each platform, and offers a public API, MCP and CLI.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: postiz-app, gitroomhq/postiz-app

Tags: scheduler, self-hosted, mcp

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the self-hostable scheduler an agent can drive over MCP or its API, so one render can be queued to several platforms.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | none-stated |
| levers | publishing |
| cost | mixed |

Self-hosting means your own app per platform: YouTube now publishes publicly without an audit, but TikTok leaves an own-account app private-only (see the TikTok guidelines record). The README states AGPL-3.0 for the self-hosted edition. The README's sponsor table advertises residential proxy IPs 'for social media'; that is a sponsor, not a Postiz feature, and proxy rotation is out of this hub's scope. The supported-platform list is drawn as images in the README and was not read. Not run here.

## Claims

1. The self-hosted edition requires creating your own developer app on each platform and passing its approval.

   > You create your own developer apps on each platform and go through their approval (Meta, YouTube, TikTok can take weeks)

   Locator: README, Postiz Cloud vs. Open-source table, Social platform apps. Source: <https://github.com/gitroomhq/postiz-app>, retrieved 2026-11-12.

2. The self-hosted edition is free under AGPL-3.0; you pay for your own infrastructure.

   > Free forever (AGPL-3.0); you pay only for your own infra

   Locator: README, Postiz Cloud vs. Open-source table, Cost. Source: <https://github.com/gitroomhq/postiz-app>, retrieved 2026-11-12.

3. It exposes MCP, CLI and agent connectors on a self-hosted instance.

   > Included, you point the MCP / CLI at your own instance

   Locator: README, Postiz Cloud vs. Open-source table, Agentic surfaces. Source: <https://github.com/gitroomhq/postiz-app>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. GitHub README visible text against the claims
- Next check due: 2027-02-10
- Licence: AGPL-3.0
- URL status: live
- Saved source sha256: `e4830dfc8177daee415b33b804f2b57ce885add85c72c07952055cb31cdc5219`
- Lane: publishing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2023-07-08
- default_branch: main
- fetched_at: 2026-11-12
- forks: 7900
- last_activity: 2026-11-12
- licence: AGPL-3.0
- open_issues: 209
- sources: https://api.github.com/repos/gitroomhq/postiz-app, https://skills.sh/api/search?q=postiz-app
- stars: 41418

## Related

- depends_on: [TikTok Content Sharing Guidelines (Direct Post API)](../source/developers.tiktok.com__doc__content-sharing-guidelines.md) - TikTok audit rules apply to the app you register.
- depends_on: [YouTube Data API (v3) revision history](../source/developers.google.com__youtube__v3__revision_history.md)
- alternative_to: [Mixpost](inovector__mixpost.md)

## Referenced by

- [TikTok Content Sharing Guidelines (Direct Post API)](../source/developers.tiktok.com__doc__content-sharing-guidelines.md) (integrates_with)
- [Mixpost](inovector__mixpost.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
