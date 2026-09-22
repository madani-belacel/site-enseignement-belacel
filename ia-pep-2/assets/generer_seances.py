#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du module « Intelligence Artificielle — PEP ENS 2ème année »
(Dr. Madani BELACEL, Université de Mostaganem).

Pédagogie revisitée : chaque séance suit la structure « Accroche → Explication
pas à pas → Démonstration → Exercice guidé → Résumé visuel » inspirée des
vidéos de vulgarisation (analogies simples, exemples concrets, progression pas
à pas, vérifications de compréhension).

Pour chaque séance (seance_XX.py) :
  - index.html          : page web du cours, trilingue (EN/FR/AR) avec onglets
  - cours-fr.md         : cours détaillé en français
  - cours-en.md         : cours détaillé en anglais
  - fiche-synthese.md   : fiche de synthèse (points clés, analogies, exemples, quiz)
  - presentation.pptx   : support de présentation (python-pptx)
  - slides.md           : diapositives (Marp)
  - dialogues-fr.md     : scripts de dialogues en français
  - dialogues-en.md     : scripts de dialogues en anglais

Pages globales du module :
  - index.html          : sommaire des 10 séances (trilingue)
  - outils-ia.html      : boîte à outils (12+ outils IA détaillés)
  - construire-ia.html  : 3 approches pour construire sa propre IA

Usage :
    python3 ia-pep-2/assets/generer_seances.py [--seances 1 3 5]
"""
import pathlib
import sys

BASE = pathlib.Path(__file__).resolve().parent.parent  # ia-pep-2/
DATA = pathlib.Path(__file__).resolve().parent / "data"
ROOT = BASE.parent  # racine du site

import importlib

try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
    PPTX_OK = True
except Exception:  # pragma: no cover
    PPTX_OK = False

SITE = "https://madani-belacel.github.io/site-enseignement-belacel"

# Palette du module (identique aux pages « Module Intelligence Artificielle »)
C_PRIMARY = RGBColor(0x17, 0x7B, 0xBE)
C_DARK = RGBColor(0x26, 0x32, 0x38)
C_LIGHT = RGBColor(0xEC, 0xEF, 0xF1)
C_ACCENT = RGBColor(0x2E, 0x7D, 0x32)


# --------------------------------------------------------------------------
# Petits utilitaires
# --------------------------------------------------------------------------
def tri(d, cls="p"):
    """Transforme un dict {fr,en,ar} en trois éléments balisés par la langue."""
    return (
        f'<{cls} class="lang-fr">{d["fr"]}</{cls}>',
        f'<{cls} class="lang-en">{d["en"]}</{cls}>',
        f'<{cls} class="lang-ar">{d["ar"]}</{cls}>',
    )


def trijoin(d, cls="p"):
    return "".join(tri(d, cls))


def md_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def L(fr, en, ar=None):
    """Construit un dict trilingue {fr,en,ar} (ar=en par défaut)."""
    return {"fr": fr, "en": en, "ar": ar if ar is not None else en}


LANG_EMOJI = {"fr": "🇫🇷", "en": "🇬🇧", "ar": "🇩🇿"}


# --------------------------------------------------------------------------
# Cadre HTML commun (header / nav / footer) — conforme au reste du site
# --------------------------------------------------------------------------
def head_html(title, desc, canonical, prefix, json_ld):
    return f"""<!DOCTYPE html><html lang="fr" data-theme="light"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title}</title>
<link href="{canonical}" rel="canonical"/>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{prefix}css/style.css">
<link rel="stylesheet" href="{prefix}ia-pep-2/assets/styles-seance.css">
<link rel="icon" href="{prefix}images/Université_de_Mostaganem.png">
<script type="application/ld+json">
{json_ld}
</script>
</head><body>

<header class="header" role="banner">
  <div class="header-inner">
    <div class="header-left">
      <a href="{prefix}index.html" class="header-logo">
        <picture><source srcset="{prefix}images/Université_de_Mostaganem.avif" type="image/avif"><source srcset="{prefix}images/Université_de_Mostaganem.webp" type="image/webp"><img loading="lazy" width="960" height="931" src="{prefix}images/Université_de_Mostaganem.png" alt="Université de Mostaganem"></picture>
        <div class="header-logo-text">Dr. BELACEL Madani<small>MCB — Université de Mostaganem</small></div>
      </a>
      <div class="header-faculty">
        <picture><source srcset="{prefix}images/LOGO-FLE-UNIV-Mosta.avif" type="image/avif"><source srcset="{prefix}images/LOGO-FLE-UNIV-Mosta.webp" type="image/webp"><img loading="lazy" width="207" height="243" src="{prefix}images/LOGO-FLE-UNIV-Mosta.jpeg" alt="Faculté des langues étrangères"></picture>
      </div>
    </div>
    <img loading="lazy" width="132" height="95" src="{prefix}images/alg_drap.gif" alt="Algérie" class="flag-corner">
    <button id="nav-toggle" class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <nav role="navigation" aria-label="Navigation principale">
      <ul id="nav-list" class="nav-list">
      <li><a href="{prefix}index.html">Accueil</a></li>
      <li class="nav-dropdown">
        <a href="#" class="nav-dropdown-toggle" role="button">À Propos</a>
        <ul class="nav-dropdown-menu">
          <li><a href="{prefix}index.html#about">Présentation</a></li>
          <li><a href="{prefix}habilitation.html">Habilitation Universitaire</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
        </ul>
      </li>
      <li><a href="{prefix}enseignement.html">Enseignement</a></li>
      <li class="nav-dropdown">
        <a href="#" class="nav-dropdown-toggle" role="button">Domaines d'expertise</a>
        <ul class="nav-dropdown-menu">
          <li><a href="{prefix}tic.html">TIC</a></li>
          <li><a href="{prefix}cours/Examen-TIC/index.html">Examens TIC</a></li>
          <li><a href="{prefix}informatique-ens.html">Informatique ENS</a></li>
          <li><a href="{prefix}recherche-documentaire.html">Recherche Documentaire</a></li>
          <li><a href="{prefix}reseaux.html">Réseaux Mostaganem</a></li>
          <li><a href="{prefix}cours/_index_Module_Recherche_Articles.html">Recherche &amp; Articles</a></li>
          <li><a href="{prefix}ia-pep-2/index.html">IA en Éducation (PEP 2A)</a></li>
          <li><a href="{prefix}ia-pep-2/outils-ia.html">IA PEP 2A — Outils</a></li>
          <li><a href="{prefix}ia-pep-2/construire-ia.html">IA PEP 2A — Construire</a></li>
        </ul>
      </li>
      <li><a href="{prefix}recherche.html">Recherche</a></li>
      <li><a href="{prefix}ressources.html">Ressources</a></li>
      <li class="nav-dropdown">
        <a href="#" class="nav-dropdown-toggle" role="button">Dernières Actualités</a>
        <ul class="nav-dropdown-menu">
          <li><a href="{prefix}index.html#news">Actualités des Modules</a></li>
          <li><a href="{prefix}ressources.html">Ressources</a></li>
        </ul>
      </li>
      <li><a href="{prefix}contact.html">Contact</a></li>
      <li><button type="button" id="theme-toggle" class="theme-toggle" aria-label="Changer le thème">☾</button></li>
      </ul>
    </nav>
  </div>
</header>
"""


def footer_html(prefix):
    return f"""<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer-logos">
      <picture><source srcset="{prefix}images/Université_de_Mostaganem.avif" type="image/avif"><source srcset="{prefix}images/Université_de_Mostaganem.webp" type="image/webp"><img loading="lazy" width="960" height="931" src="{prefix}images/Université_de_Mostaganem.png" alt="Université de Mostaganem" class="footer-logo"></picture>
      <img loading="lazy" width="132" height="95" src="{prefix}images/alg_drap.gif" alt="Algérie" class="footer-logo">
    </div>
    <div class="footer-infos">
      <span>📧 madani.belacel [at] univ-mosta.dz</span>
      <span>📍 Université de Mostaganem</span>
      <span>📅 2026-2027</span>
    </div>
    <p>© 2026 Dr. Madani BELACEL — Tous droits réservés. Supports pédagogiques librement téléchargeables.</p>
  </div>
</footer>
<script src="{prefix}js/main.v2.js"></script>
"""


TABS_SCRIPT = """<script>
(function() {
  var root = document.querySelector('.seance-content, .module-content, .ia-page');
  var tabs = document.querySelectorAll('.lang-tab');
  if (!root) return;
  function setLang(lang) {
    root.classList.remove('lang-en', 'lang-fr', 'lang-ar');
    root.classList.add('lang-' + lang);
    tabs.forEach(function(t) {
      t.classList.toggle('active', t.getAttribute('data-lang') === lang);
    });
  }
  tabs.forEach(function(t) {
    t.addEventListener('click', function() { setLang(t.getAttribute('data-lang')); });
  });
  setLang('fr');
})();
</script>
</body></html>"""


def lang_tabs():
    return """<div class="language-switcher">
    <div class="lang-tabs" role="group" aria-label="Choisir la langue">
  <button type="button" class="lang-tab active" data-lang="fr">🇫🇷 Français</button>
  <button type="button" class="lang-tab" data-lang="en">🇬🇧 English</button>
  <button type="button" class="lang-tab" data-lang="ar">🇩🇿 العربية</button>
</div>
    </div>"""


# --------------------------------------------------------------------------
# Rendu d'une séance
# --------------------------------------------------------------------------
def render_blocks(blocks):
    """Rend une liste de blocs (p / ul / table / note / pre) en 3 langues."""
    fr, en, ar = [], [], []
    for b in blocks:
        typ = b["t"]
        if typ == "p":
            for lang, acc in (("fr", fr), ("en", en), ("ar", ar)):
                acc.append(f'<p class="lang-{lang}">{b[lang]}</p>')
        elif typ == "ul":
            for lang, acc in (("fr", fr), ("en", en), ("ar", ar)):
                items = "".join(f"<li>{i}</li>" for i in b[lang])
                acc.append(f'<ul class="lang-{lang}">{items}</ul>')
        elif typ == "ol":
            for lang, acc in (("fr", fr), ("en", en), ("ar", ar)):
                items = "".join(f"<li>{i}</li>" for i in b[lang])
                acc.append(f'<ol class="lang-{lang}">{items}</ol>')
        elif typ == "note":
            kind = b.get("kind", "tip")
            cls = {"tip": "tip-box", "warn": "warn-box", "goal": "goal-box", "idea": "idea-box", "verify": "check-box"}.get(kind, "tip-box")
            icon = {"tip": "💡", "warn": "⚠️", "goal": "🎯", "idea": "🧩", "verify": "✅"}.get(kind, "💡")
            for lang in ("fr", "en", "ar"):
                acc_target = fr if lang == "fr" else en if lang == "en" else ar
                acc_target.append(f'<div class="{cls} lang-{lang}">{icon} {b[lang]}</div>')
        elif typ == "table":
            for lang in ("fr", "en", "ar"):
                head = "".join(f"<th>{h}</th>" for h in b["header"][lang])
                rows = "".join(
                    "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
                    for r in b["rows"][lang]
                )
                acc_target = fr if lang == "fr" else en if lang == "en" else ar
                acc_target.append(
                    f'<table class="plan-table lang-{lang}"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>'
                )
        elif typ == "pre":
            for lang in ("fr", "en", "ar"):
                acc_target = fr if lang == "fr" else en if lang == "en" else ar
                acc_target.append(
                    f'<pre class="lang-{lang}"><code>{md_escape(b.get(lang, b.get("fr", "")))}</code></pre>'
                )
    return "\n".join(fr), "\n".join(en), "\n".join(ar)


def render_phase_h2(prefix, titre_fr, titre_en, titre_ar):
    return f'<h2><span class="lang-fr">{titre_fr}</span><span class="lang-en">{titre_en}</span><span class="lang-ar">{titre_ar}</span></h2>'


def render_accroche_html(seance):
    """Phase A — Accroche et analogie simple."""
    acc = seance.get("accroche")
    if not acc:
        return ""
    rows = []
    if acc.get("question"):
        rows.append(
            '<div class="hook-row"><span class="hook-emoji">❓</span><div>'
            f"{trijoin(acc['question'], 'div')}</div></div>"
        )
    if acc.get("analogie"):
        rows.append(
            '<div class="hook-row"><span class="hook-emoji">🍳</span><div>'
            f"{trijoin(acc['analogie'], 'div')}</div></div>"
        )
    if acc.get("phrase"):
        rows.append(
            '<div class="hook-row hook-phrase"><span class="hook-emoji">💡</span><div>'
            f"{trijoin(acc['phrase'], 'div')}</div></div>"
        )
    return f"""<section id="accroche" class="hook-box">
{render_phase_h2(None, "🎬 Accroche et analogie — 5 min", "🎬 Hook and analogy — 5 min", "🎬 انطلاقة وتشبيه — 5 دقائق")}
{''.join(rows)}
</section>"""


def render_videos_html(seance):
    """Ressources vidéo — une carte par vidéo."""
    vids = seance.get("videos") or []
    if not vids:
        return ""
    cards = []
    for v in vids:
        titre = "".join(tri(v["titre"], "div"))
        concept = "".join(tri(v["concept"], "div"))
        lang_badge = LANG_EMOJI.get(v.get("langue", "fr"), "")
        todo = "\n<!-- TODO: remplacer par lien définitif -->" if "results?search_query" in v.get("url", "") else ""
        cards.append(
            f'<a class="video-card" href="{v["url"]}" target="_blank" rel="noopener">'
            f'<span class="vid-thumb">▶️</span>'
            f'<span class="vid-info">{titre}<span class="vid-lang">{lang_badge} YouTube</span>{concept}</span>'
            f'</a>{todo}'
        )
    return f"""<section id="videos">
{render_phase_h2(None, "📺 Vidéos pour mieux comprendre", "📺 Videos to understand better", "📺 فيديوهات لفهم أفضل")}
<div class="video-grid">{"".join(cards)}</div>
</section>"""


def render_exercice_html(seance):
    """Phase D — Exercice guidé avec solution."""
    ex = seance.get("exercise_guide")
    if not ex:
        return ""
    enonce = "".join(tri(ex["enonce"], "div"))
    demarche = "".join(tri(ex.get("demarche", ex["enonce"]), "div"))
    sol = "".join(tri(ex["solution"], "div"))
    demarche_label = '<span class="lang-fr">💭 Démarche (méthode à suivre)</span><span class="lang-en">💭 Method (steps to follow)</span><span class="lang-ar">💭 الخطوات المتبّعة</span>'
    return f"""<section id="exercice" class="ex-box">
{render_phase_h2(None, "✏️ Exercice guidé — 15 min", "✏️ Guided exercise — 15 min", "✏️ تمرين موجّه — 15 دقيقة")}
<div class="ex-enonce">{enonce}</div>
<details class="ex-solution" open><summary>💭 {demarche_label}</summary>
<div style="margin-top:.6rem;">{demarche}</div></details>
<details class="ex-solution"><summary>🔓 <span class="lang-fr">Solution et correction</span><span class="lang-en">Solution and correction</span><span class="lang-ar">الحلّ والتصحيح</span></summary>
<div style="margin-top:.6rem;">{sol}</div></details>
</section>"""


def render_verifications_html(seance):
    """Vérifications « As-tu bien compris ? »."""
    v = seance.get("verifications") or []
    if not v:
        return ""
    items = []
    for i, item in enumerate(v, 1):
        q = "".join(tri(item["q"], "div"))
        r = "".join(tri(item["r"], "div"))
        items.append(
            f'<details class="verify-item"><summary><span class="verify-num">Q{i}</span><span>{q}</span></summary>'
            f'<div class="verify-ans">{r}</div></details>'
        )
    return f"""<section id="verif">
{render_phase_h2(None, "💭 As-tu bien compris ?", "💭 Did you understand?", "💭 هل فهمت جيداً؟")}
<div class="verify-list">{"".join(items)}</div>
</section>"""


def render_fiche_html(seance):
    """Phase E — Fiche de synthèse (points, analogies, exemples) + quiz."""
    fs = seance.get("fiche_synthese") or {}
    parts = []
    points = fs.get("points") or []
    if points:
        lis = "".join(f"<li>{trija3(p)}</li>" for p in points)
        parts.append(
            f'<div class="fiche-col"><h3>🗝️ <span class="lang-fr">Points clés</span><span class="lang-en">Key points</span><span class="lang-ar">النقاط الرئيسية</span></h3><ul>'
            f'{"".join("<li>" + "".join(tri(p, "span")) + "</li>" for p in points)}</ul></div>'
        )
    analogies = fs.get("analogies") or []
    if analogies:
        parts.append(
            f'<div class="fiche-col"><h3>🍳 <span class="lang-fr">Analogies utilisées</span><span class="lang-en">Analogies used</span><span class="lang-ar">التشبيهات المستعملة</span></h3><ul>'
            f'{"".join("<li>🎯 " + "".join(tri(a, "span")) + "</li>" for a in analogies)}</ul></div>'
        )
    exemples = fs.get("exemples") or []
    if exemples:
        parts.append(
            f'<div class="fiche-col"><h3>🧩 <span class="lang-fr">Exemples concrets</span><span class="lang-en">Concrete examples</span><span class="lang-ar">أمثلة ملموسة</span></h3><ul>'
            f'{"".join("<li>✏️ " + "".join(tri(e, "span")) + "</li>" for e in exemples)}</ul></div>'
        )
    fiche_html = ""
    if parts:
        fiche_html = (
            f'<section id="fiche">'
            f'{render_phase_h2(None, "📋 Fiche de synthèse — 5 min", "📋 Summary sheet — 5 min", "📋 بطاقة التركيب — 5 دقائق")}'
            f'<div class="fiche-grid">{"".join(parts)}</div></section>'
        )
    if fs.get("analogie_finale"):
        fiche_html += (
            '<section id="symbiose"><div class="hook-row hook-phrase"><span class="hook-emoji">🏁</span><div>'
            f"{trijojo(fs['analogie_finale'], 'div')}</div></div></section>"
        )
    return fiche_html


def trijojo(d, cls="div"):
    return "".join(tri(d, cls))


def trija3(d):
    return "".join(tri(d, "span"))


def quiz_opts(q):
    """Normalise les options d'une question quiz en liste de dicts {fr,en,ar}.

    Les sources utilisent L([...],[...],[...]) soit un dict de listes ;
    le rendu attend une liste de dicts. Les deux formats sont acceptés.
    """
    opts = q.get("options")
    if isinstance(opts, dict):
        fr = opts.get("fr", []) or []
        en = opts.get("en", []) or []
        ar = opts.get("ar", []) or []
        n = max(len(fr), len(en), len(ar))
        return [
            {
                "fr": fr[k] if k < len(fr) else "",
                "en": en[k] if k < len(en) else "",
                "ar": ar[k] if k < len(ar) else "",
            }
            for k in range(n)
        ]
    return opts or []


def render_quiz_html(seance):
    """Quiz de 3 à 5 questions — les réponses sont dans des <details>."""
    fs = seance.get("fiche_synthese") or {}
    quiz = fs.get("quiz") or []
    if not quiz:
        return ""
    items = []
    for i, q in enumerate(quiz, 1):
        opts = []
        for j, opt in enumerate(quiz_opts(q)):
            mark = "✅" if j == q.get("answer", 0) else "🔘"
            fd = f'<div class="lang-fr">{opt["fr"]}</div><div class="lang-en">{opt["en"]}</div><div class="lang-ar">{opt["ar"]}</div>'
            opts.append(f'<div class="quiz-opt {("quiz-ok" if j == q.get("answer", 0) else "")}">{mark} {fd}</div>')
        qq = "".join(tri(q["q"], "div"))
        exp = qq2 = "".join(tri(q.get("exp", q["q"]), "div"))
        items.append(
            f'<details class="quiz-item"><summary><span class="verify-num">Q{i}</span><span>{qq}</span></summary>'
            f'<div class="quiz-opts">{"" .join(opts)}</div>'
            f'<div class="verify-ans">{exp}</div></details>'
        )
    return f"""<section id="quiz">
{render_phase_h2(None, "🧠 Quiz — vérifie ta compréhension", "🧠 Quiz — check your understanding", "🧠 اختبار — تحقّق من فهمك")}
<div class="verify-list">{"".join(items)}</div>
</section>"""


def render_seance_html(seance, prefix):
    n = seance["num"]
    seg = seance["slug"]
    icon = seance["icon"]
    t = seance["titles"]
    canonical = f"{SITE}/ia-pep-2/{seg}/index.html"
    json_ld = f"""{{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Séance {n:02d} — {t['fr']}",
  "url": "{canonical}",
  "author": {{ "@type": "Person", "name": "Dr. BELACEL Madani" }},
  "provider": {{ "@type": "Organization", "name": "ENS — Université de Mostaganem" }},
  "inLanguage": "fr",
  "learningResourceType": "Cours universitaire (1h30)",
  "isPartOf": {{ "@type": "Course", "name": "Intelligence Artificielle en Éducation — PEP 2ème année" }}
}}"""

    # Objectifs
    obj_fr = "".join(f"<li>{o['fr']}</li>" for o in seance["objectifs"])
    obj_en = "".join(f"<li>{o['en']}</li>" for o in seance["objectifs"])
    obj_ar = "".join(f"<li>{o['ar']}</li>" for o in seance["objectifs"])

    # Plan (déroulé = 5 phases A-E + atelier)
    plan_rows_fr, plan_rows_en, plan_rows_ar = [], [], []
    for ph in seance["plan"]:
        badge = ph.get("badge", "")
        badge_html = f'<span class="phase-badge">{badge}</span> ' if badge else ""
        plan_rows_fr.append(f'<tr><td class="time">{ph["time"]}</td><td>{badge_html}<strong>{ph["fr"]}</strong><br><span style="color:var(--text-muted);font-size:.9em;">{ph.get("detail", {}).get("fr", "")}</span></td></tr>')
        plan_rows_en.append(f'<tr><td class="time">{ph["time"]}</td><td>{badge_html}<strong>{ph["en"]}</strong><br><span style="color:var(--text-muted);font-size:.9em;">{ph.get("detail", {}).get("en", "")}</span></td></tr>')
        plan_rows_ar.append(f'<tr><td class="time">{ph["time"]}</td><td>{badge_html}<strong>{ph["ar"]}</strong><br><span style="color:var(--text-muted);font-size:.9em;">{ph.get("detail", {}).get("ar", "")}</span></td></tr>')

    # Sections détaillées (phases B + C)
    sections_html = []
    sec_i = 0
    for sec in seance["sections"]:
        sec_i += 1
        sfr, sen, sar = render_blocks(sec["blocks"])
        sec_cls = ' class="profiter-section"' if sec["id"] == "profiter" else ""
        sections_html.append(f"""
<section id="{sec['id']}"{sec_cls}>
<h2><span class="lang-fr">{sec["titre"]["fr"]}</span><span class="lang-en">{sec["titre"]["en"]}</span><span class="lang-ar">{sec["titre"]["ar"]}</span></h2>
<div class="lang-fr">{sfr}</div>
<div class="lang-en">{sen}</div>
<div class="lang-ar">{sar}</div>
</section>""")
    sections_html = "\n".join(sections_html)

    # Activités
    act_fr = "".join(f"<li>{a['fr']}</li>" for a in seance["activites"])
    act_en = "".join(f"<li>{a['en']}</li>" for a in seance["activites"])
    act_ar = "".join(f"<li>{a['ar']}</li>" for a in seance["activites"])

    # À retenir
    ret_fr = "".join(f"<li>{r['fr']}</li>" for r in seance["retenir"])
    ret_en = "".join(f"<li>{r['en']}</li>" for r in seance["retenir"])
    ret_ar = "".join(f"<li>{r['ar']}</li>" for r in seance["retenir"])

    # Glossaire
    gloss = []
    for g in seance["glossaire"]:
        gloss.append(
            f'<details><summary class="gl-term">{g["term"]} <span style="font-weight:400;color:var(--text-muted);">— {g.get("term_en", "")}</span></summary>'
            f'<p class="lang-fr">{g["def_fr"]}</p>'
            f'<p class="lang-en">{g["def_en"]}</p>'
            f'<p class="lang-ar">{g["def_ar"]}</p></details>'
        )
    gloss_html = f'<div class="glossary">{"".join(gloss)}</div>'

    # Extra pédagogique
    accroche_html = render_accroche_html(seance)
    videos_html = render_videos_html(seance)
    exercice_html = render_exercice_html(seance)
    verif_html = render_verifications_html(seance)
    fiche_html = render_fiche_html(seance)
    quiz_html = render_quiz_html(seance)

    # Ressources
    res_files = [
        ("📘", "cours-fr.md", "Cours détaillé (Français)", "Document texte complet de la séance en français."),
        ("📗", "cours-en.md", "Course notes (English)", "Full written lesson in English."),
        ("📙", "cours-ar.md", "Cours résumé (العربية)", "ملخّص الدرس باللغة العربية."),
        ("🗒️", "fiche-synthese.md", "Fiche de synthèse + quiz", "Points clés, analogies, exemples et quiz corrigé."),
        ("🖥️", "presentation.pptx", "Présentation PowerPoint", "Support de cours à projeter en classe."),
        ("🎞️", "slides.md", "Diapositives (Marp)", "Support de présentation au format Markdown."),
        ("💬", "dialogues-fr.md", "Dialogues pédagogiques (FR)", "Scripts de dialogues à jouer en classe, en français."),
        ("💬", "dialogues-en.md", "Pedagogical dialogues (EN)", "Classroom dialogue scripts in English."),
        ("🧰", "../outils-ia.html", "Outils IA (boîte à outils)", "12+ outils IA détaillés : usage, exemple, forces, limites."),
        ("🛠️", "../construire-ia.html", "Construire son IA", "3 approches : no-code (Dify), API Python, local (Ollama)."),
    ]
    res_cards = "".join(
        f'<a class="resource-card" href="{r[1]}"><span class="rc-icon">{r[0]}</span>'
        f'<div class="rc-title">{r[2]}</div><div class="rc-desc">{r[3]}</div></a>'
        for r in res_files
    )

    # Navigation entre séances
    prev_n, next_n = max(1, n - 1), min(10, n + 1)
    nav = [
        ('<a href="../seance-%02d/index.html">◀ Séance précédente</a>' % prev_n) if n > 1 else '<a class="disabled">◀ Séance précédente</a>',
        '<a href="../index.html">📋 Sommaire du module</a>',
        ('<a href="../seance-%02d/index.html">Séance suivante ▶</a>' % next_n) if n < 10 else '<a class="disabled">Séance suivante ▶</a>',
    ]
    nav_html = '<div class="seance-nav">' + "".join(nav) + '</div>'

    html = head_html(
        f'Séance {n:02d} — {t["fr"]} — IA en Éducation PEP 2A — Dr. Madani BELACEL',
        seance["descriptions"]["fr"],
        canonical,
        prefix,
        json_ld,
    )
    html += f"""
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="{prefix}index.html">Accueil</a></li>
    <li><a href="{prefix}enseignement.html">Enseignement</a></li>
    <li><a href="{prefix}ia-pep-2/index.html">IA en Éducation — PEP 2A</a></li>
    <li class="current">Séance {n:02d}</li>
  </ol>
</nav>

<main class="page-content">
  <div class="seance-content">
    <h1>{icon} <span class="lang-fr">Séance {n:02d} — {t["fr"]}</span><span class="lang-en">Session {n:02d} — {t["en"]}</span><span class="lang-ar">الحصة {n:02d} — {t["ar"]}</span></h1>
    <p style="font-size:1.05rem;color:var(--text-muted);margin:0.3rem 0 0.2rem;">
      {trija3(seance["descriptions"])}
    </p>
    <p style="font-size:.85rem;color:var(--text-muted);">
      <span class="lang-fr">Durée : {seance["duration"]} · Module « Intelligence Artificielle » · 2ème année PEP — ENS</span>
      <span class="lang-en">Duration: {seance["duration"]} · Module "Artificial Intelligence" · 2nd year PEP — ENS</span>
      <span class="lang-ar">المدّة: {seance["duration"]} · وحدة « الذكاء الاصطناعي » · السنة الثانية PEP — المدرسة العليا للأساتذة</span>
    </p>
    {lang_tabs()}

    <div class="seance-meta">
      <strong class="lang-fr">🎯 Objectifs pédagogiques</strong>
      <strong class="lang-en">🎯 Learning objectives</strong>
      <strong class="lang-ar">🎯 الأهداف البيداغوجية</strong>
      <ul class="lang-fr">{obj_fr}</ul>
      <ul class="lang-en">{obj_en}</ul>
      <ul class="lang-ar">{obj_ar}</ul>
      <strong class="lang-fr">🧱 Prérequis</strong>
      <strong class="lang-en">🧱 Prerequisites</strong>
      <strong class="lang-ar">🧱 المكتسبات القبلية</strong>
      <p class="lang-fr">{seance["prerequis"]["fr"]}</p>
      <p class="lang-en">{seance["prerequis"]["en"]}</p>
      <p class="lang-ar">{seance["prerequis"]["ar"]}</p>
    </div>

    <h2><span class="lang-fr">⏱️ Déroulé de la séance (1 h 30)</span><span class="lang-en">⏱️ Session plan (1h30)</span><span class="lang-ar">⏱️ سير الحصة (ساعة و30 دقيقة)</span></h2>
    <table class="plan-table lang-fr"><thead><tr><th>Durée</th><th>Étape</th></tr></thead><tbody>{"".join(plan_rows_fr)}</tbody></table>
    <table class="plan-table lang-en"><thead><tr><th>Time</th><th>Step</th></tr></thead><tbody>{"".join(plan_rows_en)}</tbody></table>
    <table class="plan-table lang-ar"><thead><tr><th>المدّة</th><th>المرحلة</th></tr></thead><tbody>{"".join(plan_rows_ar)}</tbody></table>

    <h2><span class="lang-fr">📚 Contenu de la séance</span><span class="lang-en">📚 Lesson content</span><span class="lang-ar">📚 محتوى الحصة</span></h2>
    {accroche_html}
    {sections_html}
    {videos_html}
    {exercice_html}
    {verif_html}
    {fiche_html}
    {quiz_html}

    <h2><span class="lang-fr">✏️ Activités et exercices</span><span class="lang-en">✏️ Activities and exercises</span><span class="lang-ar">✏️ الأنشطة والتمارين</span></h2>
    <ul class="lang-fr">{act_fr}</ul>
    <ul class="lang-en">{act_en}</ul>
    <ul class="lang-ar">{act_ar}</ul>

    <h2><span class="lang-fr">🧠 À retenir</span><span class="lang-en">🧠 Key takeaways</span><span class="lang-ar">🧠 ما يجب تذكّره</span></h2>
    <ul class="lang-fr">{ret_fr}</ul>
    <ul class="lang-en">{ret_en}</ul>
    <ul class="lang-ar">{ret_ar}</ul>

    <h2><span class="lang-fr">📖 Glossaire</span><span class="lang-en">📖 Glossary</span><span class="lang-ar">📖 مسرد المصطلحات</span></h2>
    {gloss_html}

    <h2><span class="lang-fr">📂 Ressources de la séance</span><span class="lang-en">📂 Session resources</span><span class="lang-ar">📂 موارد الحصة</span></h2>
    <div class="resource-grid">{res_cards}</div>

    {nav_html}
  </div>
</main>

footer_placeholder""" + TABS_SCRIPT

    html = html.replace("footer_placeholder", footer_html(prefix))
    return html


# --------------------------------------------------------------------------
# Cours Markdown (FR / EN / AR)
# --------------------------------------------------------------------------
def md_for(lang, seance):
    m = [f"# Séance {seance['num']:02d} — {seance['titles'][lang]}", ""]
    m.append(f"**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  ")
    m.append(f"**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  ")
    m.append(f"**Durée : {seance['duration']}**  ")
    m.append(f"")
    m.append(seance["descriptions"][lang])
    m.append("")
    m.append("## Objectifs pédagogiques")
    for o in seance["objectifs"]:
        m.append(f"- {o[lang]}")
    m.append("")
    m.append("## Déroulé de la séance (1 h 30)")
    for ph in seance["plan"]:
        m.append(f"- **{ph['time']} — {ph[lang]}** : {ph.get('detail', {}).get(lang, '')}")
    m.append("")
    m.append("## A. Accroche et analogie (5 min)")
    acc = seance.get("accroche")
    if acc:
        m.append(f"- **Question :** {acc['question'][lang]}")
        m.append(f"- **Analogie :** {acc['analogie'][lang]}")
        m.append(f"- **En une phrase :** {acc['phrase'][lang]}")
    m.append("")
    m.append("## B + C. Explication pas à pas et démonstration")
    for sec in seance["sections"]:
        m.append(f"### {sec['titre'][lang]}")
        for b in sec["blocks"]:
            t = b["t"]
            if t == "p":
                m.append(b[lang])
            elif t in ("ul", "ol"):
                m.append("")
                for i in b[lang]:
                    m.append(f"- {i}")
            elif t == "note":
                m.append(f"> 💡 **{b[lang]}**")
            elif t == "table":
                m.append("")
                m.append("| " + " | ".join(b["header"][lang]) + " |")
                m.append("|" + "---|".join([""] * len(b["header"][lang])) + "---|")
                for r in b["rows"][lang]:
                    m.append("| " + " | ".join(r) + " |")
            elif t == "pre":
                m.append("")
                m.append("```")
                m.append(b.get(lang, b.get("fr", "")))
                m.append("```")
        m.append("")
    vids = seance.get("videos") or []
    if vids:
        m.append("## 📺 Ressources vidéo")
        for v in vids:
            m.append(f"- **{v['titre'][lang]}** ({v.get('langue', 'fr')}): {v['url']} — {v['concept'][lang]}")
        m.append("")
    ex = seance.get("exercise_guide")
    if ex:
        m.append("## D. Exercice guidé (15 min)")
        m.append(f"**Énoncé :** {ex['enonce'][lang]}")
        m.append(f"**Méthode :** {ex.get('demarche', ex['enonce'])[lang]}")
        m.append(f"**Solution :** {ex['solution'][lang]}")
        m.append("")
    verifs = seance.get("verifications") or []
    if verifs:
        m.append("## 💭 As-tu bien compris ?")
        for i, v in enumerate(verifs, 1):
            m.append(f"- **Q{i}.** {v['q'][lang]}")
            m.append(f"  *Réponse :* {v['r'][lang]}")
        m.append("")
    fs = seance.get("fiche_synthese") or {}
    if fs.get("points"):
        m.append("## E. Résumé visuel et mémorable (5 min)")
        m.append("### Points clés")
        for p in fs["points"]:
            m.append(f"- {p[lang]}")
        if fs.get("analogies"):
            m.append("### Analogies utilisées")
            for a in fs["analogies"]:
                m.append(f"- 🍳 {a[lang]}")
        if fs.get("exemples"):
            m.append("### Exemples concrets")
            for e in fs["exemples"]:
                m.append(f"- ✏️ {e[lang]}")
        if fs.get("analogie_finale"):
            m.append(f"> 🏁 **Analogie finale :** {fs['analogie_finale'][lang]}")
        quiz = fs.get("quiz") or []
        if quiz:
            m.append("### Quiz — vérifie ta compréhension")
            for i, q in enumerate(quiz, 1):
                m.append(f"**Q{i}.** {q['q'][lang]}")
                for j, opt in enumerate(quiz_opts(q)):
                    mark = "✅" if j == q.get("answer", 0) else "🔘"
                    m.append(f"   - {mark} {opt[lang]}")
                m.append(f"   *Explication :* {q.get('exp', q['q'])[lang]}")
        m.append("")
    m.append("## Activités et exercices")
    for a in seance["activites"]:
        m.append(f"- {a[lang]}")
    m.append("")
    m.append("## À retenir")
    for r in seance["retenir"]:
        m.append(f"- {r[lang]}")
    m.append("")
    m.append("## Glossaire")
    for g in seance["glossaire"]:
        key = {"fr": "def_fr", "en": "def_en", "ar": "def_ar"}.get(lang, "def_fr")
        m.append(f"- **{g['term']}** : {g[key]}")
    m.append("")
    m.append("## Ressources de la séance")
    m.append("- fiche-synthese.md (fiche de synthèse + quiz corrigé)")
    m.append("- presentation.pptx (support de cours)")
    m.append("- slides.md (diapositives Marp)")
    m.append("- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)")
    m.append("- outils-ia.html / construire-ia.html (boîte à outils du module)")
    return "\n".join(m)


# --------------------------------------------------------------------------
# Fiche de synthèse (Markdown trilingue léger)
# --------------------------------------------------------------------------
def fiche_synthese_md(seance):
    n = seance["num"]
    t = seance["titles"]
    fs = seance.get("fiche_synthese") or {}
    m = [f"# Fiche de synthèse — Séance {n:02d} : {t['fr']}", ""]
    m.append(f"**{t['en']}**")
    m.append("")
    m.append(f"> {seance['descriptions']['fr']}")
    m.append("")
    m.append("## Points clés")
    for p in fs.get("points", []):
        m.append(f"1. {p['fr']}")
        m.append(f"> EN: {p['en']}")
        m.append(f"> AR: {p['ar']}")
    m.append("")
    m.append("## Analogies utilisées")
    for a in fs.get("analogies", []):
        m.append(f"- 🍳 {a['fr']}")
    m.append("")
    m.append("## Exemples concrets")
    for e in fs.get("exemples", []):
        m.append(f"- ✏️ {e['fr']}")
    if fs.get("analogie_finale"):
        m.append("")
        m.append(f"> 🏁 **Analogie finale :** {fs['analogie_finale']['fr']}")
        m.append(f"> EN: {fs['analogie_finale']['en']} / AR: {fs['analogie_finale']['ar']}")
    m.append("")
    quiz = fs.get("quiz") or []
    m.append("## Quiz (5 questions) — réponses cachées")
    m.append("")
    m.append("<details>")
    m.append("<summary>Réponses du quiz</summary>")
    m.append("")
    for i, q in enumerate(quiz, 1):
        m.append(f"**Q{i}. {q['q']['fr']}**")
        for j, opt in enumerate(quiz_opts(q)):
            mark = "✅" if j == q.get("answer", 0) else "🔘"
            m.append(f"- {mark} {opt['fr']}")
        m.append(f"*Explication : {q.get('exp', q['q'])['fr']}*")
        m.append("")
    m.append("</details>")
    m.append("")
    m.append(f"---")
    m.append("")
    m.append("**À retenir :** " + " ; ".join(r["fr"] for r in seance["retenir"]))
    m.append("")
    return "\n".join(m)


# --------------------------------------------------------------------------
# PowerPoint
# --------------------------------------------------------------------------
def build_pptx(seance, path):
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    def add_title_slide(extra=""):
        slide = prs.slides.add_slide(prs.slide_layouts[6])
        bg = slide.background
        bg.fill.solid()
        bg.fill.fore_color.rgb = C_DARK
        tb = slide.shapes.add_textbox(Inches(0.9), Inches(2.0), Inches(11.5), Inches(2))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = f"Séance {seance['num']:02d} — {seance['titles']['fr']}"
        r.font.size = Pt(40)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        p2 = tf.add_paragraph()
        r2 = p2.add_run()
        r2.text = seance["titles"]["en"]
        r2.font.size = Pt(20)
        r2.font.color.rgb = C_LIGHT
        sub = slide.shapes.add_textbox(Inches(0.9), Inches(4.4), Inches(11.5), Inches(1.6))
        tf2 = sub.text_frame
        tf2.word_wrap = True
        p3 = tf2.paragraphs[0]
        r3 = p3.add_run()
        r3.text = "Module « Intelligence Artificielle » — 2ème année PEP · ENS\nDr. Madani BELACEL — Université de Mostaganem" + (extra and f"\n{extra}" or "")
        r3.font.size = Pt(15)
        r3.font.color.rgb = C_LIGHT
        return slide

    def add_content_slide(title_fr, title_en, bullets_fr, bullets_en):
        slide = prs.slides.add_slide(prs.slide_layouts[1])
        slide.shapes.title.text = title_fr
        if title_en and title_en != title_fr:
            slide.shapes.title.text_frame.paragraphs[0].add_run().text = f"  ·  {title_en}"
        body = slide.placeholders[1].text_frame
        body.word_wrap = True
        first = True
        for b in bullets_fr:
            p = body.paragraphs[0] if first else body.add_paragraph()
            first = False
            p.text = b
            p.level = 0
            p.font.size = Pt(20)
        if bullets_en:
            p = body.add_paragraph()
            p.text = ""
            p = body.add_paragraph()
            p.text = "English summary:"
            p.font.size = Pt(13)
            p.font.italic = True
            p.font.color.rgb = RGBColor(0x78, 0x89, 0x9C)
            for b in bullets_en:
                pe = body.add_paragraph()
                pe.text = "• " + b
                pe.level = 1
                pe.font.size = Pt(13)
                pe.font.color.rgb = RGBColor(0x54, 0x6E, 0x7A)
        return slide

    add_title_slide()
    # Objectifs
    add_content_slide(
        "Objectifs de la séance", "Learning objectives",
        [o["fr"] for o in seance["objectifs"]],
        [o["en"] for o in seance["objectifs"]],
    )
    # Déroulé
    add_content_slide(
        "Déroulé pédagogique (1 h 30)", "Session plan",
        [f"{ph['time']} — {ph['fr']}" for ph in seance["plan"]],
        [ph["en"] for ph in seance["plan"]],
    )
    # A. Accroche
    acc = seance.get("accroche")
    if acc:
        add_content_slide(
            "🎬 Accroche (5 min)", "Hook",
            [f"❓ {acc['question']['fr']}", f"🍳 {acc['analogie']['fr']}", f"💡 {acc['phrase']['fr']}"],
            [acc["phrase"]["en"]],
        )
    # Une diapo par section (B + C)
    for sec in seance["sections"]:
        fr_bullets = []
        for b in sec["blocks"]:
            if b["t"] == "p":
                fr_bullets.append(b["fr"])
            elif b["t"] == "ul":
                fr_bullets.extend(b["fr"])
        en_bullets = []
        for b in sec["blocks"]:
            if b["t"] == "p":
                en_bullets.append(b["en"])
            elif b["t"] == "ul":
                en_bullets.extend(b["en"])
        add_content_slide(
            sec["titre"]["fr"], sec["titre"]["en"],
            fr_bullets[:6], en_bullets[:4],
        )
    # Vidéos
    vids = seance.get("videos") or []
    if vids:
        add_content_slide(
            "📺 À regarder pour comprendre", "Recommended videos",
            [f"▶️ {v['titre']['fr']} ({v.get('langue', 'fr')})" for v in vids[:4]],
            [v["url"] for v in vids[:4]],
        )
    # D. Exercice
    ex = seance.get("exercise_guide")
    if ex:
        add_content_slide(
            "✏️ Exercice guidé (15 min)", "Guided exercise",
            [ex["enonce"]["fr"], "—", "▶ Solution :", ex["solution"]["fr"]],
            [ex["enonce"]["en"], ex["solution"]["en"]],
        )
    # E. Fiche
    fs = seance.get("fiche_synthese") or {}
    if fs.get("points"):
        add_content_slide(
            "🧠 Fiche de synthèse — points clés", "Summary sheet",
            fs["points"][:5] and [p["fr"] for p in fs["points"][:5]] or [],
            [p["en"] for p in fs["points"][:3]],
        )
    # Quiz
    quiz = fs.get("quiz") or []
    if quiz:
        add_content_slide(
            "🧠 Quiz éclair (3 questions)", "Quick quiz",
            [
                f"Q{i+1}. {q['q']['fr']}\n   ✅ {quiz_opts(q)[q.get('answer', 0)]['fr']}"
                for i, q in enumerate(quiz[:3])
            ],
            [q["q"]["en"] for q in quiz[:3]],
        )
    # À retenir
    add_content_slide(
        "À retenir", "Key takeaways",
        [r["fr"] for r in seance["retenir"]],
        [r["en"] for r in seance["retenir"]],
    )
    # Merci
    add_title_slide("Prochaine séance : à venir.")
    prs.save(path)


# --------------------------------------------------------------------------
# Support de présentation au format Marp (slides.md)
# --------------------------------------------------------------------------
def slides_md(seance):
    n = seance["num"]
    t = seance["titles"]
    icon = seance["icon"]
    lines = [
        "---",
        "marp: true",
        "theme: default",
        "paginate: true",
        "size: 16:9",
        f"title: Séance {n:02d} — {t['fr']}",
        "---",
        "",
        f"# {icon} Séance {n:02d} — {t['fr']}",
        "",
        f"*{t['en']}*",
        "",
        f"**Module Intelligence Artificielle — 2ème année PEP · ENS**",
        "",
        f"Dr. Madani BELACEL — Université de Mostaganem",
    ]
    # Déroulé
    lines += ["", "---", "", "## ⏱️ Déroulé de la séance (1 h 30)", ""]
    for ph in seance["plan"]:
        lines.append(f"- **{ph['time']}** — {ph['fr']}")
    # Objectifs
    lines += ["", "---", "", "## 🎯 Objectifs pédagogiques", ""]
    for o in seance["objectifs"]:
        lines.append(f"- {o['fr']}")
    # A. Accroche
    acc = seance.get("accroche")
    if acc:
        lines += ["", "---", "", "## 🎬 Accroche (5 min)", ""]
        lines.append(f"❓ {acc['question']['fr']}")
        lines.append("")
        lines.append(f"🍳 **Analogie :** {acc['analogie']['fr']}")
        lines.append("")
        lines.append(f"💡 {acc['phrase']['fr']}")
    # Une diapo par section (B+C)
    for sec in seance["sections"]:
        lines += ["", "---", "", f"## {sec['titre']['fr']}", ""]
        fr_bullets = []
        for b in sec["blocks"]:
            if b["t"] == "p":
                fr_bullets.append(b["fr"])
            elif b["t"] == "ul":
                fr_bullets.extend(b["fr"])
            elif b["t"] == "ol":
                fr_bullets.extend(b["fr"])
            elif b["t"] == "note":
                fr_bullets.append(f"💡 {b['fr']}")
        lines.extend("- " + bl.replace("<strong>", "**").replace("</strong>", "**") for bl in fr_bullets[:6])
        lines.append("")
        lines.append(f"*{sec['titre']['en']}*")
    # Vidéos
    vids = seance.get("videos") or []
    if vids:
        lines += ["", "---", "", "## 📺 À regarder après la classe", ""]
        for v in vids[:5]:
            lines.append(f"- **{v['titre']['fr']}** ({v.get('langue', 'fr')}) — {v['url']}")
    # D. Exercice
    ex = seance.get("exercise_guide")
    if ex:
        lines += ["", "---", "", "## ✏️ Exercice guidé (15 min)", ""]
        lines.append(f"**Énoncé :** {ex['enonce']['fr']}")
        lines.append("")
        lines.append(f"**Solution :** {ex['solution']['fr']}")
    # Vérifications
    verifs = seance.get("verifications") or []
    if verifs:
        lines += ["", "---", "", "## 💭 As-tu bien compris ?", ""]
        for v in verifs:
            lines.append(f"- **{v['q']['fr']}**")
            lines.append(f"   - ✅ {v['r']['fr']}")
    # E. Fiche + quiz
    fs = seance.get("fiche_synthese") or {}
    if fs.get("points"):
        lines += ["", "---", "", "## 🧠 Fiche de synthèse — points clés", ""]
        for p in fs["points"][:5]:
            lines.append(f"- {p['fr']}")
        if fs.get("analogie_finale"):
            lines.append("")
            lines.append(f"> 🏁 {fs['analogie_finale']['fr']}")
    quiz = fs.get("quiz") or []
    if quiz:
        lines += ["", "---", "", "## ✅ Quiz éclair (1 min)", ""]
        for i, q in enumerate(quiz[:3]):
            lines.append(f"**Q{i+1}. {q['q']['fr']}**")
            for j, opt in enumerate(quiz_opts(q)):
                mark = "✅" if j == q.get("answer", 0) else "🔘"
                lines.append(f"   - {mark} {opt['fr']}")
    # Activités
    lines += ["", "---", "", "## ✏️ Activités et exercices", ""]
    for a in seance["activites"]:
        lines.append(f"1. {a['fr']}")
    # À retenir
    lines += ["", "---", "", "## 🧠 À retenir", ""]
    for r in seance["retenir"]:
        lines.append(f"- {r['fr']}")
    # Merci
    lines += [
        "",
        "---",
        "",
        "# 🎓 Merci de votre attention",
        "",
        f"**Séance {n:02d} — {t['fr']}**",
        "",
        "*Prochaine séance : venez avec un ordinateur ou un smartphone.*",
        "",
        "Dr. Madani BELACEL — ENS Université de Mostaganem",
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Page d'accueil du module (index.html)
# --------------------------------------------------------------------------
def render_module_index(seances):
    prefix = "../"
    canonical = f"{SITE}/ia-pep-2/index.html"
    json_ld = f"""{{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Intelligence Artificielle en Éducation — PEP 2ème année (ENS)",
  "url": "{canonical}",
  "author": {{ "@type": "Person", "name": "Dr. BELACEL Madani" }},
  "provider": {{ "@type": "Organization", "name": "ENS — Université de Mostaganem" }},
  "inLanguage": "fr",
  "numberOfCredits": "10 séances de 1h30"
}}"""
    cards = []
    for i, (num, s) in enumerate(seances):
        grad = "module-ia-g1" if i % 2 == 0 else "module-ia-g2"
        sseg = s["slug"]
        cards.append(f"""      <a href="{sseg}/index.html" class="module-card">
        <div class="module-card-gradient {grad}"><div class="card-pattern"></div><span class="card-icon">{s["icon"]}</span></div>
        <div class="module-card-content">
          <div class="module-card-date"><span class="lang-fr">Séance {i+1:02d} · {s["duration"]}</span><span class="lang-en">Session {i+1:02d} · {s["duration"]}</span><span class="lang-ar">الحصة {i+1:02d} · {s["duration"]}</span></div>
          <h3><span class="lang-fr">{s["titles"]["fr"]}</span><span class="lang-en">{s["titles"]["en"]}</span><span class="lang-ar">{s["titles"]["ar"]}</span></h3>
          <p><span class="lang-fr">{s["descriptions"]["fr"]}</span><span class="lang-en">{s["descriptions"]["en"]}</span><span class="lang-ar">{s["descriptions"]["ar"]}</span></p>
          <span class="module-card-link"><span class="lang-fr">Ouvrir la séance</span><span class="lang-en">Open the session</span><span class="lang-ar">فتح الحصة</span></span>
        </div>
      </a>""")
    cards_html = "\n".join(cards)

    html = head_html(
        "Module Intelligence Artificielle en Éducation — PEP 2ème année — Dr. Madani BELACEL",
        "10 séances (1h30) pour apprendre à l'étudiant de 2ème année PEP à utiliser l'IA comme assistant de ses études universitaires : recherche, synthèse, exposés, révision, programmation, rédaction, organisation et éthique.",
        canonical,
        prefix,
        json_ld,
    )
    html += f"""
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="{prefix}index.html">Accueil</a></li>
    <li><a href="{prefix}enseignement.html">Enseignement</a></li>
    <li><a href="{prefix}informatique-ens.html">Informatique ENS</a></li>
    <li class="current">IA en Éducation — PEP 2A</li>
  </ol>
</nav>

<main class="page-content">
  <div class="module-content" style="max-width:1100px;margin:0 auto;padding:0 1.5rem;">

    <h1 style="font-family:var(--font-heading);color:var(--primary);margin:1.2rem 0 0.2rem;font-size:1.7rem;">
      🤖 <span class="lang-fr">Intelligence Artificielle en Éducation — PEP 2ème année</span>
      <span class="lang-en">Artificial Intelligence in Education — 2nd year PEP</span>
      <span class="lang-ar">الذكاء الاصطناعي في التربية — السنة الثانية PEP</span>
    </h1>
    <p style="color:var(--text-muted);font-size:.95rem;margin:0 0 0.3rem;">
      <span class="lang-fr">10 séances de 1 h 30 — Dr. Madani BELACEL · ENS Université de Mostaganem · 2026-2027</span>
      <span class="lang-en">10 sessions of 1h30 — Dr. Madani BELACEL · ENS University of Mostaganem · 2026-2027</span>
      <span class="lang-ar">10 حصص من ساعة و30 دقيقة — د. مداني بلعسل · المدرسة العليا للأساتذة - مستغانم · 2026-2027</span>
    </p>
    {lang_tabs()}

    <div class="seance-meta">
      <p class="lang-fr">Ce module apprend à l'étudiant de <strong>2ème année PEP</strong> (futur professeur des écoles) à utiliser l'IA pour <strong>ses propres études universitaires</strong> : suivre les cours, préparer des exposés, faire des recherches, programmer, réviser et comprendre les autres modules. Chaque séance suit la même méthode pédagogique, inspirée des meilleures vidéos de vulgarisation : <strong>accroche, explication pas à pas, démonstration, exercice guidé, résumé visuel</strong>. Chaque séance contient : une page web trilingue (FR/EN/AR), un cours écrit, une fiche de synthèse + quiz, un support PowerPoint, des diapositives et des dialogues à jouer. La page <a href="outils-ia.html">Outils IA</a> centralise 12+ outils, et la page <a href="construire-ia.html">Construire son IA</a> explique 3 approches pour bâtir sa propre IA.</p>
      <p class="lang-en">This module teaches the <strong>2nd-year PEP student</strong> (future primary school teacher) to use AI for <strong>their own university studies</strong>: following courses, preparing presentations, doing research, programming, revising and understanding other modules. Each session follows the same teaching method, inspired by the best explainer videos: <strong>hook, step-by-step explanation, demonstration, guided exercise, visual summary</strong>. Each session contains: a trilingual web page (FR/EN/AR), a written lesson, a summary sheet + quiz, a PowerPoint deck, slides and playable dialogues. The <a href="outils-ia.html">AI Tools</a> page centralises 12+ tools, and the <a href="construire-ia.html">Build your own AI</a> page explains 3 approaches.</p>
      <p class="lang-ar">تُعلّم هذه الوحدةُ طالبَ <strong>السنة الثانية PEP</strong> كيفية استعمال الذكاء الاصطناعي في <strong>دراسته الجامعية</strong>. تتبع كل حصة المنهج البيداغوجي نفسه المستوحى من أفضل فيديوهات التبسيط: <strong>انطلاقة، شرح خطوة بخطوة، عرض تطبيقي، تمرين موجّه، ملخص بصري</strong>. تحتوي كل حصة على: صفحة ويب ثلاثية اللغات، ودرس مكتوب، وبطاقة تركيب + اختبار، وعرض PowerPoint، وشرائح، وحوارات للتمثيل. صفحة <a href="outils-ia.html">أدوات الذكاء الاصطناعي</a> تجمع أكثر من 12 أداة، وصفحة <a href="construire-ia.html">بناء ذكاء اصطناعي</a> تشرح ثلاث مقاربات.</p>
    </div>

    <h2 style="font-family:var(--font-heading);color:var(--navy);margin:1.6rem 0 .6rem;font-size:1.4rem;border-bottom:1px solid var(--border);padding-bottom:.3rem;">
      <span class="lang-fr">🗺️ Les 10 séances du module</span>
      <span class="lang-en">🗺️ The 10 sessions of the module</span>
      <span class="lang-ar">🗺️ حصص الوحدة العشر</span>
    </h2>
    <div class="module-grid">
{cards_html}
      <a href="outils-ia.html" class="module-card">
        <div class="module-card-gradient module-ia-g2" style="box-shadow:inset 0 0 0 2px #fff;"><div class="card-pattern"></div><span class="card-icon">🧰</span></div>
        <div class="module-card-content">
          <div class="module-card-date"><span class="lang-fr">Boîte à outils</span><span class="lang-en">Toolbox</span><span class="lang-ar">صندوق الأدوات</span></div>
          <h3><span class="lang-fr">Outils IA : 12+ outils comparés</span><span class="lang-en">AI Tools: 12+ compared tools</span><span class="lang-ar">أدوات الذكاء الاصطناعي: أكثر من 12 أداة مقارنة</span></h3>
          <p><span class="lang-fr">Pour chaque outil : type, usage, étapes simples, exemple pour un étudiant PEP, forces et limites.</span><span class="lang-en">For each tool: type, use, simple steps, an example for a PEP student, strengths and limits.</span><span class="lang-ar">لكل أداة: النوع، الاستعمال، خطوات بسيطة، مثال لطالب PEP، مزايا وحدود.</span></p>
          <span class="module-card-link"><span class="lang-fr">Ouvrir la page</span><span class="lang-en">Open the page</span><span class="lang-ar">فتح الصفحة</span></span>
        </div>
      </a>
      <a href="construire-ia.html" class="module-card">
        <div class="module-card-gradient module-ia-g1"><div class="card-pattern"></div><span class="card-icon">🛠️</span></div>
        <div class="module-card-content">
          <div class="module-card-date"><span class="lang-fr">Atelier code</span><span class="lang-en">Code workshop</span><span class="lang-ar">ورشة البرمجة</span></div>
          <h3><span class="lang-fr">Construire sa propre IA</span><span class="lang-en">Build your own AI</span><span class="lang-ar">بناء ذكاء اصطناعي خاص بك</span></h3>
          <p><span class="lang-fr">3 approches : no-code (Dify), API Python (Gemini/OpenAI), local (Ollama). Projet de la séance 07.</span><span class="lang-en">3 approaches: no-code (Dify), Python API (Gemini/OpenAI), local (Ollama). Session 7 project.</span><span class="lang-ar">ثلاث مقاربات: بدون كود (Dify)، بواجهة Python (Gemini/OpenAI)، ومحلياً (Ollama). مشروع الحصة السابعة.</span></p>
          <span class="module-card-link"><span class="lang-fr">Ouvrir la page</span><span class="lang-en">Open the page</span><span class="lang-ar">فتح الصفحة</span></span>
        </div>
      </a>
    </div>

    <div class="highlight-box" style="margin:2.5rem 0;">
      <div class="highlight-icon">🎯</div>
      <div class="highlight-content">
        <h3 class="lang-fr">Comment utiliser ce module ?</h3>
        <h3 class="lang-en">How to use this module?</h3>
        <h3 class="lang-ar">كيف تستعملون هذه الوحدة؟</h3>
        <p class="lang-fr">Suivez les séances dans l'ordre (1 à 10). Pour chaque séance : projetez le PowerPoint, distribuez le cours écrit et la <strong>fiche de synthèse</strong>, faites l'exercice guidé, puis faites jouer les dialogues en binômes. Les durées des 5 phases pédagogiques (accroche, explication, démonstration, exercice, résumé) sont indiquées dans le plan de la séance. Consultez <a href="outils-ia.html">Outils IA</a> et <a href="construire-ia.html">Construire son IA</a> pour les outils à comparer, installer et coder.</p>
        <p class="lang-en">Follow the sessions in order (1 to 10). For each session: project the PowerPoint, hand out the written course and the <strong>summary sheet</strong>, run the guided exercise, then let students perform the dialogues in pairs. Timings for the 5 pedagogical phases (hook, explanation, demonstration, exercise, summary) are in the session plan. Check <a href="outils-ia.html">AI Tools</a> and <a href="construire-ia.html">Build your own AI</a> for the tools to compare, install and code.</p>
        <p class="lang-ar">اتبعوا الحصص بالترتيب (من 1 إلى 10). في كل حصة: اعرضوا PowerPoint، وقدّموا الدرس المكتوب و<strong>بطاقة التركيب</strong>، وأنجزوا التمرين الموجّه، ثم اجعلوا الطلبة يمثّلون الحوارات في مجموعات ثنائية. مدد المراحل الخمس (انطلاقة، شرح، عرض، تمرين، ملخص) مذكورة في خطة الحصة. راجعوا <a href="outils-ia.html">أدوات الذكاء الاصطناعي</a> و<a href="construire-ia.html">بناء ذكاء اصطناعي</a>.</p>
      </div>
    </div>

  </div>
</main>

footer_placeholder""" + TABS_SCRIPT

    # gradient inline pour le module
    grad_css = """<style>
  .module-ia-g1{background:linear-gradient(135deg,#263238,#455a64,#78909c);}
  .module-ia-g2{background:linear-gradient(135deg,#1a237e,#283593,#5c6bc0);}
  .module-content .lang-fr{display:none!important;}.module-content .lang-ar{display:none!important;}
  .module-content.lang-fr .lang-en{display:none!important;}.module-content.lang-fr .lang-ar{display:none!important;}.module-content.lang-fr .lang-fr{display:block!important;}
  .module-content.lang-en .lang-fr{display:none!important;}.module-content.lang-en .lang-ar{display:none!important;}.module-content.lang-en .lang-en{display:block!important;}
  .module-content.lang-ar .lang-fr{display:none!important;}.module-content.lang-ar .lang-en{display:none!important;}.module-content.lang-ar .lang-ar{display:block!important;direction:rtl;text-align:right;}
  @media print{.module-content.lang-fr .lang-en,.module-content.lang-fr .lang-ar{display:block!important;}}
</style>"""
    html = html.replace("<main class=\"page-content\">", grad_css + "\n<main class=\"page-content\">")
    html = html.replace("footer_placeholder", footer_html(prefix))
    return html


# --------------------------------------------------------------------------
# Page « Outils IA » (12+ outils)
# --------------------------------------------------------------------------
def render_outils_ia(seances):
    prefix = "../"
    canonical = f"{SITE}/ia-pep-2/outils-ia.html"
    json_ld = f"""{{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Outils IA — Boîte à outils du module IA PEP 2A",
  "url": "{canonical}",
  "author": {{ "@type": "Person", "name": "Dr. BELACEL Madani" }},
  "inLanguage": "fr"
}}"""
    outils = [
        {
            "emoji": "💬",
            "nom": "ChatGPT (OpenAI)",
            "type": L("Assistant de conversation / texte", "Conversational / text assistant", "مساعد محادثة / نص"),
            "usage": L("Expliquer, résumer, rédiger, reformuler, générer des idées.", "Explain, summarise, write, rephrase, generate ideas.", "يشرح ويلخّص ويكتب ويعيد الصياغة ويولّد أفكاراً."),
            "etapes": L("1. Aller sur chatgpt.com → 2. Créer un compte gratuit → 3. Écrire un prompt précis (contexte, objectif, format) → 4. Vérifier la réponse avec son cours.", "1. Go to chatgpt.com → 2. Create a free account → 3. Write a precise prompt (context, goal, format) → 4. Check the answer against your lesson.", "1. ادخل إلى chatgpt.com → 2. أنشئ حساباً مجانياً → 3. اكتب صياغة دقيقة (سياق، هدف، صيغة) → 4. تحقّق من الإجابة مع درسك."),
            "exemple": L("« Je suis étudiant 2ème année PEP. Explique-moi Piaget en 5 points avec un exemple pour le primaire. »", "\"I am a 2nd-year PEP student. Explain Piaget in 5 points with a primary-class example.\"", "« أنا طالب السنة الثانية PEP. اشرح لي بياجيه في خمس نقاط مع مثال للمرحلة الابتدائية »"),
            "forces": L("Polyvalent, gratuit de base, reconnaît l'arabe et le français.", "Versatile, free basics, handles Arabic and French.", "متعدّد الاستعمالات، مجاني أساساً، يفهم العربية والفرنسية."),
            "limites": L("Peut halluciner, pas de sources affichées par défaut.", "Can hallucinate, no sources shown by default.", "قد يهلوس، لا يعرض مصادر افتراضياً."),
        },
        {
            "emoji": "✨",
            "nom": "Google Gemini",
            "type": L("Assistant multimodal (texte, image, voix)", "Multimodal assistant (text, image, voice)", "مساعد متعدّد الوسائط (نص، صورة، صوت)"),
            "usage": L("Mêmes usages que ChatGPT + lecture d'images, de PDF et d'extraits de cours.", "Same uses as ChatGPT + reading images, PDFs and course excerpts.", "نفس استعمالات ChatGPT مع قراءة الصور وملفات PDF ومقتطفات الدروس."),
            "etapes": L("1. gemini.google.com → 2. Compte Google → 3. Coller un extrait de cours → 4. Poser une question ciblée.", "1. gemini.google.com → 2. Google account → 3. Paste a course excerpt → 4. Ask a targeted question.", "1. gemini.google.com → 2. حساب Google → 3. الصق مقتطف درس → 4. اطرح سؤالاً محدّداً."),
            "exemple": L("Photo d'un tableau du cours + « Transforme ce tableau en questions de révision. »", "Photo of a lesson table + \"Turn this table into revision questions.\"", "صورة لجدول من الدرس + « حوّل هذا الجدول إلى أسئلة مراجعة »"),
            "forces": L("Traitement d'image intégré, bonne capacité en arabe.", "Built-in image understanding, good Arabic.", "فهم الصور مدمج، قدرة جيدة على العربية."),
            "limites": L("Compte Google requis ; qualité variable selon le modèle choisi.", "Google account required; quality varies by model.", "يتطلب حساب Google؛ الجودة تختلف حسب النموذج."),
        },
        {
            "emoji": "🎨",
            "nom": "Claude (Anthropic)",
            "type": L("Assistant de texte avancé (rédaction, analyse)", "Advanced text assistant (writing, analysis)", "مساعد نصّي متقدّم (كتابة، تحليل)"),
            "usage": L("Rédaction nuancée, analyse longue d'articles, synthèse de documents.", "Nuanced writing, long-form article analysis, document synthesis.", "كتابة دقيقة، تحليل مقالات طويلة، تركيب وثائق."),
            "etapes": L("1. claude.ai → 2. Compte gratuit → 3. Déposer un document ou coller un texte → 4. Demander analyse, résumé ou révision.", "1. claude.ai → 2. Free account → 3. Upload a document or paste text → 4. Ask for analysis, summary or proofreading.", "1. claude.ai → 2. حساب مجاني → 3. ارفع وثيقة أو الصق نصاً → 4. اطلب تحليلاً أو تلخيصاً أو مراجعة."),
            "exemple": L("« Relis mon introduction de mémoire : faut-il une virgule avant « parce que » ? Argumente en 3 lignes. »", "\"Proofread my thesis introduction: is a comma needed before 'parce que'? Argue in 3 lines.\"", "« راجع مقدمة مذكرتي: هل نحتاج فاصلة قبل « لأنّ »؟ علّل في ثلاثة أسطر »"),
            "forces": L("Excellent en français écrit, grand contexte (longs textes).", "Excellent in written French, large context (long texts).", "ممتاز في الفرنسية المكتوبة، سياق كبير (نصوص طويلة)."),
            "limites": L("Moins connu des étudiants ; version gratuite limitée en volume.", "Less known to students; free version limited in volume.", "أقل شهرة عند الطلبة؛ النسخة المجانية محدودة الحجم."),
        },
        {
            "emoji": "🔎",
            "nom": "Perplexity",
            "type": L("Moteur de réponse sourcée", "Sourced answer engine", "محرّك إجابات بمصادر"),
            "usage": L("Répondre avec des sources citées ; vérifier une information ; trouver des liens utiles.", "Answer with cited sources; check a fact; find useful links.", "يجيب مع مصادر مذكورة؛ تثبّت من معلومة؛ إيجاد روابط مفيدة."),
            "etapes": L("1. perplexity.ai → 2. Poser la question → 3. Lire les sources en bas → 4. Ouvrir et vérifier 2 sources.", "1. perplexity.ai → 2. Ask the question → 3. Read the sources below → 4. Open and check 2 sources.", "1. perplexity.ai → 2. اطرح السؤال → 3. اقرأ المصادر أسفله → 4. افتح وتحقق من مصدرين."),
            "exemple": L("Fonction « focus academic » : « Quels sont les effets des écrans sur le sommeil des enfants ? »", "\"Academic focus\": \"What are the effects of screens on children's sleep?\"", "وظيفة « التوجيه الأكاديمي »: « ما تأثيرات الشاشات على نوم الأطفال؟ »"),
            "forces": L("Sources visibles, options Academic / YouTube / Research.", "Visible sources, Academic / YouTube / Research options.", "مصادر ظاهرة، خيارات أكاديمية / يوتيوب / بحث."),
            "limites": L("Sources pas toujours de première qualité ; usage gratuit limité.", "Sources not always top-quality; limited free usage.", "المصادر ليست دائماً عالية الجودة؛ الاستعمال المجاني محدود."),
        },
        {
            "emoji": "📚",
            "nom": "Google Scholar / Consensus",
            "type": L("Moteurs de littérature scientifique", "Scientific literature engines", "محرّكات الأدبيات العلمية"),
            "usage": L("Trouver des articles, thèses, études vérifiables ; connaître le consensus scientifique.", "Find papers, theses, verifiable studies; know the scientific consensus.", "إيجاد المقالات والأطروحات والدراسات القابلة للتحقق؛ معرفة الإجماع العلمي."),
            "etapes": L("1. scholar.google.com → 2. Mots-clés en anglais → 3. Filtrer par année → 4. Lire l'abstract → / Consensus : taper une question en anglais.", "1. scholar.google.com → 2. English keywords → 3. Filter by year → 4. Read the abstract. / Consensus: type a question in English.", "1. scholar.google.com → 2. كلمات مفتاحية بالإنجليزية → 3. صفِّ بالسنة → 4. اقرأ الملخص. / Consensus: اكتب سؤالاً بالإنجليزية."),
            "exemple": L("Rechercher « primary school morphology instruction 2020 » et vérifier la revue et l'année.", "Search \"primary school morphology instruction 2020\" and check the journal and year.", "ابحث عن التربية... بالكلمات المفتاحية الإنجليزية وتحقق من المجلة والسنة."),
            "forces": L("Fiabilité scientifique, citations, filtres précis.", "Scientific reliability, citations, precise filters.", "موثوقية علمية، استشهادات، فلاتر دقيقة."),
            "limites": L("Interface en anglais, nécessite de savoir lire un résumé.", "English interface, requires knowing how to read an abstract.", "الواجهة إنجليزية، يتطلب معرفة قراءة الملخص."),
        },
        {
            "emoji": "📓",
            "nom": "NotebookLM (Google)",
            "type": L("Assistant de notes basé sur vos documents", "Notes assistant based on your documents", "مساعد ملاحظات يعتمد على وثائقك"),
            "usage": L("Poser des questions à VOS cours (résumés, quiz, podcats audio de révision).", "Ask questions to YOUR lessons (summaries, quizzes, revision audio podcasts).", "اطرح أسئلة على دروسك (ملخصات، اختبارات، بودكاست مراجعة)."),
            "etapes": L("1. notebooklm.google.com → 2. Compte Google → 3. Importer un PDF de cours → 4. Poser des questions avec sources.", "1. notebooklm.google.com → 2. Google account → 3. Import a course PDF → 4. Ask with sources.", "1. notebooklm.google.com → 2. حساب Google → 3. استورد PDF درسك → 4. اسأل مع المصادر."),
            "exemple": L("Importer un polycopié d'anglais → « Crée un quiz de 10 questions sur ce chapitre. »", "Import an English handout → \"Create a 10-question quiz on this chapter.\"", "استورد طبقة إنجليزية → « أنشئ اختباراً من 10 أسئلة حول هذا الفصل »"),
            "forces": L("Reste fidèle à vos documents ; génère des podcasts audio.", "Stays faithful to your documents; generates audio podcasts.", "يظل وفيّاً لوثائقك؛ يولّد بودكاست صوتياً."),
            "limites": L("Nécessite vos documents ; en anglais pour certaines fonctions.", "Requires your documents; some features English-only.", "يتطلب وثائقك؛ بعض الوظائف بالإنجليزية فقط."),
        },
        {
            "emoji": "🖥️",
            "nom": "Gamma (canva-gamma)",
            "type": L("Générateur de présentations IA", "AI presentation generator", "مولّد عروض عرض ذكي"),
            "usage": L("Créer un diaporama complet (texte, images, mise en page) à partir d'un prompt.", "Create a full slide deck (text, images, layout) from a prompt.", "أنشئ عرضاً كاملاً (نصوص، صور، تنسيق) من صياغة."),
            "etapes": L("1. gamma.app → 2. « Generate » → 3. Coller le plan de votre exposé → 4. Choisir un style → 5. Exporter en PDF/PPT.", "1. gamma.app → 2. \"Generate\" → 3. Paste your outline → 4. Pick a style → 5. Export to PDF/PPT.", "1. gamma.app → 2. « توليد » → 3. الصق خطة عرضك → 4. اختر نمطاً → 5. صدّر PDF/PPT."),
            "exemple": L("Prompt : plan d'exposé en 6 sections sur l'eau dans le programme de CE2.", "Prompt: a 6-section outline on water in the Year-4 curriculum.", "صياغة: خطة عرض من 6 أقسام عن الماء في منهاج CE2."),
            "forces": L("Rapide, visuel, très joli rendu.", "Fast, visual, great-looking output.", "سريع، بصري، نتيجة جميلة جداً."),
            "limites": L("Crédits gratuits limités ; toujours relire/corriger le contenu.", "Limited free credits; always proofread/edit.", "رصيد مجاني محدود؛ راجع المحتوى دائماً."),
        },
        {
            "emoji": "🧑‍🎨",
            "nom": "Canva IA (Magic Studio)",
            "type": L("Design graphique assisté par IA", "AI-assisted graphic design", "تصميم جرافيكي بمساعدة الذكاء الاصطناعي"),
            "usage": L("Affiches, cartes, images d'illustration, fiches pédagogiques attrayantes.", "Posters, cards, illustrations, attractive teaching sheets.", "ملصقات، بطاقات، صور توضيحية، بطاقات تربوية جذابة."),
            "etapes": L("1. canva.com (compte étudiant gratuit) → 2. « Magic Design » → 3. Décrire l'affiche souhaitée → 4. Personnaliser.", "1. canva.com (free student account) → 2. \"Magic Design\" → 3. Describe the poster → 4. Customise.", "1. canva.com (حساب طالب مجاني) → 2. « التصميم السحري » → 3. صف الملصق المطلوب → 4. خصّص."),
            "exemple": L("« Affiche A3 pour la classe : les 4 saisons, style dessin animé. »", "\"A3 classroom poster: the 4 seasons, cartoon style.\"", "« ملصق A3 للقسم: الفصول الأربعة، بأسلوب كرتوني »"),
            "forces": L("Simple, modèles riches, gratuit pour les étudiants.", "Simple, rich templates, free for students.", "بسيط، قوالب غنية، مجاني للطلبة."),
            "limites": L("Connexion requise ; attention aux images générées (à vérifier).", "Internet required; check generated images.", "يتطلب اتصالاً؛ تحقق من الصور المولَّدة."),
        },
        {
            "emoji": "💻",
            "nom": "GitHub Copilot / Cursor",
            "type": L("Assistants de code pour programmeurs", "Coding assistants for programmers", "مساعدي برمجة للمطورين"),
            "usage": L("Auto-complétion, explication de code, correction de bugs, suggestions.", "Auto-completion, code explanation, bug fixing, suggestions.", "إكمال تلقائي للكود، تفسير الكود، تصحيح أخطاء، اقتراحات."),
            "etapes": L("1. Installer VS Code (gratuit) → 2. Ajouter l'extension Copilot ou installer Cursor → 3. Ouvrir un fichier .py → 4. Décrire en commentaire ce qu'on veut.", "1. Install VS Code (free) → 2. Add the Copilot extension or install Cursor → 3. Open a .py file → 4. Describe in a comment what you want.", "1. ثبّت VS Code (مجاني) → 2. أضف إضافة Copilot أو ثبّت Cursor → 3. افتح ملف .py → 4. صف في تعليق ما تريد."),
            "exemple": L("Dans un fichier : « # script qui calcule la moyenne d'une liste » puis laisser Copilot compléter.", "In a file: \"# script that computes the average of a list\" then let Copilot complete.", "في ملف: « # برنامج يحسب معدل قائمة » ثم اترك Copilot يكمل."),
            "forces": L("Énorme gain de temps pour les modules d'informatique.", "Huge time saver for computer science modules.", "توفير وقت هائل في وحدات المعلوماتية."),
            "limites": L("Couteux pour l'usage intensif ; comprendre le code reste indispensable.", "Costly for heavy use; understanding code still essential.", "مكلفة للاستعمال المكثف؛ فهم الكود يبقى ضرورياً."),
        },
        {
            "emoji": "🗂️",
            "nom": "Notion AI",
            "type": L("Notes et organisation avec IA", "Notes and organisation with AI", "ملاحظات وتنظيم مع الذكاء الاصطناعي"),
            "usage": L("Organiser cours, fiches, projets ; résumer ; créer des tableaux.", "Organise lessons, sheets, projects; summarise; create tables.", "تنظيم الدروس والبطاقات والمشاريع؛ تلخيص؛ إنشاء جداول."),
            "etapes": L("1. notion.so (gratuit pour étudiants) → 2. Créer une page → 3. « Ask AI » → 4. Résumer un texte collé, générer un plan.", "1. notion.so (free for students) → 2. Create a page → 3. \"Ask AI\" → 4. Summarise pasted text, generate an outline.", "1. notion.so (مجاني للطلبة) → 2. أنشئ صفحة → 3. « اسأل الذكاء » → 4. لخّص نصاً أو ولّد خطة."),
            "exemple": L("Un bloc « Base de données » pour suivre 6 modules + une fiche par séance générée à l'IA.", "A \"Database\" block to track 6 modules + a per-session sheet generated with AI.", "قاعدة بيانات تتبع 6 وحدات + بطاقة لكل حصة مولّدة بالذكاء الاصطناعي."),
            "forces": L("Base de tout : notes, planification, collaboration.", "One place for notes, planning, collaboration.", "قاعدة لكل شيء: ملاحظات، تخطيط، تعاون."),
            "limites": L("Fonctions IA limitées dans la version gratuite.", "AI features limited in the free version.", "وظائف الذكاء الاصطناعي محدودة في النسخة المجانية."),
        },
        {
            "emoji": "🖼️",
            "nom": "DALL·E / Midjourney",
            "type": L("Générateurs d'images", "Image generators", "مولّدو الصور"),
            "usage": L("Illustrer un exposé, créer des images d'exercices ou de départ d'activités.", "Illustrate presentations, create images for exercises or activity starters.", "توضيح العروض، إنشاء صور للتمارين أو لبدايات الأنشطة."),
            "etapes": L("1. Choisir l'outil (DALL·E dans ChatGPT, ou midjourney.com) → 2. Décrire l'image en détail → 3. Générer → 4. Retoucher ou régénérer.", "1. Choose the tool (DALL·E in ChatGPT, or midjourney.com) → 2. Describe the image in detail → 3. Generate → 4. Edit or regenerate.", "1. اختر الأداة (DALL·E في ChatGPT أو midjourney.com) → 2. صف الصورة بالتفصيل → 3. ولّد → 4. عدّل أو أعد التوليد."),
            "exemple": L("« Dessin d'un enfant qui lit sous un arbre, style livre d'école, sans texte. »", "\"A child reading under a tree, schoolbook style, no text.\"", "« رسم طفل يقرأ تحت شجرة، بأسلوب الكتب المدرسية، دون نص »"),
            "forces": L("Images uniques et rapides ; bonnes pour capter l'attention.", "Unique, fast images; great for grabbing attention.", "صور فريدة وسريعة؛ جيدة لجذب الانتباه."),
            "limites": L("Attention aux droits d'image ; résultats parfois bizarres (vérifier).", "Watch image rights; results sometimes odd (check).", "انتبه لحقوق الصور؛ النتائج أحياناً غريبة (تحقق)."),
        },
        {
            "emoji": "🎧",
            "nom": "ElevenLabs / Whisper",
            "type": L("Audio : synthèse vocale et transcription", "Audio: text-to-speech and transcription", "صوت: تخليق كلامي ونسخ"),
            "usage": L("Lire un cours à voix haute (révision auditive), transcrire une vidéo ou un enregistrement.", "Read a lesson aloud (audio revision), transcribe a video or recording.", "قراءة درس بصوت عالٍ (مراجعة سمعية)، نسخ فيديو أو تسجيل."),
            "etapes": L("1. Whisper : ouvrir une vidéo YouTube et demander la transcription / ElevenLabs : coller un texte, choisir une voix, générer le MP3.", "1. Whisper: open a YouTube video and get the transcript / ElevenLabs: paste text, pick a voice, generate MP3.", "1. Whisper: افتح فيديو يوتيوب واحصل على النسخ / ElevenLabs: الصق نصاً، اختر صوتاً، ولّد MP3."),
            "exemple": L("Convertir son propre résumé de cours en fichier audio de 3 minutes à écouter dans le bus.", "Turn your own lesson summary into a 3-minute audio file to listen to on the bus.", "حوّل ملخصك الخاص إلى ملف صوتي من 3 دقائق تستمع إليه في الحافلة."),
            "forces": L("Révise en marchant ; très utile pour la phonétique anglaise.", "Revise on the go; great for English phonetics.", "تراجع وأنت تمشي؛ مفيد جداً للنطق الإنجليزي."),
            "limites": L("Vérifier la fidélité de la transcription ; quotas gratuits limités.", "Check transcription accuracy; limited free quotas.", "تحقق من دقة النسخ؛ حصص مجانية محدودة."),
        },
        {
            "emoji": "🐋",
            "nom": "Ollama",
            "type": L("Modèles d'IA open source en local", "Open-source AI models, run locally", "نماذج ذكاء اصطناعي مفتوحة المصدر محلياً"),
            "usage": L("Faire tourner un modèle d'IA sur son propre ordinateur, sans Internet, gratuitement.", "Run an AI model on your own computer, offline, for free.", "تشغيل نموذج ذكاء اصطناعي على جهازك، دون إنترنت، مجاناً."),
            "etapes": L("1. ollama.com → 2. Installer → 3. `ollama run llama3.2` → 4. Discuter dans le terminal.", "1. ollama.com → 2. Install → 3. `ollama run llama3.2` → 4. Chat in the terminal.", "1. ollama.com → 2. ثبّت → 3. `ollama run llama3.2` → 4. تحدث في الطرفية."),
            "exemple": L("`ollama run qwen2.5:3b` → « résume ce texte en français : … » (voir séance 09, construire-ia).", "`ollama run qwen2.5:3b` → \"summarise this text in French: …\" (see session 9, build).", "`ollama run qwen2.5:3b` → « لخّص هذا النص بالفرنسية: … » (انظر الحصة 9 والبناء)."),
            "forces": L("Gratuit, hors-ligne, respect de la vie privée.", "Free, offline, privacy-friendly.", "مجاني، دون اتصال، يحترم الخصوصية."),
            "limites": L("Nécessite un PC correct ; modèles moins puissants que le cloud.", "Needs a decent PC; models less powerful than cloud.", "يتطلب جهازاً جيداً؛ نماذج أقل قوة من السحابة."),
        },
        {
            "emoji": "🔗",
            "nom": "Dify",
            "type": L("Plateforme no-code pour construire des IA", "No-code platform to build AIs", "منصة بدون كود لبناء ذكاءات اصطناعية"),
            "usage": L("Créer un chatbot qui répond à partir de vos PDF/notes, avec base de connaissances.", "Create a chatbot that answers from your PDFs/notes, with a knowledge base.", "بناء روبوت محادثة يجيب من ملفاتك وملاحظاتك، مع قاعدة معرفة."),
            "etapes": L("1. dify.ai → 2. Compte gratuit → 3. Créer une app → 4. « Knowledge » : importer un PDF → 5. Personnaliser le prompt → 6. Publier.", "1. dify.ai → 2. Free account → 3. Create an app → 4. \"Knowledge\": import a PDF → 5. Customise the prompt → 6. Publish.", "1. dify.ai → 2. حساب مجاني → 3. أنشئ تطبيقاً → 4. « المعرفة »: استورد PDF → 5. خصّص الصياغة → 6. انشر."),
            "exemple": L("Chatbot « SOS modules » qui répond aux questions des étudiants à partir de vos fiches de cours.", "A \"Module SOS\" chatbot that answers student questions from your course sheets.", "روبوت « إسعاف الوحدات » يجيب على أسئلة الطلبة انطلاقاً من بطاقاتك."),
            "forces": L("Sans code, résultats fiables basés sur vos documents.", "No-code, reliable answers based on your documents.", "بدون كود، نتائج موثوقة مبنية على وثائقك."),
            "limites": L("Courbe d'apprentissage ; moins gratuit que les essais locaux.", "Learning curve; less free than local experiments.", "منحنى تعليمي؛ أقل مجانية من التجارب المحلية."),
        },
    ]

    cards = []
    for o in outils:
        cards.append(f"""<article class="outil-card">
  <div class="outil-head"><span class="outil-emoji">{o['emoji']}</span><h3>{o['nom']}</h3></div>
  <div class="outil-body">
    <p><strong>🔖 <span class="lang-fr">Type</span><span class="lang-en">Type</span><span class="lang-ar">النوع</span> :</strong> {trija3(o['type'])}</p>
    <p><strong>🎯 <span class="lang-fr">À quoi ça sert</span><span class="lang-en">What it does</span><span class="lang-ar">ما فائدته</span> :</strong> {trija3(o['usage'])}</p>
    <p><strong>🪜 <span class="lang-fr">Comment l'utiliser</span><span class="lang-en">How to use it</span><span class="lang-ar">كيف تستعمله</span> :</strong> {trija3(o['etapes'])}</p>
    <p class="outil-exemple"><strong>✏️ <span class="lang-fr">Exemple étudiant PEP</span><span class="lang-en">PEP student example</span><span class="lang-ar">مثال طالبي</span> :</strong> {trija3(o['exemple'])}</p>
    <p><strong>💪 <span class="lang-fr">Forces</span><span class="lang-en">Strengths</span><span class="lang-ar">مزايا</span> :</strong> {trija3(o['forces'])}</p>
    <p><strong>⚠️ <span class="lang-fr">Limites</span><span class="lang-en">Limits</span><span class="lang-ar">حدود</span> :</strong> {trija3(o['limites'])}</p>
  </div>
</article>""")

    # liens séances pour chaque famille
    liaison = f"""<div class="highlight-box" style="margin:1.6rem 0;">
  <div class="highlight-icon">🧭</div>
  <div class="highlight-content">
    <h3 class="lang-fr">Où tester ces outils dans le module ?</h3>
    <h3 class="lang-en">Where to try these tools in the module?</h3>
    <h3 class="lang-ar">أين تجرّب هذه الأدوات في الوحدة؟</h3>
    <p class="lang-fr">🧾 Chercher/résumer : séances 03 et 04 · ✍️ Rédiger : séance 08 · 🎤 Exposé (Gamma/Canva) : séance 05 · 💻 Coder avec l'IA (mini-projet Python) : séance 07 · 🧠 Réviser (quiz/flashcards) : séance 06 · 🗂️ S'organiser (Notion) : séance 09 · 🛠️ Construire sa propre IA : <a href="construire-ia.html">construire-ia.html</a>.</p>
    <p class="lang-en">🧾 Search/summarise: sessions 03 and 04 · ✍️ Writing: session 08 · 🎤 Presentation (Gamma/Canva): session 05 · 💻 Coding with AI (Python mini-project): session 07 · 🧠 Revising (quiz/flashcards): session 06 · 🗂️ Organising (Notion): session 09 · 🛠️ Build your own AI: <a href="construire-ia.html">construire-ia.html</a>.</p>
    <p class="lang-ar">🧾 البحث/التلخيص: الحصتان 3 و4 · ✍️ الكتابة: الحصة 8 · 🎤 العرض: الحصة 5 · 💻 البرمجة مع الذكاء الاصطناعي (مشروع بايثون): الحصة 7 · 🧠 المراجعة: الحصة 6 · 🗂️ التنظيم: الحصة 9 · 🛠️ بناء الذكاء الخاص: <a href="construire-ia.html">construire-ia.html</a>.</p>
  </div>
</div>"""

    html = head_html(
        "Outils IA — Boîte à outils · Module IA en Éducation PEP 2A — Dr. Madani BELACEL",
        "Plus de 12 outils d'IA présentés pour un étudiant PEP 2A : type, usage, étapes simples, exemple concret, forces et limites.",
        canonical,
        prefix,
        json_ld,
    )
    html += f"""
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="{prefix}index.html">Accueil</a></li>
    <li><a href="{prefix}enseignement.html">Enseignement</a></li>
    <li><a href="index.html">IA en Éducation — PEP 2A</a></li>
    <li class="current">Outils IA</li>
  </ol>
</nav>
<main class="page-content"><div class="ia-page" style="max-width:1100px;margin:0 auto;padding:0 1.5rem;">
  <h1 style="font-family:var(--font-heading);color:var(--primary);margin:1.2rem 0 0.2rem;font-size:1.6rem;">🧰 <span class="lang-fr">Outils IA — boîte à outils</span><span class="lang-en">AI Tools — toolbox</span><span class="lang-ar">أدوات الذكاء الاصطناعي — صندوق الأدوات</span></h1>
  <p style="color:var(--text-muted);font-size:.95rem;">
    <span class="lang-fr">14 outils comparés — version gratuite d'abord, toujours vérifier la réponse, toujours garder le contrôle.</span>
    <span class="lang-en">14 compared tools — start with free versions, always check the answer, always keep control.</span>
    <span class="lang-ar">14 أداة مقارنة — ابدأ بالنسخة المجانية، تحقق دائماً من الإجابة، واحتفظ بالسيطرة.</span>
  </p>
  {lang_tabs()}
  {liaison}
  <div class="outil-grid">
{"".join(cards)}
  </div>
</div></main>
footer_placeholder"""""
    html = html.replace("footer_placeholder", footer_html(prefix))
    html += TABS_SCRIPT
    # CSS local
    extra_css = """
<style>
  .ia-page .lang-fr{display:none!important;}.ia-page .lang-ar{display:none!important;}
  .ia-page.lang-fr .lang-en{display:none!important;}.ia-page.lang-fr .lang-ar{display:none!important;}.ia-page.lang-fr .lang-fr{display:block!important;}
  .ia-page.lang-en .lang-fr{display:none!important;}.ia-page.lang-en .lang-ar{display:none!important;}.ia-page.lang-en .lang-en{display:block!important;}
  .ia-page.lang-ar .lang-fr{display:none!important;}.ia-page.lang-ar .lang-en{display:none!important;}.ia-page.lang-ar .lang-ar{display:block!important;direction:rtl;text-align:right;}
  .outil-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:1rem;margin:1.2rem 0;}
  .outil-card{border:1px solid var(--border);border-radius:var(--radius);background:var(--bg-card);overflow:hidden;display:flex;flex-direction:column;}
  .outil-head{display:flex;align-items:center;gap:.7rem;background:var(--bg-alt);padding:.7rem 1rem;border-bottom:1px solid var(--border);}
  .outil-head h3{margin:0;font-family:var(--font-heading);color:var(--primary);}
  .outil-emoji{font-size:1.7rem;}
  .outil-body{padding:.9rem 1rem;font-size:.9rem;flex:1;}
  .outil-body p{margin:.4rem 0;line-height:1.65;}
  .outil-exemple{background:var(--bg-alt);border-radius:var(--radius);padding:.55rem .7rem;}
  @media print{.ia-page.lang-fr .lang-en,.ia-page.lang-fr .lang-ar{display:block!important;}}
</style>"""
    html = html.replace("<main class=\"page-content\">", extra_css + "\n<main class=\"page-content\">")
    return html


# --------------------------------------------------------------------------
# Page « Construire son IA » (3 approches + projet séance 07)
# --------------------------------------------------------------------------
def render_construire_ia(seances):
    prefix = "../"
    canonical = f"{SITE}/ia-pep-2/construire-ia.html"
    json_ld = f"""{{
  "@context": "https://schema.org",
  "@type": "LearningResource",
  "name": "Construire son IA — 3 approches · Module IA PEP 2A",
  "url": "{canonical}",
  "author": {{ "@type": "Person", "name": "Dr. BELACEL Madani" }},
  "inLanguage": "fr"
}}"""
    code_py = """# assistant_chat.py -- mini assistant IA (projet séance 07)
# python -m pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key="COLLE_TA_CLE_ICI")  # keys for free at ai.google.dev
model = genai.GenerativeModel("gemini-2.0-flash")

print("Assistant IA pour étudiant (tape 'quit' pour sortir)")
while True:
    question = input("\\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    reponse = model.generate_content(question)
    print("IA   >", reponse.text)"""
    approches = [
        {
            "emoji": "🧩",
            "nom": L("1. No-code : Dify (chatbot sur vos PDF)", "1. No-code: Dify (chatbot on your PDFs)", "1. بدون كود: Dify (روبوت على ملفاتك)"),
            "difficulte": L("Facile — aucune ligne de code", "Easy — no code at all", "سهل — دون أي سطر برمجة"),
            "temps": L("± 45 min pour un premier chatbot", "About 45 min for a first chatbot", "حوالي 45 دقيقة لأول روبوت"),
            "prerequis": L("Compte gratuit dify.ai, un PDF de cours", "Free dify.ai account, a course PDF", "حساب مجاني dify.ai وملف درس PDF"),
            "usage": L("Importer ses fiches → poser des questions → publi. Idéal pour créer un « assistant-module » pour le groupe.", "Import your sheets → ask questions → publish. Ideal to build a \"module assistant\" for the class.", "استورد بطاقاتك → اطرح أسئلة → انشر. مثالي لإنشاء « مساعد وحدة » للمجموعة."),
            "exemple": L("« Réponds en français à partir de mes fiches de psycho seulement. »", "\"Answer in French using only my psychology sheets.\"", "« أجب بالفرنسية انطلاقاً من بطاقاتي في علم النفس فقط »"),
        },
        {
            "emoji": "🐍",
            "nom": L("2. Avec code : Python + API Gemini/OpenAI", "2. With code: Python + Gemini/OpenAI API", "2. بالكود: Python + واجهة Gemini/OpenAI"),
            "difficulte": L("Moyenne — notions de base en Python", "Medium — basic Python", "متوسطة — أساسيات بايثون"),
            "temps": L("± 1 h 30 (projet de la séance 07)", "About 1h30 (session 7 project)", "حوالي ساعة و30 دقيقة (مشروع الحصة 7)"),
            "prerequis": L("Python installé, clé API gratuite (ai.google.dev)", "Python installed, free API key (ai.google.dev)", "بايثون مثبّتة، مفتاح API مجاني (ai.google.dev)"),
            "usage": L("Un script qui dialogue avec un modèle d'IA, et qu'on peut modifier (historique, fonctions, sauvegarde).", "A script that chats with an AI model and can be modified (history, functions, saving).", "برنامج يحاور نموذج ذكاء اصطناعي ويمكن تعديله (تاريخ، وظائف، حفظ)."),
            "exemple": L("`python assistant_chat.py` puis taper ses questions de révision.", "`python assistant_chat.py` then type your revision questions.", "`python assistant_chat.py` ثم اكتب أسئلة مراجعتك."),
        },
        {
            "emoji": "🐋",
            "nom": L("3. Local : Ollama (open source hors-ligne)", "3. Local: Ollama (offline open source)", "3. محلياً: Ollama (مفتوح المصدر دون اتصال)"),
            "difficulte": L("Moyenne — installation en ligne de commande", "Medium — command-line installation", "متوسطة — ثبّت من سطر الأوامر"),
            "temps": L("± 30 min de mise en route", "About 30 min to start", "حوالي 30 دقيقة للانطلاق"),
            "prerequis": L("PC récent (8 Go RAM conseillés), ~4 Go libres", "Recent PC (8 GB RAM advised), ~4 GB free", "جهاز حديث (8 غيغا رام يُنصح بها)، ~4 غيغا فارغة"),
            "usage": L("`ollama run llama3.2` : un modèle entier chez soi, sans Internet, pour tester et bricoler.", "`ollama run llama3.2`: a whole model on your machine, offline, to test and tinker.", "`ollama run llama3.2`: نموذج كامل على جهازك، دون إنترنت، للتجريب."),
            "exemple": L("Consulter ce chatbot même en mode avion pendant la révision.", "Ask this chatbot even in airplane mode while revising.", "استشر هذا الروبوت حتى مع إيقاف الشبكة أثناء المراجعة."),
        },
    ]
    cards = []
    for a in approches:
        cards.append(f"""<article class="outil-card">
  <div class="outil-head"><span class="outil-emoji">{a['emoji']}</span><h3>{trija3(a['nom'])}</h3></div>
  <div class="outil-body">
    <p><strong>🌡️ <span class="lang-fr">Difficulté</span><span class="lang-en">Difficulty</span><span class="lang-ar">الصعوبة</span> :</strong> {trija3(a['difficulte'])} · <strong>⏱️ {trija3(a['temps'])}</strong></p>
    <p><strong>🎒 <span class="lang-fr">Prérequis</span><span class="lang-en">Prerequisites</span><span class="lang-ar">المتطلبات</span> :</strong> {trija3(a['prerequis'])}</p>
    <p class="outil-exemple"><strong>🪜 <span class="lang-fr">Usage type</span><span class="lang-en">Typical use</span><span class="lang-ar">استعمال نموذجي</span> :</strong> {trija3(a['usage'])}</p>
    <p><strong>✏️ {trija3(L("Exemple", "Example", "مثال"))} :</strong> {trija3(a['exemple'])}</p>
  </div>
</article>""")

    html = head_html(
        "Construire son IA — 3 approches · Module IA PEP 2A — Dr. Madani BELACEL",
        "Trois façons de construire une IA personnelle : no-code avec Dify, API Python avec Gemini/OpenAI, et local avec Ollama. Projet de la séance 07.",
        canonical,
        prefix,
        json_ld,
    )
    html += f"""
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="{prefix}index.html">Accueil</a></li>
    <li><a href="{prefix}enseignement.html">Enseignement</a></li>
    <li><a href="index.html">IA en Éducation — PEP 2A</a></li>
    <li class="current">Construire son IA</li>
  </ol>
</nav>
<main class="page-content"><div class="ia-page" style="max-width:1100px;margin:0 auto;padding:0 1.5rem;">
  <h1 style="font-family:var(--font-heading);color:var(--primary);margin:1.2rem 0 0.2rem;font-size:1.6rem;">🛠️ <span class="lang-fr">Construire sa propre IA</span><span class="lang-en">Build your own AI</span><span class="lang-ar">بناء ذكاء اصطناعي خاص بك</span></h1>
  <p style="color:var(--text-muted);font-size:.95rem;">
    <span class="lang-fr">Trois chemins possibles, du plus facile au plus « geek » : sans code, avec code, ou en local. La voie « code » est le projet de la <a href="seance-07/index.html">séance 07</a>.</span>
    <span class="lang-en">Three possible paths, from easiest to most \"geek\": no-code, with code, or locally. The \"code\" path is the <a href="seance-07/index.html">session 07</a> project.</span>
    <span class="lang-ar">ثلاثة مسارات، من الأسهل إلى الأكثر « تقنياً »: بدون كود، بالكود، أو محلياً. مسار « الكود » هو مشروع <a href="seance-07/index.html">الحصة السابعة</a>.</span>
  </p>
  {lang_tabs()}
  <div class="outil-grid">
{"".join(cards)}
  </div>
  <h2 style="font-family:var(--font-heading);color:var(--navy);margin:1.4rem 0 .5rem;font-size:1.3rem;">🐍 <span class="lang-fr">Le projet de la séance 07 : assistant Python qui interroge une IA</span><span class="lang-en">Session 07 project: a Python assistant calling an AI</span><span class="lang-ar">مشروع الحصة السابعة: مساعد بايثون يستدعي ذكاءً اصطناعياً</span></h2>
  <ol style="margin:.5rem 0 .5rem 1.4rem;line-height:1.8;">
    <li class="lang-fr">Obtenir une clé API gratuite sur <strong>ai.google.dev</strong> (Gemini) ou <strong>platform.openai.com</strong>.</li>
    <li class="lang-en">Get a free API key at <strong>ai.google.dev</strong> (Gemini) or <strong>platform.openai.com</strong>.</li>
    <li class="lang-ar">احصل على مفتاح API مجاني من <strong>ai.google.dev</strong> (Gemini) أو <strong>platform.openai.com</strong>.</li>
    <li class="lang-fr">Installer la bibliothèque : <code>python -m pip install google-generativeai</code>.</li>
    <li class="lang-en">Install the library: <code>python -m pip install google-generativeai</code>.</li>
    <li class="lang-ar">ثبّت المكتبة: <code>python -m pip install google-generativeai</code>.</li>
    <li class="lang-fr">Copier le script ci-dessous, coller la clé, exécuter : <code>python assistant_chat.py</code>.</li>
    <li class="lang-en">Copy the script below, paste your key, run: <code>python assistant_chat.py</code>.</li>
    <li class="lang-ar">انسخ البرنامج أدناه، والصق المفتاح، وشغّل: <code>python assistant_chat.py</code>.</li>
  </ol>
  <pre><code>{md_escape(code_py)}</code></pre>
  <div class="highlight-box" style="margin:1.6rem 0;">
    <div class="highlight-icon">🔒</div>
    <div class="highlight-content">
      <p class="lang-fr"><strong>Sécurité :</strong> ne partage jamais ta clé API, ne la mets jamais dans un devoir ou un dépôt public. Elle est comme un mot de passe.</p>
      <p class="lang-en"><strong>Security:</strong> never share your API key, never put it in an assignment or a public repository. Treat it like a password.</p>
      <p class="lang-ar"><strong>الأمان:</strong> لا تشارك مفتاحك أبداً، ولا تضعه في واجب أو مستودع عام. تعامل معه ككلمة مرور.</p>
    </div>
  </div>
</div></main>
footer_placeholder"""""
    html = html.replace("footer_placeholder", footer_html(prefix))
    html += TABS_SCRIPT
    extra_css = """
<style>
  .ia-page .lang-fr{display:none!important;}.ia-page .lang-ar{display:none!important;}
  .ia-page.lang-fr .lang-en{display:none!important;}.ia-page.lang-fr .lang-ar{display:none!important;}.ia-page.lang-fr .lang-fr{display:block!important;}
  .ia-page.lang-en .lang-fr{display:none!important;}.ia-page.lang-en .lang-ar{display:none!important;}.ia-page.lang-en .lang-en{display:block!important;}
  .ia-page.lang-ar .lang-fr{display:none!important;}.ia-page.lang-ar .lang-en{display:none!important;}.ia-page.lang-ar .lang-ar{display:block!important;direction:rtl;text-align:right;}
  .outil-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:1rem;margin:1.2rem 0;}
  .outil-card{border:1px solid var(--border);border-radius:var(--radius);background:var(--bg-card);overflow:hidden;}
  .outil-head{display:flex;align-items:center;gap:.7rem;background:var(--bg-alt);padding:.7rem 1rem;border-bottom:1px solid var(--border);}
  .outil-head h3{margin:0;font-family:var(--font-heading);color:var(--primary);font-size:1rem;}
  .outil-emoji{font-size:1.7rem;}
  .outil-body{padding:.9rem 1rem;font-size:.9rem;line-height:1.65;}
  .outil-body p{margin:.45rem 0;}
  .outil-exemple{background:var(--bg-alt);border-radius:var(--radius);padding:.55rem .7rem;}
  @media print{.ia-page.lang-fr .lang-en,.ia-page.lang-fr .lang-ar{display:block!important;}}
</style>"""
    html = html.replace("<main class=\"page-content\">", extra_css + "\n<main class=\"page-content\">")
    return html


# --------------------------------------------------------------------------
# Chargement + génération
# --------------------------------------------------------------------------
def load_seances(nums=None):
    seances = []
    files = sorted(DATA.glob("seance_*.py"))
    for f in files:
        num = int(f.stem.split("_")[-1])
        if nums and num not in nums:
            continue
        spec = importlib.util.spec_from_file_location(f"DYN_{f.stem}", f)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        seances.append((num, mod.SEANCE))
    seances.sort()
    return seances


def main():
    nums = None
    if "--seances" in sys.argv:
        i = sys.argv.index("--seances")
        nums = {int(x) for x in sys.argv[i + 1].split(",")}
    all_seances = load_seances()
    (BASE / "index.html").write_text(render_module_index(all_seances), encoding="utf-8")
    (BASE / "outils-ia.html").write_text(render_outils_ia(all_seances), encoding="utf-8")
    (BASE / "construire-ia.html").write_text(render_construire_ia(all_seances), encoding="utf-8")
    for num, s in [x for x in all_seances if nums is None or x[0] in nums]:
        seg = s["slug"]
        sdir = BASE / seg
        sdir.mkdir(parents=True, exist_ok=True)
        prefix = "../../"  # ia-pep-2/seance-XX/index.html → racine du site
        (sdir / "index.html").write_text(
            render_seance_html(s, prefix), encoding="utf-8"
        )
        (sdir / "cours-fr.md").write_text(md_for("fr", s), encoding="utf-8")
        (sdir / "cours-en.md").write_text(md_for("en", s), encoding="utf-8")
        (sdir / "cours-ar.md").write_text(md_for("ar", s), encoding="utf-8")
        (sdir / "fiche-synthese.md").write_text(fiche_synthese_md(s), encoding="utf-8")
        (sdir / "dialogues-fr.md").write_text(s["dialogues_fr"], encoding="utf-8")
        (sdir / "dialogues-en.md").write_text(s["dialogues_en"], encoding="utf-8")
        (sdir / "slides.md").write_text(slides_md(s), encoding="utf-8")
        if PPTX_OK:
            build_pptx(s, str(sdir / "presentation.pptx"))
        print(f"✓ séance {num:02d} générée ({seg})")
    print("Terminé.")


if __name__ == "__main__":
    main()