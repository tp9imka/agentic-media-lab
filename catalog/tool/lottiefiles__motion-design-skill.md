# motion-design skill (LottieFiles)

`tool:lottiefiles/motion-design-skill` - tool - <https://github.com/LottieFiles/motion-design-skill>

A tool-agnostic motion design skill: director notes, easing and timing tables, patterns, and a quality checklist with severity tiers.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Agent Skills](../../docs/glossary.md#agent-skills), [Agent portability](../../docs/glossary.md#agent-portability)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its checklist turns motion taste into checks an agent can tick before rendering, with a stated severity for each miss.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, any-skill |
| levers | motion, review-loop |
| cost | free-local |

Written for UI motion first: some checks (prefers-reduced-motion, pausable animations over 5 s) do not apply to a rendered MP4; skip them. The checklist is for the agent to read code or frames against; the skill ships no tool that measures a render. Its ban on linear easing matches tool:haidrrrry/claude-remotion-skill.

## Claims

1. Its checklist caps the total stagger of a sequence below 500 ms and marks more as critical.

   > - [ ] Stagger total <500ms

   Locator: skills/motion-design/reference/quality-checklist.md, Technical Quality. Source: <https://github.com/LottieFiles/motion-design-skill/blob/HEAD/skills/motion-design/reference/quality-checklist.md>, retrieved 2026-11-12.

2. It allows at most a third of the elements on screen to move at the same time.

   > - [ ] 1/3 rule (density): max 1/3 elements active simultaneously

   Locator: skills/motion-design/reference/quality-checklist.md, Visual Quality. Source: <https://github.com/LottieFiles/motion-design-skill/blob/HEAD/skills/motion-design/reference/quality-checklist.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. quality-checklist.md and README.md against both claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `d2399cd6df302b7d1970d973a0b98fe105e71cb187d912fe04675150ede4d271`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-03-12
- default_branch: main
- fetched_at: 2026-11-12
- forks: 205
- installs: 24654
- installs_by_skill: {"motion-design": 24654}
- last_activity: 2026-05-18
- licence: MIT
- open_issues: 4
- registry: skills.sh
- sources: https://api.github.com/repos/LottieFiles/motion-design-skill, https://skills.sh/api/search?q=motion-design-skill
- stars: 2966

## Related

- alternative_to: [claude-remotion-skill](haidrrrry__claude-remotion-skill.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
