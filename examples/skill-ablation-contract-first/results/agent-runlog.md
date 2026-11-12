2026-11-12T12:53:09Z

# RUNLOG - "Quote first" (HyperFrames + contract-first-video)

All times UTC, 2026-11-12.

## Timeline

- 12:53:09 start. Read BRIEF.md and skills/contract-first-video/SKILL.md.
- 12:53:39 `npm init -y` + `npm install hyperframes` done (hyperframes 0.9.38, local).
- 12:53-12:55 read the bundled skills: hyperframes/SKILL.md, references/format.md, references/motion.md,
  hyperframes-cli/SKILL.md, parts of references/preview-render.md and lint-validate-inspect.md.
  Also read clipcheck.py and rules.json (read only, not edited) to learn what is measured.
- 12:54:30 (about) contract.json written, before any scene.
- 12:54:58 `npx hyperframes init video --skip-skills` (project lives in `video/`).
- 12:56:18 scenes written; `npx hyperframes lint`: 0 errors, 10 warnings (all `font_face_local_only`).
- 12:56:30 `npx hyperframes check --json`: ok=true, 0 errors; 1 craft warning `film_silent`.
- 12:56:50 `npx hyperframes snapshot --at 1.5,5.5,10.5,15,18.5`; opened contact-sheet.jpg.
  Saw: all scenes mount, copy right, but type small and every scene in the left half. Enlarged the
  type scale before the first render (hero 136=>162, title 243, head 60=>72, body 46=>56, small 30=>36).
- 12:57:14 render 1. 12:57:36 checker run 1.
- 12:58:23 look sheets made (look1/), clean-context reviewer started.

## Contract as first written

See `contract.json`. Not changed since first write (no later changes).

- stream 1920x1080, 30 fps, 20.0 s +/- 0.5, h264
- palette background #0F1419, allowed #F2F4F7 #4CC38A, tolerance 30, max off-palette share 0.002
- safe_area L0.04 R0.04 T0.09 B0.09
- scenes: title 0-3, step1-source 3-8, step2-quote 8-13, step3-gate 13-17, closing 17-20
- cut_tolerance_s 0.35; motion max_abrupt_stop_share 0.34, max_still_s 4.0
- audio required=false (template loudness range kept); captions block deleted (brief has none)
- copy (11): "Quote first." / "How one claim gets into the hub" / "Open the primary source." /
  "The skill file. The licence. The pricing page." / "Copy the quote. Then write the sentence." /
  "Exits are 40-50% shorter than their entrances." / "motion.md, section Motion craft" /
  "The gate finds the quote in the saved source." / "quote-found: 147   quote-not-found: 0" /
  "No quote, no claim." / "agentic-media-lab"
- numbers_allowed: 147, 0, 40, 50

## Decisions recorded in the contract

1. Role names in the brief (Title, Subtitle, Step 1/2/3, Supporting line, Closing card, Small line) are
   not shown on screen; the brief does not say to show them, so the reading that adds no text was chosen.
2. The double quotes around each string in the brief are delimiters, not copy; no quotation-mark glyphs
   are drawn, also not around the quote in scene 3. The quote block is marked by an accent rule on its left.
3. The three spaces in "quote-found: 147   quote-not-found: 0" are kept as written (white-space: pre) on
   one monospace line.
4. No captions, no audio: captions block deleted, audio required=false, clip is silent. The HyperFrames
   rule "a film over ~15 s gets music and sound" is not followed (no media supplied, brief says no audio
   track required).
5. Safe-area margins, cut tolerance, motion limits, palette tolerance: not in the brief, the skill's
   template values used unchanged (my choice).
6. "System fonts only, no font downloads": @font-face local() (Helvetica Neue for copy, Menlo for
   scene 4) so HyperFrames does not swap them for bundled Inter or fetch from Google Fonts.
7. Secondary lines use the text colour or the accent, never a new grey.
8. The brief says stop at 30 minutes, the run instructions say 40; 30 is the target, 40 the hard stop.

## Renders and checker output

### Render 1

Command (in `video/`): `HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 npx hyperframes render --quality delivery -o ../out/final.mp4`
Time: 13.0 s wall (tool reports "rendered in 10.8s", 8 workers, screenshot capture, hardware gpu).

Checker: `python3 skills/contract-first-video/clipcheck/clipcheck.py out/final.mp4 --contract contract.json --ocr --json clipcheck.json`

```
ERROR   copy: 3 of 11 contract strings were not read in any sampled frame: 'How one claim gets into the hub'; 'quote-found: 147   quote-not-found: 0'; 'agentic-media-lab'
ok      stream: 1920x1080 30 fps 20.00 s h264
ok      colour-tags: bt709/bt709/bt709
ok      first-frame: presence 0.064
ok      empty-frames: lowest mid-clip content 0.0170
ok      sparse-frames: typical content 0.0539
ok      palette: peak off-palette share 0.0000
ok      safe-area: margins L0.04 T0.09 R0.04 B0.09 held
ok      scene-times: 4 scene changes fall on motion
ok      abrupt-stops: 0 of 5 moves stop dead
ok      long-hold: no hold over 4 s
ok      stray-numbers: only contract numbers were read
CLIPCHECK: FAIL (1 errors, 0 warnings)
```

#### The `copy` finding: suspected false positive, not "fixed"

Cause is in the OCR, not the source. Evidence:

- Opened full frames at 2.0 s and 15.5 s from out/final.mp4: the subtitle reads
  "How one claim gets into the hub", the mono line reads "quote-found: 147   quote-not-found: 0".
- Reproduced the checker's OCR (`negate`, `tesseract --psm 11`) on the full frame:
  2.0 s => "Quote first.  aim get  b"; 15.5 s => "... quote-found: 147  quote-not-found: @";
  19.0 s => "No quote, no claim.  age tic edia lab".
- Same frames cropped to the line, `--psm 7`: subtitle => "How one claim gets into the hub" (correct);
  small line (2x upscale) => "agentic-media-lab" (correct); mono line => "quote-found: 147 quote-not-found: @".
- So: (a) full-frame sparse OCR loses a 56 px line under a 243 px title and a 36 px accent line under a
  162 px title; (b) Menlo's slashed zero is read as "@".

Per Step 3 ("do not change a part of the clip that is fine in order to silence it") no edit was made for
this at this point.

### Render 2 (after look round 1)

Same command. 12.65 s wall ("rendered in 9.9s"). Before it: `npx hyperframes check --json` ok=true, 0 errors,
craft warning film_silent only.

Checker: identical to render 1 - one finding line
`ERROR   copy: 3 of 11 contract strings were not read in any sampled frame: 'How one claim gets into the hub'; 'quote-found: 147   quote-not-found: 0'; 'agentic-media-lab'`
all other rules ok (empty-frames lowest content 0.0184, sparse typical 0.0574, abrupt-stops 0 of 5).
Last line: `CLIPCHECK: FAIL (1 errors, 0 warnings)`

### Render 3 (after look round 2) - the delivered file

Same command. 24.95 s wall ("rendered in 21.7s"). `check --json` before it: ok=true, 0 errors, film_silent only.

Checker: same single finding (copy, same 3 strings); ok lines: stream 1920x1080 30 fps 20.00 s h264;
colour-tags bt709/bt709/bt709; first-frame presence 0.064; empty-frames lowest mid-clip content 0.0142;
sparse-frames typical 0.0517; palette peak off-palette 0.0000; safe-area held; scene-times 4 changes on
motion; abrupt-stops 0 of 5; long-hold none over 4 s; stray-numbers only contract numbers.
Last line: `CLIPCHECK: FAIL (1 errors, 0 warnings)`

ffprobe out/final.mp4: h264, 1920x1080, yuv420p, 30/1, nb_frames 600, duration 20.000000.

| render | errors | warnings | findings |
|---|---|---|---|
| 1 | 1 | 0 | copy (3 strings unread by OCR) |
| 2 | 1 | 0 | copy (same) |
| 3 (delivered) | 1 | 0 | copy (same) |

## Fixes

Checker findings fixed: none. The only finding (copy) is left as a suspected false positive, see above.
Fix rounds used for the checker: 0 of 4.

Pre-render fix (from HyperFrames snapshot, before render 1): type too small, all scenes in the left half
=> type scale enlarged in the shared CSS of compositions/*.html.

## Look step

Sheets: look1/ (render 1), look2/ (render 2), look3/ (render 3, delivered): sheet.png + cut-3/8/13/17.png each,
made by mksheets.sh (the skill's two ffmpeg commands). look/ holds a failed first attempt (four identical,
mis-named cut sheets from a zsh word-splitting mistake; a removal was blocked by the harness, files left).

### Round 1 - clean-context sub-agent (given only BRIEF.md, the 5 sheets of look1/, the six points)

1. stacked texts: NO (all four cut sheets: outgoing only in tiles 1-8, incoming only in tiles 9-23).
2. sliding across: NO (only small upward drift; within-scene reveals not covered by tiles).
3. dim/blurred at a cut: YES per reviewer - outgoing scene dim and blurred in tiles 7-8 of every cut sheet
   (frames 88-89, 238-239, 388-389, 508-509). My reading: this is the 0.27 s exit itself, not an incoming
   element; not changed.
4. unlisted text: NO added strings. Noted: sheet tile 4 (frame 150) shows "The skill file. The licence."
   without the third sentence (staged reveal); hyphen vs en dash in the mono line not decidable at sheet scale.
   Source uses U+002D; full-res frame at 15.5 s shows Menlo's long hyphen.
5. half the frame empty: YES - content in one band of about 240-400 px height; scene 2 heading-only frame 100
   (sheet tile 3, cut-3 tiles 9-23) ends at about 54% width.
6. clipped glyphs in a wipe: NO (no wipes).
Other: (a) scenes heading-only for long stretches (sheet tiles 3, 6, 9; cut-17 tiles 9-21); (c) rule missing
on cut frames 90/240/390 (tile 9); (d) step heading at y 500 / 459 / 480 in scenes 2/3/4; (e)(f) title and
closing moves (the designed entrances); (g) small text about 33-35 px.

Changed because of it (render 2):
- (d) step scenes: column anchored to the top (justify-content flex-start + fixed padding-top) instead of
  vertical centring, so all three step headings share one y.
- (c) step rule no longer draws on from scaleX 0; it is full length on the cut frame and rises with the heading.
- (a) reveals earlier: step1 sentences 0.45 s + 0.5 s stagger (was 0.7 + 0.8); step2 bar 0.4, quote 0.6,
  label 1.3 (was 0.6 / 0.85 / 2.0); step3 mono halves 0.45 + 0.5 stagger, underline 1.5 (was 0.8 + 0.6, 2.0);
  closing rule 0.2, small line 0.5 (was 0.4 / 0.8); title rule 0.15, subtitle words 0.45 (was 0.3 / 0.7).
- (5) gap between heading and evidence raised to 150 px so the block spans more of the height.

### Round 2 - me, on look2/ (sheet.png, cut-8.png, cut-13.png)

1. NO - cut-8 and cut-13: tiles 1-8 outgoing only, tiles 9-23 incoming only.
2. NO - cut-8 tiles 9-12: heading and rule rise together, nothing crossed.
3. Incoming: NO - cut-8 tile 9 (frame 240), cut-13 tile 9 (frame 390): heading and rule sharp, full brightness.
   Outgoing dim in tiles 7-8 as before (exit).
4. NO - sheet tiles 1-12: every string matches the contract, one line each, no labels, no quote marks.
5. YES, still - sheet tiles 3-11: step block sat in the top 55%, bottom 40% empty.
6. NO - no wipes.
Changed (render 3): step column padding-top 150 => 240 px, block now spans y 348-770 (checked at 11.0 s).

Two look rounds used (the maximum). After render 3 I opened look3/sheet.png, look3/cut-17.png and the full
frame at 11.0 s as verification only, not a third round.

## Skill instructions not followed, and why

contract-first-video:
- Step 3 "fix every ERROR": the copy error was not fixed; it is reported as a suspected false positive
  (the same step says not to change a fine clip to silence a finding). Final checker line is FAIL.
- Step 1 "show the contract to the user": no user present.

HyperFrames:
- Usage beacons (`npx hyperframes events --skill=...`), `usage --json`, `feedback --rating`: skipped
  (run rule: no telemetry/usage/feedback commands).
- `npx hyperframes skills update`: not run (run rule); bundled skills read from node_modules.
- `init ... --skill=hyperframes`: flag dropped (looked like usage attribution); `--skip-skills` kept.
- "A film over ~15 s gets music and sound": skipped (brief: no audio required; no media). check warns film_silent.
- story.md three storylines / SPEC.md / REVIEW.md / `snapshot --review`: skipped; the brief fixes the
  content and contract.json + the contract-first look step took their place.
- Studio preview before the delivery render, `history begin/end`, Framey hand-off line: skipped (no person).
- "Copy, brand colours are variables (data-var-text)": not done; copy and colours are literals in the scenes.
- Bundled fonts: not used; @font-face local() instead (brief: system fonts). Lint warns font_face_local_only x10.
- Registry search before hand-writing transitions: not done (would be a network lookup; transition is a plain
  exit/enter).
- motion.md transitions "3-5 kinds": one kind used (exit up with blur/fade, new heading rises in at the cut).
- GSAP still loads from the jsdelivr CDN, as the scaffold writes it. Not verified whether the render used a
  cached copy or the network.

## Blocked / surprised / unclear in contract-first-video

- The copy rule OCRs the full frame with `--psm 11`. It lost a 56 px line under a 243 px title, a 36 px
  accent line under a 162 px title, and reads Menlo's slashed zero as "@". The same lines OCR correctly when
  cropped (`--psm 7`), except the slashed zero. The skill gives no way to record an accepted false positive, so
  the final line stays FAIL although the clip matches the copy list.
- "Do not silence a finding" vs "fix every ERROR" leaves the final status ambiguous: is FAIL with a
  documented false positive deliverable?
- Look point 3 does not say whether it covers the outgoing scene. The reviewer flagged the exit's last two
  frames at every cut; the skill itself asks for an exit that ends at the cut.
- Look point 5 does not define "half": the reviewer counted vertical emptiness of a centred text layout.
- Step 4's cut-sheet command makes 23 tiles in a 6x4 grid; tile 24 is black and the tile-to-frame mapping is
  not stated (I had to tell the reviewer: tile k = frame F-9+k).
- The sheets sample every 50th frame, so within-scene reveals are never seen by the reviewer (it said so).
- The scene-times rule passed although my transition is a 0.27 s exit plus an entrance; the skill does not
  say what counts as a transition.
- clipcheck prints "why:" provenance but `rules.json` says it resolves quotes from index/records.jsonl, which
  is not shipped beside the skill; nothing told me whether that matters.
- BRIEF.md says stop at 30 min, the run prompt 40.
- My own slip: the first sheet loop relied on zsh word splitting and produced four identical sheets.

## End

End: 2026-11-12T13:03:01Z. Start 2026-11-12T12:53:09Z. 3 renders, 2 look rounds (1 sub-agent, 1 me).
Status: delivered out/final.mp4, checker FAIL (1 errors, 0 warnings) on a suspected OCR false positive.
