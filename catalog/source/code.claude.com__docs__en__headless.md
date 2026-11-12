# Run Claude Code programmatically (claude -p)

`source:code.claude.com/docs/en/headless` - source - <https://code.claude.com/docs/en/headless>

Anthropic's docs for the non-interactive claude -p mode: tool allow lists, permission modes for scripts, output formats. Saved with the data-usage page for the telemetry defaults.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** claude -p is what a system crontab, launchd job or CI runner calls; this page sets what such a run may do without a person.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

claude -p brings no scheduler; pair it with cron, launchd or GitHub Actions. A run denies what it cannot get approved, so list tools with --allowedTools rather than reaching for broad modes. Metrics telemetry is on with an Anthropic sign-in and off by default on Bedrock, Vertex and Foundry.

## Claims

1. From v2.1.302, claude -p starts in Manual mode when nothing sets a mode, and a call needing approval is denied unless a hook or prompt tool approves it.

   > With Claude Code v2.1.302 or later, `claude -p` runs start in Manual mode when [nothing sets a permission mode](https://code.claude.com/docs/en/permission-modes.md#which-mode-a-non-interactive-run-starts-in).

   Locator: headless.md, section Auto-approve tools. Source: <https://code.claude.com/docs/en/headless>, retrieved 2026-11-12.

2. For an unattended run the docs show auto mode with prompts turned off, so anything that would prompt is denied.

   > claude -p "Update the dependency pins and run the tests" --permission-mode auto --permission-prompts none

   Locator: headless.md, section Auto-approve tools, example. Source: <https://code.claude.com/docs/en/headless>, retrieved 2026-11-12.

3. Usage metrics are on by default with an Anthropic sign-in; DISABLE_TELEMETRY=1 turns them off.

   > | **Metrics** | Default on. `DISABLE_TELEMETRY=1` to disable.

   Locator: data-usage.md, section Default behaviors by API provider, table. Source: <https://code.claude.com/docs/en/data-usage>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. headless.md and data-usage.md (markdown versions) against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `7b44923d96826dd34ead76976eeea99482a65c58210e385cf7ba08a621e01aa6`
- Lane: automation

## Observed

Nothing collected yet.

## Related

- alternative_to: [Claude Code cloud scheduled tasks (formerly routines)](code.claude.com__docs__en__routines.md)
- integrates_with: [GitHub Actions: events that trigger workflows (schedule)](docs.github.com__en__actions__reference__workflows-and-actions__events-that-trigger-workflows.md)

## Referenced by

- [Claude Code cloud scheduled tasks (formerly routines)](code.claude.com__docs__en__routines.md) (alternative_to)
- [GitHub Actions: events that trigger workflows (schedule)](docs.github.com__en__actions__reference__workflows-and-actions__events-that-trigger-workflows.md) (integrates_with)
- [Codex non-interactive mode (codex exec)](learn.chatgpt.com__docs__non-interactive-mode.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
