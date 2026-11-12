import { DECODER_URL, badge, el, fetchJson, highlight, indexErrorText, initChrome, marker, searchEngine, siteLink } from "./common.js";
import { decode, nearestRows } from "./search_core.js";

const RESULT_LIMIT = 8;
const EXAMPLE_COUNT = 3;
// URL key => [label, record field]
const FACETS = [["kind", "Kind", "kind"], ["tool_type", "Tool type", "tool_type"], ["lever", "Lever", "levers"],
  ["agent", "Agent", "agents"], ["cost", "Cost", "cost"], ["access", "Access", "access"]];

const $ = id => document.getElementById(id);
let rows = [];
let records = null;

function readUrl() {
  const p = new URLSearchParams(location.search);
  const filters = {};
  for (const [key] of FACETS) if (p.get(key)) filters[key] = p.get(key);
  return { q: p.get("q") || "", filters, all: p.get("all") === "1" };
}

function writeUrl(state, push) {
  const extra = { q: state.q, ...state.filters, all: state.all ? "1" : "" };
  const url = siteLink("search.html", extra);
  if (push) history.pushState(null, "", url);
  else history.replaceState(null, "", url);
}

function formState() {
  const filters = {};
  for (const [key] of FACETS) {
    const v = $(`f-${key}`)?.value;
    if (v) filters[key] = v;
  }
  return { q: $("q").value.trim(), filters, all: $("f-all").checked };
}

function buildFacets(state) {
  const box = $("facets");
  box.replaceChildren();
  for (const [key, label, field] of FACETS) {
    const values = new Set();
    for (const r of records) {
      const v = r[field];
      for (const x of Array.isArray(v) ? v : [v]) if (x) values.add(String(x));
    }
    if (state.filters[key]) values.add(state.filters[key]);
    if (!values.size) continue;
    const sel = el("select", { id: `f-${key}`, name: key }, el("option", { value: "", text: "Any" }),
      [...values].sort().map(v => el("option", { value: v, text: v, selected: v === state.filters[key] })));
    sel.addEventListener("change", () => run(formState(), false));
    box.append(el("div", { class: "field" }, el("label", { for: `f-${key}`, text: label }), sel));
  }
  $("f-all").checked = state.all;
}

function hitItem(h) {
  const isPage = h.kind === "page";
  const href = isPage ? `../${h.path}${h.anchor ? "#" + h.anchor : ""}` : siteLink("record.html", { id: h.id });
  const meta = el("p", { class: "hit-meta" },
    isPage ? el("span", { class: "badge badge-page" }, el("span", { class: "glyph", "aria-hidden": "true", text: "\u00A7" }), " Guide section") : badge(h.badge),
    el("span", { class: "kind", text: h.kind }),
    h.stale ? marker("stale", "\u26A0 Check overdue") : null,
    h.hidden ? marker("hidden", "Archived or shut down") : null);
  return el("li", { class: "hit" + (h.hidden ? " is-hidden" : "") },
    el("h2", { class: "hit-title" }, el("a", { href }, highlight(h.title, h.matched))),
    meta,
    h.why ? el("p", { class: "hit-why" }, highlight(h.why, h.matched)) : null,
    h.excerpt ? el("p", { class: "hit-excerpt" }, highlight(h.excerpt, h.matched)) : null,
    el("p", { class: "hit-path" }, el("code", { text: h.path + (h.anchor ? "#" + h.anchor : "") }),
      h.matched.length ? el("span", { class: "matched", text: `matched: ${h.matched.join(", ")}` }) : null));
}

function keywordLink(r) {
  return el("a", { href: siteLink("search.html", { q: (r.keywords || []).join(" ") }) }, r.question);
}

function showDecoded(q) {
  const box = $("decoded");
  const body = $("decoded-body");
  body.replaceChildren();
  const got = q ? decode(rows, q) : [];
  box.hidden = !got.length;
  if (!got.length) return;
  const r = got[0];
  body.append(el("p", { class: "decoded-q" }, el("strong", { text: `${r.id}: ` }), r.question));
  if (r.status === "not-covered") {
    body.append(el("p", { text: "Not covered yet: the hub has no route for this question." }));
  } else {
    if (r.status === "thin") body.append(el("p", { text: "Thin: the route rests on few records so far." }));
    if (r.approach) body.append(el("p", { text: r.approach }));
    const links = [...r.pages.map(p => el("a", { href: `../${p}` }, p)),
      ...r.record_ids.map(id => el("a", { href: siteLink("record.html", { id }) }, id))];
    if (links.length) body.append(el("ul", { class: "plain-list" }, links.map(a => el("li", {}, a))));
    if (r.risk) body.append(el("p", { text: `Risk: ${r.risk}` }));
  }
  if (r.keywords.length) {
    body.append(el("p", {}, "Search with its keywords: ",
      el("a", { href: siteLink("search.html", { q: r.keywords.join(" ") }) }, r.keywords.join(" "))));
  }
}

function showExamples(on) {
  const list = $("example-list");
  list.replaceChildren();
  if (on) for (const r of rows.slice(0, EXAMPLE_COUNT)) {
    list.append(el("li", {}, el("a", { href: siteLink("search.html", { q: r.question }) }, r.question)));
  }
  $("examples").hidden = !on || !rows.length;
}

async function run(state, push) {
  writeUrl(state, push);
  $("q").value = state.q;
  const results = $("results");
  const stateLine = $("state");
  const hasFilters = Object.keys(state.filters).length > 0;
  const active = Object.keys(state.filters).length + (state.all ? 1 : 0);
  $("filters-title").textContent = active ? `Filters (${active} active)` : "Filters";
  $("nearest").hidden = true;
  results.replaceChildren();
  if (!records) {
    stateLine.textContent = "Loading the index...";
    return;
  }
  if (!state.q && !hasFilters) {
    $("results-title").textContent = "Search";
    stateLine.textContent = "Type a question or a few words, or pick a filter.";
    $("decoded").hidden = true;
    showExamples(true);
    return;
  }
  showExamples(false);
  $("results-title").textContent = state.q ? `Results for "${state.q}"` : "Records matching the filters";
  showDecoded(state.q);
  const { hits, total } = await searchEngine().query(state.q, state.filters, state.all, RESULT_LIMIT);
  if (!hits.length) {
    stateLine.textContent = state.q
      ? `Searched, nothing found for "${state.q}"${hasFilters ? " with these filters" : ""}.`
      : "Searched, nothing found with these filters.";
    if (hasFilters) $("filters-box").open = true;
    if (rows.length && state.q) {
      const list = $("nearest-list");
      list.replaceChildren(...nearestRows(rows, state.q).map(r =>
        el("li", {}, keywordLink(r), el("span", { class: "muted", text: ` (${r.status})` }))));
      $("nearest").hidden = false;
    }
    return;
  }
  stateLine.textContent = `${hits.length} of ${total} results.`;
  results.append(...hits.map(hitItem));
}

async function main() {
  initChrome();
  const state = readUrl();
  $("q").value = state.q;
  $("filters").hidden = true;
  const decoder = await fetchJson(DECODER_URL, true).catch(() => null);
  rows = (decoder && decoder.rows) || [];
  try {
    records = await searchEngine().ready;
  } catch (err) {
    $("state").textContent = indexErrorText(err);
    return;
  }
  if (!records.length) {
    $("state").textContent = "The hub has no records yet, so there is nothing to search.";
    return;
  }
  buildFacets(state);
  $("filters").hidden = false;
  $("filters-box").open = Object.keys(state.filters).length > 0 || state.all;
  $("f-all").addEventListener("change", () => run(formState(), false));
  $("clear-filters").addEventListener("click", () => {
    for (const s of $("facets").querySelectorAll("select")) s.value = "";
    $("f-all").checked = false;
    run(formState(), false);
  });
  $("search-form").addEventListener("submit", ev => {
    ev.preventDefault();
    run(formState(), true);
  });
  window.addEventListener("popstate", () => {
    const s = readUrl();
    buildFacets(s);
    run(s, false);
  });
  run(state, false);
}

main();
