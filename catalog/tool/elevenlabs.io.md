# ElevenLabs API

`tool:elevenlabs.io` - tool - <https://elevenlabs.io/pricing/api>

A hosted voice and audio API: text to speech with stock voices, sound effects, music, speech to text and dubbing, billed in US dollars per character or per minute.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Cost](../../docs/glossary.md#cost), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: ElevenLabs, Eleven Music, ElevenLabs Sound Effects

Tags: tts, voiceover, sound-effects, music, pricing

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the one hosted vendor that sells TTS, sound effects and music under one key with per-unit prices on the page, which makes a full audio bed costable before the run.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: established.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | audio, asset |
| cost | mixed |

Free-plan output may only be used non-commercially, so a free key is not enough for client or monetised video. The terms give ElevenLabs a perpetual licence to your Input and Output for improving services. The terms make the user responsible for reviewing output before use, and say output may match another user's, so do not treat a generated jingle or effect as exclusive. Voice cloning features exist and are out of scope here; use library or stock voices. Its MCP server was not opened in this lane. Prices go stale in about 30 days.

## Claims

1. Text to speech costs $0.08 per 1,000 characters on multilingual models or $0.04 on Flash/Turbo, billed in dollars.

   > API usage is billed in US dollars, not credits. Text to Speech $0.08 per 1,000 characters (multilingual models) or $0.04 (Flash/Turbo).

   Locator: API pricing page, FAQ, billing answer. Source: <https://elevenlabs.io/pricing/api>, retrieved 2026-11-12.

2. Eleven Music costs $0.15 per minute and Sound Effects $0.12 per minute.

   > Eleven Music $0.15 per minute. Voice Changer and Voice Isolator $0.12 per minute. Sound Effects $0.12 per minute.

   Locator: API pricing page, FAQ, billing answer. Source: <https://elevenlabs.io/pricing/api>, retrieved 2026-11-12.

3. Free users may use the services only for non-commercial purposes; paid users may use them commercially.

   > (i) if you access or use our Services free of charge (such a user, a “Free User”), you may only use the Services for non-commercial purposes; (ii) if you access or use our Services through a paid subscription plan (such a user, a “Paid User”), you may use the Services for commercial purposes

   Locator: Terms of Service, Use Restrictions (c). Source: <https://elevenlabs.io/terms-of-use>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. ElevenLabs API pricing page FAQ and Terms of Service (use restrictions, inputs and outputs, output responsibility) against the claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `d2e42a6dbf929f07a2bff090409839592f207dc36ed6024fda1d413cd9ae7bff`
- Lane: media-stages

## Observed

Nothing collected yet.

## Related

- alternative_to: [Gemini TTS (Gemini 3.8 Flash TTS)](../model/google__gemini-tts.md)
- alternative_to: [OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)](../model/openai__gpt-4o-mini-tts.md)
- integrates_with: [video-use](browser-use__video-use.md) - video-use uses an ElevenLabs key for transcription.

## Referenced by

- [Gemini TTS (Gemini 3.8 Flash TTS)](../model/google__gemini-tts.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
