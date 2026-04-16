(function () {
  var root = document.documentElement;
  var toggleBtn = document.getElementById("themeToggle");
  var toggleIcon = document.getElementById("themeToggleIcon");
  var toggleText = document.getElementById("themeToggleText");
  var storageKey = "megapartes-panel-theme";

  function resolveAutoTheme() {
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function getStoredTheme() {
    var stored = localStorage.getItem(storageKey);
    if (stored === "light" || stored === "dark") {
      return stored;
    }
    return "auto";
  }

  function updateToggleUi(activeTheme) {
    if (!toggleBtn || !toggleIcon || !toggleText) {
      return;
    }

    var effectiveTheme = activeTheme === "auto" ? resolveAutoTheme() : activeTheme;
    var willSwitchToDark = effectiveTheme === "light";

    if (willSwitchToDark) {
      toggleIcon.className = "bi bi-moon-stars";
      toggleText.textContent = "Oscuro";
      toggleBtn.setAttribute("aria-label", "Cambiar a modo oscuro");
    } else {
      toggleIcon.className = "bi bi-brightness-high";
      toggleText.textContent = "Claro";
      toggleBtn.setAttribute("aria-label", "Cambiar a modo claro");
    }
  }

  function applyTheme(theme, persist) {
    root.setAttribute("data-bs-theme", theme);

    if (persist) {
      localStorage.setItem(storageKey, theme);
    }

    updateToggleUi(theme);
  }

  var initialTheme = getStoredTheme();
  applyTheme(initialTheme, false);

  if (toggleBtn) {
    toggleBtn.addEventListener("click", function () {
      var currentTheme = root.getAttribute("data-bs-theme") || "auto";
      var effectiveTheme = currentTheme === "auto" ? resolveAutoTheme() : currentTheme;
      var nextTheme = effectiveTheme === "dark" ? "light" : "dark";
      applyTheme(nextTheme, true);
    });
  }

  var media = window.matchMedia("(prefers-color-scheme: dark)");
  media.addEventListener("change", function () {
    if ((root.getAttribute("data-bs-theme") || "auto") === "auto") {
      updateToggleUi("auto");
    }
  });

  if (window.gsap) {
    gsap.from(".reveal", {
      y: 18,
      opacity: 0,
      duration: 0.45,
      ease: "power2.out"
    });
  }
})();
