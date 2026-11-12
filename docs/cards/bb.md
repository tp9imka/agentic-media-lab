---
id: guide:bb
title: bb for scheduled Claude Code and Codex runs
summary: What bb's automations plugin can and cannot carry in a scheduled content pipeline, from its own docs, read, not run.
use_when: "Use this page when you are deciding whether to schedule Claude Code or Codex runs with bb."
concepts: [concept:scheduling-and-runtimes, concept:automation, concept:orchestration, concept:agent-portability]
last_reviewed: 2026-11-12
---

# bb for scheduled Claude Code and Codex runs

A card on bb for a developer who wants Claude Code or Codex to run on a timer. Everything on this page is read, not run: the hub has not started a bb schedule. Read the stage table and the permission default first. Other places a schedule can live are compared in [Run it on a schedule with an approval step](../cheatsheets/schedule-with-approval.md).

## What it is

bb is a local server and app that runs Claude Code, Codex and other agent CLIs as threads ([bb]). Its builtin automations plugin fires an agent prompt or a stored script on a 5-field cron with a timezone, or once at a set time or delay ([bb]).

## What it can carry

| Pipeline stage | bb feature |
|---|---|
| Fire on a timer | Automations: recurring cron or one-shot time or delay ([bb]) |
| Agent step | An agent automation that runs Claude Code or Codex ([bb]) |
| Script step (your render or upload script) | A stored script automation ([bb script runtime]) |
| Overlapping tick | "An automation has at most one active run." ([bb script runtime]) |
| Failed run | Retries after 30 seconds and then 60 seconds, never past the next scheduled run ([bb script runtime]) |
| Run history, pause, re-run | Run history and a sidebar to pause or re-run ([bb]) |
| Ask a person a question | Ask User Question card, open 30 minutes by default ([bb configuration]) |
| Generate video, images or audio | No bb feature |
| Approval gate before publish | No bb feature ([bb]) |
| Post to a platform | No bb feature |

"No bb feature" means none of the four bb records names one; the tool record lists orchestration as its only lever ([bb]). A failing run never pauses the automation ([bb script runtime]). A process that starts its own session, such as `tmux`, `setsid` or a daemon, is not stopped by bb ([bb script runtime]), so a long render launched that way is not cleaned up.

## How a schedule is declared

The schedule flags, quoted from bb's automations skill ([bb], as quoted on 2026-11-12):

```text
--cron <expr>                  Recurring 5-field cron expression
--timezone <tz>                IANA timezone for --cron
--at <datetime>                One-shot run time, preferably ISO 8601
--in <duration>                One-shot delay, e.g. 30s, 5m, 2h, 1d
```

The full create command is not quoted in the record. Read `plugins/automations/skills/automations/references/creation.md`, the source named on the [bb] record.

## What must stay running

The bb server machine, awake. bb's guide says: "while the server machine is asleep or off, nothing can reach bb and running threads may stop" ([bb multiple devices]). The Keep Awake plugin runs caffeinate, but a closed laptop lid still sleeps ([bb]). All state, including automations, lives under `~/.bb/` by default ([bb configuration]).

## Permission modes for unattended runs

The default when no mode is given, quoted ([bb]):

> When `--permission-mode` is omitted, the plugin chooses Approve for me (`auto`) when the provider supports it and otherwise uses Full Access (`full`).

In Full Access, the Claude Code provider setting `fullAccessApprovalsEnabled` defaults to false, and the docs say "`false` approves every request" ([bb configuration]). Set to true, it shows Claude Code's own `permissions.ask` rules, PreToolUse hooks that answer `ask`, and built-in safety checks ([bb configuration]). The records quote no other permission-mode values.

## Approval

What exists:

- An agent can ask a person through the Ask User Question card, which stays open 30 minutes by default; a server restart closes every open question ([bb configuration]).
- A person can pause or re-run an automation from the sidebar ([bb]).

What does not:

- Automations have no approval step of their own ([bb]).
- The records do not say whether an automation run can raise an Ask User Question card.

A gate before publish has to come from elsewhere; options are in [Run it on a schedule with an approval step](../cheatsheets/schedule-with-approval.md).

## Secrets and telemetry

- Plugins are full-trust code inside the server process and keep secret settings under `<dataDir>/plugins/<id>/secrets/` ([bb configuration]).
- The script runtime injects `BB_SERVER_URL` and IDs, not secrets ([bb script runtime]).
- A code read recorded on the tool record shows variables passed with `--env-json` kept as a string map in the plugin's SQLite file, so API keys do not belong there; the docs do not say this ([bb]).
- Binding the server to 0.0.0.0 exposes an API that, in the docs' words, "is unauthenticated and permits command execution and file reads" ([bb configuration]). Keep it on 127.0.0.1 and use bb connect or Tailscale Serve for phone access ([bb configuration]).
- Telemetry, quoted: "Production runs (the desktop app, `npx bb-app`, and `pnpm start` checkouts) send anonymous usage telemetry" ([bb]). The record states that `BB_TELEMETRY=false` turns it off and that it goes to PostHog ([bb]). The saved quote stops before the opt-out sentence, so the opt-out is the record's paraphrase, not a verbatim quote.

## What the hub did not find

- No independent report of bb used outside coding. Every bb source in the hub is bb's own documentation, marked single-source ([bb configuration], [bb script runtime], [bb multiple devices]).
- Missed-tick behaviour after sleep: not confirmed by the docs. The tool record's fit notes say a code read suggests missed ticks collapse into one run, and that no doc states it ([bb]).

[bb]: ../../catalog/tool/get-bb__bb.md
[bb configuration]: ../../catalog/source/github.com__get-bb__bb__blob__main__docs__configuration.md.md
[bb script runtime]: ../../catalog/source/github.com__get-bb__bb__blob__main__plugins__automations__skills__automations__references__script-runtime.md.md
[bb multiple devices]: ../../catalog/source/github.com__get-bb__bb__blob__main__docs__multiple-devices.md.md

## Not covered yet

- Behaviour of a tick missed while the Mac slept, from bb's docs.
- The verbatim telemetry opt-out sentence.
- The full `create` command and the list of `--permission-mode` values.
- Whether an automation run can ask a person and wait.
- Any bb run by the hub, so no timing or reliability figure.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
