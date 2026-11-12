// node --test site/tests/ : the site scorer on the CLI test fixture.
import { test } from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import * as core from "../search_core.js";

const root = fileURLToPath(new URL("../../", import.meta.url));
const fix = root + "tools/tests_query/fixtures/index/";
const records = core.parseJsonl(readFileSync(fix + "records.jsonl", "utf8"));
const concepts = JSON.parse(readFileSync(fix + "concepts.json", "utf8")).concepts;
const pages = core.parseJsonl(readFileSync(fix + "pages.jsonl", "utf8"));
const rows = JSON.parse(readFileSync(root + "evals/decoder.json", "utf8")).rows;
const index = core.buildIndex(records, concepts, pages);

test("tokeniser keeps codes and folds alias pairs", () => {
  assert.deepEqual(core.tokens("T2V i2v MP4 on an M3 Max"), ["t2v", "i2v", "mp4", "m3", "max"]);
  assert.deepEqual(core.tokens("text to video"), ["t2v"]);
  assert.deepEqual(core.tokens("mcp-server"), core.tokens("mcpserver"));
});

test("ranks the expected record first", () => {
  const [hits] = core.search(index, "mcp-server render upload");
  assert.equal(hits[0].id, "tool:example/clip-mcp");
});

test("hidden records need includeHidden", () => {
  const ids = h => h[0].map(x => x.id);
  assert.ok(!ids(core.search(index, "oldcaptioner")).includes("tool:example/old-captioner"));
  assert.ok(ids(core.search(index, "oldcaptioner", {}, true)).includes("tool:example/old-captioner"));
});

test("filters keep only matching kinds and page chunks drop out", () => {
  const [hits] = core.search(index, "review loop", { kind: "source" }, false, 50);
  assert.ok(hits.length > 0);
  assert.ok(hits.every(h => h.kind === "source"));
});

test("default limit is 8", () => {
  const [hits, total] = core.search(index, "fixture");
  assert.equal(hits.length, 8);
  assert.ok(total > 8);
});

test("decoder: paraphrases hit their row, off-topic finds nothing", () => {
  const cases = JSON.parse(readFileSync(root + "evals/decoder_cases.json", "utf8"));
  for (const c of cases) assert.equal(core.decode(rows, c.question)[0]?.id, c.expect_row, c.question);
  assert.deepEqual(core.decode(rows, "best pizza recipe in town"), []);
  assert.equal(core.nearestRows(rows, "best pizza recipe in town").length, 3);
});

test("referencedBy covers related and recipe stages", () => {
  const refs = core.referencedBy(records, "tool:example/framewright");
  assert.ok(refs.some(([id, rel]) => id === "recipe:local-explainer" && rel === "stage"));
  assert.ok(refs.some(([id, rel]) => id === "tool:example/motion-skill" && rel === "extends"));
});

test("empty index gives nothing, not an error", () => {
  const empty = core.buildIndex([], [], []);
  assert.deepEqual(core.search(empty, "remotion"), [[], 0]);
});
