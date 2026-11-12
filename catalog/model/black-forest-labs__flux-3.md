# FLUX 3

`model:black-forest-labs/flux-3` - model - <https://bfl.ai/pricing>

Black Forest Labs' FLUX 3 family on the BFL API: FLUX 3 Video for text, image or video input, and FLUX 3 Image for text or image input.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Image models](../../docs/glossary.md#image-models), [Cost](../../docs/glossary.md#cost)

Also known as: FLUX 3 Video, FLUX 3 Image, FLUX 3 Video Draft, FLUX 3 Image Klein, BFL API

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its pricing page states video rates for four resolution bands, whether audio is included, and the longest output.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v, v2v, t2i, i2i |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Video-to-video costs more than text- or image-to-video at every band ($0.27 vs $0.24 at FHD). Draft mode at $0.06/s exists only in HD; a Draft Enhance render is billed as a full generation. FLUX 3 Image at 4K jumps to $0.607 per image, six times the 2K price. Exact API model ids were not read; docs.bfl.ai was not opened.

## Claims

1. FLUX 3 Video costs $0.15 per second at HD, $0.24 at FHD, $0.28 at QHD and $0.41 at UHD for text or image to video.

   > FLUX 3 Video Text / Image → Video, HD $0.15/s Text / Image → Video, FHD $0.24/s Text / Image → Video, QHD (2K) $0.28/s Text / Image → Video, UHD (4K) $0.41/s

   Locator: Pricing page, FLUX 3 Video table. Source: <https://bfl.ai/pricing>, retrieved 2026-11-12.

2. Audio is included at no extra charge and clips run up to 20 seconds.

   > Is audio included, and how long can clips be? Audio is included at no extra charge. Clips up to 20 seconds.

   Locator: Pricing page, FAQs FLUX 3 Video. Source: <https://bfl.ai/pricing>, retrieved 2026-11-12.

3. FLUX 3 Image costs $0.048 per 1K image and $0.10 per 2K image.

   > FLUX 3 Image $0.041/img $0.048/img $0.07/img $0.10/img $0.607/img

   Locator: Pricing page, FLUX 3 Image table (columns 768 x 768, 1K, 1.5K, 2K, 4K). Source: <https://bfl.ai/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. BFL pricing page against all three claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `2ee6f1e47d051228adc132313005f4b5523e38e79943af8c662f2eb05d62f890`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
