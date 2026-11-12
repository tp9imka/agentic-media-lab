#!/usr/bin/env python3
"""Measure a delivered clip against the brief. Stdlib + ffmpeg/ffprobe on PATH.

usage: measure.py <arm-name> <video.mp4> [--sheet out.png] [--out result.json]
Writes results/<arm>.json next to this file (or --out) and prints PASS or FAIL with reasons.
The thresholds were fixed before any arm ran; see README.md.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

WIDTH, HEIGHT, FPS = 1920, 1080, 30.0
DURATION_S, DURATION_TOLERANCE_S = 20.0, 0.5
BLACK_MAX_S, BLACK_IGNORE_BEFORE_S = 1.0, 0.5
FREEZE_MAX_S, FREEZE_NOISE_DB = 4.0, -60
SHEET_FRAMES, SHEET_COLUMNS, SHEET_TILE_WIDTH = 12, 4, 640

HERE = Path(__file__).resolve().parent


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(video):
    out = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
               "stream=codec_name,width,height,r_frame_rate,nb_frames,pix_fmt", "-show_entries",
               "format=duration,size", "-of", "json", str(video)])
    if out.returncode != 0:
        return None
    data = json.loads(out.stdout)
    stream = (data.get("streams") or [{}])[0]
    num, _, den = (stream.get("r_frame_rate") or "0/1").partition("/")
    return {"codec": stream.get("codec_name"), "width": stream.get("width"), "height": stream.get("height"),
            "fps": round(float(num) / float(den or 1), 3), "frames": int(stream.get("nb_frames") or 0),
            "pix_fmt": stream.get("pix_fmt"), "duration_s": round(float(data["format"]["duration"]), 3),
            "bytes": int(data["format"]["size"])}


def segments(video, vf, start_key, dur_key):
    log = run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(video), "-vf", vf, "-an", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(start_key + r"[:=]\s*([0-9.]+)", log)]
    durs = [float(x) for x in re.findall(dur_key + r"[:=]\s*([0-9.]+)", log)]
    return [{"start_s": round(s, 2), "duration_s": round(d, 2)} for s, d in zip(starts, durs)]


def contact_sheet(video, out_png, duration):
    step = duration / SHEET_FRAMES
    rows = -(-SHEET_FRAMES // SHEET_COLUMNS)
    # One frame from the middle of each of SHEET_FRAMES equal slices, picked by frame number.
    picks = "+".join(f"eq(n\\,{int((i + 0.5) * step * FPS)})" for i in range(SHEET_FRAMES))
    vf = f"select='{picks}',scale={SHEET_TILE_WIDTH}:-1,tile={SHEET_COLUMNS}x{rows}"
    return run(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(video), "-vf", vf,
                "-fps_mode", "vfr", "-frames:v", "1", str(out_png)]).returncode == 0


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    arm, video = sys.argv[1], Path(sys.argv[2])
    sheet = Path(sys.argv[sys.argv.index("--sheet") + 1]) if "--sheet" in sys.argv else None
    result = {"arm": arm, "file": video.name, "thresholds": {
        "width": WIDTH, "height": HEIGHT, "fps": FPS, "duration_s": DURATION_S,
        "duration_tolerance_s": DURATION_TOLERANCE_S, "black_max_s": BLACK_MAX_S,
        "black_ignore_before_s": BLACK_IGNORE_BEFORE_S, "freeze_max_s": FREEZE_MAX_S,
        "freeze_noise_db": FREEZE_NOISE_DB}}
    reasons = []
    info = probe(video) if video.exists() else None
    if not info:
        reasons.append("no readable MP4 delivered")
    else:
        result["stream"] = info
        if (info["width"], info["height"]) != (WIDTH, HEIGHT):
            reasons.append(f"size {info['width']}x{info['height']}, wanted {WIDTH}x{HEIGHT}")
        if abs(info["fps"] - FPS) > 0.01:
            reasons.append(f"fps {info['fps']}, wanted {FPS}")
        if abs(info["duration_s"] - DURATION_S) > DURATION_TOLERANCE_S:
            reasons.append(f"duration {info['duration_s']} s, wanted {DURATION_S} +/- {DURATION_TOLERANCE_S}")
        if info["codec"] != "h264":
            reasons.append(f"codec {info['codec']}, wanted h264")
        black = segments(video, "blackdetect=d=0.1:pix_th=0.10", "black_start", "black_duration")
        freeze = segments(video, f"freezedetect=n={FREEZE_NOISE_DB}dB:d=0.5", "freeze_start", "freeze_duration")
        result["black_segments"], result["freeze_segments"] = black, freeze
        for seg in black:
            if seg["duration_s"] > BLACK_MAX_S and seg["start_s"] >= BLACK_IGNORE_BEFORE_S:
                reasons.append(f"black for {seg['duration_s']} s at {seg['start_s']} s")
        for seg in freeze:
            if seg["duration_s"] > FREEZE_MAX_S:
                reasons.append(f"frozen for {seg['duration_s']} s at {seg['start_s']} s")
        result["longest_freeze_s"] = max((s["duration_s"] for s in freeze), default=0.0)
        result["frozen_share"] = round(sum(s["duration_s"] for s in freeze) / info["duration_s"], 3)
        if sheet:
            result["contact_sheet"] = sheet.name if contact_sheet(video, sheet, info["duration_s"]) else None
    result["verdict"] = "fail" if reasons else "pass"
    result["reasons"] = reasons
    out = Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else HERE / "results" / f"{arm}.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(("FAIL" if reasons else "PASS") + f" {arm}: " + ("; ".join(reasons) or "meets the brief's stream and stillness thresholds"))
    return 1 if reasons else 0


if __name__ == "__main__":
    sys.exit(main())
