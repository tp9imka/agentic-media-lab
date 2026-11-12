# OpenDirector

`tool:seme-org/open-director` - tool - <https://github.com/seme-org/open-director>

A self-hosted Docker studio where nine LangGraph agents (research, script, art style, storyboard, character, location, voice, music, media) turn one sentence into a storyboard of generated stills with voiceover and music, then render a video.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Consistency](../../docs/glossary.md#consistency), [Still images](../../docs/glossary.md#still-images)

Tags: langgraph, docker, storyboard

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Shows the reference-image route to character consistency in a small, readable stack, and names the model setting that silently breaks it.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | none-stated |
| levers | orchestration, story, consistency, audio |
| cost | mixed |

Paid parts: a WaveSpeed key for images and an OpenAI-compatible LLM (default gpt-4o-mini; Ollama is listed). The nine agents include no reviewer, so nothing checks the frames. The pipeline in the README generates images, not video-model clips. The README calls Edge TTS local; Edge TTS is usually a Microsoft online voice service (not verified here). docker compose ships fixed default MinIO credentials; change them before exposing the host. Not run here.

## Claims

1. Storyboard frames that show a character must go through an image-to-image or edit model so the character reference is used.

   > OpenDirector uses WaveSpeed for image generation. Character and location plates use a text-to-image model, while storyboard frames with character references must use an image-to-image/edit model so reference images are honored.

   Locator: README.md, Media Generation. Source: <https://github.com/seme-org/open-director>, retrieved 2026-11-12.

2. Setting the image-to-image model to the plain nano-banana alias sends frames to a text-to-image endpoint that can ignore character references.

   > Do not set `WAVESPEED_IMAGE_TO_IMAGE_MODEL` to `nano-banana`: that alias routes to a text-to-image endpoint and can ignore character reference images.

   Locator: README.md, Media Generation. Source: <https://github.com/seme-org/open-director>, retrieved 2026-11-12.

3. The default MinIO console runs with fixed credentials.

   > | MinIO Console | http://localhost:9001 | `opendirector` / `opendirector-secret` |

   Locator: README.md, Default services table. Source: <https://github.com/seme-org/open-director>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README pipeline, media generation, LLM and services sections
- Next check due: 2027-02-10
- Licence: LGPL-3.0
- URL status: live
- Saved source sha256: `761ce2662c1295ec211935e6cd17b83aea0c94307d58a4c95b3301b96c0bcab9`
- Lane: pipelines-research

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-05-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 25
- last_activity: 2026-05-29
- licence: LGPL-3.0
- open_issues: 1
- sources: https://api.github.com/repos/seme-org/open-director, https://skills.sh/api/search?q=open-director
- stars: 132

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
