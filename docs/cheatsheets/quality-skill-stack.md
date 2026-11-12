---
id: guide:quality-skill-stack
title: "My agent-made video looks amateur: which skill fixes which problem"
summary: Maps each visible defect in an agent-made clip to the lever, the skill records that instruct the agent on it, and one quoted instruction per row.
use_when: "Use this page when an agent-made clip looks amateur and you want to know which skill instructs the agent on the defect you see."
concepts: [concept:craft, concept:agent-skills, concept:motion-and-transitions, concept:visual-design, concept:audio-and-captions, concept:review-loop, concept:delivery, concept:agent-portability, concept:popularity-and-trust]
last_reviewed: 2026-11-12
---

# My agent-made video looks amateur: which skill fixes which problem

For a developer whose agent (Claude Code, some Codex) makes the clip. Find the defect in the first table, then read [where the skills contradict each other](../research/skill-rule-conflicts.md). Every skill here is "read, not run" unless marked "run here once"; no record holds an independent before/after measurement, so rows say what a skill instructs.

## Symptom to skill

| What you see | Lever | Records | Instruction, quoted from the first record |
|---|---|---|---|
| Flat or robotic motion | motion | [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md), [motion-design skill](../../catalog/tool/lottiefiles__motion-design-skill.md), [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md) | "The same `power2.out` at 0.5 s on everything is the flat default that makes a film feel generated." |
| Default fonts, drifting alignment | design | [motion-video-director](../../catalog/tool/mattypark__motion-graphics-skill.md) | "Never ship a font whose license you couldn't verify." |
| Text touching the frame edge | design | [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md) | "For 1080px-wide videos, keep key text at least 80px from the sides and 100px from the top and bottom." |
| Clicks or uneven loudness | audio | [video-use](../../catalog/tool/browser-use__video-use.md), [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md) | "**Never cut inside a word.** Snap every cut edge to a word boundary from the Scribe transcript." |
| Captions hard to read | captions | [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md) | "python skills/production/audio-craft/captions-media-accessibility/scripts/validate_captions.py --max-lines 2 --max-chars-per-line 42 --cps-warning 20 captions_en.vtt" |
| Scenes that do not match each other | consistency | [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md), [claude-code-video-toolkit](../../catalog/tool/digitalsamba__claude-code-video-toolkit.md) | "**Locked**: must remain constant unless user approves a redesign." |
| It rendered but nobody looked | review-loop | [ffmpeg-skill](../../catalog/tool/kajisho5__ffmpeg-skill.md), [video-shotcraft](../../catalog/tool/vincentwei1021__video-shotcraft.md), [remotion-superpowers](../../catalog/tool/dojocodinglabs__remotion-superpowers.md) | "8. **Look** after any picture change: `look.py OUTPUT --tiles 3x2`, view the PNG, name it in `Look:`;" |
| Wrong export for the platform | delivery | [ffmpeg-skill](../../catalog/tool/kajisho5__ffmpeg-skill.md), [motion-skills (iArt)](../../catalog/tool/iart-ai__motion-skills.md) | "5. **Check** with `check.py OUTPUT --platform X --expect-identity S:M`" |

Loudness targets in these skills disagree with the EBU records: see [loudness](../research/skill-rule-conflicts.md#loudness-target).

## Claude Code first

All state Claude Code support. Codex support is "stated by the project", untested here (filter: `python3 tools/query.py search "video skill" --agent codex`).

| Support stated | Records |
|---|---|
| Claude Code only | [claude-code-video-toolkit](../../catalog/tool/digitalsamba__claude-code-video-toolkit.md), [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md), [claude-plugin-marketplace](../../catalog/tool/josiahsiegel__claude-plugin-marketplace.md), [claude-video-vision](../../catalog/tool/jordanrendric__claude-video-vision.md), [smooth-animation-skill](../../catalog/tool/flchntc__smooth-animation-skill.md) |
| Claude Code and Codex | [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md), [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md), [ffmpeg-skill](../../catalog/tool/kajisho5__ffmpeg-skill.md), [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md), [video-use](../../catalog/tool/browser-use__video-use.md), [video-shotcraft](../../catalog/tool/vincentwei1021__video-shotcraft.md), [motion-design skill](../../catalog/tool/lottiefiles__motion-design-skill.md), [OpenMontage](../../catalog/tool/openmontageinc__openmontage.md), [remotion-superpowers](../../catalog/tool/dojocodinglabs__remotion-superpowers.md), [motion-skills (iArt)](../../catalog/tool/iart-ai__motion-skills.md), [motion-graphics (Mort1d)](../../catalog/tool/mort1d__motion-graphics-skills.md), [motion-video-director](../../catalog/tool/mattypark__motion-graphics-skill.md), [marketingskills](../../catalog/tool/coreyhaines31__marketingskills.md) |

## A minimal stack per kind of video

Every stack ends with [ffmpeg-skill](../../catalog/tool/kajisho5__ffmpeg-skill.md) for the platform check and contact sheet. Only the renderer skills were "run here once", in the [worked example](../../examples/hyperframes-vs-remotion/README.md); the rest is "read, not run".

| Kind | Records and what each adds | Still lacks |
|---|---|---|
| Code-driven motion graphics | [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md) or [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md): renderer rules. [motion-design skill](../../catalog/tool/lottiefiles__motion-design-skill.md): "Stagger total <500ms". [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md): frame inspection | audio and captions were not run; nobody watched the example clips at speed |
| Edited real footage | [video-use](../../catalog/tool/browser-use__video-use.md): cuts on word boundaries. [Auto-Editor](../../catalog/tool/wyattblue__auto-editor.md): `--preview` before a long render. [makemyclip editor](../../catalog/tool/makemyclip__editor.md): a cut check on local whisper.cpp | a run here; video-use transcription needs a paid ElevenLabs key as shipped |
| Generated footage | [arXiv 2606.07649](../../catalog/source/arxiv.org__abs__2606.07649.md): shot fields and two keyframe candidates per shot. [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md): continuity tolerance per feature. [arXiv 2604.24842](../../catalog/source/arxiv.org__abs__2604.24842.md): "local refinement is capped at 3 retries" | a skill that measures identity drift between shots |

## Make the skill actually load

In [Vercel's eval](../../catalog/source/vercel.com__blog__agents-md-outperforms-skills-in-our-agent-evals.md): "In 56% of eval cases, the skill was never invoked." The same page reports that "A compressed 8KB docs index embedded directly in AGENTS.md achieved a 100% pass rate, while skills maxed out at 79%". The record's notes say: put a short index of the renderer's rules, or a line naming which skill to load and when, in CLAUDE.md or AGENTS.md; "explore the project first, then invoke the skill" did better than "you MUST invoke the skill". One framework, one eval suite, and Vercel runs skills.sh. [Remotion](../../catalog/source/remotion.dev__docs__ai__mcp.md) reports the same for MCP. Run here once, the HyperFrames scaffold wrote an AGENTS.md and a CLAUDE.md into the project ([run log](../../examples/hyperframes-vs-remotion/results/hyperframes-runlog.md)).

## Before you install any of these

[skills.sh](../../catalog/source/skills.sh__docs.md) says it "cannot guarantee the quality or security of every skill listed", and [Snyk](../../catalog/source/snyk.io__blog__toxicskills-malicious-ai-agent-skills-clawhub.md) found 13.4% of skills scanned (534) with a critical issue; [a registry study](../../catalog/source/arxiv.org__abs__2605.11418.md) shows audit verdicts evaded by wording. [Fake stars](../../catalog/source/arxiv.org__abs__2412.13459.md) are bought at scale, and [clones](../../catalog/source/skills.sh__api__search__ai-video-generation.md) of one skill outrank the original. Read the skill first: the [HyperFrames skill](../../catalog/source/github.com__heygen-com__hyperframes__blob__main__skills__hyperframes__skill.md.md) asks the agent to send a usage beacon at start.

## Not covered yet

- A quoted skill rule for a type scale, a single left edge, or audio fades at cuts.
- Any skill run under Codex, or an independent before/after measurement of a skill.
- A skill that measures identity drift across generated shots.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
