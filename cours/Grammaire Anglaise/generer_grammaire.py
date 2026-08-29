# -*- coding: utf-8 -*-
"""Générateur du site : قواعد اللغة الإنجليزية — English Grammar.
Lit data_levels_*.py et produit index.html + niveaux/Niveau_X.html
dans le même style que « dialogue anglais »."""

import os

from data_grammaire import LEVELS
from prononciation import ar_pron

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "niveaux")

STYLE_COMMON = """
<style>
:root {
  --bg: #f3f6f2;
  --bg-strong: #eaf2ec;
  --paper: #ffffff;
  --paper-soft: #f8fbf8;
  --line: #dfe9e1;
  --primary: #1f6b3a;
  --primary-dark: #143d29;
  --primary-soft: #e8f5e9;
  --text: #1d2a22;
  --muted: #5d6d63;
  --gold: #9a6500;
  --shadow: 0 18px 40px rgba(19, 42, 29, 0.08);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Segoe UI', Arial, sans-serif;
  max-width: 980px;
  margin: 0 auto;
  padding: 24px 18px 60px;
  background: radial-gradient(circle at top, #f8fbf9 0%, #f3f6f2 30%, #edf3ee 100%);
  color: var(--text);
  line-height: 1.75;
}
.content-shell {
  width: min(100%, 980px);
  margin: 0 auto;
}
.page-shell {
  background: rgba(255,255,255,0.7);
  border: 1px solid rgba(31,107,58,0.08);
  border-radius: 22px;
  padding: 18px 18px 26px;
  box-shadow: var(--shadow);
  backdrop-filter: blur(2px);
}
.sidebar {
  position: sticky; top: 18px;
  background: linear-gradient(180deg, #ffffff 0%, #f6faf7 100%);
  border: 1px solid var(--line);
  border-radius: 18px; padding: 16px 14px; box-shadow: 0 18px 26px rgba(17,35,25,0.08);
  margin: 0 0 18px;
}
.brand {
  display: flex; align-items: center; gap: 12px; margin-bottom: 16px; padding: 8px 8px 12px; border-bottom: 1px solid #eaeef0;
}
.brand-mark {
  width: 42px; height: 42px; display: grid; place-items: center; border-radius: 12px;
  background: linear-gradient(135deg, #144d2d 0%, #2f8b56 100%); color: #fff; font-size: 1.2rem;
  box-shadow: 0 10px 14px rgba(20,77,45,0.16);
}
.brand h3 { margin: 0; font-size: 1rem; color: var(--primary-dark); }
.brand small { color: var(--muted); }
.side-menu, .side-section { display: grid; gap: 8px; }
.side-section { margin-top: 14px; }
.side-section-title {
  font-size: 0.72em; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); font-weight: 700; padding: 0 8px;
}
.side-link {
  display: flex; align-items: center; justify-content: flex-start; gap: 8px;
  padding: 9px 12px; border-radius: 10px; font-size: 0.9em; color: var(--text); text-decoration: none;
  border: 1px solid transparent; transition: all 0.2s ease;
}
.side-link:hover, .side-link.active {
  background: linear-gradient(180deg, var(--primary-soft) 0%, #eaf7ee 100%);
  border-color: rgba(31,107,58,0.14);
  color: var(--primary-dark);
}
.side-link.disabled { opacity: 0.45; pointer-events: none; }
.topbar {
  display: flex; align-items: center; gap: 8px; flex-wrap: wrap; margin: 0 0 16px;
}
.btn {
  display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  background: linear-gradient(180deg, #1d653a 0%, #2b7b4a 100%); color: #fff; border-radius: 10px;
  padding: 8px 12px; text-decoration: none; font-size: 0.9em; font-weight: 600; box-shadow: 0 10px 16px rgba(31,107,58,0.16);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.btn:hover { transform: translateY(-1px); box-shadow: 0 12px 18px rgba(31,107,58,0.2); }
.btn.disabled { background: #dde5dd; color: #728077; box-shadow: none; pointer-events: none; }
.spacer { flex: 1; }
h1 {
  color: var(--primary-dark);
  border-bottom: 3px solid var(--primary);
  padding-bottom: 10px;
  font-size: clamp(1.5rem, 2.4vw, 2.1rem);
  margin-top: 8px;
  letter-spacing: -0.02em;
}
h2 { color: #1a3c22; }
img.flag-corner {
  position: fixed; top: 10px; right: 10px; z-index: 9999;
  width: 52px; height: auto; opacity: 0.9; pointer-events: none;
  border-radius: 8px; box-shadow: 0 6px 18px rgba(0,0,0,0.12);
}
.header-banner {
  display: flex; align-items: center; gap: 16px;
  background: linear-gradient(135deg, #164f2d 0%, #236a3f 55%, #2d7a49 100%);
  color: #fff; border-radius: 16px; padding: 16px 20px; margin: 18px 0 22px;
  box-shadow: 0 14px 26px rgba(20, 77, 45, 0.18);
}
.header-banner img.prof-photo {
  width: 90px; height: 90px; border-radius: 50%; border: 3px solid rgba(255,255,255,0.55);
  object-fit: cover; flex-shrink: 0; background: #fff;
}
.header-banner .hb-info h2 { margin: 0; font-size: 1.22rem; line-height: 1.3; }
.header-banner .hb-info h2 small {
  display: block; font-size: 0.82rem; opacity: 0.9; font-weight: normal; margin-top: 2px;
}
.header-banner .hb-info p { margin: 5px 0 0; font-size: 0.9em; opacity: 0.96; line-height: 1.5; }
.badge {
  display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.8em; font-weight: 700; color: #fff;
  margin-right: 6px; letter-spacing: 0.03em; box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
.badge.beginner { background: #4d9b43; }
.badge.elementary { background: #7ca442; }
.badge.intermediate { background: #d48a1d; }
.badge.upper { background: #d56b1c; }
.badge.advanced { background: #b94a31; }
.badge.proficiency { background: #882f2e; }
.badge.root { background: #5bb; }
.card {
  background: linear-gradient(180deg, #ffffff 0%, #f8fbf9 100%);
  border: 1px solid var(--line); border-radius: 16px; padding: 18px 18px 16px; margin: 18px 0;
  box-shadow: 0 10px 18px rgba(17, 32, 24, 0.04);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.card:hover { transform: translateY(-1px); box-shadow: 0 14px 22px rgba(17, 32, 24, 0.06); }
.card h3 { margin: 0 0 8px; color: var(--primary-dark); font-size: 1.08rem; }
.card .cat { font-size: 0.85em; margin: 2px 0 8px; }
.card .cat .en { font-weight: bold; color: var(--primary); }
.ar { font-family: 'Traditional Arabic', 'Amiri', 'Segoe UI', serif; direction: rtl; text-align: right; }
.expl { margin: 10px 0; }
.expl .ar { color: #1a3c22; font-size: 1.02em; margin-bottom: 4px; }
.expl .en { color: #3a4b3f; font-size: 0.97em; }
.formula {
  background: linear-gradient(180deg, #edf9ee 0%, #e5f4ea 100%); border-left: 4px solid var(--primary); border-radius: 10px;
  padding: 10px 12px; margin: 12px 0; font-family: 'Consolas', monospace; font-size: 0.94em; color: #173522;
}
.cat-label { color: #b45309; font-weight: bold; font-size: 0.82em; }
table.ex { border-collapse: collapse; width: 100%; margin-top: 10px; border-radius: 12px; overflow: hidden; }
table.ex th { background: linear-gradient(180deg, #1b653a 0%, #2b7d48 100%); color: #fff; text-align: left; padding: 9px 12px; }
table.ex td { padding: 10px 12px; border-bottom: 1px solid #ebefe9; background: #fff; }
table.ex td:first-child { width: 44%; }
table.ex .en-c { color: #0f3d24; }
table.ex .ar-c { font-family: 'Traditional Arabic', 'Amiri', serif; direction: rtl; text-align: right; color: #1a3c22; }
table.ex .pron-c { font-family: 'Traditional Arabic', 'Amiri', serif; direction: rtl; text-align: center; color: var(--gold); font-size: 0.95em; }
.idea-num {
  display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #123f29 0%, #2c7d4d 100%);
  color: #fff; border-radius: 50%; width: 28px; height: 28px; line-height: 28px; font-size: 0.85em; margin-right: 8px;
  box-shadow: 0 8px 16px rgba(20,61,41,0.18);
}
.meta {
  background: linear-gradient(180deg, #ecf6ee 0%, #e5f1e8 100%); border: 1px solid #cfe0d3; border-radius: 12px;
  padding: 12px 14px; margin: 16px 0; color: #1a3c22; font-size: 0.96em; box-shadow: 0 4px 10px rgba(28, 76, 48, 0.04);
}
.summary-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 12px; margin: 16px 0 18px;
}
.summary-card {
  background: linear-gradient(180deg, #f9fcfa 0%, #eef6f0 100%); border: 1px solid #dfe9df; border-radius: 12px; padding: 12px 14px;
  box-shadow: 0 4px 10px rgba(26, 60, 34, 0.04);
}
.summary-card .label { display: block; font-size: 0.74em; text-transform: uppercase; letter-spacing: 0.08em; color: #5d6e63; margin-bottom: 6px; }
.summary-card .value { font-size: 1.15rem; font-weight: 700; color: #1a3c22; }
.toc {
  background: #ffffff; border: 1px solid #e0e9e1; border-radius: 14px; padding: 12px 14px; margin: 14px 0 18px; box-shadow: 0 8px 14px rgba(19,42,29,0.03);
}
.toc h3 { margin: 0 0 10px; color: var(--primary-dark); font-size: 1rem; }
.toc-list { display: flex; flex-wrap: wrap; gap: 8px; }
.toc-list a {
  display: inline-block; padding: 6px 10px; border-radius: 999px; background: #edf5f0; color: #1c5a39; text-decoration: none; font-size: 0.85em; border: 1px solid #d9e8dc; transition: all 0.2s ease;
}
.toc-list a:hover { background: #e2f0e7; transform: translateY(-1px); }
.story-box {
  border-left: 4px solid #2c6e49; background: linear-gradient(180deg, #eef7f1 0%, #e7f3eb 100%); border-radius: 10px; padding: 12px 14px; margin: 12px 0;
  color: #1d2a22; box-shadow: inset 0 1px 0 rgba(255,255,255,0.5);
}
a.back { display: inline-block; margin: 6px 0 10px; padding: 6px 14px; border-radius: 5px; background: var(--primary); color: #fff; text-decoration: none; font-size: 0.9em; }
@media (max-width: 700px) {
  body { padding: 16px 12px 42px; }
  .header-banner { flex-direction: column; align-items: flex-start; }
  .header-banner img.prof-photo { width: 72px; height: 72px; }
  img.flag-corner { width: 36px; top: 8px; right: 8px; }
  .card { padding: 14px 12px; }
  table.ex, table.ex thead, table.ex tbody, table.ex th, table.ex td, table.ex tr { display: block; width: 100%; }
  table.ex th { display: none; }
  table.ex tr { margin-bottom: 10px; border: 1px solid #edf1ed; border-radius: 8px; overflow: hidden; }
  table.ex td { border-bottom: 1px solid #edf1ed; }
}
</style>
"""


def banner():
    return """<div class="header-banner">
<img class="prof-photo" src="../photo-profil.png" alt="Dr. BELACEL Madani">
<div class="hb-info">
<h2>Dr. BELACEL Madani <small>Maître de Conférences B (MCB)</small></h2>
<p>Université de Mostaganem — Faculté des langues étrangères · Département de français<br>madani.belacel@gmail.com</p>
</div>
</div>
"""


def cefr_class(cefr):
    c = cefr.upper()
    if c.startswith("A1"):
        return "beginner"
    if c.startswith("A2"):
        return "elementary"
    if c.startswith("B1"):
        return "intermediate"
    if c.startswith("B2"):
        return "upper"
    if c.startswith("C1"):
        return "advanced"
    return "proficiency"


def format_arabic_explanation(text):
    if not text:
        return ""
    text = text.replace(chr(10), " ").replace(chr(13), " ")
    text = " ".join(text.split())
    text = text.replace("،", ",").replace("؛", ";").replace("…", ".")

    parts = []
    current = []
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            if depth > 0:
                depth -= 1

        current.append(ch)

        if depth == 0 and ch in ",;.!?":
            segment = "".join(current).strip()
            if segment:
                parts.append(segment)
            current = []

    if current:
        segment = "".join(current).strip()
        if segment:
            parts.append(segment)

    cleaned = []
    for part in parts:
        part = part.strip()
        if part:
            cleaned.append(part)

    return "<br>".join(cleaned) if cleaned else ""


def render_level(lvl):
    n = lvl["num"]
    ideas = lvl["ideas"]
    cefr = lvl.get("cefr", "A1")
    title_en = lvl["title_en"]
    title_ar = lvl["title_ar"]
    cat = lvl.get("category", "")
    cat_ar = lvl.get("category_ar", "")
    prev = f'<a class="btn" href="Niveau%20{n-1}.html">◀ السابق</a>' if n > 1 else '<a class="btn disabled">◀ السابق</a>'
    nxt = f'<a class="btn" href="Niveau%20{n+1}.html">التالي ▶</a>' if n < len(LEVELS) else '<a class="btn disabled">التالي ▶</a>'

    cards = []
    toc_links = []
    for i, idea in enumerate(ideas, 1):
        def ex_row(row):
            en, ar = row[0], row[1]
            pron = row[2] if len(row) > 2 and row[2].strip() else ar_pron(en)
            return (f'<tr>'
                    f'<td class="en-c">{en}</td>'
                    f'<td class="ar-c">{ar}</td>'
                    f'<td class="pron-c">«{pron}»</td>'
                    f'</tr>')
        ex_rows = "".join(ex_row(row) for row in idea.get("examples", []))
        ex_html = ""
        if idea.get("examples"):
            ex_html = f'<table class="ex"><tr><th>English</th><th>العربية</th><th>النُّطق «...»</th></tr>{ex_rows}</table>'
        formula = ""
        if idea.get("formula"):
            formula = f'<div class="formula">{idea["formula"]}</div>'
        anchor = f"idea-{i}"
        toc_links.append(f'<a href="#{anchor}">{i}. {idea["en"]}</a>')
        cards.append(f"""
<div class="card" id="{anchor}">
<h3><span class="idea-num">{i}</span>{idea["en"]} — <span class="ar">{idea["ar"]}</span></h3>
<div class="expl">
<div class="ar">📘 {format_arabic_explanation(idea.get("expl_ar", ""))}</div>
<div class="en">📗 Explication claire : {idea.get("expl_en", "").replace(chr(10), "<br>")}</div>
</div>
{formula}
{ex_html}
</div>""")

    ideas_content = "\n".join(cards)
    badge = f'<span class="badge {cefr_class(cefr)}">{cefr}</span>'
    catline = f'<span class="cat-label">{cat}</span>'
    if cat_ar:
        catline += f' <span class="ar">— {cat_ar}</span>'

    groups = []
    for start in range(1, len(LEVELS) + 1, 10):
        end = min(start + 9, len(LEVELS))
        groups.append(f'<a class="side-link" href="Niveau%20{start}.html">Niveaux {start}-{end}</a>')

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>قواعد اللغة الإنجليزية — Niveau {n}</title>
{STYLE_COMMON}
</head>
<body>
<div class="sidebar">
  <div class="brand">
    <div class="brand-mark">📘</div>
    <div>
      <h3>English Grammar</h3>
      <small>Grammaire / niveaux</small>
    </div>
  </div>
  <nav class="side-menu">
    <a class="side-link active" href="../index.html">🏠 Accueil</a>
    <a class="side-link" href="../index.html#catalogue">📚 Catalogue</a>
    {prev.replace('class="btn"', 'class="side-link"').replace('class="btn disabled"', 'class="side-link disabled"')}
    {nxt.replace('class="btn"', 'class="side-link"').replace('class="btn disabled"', 'class="side-link disabled"')}
  </nav>
  <div class="side-section">
    <div class="side-section-title">Sujets</div>
    {''.join(groups)}
  </div>
</div>
<div class="content-shell">
  <div class="page-shell">
    <div class="topbar">
      <a class="btn" href="../index.html">🏠 الرئيسية</a>
      {prev}
      <span class="spacer"></span>
      {nxt}
    </div>
    <h1>📖 مستوى {n} — {title_en}</h1>
    <div class="ar" style="color:#dfeee9;font-size:1.1rem;">{title_ar}</div>
    {banner()}
    <div class="summary-grid">
      <div class="summary-card"><span class="label">CEFR</span><span class="value">{badge}</span></div>
      <div class="summary-card"><span class="label">القواعد</span><span class="value">{len(ideas)}</span></div>
      <div class="summary-card"><span class="label">الفئة</span><span class="value">{cat if cat else 'General'}</span></div>
      <div class="summary-card"><span class="label">الترتيب</span><span class="value">Niveau {n}</span></div>
    </div>
    <div class="meta">
    <b>{badge} {catline}</b><br>
    <div class="en">Ce niveau propose <b>{len(ideas)}</b> points de grammaire à maîtriser.</div>
    <div class="ar">يحتوي هذا المستوى على <b>{len(ideas)}</b> نقطة لغوية أساسية للتدريب والتطبيق.</div>
    </div>
    <div class="toc">
      <h3>Sommaire rapide</h3>
      <div class="toc-list">{''.join(toc_links)}</div>
    </div>
    <div class="story-box">
      <strong>Objectif du niveau :</strong> maîtriser les bases de ce thème pour les utiliser naturellement dans des phrases simples, claires et correctes.
    </div>
    {ideas_content}
    <div class="topbar" style="margin-top:24px;">
      {prev}
      <span class="spacer"></span>
      <a class="btn" href="../index.html">🏠 الرجوع إلى الفهرس</a>
      <span class="spacer"></span>
      {nxt}
    </div>
  </div>
</div>
<img src="../alg_drap.gif" alt="Algérie" class="flag-corner">
</body>
</html>"""
    return html


def render_index():
    rows = []
    n = len(LEVELS)
    total_levels = len(LEVELS)
    cefr_found = sorted({l.get("cefr", "A1") for l in LEVELS})
    cefr_txt = " → ".join(cefr_found) if cefr_found else ""
    for lvl in LEVELS:
        cls = cefr_class(lvl.get("cefr", "A1"))
        rows.append(
            f"""<tr>
<td class="num">{lvl['num']}</td>
<td><span class="badge {cls}">{lvl.get('cefr','A1')}</span></td>
<td class="nm">{lvl['title_en']}</td>
<td class="ar t">{lvl['title_ar']}</td>
<td>{len(lvl['ideas'])}</td>
<td class="links"><a href="niveaux/Niveau%20{lvl['num']}.html">فتح الصفحة</a></td>
</tr>"""
        )
    style = """
<style>
:root {
  --bg: #f5f7f4;
  --paper: #ffffff;
  --paper-soft: #edf7f0;
  --line: #e0e7df;
  --primary: #1d683d;
  --primary-dark: #124d2d;
  --primary-soft: #dfeee2;
  --text: #1f2b23;
  --muted: #5e6d65;
  --shadow: 0 14px 32px rgba(24, 52, 34, 0.08);
}
* { box-sizing: border-box; }
body {
  font-family: 'Segoe UI', Arial, sans-serif; max-width: 1200px; margin: 0 auto; padding: 24px 18px 60px;
  background: radial-gradient(circle at top, #f9fcfa 0%, #f4f6f3 18%, #edf3ee 100%); color: var(--text);
}
h1 { color: var(--primary-dark); border-bottom: 3px solid var(--primary); padding-bottom: 10px; }
p.desc { color: var(--muted); }
.table-wrap {
  background: rgba(255,255,255,0.9); border-radius: 16px; overflow: hidden; box-shadow: 0 12px 28px rgba(19,42,29,0.06);
  border: 1px solid var(--line);
}
.table-tools {
  display: flex; justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap;
  margin: 18px 0 12px; padding: 12px 14px; background: rgba(29,104,61,0.06); border-radius: 12px; border: 1px solid rgba(29,104,61,0.08);
}
.table-tools .search-box {
  flex: 1 1 260px; max-width: 420px; display: flex; align-items: center; gap: 8px; background: #fff; border: 1px solid var(--line);
  border-radius: 10px; padding: 8px 12px; box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
}
.table-tools input {
  border: 0; background: transparent; width: 100%; outline: none; font-size: 0.96em; color: var(--text);
}
.table-tools .stats {
  color: var(--muted); font-size: 0.92em; font-weight: 600;
}
table { width: 100%; border-collapse: collapse; background: #fff; }
th {
  background: linear-gradient(180deg, #1b653a 0%, #2a804d 100%); color: #fff; text-align: left; padding: 12px 14px; }
td { padding: 12px 14px; border-bottom: 1px solid var(--line); vertical-align: middle; }
tr:hover td { background: #f1f8f3; }
.num { width: 52px; color: #7a807b; font-weight: bold; }
.nm { font-weight: bold; }
.links { white-space: nowrap; }
.links a {
  display: inline-block; padding: 7px 12px; border-radius: 8px; text-decoration: none; font-size: 0.9em; background: var(--primary); color: #fff; font-weight: 600;
  box-shadow: 0 6px 12px rgba(29,104,61,0.18); transition: transform 0.2s ease, background 0.2s ease;
}
.links a:hover { transform: translateY(-1px); background: var(--primary-dark); }
.ar { font-family: 'Traditional Arabic', 'Amiri', 'Segoe UI', serif; }
.ar.t { direction: rtl; text-align: right; color: #1a3c22; }
img.flag-corner {
  position: fixed; top: 8px; right: 8px; z-index: 9999; width: 48px; height: auto; opacity: 0.9; pointer-events: none;
}
.header-banner {
  display: flex; align-items: center; gap: 16px; background: linear-gradient(135deg, #1a5c33 0%, #2c6e49 60%, #3f8a5f 100%);
  color: #fff; border-radius: 14px; padding: 16px 20px; margin: 14px 0 18px; box-shadow: 0 8px 18px rgba(0,0,0,0.12);
}
.header-banner img.prof-photo { width: 96px; height: 96px; border-radius: 50%; border: 3px solid rgba(255,255,255,0.5); object-fit: cover; flex-shrink: 0; }
.header-banner .hb-info h2 { margin: 0; font-size: 1.25rem; line-height: 1.3; }
.header-banner .hb-info h2 small { display: block; font-size: 0.85rem; opacity: 0.85; font-weight: normal; margin-top: 2px; }
.header-banner .hb-info p { margin: 4px 0 0; font-size: 0.9em; opacity: 0.92; line-height: 1.45; }
.badge { display: inline-block; padding: 4px 12px; border-radius: 999px; font-size: 0.8em; font-weight: 700; color: #fff; }
.badge.beginner { background: #4c9c3a; }
.badge.elementary { background: #7a9c3a; }
.badge.intermediate { background: #c98a2c; }
.badge.upper { background: #c96a2c; }
.badge.advanced { background: #b5482c; }
.badge.proficiency { background: #8d2f2f; }
.legend { margin: 14px 0 0; font-size: 0.9em; color: #555; display: flex; gap: 8px; flex-wrap: wrap; align-items: center; }
.legend .badge { font-size: 0.76em; }
.summary-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; margin: 18px 0 20px;
}
.summary-card {
  background: linear-gradient(180deg, #f9fcfa 0%, #eef6f0 100%); border: 1px solid #dfe9df; border-radius: 12px; padding: 12px 14px;
  box-shadow: 0 4px 10px rgba(26, 60, 34, 0.04);
}
.summary-card .label { display: block; font-size: 0.72em; text-transform: uppercase; letter-spacing: 0.06em; color: #5d6e63; margin-bottom: 5px; }
.summary-card .value { font-size: 1.05rem; font-weight: 700; color: #1a3c22; }
.hidden-row { display: none; }
.empty-state {
  padding: 18px; text-align: center; color: var(--muted); background: #f7faf8; border-top: 1px solid var(--line);
}
@media (max-width: 720px) {
  body { padding: 16px 10px 36px; }
  .header-banner { flex-direction: column; align-items: flex-start; }
  .header-banner img.prof-photo { width: 72px; height: 72px; }
  .table-tools { display: block; }
  .table-tools .search-box { max-width: none; margin-bottom: 10px; }
  table { display: block; overflow-x: auto; }
}
</style>
"""
    summary_cards = f"""
<div class="summary-grid">
  <div class="summary-card"><span class="label">Total</span><span class="value">{n}</span></div>
  <div class="summary-card"><span class="label">Idées</span><span class="value">{sum(len(l['ideas']) for l in LEVELS)}</span></div>
  <div class="summary-card"><span class="label">Progression</span><span class="value">A1 → {cefr_txt.split(' → ')[-1] if ' → ' in cefr_txt else cefr_txt}</span></div>
  <div class="summary-card"><span class="label">Format</span><span class="value">100% HTML</span></div>
</div>
"""
    sidebar_links = []
    for start in range(1, len(LEVELS) + 1, 10):
        end = min(start + 9, len(LEVELS))
        sidebar_links.append(f'<a class="side-link" href="niveaux/Niveau%20{start}.html">Niveaux {start}-{end}</a>')

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#0f1720">
<title>قواعد اللغة الإنجليزية — Fiches de grammaire</title>
{style}
</head>
<body>
<div class="sidebar">
  <div class="brand">
    <div class="brand-mark">📘</div>
    <div>
      <h3>English Grammar</h3>
      <small>Fiches de grammaire</small>
    </div>
  </div>
  <nav class="side-menu">
    <a class="side-link active" href="#">🏠 Accueil</a>
    <a class="side-link" href="#catalogue">📚 Catalogue</a>
    <a class="side-link" href="niveaux/Niveau%201.html">▶ Niveau 1</a>
    <a class="side-link" href="niveaux/Niveau%2010.html">▶ Niveau 10</a>
    <a class="side-link" href="niveaux/Niveau%2020.html">▶ Niveau 20</a>
  </nav>
  <div class="side-section">
    <div class="side-section-title">Groupes</div>
    {''.join(sidebar_links)}
  </div>
</div>
<div class="content-shell">
  <div class="page-shell">
    <img src="alg_drap.gif" alt="Algérie" class="flag-corner">
    <h1>📚 قواعد اللغة الإنجليزية — English Grammar</h1>
    <div class="header-banner">
      <img class="prof-photo" src="photo-profil.png" alt="Dr. BELACEL Madani">
      <div class="hb-info">
        <h2>Dr. BELACEL Madani <small>Maître de Conférences B (MCB)</small></h2>
        <p>Université de Mostaganem — Faculté des langues étrangères · Département de français<br>madani.belacel@gmail.com</p>
      </div>
    </div>
    <p class="desc">{n} مستوى من <b>المبتدئ (A1)</b> إلى <b>{cefr_txt}</b>. كل مستوى يحتوي على قواعد مفسّرة بالعربية وبالإنجليزية البسيطة، مع أمثلة مترجمة مع النُّطق.</p>
    <p class="desc">Chaque niveau contient des règles expliquées en arabe et en anglais simple, avec des exemples traduits et leur prononciation.</p>
    {summary_cards}
    <div class="table-tools">
      <label class="search-box" for="level-search" aria-label="Rechercher un niveau">
        <span>🔎</span>
        <input id="level-search" type="search" placeholder="Rechercher un niveau, un thème ou un niveau CEFR...">
      </label>
      <div class="stats" id="level-stats">{n} niveaux disponibles</div>
    </div>
    <div id="catalogue" class="table-wrap">
      <table>
        <tr><th>المستوى</th><th>المستوى الأوروبي</th><th>القاعدة (English)</th><th>العنوان بالعربية</th><th>القواعد</th><th>الوصول</th></tr>
        {''.join(rows)}
      </table>
      <div class="empty-state hidden-row" id="empty-state">Aucun niveau ne correspond à votre recherche.</div>
    </div>
    <div class="legend">
      <span>مفتاح المستويات:</span>
      <span class="badge beginner">A1 مبتدئ</span>
      <span class="badge elementary">A2 ابتدائي</span>
      <span class="badge intermediate">B1 متوسط</span>
      <span class="badge upper">B2 فوق المتوسط</span>
      <span class="badge advanced">C1 متقدم</span>
      <span class="badge proficiency">C2 أستاذية</span>
    </div>
  </div>
</div>
<script>
  const searchInput = document.getElementById('level-search');
  const rows = Array.from(document.querySelectorAll('table tr')).filter((row) => !row.querySelector('th'));
  const emptyState = document.getElementById('empty-state');
  const stats = document.getElementById('level-stats');

  function filterLevels() {{
    const query = searchInput.value.trim().toLowerCase();
    let visible = 0;
    rows.forEach((row) => {{
      const text = row.textContent.toLowerCase();
      const matches = !query || text.includes(query);
      row.classList.toggle('hidden-row', !matches);
      if (matches) visible += 1;
    }});
    emptyState.classList.toggle('hidden-row', visible !== 0);
    stats.textContent = visible + ' niveau(s) visible(s)';
  }}

  if (searchInput) {{
    searchInput.addEventListener('input', filterLevels);
    filterLevels();
  }}
</script>
</body>
</html>"""
    return html


def main():
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    for lvl in LEVELS:
        page = render_level(lvl)
        path = os.path.join(OUT, f"Niveau {lvl['num']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        print(f"Niveau {lvl['num']} : {len(lvl['ideas'])} idées → {path}")
    print(f"Total : {len(LEVELS)} niveaux générés.")

    import re
    total_ideas = sum(len(l["ideas"]) for l in LEVELS)
    print(f"Total idées : {total_ideas}")


if __name__ == "__main__":
    main()