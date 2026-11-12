---
id: example:clipcheck-fix-loop
title: An agent fixes a clip from checker output alone
summary: A failing clip, a contract checker, and an agent that may not look at a single frame. It passes in two rounds and a blind reviewer scores the result higher.
use_when: "Use this page when you want a review loop for agent-made video that does not depend on the agent looking at stills, or want to know what a deterministic checker catches and misses."
concepts: [concept:review-loop, concept:code-driven-video, concept:evaluation, concept:motion-and-transitions]
last_reviewed: 2026-11-12
---

# An agent fixes a clip from checker output alone

What this is: one experiment with [clipcheck](../../lab/clipcheck/README.md), the hub's contract
checker. For anyone building a review loop for agent-made video. Read the result table, then
"What the checker got wrong".

**Status: ran.** One clip, one agent run, one reviewer, on 2026-11-12. A tiny sample. It shows
the loop works once and where it misleads. It does not show how often.

## Goal

Every skill in the hub tells the agent to render stills and look at them. Can a deterministic
checker carry the review loop instead: seconds per run, frame-exact, no vision tokens? And if
an agent optimises against a checker, does the clip get better or does it only pass?

## Setup

- The clip: the HyperFrames arm of [the first example](../hyperframes-vs-remotion/README.md),
  which a blind reviewer had marked down for frames that showed only an accent bar and for a
  counter that ran through numbers the brief does not contain.
- The contract: [quote-first.json](../../lab/clipcheck/contracts/quote-first.json). It is the
  example's brief as data: size, palette, safe area, scene times, copy, allowed numbers.
- The agent: a fresh Claude subagent given the project and the checker. Its only feedback was
  the checker's output. It was told not to render stills, open images or run any review command.
- Stop rule: `CLIPCHECK: PASS`, or 4 fix rounds, or 30 minutes.
- Then a blind review: a separate agent scored the before and after clips as "B" and "A" on a
  six-point rubric, from a brief with the tool names removed. It was asked to list differences
  that made a clip worse as well as better.

## Threshold (fixed before the run)

The experiment passes if the agent reaches `CLIPCHECK: PASS` inside the stop rule **and** the
blind reviewer does not score the after clip lower than the before clip. A pass on the checker
with a lower reviewer score would be published as a negative result.

## Results

Checker verdicts, measured here by `clipcheck.py` with the rules as committed
([before](results/clipcheck-before.json), [after](results/clipcheck-after.json)):

| | Before | After |
|---|---|---|
| Verdict | fail | pass |
| Errors | 1 | 0 |
| Warnings | 1 | 0 |
| Findings | empty-frames at 2.967-3.167 s, 7.967-8 s, 13-13.033 s; stray-numbers (126) at 14 s | none |

From the agent's log ([agent-runlog.md](results/agent-runlog.md)), self-reported:

| | |
|---|---|
| Fix rounds to pass | 2 |
| Renders | 3, about 11 s each |
| Wall time | about 3.5 minutes |
| Frames looked at | none |

Blind review, one reviewer, judgement ([review.md](results/review.md)):

| Criterion (0-2) | Before | After |
|---|---|---|
| Copy exact | 1 | 1 |
| Hierarchy and type | 2 | 2 |
| Alignment and safe area | 1 | 1 |
| Palette obeyed | 1 | 1 |
| Entrances and transitions | 1 | 2 |
| Nothing clipped, overlapping or broken | 0 | 1 |
| Total out of 12 | 6 | 8 |

The reviewer compared the clips frame by frame and listed seven differences. It judged the
after clip better at four of them, marginally better at one, saw no visible difference at one,
and gave no verdict at one.

Clips: [before.mp4](results/before.mp4), [after.mp4](results/after.mp4). Contact sheets:
[before](results/before-sheet.png), [after](results/after-sheet.png). The agent's edited
scenes: [results/source-after/](results/source-after/).

Verdict against the threshold: **pass**.

## What the agent changed

- **Empty frames at three scene changes.** Cause: two exit tweens ended one frame before the
  cut, and two scenes entered from zero opacity. Fix: later exit starts, and entrances that
  begin at 25 to 30 percent opacity.
- **A counter running from 0 to 147.** Fix: the count-up was removed; 147 is revealed as static
  text. The reviewer counted 17 intermediate values in the before clip. The checker had read
  only one of them (126), because it reads on-screen text every 0.5 s.
- **A scene change with nothing moving**, which the first fix had introduced. Fix: the next
  scene's entrance starts at the cut.

## What the checker got wrong

- **It pushed the agent to change something that was fine.** The first version of the
  "long hold" rule ignored slow motion, so three line wipes read as a 4.4 s hold. To clear the
  warning the agent shortened the wipes from 12 frames to 4. The reviewer gave no verdict on
  that change and noted that a 2-frame reveal "may be too fast to register as motion". The rule
  has since been corrected; with the committed rules the before clip no longer raises it. This
  is the main lesson of the run: an agent optimises against the checker, including its mistakes.
- **It cannot tell readable from present.** After the fix, incoming headlines are on screen at
  the cut but blurred and dim. The checker counts the frame as not empty. The reviewer called
  one of them "an unreadable ghost headline for 2 frames".
- **It missed defects the reviewer found in both clips**: text sliding across the accent bar at
  12.8 s, a grey panel behind the quote, "Step N" labels that the brief does not list as copy,
  and a layout that leaves the right half of the frame empty.

## Limits

- One clip, one agent run, one reviewer.
- The agent ran against an earlier version of the checker, which also raised the false "long
  hold" warning. The table above is measured with the corrected rules.
- The agent read two threshold constants in the checker's source when the output did not
  explain a finding. That is more than "output only". The messages now state those thresholds.
- The same reviewer protocol scored this "before" clip 8 of 12 in the first example and 6 of 12
  here. Scores from different review sessions are not comparable; only the two columns of one
  session are.
- Motion was judged from stills. Nobody watched either clip play.
- Not measured: token cost of either review style, repeatability, other renderers.

## Run it

```sh
python3 lab/clipcheck/clipcheck.py examples/clipcheck-fix-loop/results/before.mp4 --contract lab/clipcheck/contracts/quote-first.json
python3 examples/clipcheck-fix-loop/test_smoke.py
```

Add `--ocr` to read on-screen text (needs `tesseract` on PATH).

## Sources

- The checker and its rule pack: [lab/clipcheck](../../lab/clipcheck/README.md).
- Records the rules cite: [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md),
  [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md),
  [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md),
  [HyperFrames issue 4435](../../catalog/source/github.com__heygen-com__hyperframes__issues__4435.md).

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
