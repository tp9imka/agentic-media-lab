#!/usr/bin/env python3
"""Static checks on site/: origins, images, contrast, byte budgets, landmarks, targets. Stdlib only.

  python3 site/tests/test_site.py      prints the contrast table, then runs the checks
"""
import re
import sys
import unittest
from html.parser import HTMLParser
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
PAGES = ("index.html", "search.html", "record.html")
CSS = SITE / "style.css"
# First-load bytes per page: the HTML, style.css, theme.js and every module it imports
# (search_worker.js included: the search box starts it on first focus).
PAGE_BUDGET_BYTES = {"index.html": 55_000, "search.html": 60_000, "record.html": 60_000}
TEXT_MIN = 4.5
UI_MIN = 3.0
TARGET_MIN_PX = 24
ROOT_FONT_PX = 16
NARROW_VIEWPORT_PX = 320
PAGE_GUTTER_PX = 32  # --sp-4 on both sides

TEXT_PAIRS = [("text", "bg"), ("text", "surface"), ("muted", "bg"), ("muted", "surface"),
              ("link", "bg"), ("link", "surface"), ("measured", "bg"), ("measured", "surface"),
              ("primary", "bg"), ("primary", "surface"), ("secondary", "bg"), ("secondary", "surface"),
              ("unverified", "bg"), ("unverified", "surface"), ("text", "mark"), ("warn-text", "warn-bg"),
              ("on-button", "button")]
UI_PAIRS = [("border", "bg"), ("border", "surface"), ("focus", "bg"), ("focus", "surface"),
            ("warn-border", "warn-bg"), ("button", "bg")]

ABSOLUTE = re.compile(r"^\s*(?:[a-z][a-z0-9+.-]*:|//)", re.I)
ALLOWED_SCHEMES = ("data:",)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))

    def find(self, tag=None, **want):
        return [a for t, a in self.tags if (tag is None or t == tag)
                and all(a.get(k.rstrip("_").replace("_", "-")) == v for k, v in want.items())]


def parse(name):
    p = Page()
    p.feed((SITE / name).read_text(encoding="utf-8"))
    return p


def css_text():
    return CSS.read_text(encoding="utf-8")


def root_block(css):
    m = re.search(r":root\s*\{(.*?)\}", css, re.S)
    return m.group(1) if m else ""


def tokens(css):
    """{name: (light hex, dark hex)} for --c-* tokens, and {name: value} for the rest."""
    colours, other = {}, {}
    for name, value in re.findall(r"--([a-z0-9-]+)\s*:\s*([^;]+);", root_block(css)):
        m = re.fullmatch(r"light-dark\(\s*(#[0-9a-fA-F]{6})\s*,\s*(#[0-9a-fA-F]{6})\s*\)", value.strip())
        if name.startswith("c-"):
            colours[name[2:]] = (m.group(1), m.group(2)) if m else None
        else:
            other[name] = value.strip()
    return colours, other


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
    colours, _ = tokens(css_text())
    rows = []
    for kind, pairs, need in (("text", TEXT_PAIRS, TEXT_MIN), ("ui", UI_PAIRS, UI_MIN)):
        for fg, bg in pairs:
            light = contrast(colours[fg][0], colours[bg][0])
            dark = contrast(colours[fg][1], colours[bg][1])
            rows.append((kind, fg, bg, need, light, dark))
    return rows


def local_imports(path, seen):
    if path in seen or not path.is_file():
        return
    seen.add(path)
    src = path.read_text(encoding="utf-8")
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


class Origins(unittest.TestCase):
    def test_no_third_party_src_or_href(self):
        for name in PAGES:
            for tag, attrs in parse(name).tags:
                for key in ("src", "href", "action", "cite"):
                    v = attrs.get(key)
                    if v and ABSOLUTE.match(v):
                        self.assertTrue(v.startswith(ALLOWED_SCHEMES), f"{name}: <{tag} {key}={v}>")

    def test_no_third_party_in_css(self):
        css = css_text()
        for ref in re.findall(r"@import\s+(?:url\()?\s*['\"]?([^'\")\s;]+)", css) + \
                re.findall(r"url\(\s*['\"]?([^'\")]+)", css):
            self.assertFalse(ABSOLUTE.match(ref) and not ref.startswith(ALLOWED_SCHEMES), ref)

    def test_no_absolute_urls_in_site_code(self):
        for f in site_files(".js", ".html", ".css"):
            self.assertIsNone(re.search(r"https?://", f.read_text(encoding="utf-8")), f.name)

    def test_no_web_fonts(self):
        self.assertNotIn("@font-face", css_text())


class Images(unittest.TestCase):
    def test_every_image_has_width_and_height(self):
        for name in PAGES:
            for a in parse(name).find("img"):
                self.assertTrue(a.get("width") and a.get("height"), f"{name}: {a}")


class Contrast(unittest.TestCase):
    def test_all_colour_tokens_use_light_dark(self):
        colours, _ = tokens(css_text())
        self.assertTrue(colours)
        for name, v in colours.items():
            self.assertIsNotNone(v, f"--c-{name} is not light-dark(#hex, #hex)")

    def test_colours_live_only_in_tokens(self):
        rest = css_text().replace(root_block(css_text()), "")
        self.assertIsNone(re.search(r"#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(", re.sub(r"/\*.*?\*/", "", rest, flags=re.S)))

    def test_pairs_meet_wcag(self):
        for kind, fg, bg, need, light, dark in contrast_table():
            self.assertGreaterEqual(light, need, f"light {fg} on {bg}: {light:.2f}")
            self.assertGreaterEqual(dark, need, f"dark {fg} on {bg}: {dark:.2f}")

    def test_manual_toggle_and_system_theme(self):
        css = css_text()
        self.assertIn('[data-theme="light"] { color-scheme: light; }', css)
        self.assertIn('[data-theme="dark"] { color-scheme: dark; }', css)
        self.assertIn("color-scheme: light dark", root_block(css))


class Budgets(unittest.TestCase):
    def test_page_bytes_under_budget(self):
        for name in PAGES:
            size, files = page_bytes(name)
            self.assertLessEqual(size, PAGE_BUDGET_BYTES[name], f"{name}: {size} bytes over {files}")


class Landmarks(unittest.TestCase):
    def test_required_landmarks_and_labels(self):
        for name in PAGES:
            p = parse(name)
            self.assertTrue(p.find("html") and p.find("html")[0].get("lang"), name)
            self.assertTrue(p.find("meta", name="viewport"), name)
            self.assertEqual(len(p.find("header")), 1 + len(p.find("header", class_="record-head")), name)
            self.assertEqual(len(p.find("main", id="main")), 1, name)
            self.assertEqual(len(p.find("main")), 1, name)
            self.assertTrue(p.find("footer"), name)
            self.assertTrue(p.find("nav", aria_label="Site"), name)
            self.assertTrue(p.find("a", href="#main"), f"{name}: skip link")
            self.assertTrue(p.find("link", rel="describedby", href="../llms.txt"), name)
            self.assertTrue(p.find("link", rel="alternate", type="text/markdown"), name)
            self.assertTrue(p.find("button", id="theme-toggle"), name)
            self.assertTrue(p.find("script", src="theme.js"), name)

    def test_search_box_is_a_labelled_combobox(self):
        for name in PAGES:
            p = parse(name)
            box = p.find("input", id="q")
            self.assertEqual(len(box), 1, name)
            box = box[0]
            self.assertEqual(box.get("role"), "combobox", name)
            self.assertEqual(box.get("aria-expanded"), "false", name)
            self.assertTrue(p.find("label", **{"for": "q"}), name)
            self.assertTrue(p.find("ul", id=box["aria-controls"], role="listbox"), name)
            self.assertTrue(p.find("form", role="search"), name)
            self.assertTrue(p.find(id="q-status", role="status"), name)

    def test_search_page_has_loading_state_and_live_region(self):
        p = parse("search.html")
        self.assertTrue(p.find("p", id="state", role="status"))
        self.assertIn("Loading the index...", (SITE / "search.html").read_text())
        self.assertNotIn("0 results", (SITE / "search.html").read_text())


class Layout(unittest.TestCase):
    def test_pointer_targets(self):
        css = css_text()
        _, other = tokens(css)
        self.assertGreaterEqual(px("var(--target)", other), TARGET_MIN_PX)
        rule = re.search(r"([^{}]*\bbutton\b[^{}]*)\{\s*min-height:\s*([^;]+);", css)
        self.assertIsNotNone(rule)
        for sel in ("button", "select", 'input[type="text"]', ".option"):
            self.assertIn(sel, rule.group(1))
        self.assertGreaterEqual(px(rule.group(2), other), TARGET_MIN_PX)

    def test_visible_focus(self):
        css = css_text()
        self.assertRegex(css, r":focus-visible\s*\{[^}]*outline:\s*var\(--focus-w\) solid var\(--c-focus\)")

    def test_nothing_wider_than_a_narrow_phone(self):
        css = css_text()
        _, other = tokens(css)
        room = NARROW_VIEWPORT_PX - PAGE_GUTTER_PX
        for v in re.findall(r"minmax\(\s*([0-9.]+(?:px|rem))", css):
            self.assertLessEqual(px(v, other), room, f"minmax({v})")
        for prop, v in re.findall(r"(?<![a-z-])(width|min-width)\s*:\s*([0-9.]+(?:px|rem))", css):
            self.assertLessEqual(px(v, other), room, f"{prop}: {v}")
        self.assertIn(".table-wrap { overflow-x: auto; }", css)


class Copy(unittest.TestCase):
    def test_plain_hyphens_only(self):
        for f in site_files(".js", ".html", ".css"):
            text = f.read_text(encoding="utf-8")
            self.assertNotRegex(text, "[\u2013\u2014]|\\\\u201[34]", f.name)

    def test_no_placeholder_text(self):
        for f in site_files(".js", ".html"):
            self.assertNotRegex(f.read_text(encoding="utf-8").lower(), r"lorem|ipsum|todo", f.name)


def print_contrast():
    print(f"{'kind':5} {'pair':28} {'need':>5} {'light':>6} {'dark':>6}")
    for kind, fg, bg, need, light, dark in contrast_table():
        print(f"{kind:5} {fg + ' on ' + bg:28} {need:5.1f} {light:6.2f} {dark:6.2f}")
    for name in PAGES:
        size, _ = page_bytes(name)
        print(f"bytes {name}: {size} (budget {PAGE_BUDGET_BYTES[name]})")


if __name__ == "__main__":
    print_contrast()
    unittest.main(argv=[sys.argv[0]] + sys.argv[1:])
