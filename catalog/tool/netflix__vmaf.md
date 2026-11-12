# VMAF (libvmaf)

`tool:netflix/vmaf` - tool - <https://github.com/Netflix/vmaf>

Netflix's full-reference perceptual video quality metric, as a C library, CLI and ffmpeg filter, with PSNR, SSIM and the CAMBI banding detector included.

Concepts: [Evaluation](../../docs/glossary.md#evaluation), [Delivery](../../docs/glossary.md#delivery)

Tags: quality-metric, qc, banding

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It measures what an export step lost against the master, and the phone model fits clips watched on a phone.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | review-loop, delivery |
| cost | free-local |

Full-reference only: it needs the lossless master and the encode at the same size and frame count, so it checks the encode, not whether a generated clip looks good. Use the phone model for 9:16 shorts. CAMBI is useful on generated gradients and skies. The v1 models date from 2026-06; an ffmpeg build may still ship v0, check the model path. Not run here.

## Claims

1. The v1 phone model assumes a viewing distance of 5 screen heights.

   > Phone Model: Derived by setting the normalized viewing distance to 5H (based on experimental data)

   Locator: models_v1.md, model list. Source: <https://github.com/Netflix/vmaf/blob/master/resource/doc/models_v1.md>, retrieved 2026-11-12.

2. A new v1 model set was released in June 2026.

   > (2026-06) We are releasing a new set of VMAF models (v1).

   Locator: README, News. Source: <https://github.com/Netflix/vmaf>, retrieved 2026-11-12.

3. libvmaf includes CAMBI, a detector for banding artefacts.

   > (2021-10-7) We are open-sourcing CAMBI (Contrast Aware Multiscale Banding Index) - Netflix's detector for banding (aka contouring) artifacts.

   Locator: README, News. Source: <https://github.com/Netflix/vmaf>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README and models_v1.md against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `ae6e2809e193fda254223d36202e361af8f6b3b7c1deb848fb4801bdb712d72f`
- Lane: craft

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2016-02-08
- default_branch: master
- fetched_at: 2026-11-12
- forks: 850
- last_activity: 2026-11-02
- licence: unknown
- open_issues: 188
- sources: https://api.github.com/repos/Netflix/vmaf, https://skills.sh/api/search?q=vmaf
- stars: 5597

## Related

- integrates_with: [FFmpeg](ffmpeg__ffmpeg.md) - ffmpeg libvmaf filter when built with it

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
