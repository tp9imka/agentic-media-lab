# ffmpeg-skill

`tool:kajisho5/ffmpeg-skill` - tool - <https://github.com/kajisho5/ffmpeg-skill>

An Agent Skill and MCP server of 42 local FFmpeg tools for cutting, captions, loudness and platform export, with a fixed probe, edit, check, verify, look workflow.

Concepts: [Delivery](../../docs/glossary.md#delivery), [Review loop](../../docs/glossary.md#review-loop), [Editing real footage](../../docs/glossary.md#footage-editing), [Agent portability](../../docs/glossary.md#agent-portability)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the clearest delivery skill found: platform checks on the output file, numbers in the report, and a contact sheet the agent must view after any picture change.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, any-skill, any-mcp |
| levers | delivery, review-loop, captions, audio |
| cost | free-local |

Needs FFmpeg 6.1+ and Python 3.10+ locally; no cloud. It tells the agent to use only its scripts and never raw ffmpeg, so a job the 42 tools do not cover stops there. A good last step after any renderer: hand it the MP4 and ask for a platform check. I did not run it.

## Claims

1. Before reporting done, the agent checks the output against a named platform.

   > 5. **Check** with `check.py OUTPUT --platform X --expect-identity S:M`

   Locator: skills/ffmpeg-skill/SKILL.md, Workflow (in this order), step 5. Source: <https://github.com/kajisho5/ffmpeg-skill/blob/HEAD/skills/ffmpeg-skill/SKILL.md>, retrieved 2026-11-12.

2. After any picture change it must view a tiled contact sheet, and say so when it could not look.

   > 8. **Look** after any picture change: `look.py OUTPUT --tiles 3x2`, view the PNG, name it in `Look:`;

   Locator: skills/ffmpeg-skill/SKILL.md, Workflow (in this order), step 8. Source: <https://github.com/kajisho5/ffmpeg-skill/blob/HEAD/skills/ffmpeg-skill/SKILL.md>, retrieved 2026-11-12.

3. It burns caption words as written and never shortens them to fit.

   > - **The words in a caption** — burned as written; never rewrite or shorten them, even to "make it fit".

   Locator: skills/ffmpeg-skill/SKILL.md, section on what the agent never changes. Source: <https://github.com/kajisho5/ffmpeg-skill/blob/HEAD/skills/ffmpeg-skill/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/ffmpeg-skill/SKILL.md and README.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `afb24e0587b3fe2a387fe2bb6031b9a953f97a0404655f339527445640c10e4e`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-09-03
- default_branch: main
- fetched_at: 2026-11-12
- forks: 434
- installs: 1287
- installs_by_skill: {"building-python-mcp-servers": 41, "ci-pipeline-synthesizer": 41, "concurrent-branches": 41, "ffmpeg-skill": 1287, "guarding-destructive-operations": 41, "keeping-git-repos-clean": 41, "managing-python-releases": 41, "reproducing-ci-locally": 41, "running-github-actions-efficiently": 41, "shipping-across-surfaces": 41}
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 31
- registry: skills.sh
- sources: https://api.github.com/repos/kajisho5/ffmpeg-skill, https://skills.sh/api/search?q=ffmpeg-skill
- stars: 5134

## Related

- alternative_to: [video-use](browser-use__video-use.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
