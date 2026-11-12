# Draw Things

`tool:drawthings.ai` - tool - <https://drawthings.ai/downloads/>

A Mac and iOS app that runs open image and video models on Apple hardware, with its own release log of supported models.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Image models](../../docs/glossary.md#image-models), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: DrawThings, Draw Things app

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its release log is the most up-to-date record of which open models run on a Mac at all, including LTX-2.3, MiniMax H3 and FLUX 3 Image Klein.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | none-stated |
| levers | gen-model-craft, asset |
| cost | mixed |

Best for a person to try a model by hand. For an agent the only interfaces named on this page are a gRPC server and in-app scripts; a stable CLI or HTTP API was not found here, so plan on mflux or mlx-video for scripted runs. The app has paid tiers and an optional cloud offload; their prices were not checked.

## Claims

1. The 2026-10-22 release added FLUX 3 Image Klein.

   > Add support for FLUX.3 [klein] 5.6B series models.

   Locator: Downloads page, release 26.1020.0, October 22, 2026. Source: <https://drawthings.ai/downloads/>, retrieved 2026-11-12.

2. The 2026-09-11 release added MiniMax H3, with LoRAs and TeaCache.

   > Add support for MiniMax H3 series models, including LoRAs and TeaCache.

   Locator: Downloads page, release 26.0910.1, September 11, 2026. Source: <https://drawthings.ai/downloads/>, retrieved 2026-11-12.

3. The app can run a gRPC server so another device can use its compute.

   > Add "Server Offload" feature which allows you to enable gRPC server on one instance of the app on a different device and connect to that device to use its compute.

   Locator: Downloads page, older release entry. Source: <https://drawthings.ai/downloads/>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Draw Things downloads page (release log, visible text) against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `8d00e9a16867b5d8ffd53b46347b44324b5a58d531d4238aa9fbe17ed8b3b522`
- Lane: local-models

## Observed

Nothing collected yet.

## Related

- integrates_with: [MiniMax H3](../model/minimaxai__minimax-h3.md)
- integrates_with: [LTX-2](../model/lightricks__ltx-2.md)
- integrates_with: [FLUX 3 Image Klein](../model/black-forest-labs__flux-3-image-klein.md)

## Referenced by

- [FLUX 3 Image Klein](../model/black-forest-labs__flux-3-image-klein.md) (integrates_with)
- [SeedVR2](../model/bytedance-seed__seedvr.md) (integrates_with)
- [LTX-2](../model/lightricks__ltx-2.md) (integrates_with)
- [Wan 2.2](../model/wan-ai__wan2.2.md) (integrates_with)
- [mlx-video](blaizzy__mlx-video.md) (alternative_to)
- [MFLUX](mflux-community__mflux.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
