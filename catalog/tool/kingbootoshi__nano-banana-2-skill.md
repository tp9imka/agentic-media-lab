# Nano Banana 2 Skill

`tool:kingbootoshi/nano-banana-2-skill` - tool - <https://github.com/kingbootoshi/nano-banana-2-skill>

A Bun CLI, also packaged as a Claude Code skill, that calls Gemini image models with size, aspect ratio, reference images, cost logging and a green-screen transparency mode.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Still images](../../docs/glossary.md#still-images), [Cost](../../docs/glossary.md#cost)

Also known as: nano-banana CLI, nano-banana-2-skill

Tags: image-generation, thumbnail, transparency, gemini

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives Claude Code a one-line route to 16:9 or 9:16 stills with a cost log, and transparent PNG overlays for compositing.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code |
| levers | asset, design |
| cost | paid |

The /init step has the agent clone the repo, run bun install and link a global command, which is remote code on your machine: read the repo first. The key is stored in plain text at ~/.nano-banana/.env. Its cost table matches Google's gemini-3.1-flash-image prices read on 2026-11-12 ($0.067 per 1K image); gemini-nano-banana-2.1 is $0.0336 on the same page and is not the default. Transparent mode needs ffmpeg and ImageMagick and keys out green, so green subjects lose pixels. Not run here.

## Claims

1. Installing it as a skill makes the agent clone the repo, install dependencies and link the command.

   > When installed as a Claude Code skill, just say `/init` and Claude will clone the repo, install deps, and link the command for you.

   Locator: README.md, As a Claude Code Skill. Source: <https://github.com/kingbootoshi/nano-banana-2-skill/blob/main/README.md>, retrieved 2026-11-12.

2. Its cost table gives about $0.067 per 1K image for the Flash default and twice that for Pro.

   > | `1K` | ~1024x1024 | ~$0.067 | ~$0.134 |

   Locator: README.md, Sizes and Costs table. Source: <https://github.com/kingbootoshi/nano-banana-2-skill/blob/main/README.md>, retrieved 2026-11-12.

3. Transparency works by generating on a green screen and keying it out with FFmpeg.

   > The `-t` flag automatically prompts the AI to generate on a green screen, then uses FFmpeg `colorkey` + `despill` to key out the background and remove green spill from edge pixels.

   Locator: README.md, Transparent Assets. Source: <https://github.com/kingbootoshi/nano-banana-2-skill/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. kingbootoshi/nano-banana-2-skill README against the claims; cost table compared with the Gemini API pricing page read for model:google/gemini-tts
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `446c4d06e12dc032e8d96bce4d55c45bfabd38d80fd0855280bbf39c00670f13`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-02-24
- default_branch: main
- fetched_at: 2026-11-12
- forks: 50
- installs: 679
- installs_by_skill: {"nano-banana": 679}
- last_activity: 2026-10-31
- licence: MIT
- open_issues: 6
- registry: skills.sh
- sources: https://api.github.com/repos/kingbootoshi/nano-banana-2-skill, https://skills.sh/api/search?q=nano-banana-2-skill
- stars: 418

## Related

- integrates_with: [Nano Banana (Gemini image models)](../model/google__nano-banana.md)
- alternative_to: [Nano Banana extension for Gemini CLI](gemini-cli-extensions__nanobanana.md)

## Referenced by

- [Nano Banana extension for Gemini CLI](gemini-cli-extensions__nanobanana.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
