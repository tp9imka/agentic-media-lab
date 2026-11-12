# motion-graphics-skills (Charlie Hills)

`tool:charlie947/motion-graphics-skills` - tool - <https://github.com/charlie947/motion-graphics-skills>

Fifteen Claude Code and Codex skills for launch videos, animated charts, loops, explainers and title sequences, each built as one HTML file with window.seek() and exported through HyperFrames. A brand-intake skill writes brand.md and MOTION.md, which every other skill reads first.

Concepts: [Visual design](../../docs/glossary.md#visual-design), [Consistency](../../docs/glossary.md#consistency), [Agent Skills](../../docs/glossary.md#agent-skills), [Story and decomposition](../../docs/glossary.md#story-and-decomposition)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It stores taste as a file the agent must read before animating, with ASK ME where a value is unknown, instead of repeating style adjectives in each prompt.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex |
| levers | design, consistency, story, review-loop |
| cost | free-local |

Borrow: the 7-section MOTION.md prompt (skills/brand-intake/SKILL.md, Step 3) and the 5-line CLAUDE.md read-first block (Step 4), copied as text, MIT. This is a prompt pattern: no schema or validator checks MOTION.md, and the agent itself checks its frames against it. The pack has no render, beat or audio code; MP4 export goes through tool:heygen-com/hyperframes, and validate-skills.sh only lints skill files for house style. launch-video gives a default 7-beat, 45 s beat sheet and waits for approval. The lead said 13 skills; the tree holds 15 skill folders and the README says both 15 and fourteen. Not run here.

## Claims

1. brand-intake adds a fixed rule to CLAUDE.md that makes the agent read MOTION.md before any animation.

   > Before designing, generating or animating anything, read MOTION.md in full.

   Locator: skills/brand-intake/SKILL.md, Step 4: Add the read-first rule to CLAUDE.md. Source: <https://github.com/charlie947/motion-graphics-skills/blob/main/skills/brand-intake/SKILL.md>, retrieved 2026-11-12.

2. MOTION.md is written from 3 to 5 reference frames, and unknown values are marked ASK ME rather than guessed.

   > Work only from what is in the frames. Where you cannot tell, write ASK ME rather than guessing.

   Locator: skills/brand-intake/SKILL.md, Step 3: Write MOTION.md from the frames. Source: <https://github.com/charlie947/motion-graphics-skills/blob/main/skills/brand-intake/SKILL.md>, retrieved 2026-11-12.

3. The launch-video skill stops for approval of its beat sheet before the build.

   > Show the beat sheet and wait for a yes.

   Locator: skills/launch-video/SKILL.md, Step 2: Lay out the beats. Source: <https://github.com/charlie947/motion-graphics-skills/blob/main/skills/launch-video/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/brand-intake/SKILL.md, prompts/brand-design-system.md, skills/launch-video/SKILL.md, skills/motion-effects/SKILL.md, LICENSE and README.md against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `da10c4363b7c468ad9e936ba49d8eeacb66c2e5463ce20a8cf85ab184b7942c1`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-26
- default_branch: main
- fetched_at: 2026-11-12
- forks: 86
- installs: 3129
- installs_by_skill: {"animated-chart": 2946, "apple-launch-film": 2829, "brand-intake": 2989, "launch-video": 2856, "milestone-reveal": 2769, "motion-brief-writer": 2863, "motion-effects": 3129, "reel-export": 3006, "title-sequence-3d": 2852, "vox-explainer": 3098}
- last_activity: 2026-10-11
- licence: MIT
- open_issues: 2
- registry: skills.sh
- sources: https://api.github.com/repos/charlie947/motion-graphics-skills, https://skills.sh/api/search?q=motion-graphics-skills
- stars: 650

## Related

- depends_on: [HyperFrames](heygen-com__hyperframes.md) - export step

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
