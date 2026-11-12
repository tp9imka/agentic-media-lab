# Luma Ray3.2

`model:lumalabs/ray` - model - <https://lumalabs.ai/api/pricing>

Luma's video generation model on the Luma API, with keyframes, video-to-video, reframe and HDR or EXR output.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost)

Also known as: Ray3.2, Ray 3.2, Ray, Dream Machine API

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Native HDR and 16-bit EXR export are rare among hosted models and matter when the clip is composited with live footage.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v, v2v |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

The pricing page gives credits only, with no dollar value per credit, so the dollar cost cannot be worked out from it. 1080p text- or image-to-video for 10 s is 1,200 credits SDR (1,440 for video-to-video); HDR doubles it. The docs page opened (docs.lumalabs.ai video-generation) shows ray-2 examples, not Ray3.2 ids, so the exact Ray3.2 model id was not confirmed. Audio not stated.

## Claims

1. Ray3.2 text- or image-to-video costs 100 credits for 5 s at 720p and 400 at 1080p; 10 s costs 300 and 1,200.

   > Task 360p 540p 720p 1080p T2V/I2V (5s) 20 50 100 400 T2V/I2V (10s) 60 150 300 1,200

   Locator: API pricing page, Cost Breakdown, Ray3.2 tab. Source: <https://lumalabs.ai/api/pricing>, retrieved 2026-11-12.

2. Prices are in credits; HDR output costs twice SDR and HDR with EXR three times.

   > Prices are in credits Prices shown are SDR output HDR output is 2× SDR pricing HDR + EXR output is 3× SDR pricing

   Locator: API pricing page, notes under the Ray3.2 table. Source: <https://lumalabs.ai/api/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `6c998d1fb0ebc092cfb37b8c7019de1056c391539241eb55ab04dfa4f4725c70`
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
