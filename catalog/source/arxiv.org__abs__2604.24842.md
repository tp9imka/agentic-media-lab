# Co-Director: Agentic Generative Video Storytelling (arXiv 2604.24842)

`source:arxiv.org/abs/2604.24842` - source - <https://arxiv.org/abs/2604.24842>

A paper on short ad generation with agents: a pre-production agent writes brief, storyline and storyboard, a production agent makes keyframes, clips and audio, and an LLM judge scores each storyline before it is used.

Concepts: [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Review loop](../../docs/glossary.md#review-loop)

Tags: shot-planning, hook, ads

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the closest paper to the reader's job, a 12-second multi-shot ad, and its judge rubric scores the hook in the first 1-2 seconds.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Reuse two of its fixed choices: four shots for a 12-second spot, and a refinement loop capped at three retries. The storyline judge rubric in the appendix can be adapted as a pre-render check. The pipeline runs on Google hosted models (Gemini 3 Pro, Veo 3.1 and others), so a replica costs per call; cost was not checked. Authors' own evaluation, not reproduced here.

## Claims

1. The final videos are four shots totalling 12 seconds.

   > Final videos feature 4 shots totaling 12 seconds.

   Locator: HTML, section on implementation details. Source: <https://arxiv.org/html/2604.24842>, retrieved 2026-11-12.

2. Local refinement is capped at three retries.

   > and local refinement is capped at 3 retries.

   Locator: HTML, section on implementation details. Source: <https://arxiv.org/html/2604.24842>, retrieved 2026-11-12.

3. The storyline judge asks whether the story grabs attention within the first 1-2 seconds.

   > Does the story immediately grab attention within the first 1-2 seconds?

   Locator: HTML, appendix, storyline evaluation prompt, Hook Quality (0-20 pts). Source: <https://arxiv.org/html/2604.24842>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. arXiv abstract page and HTML full text against the claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `fe095fe3b10e4ea0c203355da5b0104aec5bd34dc26ff158abac904f087b0446`
- Citation: type article; author Yale Song, Yiwen Song, Nick Losier, Nathan Hodson, Ye Jin, Rhyard Zhu, Yan Xu, Daniel Vlasic, Carina Claassen, Jasmine Leon, Khanh G. LeViet, Zack Chomyn, Joe Timmons, Brett Slatkin, Scott Penberthy, Tomas Pfister; issued 2026; container_title arXiv; url https://arxiv.org/abs/2604.24842; accessed 2026-11-12
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [ViMax: Agentic Video Generation (arXiv 2606.07649)](arxiv.org__abs__2606.07649.md)
- depends_on: [Veo 3.1](../model/google__veo-3.1.md)

## Referenced by

- [ViMax: Agentic Video Generation (arXiv 2606.07649)](arxiv.org__abs__2606.07649.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
