/**
 * BELACEL Madani — Site académique
 * main.js — Thème, navigation, recherche, animations
 */

(function () {
  'use strict';

  /* ── Theme Toggle ── */
  const themeToggle = document.getElementById('theme-toggle');
  const html = document.documentElement;

  function getPreferredTheme() {
    const stored = localStorage.getItem('theme');
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
    if (themeToggle) {
      themeToggle.textContent = theme === 'dark' ? '\u2600' : '\u263E';
      themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Activer le mode clair' : 'Activer le mode sombre');
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = html.getAttribute('data-theme');
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
  }
  setTheme(getPreferredTheme());

  /* ── Mobile Nav Toggle ── */
  const navToggle = document.getElementById('nav-toggle');
  const navList = document.getElementById('nav-list');
  if (navToggle && navList) {
    navToggle.addEventListener('click', function () {
      const isOpen = navList.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
      navToggle.textContent = isOpen ? '\u2715' : '\u2630';
    });
    document.addEventListener('click', function (e) {
      if (!navToggle.contains(e.target) && !navList.contains(e.target)) {
        navList.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
        navToggle.textContent = '\u2630';
        document.querySelectorAll('.nav-dropdown.open').forEach(function(d){ d.classList.remove('open'); });
      }
    });
  }

  /* ── Mobile dropdown toggle ── */
  document.querySelectorAll('.nav-dropdown-toggle').forEach(function(toggle) {
    toggle.setAttribute('role', 'button');
    toggle.setAttribute('aria-haspopup', 'true');
    // ensure aria-expanded reflects state
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      const parent = this.closest('.nav-dropdown');
      const isOpen = parent.classList.toggle('open');
      this.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

  /* ── Active nav link ── */
  (function setActiveNav() {
    function normalize(p) {
      if (!p) return 'index.html';
      // strip query + hash
      p = p.split('?')[0].split('#')[0];
      // if path ends with '/', it's index
      if (p.endsWith('/')) return 'index.html';
      // return last segment
      var parts = p.split('/');
      var last = parts.pop() || parts.pop() || 'index.html';
      return last || 'index.html';
    }

    const current = normalize(window.location.pathname);
    document.querySelectorAll('.nav-list a').forEach(function (a) {
      const href = a.getAttribute('href');
      if (normalize(href) === current) a.classList.add('active');
      else if (current === '' && normalize(href) === 'index.html') a.classList.add('active');
    });
  })();

  /* ── Search functionality ── */
  function initSearch() {
    var searchInput = document.getElementById('search-input');
    var filterModule = document.getElementById('filter-module');
    var filterType = document.getElementById('filter-type');
    var filterLang = document.getElementById('filter-lang');
    var resultsContainer = document.getElementById('search-results');

    if (!searchInput) return;

    // Build course data from DOM
    var allDocs = [];
    document.querySelectorAll('.doc-item').forEach(function (item) {
      allDocs.push({
        el: item,
        title: (item.querySelector('.doc-title') || {}).textContent || '',
        date: (item.querySelector('.doc-date') || {}).textContent || '',
        badges: Array.from(item.querySelectorAll('.badge')).map(function (b) { return b.textContent; }),
        module: item.getAttribute('data-module') || '',
        level: item.getAttribute('data-level') || ''
      });
    });

    function filterDocs() {
      var query = (searchInput.value || '').toLowerCase().trim();
      var mod = (filterModule ? filterModule.value : '');
      var typ = (filterType ? filterType.value : '');
      var lang = (filterLang ? filterLang.value : '');

      var matched = allDocs.filter(function (d) {
        if (query && d.title.toLowerCase().indexOf(query) === -1) return false;
        if (mod && d.module !== mod) return false;
        if (lang) {
          if (lang === 'fr' && d.badges.indexOf('FR') === -1 && d.badges.indexOf('Français') === -1) return false;
          if (lang === 'en' && d.badges.indexOf('EN') === -1 && d.badges.indexOf('Anglais') === -1) return false;
        }
        if (typ) {
          if (typ === 'cours' && d.badges.indexOf('Cours') === -1 && d.title.indexOf('Cours') === -1 && d.title.indexOf('Chapitre') === -1) return false;
          if (typ === 'td' && d.badges.indexOf('TD') === -1 && d.title.indexOf('TD') === -1) return false;
          if (typ === 'tp' && d.badges.indexOf('TP') === -1 && d.title.indexOf('TP') === -1) return false;
        }
        return true;
      });

      // Hide/show
      allDocs.forEach(function (d) { d.el.style.display = 'none'; });
      matched.forEach(function (d) { d.el.style.display = 'flex'; });

      // Update count
      var countEl = document.getElementById('results-count');
      if (countEl) countEl.textContent = matched.length + ' document' + (matched.length > 1 ? 's' : '');
    }

    searchInput.addEventListener('input', filterDocs);
    if (filterModule) filterModule.addEventListener('change', filterDocs);
    if (filterType) filterType.addEventListener('change', filterDocs);
    if (filterLang) filterLang.addEventListener('change', filterDocs);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initSearch);
  } else {
    initSearch();
  }

  /* ── Carousel ── */
  (function initCarousel() {
    var track = document.getElementById('carousel-track');
    if (!track) return;
    var slides = track.querySelectorAll('.carousel-slide');
    var totalSlides = slides.length;
    var dotsContainer = document.getElementById('carousel-dots');
    var prevBtn = document.querySelector('.carousel-btn-prev');
    var nextBtn = document.querySelector('.carousel-btn-next');
    var current = 0;
    var autoInterval;

    function getVisible() {
      if (window.innerWidth <= 600) return 1;
      if (window.innerWidth <= 900) return 2;
      return 3;
    }

    function goTo(index) {
      var v = getVisible();
      var max = Math.max(0, totalSlides - v);
      if (index < 0) index = max;
      if (index > max) index = 0;
      current = index;
      var pct = (100 / v) * current;
      track.style.transform = 'translateX(-' + pct + '%)';
      if (dotsContainer) {
        var dots = dotsContainer.querySelectorAll('.carousel-dot');
        var dotIndex = Math.min(current, dots.length - 1);
        dots.forEach(function(d, i) { d.classList.toggle('active', i === dotIndex); });
      }
    }

    function nextSlide() { goTo(current + 1); }
    function prevSlide() { goTo(current - 1); }

    // Dots
    if (dotsContainer) {
      var dotCount = Math.max(1, totalSlides - getVisible() + 1);
      for (var i = 0; i < dotCount; i++) {
        var dot = document.createElement('button');
        dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
        dot.setAttribute('aria-label', 'Aller au slide ' + (i + 1));
        dot.addEventListener('click', (function(idx) { return function() { goTo(idx); }; })(i));
        dotsContainer.appendChild(dot);
      }
    }

    // Buttons
    if (prevBtn) prevBtn.addEventListener('click', function() { prevSlide(); resetAuto(); });
    if (nextBtn) nextBtn.addEventListener('click', function() { nextSlide(); resetAuto(); });

    function startAuto() { autoInterval = setInterval(nextSlide, 4000); }
    function resetAuto() { clearInterval(autoInterval); startAuto(); }

    // Pause on hover
    var container = track.closest('.carousel-container');
    if (container) {
      container.addEventListener('mouseenter', function() { clearInterval(autoInterval); });
      container.addEventListener('mouseleave', function() { startAuto(); });
    }

    // Touch support
    var startX = 0;
    track.addEventListener('touchstart', function(e) { startX = e.changedTouches[0].screenX; });
    track.addEventListener('touchend', function(e) {
      var diff = startX - e.changedTouches[0].screenX;
      if (Math.abs(diff) > 40) { diff > 0 ? nextSlide() : prevSlide(); resetAuto(); }
    });

    // Resize
    window.addEventListener('resize', function() { goTo(current); });

    startAuto();
  })();

  /* ── Fade in on scroll ── */
  if (typeof IntersectionObserver !== 'undefined') {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('.module-card, .level-item, .news-item').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    // Fallback: add fade-in class to all elements immediately
    document.querySelectorAll('.module-card, .level-item, .news-item').forEach(function (el) {
      el.classList.add('fade-in');
    });
  }

})();
