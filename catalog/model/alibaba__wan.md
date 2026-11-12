# Wan 3.0

`model:alibaba/wan` - model - <https://www.alibabacloud.com/help/en/model-studio/model-pricing>

Alibaba's hosted video generation family on Model Studio. Wan 3.0 comes in two ids, wan3.0-video and wan3.0-video-prime, at 480P, 720P and 1080P.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost)

Also known as: wan3.0-video, wan3.0-video-prime, Wan, Wanx, Alibaba Model Studio video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It led the Artificial Analysis text-to-video board on 2026-11-12, and its 1080P list price is lower than Seedance 2.5 or FLUX 3 Video at 1080p.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, v2v |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Input video is billed too: billable seconds are input plus output, so a video-to-video edit with a 10 s input and a 10 s output bills 20 s. The 30 s free quota exists only in the Singapore region and only for wan3.0-video, and is valid for 90 days from activation, model release or approval, whichever is later. The 30% discount is labelled limited-time with no end date on the page. Maximum duration and whether audio is generated are not on the pricing page; OpenRouter lists 2-30 s for its resold copy, not checked at Alibaba.

## Claims

1. In the Singapore region wan3.0-video lists at $0.05 per second at 480P, $0.1 at 720P and $0.2 at 1080P, shown with a limited-time 30% discount, and carries a 30 second free quota valid for 90 days from Model Studio activation, model release or application approval, whichever is later.

   > wan3.0-video | International | 480P | List price $0.05/second (Limited-time 30% off) | 30 seconds | 720P | List price $0.1/second (Limited-time 30% off) | 1080P | List price $0.2/second (Limited-time 30% off)

   Locator: Model pricing page, section Wan 3.0-Video Generation, Singapore table. Source: <https://www.alibabacloud.com/help/en/model-studio/model-pricing>, retrieved 2026-11-12.

2. wan3.0-video-prime costs $0.068, $0.14 and $0.28 per second at 480P, 720P and 1080P in Singapore, with no free quota.

   > wan3.0-video-prime | International | 480P | $0.068/second | No free quota | 720P | $0.14/second | 1080P | $0.28/second

   Locator: Model pricing page, section Wan 3.0-Video Generation, Singapore table. Source: <https://www.alibabacloud.com/help/en/model-studio/model-pricing>, retrieved 2026-11-12.

3. Both input and output video seconds are billed, and failed requests are not.

   > Pricing rule: both input and output videos are billed by video duration (seconds). Failed requests are not billed and do not consume the free quota.

   Locator: Model pricing page, section Wan 3.0-Video Generation, pricing rule. Source: <https://www.alibabacloud.com/help/en/model-studio/model-pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `82c4a2150ab95f586777787139ffa93a50c21878c02b8471026d644058f55a1e`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- evaluated_on: [Artificial Analysis Video Arena: text-to-video and image-to-video leaderboards](../source/artificialanalysis.ai__video__leaderboard__text-to-video.md)
- integrates_with: [OpenRouter video generation API](../tool/openrouter__video-generation.md) - resold as alibaba/wan-3.0 at the same list price

## Referenced by

- [HappyHorse](alibaba__happyhorse.md) (alternative_to)
- [Artificial Analysis Video Arena: text-to-video and image-to-video leaderboards](../source/artificialanalysis.ai__video__leaderboard__text-to-video.md) (evaluated_on)
- [OpenRouter video generation API](../tool/openrouter__video-generation.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
