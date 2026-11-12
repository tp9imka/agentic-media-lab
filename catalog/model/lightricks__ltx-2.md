# LTX-2

`model:lightricks/ltx-2` - model - <https://github.com/Lightricks/LTX-2>

Lightricks' open-weights video model family that generates video and synchronized audio. The repo README points to LTX-2.5 (22B distilled transformer with a Gemma 4 12B text encoder).

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Generated footage](../../docs/glossary.md#generated-footage), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: LTX-2.3, LTX-2.5, LTX Video, Lightricks LTX

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the open video model with the most documented Mac routes: the official PyTorch code on MPS, mlx-video for LTX-2 and 2.3, and Draw Things for 2.3.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | weights |
| apple_silicon | documented |
| licence_class | commercial-threshold |

Free under the licence only while your organisation earns under $10M a year. The official Mac path is PyTorch on MPS; the fastest VAE backend (natten) is Linux and CUDA only and is skipped on macOS. The LTX-2.5 file names give a 22B transformer and a 12B text encoder in bf16, which by our arithmetic is over 64 GB before any quantization; no Mac memory figure is published. Not run here.

## Claims

1. Organisations with annual revenue of $10M or more need a paid licence for any use beyond non-commercial purposes.

   > provided however, that Entities with annual revenues of at least $10,000,000 (the "Commercial Entities") are required to obtain a paid license for any use

   Locator: LICENSE-2_x, section 2.1 Grant of License. Source: <https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x>, retrieved 2026-11-12.

2. Since release 1.3.0 (2026-08-25) the install on macOS uses PyPI PyTorch with MPS on Apple Silicon.

   > `uv sync` on macOS no longer fails looking for CUDA-only torch wheels. Macs use PyPI (MPS on Apple Silicon); Linux and Windows still use the CUDA 13.2 indexes.

   Locator: CHANGELOG.md, 1.3.0 - 2026-08-25, Fixed. Source: <https://github.com/Lightricks/LTX-2/blob/main/CHANGELOG.md>, retrieved 2026-11-12.

3. Release 1.2.0 (2026-08-11) fixed VAE decode tiling on Apple Silicon, which before could not fit any tile at any resolution.

   > Fixed diffusion-VAE decode tiling on Apple Silicon. The decode memory budget was probed only on CUDA, so on other backends it reported zero bytes available and no decode tile could ever fit, at any resolution. Automatic tiling now sizes itself from the Metal working set on MPS.

   Locator: CHANGELOG.md, 1.2.0 - 2026-08-11, Fixed. Source: <https://github.com/Lightricks/LTX-2/blob/main/CHANGELOG.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. LTX-2 CHANGELOG, LICENSE-2_x and README against the claims
- Next check due: 2026-12-12
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `4ffa66289ae55b2e5b71463ff7f596d192c26af8d4bcc53e62c2d2080c630d35`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-01-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1623
- installs: 11
- installs_by_skill: {"train-model": 11}
- last_activity: 2026-11-05
- licence: Apache-2.0
- open_issues: 37
- registry: skills.sh
- sources: https://api.github.com/repos/Lightricks/LTX-2, https://skills.sh/api/search?q=LTX-2
- stars: 10201
- Popularity: installs and stars differ by more than 100x

## Related

- integrates_with: [mlx-video](../tool/blaizzy__mlx-video.md)
- integrates_with: [Draw Things](../tool/drawthings.ai.md)
- alternative_to: [Wan 2.2](wan-ai__wan2.2.md)

## Referenced by

- [Wan 2.2](wan-ai__wan2.2.md) (alternative_to)
- [mlx-video](../tool/blaizzy__mlx-video.md) (integrates_with)
- [Draw Things](../tool/drawthings.ai.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
