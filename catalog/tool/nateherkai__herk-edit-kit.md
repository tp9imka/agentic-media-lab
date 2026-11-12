# Herk Edit Kit

`tool:nateherkai/herk-edit-kit` - tool - <https://github.com/nateherkai/herk-edit-kit>

A Codex and Claude Code workspace for editing talking-head recordings on HyperFrames. A cut-silences agent and a review-gated cut-mistakes agent work from a word-level transcript and cut with ffmpeg; later skills add motion-graphic cards, short-form edits and showreels. It bundles copies of the HyperFrames and GSAP skills.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Code-driven video](../../docs/glossary.md#code-driven-video)

Also known as: hyperframes-student-kit, nateherkai/hyperframes-student-kit

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its silence cutter is deterministic with stated thresholds, and its mistake cutter proposes cuts for approval instead of deleting on its own.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | codex, claude-code |
| levers | story, motion, captions, orchestration |
| cost | mixed |

Borrow: .claude/skills/cut-silences/scripts/cut-silences.mjs, one Node file that needs only ffmpeg (defaults: gap 0.55 s, head pad 0.22 s, tail pad 0.34 s, kept breath 0.14-0.24 s; writes an EDL, a re-timed transcript and a trim/atrim concat filtergraph); and the cut-mistakes pair find-cut-candidates.mjs plus apply-cuts.mjs with the approval file shape {cuts:[{start,end,reason}]}. Retakes are found by Jaccard similarity of segments (score 0.34 or more => recommend cut). Transcripts: the bundled scripts/transcribe-elevenlabs.mjs uploads the audio to ElevenLabs Scribe and needs ELEVENLABS_API_KEY (hosted, paid); the cutters also accept a generic {words:[{text,start,end}]} JSON, so a local Whisper transcript should fit (not tested here). Licence: GitHub reports NOASSERTION because LICENSE is MIT plus a note that the AIS brand assets are not licensed, and a second grant covers imported pipeline material without a per-file list; keep both notices when copying a skill. The bundled HyperFrames skills are Apache-2.0 copies and may lag tool:heygen-com/hyperframes. Not run here.

## Claims

1. The silence cutter leaves pauses under 0.55 s alone and trims longer ones down to a kept breath.

   > Pauses below `--gap` (0.55s) are left alone — natural speech rhythm.

   Locator: .claude/skills/cut-silences/SKILL.md, How it decides (the silence rules). Source: <https://github.com/nateherkai/herk-edit-kit/blob/main/.claude/skills/cut-silences/SKILL.md>, retrieved 2026-11-12.

2. The mistake cutter only renders cuts that the agent and the user approved.

   > So this agent is **review-gated by default**: it surfaces candidates with full context; the agent (and the user) decide; only approved cuts are rendered.

   Locator: .claude/skills/cut-mistakes/SKILL.md, introduction. Source: <https://github.com/nateherkai/herk-edit-kit/blob/main/.claude/skills/cut-mistakes/SKILL.md>, retrieved 2026-11-12.

3. MIT covers the original kit; imported pipeline material is under a separate use permission.

   > See LICENSE for the MIT permission for the original kit material. Imported pipeline resources retain the grant in licenses/PIPELINE-USE-PERMISSION.txt.

   Locator: THIRD_PARTY_NOTICES.md, Resource provenance. Source: <https://github.com/nateherkai/herk-edit-kit/blob/main/THIRD_PARTY_NOTICES.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. cut-silences and cut-mistakes SKILL.md, find-cut-candidates.mjs, transcribe-elevenlabs.mjs, LICENSE, THIRD_PARTY_NOTICES.md, licenses/PIPELINE-USE-PERMISSION.txt and README.md against the claims; nateherkai/hyperframes-student-kit resolves to this repo via the GitHub API
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `c0e90ef532b35b8d9928d05e0933c1971e8ff53a61f2f4a23b77942adb59343f`
- Lane: community-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-04-18
- default_branch: main
- fetched_at: 2026-11-12
- forks: 673
- installs: 331
- installs_by_skill: {"cut-mistakes": 315, "cut-silences": 312, "edit-video": 283, "gsap": 25, "hyperframes-video-beats": 280, "make-a-video": 319, "short-form-edit": 331, "short-form-video": 258, "style-library": 269, "video-storytelling": 309}
- last_activity: 2026-10-14
- licence: unknown
- open_issues: 13
- registry: skills.sh
- sources: https://api.github.com/repos/nateherkai/herk-edit-kit, https://skills.sh/api/search?q=herk-edit-kit
- stars: 2779

## Related

- depends_on: [HyperFrames](heygen-com__hyperframes.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
