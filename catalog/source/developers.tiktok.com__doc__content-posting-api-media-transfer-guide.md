# TikTok Content Posting API - Media Transfer Guide

`source:developers.tiktok.com/doc/content-posting-api-media-transfer-guide` - source - <https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide>

TikTok's rules for sending the file: chunked FILE_UPLOAD sizes, PULL_FROM_URL with a verified domain, and the accepted video formats, frame rates, resolution, length and size.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Delivery](../../docs/glossary.md#delivery)

Tags: tiktok, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** These are the encode targets for a clip an agent renders for TikTok, from TikTok's own API page rather than a creator blog.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Render H.264 MP4 at 23-60 fps, 360-4096 px per side, at most 4 GB. The API accepts up to 10 minutes, but the account's own cap (3, 5 or 10 minutes) applies and creator_info returns it as max_video_post_duration_sec. Chunks must be 5-64 MB, files under 5 MB go in one piece. PULL_FROM_URL needs a domain verified in the TikTok developer portal, so a laptop pipeline usually uses FILE_UPLOAD.

## Claims

1. TikTok accepts MP4, WebM or MOV in H.264, H.265, VP8 or VP9, at 23 to 60 fps.

   > Framerate restrictions Minimum of 23 FPS Maximum of 60 FPS

   Locator: Video restrictions, Framerate restrictions. Source: <https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide>, retrieved 2026-11-12.

2. The API takes videos up to 10 minutes; the creator's own maximum may be shorter and TikTok users may trim.

   > The longest video a developer can send via the initialize Upload Video endpoint is 10 minutes. TikTok users may trim developer-sent videos inside the TikTok app to fit their accounts' actual maximum publish durations.

   Locator: Video restrictions, Duration restrictions. Source: <https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide>, retrieved 2026-11-12.

3. Upload chunks must be between 5 MB and 64 MB, and the final chunk may be up to 128 MB.

   > Each chunk must be at least 5 MB but no greater than 64 MB, except for the final chunk, which can be greater than chunk_size (up to 128 MB) to accommodate any trailing bytes.

   Locator: File upload, chunk restrictions. Source: <https://developers.tiktok.com/doc/content-posting-api-media-transfer-guide>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. visible guide text, Video restrictions and chunk rules, against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `aec1d1c8efddd2a158489acfef49404e71b2156ce863e7cc51d1c8673cc8f603`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- integrates_with: [TikTok Content Posting API - Direct Post reference](developers.tiktok.com__doc__content-posting-api-reference-direct-post.md)

## Referenced by

- [TikTok Content Posting API - Direct Post reference](developers.tiktok.com__doc__content-posting-api-reference-direct-post.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
