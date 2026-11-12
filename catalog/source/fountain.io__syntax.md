# Fountain screenplay syntax

`source:fountain.io/syntax` - source - <https://fountain.io/syntax/>

A plain-text screenplay markup. Scene headings, action, dialogue and transitions are recognised from line shape, and sections and synopses add outline notes that do not print.

Concepts: [Story and decomposition](../../docs/glossary.md#story-and-decomposition)

Tags: screenplay, script-format

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An agent can write the script stage as a Fountain file the reader can open in screenwriting apps, with scenes and transitions parseable by line rules.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Emit one scene heading per scene and put shot notes in synopses (= lines) so they stay out of printed pages; not every screenwriting app supports synopses, and some import them as notes. Fountain has no field for duration, camera or asset; keep a separate JSON shot list keyed by scene number (#1#, #1A#) for those. Parsers differ on edge cases; none were run here.

## Claims

1. Unless forced with a leading period, a scene heading is a line starting with INT, EXT or similar, with a blank line before and after it.

   > A Scene Heading is any line that has a blank line following it, and either begins with INT or EXT or similar (full list below).

   Locator: section Scene Headings. Source: <https://fountain.io/syntax/>, retrieved 2026-11-12.

2. Unless forced with a leading >, a transition is uppercase, has empty lines around it and ends in TO:.

   > Uppercase Preceded by and followed by an empty line Ending in TO:

   Locator: section Transition. Source: <https://fountain.io/syntax/>, retrieved 2026-11-12.

3. Synopses are single lines starting with = and are left out of formatted output.

   > Synopses are single lines prefixed by an equals sign =. They can be located anywhere within the screenplay.

   Locator: section Sections and Synopses. Source: <https://fountain.io/syntax/>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `e573bf613686a703ca1126c360df489c5e3f472612171a240bbd127df6731a79`
- Lane: craft

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
