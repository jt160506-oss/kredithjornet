/* ============================================================
   Kredithjørnet — navigation
   Header og footer står nu direkte i hver HTML-side (indsat af
   tools/opdater-header-footer.sh), så de vises med det samme.
   Denne fil markerer kun den aktive side og styrer mobilmenuen.
   ============================================================ */
(function () {
  "use strict";

  function normalize(path) {
    if (!path) return "/";
    path = path.replace(/index\.html$/, "");
    if (!path.endsWith("/")) path += "/";
    return path;
  }

  var current = normalize(window.location.pathname);

  function markActive(root) {
    if (!root) return;
    root.querySelectorAll("a[href]").forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href || href.charAt(0) !== "/") return; // kun interne stier
      if (normalize(href.split("#")[0]) !== current) return;

      a.classList.add("active");
      var drop = a.closest(".nav-drop");
      if (drop) {
        var top = drop.querySelector(":scope > a");
        if (top) top.classList.add("active");
      }
    });

    // Forside: fremhæv intet menupunkt (kun brandet fører hjem)
    if (current === "/") return;

    // Dybe sider uden eget menupunkt: fremhæv den nærmeste dropdown
    if (root.querySelector(".nav-pill a.active")) return;
    var best = null, bestLen = 0;
    root.querySelectorAll(".nav-drop > a[href]").forEach(function (top) {
      var base = normalize(top.getAttribute("href").split("#")[0]);
      if (base !== "/" && current.indexOf(base) === 0 && base.length > bestLen) {
        best = top; bestLen = base.length;
      }
    });
    if (best) best.classList.add("active");
  }

  function initMobileToggle(root) {
    root.querySelectorAll(".menu-toggle").forEach(function (toggle) {
      var menu = document.getElementById(toggle.getAttribute("aria-controls"));
      if (!menu) return;

      function setOpen(open) {
        toggle.setAttribute("aria-expanded", open ? "true" : "false");
        document.body.classList.toggle("menu-open", open);
      }

      toggle.addEventListener("click", function () {
        setOpen(toggle.getAttribute("aria-expanded") !== "true");
      });
      menu.querySelectorAll("a").forEach(function (link) {
        link.addEventListener("click", function () { setOpen(false); });
      });
      document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") setOpen(false);
      });
    });
  }

  function boot() {
    var header = document.getElementById("site-header");
    if (!header) return;
    markActive(header);
    initMobileToggle(header);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
