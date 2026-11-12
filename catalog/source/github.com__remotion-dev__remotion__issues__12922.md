# Remotion issue 12922: the skill asks agents to check audio they cannot hear

`source:github.com/remotion-dev/remotion/issues/12922` - source - <https://github.com/remotion-dev/remotion/issues/12922>

An open Remotion issue, filed by the maintainer, reporting that the official video-editing skill tells agents to check audio around cuts, so agents try to play the composition in Studio. A community fix (PR 13039) was closed without merging, and the line is still in the published skill on 2026-11-12.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Review loop](../../docs/glossary.md#review-loop)

Tags: remotion, audio-check

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** An agent cannot listen, so an audio check in a skill turns into wasted Studio sessions or a false 'checked'. The closed PR spells out what an agent can check instead.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Until the skill changes, override the line in your own AGENTS.md or prompt: check audio in code (from, trimBefore, trimAfter, durationInFrames, volume envelope against the cut frames), render stills for the visual side, and hand the user a list of timestamps to listen to. For a real signal, measure loudness and silence with ffmpeg rather than asking the agent to listen. The fix PR was closed without a stated reason in its body; the reason was not checked here.

## Claims

1. The issue was opened on 2026-11-03 and is open on 2026-11-12; the fix PR 13039 was closed on 2026-11-07 without being merged.

   > Merged: n/a Created: 2026-11-06T21:37:58Z Closed: 2026-11-07T12:56:33Z

   Locator: GitHub API pulls/13039, merged_at and closed_at fields (saved header); issue state in the first block. Source: <https://github.com/remotion-dev/remotion/pull/13039>, retrieved 2026-11-12.

2. The published Remotion skill still tells the agent to check audio around cuts, which it cannot hear.

   > Check visual output and audio around cuts, overlay boundaries, and sound tails.

   Locator: skills/remotion-markup/video-editing.md, section Preserve the edit when restructuring, paragraph 2. Source: <https://github.com/remotion-dev/skills/blob/main/skills/remotion-markup/video-editing.md>, retrieved 2026-11-12.

3. The proposed replacement checks audio in code: each sound's timing fields and volume envelope against the cuts.

   > for audio, confirm in code that each sound's `from`, `trimBefore`, `trimAfter`, `durationInFrames` and volume envelope still line up with the cuts and leave room for sound tails

   Locator: PR 13039 body, bullet 2. Source: <https://github.com/remotion-dev/remotion/pull/13039>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. issue 12922 and PR 13039 from the GitHub API, and the published skill file on main, against the record
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `fe48f59bb452de06059287f3965529b4ed27f5c6489d8cc27ed1d63538defe90`
- Lane: radar-2026-11-12

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-06-23
- default_branch: main
- fetched_at: 2026-11-12
- forks: 6075
- installs: 2885
- installs_by_skill: {"add-effect": 940, "add-expert": 2550, "add-sfx": 2785, "docs-demo": 2573, "fix-dependabot": 1103, "make-pr": 998, "pr-name": 1103, "video-report": 2812, "web-renderer-test": 2885, "writing-docs": 2865}
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 195
- registry: skills.sh
- sources: https://api.github.com/repos/remotion-dev/remotion, https://skills.sh/api/search?q=remotion
- stars: 72681

## Related

- evaluated_on: [Remotion Agent Skills](../tool/remotion-dev__skills.md)
- extends: [Remotion PR 13133: agents skipped the interactivity skill](github.com__remotion-dev__remotion__pull__13133.md) - Same week, same skill set: another case where skill text does not match what an agent can do.

## Referenced by

- [Codex issue 60616: async video task ended with no file and no check](github.com__openai__codex__issues__60616.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
