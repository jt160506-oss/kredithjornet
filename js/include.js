/* ============================================================
   Kredithjørnet — fælles header/footer + navigation
   Henter partials/header.html og partials/footer.html ind ét sted,
   så menu og footer kun vedligeholdes i én fil.
   ============================================================ */
(function () {
  "use strict";

  function normalize(path) {
    if (!path) return "/";
    // fjern index.html, sikr afsluttende skråstreg
    path = path.replace(/index\.html$/, "");
    if (!path.endsWith("/")) path += "/";
    return path;
  }

  var current = normalize(window.location.pathname);

  function markActive(root) {
    if (!root) return;
    var links = root.querySelectorAll("a[href]");
    links.forEach(function (a) {
      var href = a.getAttribute("href");
      if (!href || href.charAt(0) !== "/") return; // kun interne stier
      var target = normalize(href.split("#")[0]);

      // Præcist match = aktiv side
      if (target === current) {
        a.classList.add("active");
        // fremhæv også dropdown-forælderen
        var drop = a.closest(".nav-drop");
        if (drop) {
          var top = drop.querySelector(":scope > a");
          if (top) top.classList.add("active");
        }
      }
    });

    // Forside: fremhæv intet menupunkt (kun brandet fører hjem)
    if (current === "/") return;

    // Hvis ingen præcis match (fx dybe sider uden eget menupunkt),
    // fremhæv den dropdown hvis basissti matcher starten af current.
    var anyActive = root.querySelector(".nav-pill a.active");
    if (!anyActive) {
      var tops = root.querySelectorAll(".nav-drop > a[href]");
      var best = null, bestLen = 0;
      tops.forEach(function (top) {
        var base = normalize(top.getAttribute("href").split("#")[0]);
        if (base !== "/" && current.indexOf(base) === 0 && base.length > bestLen) {
          best = top; bestLen = base.length;
        }
      });
      if (best) best.classList.add("active");
    }
  }

  function initMobileToggle(root) {
    var toggles = root.querySelectorAll(".menu-toggle");
    toggles.forEach(function (toggle) {
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

  function inject(mountId, url, after) {
    var mount = document.getElementById(mountId);
    if (!mount) return Promise.resolve();
    return fetch(url)
      .then(function (r) { return r.ok ? r.text() : ""; })
      .then(function (html) {
        if (html) mount.innerHTML = html;
        if (after) after(mount);
      })
      .catch(function () { /* uden JS/fetch bevares tomt mount-punkt */ });
  }

  function boot() {
    inject("site-header", "/partials/header.html", function (mount) {
      markActive(mount);
      initMobileToggle(mount);
    });
    inject("site-footer", "/partials/footer.html");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
