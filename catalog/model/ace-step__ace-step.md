# ACE-Step 1.5

`model:ace-step/ace-step` - model - <https://github.com/ace-step/ACE-Step-1.5>

An open music generation model that writes songs with or without lyrics. Version 1.5 has a 2B model and, since 2026-04, a 4B XL model.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: ACE-Step, ACE-Step-1.5, acestep-v15, ACE-Step 1.5 XL

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives a local soundtrack with a stated permission for commercial use of the output, and its macOS scripts use MLX.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| modes | music |
| access | weights |
| apple_silicon | documented |
| licence_class | permissive |

An agent can start the REST API server and post requests to localhost:8001. The VRAM table in the README is for GPUs; no memory figure for Macs is given. The start scripts check for updates at launch and can install uv; read them before running. The disclaimer asks users to check output for similarity to protected styles.

## Claims

1. The macOS scripts select the MLX backend on Apple Silicon and fall back to PyTorch elsewhere.

   > The macOS scripts automatically set `ACESTEP_LM_BACKEND=mlx` and `--backend mlx` for native Apple Silicon acceleration, and fall back to PyTorch backend on non-arm64 machines.

   Locator: docs/en/INSTALL.md, section macOS (Apple Silicon / MLX). Source: <https://github.com/ace-step/ACE-Step-1.5/blob/main/docs/en/INSTALL.md>, retrieved 2026-11-12.

2. A REST API server listens on port 8001 next to the Gradio UI on 7860.

   > Open http://localhost:7860 (Gradio) or http://localhost:8001 (API).

   Locator: README.md, section Quick Start. Source: <https://github.com/ace-step/ACE-Step-1.5/blob/main/README.md>, retrieved 2026-11-12.

3. The model card states that generated music can be used commercially.

   > Trained on legally compliant datasets. Generated music can be used for commercial purposes.

   Locator: acestep-v15-xl-turbo model card, feature list. Source: <https://huggingface.co/ACE-Step/acestep-v15-xl-turbo/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. ACE-Step-1.5 README, docs/en/INSTALL.md and the xl-turbo model card against the claims
- Next check due: 2026-12-12
- Licence: MIT
- URL status: live
- Saved source sha256: `7c4225f3d011098525004ba0cf0222941805d538c6c0d116ce3d3b1032a5e74c`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-09-04
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1944
- installs: 202
- installs_by_skill: {"acestep": 120, "acestep-docs": 78, "acestep-lyrics-transcription": 69, "acestep-simplemv": 79, "acestep-songwriting": 202, "acestep-thumbnail": 27}
- last_activity: 2026-11-08
- licence: MIT
- open_issues: 164
- registry: skills.sh
- sources: https://api.github.com/repos/ace-step/ACE-Step-1.5, https://skills.sh/api/search?q=ACE-Step-1.5
- stars: 14672

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
