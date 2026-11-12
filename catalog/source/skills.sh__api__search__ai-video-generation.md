# skills.sh search results for 'ai-video-generation': cloned listings on new repos

`source:skills.sh/api/search/ai-video-generation` - source - <https://skills.sh/api/search?q=ai-video-generation&limit=30>

The skills.sh search API returns the same 'ai-video-generation' skill under many owners. Most of the top listings sit in repos created between August and October 2026, pushed seconds after creation, and the skill text credits inference.sh.

Concepts: [Popularity and trust](../../docs/glossary.md#popularity-and-trust), [Agent Skills](../../docs/glossary.md#agent-skills), [Hosted video models](../../docs/glossary.md#hosted-video-models)

Tags: install-counts, cloned-skills, supply-chain

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A reader who sorts video skills by installs will land on these copies first; the listing itself shows that install rank is not evidence of quality or of who maintains the skill.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Install counts are not copied here; data/observed.json carries them. Read on 2026-11-12: the top seven listings point to repos created 2026-08-12 to 2026-10-06, and the listing under the inference-sh org itself ranks far below its copies. The 101-skills copy tells the agent to install the belt CLI, whose install page starts with a curl-pipe-to-shell command, and to run `belt login`, which needs an inference.sh account; generation is paid per model on inference.sh (prices not checked). It lists Veo 3.1 apps; whether inference.sh still serves them after Veo 3.1 left the Gemini API was not checked. Do not install any of the copies; if you want this skill, read the inference-sh/skills original and compare. Other copies (for example the gencraft-labs one) route to a different vendor CLI (runcomfy), so the same name does not mean the same code. Only the 101-skills SKILL.md was read in full.

## Claims

1. The same skill id is listed under many unrelated owners, including the inference-sh org that the skill text names.

   > "id": "inference-sh/skills/ai-video-generation",

   Locator: skills.sh /api/search response, skills[] entry. Source: <https://skills.sh/api/search?q=ai-video-generation&limit=30>, retrieved 2026-11-12.

2. The top-listed copy's repo was created on 2026-08-31 and last pushed nine seconds later.

   > 101-skills/superpowers created_at=2026-08-31T22:58:44Z pushed_at=2026-08-31T22:58:53Z fork=false parent=-

   Locator: GitHub REST repos/101-skills/superpowers, fields created_at and pushed_at. Source: <https://api.github.com/repos/101-skills/superpowers>, retrieved 2026-11-12.

3. The copy requires the inference.sh CLI and points the agent at a remote install page, whose first option pipes a downloaded script to the shell.

   > > Requires inference.sh CLI (`belt`). [Install instructions](https://raw.githubusercontent.com/inference-sh/skills/refs/heads/main/cli-install.md)

   Locator: 101-skills/superpowers tools/video/ai-video-generation/SKILL.md, section Quick Start. Source: <https://github.com/101-skills/superpowers/blob/main/tools/video/ai-video-generation/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills.sh search API JSON, GitHub repo metadata for seven listed repos, the 101-skills SKILL.md and the linked cli-install.md
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `726fc1f9062eb05ac6f6d568f552b892972bb9d1cc48bcbf563d24e42823afad`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- extends: [skills.sh docs: how the leaderboard ranks skills and what audits cover](skills.sh__docs.md) - The counting rule that lets copies outrank the original.
- integrates_with: [Veo 3.1](../model/google__veo-3.1.md) - The skill lists Veo 3.1 apps; availability via inference.sh not checked.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
