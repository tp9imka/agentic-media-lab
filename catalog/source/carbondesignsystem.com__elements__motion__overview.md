# IBM Carbon Design System - Motion

`source:carbondesignsystem.com/elements/motion/overview` - source - <https://carbondesignsystem.com/elements/motion/overview/>

IBM Carbon's motion guidance: productive and expressive easing curves, entrance and exit easing, and six fixed duration tokens from 70 ms to 700 ms.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Tags: easing, duration

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It states the rule that duration grows with distance or size and gives curves in both CSS and After Effects terms, which maps onto code-driven video.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

Use productive curves for small UI moves and expressive for a hero element. The page also gives exit easing that speeds up as the element leaves, matching the HyperFrames skill rule that exits are shorter than entrances. The duration table is for interface feedback; scale up for video and keep the ratios. Table cells are joined with | in the saved text.

## Claims

1. Carbon ships six fixed duration tokens; the fastest, fast-01, is 70 ms.

   > duration-fast-01 | Micro-interactions such as button and toggle | 70ms

   Locator: section Duration, token table, first row. Source: <https://carbondesignsystem.com/elements/motion/overview/>, retrieved 2026-11-12.

2. Productive standard easing is cubic-bezier(0.2, 0, 0.38, 0.9).

   > motion(standard, productive) | cubic-bezier(0.2, 0, 0.38, 0.9)

   Locator: section Easing, Standard easing table, Productive row. Source: <https://carbondesignsystem.com/elements/motion/overview/>, retrieved 2026-11-12.

3. Duration should grow with the distance travelled or the size change.

   > the larger the change in distance (traveled) or size (scaling) of the element, the longer the animation takes.

   Locator: section Duration, first paragraph. Source: <https://carbondesignsystem.com/elements/motion/overview/>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `0ccd3f80b030d3d9b2e8a4ef95b77a74b87e28f7c68496977f3483ae2daa9b43`
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [Material 3 motion tokens (material-web, _md-sys-motion.scss)](github.com__material-components__material-web__blob__main__tokens__versions__latest__sass___md-sys-motion.scss.md)
- integrates_with: [HyperFrames](../tool/heygen-com__hyperframes.md) - both shorten or accelerate exits

## Referenced by

- [Material 3 motion tokens (material-web, _md-sys-motion.scss)](github.com__material-components__material-web__blob__main__tokens__versions__latest__sass___md-sys-motion.scss.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
