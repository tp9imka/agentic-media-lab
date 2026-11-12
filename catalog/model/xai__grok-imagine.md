# Grok Imagine

`model:xai/grok-imagine` - model - <https://docs.x.ai/docs/guides/video-generation>

xAI's image and video generation models on the xAI API: grok-imagine-image-2.0, grok-imagine-video-1.5 and a lower-priced Lite variant.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Image models](../../docs/glossary.md#image-models), [Cost](../../docs/glossary.md#cost)

Also known as: grok-imagine-video-1.5, grok-imagine-video-1.5-lite, grok-imagine-image-2.0, Grok Imagine Video, Grok Imagine Image

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The Lite variant gives video with lip-synced speech from $0.02 per second, the lowest first-party video price found here.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v, v2v, edit, t2i, i2i |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Prices on this page are 'From' prices; the per-resolution table is on the xAI pricing page, not opened. OpenRouter lists 8, 14 and 25 cents per second for 1.5 at 480p, 720p and 1080p. The docs nav lists an Imagine image quality retirement on 2026-11-02 and an Output Watermarking page; neither was opened. The page also offers an llms.txt and a Docs MCP.

## Claims

1. grok-imagine-video-1.5 does native 1080p from text or an image with lip-synced speech, priced from $0.08 per second.

   > grok-imagine-video-1.5 Native 1080p from text or an image, lip-synced speech, up to 14 reference images and 3 voice references, and pinned frames. PricingFrom $0.08 / sec

   Locator: Imagine Overview page, Video Generation card. Source: <https://docs.x.ai/docs/guides/video-generation>, retrieved 2026-11-12.

2. grok-imagine-video-1.5-lite goes up to 1080p and 15 seconds, from $0.02 per second.

   > Text or image to video with lip-synced speech, up to 1080p and 15 seconds, at the lowest price per second. PricingFrom $0.02 / sec

   Locator: Imagine Overview page, Video 1.5 Lite card. Source: <https://docs.x.ai/docs/guides/video-generation>, retrieved 2026-11-12.

3. grok-imagine-image-2.0 costs $0.04 per image at 1K or 2K.

   > grok-imagine-image-2.0 Generate images from text, or edit them with up to 5 reference images. Pricing$0.04 / image Resolution1K & 2K

   Locator: Imagine Overview page, Image Generation card. Source: <https://docs.x.ai/docs/guides/video-generation>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. xAI Imagine overview page (served at the video-generation guide URL) against all three claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `2ba3b84ae33d18cc56724a9a784f0b31c405736ec1c4d4d6ac396d8b45fed156`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- integrates_with: [OpenRouter video generation API](../tool/openrouter__video-generation.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
