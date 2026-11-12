# Netflix English (USA) Timed Text Style Guide

`source:partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-english-usa-timed-text-style-guide` - source - <https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide>

Netflix's subtitle rules for English (USA), read together with its general timed-text requirements: characters per line, reading speed and per-event duration limits.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions)

Tags: subtitles, reading-speed, cps

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Every number here is a direct lint rule for an SRT or VTT file an agent writes: line length, characters per second, minimum and maximum time on screen.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Lint each cue: max 2 lines, <= 42 characters per line, <= 20 characters per second, duration between 0.834 s and 7 s. The 42-character line assumes a 16:9 frame; for 9:16 use the BBC width rule instead. One skill in the hub ships a caption validator with the same 42 and 20 defaults. Written for long-form dialogue, not for word-by-word kinetic captions.

## Claims

1. Adult programmes allow up to 20 characters per second; children's up to 17.

   > Adult programs: Up to 20 characters per second

   Locator: English (USA) guide, section I.14 Reading Speed Limits. Source: <https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide>, retrieved 2026-11-12.

2. A line holds at most 42 characters.

   > I.2. Character Limitation 42 characters per line

   Locator: English (USA) guide, section I.2 Character Limitation. Source: <https://partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-English-USA-Timed-Text-Style-Guide>, retrieved 2026-11-12.

3. Each subtitle event stays on screen at least 5/6 of a second (20 frames at 24 fps) and at most 7 seconds.

   > Minimum duration: 5/6 (five-sixths) of a second per subtitle event (e.g. 20 frames for 24fps) Maximum duration: 7 seconds per subtitle event

   Locator: General Requirements article, section 1 Duration. Source: <https://partnerhelp.netflixstudios.com/hc/en-us/articles/215758617-Timed-Text-Style-Guide-General-Requirements>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. English (USA) guide and General Requirements article against the claims
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `728a2b5bbb9081dfeff0c1c9626c7c9181defdb937f8574ff3bd828e61644ff9`
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [BBC Subtitle Guidelines](bbc.co.uk__accessibility__forproducts__guides__subtitles.md)
- integrates_with: [generative-media-skills](../tool/calesthio__generative-media-skills.md) - its validate_captions.py defaults to 42 characters per line and a 20 cps warning

## Referenced by

- [BBC Subtitle Guidelines](bbc.co.uk__accessibility__forproducts__guides__subtitles.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
