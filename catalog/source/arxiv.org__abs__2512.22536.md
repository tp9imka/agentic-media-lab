# CoAgent: Collaborative Planning and Consistency Agent for Coherent Video Generation

`source:arxiv.org/abs/2512.22536` - source - <https://arxiv.org/abs/2512.22536>

A plan-synthesize-verify-edit pipeline: a Storyboard Planner writes shot plans, a Global Context Manager keeps entity memory, Wan2.1 renders each shot, a Verifier Agent scores it and triggers regeneration below a threshold, and a pacing-aware editor sets rhythm and transitions.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Review loop](../../docs/glossary.md#review-loop), [Consistency](../../docs/glossary.md#consistency), [Evaluation](../../docs/glossary.md#evaluation)

Also known as: CoAgent

Tags: verifier, regeneration, wan

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It reports how often the verify-and-regenerate loop fires and how many retries it needs, which is the number to budget against.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

The clip model is open-weights Wan2.1, but the planner (Gemini2.5-Flash) and verifier and memory (GPT-4o) are paid APIs. Attempts are capped at N=3, counting the first one; the paper reports 98% of shots pass within it. Scores are VBench and VideoScore, which measure per-clip quality more than cross-shot identity (see source:arxiv.org/abs/2605.15199). No code link was found in the paper text read here.

## Claims

1. 72% of shots pass the verifier first time; the rest need about 1.4 more generations on average.

   > Pass Rate: On average, 72% of shots pass on the first attempt

   Locator: arXiv 2512.22536 HTML, 7.3 Regeneration Efficiency Analysis. Source: <https://arxiv.org/html/2512.22536>, retrieved 2026-11-12.

2. Wrapping Wan2.1 in the agent loop raised its VideoScore visual quality from 2.788 to 2.953 and text-video alignment from 2.550 to 2.731.

   > we improve Visual Quality from 2.788 to 2.953 (+5.9%) and Text-Video Alignment from 2.550 to 2.731 (+7.1%)

   Locator: arXiv 2512.22536 HTML, comparison with foundation models, Table 2. Source: <https://arxiv.org/html/2512.22536>, retrieved 2026-11-12.

3. The authors say the system still makes physics errors such as objects passing through each other.

   > the system occasionally produces ”physics hallucinations,” such as solid objects passing through one another.

   Locator: arXiv 2512.22536 HTML, 8.2 Limitations. Source: <https://arxiv.org/html/2512.22536>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `dd87e6ffcc2d98be97bd5dfbe3362a9ed7a589200c9c2647e5cb69f826af1277`
- Citation: type article; author Qinglin Zeng, Kaitong Cai, Ruiqi Chen, Qinhan Lv, Keze Wang; issued 2025-12-27; container_title arXiv preprint; doi 10.48550/arXiv.2512.22536; url https://arxiv.org/abs/2512.22536; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
