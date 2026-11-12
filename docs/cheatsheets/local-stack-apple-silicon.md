---
id: guide:local-stack-apple-silicon
title: What runs free on an Apple Silicon Mac
summary: Local models and runtimes per stage with their documented Apple Silicon path, stated memory and the licence clause that matters, read, not run.
use_when: "Use this page when you want to make video, images, speech, music or captions on an Apple Silicon Mac without a paid service and need to know what has a documented path and which licences bite."
concepts: [concept:local-video-models, concept:image-models, concept:audio-and-captions, concept:licences-and-territory, concept:cost]
last_reviewed: 2026-11-12
---

# What runs free on an Apple Silicon Mac

Tables by stage for a developer with an Apple Silicon Mac who wants to stay off paid services. Every row is read, not run: the hub has measured no model on a Mac. Memory figures are stated by the project, on the machine they name. Read the stage you need, then "Licence traps" before any client or monetised work.

Contents: [Video models](#video-models), [Image models](#image-models), [Speech](#speech), [Music](#music), [Captions](#captions), [Upscale](#upscale), [Runtimes](#runtimes), [Licence traps](#licence-traps), [What nobody has published](#what-nobody-has-published), [Not covered yet](#not-covered-yet).

## Video models

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [Wan 2.2] | Third-party, via [mlx-video]: "T2V-14B, TI2V-5B, and I2V-14B models" | Mac: none; Wan's card lists 24 GB VRAM on NVIDIA for the 5B command | permissive: "licensed under the Apache 2.0 License" | no - read, not run |
| [LTX-2] | "Macs use PyPI (MPS on Apple Silicon)" | No Mac figure published | commercial-threshold: "annual revenues of at least $10,000,000" need a paid licence | no - read, not run |
| [Vimoo 1.0] | "TI2V Distilled for MLX on Apple Silicon" (Lite only) | None stated | permissive: "Commercial use, modification, and redistribution are permitted" | no - read, not run |
| [MiniMax H3] | [Draw Things]: "Add support for MiniMax H3 series models" | None stated | territory-restricted, see traps | no - read, not run |

## Image models

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [Z-Image] | [mflux], 8-bit | "Peak, one image" 7.5 GB, 64 GB Mac | permissive: card tag "license: apache-2.0" | no - read, not run |
| [FLUX 3 Image Klein] | [mflux] | 22.8 GB peak at `-q 8`, M4 Pro 64 GB | commercial-threshold, quoted second-hand via mflux | no - read, not run |
| [Qwen-Image] | [mflux], bf16 | "Peak memory is ~46 GB" | non-commercial, see traps | no - read, not run |

## Speech

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [Kokoro] | "`PYTORCH_ENABLE_MPS_FALLBACK=1` to enable GPU acceleration" | None published | permissive: "This is an Apache-licensed model" | no - read, not run |
| [Piper] | No Apple Silicon note found | Not stated | Per voice; see traps | no - read, not run |

## Music

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [ACE-Step] | macOS scripts set "`--backend mlx`" | GPU table only | permissive: "Generated music can be used for commercial purposes." | no - read, not run |
| [Stable Audio Open] | None documented on the 1.0 card | Not stated | commercial-threshold: under "$1M" of annual revenue | no - read, not run |
| [MusicGen] | Not checked | Not stated | non-commercial: weights "CC-BY-NC 4.0" | no - read, not run |

## Captions

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [whisper.cpp] | "runs fully on the GPU via Metal" | large model "~3.9 GB" | MIT, collected | no - read, not run |
| [mlx-whisper] | "Speech recognition with Whisper in MLX." | Not in the README | MIT, collected | no - read, not run |
| [WhisperX] | CPU only on a Mac | Not stated | BSD-2-Clause, collected | no - read, not run |

## Upscale

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [SeedVR2] | [mflux], images in a folder, not video files | None published | permissive: "licensed under the Apache 2.0" | no - read, not run |

## Runtimes

| Record | Documented Apple Silicon path | Memory the authors state | Licence class and clause | Measured here? |
|---|---|---|---|---|
| [mflux] | "locally on your Mac in native MLX" | In per-model READMEs | MIT, collected | no - read, not run |
| [mlx-video] | "macOS with Apple Silicon" | None in the README | MIT, collected | no - read, not run |
| [MLX-Audio] | "Built on MLX" | None for an M3 Max | MIT, collected; each model keeps its own | no - read, not run |
| [ComfyUI] | "Apple Mac silicon (M1, M2, M3 or M4)" | Not stated | GPL-3.0, collected | no - read, not run |
| [Draw Things] | App; gRPC server offload | Not stated | Not collected | no - read, not run |

## Licence traps

- Territory exclusion, [MiniMax H3]: "“Excluded Territories” means the European Union, the United Kingdom, the Republic of Korea and the United States of America."
- Revenue threshold, [LTX-2]: "Entities with annual revenues of at least $10,000,000 (the "Commercial Entities") are required to obtain a paid license for any use". [FLUX 3 Image Klein], per mflux: "less than US$5M gross annualized revenue, including affiliates". [Stable Audio Open]: "individuals or organizations that generate under $1M".
- Research-only, [Qwen-Image]: the licence defines non-commercial as "for research or evaluation purposes only."
- Voice corpus, [Piper]: `en_US-lessac-medium` was trained on a corpus whose licence "excludes commercial use of the resulting synthesis." A copy downloaded before the late-2026 retrain "does not qualify" for the commercial-use list.
- Non-commercial weights, [MusicGen]: "released under the CC-BY-NC 4.0 license".

## What nobody has published

No record holds an M3 Max timing for any model. Wan and mlx-video publish no Mac timing ([Wan 2.2], [mlx-video]). For MiniMax H3 the one published timing is minutes per denoising step on a larger machine ([MiniMax H3]). Mac figures that do exist are for other chips: about 1.5 s per step on an M5 Max ([Qwen-Image]) and 7.0 s per step on an M4 Pro ([FLUX 3 Image Klein]). The hub's one M3 Max run was a code renderer, run here once ([worked example](../../examples/hyperframes-vs-remotion/README.md)). M3 Max timings are a gap the hub intends to measure.

[Wan 2.2]: ../../catalog/model/wan-ai__wan2.2.md
[LTX-2]: ../../catalog/model/lightricks__ltx-2.md
[Vimoo 1.0]: ../../catalog/model/vimoo-ai__vimoo-1.0.md
[MiniMax H3]: ../../catalog/model/minimaxai__minimax-h3.md
[Z-Image]: ../../catalog/model/tongyi-mai__z-image.md
[FLUX 3 Image Klein]: ../../catalog/model/black-forest-labs__flux-3-image-klein.md
[Qwen-Image]: ../../catalog/model/qwen__qwen-image.md
[Kokoro]: ../../catalog/model/hexgrad__kokoro.md
[Piper]: ../../catalog/tool/ohf-voice__piper1-gpl.md
[ACE-Step]: ../../catalog/model/ace-step__ace-step.md
[Stable Audio Open]: ../../catalog/model/stabilityai__stable-audio.md
[MusicGen]: ../../catalog/model/facebook__musicgen.md
[whisper.cpp]: ../../catalog/tool/ggml-org__whisper.cpp.md
[mlx-whisper]: ../../catalog/tool/ml-explore__mlx-examples__whisper.md
[WhisperX]: ../../catalog/tool/m-bain__whisperx.md
[SeedVR2]: ../../catalog/model/bytedance-seed__seedvr.md
[mflux]: ../../catalog/tool/mflux-community__mflux.md
[mlx-video]: ../../catalog/tool/blaizzy__mlx-video.md
[MLX-Audio]: ../../catalog/tool/blaizzy__mlx-audio.md
[ComfyUI]: ../../catalog/tool/comfy-org__comfyui.md
[Draw Things]: ../../catalog/tool/drawthings.ai.md

## Not covered yet

- M3 Max timings and peak memory for every model above.
- Mac memory figures for Wan 2.2, LTX-2, Vimoo, MiniMax H3, Kokoro and ACE-Step.
- A documented Mac path for Piper, Stable Audio Open 1.0 and MusicGen.
- The FLUX Kommunity License text itself (login required).
- Frame-to-frame consistency of upscaling a clip frame by frame with SeedVR2.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
