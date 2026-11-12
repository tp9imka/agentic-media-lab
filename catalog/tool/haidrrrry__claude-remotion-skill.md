# claude-remotion-skill

`tool:haidrrrry/claude-remotion-skill` - tool - <https://github.com/haidrrrry/claude-remotion-skill>

A Remotion motion-graphics skill with non-negotiable easing, stagger and exit rules and a mandatory render, extract frames, inspect, fix loop.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Agent Skills](../../docs/glossary.md#agent-skills), [Review loop](../../docs/glossary.md#review-loop), [Code-driven video](../../docs/glossary.md#code-driven-video)

Also known as: remotion-motion-graphics

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Adds the frame-inspection step the official Remotion skills leave to a person.

**Last checked:** 2026-11-12, primary-read, by agent:driver. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | motion, design, consistency, audio, review-loop |
| cost | free-local |

Two of its rules (idle elements breathe; never a flat background) contradict the HyperFrames and video-design skills. Pick one rule set per project.

## Claims

1. It bans linear interpolation in every composition.

   > **NEVER use linear interpolation.**

   Locator: remotion-motion-graphics/SKILL.md, Non-negotiable rules, rule 1. Source: <https://github.com/haidrrrry/claude-remotion-skill/blob/main/remotion-motion-graphics/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:driver, depth primary-read. SKILL.md against the claim
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `7bc57dcc03c9812feb94b32785bb2fb26ab9740f523f7def580a1b372b3b6336`
- Lane: quality-skills

## Observed

Nothing collected yet.

## Related

- extends: [Remotion Agent Skills](remotion-dev__skills.md)
- contradicts: [HyperFrames](heygen-com__hyperframes.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
