# mlx-video

`tool:blaizzy/mlx-video` - tool - <https://github.com/Blaizzy/mlx-video>

A Python package that runs LTX-2, LTX-2.3, Wan2.1 and Wan2.2 video models in MLX on a Mac, called as python -m mlx_video.<model>.generate.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Generated footage](../../docs/glossary.md#generated-footage), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: MLX-Video, mlx_video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the documented MLX path for the two main open video families, with a command an agent can call and an MP4 as output.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | gen-model-craft, asset |
| cost | free-local |

Installs from git, not from a package index, so pin a commit. Wan weights must be converted first and conversion needs PyTorch; LTX weights have pre-converted copies on a contributor's Hugging Face account, not Lightricks'. The README states no memory figures and no timings, so check a short, low-resolution clip before a long one. LTX-2.5 is not in its model list as of 2026-11-12.

## Claims

1. It describes itself as a package for running and fine-tuning image, video and audio generation models on a Mac with MLX.

   > MLX-Video is the best package for inference and finetuning of Image-Video-Audio generation models on your Mac using MLX.

   Locator: README.md, opening paragraph. Source: <https://github.com/Blaizzy/mlx-video/blob/main/README.md>, retrieved 2026-11-12.

2. It requires macOS on Apple Silicon.

   > macOS with Apple Silicon

   Locator: README.md, section Requirements. Source: <https://github.com/Blaizzy/mlx-video/blob/main/README.md>, retrieved 2026-11-12.

3. Converting weights needs PyTorch installed as well.

   > For weight conversion: PyTorch (`pip install torch`)

   Locator: README.md, section Requirements. Source: <https://github.com/Blaizzy/mlx-video/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. mlx-video README against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `56215953175bdf3852aede2d08e7dcee0958e229e4a2c64bb1c8a789b443edf3`
- Lane: local-models

## Observed

Nothing collected yet.

## Related

- integrates_with: [LTX-2](../model/lightricks__ltx-2.md)
- integrates_with: [Wan 2.2](../model/wan-ai__wan2.2.md)
- alternative_to: [Draw Things](drawthings.ai.md)

## Referenced by

- [LTX-2](../model/lightricks__ltx-2.md) (integrates_with)
- [Wan 2.2](../model/wan-ai__wan2.2.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
