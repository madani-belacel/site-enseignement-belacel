(function(){'use strict';document.querySelectorAll('button:not([type])').forEach(function(button){if(!button.closest('form'))button.type='button';});function stripAccents(s){return s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();}
var sayAudio=null;function stopSay(){if(sayAudio){sayAudio.pause();sayAudio.currentTime=0;sayAudio=null;}
if('speechSynthesis'in window)speechSynthesis.cancel();}
function playSay(btn){stopSay();var src=btn.getAttribute('data-src');var label=(btn.getAttribute('data-label')||'').trim();if(src){try{sayAudio=new Audio(src);sayAudio.play().catch(function(){speakLabel(label);});return;}catch(e){speakLabel(label);}}else{speakLabel(label);}}
function speakLabel(label){if(label&&'speechSynthesis'in window){var u=new SpeechSynthesisUtterance(label);u.lang='en-GB';u.rate=0.92;speechSynthesis.speak(u);}}
document.addEventListener('click',function(e){var btn=e.target&&e.target.closest?e.target.closest('.say'):null;if(!btn)return;e.preventDefault();playSay(btn);});var themeToggle=document.getElementById('theme-toggle');var html=document.documentElement;function getPreferredTheme(){try{var stored=localStorage.getItem('theme');if(stored)return stored;}catch(e){}
return window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}
function setTheme(theme){html.setAttribute('data-theme',theme);try{localStorage.setItem('theme',theme);}catch(e){}
if(themeToggle){themeToggle.textContent=theme==='dark'?'\u2600':'\u263E';themeToggle.setAttribute('aria-label',theme==='dark'?'Activer le mode clair':'Activer le mode sombre');}}
if(themeToggle){themeToggle.addEventListener('click',function(){var current=html.getAttribute('data-theme');setTheme(current==='dark'?'light':'dark');});}
setTheme(getPreferredTheme());function convertTablesToDocList(){document.querySelectorAll('section.section-alt').forEach(function(sec){var table=sec.querySelector('table');if(!table)return;try{var tbody=table.querySelector('tbody');if(!tbody)return;var docList=document.createElement('div');docList.className='doc-list';Array.prototype.forEach.call(tbody.querySelectorAll('tr'),function(tr){var tds=tr.querySelectorAll('td');if(tds.length<7)return;var num=tds[0].textContent.trim();var title=tds[1].textContent.trim();var desc=tds[2].textContent.trim();var dialogues=tds[3].textContent.trim();var phrases=tds[4].textContent.trim();var pptx=tds[5].textContent.trim();var linksTd=tds[6];var row=document.createElement('div');row.className='doc-row';var mainA=document.createElement('a');mainA.className='doc-item';var audio=linksTd.querySelector('a');mainA.href=audio?audio.getAttribute('href'):'#';var icon=document.createElement('span');icon.className='doc-icon';icon.textContent='📘';mainA.appendChild(icon);var info=document.createElement('div');info.className='doc-info';var titleDiv=document.createElement('div');titleDiv.className='doc-title';titleDiv.textContent=num+'. '+title;var dateDiv=document.createElement('div');dateDiv.className='doc-date';dateDiv.textContent=desc+' · '+dialogues+' dialogues · '+phrases+' phrases · '+pptx+' PPTX';info.appendChild(titleDiv);info.appendChild(dateDiv);mainA.appendChild(info);var extras=document.createElement('div');extras.className='doc-extras';Array.prototype.forEach.call(linksTd.querySelectorAll('a'),function(a){var b=document.createElement('a');b.className='access-badge';b.href=a.getAttribute('href');b.textContent=a.textContent.trim();extras.appendChild(b);});mainA.appendChild(extras);row.appendChild(mainA);docList.appendChild(row);});table.parentNode.replaceChild(docList,table);}catch(e){console.error('convertTablesToDocList error',e);}});}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',convertTablesToDocList);}else{convertTablesToDocList();}
function getAssetBaseUrl(){var pathname=window.location.pathname||'';var repoMatch=pathname.match(/^(.*\/(?:site-enseignement-belacel|site-belacel))(?:\/|$)/);if(repoMatch&&repoMatch[1]){if(window.location.protocol==='file:'){return'file://'+repoMatch[1]+'/';}
return window.location.origin+repoMatch[1]+'/';}
if(window.location.protocol==='file:'){return new URL('.',window.location.href).href;}
return window.location.origin+'/';}
function resolveAssetUrl(assetPath){return new URL(assetPath,getAssetBaseUrl()).href;}
(function initHeaderIdentity(){var headerInner=document.querySelector('.header-inner');var headerLeft=headerInner&&headerInner.querySelector('.header-left');var logoLink=headerLeft&&headerLeft.querySelector('.header-logo');if(!headerLeft||!logoLink)return;var existingPhoto=headerLeft.querySelector('.header-profile-photo');if(!existingPhoto){var photo=document.createElement('img');photo.src=resolveAssetUrl('images/photo-profil-96.avif');photo.alt='Dr. BELACEL Madani';photo.loading='eager';photo.decoding='async';photo.width=52;photo.height=52;photo.className='header-profile-photo';photo.setAttribute('draggable','false');photo.onerror=function(){this.onerror=null;this.src=resolveAssetUrl('images/photo-profil-96.webp');};headerLeft.insertBefore(photo,logoLink);}
var title=logoLink.querySelector('.header-logo-text');if(title){title.innerHTML='Dr. BELACEL Madani<small>MCB — Université de Mostaganem</small>';}
var banner=document.querySelector('.header-banner');if(banner)banner.remove();})();(function initPreviousNavigation(){var previousButtons=document.querySelectorAll('a.btn');Array.prototype.forEach.call(previousButtons,function(button){var text=(button.textContent||'').replace(/\s+/g,' ').trim();if(!/Précédent|Previous|◀/.test(text))return;button.setAttribute('href','#previous');button.addEventListener('click',function(event){event.preventDefault();var ref=document.referrer;if(ref&&ref!==''&&ref!==window.location.href){try{var refUrl=new URL(ref,window.location.href);if(refUrl.origin===window.location.origin||refUrl.protocol==='file:'){window.location.href=refUrl.href;return;}}catch(e){}}
if(window.history.length>1){window.history.back();return;}
var pathname=window.location.pathname;var trimmed=pathname.replace(/\/[^/]+$/,'/');var fallback=trimmed+'index.html';window.location.href=fallback;});});})();
/* Lien d'evitement : WCAG 2.4.1 (contourner les blocs).
   77 pages l'avaient ecrit dans leur HTML, 2 806 ne l'avaient pas. Plutot
   que modifier 2 883 fichiers, on l'injecte ici — comme la barre de langue.
   Invisible tant qu'il n'a pas le focus, puis il ramene au contenu. */
function placeSkipLink() {
  if (document.querySelector('.skip-link')) return;
  var cible = document.getElementById('main-content');
  if (!cible) {
    cible = document.querySelector('main') ||
            document.querySelector('.page-content') ||
            document.querySelector('article');
    if (cible && !cible.id) cible.id = 'main-content';
  }
  if (!cible) return;
  var a = document.createElement('a');
  a.href = '#' + cible.id;
  a.className = 'skip-link';
  a.textContent = 'Aller au contenu principal';
  var tete = document.querySelector('header.header') || document.body;
  if (tete && tete.parentNode) tete.parentNode.insertBefore(a, tete);
  else document.body.insertBefore(a, document.body.firstChild);
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', placeSkipLink);
} else {
  placeSkipLink();
}

function placeLanguageAndFlag() {
  var headerInner = document.querySelector('.header-inner');
  if (!headerInner) return;
  var header = document.querySelector('header.header') || headerInner.parentNode;

  /* Une barre fine est toujours creee sous le menu. Deux raisons :
     - le selecteur de langue y reste visible en permanence (l'en-tete etant
       sticky) sans masquer aucun lien ;
     - le drapeau s'y pose a droite, dans un emplacement vide. Il ne peut
       pas aller dans l'en-tete : elle est deja pleine (logo + faculty +
       7 liens + bouton de theme) et le drapeau y recouvrait
       « Dernieres Actualites » tout en etant coupe par le bord. */
  var bar = header.querySelector('.lang-bar');
  if (!bar) {
    bar = document.createElement('div');
    bar.className = 'lang-bar';
    header.appendChild(bar);
  }

  var switcher = document.querySelector('.language-switcher, .qr-tabs');
  if (switcher && !switcher.closest('.header')) {
    bar.appendChild(switcher);
    switcher.classList.add('lang-switcher-docked');
  }

  var flag = document.querySelector('.flag-corner');
  if (flag && !flag.closest('footer')) {
    bar.appendChild(flag);
    flag.className = 'flag-corner flag-corner-inline';
  }
}
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', placeLanguageAndFlag);
} else {
  placeLanguageAndFlag();
}

var navToggle=document.getElementById('nav-toggle');var navList=document.getElementById('nav-list');function closeDropdowns(){document.querySelectorAll('.nav-dropdown.open').forEach(function(dropdown){dropdown.classList.remove('open');var toggle=dropdown.querySelector('.nav-dropdown-toggle');if(toggle)toggle.setAttribute('aria-expanded','false');});}function closeMobileNav(){if(!navToggle||!navList)return;navList.classList.remove('open');navToggle.setAttribute('aria-expanded','false');navToggle.textContent='\u2630';}if(navToggle&&navList){navToggle.setAttribute('aria-controls','nav-list');navToggle.addEventListener('click',function(){var isOpen=navList.classList.toggle('open');navToggle.setAttribute('aria-expanded',isOpen?'true':'false');navToggle.textContent=isOpen?'\u2715':'\u2630';});document.addEventListener('click',function(e){if(!navToggle.contains(e.target)&&!navList.contains(e.target)){closeMobileNav();closeDropdowns();}});document.addEventListener('keydown',function(e){if(e.key==='Escape'){closeMobileNav();closeDropdowns();}});window.addEventListener('resize',function(){if(window.innerWidth>768)closeMobileNav();});}
document.querySelectorAll('.nav-dropdown-toggle').forEach(function(toggle,index){var menu=toggle.nextElementSibling;if(menu&&!menu.id)menu.id='nav-submenu-'+(index+1);toggle.setAttribute('role','button');toggle.setAttribute('aria-haspopup','true');toggle.setAttribute('aria-expanded','false');if(menu)toggle.setAttribute('aria-controls',menu.id);function toggleMenu(event){event.preventDefault();event.stopPropagation();var parent=toggle.closest('.nav-dropdown');var isOpen=parent.classList.toggle('open');toggle.setAttribute('aria-expanded',isOpen?'true':'false');}toggle.addEventListener('click',toggleMenu);toggle.addEventListener('keydown',function(event){if(event.key==='Enter'||event.key===' '){toggleMenu(event);}else if(event.key==='Escape'){var parent=toggle.closest('.nav-dropdown');parent.classList.remove('open');toggle.setAttribute('aria-expanded','false');}});});(function setActiveNav(){function normalizeUrl(value){try{var path=decodeURI(new URL(value,window.location.href).pathname).replace(/\/index\.html$/,'/').replace(/\/{2,}/g,'/');return path.length>1?path.replace(/\/$/,''):path;}catch(e){return(value||'').split(/[?#]/)[0];}}var current=normalizeUrl(window.location.href);document.querySelectorAll('.nav-list a').forEach(function(a){if(a.classList.contains('nav-dropdown-toggle')||!a.getAttribute('href'))return;if(normalizeUrl(a.href)===current){a.classList.add('active');var parent=a.closest('.nav-dropdown');var toggle=parent&&parent.querySelector('.nav-dropdown-toggle');if(toggle)toggle.classList.add('active');}});})();function initSearch(){var searchInput=document.getElementById('search-input');var filterModule=document.getElementById('filter-module');var filterType=document.getElementById('filter-type');var filterLang=document.getElementById('filter-lang');var countEl=document.getElementById('results-count');if(!searchInput)return;var allDocs=[];document.querySelectorAll('.doc-item').forEach(function(item){allDocs.push({el:item,title:stripAccents((item.querySelector('.doc-title')||{}).textContent||''),date:(item.querySelector('.doc-date')||{}).textContent||'',badges:Array.from(item.querySelectorAll('.badge')).map(function(b){return b.textContent;}),module:item.getAttribute('data-module')||'',level:item.getAttribute('data-level')||''});});var allCards=[];document.querySelectorAll('.module-card').forEach(function(card){allCards.push({el:card,title:stripAccents((card.querySelector('h3')||{}).textContent||''),desc:stripAccents((card.querySelector('p')||{}).textContent||''),badges:Array.from(card.querySelectorAll('.badge')).map(function(b){return b.textContent;}),module:card.getAttribute('data-module')||'',types:(card.getAttribute('data-types')||'').split(/\s+/).filter(Boolean)});});function filterDocs(){var query=stripAccents((searchInput.value||'').trim());var mod=filterModule?filterModule.value:'';var typ=filterType?filterType.value:'';var lang=filterLang?filterLang.value:'';var matched=allDocs.filter(function(d){if(query&&d.title.indexOf(query)===-1)return false;if(mod&&d.module!==mod)return false;if(lang){if(lang==='fr'&&d.badges.indexOf('FR')===-1&&d.badges.indexOf('Français')===-1)return false;if(lang==='en'&&d.badges.indexOf('EN')===-1&&d.badges.indexOf('Anglais')===-1)return false;}
if(typ){if(typ==='cours'&&d.badges.indexOf('Cours')===-1&&d.title.indexOf('cours')===-1&&d.title.indexOf('chapitre')===-1)return false;if(typ==='td'&&d.badges.indexOf('TD')===-1&&d.title.indexOf('td')===-1)return false;if(typ==='tp'&&d.badges.indexOf('TP')===-1&&d.title.indexOf('tp')===-1)return false;}
return true;});var matchedCards=allCards.filter(function(c){if(query&&c.title.indexOf(query)===-1&&c.desc.indexOf(query)===-1)return false;if(mod&&c.module!==mod)return false;if(typ&&c.types.indexOf(typ)===-1)return false;if(lang){if(lang==='fr'&&c.badges.indexOf('FR')===-1)return false;if(lang==='en'&&c.badges.indexOf('EN')===-1)return false;}
return true;});allDocs.forEach(function(d){d.el.style.display='none';});matched.forEach(function(d){d.el.style.display='flex';});allCards.forEach(function(c){c.el.style.display='none';});matchedCards.forEach(function(c){c.el.style.display='';});var total=matched.length+matchedCards.length;if(countEl){if(total===0){countEl.textContent=query?'Aucun résultat pour « '+searchInput.value.trim()+' »':'Aucun résultat pour les filtres sélectionnés';}else{countEl.textContent=total+' résultat'+(total>1?'s':'');}}}
var debounceTimer=null;function debouncedFilter(){clearTimeout(debounceTimer);debounceTimer=setTimeout(filterDocs,300);}
searchInput.addEventListener('input',debouncedFilter);if(filterModule)filterModule.addEventListener('change',filterDocs);if(filterType)filterType.addEventListener('change',filterDocs);if(filterLang)filterLang.addEventListener('change',filterDocs);filterDocs();}
if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',initSearch);}else{initSearch();}
(function initCarousel(){var track=document.getElementById('carousel-track');if(!track)return;var slides=track.querySelectorAll('.carousel-slide');var totalSlides=slides.length;var dotsContainer=document.getElementById('carousel-dots');var prevBtn=document.querySelector('.carousel-btn-prev');var nextBtn=document.querySelector('.carousel-btn-next');var current=0;var autoInterval;var prefersReduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;function getVisible(){if(window.innerWidth<=600)return 1;if(window.innerWidth<=900)return 2;return 3;}
function goTo(index){var v=getVisible();var max=Math.max(0,totalSlides-v);if(index<0)index=max;if(index>max)index=0;current=index;var pct=(100/v)*current;track.style.transform='translateX(-'+pct+'%)';if(dotsContainer){var dots=dotsContainer.querySelectorAll('.carousel-dot');var dotIndex=Math.min(current,dots.length-1);dots.forEach(function(d,i){d.classList.toggle('active',i===dotIndex);});}}
function nextSlide(){goTo(current+1);}
function prevSlide(){goTo(current-1);}
if(dotsContainer){var dotCount=Math.max(1,totalSlides-getVisible()+1);for(var i=0;i<dotCount;i++){var dot=document.createElement('button');dot.className='carousel-dot'+(i===0?' active':'');dot.setAttribute('aria-label','Aller au slide '+(i+1));dot.addEventListener('click',(function(idx){return function(){goTo(idx);};})(i));dotsContainer.appendChild(dot);}}
if(prevBtn)prevBtn.addEventListener('click',function(){prevSlide();resetAuto();});if(nextBtn)nextBtn.addEventListener('click',function(){nextSlide();resetAuto();});function startAuto(){if(prefersReduced)return;autoInterval=setInterval(nextSlide,4000);}
function resetAuto(){clearInterval(autoInterval);startAuto();}
var container=track.closest('.carousel-container');if(container){container.addEventListener('mouseenter',function(){clearInterval(autoInterval);});container.addEventListener('mouseleave',function(){startAuto();});container.addEventListener('focusin',function(){clearInterval(autoInterval);});container.addEventListener('focusout',function(){startAuto();});}
var startX=0;track.addEventListener('touchstart',function(e){startX=e.changedTouches[0].screenX;});track.addEventListener('touchend',function(e){var diff=startX-e.changedTouches[0].screenX;if(Math.abs(diff)>40){diff>0?nextSlide():prevSlide();resetAuto();}});window.addEventListener('resize',function(){goTo(current);});document.addEventListener('visibilitychange',function(){if(document.hidden)clearInterval(autoInterval);else startAuto();});if(!prefersReduced)startAuto();})();if(typeof IntersectionObserver!=='undefined'){var observer=new IntersectionObserver(function(entries){entries.forEach(function(entry){if(entry.isIntersecting){entry.target.classList.add('fade-in');observer.unobserve(entry.target);}});},{threshold:0.1});document.querySelectorAll('.module-card, .level-item, .news-item').forEach(function(el){observer.observe(el);});}else{document.querySelectorAll('.module-card, .level-item, .news-item').forEach(function(el){el.classList.add('fade-in');});}})();(function(){
  var btt=document.createElement('button');
  btt.className='btt';btt.type='button';btt.setAttribute('aria-label','Revenir en haut de la page');btt.textContent='⬆';
  btt.addEventListener('click',function(){var reduceMotion=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;window.scrollTo({top:0,behavior:reduceMotion?'auto':'smooth'});});
  var shown=false;
  window.addEventListener('scroll',function(){
    var y=window.scrollY||document.documentElement.scrollTop;
    if(y>420&&!shown){document.body.appendChild(btt);requestAnimationFrame(function(){btt.classList.add('show');});shown=true;}
    else if(y<=420&&shown){btt.classList.remove('show');}
  },{passive:true});
})();
