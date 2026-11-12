# GSAP

`tool:greensock/gsap` - tool - <https://github.com/greensock/GSAP>

A JavaScript animation library, owned by Webflow, that HyperFrames uses for motion and Remotion projects can seek. It has no renderer of its own; a frame-seeking renderer captures it.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Code-driven video](../../docs/glossary.md#code-driven-video)

Also known as: GreenSock, gsap

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Most HTML video an agent writes moves with GSAP, so its licence terms apply to every HyperFrames project that uses it.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: established.

| field | value |
|---|---|
| tool_type | library |
| agents | none-stated |
| levers | motion |
| cost | free-local |

Commercial use costs nothing, including the plugins that used to be paid. The licence is not open source: it bans use in no-code visual animation builders that compete with Webflow without prior written consent, and Webflow can change the terms by posting new ones. A renderer must pause and seek GSAP timelines per frame; a tween left playing on the wall clock is what breaks HyperFrames and Remotion renders.

## Claims

1. Commercial use is covered at no charge, including formerly members-only plugins such as SplitText and MorphSVG.

   > Commercial usage is covered under the standard license.

   Locator: gsap.com/standard-license, FAQ. Source: <https://gsap.com/standard-license>, retrieved 2026-11-12.

2. Use inside no-code visual animation tools that compete with Webflow is prohibited without prior written consent.

   > "Prohibited Uses" means any implementation and/or use of GSAP Products in tools that allow users to build visual animations without code that encourages, induces, or materially assists in creating a solution that competes with Webflow’s visual animation building capabilities.

   Locator: gsap.com/standard-license, I. Definitions. Source: <https://gsap.com/standard-license>, retrieved 2026-11-12.

3. AI-generated GSAP code is stated not to be a prohibited use.

   > AI-generated code is not a "Prohibited Use".

   Locator: gsap.com/standard-license, FAQ. Source: <https://gsap.com/standard-license>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `6340dffdce733fa2af357358defa467bbfcadddda8c566fa07cfed48fbb85b21`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2012-09-21
- default_branch: master
- fetched_at: 2026-11-12
- forks: 2380
- last_activity: 2026-11-04
- licence: unknown
- open_issues: 6
- sources: https://api.github.com/repos/greensock/GSAP, https://skills.sh/api/search?q=GSAP
- stars: 30504

## Related

- integrates_with: [HyperFrames](heygen-com__hyperframes.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
