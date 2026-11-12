# motion-video-director (mattypark)

`tool:mattypark/motion-graphics-skill` - tool - <https://github.com/mattypark/Motion-graphics-skill>

A skill for code-drawn motion graphics and edited videos with a fixed intake, storyboard and preview flow, plus stock, SFX, font and Lottie sourcing through MCPs and APIs.

Concepts: [Code-driven video](../../docs/glossary.md#code-driven-video), [Story and decomposition](../../docs/glossary.md#story-and-decomposition), [Agent Skills](../../docs/glossary.md#agent-skills), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: motion-video-director

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It is the candidate with the most explicit asset rules: a manifest with source and licence for every downloaded file, and no font shipped without a verified licence.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor |
| levers | asset, story, audio, motion |
| cost | mixed |

Asset search needs Pixabay, Freesound and Firecrawl keys. It adds the Playwright MCP through npx with @latest, which runs whatever version is newest; pin a version. It uses Pinterest, Behance and Dribbble for style references and says reference-only unless licensed; check that the agent keeps to that. The SKILL.md is 53 KB.

## Claims

1. It records licence and attribution for every downloaded asset in a manifest.

   > Record license/attribution for every downloaded asset in `manifest.json`.

   Locator: skills/motion-video-director/SKILL.md, project rules. Source: <https://github.com/mattypark/Motion-graphics-skill/blob/HEAD/skills/motion-video-director/SKILL.md>, retrieved 2026-11-12.

2. It never ships a font whose licence it could not verify.

   > Never ship a font whose license you couldn't verify.

   Locator: skills/motion-video-director/SKILL.md, font sourcing workflow. Source: <https://github.com/mattypark/Motion-graphics-skill/blob/HEAD/skills/motion-video-director/SKILL.md>, retrieved 2026-11-12.

3. It installs the Playwright MCP from npm at its newest version.

   > "playwright": { "command": "npx", "args": ["@playwright/mcp@latest"

   Locator: skills/motion-video-director/SKILL.md, setup table, row MCP Playwright. Source: <https://github.com/mattypark/Motion-graphics-skill/blob/HEAD/skills/motion-video-director/SKILL.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/motion-video-director/SKILL.md against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `02f07b4e640b2fd04512ad8b82386aaa70f8aebf5904f3b07ca9529c598f6697`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-10-08
- default_branch: main
- fetched_at: 2026-11-12
- forks: 26
- last_activity: 2026-10-08
- licence: unknown
- open_issues: 0
- sources: https://api.github.com/repos/mattypark/Motion-graphics-skill, https://skills.sh/api/search?q=Motion-graphics-skill
- stars: 47

## Related

None.

## Referenced by

- [Anthropic Agent Skills (canvas-design, algorithmic-art)](anthropics__skills.md) (contradicts)
- [motion-graphics (Mort1d)](mort1d__motion-graphics-skills.md) (alternative_to)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
