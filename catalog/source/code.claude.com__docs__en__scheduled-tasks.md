# Claude Code: run prompts on a schedule (/loop) and compare scheduling options

`source:code.claude.com/docs/en/scheduled-tasks` - source - <https://code.claude.com/docs/en/scheduled-tasks>

Anthropic's page for session-scoped /loop tasks, with a table comparing cloud, Desktop and /loop scheduling.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: /loop, claude code desktop scheduled tasks

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The comparison table answers where each Claude Code schedule runs and what must stay on, in one place.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

/loop is for polling inside an open session, not for a nightly job. Desktop tasks need the app open and the machine awake. For durable local runs, use Desktop tasks or claude -p from cron.

## Claims

1. Cloud tasks need neither machine nor session; Desktop needs the machine on; /loop needs an open session.

   > | Requires machine on | No | Yes | Yes | | Requires open session | No | No | Yes |

   Locator: section Compare scheduling options, table. Source: <https://code.claude.com/docs/en/scheduled-tasks>, retrieved 2026-11-12.

2. Recurring /loop tasks delete themselves 7 days after creation.

   > Recurring tasks automatically expire 7 days after creation.

   Locator: section Seven-day expiry. Source: <https://code.claude.com/docs/en/scheduled-tasks>, retrieved 2026-11-12.

3. Missed fires are not caught up; a busy session fires once when idle.

   > No catch-up for missed fires.

   Locator: section Limitations. Source: <https://code.claude.com/docs/en/scheduled-tasks>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. scheduled-tasks.md (markdown version) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `ef9be1d49e12d3b25196cdf892b6982290677ac4ee86ae43393c7dd5803379ca`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- alternative_to: [Claude Code cloud scheduled tasks (formerly routines)](code.claude.com__docs__en__routines.md)

## Referenced by

- [Claude Code cloud scheduled tasks (formerly routines)](code.claude.com__docs__en__routines.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
