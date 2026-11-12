# BBC Subtitle Guidelines

`source:bbc.co.uk/accessibility/forproducts/guides/subtitles` - source - <https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>

The BBC's editorial and technical rules for subtitles: reading rate, line length, line count, font size and placement, with separate numbers for vertical 9:16 video.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Visual design](../../docs/glossary.md#visual-design)

Tags: subtitles, reading-speed, vertical-video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the one primary caption guide found that gives line width and font size for vertical video, which is the frame most agent-made shorts use.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Turn the rate into a check: on-screen seconds >= 0.3 x word count per caption. The page also recommends at most three lines for 9:16 and two for 16:9. Width is set as a share of the frame, so measure rendered text width rather than counting characters when the font is proportional. The older address bbc.github.io/subtitle-guidelines returned 404 on 2026-11-12. The page is long; only the sections quoted were compared.

## Claims

1. Leave a caption up for about 0.3 seconds per word, based on 160-180 words per minute.

   > Based on the recommended rate of 160-180 words per minute, you should aim to leave a subtitle on screen for a minimum period of around 0.3 seconds per word (e.g. 1.2 seconds for a 4-word subtitle).

   Locator: section 4.1 Target minimum timing. Source: <https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>, retrieved 2026-11-12.

2. As a guide, a 90%-width region of vertical 9:16 video holds about 25 characters, the equivalent of 37 characters in a 75%-width 16:9 region.

   > As a guide, the equivalent to 37 characters in a 75% width region of a 16:9 (landscape) video is 25 characters in a 90% width region of a 9:16 (vertical) video.

   Locator: section 3.1 Line length, table Characters per line and note below it. Source: <https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>, retrieved 2026-11-12.

3. For 9:16 video, set the font to fit a line height of 3.9% to 4.5% of the active video height.

   > Font size should be set to fit within a line height in the range 3.9% to 4.5% of the active video height for 9:16 aspect ratio videos,

   Locator: section 9.2.1 Authoring font size. Source: <https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `91cd8d1d9c3edebf1af3f189f77573eb5c463a5226beaf62662f70b530bf2584`
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [Netflix English (USA) Timed Text Style Guide](partnerhelp.netflixstudios.com__hc__en-us__articles__217350977-english-usa-timed-text-style-guide.md) - Netflix counts characters per second; BBC counts words per minute
- integrates_with: [ttml-validator (BBC)](../tool/bbc__ttml-validator.md)

## Referenced by

- [TikTok Ads - Creative best practices for performance ads](ads.tiktok.com__help__article__creative-best-practices.md) (contradicts)
- [Netflix English (USA) Timed Text Style Guide](partnerhelp.netflixstudios.com__hc__en-us__articles__217350977-english-usa-timed-text-style-guide.md) (alternative_to)
- [ttml-validator (BBC)](../tool/bbc__ttml-validator.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
