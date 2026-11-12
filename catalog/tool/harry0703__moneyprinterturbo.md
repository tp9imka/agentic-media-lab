# MoneyPrinterTurbo

`tool:harry0703/moneyprinterturbo` - tool - <https://github.com/harry0703/MoneyPrinterTurbo>

A topic-to-short-video app: an LLM writes the script, the app matches stock or generated footage, adds TTS voiceover, subtitles and music, and renders the file. It runs as WebUI, API, CLI or through an agent skill.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Cost](../../docs/glossary.md#cost), [Popularity and trust](../../docs/glossary.md#popularity-and-trust)

Tags: stock-footage, edge-tts, short-video

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** A widely used template-style pipeline that can run on free stock footage and free TTS; it has no shot planning for consistency and no step that checks the output.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | any-skill |
| levers | orchestration, audio, captions, asset, delivery |
| cost | mixed |

Cheapest route in this lane: stock footage from Pexels or Pixabay and Edge TTS, plus an LLM key. The skill route has the agent fetch a remote SKILL.md, install the app and ask for missing API keys during the chat; read that SKILL.md first and set keys in config.toml yourself. The README is dense with sponsor and referral links. It also offers voice cloning from reference audio; this hub does not cover that feature. Nothing in the README inspects the render before delivery. Not run here.

## Claims

1. From a topic or keyword it writes the script, matches footage, adds subtitles and music and renders a short video.

   > Provide a video <b>topic</b> or <b>keyword</b>, and MoneyPrinterTurbo will generate the script, match footage, create subtitles and background music, and produce an HD short video.

   Locator: README-en.md, header. Source: <https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README-en.md>, retrieved 2026-11-12.

2. A GPU is optional; it only speeds up local transcription and processing.

   > A GPU is not required, but it is recommended if you want faster local transcription, faster video processing, or smoother batch generation

   Locator: README-en.md, requirements. Source: <https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README-en.md>, retrieved 2026-11-12.

3. The agent route installs the app from a remote skill file and asks the user for missing API keys; it supports macOS and Windows.

   > It will ask only for required API keys that are not already configured. This workflow currently supports macOS and Windows.

   Locator: README-en.md, Generate Videos with an AI Agent. Source: <https://github.com/harry0703/MoneyPrinterTurbo/blob/main/README-en.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. English README features, requirements and agent workflow sections
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `2cdbbcfa59e42512189d12dbd5eaf0fec9cd877df7f3bed262545ad3aae3d935`
- Lane: pipelines-research

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2024-03-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 22831
- installs: 288
- installs_by_skill: {"moneyprinterturbo-video": 288}
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 79
- registry: skills.sh
- sources: https://api.github.com/repos/harry0703/MoneyPrinterTurbo, https://skills.sh/api/search?q=MoneyPrinterTurbo
- stars: 142725
- Popularity: installs and stars differ by more than 100x

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
