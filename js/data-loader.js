// Async data loader: fetches generated_courses.json and exposes window.COURSES_DATA / window.NEWS_DATA,
// then dispatches a 'data-loaded' event so pages can render after availability.
(function () {
  'use strict';
  if (typeof window === 'undefined') return;

  function resolveJsonUrl() {
    try {
      var scriptEl = document.currentScript || document.querySelector('script[src*="data-loader.js"]');
      if (scriptEl && scriptEl.src) {
        return new URL('generated_courses.json', new URL(scriptEl.src, window.location.href)).href;
      }
    } catch (e) {}

    var fallback = new URL('js/generated_courses.json', window.location.href);
    return fallback.href;
  }

  function emit(courses, news) {
    document.dispatchEvent(new CustomEvent('data-loaded', { detail: { courses: courses || null, news: news || null } }));
  }

  var jsonUrl = resolveJsonUrl();

  fetch(jsonUrl, { cache: 'no-cache' })
    .then(function (resp) {
      if (!resp.ok) throw new Error('HTTP ' + resp.status);
      return resp.json();
    })
    .then(function (j) {
      if (j && j.courses) window.COURSES_DATA = j.courses;
      if (j && j.news) window.NEWS_DATA = j.news;
      console.info('data-loader: données chargées depuis', jsonUrl);
      emit(window.COURSES_DATA, window.NEWS_DATA);
    })
    .catch(function (err) {
      console.warn('data-loader: échec du chargement des données', err);
      emit(null, null);
    });
})();
