#!/usr/bin/env python3
"""Static checks on site/: origins, images, contrast, byte budgets, landmarks, targets, data. Stdlib only.

  python3 site/tests/test_site.py      prints the contrast table and page sizes, then runs the checks
"""
import hashlib
import html
import json
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
ROOT = SITE.parent
PAGES = ("index.html", "search.html", "record.html", "lab.html")
TOKENS = SITE / "tokens.css"
STYLES = (SITE / "style.css", SITE / "home.css")
FONTS = SITE / "fonts"
# First-load bytes per page: the HTML, its stylesheets, its scripts and every module they import
# (search_worker.js included: the search box starts it on first focus). Fonts are budgeted below.
PAGE_BUDGET_BYTES = {"index.html": 110_000, "search.html": 70_000, "record.html": 70_000, "lab.html": 62_000}
FONT_BUDGET_BYTES = 520_000
TEXT_MIN = 4.5
UI_MIN = 3.0
TARGET_MIN_PX = 24
PHONE_TARGET_PX = 44
ROOT_FONT_PX = 16
NARROW_VIEWPORT_PX = 320
PAGE_GUTTER_PX = 32  # 16 px on both sides at the narrowest width

# Foreground on background, as the pages use them. Hairline is for rules only (Foundations board).
TEXT_PAIRS = [("ink", "paper"), ("graphite", "paper"), ("signal", "paper"), ("amber", "paper"),
              ("ink", "mark"), ("paper", "ink"), ("specimen-ink", "specimen"), ("specimen-text", "specimen"),
              ("signal-bright", "specimen"), ("amber-bright", "specimen"), ("on-flag", "amber-bright")]
UI_PAIRS = [("ink", "paper"), ("graphite", "paper"), ("signal", "paper"), ("amber", "paper"),
            ("specimen-ink", "specimen"), ("specimen-text", "specimen"), ("amber-bright", "specimen"),
            ("signal-bright", "specimen")]

ABSOLUTE = re.compile(r"^\s*(?:[a-z][a-z0-9+.-]*:|//)", re.I)
ALLOWED_SCHEMES = ("data:",)
SVG_NAMESPACE = "http://www.w3.org/2000/svg"  # an identifier, never fetched
REPORT = ROOT / "examples/clipcheck-fix-loop/results/clipcheck-before.json"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.labels = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "input" and self.labels:
            a["in-label"] = "yes"
        self.labels += tag == "label"
        self.tags.append((tag, a))

    def handle_endtag(self, tag):
        self.labels -= tag == "label" and self.labels > 0

    def find(self, tag=None, **want):
        return [a for t, a in self.tags if (tag is None or t == tag)
                and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in want.items())]


def parse(name):
    p = Page()
    p.feed((SITE / name).read_text(encoding="utf-8"))
    return p


def read(path):
    return path.read_text(encoding="utf-8")


def block(css, selector):
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\}", css, re.S)
    return m.group(1) if m else ""


def declarations(text):
    return dict(re.findall(r"--([a-z0-9-]+)\s*:\s*([^;]+);", text))


def colour_tokens():
    """{name: (light hex, dark hex)}: light from :root, dark = light overridden by [data-theme="dark"]."""
    css = read(TOKENS)
    light = {k[2:]: v.strip() for k, v in declarations(block(css, ":root")).items() if k.startswith("c-")}
    dark_over = {k[2:]: v.strip() for k, v in declarations(block(css, ':root[data-theme="dark"]')).items()}
    return {k: (v, dark_over.get(k, v)) for k, v in light.items()}


def other_tokens():
    return {k: v.strip() for k, v in declarations(block(read(TOKENS), ":root")).items() if not k.startswith("c-")}


def luminance(hexcolour):
    out = []
    for i in (1, 3, 5):
        c = int(hexcolour[i:i + 2], 16) / 255
        out.append(c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def contrast_table():
    colours = colour_tokens()
    rows = []
    for kind, pairs, need in (("text", TEXT_PAIRS, TEXT_MIN), ("ui", UI_PAIRS, UI_MIN)):
        for fg, bg in pairs:
            rows.append((kind, fg, bg, need, contrast(colours[fg][0], colours[bg][0]), contrast(colours[fg][1], colours[bg][1])))
    return rows


def local_imports(path, seen):
    if path in seen or not path.is_file():
        return
    seen.add(path)
    src = read(path)
    refs = re.findall(r"""(?:import\s[^"']*?from\s*|import\s*\(\s*|import\s+|new URL\(\s*)["'](\.{1,2}/[^"']+\.js)["']""", src)
    for ref in refs:
        local_imports((path.parent / ref).resolve(), seen)


def page_bytes(name):
    files = {SITE / name}
    p = parse(name)
    for a in p.find("link", rel="stylesheet"):
        files.add((SITE / a["href"]).resolve())
    mods = set()
    for a in p.find("script"):
        if a.get("src"):
            f = (SITE / a["src"]).resolve()
            files.add(f)
            local_imports(f, mods)
    files |= mods
    return sum(f.stat().st_size for f in files), sorted(f.name for f in files)


def site_files(*exts):
    return [f for f in SITE.rglob("*") if f.suffix in exts and "tests" not in f.relative_to(SITE).parts]


def px(value, other):
    value = value.strip()
    m = re.fullmatch(r"var\(--([a-z0-9-]+)\)", value)
    if m:
        value = other[m.group(1)]
    m = re.fullmatch(r"([0-9.]+)(px|rem)", value)
    if not m:
        raise ValueError(value)
    return float(m.group(1)) * (ROOT_FONT_PX if m.group(2) == "rem" else 1)


def time_text(w):
    s, e = w["start_s"], w["end_s"]
    if e > s:
        return f"{s:.3f}-{e:.3f} s"
    return f"{s:.1f} s" if float(s).is_integer() else f"{s} s"


def expected_marks(report):
    """Same numbering as home.js: E1..En over error ranges, W1..Wn over the rest."""
    out, count = [], {"E": 0, "W": 0}
    for f in report["findings"]:
        p = "E" if f["severity"] == "error" else "W"
        for w in f["where"]:
            count[p] += 1
            out.append((p + str(count[p]), time_text(w), f))
    return out


class Origins(unittest.TestCase):
    def test_no_third_party_src_or_href(self):
        for name in PAGES:
            for tag, attrs in parse(name).tags:
                for key in ("src", "href", "action", "cite"):
                    v = attrs.get(key)
                    if v and ABSOLUTE.match(v):
                        self.assertTrue(v.startswith(ALLOWED_SCHEMES), f"{name}: <{tag} {key}={v}>")

    def test_no_third_party_in_css(self):
        for f in site_files(".css"):
            css = read(f)
            refs = re.findall(r"@import\s+(?:url\()?\s*['\"]?([^'\")\s;]+)", css) + re.findall(r"url\(\s*['\"]?([^'\")]+)", css)
            for ref in refs:
                self.assertFalse(ABSOLUTE.match(ref) and not ref.startswith(ALLOWED_SCHEMES), f"{f.name}: {ref}")

    def test_no_absolute_urls_in_site_code(self):
        for f in site_files(".js", ".html", ".css"):
            code = read(f).replace(SVG_NAMESPACE, "")
            self.assertIsNone(re.search(r"https?://", code), f.name)


class Fonts(unittest.TestCase):
    def test_font_faces_are_local_files_with_swap(self):
        css = read(TOKENS)
        faces = re.findall(r"@font-face\s*\{(.*?)\}", css, re.S)
        self.assertGreaterEqual(len(faces), 4)
        for face in faces:
            self.assertIn("font-display: swap", face)
            for ref in re.findall(r"url\(\s*['\"]?([^'\")]+)", face):
                self.assertTrue((SITE / ref).is_file(), ref)

    def test_fonts_under_budget_licensed_and_listed(self):
        files = sorted(FONTS.glob("*.woff2"))
        self.assertTrue(files)
        self.assertLessEqual(sum(f.stat().st_size for f in files), FONT_BUDGET_BYTES)
        third = read(ROOT / "THIRD_PARTY.md")
        for f in files:
            digest = hashlib.sha256(f.read_bytes()).hexdigest()
            self.assertIn(f"site/fonts/{f.name}` | `{digest}`", third, f"{f.name}: sha256 not listed in THIRD_PARTY.md")
            family = f.name.split("-")[0]
            self.assertTrue((FONTS / "LICENSES" / f"{family}-OFL.txt").is_file(), f.name)
        self.assertIn("site/fonts/LICENSES", read(ROOT / "LICENSES/README.md"))


class Images(unittest.TestCase):
    def test_every_served_image_has_size_and_alt(self):
        for name in PAGES:
            for a in parse(name).find("img"):
                self.assertTrue(a.get("width") and a.get("height") and a.get("alt"), f"{name}: {a}")
                self.assertTrue((SITE / a["src"]).is_file(), f"{name}: {a['src']}")

    def test_script_made_images_have_size_alt_and_lazy(self):
        for f in site_files(".js"):
            for call in re.findall(r'el\("img",\s*\{(.*?)\}\)', read(f), re.S):
                for key in ("width", "height", "alt", "loading"):
                    self.assertRegex(call, rf"\b{key}\s*:", f"{f.name}: img without {key}")

    def test_frames_readme(self):
        readme = read(SITE / "assets/frames/README.md")
        self.assertIn("examples/clipcheck-fix-loop/results/before.mp4", readme)
        self.assertIn("ffmpeg ", readme)
        for img in (SITE / "assets/frames").glob("*.jpg"):
            self.assertIn(img.name, readme)


class Contrast(unittest.TestCase):
    def test_every_colour_token_is_hex(self):
        colours = colour_tokens()
        self.assertTrue(colours)
        for name, (light, dark) in colours.items():
            for v in (light, dark):
                self.assertRegex(v, r"^#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?$", f"--c-{name}")

    def test_dark_mapping_is_the_same_for_system_and_toggle(self):
        css = read(TOKENS)
        system = declarations(block(css, ':root:not([data-theme="light"])'))
        toggle = declarations(block(css, ':root[data-theme="dark"]'))
        self.assertTrue(toggle)
        self.assertEqual(system, toggle)
        self.assertIn("@media (prefers-color-scheme: dark)", css)

    def test_colours_live_only_in_tokens(self):
        for f in site_files(".css"):
            if f == TOKENS:
                continue
            text = re.sub(r"/\*.*?\*/", "", read(f), flags=re.S)
            self.assertIsNone(re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(", text), f.name)

    def test_pairs_meet_wcag_in_both_themes(self):
        for kind, fg, bg, need, light, dark in contrast_table():
            self.assertGreaterEqual(light, need, f"light {kind} {fg} on {bg}: {light:.2f}")
            self.assertGreaterEqual(dark, need, f"dark {kind} {fg} on {bg}: {dark:.2f}")


class Budgets(unittest.TestCase):
    def test_page_bytes_under_budget(self):
        for name in PAGES:
            size, files = page_bytes(name)
            self.assertLessEqual(size, PAGE_BUDGET_BYTES[name], f"{name}: {size} bytes over {files}")


class Landmarks(unittest.TestCase):
    def test_required_landmarks(self):
        for name in PAGES:
            p = parse(name)
            self.assertTrue(p.find("html") and p.find("html")[0].get("lang"), name)
            self.assertTrue(p.find("meta", name="viewport"), name)
            self.assertEqual(len(p.find("h1")), 1, f"{name}: one h1")
            self.assertEqual(len(p.find("main", id="main")), 1, name)
            self.assertEqual(len(p.find("main")), 1, name)
            self.assertEqual(len([a for t, a in p.tags if t == "header" and "data-chrome" in a]), 1, f"{name}: shared header")
            self.assertEqual(len([a for t, a in p.tags if t == "footer" and "data-chrome" in a]), 1, f"{name}: shared footer")
            self.assertTrue(p.find("script", src="chrome.js"), name)
            self.assertTrue(p.find("script", src="theme.js"), name)
            self.assertTrue(p.find("link", rel="stylesheet", href="tokens.css"), name)
            self.assertTrue(p.find("a", href="#main"), f"{name}: skip link")
            self.assertTrue(p.find("link", rel="describedby", href="../llms.txt"), name)

    def test_chrome_has_nav_toggle_and_only_existing_destinations(self):
        js = read(SITE / "chrome.js")
        self.assertIn('aria-label="Site"', js)
        self.assertIn('id="theme-toggle"', js)
        nav = re.search(r"var NAV = (\[.*?\]);", js).group(1)
        for href in re.findall(r'\["([^"]+)"', nav):
            self.assertTrue((SITE / href).resolve().is_file(), href)
        for href in re.findall(r'href="(\.\./[^"]+)"', js):
            self.assertTrue((SITE / href).resolve().is_file(), href)

    def test_inputs_are_labelled(self):
        for name in PAGES:
            p = parse(name)
            labels = {a.get("for") for a in p.find("label")}
            for a in p.find("input"):
                if a.get("type") == "hidden":
                    continue
                self.assertTrue(a.get("in-label") or a.get("id") in labels, f"{name}: input {a}")

    def test_search_box_is_a_labelled_combobox(self):
        for name in ("index.html", "search.html", "record.html"):
            p = parse(name)
            box = p.find("input", id="q")
            self.assertEqual(len(box), 1, name)
            box = box[0]
            self.assertEqual(box.get("role"), "combobox", name)
            self.assertEqual(box.get("aria-expanded"), "false", name)
            self.assertTrue(p.find("ul", id=box["aria-controls"], role="listbox"), name)
            self.assertTrue(p.find("form", role="search", action="search.html"), name)
            self.assertTrue(p.find(id="q-status", role="status"), name)

    def test_search_page_has_loading_state_and_live_region(self):
        p = parse("search.html")
        self.assertTrue(p.find("p", id="state", role="status"))
        self.assertIn("Loading the index...", read(SITE / "search.html"))
        self.assertNotIn("0 results", read(SITE / "search.html"))


class Home(unittest.TestCase):
    def test_findings_table_is_served_and_matches_the_report(self):
        page = read(SITE / "index.html")
        self.assertIn('<table id="findings"', page)
        body = re.search(r'<tbody id="findings-body">(.*?)</tbody>', page, re.S).group(1)
        report = json.loads(read(REPORT))
        marks = expected_marks(report)
        self.assertEqual(re.findall(r'data-mark="(\w+)"', body), [m[0] for m in marks])
        self.assertEqual([html.unescape(t) for t in re.findall(r'<span class="t">([^<]+)</span>', body)], [m[1] for m in marks])
        text = html.unescape(body)
        for f in report["findings"]:
            for key in ("rule", "title", "message", "hint"):
                self.assertIn(f[key], text, f"{f['rule']}: served {key} differs from the report")
            for p in f["provenance"]:
                self.assertIn(p["record"], text)
                if p["note"]:
                    self.assertIn(p["note"], text)
                if p["quote"]:
                    self.assertIn(re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p["quote"]), html.unescape(body))

    def test_frames_exist_for_every_finding(self):
        report = json.loads(read(REPORT))
        fps = report["stream"]["fps"]
        for f in report["findings"]:
            for w in f["where"]:
                frame = w.get("first_frame", round(w["start_s"] * fps))
                self.assertTrue((SITE / f"assets/frames/hf-d{frame:03d}.jpg").is_file(), frame)

    def test_data_files_the_home_page_reads_exist(self):
        js = read(SITE / "home.js")
        base = re.search(r'const EXAMPLE = "([^"]+)"', js).group(1)
        for rel in re.findall(r'EXAMPLE \+ "([^"]+)"', js):
            self.assertTrue((SITE / (base + rel)).resolve().is_file(), rel)
        for rel in re.findall(r'"(\.\./(?:evals|index)/[^"]+\.json)"', js):
            self.assertTrue((SITE / rel).resolve().is_file(), rel)

    def test_noscript_notice(self):
        self.assertIn("<noscript>", read(SITE / "index.html"))


class Layout(unittest.TestCase):
    def test_pointer_targets(self):
        css = read(SITE / "style.css")
        other = other_tokens()
        self.assertGreaterEqual(px("var(--target-min)", other), TARGET_MIN_PX)
        self.assertGreaterEqual(px("var(--target)", other), PHONE_TARGET_PX)
        rule = re.search(r"([^{}]*\bbutton\b[^{}]*)\{\s*min-height:\s*([^;]+);", css)
        self.assertIsNotNone(rule)
        for sel in ("button", "select", 'input[type="text"]', ".option"):
            self.assertIn(sel, rule.group(1))
        self.assertGreaterEqual(px(rule.group(2), other), PHONE_TARGET_PX)

    def test_visible_focus(self):
        css = read(SITE / "style.css")
        self.assertRegex(css, r":focus-visible\s*\{[^}]*outline:\s*var\(--focus-w\) solid var\(--c-ink\)")
        self.assertRegex(css, r'\[data-surface="specimen"\] :focus-visible\s*\{[^}]*outline-color')

    def test_reduced_motion(self):
        self.assertIn("prefers-reduced-motion: reduce", read(SITE / "style.css"))
        for f in site_files(".css", ".js"):
            self.assertNotRegex(read(f), r"@keyframes|autoplay", f.name)

    def test_nothing_wider_than_a_narrow_phone(self):
        other = other_tokens()
        room = NARROW_VIEWPORT_PX - PAGE_GUTTER_PX
        for f in STYLES:
            css = read(f)
            for v in re.findall(r"minmax\(\s*(?:min\()?\s*([0-9.]+(?:px|rem))", css):
                self.assertLessEqual(px(v, other), room, f"{f.name}: minmax({v})")
            for prop, v in re.findall(r"(?<![a-z-])(width|min-width)\s*:\s*([0-9.]+(?:px|rem))", css):
                self.assertLessEqual(px(v, other), room, f"{f.name}: {prop}: {v}")
        self.assertIn(".table-wrap { overflow-x: auto; }", read(SITE / "style.css"))
        self.assertRegex(read(SITE / "style.css"), r"#r-facts td \{[^}]*overflow-wrap: anywhere")


class Copy(unittest.TestCase):
    def test_plain_hyphens_only(self):
        for f in site_files(".js", ".html", ".css", ".md"):
            self.assertNotRegex(read(f), "[–—→]|\\\\u201[34]", f.name)

    def test_no_placeholder_text(self):
        for f in site_files(".js", ".html"):
            self.assertNotRegex(read(f).lower(), r"lorem|ipsum|todo", f.name)

    def test_no_debug_logging(self):
        for f in site_files(".js"):
            self.assertNotRegex(read(f), r"console\.(log|debug)", f.name)


def print_contrast():
    print(f"{'kind':5} {'pair':30} {'need':>5} {'light':>6} {'dark':>6}")
    for kind, fg, bg, need, light, dark in contrast_table():
        print(f"{kind:5} {fg + ' on ' + bg:30} {need:5.1f} {light:6.2f} {dark:6.2f}")
    for name in PAGES:
        size, _ = page_bytes(name)
        print(f"bytes {name}: {size} (budget {PAGE_BUDGET_BYTES[name]})")
    fonts = sum(f.stat().st_size for f in FONTS.glob("*.woff2"))
    print(f"bytes fonts: {fonts} (budget {FONT_BUDGET_BYTES})")


if __name__ == "__main__":
    print_contrast()
    unittest.main(argv=[sys.argv[0]] + sys.argv[1:])
