// Shared page code: index location, DOM helpers, badge, theme toggle, Cmd/Ctrl-K, combobox.
import { stem, rawWords } from "./search_core.js";

export const DEFAULT_INDEX = "../index/";
export const CONFIG_URL = "../hub.config.json";
export const DECODER_URL = "../evals/decoder.json";
const SUGGEST_LIMIT = 8;
const SUGGEST_DELAY_MS = 120;
const THEMES = ["auto", "light", "dark"];
export const BADGE_GLYPH = { "measured": "\u25CF", "quoted-primary": "\u25C6", "quoted-secondary": "\u25C7", "unverified": "\u25CB" };

const params = new URLSearchParams(location.search);

// ?index= lets a check point the site at another index copy. Same origin and relative only.
export function indexParam() {
  const raw = params.get("index");
  if (!raw || /^[a-z][a-z0-9+.-]*:|^\/\//i.test(raw)) return null;
  const url = new URL(raw.endsWith("/") ? raw : raw + "/", location.href);
  return url.origin === location.origin ? raw : null;
}

export function indexBase() {
  const p = indexParam();
  return new URL(p ? (p.endsWith("/") ? p : p + "/") : DEFAULT_INDEX, location.href).href;
}

export function siteLink(page, extra = {}) {
  const q = new URLSearchParams();
  for (const [k, v] of Object.entries(extra)) if (v) q.set(k, v);
  const p = indexParam();
  if (p) q.set("index", p);
  const s = q.toString();
  return page + (s ? "?" + s : "");
}

export function el(tag, attrs = {}, ...kids) {
  const n = document.createElement(tag);
  for (const [k, v] of Object.entries(attrs)) {
    if (v === null || v === undefined || v === false) continue;
    if (k === "class") n.className = v;
    else if (k === "text") n.textContent = v;
    else n.setAttribute(k, v === true ? "" : String(v));
  }
  for (const kid of kids.flat()) if (kid !== null && kid !== undefined && kid !== false) n.append(kid);
  return n;
}

export function safeHref(url) {
  try {
    const u = new URL(url);
    return u.protocol === "https:" || u.protocol === "http:" ? u.href : null;
  } catch (e) { return null; }
}

export function extLink(url, text) {
  const href = safeHref(url);
  return href ? el("a", { href, rel: "noopener noreferrer" }, text || url) : document.createTextNode(text || url || "-");
}

export async function fetchText(url, optional = false) {
  const res = await fetch(url);
  if (!res.ok) {
    if (optional) return null;
    const err = new Error(`HTTP ${res.status} for ${url}`);
    err.status = res.status;
    throw err;
  }
  return res.text();
}

export async function fetchJson(url, optional = false) {
  const t = await fetchText(url, optional);
  return t === null ? null : JSON.parse(t);
}

export function badge(b) {
  const tier = (b && b.tier) || "unverified";
  return el("span", { class: `badge badge-${tier}` },
    el("span", { class: "glyph", "aria-hidden": "true", text: BADGE_GLYPH[tier] || BADGE_GLYPH.unverified }),
    " ", (b && b.label) || "Unverified");
}

export function marker(kind, text) {
  return el("span", { class: `marker marker-${kind}` }, text);
}

// Text with every word whose stem was matched wrapped in <mark>.
export function highlight(text, matched) {
  const stems = new Set((matched || []).map(w => stem(w)));
  const frag = document.createDocumentFragment();
  for (const part of String(text || "").split(/([A-Za-z0-9]+)/)) {
    if (!part) continue;
    const w = rawWords(part)[0];
    if (w && /^[A-Za-z0-9]+$/.test(part) && stems.has(stem(w))) frag.append(el("mark", {}, part));
    else frag.append(part);
  }
  return frag;
}

export function shareText(v) {
  if (typeof v !== "number" || !isFinite(v)) return "not reported";
  const pct = v <= 1 ? v * 100 : v;
  return `${Math.round(pct)}%`;
}

export function dateText(v) {
  return v ? String(v).slice(0, 10) : "not reported";
}

// One search engine per page: a module worker, or the main thread where workers are missing.
let engine = null;
export function searchEngine() {
  if (engine) return engine;
  const base = indexBase();
  let send;
  const ready = new Promise((resolve, reject) => {
    try {
      const w = new Worker(new URL("./search_worker.js", import.meta.url), { type: "module" });
      const waiting = new Map();
      let seq = 0;
      w.onmessage = ev => {
        const m = ev.data;
        if (m.type === "ready") resolve(m.records);
        else if (m.type === "error") reject(new Error(m.message));
        else if (m.type === "result") { waiting.get(m.id)?.(m); waiting.delete(m.id); }
      };
      w.onerror = () => reject(new Error("worker failed"));
      send = (q, filters, all, limit) => new Promise(res => {
        seq += 1;
        waiting.set(seq, res);
        w.postMessage({ type: "search", id: seq, q, filters, all, limit });
      });
      w.postMessage({ type: "init", base });
    } catch (e) {
      import("./search_core.js").then(async core => {
        const recs = await fetchText(base + "records.jsonl");
        const concepts = await fetchJson(base + "concepts.json");
        const pages = await fetchText(base + "pages.jsonl", true);
        const records = core.parseJsonl(recs);
        const index = core.buildIndex(records, concepts.concepts || [], core.parseJsonl(pages || ""));
        send = async (q, filters, all, limit) => {
          const [hits, total] = core.search(index, q, filters, all, limit);
          return { hits, total };
        };
        resolve(records);
      }).catch(reject);
    }
  });
  engine = { ready, query: (q, filters = {}, all = false, limit = SUGGEST_LIMIT) => ready.then(() => send(q, filters, all, limit)) };
  return engine;
}

export function indexErrorText(err) {
  return /missing|404/.test(String(err && err.message))
    ? "The index is not built yet. Run python3 tools/build.py, then reload."
    : `The index could not be loaded: ${err && err.message}`;
}

function initTheme() {
  const btn = document.getElementById("theme-toggle");
  if (!btn) return;
  const root = document.documentElement;
  const show = () => { btn.textContent = `Theme: ${root.dataset.theme || "auto"}`; };
  btn.addEventListener("click", () => {
    const next = THEMES[(THEMES.indexOf(root.dataset.theme || "auto") + 1) % THEMES.length];
    if (next === "auto") delete root.dataset.theme;
    else root.dataset.theme = next;
    try {
      if (next === "auto") localStorage.removeItem("aml-theme");
      else localStorage.setItem("aml-theme", next);
    } catch (e) { /* storage blocked: the choice lasts for this page only */ }
    show();
  });
  show();
}

function initShortcut(input) {
  document.addEventListener("keydown", ev => {
    if ((ev.metaKey || ev.ctrlKey) && !ev.altKey && ev.key.toLowerCase() === "k") {
      ev.preventDefault();
      input.focus();
      input.select();
    }
  });
}

// ARIA combobox with a listbox popup of up to 8 records (APG "list autocomplete" pattern).
function initCombobox(input) {
  const list = document.getElementById(input.getAttribute("aria-controls"));
  const status = document.getElementById("q-status");
  const form = input.form;
  let options = [];
  let active = -1;
  let timer = 0;
  let asked = 0;

  const close = () => {
    list.hidden = true;
    input.setAttribute("aria-expanded", "false");
    input.removeAttribute("aria-activedescendant");
    active = -1;
  };
  const setActive = i => {
    options.forEach((o, n) => o.el.setAttribute("aria-selected", String(n === i)));
    active = i;
    if (i >= 0) {
      input.setAttribute("aria-activedescendant", options[i].el.id);
      options[i].el.scrollIntoView({ block: "nearest" });
    } else input.removeAttribute("aria-activedescendant");
  };
  const go = i => { location.href = siteLink("record.html", { id: options[i].hit.id }); };
  const render = (hits, q) => {
    list.replaceChildren();
    options = hits.filter(h => h.kind !== "page").map((h, n) => {
      const li = el("li", { id: `q-opt-${n}`, role: "option", "aria-selected": "false", class: "option" },
        el("span", { class: "option-title" }, highlight(h.title, h.matched)), " ",
        el("span", { class: "option-kind", text: h.kind }));
      li.addEventListener("mousedown", ev => ev.preventDefault());
      li.addEventListener("click", () => go(n));
      list.append(li);
      return { el: li, hit: h };
    });
    if (options.length) {
      list.hidden = false;
      input.setAttribute("aria-expanded", "true");
    } else close();
    if (status) status.textContent = q ? `${options.length} suggestions` : "";
    active = -1;
  };
  const suggest = () => {
    const q = input.value.trim();
    const mine = ++asked;
    if (!q) { render([], ""); return; }
    if (status) status.textContent = "Loading the index...";
    searchEngine().query(q).then(r => { if (mine === asked) render(r.hits, q); })
      .catch(err => { if (status) status.textContent = indexErrorText(err); close(); });
  };

  input.addEventListener("focus", () => { searchEngine(); }, { once: true });
  input.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(suggest, SUGGEST_DELAY_MS); });
  input.addEventListener("blur", close);
  input.addEventListener("keydown", ev => {
    const open = !list.hidden && options.length;
    if (ev.key === "ArrowDown") {
      ev.preventDefault();
      if (!open) { suggest(); return; }
      setActive(active + 1 >= options.length ? 0 : active + 1);
    } else if (ev.key === "ArrowUp") {
      if (!open) return;
      ev.preventDefault();
      setActive(active <= 0 ? options.length - 1 : active - 1);
    } else if (ev.key === "Enter") {
      if (open && active >= 0) { ev.preventDefault(); go(active); }
    } else if (ev.key === "Escape") {
      if (open) { ev.preventDefault(); close(); }
      else if (input.value) { ev.preventDefault(); input.value = ""; }
    }
  });
  if (form) {
    form.addEventListener("submit", () => {
      const p = indexParam();
      const hidden = form.querySelector('input[name="index"]');
      if (p && !hidden) form.append(el("input", { type: "hidden", name: "index", value: p }));
    });
  }
}

const FALLBACK_NAME = "Knowledge hub";

export function initChrome() {
  initTheme();
  fetchJson(CONFIG_URL, true).then(config => {
    const name = config && (config.title || config.name);
    if (!name) return;
    for (const b of document.querySelectorAll(".brand")) b.textContent = name;
    document.title = document.title.replace(FALLBACK_NAME, name);
  }).catch(() => {});
  const input = document.getElementById("q");
  if (input) {
    initShortcut(input);
    initCombobox(input);
  }
  for (const a of document.querySelectorAll("a[data-site-link]")) a.href = siteLink(a.getAttribute("href"));
}
