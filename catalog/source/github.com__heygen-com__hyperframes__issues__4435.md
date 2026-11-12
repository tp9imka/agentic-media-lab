# HyperFrames issue 4435: parallel render workers capture a blank first frame

`source:github.com/heygen-com/hyperframes/issues/4435` - source - <https://github.com/heygen-com/hyperframes/issues/4435>

An open HyperFrames bug report (opened 2026-09-24, version 0.8.72) with a repro: in screenshot capture mode with several workers, each worker's first frame can come out blank. Read with the vendor's determinism page.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop)

Tags: hyperframes, determinism

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** HyperFrames' skill tells the agent every render is identical; this report, with a repro and a named unmerged fix, shows parallel renders can differ between runs.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Gotcha for agents: the render exits normally, so only a frame check catches it. Until the issue closes, render final output with `--workers 1` or scan for blank frames at worker shard boundaries (frame = worker index x total frames / workers). A related open issue, 5888 (0.8.145), reports the same class with GSAP and PNG sequences. The vendor's determinism page says output is identical but also says a local render can shift by a pixel between machines and recommends `--docker` for exact output. The repro was not run here.

## Claims

1. With 4 parallel workers in screenshot capture mode, frames at each worker's first frame came out fully transparent, intermittently; one worker gave no blank frames.

   > `--workers 1` produces zero blank frames; the anomaly is deterministic in position across parallel runs but intermittent (some runs clean), matching the paint-settle race described in #2477.

   Locator: issue 4435 body, section Describe the bug, paragraph 2. Source: <https://github.com/heygen-com/hyperframes/issues/4435>, retrieved 2026-11-12.

2. The earlier fix for this bug was closed without merging, according to the reporter.

   > The fix PR #2489 was closed unmerged, and `discardWarmupCapture` still has **zero call sites** on current `main` (a3d7736)

   Locator: issue 4435 body, section Describe the bug, paragraph 1. Source: <https://github.com/heygen-com/hyperframes/issues/4435>, retrieved 2026-11-12.

3. The vendor's own determinism page says local renders can differ by a pixel between machines and points to Docker for exact output.

   > Fonts and Chrome versions differ between computers, so a local render can shift by a pixel from one machine to the next.

   Locator: docs/concepts/determinism.mdx, section Rule out your machine as a variable. Source: <https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/determinism.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. issue 4435 body via gh issue view, docs/concepts/determinism.mdx and SKILL.md line 12 on main
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `691385421b1b245435e87141a0f2e0a816318b47a951e238b80b655827c720da`
- Lane: contrarian

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-03-10
- default_branch: main
- fetched_at: 2026-11-12
- forks: 7671
- installs: 1524572
- installs_by_skill: {"general-video": 661816, "hyperframes": 1486779, "hyperframes-animation": 1005453, "hyperframes-audio": 663932, "hyperframes-cli": 1524572, "hyperframes-core": 931131, "hyperframes-creative": 917182, "hyperframes-keyframes": 754861, "hyperframes-registry": 1274564, "media-use": 1395655}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 245
- registry: skills.sh
- sources: https://api.github.com/repos/heygen-com/hyperframes, https://skills.sh/api/search?q=hyperframes
- stars: 83132

## Related

- evaluated_on: [HyperFrames](../tool/heygen-com__hyperframes.md)
- contradicts: [HyperFrames vs Remotion (HeyGen guide)](hyperframes.heygen.com__guides__hyperframes-vs-remotion.md) - The vendor comparison presents rule-following as the only way HyperFrames breaks; this issue is an engine-side capture race.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
