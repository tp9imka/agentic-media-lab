---
id: guide:publishing-rules
title: What each platform requires for automated, AI-assisted posts from one developer's own account
summary: Per-platform audit, rate limit, AI disclosure, monetisation and price rules for posting agent-made clips through official APIs, as quoted on 2026-11-12.
use_when: "Use this page when you want to post agent-made clips to your own accounts through official APIs and need each platform's audit, limit and AI-label rules."
concepts: [concept:publishing, concept:platform-rules, concept:automation]
last_reviewed: 2026-11-12
---

# What each platform requires for automated, AI-assisted posts from one developer's own account

A table of platform rules for a developer who posts their own clips through official APIs. All of it is read, not run: the hub has posted nothing. Read the table, then the TikTok and YouTube sections. Every cell is from the record linked in its row unless the cell links another, as quoted on 2026-11-12; "not stated" means not stated in the record. Policy pages change without notice.

| Platform | Public posting without audit or review? | Daily or rate limit | AI disclosure rule | Monetisation rule on AI or mass-produced content | Price of posting |
|---|---|---|---|---|---|
| YouTube ([YT revisions], [YT insert]) | Yes since 2026-11-02; default privacy is public | "100 videos.insert calls" per day per project | Disclose realistic AI content ([YT disclosure]); API flag `status.containsSyntheticMedia` | Not "mass-produced, generic, repetitive, or manipulative" ([YT monetisation]) | No cost stated |
| TikTok ([TT guidelines], [TT direct post]) | No: unaudited posts are private-only | "typically around 15 posts per day/ creator account"; init 6 requests per minute per token | Label realistic AI content ([TT community]); API flag `is_aigc` | Not stated | Not stated |
| Instagram ([IG publishing]) | Not stated; app review for Advanced Access not read | "100 API-published posts within a 24-hour moving period" | `is_ai_generated` on the media container | Not stated | Not stated |
| Facebook Reels ([FB reels]) | Not stated; posts to a Page, not a profile | "30 API-published posts within a 24-hour moving period" | `is_ai_generated`, defaults to false | Primarily unoriginal accounts "may see their account deemed non-recommendable and demonetized" ([Meta originality]) | Not stated |
| Threads ([Threads posts]) | Not stated; app review not read | "250 published posts within a 24-hour period" | `is_made_with_ai`; false "does not prevent automatic AI labeling" | Not stated | Not stated |
| X ([X pricing], [X automation]) | Not stated; automated posts allowed "for entertainment, informational, or novelty purposes" | Not stated | No label required or offered ([X authenticity]) | No monetisation rule; "duplicative or substantially similar posts" banned | "$0.015 per request", "$0.200" with a URL |
| LinkedIn ([LinkedIn share]) | Own profile: add the self-serve Share on LinkedIn product | No daily limit found | Not stated | Not stated | Not stated |
| Bluesky ([Bluesky video]) | No audit mentioned; verified email needed | A daily video-post limit exists; number not on the page | Not stated | Not stated | Not stated |
| Mastodon ([Mastodon posting]) | No app review; own-account token | Rate limits not read | Not stated | Not stated | Not stated |

## The TikTok dead end

TikTok's guidelines say: "all content uploaded via this endpoint will be restricted to private viewing mode. To lift this restriction, your API client must undergo an audit" ([TT guidelines]). The audit's intended-use list then rejects the one-developer case: "Not acceptable: A utility tool to help upload contents to the account(s) you or your team manages." ([TT guidelines]). An unaudited client is also blocked unless the account itself is private ([TT direct post]). Posts can be made public later by hand in the app ([TT guidelines]).

## What changed on YouTube on 2026-11-02

The revision history says: "Videos uploaded through the videos.insert method from unverified API projects are no longer restricted to private viewing mode." ([YT revisions]). It adds: "If you don't specify a value for the status.privacyStatus property in a videos.insert request, the uploaded video's privacy status defaults to public." ([YT revisions]). A test upload therefore needs `status.privacyStatus` set explicitly.

## Contradictions inside a platform's docs

- Instagram: the guide quotes 100 API posts per 24 hours in its rate-limit section, and the record notes 50 published posts per 24 hours in the carousel section; the record advises planning for 50 ([IG publishing]).
- LinkedIn: the Videos API gives "Between 75kb and 500MB", and the record notes the same page also states 5 GB ([LinkedIn share]).
- YouTube: the July 28, 2020 private-only rule is still on the same revision page; the 2026-11-02 entry reverses it ([YT revisions]).

## C2PA and labels

A C2PA manifest is "digitally signed by a trusted implementation" ([C2PA]). YouTube says content "containing C2PA metadata" gets a label the creator "can not" adjust ([YT disclosure]). YouTube is the only platform record found that states it reads C2PA ([C2PA]). On Threads, leaving `is_made_with_ai` false does not prevent automatic AI labelling ([Threads posts]).

## Self-hosted schedulers and their limits

- [Postiz]: self-hosting means "You create your own developer apps on each platform and go through their approval"; the self-hosted edition is AGPL-3.0. A self-hosted TikTok app hits the same audit wall ([TT guidelines]).
- [Mixpost]: Lite publishes to Facebook Pages, Mastodon and X; other platforms need Pro, "$299" one-time, as quoted on 2026-11-12.

## Pages the hub could not read

- TikTok's support page on AI labels: rendered empty ([TT community]).
- Meta's AI-labelling pages: did not render ([C2PA]).
- Meta's help-centre page on original content: not opened ([Meta originality]).
- X's synthetic-manipulated-media-policy URL: returned 404 ([X authenticity]).
- Instagram Advanced Access app review, Threads app review, Facebook Reels permissions ([IG publishing], [Threads posts], [FB reels]).
- X codec and resolution rules ([X upload]); TikTok's separate rate-limit page ([TT direct post]).
- The C2PA specification itself ([C2PA]).

[YT revisions]: ../../catalog/source/developers.google.com__youtube__v3__revision_history.md
[YT insert]: ../../catalog/source/developers.google.com__youtube__v3__docs__videos__insert.md
[YT disclosure]: ../../catalog/source/support.google.com__youtube__answer__14328491.md
[YT monetisation]: ../../catalog/source/support.google.com__youtube__answer__1311392.md
[TT guidelines]: ../../catalog/source/developers.tiktok.com__doc__content-sharing-guidelines.md
[TT direct post]: ../../catalog/source/developers.tiktok.com__doc__content-posting-api-reference-direct-post.md
[TT community]: ../../catalog/source/www.tiktok.com__community-guidelines__en__integrity-authenticity.md
[IG publishing]: ../../catalog/source/developers.facebook.com__docs__instagram-platform__content-publishing.md
[FB reels]: ../../catalog/source/developers.facebook.com__docs__video-api__guides__reels-publishing.md
[Meta originality]: ../../catalog/source/about.fb.com__news__2026__03__rewarding-original-creators-on-facebook.md
[Threads posts]: ../../catalog/source/developers.facebook.com__docs__threads__posts.md
[X pricing]: ../../catalog/source/docs.x.com__x-api__getting-started__pricing.md
[X upload]: ../../catalog/source/docs.x.com__x-api__media__quickstart__media-upload-chunked.md
[X automation]: ../../catalog/source/help.x.com__en__rules-and-policies__x-automation.md
[X authenticity]: ../../catalog/source/help.x.com__en__rules-and-policies__authenticity.md
[LinkedIn share]: ../../catalog/source/learn.microsoft.com__en-us__linkedin__consumer__integrations__self-serve__share-on-linkedin.md
[Bluesky video]: ../../catalog/source/docs.bsky.app__docs__tutorials__video.md
[Mastodon posting]: ../../catalog/source/docs.joinmastodon.org__user__posting.md
[C2PA]: ../../catalog/source/c2pa.org__faqs.md
[Postiz]: ../../catalog/tool/gitroomhq__postiz-app.md
[Mixpost]: ../../catalog/tool/inovector__mixpost.md

## Not covered yet

- No record for Pinterest, Snapchat, Vimeo or Reddit: searched, nothing found.
- Monetisation rules for TikTok, Instagram, Threads, LinkedIn, Bluesky and Mastodon.
- AI disclosure rules for LinkedIn, Bluesky and Mastodon.
- Bluesky's daily video number and Mastodon's rate limits.
- A hosted scheduler with an audited TikTok app.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
