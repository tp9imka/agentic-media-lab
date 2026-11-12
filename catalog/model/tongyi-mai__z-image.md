# Z-Image

`model:tongyi-mai/z-image` - model - <https://huggingface.co/Tongyi-MAI/Z-Image-Turbo>

A 6B text-to-image model from Alibaba's Tongyi lab. The Turbo version is distilled to about 8 or 9 steps and renders English and Chinese text.

Concepts: [Image models](../../docs/glossary.md#image-models), [Still images](../../docs/glossary.md#still-images)

Also known as: Z-Image-Turbo, Z-Image Turbo, Z-Image Base

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the small, permissive image model with published memory numbers on a 64 GB Apple Silicon Mac, which makes it the default for local stills and keyframes.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| modes | t2i |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

Run it with mflux-generate-z-image-turbo -q 8. The full bf16 download is about 31 GB per mflux; the 7.5 GB peak below is for an 8-bit saved copy. The vendor card lists only NVIDIA figures. The Apache-2.0 statement is the card's metadata tag; the repo has no LICENSE file, which was checked in the file list.

## Claims

1. mflux measured Z-Image-Turbo on an Apple Silicon Mac with 64 GB, 8-bit, 1024x1024, 9 steps.

   > Test setup: Apple Silicon Mac, 64 GB, MLX 0.32.0, Z-Image-Turbo `-q 8` saved with `mflux-save`, 1024×1024, 9 steps.

   Locator: mflux src/mflux/models/z_image/README.md, section on --small-text-encoder. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md>, retrieved 2026-11-12.

2. In that setup one image peaked at 7.5 GB of memory.

   > | Peak, one image | 7.5 GB | 7.5 GB |

   Locator: mflux src/mflux/models/z_image/README.md, table after the test setup. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/z_image/README.md>, retrieved 2026-11-12.

3. The model card is tagged Apache 2.0.

   > license: apache-2.0

   Locator: Z-Image-Turbo model card, metadata header. Source: <https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Z-Image-Turbo model card and mflux Z-Image README against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `8657a6beed1109ffb4a481599f48089a27e3c1d4726dfabe5d098c68e31fd7b0`
- Lane: local-models

## Observed

Nothing collected yet.

## Related

- integrates_with: [MFLUX](../tool/mflux-community__mflux.md)
- alternative_to: [FLUX 3 Image Klein](black-forest-labs__flux-3-image-klein.md)

## Referenced by

- [FLUX 3 Image Klein](black-forest-labs__flux-3-image-klein.md) (alternative_to)
- [Qwen-Image](qwen__qwen-image.md) (alternative_to)
- [MFLUX](../tool/mflux-community__mflux.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
