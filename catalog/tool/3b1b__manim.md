# ManimGL (3b1b/manim)

`tool:3b1b/manim` - tool - <https://github.com/3b1b/manim>

Grant Sanderson's own Manim, installed as `manimgl`. It plays scenes in an OpenGL window and writes a file with `-w`.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Also known as: manimgl, 3b1b manim

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The original engine behind 3Blue1Brown videos. An agent that writes ManimCE code for it, or the reverse, gets errors, so the reader must pick one.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | renderer |
| agents | none-stated |
| levers | motion, design |
| cost | free-local |

On a Mac it needs FFmpeg and, on ARM, Cairo from Homebrew; LaTeX is optional (MacTeX is about 6 GB, BasicTeX is the README's lighter path). The default run opens a window for a person; an agent needs `-w` to write a file or `-so` to save the final frame. Fewer tests and docs than ManimCE by its own README's account.

## Claims

1. Its README says the community edition was forked to be more stable, better tested and easier to start with.

   > In 2020 a group of developers forked it into what is now the [community edition](https://github.com/ManimCommunity/manim/), with a goal of being more stable, better tested, quicker to respond to community contributions, and all around friendlier to get started with.

   Locator: README.md, introduction. Source: <https://github.com/3b1b/manim/blob/master/README.md>, retrieved 2026-11-12.

2. The pip package is manimgl, not manim.

   > The package name is `manimgl` instead of `manim` or `manimlib`.

   Locator: README.md, Installation, note. Source: <https://github.com/3b1b/manim/blob/master/README.md>, retrieved 2026-11-12.

3. A flag saves the final frame as an image, which an agent can inspect.

   > `-so` will save the final frame to an image and show it

   Locator: README.md, Using manim, CLI flags. Source: <https://github.com/3b1b/manim/blob/master/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md against the claims and against the ManimCE README
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `11b1db61a963e7168ed0af276cfb88f4f9110892c851638815b9a6a2f61e1324`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2015-03-22
- default_branch: master
- fetched_at: 2026-11-12
- forks: 7923
- last_activity: 2026-09-09
- licence: MIT
- open_issues: 519
- sources: https://api.github.com/repos/3b1b/manim, https://skills.sh/api/search?q=manim
- stars: 96431

## Related

- alternative_to: [Manim Community Edition](manimcommunity__manim.md)

## Referenced by

- [Manim Community Edition](manimcommunity__manim.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
