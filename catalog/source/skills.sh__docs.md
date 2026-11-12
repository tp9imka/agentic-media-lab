# skills.sh docs: how the leaderboard ranks skills and what audits cover

`source:skills.sh/docs` - source - <https://skills.sh/docs>

The skills.sh directory's own docs page, plus the skills CLI telemetry section, on where install counts come from and what its security audits promise.

Concepts: [Popularity and trust](../../docs/glossary.md#popularity-and-trust), [Agent Skills](../../docs/glossary.md#agent-skills)

Tags: skills-sh, install-counts

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** skills.sh install counts are the popularity number most video skills advertise; the directory itself says they come from CLI telemetry and that it does not guarantee a listed skill is safe.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

An install is counted when the skills CLI reports it, with telemetry on by default (opt out with DISABLE_TELEMETRY=1 or DO_NOT_TRACK=1). Nothing on the page says installs are de-duplicated per user or machine, so CI runs and scripted installs count the same as people; this was not checked against the CLI source. See the ai-video-generation clone record for what that allows. The audits are run by Vercel, which also runs the directory; the audit method is not described on this page.

## Claims

1. The leaderboard ranks skills from anonymous install telemetry sent by the skills CLI.

   > The skills leaderboard ranks skills based on anonymous telemetry data collected from the skills CLI.

   Locator: skills.sh/docs, leaderboard section. Source: <https://skills.sh/docs>, retrieved 2026-11-12.

2. skills.sh runs security audits but says it cannot guarantee the quality or security of any listed skill and asks users to review skills first.

   > We do our best to maintain a safe ecosystem, but we cannot guarantee the quality or security of every skill listed on skills.sh. We encourage you to review skills before installing and use your own judgment.

   Locator: skills.sh/docs, security section. Source: <https://skills.sh/docs>, retrieved 2026-11-12.

3. The CLI sends install telemetry unless DISABLE_TELEMETRY or DO_NOT_TRACK is set.

   > Set `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` to disable both entirely.

   Locator: vercel-labs/skills docs/troubleshooting.md, section Telemetry. Source: <https://github.com/vercel-labs/skills/blob/main/docs/troubleshooting.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills.sh/docs visible text and vercel-labs/skills troubleshooting.md Telemetry section against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `715044ecf908476b54f01e60a2151282270210009323f76bf1a73ec7eff4838f`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

- [Under the Hood of SKILL.md: Semantic Supply-chain Attacks on AI Agent Skill Registry](arxiv.org__abs__2605.11418.md) (contradicts)
- [skills.sh search results for 'ai-video-generation': cloned listings on new repos](skills.sh__api__search__ai-video-generation.md) (extends)
- [Snyk ToxicSkills: security audit of agent skills on ClawHub and skills.sh](snyk.io__blog__toxicskills-malicious-ai-agent-skills-clawhub.md) (evaluated_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
