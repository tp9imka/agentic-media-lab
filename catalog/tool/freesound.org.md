# Freesound API

`tool:freesound.org` - tool - <https://freesound.org/docs/api/>

A collaborative library of Creative Commons sound recordings with a REST API (APIv2) for search, metadata and download, using token or OAuth2 authentication.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Licences and territory](../../docs/glossary.md#licences-and-territory)

Also known as: Freesound, freesound apiv2

Tags: sound-effects, creative-commons, attribution

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the free source of real recorded sound effects an agent can search by text, but each sound carries its own licence, so the agent must filter and credit.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | audio, asset |
| cost | free-tier |

Filter to CC0 for zero obligations; CC BY needs a credit line in the description; drop CC BY-NC and the legacy Sampling+ for monetised or ad work. A key needs a free account at freesound.org/apiv2/apply. Some resources are OAuth2-only; which ones (likely full-quality download) was not checked here, previews are low-bitrate mp3 or ogg per the FAQ. Stable Audio Open was trained mostly on Freesound CC audio, which does not change the licence of a sound you download.

## Claims

1. Freesound's own summary of its licences: CC0 allows almost anything, CC BY needs credit, and non-commercial bars earning money from the work.

   > for the "zero" license you can do pretty much what you want with the sound. You could even sell the sound, ... but you can't claim you are the author! For "attribution" you should always mention the original creators of the sounds when you use them. "Noncommercial" works like attribution, but you can't earn any money with the piece of work you create!

   Locator: FAQ, Licenses, answer to which files you can use. Source: <https://freesound.org/help/faq/>, retrieved 2026-11-12.

2. Legacy Sampling+ sounds also cannot be used in commercial advertising.

   > you can do pretty much what you could do with the attribution noncommercial license, but additionally you can't make commercial advertisement with the sound.

   Locator: FAQ, Licenses, Sampling+ paragraph. Source: <https://freesound.org/help/faq/>, retrieved 2026-11-12.

3. Token authentication is enough for most resources, but some are restricted to OAuth2.

   > Most of the resources are accessible using both authentication strategies but some of them are restricted to the use of OAuth2.

   Locator: API docs, Authentication, introduction. Source: <https://freesound.org/docs/api/authentication.html>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Freesound API index, API authentication page and the Freesound FAQ licence sections against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `baf87a342f9f61d86a814c940acbf6387a27c671044c497554b768545c9a06c6`
- Lane: media-stages

## Observed

Nothing collected yet.

## Related

- alternative_to: [Stable Audio Open](../model/stabilityai__stable-audio.md) - Generated SFX instead of recorded; trained on Freesound CC0, CC BY and CC Sampling+ audio.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
