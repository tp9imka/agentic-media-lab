# Runway Aleph 2.0

`model:runwayml/aleph` - model - <https://docs.dev.runwayml.com/guides/pricing>

Runway's video-to-video editing model on the Runway Dev API.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Editing real footage](../../docs/glossary.md#footage-editing), [Cost](../../docs/glossary.md#cost)

Also known as: aleph2, Aleph

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It edits an existing video by prompt, the step after generation when one shot is almost right.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | v2v, edit |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

28 credits = $0.28 per second with a 56 credit ($0.56) minimum, so even a 1 s edit costs $0.56. Maximum input length was not found on the pricing page.

## Claims

1. Aleph 2.0 costs 28 credits per second with a 56 credit minimum per generation.

   > aleph2 | 28 credits per second (56 credit minimum per generation)

   Locator: API pricing page, Video Generation Pricing table. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12.

2. Runway credits cost $0.01 each.

   > Credits can be purchased for $0.01 per credit in the developer portal for a project.

   Locator: API pricing page, API Pricing & Costs intro. Source: <https://docs.dev.runwayml.com/guides/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `d7c0e02a094e7889d3804758531245be8295700e43b05f1b1d85c1e1c15383c0`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- depends_on: [Runway Dev API](../tool/runwayml__runway-api.md)
- alternative_to: [Runway Gen-4.5](runwayml__gen-4.5.md)

## Referenced by

- [Runway Dev API](../tool/runwayml__runway-api.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
