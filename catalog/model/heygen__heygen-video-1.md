# HeyGen Video 1

`model:heygen/heygen-video-1` - model - <https://developers.heygen.com/docs/models/heygen-video>

HeyGen's general-purpose video generation model, built on MiniMax H3 and post-trained by HeyGen. It makes the scene and its sound in one call.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: heygen-video-1

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It led the silent text-to-video board on Artificial Analysis read 2026-11-12, and it returns dialogue, ambience and effects with the clip.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Only the generation model is in scope here, not HeyGen avatars. The page gives no dollar price; OpenRouter lists $0.036 per second at 768p and $0.10 at 1080p, which is close to the stated 3x. Runs on paid API keys only. Unknown request fields are rejected, so copy field names exactly.

## Claims

1. Text-to-video and image-to-video clips run 5 to 30 seconds and each has its own generated audio track.

   > Text-to-video and image-to-video clips can run 5 to 30 seconds with compatible settings; reference-to-video stays at 5 to 15 seconds. Each clip has its own audio track of dialogue, ambience and sound effects

   Locator: HeyGen Video model page, intro. Source: <https://developers.heygen.com/docs/models/heygen-video>, retrieved 2026-11-12.

2. Resolution defaults to 768p, and 1080p and 2k bill at three times the 768p rate.

   > resolution defaults to 768p (1080p and 2k bill at 3× the 768p rate)

   Locator: HeyGen Video model page, request fields paragraph. Source: <https://developers.heygen.com/docs/models/heygen-video>, retrieved 2026-11-12.

3. The model is built on MiniMax H3.

   > built on MiniMax H3 and post-trained by HeyGen

   Locator: HeyGen Video model page, intro. Source: <https://developers.heygen.com/docs/models/heygen-video>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. HeyGen developer docs model page against all three claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `70f6cb613ba1dfea9c7e5e43266e9300155d7792c642ae911d9a4d793cc70c62`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- extends: [MiniMax H3](minimaxai__minimax-h3.md) - HeyGen says it is built on MiniMax H3
- integrates_with: [OpenRouter video generation API](../tool/openrouter__video-generation.md)

## Referenced by

- [OpenRouter video generation API](../tool/openrouter__video-generation.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
