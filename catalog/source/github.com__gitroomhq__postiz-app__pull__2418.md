# Postiz PR 2418: TikTok inbox uploads marked published that never arrive

`source:github.com/gitroomhq/postiz-app/pull/2418` - source - <https://github.com/gitroomhq/postiz-app/pull/2418>

A merged Postiz pull request (2026-11-12) that adds logging after a customer reported TikTok inbox uploads that TikTok acknowledged but that never appeared. Postiz marks an inbox upload published as soon as TikTok answers SEND_TO_USER_INBOX and does not track it afterwards.

Concepts: [Publishing](../../docs/glossary.md#publishing), [Platform rules](../../docs/glossary.md#platform-rules), [Automation](../../docs/glossary.md#automation)

Tags: tiktok, postiz

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** A scheduler's 'published' status for a TikTok inbox upload is not proof the video reached the inbox, so an unattended pipeline can report success for a post that does not exist.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

The PR only adds a log line; it does not change the post state, so Postiz still shows such posts as published. For an agent pipeline, poll TikTok's post status for the publish id later, or check the inbox, before counting a TikTok upload as delivered. The cause of the missing items is not known in the PR. One customer report, relayed by a maintainer.

## Claims

1. The pull request was merged on 2026-11-12.

   > Merged: 2026-11-12T06:23:51Z

   Locator: GitHub API pulls/2418, merged_at field (saved header). Source: <https://github.com/gitroomhq/postiz-app/pull/2418>, retrieved 2026-11-12.

2. Postiz marks an inbox upload published when TikTok answers SEND_TO_USER_INBOX and keeps no record of TikTok's later status.

   > Inbox uploads are marked published when TikTok answers `SEND_TO_USER_INBOX`, and Postiz keeps no record of what TikTok reports about the item afterwards.

   Locator: PR body, Why was this change needed?, sentence 1. Source: <https://github.com/gitroomhq/postiz-app/pull/2418>, retrieved 2026-11-12.

3. A customer reports acknowledged uploads that regularly never show up, clustered at one time of day across several accounts.

   > A customer reports that uploads TikTok acknowledged within a minute regularly never show up in the TikTok inbox, concentrated at one time of day across several accounts.

   Locator: PR body, Why was this change needed?, sentence 2. Source: <https://github.com/gitroomhq/postiz-app/pull/2418>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. PR body and merge state from the GitHub API against the record
- Next check due: 2027-02-10
- Licence: AGPL-3.0
- URL status: live
- Saved source sha256: `5d572ce318cac566b35de928eea6b062c826d32b8e9d72ac98108907a2058f64`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2023-07-08
- default_branch: main
- fetched_at: 2026-11-12
- forks: 7904
- last_activity: 2026-11-12
- licence: AGPL-3.0
- open_issues: 209
- sources: https://api.github.com/repos/gitroomhq/postiz-app, https://skills.sh/api/search?q=postiz-app
- stars: 41429

## Related

- evaluated_on: [Postiz](../tool/gitroomhq__postiz-app.md)
- extends: [TikTok Content Sharing Guidelines (Direct Post API)](developers.tiktok.com__doc__content-sharing-guidelines.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
