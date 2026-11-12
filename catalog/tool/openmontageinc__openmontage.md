# OpenMontage

`tool:openmontageinc/openmontage` - tool - <https://github.com/OpenMontageInc/OpenMontage>

An agent-driven video production system with staged skills: proposal, scene plan, edit, compose, each followed by a reviewer pass. Creative skills hold typography, safe-zone, storytelling and sound numbers.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Visual design](../../docs/glossary.md#visual-design), [Audio and captions](../../docs/glossary.md#audio-and-captions)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its reviewer skill makes every critical finding carry a concrete fix and bounds revision rounds, and its typography skill has per-platform vertical safe zones.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | claude-code, codex, cursor |
| levers | review-loop, design, captions, story, audio |
| cost | mixed |

AGPL: if you change it and run it as a service, the licence asks you to publish your changes; read it before client or SaaS use. The repo also ships face-swap and avatar skills, which this hub does not cover; this record covers only reviewer.md and the creative skills. Its two-round review bound is lower than the three rounds in tool:digitalsamba/claude-code-video-toolkit. The safe-zone table cites a third-party site; I did not open it.

## Claims

1. Any critical finding forces a revision and a re-review, at most two rounds.

   > | 1+ critical findings | **Revise** — fix all critical findings, then re-review (max 2 rounds). |

   Locator: skills/meta/reviewer.md, decision table. Source: <https://github.com/OpenMontageInc/OpenMontage/blob/HEAD/skills/meta/reviewer.md>, retrieved 2026-11-12.

2. It lists the dead zones of the TikTok UI on a 1080x1920 frame: 108 px top, 320 px bottom, 120 px right.

   > | **TikTok** | 900x1492 | 108px | 320px | 120px |

   Locator: skills/creative/typography.md, Platform-Specific Safe Zones (Vertical 1080x1920), row TikTok. Source: <https://github.com/OpenMontageInc/OpenMontage/blob/HEAD/skills/creative/typography.md>, retrieved 2026-11-12.

3. The project is under the GNU AGPL version 3.

   > GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007

   Locator: LICENSE, title lines. Source: <https://github.com/OpenMontageInc/OpenMontage/blob/HEAD/LICENSE>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/meta/reviewer.md, skills/creative/typography.md, README.md and LICENSE against the three claims; the git tree listing for the face-swap skill
- Next check due: 2027-02-10
- Licence: AGPL-3.0
- URL status: live
- Saved source sha256: `60e5591263ea7213c0ec7802ccbb557ac6f4bd9707cdbb37603800f8524228eb`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-03-29
- default_branch: main
- fetched_at: 2026-11-12
- forks: 10704
- installs: 1945
- installs_by_skill: {"ai-video-gen": 1576, "character-animation-qa": 1586, "ffmpeg": 1548, "pose-library-design": 1510, "remotion": 1536, "svg-character-animation": 1945, "text-to-speech": 1515, "video-download": 1575, "video-edit": 1905, "video-understand": 1780}
- last_activity: 2026-11-09
- licence: AGPL-3.0
- open_issues: 341
- registry: skills.sh
- sources: https://api.github.com/repos/OpenMontageInc/OpenMontage, https://skills.sh/api/search?q=OpenMontage
- stars: 79811

## Related

- contradicts: [claude-plugin-marketplace (ffmpeg-kinetic-captions)](josiahsiegel__claude-plugin-marketplace.md) - 320 px bottom dead zone vs 50 px edge margin
- alternative_to: [claude-code-video-toolkit](digitalsamba__claude-code-video-toolkit.md) - two review rounds vs three

## Referenced by

- [generative-media-skills](calesthio__generative-media-skills.md) (integrates_with)
- [claude-plugin-marketplace (ffmpeg-kinetic-captions)](josiahsiegel__claude-plugin-marketplace.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
