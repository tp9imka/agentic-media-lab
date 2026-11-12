# Instagram Platform - Content Publishing (with Reels specs)

`source:developers.facebook.com/docs/instagram-platform/content-publishing` - source - <https://developers.facebook.com/docs/instagram-platform/content-publishing>

Meta's guide to publishing images, videos, Reels and carousels to an Instagram professional account, read with the IG User media reference that holds the Reels specs.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Delivery](../../docs/glossary.md#delivery)

Tags: instagram, rate-limit, ai-label, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives the daily limit, the AI self-disclosure flag and the Reels encode targets for Instagram.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Needs an Instagram professional (Business or Creator) account and the instagram_content_publish or instagram_business_content_publish permission; the page lists Standard and Advanced Access, and app review for Advanced Access was not read here. The guide states two different limits: 100 API posts per 24 hours in Rate Limit and 50 published posts per 24 hours in the carousel section. Plan for 50 until Meta resolves it. Reels: H.264 or HEVC, 23-60 fps, 3 s to 15 min, 300 MB, 9:16 recommended. The docs URL redirects to developers.facebook.com/documentation/...

## Claims

1. The guide's Rate Limit section allows 100 API-published posts per account in a moving 24-hour window; its carousel section says 50 per 24 hours.

   > Instagram accounts are limited to 100 API-published posts within a 24-hour moving period.

   Locator: Limitations, Rate Limit. Source: <https://developers.facebook.com/docs/instagram-platform/content-publishing>, retrieved 2026-11-12.

2. is_ai_generated=true on the media container is the AI self-disclosure, for both Instagram login routes; on a carousel set it only on the parent.

   > For carousels, only the carousel container needs to have the `is_ai_generated` parameter set to `true`. Setting this parameter on carousel children will result in an error. This parameter is available to both Instagram API with Facebook Login and Instagram Login.

   Locator: AI Content. Source: <https://developers.facebook.com/docs/instagram-platform/content-publishing>, retrieved 2026-11-12.

3. Reels may run from 3 seconds to 15 minutes and up to 300 MB.

   > - Duration: 15 mins maximum, 3 seconds minimum

   Locator: IG User media reference, Reel Specifications. Source: <https://developers.facebook.com/docs/instagram-platform/instagram-graph-api/reference/ig-user/media>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `204de9647c4f896d78f6602830efd45fa9a61b96f65d89793e06ec0b7f18197f`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- alternative_to: [Facebook Video API - Reels Publishing guide](developers.facebook.com__docs__video-api__guides__reels-publishing.md)
- alternative_to: [Threads API - Posts](developers.facebook.com__docs__threads__posts.md)

## Referenced by

- [Threads API - Posts](developers.facebook.com__docs__threads__posts.md) (alternative_to)
- [Facebook Video API - Reels Publishing guide](developers.facebook.com__docs__video-api__guides__reels-publishing.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
