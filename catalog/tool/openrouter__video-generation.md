# OpenRouter video generation API

`tool:openrouter/video-generation` - tool - <https://openrouter.ai/docs/guides/overview/multimodal/video-generation>

OpenRouter's asynchronous video generation API, which resells video models from Google, Alibaba, ByteDance, MiniMax, xAI, Kling, Runway, BFL and HeyGen, with a public JSON list of models, durations, resolutions and prices.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost), [Agent Skills](../../docs/glossary.md#agent-skills)

Also known as: OpenRouter videos, api/v1/videos/models, openrouter-video skill

**Badge:** quoted, not read at the primary source (`quoted-secondary`): a claim is quoted via a secondary source.

**Why:** The models endpoint is a machine-readable price and limits list an agent can read before choosing a model, without a key.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | any-skill |
| levers | gen-model-craft, orchestration |
| cost | paid |

The models list was read without a key on 2026-11-12. Prices there are OpenRouter's, mixed units (dollars per second, cents per second, dollars per token) by model. Some resold models expose fewer options than the vendor: bytedance/seedance-2.5 lists 480p and 720p only, while BytePlus offers 1080p. The guide's own sample response still shows google/veo-3.1. The page mentions an openrouter-video skill; it was not opened or installed.

## Claims

1. The video models endpoint lists every video model with its supported durations, resolutions and pricing SKUs.

   > Use the dedicated video models endpoint to list all available video generation models along with their supported parameters: curl "https://openrouter.ai/api/v1/videos/models"

   Locator: Video Generation guide, Model Discovery, Via the Video Models API. Source: <https://openrouter.ai/docs/guides/overview/multimodal/video-generation>, retrieved 2026-11-12.

2. OpenRouter lists alibaba/wan-3.0 at $0.05, $0.1 and $0.2 per second for 480p, 720p and 1080p.

   > "pricing_skus":{"duration_seconds_480p":"0.05","duration_seconds_720p":"0.1","duration_seconds_1080p":"0.2"}

   Locator: GET /api/v1/videos/models, entry id alibaba/wan-3.0, field pricing_skus. Source: <https://openrouter.ai/api/v1/videos/models>, retrieved 2026-11-12. Via: OpenRouter (reseller); first-party price is on Alibaba Model Studio.

3. OpenRouter lists heygen/heygen-video-1 at $0.036 per second at 768p and $0.10 at 1080p.

   > "pricing_skus":{"duration_seconds_2k":"0.1","duration_seconds_480p":"0.02","duration_seconds_768p":"0.036","duration_seconds_1080p":"0.1"

   Locator: GET /api/v1/videos/models, entry id heygen/heygen-video-1, field pricing_skus. Source: <https://openrouter.ai/api/v1/videos/models>, retrieved 2026-11-12. Via: OpenRouter (reseller); HeyGen's page gives no dollar price.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. OpenRouter video generation guide and the public /api/v1/videos/models JSON against all three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `359058b7859ae4e38779ce5f34c43003f63e1901090d8895b103f7df63b83600`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- integrates_with: [Wan 3.0](../model/alibaba__wan.md)
- integrates_with: [Dreamina Seedance 2.5](../model/bytedance__seedance.md)
- integrates_with: [HeyGen Video 1](../model/heygen__heygen-video-1.md)

## Referenced by

- [Wan 3.0](../model/alibaba__wan.md) (integrates_with)
- [HeyGen Video 1](../model/heygen__heygen-video-1.md) (integrates_with)
- [Grok Imagine](../model/xai__grok-imagine.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
