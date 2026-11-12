---
id: example:hyperframes-vs-remotion
title: Same brief, HyperFrames vs Remotion, vendor skills only
summary: Two fresh Claude agents get one fixed 20 s brief, one per stack, and render locally with no human help.
use_when: "Use this page when you are choosing between HyperFrames and Remotion for agent-written video, or want to see what each vendor's skills make an agent do."
concepts: [concept:code-driven-video, concept:agent-skills, concept:review-loop, concept:motion-and-transitions]
last_reviewed: 2026-11-12
---

# Same brief, HyperFrames vs Remotion, vendor skills only

What this is: one controlled run per stack. For anyone choosing a code-driven renderer for a
coding agent. Read the verdict table, then "What the runs found", then the limits.

**Status: ran.** One run per arm on 2026-11-12. This is a tiny sample. It shows that both
stacks work end to end from the vendor's skills alone, and what each first deliverable looked
like. It does not rank the stacks.

## Goal

With only the vendor's own skills and one fixed [brief](BRIEF.md), does a Claude agent get a
spec-conformant 20 s clip out of each stack, locally, with no human help? What defects does
each first deliverable carry?

## Setup

- Agent under test: one fresh Claude subagent per arm, given the brief and an empty folder.
- Skills: the ones each vendor ships. No other skills, no web search, no example repos.
- Machine: Apple M3 Max, 64 GB, macOS, Node 22, ffmpeg 7.1.1. Local render only.
- No human message during a run. A 30 minute cap.
- The pass or fail thresholds below were written down before either arm ran.

## Threshold (fixed before the run)

An arm passes when its file is a readable MP4 at 1920x1080, 30 fps, 20.0 s +/- 0.5 s, h264,
has no black segment over 1.0 s after the first 0.5 s, no frozen segment over 4.0 s, and was
delivered inside the cap with no human message. [measure.py](measure.py) checks all but the
last two.

## Results

Measured by `measure.py` on the delivered files (rung: agent-run for the clips, scripted-run
for the measurement). Files: [results/hyperframes.json](results/hyperframes.json),
[results/remotion.json](results/remotion.json).

| | HyperFrames | Remotion |
|---|---|---|
| Verdict against the threshold | pass | pass |
| Size, rate, length | 1920x1080, 30 fps, 600 frames, 20.0 s | 1920x1080, 30 fps, 600 frames, 20.0 s |
| Codec | h264, yuv420p | h264, yuv420p |
| File size | 780,393 bytes | 722,822 bytes |
| Black segments | 0.33 s at 2.97 s | 0.23 s at 0.0 s, 0.17 s at 7.93 s |
| Longest frozen segment | 2.17 s | 2.5 s |
| Share of the clip frozen | 0.716 | 0.544 |

From the agents' own run logs ([HyperFrames](results/hyperframes-runlog.md),
[Remotion](results/remotion-runlog.md)). These are self-reported, not measured by us:

| | HyperFrames | Remotion |
|---|---|---|
| Wall time | 7 min 46 s | 11.0 min |
| Full renders | 1 | 3 |
| Times the agent inspected frames | 3 | 4 |
| Fixes made after looking | 2 | 3 |
| Size of the working folder | 121M, plus 199M of cache outside it | 857M |

Clips: [results/hyperframes.mp4](results/hyperframes.mp4),
[results/remotion.mp4](results/remotion.mp4).
Contact sheets (12 frames each): [HyperFrames](results/hyperframes-sheet.png),
[Remotion](results/remotion-sheet.png).

### Blind review (judgement, one reviewer, one clip per arm)

A separate agent scored the two clips as "A" and "B" on six criteria, 0 to 2 each, from
stills. Full text with frame evidence: [results/review.md](results/review.md).

| Criterion | HyperFrames | Remotion |
|---|---|---|
| Copy exact | 1 | 1 |
| Hierarchy and type | 2 | 2 |
| Alignment and safe area | 2 | 2 |
| Palette obeyed | 1 | 2 |
| Entrances and transitions | 1 | 2 |
| Nothing clipped, overlapping or broken | 1 | 1 |
| Total out of 12 | 8 | 10 |

Why the two points differ, in the reviewer's words: the HyperFrames clip added a grey quote
panel and grey secondary text to the three briefed colours, and three of its scene changes
pass through a frame that shows only the accent bar. The Remotion clip's two dissolves stack
the outgoing and incoming headline for about five frames.

The reviewer could not judge easing or how the motion feels at speed. Nobody watched either
clip play.

## What the runs found

These are single observations from one run each.

- **Both install commands differ from the documentation.**
  - HyperFrames: `npx hyperframes skills update` starts a skills installer with `--global`
    that writes into the home directory's agent skill folders. The agent read that in the CLI
    source and did not run it. It used the skills bundled in the local npm package instead.
  - Remotion: `npx remotion skill` does not exist in 4.0.543. The command is
    `npx remotion skills add`, and it installs at project scope.
- **The HyperFrames CLI wrote outside the project**: a config file with telemetry enabled and
  an anonymous id, a 199M cache with its own headless browser, and preview logs, all under
  the home directory. The agent set `HYPERFRAMES_NO_TELEMETRY=1` and `DO_NOT_TRACK=1` and
  skipped the usage beacons the skill asks for. Four help calls ran before the opt-out.
- **Remotion's default render was untagged for colour.** The first render decoded the accent
  as `#43B589` instead of the briefed `#4CC38A`. The agent found `--color-space=bt709` in the
  CLI help and used it for the final. That flag is not in the skills. The skills-only render
  is described in the run log.
- **Both agents found their layout bugs only by rendering stills and looking.** HyperFrames:
  a data line readable for about 1.3 s, labels too small at phone width. Remotion: an accent
  bar that had shrunk to nothing, and non-opaque pixels during slides.
- **Each skill shaped the result in a visible way.** HyperFrames' motion rules produced four
  different entrances and three kinds of seam. Remotion's `TransitionSeries` rule produced
  overlapping transitions with no empty frame at a cut.
- **The HyperFrames clip counts up to 147**, so it shows numbers that are not in the brief
  (54, 112) on the way. For a line that reports a verification result, that is a defect.

## Limits

- One run per arm. A second run could reverse any difference here.
- The agent under test was a Claude subagent, not an interactive Claude Code session, and
  it could not open a live preview.
- The HyperFrames arm used the skills bundled in the npm package, not the ones the installer
  fetches. They were not compared.
- The reviewer's brief names both toolchains, so it knew which two stacks were compared,
  though not which clip was which.
- The brief is ambiguous on whether "Step 1" is on-screen copy. Each arm read it differently
  and each lost a point for copy.
- Wall time, render counts and fix counts come from the agents' logs.
- Not measured: token cost, repeatability, audio, motion at playback speed.

## Run it

```sh
python3 examples/hyperframes-vs-remotion/measure.py hyperframes examples/hyperframes-vs-remotion/results/hyperframes.mp4 --out /tmp/hf.json
python3 examples/hyperframes-vs-remotion/test_smoke.py
```

To repeat an arm, give an agent [BRIEF.md](BRIEF.md) and the vendor's skills, then measure
the file it delivers. Read the install notes above first.

## Sources

- Records: [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md),
  [Remotion](../../catalog/tool/remotion-dev__remotion.md),
  [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md).
- Agent-written source for both clips: [results/source/](results/source/).

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
