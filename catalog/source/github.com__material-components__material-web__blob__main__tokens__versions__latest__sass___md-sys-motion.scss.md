# Material 3 motion tokens (material-web, _md-sys-motion.scss)

`source:github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss` - source - <https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss>

Google's generated Sass file of Material 3 system motion tokens for the web: duration steps from 50 ms to 1000 ms, cubic-bezier easing curves, and spring damping and stiffness values.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Tags: easing, duration, design-tokens

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An agent animating UI-style titles can use these values as named durations and curves instead of one default ease for everything.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

Read from the token file because m3.material.io renders by script and returned no text. A search snippet from m3.material.io says the easing and duration system is no longer maintained in favour of springs; that page was not opened. The same file carries spring tokens (stiffness and damping) for GSAP or Motion Canvas spring eases. UI durations are for taps; a video title entrance usually runs longer.

## Claims

1. The medium duration steps are 250, 300, 350 and 400 ms.

   > $duration-medium1: 250ms; /// md.sys.motion.duration.medium2 (Duration) $duration-medium2: 300ms; /// md.sys.motion.duration.medium3 (Duration) $duration-medium3: 350ms; /// md.sys.motion.duration.medium4 (Duration) $duration-medium4: 400ms;

   Locator: _md-sys-motion.scss, duration tokens. Source: <https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss>, retrieved 2026-11-12.

2. The emphasized-decelerate curve is cubic-bezier(0.05, 0.7, 0.1, 1).

   > $easing-emphasized-decelerate: cubic-bezier(0.05, 0.7, 0.1, 1);

   Locator: _md-sys-motion.scss, easing tokens. Source: <https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss>, retrieved 2026-11-12.

3. In this web token set, the emphasized easing is an alias of standard, not its own curve.

   > /// md.sys.motion.easing.emphasized (Easing) $easing-emphasized: $easing-standard;

   Locator: _md-sys-motion.scss, last token. Source: <https://github.com/material-components/material-web/blob/main/tokens/versions/latest/sass/_md-sys-motion.scss>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `2493ded90850d1593f0c4271564ef716c6717f8cfa1b53b704f12371229de6f7`
- Lane: craft

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2018-03-27
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1171
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 193
- sources: https://api.github.com/repos/material-components/material-web, https://skills.sh/api/search?q=material-web
- stars: 11434

## Related

- alternative_to: [IBM Carbon Design System - Motion](carbondesignsystem.com__elements__motion__overview.md)

## Referenced by

- [IBM Carbon Design System - Motion](carbondesignsystem.com__elements__motion__overview.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
