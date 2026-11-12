# Remotion 5.0 migration: mandatory telemetry for licensed companies

`source:remotion.dev/docs/5-0-migration` - source - <https://www.remotion.dev/docs/5-0-migration>

Remotion's planned breaking changes for 5.0 (not released on 2026-11-12) and its telemetry page, which make render telemetry and a licence key mandatory for Company License customers on the Automators option, with Creators exempt.

Concepts: [Licences and territory](../../docs/glossary.md#licences-and-territory), [Code-driven video](../../docs/glossary.md#code-driven-video), [Automation](../../docs/glossary.md#automation)

Tags: remotion, telemetry, licence-change

**Badge:** quoted, primary source read (`quoted-primary`): primary source read.

**Why:** An automated video pipeline on Remotion is the 'Automators' case, so for a company on that option, upgrading to 5.0 means sending render events to Remotion or arranging another way to report counts.

**Last checked:** 2026-11-12, primary-read, by agent:codex. Next check due 2027-02-10.

## Fit notes

Fit: high. Level: intermediate. Maturity: -.

Updates tool:remotion-dev/remotion, whose fit_notes point to the 5.0 licence change. Free-licence users are not obliged to send telemetry, but client-side rendering sends an event for every render that is not aborted, including the end user's IP address, even without a licence key. renderFrames() and stitchFramesToVideo() do not report on their own, so a pipeline built on them must call registerUsageEvent() itself. Telemetry never fails a render, per the page. Pin Remotion 4.x if your company policy blocks outbound calls, until a reporting arrangement exists.

## Claims

1. Upgrading to 5.0 requires company licence holders to enable telemetry or arrange another way to deliver render counts; the telemetry page exempts companies on the Remotion for Creators option.

   > If you upgrade to Remotion 5.0, you must enable telemetry if you are a company license holder or contact Remotion to arrange a plausible delivery of render counts.

   Locator: 5-0-migration, section Telemetry is now mandatory for Company License customers. Source: <https://www.remotion.dev/docs/5-0-migration>, retrieved 2026-11-12.

2. In 5.0, Automators customers must set licenseKey and opt into telemetry; Creators are not obliged.

   > In Remotion 5.0, it becomes obligatory for companies which are under the "Remotion for Automators" option to set the licenseKey field and opt into telemetry.

   Locator: license/telemetry, 5.0 section. Source: <https://www.remotion.dev/docs/license/telemetry>, retrieved 2026-11-12.

3. Client-side rendering sends a telemetry event for every render that succeeds or fails, even with no licence key, including the end user's IP address; an aborted render sends none.

   > Client-side rendering APIs always send a telemetry event for every render, even if no licenseKey is set:

   Locator: license/telemetry, section Telemetry in client-side rendering. Source: <https://www.remotion.dev/docs/license/telemetry>, retrieved 2026-11-12.

## Provenance

- Source type: vendor-or-author
- Corroboration: single-source
- Checked: 2026-11-12 by agent:codex, depth primary-read. independent fact-check: claims, prose and category fields against the saved source
- Next check due: 2027-02-10
- Licence: unknown
- URL status: live
- Saved source sha256: `2e25fe264f53994b713b2debac8f785ffd02fd23e8876fc36e805499ef4b9430`
- Lane: contrarian

## Observed

Nothing collected yet.

## Related

- extends: [Remotion](../tool/remotion-dev__remotion.md) - The 5.0 change its fit_notes refer to.

## Referenced by

None.

## Status

Status: current.

Index of all pages: https://tp9imka.github.io/agentic-media-lab/llms.txt
