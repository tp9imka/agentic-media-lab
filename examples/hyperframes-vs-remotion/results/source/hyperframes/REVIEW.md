# REVIEW

## Creative calls
- The brief gave the script and the shot list, so no three storylines were written (story.md: "When the person gave a script ... follow theirs").
- One carrier: a 12 px accent margin rule present in every scene. Type is large and left-aligned on x=252 to stay out of the "small things floating in a dark void" default; the ground colour itself is fixed by the brief.
- Scene 3 shows the order it describes: quote block opens first, "Then write the sentence." sits dimmed and only goes to ink afterwards.
- Seams: blur swap (1=>2, 2=>3), whip left with a mirrored arrival (3=>4), the rule floods the frame and retracts (4=>5). Three kinds.
- "Step 1/2/3" are shown as quiet labels because they are in the brief's on-screen copy column.
- Accent appears on the rule, the number 147 and the flood only.

## Measured
- `check --json`: 0 errors (lint, runtime, layout 9 samples, contrast 24/24). Motion assertions not written (motion.enabled false).
- ffprobe on out/final.mp4: h264, 1920x1080, 30/1, 600 frames, 20.000000 s, no audio stream.

## Looked at
- `snapshot --review`: beat sheet, seam strips 3 and 4, phone sheet. Seam strips 1 and 2 were generated but not opened.
- Pass 2: 9 frames after the fixes. Then 12 frames decoded from the final MP4.
- Nobody watched it at full speed; eases and pacing were judged from stills only.

## Notes fixed
- t=15.2-16.6s - S4 data line - full line readable ~1.3 s before the flood => count starts at 0.9 s, second half at 1.7 s (now ~1.7 s).
- phone sheet - step labels, source label, closing small line too small => 52 / 46 / 48 px.

## Weakest shot
- Seam 3=>4: the frame at 13.0 s is the rule alone (outgoing copy gone, incoming at opacity 0), and the outgoing copy crosses the rule while leaving. With more time: overlap the arrival or clip the copy at the rule.
- Scenes 1, 2 and 5 leave the lower third empty.

## Warnings kept on purpose
- `film_silent`: the brief says no audio track is required and allows no stock assets.
- `font_face_local_only` x10: the brief requires system fonts and no font downloads, so Helvetica Neue and Menlo are bound with local(). A render on another machine may fall back.
