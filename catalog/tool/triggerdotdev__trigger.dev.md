# Trigger.dev

`tool:triggerdotdev/trigger.dev` - tool - <https://github.com/triggerdotdev/trigger.dev>

A TypeScript background-job platform, hosted or self-hosted, with cron-scheduled tasks and waitpoint tokens that pause a run until completed.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Review loop](../../docs/glossary.md#review-loop)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Waitpoint tokens give code-first approval: a render task waits for an 'approved' or 'rejected' payload before it publishes.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | orchestration, review-loop |
| cost | mixed |

Self-hosting lacks checkpoints, so a waiting run holds its resources instead of sleeping; long approval waits cost more there. Declarative schedules apply only after a dev or deploy command. Telemetry default of the self-hosted build was not checked.

## Claims

1. Waitpoint tokens pause a run until completed and are meant for approval and human-in-the-loop steps.

   > Waitpoint tokens pause task runs until you complete the token. They're commonly used for approval workflows

   Locator: docs/wait-for-token.mdx, intro. Source: <https://github.com/triggerdotdev/trigger.dev/blob/main/docs/wait-for-token.mdx>, retrieved 2026-11-12.

2. Declarative schedules live on the task and sync when you run the dev command or deploy.

   > They sync when you run the dev command or deploy.

   Locator: docs/tasks/scheduled.mdx, Attaching schedules. Source: <https://github.com/triggerdotdev/trigger.dev/blob/main/docs/tasks/scheduled.mdx>, retrieved 2026-11-12.

3. Checkpoints (non-blocking waits) are Cloud-only; self-hosted runs do not get them.

   > | Checkpoints | ✅ | ❌ | Non-blocking waits, less resource usage |

   Locator: docs/self-hosting/overview.mdx, feature table. Source: <https://github.com/triggerdotdev/trigger.dev/blob/main/docs/self-hosting/overview.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. three docs files from the repo against the claims
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `5a560e63d9a00697673093fa4e3e01bf508bca80e0b8194fb3f0e5dd29b90863`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-11-30
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1531
- installs: 233
- installs_by_skill: {"errors-api-e2e": 12, "span-timeline-events": 21, "trigger-authoring-chat-agent": 2, "trigger-authoring-tasks": 2, "trigger-chat-agent-advanced": 2, "trigger-cost-savings": 1, "trigger-dev-tasks": 233, "trigger-getting-started": 1, "trigger-realtime-and-frontend": 2}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 265
- registry: skills.sh
- sources: https://api.github.com/repos/triggerdotdev/trigger.dev, https://skills.sh/api/search?q=trigger.dev
- stars: 16749

## Related

- alternative_to: [Temporal](temporalio__temporal.md)

## Referenced by

- [Temporal](temporalio__temporal.md) (alternative_to)
- [Windmill](windmill-labs__windmill.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
