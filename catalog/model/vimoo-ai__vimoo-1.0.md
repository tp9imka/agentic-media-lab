# Vimoo 1.0

`model:vimoo-ai/vimoo-1.0` - model - <https://huggingface.co/Vimoo-AI/Vimoo-1.0>

An open video model family released in October 2026: an 11.7B model per task (text-to-video, image-to-video) and a 9.5B Lite model that does both. The vendor ships its own MLX build of Lite.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Generated footage](../../docs/glossary.md#generated-footage)

Also known as: Vimoo-1.0, Vimoo-1.0-Lite, Vimoo-1.0-MLX, vimoo-mlx

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the one open video model whose own vendor publishes an Apple Silicon package with a CLI, under Apache 2.0.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: experimental.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

Only the Lite distilled model has an MLX build; the full 11.7B models run through Diffusers or ComfyUI. The agent calls vimoo-mlx with --prompt and optional --image and gets an MP4 plus a JSON of settings and timings. No memory figure is stated (the README says memory is managed automatically). Prompts are validated in English only. Released 2026-10, so expect changes.

## Claims

1. The MLX build covers only the Lite text-and-image-to-video distilled model.

   > TI2V Distilled for MLX on Apple Silicon

   Locator: Vimoo-1.0 model card, model table, row Vimoo 1.0 - Lite. Source: <https://huggingface.co/Vimoo-AI/Vimoo-1.0/blob/main/README.md>, retrieved 2026-11-12.

2. The MLX CLI needs macOS 14 or newer on Apple Silicon and native arm64 Python 3.11 or newer.

   > Use macOS 14 or newer on Apple Silicon, native arm64 Python 3.11 or newer,

   Locator: Vimoo-1.0-MLX README.md, section Quick Start > Installation. Source: <https://github.com/Vimoo-AI/Vimoo-1.0-MLX/blob/main/README.md>, retrieved 2026-11-12.

3. The weights and code allow commercial use, modification and redistribution under the licence.

   > Commercial use, modification, and redistribution are permitted under the terms of the license.

   Locator: Vimoo-1.0 model card, section License. Source: <https://huggingface.co/Vimoo-AI/Vimoo-1.0/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Vimoo-1.0 model card and Vimoo-1.0-MLX README against the claims
- Next check due: 2026-12-12
- Licence: apache-2.0
- URL status: live
- Saved source sha256: `39393351efd118f5349f76165c3ed6e395c7933ea175e91fa0684f1059eb2482`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2026-09-30
- fetched_at: 2026-11-12
- gated: false
- hf_downloads: 52
- hf_likes: 17
- last_activity: 2026-11-04
- licence: apache-2.0
- sources: https://huggingface.co/api/models/Vimoo-AI/Vimoo-1.0

## Related

- integrates_with: [ComfyUI](../tool/comfy-org__comfyui.md)
- alternative_to: [Wan 2.2](wan-ai__wan2.2.md)

## Referenced by

- [ComfyUI](../tool/comfy-org__comfyui.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
