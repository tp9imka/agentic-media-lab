# video-use

`tool:browser-use/video-use` - tool - <https://github.com/browser-use/video-use>

A skill for cutting raw footage into a finished video by conversation, with hard audio and cut rules and a self-evaluation pass on the rendered file.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Agent Skills](../../docs/glossary.md#agent-skills), [Review loop](../../docs/glossary.md#review-loop), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: browser-use video-use

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The clearest example of a skill that inspects its own output at every cut before handing it over.

**Last checked:** 2026-11-12, primary-read, by agent:driver. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, hermes |
| levers | motion, audio, captions, review-loop |
| cost | paid |

Transcription uses a paid ElevenLabs key, so it is not a free local path as shipped. Its README tells the agent to ask you to paste the key into chat; set it in the environment yourself.

## Claims

1. It forbids cutting inside a word and snaps cuts to transcript word boundaries.

   > **Never cut inside a word.** Snap every cut edge to a word boundary from the Scribe transcript.

   Locator: SKILL.md, Hard Rules, rule 6. Source: <https://github.com/browser-use/video-use/blob/main/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:driver, depth primary-read. SKILL.md against the claim
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `d3bbeb19bc0e81e197d74806fba15e0a5f5694a0cdf33f0a2348bffe8472a27b`
- Lane: quality-skills

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
