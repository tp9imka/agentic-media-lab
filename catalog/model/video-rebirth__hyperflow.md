# HyperFlow H3 Flash (Video Rebirth)

`model:video-rebirth/hyperflow` - model - <https://github.com/Video-Rebirth/hyperflow-h3-flash>

Video Rebirth's pruned, INT8 and few-step version of MiniMax-H3: 13.7B parameters instead of about 31B, 4-8 sampling steps without CFG, video with stereo audio in one pass. Ships as a Python package and as GGUF for ComfyUI.

Concepts: [Local video models](../../docs/glossary.md#local-video-models), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Generated footage](../../docs/glossary.md#generated-footage)

Also known as: HyperFlow, hyperflow-h3-flash, HyperFlow H3 Flash

Tags: minimax-h3, quantized, gguf

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It brings MiniMax-H3 class output to a single consumer NVIDIA card with published end-to-end timings. It keeps the MiniMax-H3 territory exclusions, and the README gives no Apple Silicon path.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: low. Level: advanced. Maturity: experimental.

| field | value |
|---|---|
| modes | t2v, i2v |
| access | weights |
| apple_silicon | no-documented-path |
| licence_class | territory-restricted |

On the M3 Max: no documented path. The Python package needs an NVIDIA GPU and CUDA, and the GGUF route is described for ComfyUI on RTX cards; a stable-diffusion.cpp patch exists, but nothing says it was run on Metal. Rent an RTX 4090 or 5090 instead: 5.2 s takes about 1.5-2.5 min there. First run downloads about 90 GB (68 GB with the fp8 text encoder). Weights inherit the MiniMax-H3 licence, so the same EU, UK, Korea and US exclusion applies as on model:minimaxai/minimax-h3. The vendor published the timings; a commenter asks for a quality comparison against the quants and against FastVideo's FastH3, which was not opened here.

## Claims

1. On the vendor's runs, a 5.2 s clip at 6 steps took 8.7 s on 4x B200, 36 s on one H200 and 92 s on one RTX 5090.

   > **Speed (5.2 s clip, 6 steps):** 8.7 s on 4× B200, 36 s on 1× H200, 92 s on 1× RTX 5090.

   Locator: README, intro bullets, Speed. Source: <https://github.com/Video-Rebirth/hyperflow-h3-flash>, retrieved 2026-11-12.

2. The Python package requires an Ampere or newer NVIDIA GPU with CUDA.

   > Python 3.10+, PyTorch 2.6+ with CUDA and Triton (`pip install triton-windows` on native Windows), an Ampere or newer NVIDIA GPU, and `diffusers >= 0.40`.

   Locator: README, Python Package, Install, Requirements. Source: <https://github.com/Video-Rebirth/hyperflow-h3-flash>, retrieved 2026-11-12.

3. The weights are a MiniMax-H3 derivative whose licence does not cover the EU, UK, South Korea or US without MiniMax's authorization.

   > The weights are a derivative of MiniMax-H3 under its Community License, which does not cover the US, EU, UK or South Korea without MiniMax’s authorization.

   Locator: HN Show HN thread 50405263, submitter's first comment, paragraph License. Source: <https://news.ycombinator.com/item?id=50405264>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README (raw) and the Show HN submitter comment against the record; the README License section states the same territory exclusion
- Next check due: 2026-12-12
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `291c0750fdca672cf038b8882763422e4b85730da547e159e4957d555f546d4b`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-11-06
- default_branch: main
- fetched_at: 2026-11-12
- forks: 12
- last_activity: 2026-11-11
- licence: Apache-2.0
- open_issues: 0
- sources: https://api.github.com/repos/Video-Rebirth/hyperflow-h3-flash, https://skills.sh/api/search?q=hyperflow-h3-flash
- stars: 196

## Related

- extends: [MiniMax H3](minimaxai__minimax-h3.md) - A compressed derivative of the MiniMax-H3 transformer under the same community licence.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
