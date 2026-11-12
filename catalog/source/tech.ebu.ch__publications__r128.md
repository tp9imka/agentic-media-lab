# EBU R 128 - Loudness normalisation and permitted maximum level of audio signals

`source:tech.ebu.ch/publications/r128` - source - <https://tech.ebu.ch/publications/r128>

The European Broadcasting Union recommendation that sets programme loudness, true-peak ceiling and the meters to measure them. Version 5.0, November 2023. Supplement s1 adds a short-term loudness cap for adverts and promos.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Delivery](../../docs/glossary.md#delivery)

Tags: loudness, lufs, true-peak

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives the two numbers a mix check needs, integrated loudness and true peak, plus a third for short clips, all measurable with ffmpeg ebur128.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Check a render with `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -` and compare I and True peak with the numbers below. -23 LUFS is a broadcast target: it plays quiet next to phone-first feeds, see the streaming supplement s2 for the interim range. The main text says Loudness Range is not recommended for programmes under 1 minute, so do not gate a short clip on LRA. The publication page sits behind a member-login banner but the PDF opened without one.

## Claims

1. The programme's integrated loudness target is -23.0 LUFS.

   > the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS

   Locator: r128.pdf (v5.0, 2023), recommends item h. Source: <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128.pdf>, retrieved 2026-11-12.

2. True peak must stay at or below -1 dBTP during production.

   > that the True Peak Level of a programme shall not exceed −1 dBTP (dB True Peak) during production (linear audio)

   Locator: r128.pdf (v5.0, 2023), recommends item m. Source: <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128.pdf>, retrieved 2026-11-12.

3. For short-form content such as adverts and promos, short-term (3 s) loudness must not exceed -18.0 LUFS.

   > that the Short-term Loudness Level (measured in compliance with EBU Tech 3341 [2]) shall not exceed −18.0 LUFS (+5.0 LU on the relative scale)

   Locator: r128s1.pdf (2020), recommends item d. Source: <https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s1.pdf>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. publication page, R 128 v5.0 PDF and R 128 s1 PDF against the three claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `3884fc6fdb228acb7d988b3c6f7f8a5b8217a6737198f6e2ce35b164b344366f`
- Citation: type report; author European Broadcasting Union; issued 2023-11; container_title EBU Recommendation R 128; url https://tech.ebu.ch/files/live/sites/tech/files/shared/r/r128.pdf; accessed 2026-11-12
- Lane: craft

## Observed

Nothing collected yet.

## Related

- integrates_with: [FFmpeg](../tool/ffmpeg__ffmpeg.md) - ebur128 measures, loudnorm corrects; loudnorm defaults to I=-24
- extends: [EBU R 128 s2 - Loudness in Streaming](tech.ebu.ch__files__live__sites__tech__files__shared__r__r128s2.pdf.md)

## Referenced by

- [EBU R 128 s2 - Loudness in Streaming](tech.ebu.ch__files__live__sites__tech__files__shared__r__r128s2.pdf.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
