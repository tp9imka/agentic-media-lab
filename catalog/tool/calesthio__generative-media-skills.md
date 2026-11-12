# generative-media-skills

`tool:calesthio/generative-media-skills` - tool - <https://github.com/calesthio/generative-media-skills>

A large provider-independent skill library for media production. Separate skills cover captions and accessibility, final QC and delivery, character continuity, audio mixing and generated-media QA, several with small validator scripts.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Delivery](../../docs/glossary.md#delivery), [Consistency](../../docs/glossary.md#consistency), [Agent Skills](../../docs/glossary.md#agent-skills), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: captions-media-accessibility, media-qc-delivery, character-design-continuity

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the only candidate found that covers caption limits, delivery specs and character continuity in one place, with a caption validator that turns line length and reading speed into numbers.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, hermes, any-skill |
| levers | captions, delivery, consistency, audio, review-loop |
| cost | free-local |

Load single skills, not the whole library: each SKILL.md is 25-30 KB, so three of them fill a lot of context. The caption validator checks timing and line counts only; its own text says it does not judge accuracy, contrast or placement. The platform specs inside are dated by the author (verified 2026-07-10 in the text); re-check them before a paid ad delivery. I did not run any of its scripts. The README links to calesthio/OpenMontage, which is the same project as tool:openmontageinc/openmontage.

## Claims

1. Its caption skill runs a validator with a two-line limit, 42 characters per line and a warning above 20 characters per second.

   > python skills/production/audio-craft/captions-media-accessibility/scripts/validate_captions.py --max-lines 2 --max-chars-per-line 42 --cps-warning 20 captions_en.vtt

   Locator: skills/production/audio-craft/captions-media-accessibility/SKILL.md, section on the bundled validator, example command. Source: <https://github.com/calesthio/generative-media-skills/blob/HEAD/skills/production/audio-craft/captions-media-accessibility/SKILL.md>, retrieved 2026-11-12.

2. Its delivery skill keeps at least 1 dB of true-peak headroom for web and social files when no target is given.

   > Leave at least 1 dB true-peak headroom for generic web/social delivery when no loudness target is specified; use the mandated loudness target for broadcast/streaming.

   Locator: skills/production/governance-delivery/media-qc-delivery/SKILL.md, export and encode rules. Source: <https://github.com/calesthio/generative-media-skills/blob/HEAD/skills/production/governance-delivery/media-qc-delivery/SKILL.md>, retrieved 2026-11-12.

3. Its continuity skill marks a character's features as locked, so they may not change across shots unless the user approves.

   > **Locked**: must remain constant unless user approves a redesign.

   Locator: skills/production/creative-direction/character-design-continuity/SKILL.md, section Identity lock. Source: <https://github.com/calesthio/generative-media-skills/blob/HEAD/skills/production/creative-direction/character-design-continuity/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. captions-media-accessibility, media-qc-delivery and character-design-continuity SKILL.md files and the README against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `db48605a44d26c71a0beede32bffbbaf1aa63fc0ba05e93194699512f1b2b43c`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-07-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 50
- installs: 419
- installs_by_skill: {"2d-character-rig-animation": 300, "audio-mixing-mastering": 417, "character-design-continuity": 265, "cinematic-shot-direction": 285, "color-grading-finishing": 419, "editing-montage": 349, "generated-media-qa": 233, "sound-design-foley": 338, "storyboard-previsualization": 263, "title-kinetic-typography": 238}
- last_activity: 2026-07-14
- licence: MIT
- open_issues: 1
- registry: skills.sh
- sources: https://api.github.com/repos/calesthio/generative-media-skills, https://skills.sh/api/search?q=generative-media-skills
- stars: 242

## Related

- integrates_with: [OpenMontage](openmontageinc__openmontage.md)

## Referenced by

- [Netflix English (USA) Timed Text Style Guide](../source/partnerhelp.netflixstudios.com__hc__en-us__articles__217350977-english-usa-timed-text-style-guide.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
