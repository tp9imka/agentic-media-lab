# Snyk ToxicSkills: security audit of agent skills on ClawHub and skills.sh

`source:snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub` - source - <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>

Snyk's February 2026 scan of 3,984 agent skills from ClawHub and skills.sh for malware, prompt injection and exposed secrets, with human review of the malicious ones.

Concepts: [Popularity and trust](../../docs/glossary.md#popularity-and-trust), [Agent Skills](../../docs/glossary.md#agent-skills)

Tags: supply-chain, prompt-injection

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Video skills come from the same registries; the audit puts a number on how many skills carry critical issues and shows that malicious ones pair code with prompt injection.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Snyk sells scanning tools, so treat the detector claims as a vendor's. The page title says '1467 Malicious Payloads' while the body says 1,467 skills have at least one flaw of any severity and 76 payloads were confirmed malicious; several later articles repeat the title's figure. Cite 76 confirmed and 534 critical. The confirmed malicious skills were on ClawHub (OpenClaw); the skills.sh sample was the curated top 100, on which Snyk reports no critical false positives. Snyk's own scanner was not run here.

## Claims

1. 13.4% of the 3,984 skills scanned (534) had at least one critical issue, and 36.82% (1,467) had at least one flaw of any severity.

   > The findings are stark: 13.4% of all skills, or 534 in total, all contain at least one critical-level security issue, including malware distribution, prompt injection attacks, and exposed secrets. Expand to any severity level, and over a third of the ecosystem is affected: 36.82% (1,467 skills) have at least one security flaw,

   Locator: intro, paragraph 1. Source: <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>, retrieved 2026-11-12.

2. Human review confirmed 76 malicious payloads; 8 of the malicious skills were still public on clawhub.ai at publication.

   > we confirmed active threats through HITL: 76 malicious payloads designed for credential theft, backdoor installation, and data exfiltration. From this small sample alone, 8 of these malicious skills remain publicly available on clawhub.ai as of publication.

   Locator: intro, paragraph 2. Source: <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>, retrieved 2026-11-12.

3. Every confirmed malicious skill contained malicious code patterns and 91% also used prompt injection techniques.

   > 100% of confirmed malicious skills contain malicious code patterns, while 91% simultaneously employ prompt injection techniques.

   Locator: section 100% of confirmed malicious skills contain malicious code. Source: <https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `6e0bd92555ba5e4e11f0d5f9d30d524bc8faee622d7b6e074d0f49ed8f82b2f9`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- evaluated_on: [skills.sh docs: how the leaderboard ranks skills and what audits cover](skills.sh__docs.md) - Snyk scanned the skills.sh top 100 as its benign set.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
