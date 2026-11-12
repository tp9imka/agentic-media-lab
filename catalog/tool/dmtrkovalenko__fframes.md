# fframes

`tool:dmtrkovalenko/fframes` - tool - <https://github.com/dmtrKovalenko/fframes>

A Rust framework where each frame is an SVG tree returned by a function, drawn with Skia on the GPU and encoded with statically linked FFmpeg libraries. It ships a skill and a preview window with scrubbing.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent Skills](../../docs/glossary.md#agent-skills), [Review loop](../../docs/glossary.md#review-loop)

Also known as: cargo-fframes

**Badge:** quoted, not read at the primary source (`quoted-secondary`): primary source read; downgraded one step: interested-party.

**Why:** A browser-free renderer aimed at agent iteration speed. Its speed claim against Remotion is the vendor's own and unmeasured here.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | any-skill |
| levers | motion, audio, captions, review-loop |
| cost | free-local |

Needs Rust and, on macOS, `brew install pkg-config ffmpeg x264 x265 opus nasm ninja`; the first build downloads prebuilt Skia and FFmpeg for macOS arm64. The agent writes Rust, so compile errors are part of the loop. The skill installs from a remote site (`npx skills add https://fframes.studio`); read it before installing. `cargo run --release -- preview` opens a window for a person; I did not find a documented still-frame command for the agent.

## Claims

1. The project claims to render more than 30 times faster than Remotion.

   > we are over 30x faster than remotion

   Locator: README.md, What is it for. Source: <https://github.com/dmtrKovalenko/fframes/blob/main/README.md>, retrieved 2026-11-12.

2. A missing font falls back silently in the render; the inspect command reports it and the fix is to put the font file in media/.

   > **Text renders in the wrong font:** `inspect` reports `No match for ... font-family`; put the font file in the

   Locator: README.md, Requirements, Troubleshooting. Source: <https://github.com/dmtrKovalenko/fframes/blob/main/README.md>, retrieved 2026-11-12.

3. Its skill installs from the project's website rather than from the repo.

   > npx skills add https://fframes.studio

   Locator: README.md, Get started. Source: <https://github.com/dmtrKovalenko/fframes/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `bacfcc9216c364c300193c95df4041063a59215984fdaa2ee0d40bb6a020dba4`
- Badge downgraded: interested-party - The speed claim is the vendor's own benchmark against a competitor.
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2021-11-22
- default_branch: main
- fetched_at: 2026-11-12
- forks: 94
- installs: 211
- installs_by_skill: {"fframes-video": 211}
- last_activity: 2026-11-08
- licence: MIT
- open_issues: 24
- registry: skills.sh
- sources: https://api.github.com/repos/dmtrKovalenko/fframes, https://skills.sh/api/search?q=fframes
- stars: 3080

## Related

- alternative_to: [Remotion](remotion-dev__remotion.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
