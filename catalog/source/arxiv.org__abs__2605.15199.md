# EntityBench: entity-consistent long-range multi-shot video benchmark

`source:arxiv.org/abs/2605.15199` - source - <https://arxiv.org/abs/2605.15199>

A benchmark of 140 episodes and 2,491 shots from real narrative media, with per-shot schedules of which characters, objects and locations appear. It scores quality, prompt following and cross-shot consistency with 51 metrics and a fidelity gate, and adds EntityMem, a per-entity memory baseline.

Concepts: [Evaluation](../../docs/glossary.md#evaluation), [Consistency](../../docs/glossary.md#consistency), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines)

Also known as: EntityBench, EntityMem

Tags: multi-shot, benchmark, entity-memory

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It shows that a high VBench-style score says little about whether the right character keeps appearing, which matters when picking a pipeline by its reported numbers.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Use it to read other papers' claims: consistency drops as the gap between appearances grows, and embedding similarity (DINOv2) can rate a repeated face as consistent while an LLM judge says it is the wrong person. The authors' own memory baseline loses on objects (a 'sticker look'). Code and data are said to be released; the repo was not opened here.

## Claims

1. The benchmark has 140 episodes and 2,491 shots taken from real narrative media.

   > We introduce EntityBench, a benchmark of 140 episodes (2,491 shots) derived from real narrative media

   Locator: arXiv 2605.15199 abstract. Source: <https://arxiv.org/abs/2605.15199>, retrieved 2026-11-12.

2. One method won every highlighted VBench dimension yet had the lowest character presence and character accuracy.

   > CineTrans wins all four highlighted VBench dimensions (subject_consistency 0.97, imaging_quality 68.6) yet has the lowest character presence (0.80) and the worst LLM character accuracy (0.09) of all four methods.

   Locator: arXiv 2605.15199 HTML, F.4 Trade-offs and Limitations. Source: <https://arxiv.org/html/2605.15199>, retrieved 2026-11-12.

3. Code and data are stated to be available.

   > Code and data are available at this https URL.

   Locator: arXiv 2605.15199 abstract. Source: <https://arxiv.org/abs/2605.15199>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. abstract and appendix F.4 trade-offs
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `adb3d6fcadf02ac06c45c468f3bc8fa3f36aabbdf1a743c3d26fffc3ab874b25`
- Citation: type article; author Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez; issued 2026-05-14; container_title arXiv preprint; doi 10.48550/arXiv.2605.15199; url https://arxiv.org/abs/2605.15199; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

- contradicts: [VBench-2.0: benchmark suite for intrinsic faithfulness](arxiv.org__abs__2503.21755.md) - Per-clip VBench-family scores did not predict entity consistency here.

## Referenced by

- [GroundShot: Entity-Grounded Shot Scheduling for multi-shot video (and GroundBench)](arxiv.org__abs__2606.20799.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
