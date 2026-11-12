// One header and one footer for every page, written into <header data-chrome> and <footer data-chrome>.
// Owns the theme toggle. Classic deferred script: it runs before the page's module script.
(function () {
  "use strict";
  var NAV = [["search.html", "Answers"], ["lab.html", "Lab"], ["../llms.txt", "llms.txt"]];
  var THEMES = ["auto", "light", "dark"];
  var THEME_KEY = "aml-theme";
  var META_URL = "../index/meta.json";
  var CONFIG_URL = "../hub.config.json";
  var NAME = "Agentic Media Lab";
  var SQUARE = '<svg width="8" height="8" viewBox="0 0 8 8" aria-hidden="true" focusable="false"><rect width="8" height="8" fill="currentColor"/></svg>';

  var here = location.pathname.split("/").pop() || "index.html";

  function navItem(item) {
    var cur = item[0] === here ? ' aria-current="page"' : "";
    var site = item[0].indexOf("../") === 0 ? "" : " data-site-link";
    return '<li><a href="' + item[0] + '"' + site + cur + ">" + item[1] + "</a></li>";
  }

  function living(id) {
    return '<p class="living" id="' + id + '">' + SQUARE + '<span data-living>checking the last build date...</span></p>';
  }

  var header = document.querySelector("header[data-chrome]");
  if (header) {
    header.className = "site-header";
    header.innerHTML = '<div class="wrap header-row">' +
      '<a class="brand" href="index.html" data-site-link>' + NAME + "</a>" +
      '<nav class="site-nav" aria-label="Site"><ul>' + NAV.map(navItem).join("") + "</ul></nav>" +
      '<div class="header-tools">' + living("living-head") +
      '<button id="theme-toggle" type="button">Theme: auto</button></div></div>';
  }

  var footer = document.querySelector("footer[data-chrome]");
  if (footer) {
    footer.className = "site-footer";
    footer.innerHTML = '<div class="wrap footer-row">' +
      '<p class="brand-foot">' + NAME + "</p>" +
      '<p>Code <a href="../LICENSES/Apache-2.0.txt">Apache-2.0</a>. Docs and data <a href="../LICENSES/CC-BY-4.0.txt">CC BY 4.0</a>.</p>' +
      living("living-foot") +
      '<ul><li data-repo hidden><a href="#">Repository</a></li>' +
      '<li><a href="../llms.txt">llms.txt</a></li>' +
      '<li><a href="../docs/fact-check.md">Fact-check</a></li>' +
      '<li><a href="../CONTRIBUTING.md">Contributing</a></li></ul></div>';
  }

  var root = document.documentElement;
  var btn = document.getElementById("theme-toggle");
  if (btn) {
    var show = function () { btn.textContent = "Theme: " + (root.dataset.theme || "auto"); };
    btn.addEventListener("click", function () {
      var next = THEMES[(THEMES.indexOf(root.dataset.theme || "auto") + 1) % THEMES.length];
      if (next === "auto") delete root.dataset.theme;
      else root.dataset.theme = next;
      try {
        if (next === "auto") localStorage.removeItem(THEME_KEY);
        else localStorage.setItem(THEME_KEY, next);
      } catch (e) { /* storage blocked: the choice lasts for this page only */ }
      show();
    });
    show();
  }

  function setLiving(text) {
    var spans = document.querySelectorAll("[data-living]");
    for (var i = 0; i < spans.length; i++) spans[i].textContent = text;
  }

  // ?index= points the site at another index copy (same origin, relative only), as common.js does.
  var raw = new URLSearchParams(location.search).get("index");
  var metaUrl = raw && !/^[a-z][a-z0-9+.-]*:|^\/\//i.test(raw) ? raw.replace(/\/?$/, "/") + "meta.json" : META_URL;

  fetch(metaUrl).then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (m) {
      var life = m.lifetime === "snapshot" ? "snapshot" : m.lifetime === "living" ? "living" : "status not reported";
      setLiving(life + ", last checked " + (m.built ? String(m.built).slice(0, 10) : "date not reported"));
    })
    .catch(function () { setLiving("last build date could not be loaded"); });

  fetch(CONFIG_URL).then(function (r) { return r.ok ? r.json() : null; }).then(function (c) {
    var li = document.querySelector("[data-repo]");
    if (!c || !li || !/^https:\/\//.test(c.repo_url || "")) return;
    li.firstChild.href = c.repo_url;
    li.hidden = false;
  }).catch(function () { /* no config: the repository link stays hidden */ });
})();
