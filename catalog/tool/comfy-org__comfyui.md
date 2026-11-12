# ComfyUI

`tool:comfy-org/comfyui` - tool - <https://github.com/Comfy-Org/ComfyUI>

A node-graph runtime for image and video models, with a local server. comfy-cli installs it and submits workflow JSON to it from the terminal.

Concepts: [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Local video models](../../docs/glossary.md#local-video-models), [Image models](../../docs/glossary.md#image-models), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines)

Also known as: comfyanonymous/ComfyUI, comfy-cli, comfy run

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Many model vendors ship ComfyUI workflows first, and comfy-cli gives an agent a command to run them locally on a Mac.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | framework |
| agents | claude-code, cursor |
| levers | gen-model-craft, orchestration, asset |
| cost | mixed |

On a Mac it runs on PyTorch MPS, and the README asks for a nightly PyTorch build. comfy-cli mixes local and paid paths: comfy setup also offers Comfy Cloud sign-in, comfy generate calls hosted partner models for credits, and comfy run --where cloud spends credits. Keep runs on --where local. The bundled default text-to-image graph needs an SD1.5 checkpoint that comfy-cli does not download. Which nodes work on MPS was not checked.

## Claims

1. ComfyUI documents an install on Apple Silicon Macs (M1 to M4).

   > You can install ComfyUI in Apple Mac silicon (M1, M2, M3 or M4) with any recent macOS version.

   Locator: ComfyUI README.md, section Others > Apple Mac silicon. Source: <https://github.com/Comfy-Org/ComfyUI/blob/master/README.md>, retrieved 2026-11-12.

2. comfy-cli runs workflows against a local ComfyUI server and converts UI-format JSON.

   > Run workflows against a local ComfyUI server, including auto-conversion of UI-format JSON

   Locator: comfy-cli README.md, feature list. Source: <https://github.com/Comfy-Org/comfy-cli/blob/main/README.md>, retrieved 2026-11-12.

3. Every comfy-cli command can emit structured JSON output for an agent.

   > Agent-friendly: every command emits structured `--json` envelopes

   Locator: comfy-cli README.md, feature list. Source: <https://github.com/Comfy-Org/comfy-cli/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. ComfyUI README (Apple Mac silicon section) and comfy-cli README against the claims
- Next check due: 2027-02-10
- Licence: GPL-3.0
- URL status: live
- Saved source sha256: `6af0d57adb5acfde5884700af74dd8e7ebceb96fefb0ae44be6ec40f485c2963`
- Lane: local-models

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2023-01-17
- default_branch: master
- fetched_at: 2026-11-12
- forks: 17446
- last_activity: 2026-11-12
- licence: GPL-3.0
- open_issues: 5529
- sources: https://api.github.com/repos/Comfy-Org/ComfyUI, https://skills.sh/api/search?q=ComfyUI
- stars: 146436

## Related

- alternative_to: [MFLUX](mflux-community__mflux.md)
- integrates_with: [Vimoo 1.0](../model/vimoo-ai__vimoo-1.0.md)

## Referenced by

- [Vimoo 1.0](../model/vimoo-ai__vimoo-1.0.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
