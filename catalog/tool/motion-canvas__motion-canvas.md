# Motion Canvas

`tool:motion-canvas/motion-canvas` - tool - <https://github.com/motion-canvas/motion-canvas>

A TypeScript library that programs vector animation with generators, plus a browser editor with live preview. Rendering is started from the editor.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Audio and captions](../../docs/glossary.md#audio-and-captions)

Also known as: motion-canvas

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Good for code explainers synced to voice-over, but its render step is a button in a browser editor, which an agent cannot press without browser automation.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | none-stated |
| levers | motion, audio |
| cost | free-local |

For an agent that must produce the MP4 itself, use Revideo, its fork with a headless render API. The default exporter writes an image sequence; MP4 needs the FFmpeg exporter. Snapshots of the current frame go to /still in the output folder, again from the editor. I did not check for a documented headless or CLI render path beyond the rendering page.

## Claims

1. It is a generator-based TypeScript library plus an editor for real-time preview, aimed at vector animation synced to voice-over.

   > It's a specialized tool designed to create informative vector animations and synchronize them with voice-overs.

   Locator: README.md, Motion Canvas. Source: <https://github.com/motion-canvas/motion-canvas/blob/main/README.md>, retrieved 2026-11-12.

2. Rendering starts from the RENDER button in the editor, which plays through the animation.

   > Clicking the RENDER button will initialize rendering

   Locator: motion-canvas.io docs, Rendering, Rendering. Source: <https://motion-canvas.io/docs/rendering>, retrieved 2026-11-12.

3. Without an extra exporter the output is an image sequence, not a video.

   > If you don't see this option, it means that you don't have any additional exporters installed and the default Image sequence exporter will be used.

   Locator: motion-canvas.io docs, Rendering, Exporter. Source: <https://motion-canvas.io/docs/rendering>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md and the docs Rendering page against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `4b7701ce1d31a80717dc873db69e4673f214e1e795b4e39ffd4ed8e0874441c3`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2022-08-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 894
- last_activity: 2026-07-02
- licence: MIT
- open_issues: 178
- sources: https://api.github.com/repos/motion-canvas/motion-canvas, https://skills.sh/api/search?q=motion-canvas
- stars: 19780

## Related

- alternative_to: [Revideo](midrender__revideo.md) - Revideo is forked from Motion Canvas and adds headless rendering.

## Referenced by

- [Revideo](midrender__revideo.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
