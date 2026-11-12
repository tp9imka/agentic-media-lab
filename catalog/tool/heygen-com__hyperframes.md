# HyperFrames

`tool:heygen-com/hyperframes` - tool - <https://github.com/heygen-com/hyperframes>

An HTML and GSAP video renderer with a skill pack. The agent writes a page, the CLI captures it frame by frame and encodes MP4.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent Skills](../../docs/glossary.md#agent-skills), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Review loop](../../docs/glossary.md#review-loop)

Also known as: hyperframes skill, HeyGen HyperFrames

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** One of the two renderers most agent-made video runs on, and its skill carries numeric motion, review and loudness rules.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | renderer |
| agents | claude-code, codex, cursor, gemini-cli |
| levers | motion, design, story, audio, captions, review-loop, asset |
| cost | free-local |

Start here for a fully local render with no licence fee. The skill asks the agent to send a usage beacon through the CLI at start; read the skill before installing if that matters to you. Hosted media features need a HeyGen sign-in.

## Claims

1. Its motion reference tells the agent not to reuse one ease and duration for every element.

   > The same `power2.out` at 0.5 s on everything is the flat default that makes a film feel generated.

   Locator: skills/hyperframes/references/motion.md, section Motion craft. Source: <https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/motion.md>, retrieved 2026-11-12.

2. It sets exits shorter than entrances by a stated ratio.

   > **Exits** are 40-50% shorter than their entrances.

   Locator: skills/hyperframes/references/motion.md, section Motion craft. Source: <https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/references/motion.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `bd55ea56343346060cd612a30874996e82f48ac5051ecb2bd1ab01efe4e2fc71`
- Lane: quality-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-03-10
- default_branch: main
- fetched_at: 2026-11-12
- forks: 7665
- installs: 1524572
- installs_by_skill: {"general-video": 661816, "hyperframes": 1486779, "hyperframes-animation": 1005453, "hyperframes-audio": 663932, "hyperframes-cli": 1524572, "hyperframes-core": 931131, "hyperframes-creative": 917182, "hyperframes-keyframes": 754861, "hyperframes-registry": 1274564, "media-use": 1395655}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 243
- registry: skills.sh
- sources: https://api.github.com/repos/heygen-com/hyperframes, https://skills.sh/api/search?q=hyperframes
- stars: 83101

## Related

- alternative_to: [Remotion Agent Skills](remotion-dev__skills.md)

## Referenced by

- [IBM Carbon Design System - Motion](../source/carbondesignsystem.com__elements__motion__overview.md) (integrates_with)
- [HyperFrames vs Remotion research note (GenMotion)](../source/github.com__haxzie__genmotion__blob__main__docs__research__hyperframes-remotion.md.md) (evaluated_on)
- [HyperFrames skill: usage beacon and CLI telemetry](../source/github.com__heygen-com__hyperframes__blob__main__skills__hyperframes__skill.md.md) (extends)
- [HyperFrames issue 4435: parallel render workers capture a blank first frame](../source/github.com__heygen-com__hyperframes__issues__4435.md) (evaluated_on)
- [HyperFrames vs Remotion (HeyGen guide)](../source/hyperframes.heygen.com__guides__hyperframes-vs-remotion.md) (evaluated_on)
- [HN comment: Remotion for render infrastructure, HyperFrames 'vibe-coded'](../source/news.ycombinator.com__item__50369261.md) (evaluated_on)
- [I Quit Remotion After Claude Made These Motion Graphics (Guney Topcu, video)](../source/youtu.be__fvvrcpcfjyk.md) (evaluated_on)
- [Kinetograph](0xs4n4tg__kinetograph.md) (alternative_to)
- [product-launch-motion](abubakrchan__product-launch-motion.md) (integrates_with)
- [motion-graphics-skills (Charlie Hills)](charlie947__motion-graphics-skills.md) (depends_on)
- [smooth-animation-skill](flchntc__smooth-animation-skill.md) (extends)
- [GSAP](greensock__gsap.md) (integrates_with)
- [talking-head-editor](griffinwooldridge__talking-head-editor.md) (depends_on)
- [claude-remotion-skill](haidrrrry__claude-remotion-skill.md) (contradicts)
- [Herk Edit Kit](nateherkai__herk-edit-kit.md) (depends_on)
- [html-video](nexu-io__html-video.md) (depends_on)
- [Remotion](remotion-dev__remotion.md) (alternative_to)
- [Remotion Agent Skills](remotion-dev__skills.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
