# Stable Audio Open

`model:stabilityai/stable-audio` - model - <https://huggingface.co/stabilityai/stable-audio-open-1.0>

Stability AI's open-weight text-to-audio models. Stable Audio Open 1.0 makes up to 47 seconds of 44.1 kHz stereo from a text prompt and is stronger on sound effects than music. Stable Audio 3 checkpoints exist on Hugging Face behind a gate.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Models](../../docs/glossary.md#models)

Also known as: stable-audio-open-1.0, Stable Audio 3, stable-audio-tools

Tags: sound-effects, music, stability

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the local route to generated sound effects and ambience for a clip, under a licence that allows commercial use below a revenue line.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | music |
| access | weights |
| apple_silicon | not-checked |
| licence_class | commercial-threshold |

Weights are gated: a Hugging Face login and accepting the licence form are needed before download, so an agent cannot fetch them unattended. Commercial use is free under USD 1M annual revenue; above it an Enterprise licence is needed. Outputs belong to the user. Keep clips under 47 s per generation and plan crossfades for longer beds. No Mac path is documented on the 1.0 card; mlx-audio lists Stable Audio 3 MLX ports, whose card was not read here.

## Claims

1. Stable Audio Open 1.0 generates up to 47 seconds of 44.1 kHz stereo audio.

   > Stable Audio Open 1.0 generates variable-length (up to 47s) stereo audio at 44.1kHz from text prompts.

   Locator: Model card, Model Details. Source: <https://huggingface.co/stabilityai/stable-audio-open-1.0>, retrieved 2026-11-12.

2. The card says it is better at sound effects and field recordings than music.

   > The model is better at generating sound effects and field recordings than music.

   Locator: Model card, Limitations. Source: <https://huggingface.co/stabilityai/stable-audio-open-1.0>, retrieved 2026-11-12.

3. The Community License allows commercial use for individuals and organisations under USD 1M annual revenue.

   > The Stability AI Community License allows for research, non-commercial, and commercial use of the Core Models for individuals or organizations that generate under $1M (or local currency equivalent) of annual revenue, regardless of the source of that revenue.

   Locator: stability.ai/license, FAQ. Source: <https://stability.ai/license>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. stable-audio-open-1.0 model card page, stability.ai/license FAQ and the Stability AI Community License Agreement page against the claims; the stable-audio-3 card was gated and not read
- Next check due: 2026-12-12
- Licence: other
- URL status: live
- Saved source sha256: `a1b3f236e09b21be58ad3e03ab864b4d2090c0c292dc94cb62905f0f253717fe`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- created: 2024-05-24
- fetched_at: 2026-11-12
- gated: auto
- hf_downloads: 24904
- hf_likes: 1949
- last_activity: 2025-06-19
- licence: other
- sources: https://huggingface.co/api/models/stabilityai/stable-audio-open-1.0

## Related

- alternative_to: [ACE-Step 1.5](ace-step__ace-step.md) - ACE-Step is stronger for songs; Stable Audio Open for effects.
- integrates_with: [MLX-Audio](../tool/blaizzy__mlx-audio.md)

## Referenced by

- [MusicGen and AudioGen (AudioCraft)](facebook__musicgen.md) (alternative_to)
- [MLX-Audio](../tool/blaizzy__mlx-audio.md) (integrates_with)
- [Freesound API](../tool/freesound.org.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
