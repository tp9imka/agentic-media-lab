# remotion-superpowers

`tool:dojocodinglabs/remotion-superpowers` - tool - <https://github.com/DojoCodingLabs/remotion-superpowers>

A plugin on top of the official Remotion skills that adds voiceover, music, footage, caption presets and a /review-video command that scores a render.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Plugins](../../docs/glossary.md#plugins), [Agent portability](../../docs/glossary.md#agent-portability)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its review command does a cheap local frame check first, then a scored AI watch of the full render, and tells the agent to trust its own frames when they disagree.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | claude-code, codex, gemini-cli, cursor, any-skill |
| levers | review-loop, captions, audio |
| cost | paid |

The full review uploads your render to TwelveLabs, and voice and music use ElevenLabs: paid keys and your video leaves the machine. Step 1 alone (local stills) is free and works without either. Its caption placement agrees with tool:openmontageinc/openmontage and contradicts the 50 px margin in tool:josiahsiegel/claude-plugin-marketplace. Remotion's company licence applies as for tool:remotion-dev/skills.

## Claims

1. Review starts with a local check of rendered stills, then has TwelveLabs watch and score the full render.

   > Starts with a cheap local check of rendered still frames, then has TwelveLabs watch the full render and score it against a JSON rubric

   Locator: skills/review-video/SKILL.md, frontmatter description. Source: <https://github.com/DojoCodingLabs/remotion-superpowers/blob/HEAD/skills/review-video/SKILL.md>, retrieved 2026-11-12.

2. When the AI review and the agent's own frames disagree on something visible, the frames win.

   > Cross-check the AI review against your own frame check from step 1; if they disagree on something visible, trust the frames and say so.

   Locator: skills/review-video/SKILL.md, after the review format. Source: <https://github.com/DojoCodingLabs/remotion-superpowers/blob/HEAD/skills/review-video/SKILL.md>, retrieved 2026-11-12.

3. On 1080x1920 shorts it puts captions 15-25% up from the bottom to clear the platform UI.

   > | TikTok / Reels / Shorts (1080x1920) | About 15-25% up from the bottom (`bottom` around 300-480), or dead center for punchy hooks |

   Locator: skills/remotion-production/rules/captions-workflow.md, Placement for platforms (safe zones), table. Source: <https://github.com/DojoCodingLabs/remotion-superpowers/blob/HEAD/skills/remotion-production/rules/captions-workflow.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/review-video/SKILL.md and rules/captions-workflow.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `571287eab345a8066f464cf9c18387a0775e3e21d3f7f35a834f2359b2fea159`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-02-09
- default_branch: main
- fetched_at: 2026-11-12
- forks: 34
- installs: 296
- installs_by_skill: {"add-captions": 65, "add-transitions": 63, "add-voiceover": 65, "create-short": 64, "create-video": 63, "find-footage": 65, "generate-clip": 63, "remotion-production": 296, "review-video": 65, "setup-guide": 251}
- last_activity: 2026-10-29
- licence: MIT
- open_issues: 2
- registry: skills.sh
- sources: https://api.github.com/repos/DojoCodingLabs/remotion-superpowers, https://skills.sh/api/search?q=remotion-superpowers
- stars: 166

## Related

- extends: [Remotion Agent Skills](remotion-dev__skills.md)
- contradicts: [claude-plugin-marketplace (ffmpeg-kinetic-captions)](josiahsiegel__claude-plugin-marketplace.md) - caption placement on vertical video

## Referenced by

- [claude-plugin-marketplace (ffmpeg-kinetic-captions)](josiahsiegel__claude-plugin-marketplace.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
