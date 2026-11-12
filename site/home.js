import { CONFIG_URL, DECODER_URL, dateText, el, fetchJson, indexBase, initChrome, shareText, siteLink } from "./common.js";

const EXAMPLE_COUNT = 3;

function recordCount(meta, kinds) {
  const c = (meta && meta.counts) || {};
  if (typeof c.records === "number") return c.records;
  if (typeof c.total === "number") return c.total;
  return kinds.reduce((n, k) => n + (typeof c[k] === "number" ? c[k] : 0), 0);
}

function setText(id, text) {
  const n = document.getElementById(id);
  if (n) n.textContent = text;
}

async function main() {
  initChrome();
  const [config, decoder] = await Promise.all([
    fetchJson(CONFIG_URL, true).catch(() => null),
    fetchJson(DECODER_URL, true).catch(() => null),
  ]);
  let meta = null;
  let metaError = null;
  try { meta = await fetchJson(indexBase() + "meta.json"); } catch (e) { metaError = e; }

  if (config) {
    setText("hub-title", config.title || config.name || "Knowledge hub");
    setText("hub-tagline", config.tagline || "");
    document.title = config.title || document.title;
    document.querySelector(".brand").textContent = config.title || config.name || "Knowledge hub";
    if (config.base_url) {
      document.getElementById("llms-live").textContent = ` (live: ${new URL("llms.txt", config.base_url).href})`;
    }
    if (config.repo_url) {
      setText("clone-line", `git clone ${config.repo_url}\ncd ${config.name || "hub"}\n` +
        `python3 tools/query.py search "<words>"\npython3 tools/query.py decode "<question>"`);
    }
  }

  const state = document.getElementById("counters-state");
  const records = meta ? recordCount(meta, (config && config.kinds) || []) : 0;
  if (!meta) {
    state.textContent = metaError && metaError.status === 404
      ? "The index is not built yet, so the hub has no records to show. Run python3 tools/build.py."
      : "The hub's numbers could not be loaded.";
  } else if (!records) {
    state.textContent = "The hub has no records yet.";
  } else {
    state.hidden = true;
    const lifetime = meta.lifetime || (config && config.lifetime) || "not reported";
    const dl = document.getElementById("counters");
    for (const [term, value] of [
      ["Records", String(records)],
      ["Read at the primary source", shareText(meta.primary_read_share)],
      ["Last build", dateText(meta.built)],
      ["Living or snapshot", lifetime === "living" ? "Living, still updated" : lifetime === "snapshot" ? "Snapshot, no longer updated" : lifetime],
    ]) dl.append(el("div", { class: "counter" }, el("dt", { text: term }), el("dd", { text: value })));
    dl.hidden = false;
  }

  const rows = (decoder && decoder.rows) || [];
  if (rows.length && records) {
    const covered = rows.filter(r => r.status === "covered");
    const pick = (covered.length >= EXAMPLE_COUNT ? covered : rows).slice(0, EXAMPLE_COUNT);
    const list = document.getElementById("example-list");
    for (const r of pick) list.append(el("li", {}, el("a", { href: siteLink("search.html", { q: r.question }) }, r.question)));
    document.getElementById("examples").hidden = false;
  }

  if (meta || config) {
    const bits = [];
    if (meta && meta.built) bits.push(`Last build ${dateText(meta.built)}.`);
    const life = (meta && meta.lifetime) || (config && config.lifetime);
    if (life) bits.push(life === "living" ? "This hub is living: it is still updated." : "This hub is a snapshot.");
    bits.push("No tracking.");
    setText("footer-line", bits.join(" "));
  }
}

main();
