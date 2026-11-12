# clipcheck

A contract checker for agent-made video. Stdlib Python plus `ffmpeg` and `ffprobe` on PATH.

The brief becomes data: a **contract** with the clip's size, rate, length, palette, safe area,
scene times, copy, allowed numbers, loudness range and caption limits. clipcheck measures a
rendered MP4 against it frame by frame and prints findings with timestamps and a fix hint.
Every rule names the hub record it comes from, and the quote it shows is pulled from the hub's
index when it runs.

It is the deterministic half of a review loop. It takes about 2 seconds per 20 s clip
(about 9 with text reading), reports exact frame times, and needs no vision model. It does not
replace looking: see "What it cannot see".

## Use

```sh
python3 lab/clipcheck/clipcheck.py out/final.mp4 --contract lab/clipcheck/contracts/quote-first.json
python3 lab/clipcheck/clipcheck.py out/final.mp4 --contract my-contract.json --source ./project --captions captions.vtt --ocr --json result.json
```

Exit code 0 when there is no error-level finding, 1 when there is, 2 on a usage problem.
`--ocr` reads on-screen text with `tesseract` when it is installed. `--json` writes the full
result, including per-frame series for content, motion and off-palette share.

Tell an agent: render, run clipcheck, fix what it reports, repeat until `CLIPCHECK: PASS`, then
look at a contact sheet once.

## Rules

| Rule | Level | What it measures |
|---|---|---|
| stream | error | size, frame rate, length and codec against the contract |
| colour-tags | warning | colour space, primaries and transfer are tagged in the file |
| first-frame | warning | the first frame is not background only |
| empty-frames | error | no frame mid-clip without scene content; fixed elements such as a rule that never leaves do not count as content |
| sparse-frames | warning | no run of 3 or more frames holding under 20% of the clip's usual content |
| palette | error | colours outside the contract palette; a tint between the background and an allowed colour passes |
| safe-area | error | content stays inside the contract margins for any half second or more |
| scene-times | warning | a move overlaps each contract scene change |
| abrupt-stops | warning | share of moves that end near their peak speed, the signature of linear motion |
| long-hold | warning | no stretch longer than the contract allows with no change on screen |
| loudness | error | integrated loudness and true peak inside the contract range |
| captions | error | lines, characters per line, characters per second and shortest time on screen |
| copy-source | error | every contract string is in the project's source files (with `--source <folder>`) |
| copy | warning | contract strings can be read on screen (with `--ocr`); advisory, because text reading misses small, coloured and monospace text |
| stray-numbers | warning | no number on screen that the contract does not list (with `--ocr`) |

Rule metadata, hints and sources are in [rules.json](rules.json). Contracts:
[quote-first.json](contracts/quote-first.json) (the brief of the hub's first example) and
[vertical-short.template.json](contracts/vertical-short.template.json) (1080x1920 with a
platform safe zone, a streaming loudness range and caption limits).

## Evidence

- On the two clips of [the first example](../../examples/hyperframes-vs-remotion/README.md) it
  reported the frame-level defects a blind reviewer had found by looking: three stretches with
  only an accent bar on screen at 2.97, 7.97 and 13.0 s, a counter showing a number that is not
  in the brief, and seven blank opening frames.
- In [the fix-loop experiment](../../examples/clipcheck-fix-loop/README.md) an agent given only
  its output got a failing clip to pass in two rounds, and one blind reviewer scored the result
  8 of 12 against 6 of 12 before. One run, one reviewer.

## What it cannot see

Found by the reviewer and missed by the checker, in the same clips:

- two headlines stacked on each other during a dissolve;
- text sliding across another element;
- an element that is on screen but too blurred or dim to read;
- added labels and changed line breaks (it checks that copy is present, not that nothing else is);
- an unbalanced layout.

Known weaknesses:

- **An agent optimises against it, including its mistakes.** An early version of the hold rule
  ignored slow motion; an agent sped up a wipe that was fine to clear the warning.
- Text is read every 0.5 s, so short-lived text can pass unseen.
- Reading text from pixels is unreliable: in a clean clip it missed two strings that were on screen. Exact copy is therefore checked in the project source, and the on-screen reading only advises.
- Analysis runs on a 160 x 90 grid; an element under about 12 px on a 1920 px frame may be missed.
- Thresholds are constants at the top of [clipcheck.py](clipcheck.py), set on two clips.
- Tints of palette colours pass by design. A brief that forbids them needs a stricter rule.

## Tests

`python3 examples/clipcheck-fix-loop/test_smoke.py` checks the before and after verdicts and
that every rule's source resolves to a quote in the hub index.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
