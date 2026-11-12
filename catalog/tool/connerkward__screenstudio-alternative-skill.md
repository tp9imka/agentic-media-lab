# screenstudio-alt

`tool:connerkward/screenstudio-alternative-skill` - tool - <https://github.com/connerkward/screenstudio-alternative-skill>

A macOS Claude Code skill that polishes a screen recording headless: eased auto-zoom on clicks, idle speed-up, keystroke chips, a smoothed cursor, callouts and 9:16 export, with FCPXML handoff.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Review loop](../../docs/glossary.md#review-loop)

Also known as: screenstudio-alt, Screen Studio alternative skill

Tags: screen-recording, auto-zoom

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The only headless, agent-driven zoom and cursor pass found for screen recordings, and it says plainly which effects need data captured while recording.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | motion, review-loop, delivery |
| cost | mixed |

Auto-zoom, keys and cursor need its Swift event logger running during capture, with Accessibility and Input Monitoring granted; an old recording only gets idle speed-up. Its review step uploads the render to a hosted video model chosen through fal, which costs money and sends your screen content off the machine; skip that step for private material and review frames locally. Claude Code only as stated.

## Claims

1. Auto-zoom, keystrokes and cursor need event data logged during capture.

   > **Auto-zoom/keys/cursor need this data at capture time — it cannot be recovered from pixels later.**

   Locator: SKILL.md, component events-log. Source: <https://github.com/connerkward/screenstudio-alternative-skill/blob/main/SKILL.md>, retrieved 2026-11-12.

2. Idle speed-up works on any existing recording without event data.

   > `--speedup` works WITHOUT events (freezedetect only)

   Locator: SKILL.md, component polish.py. Source: <https://github.com/connerkward/screenstudio-alternative-skill/blob/main/SKILL.md>, retrieved 2026-11-12.

3. Before delivery it tells the agent to send the rendered MP4 to a hosted video-understanding model for critique.

   > Before handing a demo over, **stop judging it from stills — send the actual rendered mp4 to a video-understanding model and act on its critique.**

   Locator: SKILL.md, section Get an objective critique. Source: <https://github.com/connerkward/screenstudio-alternative-skill/blob/main/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and SKILL.md against the three claims; docs/ARCHITECTURE.md not opened
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `a58c4ec22e0345d4be7d79c33131d4477b70d1ddfef6d0b2e00a6240996dc416`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-06-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1
- last_activity: 2026-06-23
- licence: MIT
- moved_to: connerkward/screenstudio-alt-skill
- open_issues: 0
- sources: https://api.github.com/repos/connerkward/screenstudio-alternative-skill, https://api.github.com/repositories/1266648955, https://skills.sh/api/search?q=screenstudio-alternative-skill
- stars: 11

## Related

- alternative_to: [Reelbird](btahir__reelbird.md)
- integrates_with: [marketingskills (video, product-demo-recording)](coreyhaines31__marketingskills.md) - its product-demo-recording reference covers capture; this covers polish

## Referenced by

- [Reelbird](btahir__reelbird.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
