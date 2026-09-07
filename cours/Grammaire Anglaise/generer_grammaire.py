# -*- coding: utf-8 -*-
"""Générateur du site : قواعد اللغة الإنجليزية — English Grammar.
Lit data_levels_*.py et produit index.html + niveaux/Niveau_X.html
dans le même style que « dialogue anglais »."""

import asyncio
import os

from data_grammaire import LEVELS
from prononciation import ar_pron

import edge_tts

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "niveaux")
AUDIO_DIR = os.path.join(OUT, "_audio_niveaux")
AUDIO_VOICE = "en-GB-SoniaNeural"

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
.pron-table-wrap { overflow-x: auto; margin: 18px 0; border: 1px solid var(--line); border-radius: 14px; box-shadow: 0 10px 18px rgba(17, 32, 24, 0.06); background: #fff; }
table.pron { border-collapse: collapse; width: 100%; font-size: 0.92em; table-layout: auto; }
table.pron th { background: linear-gradient(180deg, #1b653a 0%, #2b7d48 100%); color: #fff; padding: 10px 12px; }
table.pron td { padding: 9px 12px; border-bottom: 1px solid #ebefe9; vertical-align: top; }
table.pron tr:nth-child(even) td { background: #f7faf8; }
table.pron td.num { width: 40px; text-align: center; color: #7a807b; font-weight: bold; white-space: nowrap; }
table.pron td.ar { font-family: 'Traditional Arabic', 'Amiri', serif; direction: rtl; text-align: right; color: #1a3c22; overflow-wrap: anywhere; }
table.pron td.en { color: #0f3d24; overflow-wrap: anywhere; }
table.pron tr.sec td { background: linear-gradient(180deg, #164f2d 0%, #2a6e45 100%); color: #fff; font-weight: 700; font-family: 'Traditional Arabic', 'Amiri', serif; direction: rtl; text-align: right; padding: 10px 12px; letter-spacing: 0.02em; }
table.pron tr.note td { background: linear-gradient(180deg, #fff8e7 0%, #fdf0d0 100%); color: #5a3e00; border-top: 2px solid #e8c169; border-bottom: 1px solid #ead9a8; font-family: 'Traditional Arabic', 'Amiri', serif; direction: rtl; text-align: right; padding: 12px 14px; font-size: 0.95em; line-height: 1.75; }
table.pron tr.note td b { color: #8a5a00; }
table.pron td.audio-cell, table.pron td.audio-cell { width: 44px; text-align: center; white-space: nowrap; padding: 9px 6px; }
table.pron th:last-child { white-space: normal; }
.idea-num {
  display: inline-flex; align-items: center; justify-content: center; background: linear-gradient(135deg, #123f29 0%, #2c7d4d 100%);
  color: #fff; border-radius: 50%; width: 28px; height: 28px; line-height: 28px; font-size: 0.85em; margin-right: 8px;
  box-shadow: 0 8px 16px rgba(20,61,41,0.18);
}
td.audio-cell { text-align: center; }
button.say {
  background: linear-gradient(135deg, #123f29 0%, #2c7d4d 100%); color: #fff; border: none; cursor: pointer;
  width: 30px; height: 30px; border-radius: 50%; font-size: 0.8rem; line-height: 1;
  box-shadow: 0 6px 12px rgba(20,61,41,0.22); transition: transform .15s ease, box-shadow .15s ease;
}
button.say:hover { transform: translateY(-1px) scale(1.06); box-shadow: 0 10px 16px rgba(20,61,41,0.28); }
button.say:active { transform: translateY(0) scale(0.97); }
.player-bar {
  display: flex; align-items: center; gap: 12px; flex-wrap: wrap; background: linear-gradient(180deg, #ecf6ee 0%, #e5f1e8 100%);
  border: 1px solid #cfe0d3; border-radius: 12px; padding: 10px 14px; margin: 14px 0;
}
.player-bar .now-playing { font-size: .92em; color: #1a3c22; font-weight: 600; }
.btn.stop { background: linear-gradient(180deg, #b33f2c 0%, #c95a45 100%); padding: 6px 12px; font-size: .85em; }
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

# Pages au format tableau (niveaux de prononciation 101-110) :
# élargit la feuille pour que les colonnes respirent.
STYLE_TABLE_WIDTH = """
<style>
body { max-width: 1600px; }
.content-shell { width: min(100%, 1600px); }
table.pron th, table.pron td { padding: 10px 14px; }
table.pron { font-size: 0.95em; }
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


def table_rule_count(rows):
    return sum(1 for r in rows if r and r[0] not in ("SECTION", "NOTE"))


def _audio_player_bar():
    return """<div class="player-bar">
<audio id="gram-audio" preload="none"></audio>
<button class="btn stop" id="gram-stop" onclick="stopAudio()">⏹ إيقاف</button>
<span id="gram-now-playing" class="now-playing"></span>
</div>"""


def _audio_player_script():
    return """
<script>
const gramAudio = document.getElementById('gram-audio');
const nowPlaying = document.getElementById('gram-now-playing');
function playAudio(btn){
  gramAudio.src = btn.dataset.src;
  gramAudio.play();
  nowPlaying.textContent = '🔊 ' + (btn.dataset.label || '');
}
function stopAudio(){ gramAudio.pause(); gramAudio.currentTime = 0; nowPlaying.textContent=''; }
document.querySelectorAll('.say').forEach(btn=>{
  btn.addEventListener('click', ()=>playAudio(btn));
});
gramAudio.addEventListener('ended', ()=>{ nowPlaying.textContent=''; });
</script>
"""


def _audio_clean(text):
    if isinstance(text, str):
        text = text.replace("→", ", ").replace("←", ", ")
        text = text.replace("؛", ", ").replace("،", ", ")
        text = " ".join(text.split())
    return text


def _audio_fname(text):
    import hashlib
    h = hashlib.sha1(text.strip().encode("utf-8")).hexdigest()[:12]
    return f"{h}.mp3"


def ensure_audio_files(levels):
    """Génère les MP3 manquants (prononciation anglaise des exemples)."""
    os.makedirs(AUDIO_DIR, exist_ok=True)

    def _schedule(text):
        text = _audio_clean(text)
        if not text:
            return
        fname = _audio_fname(text)
        path = os.path.join(AUDIO_DIR, fname)
        if not os.path.exists(path):
            tasks.append((text, path))

    tasks = []
    for lvl in levels:
        if lvl.get("layout") == "table":
            col = lvl.get("audio_col")
            build = lvl.get("audio_build")
            if col is None and build is None:
                continue
            for row in lvl.get("table_rows", []):
                if row and row[0] in ("SECTION", "NOTE"):
                    continue
                if build:
                    _schedule(build(row))
                elif col is not None and col < len(row):
                    text = _audio_clean(row[col])
                    pcol = lvl.get("audio_prefix_col")
                    if pcol is not None and pcol < len(row):
                        text = f"{_audio_clean(row[pcol])}. {text}"
                    _schedule(text)
        else:
            # niveaux classiques (1-100) : une piste MP3 par phrase d'exemple anglaise
            for idea in lvl.get("ideas", []):
                for row in (idea.get("examples") or []):
                    if len(row) and row[0]:
                        _schedule(row[0])
            # extra_tables : exemples prononciation des tableaux fusionnés (ex. alphabet 102)
            for tbl in (lvl.get("extra_tables") or []):
                col = tbl.get("audio_col")
                for row in tbl.get("table_rows", []):
                    if row and row[0] in ("SECTION", "NOTE"):
                        continue
                    if col is None or col >= len(row):
                        continue
                    text = _audio_clean(row[col])
                    pcol = tbl.get("audio_prefix_col")
                    if text and pcol is not None and pcol < len(row):
                        text = f"{_audio_clean(row[pcol])}. {text}"
                    _schedule(text)
    print(f"Audio : {len(tasks)} MP3 manquants à générer.")
    if not tasks:
        return

    async def worker(text, path):
        com = edge_tts.Communicate(text, voice=AUDIO_VOICE, rate="-8%")
        try:
            await com.save(path)
            print("  audio ✓", text[:50])
        except Exception as e:  # noqa: BLE001
            print("  audio ✗", text[:50], "→", e)

    async def _run():
        await asyncio.gather(*(worker(t, p) for t, p in tasks))

    asyncio.run(_run())


def render_table(lvl):
    """Rendu d'un niveau au format tableau (prononciation : الأصوات المركبة ...)."""
    columns = lvl["table_columns"]
    rows = lvl["table_rows"]
    audio_col = lvl.get("audio_col")  # colonne dont le texte est lu à voix haute
    audio_build = lvl.get("audio_build")  # fonction custom pour générer le texte audio
    has_audio = audio_col is not None or audio_build is not None
    colspan = len(columns) + (1 if has_audio else 0) + 1

    thead = "".join(f"<th>{c}</th>" for c in columns)
    if has_audio:
        thead += '<th title="استمع إلى النطق">🔊</th>'
    tbody = ""
    counter = 0
    for row in rows:
        if row and row[0] == "SECTION":
            tbody += f'<tr class="sec"><td colspan="{colspan}" class="sec">{row[1]}</td></tr>'
            continue
        if row and row[0] == "NOTE":
            note_text = row[1].replace("\n", "<br>")
            tbody += f'<tr class="note"><td colspan="{colspan}" class="note">{note_text}</td></tr>'
            continue
        counter += 1
        tds = "".join(
            f'<td class="{"en" if j in (0, 2) else "ar"}">{c}</td>'
            for j, c in enumerate(row)
        )
        if has_audio:
            if audio_build:
                atext = _audio_clean(audio_build(row))
            elif audio_col is not None and audio_col < len(row):
                atext = _audio_clean(row[audio_col])
                if lvl.get("audio_prefix_col") is not None and lvl.get("audio_prefix_col") < len(row):
                    atext = f"{_audio_clean(row[lvl.get('audio_prefix_col')])}. {atext}"
            else:
                atext = ""
            if atext:
                fname = _audio_fname(atext)
                tds += f'<td class="audio-cell"><button class="say" data-src="_audio_niveaux/{fname}" data-label="{row[0]}" title="استمع إلى النطق" aria-label="استمع">▶</button></td>'
            else:
                tds += '<td class="audio-cell"></td>'
        else:
            tds += '<td class="audio-cell"></td>'
        tbody += f'<tr><td class="num">{counter}</td>{tds}</tr>'

    audio_script = ""
    if has_audio:
        audio_script = _audio_player_bar() + _audio_player_script()

    return f"""<div class="pron-table-wrap">
<table class="pron">
<thead><tr><th class="num">#</th>{thead}</tr></thead>
<tbody>{tbody}</tbody>
</table>
</div>
{audio_script}"""


def visible_levels():
    return [l for l in LEVELS if not l.get("hidden")]


def _nav_links(n):
    vis = visible_levels()
    nums = [l["num"] for l in vis]
    idx = nums.index(n) if n in nums else None
    def link(target, label, disabled_label):
        if target is None:
            return f'<a class="btn disabled">{disabled_label}</a>'
        return f'<a class="btn" href="Niveau%20{target}.html">{label}</a>'
    prev_target = nums[idx - 1] if idx not in (None, 0) else None
    nxt_target = nums[idx + 1] if idx is not None and idx + 1 < len(nums) else None
    return (
        link(prev_target, "◀ السابق", "◀ السابق"),
        link(nxt_target, "التالي ▶", "التالي ▶"),
    )


def render_level(lvl):
    n = lvl["num"]
    ideas = lvl.get("ideas", [])
    cefr = lvl.get("cefr", "A1")
    title_en = lvl["title_en"]
    title_ar = lvl["title_ar"]
    cat = lvl.get("category", "")
    cat_ar = lvl.get("category_ar", "")
    prev, nxt = _nav_links(n)

    if lvl.get("layout") == "table":
        icon = "📗"
        style_extra = STYLE_TABLE_WIDTH
        ideas_content = render_table(lvl)
        n_points = table_rule_count(lvl.get("table_rows", []))
        toc_links = []
        toc_html = ""
        meta_en = f"Ce niveau présente <b>{n_points}</b> règles de prononciation sous forme d'un tableau récapitulatif."
        meta_ar = f"يحتوي هذا المستوى على <b>{n_points}</b> قاعدة نطق للحروف المركبة في شكل جدول ملخّص."
        objectif = "maîtriser les règles de prononciation des digraphes anglais pour lire et prononcer correctement les mots."
        audio_block = ""
    else:
        style_extra = STYLE_TABLE_WIDTH if lvl.get("extra_tables") else ""
        icon = "📖"
        cards = []
        toc_links = []
        for i, idea in enumerate(ideas, 1):
            def ex_row(row):
                en, ar = row[0], row[1]
                pron = row[2] if len(row) > 2 and row[2].strip() else ar_pron(en)
                say = ""
                if en.strip():
                    fname = _audio_fname(_audio_clean(en))
                    say = (f' <button class="say" data-src="_audio_niveaux/{fname}" '
                           f'data-label="{en}" title="استمع إلى النطق" aria-label="Écouter">▶</button>')
                return (f'<tr>'
                        f'<td class="en-c">{en}{say}</td>'
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
        for et in (lvl.get("extra_tables") or []):
            et_lvl = {
                "num": lvl["num"],
                "table_columns": et["table_columns"],
                "table_rows": et["table_rows"],
                "audio_col": et.get("audio_col"),
                "audio_prefix_col": et.get("audio_prefix_col"),
            }
            ideas_content += f'\n<div class="card" style="overflow:visible;">'
            ideas_content += f'<h3>{et.get("title_en", "")} — <span class="ar">{et.get("title_ar", "")}</span></h3>'
            if et.get("source"):
                ideas_content += f'<div class="cat-label">📎 {et["source"]} — alphabet complet (A–Z)</div>'
            ideas_content += render_table(et_lvl)
            ideas_content += '</div>'
        n_points = len(cards)
        toc_html = f'<div class="toc"><h3>Sommaire rapide</h3><div class="toc-list">{"".join(toc_links)}</div></div>'
        meta_en = f"Ce niveau propose <b>{n_points}</b> points de grammaire à maîtriser."
        meta_ar = f"يحتوي هذا المستوى على <b>{n_points}</b> نقطة لغوية أساسية للتدريب والتطبيق."
        objectif = "maîtriser les bases de ce thème pour les utiliser naturellement dans des phrases simples, claires et correctes."
        audio_block = _audio_player_bar() + _audio_player_script()

    badge = f'<span class="badge {cefr_class(cefr)}">{cefr}</span>'
    catline = f'<span class="cat-label">{cat}</span>'
    if cat_ar:
        catline += f' <span class="ar">— {cat_ar}</span>'

    groups = []
    vis_nums = [l["num"] for l in visible_levels()]
    for start in range(1, max(vis_nums) + 1, 10):
        end = min(start + 9, max(vis_nums))
        groups.append(f'<a class="side-link" href="Niveau%20{start}.html">Niveaux {start}-{end}</a>')

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>قواعد اللغة الإنجليزية — Niveau {n}</title>
{STYLE_COMMON}{style_extra}
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
    <h1>{icon} مستوى {n} — {title_en}</h1>
    <div class="ar" style="color:#dfeee9;font-size:1.1rem;">{title_ar}</div>
    {banner()}
    <div class="summary-grid">
      <div class="summary-card"><span class="label">CEFR</span><span class="value">{badge}</span></div>
      <div class="summary-card"><span class="label">القواعد</span><span class="value">{n_points}</span></div>
      <div class="summary-card"><span class="label">الفئة</span><span class="value">{cat if cat else 'General'}</span></div>
      <div class="summary-card"><span class="label">الترتيب</span><span class="value">Niveau {n}</span></div>
    </div>
    <div class="meta">
    <b>{badge} {catline}</b><br>
    <div class="en">{meta_en}</div>
    <div class="ar">{meta_ar}</div>
    </div>
    {toc_html}
    <div class="story-box">
      <strong>Objectif du niveau :</strong> {objectif}
    </div>
    {ideas_content}
    {audio_block}
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
    vis = [l for l in LEVELS if not l.get("hidden")]
    rows = []
    n = len(vis)
    total_levels = len(vis)
    cefr_found = sorted({l.get("cefr", "A1") for l in vis})
    cefr_txt = " → ".join(cefr_found) if cefr_found else ""
    for lvl in vis:
        cls = cefr_class(lvl.get("cefr", "A1"))
        n_points = table_rule_count(lvl.get("table_rows", [])) if lvl.get("layout") == "table" else len(lvl.get("ideas", []))
        rows.append(
            f"""<tr>
<td class="num">{lvl['num']}</td>
<td><span class="badge {cls}">{lvl.get('cefr','A1')}</span></td>
<td class="nm">{lvl['title_en']}</td>
<td class="ar t">{lvl['title_ar']}</td>
<td>{n_points}</td>
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
  <div class="summary-card"><span class="label">Idées</span><span class="value">{sum((table_rule_count(l.get('table_rows', [])) if l.get('layout') == 'table' else len(l.get('ideas', []))) for l in LEVELS)}</span></div>
  <div class="summary-card"><span class="label">Progression</span><span class="value">A1 → {cefr_txt.split(' → ')[-1] if ' → ' in cefr_txt else cefr_txt}</span></div>
  <div class="summary-card"><span class="label">Format</span><span class="value">100% HTML</span></div>
</div>
"""
    sidebar_links = []
    vis_nums = [l["num"] for l in visible_levels()]
    for start in range(1, max(vis_nums) + 1, 10):
        end = min(start + 9, max(vis_nums))
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
    ensure_audio_files(LEVELS)
    with open(os.path.join(BASE, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_index())
    for lvl in LEVELS:
        if lvl.get("hidden"):
            continue
        page = render_level(lvl)
        path = os.path.join(OUT, f"Niveau {lvl['num']}.html")
        with open(path, "w", encoding="utf-8") as f:
            f.write(page)
        n_points = table_rule_count(lvl.get("table_rows", [])) if lvl.get("layout") == "table" else len(lvl["ideas"])
        print(f"Niveau {lvl['num']} : {n_points} idées → {path}")
    print(f"Total : {len(visible_levels())} niveaux générés.")

    def _points(l):
        return table_rule_count(l.get("table_rows", [])) if l.get("layout") == "table" else len(l.get("ideas", []))
    total_ideas = sum(_points(l) for l in visible_levels())
    print(f"Total idées : {total_ideas}")


if __name__ == "__main__":
    main()