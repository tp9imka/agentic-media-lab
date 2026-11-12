# Kinetograph

`tool:0xs4n4tg/kinetograph` - tool - <https://github.com/0xS4N4TG/kinetograph>

A browser-free video engine: Node runs a Remotion-style TSX or HTML project and a Rust GPU compositor draws each frame. It states that Remotion and HyperFrames projects render unchanged.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Consistency](../../docs/glossary.md#consistency)

Also known as: kinetograph

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It could give Remotion or HyperFrames code a render path with no Chrome, and its docs list in detail what it cannot draw. The repo was created on 2026-10-23 and is in beta.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: experimental.

| field | value |
|---|---|
| tool_type | renderer |
| agents | claude-code, codex |
| levers | motion, design, audio, review-loop |
| cost | free-local |

Prebuilt package for macOS on Apple Silicon, Node 22+. `kinetograph doctor <entry>` lists every unsupported element and frame before a long render, and `--strict` fails the render instead of drawing an approximation; use both in agent loops. It reads no system fonts: CJK, Arabic and Devanagari draw as boxes unless you load a font. Compatibility claims against Remotion and HyperFrames are the author's; not measured here. Running it on Remotion code does not change what Remotion's licence asks of you; I did not check that question.

## Claims

1. It renders without a browser, using a Rust GPU compositor, and states that Remotion and HyperFrames projects render as they are.

   > Existing Remotion projects render as they are, and so do

   Locator: README.md, introduction. Source: <https://github.com/0xS4N4TG/kinetograph/blob/main/README.md>, retrieved 2026-11-12.

2. A doctor command checks every frame without the GPU and lists what cannot be drawn, before a long render.

   > kinetograph doctor <entry> goes through every frame without the GPU and lists what can't be drawn, on which frames, and any scene a render would refuse.

   Locator: kinetograph.dev docs, Compatibility, introduction. Source: <https://kinetograph.dev/docs/compat/>, retrieved 2026-11-12.

3. Its docs admit rare non-identical output between GPU renders at the same settings, and give a bit-exact fallback.

   > Rarely, when renderers share the GPU, two renders at the same concurrency differ by 1 in one colour channel on a few pixels of a frame.

   Locator: kinetograph.dev docs, Compatibility, last section. Source: <https://kinetograph.dev/docs/compat/>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and the docs Compatibility page against the claims
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `bba2ef425d116dae0fd1bf10002f04e72d46640b10e0de67ae5bcaabaddb2e79`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-23
- default_branch: main
- fetched_at: 2026-11-12
- forks: 38
- installs: 199
- installs_by_skill: {"kinetograph": 199, "kinetograph-create": 9, "kinetograph-migrate": 165, "kinetograph-render": 9, "kinetograph-studio": 9}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 9
- registry: skills.sh
- sources: https://api.github.com/repos/0xS4N4TG/kinetograph, https://skills.sh/api/search?q=kinetograph
- stars: 501

## Related

- alternative_to: [Remotion](remotion-dev__remotion.md)
- alternative_to: [HyperFrames](heygen-com__hyperframes.md)

## Referenced by

- [Remotion](remotion-dev__remotion.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
