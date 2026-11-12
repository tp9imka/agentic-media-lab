# OpenAI Agent Skills (imagegen, speech)

`tool:openai/skills` - tool - <https://github.com/openai/skills>

OpenAI's catalogue of Codex skills, marked deprecated in favour of the openai/plugins repository. Its imagegen skill prefers the built-in Codex image tool, and its speech skill wraps the OpenAI speech endpoint with built-in voices.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Still images](../../docs/glossary.md#still-images)

Also known as: openai skills, imagegen skill, speech skill, $skill-installer

Tags: tts, voiceover, image-generation, disclosure, deprecated

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** These are the default image and voiceover hooks a Codex user meets, and the speech skill states the AI-voice disclosure rule an agent must pass on.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: dormant.

| field | value |
|---|---|
| tool_type | skill |
| agents | codex |
| levers | audio, asset, review-loop |
| cost | paid |

The speech skill defaults to gpt-4o-mini-tts-2025-12-15, and OpenAI's TTS guide says the gpt-4o-mini-tts models shut down on 2027-01-06, so the skill stops working then unless it is updated. Both skills need OPENAI_API_KEY for the CLI path and outbound network. The speech skill's codex-network.md suggests approval_policy = "never" to cut prompts; do not adopt that for an untrusted repo. The successor plugin creative-production is built around a Codex desktop board app and MCP tool, not a plain CLI. Licence per skill is in each LICENSE.txt, not read here. Not run here.

## Claims

1. The repository is deprecated; OpenAI points to openai/plugins instead.

   > **This repository is deprecated.** For current Codex skill and plugin examples, use the [OpenAI Plugins repository](https://github.com/openai/plugins).

   Locator: README.md, notice at the top. Source: <https://github.com/openai/skills/blob/main/README.md>, retrieved 2026-11-12.

2. The speech skill uses the built-in voices only; custom voice creation is outside it.

   > - Built-in voices only. Custom voices are out of scope for this skill.

   Locator: skills/.curated/speech/SKILL.md, Defaults & rules. Source: <https://github.com/openai/skills/blob/main/skills/.curated/speech/SKILL.md>, retrieved 2026-11-12.

3. Before shipping an important clip the speech skill asks the agent to check intelligibility, pacing and pronunciation, then change one thing at a time.

   > 6. For important clips, validate: intelligibility, pacing, pronunciation, and adherence to constraints. 7. Iterate with a single targeted change (voice, speed, or instructions), then re-check.

   Locator: skills/.curated/speech/SKILL.md, Workflow, steps 6-7. Source: <https://github.com/openai/skills/blob/main/skills/.curated/speech/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. openai/skills README, skills/.system/imagegen/SKILL.md, skills/.curated/speech/SKILL.md, speech references voiceover.md and codex-network.md, and openai/plugins creative-production README and produce SKILL.md, against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `a215225825369b96630c12476bd8536c2cbc5b887c1fa9c371db5d9cc4388079`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-11-25
- default_branch: main
- fetched_at: 2026-11-12
- forks: 2005
- last_activity: 2026-10-28
- licence: unknown
- open_issues: 297
- sources: https://api.github.com/repos/openai/skills, https://skills.sh/api/search?q=skills
- stars: 28704

## Related

- contradicts: [OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)](../model/openai__gpt-4o-mini-tts.md) - Skill default model is deprecated with shutdown 2027-01-06 per the TTS guide.
- integrates_with: [GPT Image 2](../model/openai__gpt-image.md)

## Referenced by

- [OpenAI TTS (gpt-4o-mini-tts, tts-1, tts-1-hd)](../model/openai__gpt-4o-mini-tts.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
