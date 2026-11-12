# motion-graphics (Mort1d)

`tool:mort1d/motion-graphics-skills` - tool - <https://github.com/Mort1d/motion-graphics-skills>

A skill that directs, animates, scores and renders a promo or reel from HTML scenes in headless Chrome, with sub-frame motion blur and an original score on the same beat grid.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Delivery](../../docs/glossary.md#delivery), [Audio and captions](../../docs/glossary.md#audio-and-captions)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It fixes a master spec, forbids copying reference material, and makes the agent critique until every score is 8 or more before the final render.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, gemini-cli, any-skill |
| levers | motion, audio, delivery, review-loop, asset |
| cost | free-local |

No npm packages or API keys per its compatibility line; needs Node 22.4+, ffmpeg and a Chromium browser. The SKILL.md is 35 KB. Its -1 dBTP ceiling is looser than the -1.5 dBTP in tool:mattypark/motion-graphics-skill. The critique score is the agent grading itself; nothing independent checks it. I did not run it.

## Claims

1. It sets the master: 60 fps, H.264 and AAC, -14 LUFS, true peak at or below -1 dBTP.

   > the master (1920×1080 or the chosen format, 60 fps, H.264 + AAC, -14 LUFS, true peak ≤ -1 dBTP)

   Locator: skills/motion-graphics/SKILL.md, outputs list. Source: <https://github.com/Mort1d/motion-graphics-skills/blob/HEAD/skills/motion-graphics/SKILL.md>, retrieved 2026-11-12.

2. It forbids copying footage, frames, music or a recognisable design from a reference.

   > Never copy footage, frames, music or a recognisable design from a reference

   Locator: skills/motion-graphics/SKILL.md, references rules. Source: <https://github.com/Mort1d/motion-graphics-skills/blob/HEAD/skills/motion-graphics/SKILL.md>, retrieved 2026-11-12.

3. It critiques until every score is 8 or more, then renders and runs QA.

   > ### 7. Critique until every score is 8+, then render + QA

   Locator: skills/motion-graphics/SKILL.md, step 7. Source: <https://github.com/Mort1d/motion-graphics-skills/blob/HEAD/skills/motion-graphics/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/motion-graphics/SKILL.md and README.md against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `e7b90c6073b7e5a8782403144dd323f63463c7131f39af19a4e5b22e64c949e0`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-28
- default_branch: main
- fetched_at: 2026-11-12
- forks: 5
- installs: 175
- installs_by_skill: {"motion-graphics": 175}
- last_activity: 2026-09-30
- licence: unknown
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/Mort1d/motion-graphics-skills, https://skills.sh/api/search?q=motion-graphics-skills
- stars: 78

## Related

- alternative_to: [motion-video-director (mattypark)](mattypark__motion-graphics-skill.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
