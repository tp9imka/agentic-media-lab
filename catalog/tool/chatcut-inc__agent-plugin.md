# ChatCut agent plugin

`tool:chatcut-inc/agent-plugin` - tool - <https://github.com/ChatCut-Inc/agent-plugin>

Plugins and an MCP server that connect Codex, Claude Code, Cursor, Gemini CLI and other agents to ChatCut, a commercial editor with a desktop app and a hosted web version. It covers talking-head cleanup, text-based editing, captions, b-roll and XML export.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Plugins](../../docs/glossary.md#plugins), [MCP servers](../../docs/glossary.md#mcp-servers), [Cost](../../docs/glossary.md#cost)

Also known as: ChatCut, chatcut plugin

Tags: hosted

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It covers almost every step of the question in one product, so it is the yardstick for what the free tools leave out. It is a hosted account service, not a free local path.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: low. Level: intro. Maturity: active.

| field | value |
|---|---|
| tool_type | plugin |
| agents | claude-code, codex, cursor, gemini-cli, any-mcp |
| levers | captions, audio, review-loop, asset, delivery |
| cost | paid |

Needs a ChatCut account and sign-in; generation spends credits (pricing page not opened). Desktop keeps media local, Web uploads it. The recommended setup has the agent install the desktop app itself, and the manual macOS install downloads a remote script into the shell; read it first. Its generation features include voice clones and lip sync, which this hub does not cover.

## Claims

1. Its editing list covers removing silences, filler words and repeated takes from talking-head footage.

   > Talking-head cleanup: remove silences, filler words, repeated takes and stumbles, and tighten the pacing.

   Locator: README.md, section Everything ChatCut can make, Editing. Source: <https://github.com/ChatCut-Inc/agent-plugin/blob/main/README.md>, retrieved 2026-11-12.

2. Generation spends ChatCut credits, with the agent asking first.

   > Generation uses ChatCut credits, and the agent asks before spending them.

   Locator: README.md, section Everything ChatCut can make. Source: <https://github.com/ChatCut-Inc/agent-plugin/blob/main/README.md>, retrieved 2026-11-12.

3. The recommended setup has the agent itself install the ChatCut Desktop app and connect to it.

   > The agent installs ChatCut Desktop, opens sign-in and connects itself to Desktop's local `chatcut_desktop` MCP server.

   Locator: README.md, section Desktop setup. Source: <https://github.com/ChatCut-Inc/agent-plugin/blob/main/README.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. README.md (main) against the three claims; chatcut.io pricing and docs not opened
- Next check due: 2027-02-10
- Licence: Apache-2.0
- URL status: live
- Saved source sha256: `75b8ae26691f533190c9329d04c833ed06fceeadf82cbfe309a5afc515baa0b5`
- Lane: footage-editing

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-06-25
- default_branch: main
- fetched_at: 2026-11-12
- forks: 84
- installs: 170
- installs_by_skill: {"asset-import": 170, "create-motion-graphics": 167, "export": 165, "product-help": 157, "talking-head-guide": 168, "transcription": 159, "verification": 163, "video-gen": 159, "voice": 157}
- last_activity: 2026-11-12
- licence: Apache-2.0
- open_issues: 12
- registry: skills.sh
- sources: https://api.github.com/repos/ChatCut-Inc/agent-plugin, https://skills.sh/api/search?q=agent-plugin
- stars: 1030

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
