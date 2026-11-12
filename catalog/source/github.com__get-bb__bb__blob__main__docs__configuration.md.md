# bb configuration reference

`source:github.com/get-bb/bb/blob/main/docs/configuration.md` - source - <https://github.com/get-bb/bb/blob/main/docs/configuration.md>

bb's full settings reference: data directory, plugins, provider settings, Keep Awake, Ask User Question, startup flags and telemetry.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Review loop](../../docs/glossary.md#review-loop)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It names the two settings that decide how unattended a scheduled bb run really is, and the one network setting that exposes command execution.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Plugins are full-trust code inside the server process and keep secret settings under <dataDir>/plugins/<id>/secrets/. All state, including automations, lives under ~/.bb/ by default. Keep the server on 127.0.0.1 and use bb connect or Tailscale Serve for phone access.

## Claims

1. Binding the server to 0.0.0.0 exposes an unauthenticated API that can run commands and read files.

   > the public API is unauthenticated and permits command execution and file reads.

   Locator: section Startup Flags. Source: <https://github.com/get-bb/bb/blob/main/docs/configuration.md>, retrieved 2026-11-12.

2. In Full Access, Claude Code's own ask rules and hooks are skipped by default, so every request is approved.

   > Shows Claude Code's own prompts in Full Access (`permissions.ask` rules, PreToolUse hooks that answer `ask`, and built-in safety checks); `false` approves every request.

   Locator: section Plugins > Claude Code provider, fullAccessApprovalsEnabled row (default false). Source: <https://github.com/get-bb/bb/blob/main/docs/configuration.md>, retrieved 2026-11-12.

3. A question an agent asks a person times out after 30 minutes by default, and a server restart closes every open question.

   > The builtin Ask User Question plugin keeps an unanswered question card open for 30 minutes by default.

   Locator: section Ask User Question plugin. Source: <https://github.com/get-bb/bb/blob/main/docs/configuration.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. docs/configuration.md sections Startup Flags, Claude Code provider, Ask User Question, Plugins, Keep Awake against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `2eebd4d587790880a920fba4dc63abfbc7e785449fcd2044317b197c92289efe`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-02-24
- default_branch: main
- fetched_at: 2026-11-12
- forks: 786
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 852
- sources: https://api.github.com/repos/get-bb/bb, https://skills.sh/api/search?q=bb
- stars: 5381

## Related

- extends: [bb](../tool/get-bb__bb.md)

## Referenced by

- [bb](../tool/get-bb__bb.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
