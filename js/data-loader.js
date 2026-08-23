// Async data loader: fetches generated_courses.json and exposes window.COURSES_DATA / window.NEWS_DATA,
// then dispatches a 'data-loaded' event so pages can render after availability.
(function () {
  'use strict';
  if (typeof window === 'undefined') return;
  var base = '/js/';
  try {
    if (document.currentScript && document.currentScript.src) {
      base = document.currentScript.src.replace(/[^/]*$/, '');
    }
  } catch (e) {}
  function emit(courses, news) {
    document.dispatchEvent(new CustomEvent('data-loaded', { detail: { courses: courses || null, news: news || null } }));
  }
  fetch(base + 'generated_courses.json', { cache: 'no-cache' })
    .then(function (resp) {
      if (!resp.ok) throw new Error('HTTP ' + resp.status);
      return resp.json();
    })
    .then(function (j) {
      if (j.courses) window.COURSES_DATA = j.courses;
      if (j.news) window.NEWS_DATA = j.news;
      console.info('data-loader: données chargées depuis', base + 'generated_courses.json');
      emit(window.COURSES_DATA, window.NEWS_DATA);
    })
    .catch(function (err) {
      console.warn('data-loader: échec du chargement des données', err);
      emit(null, null);
    });
})();
