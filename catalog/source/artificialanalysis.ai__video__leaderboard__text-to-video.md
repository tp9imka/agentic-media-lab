# Artificial Analysis Video Arena: text-to-video and image-to-video leaderboards

`source:artificialanalysis.ai/video/leaderboard/text-to-video` - source - <https://artificialanalysis.ai/video/leaderboard/text-to-video>

A leaderboard that ranks video models by Elo from blind pairwise human votes, with 95% intervals, sample counts and a per-minute API price per model.

Concepts: [Evaluation](../../docs/glossary.md#evaluation), [Hosted video models](../../docs/glossary.md#hosted-video-models)

Also known as: AA-Video-T2V v2.1, Artificial Analysis video arena, AA leaderboard

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the most used public ranking of hosted video models, and it shows rank ranges, so close models can be read as ties.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2026-12-12.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Read 2026-11-12. The top five on text-to-video have overlapping 95% intervals (Wan 3.0 1162-1188 down to Gemini Omni Flash 1.2 1140-1168), so the order among them is not settled. Utopai X ranks second with 'No API available'. Prices are per minute at 1080p where offered, so they differ from cheaper 480p or 720p runs. Votes come from the vendor's own evaluator pool; method details beyond the page FAQ were not read. The video-editing and open-weights views were not opened.

## Claims

1. On 2026-11-12 the text-to-video top five were Wan 3.0 (1175), Utopai X (1170), MiniMax H3 768p (1161), Dreamina Seedance 2.5 (1155) and Gemini Omni Flash 1.2 (1154).

   > The top models on AA-Video-T2V v2.1 by Elo rating are: 1. Wan 3.0 (Elo 1175), 2. Utopai X (Elo 1170), 3. MiniMax H3 (768p) (Elo 1161), 4. Dreamina Seedance 2.5 (Elo 1155), and 5. Gemini Omni Flash 1.2 (Elo 1154).

   Locator: Text-to-video leaderboard, FAQ 'What are the top models'. Source: <https://artificialanalysis.ai/video/leaderboard/text-to-video>, retrieved 2026-11-12.

2. Models are ranked by Elo from blind comparisons of two videos made from the same prompt, judged by the site's own evaluators.

   > Models are ranked using an Elo rating system derived from blind comparisons judged by our validated private evaluators. Voters compare two videos generated from the same text prompt without knowing which model created each video.

   Locator: Text-to-video leaderboard, FAQ 'How are Text to Video models ranked'. Source: <https://artificialanalysis.ai/video/leaderboard/text-to-video>, retrieved 2026-11-12.

3. On image-to-video, Dreamina Seedance 2.5 ranked first (1161, range 1-2) and Utopai X second (1151, range 1-3).

   > | 1 | 1-2 | Dreamina Seedance 2.5 | 1161±1595% interval 1146 to 1176 | 6,540 | Jul 2026 | $34.12 /min | 2 | 1-3 | Utopai X | 1151±1495% interval 1137 to 1165

   Locator: Image-to-video leaderboard, table rows 1-2. Source: <https://artificialanalysis.ai/video/leaderboard/image-to-video>, retrieved 2026-11-12.

## Provenance

- Source type: independent-secondary
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Artificial Analysis text-to-video and image-to-video leaderboard pages against all three claims
- Next check due: 2026-12-12
- Licence: unknown
- URL status: live
- Saved source sha256: `48b02e290586d6e7f4c698f9af4b3195fd10e5a9b2e61a0d580aca1ec12b28b7`
- Lane: hosted-models-2

## Observed

Nothing collected yet.

## Related

- evaluated_on: [Wan 3.0](../model/alibaba__wan.md)
- evaluated_on: [Dreamina Seedance 2.5](../model/bytedance__seedance.md)

## Referenced by

- [Wan 3.0](../model/alibaba__wan.md) (evaluated_on)
- [Dreamina Seedance 2.5](../model/bytedance__seedance.md) (evaluated_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
