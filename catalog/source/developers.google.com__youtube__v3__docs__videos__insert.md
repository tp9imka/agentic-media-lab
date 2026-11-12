# YouTube Data API - videos.insert and quota costs

`source:developers.google.com/youtube/v3/docs/videos/insert` - source - <https://developers.google.com/youtube/v3/docs/videos/insert>

The reference for uploading a video through the YouTube Data API, read together with the quota cost page.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Automation](../../docs/glossary.md#automation)

Tags: youtube, quota, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives the default daily upload quota and file limits a scheduled pipeline has to plan around.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

By default, uploads have their own bucket of 100 calls per day per project, separate from the 10,000 units for other calls; this replaces the 1,600-units-per-upload figure many guides still quote. Quotas reset at midnight Pacific Time. Files up to 256 GB, any video/* type. Needs a Google Cloud project and OAuth consent for your own channel; no cost stated. Both pages redirect to developers.google.com/youtube/data/...

## Claims

1. By default, videos.insert has its own bucket of 100 calls per day, 1 unit each.

   > Quota impact: 100 calls per day. A call to this method has a quota cost of 1 unit in the Video Uploads quota bucket.

   Locator: videos.insert, Quota impact. Source: <https://developers.google.com/youtube/v3/docs/videos/insert>, retrieved 2026-11-12.

2. By default, a project gets 100 search.list calls, 100 videos.insert calls and 10,000 units for all other endpoints per day.

   > Projects that enable the YouTube Data API have a default quota allocation of 100 search.list calls, 100 videos.insert calls, and 10,000 units per day combined for all other endpoints.

   Locator: Quota cost page, introduction. Source: <https://developers.google.com/youtube/v3/determine_quota_cost>, retrieved 2026-11-12.

3. Uploads may be up to 256 GB of any video MIME type.

   > Maximum file size: 256GB Accepted Media MIME types: video/*, application/octet-stream

   Locator: videos.insert, Request, Upload. Source: <https://developers.google.com/youtube/v3/docs/videos/insert>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `849264d086a81c4c226d6deb914f096c8685d10a4bb7df39a5cd145c8f53fbbf`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- integrates_with: [YouTube Data API (v3) revision history](developers.google.com__youtube__v3__revision_history.md)

## Referenced by

- [YouTube Data API (v3) revision history](developers.google.com__youtube__v3__revision_history.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
