// Loaded in <head> without defer so a stored theme applies before first paint.
try {
  const t = localStorage.getItem("aml-theme");
  if (t === "light" || t === "dark") document.documentElement.dataset.theme = t;
} catch (e) { /* storage blocked: follow the system theme */ }
