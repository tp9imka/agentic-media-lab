# claude-motion

`tool:whaleyxbt/claude-motion` - tool - <https://github.com/whaleyxbt/claude-motion>

A Remotion project with four skills (motion-design taste rules, review-loop, sound-design, web-sims) and a pure-Python SFX engine that reads the same timeline.json as the picture. A second pipeline renders web simulations frame by frame to video.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Review loop](../../docs/glossary.md#review-loop), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Agent Skills](../../docs/glossary.md#agent-skills)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** One timeline file drives both picture and sound, so retiming cannot put the audio out of sync, and the sound is synthesized with no sample licences to track.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, cursor, codex |
| levers | audio, review-loop, motion, design |
| cost | mixed |

Borrow: the sfx/ package (synth.py, mix.py, loudness.py; Python stdlib only, BS.1770 loudness, automatic master to -14 LUFS with true peak at or under -2 dBFS), copied as a folder, MIT; and the timeline.json pattern: named beats per scene read by the components and by the cue sheet, with no typed times in either. scripts/sheet.mjs makes the per-beat contact sheets the review loop reads. Gotchas: the picture side is Remotion 4.0.529, so Remotion's company licence applies (see tool:remotion-dev/remotion); the sfx engine and the sims/ pipeline do not need Remotion. The sound-design skill admits its own example mixes two keys. The optional ElevenLabs MCP in .mcp.json.example needs an API key. Synthesized SFX are banned by tool:barty-bart/motion-graphics. Not run here.

## Claims

1. Components and the audio cue sheet read the same timeline.json, which keeps picture and sound locked.

   > Components read it through `TL` from `src/lib.ts`; the video's cue sheet in `sfx/cues/` reads the same file. That is what keeps picture and sound locked.

   Locator: .claude/skills/motion-design/SKILL.md, 1. Time lives in timeline.json. Source: <https://github.com/whaleyxbt/claude-motion/blob/main/.claude/skills/motion-design/SKILL.md>, retrieved 2026-11-12.

2. Every sound is synthesized in Python stdlib, with no samples or licences.

   > The `sfx/` engine synthesizes every sound in pure Python stdlib: no samples, no licenses, no installs, same output on every run.

   Locator: .claude/skills/sound-design/SKILL.md, introduction. Source: <https://github.com/whaleyxbt/claude-motion/blob/main/.claude/skills/sound-design/SKILL.md>, retrieved 2026-11-12.

3. The review loop renders one frame 0.3 s after each timeline beat into labelled 4x2 sheets and repeats until a full pass finds nothing.

   > `npm run sheet` — one frame per timeline beat, 0.3 s after it so motion has settled, tiled 4×2 into `out/sheets/beats-N.png`.

   Locator: .claude/skills/review-loop/SKILL.md, Loop, step 2. Source: <https://github.com/whaleyxbt/claude-motion/blob/main/.claude/skills/review-loop/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. .claude/skills motion-design, review-loop and sound-design SKILL.md, timeline.json, sims/beats.py, package.json, .mcp.json.example, LICENSE and README.md against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `f6c03807ce662e052bd74a7e2490f69b14ebc821d12ccae8e62e0bdad42ae792`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-29
- default_branch: main
- fetched_at: 2026-11-12
- forks: 119
- installs: 295
- installs_by_skill: {"motion-design": 274, "review-loop": 285, "sound-design": 295, "web-sims": 266}
- last_activity: 2026-11-08
- licence: MIT
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/whaleyxbt/claude-motion, https://skills.sh/api/search?q=claude-motion
- stars: 955

## Related

- depends_on: [Remotion](remotion-dev__remotion.md)
- contradicts: [motion-graphics (Bart)](barty-bart__motion-graphics.md) - synthesized SFX here; Barty's sound-effects skill bans them

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
