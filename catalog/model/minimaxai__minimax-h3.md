# MiniMax H3

`model:minimaxai/minimax-h3` - model - <https://huggingface.co/MiniMaxAI/MiniMax-H3>

An open-weights video generation model from MiniMax, also sold through its API.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Hosted video models](../../docs/glossary.md#hosted-video-models), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: Hailuo 3, MiniMax-H3, H3

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A leading open-weights video model whose licence does not cover several major regions.

**Last checked:** 2026-11-12, primary-read, by agent:driver. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | weights |
| apple_silicon | documented |
| licence_class | territory-restricted |

Read the licence for where you are before using the weights. Ports for Apple Silicon exist, but the one published timing is minutes per denoising step on a larger machine, and nothing was measured here.

## Claims

1. The licence defines the EU, the UK, South Korea and the USA as excluded territories.

   > “Excluded Territories” means the European Union, the United Kingdom, the Republic of Korea and the United States of America.

   Locator: LICENSE, Definitions, item 5. Source: <https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE>, retrieved 2026-11-12.

2. The licence applies worldwide except those territories.

   > “Applicable Territory” means worldwide, excluding the Excluded Territories.

   Locator: LICENSE, Definitions, item 3. Source: <https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:driver, depth primary-read. LICENSE file on the model repository against both claims
- Next check due: 2026-12-12
- Licence: other
- URL status: live
- Saved source sha256: `59b99642b95ea21630e311198ddbfffbfe05aadba0c2f5d884cbdf4efcc90f44`
- Lane: hosted-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2026-07-28
- fetched_at: 2026-11-12
- gated: false
- hf_downloads: 6502936
- hf_likes: 6825
- last_activity: 2026-11-09
- licence: other
- sources: https://huggingface.co/api/models/MiniMaxAI/MiniMax-H3

## Related

None.

## Referenced by

- [Draw Things](../tool/drawthings.ai.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
