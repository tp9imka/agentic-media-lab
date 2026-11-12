# TikTok Content Sharing Guidelines (Direct Post API)

`source:developers.tiktok.com/doc/content-sharing-guidelines` - source - <https://developers.tiktok.com/doc/content-sharing-guidelines>

TikTok's developer rules for the Content Posting API's Direct Post: what an unaudited client may do, the daily caps, the audit's intended-use test and the UX a posting app must show.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Automation](../../docs/glossary.md#automation)

Also known as: TikTok Direct Post guidelines, TikTok audit

Tags: tiktok, audit, rate-limit

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** This page decides whether a one-person pipeline can publish to TikTok publicly at all. Without an audit every post is private, and the audit does not accept a tool for your own accounts.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

For one developer posting to their own account this is a dead end for public posts: unaudited clients post SELF_ONLY, and the audit's 'Not acceptable' list names a utility tool for accounts you or your team manage. Posts can be made public later by hand in the app. Self-hosted schedulers (Postiz, Mixpost Pro) need their own TikTok app and hit the same wall; a hosted scheduler with an audited app is the remaining official route, not checked here. Unaudited clients are also limited to 5 posting users per 24 hours. The page bans watermarks or promo text on shared content. Page last updated August 4, 2026.

## Claims

1. Without an audit, every Direct Post upload is private-only; an audit lifts it.

   > As a developer, you can use this API in an unverified status, but all content uploaded via this endpoint will be restricted to private viewing mode. To lift this restriction, your API client must undergo an audit to verify compliance with our Terms of Service.

   Locator: Direct Post API - Developer Guidelines, first paragraph. Source: <https://developers.tiktok.com/doc/content-sharing-guidelines>, retrieved 2026-11-12.

2. The guidelines list a utility tool that uploads to accounts you or your team manage as not acceptable; clients must serve a wide audience, not private use.

   > Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages. ❌

   Locator: Intended Use, item 2. Source: <https://developers.tiktok.com/doc/content-sharing-guidelines>, retrieved 2026-11-12.

3. Each creator account has a cap of about 15 Direct Posts a day, shared across every app that posts for it.

   > The upper limit may vary among creators (typically around 15 posts per day/ creator account) and is shared across all API Clients using Direct Post.

   Locator: Direct Post API - Developer Guidelines, Posting cap. Source: <https://developers.tiktok.com/doc/content-sharing-guidelines>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `d8e4021ae965c417a1911395ba50e46901cfc3bfea1c5580437235c5595c073c`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- integrates_with: [TikTok Content Posting API - Direct Post reference](developers.tiktok.com__doc__content-posting-api-reference-direct-post.md)
- integrates_with: [Postiz](../tool/gitroomhq__postiz-app.md) - A self-hosted Postiz needs its own TikTok app, which this audit rule leaves private-only for own-account use.

## Referenced by

- [TikTok Content Posting API - Direct Post reference](developers.tiktok.com__doc__content-posting-api-reference-direct-post.md) (depends_on)
- [Postiz](../tool/gitroomhq__postiz-app.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
