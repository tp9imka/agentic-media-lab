# Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry

`source:arxiv.org/abs/2605.11418` - source - <https://arxiv.org/abs/2605.11418>

A paper that tests attacks using only SKILL.md text against real ClawHub skills at three stages: registry search, agent selection, and registry moderation.

Concepts: [Popularity and trust](../../docs/glossary.md#popularity-and-trust), [Agent Skills](../../docs/glossary.md#agent-skills)

Tags: supply-chain, prompt-injection

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It shows that the description text of a skill decides whether an agent picks it and whether a registry blocks it, so a well-worded copy can beat the original without any code change.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

Measured on ClawHub mechanisms, not on skills.sh or the Claude Code plugin marketplace, so the numbers do not transfer directly. The arXiv page renders SKILL.md as 'this http URL', which is kept in the quotes. Practical reading: a description that matches your request better is not evidence the skill is better; compare skills by their files, not by how they describe themselves. Only the abstract was read.

## Claims

1. When two skills do the same thing, description wording alone made agents pick the adversarial one in 77.6% of paired trials on average.

   > In Selection, description-only framing biases agents toward functionally equivalent adversarial variants, which are selected in 77.6% of paired trials on average.

   Locator: arXiv abstract, Selection result. Source: <https://arxiv.org/abs/2605.11418>, retrieved 2026-11-12.

2. Wording changes let malicious skills avoid a blocking verdict from registry moderation in 36.5% to 100% of cases.

   > In Governance, semantic evasion strategies cause malicious skills to avoid a blocking verdict in 36.5%-100% of cases.

   Locator: arXiv abstract, Governance result. Source: <https://arxiv.org/abs/2605.11418>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. arXiv abstract page against the two claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `a247faa84e2b6a7c42bf04d2c5e7f88ee238546c778381ce5681293f87f3aebd`
- Citation: type article; doi 10.48550/arXiv.2605.11418; url https://arxiv.org/abs/2605.11418; accessed 2026-11-12
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- contradicts: [skills.sh docs: how the leaderboard ranks skills and what audits cover](skills.sh__docs.md) - Registry audits are what skills.sh offers as its safety step; this paper shows audit verdicts on another registry (ClawHub) can be evaded by wording.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
