# GroundShot: Entity-Grounded Shot Scheduling for multi-shot video (and GroundBench)

`source:arxiv.org/abs/2606.20799` - source - <https://arxiv.org/abs/2606.20799>

A training-free agent loop for multi-shot video: it generates the shots that best establish characters, objects and places first, crops each entity from accepted shots into a memory, checks each new shot with a VLM critic, and repairs failures by issue type.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Consistency](../../docs/glossary.md#consistency), [Review loop](../../docs/glossary.md#review-loop), [Local video models](../../docs/glossary.md#local-video-models)

Also known as: GroundShot, GroundBench

Tags: entity-memory, shot-scheduling, vlm-critic

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It turns consistency into a scheduling and reference-management job that works with any reference-to-video model, including an open-weights one.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Primary backend is Vidu (paid); Kling and Wan2.1 + Phantom-14B were also run, so a local route exists if you can run a 14B model (not checked on Apple Silicon). Decisions use GPT-4o and GPT-4.1; entity cropping runs locally with ReferDINO. About 1.2 generations per final shot is the cost to plan for. The authors say it is capped by the generator's own quality. No code or GroundBench release link was found in the text read here.

## Claims

1. Average cost is 1.20 video generations per final shot; 83.1% of shots pass the critic first time.

   > On GroundBench, GroundShot averages 1.20 video generation calls per final shot, with 83.1% of shots passing on the first attempt; regeneration is therefore occasional rather than the default.

   Locator: arXiv 2606.20799 HTML, overhead analysis. Source: <https://arxiv.org/html/2606.20799>, retrieved 2026-11-12.

2. Each failure type has its own repair: identity mismatch => stronger or different reference; missing entities => explicit count in the prompt.

   > For example, identity mismatch can trigger stronger reference conditioning or a different retrieved reference; missing or extra entities can add explicit count and presence instructions to the revised prompt

   Locator: arXiv 2606.20799 HTML, Shot verification. Source: <https://arxiv.org/html/2606.20799>, retrieved 2026-11-12.

3. The gain also held with the open-source Wan2.1 + Phantom backend.

   > The open-source Wan2.1+Phantom setting further indicates that the framework is not tied to commercial backends: even with a weaker open-source backend, the same grounded entity-level memory and shot scheduling yield gains.

   Locator: arXiv 2606.20799 HTML, backend analysis of Table 1. Source: <https://arxiv.org/html/2606.20799>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. abstract, method, implementation, Table 1 text, overhead and conclusion
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `042cbd5fc2402744f644c3b988be9e8494a408b70e15098a8dd677bbc4036995`
- Citation: type article; author Yixuan Lai, Tianjia Shao, Weijia Dou, Siyu Zhu, Jingdong Wang; issued 2026-06-18; container_title arXiv preprint; doi 10.48550/arXiv.2606.20799; url https://arxiv.org/abs/2606.20799; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

- alternative_to: [EntityBench: entity-consistent long-range multi-shot video benchmark](arxiv.org__abs__2605.15199.md) - Both store per-entity references; EntityMem builds them before generation, GroundShot from accepted shots.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
