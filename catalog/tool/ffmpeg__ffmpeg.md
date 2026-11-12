# FFmpeg

`tool:ffmpeg/ffmpeg` - tool - <https://ffmpeg.org/>

The command-line encoder and filter engine under almost every renderer here. Filtergraphs alone can cross-fade clips (xfade), burn in text (drawtext) and normalise loudness (loudnorm).

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Delivery](../../docs/glossary.md#delivery), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Also known as: ffmpeg, ffprobe, libav

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An agent can finish or assemble a clip with FFmpeg alone, and most render failures that reach the reader are FFmpeg input mismatches.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: established.

| field | value |
|---|---|
| tool_type | runtime |
| agents | none-stated |
| levers | motion, audio, captions, delivery |
| cost | free-local |

xfade fails unless both inputs share resolution, pixel format, frame rate and timebase: scale and fps-normalise first. loudnorm defaults to -24 LUFS integrated; set I= to the platform target yourself. drawtext exists only if your build was configured with libfreetype and libharfbuzz; run `ffmpeg -filters | grep drawtext` before relying on it. I did not check which flags the Homebrew build enables.

## Claims

1. xfade needs both inputs to match in frame rate, resolution, pixel format and timebase.

   > Both inputs must be constant frame-rate and have the same resolution, pixel format, frame rate and timebase.

   Locator: ffmpeg-filters, 11.292 xfade. Source: <https://ffmpeg.org/ffmpeg-filters.html>, retrieved 2026-11-12.

2. loudnorm defaults to an integrated loudness target of -24.

   > Range is -70.0 - -5.0. Default value is -24.0.

   Locator: ffmpeg-filters, 8.97 loudnorm, option I. Source: <https://ffmpeg.org/ffmpeg-filters.html>, retrieved 2026-11-12.

3. drawtext is only compiled in when FFmpeg is configured with libfreetype and libharfbuzz.

   > To enable compilation of this filter, you need to configure FFmpeg with --enable-libfreetype and --enable-libharfbuzz.

   Locator: ffmpeg-filters, 11.76 drawtext. Source: <https://ffmpeg.org/ffmpeg-filters.html>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. ffmpeg-filters.html sections xfade, loudnorm and drawtext against the claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `de713d78ed02106ab97410b2bbe763ad1f8372b5dff9461befa59d6cfcfdcf56`
- Lane: renderers

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2011-04-14
- default_branch: master
- fetched_at: 2026-11-12
- forks: 14614
- last_activity: 2026-11-12
- licence: unknown
- open_issues: 3
- sources: https://api.github.com/repos/ffmpeg/ffmpeg, https://skills.sh/api/search?q=ffmpeg
- stars: 67102

## Related

- integrates_with: [editly](mifi__editly.md)
- integrates_with: [MoviePy](zulko__moviepy.md)

## Referenced by

- [EBU R 128 - Loudness normalisation and permitted maximum level of audio signals](../source/tech.ebu.ch__publications__r128.md) (integrates_with)
- [PySceneDetect](breakthrough__pyscenedetect.md) (alternative_to)
- [MakeMyClip Editor](makemyclip__editor.md) (depends_on)
- [editly](mifi__editly.md) (depends_on)
- [Video & Audio Editing MCP Server](misbahsy__video-audio-mcp.md) (depends_on)
- [VMAF (libvmaf)](netflix__vmaf.md) (integrates_with)
- [MoviePy](zulko__moviepy.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
