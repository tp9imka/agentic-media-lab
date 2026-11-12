# How I Make $880/Day with AI Motion Design (Sanji Nai-Chien, video)

`source:youtu.be/d5qpbbewtxo` - source - <https://www.youtube.com/watch?v=D5qpBbEWTxo>

A YouTuber builds a 30 s SaaS launch video with Claude Opus 5.5 and a custom motion skill, shows the broken first render and the cause of each bug, shows the same prompt without a storyboard, and compares the result with a $1,000 human motion designer on the same brief.

Concepts: [Motion and transitions](../../docs/glossary.md#motion-and-transitions), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Visual design](../../docs/glossary.md#visual-design)

Tags: storyboard, fonts, motion-skill

**Badge:** quoted, not read at the primary source (`quoted-secondary`): primary source read; downgraded one step: interested-party.

**Why:** The first-render bug list names causes an agent can fix in one line: Figma frames at 1440 px in a 1920 px canvas, and a font not loaded before the first frame. The no-storyboard run shows what skipping the plan costs.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

Add both fixes to a motion prompt: lock the canvas to the output size and position from the centre, and load fonts before frame 0 (in Remotion, delayRender until the font loads). The renderer is not named in the transcript. The human-versus-agent part is one brief judged by the author, and the description links the skill through a higgsfield.ai referral link; the channel sells a way to make money with AI. The skill itself was not opened. Transcript only; the video was not watched.

## Claims

1. The first render's layout broke because the Figma screens were 1440 px wide and the video was 1920 px.

   > The layout exploded because the Figma screens were designed 1440 pixels wide, and the video we asked for is 1920.

   Locator: transcript 12:29-12:36. Source: <https://www.youtube.com/watch?v=D5qpBbEWTxo>, retrieved 2026-11-12.

2. The font fell back to Times New Roman because it was not loaded before the first frame.

   > The font, on the other hand, broke because it wasn't loaded before the first frame.

   Locator: transcript 12:45-12:49. Source: <https://www.youtube.com/watch?v=D5qpBbEWTxo>, retrieved 2026-11-12.

3. Without a storyboard, the same assets, skill and prompt gave scenes in random order with everything moving at once.

   > Scenes come in in a totally random order. Everything moves at the same time and there's just no coherent story.

   Locator: transcript 14:19-14:26. Source: <https://www.youtube.com/watch?v=D5qpBbEWTxo>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. description and English auto-caption transcript (YouTube timedtext) against the record; the video itself was not watched
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `c0ab78f967f0c9f63f948a4dbb0f4970f193ff0d8508d258ca2875caa4230651`
- Badge downgraded: interested-party - The description links the author's skill through a referral link and the video sells the workflow.
- Lane: radar-2026-11-12

## Observed

Nothing collected yet.

## Related

- extends: [I Quit Remotion After Claude Made These Motion Graphics (Guney Topcu, video)](youtu.be__fvvrcpcfjyk.md) - Both are storyboard-first, agent-made motion graphics videos with a comparison judged by the author.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
