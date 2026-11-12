# HappyHorse

`model:alibaba/happyhorse` - model - <https://www.alibabacloud.com/help/en/model-studio/model-pricing>

A second Alibaba video family on Model Studio, with text-to-video, first-frame image-to-video and reference-to-video ids per version.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost)

Also known as: happyhorse-1.1-t2v, happyhorse-1.1-i2v, happyhorse-1.1-r2v, HappyHorse 1.0

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the cheapest way found here to try an Alibaba video model at 480P, with a small free quota.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

On the Artificial Analysis boards read 2026-11-12, HappyHorse ranks well below Wan 3.0 (text-to-video rank 20 for 1.0). Pick Wan 3.0 for quality; HappyHorse 1.1 at 480P is a cheap draft step. Free quota is Singapore-only. Clip length and audio not on the pricing page.

## Claims

1. happyhorse-1.1-t2v costs $0.07 per second at 480P, $0.14 at 720P and $0.18 at 1080P in Singapore, with a 10 second free quota.

   > happyhorse-1.1-t2v | International | 480P | $0.07/second | 10 seconds | 720P | $0.14/second | 1080P | $0.18/second

   Locator: Model pricing page, section HappyHorse-Text-to-video, Singapore table. Source: <https://www.alibabacloud.com/help/en/model-studio/model-pricing>, retrieved 2026-11-12.

2. The free quota is offered only in the Singapore region.

   > NoteThe following models offer a free quota only in Singapore. No free quota is available in other regions.

   Locator: Model pricing page, section HappyHorse-Text-to-video, note above the table. Source: <https://www.alibabacloud.com/help/en/model-studio/model-pricing>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Alibaba Cloud Model Studio pricing page, HappyHorse section, against both claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `82c4a2150ab95f586777787139ffa93a50c21878c02b8471026d644058f55a1e`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- alternative_to: [Wan 3.0](alibaba__wan.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
