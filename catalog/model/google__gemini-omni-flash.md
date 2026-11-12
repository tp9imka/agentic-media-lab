# Gemini Omni Flash

`model:google/gemini-omni-flash` - model - <https://ai.google.dev/gemini-api/docs/pricing>

Google's video generation and editing model on the Gemini API, with audio.

Concepts: [Hosted video models](../../docs/glossary.md#hosted-video-models), [Cost](../../docs/glossary.md#cost)

Also known as: gemini-omni-1.2-flash, Omni Flash

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the replacement Google names for Veo 3.1 on the Gemini API.

**Last checked:** 2026-11-12, primary-read, by agent:driver. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| modes | t2v, i2v, v2v, edit |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Paid tier only, so it cannot be tried for free. Priced in output tokens; the per-second figures are Google's own approximation.

## Claims

1. Google prices 720p output at about $0.07 per second, so a 10 second clip is about $0.70.

   > approximately $0.07 per second (~$0.70 for a 10s clip, ~$1.04 for a 15s clip;

   Locator: Gemini API pricing page, section Gemini Omni 1.2 Flash. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

2. It generates and edits up to 15 seconds of video with audio, on the paid tier only.

   > up to 15 seconds of video generation and editing with native audio, now generally available to developers on the paid tier of the Gemini API.

   Locator: Gemini API pricing page, section Gemini Omni 1.2 Flash. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:driver, depth primary-read. Gemini API pricing page against both claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `e508333dc4ae245e20b992701878879c4f30d70b7e4ed300151bbc11f30baca0`
- Lane: hosted-models

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

- [Veo 3.1](google__veo-3.1.md) (alternative_to)
- [Veo 3.1](google__veo-3.1.md) (superseded_by)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
