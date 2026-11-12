# SGA: Plug&Play Geometric Verification for Educational Video Synthesis

`source:arxiv.org/abs/2607.18116` - source - <https://arxiv.org/abs/2607.18116>

KAUST paper: a module for Manim pipelines that partially executes the LLM's code, builds a scene graph of object boxes, finds overlaps and off-canvas objects, and asks the LLM to fix them, without rendering. Tested inside Code2Video and TheoremExplainAgent.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Code-driven video](../../docs/glossary.md#code-driven-video), [Evaluation](../../docs/glossary.md#evaluation)

Also known as: Symbolic Geometric Agent, MVQS, MMMC-Code

Tags: manim, layout-check

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A cheaper check than a VLM looking at rendered frames for the commonest Manim defect, overlapping labels, with runtime numbers.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

Applies to 2D Manim only, and it does not catch timing errors such as a label appearing late. The idea transfers: check bounding boxes in code before a full render. Its MVQS metric is the authors' own proxy; human raters preferred SGA in 84.4% of pairs versus the raw output. Whether code is released was not checked; the paper links a project page.

## Claims

1. Inside Code2Video with GPT-5.1 it reached MVQS 73.11, 16.1% above the raw baseline, and improved 7 of 8 setups.

   > SGA achieves a peak MVQS of 73.11 (Code2Video + GPT-5.1), corresponding to a 16.1% relative improvement over the raw baseline, and improves MVQS in 7 of 8 backbone x pipeline configurations.

   Locator: arXiv 2607.18116 abstract. Source: <https://arxiv.org/abs/2607.18116>, retrieved 2026-11-12.

2. Code2Video with GPT-5.1 takes 6.4 minutes per sample, and 8.8 minutes with a VLM layout critic.

   > At the pipeline level, using GPT-5.1 as the backbone, the baseline Code2Video system requires 6.4 minutes per sample and increases to 8.8 minutes when augmented with a VLM layout critic.

   Locator: arXiv 2607.18116 HTML, efficiency analysis. Source: <https://arxiv.org/html/2607.18116>, retrieved 2026-11-12.

3. It only handles 2D primitives in Manim.

   > First, the current implementation is specialized for 2D geometric primitives within the Manim engine

   Locator: arXiv 2607.18116 HTML, Limitations. Source: <https://arxiv.org/html/2607.18116>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. abstract, efficiency section and limitations
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `435d71c8983de976a90687c6242c5ef0ca401ee6359d0ec50f617fc57cab7f60`
- Citation: type article; author Jhon Lopez, Carlos Hinojosa, Bernard Ghanem; issued 2026-07-20; container_title arXiv preprint; doi 10.48550/arXiv.2607.18116; url https://arxiv.org/abs/2607.18116; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

- extends: [Code2Video](../tool/showlab__code2video.md)
- integrates_with: [Manim Community Edition](../tool/manimcommunity__manim.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
