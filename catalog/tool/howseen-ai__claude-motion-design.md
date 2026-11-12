# claude-motion-design (Howseen)

`tool:howseen-ai/claude-motion-design` - tool - <https://github.com/howseen-ai/claude-motion-design>

One long Claude Code skill (skill/motion-design/SKILL.md, about 34 KB) plus Python scripts for launch films in HTML, Playwright and ffmpeg: beat map first, four stills approved, subframe render, pop scan, SFX placed by measured peak, two-pass loudnorm. It also has a remake mode that copies a reference video's shot timing.

Concepts: [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent Skills](../../docs/glossary.md#agent-skills)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its critique loop is a fixed rubric of seven 1-10 scores with a stop rule, and its audio scripts are short enough to copy.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | review-loop, audio, motion, delivery |
| cost | free-local |

Borrow: (1) section 8, Critique loop: four ffmpeg tile commands (contact sheet at 2 fps, 12-frame strip around a fast move, 1 fps phone-width sheet, loop seam) plus the seven-score rubric and the stop rule 'every score 8+', copied as text; (2) scripts/analyze_song.py, one file of about 20 lines (onset autocorrelation for BPM, per-second full and low band energy to find the drop); (3) the peak-alignment loop in scripts/audio_template.py, which shifts each SFX so its argmax lands on the cue. All MIT; needs Python, numpy, imageio-ffmpeg and Playwright. Gotchas: SKILL.md is the author's working notebook, with hardcoded Mixkit ids, the author's name and folders not in the repo (crave/, reel2/, h20/). The assets section has the agent pull meme clips from YouTube with yt_dlp and send a non-default User-Agent to get past Cloudflare; skip those parts. scripts/mcp21_client.py reads a 21st.dev API key from ~/.config/21st.key. The 8+ scores are graded by the same model that made the film. Not run here.

## Claims

1. The critique loop scores seven named criteria from 1 to 10 on contact sheets, then fixes, re-renders and re-scores until every score is 8 or more.

   > Open them and **score 1-10**: hook in the first 2 s · readability at 360 px · motion quality (springs, no dead frames) · variety (something new every 2-4 s) · composition · brand/data accuracy · sound sync.

   Locator: skill/motion-design/SKILL.md, 8. Critique loop. Source: <https://github.com/howseen-ai/claude-motion-design/blob/main/skill/motion-design/SKILL.md>, retrieved 2026-11-12.

2. It finds the music drop from per-bar band energy rather than trusting an automatic beat grid.

   > **Find the drop by energy**, never trust an auto grid: per-bar low/full band energy, then 20-50 ms windows around the jump.

   Locator: skill/motion-design/SKILL.md, 4. Music & SFX. Source: <https://github.com/howseen-ai/claude-motion-design/blob/main/skill/motion-design/SKILL.md>, retrieved 2026-11-12.

3. It tells the agent to send a non-default User-Agent where Cloudflare blocks Python's.

   > Cloudflare blocks Python's default UA on some APIs: send `User-Agent: claude-code-mcp-client/1.0`.

   Locator: skill/motion-design/SKILL.md, 6. Gotchas. Source: <https://github.com/howseen-ai/claude-motion-design/blob/main/skill/motion-design/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skill/motion-design/SKILL.md, scripts/analyze_song.py, scripts/audio_template.py, LICENSE and README.md against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `52e5129c0dfe2ca02bf1e87a0d4ece0cde457ccc47d423a362e58caf5f7e00ab`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-27
- default_branch: main
- fetched_at: 2026-11-12
- forks: 105
- last_activity: 2026-10-04
- licence: MIT
- open_issues: 2
- sources: https://api.github.com/repos/howseen-ai/claude-motion-design, https://skills.sh/api/search?q=claude-motion-design
- stars: 814

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
