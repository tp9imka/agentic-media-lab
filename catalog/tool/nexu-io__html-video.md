# html-video

`tool:nexu-io/html-video` - tool - <https://github.com/nexu-io/html-video>

A local studio and CLI that has a coding agent write animated HTML frames from a prompt, article or repo, then renders them to MP4 through the HyperFrames engine.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent portability](../../docs/glossary.md#agent-portability), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines)

Also known as: nexu-io html-video, Open Design html-video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A wrapper that drives Claude Code or Codex as a subprocess and ships 21 templates; only the HyperFrames engine works so far.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: experimental.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex, cursor, gemini-cli, hermes |
| levers | design, story, audio, orchestration |
| cost | mixed |

Needs Node 20+, pnpm, ffmpeg and Playwright Chromium. Remotion, Motion Canvas, Revideo and Manim adapters are planned, not built. It runs some agents with permission-skipping flags (`--yolo`, `--allow-all-tools`); check what it launches before use. Optional soundtrack needs a paid MiniMax key. Its engine table says Remotion is paid above 4 devs, which differs from Remotion's own licence text (free up to 3 employees).

## Claims

1. Only the HyperFrames engine renders today; the other engines are on the roadmap.

   > Remotion, Motion Canvas / Revideo, and Manim are on the roadmap: the adapter interface is designed for them, but their adapters aren't built yet.

   Locator: README.md, Why this exists, Status note. Source: <https://github.com/nexu-io/html-video/blob/main/README.md>, retrieved 2026-11-12.

2. It invokes some agent CLIs with flags that skip permission prompts.

   > `copilot --allow-all-tools`, prompt via stdin

   Locator: README.md, Supported agents, GitHub Copilot CLI row. Source: <https://github.com/nexu-io/html-video/blob/main/README.md>, retrieved 2026-11-12.

3. Its engine table describes Remotion's licence as paid above 4 developers.

   > Source-available, paid above 4 devs

   Locator: README.md, Why this exists, engine table, Remotion row. Source: <https://github.com/nexu-io/html-video/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `dc1a5fc6c7f1123ffef42929c0931cf941a78024a740681837be2926feadcce6`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-05-27
- default_branch: main
- fetched_at: 2026-11-12
- forks: 583
- installs: 77
- installs_by_skill: {"frame-bold-signal": 73, "frame-build-minimal": 75, "frame-data-chart-nyt": 71, "frame-electric-studio": 77, "frame-glitch-title": 69, "frame-light-leak-cinema": 71, "frame-liquid-bg-hero": 69, "frame-logo-outro": 69, "frame-pentagram-stat": 74, "vfx-text-cursor": 69}
- last_activity: 2026-06-21
- licence: Apache-2.0
- open_issues: 55
- registry: skills.sh
- sources: https://api.github.com/repos/nexu-io/html-video, https://skills.sh/api/search?q=html-video
- stars: 4831

## Related

- depends_on: [HyperFrames](heygen-com__hyperframes.md)
- contradicts: [Remotion](remotion-dev__remotion.md) - Licence threshold stated differently.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
