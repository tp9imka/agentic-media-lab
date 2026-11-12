# Auto-Editor

`tool:wyattblue/auto-editor` - tool - <https://github.com/WyattBlue/auto-editor>

A CLI that cuts dead space by audio level, motion or black frames, cuts by spoken words from subtitles, and exports to Premiere, Resolve, Final Cut, Shotcut, Kdenlive or EDL. The repo ships its own Agent Skills.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: auto-editor, auto-editor skill

Tags: silence-removal

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The standard first pass for silence removal, now with skills from the author, a dry-run preview and filler-word cuts from a local transcript.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: established.

| field | value |
|---|---|
| tool_type | skill |
| agents | any-skill |
| levers | audio, captions, delivery |
| cost | free-local |

Install with `npx skills add WyattBlue/auto-editor`; the CLI is installed separately (see auto-editor.com/installing, not opened). Use `--preview` before a long render and `--margin 0.3s,1.5sec` to avoid clipped words. `-anorm ebu` applies EBU R128 loudness on render. Transcription needs a ggml model file; the Apple backend needs macOS 26 and may download a speech model on first use. The online app and desktop app are separate, with proprietary assets.

## Claims

1. A preview flag prints what would be cut without rendering, so the agent can check before a long render.

   > `--preview` prints what *would* be cut and exits without rendering — use it to sanity-check before a long render.

   Locator: skills/auto-editor/SKILL.md, introduction. Source: <https://github.com/WyattBlue/auto-editor/blob/master/skills/auto-editor/SKILL.md>, retrieved 2026-11-12.

2. Filler words can be cut by inverting a word match on the transcript.

   > auto-editor video.mp4 --edit "(not word:um)"

   Locator: skills/auto-editor-transcribe/SKILL.md, section Edit by spoken content. Source: <https://github.com/WyattBlue/auto-editor/blob/master/skills/auto-editor-transcribe/SKILL.md>, retrieved 2026-11-12.

3. It can transcribe with Apple's built-in recogniser on macOS 26 or later.

   > - **Apple**: the magic model name `apple` uses Apple's built-in transcriber; requires macOS 26 or later.

   Locator: skills/auto-editor-transcribe/SKILL.md, section Transcribe. Source: <https://github.com/WyattBlue/auto-editor/blob/master/skills/auto-editor-transcribe/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and two SKILL.md files (auto-editor, auto-editor-transcribe) against the three claims; effects, transitions and export skills listed but not read
- Next check due: 2027-02-10
- Licence: Unlicense
- URL status: live
- Saved source sha256: `1e204a1a15ba0255f110c28ce3b5d3c3e1da6998e37b96e2ae1791674aff26a0`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2020-04-30
- default_branch: master
- fetched_at: 2026-11-12
- forks: 726
- installs: 1211
- installs_by_skill: {"auto-editor": 1211, "auto-editor-effects": 984, "auto-editor-export": 1086, "auto-editor-transcribe": 1052, "auto-editor-transitions": 213}
- last_activity: 2026-11-12
- licence: Unlicense
- open_issues: 0
- registry: skills.sh
- sources: https://api.github.com/repos/WyattBlue/auto-editor, https://skills.sh/api/search?q=auto-editor
- stars: 5856

## Related

- integrates_with: [whisper.cpp](ggml-org__whisper.cpp.md)
- integrates_with: [FCPXML Reference (Apple Developer)](../source/developer.apple.com__documentation__professional-video-applications__fcpxml-reference.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
