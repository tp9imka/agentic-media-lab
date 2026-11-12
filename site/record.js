import { CONFIG_URL, badge, glyph, dateText, el, extLink, fetchJson, fetchText, indexBase, indexErrorText, initChrome, marker, safeHref, siteLink } from "./common.js";
import { dice, isHidden, parseJsonl, referencedBy, trigrams } from "./search_core.js";

const NEAREST_IDS = 3;
const DEFAULT_RATIO = 100;
const ISSUE_BODY_CHARS = 1500;
const KIND_FACTS = {
  tool: [["tool_type", "Tool type"], ["agents", "Agents"], ["levers", "Levers"], ["cost", "Cost"]],
  model: [["modes", "Modes"], ["access", "Access"], ["apple_silicon", "Apple Silicon"], ["licence_class", "Licence class"]],
  source: [["citation", "Citation"]],
  recipe: [["video_types", "Video types"]],
};
const COMMON_FACTS = [["kind", "Kind"], ["maturity", "Maturity"], ["level", "Level"], ["status", "Status"],
  ["url", "Canonical URL"], ["url_status", "Link status"], ["source_type", "Source type"],
  ["corroboration", "Corroboration"], ["concept_labels", "Concepts"], ["lane", "Research lane"]];
const OBSERVED = [["licence", "Licence"], ["stars", "Stars"], ["installs", "Installs"],
  ["downloads_week", "Downloads per week"], ["last_activity", "Last activity"], ["archived", "Archived upstream"],
  ["fetched_at", "Fetched"]];

const $ = id => document.getElementById(id);

function valueText(v) {
  if (v === null || v === undefined || v === "") return "not recorded";
  if (Array.isArray(v)) return v.length ? v.join(", ") : "none";
  if (typeof v === "boolean") return v ? "yes" : "no";
  if (typeof v === "object") return Object.entries(v).map(([k, x]) => `${k}: ${x}`).join("; ");
  return String(v);
}

function recordLink(id, byId) {
  const r = byId.get(id);
  const a = el("a", { href: siteLink("record.html", { id }) }, r ? r.title || id : id);
  return r ? a : el("span", {}, el("code", { text: id }), " (not in the index)");
}

function fail(text, extra) {
  $("state").textContent = text;
  if (extra) $("state").after(extra);
}

function nearest(id, ids) {
  const g = trigrams(id);
  return ids.map(x => [dice(g, trigrams(x)), x]).sort((a, b) => b[0] - a[0] || (a[1] < b[1] ? -1 : 1))
    .slice(0, NEAREST_IDS).map(x => x[1]);
}

function factsRows(r) {
  const tbody = $("r-facts").tBodies[0];
  for (const [key, label] of (KIND_FACTS[r.kind] || []).concat(COMMON_FACTS)) {
    if (!(key in r) && key !== "kind") continue;
    const v = r[key];
    const cell = key === "url" && safeHref(v) ? el("td", {}, extLink(v)) : el("td", { text: valueText(v) });
    if (key === "status" && r.status_note) cell.append(` (${r.status_note})`);
    tbody.append(el("tr", {}, el("th", { scope: "row", text: label }), cell));
  }
}

function stages(r, byId) {
  if (!Array.isArray(r.stages) || !r.stages.length) return;
  $("r-stages").append(el("h3", { text: "Stages" }), el("ol", { class: "stages" }, r.stages.map(s =>
    el("li", {}, el("strong", { text: `${s.stage || "stage"}: ` }), recordLink(s.record_id, byId),
      s.note ? ` - ${s.note}` : ""))));
}

function claims(r) {
  const box = $("r-claims");
  const list = (r.claims || []).filter(c => c && typeof c === "object");
  if (!list.length) {
    box.append(el("p", { text: "No claims recorded yet." }));
    return;
  }
  box.append(el("ol", { class: "claims" }, list.map(c => el("li", {},
    el("p", { text: c.text || "" }),
    c.quote ? el("blockquote", safeHref(c.url) ? { cite: safeHref(c.url) } : {}, el("p", { text: c.quote })) : null,
    el("p", { class: "claim-meta" },
      c.locator ? `${c.locator}. ` : "", c.url ? extLink(c.url, "Source") : "No source link",
      c.retrieved ? `. Retrieved ${c.retrieved}.` : ".",
      c.via ? el("span", {}, " Read through a secondary source: ", extLink(c.via)) : null)))));
}

function observed(r, ratio) {
  const box = $("r-observed");
  const o = r.observed || {};
  if (r.popularity_flag === "disagree") {
    box.append(el("p", { class: "warning", role: "note" },
      glyph("warning"), " ",
      el("strong", { text: "Popularity warning: " }),
      `stars and installs disagree by more than ${ratio}x. Do not read either number as a quality signal.`));
  }
  if (!Object.keys(o).length) {
    box.append(el("p", { text: "No upstream data collected yet." }));
    return;
  }
  box.append(el("dl", { class: "facts-dl" }, OBSERVED.map(([k, label]) =>
    el("div", {}, el("dt", { text: label }), el("dd", { text: k in o ? valueText(o[k]) : "not collected" })))));
}

function links(r, records, byId) {
  const rel = (r.related || []).filter(x => x && x.id);
  $("r-related").append(...(rel.length ? rel.map(x => el("li", {}, el("span", { class: "rel", text: `${x.rel || "related"}: ` }), recordLink(x.id, byId)))
    : [el("li", { text: "None recorded." })]));
  const refs = referencedBy(records, r.id);
  $("r-refby").append(...(refs.length ? refs.map(([id, kind]) => el("li", {}, el("span", { class: "rel", text: `${kind}: ` }), recordLink(id, byId)))
    : [el("li", { text: "Nothing in the index links here." })]));
}

function actions(r, config) {
  const ul = $("r-actions");
  if (r.path) ul.append(el("li", {}, el("a", { href: `../${r.path}`, type: "text/markdown" }, "View as markdown")));
  const blob = new Blob([JSON.stringify(r, null, 1) + "\n"], { type: "application/json" });
  ul.append(el("li", {}, el("a", { href: URL.createObjectURL(blob), download: `${r.id.replace(/[^a-z0-9._-]+/gi, "_")}.json` }, "Download JSON")));
  const repo = config && safeHref(config.repo_url);
  if (repo) {
    const body = [`Record: ${r.id}`, `Page: ${location.href}`, `Markdown: ${r.path || "-"}`,
      `Last checked: ${(r.checked || {}).date || "-"}`, "", "What is wrong:", "", "Source for the correction:", ""]
      .join("\n").slice(0, ISSUE_BODY_CHARS);
    const q = new URLSearchParams({ title: `Error in ${r.id}`, body });
    ul.append(el("li", {}, el("a", { href: `${repo.replace(/\/$/, "")}/issues/new?${q}`, rel: "noopener noreferrer" }, "Report an error")));
  }
}

function render(r, records, config) {
  const byId = new Map(records.map(x => [x.id, x]));
  const title = r.title || r.id;
  document.title = `${title} - ${(config && config.title) || "Knowledge hub"}`;
  if (r.path) $("md-alternate").href = `../${r.path}`;
  $("crumb-kind").textContent = r.kind ? `${r.kind} records` : "Records";
  $("crumb-kind").href = siteLink("search.html", { kind: r.kind });
  $("crumb-id").textContent = title;
  $("r-title").textContent = title;
  const chk = r.checked || {};
  $("r-badges").append(...[badge(r.badge), el("span", { class: "kind", text: r.kind || "" }),
    r.stale ? marker("stale", "check overdue") : null,
    isHidden(r) ? marker("hidden", "Archived or shut down") : null].filter(Boolean));
  $("r-why").textContent = r.why_it_matters || r.summary || "";
  $("r-checked").textContent = `Last checked ${dateText(chk.date)} (${chk.depth || "depth not recorded"}). ` +
    `Next check due ${dateText(chk.next_due)}.`;
  if (isHidden(r) || (r.status && r.status !== "current")) {
    $("r-status").hidden = false;
    $("r-status").textContent = `Status: ${r.status || "-"}${r.status_note ? ` - ${r.status_note}` : ""}` +
      (isHidden(r) ? " Left out of default search." : "");
  }
  $("r-fit").append(el("p", {}, el("strong", { text: `Fit: ${r.fit || "not judged"}. ` }), r.fit_notes || ""),
    r.summary ? el("p", { text: r.summary }) : null);
  factsRows(r);
  stages(r, byId);
  claims(r);
  observed(r, (config && config.popularity_disagreement_ratio) || DEFAULT_RATIO);
  links(r, records, byId);
  actions(r, config);
  if (isHidden(r)) $("record").classList.add("is-hidden");
  $("state").hidden = true;
  $("record").hidden = false;
}

async function main() {
  initChrome();
  const id = new URLSearchParams(location.search).get("id");
  const config = await fetchJson(CONFIG_URL, true).catch(() => null);
  if (!id) {
    fail("No record id given. ", el("p", {}, el("a", { href: siteLink("search.html") }, "Search the hub")));
    return;
  }
  let records;
  try {
    records = parseJsonl(await fetchText(indexBase() + "records.jsonl"));
  } catch (err) {
    fail(err.status === 404 ? indexErrorText(new Error("missing")) : indexErrorText(err));
    return;
  }
  if (!records.length) {
    fail("The hub has no records yet.");
    return;
  }
  const r = records.find(x => x.id === id);
  if (!r) {
    fail(`No record with id ${id}.`, el("div", {}, el("p", { text: "Nearest ids:" }),
      el("ul", { class: "plain-list" }, nearest(id, records.map(x => x.id)).map(x => el("li", {}, recordLink(x, new Map(records.map(y => [y.id, y]))))))));
    return;
  }
  render(r, records, config);
}

main();
