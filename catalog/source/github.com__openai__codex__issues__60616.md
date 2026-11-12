# Codex issue 60616: async video task ended with no file and no check

`source:github.com/openai/codex/issues/60616` - source - <https://github.com/openai/codex/issues/60616>

An open Codex Desktop issue (2026-11-10): asked to make a 40-45 s video through the HeyGen connector and save the MP4, the agent reported 'still generating', ended its turn with no file, and only noticed the failed render when the user asked again about 30 minutes later.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Feedback loop](../../docs/glossary.md#feedback-loop), [Hosted video models](../../docs/glossary.md#hosted-video-models)

Tags: async-jobs, codex

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** Hosted video jobs are asynchronous, and an agent that ends its turn on a job id hands back nothing. The reader needs an explicit poll-until-terminal and file check in the task.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Put the done condition in the prompt or AGENTS.md: poll the job to a terminal state, download, then check the file exists at the path and probe it (duration, resolution) with ffprobe before saying done. The same failure applies to any async video API, not only HeyGen. One user report on Windows; the reporter says the HeyGen render failure went to HeyGen separately. Not reproduced here.

## Claims

1. The issue was opened on 2026-11-10 and is open on 2026-11-12.

   > State: open Merged: n/a Created: 2026-11-10T16:13:15Z

   Locator: GitHub API issues/60616, state and created_at fields (saved header). Source: <https://github.com/openai/codex/issues/60616>, retrieved 2026-11-12.

2. The agent ended its turn with no video and no file in the requested folder.

   > then ended its turn without a video or a file in the requested folder.

   Locator: issue body, Product feedback / observed failure, paragraph 1. Source: <https://github.com/openai/codex/issues/60616>, retrieved 2026-11-12.

3. The reporter asks that Codex verify the output file and destination before presenting the task as complete.

   > verify the requested output artifact and destination before presenting the task as complete

   Locator: issue body, Expected behavior. Source: <https://github.com/openai/codex/issues/60616>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. issue body and state from the GitHub API against the record
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `708b0e4212cbafe630b226768cfa89e2f794ce95e17fe81245be77a3c719329d`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-04-13
- default_branch: main
- fetched_at: 2026-11-12
- forks: 21388
- installs: 4155
- installs_by_skill: {"babysit-pr": 4155, "code-review": 749, "test-tui": 2834}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 27422
- registry: skills.sh
- sources: https://api.github.com/repos/openai/codex, https://skills.sh/api/search?q=codex
- stars: 135000

## Related

- extends: [Remotion issue 12922: the skill asks agents to check audio they cannot hear](github.com__remotion-dev__remotion__issues__12922.md) - Both are cases of an agent saying a check happened that it could not or did not do.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
