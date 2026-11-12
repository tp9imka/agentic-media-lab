# Hermes Agent security: dangerous command approval

`source:hermes-agent.nousresearch.com/docs/user-guide/security` - source - <https://hermes-agent.nousresearch.com/docs/user-guide/security>

Hermes Agent's security model: approval modes, per-surface rules for cron and unattended sessions, YOLO mode, deny rules and who may approve in a shared chat.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Review loop](../../docs/glossary.md#review-loop)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It states exactly what a cron job does when it hits a command that needs a person, and how approvals reach you in Slack, Telegram or Discord.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Keep cron_mode at deny and approvals.mode off of any profile that runs cron. The page itself says deny rules are not a sandbox; use a container backend for containment.

## Claims

1. Cron jobs deny dangerous commands by default; approve mode auto-approves everything in cron.

   > `deny` blocks the command (the agent must find another path); `approve` auto-approves everything in cron context.

   Locator: section Approval Modes, table row cron_mode (default deny). Source: <https://hermes-agent.nousresearch.com/docs/user-guide/security>, retrieved 2026-11-12.

2. Turning approvals off for a profile also covers its cron jobs.

   > `approvals.mode: off` covers every chat and cron job of that profile.

   Locator: section YOLO Mode. Source: <https://hermes-agent.nousresearch.com/docs/user-guide/security>, retrieved 2026-11-12.

3. By default any admitted chat member may answer a pending approval; a list of user ids narrows it.

   > `["*"]`: any admitted member.

   Locator: section Approval Modes, table row approvers. Source: <https://hermes-agent.nousresearch.com/docs/user-guide/security>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. website/docs/user-guide/security.md against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `8dee04b89f602a5b48abd1dab7cb4e5eaf2f2bb49510ae64eb6f78c3433c2cda`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- extends: [Hermes Agent](../tool/nousresearch__hermes-agent.md)

## Referenced by

- [Hermes Agent](../tool/nousresearch__hermes-agent.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
