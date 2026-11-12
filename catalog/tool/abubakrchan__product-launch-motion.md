# product-launch-motion

`tool:abubakrchan/product-launch-motion` - tool - <https://github.com/AbubakrChan/product-launch-motion>

A Claude Code skill for product launch films rendered from one HTML file: every style computed in a pure seek(t), closed-form springs, Playwright subframe capture blended by ffmpeg tmix, and a numpy beat grid. A legacy/ folder keeps the older HyperFrames pipeline with scripts for word timing, audio and a film grade.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent Skills](../../docs/glossary.md#agent-skills), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Review loop](../../docs/glossary.md#review-loop)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its technique file ships the spring and motion-blur code as short snippets, the part of launch-film polish that most skills leave as adjectives.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | motion, design, audio, review-loop |
| cost | free-local |

Borrow: the closed-form spring stepR() and the Track class (one spring per target change, summed) from references/technique.md, section Springs, about 10 lines of JS under MIT; the 4-subframe Playwright capture plus the ffmpeg tmix command from section Render for 60 fps motion blur; and legacy/scripts/wire-grade.mjs, one self-contained file that adds deterministic grain, a vignette and specular sweeps on named beats to a HyperFrames film (no blend modes, with a reason in its header). Gotcha: the beat analysis, SFX synth and render scripts that technique.md names sit under ~/code/cheerful-motion/ on the author's machine and are not in the repo, so the beat grid and synth are described, not shipped. SKILL.md tells the agent to read real numbers from the product's database read-only and to serve the output over a tailnet; both assume the author's setup. NOTICE takes the sample films, frames and brand marks out of the MIT grant. Its rule that every UI sound is synthesized is the opposite of tool:barty-bart/motion-graphics. Not run here.

## Claims

1. Its springs are closed-form damped step responses, with damping 0.72-0.9 for a small overshoot and 1.0 for camera and text.

   > Damping 0.72–0.9 for a tiny overshoot, 1.0 for camera and text.

   Locator: references/technique.md, section Springs. Source: <https://github.com/AbubakrChan/product-launch-motion/blob/main/references/technique.md>, retrieved 2026-11-12.

2. The reference implementation the technique file points to is a local folder on the author's machine, not part of the repo.

   > Reference implementation: `~/code/cheerful-motion/launch2/`

   Locator: references/technique.md, first paragraph. Source: <https://github.com/AbubakrChan/product-launch-motion/blob/main/references/technique.md>, retrieved 2026-11-12.

3. The MIT licence does not cover the sample films or their frames.

   > You may not reuse, redistribute or modify the films or their frames.

   Locator: NOTICE, section The v2 sample films. Source: <https://github.com/AbubakrChan/product-launch-motion/blob/main/NOTICE>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. SKILL.md, references/technique.md, LICENSE, NOTICE, README.md and legacy/scripts/wire-grade.mjs against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `4c169c8cdfcd5a89c89c9130c29e84688e6fcfc75532c0ef11731c9266ddb7c2`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-07-27
- default_branch: main
- fetched_at: 2026-11-12
- forks: 59
- installs: 980
- installs_by_skill: {"motion-launch-video": 65, "product-launch-motion": 980, "product-launch-motion-v1": 14}
- last_activity: 2026-10-21
- licence: MIT
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/AbubakrChan/product-launch-motion, https://skills.sh/api/search?q=product-launch-motion
- stars: 453

## Related

- integrates_with: [HyperFrames](heygen-com__hyperframes.md) - legacy/ v1 scripts target HyperFrames; v2 uses its own Playwright renderer

## Referenced by

- [GSAP Agent Skills](greensock__gsap-skills.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
