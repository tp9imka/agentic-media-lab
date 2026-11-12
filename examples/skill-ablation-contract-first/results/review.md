# Blind review: vendor skills only against vendor skills plus contract-first-video

Clip A was the vendor-skills-only clip from the first example. Clip B was the clip made with the added skill. The reviewer saw only the labels A and B, and a brief with the tool names removed.
One reviewer agent, one clip each, judged from stills and pixel measurements. This is a judgement, not a measurement.


Both clips probe as 1920x1080, 30 fps, 600 frames, H.264, no audio. Frame numbers `nNNN` are zero-based video frames (n090 = 3.0 s). Strip files are 5-column tiles in `extra/`; tile k of a cut strip is frame start+k-1 (cut3 starts n081, cut8 n231, cut13 n381, cut17 n501; start n000; end n585). Mid-scene strips step 5 frames.

## Scores

| Criterion | A | A evidence | B | B evidence |
|---|---|---|---|---|
| 1. Copy exact | 1 | Counter shows values not in the brief: "quote-found: 54", then 112, 139 (`A-frames/f029.png`, `extra/A_strip_s4mid.png` tiles 4-6). Also: "Step 1/2/3" role labels shown while no other role label is shown (`extra/A_full_n225.png`, `A_full_n075.png`); quote marks only on the quote block (`extra/A_full_n375.png`); two headlines broken into two lines (`A_full_n375.png`, `A_full_n495.png`). All strings present and spelled correctly. | 2 | All ten strings present as written, each on one line, no role labels, no quote marks anywhere (consistent), no transient values - the 147 and 0 appear as final values (`B-frames/f029.png`, `extra/B_strip_s4mid.png`, `extra/B_full_n075/225/375/495/595.png`). |
| 2. Hierarchy and type | 2 | Four clear levels: dim label, large bold headline, regular support, dim small line. Headline is large and comfortable (`extra/A_full_n225.png`, `A_full_n495.png`, `A_full_n595.png`). | 1 | Title and closing cards are strong (`extra/B_full_n075.png`, `B_full_n595.png`). In the three step scenes the bold headline and the supporting line are close in size, separated mostly by weight (`extra/B_full_n225.png`, `B_full_n375.png`); in scene 4 the all-green mono line competes with the headline (`B_full_n495.png`). "agentic-media-lab" is the smallest text in either clip, about 30 px, in green (`B_full_n595.png`). Readable, but flatter. Borderline 1/2. |
| 3. Alignment and safe area | 2 | Rail at x=192, y=108-971 and text edge at x=252 in every scene; right edge max x=1727. Content block is vertically centred, so the label/headline top moves between scenes (y about 350, 155, 250 in `A_full_n225/375/495.png`). Frame well filled. | 2 | Left edge x=192 in every scene; accent bar y=348 and headline top y=415 identical across the three step scenes (`B_full_n225/375/495.png`). Nothing near an edge (max x=1682). Step scenes leave the lower and right parts of the frame unused. |
| 4. Palette obeyed | 1 | Quote panel is a fourth flat colour, sampled (26,32,37), about 444k px (`extra/A_full_n375.png`, `extra/A_strip_s3mid.png`). Otherwise bg/text/accent only; greys are the text colour dimmed. No gradients, no off-hue pixels in sampled frames. One full-accent frame during the wipe (n510, `extra/A_strip_cut17.png` tile 10) - accent, not a new hue. | 2 | Only background, text and accent plus dimmed versions during fades (`extra/B_full_n*.png`, all cut strips). No panel, no gradient, no off-hue pixels in sampled frames. |
| 5. Entrances and transitions | 2 | Every scene enters with animation and every change is a designed transition: blur-fade out, short hold on the rail, staggered fade-in at 3 s and 8 s (`extra/A_strip_cut3.png`, `A_strip_cut8.png`); blurred horizontal push at 13 s (`A_strip_cut13.png`); full-frame accent wipe at 17 s (`A_strip_cut17.png`). Rail draws on in the first 0.2 s (`A_strip_start.png`). Rail-only frames n089-n091 and n239 are brief and the rail persists, so not scored as empty. | 1 | Same move at all four changes: a 4-frame blur/fade/rise of the old scene that stops at about a third brightness (n089, n239, n389, n509), then the new headline is on screen at full opacity on the very next frame and only settles upward about 44 px over 6 frames (`extra/B_strip_cut3/cut8/cut13/cut17.png` tiles 9-10; measured max luminance 85-92 => 246 in one frame). Frame n000 also starts with the title at full opacity (`extra/B_strip_start.png`). Secondary elements do animate in (bar draw, word and sentence reveals, underline draw). Reads as cuts with a short settle. |
| 6. Nothing clipped, overlapping or broken | 1 | During the 13 s push the outgoing text and panel slide across the fixed rail: rail cuts through "Step 2" / "Copy" / the quote (n386-n388) and text reaches the frame edge at n389 (`extra/A_strip_cut13.png` tiles 6-9). Minor: at 8 s the dim second line "Then write the sentence." is on screen alone before the first line (n240-n244, `A_strip_cut8.png` tiles 10-14). Transient, a few frames each. | 2 | No clipped text, collisions or empty frames found in any strip. |

**Totals: A 9 / 12, B 10 / 12.**

Note on colour values: decoded background samples as (13,19,22), text (240,243,246), accent (74,193,136) in both clips, against spec (15,20,25), (242,244,247), (76,195,138). The shift is identical in both, so I did not score it.

## Defects - clip A

1. Counter runs through 54 / 112 / 139 before 147 - numbers the brief does not contain (`A-frames/f029.png`, `extra/A_strip_s4mid.png` tiles 4-6).
2. Outgoing scene 3 slides over the static rail at 13 s; rail and text collide for 3 frames, text touches the frame edge (`extra/A_strip_cut13.png` tiles 6-9).
3. Quote panel adds a grey-blue tint outside the three-colour palette (`extra/A_full_n375.png`).
4. "Then write the sentence." sits at very low contrast for about 3 s (n240 to about n320) and appears before line one at the cut; in stills the scene reads half-lit (`extra/A_strip_cut8.png`, `A_strip_s3mid.png` tiles 1-13, `A-sheet.png` tiles 6-7).
5. Role labels are inconsistent: "Step N" shown, no label on title or closing; quote marks on one string only (`A_full_n225.png`, `A_full_n375.png`). Lesser: headline top position differs per scene (`A_full_n225/375/495.png`). Both partly taste.

## Defects - clip B

1. Scene changes are effectively cuts: old scene dropped mid-fade, new headline at full opacity in one frame (`extra/B_strip_cut3.png` tiles 9-10, same in cut8/cut13/cut17).
2. Opening frame has the title already fully visible; only a small rise (`extra/B_strip_start.png` tiles 1-5).
3. Step scenes: headline and support too close in size; composition sits in a band with the lower third empty (`extra/B_full_n225.png`, `B_full_n375.png`). Partly taste.
4. Small lines are small and in green: "agentic-media-lab" about 30 px, "motion.md, section Motion craft" about 36 px (`B_full_n595.png`, `B_full_n375.png`).
5. Plain and repetitive: same layout and same transition four times, scene 4 line all in accent so the 147 is not singled out (`B-sheet.png`, `B_full_n495.png`). Taste, not a fault.

## Differences

| # | Difference | Verdict |
|---|---|---|
| 1 | Copy fidelity: A adds count-up values, "Step N" labels, quote marks on the quote, two-line headlines; B shows the strings bare (`A-frames/f029.png` vs `B-frames/f029.png`). | B better |
| 2 | Scene transitions: A has three designed transitions with full exits and staggered entrances; B drops the old scene mid-fade and cuts the new headline in (`A_strip_cut3/13/17.png` vs `B_strip_cut3/13/17.png`). | A better |
| 3 | Type scale and hierarchy in step scenes: A's headline is roughly 1.5x B's and has a clear label/headline/support ladder (`A_full_n225.png` vs `B_full_n225.png`). | A better |
| 4 | Palette discipline: A adds a tinted panel; B stays on three colours (`A_full_n375.png` vs `B_full_n375.png`). | B better |
| 5 | Cleanliness of in-between frames: A has the rail/text collision at 13 s and the dim-line-first state at 8 s; B has none (`A_strip_cut13.png`, `A_strip_cut8.png` vs B cut strips). | B better |

Also noted, no score impact: A is the more designed and varied piece (persistent rail, panel, wipe, highlighted 147) and B the plainer, more uniform one - which reads as better is taste.

## Could not judge from stills

- Easing and feel of any move (curves, overshoot, whether B's 6-frame settle softens the cut in motion, whether A's wipe and push feel smooth or abrupt).
- Whether A's 0.1-0.2 s rail-only holds read as a pause or a gap at speed.
- Whether A's full-accent frame at n510 reads as a flash.
- Legibility of the count-up digits and of B's smallest text at normal viewing distance.
- Motion blur vs. applied blur, flicker, compression artefacts in playback.
- Exact font families (both look like the same system sans and mono).

## Frames opened

- `BRIEF.md`, `A-sheet.png`, `B-sheet.png`, `A-frames/f029.png`, `B-frames/f029.png`
- `extra/A_strip_*.png` and `extra/B_strip_*.png`: `start`, `cut3`, `cut8`, `cut13`, `cut17`, `end`, `s1mid`, `s2mid`, `s3mid`, `s4mid`, `s5mid` (11 per clip, every frame from 0.3 s before to 0.5 s after each cut, first and last 0.5 s, every 5th frame mid-scene)
- Full resolution: `extra/A_full_n075/225/375/495/595.png`, `extra/B_full_n075/225/375/495/595.png`
- Pixel statistics (not viewed): the ten full-res frames, plus per-frame measurements over n000-006, n086-096, n236-246, n384-396, n504-516, n596-599 in both clips. `A_full_n000/599` and `B_full_n000/599` were extracted but only seen through the strips.
