# Blind review

Clip A was the Remotion arm and clip B was the HyperFrames arm. The reviewer saw only the labels A and B.
The brief it was given names both toolchains, so it knew which two stacks were compared, not which clip was which.
One reviewer agent, one clip per arm, judged from stills. This is a judgement, not a measurement.

## Scores

| Criterion | A | A evidence | B | B evidence |
|---|---|---|---|---|
| 1. Copy exact | 1 | All strings present and spelled as briefed (`A-frames/f005.png`, `f015.png`, `f025.png`, `f033.png`, `f039.png`). Deviation: the supporting line "The skill file. The licence. The pricing page." is broken into three stacked lines (`A-frames/f015.png`). No "Step N" labels and no quote marks around the quote - consistent with reading the brief's quote marks and "Step 1:" as delimiters/roles. Full stops of title and closing card are recoloured green, text unchanged. | 1 | All strings present and spelled as briefed (`B-frames/f005.png`, `f015.png`, `f025.png`, `f033.png`, `f039.png`). Deviations: "Step 1", "Step 2", "Step 3" shown as on-screen labels (`B-frames/f015.png`, `f025.png`, `f033.png`) while "Title"/"Subtitle" are not, and literal straight quote marks added around the quote only (`B-frames/f025.png`). The counter also shows values that are not in the brief while it runs: "quote-found: 54" (`B-frames/f029.png`), "112" (`B-sheet.png`, tile 9). |
| 2. Hierarchy and type | 2 | Two clear levels in every scene, large heavy sans headline over regular-weight support; mono line clearly a different face (`A-frames/f033.png`); smallest text (label in `f025.png`, small line in `f039.png`) is about 40 px tall at 1080p, readable. | 2 | Three clear levels: grey step label, bold headline, support line (`B-frames/f015.png`, `f033.png`); mono line distinct; smallest text about 40 px at 1080p (`B-frames/f039.png`, `f025.png`), readable. |
| 3. Alignment and safe area | 2 | Left edge constant at x = 142 px in all five settled scenes, content never beyond x = 1711 or outside y = 239-840 (measured on frames at 2, 6.5, 11.5, 15.5, 19 s). Blocks vertically centred. Left-weighted: title scene leaves the right third empty (`A-frames/f005.png`). | 2 | Persistent accent bar at x = 192 px, y = 108-971, text edge constant at x = 254 px in all scenes, content never beyond x = 1617 (same five timestamps). Blocks vertically centred beside the bar. Left-weighted: right third mostly empty in scenes 1 and 5 (`B-frames/f005.png`, `f039.png`). |
| 4. Palette obeyed | 2 | Sampled: background #0D1318, text #EFF2F5, accent #4AC188 - within a few levels of spec (plausible encode drift). No other hues, no gradients, corners and centre identical. Only the three colours in settled frames (`A-frames/f025.png`, `f033.png`). | 1 | Sampled: background #0D1316, text #F0F3F6, accent #4AC188 - within encode drift. Extra tones: quote block is a filled panel #1A2025 (`B-frames/f025.png`), and secondary text is a neutral grey #979DA1 (`B-frames/f005.png`, `f015.png`, `f039.png`). No other hues, no gradients. |
| 5. Entrances and transitions | 2 | Every scene has staggered entrances (rule draws, lines arrive in sequence, quote bar grows: `A-sheet.png` tiles 3-4 and 6-7). Cuts: dissolve at 3 s (`A-frames/f007.png`, `extra/A-fr3.png`), horizontal push at 8 s and 13 s (`A-frames/f017.png`, `f027.png`, `extra/A-fr8.png`, `extra/A-fr13.png`), dissolve at 17 s (`A-frames/f035.png`, `extra/A-fr17.png`). No hard cut, no empty frame at any cut. | 1 | Every scene has an entrance (bar draws down, word-by-word reveal: `extra/B-ends.png`, `extra/B-fr3.png`). Cuts at 3 s, 8 s, 13 s are a fast exit to a bar-only frame, then the next entrance: `B-frames/f007.png` and `B-frames/f027.png` show nothing but the bar; `B-frames/f017.png` shows only a dimmed "Then write the sentence." with no label and no first line, which reads as unfinished. Cut at 17 s is a full-frame accent wipe and looks intentional (`B-frames/f035.png`, `extra/B-fr17.png`). |
| 6. Nothing clipped, overlapping or broken | 1 | Settled frames are clean. One kind of defect, at both dissolves: outgoing and incoming headlines are superimposed and illegible for about 5 frames ("Open the primary source." over "Quote first." in `extra/A-fr3.png` tiles 5-8; "No quote, no claim." over the gate headline in `extra/A-fr17.png` tile 7, also `extra/A-cuts-13-17.png` tile 10). Falls between the supplied 0.5 s frames. | 1 | Settled frames are clean, nothing clipped. Transitional defects: bar-only frames mid-video for 3 frames at 2.97-3.03 s and 1 frame each at 7.97 s and 13.0 s (`B-frames/f007.png`, `f027.png`); half-rendered state at 8.0 s (`B-frames/f017.png`); at the 13 s exit the text block slides left across the accent bar, bar drawn through the text (`extra/B-fr13.png` tiles 1-5). Several, each minor and short, none in a settled frame. |

## Totals

- A: 10 / 12
- B: 8 / 12

## Three most important defects per clip

A
1. Both dissolves stack two headlines on the same spot, unreadable for about 0.15 s each - `extra/A-fr3.png` (frames 93-95), `extra/A-fr17.png` (frame 515).
2. Supporting line of scene 2 restructured into three lines instead of the one line briefed - `A-frames/f015.png`.
3. The clip opens on 7 empty background frames (0.0-0.2 s), so the first frame / thumbnail is blank - `A-frames/f001.png`.

B
1. Scene changes at 3 s, 8 s and 13 s pass through a frame with only the accent bar, and the 8.0 s frame shows a lone dimmed second line - `B-frames/f007.png`, `B-frames/f017.png`, `B-frames/f027.png`.
2. Text added beyond the brief: "Step 1/2/3" labels and quote marks around the quote - `B-frames/f015.png`, `B-frames/f025.png`, `B-frames/f033.png`.
3. Palette: grey filled quote panel (#1A2025) and grey secondary text (#979DA1) on top of the three briefed colours - `B-frames/f025.png`.

## Not scored: timing and other notes

Timing. Both clips are 1920x1080, 30 fps, 600 frames, 20.0 s, H.264 (ffprobe). Both change scene at 3.0, 8.0, 13.0 and 17.0 s within about 0.2 s, so every scene sits in its slot. Neither has an exit on the last card; both hold it to 20.0 s.
- A: scene content is fully on screen by about 0.8, 5.5, 10.0, 14.3 and 18.0 s.
- B: scene content is fully on screen by about 1.0, 6.0, 11.0, 15.0 and 18.0 s. The counter in scene 4 only reaches 147 / shows "quote-not-found: 0" at about 15.0 s, leaving under 2 s to read the final line.

Other things a professional would flag.
- A: headline tracking is very tight, letters nearly touch (`A-frames/f015.png`, `f033.png`). The quote is set in italics with a left rule and no quote marks; both mono numbers are accent-coloured. Two different transition types are used (dissolve, push, push, dissolve).
- B: the count-up shows false intermediate figures (54, 112) for a line that reports a verification result (`B-frames/f029.png`). Blur-in reveals mean several sampled frames have visibly blurred text (`extra/B-fr3.png`, `extra/B-fr13.png`). The quote panel appears at full height with empty space where the label later lands (`B-frames/f019.png`). First frame has a dimmed title and no bar yet (`B-frames/f001.png`). In scene 4 "147" is accent and "0" is white.
- Both: the mono face renders the hyphens in "quote-found" as long dashes (`A-frames/f033.png`, `B-frames/f033.png`). Both layouts are left-weighted.
- Brief ambiguity that affects criterion 1: it is not clear whether "Step N" is on-screen copy or a role name like "Title:". Under either reading each clip has one deviation, so the scores do not depend on it.

## What I could not judge from stills

- Easing, speed and overall feel of the motion; whether the dissolves and the fast exits read as smooth or abrupt at playback speed.
- Flicker or one-frame glitches other than empty frames. I counted non-background pixels on all 600 frames of each clip at 480x270, which catches empty frames but not subtle errors.
- Exact source colours. Sampled values are 2-3 levels off spec in both clips, which fits encoding; I cannot tell whether the source values were exact.
- Which font families were used, and so whether they are system fonts as briefed.
- Compression artefacts in motion, and audio (not required).

## Frames opened

Supplied:
- `A-sheet.png`, `B-sheet.png`
- `A-frames/`: f005, f015, f025, f033, f039 at 960 px; f001, f002, f007, f008, f017, f018, f019, f027, f028, f029, f035, f036 as a tiled sheet (`extra/A-named.png`)
- `B-frames/`: f005, f015, f025, f033, f039 at 960 px; f001, f002, f007, f008, f017, f018, f019, f027, f028, f029, f035, f036 as a tiled sheet (`extra/B-named.png`)

Extracted by me (640 px tiles, all in `extra/`):
- `A-cuts-3-8.png`, `A-cuts-13-17.png`, `B-cuts-3-8.png`, `B-cuts-13-17.png` - 0.2 s steps from 0.4 s before to 0.6 s after each cut
- `A-ends.png`, `B-ends.png` - 0.0, 0.2, 0.4, 0.6, 19.6, 19.9 s
- `A-fr3.png` (frames 86-98), `A-fr8.png` (234-250), `A-fr13.png` (384-400), `A-fr17.png` (504-522)
- `B-fr3.png` (86-99), `B-fr8.png` (236-250), `B-fr13.png` (385-394), `B-fr17.png` (500-518)

Numeric checks: per-frame non-background pixel counts for all 600 frames (`extra/A-cov.txt`, `extra/B-cov.txt`); colour histograms and content bounding boxes at 2, 6.5, 11.5, 15.5 and 19 s at full resolution.
