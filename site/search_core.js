// Line-for-line port of tools/search_core.py. Change both together;
// `python3 tools/search_eval.py --parity` compares their rankings. No DOM use: runs in the
// browser, in a worker and under node.

export const K1 = 1.2;
export const SCORE_SCALE = 1000000;
export const EXCERPT_CHARS = 180;
export const WHY_CHARS = 160;

export const FIELDS = ["title", "aliases", "concepts", "facets", "summary", "why", "fit_notes", "claims", "text"];
export const FIELD_W = { title: 4.0, aliases: 3.0, concepts: 2.0, facets: 1.5, summary: 1.5,
  why: 1.0, fit_notes: 0.8, claims: 0.6, text: 1.0 };
export const FIELD_B = { title: 0.3, aliases: 0.3, concepts: 0.2, facets: 0.0, summary: 0.75,
  why: 0.75, fit_notes: 0.75, claims: 0.75, text: 0.75 };
const RECORD_SPEC = [FIELDS, FIELD_W, FIELD_B];

export const DECODE_FIELDS = ["keywords", "question", "approach", "risk"];
export const DECODE_W = { keywords: 2.0, question: 1.5, approach: 0.5, risk: 0.3 };
export const DECODE_B = { keywords: 0.3, question: 0.5, approach: 0.75, risk: 0.75 };
const DECODE_SPEC = [DECODE_FIELDS, DECODE_W, DECODE_B];
export const DECODE_MAX_ROWS = 3;
export const DECODE_NEAREST = 3;
export const DECODE_MIN_SHARE = 0.2;
export const DECODE_MIN_SCORE = 2.5;
export const DECODE_STRONG_SHARE = 0.6;
export const DECODE_STRONG_SCORE = 1.0;
export const DECODE_KEEP = 0.5;
const TRIGRAM = 3;

const STOP = new Set((
  "a an and are as at be by can could do does for from had has have how i if in into is it its " +
  "me my of on or our should so than that the their them then there these they this those to " +
  "us was we what when where which who why will with would you your").split(" "));
const PHRASES = [
  [["text", "to", "video"], ["t2v"]],
  [["image", "to", "video"], ["i2v"]],
  [["video", "to", "video"], ["v2v"]],
  [["text", "to", "image"], ["t2i"]],
  [["image", "to", "image"], ["i2i"]],
  [["text", "to", "speech"], ["tts"]],
  [["speech", "to", "text"], ["stt"]],
  [["mcpserver"], ["mcp", "server"]],
  [["mcpservers"], ["mcp", "server"]],
];
const SPLIT = /[^a-z0-9]+/;
const DIGIT = /[0-9]/;

export const HIDDEN_STATUS = ["archived", "retracted"];
export const SHUT_DOWN = "shut-down";
export const FILTERS = [["kind", "kind"], ["fit", "fit"], ["level", "level"], ["status", "status"],
  ["tool_type", "tool_type"], ["lever", "levers"], ["agent", "agents"],
  ["mode", "modes"], ["access", "access"], ["cost", "cost"]];
export const PAGE_KIND = "page";

const cmp = (a, b) => (a < b ? -1 : a > b ? 1 : 0);

export function stem(t) {
  if (DIGIT.test(t)) return t;
  if (t.length > 4 && t.endsWith("ies")) t = t.slice(0, -3) + "y";
  else if (t.length > 3 && t.endsWith("s") && !t.endsWith("ss") && !t.endsWith("us") && !t.endsWith("is")) t = t.slice(0, -1);
  let cut = false;
  if (t.length > 5 && t.endsWith("ing")) { t = t.slice(0, -3); cut = true; }
  else if (t.length > 4 && t.endsWith("ed") && !t.endsWith("eed")) { t = t.slice(0, -2); cut = true; }
  if (cut && t.length > 3 && t[t.length - 1] === t[t.length - 2] && !"lsz".includes(t[t.length - 1])) t = t.slice(0, -1);
  else if (t.length > 3 && t.endsWith("e")) t = t.slice(0, -1);
  return t;
}

export function rawWords(text) {
  const out = [];
  for (const w of String(text ?? "").toLowerCase().split(SPLIT)) if (w) out.push(w);
  return out;
}

function foldPhrases(words) {
  const out = [];
  let i = 0;
  while (i < words.length) {
    let hit = null;
    for (const [pat, rep] of PHRASES) {
      if (pat.every((p, j) => words[i + j] === p)) { hit = [pat, rep]; break; }
    }
    if (hit) { out.push(...hit[1]); i += hit[0].length; }
    else { out.push(words[i]); i += 1; }
  }
  return out;
}

export function surfaceWords(text) {
  return foldPhrases(rawWords(text)).filter(w => !STOP.has(w));
}

export function tokens(text) {
  return surfaceWords(text).map(stem);
}

export function queryTerms(query) {
  const out = [];
  const seen = new Set();
  for (const w of surfaceWords(query)) {
    const t = stem(w);
    if (!seen.has(t)) { seen.add(t); out.push([t, w]); }
  }
  return out;
}

export function join(v) {
  if (Array.isArray(v)) return v.filter(x => x !== null && x !== undefined).map(String).join(" ");
  return v === null || v === undefined ? "" : String(v);
}

export function isHidden(rec) {
  return HIDDEN_STATUS.includes(rec.status) || rec.maturity === SHUT_DOWN || rec.access === SHUT_DOWN;
}

function conceptText(ids, labels, conceptsById) {
  const parts = [...(labels || [])];
  for (const cid of ids || []) {
    const c = conceptsById.get(cid);
    if (c) {
      if (c.label && !parts.includes(c.label)) parts.push(c.label);
      parts.push(...(c.alt_labels || []));
      parts.push(...(c.hidden_labels || []));
    }
  }
  return join(parts);
}

export function recordEntry(rec, conceptsById) {
  const facets = [rec.tool_type, join(rec.levers), join(rec.modes), join(rec.agents), join(rec.video_types)];
  const claims = (rec.claims || []).filter(c => c && typeof c === "object").map(c => c.text);
  return { id: rec.id, kind: rec.kind || "", rec, fields: {
    title: join(rec.title), aliases: join(rec.aliases),
    concepts: conceptText(rec.concepts, rec.concept_labels, conceptsById),
    facets: join(facets), summary: join(rec.summary), why: join(rec.why_it_matters),
    fit_notes: join(rec.fit_notes), claims: join(claims), text: "" } };
}

export function pageEntry(chunk, conceptsById) {
  const heads = [];
  for (const h of [chunk.title].concat(chunk.heading_path || [])) if (h && !heads.includes(h)) heads.push(h);
  return { id: `${chunk.page_id ?? ""}#${chunk.anchor ?? ""}`, kind: PAGE_KIND, rec: chunk,
    fields: { title: join(heads), concepts: conceptText(chunk.concepts, [], conceptsById), text: join(chunk.text) } };
}

export class Index {
  constructor(entries, spec = RECORD_SPEC) {
    [this.fields, this.w, this.b] = spec;
    this.docs = [];
    for (const e of entries) {
      const lens = {};
      const tf = {};
      for (const f of this.fields) {
        const toks = tokens(e.fields[f] ?? "");
        lens[f] = toks.length;
        const m = new Map();
        for (const t of toks) m.set(t, (m.get(t) || 0) + 1);
        tf[f] = m;
      }
      this.docs.push({ e, len: lens, tf });
    }
    this.n = this.docs.length;
    this.avg = {};
    for (const f of this.fields) {
      let total = 0;
      for (const d of this.docs) total += d.len[f];
      this.avg[f] = (this.n ? total / this.n : 0) || 1.0;
    }
    this.df = new Map();
    for (const d of this.docs) {
      const seen = new Set();
      for (const f of this.fields) for (const t of d.tf[f].keys()) seen.add(t);
      for (const t of seen) this.df.set(t, (this.df.get(t) || 0) + 1);
    }
  }

  idf(t) {
    const c = this.df.get(t) || 0;
    return Math.log(1 + (this.n - c + 0.5) / (c + 0.5));
  }

  score(d, q) {
    let s = 0.0;
    const matched = [];
    for (const [t, w] of q) {
      let tfw = 0.0;
      for (const f of this.fields) {
        const c = d.tf[f].get(t) || 0;
        if (c) {
          const norm = 1 - this.b[f] + this.b[f] * d.len[f] / this.avg[f];
          tfw += this.w[f] * c / norm;
        }
      }
      if (tfw > 0) {
        s += this.idf(t) * tfw / (K1 + tfw);
        matched.push(w);
      }
    }
    return [s, matched];
  }

  rank(query) {
    const q = queryTerms(query);
    if (!q.length) return [];
    const hits = [];
    for (const d of this.docs) {
      const [s, matched] = this.score(d, q);
      if (s > 0) hits.push([Math.floor(s * SCORE_SCALE + 0.5), d.e, matched]);
    }
    hits.sort((a, b) => b[0] - a[0] || cmp(a[1].id, b[1].id));
    return hits.map(([s, e, m]) => [s / SCORE_SCALE, e, m]);
  }
}

export function buildIndex(records, concepts = [], pages = []) {
  const byId = new Map((concepts || []).map(c => [c.id, c]));
  const entries = (records || []).map(r => recordEntry(r, byId));
  for (const p of pages || []) entries.push(pageEntry(p, byId));
  return new Index(entries);
}

export function filterOk(rec, filters) {
  for (const [name, field] of FILTERS) {
    const want = filters[name];
    if (!want) continue;
    const have = rec[field];
    if (Array.isArray(have)) { if (!have.includes(want)) return false; }
    else if (have !== want) return false;
  }
  return true;
}

export function visible(entry, filters, includeHidden) {
  const active = {};
  for (const [k, v] of Object.entries(filters || {})) if (v) active[k] = v;
  const keys = Object.keys(active);
  if (entry.kind === PAGE_KIND) return !keys.length || (keys.length === 1 && active.kind === PAGE_KIND);
  const rec = entry.rec;
  if (!filterOk(rec, active)) return false;
  if (includeHidden || !isHidden(rec)) return true;
  return HIDDEN_STATUS.includes(active.status) || active.access === SHUT_DOWN;
}

export function clip(text, limit) {
  text = String(text ?? "").replace(/\s+/g, " ").trim();
  const chars = Array.from(text);
  if (chars.length <= limit) return text;
  let cut = chars.slice(0, limit).join("");
  const space = cut.lastIndexOf(" ");
  if (space > 0) cut = cut.slice(0, space);
  return cut.replace(/[ ,;:.]+$/, "") + "...";
}

export function oneLine(text, limit = WHY_CHARS) {
  text = String(text ?? "").replace(/\s+/g, " ").trim();
  const m = /[.!?](\s|$)/.exec(text);
  if (m) text = text.slice(0, m.index + 1);
  return clip(text, limit);
}

export function hitOf(entry, score, matched) {
  const rec = entry.rec;
  if (entry.kind === PAGE_KIND) {
    return { id: entry.id, kind: PAGE_KIND, title: rec.title || entry.id, badge: null,
      why: (rec.heading_path || []).join(" > "), path: rec.path || "", anchor: rec.anchor || "", score,
      matched, excerpt: clip(rec.text, EXCERPT_CHARS), checked_date: rec.last_reviewed || "",
      hidden: false, stale: false };
  }
  const badge = rec.badge || {};
  return { id: rec.id, kind: rec.kind || "", title: rec.title || rec.id,
    badge: { tier: badge.tier || "unverified", label: badge.label || "Unverified" },
    why: oneLine(rec.why_it_matters), path: rec.path || "", anchor: "", score, matched,
    excerpt: clip(rec.summary, EXCERPT_CHARS), checked_date: (rec.checked || {}).date || "",
    hidden: isHidden(rec), stale: Boolean(rec.stale) };
}

export function search(index, query, filters = {}, includeHidden = false, limit = 8) {
  let pool;
  if (!queryTerms(query).length) {
    if (!String(query ?? "").trim()) {
      pool = index.docs.filter(d => d.e.kind !== PAGE_KIND).map(d => [0.0, d.e, []]);
      pool.sort((a, b) => cmp(a[1].id, b[1].id));
    } else pool = [];
  } else pool = index.rank(query);
  const kept = pool.filter(([, e]) => visible(e, filters, includeHidden)).map(([s, e, m]) => hitOf(e, s, m));
  return [kept.slice(0, Math.max(0, limit)), kept.length];
}

// ---- decoder

export function decoderIndex(rows) {
  const entries = rows.map(r => ({ id: r.id, kind: "row", rec: r, fields: {
    keywords: join(r.keywords), question: join(r.question), approach: join(r.approach), risk: join(r.risk) } }));
  return new Index(entries, DECODE_SPEC);
}

export function trigrams(text) {
  const s = " " + rawWords(text).join(" ") + " ";
  const out = new Set();
  for (let i = 0; i < s.length - TRIGRAM + 1; i++) out.add(s.slice(i, i + TRIGRAM));
  return out;
}

export function dice(a, b) {
  if (!a.size || !b.size) return 0.0;
  let both = 0;
  for (const g of a) if (b.has(g)) both += 1;
  return 2 * both / (a.size + b.size);
}

function rowOut(r, score, matched) {
  return { id: r.id, question: r.question || "", status: r.status || "not-covered", score, matched,
    keywords: [...(r.keywords || [])], approach: r.approach || "", pages: [...(r.pages || [])],
    record_ids: [...(r.record_ids || [])], examples: [...(r.examples || [])], risk: r.risk || "" };
}

export function decode(rows, question, limit = DECODE_MAX_ROWS) {
  if (!rows || !rows.length) return [];
  const idx = decoderIndex(rows);
  const q = queryTerms(question);
  let total = 0.0;
  for (const [t] of q) total += idx.idf(t);
  const ranked = idx.rank(question);
  if (!ranked.length || total <= 0) return [];
  const out = [];
  const best = ranked[0][0];
  for (const [s, e, m] of ranked.slice(0, Math.max(1, limit))) {
    let share = 0.0;
    for (const [t, w] of q) if (m.includes(w)) share += idx.idf(t);
    share = share / total;
    const answers = (share >= DECODE_MIN_SHARE && s >= DECODE_MIN_SCORE) ||
      (share >= DECODE_STRONG_SHARE && s >= DECODE_STRONG_SCORE);
    if (!answers || (out.length && s < DECODE_KEEP * best)) {
      if (!out.length) return [];
      break;
    }
    out.push(rowOut(e.rec, s, m));
  }
  return out;
}

export function nearestRows(rows, question, n = DECODE_NEAREST) {
  const idx = decoderIndex(rows);
  const q = queryTerms(question);
  const scores = new Map();
  for (const [s, e, m] of q.length ? idx.rank(question) : []) scores.set(e.id, [s, m]);
  const qg = trigrams(question);
  const keyed = [];
  for (const r of rows) {
    const [s, m] = scores.get(r.id) || [0.0, []];
    const tri = Math.floor(dice(qg, trigrams(join(r.question) + " " + join(r.keywords))) * SCORE_SCALE + 0.5);
    keyed.push([-Math.floor(s * SCORE_SCALE + 0.5), -tri, r.id, r, s, m]);
  }
  keyed.sort((a, b) => a[0] - b[0] || a[1] - b[1] || cmp(a[2], b[2]));
  return keyed.slice(0, n).map(k => rowOut(k[3], k[4], k[5]));
}

export function referencedBy(records, rid) {
  const out = [];
  for (const r of records) {
    if (r.id === rid) continue;
    for (const rel of r.related || []) {
      if (rel && typeof rel === "object" && rel.id === rid) out.push([r.id, rel.rel || "related"]);
    }
    for (const st of r.stages || []) {
      if (st && typeof st === "object" && st.record_id === rid) out.push([r.id, "stage"]);
    }
  }
  out.sort((a, b) => cmp(a[0], b[0]) || cmp(a[1], b[1]));
  const dedup = [];
  for (const x of out) if (!dedup.some(y => y[0] === x[0] && y[1] === x[1])) dedup.push(x);
  return dedup;
}

export function parseJsonl(text) {
  return String(text || "").split("\n").filter(l => l.trim()).map(l => JSON.parse(l));
}
