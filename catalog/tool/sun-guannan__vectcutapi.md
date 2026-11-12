# VectCutAPI

`tool:sun-guannan/vectcutapi` - tool - <https://github.com/sun-guannan/VectCutAPI>

A Python HTTP and MCP server that builds CapCut or Jianying draft folders: video, audio, text, subtitles from SRT, effects and keyframes. The draft is then opened in the CapCut app.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [MCP servers](../../docs/glossary.md#mcp-servers), [Agent Skills](../../docs/glossary.md#agent-skills)

Also known as: CapCutAPI, VectCut, CapCut MCP, Jianying

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** The only route found to hand an agent-built timeline to CapCut, which many short-form editors already use.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | mcp-server |
| agents | claude-code, any-mcp |
| levers | captions, motion |
| cost | mixed |

The open part writes drafts locally; the vendor's cloud preview and cloud render are hosted and not open. The examples pass media as URLs. No step makes the agent look at the result, so a person checks the draft in CapCut. CapCut itself and its terms were not checked here. Not run here.

## Claims

1. The project describes itself as cloud-based editing APIs and skills for agents.

   > It provides a rich set of cloud-based editing APIs and Skills, including features such as adding subtitles, illustrations, picture-in-picture (PiP), AI voiceovers, filters, and more.

   Locator: README.md, section Preview. Source: <https://github.com/sun-guannan/VectCutAPI/blob/main/README.md>, retrieved 2026-11-12.

2. Saving writes a draft folder that you copy into the CapCut or Jianying drafts directory by hand.

   > Calling `save_draft` will generate a folder starting with `dfd_` in the current directory of `capcut_server.py`. Copy this to the CapCut/Jianying drafts directory to see the generated draft in the application.

   Locator: README.md, section Downloading Drafts. Source: <https://github.com/sun-guannan/VectCutAPI/blob/main/README.md>, retrieved 2026-11-12.

3. The editing agent, web client and cloud rendering are not open source.

   > the code for the MCP Editing Agent, web-based editing client, and cloud rendering modules has not been open-sourced yet.

   Locator: README.md, section Collaboration. Source: <https://github.com/sun-guannan/VectCutAPI/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; skill README and MCP docs not opened
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `4a21dca6c5c95dfad42bd8f0b71d0bcdd9b7cf193cfba9c8274c4acb19a0a34e`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2025-07-11
- default_branch: main
- fetched_at: 2026-11-12
- forks: 498
- installs: 6
- installs_by_skill: {"capcut-director": 6}
- last_activity: 2026-11-07
- licence: Apache-2.0
- open_issues: 7
- registry: skills.sh
- sources: https://api.github.com/repos/sun-guannan/VectCutAPI, https://skills.sh/api/search?q=VectCutAPI
- stars: 2374
- Popularity: installs and stars differ by more than 100x

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
