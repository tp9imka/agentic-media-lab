# bb

`tool:get-bb/bb` - tool - <https://github.com/get-bb/bb>

A local server and app that runs Claude Code, Codex and other agent CLIs as threads. Its builtin automations plugin fires an agent prompt or a stored script on a 5-field cron with a timezone, or once at a set time or delay.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes), [Orchestration](../../docs/glossary.md#orchestration), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: get-bb, bb-app, bb automations

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The closest fit found for a single developer who wants a scheduled Claude Code or Codex run on their own Mac, with run history and a sidebar to pause or re-run it.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | app |
| agents | claude-code, codex |
| levers | orchestration |
| cost | free-local |

Free to run locally; agent runs bill to the provider you already pay for. The scheduler lives inside the bb server, so the Mac must be awake (the Keep Awake plugin runs caffeinate but a closed lid still sleeps). Automations have no approval step of their own: an omitted --permission-mode falls back to auto, or to Full Access when the provider lacks auto. Telemetry to PostHog is on in production runs until you set BB_TELEMETRY=false. A code read (plugins/automations/src/rpc-types.ts, data.ts) shows script variables from --env-json kept as a string map inside the execution JSON in the plugin's SQLite file, so do not pass API keys that way; the docs do not say this. Not checked: missed-tick behaviour after sleep (the code computes the next run from the current time, which suggests missed ticks collapse into one run, but no doc states it).

## Claims

1. A schedule is a 5-field cron expression with an IANA timezone, or a one-shot time or delay.

   > --cron <expr> Recurring 5-field cron expression --timezone <tz> IANA timezone for --cron --at <datetime> One-shot run time, preferably ISO 8601 --in <duration> One-shot delay, e.g. 30s, 5m, 2h, 1d

   Locator: plugins/automations/skills/automations/references/creation.md, Schedule flags. Source: <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/creation.md>, retrieved 2026-11-12.

2. With no permission mode set, an agent automation runs in auto approval, or in Full Access when the provider has no auto mode.

   > When `--permission-mode` is omitted, the plugin chooses Approve for me (`auto`) when the provider supports it and otherwise uses Full Access (`full`).

   Locator: plugins/automations/skills/automations/references/creation.md, after Agent mode flags. Source: <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/creation.md>, retrieved 2026-11-12.

3. Production runs send anonymous usage telemetry by default; BB_TELEMETRY=false turns it off.

   > Production runs (the desktop app, `npx bb-app`, and `pnpm start` checkouts) send anonymous usage telemetry

   Locator: README.md, section Telemetry. Source: <https://github.com/get-bb/bb/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `dc08dc68e6b50036b2362dfef189eac8f4287b9f6d38010b2de139be8fb24eb5`
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

- depends_on: [bb automations: script runtime reference](../source/github.com__get-bb__bb__blob__main__plugins__automations__skills__automations__references__script-runtime.md.md) - run, retry and kill rules
- depends_on: [bb configuration reference](../source/github.com__get-bb__bb__blob__main__docs__configuration.md.md) - unauthenticated API, Full Access approvals
- depends_on: [Using bb on multiple devices](../source/github.com__get-bb__bb__blob__main__docs__multiple-devices.md.md) - which machine must stay on
- alternative_to: [Hermes Agent](nousresearch__hermes-agent.md)

## Referenced by

- [bb configuration reference](../source/github.com__get-bb__bb__blob__main__docs__configuration.md.md) (extends)
- [Using bb on multiple devices](../source/github.com__get-bb__bb__blob__main__docs__multiple-devices.md.md) (extends)
- [bb automations: script runtime reference](../source/github.com__get-bb__bb__blob__main__plugins__automations__skills__automations__references__script-runtime.md.md) (extends)
- [Hermes Agent](nousresearch__hermes-agent.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
