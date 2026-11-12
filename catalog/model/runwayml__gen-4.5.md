# Runway Gen-4.5

`model:runwayml/gen-4.5` - model - <https://docs.dev.runwayml.com/guides/pricing>

Runway's own video generation model on the Runway Dev API, billed in credits per second.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost), [Delivery](../../docs/glossary.md#delivery)

Also known as: gen4.5, Gen-4.5

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is one of two models Runway lets export ProRes, PNG sequences and HDR, which matters when the output goes into a grading or compositing tool.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

12 credits = $0.12 per second. ProRes or PNG sequence adds 5 credits/s; HDR adds 20 credits/s (40 above 4 MP). OpenRouter resells it at the same 12 cents per second and lists 2-10 s at 720p. No free tier stated on the pricing page.

## Claims

1. Gen-4.5 costs 12 credits per second, and credits cost $0.01, so $0.12 per second.

   > gen4.5 | 12 credits per second

   Locator: API pricing page, Video Generation Pricing table. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12.

2. Professional and HDR output formats are available on Gen-4.5 and Aleph 2.0 and add a per-second surcharge.

   > These formats add a per-second surcharge on top of the model’s rate. Available on Gen-4.5 and Aleph 2.0

   Locator: API pricing page, section Professional and HDR output formats. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Runway Dev API pricing page against both claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `d7c0e02a094e7889d3804758531245be8295700e43b05f1b1d85c1e1c15383c0`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- depends_on: [Runway Dev API](../tool/runwayml__runway-api.md)

## Referenced by

- [Runway Aleph 2.0](runwayml__aleph.md) (alternative_to)
- [Runway Dev API](../tool/runwayml__runway-api.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
