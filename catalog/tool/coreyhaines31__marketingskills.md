# marketingskills (video, product-demo-recording)

`tool:coreyhaines31/marketingskills` - tool - <https://github.com/coreyhaines31/marketingskills>

A marketing skill set; its video skill has a reference for recording a scripted product demo with Playwright: subtitle bar, step badge, a fake visible cursor and optional TTS.

Concepts: [Editing real footage](../../docs/glossary.md#footage-editing), [Audio and captions](../../docs/glossary.md#audio-and-captions), [Agent Skills](../../docs/glossary.md#agent-skills), [Agent portability](../../docs/glossary.md#agent-portability)

Also known as: product-demo-recording

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Screen demos are the most common developer clip, and this reference fixes their usual tells: an invisible cursor, captions covering the click, a blank first frame.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intermediate. Maturity: active.

| field | value |
|---|---|
| tool_type | skill |
| agents | claude-code, codex, cursor, any-skill |
| levers | captions, motion, asset |
| cost | mixed |

It tells the agent to set bypassCSP on the browser context and, on a non-localhost host, to drop the Secure cookie flag for the recording run. Do that only on a local or staging build, never against production. It also tells the agent never to take an API key pasted into chat, which is the opposite of the video-use README. The TTS step needs a paid key.

## Claims

1. It injects a fake cursor so viewers can see each click.

   > Playwright fires DOM events with no visible pointer, so viewers can't see what got clicked. Inject a fake cursor element and wrap clicks and fills in helpers:

   Locator: skills/video/references/product-demo-recording.md, step 5 Make the cursor visible. Source: <https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/video/references/product-demo-recording.md>, retrieved 2026-11-12.

2. It sizes each scene caption at 50-80 characters.

   > - **Captions of 50-80 characters** read well and keep pauses short

   Locator: skills/video/references/product-demo-recording.md, step 4 scene helper notes. Source: <https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/video/references/product-demo-recording.md>, retrieved 2026-11-12.

3. It switches off the page's content security policy in the recording browser.

   > A `style-src 'self'` policy without `unsafe-inline` blocks the inline styles on the subtitle bar and cursor. Keep `bypassCSP: true` on the context.

   Locator: skills/video/references/product-demo-recording.md, Gotchas. Source: <https://github.com/coreyhaines31/marketingskills/blob/HEAD/skills/video/references/product-demo-recording.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. skills/video/references/product-demo-recording.md against the three claims
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `2f81e4f762c4aeae0c452072506ffa34731ab844de94b125b55ce02e4dfae53d`
- Lane: quality-skills-2

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-01-15
- default_branch: main
- fetched_at: 2026-11-12
- forks: 8744
- installs: 252436
- installs_by_skill: {"ad-creative": 145276, "ai-seo": 163013, "cold-email": 137269, "content-strategy": 175848, "copy-editing": 160338, "copywriting": 252436, "marketing-ideas": 156460, "marketing-psychology": 176027, "programmatic-seo": 160136, "seo-audit": 252420}
- last_activity: 2026-11-11
- licence: MIT
- open_issues: 77
- registry: skills.sh
- sources: https://api.github.com/repos/coreyhaines31/marketingskills, https://skills.sh/api/search?q=marketingskills
- stars: 59845

## Related

None.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
