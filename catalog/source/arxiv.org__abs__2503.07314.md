# MovieAgent: Automated Movie Generation via Multi-Agent CoT Planning

`source:arxiv.org/abs/2503.07314` - source - <https://arxiv.org/abs/2503.07314>

Show Lab paper and code: from a script synopsis and a character bank, LLM agents acting as director, screenwriter, storyboard artist and location manager plan scenes and shots, then image and video models render them with subtitles and audio.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Consistency](../../docs/glossary.md#consistency)

Also known as: MovieAgent

Tags: multi-shot, film-roles

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An early multi-agent movie pipeline (March 2025) that later systems (ViMax, Co-Director) use as a baseline and beat.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-11-12.

## Fit notes

Fit: low. Level: advanced. Maturity: -.

Consistency comes from per-character customisation (ROICtrl with a trained ED-LoRA per movie), so each new cast needs photos and a LoRA; the demo weights are for a commercial film's characters. The plan has no verifier step. Later papers score it below themselves: ViMax GC 0.4716 vs 0.5571, Co-Director 65.3 vs 81.4, both run by those rival authors. Needs a GPT-4o key; the image and video models are open weights. Code not run here.

## Claims

1. The planning is split across LLM agents named for film roles.

   > By employing multiple LLM agents to simulate the roles of a director, screenwriter, storyboard artist, and location manager, MovieAgent streamlines the production pipeline.

   Locator: arXiv 2503.07314 abstract. Source: <https://arxiv.org/abs/2503.07314>, retrieved 2026-11-12.

2. The supported model set is GPT-4o for planning, ROICtrl for character images and SVD or HunyuanVideo image-to-video for clips.

   > | GPT4-o | ROICtrl | SVD/HunyuanVideo_I2V |

   Locator: github.com/showlab/MovieAgent README, Supported Model Zoo. Source: <https://github.com/showlab/MovieAgent>, retrieved 2026-11-12.

3. Each character needs reference photos and an audio file in the input folder.

   > First, you need to prepare the `script synopsis of movie` and `photo,audio of character` as follow:

   Locator: github.com/showlab/MovieAgent README, Model and Data Preparation. Source: <https://github.com/showlab/MovieAgent>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. abstract, README model zoo and data preparation
- Next check due: 2027-11-12
- Licence: unknown
- URL status: live
- Saved source sha256: `b34cb0bce317dee9bb7e2c4bb7ef042a25f413f6261061a7ab388ad08cd18091`
- Citation: type article; author Weijia Wu, Zeyu Zhu, Mike Zheng Shou; issued 2025-03-10; container_title arXiv preprint; doi 10.48550/arXiv.2503.07314; url https://arxiv.org/abs/2503.07314; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Nothing collected yet.

## Related

None.

## Referenced by

- [ViMax](../tool/hkuds__vimax.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
