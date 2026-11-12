# Wan 2.2

`model:wan-ai/wan2.2` - model - <https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B>

Alibaba's open video models: a 5B text-and-image-to-video model at 720p 24 fps and larger 14B text-to-video and image-to-video models.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Generated footage](../../docs/glossary.md#generated-footage)

Also known as: Wan2.2, Wan2.2-TI2V-5B, Wan2.2-T2V-A14B, Wan2.2-I2V-A14B

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the main Apache-2.0 video family with a documented MLX route on a Mac, so client work carries no revenue cap.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

Wan's own card documents only NVIDIA GPUs (24 GB VRAM for the 5B command). The Mac route is third-party: mlx-video after a weight conversion that needs PyTorch, or Draw Things (5B import and 14B official models in its log). Start with TI2V-5B on a 64 GB Mac. No Mac timing is published by Wan or mlx-video.

## Claims

1. The models are under Apache 2.0 and Wan claims no rights over generated content.

   > The models in this repository are licensed under the Apache 2.0 License. We claim no rights over the your generated contents

   Locator: Wan2.2-TI2V-5B model card, section License Agreement. Source: <https://huggingface.co/Wan-AI/Wan2.2-TI2V-5B/blob/main/README.md>, retrieved 2026-11-12.

2. mlx-video, which states it is optimized for Apple Silicon with MLX, runs Wan2.2 T2V-14B, TI2V-5B and I2V-14B.

   > T2V-14B, TI2V-5B, and I2V-14B models (dual-model pipeline)

   Locator: mlx-video README.md, section Supported Models. Source: <https://github.com/Blaizzy/mlx-video/blob/main/README.md>, retrieved 2026-11-12.

3. mlx-video states it is built for Apple Silicon with MLX.

   > Optimized for Apple Silicon using MLX

   Locator: mlx-video README.md, section Features > General. Source: <https://github.com/Blaizzy/mlx-video/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Wan2.2-TI2V-5B model card and mlx-video README against the claims; LICENSE.txt read (Apache 2.0 text)
- Next check due: 2026-12-12
- Licence: apache-2.0
- URL status: live
- Saved source sha256: `15891244bc1534af1b818aaf977d28ea360be9b6bc8a4f1541ff2c1c4693c7eb`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2025-07-18
- fetched_at: 2026-11-12
- gated: false
- hf_downloads: 18923
- hf_likes: 962
- last_activity: 2025-08-07
- licence: apache-2.0
- sources: https://huggingface.co/api/models/Wan-AI/Wan2.2-TI2V-5B

## Related

- integrates_with: [mlx-video](../tool/blaizzy__mlx-video.md)
- integrates_with: [Draw Things](../tool/drawthings.ai.md)
- alternative_to: [LTX-2](lightricks__ltx-2.md)

## Referenced by

- [LTX-2](lightricks__ltx-2.md) (alternative_to)
- [Vimoo 1.0](vimoo-ai__vimoo-1.0.md) (alternative_to)
- [mlx-video](../tool/blaizzy__mlx-video.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
