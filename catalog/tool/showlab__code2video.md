# Code2Video

`tool:showlab/code2video` - tool - <https://github.com/showlab/Code2Video>

A three-agent system from Show Lab (NUS) that writes Manim code for educational videos: a Planner builds the storyboard and assets, a Coder writes and auto-fixes the Python, a Critic uses a VLM on rendered frames to fix layout. It ships the MMMC benchmark of 117 topics.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Evaluation](../../docs/glossary.md#evaluation)

Also known as: MMMC benchmark, TeachQuiz

Tags: manim, vlm-critic

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The reference pipeline for agent-written explainer video in code, and the base that later Manim checking work (SGA) is measured on.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | none-stated |
| levers | orchestration, story, review-loop, design |
| cost | paid |

Renders locally with Manim Community v0.19.0, so no video-model fee; the cost is LLM and VLM tokens. It needs an LLM key for Planner and Coder, a Gemini key for the Critic, and optionally an IconFinder key for icons. The SGA paper (source:arxiv.org/abs/2607.18116) measured 6.4 minutes per topic with GPT-5.1 and 8.8 minutes with the VLM critic on. It drives its own scripts, not Claude Code or Codex. Not run here.

## Claims

1. The README says Manim code quality was best with Claude-4-Opus as the LLM.

   > Best Manim code quality achieved with **Claude-4-Opus**.

   Locator: README.md, 2. Configure LLM API Keys. Source: <https://github.com/showlab/Code2Video>, retrieved 2026-11-12.

2. The Critic checks layout with a VLM and visual anchor prompts on the rendered output.

   > (iii) Critic, which leverages vision-language models (VLM) with visual anchor prompts to refine spatial layout and ensure clarity.

   Locator: arXiv 2510.01174 abstract. Source: <https://arxiv.org/abs/2510.01174>, retrieved 2026-11-12.

3. The authors report a 40% gain over direct code generation on their own benchmark.

   > achieving 40% improvement over direct code generation and producing videos comparable to human-crafted tutorials

   Locator: arXiv 2510.01174 abstract. Source: <https://arxiv.org/abs/2510.01174>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README setup and API key sections; paper abstract
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `d5fa6e47c8919f0905b00cdc8eec96d37f92b80b7db497695ae6da62f659cdd9`
- Citation: type article; author Yanzhe Chen, Kevin Qinghong Lin, Mike Zheng Shou; issued 2025-10-01; container_title ICML 2026 (per README); arXiv preprint; doi 10.48550/arXiv.2510.01174; url https://arxiv.org/abs/2510.01174; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-09-29
- default_branch: main
- fetched_at: 2026-11-12
- forks: 303
- last_activity: 2026-08-24
- licence: MIT
- open_issues: 0
- sources: https://api.github.com/repos/showlab/Code2Video, https://skills.sh/api/search?q=Code2Video
- stars: 2370

## Related

- depends_on: [Manim Community Edition](manimcommunity__manim.md)

## Referenced by

- [SGA: Plug&Play Geometric Verification for Educational Video Synthesis](../source/arxiv.org__abs__2607.18116.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
