# GPT Image 2

`model:openai/gpt-image` - model - <https://developers.openai.com/api/docs/pricing>

OpenAI's image generation models on the OpenAI API, priced per million image tokens.

Concepts: [Image models](../../docs/glossary.md#image-models), [Cost](../../docs/glossary.md#cost)

Also known as: gpt-image-2, gpt-image-2.6-sunburst, gpt-image-2.6-flare, GPT Image

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the image model many agent skills call by default; its price is in tokens, so the per-image cost must come from the calculator.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2i, i2i |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

The column header unit is 'Prices per 1M tokens unless noted'. The per-image calculator in the image generation guide was not read, so no per-image dollar figure is recorded. Runway resells gpt_image_2 at 1-41 credits ($0.01-0.41) per image by quality and resolution. The page tabs (Standard, Batch) render as text without clear grouping; the gpt-image-2 row sat under the Batch heading in the saved text.

## Claims

1. gpt-image-2.6-sunburst costs $8.00 per million image input tokens and $30.00 per million image output tokens.

   > Prices per 1M tokens unless noted. Images Speed StandardBatch Standard | Model | Modality | Input | Output | Cached input | gpt-image-2.6-sunburst | Image | $8.00 | $30.00 | $2.00

   Locator: API pricing page, Images section, Standard tab. Source: <https://developers.openai.com/api/docs/pricing>, retrieved 2026-11-12.

2. OpenAI points to a calculator for per-image cost estimates.

   > For image generation cost estimates, use the calculator in the image generation guide.

   Locator: API pricing page, Images section, note under the tables. Source: <https://developers.openai.com/api/docs/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. OpenAI API pricing page, Images section, against both claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `cb733aa776e21d83af339bb2718b404a2be0edf93ce821e915f8199047e5fd38`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

- [OpenAI Agent Skills (imagegen, speech)](../tool/openai__skills.md) (integrates_with)
- [Recraft API and MCP server](../tool/recraft.ai.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
