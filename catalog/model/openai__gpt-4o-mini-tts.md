# OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)

`model:openai/gpt-4o-mini-tts` - model - <https://developers.openai.com/api/docs/guides/text-to-speech>

OpenAI's text-to-speech models behind /v1/audio/speech, with built-in voices and an instructions field on gpt-4o-mini-tts. All three models are deprecated with a shutdown date.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Models](../../docs/glossary.md#models)

Also known as: OpenAI speech endpoint, /v1/audio/speech, tts-1, tts-1-hd

Tags: tts, voiceover, deprecated, disclosure

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Many skills and scripts call this endpoint for narration; they stop working on 2027-01-06 and the named successor uses a different API.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: low. Level: intro. Maturity: active.

| field | value |
|---|---|
| modes | tts |
| access | api |
| apple_silicon | no-documented-path |
| licence_class | proprietary |

Do not start a new pipeline on it: migration goes to gpt-realtime-2.1-mini on the Realtime API, which is not a drop-in for /v1/audio/speech. Until then use wav or pcm for video sync (pcm is 24 kHz 16-bit with no header). The page says 11 built-in voices in its intro and 13 in the voice list. Per-minute or per-character price was not read here. Usage policy requires telling listeners the voice is AI.

## Claims

1. tts-1, tts-1-hd and gpt-4o-mini-tts shut down on 2027-01-06; the successor is not supported on /v1/audio/speech.

   > The tts-1, tts-1-hd, and gpt-4o-mini-tts models are deprecated and will shut down on January 6, 2027. Migrate to gpt-realtime-2.1-mini using the Realtime API. This is a change of API workflow: gpt-realtime-2.1-mini isn’t a supported model for /v1/audio/speech.

   Locator: Text to speech guide, deprecation notice at the top. Source: <https://developers.openai.com/api/docs/guides/text-to-speech>, retrieved 2026-11-12.

2. OpenAI's usage policies require a clear disclosure that the voice is AI-generated.

   > Our usage policies require you to provide a clear disclosure to end users that the TTS voice they are hearing is AI-generated and not a human voice.

   Locator: Text to speech guide, introduction. Source: <https://developers.openai.com/api/docs/guides/text-to-speech>, retrieved 2026-11-12.

3. OpenAI recommends marin or cedar for best quality.

   > For best quality, we recommend using marin or cedar.

   Locator: Text to speech guide, Voice options. Source: <https://developers.openai.com/api/docs/guides/text-to-speech>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. OpenAI text-to-speech guide (deprecation notice, voice options, output formats, usage-policy note) against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `ab653afa94c3286533c7ac99c0a90a4d791473f358cb78a59360da7eacfeb6b3`
- Lane: media-stages

## Observed

Nothing collected yet.

## Related

- contradicts: [OpenAI Agent Skills (imagegen, speech)](../tool/openai__skills.md) - The speech skill still defaults to gpt-4o-mini-tts.
- alternative_to: [Gemini TTS (Gemini 3.8 Flash TTS)](google__gemini-tts.md)

## Referenced by

- [Gemini TTS (Gemini 3.8 Flash TTS)](google__gemini-tts.md) (alternative_to)
- [ElevenLabs API](../tool/elevenlabs.io.md) (alternative_to)
- [OpenAI Agent Skills (imagegen, speech)](../tool/openai__skills.md) (contradicts)

## Status

Status: current.
Note: Deprecated; OpenAI's TTS guide gives a shutdown date of 2027-01-06 (read 2026-11-12).

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
