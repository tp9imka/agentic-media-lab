# The Script is All You Need: ScripterAgent and DirectorAgent for dialogue-to-cinematic video

`source:arxiv.org/abs/2601.17737` - source - <https://arxiv.org/abs/2601.17737>

Tencent paper: ScripterAgent (a trained model) turns dialogue into a shot-level cinematic script, DirectorAgent splits it into model-sized segments and chains them by last frame, and CriticAgent (gemini-2.5-pro) scores scripts and videos. Adds ScriptBench and a Visual-Script Alignment metric.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Consistency](../../docs/glossary.md#consistency), [Model prompting](../../docs/glossary.md#model-prompting)

Also known as: ScripterAgent, DirectorAgent, CriticAgent, ScriptBench, VSA metric

Tags: frame-anchoring, last-frame

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Its DirectorAgent rules (cut at shot boundaries, fit each segment to the model window with a 10% buffer, feed the last frame forward) are a technique any pipeline can copy if its video model accepts a conditioning image.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-11-12.

## Fit notes

Fit: high. Level: advanced. Maturity: -.

The last-frame relay needs a model with image-to-video or first-frame input; the paper ran it on Sora2-Pro, Veo3.1, Kling2.6, Wan2.6, Seedance1.5-Pro and HYVideo1.5. The script model is a trained one; training is out of this hub's scope, so read it for the segmentation rules. The paper lists github.com/Tencent/digitalhuman (ScriptAgent folder) as code; not opened here. Lip sync is a stated weak spot.

## Claims

1. DirectorAgent segments at shot boundaries and conditions each segment on the last frame of the one before.

   > This strategy combines (1) intelligent, shot-aware segmentation that respects cinematographic boundaries with (2) a frame-anchoring mechanism that conditions each new segment on the final state of the previous one.

   Locator: arXiv 2601.17737 HTML, DirectorAgent. Source: <https://arxiv.org/html/2601.17737>, retrieved 2026-11-12.

2. Each segment is sized to the video model's generation window with a 10% safety margin.

   > Duration Adaptation: The total duration of a scene is constrained to fit within the target model’s generation window, with a 10% safety buffer.

   Locator: arXiv 2601.17737 HTML, Intelligent Shot-Based Segmentation. Source: <https://arxiv.org/html/2601.17737>, retrieved 2026-11-12.

3. In their tests HYVideo1.5 led on script faithfulness and character consistency while Sora2-Pro led on visual appeal.

   > Conversely, HYVideo1.5 prioritizes narrative integrity, leading in Script Faithfulness (4.6), Character Consistency (4.4), and Narrative Coherence (4.3).

   Locator: arXiv 2601.17737 HTML, results on video generation. Source: <https://arxiv.org/html/2601.17737>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `bd43119c30532b948736978ac4822a82532b0e1353e0d18e97bea9d77121652c`
- Citation: type article; author Chenyu Mu, Xin He, Qu Yang, Wanshun Chen, Jiadi Yao, Huang Liu, Zihao Yi, Bo Zhao, Xingyu Chen, Ruotian Ma, Fanghua Ye, Erkun Yang, Cheng Deng, Zhaopeng Tu, Xiaolong Li, Linus; issued 2026-01-25; container_title arXiv preprint; doi 10.48550/arXiv.2601.17737; url https://arxiv.org/abs/2601.17737; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

- [HN comment: keep generated clips 5-8 s and log model, host and defaults](news.ycombinator.com__item__50396852.md) (extends)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
