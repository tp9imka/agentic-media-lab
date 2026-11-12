# Windmill

`tool:windmill-labs/windmill` - tool - <https://github.com/windmill-labs/windmill>

A self-hostable engine for scripts, flows and schedules, with approval steps that suspend a flow until a person resumes it.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Review loop](../../docs/glossary.md#review-loop), [Licences and territory](../../docs/glossary.md#licences-and-territory)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its suspend-until-approval step is a run-time human gate in the free edition, which fits a 'render, then wait for my OK, then publish' flow.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | orchestration, review-loop |
| cost | mixed |

Licence gotcha: the Community Edition is free to use internally but may not be sold, resold or run as a managed service without an agreement; the source build is AGPLv3. Approval works through secret resume URLs, so anyone who gets the URL can approve; send it only to the approver. Telemetry default and schedule docs were not read.

## Claims

1. The Community Edition may be used free and redistributed as is, but not sold, served as a managed service or wrapped without an agreement.

   > but not to sell, resell, serve as a managed service, modify or wrap under any form without an explicit agreement.

   Locator: LICENSE, Community Edition paragraph. Source: <https://github.com/windmill-labs/windmill/blob/main/LICENSE>, retrieved 2026-11-12.

2. An approval step suspends the flow until it is approved through resume endpoints or the approval page, only by holders of the secret URLs.

   > This will suspend the execution of a flow until it has been approved through the resume endpoints or the approval page by and solely by the recipients of the secret URLs.

   Locator: docs/flows/11_flow_approval.mdx, Suspend & Approval / Prompts. Source: <https://github.com/windmill-labs/windmilldocs-public/blob/main/docs/flows/11_flow_approval.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. LICENSE from the main repo and flow approval doc from windmilldocs-public against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `366b8be6bd6e5ba6489f275e7f8d2ee3d199aaf07f4755e6796d2abd7b4ebf61`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-05-05
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1151
- installs: 1105
- installs_by_skill: {"adding-a-trigger": 6, "ai-chat": 5, "ai-evals": 5, "commit": 91, "local-review": 15, "native-trigger": 7, "pr": 85, "refine": 37, "rust-backend": 1105, "svelte-frontend": 101}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 876
- registry: skills.sh
- sources: https://api.github.com/repos/windmill-labs/windmill, https://skills.sh/api/search?q=windmill
- stars: 18545

## Related

- alternative_to: [n8n](n8n-io__n8n.md)
- alternative_to: [Trigger.dev](triggerdotdev__trigger.dev.md)

## Referenced by

- [n8n](n8n-io__n8n.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
