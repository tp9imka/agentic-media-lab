---
name: contract-first-video
description: Use every time you make, change or re-render a video from code (HyperFrames, Remotion, Manim, Motion Canvas, ffmpeg) - load it BEFORE writing any scene, and again before you say a video is done. It turns the brief into a contract, checks every render against the contract with the clipcheck script, and ends with one independent look at the frames.
---

# Contract-first video

You cannot see or hear what you render. This skill replaces "it rendered, so it is done" with
a loop you can run: write down what the clip must be, measure the file against it after every
render, fix what the measurement reports, then look once at what a measurement cannot judge.

Everything you need is in this file and in `clipcheck/` beside it. There are no other files to
open. Do not skip a step because it "seems not relevant": each one exists because an agent
shipped the defect it prevents.

Setup, once: `clipcheck/clipcheck.py` must exist beside this file (it is the `lab/clipcheck`
folder of the Agentic Media Lab hub). It needs Python 3.10+, `ffmpeg` and `ffprobe`.
`tesseract` is optional and enables the text checks.

## Step 1 - Write the contract before any scene

Create `contract.json` in the project. Fill every field the brief decides. Start from this:

```json
{
  "name": "<clip name>",
  "stream": {"size": [1920, 1080], "fps": 30, "duration_s": 20.0, "duration_tolerance_s": 0.5, "codec": "h264"},
  "palette": {"background": "#0F1419", "allowed": ["#F2F4F7", "#4CC38A"], "tolerance": 30, "max_offpalette_share": 0.002},
  "safe_area": {"left": 0.04, "right": 0.04, "top": 0.09, "bottom": 0.09},
  "scenes": [{"name": "title", "start_s": 0, "end_s": 3}],
  "cut_tolerance_s": 0.35,
  "motion": {"max_abrupt_stop_share": 0.34, "max_still_s": 4.0},
  "audio": {"required": false, "integrated_lufs": [-20.0, -16.0], "true_peak_dbtp": -1.0},
  "captions": {"max_lines": 2, "max_chars_per_line": 42, "max_chars_per_second": 20, "min_duration_s": 0.834, "min_seconds_per_word": 0.3},
  "copy": ["<every string that must appear on screen, exactly>"],
  "numbers_allowed": [],
  "decisions": []
}
```

Rules for filling it:

- `copy` is every string the viewer must read, character for character. Nothing else may
  appear on screen. A role name in the brief ("Title:", "Step 1:") is NOT copy unless the
  brief says to show it. When you cannot tell, do not guess silently: choose the reading that
  adds no text, and record it in `decisions` as one sentence.
- `numbers_allowed` lists every number that may be visible. A counter that animates from 0
  to its value shows numbers that are not true. Reveal a figure; do not count up to it.
- `palette.allowed` is the brief's colours only. A tint of an allowed colour over the
  background passes; a new grey, a panel fill or a second accent does not.
- `safe_area` margins are fractions of the frame. For a vertical clip for social platforms
  use left 0.06, right 0.06, top 0.14, bottom 0.35, and size 1080 x 1920.
- `scenes` are the brief's time slots. Keep them exact; narration and captions depend on them.
- Delete `audio` or `captions` only when the brief has none. If the clip has sound, the
  loudness range above is the streaming range; do not master louder.
- Put every ambiguity you resolved in `decisions`. If the brief gives no value for a field,
  write your value and add a decision saying it was your choice.

Show the contract to the user if one is present. Otherwise continue.

## Step 2 - Build to the contract

Rules that the checker will hold you to, and what causes each failure:

- **Never leave the screen empty mid-clip.** Start each scene's first element at the cut, and
  let the outgoing scene finish its exit at the cut, not a frame before. An exit tween that
  ends at 2.97 s under a 3.0 s cut leaves bare frames.
- **Join scenes with a real transition, not a cut with a settle.** Overlap the outgoing and
  the incoming scene for 6 to 12 frames, so both are partly on screen. An old scene dropped
  mid-fade followed by the new headline at full opacity on the next frame reads as a hard cut.
  Use two or three different kinds of transition in one clip, not the same one every time.
- **The incoming element must be readable within a few frames of arriving.** A headline that
  stays at 25% opacity or blurred for many frames is not an entrance.
- **Nothing slides across another element.** Give exits a direction that clears fixed
  elements such as a side rule.
- **Ease every move.** Arrivals decelerate. No linear interpolation, no move that ends at
  full speed.
- **Exits are shorter than entrances.**
- **The first frame shows something.** Platforms take thumbnails from early frames.
- **One left edge for all titles, one type scale, the contract's palette.** Keep a headline
  at least 1.5 times the size of its supporting text, and no text under 40 px on a 1080 px
  high frame. The same element sits at the same position in every scene.
- **These rules prevent defects; they do not make a design.** After they hold, give the clip
  one deliberate idea of its own: a persistent element, an emphasised figure, a change of
  rhythm. In a test of this skill the clip came out clean and plain.
- **Use the frame.** Do not park every scene in the left third.
- **Deterministic renders only.** No `Date.now()`, no unseeded `Math.random()`. If the
  renderer has parallel workers and you see a blank frame, render with one worker.
- **Tag the colour space** when the renderer leaves it untagged (for Remotion add
  `--color-space=bt709`), or the palette shifts on playback.
- If the render is remote or asynchronous, poll until the file exists, then check it. Never
  end your turn on a job id.

## Step 3 - Render, then run the checker. Every time.

```sh
python3 clipcheck/clipcheck.py <output.mp4> --contract contract.json --source <project folder> --ocr --json clipcheck.json
```

`--source` checks that every `copy` string is in your project's source files, exactly. That
is the hard check for copy. `--ocr` reads text from the pixels and only advises: it misses
small, coloured and monospace text, so a "not read" warning means "open a frame and confirm",
not "the text is missing". Add `--captions captions.vtt` when there are captions. Without
`tesseract`, drop `--ocr`.

- `CLIPCHECK: FAIL` => fix every ERROR using its timestamps and `fix:` line, render, run
  again. Clear warnings too when that does not break the brief.
- At most 4 fix rounds. If it still fails, stop and report the remaining findings. Do not
  loosen the contract to pass, and do not edit the checker.
- A finding you believe is wrong: do not change a part of the clip that is fine in order to
  silence it. Confirm on a frame, leave the clip alone, and report the finding as a suspected
  false positive with your evidence. A clip with only such findings left is deliverable; say
  so plainly instead of reporting a bare FAIL.
- Fixing one finding can cause another (moving an exit can leave a scene change with no
  motion). Re-read the whole output after each round.

## Step 4 - Look once, with fresh eyes

The checker cannot see these. They are the defects a reviewer found in clips that passed:

1. two texts stacked on each other during a transition;
2. text or a panel sliding across another element;
3. an INCOMING element that is present but too dim or blurred to read in the frames after a
   cut (an outgoing element fading in its last frames is fine);
4. text on screen that the contract does not list (labels, quote marks, changed line breaks);
5. a layout that leaves the right half or the lower half of the frame empty in most scenes;
6. clipped glyphs lingering during a wipe;
7. a scene that sits on its heading alone for more than about a second before the rest arrives;
8. the same element at a different position from scene to scene (a heading that jumps).

Make the sheets:

```sh
ffmpeg -v error -y -i <output.mp4> -vf "select='not(mod(n\,50))',scale=640:-1,tile=4x3" -fps_mode vfr -frames:v 1 sheet.png
```

and, for each scene change at time T seconds (frame F = T x fps), the 24 frames from F-9 to
F+14, so that tile k (1 to 24, left to right, top to bottom) is frame F-10+k and tile 10 is the
cut frame:

```sh
ffmpeg -v error -y -i <output.mp4> -vf "select='between(n\,F-9\,F+14)',scale=480:-1,tile=6x4" -fps_mode vfr -frames:v 1 cut-T.png
```

and one strip through the first two seconds of each scene, every 5th frame, to see how the
scene fills in (S = the scene's first frame):

```sh
ffmpeg -v error -y -i <output.mp4> -vf "select='between(n\,S\,S+60)*not(mod(n-S\,5))',scale=480:-1,tile=6x3" -fps_mode vfr -frames:v 1 reveal-S.png
```

Then review. If you can start a second agent with a clean context, give it ONLY the brief,
the sheets and the eight points above, and ask for frame-numbered defects against the eight points. Do not give it your
reasons or your history. If you cannot, open every sheet yourself and answer the eight points
one by one, in writing, with the sheet and tile that shows each answer. Tell the reviewer the tile-to-frame mapping.

Fix what the look finds, re-render, run Step 3 again. Two look rounds at most.

You cannot judge sound by listening. For audio, rely on the loudness numbers from the checker
and confirm timings in code.

## Step 5 - Report

End with: the checker's last line; findings you fixed (rule, cause, edit); findings left and
why; what the look found and what you changed; the `decisions` from the contract; and what
was NOT checked (text not read, motion not watched at speed, audio not heard). Do not say
the video looks good unless you opened frames from the final file and can say what is in them.

## Where these rules come from

Each rule traces to a record or an experiment in the Agentic Media Lab hub
(https://tp9imka.github.io/agentic-media-lab/llms.txt):

- contract, checker, the look points, "do not silence a finding by changing what is fine":
  `example:clipcheck-fix-loop`, `example:hyperframes-vs-remotion`
- real transitions, type ratio, "these rules do not make a design": `example:skill-ablation-contract-first`
- easing and exit timing: `tool:heygen-com/hyperframes`, `tool:haidrrrry/claude-remotion-skill`
- clean-context reviewer, seeded randomness: `tool:vincentwei1021/video-shotcraft`
- bounded fix rounds: `tool:digitalsamba/claude-code-video-toolkit`, `tool:browser-use/video-use`
- blank frames with parallel workers: `source:github.com/heygen-com/hyperframes/issues/4435`
- loudness range and true peak: `source:tech.ebu.ch/files/live/sites/tech/files/shared/r/r128s2.pdf`
- caption limits: `source:bbc.co.uk/accessibility/forproducts/guides/subtitles`,
  `source:partnerhelp.netflixstudios.com/hc/en-us/articles/217350977-english-usa-timed-text-style-guide`
- vertical safe area: `source:facebook.com/business/ads-guide/update/video/instagram-reels`
- "an agent cannot hear": `source:github.com/remotion-dev/remotion/issues/12922`
- "never end on a job id": `source:github.com/openai/codex/issues/60616`
- everything inline and imperative, because agents skip a skill routed with "if relevant" and
  packaging strips links between files: `source:github.com/remotion-dev/remotion/pull/13133`,
  `source:vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals`

To make an agent load this skill reliably, add one line to the project's `CLAUDE.md` or
`AGENTS.md`: "Before writing or re-rendering any video, load the contract-first-video skill
and follow it to the end."
