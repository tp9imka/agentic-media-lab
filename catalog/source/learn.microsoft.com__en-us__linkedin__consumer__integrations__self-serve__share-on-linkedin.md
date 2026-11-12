# LinkedIn - Share on LinkedIn (self-serve) and Videos API

`source:learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin` - source - <https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin>

LinkedIn's self-serve product for posting to a member's own feed, read with the Videos API specs and the Community Management API overview.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules)

Tags: linkedin, video-specs

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It separates the self-serve route a single developer can add today from the vetted route needed for company pages.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intermediate. Maturity: -.

For your own profile, add the 'Share on LinkedIn' product in the developer portal to get w_member_social; it supports feedshare-video. Company page posting needs the Community Management API, a vetted product with a Development tier and a Standard tier that asks for a screencast. Video (non-connected-TV specs): MP4, 3 s to 30 min, 75 KB to 500 MB per the Videos API; the same page also says the maximum is 5 GB, an inconsistency not resolved here. Daily request limits (UTC): 150 per member, 100,000 per application.

## Claims

1. A developer can grant their app w_member_social by adding the Share on LinkedIn product in the developer portal.

   > If your application does not have this permission, you can add it through the Developer Portal. Select your app from My Apps, navigate to the Products tab, and add the Share on LinkedIn product which will grant you w_member_social.

   Locator: Share on LinkedIn, Permissions. Source: <https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin>, retrieved 2026-11-12.

2. LinkedIn's specs for non-connected-TV video are MP4, 3 seconds to 30 minutes, 75 KB to 500 MB; the upload schema allows up to 5 GB.

   > Length: Three seconds to 30 minutes. File size: Between 75kb and 500MB. File format: MP4.

   Locator: Videos API, Video File Size Specifications. Source: <https://learn.microsoft.com/en-us/linkedin/marketing/community-management/shares/videos-api>, retrieved 2026-11-12.

3. The Community Management API's Standard tier requires a screencast of each use case.

   > When applying for Standard Tier, provide a screencast video demonstrating each use case specified in your access request form, matching the use cases described in the Standard Tier access request form.

   Locator: Community Management API overview, Program Tiers. Source: <https://learn.microsoft.com/en-us/linkedin/marketing/community-management/community-management-overview>, retrieved 2026-11-12.

## Provenance

- Source type: primary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `c9e4508244bc943c49acbfe0fc905424d88f9883a138585fa0742f0da1cbcb00`
- Lane: publishing

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
