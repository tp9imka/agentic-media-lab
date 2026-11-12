# HN comment: keep generated clips 5-8 s and log model, host and defaults

`source:news.ycombinator.com/item/50396852` - source - <https://news.ycombinator.com/item?id=50396852>

A Hacker News comment (2026-11-06) from the operator of a multi-model generation site gives two rules for generated footage in an edit: keep each generated clip to 5-8 s and let the editor own continuity, and log the exact model, host and defaults with every file.

Concepts: [Generated footage](../../docs/glossary.md#generated-footage), [Consistency](../../docs/glossary.md#consistency), [Story and decomposition](../../docs/glossary.md#story-and-decomposition)

Tags: provenance-log, clip-length

**Badge:** quoted, not read at the primary source (`quoted-secondary`): source type community.

**Why:** Both rules are cheap to put in an agent's instructions, and the second is what makes a client revision reproducible weeks later.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Practice in one line: have the agent write a sidecar JSON per clip with model, version, host, mode, duration, seed and prompt. The commenter runs PixelDojo, a multi-model generator, and says so. No numbers behind the 5-8 s figure. Fits with the shot-splitting rules in source:arxiv.org/abs/2601.17737.

## Claims

1. Keep generated clips short, 5-8 s each, and let the editor handle continuity, colour and cleanup.

   > Keep generative clips short (5–8s atomic). Let the editor own continuity, color, and cleanup.

   Locator: comment 50396852, note 1. Source: <https://news.ycombinator.com/item?id=50396852>, retrieved 2026-11-12.

2. Log the exact model, host and defaults with each file; a bare model name cannot reproduce a revision.

   > Log exact model/host/defaults with the media. "Kling" without mode/duration/host is how you can't reproduce a client revision two weeks later.

   Locator: comment 50396852, note 2. Source: <https://news.ycombinator.com/item?id=50396852>, retrieved 2026-11-12.

## Provenance

- Source type: community
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. comment read through the HN Algolia API against the record
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `4fa9dc660d6d367f616166bfdd098d6492b5e6ee256c99ed56a2916975cde5db`
- Lane: radar-2026-11-12

## Observed

Nothing collected yet.

## Related

- extends: [The Script is All You Need: ScripterAgent and DirectorAgent for dialogue-to-cinematic video](arxiv.org__abs__2601.17737.md) - Same idea of fitting each shot to a short generation window.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
