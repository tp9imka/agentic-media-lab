# Facebook Video API - Reels Publishing guide

`source:developers.facebook.com/docs/video-api/guides/reels-publishing` - source - <https://developers.facebook.com/docs/video-api/guides/reels-publishing>

Meta's guide to publishing Reels to a Facebook Page through the Video API: upload flow, specs, limits and the AI flag.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Delivery](../../docs/glossary.md#delivery)

Tags: facebook, rate-limit, ai-label, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Facebook Page Reels have a lower daily cap and a shorter maximum length than Instagram Reels, which matters when one render goes to both.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

Posts to a Page, not a personal profile. 30 Reels per 24 hours, 3-90 seconds, 9:16, at least 540x960, 24-60 fps; a 3-minute YouTube Short will be rejected here (error 1363128). is_ai_generated discloses AI use. The earlier scan's '30 API-published posts' wording is confirmed. Permissions and app review were not read in depth.

## Claims

1. The Reels API allows 30 API-published Reels per Page in a moving 24-hour window.

   > Reels API is limited to 30 API-published posts within a 24-hour moving period.

   Locator: Limitations, Rate Limit. Source: <https://developers.facebook.com/docs/video-api/guides/reels-publishing>, retrieved 2026-11-12.

2. A Page Reel must be 3 to 90 seconds long.

   > | Duration | 3 to 90 seconds.<br><br>A reel published as a story on a Facebook Page can not exceed 60 seconds. |

   Locator: Video Specifications table. Source: <https://developers.facebook.com/docs/video-api/guides/reels-publishing>, retrieved 2026-11-12.

3. is_ai_generated=true discloses that the Reel was made or edited with AI.

   > Set to `true` to disclose that the reel was created or edited using AI. Defaults to `false`.

   Locator: Publish parameters, is_ai_generated. Source: <https://developers.facebook.com/docs/video-api/guides/reels-publishing>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. guide served as markdown, against the claims and the earlier scan's 30-post figure
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `74a8515bbc13283f9fcc502095de29352c51ebd69d2dcb1a49a6ef6cb0f957a0`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- alternative_to: [Instagram Platform - Content Publishing (with Reels specs)](developers.facebook.com__docs__instagram-platform__content-publishing.md)

## Referenced by

- [Instagram Platform - Content Publishing (with Reels specs)](developers.facebook.com__docs__instagram-platform__content-publishing.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
