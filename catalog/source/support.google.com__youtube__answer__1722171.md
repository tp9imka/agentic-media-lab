# YouTube recommended upload encoding settings

`source:support.google.com/youtube/answer/1722171` - source - <https://support.google.com/youtube/answer/1722171>

YouTube Help's upload spec: MP4 container with fast start, H.264 High profile with closed GOP, AAC-LC or Opus audio at 48 kHz, and recommended bitrates. A linked page defines when an upload counts as a Short.

Concepts: [Delivery](../../docs/glossary.md#delivery)

Tags: export, h264, shorts

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Each line maps to an ffmpeg flag, so an agent can check its export against YouTube's own list before upload.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intro. Maturity: -.

ffmpeg mapping: -movflags +faststart, -c:v libx264 -profile:v high -pix_fmt yuv420p -bf 2 -g <fps/2>, -c:a aac -ar 48000. The page also asks for no edit lists, which Meta's Reels spec repeats. The 1080p SDR recommendation is 8 Mbps at 24-30 fps. Upload limits change; recheck within 30 days.

## Claims

1. Put the moov atom at the front of the file (fast start).

   > moov atom at the front of the file (Fast Start)

   Locator: answer 1722171, section Container: MP4. Source: <https://support.google.com/youtube/answer/1722171>, retrieved 2026-11-12.

2. Use a closed GOP of half the frame rate.

   > Closed GOP. GOP of half the frame rate.

   Locator: answer 1722171, section Video codec: H.264. Source: <https://support.google.com/youtube/answer/1722171>, retrieved 2026-11-12.

3. Square or vertical uploads up to three minutes are classed as Shorts.

   > Any videos uploaded on or after this date with a square or vertical aspect ratio up to three minutes in length will be categorized as Shorts on YouTube.

   Locator: answer 15424877, Understand three-minute YouTube Shorts. Source: <https://support.google.com/youtube/answer/15424877>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. answer 1722171 and answer 15424877 against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `63661d637980bf6e63d699ba76b531d9da0f8562d3420d553f7f67dfd1193c36`
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [Meta Ads Guide - Instagram Reels video ads](facebook.com__business__ads-guide__update__video__instagram-reels.md)

## Referenced by

- [Meta Ads Guide - Instagram Reels video ads](facebook.com__business__ads-guide__update__video__instagram-reels.md) (alternative_to)
- [YouTube Help - Add video thumbnails](support.google.com__youtube__answer__72431.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
