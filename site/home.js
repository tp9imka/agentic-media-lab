// Home page, "Proof first": every figure below is read from a data file at run time.
import { CONFIG_URL, DECODER_URL, el, fetchJson, fetchText, glyph, indexBase, initChrome, siteLink, status } from "./common.js";

const EXAMPLE = "../examples/clipcheck-fix-loop/";
const REPORT_URL = EXAMPLE + "results/clipcheck-before.json";
const SERIES_URL = EXAMPLE + "results/series-before.json";
const EXAMPLE_URL = EXAMPLE + "example.json";
const README_URL = EXAMPLE + "README.md";
const FACTCHECK_URL = "../evals/factcheck/2026-11-12.json";
const FRAME_DIR = "assets/frames/";
const FRAME_W = 640;
const FRAME_H = 360;
const QUESTION_IDS = ["q02", "q01", "q07"];
const ASK_QUESTION_ID = "q01";
const SVG_NS = "http://www.w3.org/2000/svg";

const TRACE_MAX_SHARE = 0.30;
const TRACE_VIEW_H = 40;
const TICK_S = 1;
const AXIS_STEP_WIDE_S = 2;
const AXIS_STEP_NARROW_S = 5;
const MARK_MIN_PX = 3;
const FLAG_GAP_PX = 6;
const FLAG_STACK_PX = 6;

const $ = id => document.getElementById(id);

function say(id, text) {
  const n = $(id);
  n.textContent = text;
  n.hidden = false;
}

const round3 = v => v.toFixed(3);
const point = v => (Number.isInteger(v) ? v.toFixed(1) : String(v));
const timeText = w => (w.end_s > w.start_s ? `${round3(w.start_s)}-${round3(w.end_s)} s` : `${point(w.start_s)} s`);
const pct = v => `${v}%`;
const sum = obj => Object.values(obj).reduce((a, n) => a + (n || 0), 0);

// Markdown bold is kept, as on the Foundations quote block.
function inline(text) {
  const frag = document.createDocumentFragment();
  String(text).split(/\*\*(.+?)\*\*/).forEach((part, i) => { if (part) frag.append(i % 2 ? el("strong", { text: part }) : part); });
  return frag;
}

// One mark per `where` range: E1..En for errors, W1..Wn for the rest, in file order.
function marksOf(report) {
  const fps = (report.stream && report.stream.fps) || 0;
  const out = [];
  const count = { E: 0, W: 0 };
  for (const f of report.findings || []) {
    const p = f.severity === "error" ? "E" : "W";
    let lead = null;
    (f.where || []).forEach((w, i) => {
      count[p] += 1;
      const id = p + count[p];
      lead = lead || id;
      const frame = Number.isInteger(w.first_frame) ? w.first_frame : fps ? Math.round(w.start_s * fps) : null;
      out.push({ id, lead, sev: p === "E" ? "error" : "warning", finding: f, where: w, first: i === 0, span: f.where.length, frame });
    });
  }
  return out;
}

function frameNote(w) {
  if (!w.frames) return "";
  return w.frames === 1 ? `1 frame, #${w.first_frame}` : `${w.frames} frames from #${w.first_frame}`;
}

function renderMeta(r) {
  const s = r.stream || {};
  const bits = [r.video,
    s.width && s.height ? `${s.width}x${s.height}` : null,
    s.fps ? `${s.fps} fps` : null,
    s.duration ? `${s.duration.toFixed(2)} s` : null,
    s.codec || null,
    r.contract ? `contract ${r.contract}` : null].filter(Boolean);
  $("strip-stream").replaceChildren(...bits.map((t, i) => el("span", { class: i ? null : "strip-file", text: t })));
  const plural = (n, w) => `${n} ${w}${n === 1 ? "" : "s"}`;
  $("strip-verdict").replaceChildren(
    el("span", { class: `strip-verdict strip-verdict-${r.verdict}` }, glyph(r.verdict === "pass" ? "passed" : "error"),
      String(r.verdict || "no verdict").toUpperCase()),
    el("span", { text: plural(r.errors, "error") }),
    el("span", { text: plural(r.warnings, "warning") }),
    el("span", { text: `${(r.passed || []).length} rules passed` }));
  $("clip-crumb").textContent += ` / ${r.video}`;
}

function renderTrace(series, marks, duration) {
  const values = series.content || [];
  if (!values.length) throw new Error("empty series");
  const n = values.length;
  const y = v => (TRACE_VIEW_H - Math.min(v, TRACE_MAX_SHARE) / TRACE_MAX_SHARE * TRACE_VIEW_H).toFixed(2);
  const ranges = marks.filter(m => m.sev === "error").map(m => timeText(m.where));
  const label = `Share of pixels showing scene content, per frame, ${n} frames over ${duration} s.` +
    (ranges.length ? ` It falls below the empty threshold at ${ranges.join(", ")}.` : "");
  const svg = document.createElementNS(SVG_NS, "svg");
  for (const [k, v] of Object.entries({ viewBox: `0 0 ${n - 1} ${TRACE_VIEW_H}`, preserveAspectRatio: "none", role: "img", "aria-label": label, class: "trace" })) svg.setAttribute(k, v);
  const line = document.createElementNS(SVG_NS, "polyline");
  for (const [k, v] of Object.entries({ points: values.map((v, i) => `${i},${y(v)}`).join(" "), fill: "none", "vector-effect": "non-scaling-stroke" })) line.setAttribute(k, v);
  svg.append(line);
  $("strip-trace").replaceChildren(svg);
  return values.some(v => v > TRACE_MAX_SHARE);
}

function renderAxis(duration) {
  const ticks = el("div", { class: "axis-ticks" });
  ticks.style.setProperty("--ticks", Math.round(duration / TICK_S));
  for (let t = TICK_S; t <= duration + 1e-9; t += TICK_S) ticks.append(el("span", { class: Math.round(t) % AXIS_STEP_WIDE_S ? null : "major" }));
  const labels = (step, cls) => {
    const row = el("div", { class: `axis-labels ${cls}` });
    for (let t = 0; t <= duration + 1e-9; t += step) {
      const edge = t === 0 ? "first" : Math.abs(t - duration) < 1e-9 ? "last" : null;
      const s = el("span", { class: edge, text: edge ? `${t} s` : String(t) });
      if (!edge) s.style.left = pct(t / duration * 100);
      row.append(s);
    }
    return row;
  };
  $("strip-axis").replaceChildren(ticks, labels(AXIS_STEP_WIDE_S, "wide"), labels(AXIS_STEP_NARROW_S, "narrow"));
}

function renderMarks(marks, duration) {
  const box = $("strip-marks");
  box.replaceChildren(...marks.map(m => {
    const node = el("div", { class: `mark mark-${m.sev}`, "data-start": m.where.start_s, "data-end": m.where.end_s },
      el("span", { class: "flag", text: m.id }), el("span", { class: "band" }));
    node.style.left = pct(m.where.start_s / duration * 100);
    node.style.width = pct((m.where.end_s - m.where.start_s) / duration * 100);
    return node;
  }));
  const strip = $("strip");
  const lay = () => layoutFlags(strip, box, duration);
  lay();
  if ("ResizeObserver" in window) new ResizeObserver(lay).observe(strip);
  else addEventListener("resize", lay);
  if (document.fonts) document.fonts.ready.then(lay);
}

// Each flag takes the first row where it clears the flag before it; a flag that would run past
// the right edge is anchored to its mark's right side. Rows are added until nothing overlaps.
function layoutFlags(strip, box, duration) {
  const width = box.clientWidth;
  if (!width) return;
  const items = [...box.children].map(m => ({ m, f: m.firstChild, x0: m.dataset.start / duration * width, x1: m.dataset.end / duration * width }))
    .sort((a, b) => a.x0 - b.x0);
  const ends = [];
  let rowH = 0;
  for (const it of items) {
    const w = it.f.offsetWidth;
    rowH = Math.max(rowH, it.f.offsetHeight);
    const flip = it.x0 + w > width;
    const left = flip ? Math.max(it.x1, it.x0 + MARK_MIN_PX) - w : it.x0;
    let row = ends.findIndex(end => left >= end + FLAG_GAP_PX);
    if (row < 0) { row = ends.length; ends.push(0); }
    ends[row] = left + w;
    it.f.classList.toggle("flag-right", flip);
    it.m.style.setProperty("--row", row);
  }
  strip.style.setProperty("--flag-row", `${rowH + FLAG_STACK_PX}px`);
  strip.style.setProperty("--flag-rows", Math.max(1, ends.length));
}

function provenance(f) {
  return (f.provenance || []).map(p => {
    const id = p.record || "";
    const link = id.startsWith("example:")
      ? el("a", { href: `../examples/${id.slice("example:".length)}/README.md` }, id)
      : el("a", { href: siteLink("record.html", { id }) }, id);
    const src = el("p", { class: "quote-source" }, link);
    if (p.quote) return el("div", { class: "prov" }, el("blockquote", {}, el("p", {}, inline(p.quote))), src);
    return el("div", { class: "prov prov-note" }, el("p", { class: "label", text: "Run note" }),
      el("p", { class: "note-text", text: p.note || "no note recorded" }), src);
  });
}

function measured(f) {
  const rows = Object.entries(f.measured || {}).map(([k, v]) =>
    el("div", {}, el("dt", { text: k.replace(/_/g, " ") }), el("dd", { text: Array.isArray(v) ? v.join(", ") : String(v) })));
  return rows.length ? el("dl", { class: "measured" }, rows) : null;
}

function findingRow(m) {
  const f = m.finding;
  const idCell = el("td", { class: "f-id" }, el("span", { class: "fid", text: m.id }), " ", status(m.sev, m.sev),
    m.first ? null : el("span", { class: "rail-only", text: ` ${f.rule}. Same rule and source as ${m.lead}.` }));
  const img = m.frame === null ? null : el("img", {
    src: `${FRAME_DIR}hf-d${String(m.frame).padStart(3, "0")}.jpg`, width: FRAME_W, height: FRAME_H, loading: "lazy",
    alt: `Frame ${m.frame} at ${point(m.where.start_s)} s, flagged by ${f.rule}`,
  });
  if (img) img.addEventListener("error", () => img.remove());
  const note = frameNote(m.where);
  const timeCell = el("td", { class: "f-time" }, el("span", { class: "t", text: timeText(m.where) }),
    note ? " " : null, note ? el("span", { class: "t-note", text: note }) : null, img);
  const tr = el("tr", { class: `frow frow-${m.sev}`, "data-mark": m.id }, idCell, timeCell);
  if (m.first) {
    const span = m.span > 1 ? m.span : null;
    tr.append(
      el("td", { class: "f-rule", rowspan: span },
        el("p", { class: "rule-name", text: f.rule }),
        el("p", { class: "finding-title", text: f.title || f.rule }),
        el("p", { class: "finding-msg", text: f.message || "" }),
        measured(f),
        f.hint ? el("p", { class: "finding-fix", text: `Fix: ${f.hint}` }) : null),
      el("td", { class: "f-source", rowspan: span }, provenance(f)));
  }
  return tr;
}

function renderFindings(r, marks) {
  $("findings-body").replaceChildren(...marks.map(findingRow));
  const passed = r.passed || [];
  if (passed.length) {
    const p = $("passed");
    p.replaceChildren(el("span", { class: "sev sev-passed" }, glyph("passed"), `passed ${passed.length}`), " ",
      el("span", { text: passed.map(x => x.rule).join(", ") }));
    p.hidden = false;
  }
}

async function evidence() {
  let report;
  try { report = await fetchJson(REPORT_URL); } catch (e) {
    say("strip-stream", "The checker's report could not be loaded, so the strip has no marks.");
    say("findings-state", "The findings could not be loaded from clipcheck-before.json. The table below is the copy served with the page.");
    return null;
  }
  const marks = marksOf(report);
  const duration = report.stream && report.stream.duration;
  renderMeta(report);
  renderFindings(report, marks);
  if (!duration) {
    say("strip-note", "The report has no clip duration, so the marks cannot be placed.");
    return report;
  }
  renderAxis(duration);
  renderMarks(marks, duration);
  const fps = report.stream.fps;
  const frames = [...document.querySelectorAll(".strip-frames img")].map(i => +/(\d+)\.jpg$/.exec(i.src)[1]);
  const step = frames.length > 1 && fps ? (frames[1] - frames[0]) / fps : null;
  let clipped;
  try { clipped = renderTrace(await fetchJson(SERIES_URL), marks, duration); } catch (e) {
    say("strip-note", "The per-frame series could not be loaded, so the trace is missing. Marks sit at their measured times.");
    return report;
  }
  say("strip-note", (step ? `Frames sampled every ${step} s. ` : "") +
    `Green trace: share of pixels showing scene content, per frame, 0 to ${Math.round(TRACE_MAX_SHARE * 100)}%` +
    (clipped ? " (higher values are cut off at the top)" : "") + ". Marks sit at their measured times.");
  $("strip-note").classList.add("legend");
  return report;
}

function figure(term, value, opts = {}) {
  return el("div", {}, el("dt", { text: term }), el("dd", { class: opts.tone || null, text: value }),
    opts.src ? el("dd", { class: "fig-src" }, el("a", { href: opts.src }, opts.srcText || opts.src.replace(/^(\.\.\/)+/, ""))) : null);
}

async function fixLoop(report) {
  let ex, readme;
  try { [ex, readme] = await Promise.all([fetchJson(EXAMPLE_URL), fetchText(README_URL)]); } catch (e) {
    $("loop-line").textContent = "The fix-loop result could not be loaded from the example.";
    $("loop-wrong").replaceChildren(el("li", { text: "Could not be loaded." }));
    return;
  }
  const k = ex.key_result || "";
  const rt = ex.runtime || "";
  const rounds = /in (\d+) fix rounds?/i.exec(k);
  const review = /(\d+)\/(\d+) before and (\d+)\/(\d+) after/.exec(k);
  const check = /about ([\d.]+) s per clip to check/.exec(rt);
  const ocr = /([\d.]+) s with text reading/.exec(rt);
  const wall = /about ([\d.]+) minutes/.exec(rt);
  const renders = /^\|\s*Renders\s*\|\s*(\d+)/m.exec(readme);
  const sample = /\*\*Status: [^*]*\*\*\s+([^.]+\.)/.exec(readme);
  const line = $("loop-line");
  line.removeAttribute("role");
  line.textContent = rounds
    ? `Given only this output, an agent got the failing clip to PASS in ${rounds[1]} fix rounds, without looking at a frame.`
    : k;
  const dur = report && report.stream && report.stream.duration;
  const figs = [
    rounds && figure("fix rounds", rounds[1]),
    wall && figure("wall time", `~${wall[1]} min`),
    renders && figure("renders", renders[1]),
    check && figure(dur ? `clipcheck, per ${dur} s clip` : "clipcheck, per clip", `~${check[1]} s`),
    ocr && figure("with text reading", `~${ocr[1]} s`),
    review && figure(`blind review, before => after, of ${review[2]}`, `${review[1]} => ${review[3]}`),
  ].filter(Boolean);
  if (figs.length) {
    $("loop-figures").replaceChildren(...figs);
    $("loop-figures").hidden = false;
  }
  if (sample) say("loop-sample", `${sample[1]} The blind review is one reviewer's judgement.`);
  const section = readme.split(/^## What the checker got wrong\s*$/m)[1];
  const wrong = section ? [...section.split(/^## /m)[0].matchAll(/^- \*\*(.+?)\*\*/gm)].map(m => m[1].replace(/[.:]$/, "")) : [];
  $("loop-wrong").replaceChildren(...(wrong.length ? wrong : ["Not listed in the example's README."]).map(w => el("li", { text: w })));
}

function answers(decoder) {
  const rows = (decoder && decoder.rows) || [];
  const pick = QUESTION_IDS.map(id => rows.find(r => r.id === id)).filter(Boolean);
  $("questions").replaceChildren(...(pick.length ? pick.map(r => el("li", {}, el("a", { href: siteLink("search.html", { q: r.question }) },
    el("span", { class: "q-id", text: r.id }), el("span", { class: "q-text", text: r.question }),
    el("span", { class: "q-meta", text: `${(r.record_ids || []).length} records, ${(r.pages || []).length} pages =>` }))))
    : [el("li", { class: "data muted", text: "The reader questions could not be loaded." })]));
}

function areaFig(id, value, label) {
  $(id).replaceChildren(el("span", { class: "area-num", text: value }), el("span", { class: "area-label", text: label }));
}

async function areas(decoder, meta) {
  const rows = (decoder && decoder.rows) || [];
  if (rows.length) areaFig("area-answers", String(rows.length), `reader questions, ${rows.filter(r => r.status === "covered").length} covered`);
  else areaFig("area-answers", "-", "reader questions could not be loaded");
  if (meta && meta.counts) {
    const parts = Object.entries(meta.counts).filter(([, n]) => n > 0).map(([k, n]) => `${n} ${k}s`);
    areaFig("area-library", String(sum(meta.counts)), `records: ${parts.join(", ")}`);
  } else areaFig("area-library", "-", "record counts could not be loaded");
  try {
    const text = await fetchText(indexBase() + "pages.jsonl");
    const ids = new Set([...text.matchAll(/"page_id":\s*"(example:[^"]+)"/g)].map(m => m[1]));
    areaFig("area-lab", String(ids.size), "worked examples");
  } catch (e) { areaFig("area-lab", "-", "the example list could not be loaded"); }
}

async function trust(meta) {
  let fc = null;
  try { fc = await fetchJson(FACTCHECK_URL); } catch (e) { /* reported below */ }
  const t = fc && fc.combined && fc.combined.total;
  const metaSrc = indexBase() + "meta.json";
  const metaOpts = { src: metaSrc, srcText: "index/meta.json" };
  const figs = [];
  if (meta && meta.counts) figs.push(figure("records in the hub", String(sum(meta.counts)), metaOpts));
  if (t && typeof t.claims_checked === "number") {
    figs.push(figure("quotes found verbatim in their source", `${t.claims_checked - (t.quotes_not_verbatim || 0)}/${t.claims_checked}`, { tone: "tone-signal", src: FACTCHECK_URL }));
    if (typeof t.claim_rate_percent === "number")
      figs.push(figure(`of ${t.claims_checked} claims said more than their source`, `${t.claim_rate_percent}%`, { tone: "tone-amber", src: FACTCHECK_URL }));
    if (typeof t.claims_wrong === "number")
      figs.push(figure(t.claims_wrong === 1 ? "claim found wrong" : "claims found wrong", String(t.claims_wrong), { src: FACTCHECK_URL }));
  }
  if (meta && meta.lifetime) figs.push(figure(`status, last build ${meta.built || "not reported"}`, meta.lifetime, metaOpts));
  if (fc && fc.date) $("trust-h").textContent = `Fact-check, ${fc.date}`;
  const missing = [!meta && "index/meta.json", !t && "the fact-check file"].filter(Boolean);
  if (missing.length) $("trust-state").textContent = `Could not load ${missing.join(" or ")}. Figures from it are left out.`;
  else $("trust-state").hidden = true;
  if (figs.length) {
    $("trust").replaceChildren(...figs);
    $("trust").hidden = false;
  }
}

function agents(config, decoder) {
  if (config && /^https:\/\//.test(config.base_url || "")) {
    const url = new URL("llms.txt", config.base_url).href;
    $("agent-index").replaceChildren(el("a", { href: url }, url.replace(/^https:\/\//, "")));
  }
  if (config && /^https:\/\//.test(config.repo_url || "")) $("agent-clone").textContent = `git clone ${config.repo_url}`;
  const q = ((decoder && decoder.rows) || []).find(r => r.id === ASK_QUESTION_ID);
  if (q) $("agent-ask").textContent = `python3 tools/query.py decode "${q.question}"`;
}

async function main() {
  initChrome();
  const [config, decoder, meta] = await Promise.all([
    fetchJson(CONFIG_URL, true).catch(() => null),
    fetchJson(DECODER_URL, true).catch(() => null),
    fetchJson(indexBase() + "meta.json").catch(() => null),
  ]);
  agents(config, decoder);
  answers(decoder);
  const report = await evidence();
  await Promise.all([fixLoop(report), areas(decoder, meta), trust(meta)]);
}

main();
