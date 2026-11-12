# MLX-Audio

`tool:blaizzy/mlx-audio` - tool - <https://github.com/Blaizzy/mlx-audio>

A Python library and CLI that runs text-to-speech, speech-to-text, speech-to-speech and music models on Apple Silicon through MLX. It also starts a local server with an OpenAI-compatible speech endpoint.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Models](../../docs/glossary.md#models)

Also known as: mlx_audio, mlx-audio

Tags: tts, sound-effects, music, apple-silicon, mlx

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is one install that puts Kokoro, Qwen3-TTS stock voices and Stable Audio 3 SFX and music on the reader's Mac GPU, callable from a shell command.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | audio, asset |
| cost | free-local |

Each model keeps its own licence; the library's MIT licence says nothing about the weights it downloads, and many listed models are cloning models (out of scope here). When a text yields several segments the CLI writes numbered files, so an agent that expects one WAV must pass --join_audio. The README starts the server on 0.0.0.0, which listens on every network interface; use 127.0.0.1 on a shared network. MP3 and other compressed formats need ffmpeg; WAV does not. No speed or memory figures for an M3 Max are given. Not run here.

## Claims

1. It targets Apple Silicon Macs and covers speech and music generation.

   > Text-to-speech, speech-to-text, speech-to-speech, and music generation. Built on MLX.

   Locator: README.md, header tagline. Source: <https://github.com/Blaizzy/mlx-audio/blob/main/README.md>, retrieved 2026-11-12.

2. Multi-segment output is saved as numbered files unless --join_audio is passed.

   > By default, when generation yields multiple segments, mlx-audio saves numbered files such as `audio_000.wav` and `audio_001.wav`. Use `--join_audio` to save one combined file instead.

   Locator: README.md, Quick Start, Command Line, note under the examples. Source: <https://github.com/Blaizzy/mlx-audio/blob/main/README.md>, retrieved 2026-11-12.

3. Stable Audio 3 is listed for sound effects or music, 44.1 kHz stereo, up to 120 seconds.

   > | **Stable Audio 3** | Text to sound effects or music, 44.1 kHz stereo, up to 120 seconds | EN |

   Locator: README.md, Supported Models, Music Generation table. Source: <https://github.com/Blaizzy/mlx-audio/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Blaizzy/mlx-audio README (install, quick start, supported models, server, requirements) against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `35ebe7265230f5bec319a7f9e23ef3972e53f7b8cb619c8928b24f542a209a46`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2024-11-27
- default_branch: main
- fetched_at: 2026-11-12
- forks: 793
- last_activity: 2026-11-11
- licence: MIT
- moved_to: Neywa-Labs/mlx-audio
- open_issues: 94
- sources: https://api.github.com/repos/Blaizzy/mlx-audio, https://api.github.com/repositories/895253710, https://skills.sh/api/search?q=mlx-audio
- stars: 8251

## Related

- integrates_with: [Kokoro-82M](../model/hexgrad__kokoro.md)
- integrates_with: [Stable Audio Open](../model/stabilityai__stable-audio.md) - Lists Stable Audio 3 small-sfx and small-music MLX ports.
- alternative_to: [mlx-video](blaizzy__mlx-video.md) - Same author; video models instead of audio.

## Referenced by

- [Stable Audio Open](../model/stabilityai__stable-audio.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
