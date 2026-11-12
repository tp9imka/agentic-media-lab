2026-11-12T08:53:41Z
(line 1 above = start, UTC)

# RUNLOG - HyperFrames arm

- start 2026-11-12T08:53:41Z, end 2026-11-12T09:01:27Z (log written), hard stop was 09:23:41Z
- node v22.22.2, npm 11.12.1, hyperframes CLI 0.9.37

## Installs
- 08:53:4x `npm init -y` then `npm install hyperframes` in the arm folder: 78 packages, 7 s. This first install ran with NODE_TLS_REJECT_UNAUTHORIZED=0 inherited from the run environment (not set by me, noticed from the npm warning).
- 08:54 removed node_modules + package-lock.json and re-ran `npm install hyperframes` with the variable unset (TLS verification on): hyperframes@0.9.37, 4.6 s. No certificate error. Every later command ran with the variable unset.
- `du -sh`: node_modules 117M, video/ 2.9M, arm folder 121M.
- NOT run: `npx hyperframes skills update`. Read from node_modules/hyperframes/dist/chunk-4RHBW4E7.js: it spawns `npx skills@1.5.13 add https://github.com/heygen-com/hyperframes --skill ... --global --agent claude-code universal --copy --full-depth --yes` with cwd = home. That installs into ~/.claude/skills and ~/.agents/skills, outside the arm folder, so it breaks the "everything inside the arm folder" rule. I used the identical skills bundled in the local package: node_modules/hyperframes/dist/skills/ (4.4M: hyperframes, hyperframes-cli, media-use). Not verified: that the bundled copies are byte-identical to what the installer would fetch from GitHub.
- `npx hyperframes init video --skip-skills --skill=hyperframes` (the skill's own scaffold command) => video/ with index.html, package.json, hyperframes.json, meta.json, AGENTS.md, CLAUDE.md. No npm install inside video/.

## Writes outside the arm folder (made by the CLI, not asked for; left in place, not deleted)
- ~/.hyperframes/config.json + install-state.json, created 08:54:30Z by my first CLI call. config.json holds an anonymousId and "telemetryEnabled": true.
- ~/.cache/hyperframes/ (199M): chrome/chrome-headless-shell (appears to have been downloaded during check/snapshot around 08:58-08:59Z; no TLS error seen, verification was on), history/, warm/, locks/.
- ~/.local/state/hyperframes/previews/<id>.log from the preview step.

## Telemetry
- Skipped: `npx hyperframes events --skill=hyperframes` and `npx hyperframes events --skill=hyperframes-cli` (the "Usage beacon" line at the top of both SKILL.md files). Also skipped `npx hyperframes usage --json` (plan usage, account-related) and `feedback --rating` after render.
- Opt-out set: env HYPERFRAMES_NO_TELEMETRY=1 and DO_NOT_TRACK=1 on every command from init onward (both names found in the CLI dist; the documented user-facing opt-out is `hyperframes telemetry disable`, which I did not run because it writes ~/.hyperframes/config.json). Also HYPERFRAMES_NO_UPDATE_CHECK=1.
- Gap: four CLI calls ran BEFORE the opt-out was set (`--version`, `--help`, `telemetry --help`, `skills --help`, 08:53:5x-08:54:3x, the first one also with TLS verification disabled by the inherited env). The first-run telemetry notice printed during those. I cannot tell whether events were sent. `init --skill=hyperframes` carries a skill tag; it ran with the opt-out env set.

## Skill files read
- node_modules/hyperframes/dist/skills/hyperframes/SKILL.md
- node_modules/hyperframes/dist/skills/hyperframes-cli/SKILL.md
- .../hyperframes/references/types/explainer.md, story.md, spec.md, format.md, motion.md, review.md (full)
- .../hyperframes/references/sound.md (first 20 lines)
- .../hyperframes-cli/references/lint-validate-inspect.md, preview-render.md (grep for snapshot/render/preview lines only)
- Not read: look.md, film.md, runtimes.md, captions.md, overlays.md, storyboard*.md, skill-lifecycle.md, plugin-installation.md, media-use/*.

## Skill instructions followed
- SKILL.md "A new project: `npx hyperframes init <dir> --skip-skills --skill=hyperframes`" => scaffolded video/.
- SKILL.md "One scene per sub-composition ... the root holds only scene hosts" + format.md project shape => index.html with 5 hosts, compositions/s1..s5.html, each inside <template>, root styled as #root, timeline registered as window.__timelines["sN"].
- SKILL.md contract 1 and 5 "Every timed element has class=\"clip\", data-start and data-duration" / "Never tween display, visibility ... on a .clip; animate a child" => clip wrappers per scene, GSAP only touches their children.
- format.md "Use fromTo, not from, inside a scene" => every tween is fromTo.
- spec.md "before any scene, write SPEC.md ... a number wherever you would have written an adjective" => video/SPEC.md written first.
- spec.md BANNED "everything centred; ... every element fading and sliding up" => left-aligned grid, no slide-up fades; entrances vary per scene.
- motion.md "Exits are 40-50% shorter than their entrances" and "Ease by role: an arrival lands on a long tail (expo.out, power4.out) ... an exit accelerates (power3.in)" => exits 0.2-0.26 s on power3.in, arrivals expo.out/power4.out/power3.out.
- motion.md "Titles: a landed title is dead still ... Vary the entrance within a film" + the per-word blur / grey-to-ink / whole-line blur recipes => S1 grey-to-ink, S2 per-word blur 6px 0.13 s 0.067 s apart, S3 whole-line blur, S5 revealed by the wipe.
- motion.md "Use 3-5 kinds [of transition] in a film" + "Blur swap on one stage", "Whip" => blur swap, whip, accent flood.
- story.md "frame 0 is the thumbnail: never black" => title is on screen at 30% at frame 0.
- hyperframes-cli SKILL.md loop: lint => `check --json` => snapshot => preview => render => ffprobe + decoded frames. All done in that order.
- review.md "`snapshot --review` writes three sheets ... Open all three" and "REVIEW.md at the project root" => done, see below.
- SKILL.md "Before the delivery render of a new video, open the Studio preview, even in no-questions mode" => `preview --background --no-open --port 4567`, HTTP 200, then `preview --stop`. Started but not opened in a browser (nobody to look).

## Skill instructions not followed
- "Usage beacon: run npx hyperframes events --skill=..." - forbidden by the run rules.
- "npx hyperframes usage --json reports the person's remaining plan usage" - skipped, account-related.
- story.md "Write three [storylines] ... STORYLINES.md" - skipped: the same file says to follow a given script, and the brief fixes scenes and copy.
- sound.md / SKILL.md "a film over ~15 s that tells something gets music and sound" - skipped: brief says no audio required, no stock assets. `film_silent` warning kept.
- SKILL.md "Copy ... [is] variables (data-var-text ...)" - colours are declared as composition variables with hex fallbacks; copy is not (per-word spans). Not verified that the root colour variables actually reach the scenes; the fallbacks carry the same values.
- SKILL.md "Only the bundled fonts resolve by name" / lint fix "use a Google Fonts family" - the brief demands system fonts, so local() @font-face for Helvetica Neue and Menlo. 10 `font_face_local_only` warnings kept.
- SKILL.md "search the registry before hand-writing a named ... transition" - not done (/hyperframes-registry skill is not in the bundle; time).
- explainer.md "Usually 30-90 s", "Ground it first ... a person, a place" - brief fixes 20 s and the copy.
- hyperframes-cli "history begin/end", "feedback --rating" - skipped (trial feature / telemetry).
- review.md sub-agent "fresh pair of eyes" and `audio <video>` - skipped (no audio; time).
- motion.md .motion.json assertions - not written.

## Checks and renders
- 08:57:51Z `npx hyperframes lint`: 0 errors, 10 warnings (font_face_local_only), 1 s.
- 08:58:03Z `npx hyperframes check --json`: ok true, exit 0, 7 s. Only craft warning film_silent. (output: check1.json)
- 08:58:18Z `npx hyperframes snapshot --review --json`: 9 s, sheets in video/.hyperframes/artifacts/snapshots/765282c6-.../
- 08:59:02Z second `check --json` after fixes: ok true, same warnings (check2.json); `snapshot --at 0,5.5,10.5,12.6,14.6,15.2,16.5,18.5,19.9`.
- 08:59:38Z preview start/stop, HTTP 200.
- Render attempt 1 (only attempt): 08:59:43Z `npx hyperframes render --quality delivery --fps 30 -o ../out/final.mp4` => "Render complete", 762.1 KB, "rendered in 15.3s" (27.9 s wall incl. npx), screenshot capture, hardware gpu, 8 workers. No error.
- ffprobe: codec_name=h264 width=1920 height=1080 r_frame_rate=30/1 nb_frames=600 duration=20.000000; High profile, yuv420p, one video stream, no audio.
- GSAP is loaded from cdn.jsdelivr.net in index.html (the scaffold's own script tag). Not verified whether check/render fetched it from the network or from a bundled copy.

## Frame inspection (3 times)
1. review-beats.jpg, review-seam-03.jpg, review-seam-04.jpg, review-phone.jpg. Saw: all scenes mounted, copy exact, Helvetica Neue + Menlo, rule continuous. Problems: S4 data line fully visible only ~1.3 s before the flood; small labels unreadable on the phone sheet. Changed: S4 timings (0.9 s / 1.7 s), label sizes 52/46/48 px. review-seam-01/02 were not opened.
2. review/pass2-sheet.png (9 snapshots tiled with ffmpeg). Saw the fixes hold; frame 0 shows the dimmed title without the rule (rule draws in over 0.6 s). No change.
3. review/final-mp4-sheet.png: frames 0, 45, 87, 93, 165, 315, 386, 393, 450, 505, 514, 599 decoded from out/final.mp4. Same as snapshots; transitions visible at 87 (blur), 386/393 (whip), 505/514 (flood); last frame is the closing card with both lines. No change.

## Surprises / blockers
- The vendor's documented install command is a global install with --yes; could not be run under the folder rule.
- The shell profile disables Node TLS verification globally; one npm install and four help calls ran under it before I caught it.
- The CLI writes config, a 199M browser cache and history blobs to the home directory without asking.
- Shell clock: `date` readings put the whole run inside ~8 minutes.
- No blocker on the render itself.
- total wall minutes at log close: 7 min 46 s (end 2026-11-12T09:01:27Z)
