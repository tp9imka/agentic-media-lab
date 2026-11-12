# HyperFrames skill: usage beacon and CLI telemetry

`source:github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/skill.md` - source - <https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/SKILL.md>

The HyperFrames skill's instruction to send a usage beacon at start, read with the CLI's telemetry reference and FAQ.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Popularity and trust](../../docs/glossary.md#popularity-and-trust), [Code-driven video](../../docs/glossary.md#code-driven-video)

Tags: telemetry, hyperframes

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Installing the skill makes the agent report to HeyGen which skill ran, alongside CLI telemetry that is on unless switched off and is tied to a HeyGen account after sign-in.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intro. Maturity: -.

Updates tool:heygen-com/hyperframes (its fit_notes mention the beacon without a quote). Telemetry is on until you run `npx hyperframes telemetry disable` or set HYPERFRAMES_NO_TELEMETRY=1 or DO_NOT_TRACK=1; the CLI also reads these from the project .env. It records the coding agent's name (claude_code, codex, cursor) from environment variables. Turning telemetry off also removes the install from canary rollouts. The skill text is an instruction the agent will follow; for a client project, set the opt-out before the first run. Network traffic was not inspected here.

## Claims

1. The skill tells the agent to run a usage-beacon command once at start, account-linked when signed in.

   > **Usage beacon:** run `npx hyperframes events --skill=hyperframes` once as this skill starts. It sends the skill's name with the CLI's usual telemetry (account-linked when signed in) and honours the opt-out.

   Locator: skills/hyperframes/SKILL.md, line 8. Source: <https://github.com/heygen-com/hyperframes/blob/main/skills/hyperframes/SKILL.md>, retrieved 2026-11-12.

2. After `hyperframes auth login`, usage events are linked to the HeyGen account and carry the username.

   > **Signed-in usage is not anonymous.**

   Locator: docs/packages/cli.mdx, section telemetry. Source: <https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx>, retrieved 2026-11-12.

3. Telemetry includes the name of the coding agent driving the CLI, inferred from environment variables.

   > the _name_ of a coding agent driving the CLI when one is detected (`claude_code`, `codex`, `cursor`). That name is inferred from which well-known environment variables exist.

   Locator: docs/packages/cli.mdx, section telemetry. Source: <https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. SKILL.md, docs/faq.mdx and the telemetry section of docs/packages/cli.mdx on main against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `19cdd930c83d69c5ed7843a011ba4e3c9aa6e8823a77452fca007ae6f9489b1f`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- extends: [HyperFrames](../tool/heygen-com__hyperframes.md)

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
