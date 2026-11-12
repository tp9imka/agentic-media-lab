# Threads API - Posts

`source:developers.facebook.com/docs/threads/posts` - source - <https://developers.facebook.com/docs/threads/posts>

Meta's guide to creating text, image, video and carousel posts through the Threads API, with limits and the AI-label parameter.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules)

Tags: threads, rate-limit, ai-label

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Threads has the highest daily cap of the Meta surfaces and a 5-minute video limit, and its AI flag is documented with what it does not prevent.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

250 posts per 24 hours per profile. Video up to 5 minutes, 23-60 fps, 100 Mbps VBR max. is_made_with_ai goes on the container create call, not on publish. Meta recommends waiting about 30 seconds before publishing a container. App review was not read here.

## Claims

1. A Threads profile may publish 250 posts per 24 hours.

   > **Note:** Profiles are limited to 250 published posts within a 24-hour period. Publishing a carousel counts as a single post.

   Locator: Carousel posts, step 3 note. Source: <https://developers.facebook.com/docs/threads/posts>, retrieved 2026-11-12.

2. is_made_with_ai=true shows the AI info label; leaving it false does not stop Meta's automatic labelling.

   > This parameter supports text, image, video, and carousel posts. It defaults to `false`. Omitting it or setting it to `false` does not add an AI self-disclosure and does not prevent automatic AI labeling.

   Locator: Label AI-Generated Content. Source: <https://developers.facebook.com/docs/threads/posts>, retrieved 2026-11-12.

3. Threads video may be up to 5 minutes.

   > * **Duration:** 300 seconds (5 minutes) maximum, minimum longer than 0 seconds.

   Locator: Media specifications, Video. Source: <https://developers.facebook.com/docs/threads/posts>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. guide served as markdown, against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `c2893f145a2875321e9fa6300a4b47061b86750982f97a494148280891d167e4`
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
