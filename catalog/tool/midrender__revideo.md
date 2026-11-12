# Revideo

`tool:midrender/revideo` - tool - <https://github.com/midrender/revideo>

A TypeScript engine for video in code, forked from Motion Canvas, with a headless renderVideo() API and a React player for preview. It renders through Node and a headless browser.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: redotvideo/revideo, @revideo/core

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives the Motion Canvas authoring model a render call an agent can run, and it names Claude and Codex as authors.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | renderer |
| agents | claude-code, codex |
| levers | motion, audio |
| cost | free-local |

The repo moved from redotvideo/revideo to midrender/revideo and is the engine behind the Midrender product. It counts renders through PostHog unless you set DISABLE_TELEMETRY=true. The README says it borrows from Remotion and Rive while its docs say it is a Motion Canvas fork; both can be true, but expect Motion Canvas APIs. I did not find a documented single-frame still command in what I read.

## Claims

1. Its README names Claude and Codex as able to write a scene, because a scene is plain TypeScript.

   > A scene is plain TypeScript, so Claude or Codex can produce one from a prompt.

   Locator: README.md, Revideo. Source: <https://github.com/midrender/revideo/blob/main/README.md>, retrieved 2026-11-12.

2. Headless rendering runs wherever Node and a headless browser run.

   > It runs anywhere Node and a headless browser run

   Locator: README.md, Capabilities, Headless rendering. Source: <https://github.com/midrender/revideo/blob/main/README.md>, retrieved 2026-11-12.

3. It anonymously counts rendered videos and can be switched off with an environment variable.

   > Revideo anonymously counts how many videos are rendered

   Locator: README.md, Telemetry. Source: <https://github.com/midrender/revideo/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and the docs welcome page against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `27b5c7bf9de6018a718ef5e27ac194d48157474815276d6b1e916b986ffa43b0`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2024-03-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 220
- last_activity: 2026-07-15
- licence: MIT
- open_issues: 63
- sources: https://api.github.com/repos/midrender/revideo, https://skills.sh/api/search?q=revideo
- stars: 4205

## Related

- extends: [Motion Canvas](motion-canvas__motion-canvas.md)

## Referenced by

- [Motion Canvas](motion-canvas__motion-canvas.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
