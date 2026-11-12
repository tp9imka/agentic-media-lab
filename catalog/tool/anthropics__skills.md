# Anthropic Agent Skills (canvas-design, algorithmic-art)

`tool:anthropics/skills` - tool - <https://github.com/anthropics/skills>

Anthropic's public skill repository. canvas-design writes a short design philosophy and then draws a single-page PNG or PDF in code; algorithmic-art writes a seeded p5.js sketch as one HTML file.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Still images](../../docs/glossary.md#still-images), [Visual design](../../docs/glossary.md#visual-design)

Also known as: canvas-design, algorithmic-art, anthropic skills

Tags: thumbnail, title-card, generative-art, fonts

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives a model-free route to posters, title cards and abstract backgrounds, with no image API cost and no generation watermark question.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, any-skill |
| levers | design, asset |
| cost | free-local |

canvas-design tells the agent to download whatever fonts it needs, which conflicts with the font-licence rule in tool:mattypark/motion-graphics-skill; check each font's licence before a client job. algorithmic-art outputs HTML that loads p5.js from a CDN, so a still for the video needs a headless browser screenshot step the skill does not provide. Its layout rule (nothing overlaps, everything inside the margins) is the only built-in check; there is no stated safe area for video crops. canvas-design/LICENSE.txt is Apache 2.0 text. Not run here.

## Claims

1. canvas-design requires that nothing overlaps and every element stays inside the canvas with margins.

   > Regardless of text scale, nothing falls off the page and nothing overlaps. Every element must be contained within the canvas boundaries with proper margins.

   Locator: skills/canvas-design/SKILL.md, Text as a contextual element. Source: <https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md>, retrieved 2026-11-12.

2. canvas-design tells the agent to download any fonts it needs.

   > Download and use whatever fonts are needed to make this a reality.

   Locator: skills/canvas-design/SKILL.md, paragraph after Text as a contextual element. Source: <https://github.com/anthropics/skills/blob/main/skills/canvas-design/SKILL.md>, retrieved 2026-11-12.

3. algorithmic-art produces one HTML file that loads p5.js from a CDN, reproducible by seed.

   > The HTML artifact contains everything: p5.js (from CDN), the algorithm, parameter controls, and UI - all in one file that works immediately in claude.ai artifacts or any browser.

   Locator: skills/algorithmic-art/SKILL.md, output section. Source: <https://github.com/anthropics/skills/blob/main/skills/algorithmic-art/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/canvas-design/SKILL.md, skills/algorithmic-art/SKILL.md and skills/canvas-design/LICENSE.txt in anthropics/skills against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `99b371776b2d6db9320a5a36a486e415e5565493814c18cadb58e569e940fe63`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-09-22
- default_branch: main
- fetched_at: 2026-11-12
- forks: 22754
- installs: 1107660
- installs_by_skill: {"frontend-design": 1107660}
- last_activity: 2026-11-06
- licence: unknown
- open_issues: 1523
- registry: skills.sh
- sources: https://api.github.com/repos/anthropics/skills, https://skills.sh/api/search?q=skills
- stars: 193396

## Related

- contradicts: [motion-video-director (mattypark)](mattypark__motion-graphics-skill.md) - Font sourcing: download any font vs never ship an unverified font licence.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
