# Dreamina Seedance 2.5

`model:bytedance/seedance` - model - <https://ai.byteplus.com/ark/docs/seedance-2-5.md>

ByteDance's video generation family on BytePlus ModelArk. Seedance 2.5 (id dreamina-seedance-2-5-260628) generates up to 30 seconds with audio from text, frames or up to 50 reference assets, and edits or extends video.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost), [Consistency](../../docs/glossary.md#consistency)

Also known as: Seedance, dreamina-seedance-2-5-260628, dreamina-seedance-2-5-flash-261115, Seedance 2.0, BytePlus ModelArk video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It ranked first on the Artificial Analysis image-to-video board read 2026-11-12 and gives the longest single clip found here (30 s).

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v, v2v, edit |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Priced in tokens, not seconds: tokens = (input + output seconds) x width x height x fps / 1024. BytePlus' own worked example is $0.231/s at 720p 16:9 and $0.569/s at 1080p. Activation needs a BytePlus balance above USD 30, a savings plan or a resource pack, so there is no free try. BytePlus serves the docs as markdown (append .md) and lists an agent-skills index and an MCP server card at ai.byteplus.com/.well-known; those were not opened. OpenRouter resells it at 480p and 720p only.

## Claims

1. Seedance 2.5 generates up to 30 seconds in one request, can extend a video over several rounds and accepts up to 50 reference assets.

   > It can generate up to 30 seconds of video in one request, extend videos over multiple rounds, accept up to 50 omni reference assets per request, and perform precise timestamp-based editing.

   Locator: Seedance 2.5 tutorial, intro paragraph. Source: <https://ai.byteplus.com/ark/docs/seedance-2-5.md>, retrieved 2026-11-12.

2. The 1080p 5 second example costs $2.843, which BytePlus gives as $0.569 per second; 720p is $0.231 per second and 480p $0.103.

   > | Dreamina Seedance 2.5 | * $0.514 per video | * $1.156 per video | * $2.843 per video | \ | | * $0.103 per second | * $0.231 per second | * $0.569 per second |

   Locator: Model pricing, Billing examples, Dreamina Seedance 2.5 series, tab Input without video (480p, 720p, 1080p, 16:9, 5 s). Source: <https://ai.byteplus.com/ark/docs/model-pricing.md>, retrieved 2026-11-12.

3. Before Seedance 2.5 can be enabled the account needs a balance above USD 30, a USD 30 savings plan or a resource pack.

   > **Recommended:** BytePlus account balance > USD 30

   Locator: Seedance 2.5 tutorial, note before enabling the model. Source: <https://ai.byteplus.com/ark/docs/seedance-2-5.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. BytePlus Seedance 2.5 tutorial and ModelArk pricing page, markdown versions, against all three claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `00a48c8eb23a72ce0398c7878520cd706cf24d79f21e53f6a8f0f6f90244ff93`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- evaluated_on: [Artificial Analysis Video Arena: text-to-video and image-to-video leaderboards](../source/artificialanalysis.ai__video__leaderboard__text-to-video.md)
- integrates_with: [Runway Dev API](../tool/runwayml__runway-api.md) - resold as seedance2_5

## Referenced by

- [Artificial Analysis Video Arena: text-to-video and image-to-video leaderboards](../source/artificialanalysis.ai__video__leaderboard__text-to-video.md) (evaluated_on)
- [OpenRouter video generation API](../tool/openrouter__video-generation.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
