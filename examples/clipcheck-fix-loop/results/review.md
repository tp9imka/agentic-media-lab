# Blind before and after review

Clip A was the clip after the fix loop. Clip B was the clip before it. The reviewer saw only the labels A and B, and a brief with the tool names removed.
One reviewer agent, one clip each, judged from stills and per-frame scans. This is a judgement, not a measurement.

## Scores

| Criterion | A | A evidence | B | B evidence |
|---|---|---|---|---|
| 1. Copy exact | 1 | All brief strings present and spelled as written (`A-frames/f005.png`, `f025.png`, `f033.png`, `f039.png`, `A-sheet.png`). Deviations: on-screen labels "Step 1", "Step 2", "Step 3" added above the headlines (`f025.png`, `f033.png`, `extra/A_s2reveal_strip.png`); step 2 and step 3 headlines broken over two lines. No transient value: the count appears as 147 from its first frame (`extra/A_s4reveal_strip.png`). | 1 | Same strings, same added "Step N" labels and line breaks (`B-sheet.png`, `extra/B_s2reveal_strip.png`). Additional deviation: the count runs through numbers the brief does not contain - 20, 38, 54, 69, 82, 93, 103, 112, 120, 126, 131, 135, 139, 142, 144, 145, 146 - for n418-n433, about 0.53 s (`extra/B_s4reveal_strip.png`, `B-frames/f029.png` shows "quote-found: 54"). |
| 2. Hierarchy and type | 2 | Three clear levels: title/closing headline, step headlines, supporting lines; label and source line dimmed. Sans for copy, monospace for the counter line (`f005.png`, `f025.png`, `f033.png`, `f039.png`, `extra/A_n384.png` at full res: label about 48 px, quote about 52 px, headline about 100 px). | 2 | Settled frames are visually the same as A (`B-sheet.png`, `extra/B_end_strip.png`, PSNR scan: settled stretches identical or > 60 dB). |
| 3. Alignment and safe area | 1 | One left edge (text x about 250 px, accent bar x about 192-204 px, bar 108-972 px vertically) in every scene, nothing near the frame edge (`f005.png`, `f025.png`, `f033.png`, `f039.png`). Unbalanced: right 40-55% of the frame is empty in scenes 1, 2, 4, 5 and the lower third is empty in scenes 2 and 4 (`f033.png`, `f039.png`, `A-sheet.png`). | 1 | Same layout, same imbalance (`B-sheet.png`, `B-frames/f029.png`). |
| 4. Palette obeyed | 1 | Decoded modes: background `#0d1316`, text `#f0f3f6`, accent `#4ac188`/`#4bc289` - each about 2 levels under the brief values, same hue. No other hue (only green-dominant saturated pixels found), no gradient. Minor deviation: quote block panel is a lighter grey `#1a2025` (444k px at 12.0 s, `f025.png`, `extra/A_n384.png`). | 1 | Same values and the same `#1a2025` panel (histograms at 2, 7, 12, 16, 19 s; `B-sheet.png`). |
| 5. Entrances and transitions | 2 | Every scene has an entrance: bar draw + word-by-word title (`extra/A_start_strip.png`), blur/fade handovers at 3 s and 8 s with the incoming headline already on screen (`extra/A_cut3_strip.png`, `extra/A_cut8_strip.png`, `A-frames/f007.png`), slide + blur at 13 s (`extra/A_cut13_strip.png`, `f027.png`), accent wipe at 17 s (`extra/A_cut17_strip.png`). No text-free frame anywhere in the clip (scan). | 1 | Same set of entrances and the same 17 s wipe (`extra/B_cut17_strip.png`), but three joins leave text-free frames with only the accent bar: n89-n91 (2.97-3.03 s), n239 (7.97 s), n390 (13.00 s) (`extra/B_cut3_strip.png`, `extra/B_cut8_strip.png`, `extra/B_cut13_strip.png`, `B-frames/f007.png`, `B-frames/f027.png`). |
| 6. Nothing clipped, overlapping or broken | 1 | One instance: at 12.8-12.9 s the outgoing step 2 block (headline and quote panel) slides left across the accent bar, text and bar overlap (`extra/A_cut13_strip.png`, row 2 cells 1-3). Mid-glyph cuts during the supporting-line wipe last 1 frame each (`extra/A_s2reveal_strip.png`) - not counted. | 0 | Several: the same bar overlap at 12.8-12.9 s (`extra/B_cut13_strip.png`); 5 text-free frames mid-video (n89-n91, n239, n390); dimmed second line "Then write the sentence." sits alone, without label or first line, for n240-n244 (`extra/B_cut8_strip.png`, `extra/B_n242.png`); mid-glyph cut letters visible for 3-4 consecutive frames per sentence (`extra/B_s2reveal_strip.png`). Each is brief; counted as several minor. |

**Totals: A 8 / 12, B 6 / 12.**

## Differences between A and B

Frames outside the windows below decode identically or differ by less than visible encoder noise (PSNR > 60 dB). The first 1.8 s and 17.0-20.0 s are the same in both.

| # | Time | What differs | Frames | Verdict |
|---|---|---|---|---|
| 1 | 2.83-3.03 s | B starts the title exit about 2 frames earlier and finishes it, leaving 3 frames with only the bar. A overlaps: the incoming headline is already there at n90-n91, but blurred and dim (max luma 72), not readable. | `extra/A_cut3_strip.png`, `extra/B_cut3_strip.png`, `A-frames/f007.png`, `B-frames/f007.png` | A better (no empty frame). A's own cost: an unreadable ghost headline for 2 frames. |
| 2 | 3.07-3.40 s | Step 1 headline entrance. A: whole line present from the start, words sharpen and brighten left to right, complete by about n98 (3.27 s). B: label alone for n92-n94, then words appear one at a time from nothing, complete at n102 (3.40 s). | same strips, rows 2-4 | A better: line length is stable and the headline is readable about 0.13 s sooner. B holds 3 frames with only a faint "Step 1". |
| 3 | 4.23-4.33 s, 4.93-5.03 s, 5.63-5.80 s | Supporting-line sentences. A: each sentence wipes in over about 2 frames. B: each wipes in over 4-5 frames, with cut-off letters ("fil", "licer", "pag") visible on several consecutive frames. | `extra/A_s2reveal_strip.png`, `extra/B_s2reveal_strip.png`, `B-sheet.png` cell 4 ("The licenc") | No clear verdict from stills. A has fewer half-letter frames but a 2-frame reveal may be too fast to register as motion; B's reveal is long enough to register but shows clipped glyphs longer. |
| 4 | 7.83-8.23 s | Step 1 => step 2. A: one frame (n240) with the dim second line alone, label and first line in by n241-n242. B: one text-free frame (n239), then the dim second line alone for 5 frames (n240-n244), first line arrives blurred at n245, sharp at n247. | `extra/A_cut8_strip.png`, `extra/B_cut8_strip.png`, `extra/B_n242.png` | A better. In B the secondary line is on screen without its primary line for about 0.17 s. |
| 5 | 12.77-12.87 s | Tiny luminance difference in the slide-out (PSNR 56 dB). | `extra/A_cut13_strip.png`, `extra/B_cut13_strip.png` row 2 | No visible difference. |
| 6 | 13.00-13.30 s | Step 3 entrance. A: incoming block already visible at n390 (faint, heavily blurred, unreadable). B: n390 text-free, block appears one frame later and stays dimmer for a few frames. | same strips, `A-frames/f027.png`, `B-frames/f027.png` | A marginally better (no empty frame). In both the block is unreadable for about 4 frames. |
| 7 | 13.93-14.47 s | Counter. A: "147" fades in directly. B: number counts up through 17 intermediate values to 147. | `extra/A_s4reveal_strip.png`, `extra/B_s4reveal_strip.png`, `B-frames/f029.png` | A better against the brief (no text outside the copy table). B has more motion on the one data point, at the cost of copy exactness. |

## Three most important defects per clip

**A**
1. Outgoing step 2 block slides through the accent bar at 12.8-12.9 s, text over bar - `extra/A_cut13_strip.png`, `A-frames/f027.png`.
2. Added "Step 1/2/3" labels and a grey `#1a2025` quote panel, neither in the brief - `A-frames/f025.png`, `A-frames/f033.png`.
3. Left-weighted layout leaves the right half empty in four of five scenes - `A-frames/f005.png`, `A-frames/f033.png`, `A-frames/f039.png`.

**B**
1. Counter shows 17 numbers that are not in the brief (20 ... 146) - `extra/B_s4reveal_strip.png`, `B-frames/f029.png`.
2. Text-free frames at three joins (n89-n91, n239, n390) and an orphaned dim second line for 5 frames at 8.0-8.13 s - `B-frames/f007.png`, `B-frames/f027.png`, `extra/B_cut8_strip.png`, `extra/B_n242.png`.
3. Same bar overlap at 12.8-12.9 s, plus the added labels, grey panel and left-weighted layout it shares with A - `extra/B_cut13_strip.png`, `B-sheet.png`.

## Not judgeable from stills

- Easing, pacing and overall feel of any move; whether A's 2-frame sentence wipes and B's 1-3 frame gaps register at playback speed or read as flicker.
- Whether the blur on incoming headlines reads as intentional focus-pull or as softness.
- Audio (none required), playback smoothness, codec profile (only resolution, frame rate and frame count were probed: 1920x1080, 30 fps, 600 frames, both).
- Exact source colours: sampled values are after video encoding, about 2 levels below the brief's hex values in both clips; I cannot tell encoding shift from authoring.
- Which fonts are installed system fonts.

## Frames opened

- Sheets: `A-sheet.png`, `B-sheet.png`.
- `A-frames`: `f005.png`, `f007.png`, `f025.png`, `f027.png`, `f033.png`, `f039.png`.
- `B-frames`: `f007.png`, `f027.png`, `f029.png`.
- `extra/` strips (every frame, 24 per cut): `A_cut3_strip.png`, `B_cut3_strip.png`, `A_cut8_strip.png`, `B_cut8_strip.png`, `A_cut13_strip.png`, `B_cut13_strip.png`, `A_cut17_strip.png`, `B_cut17_strip.png`.
- `extra/` other: `A_start_strip.png` (n0-n14), `A_end_strip.png`, `B_end_strip.png` (n585-n599), `A_s2reveal_strip.png`, `B_s2reveal_strip.png` (n126-n131, n147-n152, n168-n175), `A_s4reveal_strip.png`, `B_s4reveal_strip.png` (n416-n435), `A_n384.png`, `B_n242.png` (full res).
- Not opened as images, covered numerically: `B_start_strip.png` (n0-n55 decode identical to A), remaining `f0xx.png` frames (PSNR scan), `extra/psnr.log`.
