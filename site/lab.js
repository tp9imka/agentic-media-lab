// Lab index: the example pages in index/pages.jsonl, each with its example.json and the clips its README links.
import { el, fetchJson, fetchText, glyph, indexBase, indexErrorText, initChrome } from "./common.js";
import { parseJsonl } from "./search_core.js";

const PREFIX = "example:";
const CLIP_LINK = /\]\((results\/[^)\s]+\.mp4)\)/g;
const STATUS_GLYPH = { ran: "measured" };
const VERDICT_GLYPH = { pass: "passed", fail: "error" };

const $ = id => document.getElementById(id);

function examplePages(rows) {
  const seen = new Map();
  for (const r of rows) {
    if (!String(r.page_id || "").startsWith(PREFIX) || seen.has(r.page_id)) continue;
    seen.set(r.page_id, { id: r.page_id, title: r.title || r.page_id, path: r.path || "" });
  }
  return [...seen.values()];
}

function word(map, value, cls) {
  const v = value || "not reported";
  return el("span", { class: `${cls} ${cls}-${map[v] ? v : "unknown"}` }, glyph(map[v] || "unknown"), v);
}

async function clips(base, readme) {
  const paths = [...new Set([...(readme || "").matchAll(CLIP_LINK)].map(m => m[1]))];
  const found = await Promise.all(paths.map(p => fetch(base + p, { method: "HEAD" }).then(r => (r.ok ? p : null)).catch(() => null)));
  return found.filter(Boolean);
}

async function item(page) {
  const base = "../" + page.path.replace(/[^/]*$/, "");
  const [ex, readme] = await Promise.all([fetchJson(base + "example.json", true).catch(() => null), fetchText("../" + page.path, true).catch(() => null)]);
  const found = await clips(base, readme);
  const facts = ex
    ? [["status", word(STATUS_GLYPH, ex.status, "verdict")], ["verdict", word(VERDICT_GLYPH, ex.verdict, "verdict")],
      ["key result", ex.key_result || "not reported"], ["threshold", ex.threshold || "not reported"]]
    : [["details", "example.json could not be loaded"]];
  return el("li", { class: "lab-item" },
    el("h2", {}, el("a", { href: "../" + page.path }, (ex && ex.title) || page.title)),
    ex && ex.summary ? el("p", { text: ex.summary }) : null,
    el("dl", {}, facts.flatMap(([k, v]) => [el("dt", { text: k }), el("dd", {}, v)])),
    el("ul", { class: "lab-links", "aria-label": "Files" },
      el("li", {}, el("a", { href: "../" + page.path }, "README.md")),
      found.map(p => el("li", {}, el("a", { href: base + p }, p.split("/").pop())))));
}

async function main() {
  initChrome();
  const state = $("state");
  let pages;
  try { pages = examplePages(parseJsonl(await fetchText(indexBase() + "pages.jsonl"))); } catch (e) {
    state.textContent = indexErrorText(e);
    return;
  }
  if (!pages.length) {
    state.textContent = "The index lists no worked examples yet.";
    return;
  }
  const list = $("examples");
  list.replaceChildren(...await Promise.all(pages.map(item)));
  list.hidden = false;
  state.textContent = `${pages.length} worked example${pages.length === 1 ? "" : "s"}.`;
}

main();
