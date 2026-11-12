# HyperFrames vs Remotion research note (GenMotion)

`source:github.com/haxzie/genmotion/blob/main/docs/research/hyperframes-remotion.md` - source - <https://github.com/haxzie/genmotion/blob/main/docs/research/hyperframes-remotion.md>

A research note dated 2026-09-30 for the GenMotion team that reads the HyperFrames and Remotion repos and compares their capture, CLI, agent and licence details.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Consistency](../../docs/glossary.md#consistency), [Review loop](../../docs/glossary.md#review-loop)

**Badge:** quoted, not read at the primary source (`quoted-secondary`): primary source read; downgraded one step: interested-party.

**Why:** The only source found that says how HyperFrames capture differs on macOS, which is the reader's machine.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

Written for the team building GenMotion, a competing engine, and kept in its repo; its last section argues for GenMotion. It read the repos, not the docs sites, which it says were blocked. The macOS capture claim needs a check against the HyperFrames engine source: the engine README I opened names BeginFrame capture but does not mention a macOS fallback, so treat the claim as unconfirmed. Its Remotion pricing line matches the Remotion licence FAQ.

## Claims

1. It says HyperFrames' atomic BeginFrame capture runs only on Linux, macOS falls back to screenshots, and --docker is the route to exact output.

   > HyperFrames' atomic `BeginFrame` capture only runs on Linux headless-shell; macOS and Windows fall back to screenshots, and it recommends `--docker` for exact output.

   Locator: Section 1 TL;DR, Determinism bullet. Source: <https://github.com/haxzie/genmotion/blob/main/docs/research/hyperframes-remotion.md>, retrieved 2026-11-12.

2. It says an <audio> element with no id is dropped from a HyperFrames render with no error at render time.

   > An `<audio>` element without an `id` is **dropped silently** (it is a lint error).

   Locator: Section 2.5 Render pipeline, Audio. Source: <https://github.com/haxzie/genmotion/blob/main/docs/research/hyperframes-remotion.md>, retrieved 2026-11-12.

3. It reports Remotion's automation price as one cent per render with a monthly minimum.

   > "automated" products such as prompt-to-video tools pay **$0.01/render with a $100/month minimum**.

   Locator: Section 1 TL;DR, Remotion bullet. Source: <https://github.com/haxzie/genmotion/blob/main/docs/research/hyperframes-remotion.md>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `67b7e0e0eec76cde6967585c4e042f54a1de57585d2cf8a3940525a79d68e99d`
- Badge downgraded: interested-party - Written by a competing engine's team.
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-06-29
- default_branch: main
- fetched_at: 2026-11-12
- forks: 2
- installs: 1
- installs_by_skill: {"ad-qa": 1, "ai-presenter": 1, "announce-feature": 1, "announce-milestone": 1, "app-store-preview": 1, "brand-sting": 1, "demo-walkthrough": 1, "device-mockup": 1, "direction": 1, "explainer": 1}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/haxzie/genmotion, https://skills.sh/api/search?q=genmotion
- stars: 7

## Related

- evaluated_on: [HyperFrames](../tool/heygen-com__hyperframes.md)
- evaluated_on: [Remotion](../tool/remotion-dev__remotion.md)
- alternative_to: [HyperFrames vs Remotion (HeyGen guide)](hyperframes.heygen.com__guides__hyperframes-vs-remotion.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
