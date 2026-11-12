# motion-graphics (Bart)

`tool:barty-bart/motion-graphics` - tool - <https://github.com/Barty-Bart/motion-graphics>

Six Claude Code skills: motion-broll times motion-graphic B-roll to a speaker's transcript, object-separation cuts a subject out of video locally with SAM 2.1, sound-effects places bundled CC0 sounds on a checked beat grid, and three explainer templates.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Agent Skills](../../docs/glossary.md#agent-skills), [Visual design](../../docs/glossary.md#visual-design)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It answers where a graphic may sit while a person talks, and how to separate the person from the background locally on a Mac.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, any-skill |
| levers | motion, audio, asset, review-loop |
| cost | free-local |

Borrow: (1) skills/motion-broll/scripts/inspect_video.py, one file of about 40 lines (ffmpeg plus numpy) that labels stretches full, pip or black, measures the subject box and warns when it moves; (2) the object-separation code blocks in skills/object-separation/SKILL.md: SAM 2.1 through Hugging Face transformers Sam2VideoModel, 60-frame chunks each seeded from the previous mask; (3) skills/sound-effects/scripts/sound_pass.py: librosa beat grid shifted by the median offset of sub-120 Hz kicks when it exceeds 30 ms, plus a licence check on every placed sound. Code MIT, bundled SFX CC0, Geist fonts OFL. Gotchas: pip detection only works when the empty area is near-black (side band mean under 8 of 255); a styled background reads as full. SAM needs click points the agent picks from a gridded still; the skill says CPU runs about 5 s per frame, M3 Max speed not measured here. Transparent panel clips need an ffmpeg with prores_ks. The sound-effects rules ban synthesized SFX, the opposite of tool:whaleyxbt/claude-motion and tool:abubakrchan/product-launch-motion. Not run here.

## Claims

1. inspect_video.py treats a near-black column band as free space for a panel beside the speaker.

   > # a column band that is near-black for a stretch = free space for an overlay panel.

   Locator: skills/motion-broll/scripts/inspect_video.py, comment above layout(). Source: <https://github.com/Barty-Bart/motion-graphics/blob/main/skills/motion-broll/scripts/inspect_video.py>, retrieved 2026-11-12.

2. On Apple Silicon the object-separation code picks SAM 2.1 hiera-base-plus on PyTorch MPS, run locally.

   > dev, MODEL = "mps", "facebook/sam2.1-hiera-base-plus"

   Locator: skills/object-separation/SKILL.md, 2. Scan the computer and pick the model. Source: <https://github.com/Barty-Bart/motion-graphics/blob/main/skills/object-separation/SKILL.md>, retrieved 2026-11-12.

3. LICENSE appends separate font and icon terms to the MIT text, which is why GitHub shows no single licence.

   > The Geist and Geist Mono fonts in skills/motion-broll/engine/fonts are licensed separately under the SIL Open Font License 1.1 (see OFL-Geist.txt).

   Locator: LICENSE, after the MIT text. Source: <https://github.com/Barty-Bart/motion-graphics/blob/main/LICENSE>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/motion-broll/SKILL.md, scripts/inspect_video.py, skills/object-separation/SKILL.md, skills/sound-effects/SKILL.md, scripts/sound_pass.py, LICENSE and README.md against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `81fa1b205fa1453dc61a97619ab530643a7044a6f682c8ecb7737ed0740a39fe`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-25
- default_branch: main
- fetched_at: 2026-11-12
- forks: 177
- installs: 3243
- installs_by_skill: {"explainer-default": 2224, "explainer-engaging": 2260, "explainer-high-energy": 2306, "motion-broll": 3243, "object-separation": 2569, "sound-effects": 2962}
- last_activity: 2026-10-13
- licence: unknown
- open_issues: 3
- registry: skills.sh
- sources: https://api.github.com/repos/Barty-Bart/motion-graphics, https://skills.sh/api/search?q=motion-graphics
- stars: 1214

## Related

None.

## Referenced by

- [claude-motion](whaleyxbt__claude-motion.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
