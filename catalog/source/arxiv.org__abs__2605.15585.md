# See Before You Code: Learning Visual Priors for Spatially Aware Educational Animation Generation (OmniManim)

`source:arxiv.org/abs/2605.15585` - source - <https://arxiv.org/abs/2605.15585>

A paper on LLM-written Manim animations: it reports that rendered output often has overlap, misalignment and broken continuity, and proposes a planner plus post-render repair.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Evaluation](../../docs/glossary.md#evaluation)

Tags: manim, render-check

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It says the main failure of code-driven video cannot be seen by reading the code, which is the case for rendering frames and looking at them before delivery.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Practical reading for Manim, Remotion or HyperFrames: do not accept 'the code ran' as done; render stills at keyframes and the frames between them, because interpolation creates defects the keyframes do not show. The paper's own system is not in the hub and was not checked for code availability; only the abstract was read, so defect rates for baseline models are not recorded here.

## Claims

1. LLM-generated animation code often renders with overlap, misalignment and broken continuity.

   > the resulting renders often exhibit visual defects, including element overlap, misalignment, and broken animation continuity.

   Locator: arXiv abstract, sentence 1. Source: <https://arxiv.org/abs/2605.15585>, retrieved 2026-11-12.

2. These defects cannot be reliably found from the code and only show up after rendering.

   > These defects cannot be reliably detected from the code alone and become apparent only after execution.

   Locator: arXiv abstract, sentence 2. Source: <https://arxiv.org/abs/2605.15585>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. arXiv abstract page against the two claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `2ad20c7459e206d25c75246f9ef71a6d7105a1bef1dbfff557d5d9a140f9a959`
- Citation: type article; doi 10.48550/arXiv.2605.15585; url https://arxiv.org/abs/2605.15585; accessed 2026-11-12
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- evaluated_on: [Manim Community Edition](../tool/manimcommunity__manim.md) - The paper's target renderer.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
