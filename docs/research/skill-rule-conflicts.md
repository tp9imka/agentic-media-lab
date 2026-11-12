---
id: guide:skill-rule-conflicts
title: "Where the skills contradict each other, and what the standards say"
summary: Lists each conflict between skill rules that the hub's records document, with both positions quoted and the standards record that decides it, if any.
use_when: "Use this page when two video skills give your agent opposite rules and you need to know which one a standard backs."
concepts: [concept:craft, concept:motion-and-transitions, concept:visual-design, concept:audio-and-captions, concept:review-loop, concept:licences-and-territory, concept:agent-skills]
last_reviewed: 2026-11-12
---

# Where the skills contradict each other, and what the standards say

For a developer who loads more than one video skill into Claude Code or Codex. Read [which skill fixes which problem](../cheatsheets/quality-skill-stack.md) first. All rules here are "read, not run"; one wins only where a standards or licensor record decides it.

## Idle motion

[claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md) has a rule that idle elements breathe, which its record says contradicts [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md). [smooth-animation-skill](../../catalog/tool/flchntc__smooth-animation-skill.md) has a "no still scenes" rule, which its record says contradicts the calm holds other skills allow. Neither record holds a quote of the rule. No standard decides it. What to do: the records say pick one rule set per project.

## Backgrounds

The notes of the [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md) record name a "never a flat background" rule that contradicts the HyperFrames and video-design skills. No quote of either side is held, and no standard decides it. What to do: pick one rule set per project.

## Caption margins on vertical video

- [claude-plugin-marketplace](../../catalog/tool/josiahsiegel__claude-plugin-marketplace.md): "- Use safe margins (50px from edges)".
- [OpenMontage](../../catalog/tool/openmontageinc__openmontage.md) lists TikTok dead zones on 1080x1920 of 108 px top, 320 px bottom, 120 px right; its record says the table cites a third-party site that was not opened.
- [remotion-superpowers](../../catalog/tool/dojocodinglabs__remotion-superpowers.md): "About 15-25% up from the bottom (`bottom` around 300-480), or dead center for punchy hooks".
- [Remotion Agent Skills](../../catalog/tool/remotion-dev__skills.md), for 1080px-wide video: "keep key text at least 80px from the sides and 100px from the top and bottom."

Standard: [Meta's Reels ads guide](../../catalog/source/facebook.com__business__ads-guide__update__video__instagram-reels.md) says "Consider leaving at least 14% of the top, 35% of the bottom, and 6% on each side of your asset free from text". It is written for ads; [TikTok's ads page](../../catalog/source/ads.tiktok.com__help__article__creative-best-practices.md) gives safe zones only as files that were not downloaded. What to do: for Reels, keep captions outside Meta's margins; for TikTok the hub has no first-party number.

## Loudness target

- [motion-graphics (Mort1d)](../../catalog/tool/mort1d__motion-graphics-skills.md) masters at "-14 LUFS, true peak ≤ -1 dBTP".
- [SynthCut](../../catalog/tool/relo-video__synthcut.md) ships "platform export presets with loudness normalization (-14/-16 LUFS)".
- [generative-media-skills](../../catalog/tool/calesthio__generative-media-skills.md): "Leave at least 1 dB true-peak headroom for generic web/social delivery when no loudness target is specified".

Standard: [EBU R 128](../../catalog/source/tech.ebu.ch__publications__r128.md) sets "a Target Level of −23.0 LUFS" and a true peak that "shall not exceed −1 dBTP". [EBU R 128 s2](../../catalog/source/tech.ebu.ch__files__live__sites__tech__files__shared__r__r128s2.pdf.md) allows "the range of −20.0 to −16.0 LUFS" for streaming without metadata, and its record marks the -14 LUFS skill as above that range. What to do: the s2 record's notes say pick -16 LUFS integrated with -1 dBTP and check with `ffmpeg -i out.mp4 -af ebur128=peak=true -f null -` (from the R 128 record).

## Frames or numbers in review

- [remotion-superpowers](../../catalog/tool/dojocodinglabs__remotion-superpowers.md): "if they disagree on something visible, trust the frames and say so."
- [screenstudio-alt](../../catalog/tool/connerkward__screenstudio-alternative-skill.md): "send the actual rendered mp4 to a video-understanding model and act on its critique."
- [smooth-animation-skill](../../catalog/tool/flchntc__smooth-animation-skill.md) fails a file on a number: "the limit is 0.1."

No standard decides it. [arXiv 2605.15585](../../catalog/source/arxiv.org__abs__2605.15585.md) says such defects "become apparent only after execution". In the [worked example](../../examples/hyperframes-vs-remotion/README.md), run here once, both agents found their layout bugs only from stills. What to do: [ffmpeg-skill](../../catalog/tool/kajisho5__ffmpeg-skill.md) runs both, a `check.py` step and then a `look.py` contact sheet.

## Motion timing

- [HyperFrames](../../catalog/tool/heygen-com__hyperframes.md): "**Exits** are 40-50% shorter than their entrances."
- [motion-design skill](../../catalog/tool/lottiefiles__motion-design-skill.md): "Stagger total <500ms". [claude-remotion-skill](../../catalog/tool/haidrrrry__claude-remotion-skill.md): "**NEVER use linear interpolation.**"
- [Carbon](../../catalog/source/carbondesignsystem.com__elements__motion__overview.md): "the larger the change in distance (traveled) or size (scaling) of the element, the longer the animation takes." Its record says Carbon's exit easing speeds up, matching HyperFrames.
- [Material 3 tokens](../../catalog/source/github.com__material-components__material-web__blob__main__tokens__versions__latest__sass___md-sys-motion.scss.md): medium durations of 250, 300, 350 and 400 ms; its record says these are for taps.

No design-system record gives an exit-to-entrance ratio, so no standard decides it. What to do: the Carbon record's notes say scale UI durations up for video and keep the ratios.

## Remotion licence threshold

- [Remotion](../../catalog/tool/remotion-dev__remotion.md) LICENSE: free for "a for-profit organization with up to 3 employees".
- [html-video](../../catalog/tool/nexu-io__html-video.md): "Source-available, paid above 4 devs".

Decided by the licensor's own text on the [Remotion](../../catalog/tool/remotion-dev__remotion.md) record, whose notes add that contractors count toward the headcount and that 5.0 ships a changed licence. [Remotion 5.0](../../catalog/source/remotion.dev__docs__5-0-migration.md) also adds telemetry duties for company licence holders. What to do: re-read LICENSE.md at each upgrade.

## Other documented conflicts

- Reading speed: [TikTok](../../catalog/source/ads.tiktok.com__help__article__creative-best-practices.md) "5-10 words per second" for text overlays against [BBC](../../catalog/source/bbc.co.uk__accessibility__forproducts__guides__subtitles.md) "160-180 words per minute"; the TikTok record says not to apply its rate to captions of speech.
- Review rounds: [OpenMontage](../../catalog/tool/openmontageinc__openmontage.md) "max 2 rounds" against [claude-code-video-toolkit](../../catalog/tool/digitalsamba__claude-code-video-toolkit.md) "Three rounds at most."
- Fonts: [Anthropic skills](../../catalog/tool/anthropics__skills.md) "Download and use whatever fonts are needed" against [motion-video-director](../../catalog/tool/mattypark__motion-graphics-skill.md) "Never ship a font whose license you couldn't verify."
- Skill or MCP: [Remotion](../../catalog/source/remotion.dev__docs__ai__mcp.md) left MCP because agents did not invoke it; [Vercel](../../catalog/source/vercel.com__blog__agents-md-outperforms-skills-in-our-agent-evals.md) measured skills "never invoked" in 56% of cases.

## Summary

| Conflict | Decided by a standard? | Record that decides it |
|---|---|---|
| Idle motion | no | - |
| Backgrounds | no | - |
| Caption margins, vertical | for Reels ads only | [Meta Reels ads guide](../../catalog/source/facebook.com__business__ads-guide__update__video__instagram-reels.md) |
| Loudness target | yes | [EBU R 128 s2](../../catalog/source/tech.ebu.ch__files__live__sites__tech__files__shared__r__r128s2.pdf.md) |
| Frames or numbers | no | - |
| Exit durations | no | - |
| Remotion licence threshold | by the licensor's text | [Remotion](../../catalog/tool/remotion-dev__remotion.md) |
| Caption reading speed | yes, for subtitles | [BBC](../../catalog/source/bbc.co.uk__accessibility__forproducts__guides__subtitles.md) |

## Not covered yet

- Verbatim quotes of the idle-motion, flat-background and no-still-scenes rules.
- A first-party TikTok safe-zone number.
- A first-party platform page stating a -14 LUFS target.
- A standard for exit-to-entrance duration ratios in video.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
