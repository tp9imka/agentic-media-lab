# Gemini TTS (Gemini 3.8 Flash TTS)

`model:google/gemini-tts` - model - <https://ai.google.dev/gemini-api/docs/speech-generation>

Google's text-to-speech models on the Gemini API, with prebuilt voices, style control through turn metadata and inline tags, and two-speaker dialogue in one request.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Cost](../../docs/glossary.md#cost), [Models](../../docs/glossary.md#models)

Also known as: gemini-3.8-flash-tts, gemini-3.8-flash-lite-tts, Gemini speech generation

Tags: tts, voiceover, pricing, gemini

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the cheapest first-party hosted narration with a price on the page, and the price doubles on 2027-01-01.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | tts |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Paid output is $9 per 1M audio tokens ($0.00225 per 10 s) through 2026-12-31 and $18 from 2027-01-01; budget with the 2027 number. The free tier exists but its data is used to improve Google products; use the paid tier for client scripts. Gemini 3.8 returns full WAV with a 44-byte header; strip it or request audio/l16 before joining turns. Voice design, remixing and replication features exist; replication is cloning and out of scope here; use prebuilt voices. No SynthID statement was found on the TTS page.

## Claims

1. Gemini 3.8 Flash TTS output costs $9.00 per 1M audio tokens through 2026-12-31 and $18.00 from 2027-01-01.

   > $9.00 (audio) through December 31, 2026. $18.00 (audio) starting January 1, 2027.

   Locator: Pricing page (markdown), Gemini 3.8 Flash TTS, Standard tab, Output price. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

2. Google equates the 2027 output price to $0.0045 per 10 seconds of audio.

   > Equivalent to $0.0045 per 10s audio

   Locator: Pricing page (markdown), Gemini 3.8 Flash TTS, Standard tab, Output price. Source: <https://ai.google.dev/gemini-api/docs/pricing>, retrieved 2026-11-12.

3. Joining separately generated turns needs raw PCM or the WAV header stripped.

   > Because unary requests return `audio/wav` with a 44-byte RIFF header by default, request raw PCM (`{"type": "audio", "mime_type": "audio/l16"}`) or strip the WAV header from each turn before concatenating the 24kHz PCM audio frames.

   Locator: Speech generation guide (markdown), Limitations, second bullet. Source: <https://ai.google.dev/gemini-api/docs/speech-generation>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Gemini API speech-generation guide (markdown) and Gemini API pricing page (markdown), Gemini 3.8 Flash TTS section, against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `77761a4179968cff32621b86fd62affb1393b3b29614b965d6435c8ebeed6e6e`
- Lane: media-stages

## Observed

Nothing collected yet.

## Related

- alternative_to: [OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)](openai__gpt-4o-mini-tts.md)
- alternative_to: [ElevenLabs API](../tool/elevenlabs.io.md)

## Referenced by

- [OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)](openai__gpt-4o-mini-tts.md) (alternative_to)
- [ElevenLabs API](../tool/elevenlabs.io.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
