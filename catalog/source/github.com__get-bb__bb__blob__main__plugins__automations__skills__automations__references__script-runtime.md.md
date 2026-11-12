# bb automations: script runtime reference

`source:github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/script-runtime.md` - source - <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/script-runtime.md>

The bb automations skill reference for stored scripts: working directory, injected variables, retries, overlap and process cleanup.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It states how a failed or overlapping scheduled run behaves, which decides whether a nightly render job can double-fire or silently stop.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

Applies to both agent and script automations for the retry rules. A script that starts tmux, setsid or a daemon keeps running after bb stops it, so a long render launched that way is not cleaned up. The plugin injects BB_SERVER_URL and IDs, not secrets.

## Claims

1. An automation never runs twice at once; a duplicate tick joins the active run.

   > An automation has at most one active run. A duplicate tick or manual request uses the active run.

   Locator: section Execution safety, bullet 1. Source: <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/script-runtime.md>, retrieved 2026-11-12.

2. Failed recurring runs retry after 30 s and 60 s, never past the next scheduled run, and a failing automation is never paused.

   > Failed recurring runs retry after 30 seconds and then 60 seconds, but never later than the next scheduled run. After two retries, a failing automation waits for its next scheduled run. A failing run never pauses the automation;

   Locator: section Execution safety, bullet 2. Source: <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/script-runtime.md>, retrieved 2026-11-12.

3. Processes that start their own session or group escape bb's cleanup.

   > A process that starts its own session or process group, such as `setsid`, `tmux`, or a daemon, leaves the script's group and is not stopped.

   Locator: section Execution safety. Source: <https://github.com/get-bb/bb/blob/main/plugins/automations/skills/automations/references/script-runtime.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. script-runtime.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `cb27b45f02d20109e6c49bb2f10b70c06a69270c8681795e8fde40cede5a4e0a`
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
