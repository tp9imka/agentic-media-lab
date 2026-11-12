# X API - chunked media upload quickstart

`source:docs.x.com/x-api/media/quickstart/media-upload-chunked` - source - <https://docs.x.com/x-api/media/quickstart/media-upload-chunked>

X's guide to uploading video in chunks with the v2 media endpoints, with the size and duration caps per media category.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Delivery](../../docs/glossary.md#delivery)

Tags: x, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives the video caps for a post on X and says they depend on the posting account's Premium status.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

tweet_video: 20 minutes and 8 GB by default, 125 minutes and 16 GB for Premium. Chunks at most 5 MB (server max 8 MB). Limits are checked again at post time, so an upload can succeed and the post still fail with 403. Codec and resolution rules are on a linked page, not read here.

## Claims

1. A regular post's video may be 20 minutes and 8 GB, or 125 minutes and 16 GB for Premium.

   > 20 min / 8 GB · Premium: 125 min / 16 GB

   Locator: Media categories table, tweet_video. Source: <https://docs.x.com/x-api/media/quickstart/media-upload-chunked>, retrieved 2026-11-12.

2. A successful upload can still be rejected when attached to a post.

   > A successful upload can still be rejected when you attach the media_id to POST /2/tweets.

   Locator: Initialize step, note. Source: <https://docs.x.com/x-api/media/quickstart/media-upload-chunked>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. visible quickstart text against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `925bc5de8d3a12ee936d7b235a8ac256b8e5a5a3932042b9f44adaf9223d1f9d`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- integrates_with: [X API pay-per-usage pricing](docs.x.com__x-api__getting-started__pricing.md)

## Referenced by

- [X API pay-per-usage pricing](docs.x.com__x-api__getting-started__pricing.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
