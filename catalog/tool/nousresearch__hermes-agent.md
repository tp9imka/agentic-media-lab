# Hermes Agent

`tool:nousresearch/hermes-agent` - tool - <https://github.com/NousResearch/hermes-agent>

Nous Research's self-hosted agent with its own model routing, skills, messaging gateways and a cron scheduler that runs agent or script jobs.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Review loop](../../docs/glossary.md#review-loop)

Also known as: hermes, hermes cron

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is a full agent, not a wrapper for Claude Code, and its cron plus chat approvals is the most complete unattended loop with a human answer step found in this lane.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | runtime |
| agents | hermes |
| levers | orchestration, review-loop |
| cost | mixed |

Needs a model provider key or the Nous Portal; it does not drive your Claude Code subscription. Jobs live in ~/.hermes/cron/jobs.json and secrets in ~/.hermes/.env. Dangerous commands in cron are denied by default (see the security source). The plugin catalog lists third-party plugins, including one that opens an unauthenticated local dashboard; read a plugin before enabling it. Telemetry default not found in README or the pages read.

## Claims

1. The scheduler runs inside the gateway daemon, which ticks every 60 seconds; the gateway can be installed as a user or system service.

   > **Cron execution is handled by the gateway daemon.** The gateway ticks the scheduler every 60 seconds, running any due jobs in isolated agent sessions.

   Locator: section How it works. Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>, retrieved 2026-11-12.

2. A missed cron occurrence runs late only inside a catch-up window of half the period, clamped to 2 minutes - 2 hours, settable per job.

   > A missed cron occurrence is run late only inside a catch-up window: half the job's period, clamped to 2 minutes–2 hours.

   Locator: section Catch-up window. Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>, retrieved 2026-11-12.

3. A job can be created paused with a reason and resumed by a person, which serves as a review gate before the first fire.

   > Omit the reason to store "Created paused; awaiting operator approval."

   Locator: section Creating a job paused (safe canary). Source: <https://hermes-agent.nousresearch.com/docs/user-guide/features/cron>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. website/docs/user-guide/features/cron.md (source of the docs page) against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `7b51974af933fe3f6f0a953c00d0871e0c46d3b9f5b26774baac075ae1e3c5fb`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-07-22
- default_branch: main
- fetched_at: 2026-11-12
- forks: 59112
- installs: 6434
- installs_by_skill: {"arxiv": 732, "claude-design": 684, "dogfood": 6434, "google-workspace": 610, "hermes-agent": 1269, "humanizer": 1322, "llm-wiki": 622, "popular-web-designs": 974, "powerpoint": 757, "songwriting-and-ai-music": 631}
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 53985
- registry: skills.sh
- sources: https://api.github.com/repos/NousResearch/hermes-agent, https://skills.sh/api/search?q=hermes-agent
- stars: 262822

## Related

- depends_on: [Hermes Agent security: dangerous command approval](../source/hermes-agent.nousresearch.com__docs__user-guide__security.md)
- alternative_to: [bb](get-bb__bb.md)

## Referenced by

- [Hermes Agent security: dangerous command approval](../source/hermes-agent.nousresearch.com__docs__user-guide__security.md) (extends)
- [bb](get-bb__bb.md) (alternative_to)
- [Kanban Video Pipeline](nousresearch__kanban-video-pipeline.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
