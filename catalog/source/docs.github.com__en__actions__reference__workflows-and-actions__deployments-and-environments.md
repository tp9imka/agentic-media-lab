# GitHub Actions: deployments and environments (required reviewers)

`source:docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments` - source - <https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments>

GitHub's reference for environments: required reviewers, wait timers, branch rules and environment secrets.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Review loop](../../docs/glossary.md#review-loop)

Also known as: required reviewers, github environments

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Required reviewers are the built-in way to make a scheduled workflow stop and wait for a person before a publish or upload step.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Plan gotcha: on Free, Pro and Team, required reviewers only work in public repositories, so a private repo on a personal plan gets no approval gate. Put the API key for the publish step in an environment secret so it unlocks only after approval.

## Claims

1. Required reviewers make jobs that reference an environment wait for one of up to six people or teams to approve.

   > Only one of the required reviewers needs to approve the job for it to proceed.

   Locator: section Required reviewers. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments>, retrieved 2026-11-12.

2. On Free, Pro and Team plans, required reviewers are only available for public repositories.

   > If you are on a GitHub Free, GitHub Pro, or GitHub Team plan, required reviewers are only available for public repositories.

   Locator: section Required reviewers, note. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments>, retrieved 2026-11-12.

3. Environment secrets stay locked until a required reviewer approves the job.

   > If the environment requires approval, a job cannot access environment secrets until one of the required reviewers approves it.

   Locator: section Environment secrets. Source: <https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. docs.github.com article body (markdown) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `7e78f7788c30a3b47db1a5c44b9451dccbe951c15255312add99646b27cd6bd7`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- integrates_with: [GitHub Actions: events that trigger workflows (schedule)](docs.github.com__en__actions__reference__workflows-and-actions__events-that-trigger-workflows.md)

## Referenced by

- [GitHub Actions: events that trigger workflows (schedule)](docs.github.com__en__actions__reference__workflows-and-actions__events-that-trigger-workflows.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
