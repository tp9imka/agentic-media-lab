"""Shared lexical scorer: BM25F over records and page chunks, plus the decoder matcher.

site/search_core.js is a line-for-line port. Change both together;
`python3 tools/search_eval.py --parity` compares their rankings. Stdlib only.
"""
import math
import re

K1 = 1.2
SCORE_SCALE = 1_000_000  # scores are rounded to this grid so Python and JS order ties alike
EXCERPT_CHARS = 180
WHY_CHARS = 160

# Record and page-chunk fields with BM25F weight and length normalisation (b).
FIELDS = ("title", "aliases", "concepts", "facets", "summary", "why", "fit_notes", "claims", "text")
FIELD_W = {"title": 4.0, "aliases": 3.0, "concepts": 2.0, "facets": 1.5, "summary": 1.5,
           "why": 1.0, "fit_notes": 0.8, "claims": 0.6, "text": 1.0}
FIELD_B = {"title": 0.3, "aliases": 0.3, "concepts": 0.2, "facets": 0.0, "summary": 0.75,
           "why": 0.75, "fit_notes": 0.75, "claims": 0.75, "text": 0.75}
RECORD_SPEC = (FIELDS, FIELD_W, FIELD_B)

# Decoder rows: keywords are written to be matched, the question is the reader's wording.
DECODE_FIELDS = ("keywords", "question", "approach", "risk")
DECODE_W = {"keywords": 2.0, "question": 1.5, "approach": 0.5, "risk": 0.3}
DECODE_B = {"keywords": 0.3, "question": 0.5, "approach": 0.75, "risk": 0.75}
DECODE_SPEC = (DECODE_FIELDS, DECODE_W, DECODE_B)
DECODE_MAX_ROWS = 3
DECODE_NEAREST = 3
# A row answers the question when it matches DECODE_MIN_SHARE of the question's idf mass with
# score DECODE_MIN_SCORE, or most of a short question (DECODE_STRONG_SHARE) with a lower score.
# Calibrated on evals/decoder_cases.json and off-topic controls in tools/tests_query.
DECODE_MIN_SHARE = 0.2
DECODE_MIN_SCORE = 2.5
DECODE_STRONG_SHARE = 0.6
DECODE_STRONG_SCORE = 1.0
DECODE_KEEP = 0.5  # rows after the first are kept when they score this share of the best
TRIGRAM = 3

STOP = frozenset((
    "a an and are as at be by can could do does for from had has have how i if in into is it its "
    "me my of on or our should so than that the their them then there these they this those to "
    "us was we what when where which who why will with would you your").split())
# Token sequences folded to one token before stopwords are dropped ("text to video" => t2v).
PHRASES = (
    (("text", "to", "video"), ("t2v",)),
    (("image", "to", "video"), ("i2v",)),
    (("video", "to", "video"), ("v2v",)),
    (("text", "to", "image"), ("t2i",)),
    (("image", "to", "image"), ("i2i",)),
    (("text", "to", "speech"), ("tts",)),
    (("speech", "to", "text"), ("stt",)),
    (("mcpserver",), ("mcp", "server")),
    (("mcpservers",), ("mcp", "server")),
)
SPLIT = re.compile(r"[^a-z0-9]+")
DIGIT = re.compile(r"[0-9]")

HIDDEN_STATUS = ("archived", "retracted")
SHUT_DOWN = "shut-down"
# CLI / URL filter name => record field. List-valued fields match when they contain the value.
FILTERS = (("kind", "kind"), ("fit", "fit"), ("level", "level"), ("status", "status"),
           ("tool_type", "tool_type"), ("lever", "levers"), ("agent", "agents"),
           ("mode", "modes"), ("access", "access"), ("cost", "cost"))
PAGE_KIND = "page"


def stem(t):
    """Light suffix folding so "renders", "rendering" and "render" meet. Tokens with digits stay."""
    if DIGIT.search(t):
        return t
    if len(t) > 4 and t.endswith("ies"):
        t = t[:-3] + "y"
    elif len(t) > 3 and t.endswith("s") and not t.endswith(("ss", "us", "is")):
        t = t[:-1]
    cut = False
    if len(t) > 5 and t.endswith("ing"):
        t, cut = t[:-3], True
    elif len(t) > 4 and t.endswith("ed") and not t.endswith("eed"):
        t, cut = t[:-2], True
    if cut and len(t) > 3 and t[-1] == t[-2] and t[-1] not in "lsz":
        t = t[:-1]
    elif len(t) > 3 and t.endswith("e"):
        t = t[:-1]
    return t


def raw_words(text):
    out = []
    for w in SPLIT.split(str(text or "").lower()):
        if w:
            out.append(w)
    return out


def fold_phrases(words):
    out = []
    i = 0
    while i < len(words):
        hit = None
        for pat, rep in PHRASES:
            if tuple(words[i:i + len(pat)]) == pat:
                hit = (pat, rep)
                break
        if hit:
            out.extend(hit[1])
            i += len(hit[0])
        else:
            out.append(words[i])
            i += 1
    return out


def surface_words(text):
    """Words after phrase folding and stopword removal, not yet stemmed."""
    return [w for w in fold_phrases(raw_words(text)) if w not in STOP]


def tokens(text):
    return [stem(w) for w in surface_words(text)]


def query_terms(query):
    """[(stem, surface word)] in query order, one per distinct stem."""
    out = []
    seen = set()
    for w in surface_words(query):
        t = stem(w)
        if t not in seen:
            seen.add(t)
            out.append((t, w))
    return out


def join(v):
    if isinstance(v, list):
        return " ".join(str(x) for x in v if x is not None)
    return "" if v is None else str(v)


def is_hidden(rec):
    return (rec.get("status") in HIDDEN_STATUS or rec.get("maturity") == SHUT_DOWN
            or rec.get("access") == SHUT_DOWN)


def concept_text(ids, labels, concepts_by_id):
    parts = list(labels or [])
    for cid in ids or []:
        c = concepts_by_id.get(cid)
        if c:
            if c.get("label") and c["label"] not in parts:
                parts.append(c["label"])
            parts.extend(c.get("alt_labels") or [])
            parts.extend(c.get("hidden_labels") or [])
    return join(parts)


def record_entry(rec, concepts_by_id):
    facets = [rec.get("tool_type"), join(rec.get("levers")), join(rec.get("modes")),
              join(rec.get("agents")), join(rec.get("video_types"))]
    claims = [c.get("text") for c in rec.get("claims") or [] if isinstance(c, dict)]
    return {"id": rec["id"], "kind": rec.get("kind", ""), "rec": rec, "fields": {
        "title": join(rec.get("title")), "aliases": join(rec.get("aliases")),
        "concepts": concept_text(rec.get("concepts"), rec.get("concept_labels"), concepts_by_id),
        "facets": join(facets), "summary": join(rec.get("summary")), "why": join(rec.get("why_it_matters")),
        "fit_notes": join(rec.get("fit_notes")), "claims": join(claims), "text": ""}}


def page_entry(chunk, concepts_by_id):
    heads = []
    for h in [chunk.get("title")] + list(chunk.get("heading_path") or []):
        if h and h not in heads:
            heads.append(h)
    return {"id": f"{chunk.get('page_id', '')}#{chunk.get('anchor', '')}", "kind": PAGE_KIND, "rec": chunk,
            "fields": {"title": join(heads), "concepts": concept_text(chunk.get("concepts"), [], concepts_by_id),
                       "text": join(chunk.get("text"))}}


class Index:
    """BM25F over entries ({"id", "fields": {name: text}}) for one field spec."""

    def __init__(self, entries, spec=RECORD_SPEC):
        self.fields, self.w, self.b = spec
        self.docs = []
        for e in entries:
            lens = {}
            tf = {}
            for f in self.fields:
                toks = tokens(e["fields"].get(f, ""))
                lens[f] = len(toks)
                m = {}
                for t in toks:
                    m[t] = m.get(t, 0) + 1
                tf[f] = m
            self.docs.append({"e": e, "len": lens, "tf": tf})
        self.n = len(self.docs)
        self.avg = {}
        for f in self.fields:
            total = 0
            for d in self.docs:
                total += d["len"][f]
            self.avg[f] = (total / self.n if self.n else 0) or 1.0
        self.df = {}
        for d in self.docs:
            seen = set()
            for f in self.fields:
                seen.update(d["tf"][f])
            for t in seen:
                self.df[t] = self.df.get(t, 0) + 1

    def idf(self, t):
        c = self.df.get(t, 0)
        return math.log(1 + (self.n - c + 0.5) / (c + 0.5))

    def score(self, d, q):
        s = 0.0
        matched = []
        for t, w in q:
            tfw = 0.0
            for f in self.fields:
                c = d["tf"][f].get(t, 0)
                if c:
                    norm = 1 - self.b[f] + self.b[f] * d["len"][f] / self.avg[f]
                    tfw += self.w[f] * c / norm
            if tfw > 0:
                s += self.idf(t) * tfw / (K1 + tfw)
                matched.append(w)
        return s, matched

    def rank(self, query):
        """[(score, entry, matched surface words)] best first, ties by id."""
        q = query_terms(query)
        if not q:
            return []
        hits = []
        for d in self.docs:
            s, matched = self.score(d, q)
            if s > 0:
                hits.append((math.floor(s * SCORE_SCALE + 0.5), d["e"], matched))
        hits.sort(key=lambda h: (-h[0], h[1]["id"]))
        return [(s / SCORE_SCALE, e, m) for s, e, m in hits]


def build_index(records, concepts=None, pages=None):
    by_id = {c["id"]: c for c in concepts or []}
    entries = [record_entry(r, by_id) for r in records]
    entries += [page_entry(p, by_id) for p in pages or []]
    return Index(entries)


def filter_ok(rec, filters):
    for name, field in FILTERS:
        want = filters.get(name)
        if not want:
            continue
        have = rec.get(field)
        if isinstance(have, list):
            if want not in have:
                return False
        elif have != want:
            return False
    return True


def visible(entry, filters, include_hidden):
    active = {k: v for k, v in filters.items() if v}
    if entry["kind"] == PAGE_KIND:
        return not active or active == {"kind": PAGE_KIND}
    rec = entry["rec"]
    if not filter_ok(rec, active):
        return False
    if include_hidden or not is_hidden(rec):
        return True
    # naming the hiding value in a filter shows those records without --all
    return active.get("status") in HIDDEN_STATUS or active.get("access") == SHUT_DOWN


def clip(text, limit):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    if len(text) <= limit:
        return text
    cut = text[:limit]
    space = cut.rfind(" ")
    if space > 0:
        cut = cut[:space]
    return cut.rstrip(" ,;:.") + "..."


def one_line(text, limit=WHY_CHARS):
    text = re.sub(r"\s+", " ", str(text or "")).strip()
    m = re.search(r"[.!?](\s|$)", text)
    if m:
        text = text[:m.start() + 1]
    return clip(text, limit)


def hit_of(entry, score, matched):
    rec = entry["rec"]
    if entry["kind"] == PAGE_KIND:
        return {"id": entry["id"], "kind": PAGE_KIND, "title": rec.get("title") or entry["id"],
                "badge": None, "why": " > ".join(rec.get("heading_path") or []),
                "path": rec.get("path") or "", "anchor": rec.get("anchor") or "", "score": score,
                "matched": matched, "excerpt": clip(rec.get("text"), EXCERPT_CHARS),
                "checked_date": rec.get("last_reviewed") or "", "hidden": False, "stale": False}
    badge = rec.get("badge") or {}
    return {"id": rec["id"], "kind": rec.get("kind", ""), "title": rec.get("title") or rec["id"],
            "badge": {"tier": badge.get("tier") or "unverified", "label": badge.get("label") or "Unverified"},
            "why": one_line(rec.get("why_it_matters")), "path": rec.get("path") or "", "anchor": "",
            "score": score, "matched": matched, "excerpt": clip(rec.get("summary"), EXCERPT_CHARS),
            "checked_date": (rec.get("checked") or {}).get("date") or "", "hidden": is_hidden(rec),
            "stale": bool(rec.get("stale"))}


def search(index, query, filters=None, include_hidden=False, limit=8):
    """(hits, total). Filters apply after ranking so corpus statistics never depend on them.
    An empty query lists the records that pass the filters, by id."""
    filters = filters or {}
    if not query_terms(query):
        if not str(query or "").strip():
            pool = [(0.0, d["e"], []) for d in index.docs if d["e"]["kind"] != PAGE_KIND]
            pool.sort(key=lambda h: h[1]["id"])
        else:
            pool = []
    else:
        pool = index.rank(query)
    kept = [hit_of(e, s, m) for s, e, m in pool if visible(e, filters, include_hidden)]
    return kept[:max(0, limit)], len(kept)


# ---- decoder

def decoder_index(rows):
    entries = [{"id": r["id"], "kind": "row", "rec": r, "fields": {
        "keywords": join(r.get("keywords")), "question": join(r.get("question")),
        "approach": join(r.get("approach")), "risk": join(r.get("risk"))}} for r in rows]
    return Index(entries, DECODE_SPEC)


def trigrams(text):
    s = " " + " ".join(raw_words(text)) + " "
    out = set()
    for i in range(len(s) - TRIGRAM + 1):
        out.add(s[i:i + TRIGRAM])
    return out


def dice(a, b):
    if not a or not b:
        return 0.0
    return 2 * len(a & b) / (len(a) + len(b))


def row_out(r, score, matched):
    return {"id": r["id"], "question": r.get("question", ""), "status": r.get("status", "not-covered"),
            "score": score, "matched": matched, "keywords": list(r.get("keywords") or []),
            "approach": r.get("approach", ""), "pages": list(r.get("pages") or []),
            "record_ids": list(r.get("record_ids") or []), "examples": list(r.get("examples") or []),
            "risk": r.get("risk", "")}


def decode(rows, question, limit=DECODE_MAX_ROWS):
    """Rows that answer the question, best first; [] when none clears DECODE_MIN_SHARE."""
    if not rows:
        return []
    idx = decoder_index(rows)
    q = query_terms(question)
    total = 0.0
    for t, _ in q:
        total += idx.idf(t)
    ranked = idx.rank(question)
    if not ranked or total <= 0:
        return []
    out = []
    best = ranked[0][0]
    for s, e, m in ranked[:max(1, limit)]:
        share = 0.0
        for t, w in q:
            if w in m:
                share += idx.idf(t)
        share = share / total
        answers = ((share >= DECODE_MIN_SHARE and s >= DECODE_MIN_SCORE)
                   or (share >= DECODE_STRONG_SHARE and s >= DECODE_STRONG_SCORE))
        if not answers or (out and s < DECODE_KEEP * best):
            if not out:
                return []
            break
        out.append(row_out(e["rec"], s, m))
    return out


def nearest_rows(rows, question, n=DECODE_NEAREST):
    """Closest rows even when nothing matched: decode score, then trigram overlap, then id."""
    idx = decoder_index(rows)
    q = query_terms(question)
    scores = {}
    for s, e, m in idx.rank(question) if q else []:
        scores[e["id"]] = (s, m)
    qg = trigrams(question)
    keyed = []
    for r in rows:
        s, m = scores.get(r["id"], (0.0, []))
        tri = math.floor(dice(qg, trigrams(join(r.get("question")) + " " + join(r.get("keywords"))))
                         * SCORE_SCALE + 0.5)
        keyed.append((-math.floor(s * SCORE_SCALE + 0.5), -tri, r["id"], r, s, m))
    keyed.sort(key=lambda k: (k[0], k[1], k[2]))
    return [row_out(k[3], k[4], k[5]) for k in keyed[:n]]


def referenced_by(records, rid):
    """[(id, rel)] of records whose related list or recipe stages point at rid."""
    out = []
    for r in records:
        if r.get("id") == rid:
            continue
        for rel in r.get("related") or []:
            if isinstance(rel, dict) and rel.get("id") == rid:
                out.append((r["id"], rel.get("rel") or "related"))
        for st in r.get("stages") or []:
            if isinstance(st, dict) and st.get("record_id") == rid:
                out.append((r["id"], "stage"))
    out.sort()
    dedup = []
    for x in out:
        if x not in dedup:
            dedup.append(x)
    return dedup
