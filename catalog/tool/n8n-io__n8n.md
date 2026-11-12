# n8n

`tool:n8n-io/n8n` - tool - <https://github.com/n8n-io/n8n>

A self-hostable visual workflow engine with schedule triggers, AI agent nodes and a human review step for agent tool calls.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Review loop](../../docs/glossary.md#review-loop), [Licences and territory](../../docs/glossary.md#licences-and-territory)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Self-hosted n8n gives a single developer a scheduler plus a Slack or Telegram approval before an agent tool runs, for example before a publish.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | orchestration, review-loop, publishing |
| cost | mixed |

Licence gotcha: the Sustainable Use License allows internal business, non-commercial or personal use, so selling n8n as a hosted service to clients is out; files with .ee. need an enterprise licence. Self-hosted telemetry is on until N8N_DIAGNOSTICS_ENABLED=false. Needs Docker or Node and a machine that stays on. It does not run Claude Code itself; call claude -p from an Execute Command node or use its own AI nodes. Schedule trigger docs were not read.

## Claims

1. Its Sustainable Use License limits use to internal business, non-commercial or personal purposes.

   > You may use or modify the software only for your own internal business purposes or for non-commercial or personal use.

   Locator: LICENSE.md, Sustainable Use License, Limitations. Source: <https://github.com/n8n-io/n8n/blob/master/LICENSE.md>, retrieved 2026-11-12.

2. A tool that needs human review pauses the workflow and sends an approval request through a channel such as Slack or Telegram.

   > The workflow pauses and sends an approval request through your configured channel (such as Slack, Telegram, or the n8n Chat interface).

   Locator: docs human-in-the-loop-for-tools, How it works, step 2. Source: <https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools>, retrieved 2026-11-12.

3. Self-hosted n8n collects telemetry by default.

   > n8n enables telemetry collection by default.

   Locator: docs control-telemetry, Opting out of data collection. Source: <https://docs.n8n.io/deploy/host-n8n/configure-n8n/security/control-telemetry>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. LICENSE.md from the repo and two n8n-docs pages (repo markdown) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `ae9396cacc783414daaf42dab90aaa61648de8d19b1c0b08ecebf44d9835cec5`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2019-06-22
- default_branch: master
- fetched_at: 2026-11-12
- forks: 61481
- installs: 847
- installs_by_skill: {"content-design": 473, "create-pr": 847, "linear-issue": 305, "loom-transcript": 301, "n8n-conventions": 433, "n8n:content-design": 288, "n8n:conventions": 342, "n8n:create-pr": 293, "n8n:spec-driven-development": 289, "reproduce-bug": 306}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 1232
- registry: skills.sh
- sources: https://api.github.com/repos/n8n-io/n8n, https://skills.sh/api/search?q=n8n
- stars: 210255
- Popularity: installs and stars differ by more than 100x

## Related

- alternative_to: [Windmill](windmill-labs__windmill.md)
- alternative_to: [Activepieces](activepieces__activepieces.md)

## Referenced by

- [Activepieces](activepieces__activepieces.md) (alternative_to)
- [Windmill](windmill-labs__windmill.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
