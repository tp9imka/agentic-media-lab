---
id: guide:fact-check
title: Fact-check results
summary: How often the hub's own sentences say more than their sources, measured by an independent checker.
use_when: "Use this page when you need to know how far to trust a record's wording, or which research lanes were least accurate."
concepts: [concept:evaluation, concept:popularity-and-trust]
last_reviewed: 2026-11-12
---

# Fact-check results

What this is: the measured error rate of the hub's records, for anyone deciding how much to
rely on them. Read the summary, then the table, then the caveats.

All numbers on this page come from [evals/factcheck/2026-11-12.json](../evals/factcheck/2026-11-12.json).

## Summary

On 2026-11-12 a different agent tool from the ones that wrote the records compared
112 records with the saved copies of their sources.

- **Quotes: 296 of 296 are verbatim.**
- **Claims: 39 of 296 (13.2%) said more than the source.**
  38 were overstated: a dropped condition, a wider scope. 1 was wrong.
- **Prose** (summaries and fit notes): 1504 statements. 74 overstated,
  22 not in the saved source, 4 wrong. 311 could not be
  checked from the saved source and are not counted as errors.
- **Category fields: 17 of 216 were not backed by the saved source.**

No invented quote and no wrong number was found in a quote. The typical fault is a true
sentence with its limiting clause removed.

## Method

- Checker: codex CLI. Writers: kiro CLI for most lanes, the driver agent for the first seven
  records. The checker got each record and the saved copy of its source, not the writer's notes.
- Unit: the atomic claim. Each got one verdict: supported, overstated, wrong, outdated, or
  not in source. Each quote was checked for being verbatim.
- First a seeded random sample: seed 20261112, 6 records per lane, 70 records,
  181 claims. Sample rate: 13.3%.
- Then every remaining record of the four lanes whose sample rate was over 15%.
- The checker did not open live pages. It judged each record against its own source.

## By lane

| Lane | Records checked | Claims | Not fully supported | Rate | Wrong | Prose findings |
|---|---|---|---|---|---|---|
| automation | 6 of 19 | 16 | 2 | 12.5% | 1 | 6 of 82 |
| contrarian | 11 of 11 | 30 | 5 | 16.7% | 0 | 16 of 142 |
| craft | 18 of 18 | 53 | 10 | 18.9% | 0 | 14 of 214 |
| footage-editing | 6 of 16 | 18 | 0 | 0.0% | 0 | 5 of 122 |
| hosted-models | 4 of 4 | 6 | 0 | 0.0% | 0 | 0 of 22 |
| hosted-models-2 | 6 of 17 | 14 | 2 | 14.3% | 0 | 7 of 79 |
| local-models | 6 of 15 | 17 | 1 | 5.9% | 0 | 1 of 81 |
| pipelines-research | 6 of 15 | 16 | 1 | 6.2% | 0 | 8 of 108 |
| publishing | 22 of 22 | 57 | 11 | 19.3% | 0 | 21 of 286 |
| quality-skills | 6 of 7 | 9 | 0 | 0.0% | 0 | 3 of 58 |
| quality-skills-2 | 6 of 12 | 16 | 2 | 12.5% | 0 | 6 of 95 |
| renderers | 15 of 15 | 44 | 5 | 11.4% | 0 | 13 of 215 |

Lanes checked in full: publishing, craft, contrarian, renderers. The other rows are samples
of 6 to 18 claims, so their rates are rough.

## What was done about it

- First pass: 80 text edits in 50 records.
- Second pass: 35 text edits in 25 records. One finding was
  disputed by the fixer with the source line that supports the original text.
- No quote was changed in either pass.
- Category fields: 17 fields were not backed by the saved source. 2 were corrected (the saved source contradicted them). The rest are true values taken from another page of the same project and are left in place until each field carries its own quoted claim.
- Checked records carry `checked.by: agent:codex`.

## Caveats

- The three lanes still above 15% after a full check are the platform-rules lane, the craft
  standards lane and the "what failed" lane. Their records have been corrected, not re-verified.
- The corrections themselves were made by an agent and reviewed as a diff. They were not
  fact-checked a second time.
- The media-stages lane (audio and image stages) landed after the sample was drawn and is
  not checked.
- Records in the eight lanes under the line that were not sampled are unchecked. Expect about
  one claim in eight of those to overstate its source.
- "Not backed by the saved source" for a field means the one saved file does not show it.

## Not covered yet

- A second, independent check of the corrected text.
- A check of each record against its live page, to catch sources that changed.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
