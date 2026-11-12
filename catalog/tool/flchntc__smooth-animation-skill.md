# smooth-animation-skill

`tool:flchntc/smooth-animation-skill` - tool - <https://github.com/Flchntc/smooth-animation-skill>

A Claude Code skill for choppy code-rendered animation (HyperFrames, Remotion, canvas, three.js), with a script that measures repeated frames, stills and jitter in the file.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Review loop](../../docs/glossary.md#review-loop), [Code-driven video](../../docs/glossary.md#code-driven-video)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It replaces 'looks choppy' with a measured number and a fixed order of fixes, and it re-measures the final file.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | motion, review-loop |
| cost | free-local |

The only evidence is the author's own before/after on two films; treat the 0.1 jump limit as the author's threshold. Rendering at 60 fps with 3 blur samples costs render time; the skill says how to cut back. Its 'no still scenes' rule contradicts the calm holds other skills allow, so pick one rule set. I did not run the meter.

## Claims

1. It starts by measuring the current file and keeping the result.

   > **1. Measure the current file and keep the result**

   Locator: SKILL.md, step 1. Source: <https://github.com/Flchntc/smooth-animation-skill/blob/HEAD/SKILL.md>, retrieved 2026-11-12.

2. It sets a jitter limit: frame-to-frame motion change above 0.1 fails.

   > `jump` compares the amount of motion from one frame to the next. Measured in tests: smooth videos stay between 0.003 and 0.04, and videos with camera jitter between 0.27 and 0.6; the limit is 0.1.

   Locator: SKILL.md, section on reading the meter. Source: <https://github.com/Flchntc/smooth-animation-skill/blob/HEAD/SKILL.md>, retrieved 2026-11-12.

3. It renders at a true 60 fps by default instead of interpolating frames.

   > **4. Render at a real 60 fps.** It is the default, not the last resort.

   Locator: SKILL.md, step 4. Source: <https://github.com/Flchntc/smooth-animation-skill/blob/HEAD/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. SKILL.md and README.md against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `99bf56e9161089b8605fa95730917defd1416213464d39a6ed37945b442e85cb`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-11-01
- default_branch: main
- fetched_at: 2026-11-12
- forks: 0
- last_activity: 2026-11-01
- licence: unknown
- open_issues: 0
- sources: https://api.github.com/repos/Flchntc/smooth-animation-skill, https://skills.sh/api/search?q=smooth-animation-skill
- stars: 1

## Related

- extends: [HyperFrames](heygen-com__hyperframes.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
