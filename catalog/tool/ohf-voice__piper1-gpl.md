# Piper (piper1-gpl)

`tool:ohf-voice/piper1-gpl` - tool - <https://github.com/OHF-Voice/piper1-gpl>

A local neural text-to-speech engine with a CLI, a Python API and an HTTP server, installed with pip install piper-tts. Development moved from rhasspy/piper to OHF-Voice/piper1-gpl under the Open Home Foundation.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: Piper TTS, piper-tts, rhasspy/piper

Tags: tts, voiceover, voice-licensing

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It runs on CPU with many stock voices in many languages, and its docs say per voice whether the training chain allows commercial use. Most narration guides miss that check.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | audio, asset |
| cost | free-local |

The CLI example voice, en_US-lessac-medium, descends from a corpus that excludes commercial use, so the copy-paste path is the wrong one for client work. Pick a voice from the COMMERCIAL_USE.md tables and read the MODEL_CARD of the copy on disk: a file downloaded before the late-2026 retrain has the same name but the old chain. CC BY voices need a credit line in the video description. The CLI reloads the model per call; for many lines use the HTTP server. The README asks for new maintainers. No Apple Silicon note was found in the pages read; GPU flags shown are CUDA only. Not run here.

## Claims

1. The project grants a licence for the engine only; each voice's rights come from its training data, and the project takes no position on derivative-work questions.

   > The Piper project makes **no license grant of its own over voice models**, and adds no restriction of its own either.

   Locator: docs/LICENSING.md, The short version, second bullet. Source: <https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/LICENSING.md>, retrieved 2026-11-12.

2. The lessac base voice, used in the CLI example and as the base of many voices, comes from a corpus whose licence excludes commercial use of the synthesis.

   > `en_US-lessac-medium` was trained on the [Lessac Blizzard 2013 corpus][blizzard], whose license limits use to "research and exploration of speech technologies" and excludes commercial use of the resulting synthesis.

   Locator: docs/LICENSING.md, section The lessac base voice. Source: <https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/LICENSING.md>, retrieved 2026-11-12.

3. A voice retrained in late 2026 keeps its file name, so an older downloaded copy does not qualify for the commercial-use list.

   > A copy downloaded before the retrain is the old version and **does not qualify**, even though it has the same file name.

   Locator: docs/COMMERCIAL_USE.md, section Check the copy you have. Source: <https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/COMMERCIAL_USE.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README, docs/LICENSING.md, docs/COMMERCIAL_USE.md and docs/CLI.md of OHF-Voice/piper1-gpl, plus the rhasspy/piper README redirect, against the claims
- Next check due: 2027-02-10
- Licence: GPL-3.0
- URL status: live
- Saved source sha256: `95d626f6415d1962535b75185d2c85590f4bd771686ce51aab3cf63b7627b921`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-03-28
- default_branch: main
- fetched_at: 2026-11-12
- forks: 625
- last_activity: 2026-11-11
- licence: GPL-3.0
- open_issues: 157
- sources: https://api.github.com/repos/OHF-Voice/piper1-gpl, https://skills.sh/api/search?q=piper1-gpl
- stars: 6260

## Related

- alternative_to: [Kokoro-82M](../model/hexgrad__kokoro.md) - Kokoro weights are Apache-licensed as a whole; Piper licensing is per voice.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
