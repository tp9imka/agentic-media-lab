# HyperFrames vs Remotion (HeyGen guide)

`source:hyperframes.heygen.com/guides/hyperframes-vs-remotion` - source - <https://hyperframes.heygen.com/guides/hyperframes-vs-remotion>

HeyGen's own comparison of HyperFrames and Remotion, with one agent run on each and a table of how timing, licence and existing web material differ.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Licences and territory](../../docs/glossary.md#licences-and-territory), [Evaluation](../../docs/glossary.md#evaluation)

**Badge:** quoted, not read at the primary source (`quoted-secondary`): primary source read; downgraded one step: interested-party.

**Why:** The vendor of one side states where the other is better and admits HyperFrames fails quietly when its rules are broken. Read it as a party with an interest.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Written by HeyGen, which makes HyperFrames. The test was one run each, and the page itself says it decides nothing about quality. Its Remotion licence line matches Remotion's LICENSE.md. The 'no node_modules installed' row is about the project folder; the CLI still needs Node 22 and FFmpeg.

## Claims

1. HyperFrames breaks quietly if an agent does not follow its rules: paused timeline, no wall clocks, no unseeded randomness.

   > HyperFrames asks you to follow rules — paused timeline, no wall clocks, no unseeded randomness — and breaks quietly if you don’t.

   Locator: Section What Remotion does better. Source: <https://hyperframes.heygen.com/guides/hyperframes-vs-remotion>, retrieved 2026-11-12.

2. A HyperFrames timeline that is not registered on window.__timelines renders as a still frame with no motion.

   > Miss the last one and you get a still frame with no motion.

   Locator: Section The same title card, written both ways. Source: <https://hyperframes.heygen.com/guides/hyperframes-vs-remotion>, retrieved 2026-11-12.

3. Its one-run test says a single run decides nothing about quality.

   > Both are good videos; a single run decides nothing about quality.

   Locator: Section Same request, two agents. Source: <https://hyperframes.heygen.com/guides/hyperframes-vs-remotion>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. visible page text against the claims and against Remotion LICENSE.md
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `f3eac858117992fd1e9791abfdc69f443b6657ed07666c31f7b7bf26c3f8719a`
- Badge downgraded: interested-party - HeyGen makes HyperFrames.
- Lane: renderers

## Observed

Nothing collected yet.

## Related

- evaluated_on: [HyperFrames](../tool/heygen-com__hyperframes.md)
- evaluated_on: [Remotion](../tool/remotion-dev__remotion.md)

## Referenced by

- [HyperFrames vs Remotion research note (GenMotion)](github.com__haxzie__genmotion__blob__main__docs__research__hyperframes-remotion.md.md) (alternative_to)
- [HyperFrames issue 4435: parallel render workers capture a blank first frame](github.com__heygen-com__hyperframes__issues__4435.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
