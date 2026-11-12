# motion-dev-animations skill

`tool:199-biotechnologies/motion-dev-animations-skill` - tool - <https://github.com/199-biotechnologies/motion-dev-animations-skill>

A Claude Code skill that writes Motion (formerly Framer Motion) code for React, Next.js, Svelte and Astro pages: entrances, hover, scroll and layout animations, with a JSON schema and a validator for animation configs.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Agent Skills](../../docs/glossary.md#agent-skills)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Thin for this hub: it targets live web UI, not rendered video, and none of its skill files mention frame-by-frame rendering.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intro. Maturity: experimental.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | motion |
| cost | free-local |

Borrow: little for video. The one reusable part is schema/motion-config.schema.json with scripts/validate_motion_config.py (JSON Schema check of one animation config, needs pip jsonschema), MIT; it bounds Motion props, not timing or taste. Motion animations run on the wall clock, so rendering them to MP4 needs a renderer that can seek them, and the skill gives no method. The '10M+ downloads/month' line in SKILL.md has no source. The repo also holds SKILL.md.backup and status files (DEPLOYMENT_STATUS.md, VALIDATION_V3.md). For video, tool:greensock/gsap-skills with a seek-based renderer fits better. Not run here.

## Claims

1. The skill itself sends SVG and canvas animation to GSAP.

   > Do NOT use for CSS-only transitions (use native CSS), static sites without JavaScript, Vue animations (use motion-v variant instead), or SVG/Canvas complex animations (GSAP better suited).

   Locator: SKILL.md, frontmatter description. Source: <https://github.com/199-biotechnologies/motion-dev-animations-skill/blob/main/SKILL.md>, retrieved 2026-11-12.

2. Its quality check is live browser frame rate in DevTools, not inspection of rendered frames.

   > | **Performance** | ≥60fps | Chrome DevTools → Performance |

   Locator: SKILL.md, Quality Standards table. Source: <https://github.com/199-biotechnologies/motion-dev-animations-skill/blob/main/SKILL.md>, retrieved 2026-11-12.

3. Its schema bounds spring damping and documents what the values feel like.

   > "description": "Spring damping (10=bouncy, 50=no bounce)"

   Locator: schema/motion-config.schema.json, props.transition.damping. Source: <https://github.com/199-biotechnologies/motion-dev-animations-skill/blob/main/schema/motion-config.schema.json>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. SKILL.md, schema/motion-config.schema.json, scripts/validate_motion_config.py, LICENSE and README.md against the claims; searched SKILL.md and reference/ for video, seek, render and frame
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `c0675ae07a10e0c71d2902198834802d09420fde9dd5d323016513da2d2ed1c5`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-11-07
- default_branch: main
- fetched_at: 2026-11-12
- forks: 36
- installs: 689
- installs_by_skill: {"motion-dev-animations": 689}
- last_activity: 2026-03-30
- licence: MIT
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/199-biotechnologies/motion-dev-animations-skill, https://skills.sh/api/search?q=motion-dev-animations-skill
- stars: 231

## Related

- alternative_to: [GSAP Agent Skills](greensock__gsap-skills.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
