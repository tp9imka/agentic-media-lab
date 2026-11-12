# EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation

`source:arxiv.org/abs/2605.15199` - source - <https://arxiv.org/abs/2605.15199>

A benchmark of 140 episodes (2,491 shots) from real narrative media that tracks characters, objects and locations across up to 50 shots, with a memory-based baseline.

Concepts: [Consistency](../../docs/glossary.md#consistency), [Evaluation](../../docs/glossary.md#evaluation), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines)

Tags: multi-shot

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Multi-shot clips made by chaining generated shots lose their characters as the gap between appearances grows; this paper measures that drift and names the fix that scored best.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

Plan shots so a recurring character or prop is regenerated from a stored reference image, not from the previous shot or a text description; that is what the paper's best method does. The abstract does not name which hosted models were tested, so it does not rank Seedance, Wan or others; the full paper and project page were not opened. No hub record claims long-range consistency outright, so this is linked by concept, not by 'contradicts'.

## Claims

1. In existing methods, entity consistency across shots falls sharply as the distance between an entity's appearances grows.

   > Experiments show that cross-shot entity consistency degrades sharply with recurrence distance in existing methods,

   Locator: arXiv abstract, results. Source: <https://arxiv.org/abs/2605.15199>, retrieved 2026-11-12.

2. Storing a verified reference per entity before generation gave the highest character fidelity among the methods tested.

   > explicit per-entity memory yields the highest character fidelity (Cohen's d = +2.33) and presence among methods evaluated.

   Locator: arXiv abstract, results. Source: <https://arxiv.org/abs/2605.15199>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. arXiv abstract page against the two claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `ec0d448d33ad87d10bec3b057f730ff5cc5fb429133697a1a1df663fe3bc3388`
- Citation: type article; doi 10.48550/arXiv.2605.15199; url https://arxiv.org/abs/2605.15199; accessed 2026-11-12
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
