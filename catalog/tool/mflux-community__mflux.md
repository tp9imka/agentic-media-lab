# MFLUX

`tool:mflux-community/mflux` - tool - <https://github.com/mflux-community/mflux>

An MLX re-implementation of open image models for Macs. Each model gets its own CLI command (for example mflux-generate-z-image-turbo) and a Python class.

Concepts: [Still images](../../docs/glossary.md#still-images), [Image models](../../docs/glossary.md#image-models), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: mflux, filipstrand/mflux, mflux-generate

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the shortest documented path from a coding agent to a local image or upscale on Apple Silicon: one shell command per image, no server.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | gen-model-craft, asset |
| cost | free-local |

Install with uv tool install --upgrade mflux; an agent then calls the mflux-generate-* commands. First run downloads weights from Hugging Face, often 20-30 GB per model, and gated models (FLUX 3 Image Klein) need hf auth login first. The per-model READMEs carry the memory and timing tables; the top README has none. The GitHub repo moved from filipstrand/mflux to mflux-community/mflux. Nothing was run here.

## Claims

1. MFLUX runs image models locally on a Mac in MLX.

   > Run the latest state-of-the-art generative image models locally on your Mac in native MLX!

   Locator: README.md, section About. Source: <https://github.com/mflux-community/mflux/blob/main/README.md>, retrieved 2026-11-12.

2. Each model is written from scratch in MLX, with only tokenizers taken from Hugging Face Transformers.

   > All models are implemented from scratch in MLX, using only tokenizers from the

   Locator: README.md, section Philosophy. Source: <https://github.com/mflux-community/mflux/blob/main/README.md>, retrieved 2026-11-12.

3. The first run of a command downloads the model, which can take a long time.

   > The first time you run this, the model will automatically download which can take some time.

   Locator: README.md, section Installation. Source: <https://github.com/mflux-community/mflux/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. mflux README (top level) against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `d562e3cd4a12e5a6ae322da6354eed6633bc2621d05ca1c91c02da57461fbf7d`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2024-08-10
- default_branch: main
- fetched_at: 2026-11-12
- forks: 209
- installs: 1
- installs_by_skill: {"mflux-dev-env": 1, "remediating-dependabot": 1}
- last_activity: 2026-11-08
- licence: MIT
- open_issues: 9
- registry: skills.sh
- sources: https://api.github.com/repos/mflux-community/mflux, https://skills.sh/api/search?q=mflux
- stars: 2598
- Popularity: installs and stars differ by more than 100x

## Related

- alternative_to: [Draw Things](drawthings.ai.md) - GUI app for the same image models
- integrates_with: [Z-Image](../model/tongyi-mai__z-image.md)
- integrates_with: [FLUX 3 Image Klein](../model/black-forest-labs__flux-3-image-klein.md)
- integrates_with: [Qwen-Image](../model/qwen__qwen-image.md)
- integrates_with: [SeedVR2](../model/bytedance-seed__seedvr.md)

## Referenced by

- [FLUX 3 Image Klein](../model/black-forest-labs__flux-3-image-klein.md) (integrates_with)
- [SeedVR2](../model/bytedance-seed__seedvr.md) (integrates_with)
- [Qwen-Image](../model/qwen__qwen-image.md) (integrates_with)
- [Z-Image](../model/tongyi-mai__z-image.md) (integrates_with)
- [ComfyUI](comfy-org__comfyui.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
