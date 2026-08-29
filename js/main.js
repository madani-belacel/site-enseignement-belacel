/**
 * BELACEL Madani — Site académique
 * main.js — Thème, navigation, recherche, animations
 */

(function () {
  'use strict';

  /* ── Helper: strip accents for search ── */
  function stripAccents(s) {
    return s.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  /* ── Theme Toggle ── */
  var themeToggle = document.getElementById('theme-toggle');
  var html = document.documentElement;

  function getPreferredTheme() {
    try {
      var stored = localStorage.getItem('theme');
      if (stored) return stored;
    } catch (e) {}
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function setTheme(theme) {
    html.setAttribute('data-theme', theme);
    try { localStorage.setItem('theme', theme); } catch (e) {}
    if (themeToggle) {
      themeToggle.textContent = theme === 'dark' ? '\u2600' : '\u263E';
      themeToggle.setAttribute('aria-label', theme === 'dark' ? 'Activer le mode clair' : 'Activer le mode sombre');
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      var current = html.getAttribute('data-theme');
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
  }
  setTheme(getPreferredTheme());

  /* ── Course pages: simplify course identity banner and keep the header bar compact ── */
  (function initCourseHeaderIdentity() {
    if (!window.location.pathname.includes('/cours/')) return;

    var headerInner = document.querySelector('.header-inner');
    var headerLeft = headerInner && headerInner.querySelector('.header-left');
    var logoLink = headerLeft && headerLeft.querySelector('.header-logo');
    if (!headerLeft || !logoLink) return;

    var existingPhoto = headerLeft.querySelector('.header-profile-photo');
    if (!existingPhoto) {
      var pathname = window.location.pathname;
      var parts = pathname.split('/').filter(Boolean);
      var courseIndex = parts.indexOf('cours');
      var nestedDepth = 0;

      if (courseIndex >= 0) {
        nestedDepth = parts.slice(courseIndex + 1, -1).length;
      }

      var relativePrefix = Array(nestedDepth + 2).join('../');
      var photo = document.createElement('img');
      photo.src = relativePrefix + 'images/photo-profil.png';
      photo.alt = 'Dr. BELACEL Madani';
      photo.loading = 'eager';
      photo.className = 'header-profile-photo';
      photo.setAttribute('draggable', 'false');
      headerLeft.insertBefore(photo, logoLink);
    }

    var title = logoLink.querySelector('.header-logo-text');
    if (title) {
      title.innerHTML = 'Dr. BELACEL Madani<small>MCB — Université de Mostaganem</small>';
    }

    var banner = document.querySelector('.header-banner');
    if (banner) banner.remove();
  })();

  /* ── Algerian flags in all four corners ── */
  (function addCornerFlags() {
    var existingFlags = document.querySelectorAll('.flag-corner');
    var hasCornerClasses = Array.prototype.some.call(existingFlags, function (flag) {
      return flag.classList.contains('flag-corner--tl') ||
        flag.classList.contains('flag-corner--tr') ||
        flag.classList.contains('flag-corner--bl') ||
        flag.classList.contains('flag-corner--br');
    });
    if (hasCornerClasses) return;

    var source = 'images/alg_drap.gif';
    var alt = 'Drapeau de l\'Algérie';
    var existing = existingFlags.length ? existingFlags[0] : null;

    if (existing) {
      existing.classList.add('flag-corner--tr');
      existing.setAttribute('alt', alt);
      source = existing.getAttribute('src') || source;
    }

    var corners = ['flag-corner--tl', 'flag-corner--bl', 'flag-corner--br'];
    corners.forEach(function (modifier) {
      var flag = document.createElement('img');
      flag.src = source;
      flag.alt = alt;
      flag.loading = 'lazy';
      flag.className = 'flag-corner ' + modifier;
      flag.setAttribute('aria-hidden', 'true');
      flag.setAttribute('draggable', 'false');
      document.body.appendChild(flag);
    });

    if (!existing) {
      var mainFlag = document.createElement('img');
      mainFlag.src = source;
      mainFlag.alt = alt;
      mainFlag.loading = 'eager';
      mainFlag.className = 'flag-corner flag-corner--tr';
      mainFlag.setAttribute('aria-hidden', 'true');
      mainFlag.setAttribute('draggable', 'false');
      document.body.appendChild(mainFlag);
    }
  })();

  /* ── Mobile Nav Toggle ── */
  var navToggle = document.getElementById('nav-toggle');
  var navList = document.getElementById('nav-list');
  if (navToggle && navList) {
    navToggle.addEventListener('click', function () {
      var isOpen = navList.classList.toggle('open');
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
    toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      var parent = this.closest('.nav-dropdown');
      var isOpen = parent.classList.toggle('open');
      this.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });
  });

  /* ── Active nav link ── */
  (function setActiveNav() {
    function normalize(p) {
      if (!p) return 'index.html';
      p = p.split('?')[0].split('#')[0];
      if (p.endsWith('/')) return 'index.html';
      var parts = p.split('/');
      var last = parts.pop() || parts.pop() || 'index.html';
      return last || 'index.html';
    }

    var current = normalize(window.location.pathname);
    document.querySelectorAll('.nav-list a').forEach(function (a) {
      var href = a.getAttribute('href');
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
    var countEl = document.getElementById('results-count');

    if (!searchInput) return;

    var allDocs = [];
    document.querySelectorAll('.doc-item').forEach(function (item) {
      allDocs.push({
        el: item,
        title: stripAccents((item.querySelector('.doc-title') || {}).textContent || ''),
        date: (item.querySelector('.doc-date') || {}).textContent || '',
        badges: Array.from(item.querySelectorAll('.badge')).map(function (b) { return b.textContent; }),
        module: item.getAttribute('data-module') || '',
        level: item.getAttribute('data-level') || ''
      });
    });

    var allCards = [];
    document.querySelectorAll('.module-card').forEach(function (card) {
      allCards.push({
        el: card,
        title: stripAccents((card.querySelector('h3') || {}).textContent || ''),
        desc: stripAccents((card.querySelector('p') || {}).textContent || ''),
        badges: Array.from(card.querySelectorAll('.badge')).map(function (b) { return b.textContent; })
      });
    });

    function filterDocs() {
      var query = stripAccents((searchInput.value || '').trim());
      var mod = filterModule ? filterModule.value : '';
      var typ = filterType ? filterType.value : '';
      var lang = filterLang ? filterLang.value : '';

      var matched = allDocs.filter(function (d) {
        if (query && d.title.indexOf(query) === -1) return false;
        if (mod && d.module !== mod) return false;
        if (lang) {
          if (lang === 'fr' && d.badges.indexOf('FR') === -1 && d.badges.indexOf('Français') === -1) return false;
          if (lang === 'en' && d.badges.indexOf('EN') === -1 && d.badges.indexOf('Anglais') === -1) return false;
        }
        if (typ) {
          if (typ === 'cours' && d.badges.indexOf('Cours') === -1 && d.title.indexOf('cours') === -1 && d.title.indexOf('chapitre') === -1) return false;
          if (typ === 'td' && d.badges.indexOf('TD') === -1 && d.title.indexOf('td') === -1) return false;
          if (typ === 'tp' && d.badges.indexOf('TP') === -1 && d.title.indexOf('tp') === -1) return false;
        }
        return true;
      });

      var matchedCards = allCards.filter(function (c) {
        if (query && c.title.indexOf(query) === -1 && c.desc.indexOf(query) === -1) return false;
        if (lang) {
          if (lang === 'fr' && c.badges.indexOf('FR') === -1) return false;
          if (lang === 'en' && c.badges.indexOf('EN') === -1) return false;
        }
        return true;
      });

      allDocs.forEach(function (d) { d.el.style.display = 'none'; });
      matched.forEach(function (d) { d.el.style.display = 'flex'; });

      allCards.forEach(function (c) { c.el.style.display = 'none'; });
      matchedCards.forEach(function (c) { c.el.style.display = ''; });

      var total = matched.length + matchedCards.length;
      if (countEl) {
        if (query && total === 0) {
          countEl.textContent = 'Aucun résultat pour « ' + searchInput.value.trim() + ' »';
        } else if (query) {
          countEl.textContent = total + ' résultat' + (total > 1 ? 's' : '');
        } else {
          countEl.textContent = '';
        }
      }
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
    var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

    if (prevBtn) prevBtn.addEventListener('click', function() { prevSlide(); resetAuto(); });
    if (nextBtn) nextBtn.addEventListener('click', function() { nextSlide(); resetAuto(); });

    function startAuto() {
      if (prefersReduced) return;
      autoInterval = setInterval(nextSlide, 4000);
    }
    function resetAuto() { clearInterval(autoInterval); startAuto(); }

    var container = track.closest('.carousel-container');
    if (container) {
      container.addEventListener('mouseenter', function() { clearInterval(autoInterval); });
      container.addEventListener('mouseleave', function() { startAuto(); });
      container.addEventListener('focusin', function() { clearInterval(autoInterval); });
      container.addEventListener('focusout', function() { startAuto(); });
    }

    var startX = 0;
    track.addEventListener('touchstart', function(e) { startX = e.changedTouches[0].screenX; });
    track.addEventListener('touchend', function(e) {
      var diff = startX - e.changedTouches[0].screenX;
      if (Math.abs(diff) > 40) { diff > 0 ? nextSlide() : prevSlide(); resetAuto(); }
    });

    window.addEventListener('resize', function() { goTo(current); });

    document.addEventListener('visibilitychange', function() {
      if (document.hidden) clearInterval(autoInterval);
      else startAuto();
    });

    if (!prefersReduced) startAuto();
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
    document.querySelectorAll('.module-card, .level-item, .news-item').forEach(function (el) {
      el.classList.add('fade-in');
    });
  }

})();
