# Manim Community Edition

`tool:manimcommunity/manim` - tool - <https://github.com/ManimCommunity/manim>

A Python animation engine for explanatory math video, forked from 3b1b/manim in 2020 and run by a community team. The `manim` CLI renders a Scene class to a video file.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Review loop](../../docs/glossary.md#review-loop), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Also known as: ManimCE, manim

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The usual route for diagram and equation animation written by an agent in Python, with a one-flag way to get the last frame as a PNG.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | renderer |
| agents | none-stated |
| levers | motion, design, review-loop |
| cost | free-local |

`manim -s` (or `--format=png`) writes only the last frame, and `-ql` renders at low quality; both cut the review loop for an agent. Install needs system packages (the README points to per-OS docs; LaTeX only for TeX). The README says a major refactor is in progress, so APIs may move. Do not mix its install steps with 3b1b/manim: the package names differ and both READMEs warn of breakage.

## Claims

1. It is the community-maintained fork of 3b1b/manim, and its maintainers recommend it over the original.

   > It was forked from 3b1b/manim, a tool originally created and open-sourced by Grant Sanderson

   Locator: README.md, note under the introduction. Source: <https://github.com/ManimCommunity/manim/blob/main/README.md>, retrieved 2026-11-12.

2. The CLI can skip the animation and save only the final frame as a PNG.

   > -s, --save_last_frame Fast-forward animations and save the last frame

   Locator: docs.manim.community, Configuration guide, command line help. Source: <https://docs.manim.community/en/stable/guides/configuration.html>, retrieved 2026-11-12.

3. Using the other project's install instructions breaks the install.

   > Trying to use these instructions to install [3b1b/manim](https://github.com/3b1b/manim) or instructions there to install this version will cause problems.

   Locator: README.md, Installation, caution box. Source: <https://github.com/ManimCommunity/manim/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and the docs configuration guide against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `b0e80254b6242cff7f662f3e8e528d868f9a94ca88d490585d02235d123fca8d`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-05-19
- default_branch: main
- fetched_at: 2026-11-12
- forks: 3326
- last_activity: 2026-11-11
- licence: MIT
- open_issues: 399
- sources: https://api.github.com/repos/ManimCommunity/manim, https://skills.sh/api/search?q=manim
- stars: 42431

## Related

- alternative_to: [ManimGL (3b1b/manim)](3b1b__manim.md) - Fork of it; different package and CLI.

## Referenced by

- [See Before You Code: Learning Visual Priors for Spatially Aware Educational Animation Generation (OmniManim)](../source/arxiv.org__abs__2605.15585.md) (evaluated_on)
- [ManimGL (3b1b/manim)](3b1b__manim.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
