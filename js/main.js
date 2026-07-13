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
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var parent = this.closest('.nav-dropdown');
      parent.classList.toggle('open');
    });
  });

  /* ── Active nav link ── */
  (function setActiveNav() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-list a').forEach(function (a) {
      const href = a.getAttribute('href');
      if (href === path) a.classList.add('active');
      else if (path === '' && href === 'index.html') a.classList.add('active');
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

  /* ── Fade in on scroll ── */
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

})();
