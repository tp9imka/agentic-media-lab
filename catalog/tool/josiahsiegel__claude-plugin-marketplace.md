# claude-plugin-marketplace (ffmpeg-kinetic-captions)

`tool:josiahsiegel/claude-plugin-marketplace` - tool - <https://github.com/JosiahSiegel/claude-plugin-marketplace>

A Claude Code plugin marketplace. Its ffmpeg-effects plugin has a kinetic-captions skill: ASS subtitle tags for word-grow, karaoke and pop captions burned in with FFmpeg, with timing per platform.

Concepts: [Audio and captions](../../docs/glossary.md#audio-and-captions), [Plugins](../../docs/glossary.md#plugins), [Motion and transitions](../../docs/glossary.md#motion-and-transitions)

Also known as: ffmpeg-kinetic-captions, ffmpeg-effects

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It gives exact word-pop timings and a reading-time formula, which is the kinetic-caption craft most other skills leave as 'make captions pop'.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | claude-code |
| levers | captions, motion |
| cost | free-local |

Install only the ffmpeg-effects plugin; the marketplace holds many unrelated plugins. Its 50 px edge margin for 1080x1920 is far smaller than the platform UI zones in tool:openmontageinc/openmontage and tool:dojocodinglabs/remotion-superpowers, so captions placed by this rule can sit under TikTok buttons. The readability file credits its 1.5 s minimum and 42-character line to WCAG 2.2; I did not open WCAG to confirm that. The skill opens with Windows path rules unrelated to video.

## Claims

1. It gives word-grow timings per platform, for example 100-150 ms grow and 115-120% scale on TikTok.

   > | **TikTok** | 100-150ms | 100-150ms | 115-120% | Fast, punchy |

   Locator: plugins/ffmpeg-effects/skills/ffmpeg-kinetic-captions/SKILL.md, section Word-Grow Timing by Platform, table row TikTok. Source: <https://github.com/JosiahSiegel/claude-plugin-marketplace/blob/HEAD/plugins/ffmpeg-effects/skills/ffmpeg-kinetic-captions/SKILL.md>, retrieved 2026-11-12.

2. Its reading-time rule holds a caption for at least 1.5 s, or word count at 160 words per minute.

   > duration = max(1.5, (word_count / 160) * 60)

   Locator: plugins/ffmpeg-effects/skills/ffmpeg-animation-timing-reference/references/caption-readability.md, section Caption Duration Calculation, Formula. Source: <https://github.com/JosiahSiegel/claude-plugin-marketplace/blob/HEAD/plugins/ffmpeg-effects/skills/ffmpeg-animation-timing-reference/references/caption-readability.md>, retrieved 2026-11-12.

3. For mobile readability it asks for 50 px safe margins from the edges.

   > - Use safe margins (50px from edges)

   Locator: plugins/ffmpeg-effects/skills/ffmpeg-kinetic-captions/SKILL.md, Troubleshooting, Poor Mobile Readability. Source: <https://github.com/JosiahSiegel/claude-plugin-marketplace/blob/HEAD/plugins/ffmpeg-effects/skills/ffmpeg-kinetic-captions/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. ffmpeg-kinetic-captions SKILL.md and caption-readability.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `5875b665b22d58b8b31372a2b16affb0263bad708326245d2ef386a9ee83762c`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-10-22
- default_branch: main
- fetched_at: 2026-11-12
- forks: 11
- installs: 8185
- installs_by_skill: {"docker-best-practices": 947, "docker-security-guide": 624, "ffmpeg-captions-subtitles": 557, "git-master": 812, "powershell-master": 1143, "tailwindcss-advanced-design-systems": 657, "tailwindcss-advanced-layouts": 8185, "tailwindcss-animations": 2376, "tailwindcss-mobile-first": 2118, "tailwindcss-responsive-darkmode": 478}
- last_activity: 2026-06-18
- licence: MIT
- open_issues: 2
- registry: skills.sh
- sources: https://api.github.com/repos/JosiahSiegel/claude-plugin-marketplace, https://skills.sh/api/search?q=claude-plugin-marketplace
- stars: 61
- Popularity: installs and stars differ by more than 100x

## Related

- contradicts: [OpenMontage](openmontageinc__openmontage.md) - 50 px edge margin vs 320 px bottom dead zone on TikTok
- contradicts: [remotion-superpowers](dojocodinglabs__remotion-superpowers.md) - 50 px edge margin vs captions 15-25% up from the bottom

## Referenced by

- [remotion-superpowers](dojocodinglabs__remotion-superpowers.md) (contradicts)
- [OpenMontage](openmontageinc__openmontage.md) (contradicts)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
