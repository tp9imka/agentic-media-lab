# SeedVR2

`model:bytedance-seed/seedvr` - model - <https://github.com/ByteDance-Seed/SeedVR>

ByteDance's diffusion models for video and image restoration and upscaling, in 3B and 7B sizes, often in one step.

Concepts: [Delivery](../../docs/glossary.md#delivery), [Still images](../../docs/glossary.md#still-images)

Also known as: SeedVR, SeedVR2-3B, SeedVR2-7B, mflux-upscale-seedvr2

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Upscaling is a cheap last step to make a local clip or still look finished, and mflux ships an MLX upscale command for it.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | upscale |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

The mflux path upscales images, not video files. For a clip, extract frames with ffmpeg, upscale the folder, and re-encode; frame-to-frame consistency of that route was not checked. --low-ram does not work in folder mode. Large target resolutions need a lot of memory; no figure is published.

## Claims

1. mflux's SeedVR2 command upscales every image in a folder when given a directory.

   > Pass a directory to `--image-path` to upscale every image inside.

   Locator: mflux src/mflux/models/seedvr2/README.md, section Upscale a Directory. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/seedvr2/README.md>, retrieved 2026-11-12.

2. Under memory pressure mflux suggests --low-ram or an MLX cache limit.

   > If you run into memory pressure, try `--low-ram` or set an MLX cache limit with `--mlx-cache-limit-gb 16`

   Locator: mflux src/mflux/models/seedvr2/README.md, section Upscale, note. Source: <https://github.com/mflux-community/mflux/blob/main/src/mflux/models/seedvr2/README.md>, retrieved 2026-11-12.

3. SeedVR and SeedVR2 are under Apache 2.0.

   > SeedVR and SeedVR2 are licensed under the Apache 2.0.

   Locator: SeedVR readme.md, section License. Source: <https://github.com/ByteDance-Seed/SeedVR/blob/main/readme.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. mflux SeedVR2 README, SeedVR readme and LICENSE against the claims
- Next check due: 2026-12-12
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `6511cec9aa380cb988b6a72733991286ddf2fe36bc189395a256facaed137d87`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-06-10
- default_branch: main
- fetched_at: 2026-11-12
- forks: 91
- last_activity: 2026-01-27
- licence: Apache-2.0
- open_issues: 51
- sources: https://api.github.com/repos/ByteDance-Seed/SeedVR, https://skills.sh/api/search?q=SeedVR
- stars: 1441

## Related

- integrates_with: [MFLUX](../tool/mflux-community__mflux.md)
- integrates_with: [Draw Things](../tool/drawthings.ai.md)

## Referenced by

- [MFLUX](../tool/mflux-community__mflux.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
