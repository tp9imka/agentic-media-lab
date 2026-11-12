# Codex non-interactive mode (codex exec)

`source:learn.chatgpt.com/docs/non-interactive-mode` - source - <https://learn.chatgpt.com/docs/non-interactive-mode>

OpenAI's docs for codex exec in scripts and CI: sandbox flags, auth, JSON output. Saved with the Agent approvals and security page for the approval and telemetry defaults.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

Also known as: codex exec, codex non-interactive

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** codex exec is the Codex counterpart of claude -p: what a cron job or CI runner calls when the reader's agent is Codex.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

The old URL developers.openai.com/codex/noninteractive redirects here (2026-11-12). --full-auto is gone; scripts that used it need --sandbox workspace-write or --approve-for-me. codex exec has no scheduler of its own. Telemetry claim covers OTel export only; other analytics were not checked.

## Claims

1. codex exec runs in a read-only sandbox by default; danger-full-access is for isolated runners only.

   > By default, `codex exec` runs in a read-only sandbox.

   Locator: non-interactive-mode.md, section Permissions and safety. Source: <https://learn.chatgpt.com/docs/non-interactive-mode>, retrieved 2026-11-12.

2. Do not put OPENAI_API_KEY or CODEX_API_KEY in a job-level env when the job runs repository code.

   > Do not set `OPENAI_API_KEY` or `CODEX_API_KEY` as a job-level environment variable in workflows that check out or run repository-controlled code.

   Locator: non-interactive-mode.md, section on authentication. Source: <https://learn.chatgpt.com/docs/non-interactive-mode>, retrieved 2026-11-12.

3. OpenTelemetry export is off by default and opt-in.

   > Telemetry is off by default; enable it explicitly in your configuration.

   Locator: agent-approvals-security.md, section Monitoring and telemetry. Source: <https://learn.chatgpt.com/docs/agent-approvals-security>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. non-interactive-mode.md and agent-approvals-security.md (markdown versions) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `f4c5fc6d8af18024737a33c6ccf97fb01e1c60d1372bbe553866ed5a816a7fda`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- alternative_to: [Run Claude Code programmatically (claude -p)](code.claude.com__docs__en__headless.md)
- alternative_to: [Codex scheduled tasks (ChatGPT app)](learn.chatgpt.com__docs__automations.md)

## Referenced by

- [Codex scheduled tasks (ChatGPT app)](learn.chatgpt.com__docs__automations.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
