# YouTube Data API (v3) revision history

`source:developers.google.com/youtube/v3/revision_history` - source - <https://developers.google.com/youtube/v3/revision_history>

Google's change log for the YouTube Data API v3. Two entries matter here: November 2, 2026, which ends private-only uploads for unverified projects, and October 30, 2024, which adds the synthetic-media flag.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules)

Also known as: YouTube API audit private-only lifted

Tags: youtube, audit, ai-label

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Most guides still say an unaudited YouTube project uploads private-only. Since November 2, 2026 that is no longer true, which makes YouTube the easiest public target for a one-person pipeline.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

The 2020 private-only rule is still on the same page under July 28, 2020; read the date. Set status.privacyStatus explicitly: since November 2, 2026 the default is public unless creator account settings make it private, so a test upload you meant to keep private can go live. Set status.containsSyntheticMedia=true on realistic generated clips (see the disclosure help page). The page URL now redirects to developers.google.com/youtube/data/revision_history. The quota (100 uploads a day) is on the videos.insert record.

## Claims

1. Since November 2, 2026, videos uploaded from unverified API projects are no longer forced private, reversing the July 2020 rule.

   > Videos uploaded through the videos.insert method from unverified API projects are no longer restricted to private viewing mode. This change reverses the policy announced on July 28, 2020, which restricted videos uploaded from unverified API projects created after that date to private viewing mode until the project completed an audit.

   Locator: Entry November 2, 2026. Source: <https://developers.google.com/youtube/v3/revision_history>, retrieved 2026-11-12.

2. From the November 2, 2026 entry, an upload without status.privacyStatus defaults to public, though creator account settings can make some uploads default to private.

   > If you don't specify a value for the status.privacyStatus property in a videos.insert request, the uploaded video's privacy status defaults to public.

   Locator: Entry November 2, 2026. Source: <https://developers.google.com/youtube/v3/revision_history>, retrieved 2026-11-12.

3. The API flag for realistic altered or synthetic content is status.containsSyntheticMedia, settable on insert or update.

   > To indicate whether a video contains A/S content, set the status.containsSyntheticMedia property. This property can be set when calling the videos.insert or videos.update methods.

   Locator: Entry October 30, 2024. Source: <https://developers.google.com/youtube/v3/revision_history>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `40077a7c1bc59481b2f5ccfb5d1858a5d2b8a9d3215a38b3c5517c35d6fc4d00`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

- integrates_with: [YouTube Data API - videos.insert and quota costs](developers.google.com__youtube__v3__docs__videos__insert.md)
- integrates_with: [YouTube Help - Disclosing use of GenAI content](support.google.com__youtube__answer__14328491.md)

## Referenced by

- [YouTube Data API - videos.insert and quota costs](developers.google.com__youtube__v3__docs__videos__insert.md) (integrates_with)
- [YouTube Help - Disclosing use of GenAI content](support.google.com__youtube__answer__14328491.md) (integrates_with)
- [Postiz](../tool/gitroomhq__postiz-app.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
