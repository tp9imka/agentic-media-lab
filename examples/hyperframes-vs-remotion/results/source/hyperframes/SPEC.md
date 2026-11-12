GOAL:    The viewer leaves knowing the order: open the source, copy the quote, then write; the gate checks it.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps
TIME:    20 s x 30 = 600 frames; no music (brief: no audio track required), so no BPM
LOOK:    ground #0F1419 flat, no texture; ink #F2F4F7; one accent #4CC38A, allowed on: the left rule,
         the number 147, the wipe into the closing card. Quiet text = ink at 60% alpha (same hue).
         Display: system sans (Helvetica Neue via local()) 700, 230 px title / 150 px closing /
         96-104 px step lines, tracking -2%. Body: same face 400, 56-60 px. Scene 4 data line: Menlo 60 px.
         Medium: a printed page with a margin rule. No shadows, no grain, no vignette, no gradients.
         Grid: everything left-aligned on x=252, inside the 80% title-safe box (192..1728, 108..972).
OBJECTS: the margin rule (12 px accent bar at x=192, full title-safe height) - the one carrier, present in
         every scene; the quote block (ink at 6% panel holding the quoted sentence and its source label).
MOTION:  enter = expo.out / power4.out; exit = power3.in; wipe = power3.in out, power3.out in.
         Word stagger 67-100 ms (2-3 frames). Entrances 4-18 frames, exits 6-8 frames (40-50% shorter).
SHOTS:   f0-90    S1 title. Rule draws down (18 f), "Quote first." goes grey => ink per word, subtitle blurs in
                  at f24. Read: 2+7 words. Out: blur swap, rule holds.
         f90-240  S2 step 1. Headline per-word blur-in, then the three sources wipe in one at a time
                  (f126, f147, f168). Out: blur swap, rule holds.
         f240-390 S3 step 2. "Copy the quote." lands, quote block wipes open (f21), source label (f45),
                  then "Then write the sentence." goes grey => ink (f75): order on screen = order of the rule.
                  Out: whip left.
         f390-510 S4 step 3. Arrives from the right (mirrored ease). Data line at f36, 147 counts up in accent,
                  "quote-not-found: 0" at f66. Out: the rule floods the frame (11 f, power3.in).
         f510-600 S5 closing. Flood retracts into the rule, "No quote, no claim." is already there, dead still;
                  small line blurs in at f27; holds to the end (>= 2 s).
BANNED:  dark void with small things floating in the middle (ground is fixed by the brief, so type is large and
         left-aligned on a grid instead); glow, particles, gradients, glass cards; everything centred; every
         element fading and sliding up; titles drifting after they land; breathing loops; numbered 01/02 chips;
         corner labels; three cards in a row; logo.
QA:      t=0 (not empty), 1.5, 5.5, 10.5, 15.5, 18.5 (each scene mid: all copy present, exact, inside safe box);
         seams at 3, 8, 13, 17 (no jump, rule continuous); phone sheet readable.
