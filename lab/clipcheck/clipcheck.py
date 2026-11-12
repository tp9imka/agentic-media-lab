#!/usr/bin/env python3
"""clipcheck - a contract checker for agent-made video. Stdlib + ffmpeg/ffprobe on PATH.

A contract is the brief as data: size, rate, length, palette, safe area, scene times, loudness,
copy. clipcheck measures a rendered MP4 against it frame by frame and prints findings with
timestamps, each tied to the hub record its rule comes from. It is the deterministic half of a
review loop: cheap to run after every render, exact where sampled stills miss things.

usage: clipcheck.py <video> --contract contract.json [--source project-dir] [--captions file.vtt]
                    [--json out.json] [--index index/records.jsonl] [--ocr] [--quiet]
exit: 0 no error-level findings, 1 at least one, 2 usage or missing tools.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
GRID_W, GRID_H = 160, 90          # analysis resolution; one cell is 12 px on a 1920-wide frame
FG_DISTANCE = 40                  # RGB distance from the background that counts as content
PRESENCE_DISTANCE = 14            # lower bar for "something is on screen", so a fading element is not read as empty
MOTION_FLOOR = 0.0015             # mean per-pixel change (0..1) above which frames belong to a "move"
STILL_FLOOR = 0.0003              # below this nothing is changing at all; slow wipes sit between the two
EMPTY_COVERAGE = 0.0025           # share of content pixels below which a frame is "near-empty"
SPARSE_FACTOR = 0.2               # "sparse" is judged against the clip's typical amount of content
SPARSE_MIN_FRAMES = 3
CHROME_SHARE = 0.9                # a pixel lit in this share of frames is fixed chrome, not scene content
ABRUPT_TAIL_RATIO = 0.6           # last-frame speed over peak speed above which a move "stops dead"
MIN_BURST_FRAMES = 4
OCR_SAMPLE_EVERY_S = 0.5


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, **kw)


def hex_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def probe(video):
    out = run(["ffprobe", "-v", "error", "-show_streams", "-show_format", "-of", "json", str(video)], text=True)
    if out.returncode != 0:
        return None
    data = json.loads(out.stdout)
    v = next((s for s in data["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in data["streams"] if s["codec_type"] == "audio"), None)
    if not v:
        return None
    num, _, den = v.get("r_frame_rate", "0/1").partition("/")
    return {"width": v["width"], "height": v["height"], "fps": float(num) / float(den or 1),
            "frames": int(v.get("nb_frames") or 0), "codec": v.get("codec_name"), "pix_fmt": v.get("pix_fmt"),
            "color_space": v.get("color_space"), "color_primaries": v.get("color_primaries"),
            "color_transfer": v.get("color_transfer"), "duration": float(data["format"]["duration"]),
            "has_audio": bool(a)}


def frames(video):
    """Yield every frame as GRID_W x GRID_H rgb24 bytes."""
    size = GRID_W * GRID_H * 3
    # Convert to RGB before scaling: scaling in YUV 4:2:0 smears chroma and invents colours on thin elements.
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(video), "-vf",
                          f"format=gbrp,scale={GRID_W}:{GRID_H}:flags=area", "-pix_fmt", "rgb24", "-f", "rawvideo", "-"],
                         stdout=subprocess.PIPE)
    while True:
        buf = p.stdout.read(size)
        if len(buf) < size:
            break
        yield buf
    p.wait()


def analyse(video, background, allowed, palette_tol):
    """One pass over the frames: coverage, content box, off-palette share, motion."""
    br, bg, bb = background
    tol2, fg2, pr2 = palette_tol * palette_tol, FG_DISTANCE * FG_DISTANCE, PRESENCE_DISTANCE * PRESENCE_DISTANCE
    rows, prev_g, off_colours = [], None, {}
    for buf in frames(video):
        r, g, b = buf[0::3], buf[1::3], buf[2::3]
        fg = off = present = 0
        mask = bytearray(GRID_W * GRID_H)
        x0, y0, x1, y1 = GRID_W, GRID_H, -1, -1
        for i in range(GRID_W * GRID_H):
            dr, dg, db = r[i] - br, g[i] - bg, b[i] - bb
            d2 = dr * dr + dg * dg + db * db
            if d2 > pr2:
                present += 1
                mask[i] = 1
            if d2 <= fg2:
                continue
            fg += 1
            x, y = i % GRID_W, i // GRID_W
            if x < x0: x0 = x
            if x > x1: x1 = x
            if y < y0: y0 = y
            if y > y1: y1 = y
            if allowed is not None:
                # Anti-aliased edges are blends of an allowed colour with the background, so a pixel
                # is on-palette when it lies near the segment background -> allowed colour.
                ok = False
                for ar, ag, ab in allowed:
                    vr, vg, vb = ar - br, ag - bg, ab - bb
                    t = (dr * vr + dg * vg + db * vb) / ((vr * vr + vg * vg + vb * vb) or 1)
                    t = 0.0 if t < 0 else 1.0 if t > 1 else t
                    er, eg, eb = dr - t * vr, dg - t * vg, db - t * vb
                    if er * er + eg * eg + eb * eb <= tol2:
                        ok = True
                        break
                if not ok:
                    off += 1
                    key = (r[i] >> 4 << 4, g[i] >> 4 << 4, b[i] >> 4 << 4)
                    off_colours[key] = off_colours.get(key, 0) + 1
        motion = 0.0
        if prev_g is not None:
            motion = sum(abs(a - c) for a, c in zip(g, prev_g)) / (255.0 * len(g))
        prev_g = g
        n = GRID_W * GRID_H
        rows.append({"coverage": fg / n, "presence": present / n, "off": off / n, "motion": motion, "mask": mask,
                     "box": None if x1 < 0 else (x0 / GRID_W, y0 / GRID_H, (x1 + 1) / GRID_W, (y1 + 1) / GRID_H)})
    # Content = what is on screen minus fixed chrome (a rule or logo that never leaves). A frame that
    # shows only chrome is empty to a viewer even though pixels are lit.
    if rows:
        total = len(rows)
        lit = [0] * (GRID_W * GRID_H)
        for r in rows:
            m = r["mask"]
            for i in range(len(m)):
                if m[i]:
                    lit[i] += 1
        chrome = bytes(1 if c >= CHROME_SHARE * total else 0 for c in lit)
        keep = bytes(1 - c for c in chrome)
        size = GRID_W * GRID_H
        for r in rows:
            r["content"] = sum(a & b for a, b in zip(r.pop("mask"), keep)) / size
        rows[0]["chrome_share"] = sum(chrome) / size
    return rows, off_colours


def estimate_background(video):
    counts = {}
    for n, buf in enumerate(frames(video)):
        if n % 15:
            continue
        for i in range(0, len(buf), 3 * 7):
            key = (buf[i], buf[i + 1], buf[i + 2])
            counts[key] = counts.get(key, 0) + 1
    return max(counts, key=counts.get) if counts else (0, 0, 0)


def spans(flags, fps, min_frames=1):
    out, start = [], None
    for i, f in enumerate(list(flags) + [False]):
        if f and start is None:
            start = i
        elif not f and start is not None:
            if i - start >= min_frames:
                out.append({"start_s": round(start / fps, 3), "end_s": round(i / fps, 3), "frames": i - start,
                            "first_frame": start})
            start = None
    return out


def bursts(rows, fps):
    """Runs of motion, with how they end: a move that decelerates has a low tail ratio."""
    out = []
    for sp in spans([r["motion"] > MOTION_FLOOR for r in rows], fps, MIN_BURST_FRAMES):
        seg = [rows[i]["motion"] for i in range(sp["first_frame"], sp["first_frame"] + sp["frames"])]
        peak = max(seg)
        tail = sum(seg[-2:]) / 2
        head = sum(seg[:2]) / 2
        sp.update({"peak": round(peak, 5), "tail_ratio": round(tail / peak, 3), "head_ratio": round(head / peak, 3)})
        out.append(sp)
    return out


def loudness(video):
    log = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-af", "ebur128=peak=true", "-f", "null", "-"],
              text=True).stderr
    tail = log[log.rfind("Summary:"):] if "Summary:" in log else ""
    i = re.search(r"I:\s*(-?[0-9.]+) LUFS", tail)
    p = re.search(r"Peak:\s*(-?[0-9.]+) dBFS", tail)
    return (float(i.group(1)) if i else None, float(p.group(1)) if p else None)


def parse_captions(path):
    cues, block = [], []
    for line in Path(path).read_text(encoding="utf-8").splitlines() + [""]:
        if line.strip():
            block.append(line.strip())
            continue
        t = next((x for x in block if "-->" in x), None)
        if t:
            a, b = [s.strip().split(" ")[0] for s in t.split("-->")]
            text = [x for x in block[block.index(t) + 1:]]
            cues.append({"start": to_seconds(a), "end": to_seconds(b), "lines": [re.sub(r"<[^>]+>", "", x) for x in text]})
        block = []
    return cues


def to_seconds(ts):
    parts = ts.replace(",", ".").split(":")
    return sum(float(p) * 60 ** i for i, p in enumerate(reversed(parts)))


def ocr_text(video, duration):
    """All text seen in frames sampled every OCR_SAMPLE_EVERY_S, lowercased. Needs tesseract."""
    seen = []
    with tempfile.TemporaryDirectory() as tmp:
        run(["ffmpeg", "-v", "error", "-i", str(video), "-vf", f"fps={1 / OCR_SAMPLE_EVERY_S},negate", f"{tmp}/f%04d.png"])
        for n, png in enumerate(sorted(Path(tmp).glob("f*.png"))):
            out = run(["tesseract", str(png), "-", "--psm", "11"], text=True).stdout
            seen.append((n * OCR_SAMPLE_EVERY_S, " ".join(out.split()).lower()))
    return seen


def norm_text(s):
    return re.sub(r"[^a-z0-9%]+", " ", s.lower()).strip()


class Report:
    def __init__(self, rules, index):
        self.rules, self.index, self.findings, self.passed = rules, index, [], []

    def provenance(self, rule_id):
        out = []
        for ref in self.rules[rule_id].get("provenance", []):
            rec = self.index.get(ref["record"])
            quote = None
            if rec:
                quote = next((c["quote"] for c in rec.get("claims", []) if ref.get("match", "\0") in c["quote"]), None)
            out.append({"record": ref["record"], "quote": quote, "note": ref.get("note"),
                        "resolved": bool(quote) or ref["record"].startswith("example:")})
        return out

    def add(self, rule_id, message, where=None, measured=None):
        r = self.rules[rule_id]
        self.findings.append({"rule": rule_id, "severity": r["severity"], "title": r["title"], "message": message,
                              "where": where or [], "measured": measured, "hint": r["hint"],
                              "provenance": self.provenance(rule_id)})

    def ok(self, rule_id, measured=None):
        self.passed.append({"rule": rule_id, "title": self.rules[rule_id]["title"], "measured": measured})


SOURCE_SUFFIXES = (".html", ".htm", ".tsx", ".jsx", ".ts", ".js", ".mjs", ".py", ".json", ".md", ".svg", ".vue", ".css")
SOURCE_SKIP_DIRS = ("node_modules", ".git", "out", "dist", "build", ".next", "__pycache__")


def source_text(root):
    """All authored text under a project folder, tags stripped, whitespace collapsed."""
    parts = []
    for path in sorted(Path(root).rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SOURCE_SUFFIXES:
            continue
        if any(part in SOURCE_SKIP_DIRS for part in path.parts) or path.name in ("contract.json", "clipcheck.json"):
            continue
        try:
            raw = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        parts.append(raw)
        parts.append(re.sub(r"<[^>]+>", " ", raw))
    return " ".join(" ".join(parts).split())


def check(video, contract, captions=None, index_path=None, use_ocr=False, source=None):
    rules = {r["id"]: r for r in json.loads((HERE / "rules.json").read_text(encoding="utf-8"))["rules"]}
    index = {}
    if index_path and Path(index_path).exists():
        index = {json.loads(l)["id"]: json.loads(l) for l in Path(index_path).read_text(encoding="utf-8").splitlines() if l}
    rep = Report(rules, index)
    info = probe(video)
    if not info:
        rep.add("stream", "no readable video stream")
        return rep, None
    fps = info["fps"]

    want = contract.get("stream", {})
    bad = []
    if want.get("size") and [info["width"], info["height"]] != want["size"]:
        bad.append(f"size {info['width']}x{info['height']}, contract {want['size'][0]}x{want['size'][1]}")
    if want.get("fps") and abs(fps - want["fps"]) > 0.01:
        bad.append(f"fps {fps:g}, contract {want['fps']}")
    if want.get("duration_s") and abs(info["duration"] - want["duration_s"]) > want.get("duration_tolerance_s", 0.5):
        bad.append(f"duration {info['duration']:.2f} s, contract {want['duration_s']} s")
    if want.get("codec") and info["codec"] != want["codec"]:
        bad.append(f"codec {info['codec']}, contract {want['codec']}")
    rep.add("stream", "; ".join(bad)) if bad else rep.ok("stream", f"{info['width']}x{info['height']} {fps:g} fps {info['duration']:.2f} s {info['codec']}")

    tags = (info["color_space"], info["color_primaries"], info["color_transfer"])
    if any(t in (None, "unknown") for t in tags):
        rep.add("colour-tags", f"colour tags are incomplete (space {tags[0]}, primaries {tags[1]}, transfer {tags[2]})",
                measured=dict(zip(("space", "primaries", "transfer"), tags)))
    else:
        rep.ok("colour-tags", "/".join(tags))

    pal = contract.get("palette") or {}
    background = hex_rgb(pal["background"]) if pal.get("background") else estimate_background(video)
    allowed = [hex_rgb(h) for h in pal.get("allowed", [])] if pal.get("allowed") else None
    rows, off_colours = analyse(video, background, allowed, pal.get("tolerance", 30))
    n = len(rows)
    covs = sorted(r["presence"] for r in rows)
    typical = covs[n // 2] if n else 0

    first_empty = next((i for i, r in enumerate(rows) if r["presence"] >= EMPTY_COVERAGE), n)
    if first_empty > 0:
        rep.add("first-frame", f"the first {first_empty} frame(s) show only the background",
                where=[{"start_s": 0.0, "end_s": round(first_empty / fps, 3)}], measured={"frames": first_empty})
    else:
        rep.ok("first-frame", f"presence {rows[0]['presence']:.3f}")

    contents = sorted(r["content"] for r in rows)
    typical_content = contents[n // 2] if n else 0
    mid = lambda s: s["first_frame"] > 0 and s["end_s"] < info["duration"] - 0.05
    gaps = [s for s in spans([r["content"] < EMPTY_COVERAGE for r in rows], fps) if mid(s)]
    if gaps:
        rep.add("empty-frames", f"{len(gaps)} stretch(es) mid-clip with no scene content on screen"
                + (" (only fixed elements remain)" if rows[0].get("chrome_share") else "")
                + f"; a frame counts as empty under {EMPTY_COVERAGE:.2%} of pixels lit, this clip usually has {typical_content:.2%}",
                where=gaps,
                measured={"frames": sum(g["frames"] for g in gaps), "chrome_share": round(rows[0].get("chrome_share", 0), 4)})
    else:
        rep.ok("empty-frames", f"lowest mid-clip content {min((r['content'] for r in rows[first_empty:]), default=0):.4f}")
    limit = typical_content * SPARSE_FACTOR
    thin = [s for s in spans([EMPTY_COVERAGE <= r["content"] < limit for r in rows], fps, SPARSE_MIN_FRAMES) if mid(s)]
    if thin:
        rep.add("sparse-frames", f"{len(thin)} stretch(es) where the frame holds under {SPARSE_FACTOR:.0%} of the usual content",
                where=thin, measured={"frames": sum(t["frames"] for t in thin), "typical": round(typical_content, 4)})
    else:
        rep.ok("sparse-frames", f"typical content {typical_content:.4f}")

    if allowed is not None:
        max_share = pal.get("max_offpalette_share", 0.002)
        offs = [s for s in spans([r["off"] > max_share for r in rows], fps, 3)]
        if offs:
            top = sorted(off_colours.items(), key=lambda kv: -kv[1])[:4]
            rep.add("palette", f"colours outside the contract palette in {sum(s['frames'] for s in offs)} frames; "
                    "most common: " + ", ".join("#%02X%02X%02X" % c for c, _ in top), where=offs[:8],
                    measured={"peak_share": round(max(r["off"] for r in rows), 4),
                              "colours": ["#%02X%02X%02X" % c for c, _ in top]})
        else:
            rep.ok("palette", f"peak off-palette share {max((r['off'] for r in rows), default=0):.4f}")

    safe = contract.get("safe_area")
    if safe:
        out_of = []
        for i, r in enumerate(rows):
            b = r["box"]
            # Full-bleed moments (a wipe, a flood) are transitions, not layout: skip frames mostly covered.
            if not b or r["coverage"] > 0.5:
                out_of.append(False)
                continue
            out_of.append(b[0] < safe["left"] - 1e-9 or b[1] < safe["top"] - 1e-9 or
                          b[2] > 1 - safe["right"] + 1e-9 or b[3] > 1 - safe["bottom"] + 1e-9)
        held = [s for s in spans(out_of, fps, int(fps * 0.5))]
        if held:
            rep.add("safe-area", f"content sits outside the safe area for {sum(s['frames'] for s in held) / fps:.1f} s in total",
                    where=held[:8])
        else:
            rep.ok("safe-area", f"margins L{safe['left']} T{safe['top']} R{safe['right']} B{safe['bottom']} held")

    bs = bursts(rows, fps)
    scenes = contract.get("scenes") or []
    cuts = [s["start_s"] for s in scenes[1:]]
    tol = contract.get("cut_tolerance_s", 0.35)
    if cuts:
        missed = [c for c in cuts if not any(b["start_s"] - tol <= c <= b["end_s"] + tol for b in bs)]
        if missed:
            rep.add("scene-times", f"no move of {MIN_BURST_FRAMES}+ frames overlaps the window of +/- {tol:g} s around contract scene change(s): "
                    + ", ".join(f"{c:g} s" for c in missed),
                    where=[{"start_s": c, "end_s": c} for c in missed])
        else:
            rep.ok("scene-times", f"{len(cuts)} scene changes fall on motion")

    moves = [b for b in bs if b["frames"] >= 6]
    if moves:
        dead = [b for b in moves if b["tail_ratio"] > ABRUPT_TAIL_RATIO]
        share = len(dead) / len(moves)
        if share > contract.get("motion", {}).get("max_abrupt_stop_share", 0.34):
            rep.add("abrupt-stops", f"{len(dead)} of {len(moves)} moves end at more than {ABRUPT_TAIL_RATIO:.0%} of their peak speed",
                    where=[{"start_s": b["start_s"], "end_s": b["end_s"]} for b in dead[:8]],
                    measured={"share": round(share, 3)})
        else:
            rep.ok("abrupt-stops", f"{len(dead)} of {len(moves)} moves stop dead")

    hold = contract.get("motion", {}).get("max_still_s")
    if hold:
        still = [s for s in spans([r["motion"] <= STILL_FLOOR for r in rows], fps) if s["frames"] / fps > hold]
        if still:
            rep.add("long-hold", f"{len(still)} hold(s) longer than {hold:g} s with no change on screen "
                    f"(per-frame change under {STILL_FLOOR})", where=still)
        else:
            rep.ok("long-hold", f"no hold over {hold:g} s")

    audio = contract.get("audio") or {}
    if audio.get("required") and not info["has_audio"]:
        rep.add("loudness", "the contract requires audio and the file has no audio stream")
    elif info["has_audio"] and audio.get("integrated_lufs"):
        lufs, peak = loudness(video)
        lo, hi = audio["integrated_lufs"]
        msgs = []
        if lufs is None or not lo <= lufs <= hi:
            msgs.append(f"integrated loudness {lufs} LUFS, contract {lo} to {hi}")
        if peak is not None and peak > audio.get("true_peak_dbtp", -1.0):
            msgs.append(f"true peak {peak} dBTP, contract at most {audio.get('true_peak_dbtp', -1.0)}")
        rep.add("loudness", "; ".join(msgs), measured={"lufs": lufs, "peak": peak}) if msgs else rep.ok("loudness", f"{lufs} LUFS, peak {peak} dBTP")

    if captions:
        lim = contract.get("captions", {})
        bad = []
        for c in parse_captions(captions):
            text = " ".join(c["lines"])
            dur = max(c["end"] - c["start"], 0.001)
            if len(c["lines"]) > lim.get("max_lines", 2):
                bad.append((c, f"{len(c['lines'])} lines"))
            elif max((len(x) for x in c["lines"]), default=0) > lim.get("max_chars_per_line", 42):
                bad.append((c, f"{max(len(x) for x in c['lines'])} characters in a line"))
            elif len(text) / dur > lim.get("max_chars_per_second", 20):
                bad.append((c, f"{len(text) / dur:.1f} characters per second"))
            else:
                # Shortest readable cue: a floor in seconds, or a per-word allowance, whichever is longer.
                need = max(lim.get("min_duration_s", 0), lim.get("min_seconds_per_word", 0) * len(text.split()))
                if dur + 1e-6 < need:
                    bad.append((c, f"on screen {dur:.2f} s, needs {need:.2f} s"))
        if bad:
            rep.add("captions", f"{len(bad)} caption cue(s) over the limits; first: {bad[0][1]}",
                    where=[{"start_s": c["start"], "end_s": c["end"]} for c, _ in bad[:8]])
        else:
            rep.ok("captions", "all cues within limits")

    copy = contract.get("copy") or []
    if copy and source:
        # Exact copy is checked where text is exact: in the project source, not in pixels.
        text = source_text(source)
        absent = [c for c in copy if " ".join(c.split()) not in text]
        if absent:
            rep.add("copy-source", f"{len(absent)} of {len(copy)} contract strings are not in the project source: "
                    + "; ".join(repr(m) for m in absent[:5]), measured={"missing": absent})
        else:
            rep.ok("copy-source", f"{len(copy)} strings found in the source")
    if copy and use_ocr and shutil.which("tesseract"):
        timed = [(t, norm_text(x)) for t, x in ocr_text(video, info["duration"])]
        seen = [x for _, x in timed]
        missing = [c for c in copy if not any(norm_text(c) in t for t in seen)]
        if missing:
            rep.add("copy", f"{len(missing)} of {len(copy)} contract strings were not read in any sampled frame "
                    "(text reading misses small or coloured text; confirm by eye): " +
                    "; ".join(repr(m) for m in missing[:5]), measured={"missing": missing})
        else:
            rep.ok("copy", f"{len(copy)} strings read by OCR")
        numbers = contract.get("numbers_allowed")
        if numbers is not None:
            allowed_n = set(map(str, numbers))
            hits = [(t, m) for t, x in timed for m in re.findall(r"\b\d{2,}\b", x) if m not in allowed_n]
            found = sorted({m for _, m in hits})
            if found:
                rep.add("stray-numbers", "numbers on screen that the contract does not list: " + ", ".join(found[:12])
                        + f" (text is read every {OCR_SAMPLE_EVERY_S:g} s, so other values may pass unseen)",
                        where=[{"start_s": t, "end_s": t} for t, _ in hits[:8]], measured={"numbers": found})
            else:
                rep.ok("stray-numbers", "only contract numbers were read")

    series = {"fps": fps, "coverage": [round(r["coverage"], 4) for r in rows], "content": [round(r["content"], 4) for r in rows], "motion": [round(r["motion"], 5) for r in rows],
              "off_palette": [round(r["off"], 4) for r in rows], "bursts": bs}
    return rep, {"stream": info, "background": "#%02X%02X%02X" % background, "series": series}


def main():
    ap = argparse.ArgumentParser(description="Check a rendered clip against a contract.")
    ap.add_argument("video")
    ap.add_argument("--contract", required=True)
    ap.add_argument("--source", help="project folder; contract copy must appear in its source files")
    ap.add_argument("--captions")
    ap.add_argument("--json")
    ap.add_argument("--index", default=str(HERE.parent.parent / "index" / "records.jsonl"))
    ap.add_argument("--ocr", action="store_true", help="read on-screen text with tesseract to check copy")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()
    if not (shutil.which("ffmpeg") and shutil.which("ffprobe")):
        print("clipcheck needs ffmpeg and ffprobe on PATH", file=sys.stderr)
        return 2
    contract = json.loads(Path(a.contract).read_text(encoding="utf-8"))
    rep, data = check(a.video, contract, a.captions, a.index, a.ocr, a.source)
    errors = [f for f in rep.findings if f["severity"] == "error"]
    result = {"video": Path(a.video).name, "contract": Path(a.contract).name,
              "verdict": "fail" if errors else "pass", "errors": len(errors),
              "warnings": len(rep.findings) - len(errors), "findings": rep.findings, "passed": rep.passed,
              **({"stream": data["stream"], "background": data["background"], "series": data["series"]} if data else {})}
    if a.json:
        Path(a.json).write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    if not a.quiet:
        for f in rep.findings:
            where = ", ".join(f"{w['start_s']:g}-{w['end_s']:g} s" for w in f["where"][:4])
            print(f"{f['severity'].upper():7} {f['rule']}: {f['message']}" + (f"  [{where}]" if where else ""))
            print(f"        fix: {f['hint']}")
            for p in f["provenance"]:
                if p["quote"]:
                    print(f"        why: {p['record']} - \"{p['quote'][:140]}\"")
                elif p.get("note"):
                    print(f"        why: {p['record']} - {p['note']}")
        for p in rep.passed:
            print(f"ok      {p['rule']}: {p['measured']}")
        print(f"CLIPCHECK: {result['verdict'].upper()} ({result['errors']} errors, {result['warnings']} warnings)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
