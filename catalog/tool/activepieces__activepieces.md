# Activepieces

`tool:activepieces/activepieces` - tool - <https://github.com/activepieces/activepieces>

A self-hostable no-code automation builder, MIT-licensed outside its enterprise folders.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Licences and territory](../../docs/glossary.md#licences-and-territory)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A permissive alternative to n8n, but its documented approval feature gates publishing a flow, not a step inside a run.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | service |
| agents | none-stated |
| levers | orchestration |
| cost | mixed |

Flow Approvals is an Enterprise or Cloud feature and reviews flow changes before they go live; it is not a run-time human step. Product analytics and a daily deployment snapshot are on until switched off. Run-time approval pieces and schedule triggers were not read.

## Claims

1. Code outside the enterprise directories is MIT (Expat) licensed.

   > Content outside of the above mentioned directories or restrictions above is available under the "MIT Expat" license as defined below.

   Locator: LICENSE, third bullet. Source: <https://github.com/activepieces/activepieces/blob/main/LICENSE>, retrieved 2026-11-12.

2. Flow Approvals is an Enterprise or Cloud feature that holds a flow offline until an approver reviews it.

   > Flow Approvals is an Enterprise / Cloud feature and requires the Environments plan.

   Locator: docs/flows/flow-approvals.mdx, info box. Source: <https://github.com/activepieces/activepieces/blob/main/docs/flows/flow-approvals.mdx>, retrieved 2026-11-12.

3. The daily deployment snapshot is on by default and ignores AP_TELEMETRY_ENABLED.

   > **Deployment setup** is a separate switch in the same place, and is on by default.

   Locator: docs/install/configure-operate/telemetry.mdx, Opting out?. Source: <https://github.com/activepieces/activepieces/blob/main/docs/install/configure-operate/telemetry.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. LICENSE, flow-approvals.mdx and telemetry.mdx from the repo against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `6f5eb5885f2a6401c991ec817766c2f93c67ec4e9ba512517fe03637973b7993`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-12-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 4460
- installs: 72
- installs_by_skill: {"activepieces-design-system": 10, "add-endpoint": 7, "add-entity": 5, "add-feature": 6, "agent-browser": 8, "db-migration": 5, "grill-me": 72, "mintlify": 8, "piece-builder": 14, "playwright-e2e-testing": 14}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 927
- registry: skills.sh
- sources: https://api.github.com/repos/activepieces/activepieces, https://skills.sh/api/search?q=activepieces
- stars: 25490
- Popularity: installs and stars differ by more than 100x

## Related

- alternative_to: [n8n](n8n-io__n8n.md)

## Referenced by

- [n8n](n8n-io__n8n.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
