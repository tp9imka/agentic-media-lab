# Claude Code cloud scheduled tasks (formerly routines)

`source:code.claude.com/docs/en/routines` - source - <https://code.claude.com/docs/en/routines>

Anthropic's docs for saved Claude Code tasks that run in its cloud on a schedule, an API call or a GitHub event, against a fresh clone of your repos.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Review loop](../../docs/glossary.md#review-loop)

Also known as: claude code routines, cloud scheduled tasks

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The only option in this lane that keeps firing with the laptop shut and needs no server of your own, at the cost of no local files.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Minimum interval 1 hour; runs exactly on the hour may start several minutes late. Bare cron hours are UTC. Environment variables are visible to anyone using the environment, so the docs say to store API keys as network secrets. Runs push to claude/ branches; use branch protection to gate merges. A fresh cloud clone cannot see local footage or a local GPU.

## Claims

1. Cloud tasks run on Anthropic's infrastructure, so they keep working when your laptop is closed.

   > so they keep working when your laptop is closed.

   Locator: section intro. Source: <https://code.claude.com/docs/en/routines>, retrieved 2026-11-12.

2. Custom cron intervals are allowed but anything more often than hourly is rejected.

   > Expressions that run more often than once per hour are rejected.

   Locator: section Add a schedule trigger, Custom intervals. Source: <https://code.claude.com/docs/en/routines>, retrieved 2026-11-12.

3. A run starts in auto mode, where a classifier allows or blocks actions; it waits for you only on ask rules or repeated blocks.

   > When a run starts a new session on Anthropic's cloud, that session begins in [auto mode](https://code.claude.com/docs/en/permission-modes.md#eliminate-prompts-with-auto-mode) unless auto mode is unavailable.

   Locator: section Permission prompts during a run. Source: <https://code.claude.com/docs/en/routines>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. routines.md (markdown version) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `771d695d4bb11166b6d6905f4f8148d31d0806a17e6194e3efffc402559f631f`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- alternative_to: [Claude Code: run prompts on a schedule (/loop) and compare scheduling options](code.claude.com__docs__en__scheduled-tasks.md)
- alternative_to: [Run Claude Code programmatically (claude -p)](code.claude.com__docs__en__headless.md)

## Referenced by

- [Run Claude Code programmatically (claude -p)](code.claude.com__docs__en__headless.md) (alternative_to)
- [Claude Code: run prompts on a schedule (/loop) and compare scheduling options](code.claude.com__docs__en__scheduled-tasks.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
