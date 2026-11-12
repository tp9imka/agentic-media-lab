# Nano Banana extension for Gemini CLI

`tool:gemini-cli-extensions/nanobanana` - tool - <https://github.com/gemini-cli-extensions/nanobanana>

A Gemini CLI extension with an MCP server that adds /generate, /edit, /icon, /diagram and related commands backed by the Gemini image models.

Concepts: [MCP servers](../../docs/glossary.md#mcp-servers), [Still images](../../docs/glossary.md#still-images), [Image models](../../docs/glossary.md#image-models)

Also known as: nanobanana, gemini-cli nanobanana

Tags: image-generation, thumbnail, diagram, gemini

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the first-party-adjacent hook for Gemini image generation from a terminal agent, including icon and diagram presets for explainer stills.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | gemini-cli |
| levers | asset, design |
| cost | paid |

Built for Gemini CLI; use from Claude Code or Codex is not documented in the README. Its default model id is gemini-3.1-flash-image-preview; the Gemini pricing page read on 2026-11-12 lists gemini-3.1-flash-image at $0.067 per 1K image and gemini-nano-banana-2.1 at half that, and it was not checked whether the -preview alias still answers. Needs a paid Gemini key in NANOBANANA_API_KEY. Images land in ./nanobanana-output/. Not run here.

## Claims

1. Nano Banana 2 under the preview id is the default model; NANOBANANA_MODEL switches it.

   > Nano Banana 2 (`gemini-3.1-flash-image-preview`) is now the default model (v1.0.11+)!

   Locator: README.md, notice at the top. Source: <https://github.com/gemini-cli-extensions/nanobanana/blob/main/README.md>, retrieved 2026-11-12.

2. It needs a Gemini API key in NANOBANANA_API_KEY.

   > **API Key**: Set the `NANOBANANA_API_KEY` environment variable with your Gemini API key.

   Locator: README.md, Prerequisites, item 3. Source: <https://github.com/gemini-cli-extensions/nanobanana/blob/main/README.md>, retrieved 2026-11-12.

3. Generated images go to a fixed subdirectory.

   > Generated images are saved to `./nanobanana-output/` which is created automatically.

   Locator: README.md, Output Directory. Source: <https://github.com/gemini-cli-extensions/nanobanana/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. gemini-cli-extensions/nanobanana README against the claims; model ids compared with the Gemini API pricing page read for model:google/gemini-tts
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `b6242eac1241dee7856c1301421c8174c20f9791b8a18f25532907646192b75e`
- Lane: media-stages

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-09-19
- default_branch: main
- fetched_at: 2026-11-12
- forks: 133
- last_activity: 2026-06-25
- licence: Apache-2.0
- open_issues: 51
- sources: https://api.github.com/repos/gemini-cli-extensions/nanobanana, https://skills.sh/api/search?q=nanobanana
- stars: 1131

## Related

- integrates_with: [Nano Banana (Gemini image models)](../model/google__nano-banana.md) - Default is not the 2.1 model named on Google's pricing page.
- alternative_to: [Nano Banana 2 Skill](kingbootoshi__nano-banana-2-skill.md)

## Referenced by

- [Nano Banana 2 Skill](kingbootoshi__nano-banana-2-skill.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
