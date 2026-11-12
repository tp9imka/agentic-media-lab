# FLUX 3 Image Klein

`model:black-forest-labs/flux-3-image-klein` - model - <https://huggingface.co/black-forest-labs/flux-3-image-klein>

Black Forest Labs' 5.6B image model from October 2026 for text-to-image and editing with up to 10 reference images, bounding-box layouts and text rendering.

Concepts: [Image models](../../docs/glossary.md#image-models), [Still images](../../docs/glossary.md#still-images), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Consistency](../../docs/glossary.md#consistency)

Also known as: FLUX.3 [klein], flux-3-image-klein, FLUX 3 Klein, flux3

**Badge:** quoted, not read at the primary source (`quoted-secondary`): a claim is quoted via a secondary source.

**Why:** It does generation and multi-reference editing in one model with measured memory on a 64 GB Mac, but its licence caps paid work by the user's revenue.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2i, i2i, edit |
| access | weights |
| apple_silicon | documented |
| licence_class | commercial-threshold |

The weights are gated: accept the licence on Hugging Face and run hf auth login before mflux can download them. We could not open the FLUX Kommunity License itself (login required); the revenue cap below is mflux's summary, so read the licence before client work. The code repo is Apache 2.0, which does not cover the weights.

## Claims

1. mflux's MLX quantization table was measured on an M4 Pro with 64 GB, 1024x1024, 16 steps.

   > Measured on an M4 Pro (64 GB), distilled model, 1024×1024, 16 steps, seed fixed.

   Locator: mflux src/mflux/models/flux3/README.md, section Quantization. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/flux3/README.md>, retrieved 2026-11-12.

2. At 8-bit the model peaked at 22.8 GB and took 7.0 s per step, against 30.7 GB in bf16.

   > | `-q 8` | 9.2 GB | 22.8 GB | 7.0 s | 44.5 dB |

   Locator: mflux src/mflux/models/flux3/README.md, section Quantization, table. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/flux3/README.md>, retrieved 2026-11-12.

3. According to mflux, the licence allows non-commercial work, and paid output only for users under US$5M gross annual revenue including affiliates.

   > non-commercial use, plus commercial output generation by Qualifying Users (less than US$5M gross annualized revenue, including affiliates), subject to the license terms.

   Locator: mflux src/mflux/models/flux3/README.md, licence note. Source: <https://huggingface.co/black-forest-labs/flux-3-image-klein/blob/main/LICENSE.md>, retrieved 2026-11-12. Via: https://github.com/mflux-community/mflux/blob/main/src/mflux/models/flux3/README.md.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. mflux FLUX 3 README and the BFL flux-3-image-klein GitHub README; the licence file itself is gated and was not opened
- Next check due: 2026-12-12
- Licence: other
- URL status: live
- Saved source sha256: `e5751ee95117905b55146a1d3a7bbfb826511633c1dd29317efe958ac95183a3`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2026-10-13
- fetched_at: 2026-11-12
- gated: auto
- hf_downloads: 192532
- hf_likes: 935
- last_activity: 2026-11-02
- licence: other
- sources: https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein

## Related

- integrates_with: [MFLUX](../tool/mflux-community__mflux.md)
- integrates_with: [Draw Things](../tool/drawthings.ai.md)
- alternative_to: [Z-Image](tongyi-mai__z-image.md)

## Referenced by

- [Z-Image](tongyi-mai__z-image.md) (alternative_to)
- [Draw Things](../tool/drawthings.ai.md) (integrates_with)
- [MFLUX](../tool/mflux-community__mflux.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
