# Kokoro-82M

`model:hexgrad/kokoro` - model - <https://huggingface.co/hexgrad/Kokoro-82M>

An 82M-parameter text-to-speech model with an inference library, pip install kokoro.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: Kokoro, kokoro TTS, KPipeline

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives an agent a free, local narration voice with commercial use allowed, small enough to run beside a video model.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| modes | tts |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

The Mac route is PyTorch MPS with a CPU fallback for unsupported ops, set by an environment variable. It needs espeak-ng for some languages and out-of-vocabulary English. This record does not cover voice cloning. No memory or speed figure for Macs is published.

## Claims

1. On M1 to M4 Macs, GPU acceleration is turned on with PYTORCH_ENABLE_MPS_FALLBACK=1.

   > On Mac M1/M2/M3/M4 devices, you can explicitly specify the environment variable `PYTORCH_ENABLE_MPS_FALLBACK=1` to enable GPU acceleration.

   Locator: kokoro README.md, section MacOS Apple Silicon GPU Acceleration. Source: <https://github.com/hexgrad/kokoro/blob/main/README.md>, retrieved 2026-11-12.

2. The weights are Apache-licensed and used in commercial APIs.

   > This is an Apache-licensed model, and Kokoro has been deployed in numerous projects and commercial APIs.

   Locator: Kokoro-82M model card, opening note. Source: <https://huggingface.co/hexgrad/Kokoro-82M/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. kokoro GitHub README and Kokoro-82M model card against both claims
- Next check due: 2026-12-12
- Licence: apache-2.0
- URL status: live
- Saved source sha256: `f29dc56bb31eb63c65885b4bbd9c2ddbb4f0e23f1ac97b87c4a5eb70ee3327bd`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2024-12-26
- fetched_at: 2026-11-12
- gated: false
- hf_downloads: 12580963
- hf_likes: 7401
- last_activity: 2025-04-10
- licence: apache-2.0
- sources: https://huggingface.co/api/models/hexgrad/Kokoro-82M

## Related

None.

## Referenced by

- [MLX-Audio](../tool/blaizzy__mlx-audio.md) (integrates_with)
- [Piper (piper1-gpl)](../tool/ohf-voice__piper1-gpl.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
