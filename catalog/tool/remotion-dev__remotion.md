# Remotion

`tool:remotion-dev/remotion` - tool - <https://github.com/remotion-dev/remotion>

A React framework for video. Each frame is a component rendered from the frame number; the CLI renders the frames in headless Chrome and encodes MP4.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Review loop](../../docs/glossary.md#review-loop), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Also known as: remotion, npx remotion

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The most established code renderer an agent can drive locally, and the one most skills target. Its licence is the first thing to check before company work.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | renderer |
| agents | none-stated |
| levers | motion, design, captions, review-loop |
| cost | mixed |

Free for a person or a company of up to 3 employees (contractors on the project, or a client that operates it, count toward the headcount); a bigger company needs a paid Company License unless an exemption such as a qualifying non-profit applies, and the FAQ adds a per-render plan for automations (code that calls renderMedia() and similar). The repo says a changed licence ships with Remotion 5.0 (PR #3750); re-read LICENSE.md when you upgrade. For agent feedback, `npx remotion still <entry> <id> out.png --frame=N` gives one PNG without a full render, and `npx remotion render <id> out/frames --frames=0,30,90 --image-format=png` gives several (v4.0.502+). Animations written with CSS keyframes or setTimeout flicker or freeze because tabs render frames out of order.

## Claims

1. The free licence covers individuals, for-profit companies with up to 3 employees, non-profits (some need written permission) and evaluation before commercial use; others need a Company License.

   > a for-profit organization with up to 3 employees

   Locator: LICENSE.md, Free License, Eligibility. Source: <https://github.com/remotion-dev/remotion/blob/main/LICENSE.md>, retrieved 2026-11-12.

2. A single frame can be rendered to an image from the CLI, which gives an agent a frame to inspect before the full render.

   > Render a still frame based on the entry point, the composition ID and save it to the output location.

   Locator: packages/docs/docs/cli/still.mdx, npx remotion still. Source: <https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/cli/still.mdx>, retrieved 2026-11-12.

3. CSS animations and timers are not captured correctly because frames render independently and out of order.

   > Remotion renders each frame independently. Frame 30 might be rendered before frame 10, or frame 50 might be rendered twice.

   Locator: packages/docs/docs/troubleshooting/css-animations.mdx, Problem. Source: <https://github.com/remotion-dev/remotion/blob/main/packages/docs/docs/troubleshooting/css-animations.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `184be77958f8ff26028d73637b86a7ef347c4206e085ab56923fce4b4fd0df97`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-06-23
- default_branch: main
- fetched_at: 2026-11-12
- forks: 6074
- installs: 2885
- installs_by_skill: {"add-effect": 938, "add-expert": 2548, "add-sfx": 2783, "docs-demo": 2573, "fix-dependabot": 1103, "make-pr": 998, "pr-name": 1103, "video-report": 2812, "web-renderer-test": 2885, "writing-docs": 2865}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 201
- registry: skills.sh
- sources: https://api.github.com/repos/remotion-dev/remotion, https://skills.sh/api/search?q=remotion
- stars: 72638

## Related

- integrates_with: [Remotion Agent Skills](remotion-dev__skills.md)
- alternative_to: [HyperFrames](heygen-com__hyperframes.md)
- alternative_to: [Kinetograph](0xs4n4tg__kinetograph.md) - Kinetograph states it renders Remotion projects without a browser.

## Referenced by

- [HyperFrames vs Remotion research note (GenMotion)](../source/github.com__haxzie__genmotion__blob__main__docs__research__hyperframes-remotion.md.md) (evaluated_on)
- [HyperFrames vs Remotion (HeyGen guide)](../source/hyperframes.heygen.com__guides__hyperframes-vs-remotion.md) (evaluated_on)
- [HN comment: Remotion for render infrastructure, HyperFrames 'vibe-coded'](../source/news.ycombinator.com__item__50369261.md) (evaluated_on)
- [Remotion 5.0 migration: mandatory telemetry for licensed companies](../source/remotion.dev__docs__5-0-migration.md) (extends)
- [I Quit Remotion After Claude Made These Motion Graphics (Guney Topcu, video)](../source/youtu.be__fvvrcpcfjyk.md) (evaluated_on)
- [Kinetograph](0xs4n4tg__kinetograph.md) (alternative_to)
- [fframes](dmtrkovalenko__fframes.md) (alternative_to)
- [Kino](kino.ai.md) (depends_on)
- [html-video](nexu-io__html-video.md) (contradicts)
- [claude-motion](whaleyxbt__claude-motion.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
