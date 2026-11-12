# Mastodon docs - Posting (attachments) and Instance media configuration

`source:docs.joinmastodon.org/user/posting` - source - <https://docs.joinmastodon.org/user/posting/>

Mastodon's user documentation on attachment limits, read with the Instance entity that exposes each server's real limits.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Delivery](../../docs/glossary.md#delivery)

Tags: mastodon, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Mastodon limits are set per server, so an agent should read them from the instance instead of hard-coding them.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: low. Level: intermediate. Maturity: -.

Default: one video per post, up to 99 MB, transcoded to H.264 at max 1300 kbps, so a render above that bitrate will be re-encoded lower. Read configuration.media_attachments.video_size_limit from GET /api/v2/instance for the server you post to. No app review; a token from your own account works. Rate limits were not read.

## Claims

1. By default a Mastodon post takes one video up to 99 MB, transcoded to H.264 MP4 at up to 1300 kbps.

   > Videos (MP4, M4V, MOV, WebM) up to 99MB. Video will be transcoded to H.264 MP4 with a maximum bitrate of 1300kbps and framerate of 120fps. Only one video can be attached, per post.

   Locator: Posting to your profile, Attachments. Source: <https://docs.joinmastodon.org/user/posting/>, retrieved 2026-11-12.

2. Each server reports its own video size limit in the instance configuration.

   > Description: The maximum size of any uploaded video, in bytes.

   Locator: Instance entity, configuration[media_attachments][video_size_limit]. Source: <https://docs.joinmastodon.org/entities/Instance/>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `09b96ebe76f6c02a9dcf9381187d1f0c7e282db0342252be1cbe170c5cd906dd`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
