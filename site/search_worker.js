// Builds the search index off the main thread and answers queries.
import { buildIndex, parseJsonl, search } from "./search_core.js";

let index = null;

async function load(base) {
  const get = async (name, optional) => {
    const res = await fetch(base + name);
    if (!res.ok) {
      if (optional) return "";
      throw new Error(res.status === 404 ? "missing" : `HTTP ${res.status} for ${name}`);
    }
    return res.text();
  };
  const [recs, concepts, pages] = await Promise.all([get("records.jsonl"), get("concepts.json"), get("pages.jsonl", true)]);
  const records = parseJsonl(recs);
  index = buildIndex(records, JSON.parse(concepts).concepts || [], parseJsonl(pages));
  return records;
}

self.onmessage = async ev => {
  const m = ev.data;
  if (m.type === "init") {
    try {
      const records = await load(m.base);
      self.postMessage({ type: "ready", records });
    } catch (err) {
      self.postMessage({ type: "error", message: String(err.message || err) });
    }
  } else if (m.type === "search") {
    const [hits, total] = search(index, m.q, m.filters, m.all, m.limit);
    self.postMessage({ type: "result", id: m.id, hits, total });
  }
};
