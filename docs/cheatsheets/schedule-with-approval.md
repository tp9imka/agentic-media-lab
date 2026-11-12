---
id: guide:schedule-with-approval
title: Run it on a schedule with an approval step
summary: Where a scheduled Claude Code or Codex run can live, what must stay on, and where a person can approve before publish, from the records, read, not run.
use_when: "Use this page when you want an agent pipeline to run on a timer and stop for a human approval before it publishes."
concepts: [concept:scheduling-and-runtimes, concept:automation, concept:orchestration, concept:review-loop]
last_reviewed: 2026-11-12
---

# Run it on a schedule with an approval step

A comparison of where the schedule can live, for a developer whose agent is Claude Code or Codex. All of it is read, not run: the hub has run no schedule. Read the two tables, then the pipeline outline. Each row's cells come from the record linked in its first column unless a cell links another. Empty cells say "not stated in the record". The [bb card](../cards/bb.md) covers bb in depth. Limits are as quoted on 2026-11-12.

## Agent-side schedulers

| Where | How declared | Must stay on | Where a human approves | Licence or plan limit | Telemetry default |
|---|---|---|---|---|---|
| [bb] | `--cron`, `--timezone`, `--at`, `--in` | The bb server machine, awake ([bb devices]) | None of its own; omitted mode => `auto`, else Full Access | MIT, collected | On in production runs; `BB_TELEMETRY=false` |
| [Hermes Agent] | Jobs in `~/.hermes/cron/jobs.json`; gateway ticks every 60 s | The gateway daemon | Job created paused "awaiting operator approval"; cron denies dangerous commands by default ([Hermes security]) | MIT, collected; agent jobs need a model provider key | Not found in the pages read |
| Claude Code [/loop][CC scheduled tasks] | `/loop` inside a session | An open session | Not stated in the record | Recurring tasks expire 7 days after creation | Not stated in the record |
| Claude Code Desktop tasks ([CC scheduled tasks]) | Not stated in the record | Machine on, app open | Not stated in the record | Not stated in the record | Not stated in the record |
| Claude Code [cloud tasks][CC routines] (formerly routines) | Schedule trigger; bare cron hours are UTC | Nothing: runs "keep working when your laptop is closed" | Starts in auto mode; waits only on ask rules or repeated blocks; runs push to `claude/` branches | More often than hourly is rejected | Not stated in the record |
| [claude -p] from cron, launchd or CI | No scheduler of its own | Not stated in the record | From v2.1.302 starts in Manual mode; a call needing approval is denied unless a hook or prompt tool approves | Not stated in the record | Metrics on with an Anthropic sign-in; `DISABLE_TELEMETRY=1` |
| [Codex scheduled tasks] | From the ChatGPT app, not the CLI | Computer on, app running, for local files | After the run, in the Scheduled inbox; no pre-step approval described | Not stated in the record | Not stated in the record |
| [codex exec] | No scheduler of its own | Not stated in the record | Read-only sandbox by default | Not stated in the record | OpenTelemetry export off by default |

## CI and self-hosted engines

| Where | How declared | Must stay on | Where a human approves | Licence or plan limit | Telemetry default |
|---|---|---|---|---|---|
| [GitHub Actions schedule] | POSIX cron in the workflow file, UTC by default, optional IANA timezone | No machine of yours | Required reviewers on an environment ([GitHub environments]) | 5-minute minimum; reviewers need a public repo on Free, Pro and Team | Not stated in the record |
| [n8n] | Schedule triggers (docs not read) | Docker or Node on a machine that stays on | Workflow pauses and sends a request via Slack, Telegram or n8n Chat | Sustainable Use License | On; `N8N_DIAGNOSTICS_ENABLED=false` |
| [Windmill] | Not stated in the record | Not stated in the record | Approval step suspends the flow; holders of secret URLs approve | Community Edition not for resale or managed service | Not read |
| [Trigger.dev] | Declarative schedules on the task, synced on dev or deploy | Self-hosted: a waiting run holds its resources | Waitpoint tokens | Apache-2.0, collected; checkpoints are Cloud-only | Not checked |
| [Temporal] | Calendar or interval specs | Temporal server plus your workers | No approval primitive; write a signal handler | MIT, collected; not quoted | Not checked |
| [Activepieces] | Not read | Not stated in the record | Flow Approvals reviews flow changes, not a run step | Flow Approvals is Enterprise or Cloud | Product analytics and a daily snapshot on |

## A pipeline with a gate before publish

1. The schedule fires: [bb], [Hermes Agent], [cloud tasks][CC routines] or the [GitHub Actions schedule].
2. The agent writes and renders the clip: [claude -p] or [codex exec]. The renderer is your choice; the [worked example](../../examples/hyperframes-vs-remotion/README.md) was run here once.
3. Measure the file. Your own script; the example's `measure.py` is one model of it.
4. Stop for a person: required reviewers ([GitHub environments]), [n8n], [Windmill], [Trigger.dev] waitpoints, or a paused [Hermes Agent] job.
5. Publish with the platform's official API. Your own script; platform rules are in [publishing rules](publishing-rules.md).
6. Log what was posted. Your own script.

On GitHub, an environment secret stays locked until a required reviewer approves the job ([GitHub environments]), so the publish key can sit behind step 4.

## Limits the records quote

- Claude Code `/loop`: "Recurring tasks automatically expire 7 days after creation." and "No catch-up for missed fires." ([CC scheduled tasks])
- Claude Code cloud tasks: "Expressions that run more often than once per hour are rejected." ([CC routines])
- GitHub Actions: "The shortest interval you can run scheduled workflows is once every 5 minutes." In a public repository a schedule is disabled after 60 days without activity, and "some queued jobs may be dropped" under load ([GitHub Actions schedule]).
- GitHub approval: "If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, required reviewers are only available for public repositories." ([GitHub environments])
- n8n: "You may use or modify the software only for your own internal business purposes or for non-commercial or personal use." ([n8n])
- Windmill Community Edition: "not to sell, resell, serve as a managed service, modify or wrap under any form without an explicit agreement." ([Windmill])
- Hermes Agent: a missed occurrence runs late only inside a catch-up window of half the period, clamped to 2 minutes to 2 hours ([Hermes Agent]).
- Temporal: the default catch-up window is one year ([Temporal]).

[bb]: ../../catalog/tool/get-bb__bb.md
[bb devices]: ../../catalog/source/github.com__get-bb__bb__blob__main__docs__multiple-devices.md.md
[Hermes Agent]: ../../catalog/tool/nousresearch__hermes-agent.md
[Hermes security]: ../../catalog/source/hermes-agent.nousresearch.com__docs__user-guide__security.md
[CC scheduled tasks]: ../../catalog/source/code.claude.com__docs__en__scheduled-tasks.md
[CC routines]: ../../catalog/source/code.claude.com__docs__en__routines.md
[claude -p]: ../../catalog/source/code.claude.com__docs__en__headless.md
[Codex scheduled tasks]: ../../catalog/source/learn.chatgpt.com__docs__automations.md
[codex exec]: ../../catalog/source/learn.chatgpt.com__docs__non-interactive-mode.md
[GitHub Actions schedule]: ../../catalog/source/docs.github.com__en__actions__reference__workflows-and-actions__events-that-trigger-workflows.md
[GitHub environments]: ../../catalog/source/docs.github.com__en__actions__reference__workflows-and-actions__deployments-and-environments.md
[n8n]: ../../catalog/tool/n8n-io__n8n.md
[Windmill]: ../../catalog/tool/windmill-labs__windmill.md
[Trigger.dev]: ../../catalog/tool/triggerdotdev__trigger.dev.md
[Temporal]: ../../catalog/tool/temporalio__temporal.md
[Activepieces]: ../../catalog/tool/activepieces__activepieces.md

## Not covered yet

- Plan or usage limits of Claude Code and Codex scheduled tasks.
- Telemetry defaults of Hermes Agent, Windmill, Trigger.dev self-hosted, Temporal and GitHub Actions.
- Schedule trigger docs of n8n, Windmill and Activepieces.
- Missed-tick behaviour of bb and of Codex scheduled tasks.
- Runner-minute billing on private GitHub repositories.
- Any schedule run by the hub.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
