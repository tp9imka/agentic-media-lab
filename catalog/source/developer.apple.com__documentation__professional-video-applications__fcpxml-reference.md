# FCPXML Reference (Apple Developer)

`source:developer.apple.com/documentation/professional-video-applications/fcpxml-reference` - source - <https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference>

Apple's reference for FCPXML, the XML format for sending media, timelines, markers and metadata into and out of Final Cut Pro.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Delivery](../../docs/glossary.md#delivery)

Tags: fcpxml, final-cut-pro

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Final Cut Pro has no scripting API an agent can call, so writing FCPXML, the format users send into Final Cut Pro, is the documented path, and several tools here export it.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

An agent can write the file; no command-line import is documented on this page. Version matters: this page states the 1.9 requirement while MakeMyClip writes 1.10, so match the version to the reader's Final Cut build. Resolve and Premiere also read FCPXML through the tools that export it, not through this page. Saved text is from the page's JSON data, not the rendered HTML.

## Claims

1. FCPXML describes media, metadata and timeline items exchanged with Final Cut Pro.

   > Use FCPXML to describe the media, metadata, and other items users send and receive between your app and Final Cut Pro.

   Locator: Overview, first paragraph. Source: <https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference>, retrieved 2026-11-12.

2. FCPXML 1.9 needs Final Cut Pro 10.4.9 or later.

   > FCPXML 1.9 requires Final Cut Pro 10.4.9 or later.

   Locator: Overview, note. Source: <https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference>, retrieved 2026-11-12.

3. It does not carry everything in a native Final Cut library.

   > But, it’s not a substitute for a native Final Cut Pro project and event data organized in a library bundle.

   Locator: Overview, note. Source: <https://developer.apple.com/documentation/professional-video-applications/fcpxml-reference>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `8a54a617efcf6429bf628c8001d2d67084ed4128cf2522067e306b7b174c792c`
- Lane: footage-editing

## Observed

Nothing collected yet.

## Related

- integrates_with: [MakeMyClip Editor](../tool/makemyclip__editor.md)

## Referenced by

- [MakeMyClip Editor](../tool/makemyclip__editor.md) (integrates_with)
- [Auto-Editor](../tool/wyattblue__auto-editor.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
