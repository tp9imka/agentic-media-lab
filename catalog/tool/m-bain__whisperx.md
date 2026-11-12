# WhisperX

`tool:m-bain/whisperx` - tool - <https://github.com/m-bain/whisperX>

A Python speech recogniser on faster-whisper that adds word-level timestamps by forced alignment with wav2vec2, voice activity detection and optional speaker labels.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Editing real footage](../../docs/glossary.md#footage-editing)

Also known as: whisperx

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Word timings decide whether captions and transcript cuts land on the word; this is the alignment step several editing skills point to.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | captions, audio |
| cost | free-local |

On a Mac it runs on CPU with int8, not on the GPU, so it is slower than whisper.cpp with Metal on an M3 Max (speed not measured here). Alignment models are per language and are fetched from torchaudio or Hugging Face on first use. Diarization needs a Hugging Face token and accepting the pyannote model terms. The README opens with a sponsor block for a paid API; the tool itself is local.

## Claims

1. It gets word-level timestamps by aligning with wav2vec2.

   > - 🎯 Accurate word-level timestamps using wav2vec2 alignment

   Locator: README.md, introduction list. Source: <https://github.com/m-bain/whisperX/blob/main/README.md>, retrieved 2026-11-12.

2. On macOS it runs on CPU.

   > To run on CPU instead of GPU (and for running on Mac OS X):

   Locator: README.md, section Usage, command line. Source: <https://github.com/m-bain/whisperX/blob/main/README.md>, retrieved 2026-11-12.

3. Speaker labels need a Hugging Face access token.

   > To **enable Speaker Diarization**, include your Hugging Face access token (read) that you can generate from

   Locator: README.md, section Speaker Diarization. Source: <https://github.com/m-bain/whisperX/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims
- Next check due: 2027-02-10
- Licence: BSD-2-Clause
- URL status: live
- Saved source sha256: `98ebee691ebee0ca5bdd9257dad72e1e74a9c216ff3adb7fa68d5164007a84ea`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-12-09
- default_branch: main
- fetched_at: 2026-11-12
- forks: 2545
- last_activity: 2026-10-22
- licence: BSD-2-Clause
- open_issues: 220
- sources: https://api.github.com/repos/m-bain/whisperX, https://skills.sh/api/search?q=whisperX
- stars: 25228

## Related

- alternative_to: [whisper.cpp](ggml-org__whisper.cpp.md) - whisper.cpp runs on Metal; whisperX has stronger word alignment but CPU only on a Mac

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
