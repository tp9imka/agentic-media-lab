# ViMax

`tool:hkuds/vimax` - tool - <https://github.com/HKUDS/ViMax>

A multi-agent video framework from HKUDS that turns an idea, a screenplay or a novel into a multi-scene, multi-shot video. Agents write the script, plan shots and a camera dependency graph, generate keyframes and clips, pick the best keyframe with a VLM judge, and assemble the cut.

Concepts: [Agentic pipelines](../../docs/glossary.md#agentic-pipelines), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Consistency](../../docs/glossary.md#consistency), [Review loop](../../docs/glossary.md#review-loop), [Generated footage](../../docs/glossary.md#generated-footage)

Also known as: ViMax agentic video generation, ViMax-Bench, Idea2Video, Script2Video, Novel2Video

Tags: multi-shot, storyboard, vlm-judge, best-of-k

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The most complete open-source idea-to-video pipeline found in this lane, with a paper that states its cost per story and admits it depends on proprietary models.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: advanced. Maturity: active.

| field | value |
|---|---|
| tool_type | framework |
| agents | none-stated |
| levers | orchestration, story, consistency, review-loop |
| cost | paid |

Needs API keys for an LLM, an image model and a video model; the paper default is Gemini-3-Flash, Gemini-3-Pro-Image and Veo 3.1, so a run is paid. The paper also ran Wan2.2 as the clip backend, the only open-weights route it reports. The README lists Linux and Windows as the OS; macOS is not listed and was not tried here. Its VLM check only chooses among keyframes, it does not re-check the finished clips, and the paper says audio and dialogue sync are not handled. The AutoCameo mode puts a person from a photo into the story; this hub does not cover that mode. Whether ViMax-Bench (35 GPT-5.2-written stories) is downloadable was not checked. Not run here.

## Claims

1. At the paper's default setting (best-of-2 keyframes) one ViMax-Bench story costs about 17.50 USD in API fees and 405 s end to end.

   > Best-of-2 yields Overall GC of 0.5571 at an average cost of $17.500 and 405s per task.

   Locator: arXiv 2606.07649 HTML, sec. on Best-of-k ablation. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

2. The VLM judge picks the best of k keyframes per shot, not the best of several videos.

   > This selection operates at the keyframe stage, not as parallel video generation.

   Locator: arXiv 2606.07649 HTML, sec. on Best-of-k ablation. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

3. The authors state that reasoning, keyframes, video and quality control all run on proprietary models, so results move when those models update.

   > First, the system depends on proprietary foundation models for reasoning, keyframe and video generation, and VLM-based quality control, making performance sensitive to model updates.

   Locator: arXiv 2606.07649 HTML, Limitations. Source: <https://arxiv.org/html/2606.07649>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README quick start and features; paper abstract, method, ablations, limitations against the claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `5e772aff1df631e0de2e0d0d8d108001649dcfcb26a41246049926af7d435f69`
- Citation: type article; author Lingxuan Huang, Sizhe He, Hengji Zhou, Liqiang Nie, Lianghao Xia, Chao Huang; issued 2026-06-02; container_title arXiv preprint; doi 10.48550/arXiv.2606.07649; url https://arxiv.org/abs/2606.07649; accessed 2026-11-12
- Lane: pipelines-research

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-03-30
- default_branch: main
- fetched_at: 2026-11-12
- forks: 1954
- last_activity: 2026-09-30
- licence: MIT
- open_issues: 55
- sources: https://api.github.com/repos/HKUDS/ViMax, https://skills.sh/api/search?q=ViMax
- stars: 12901

## Related

- alternative_to: [MovieAgent: Automated Movie Generation via Multi-Agent CoT Planning](../source/arxiv.org__abs__2503.07314.md) - MovieAgent is a baseline in ViMax Table 1 (GC 0.4716 vs 0.5571).

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
