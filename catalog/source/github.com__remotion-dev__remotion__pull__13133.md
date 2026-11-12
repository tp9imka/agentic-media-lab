# Remotion PR 13133: agents skipped the interactivity skill

`source:github.com/remotion-dev/remotion/pull/13133` - source - <https://github.com/remotion-dev/remotion/pull/13133>

A merged Remotion pull request that explains why an agent with every Remotion skill installed never loaded the interactivity skill: the routing line called it optional, and the publish step removed the links between sibling skills. It rewrites the routing and makes the stripped links name the skill and file.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Plugins](../../docs/glossary.md#plugins), [Code-driven video](../../docs/glossary.md#code-driven-video)

Tags: skill-routing, remotion

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** It is a documented case of an installed skill that an agent never read. The two causes, soft routing wording and links lost in plugin packaging, apply to any skill set a reader writes or installs.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

If you write skills: a sibling-skill link written as a relative path does not survive plugin packaging in Remotion's publish step, so name the skill and file in plain text, and write the routing line as a rule with exceptions, not 'If relevant'. If you use Remotion skills from before 2026-11-09, ask for Studio-editable markup in the prompt. The PR's eval is one replayed session with the pi harness and GPT-6 Astra, written by the PR author; it was not re-run here, and Claude Code was not in it.

## Claims

1. The pull request was merged on 2026-11-09.

   > Merged: 2026-11-09T14:06:46Z

   Locator: GitHub API pulls/13133, merged_at field (saved header). Source: <https://github.com/remotion-dev/remotion/pull/13133>, retrieved 2026-11-12.

2. The best-practices skill presented interactivity as optional, so the agent read the line and skipped the skill.

   > The skills present interactivity as optional ("If relevant").

   Locator: PR body, Problem, cause 1 Wording. Source: <https://github.com/remotion-dev/remotion/pull/13133>, retrieved 2026-11-12.

3. Publishing replaced links to sibling skills with bare text, leaving the agent no skill or file name to load; about 36 links were affected.

   > But the agent was left with "read editable timeline structure." and no skill or file name to load. About 36 links across the skills are affected.

   Locator: PR body, Problem, cause 2 Publishing. Source: <https://github.com/remotion-dev/remotion/pull/13133>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. PR description and merge state from the GitHub API against the record
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `c70e222dc07d2707a717bc4878a72b0993425fbd2dd4f0294359fc006ccf5a72`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-06-23
- default_branch: main
- fetched_at: 2026-11-12
- forks: 6075
- installs: 2885
- installs_by_skill: {"add-effect": 940, "add-expert": 2550, "add-sfx": 2785, "docs-demo": 2573, "fix-dependabot": 1103, "make-pr": 998, "pr-name": 1103, "video-report": 2812, "web-renderer-test": 2885, "writing-docs": 2865}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 195
- registry: skills.sh
- sources: https://api.github.com/repos/remotion-dev/remotion, https://skills.sh/api/search?q=remotion
- stars: 72681

## Related

- evaluated_on: [Remotion Agent Skills](../tool/remotion-dev__skills.md)
- extends: [Vercel: AGENTS.md outperforms skills in our agent evals](vercel.com__blog__agents-md-outperforms-skills-in-our-agent-evals.md) - Another case of an agent not loading an available skill; here the cause is named in the skill text and the packaging.

## Referenced by

- [Remotion issue 12922: the skill asks agents to check audio they cannot hear](github.com__remotion-dev__remotion__issues__12922.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
