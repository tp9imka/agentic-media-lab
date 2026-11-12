# WorldJen: end-to-end multi-dimensional benchmark for generative video models

`source:arxiv.org/abs/2605.03475` - source - <https://arxiv.org/abs/2605.03475>

A video-model benchmark that replaces yes/no VQA with Likert questionnaires graded by a VLM at native resolution, uses prompts that test up to 16 dimensions at once, and checks the VLM ranking against a blind human preference study.

Concepts: [Evaluation](../../docs/glossary.md#evaluation), [Review loop](../../docs/glossary.md#review-loop)

Also known as: WorldJen

Tags: benchmark, vlm-judge

**Badge:** unverified (`unverified`): checked by skim; downgraded one step: tiny-sample.

**Why:** It names a specific weakness of VBench-2.0 that matters if a pipeline uses a VLM as its own checker: yes-bias and low-resolution frames.

**Last checked:** 2026-11-12, skim, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: low. Level: advanced. Maturity: -.

The human study is 7 annotators over 50 prompts and 6 models, so the Spearman of 1.000 is agreement on three tiers across six models, not a fine ranking. Useful as a prompt-design idea for a VLM checker (ask graded questions, send full-resolution frames). Release of prompts or code was not checked. Only the abstract page was read.

## Claims

1. The authors say binary-VQA benchmarks such as VBench 2.0 show yes-bias and miss temporal failures.

   > Binary Visual Question Answering (VQA) based benchmarks like VBench~2.0 are prone to yes-bias and rely on low-resolution auditors that miss temporal failures.

   Locator: arXiv 2605.03475 abstract. Source: <https://arxiv.org/abs/2605.03475>, retrieved 2026-11-12.

2. The VLM judge's Spearman of 1.000 is read as tier agreement with the human study.

   > The VLM achieves a Spearman $\hat{\rho}=1.000,~p=0.0014$ that is interpreted as tier agreement with the human results.

   Locator: arXiv 2605.03475 abstract. Source: <https://arxiv.org/abs/2605.03475>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth skim. abstract page only
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `e7271a1a6a95c43bdec3ecfbde118b6f57d314d15dc224c4c69634b361726292`
- Badge downgraded: tiny-sample - Human ground truth covers 6 models and 50 prompts.
- Citation: type article; author Karthik Inbasekar, Guy Rom, Omer Shlomovits; issued 2026-05-05; container_title arXiv preprint; doi 10.48550/arXiv.2605.03475; url https://arxiv.org/abs/2605.03475; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

- contradicts: [VBench-2.0: benchmark suite for intrinsic faithfulness](arxiv.org__abs__2503.21755.md) - Disputes the reliability of binary VQA scoring.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
