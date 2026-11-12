# Temporal

`tool:temporalio/temporal` - tool - <https://github.com/temporalio/temporal>

A durable-execution server; Schedules start workflow executions on calendar or interval specs, with overlap and catch-up policies.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The heaviest option here, but the one with explicit, documented rules for overlapping and late runs.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | runtime |
| agents | none-stated |
| levers | orchestration |
| cost | free-local |

Needs a Temporal server plus your own workers, which is a lot for one developer making clips. There is no approval primitive in the schedule doc; a human step means writing a signal handler. The default one-year catch-up window means a server down for a week fires the backlog per the overlap policy when it returns. Licence was not quoted and telemetry was not checked.

## Claims

1. By default a scheduled start is skipped when the previous execution is still running.

   > - `Skip`: **Default**. Nothing happens; the Workflow Execution is not started.

   Locator: docs/encyclopedia/workflow/schedule.mdx, Overlap Policy. Source: <https://docs.temporal.io/schedule>, retrieved 2026-11-12.

2. The default catch-up window is one year, so late actions still run unless over a year late.

   > The default is one year, meaning Actions will be taken unless over one year late.

   Locator: docs/encyclopedia/workflow/schedule.mdx, Catchup Window. Source: <https://docs.temporal.io/schedule>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `14a7c7a69742023463deb3e0422a32f1c258e38a52d81e9f9d6de5513d4d1e93`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2019-10-16
- default_branch: main
- fetched_at: 2026-11-12
- forks: 2114
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 1138
- sources: https://api.github.com/repos/temporalio/temporal, https://skills.sh/api/search?q=temporal
- stars: 24350

## Related

- alternative_to: [Trigger.dev](triggerdotdev__trigger.dev.md)

## Referenced by

- [Trigger.dev](triggerdotdev__trigger.dev.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
