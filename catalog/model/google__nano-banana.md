# Nano Banana (Gemini image models)

`model:google/nano-banana` - model - <https://ai.google.dev/gemini-api/docs/pricing>

Google's image generation models on the Gemini API: gemini-nano-banana-2.1 and gemini-3-pro-image. Imagen 4 was shut down on the Gemini API and points to Nano Banana 2.1.

Concepts: [Image models](../../docs/glossary.md#image-models), [Cost](../../docs/glossary.md#cost)

Also known as: gemini-nano-banana-2.1, Nano Banana 2.1, gemini-3-pro-image, Nano Banana Pro, Gemini 3 Pro Image, Imagen 4

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Code that calls the GA imagen-4.0-*-001 ids on the Gemini API stopped working on 2026-08-17 (the preview ids on 2026-02-17); Nano Banana 2.1 is the named replacement.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | t2i, i2i |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Billed in output tokens; Google converts to per-image prices. Nano Banana 2.1 is $0.0336 per 1K image, gemini-3-pro-image $0.134 per 1K or 2K image, four times more. Neither has a free tier on the Gemini API. Batch halves the Nano Banana 2.1 price. fal resells Nano Banana Pro at $0.15 per image, above Google's own $0.134.

## Claims

1. gemini-nano-banana-2.1 output images cost $0.0336 at 1K, $0.0504 at 2K, priced at $30 per million tokens.

   > Output images at 1K (1024x1024px) consume 1120 tokens and are equivalent to $0.0336 per image. Output images at 2K (2048x2048px) consume 1680 tokens and are equivalent to $0.0504 per image.

   Locator: Gemini API pricing page (markdown), section Gemini Nano Banana 2.1, footnote. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

2. gemini-3-pro-image output costs $0.134 per 1K or 2K image and $0.24 per 4K image, with no free tier.

   > Equivalent to $0.134 per 1K/2K image{% sup /%} and $0.24 per 4K image

   Locator: Gemini API pricing page (markdown), section Gemini 3 Pro Image (Nano Banana Pro), Standard tab. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

3. imagen-4.0-generate-001 was shut down on 2026-08-17, with gemini-nano-banana-2.1 as the recommended replacement.

   > * `imagen-4.0-generate-001` * June 24, 2025 * August 17, 2026 * `gemini-nano-banana-2.1`

   Locator: Gemini API deprecations page (markdown), Imagen models, Deprecated models table. Source: <https://ai.google.dev/gemini-api/docs/deprecations>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `71d69e7dcc56b3cad537cb0287976d85b709420f1f564df9cf38f3546da9c6ff`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- integrates_with: [Gemini Omni Flash](google__gemini-omni-flash.md) - same Gemini API key and billing

## Referenced by

- [Nano Banana extension for Gemini CLI](../tool/gemini-cli-extensions__nanobanana.md) (integrates_with)
- [Nano Banana 2 Skill](../tool/kingbootoshi__nano-banana-2-skill.md) (integrates_with)
- [Recraft API and MCP server](../tool/recraft.ai.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
