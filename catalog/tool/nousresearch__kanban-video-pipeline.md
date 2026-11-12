# Kanban Video Pipeline

`tool:nousresearch/kanban-video-pipeline` - tool - <https://github.com/NousResearch/kanban-video-pipeline>

A Hermes Agent demo in which director, cinematographer, renderer and editor profiles split a brief into a task graph and produce an MP4 with ASCII video, p5.js and ffmpeg.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Orchestration](../../docs/glossary.md#orchestration), [Code-driven video](../../docs/glossary.md#code-driven-video)

Also known as: hermes kanban video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A worked example of an agent video pipeline driven by a task board instead of a person, with a block-and-notify path when something fails.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: experimental.

| field | value |
|---|---|
| tool_type | framework |
| agents | hermes |
| levers | orchestration, story, review-loop |
| cost | paid |

Needs Hermes, a running gateway and an OpenRouter key (the README names claude-opus-4.6), so every run is paid. No approval step before the final cut: a person only steps in when a worker blocks. The setup sources ~/.hermes/.env into the shell. It is a demo of one video, not a reusable product; setup.sh was not run or read in full.

## Claims

1. The pipeline runs with no human input; stages promote when their parents complete.

   > The entire pipeline auto-runs with zero human intervention.

   Locator: README.md, section What This Is. Source: <https://github.com/NousResearch/kanban-video-pipeline/blob/main/README.md>, retrieved 2026-11-12.

2. The gateway hosts the board dispatcher, which picks up ready tasks every 60 seconds; stuck tasks mean the gateway is down.

   > The gateway hosts the kanban dispatcher that picks up ready tasks every 60 seconds.

   Locator: RUN.md, step 2 Gateway must be running. Source: <https://github.com/NousResearch/kanban-video-pipeline/blob/main/RUN.md>, retrieved 2026-11-12.

3. A blocked worker notifies you, and unblocking respawns it with your comment in context.

   > Unblock (respawns the worker with your comment in context)

   Locator: RUN.md, section If something blocks. Source: <https://github.com/NousResearch/kanban-video-pipeline/blob/main/RUN.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and RUN.md against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `8c1720d1337450b34b6d652d1d0765b17f1b5c85b30ded1a4a9d1541fc9773ec`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-05-02
- default_branch: main
- fetched_at: 2026-11-12
- forks: 17
- last_activity: 2026-05-02
- licence: unknown
- open_issues: 1
- sources: https://api.github.com/repos/NousResearch/kanban-video-pipeline, https://skills.sh/api/search?q=kanban-video-pipeline
- stars: 63

## Related

- depends_on: [Hermes Agent](nousresearch__hermes-agent.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
