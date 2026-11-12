# TikTok Content Posting API - Direct Post reference

`source:developers.tiktok.com/doc/content-posting-api-reference-direct-post` - source - <https://developers.tiktok.com/doc/content-posting-api-reference-direct-post>

The request and response reference for TikTok's /v2/post/publish/video/init/ endpoint: post_info fields, source types, error codes and the per-token rate limit.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules)

Tags: tiktok, ai-label, rate-limit

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It holds the AI-label flag an agent should set on generated video and the error an unaudited client gets when the account is public.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Set post_info.is_aigc=true on generated clips; the page says it adds the 'Creator labeled as AI-generated' tag. The error unaudited_client_can_only_post_to_private_accounts means an unaudited client also needs the account itself set to private, not only the post. 6 init requests per minute per user token is not a constraint at 15 posts a day, but a retry loop can hit it. Rate limits for other endpoints are on a separate page (600 per minute for user/info, video/list), not made a record.

## Claims

1. Setting is_aigc marks the post with TikTok's creator AI-generated label.

   > Set to true if the video is AI generated content. If set, the video will be labelled with Creator labeled as AI-generated tag in video's description.

   Locator: Request body, post_info.is_aigc. Source: <https://developers.tiktok.com/doc/content-posting-api-reference-direct-post>, retrieved 2026-11-12.

2. An unaudited client is blocked at init when the target account is not private.

   > Unaudited clients can only post to a private account. The publish attempt will be blocked when calling /publish/video/init/.

   Locator: Error codes, unaudited_client_can_only_post_to_private_accounts. Source: <https://developers.tiktok.com/doc/content-posting-api-reference-direct-post>, retrieved 2026-11-12.

3. The init endpoint allows 6 requests per minute per user access token.

   > Note: Each user access_token is limited to 6 requests per minute.

   Locator: Direct Post, Rate limit note. Source: <https://developers.tiktok.com/doc/content-posting-api-reference-direct-post>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `93f286d53c8282b6543dbc761bcafa7ff546b6cf0ebfb0e7ca72e3853ff02bc0`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- depends_on: [TikTok Content Sharing Guidelines (Direct Post API)](developers.tiktok.com__doc__content-sharing-guidelines.md)
- integrates_with: [TikTok Content Posting API - Media Transfer Guide](developers.tiktok.com__doc__content-posting-api-media-transfer-guide.md)

## Referenced by

- [TikTok Content Posting API - Media Transfer Guide](developers.tiktok.com__doc__content-posting-api-media-transfer-guide.md) (integrates_with)
- [TikTok Content Sharing Guidelines (Direct Post API)](developers.tiktok.com__doc__content-sharing-guidelines.md) (integrates_with)
- [TikTok Community Guidelines - Integrity and Authenticity (Edited Media and AIGC)](www.tiktok.com__community-guidelines__en__integrity-authenticity.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
