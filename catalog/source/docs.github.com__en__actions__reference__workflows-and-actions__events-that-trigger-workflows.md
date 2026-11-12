# GitHub Actions: events that trigger workflows (schedule)

`source:docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows` - source - <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>

GitHub's reference for workflow triggers; the schedule section covers cron syntax, timezone, minimum interval and the delay, drop and disable rules.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: on: schedule, github actions cron

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A free scheduler for claude -p or codex exec that needs no machine of yours, with documented ways it fails to fire.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Avoid minute 0. Scheduled runs use the default branch only. The 60-day disable applies to public repositories. Secrets go in repository or environment secrets; see the environments source for an approval gate. Runner minutes on private repos are billed per plan, not checked here.

## Claims

1. A schedule is POSIX cron in the workflow file, UTC by default, with an optional IANA timezone and a 5-minute minimum.

   > The shortest interval you can run scheduled workflows is once every 5 minutes.

   Locator: section schedule. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>, retrieved 2026-11-12.

2. Scheduled runs can be delayed at high load, especially at the top of the hour, and some queued jobs may be dropped.

   > If the load is sufficiently high enough, some queued jobs may be dropped.

   Locator: section schedule, note. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>, retrieved 2026-11-12.

3. In a public repository, scheduled workflows are disabled after 60 days without repository activity.

   > In a public repository, scheduled workflows are automatically disabled when no repository activity has occurred in 60 days.

   Locator: section schedule, note. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. docs.github.com article body (markdown) for the schedule section against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `5a5687c7eda6b1bb4766c8c0121d1823ebafd6083227f93da757e29f1a9be754`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- integrates_with: [GitHub Actions: deployments and environments (required reviewers)](docs.github.com__en__actions__reference__workflows-and-actions__deployments-and-environments.md)
- integrates_with: [Run Claude Code programmatically (claude -p)](code.claude.com__docs__en__headless.md)

## Referenced by

- [Run Claude Code programmatically (claude -p)](code.claude.com__docs__en__headless.md) (integrates_with)
- [GitHub Actions: deployments and environments (required reviewers)](docs.github.com__en__actions__reference__workflows-and-actions__deployments-and-environments.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
