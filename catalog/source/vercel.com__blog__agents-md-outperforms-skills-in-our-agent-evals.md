# Vercel: AGENTS.md outperforms skills in our agent evals

`source:vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals` - source - <https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals>

A Vercel engineering post (27 Jan 2026) that ran a Next.js docs skill and an AGENTS.md docs index through the same coding-agent eval suite.

Concepts: [Agent Skills](../../docs/glossary.md#agent-skills), [Agent surface](../../docs/glossary.md#agent-surface)

Tags: skill-invocation

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** Many video skills assume the agent will load them when a video task comes up. Vercel measured that an agent often does not, which changes how a reader should wire a renderer skill into a project.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

For a video project: put a short index of the renderer's rules (or a line that says which skill to load and when) in CLAUDE.md or AGENTS.md instead of relying on the skill's description to trigger it. Vercel also found the wording of that line mattered; 'explore the project first, then invoke the skill' did better than 'you MUST invoke the skill'. One framework, one eval suite, model and agent not named on the page, and Vercel runs skills.sh. It disputes the reading of the Remotion MCP shutdown note that skills are the reliable surface: both pages report agents not calling what is available.

## Claims

1. With a skill available and no instruction to use it, the agent never invoked the skill in 56% of eval cases, and the pass rate equalled the no-docs baseline.

   > In 56% of eval cases, the skill was never invoked. The agent had access to the documentation but didn't use it. Adding the skill produced no improvement over baseline:

   Locator: section Skills weren't being triggered reliably. Source: <https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals>, retrieved 2026-11-12.

2. A compressed 8KB docs index in AGENTS.md passed 100%; skills reached at most 79% even with explicit instructions.

   > A compressed 8KB docs index embedded directly in AGENTS.md achieved a 100% pass rate, while skills maxed out at 79% even with explicit instructions telling the agent to use them.

   Locator: intro, paragraph 2. Source: <https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals>, retrieved 2026-11-12.

3. Small wording changes in the instruction to use the skill gave large swings in behaviour.

   > Same skill. Same docs. Different outcomes based on subtle wording changes.

   Locator: section Explicit instructions helped, but wording was fragile. Source: <https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. Vercel blog visible text against the three claims
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `6c4eae3c0880122a5eb825f2d8142ce80ca60e5f178b24912f5b69fdf7a4f5eb`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- contradicts: [Remotion's Model Context Protocol (shut down)](remotion.dev__docs__ai__mcp.md) - Remotion moved from MCP to skills partly because agents did not invoke MCP reliably; Vercel measured the same failure for skills.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
