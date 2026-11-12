# Using bb on multiple devices

`source:github.com/get-bb/bb/blob/main/docs/multiple-devices.md` - source - <https://github.com/get-bb/bb/blob/main/docs/multiple-devices.md>

bb's guide to browser devices, execution machines and the one server machine they all connect to.

Concepts: [Automation](../../docs/glossary.md#automation), [Scheduling and runtimes](../../docs/glossary.md#scheduling-and-runtimes)

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** It answers what must stay running for a bb schedule to fire: the server machine, awake.

**Last checked:** 2026-11-12, primary-read, by agent:kiro. Next check due 2027-02-10.

## Fit notes

Fit: medium. Level: intro. Maturity: -.

On a laptop this means scheduled renders stop when the lid closes. Remote access goes through bb connect (a bb account) or Tailscale Serve; the doc warns against Funnel or the public internet.

## Claims

1. One machine runs the bb server and holds threads, database and settings; while it sleeps nothing can reach bb and running threads may stop.

   > Pick a computer that stays on, such as a desktop, home server, or VM: while the server machine is asleep or off, nothing can reach bb and running threads may stop.

   Locator: page intro, paragraph 2. Source: <https://github.com/get-bb/bb/blob/main/docs/multiple-devices.md>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:kiro, depth primary-read. docs/multiple-devices.md intro against the claim
- Next check due: 2027-02-10
- Licence: MIT
- URL status: live
- Saved source sha256: `e80c2b6f9ae048b6edfe2c0a30f761c55db1024ff3e255fdd1497645a2a57b8f`
- Lane: automation

## Observed

Collected by `tools/enrich.py`, not typed by hand.

- archived: false
- created: 2026-02-24
- default_branch: main
- fetched_at: 2026-11-12
- forks: 786
- last_activity: 2026-11-12
- licence: MIT
- open_issues: 852
- sources: https://api.github.com/repos/get-bb/bb, https://skills.sh/api/search?q=bb
- stars: 5381

## Related

- extends: [bb](../tool/get-bb__bb.md)

## Referenced by

- [bb](../tool/get-bb__bb.md) (depends_on)

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
