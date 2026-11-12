---
id: example:skill-ablation-contract-first
title: Does the hub's own skill change the result?
summary: The same brief and renderer, with the vendor's skills alone and with the hub's contract-first-video skill added. The clip got cleaner and plainer, and gained one rubric point of the two the test required.
use_when: "Use this page when you are deciding whether a defect-prevention skill is worth adding to a video project, or want a measured before and after for one skill."
concepts: [concept:agent-skills, concept:review-loop, concept:evaluation, concept:motion-and-transitions]
last_reviewed: 2026-11-12
---

# Does the hub's own skill change the result?

What this is: a test of [contract-first-video](../../skills/contract-first-video/SKILL.md), the
first skill this hub wrote. For anyone deciding whether a rule-and-check skill makes
agent-made video better. Read the verdict, then "What the skill cost".

**Status: ran. Verdict: narrowed.** One run per arm, one reviewer, on 2026-11-12. The skill
removed the defects it was written to remove. It did not reach the improvement the test
required, and it made the clip plainer.

## Goal

With the same brief and the same renderer, does adding one skill to the vendor's skills give a
better first deliverable? As far as the hub has found, no skill in this field has a published
before and after measured by someone other than its author.

## Setup

- **Vendor only**: the HyperFrames clip from [the first example](../hyperframes-vs-remotion/README.md),
  made by a Claude subagent with the vendor's skills.
- **With the skill**: a fresh Claude subagent, the same brief, the vendor's skills from the
  local package, plus `contract-first-video` and its bundled checker. It wrote its own contract
  from the brief. It was told not to read the hub's reference contract, the other attempts, or
  the lab folder.
- Measures: [clipcheck](../../lab/clipcheck/README.md) under the hub's reference contract, which
  the agent never saw; and a blind review of both clips as "A" and "B", tool names removed.

## Threshold (fixed before the result)

- Pass: zero clipcheck errors under the reference contract **and** at least 2 points above the
  vendor-only clip out of 12.
- Narrowed: zero errors and 0 or 1 point higher.
- Fail: a checker error, or a lower score.

## Results

Checker, measured here with the rules as committed
([vendor only](results/clipcheck-vendor-only.json), [with skill](results/clipcheck-with-skill.json)):

| | Vendor only | With the skill |
|---|---|---|
| Verdict | fail | pass |
| Errors | 1 (empty frames at three scene changes) | 0 |
| Warnings | 1 (a number not in the brief) | 1 (two strings not read on screen; both are there) |

Blind review, one reviewer, judgement ([review.md](results/review.md)):

| Criterion (0-2) | Vendor only | With the skill |
|---|---|---|
| Copy exact | 1 | 2 |
| Hierarchy and type | 2 | 1 |
| Alignment and safe area | 2 | 2 |
| Palette obeyed | 1 | 2 |
| Entrances and transitions | 2 | 1 |
| Nothing clipped, overlapping or broken | 1 | 2 |
| Total out of 12 | 9 | 10 |

From the agents' own logs, self-reported:

| | Vendor only | With the skill |
|---|---|---|
| Wall time | 7 min 46 s | 9.9 min |
| Renders | 1 | 3 |
| Checker fix rounds | not used | 0 of 4 |
| Look rounds | 3, by the maker | 2, the first by a clean-context sub-agent |

Clip: [with-skill.mp4](results/with-skill.mp4). The vendor-only clip is
[hyperframes.mp4](../hyperframes-vs-remotion/results/hyperframes.mp4). Contact sheets:
[vendor only](results/vendor-only-sheet.png), [with skill](results/with-skill-sheet.png). The
agent's contract: [agent-contract.json](results/agent-contract.json). Its log:
[agent-runlog.md](results/agent-runlog.md).

**Verdict: narrowed.** One point higher, not two.

One correction to the record: when the clip was first checked, the checker reported one error,
"two strings not read on screen". Both strings are on screen. By the letter of the threshold
that was a fail on the first criterion, caused by the checker and not by the clip. The rule has
since been changed: exact copy is checked in the project's source, and reading text from
pixels only advises. The table above uses the changed rule.

## What the skill bought

- **Exact copy.** The contract's `copy` list and `decisions` settled the questions that cost
  both agents a point in the first example: no role labels, no added quote marks, no
  count-up. The reviewer found "all ten strings present as written".
- **No broken frames.** The skill's cause-level rules ("the exit ends at the cut", "reveal, do
  not count up") gave a clip that passed every frame rule on its first render, with no fix
  round.
- **Palette discipline.** No panel fill, no extra grey.
- **A second pair of eyes that found things.** The clean-context reviewer caught a heading at
  a different height in each scene, a rule missing on the cut frame, and scenes that sat on a
  heading alone. The checker cannot measure any of them.

## What the skill cost

- **Transitions became cuts.** The skill says an incoming element must be readable when it
  arrives and must not fade in from a blur. The agent followed it literally: every scene
  change is "a 4-frame blur/fade/rise of the old scene", then "the new headline is on screen
  at full opacity on the very next frame". The reviewer scored this below the vendor-only
  clip's three designed transitions. The checker passed it, because its scene-change rule only
  asks for motion at the cut.
- **A flatter design.** The reviewer found headline and supporting text "close in size", small
  green text of about 30 px, and "same layout and same transition four times". The vendor-only
  clip was "the more designed and varied piece".
- **More time.** 9.9 minutes and 3 renders against 7 minutes 46 seconds and 1.

The pattern: a skill made of prohibitions removes defects and removes ambition with them. The
rule that prevented an unreadable frame also prevented a transition.

## Limits

- One run per arm, one reviewer. The reviewer called one of its own scores "borderline".
- **The skill was written after seeing the vendor-only clip's defects.** It is tuned to this
  brief. A brief it has never seen is the fair test and has not been run.
- The arms are not matched: the vendor-only run happened earlier, with a 30 minute cap and the
  vendor's own review commands; the with-skill run had a 40 minute cap.
- This reviewer scored the vendor-only clip 9 of 12. Earlier sessions scored the same file 8
  and 6. Only the two columns of one session compare.
- Motion was judged from stills. Nobody watched either clip play.
- The skill has been edited since this run (see below). The edited version is untested.

## Changed in the skill after this run (untested)

- The copy check moved from pixels to source, as above.
- Look points grew from six to eight: a scene sitting on its heading alone, and an element
  that moves between scenes.
- Sheet commands state which tile is which frame, and add a strip through the start of each
  scene.
- New build rules: overlap the outgoing and incoming scene for several frames, a cut with a
  settle is not a transition, use more than one kind of transition, keep the headline at
  least 1.5 times the supporting text, and keep small text at 40 px or more on a 1080 px frame.

## Run it

```sh
python3 lab/clipcheck/clipcheck.py examples/skill-ablation-contract-first/results/with-skill.mp4 --contract lab/clipcheck/contracts/quote-first.json --source examples/skill-ablation-contract-first/results/source
python3 examples/skill-ablation-contract-first/test_smoke.py
```

## Sources

- The skill: [skills/contract-first-video/SKILL.md](../../skills/contract-first-video/SKILL.md).
- Records behind its rules: [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md),
  [video-shotcraft](../../catalog/tool/vincentwei1021__video-shotcraft.md),
  [Remotion PR 13133](../../catalog/source/github.com__remotion-dev__remotion__pull__13133.md),
  [Remotion issue 12922](../../catalog/source/github.com__remotion-dev__remotion__issues__12922.md),
  [Codex issue 60616](../../catalog/source/github.com__openai__codex__issues__60616.md).

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
