# EBU R 128 s2 - Loudness in Streaming

`source:tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf` - source - <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf>

EBU supplement on loudness for streamed programmes. It keeps -23 LUFS as the default and allows a louder interim distribution level for phones and noisy settings.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Delivery](../../docs/glossary.md#delivery)

Tags: loudness, lufs, streaming

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the only standards-body number found for a louder-than-broadcast streaming mix, the case most short clips fall into.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Pick -16 LUFS integrated with -1 dBTP as a phone-first target and stay inside the EBU range. A skill in the hub masters at -14 LUFS, which is louder than the top of this range; no first-party platform page stating -14 was opened here. The publication landing page returned HTTP 403 to a scripted fetch, so the PDF is the record URL.

## Claims

1. The default is to stream programmes unchanged at -23.0 LUFS.

   > that programmes should be streamed unchanged, that is at −23.0 LUFS

   Locator: r128s2.pdf (2023), recommends item e. Source: <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf>, retrieved 2026-11-12.

2. Without loudness metadata, a broadcaster that wants to control the dynamic treatment may distribute louder, in an interim range of -20.0 to -16.0 LUFS.

   > the interim value for the Distribution Loudness Level should be in the range of −20.0 to −16.0 LUFS

   Locator: r128s2.pdf (2023), further recommends item g. Source: <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `72da8698a1f60d6063411d64ab9f99c1cf6f46f0d54bcb1d793797eef835556f`
- Citation: type report; author European Broadcasting Union; issued 2023; container_title EBU Recommendation R 128 s2; url https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf; accessed 2026-11-12
- Lane: craft

## Observed

Nothing collected yet.

## Related

- extends: [EBU R 128 - Loudness normalisation and permitted maximum level of audio signals](tech.ebu.ch__publications__r128.md)
- contradicts: [motion-graphics (Mort1d)](../tool/mort1d__motion-graphics-skills.md) - the skill masters at -14 LUFS, above this range's -16.0 LUFS ceiling

## Referenced by

- [EBU R 128 - Loudness normalisation and permitted maximum level of audio signals](tech.ebu.ch__publications__r128.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
