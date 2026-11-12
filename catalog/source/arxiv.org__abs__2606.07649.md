# ViMax: Agentic Video Generation (arXiv 2606.07649)

`source:arxiv.org/abs/2606.07649` - source - <https://arxiv.org/abs/2606.07649>

A multi-agent pipeline paper: screenwriting, hierarchical story decomposition, a storyboard agent that plans shots, keyframe generation with a VLM judge, then video per shot.

Concepts: [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Review loop](../../docs/glossary.md#review-loop)

Tags: shot-planning, storyboard

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It names the fields a shot spec should carry and reports measured cost and quality for keyframe best-of-k, which sets a default for a review loop.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: medium. Level: advanced. Maturity: -.

Copy the shot-spec fields into your own shot-list schema, and default to two keyframe candidates per shot before spending on video. The 17.5 USD per task is on the paper's own benchmark with Gemini-3-Flash as backbone; it is not a price for the reader's clip. Authors' own evaluation, not reproduced here.

## Claims

1. Each planned shot carries camera angle, movement, lighting, character positions and duration.

   > contains comprehensive production details including camera angles, movements, lighting conditions, character positioning, and temporal duration, providing the technical blueprint for subsequent video generation stages.

   Locator: HTML, section on Shot Planning. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

2. Two keyframe candidates per shot scored best; three or four cost more and scored lower.

   > Best-of-2 yields Overall GC of 0.5571 at an average cost of $17.500 and 405s per task.

   Locator: HTML, Best-of-k study. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

3. Replacing the storyboard agent with plain screenplay segmentation cut a visual score from 4.94 to 3.10.

   > Replacing StoryboardArtist with deterministic screenplay segmentation preserves story order and shot count but removes agent-based visual articulation; VSU falls from 4.94 to 3.10

   Locator: HTML, ablation, Narrative-Planning Components. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `a6d7a006328f69c789d9fd351a41658730c58757331f881ce1a1bfa39eea9e9c`
- Citation: type article; author Lingxuan Huang, Sizhe He, Hengji Zhou, Liqiang Nie, Lianghao Xia, Chao Huang; issued 2026; container_title arXiv; url https://arxiv.org/abs/2606.07649; accessed 2026-11-12
- Lane: craft

## Observed

Nothing collected yet.

## Related

- alternative_to: [Co-Director: Agentic Generative Video Storytelling (arXiv 2604.24842)](arxiv.org__abs__2604.24842.md)

## Referenced by

- [Co-Director: Agentic Generative Video Storytelling (arXiv 2604.24842)](arxiv.org__abs__2604.24842.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
