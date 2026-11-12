# whisper.cpp

`tool:ggml-org/whisper.cpp` - tool - <https://github.com/ggml-org/whisper.cpp>

A C/C++ port of OpenAI's Whisper speech recognition, built as the whisper-cli binary, with Metal and Core ML support on Apple Silicon.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: whisper-cli, ggerganov/whisper.cpp

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives an agent a local transcript with timestamps for captions, on the Mac GPU, from one command.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | captions, audio |
| cost | free-local |

It has to be built with cmake; the Core ML encoder needs Python, coremltools and Xcode to generate. whisper-cli reads 16-bit WAV only, so convert with ffmpeg first. Word-level timestamps are marked experimental in the README; for word-timed captions compare with the alignment in whisperX, which only runs on CPU on a Mac.

## Claims

1. On Apple Silicon the whole inference runs on the GPU through Metal.

   > On Apple Silicon, the inference runs fully on the GPU via Metal:

   Locator: README.md, section Quick start demo. Source: <https://github.com/ggml-org/whisper.cpp/blob/master/README.md>, retrieved 2026-11-12.

2. The large model needs about 3.9 GB of memory and 2.9 GiB of disk.

   > | large | 2.9 GiB | ~3.9 GB |

   Locator: README.md, section Memory usage, table. Source: <https://github.com/ggml-org/whisper.cpp/blob/master/README.md>, retrieved 2026-11-12.

3. On Apple Silicon the encoder can also run on the Neural Engine through Core ML.

   > On Apple Silicon devices, the Encoder inference can be executed on the Apple Neural Engine (ANE) via Core ML.

   Locator: README.md, section Core ML support. Source: <https://github.com/ggml-org/whisper.cpp/blob/master/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. whisper.cpp README against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `f8ec51916700b997caa70307d95d1ac15401d40dc6e88822d3b7f6896ecfd379`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-09-25
- default_branch: master
- fetched_at: 2026-11-12
- forks: 6297
- last_activity: 2026-11-10
- licence: MIT
- open_issues: 364
- sources: https://api.github.com/repos/ggml-org/whisper.cpp, https://skills.sh/api/search?q=whisper.cpp
- stars: 55123

## Related

- alternative_to: [mlx-whisper](ml-explore__mlx-examples__whisper.md)

## Referenced by

- [WhisperX](m-bain__whisperx.md) (alternative_to)
- [MakeMyClip Editor](makemyclip__editor.md) (depends_on)
- [mlx-whisper](ml-explore__mlx-examples__whisper.md) (alternative_to)
- [Auto-Editor](wyattblue__auto-editor.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
