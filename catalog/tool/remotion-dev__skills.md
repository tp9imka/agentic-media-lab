# Remotion Agent Skills

`tool:remotion-dev/skills` - tool - <https://github.com/remotion-dev/skills>

The official skill set for writing Remotion (React) video with a coding agent: creation, markup, captions, rendering.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Agent Skills](../../docs/glossary.md#agent-skills), [Visual design](../../docs/glossary.md#visual-design), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: remotion-best-practices, remotion-create, remotion skills

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The reference skills for the other dominant renderer. They state support for Codex and Cursor as well as Claude Code.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor |
| levers | motion, design, captions |
| cost | mixed |

The skills repo has no licence file, and Remotion itself has a company licence: check both before client work. The skill opens a preview for a person; it does not make the agent inspect frames.

## Claims

1. Its layout rule keeps key text inside a stated safe area.

   > For 1080px-wide videos, keep key text at least 80px from the sides and 100px from the top and bottom.

   Locator: skills/remotion-create/video-layout.md, second bullet. Source: <https://github.com/remotion-dev/skills/blob/main/skills/remotion-create/video-layout.md>, retrieved 2026-11-12.

2. It asks for one focal point per scene.

   > Decide what the viewer should notice first in each scene. Build the frame around that one thing.

   Locator: skills/remotion-create/video-layout.md, first bullet. Source: <https://github.com/remotion-dev/skills/blob/main/skills/remotion-create/video-layout.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `7ad94c22e3ad87671292ebb9b22f234c544d6c7fed13f8cb112b84b0f7077d4c`
- Lane: quality-skills

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-01-19
- default_branch: main
- fetched_at: 2026-11-12
- forks: 741
- installs: 800255
- installs_by_skill: {"remotion-best-practices": 800255}
- last_activity: 2026-11-11
- licence: unknown
- open_issues: 23
- registry: skills.sh
- sources: https://api.github.com/repos/remotion-dev/skills, https://skills.sh/api/search?q=skills
- stars: 6888
- Popularity: installs and stars differ by more than 100x

## Related

- alternative_to: [HyperFrames](heygen-com__hyperframes.md)
- supersedes: [Remotion's Model Context Protocol (shut down)](../source/remotion.dev__docs__ai__mcp.md)

## Referenced by

- [Remotion issue 12922: the skill asks agents to check audio they cannot hear](../source/github.com__remotion-dev__remotion__issues__12922.md) (evaluated_on)
- [Remotion PR 13133: agents skipped the interactivity skill](../source/github.com__remotion-dev__remotion__pull__13133.md) (evaluated_on)
- [remotion-superpowers](dojocodinglabs__remotion-superpowers.md) (extends)
- [claude-remotion-skill](haidrrrry__claude-remotion-skill.md) (extends)
- [HyperFrames](heygen-com__hyperframes.md) (alternative_to)
- [SynthCut](relo-video__synthcut.md) (integrates_with)
- [Remotion](remotion-dev__remotion.md) (integrates_with)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
