---
id: guide:first-render-claude-code
title: "First render in a day with Claude Code"
summary: A numbered procedure for a first code-rendered clip with HyperFrames or Remotion, built from the hub's one worked example and the renderer and skill records.
use_when: "Use this page when you want Claude Code to deliver its first rendered clip and need the install side effects, the still-frame step and the measurement in order."
concepts: [concept:code-driven-video, concept:agent-skills, concept:review-loop, concept:licences-and-territory, concept:delivery]
last_reviewed: 2026-11-12
---

# First render in a day with Claude Code

A procedure for a developer who wants Claude Code to render a short code-driven clip locally. It follows the [worked example](../../examples/hyperframes-vs-remotion/README.md), which was run here once per stack with a Claude subagent, not an interactive Claude Code session. Read that page's limits first. Statements about the run say "run here once"; statements from records are "read, not run".

## Contents

- [Procedure](#procedure)
- [What each run got wrong](#what-each-run-got-wrong)
- [Not covered yet](#not-covered-yet)

## Procedure

1. **Choose the stack on licence and side effects.**
   - [Remotion](../../catalog/tool/remotion-dev__remotion.md) is free for "a for-profit organization with up to 3 employees"; its notes say a bigger company needs a paid Company License. [Remotion 5.0](../../catalog/source/remotion.dev__docs__5-0-migration.md) makes company licence holders enable telemetry.
   - [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md) has no licence fee per its notes; the hub's collected licence is Apache-2.0. Its [skill](../../catalog/source/github.com__heygen-com__hyperframes__blob__main__skills__hyperframes__skill.md.md) asks the agent to run a usage beacon at start.
   - Run here once: the HyperFrames CLI wrote outside the project, under the home directory: a config file with telemetry enabled and an anonymous id, a 199M cache with its own headless browser, and preview logs.
   - Run here once: the Remotion folder reached 857M, of which a downloaded browser in `node_modules/.remotion/` was 459M; `npx` also cached packages in `~/.npm/_npx` ([run log](../../examples/hyperframes-vs-remotion/results/remotion-runlog.md)).
2. **Install, knowing each vendor's documented command behaved differently.** Run here once:
   - HyperFrames: `npx hyperframes skills update` starts a skills installer with `--global` that writes into the home directory's agent skill folders. The agent did not run it and used the skills bundled in the local npm package (`node_modules/hyperframes/dist/skills/`). It scaffolded with `npx hyperframes init video --skip-skills --skill=hyperframes` and set `HYPERFRAMES_NO_TELEMETRY=1` and `DO_NOT_TRACK=1`; four help calls ran before the opt-out ([run log](../../examples/hyperframes-vs-remotion/results/hyperframes-runlog.md)).
   - Remotion: `npx remotion skill` does not exist in 4.0.543. The command is `npx remotion skills add`, which installed at project scope into `.agents/skills/` with symlinks in `.claude/skills/` ([run log](../../examples/hyperframes-vs-remotion/results/remotion-runlog.md)).
3. **Write a brief with exact copy, sizes and palette.** Copy the shape of [BRIEF.md](../../examples/hyperframes-vs-remotion/BRIEF.md): a table of on-screen copy per time slot, 1920 x 1080, 30 fps, 20.0 s (600 frames), H.264, background `#0F1419`, text `#F2F4F7`, one accent `#4CC38A`, system fonts only. Run here once, the brief was ambiguous on whether "Step 1" is on-screen copy; each arm read it differently and each lost a point for copy. State in your brief which labels appear on screen.
4. **Have the agent render stills before the full render.**
   - Remotion, from the [Remotion](../../catalog/tool/remotion-dev__remotion.md) record's notes: `npx remotion still <entry> <id> out.png --frame=N` for one PNG, and `npx remotion render <id> out/frames --frames=0,30,90 --image-format=png` for several (v4.0.502+).
   - HyperFrames: run here once, the agent used `npx hyperframes snapshot --review --json` before its render ([run log](../../examples/hyperframes-vs-remotion/results/hyperframes-runlog.md)). No HyperFrames record quotes a still command.
   - Run here once, both agents found their layout bugs only by rendering stills and looking.
   - For HyperFrames finals, the [issue 4435](../../catalog/source/github.com__heygen-com__hyperframes__issues__4435.md) record reports that with 4 parallel workers in screenshot mode the first frame of workers 1-3 came out fully transparent, intermittently; it quotes "`--workers 1` produces zero blank frames".
5. **Measure the file.** From the example:

   ```sh
   python3 examples/hyperframes-vs-remotion/measure.py hyperframes examples/hyperframes-vs-remotion/results/hyperframes.mp4 --out /tmp/hf.json
   ```

   [measure.py](../../examples/hyperframes-vs-remotion/measure.py) checks a readable MP4 at 1920x1080, 30 fps, 20.0 s +/- 0.5 s, h264, no black segment over 1.0 s after the first 0.5 s, and no frozen segment over 4.0 s. It does not check the 30 minute cap or the no-human-message rule. Its thresholds are constants for this brief; `--sheet out.png` adds a 12-frame contact sheet. Run here once, both files passed.
6. **Look for the defects the measurement cannot see.** See the next section.

## What each run got wrong

All run here once, one run per stack, judged by one blind reviewer from stills ([review](../../examples/hyperframes-vs-remotion/results/review.md)). The reviewer scored HyperFrames 8 and Remotion 10 out of 12, and nobody watched either clip play.

| | HyperFrames | Remotion |
|---|---|---|
| Palette | added a grey quote panel and grey secondary text | default render decoded the accent as `#43B589`, not `#4CC38A`; the agent found `--color-space=bt709` in the CLI help, not in the skills |
| Transitions | three scene changes pass through a frame showing only the accent bar | two dissolves stack the outgoing and incoming headline for about five frames |
| Content | counts up to 147, so it shows 54 and 112, which are not in the brief | - |
| Found from stills | a data line readable for about 1.3 s, labels too small at phone width | an accent bar shrunk to nothing, non-opaque pixels during slides |

## Not covered yet

- A run in an interactive Claude Code session, or under Codex.
- A second run of either stack.
- Audio, captions and token cost on either stack.
- A HyperFrames still-frame command quoted in a record.
- A comparison of the bundled HyperFrames skills with the ones the installer fetches.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
