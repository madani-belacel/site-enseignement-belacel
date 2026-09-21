#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_pptx.py — Conversion des supports de séance (slides.md) en PowerPoint.

Module « Intelligence Artificielle en Éducation — PEP 2ème année »
Dr. Madani BELACEL — ENS Université de Mostaganem.

Ce script parcourt les dossiers `seance-*` du module et, pour chaque
fichier `slides.md` trouvé, produit `presentation.pptx` dans le même dossier.

Deux formats d'entrée sont supportés :
  1. Format Marp — les diapositives sont séparées par une ligne `---`
     (l'en-tête YAML entre deux `---` est ignoré).
  2. Format Markdown standard — chaque titre niveau 2 (`## `) démarre
     une nouvelle diapositive.

Usage :
    python3 generate_pptx.py            # toutes les séances
    python3 generate_pptx.py seance-01  # une séance précise

Pré‑requis :
    pip install python-pptx
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# Dépendance
# ---------------------------------------------------------------------------
try:
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.dml.color import RGBColor
except ImportError:  # pragma: no cover
    sys.exit(
        "❌ python-pptx n'est pas installé.\n"
        "Installez-le avec la commande :\n"
        "    pip install python-pptx\n"
        "puis relancez le script."
    )

# Couleurs sobres du module
C_PRIMARY = RGBColor(0x17, 0x7B, 0xBE)   # bleu du site
C_DARK = RGBColor(0x26, 0x32, 0x38)      # ardoise foncée
C_LIGHT = RGBColor(0xEC, 0xEF, 0xF1)     # texte clair
C_MUTED = RGBColor(0x78, 0x89, 0x9C)     # texte secondaire
C_ACCENT = RGBColor(0x2E, 0x7D, 0x32)    # vert

W, H = Inches(13.333), Inches(7.5)


# ---------------------------------------------------------------------------
# Parsing de slides.md
# ---------------------------------------------------------------------------
def split_slides(text: str) -> list[str]:
    """Découpe le contenu en une liste de diapositives (texte brut)."""
    # Format Marp : en-tête YAML entre `---`, puis diapositives séparées par `---`.
    if text.lstrip().startswith("---\n"):
        # On retire précisément le frontmatter (premier bloc entre deux ---).
        parts = text.split("---", 2)
        if len(parts) == 3 and parts[1].strip().startswith(("marp", "theme", "title", "paginate")):
            body = parts[2]
        else:
            body = text
    else:
        body = text
    lines = [ln.rstrip() for ln in body.splitlines()]

    # Découpage par séparateurs Marp (ligne `---`).
    marp_slides: list[list[str]] = []
    cur: list[str] = []
    for ln in lines:
        if ln.strip() == "---":
            if cur and any(l.strip() for l in cur):
                marp_slides.append(cur)
            cur = []
        else:
            cur.append(ln)
    if cur and any(l.strip() for l in cur):
        marp_slides.append(cur)

    if marp_slides:
        return ["\n".join(s).strip() for s in marp_slides]

    # Format standard : chaque titre `## ` démarre une nouvelle diapositive.
    std_slides: list[str] = []
    cur = []
    for ln in lines:
        if ln.startswith("## "):
            if cur:
                std_slides.append("\n".join(cur).strip())
            cur = [re.sub(r"^##\s+", "# ", ln)]
        else:
            cur.append(ln)
    if cur:
        std_slides.append("\n".join(cur).strip())
    return [s for s in std_slides if s.strip()]


def slide_title(body: str) -> str:
    """Titre de la diapositive (première ligne `#`)."""
    for ln in body.splitlines():
        m = re.match(r"^#\s+(.+)$", ln)
        if m:
            return m.group(1).strip()
    return ""


def slide_content(body: str) -> list[str]:
    """Corps de la diapositive : lignes sans le titre, nettoyées."""
    out = []
    for ln in body.splitlines():
        if re.match(r"^#\s+", ln) or not ln.strip():
            continue
        out.append(ln.strip())
    return out


def md_to_plain(text: str) -> str:
    """Supprime les balises Markdown simples pour un affichage PPT propre."""
    text = re.sub(r"^#{1,6}\s+", "", text)          # titres
    text = re.sub(r"^[-*]\s+", "", text)            # puces
    text = re.sub(r"^\d+\.\s+", "", text)           # listes numérotées
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)    # gras
    text = re.sub(r"\*(.+?)\*", r"\1", text)        # italique
    text = re.sub(r"`([^`]+)`", r"\1", text)        # code inline
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # liens
    return text.strip()


# ---------------------------------------------------------------------------
# Construction du PPTX
# ---------------------------------------------------------------------------
def build_pptx(slides: list[str], out_path: Path) -> None:
    prs = Presentation()
    prs.slide_width, prs.slide_height = W, H
    blank = prs.slide_layouts[6]

    def new_slide(bg: RGBColor | None = None):
        slide = prs.slides.add_slide(blank)
        if bg is not None:
            slide.background.fill.solid()
            slide.background.fill.fore_color.rgb = bg
        return slide

    def add_text(slide, left, top, width, height, text, size, color, bold=False, italic=False, align=None):
        box = slide.shapes.add_textbox(left, top, width, height)
        tf = box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
        if align:
            p.alignment = align
        return box

    def add_bullets(slide, lines, size=20, color=None, left=Inches(0.9), top=Inches(1.6)):
        box = slide.shapes.add_textbox(left, top, Inches(11.5), Inches(5.4))
        tf = box.text_frame
        tf.word_wrap = True
        first = True
        for raw in lines:
            text = md_to_plain(raw)
            if not text:
                continue
            bold_start = raw.startswith("**")
            empty = raw.startswith("*") and not raw.startswith("**") and raw.endswith("*")
            italic = empty
            p = tf.paragraphs[0] if first else tf.add_paragraph()
            first = False
            # gère l'indentation des listes éventuelles
            p.level = 0
            r = p.add_run()
            r.text = ("• " if not text.startswith(("•", "→")) and not re.match(r"^\d+[.)]", text) else "") + text
            r.font.size = Pt(size)
            r.font.bold = bold_start
            r.font.italic = italic
            r.font.color.rgb = color or C_DARK

    is_end = False
    for i, slide_text in enumerate(slides):
        title = slide_title(slide_text)
        lines = slide_content(slide_text)
        is_end = i == len(slides) - 1 or title.startswith("Merci") and i > 0

        if i == 0 or is_end:
            slide = new_slide(C_DARK)
            st = title or f"Séance de formation"
            add_text(slide, Inches(0.9), Inches(2.1), Inches(11.5), Inches(1.6), st,
                     40, RGBColor(255, 255, 255), bold=True)
            for j, ln in enumerate(lines[:3]):
                add_text(slide, Inches(0.9), Inches(3.9 + j * 0.6), Inches(11.5), Inches(0.6),
                         md_to_plain(ln), 18, C_LIGHT, italic=True)
            add_text(slide, Inches(0.9), Inches(6.4), Inches(11.5), Inches(0.6),
                     "Module Intelligence Artificielle — PEP 2A · Dr. Madani BELACEL",
                     13, C_MUTED)
        else:
            slide = new_slide()
            add_text(slide, Inches(0.9), Inches(0.55), Inches(11.8), Inches(1.0), title or "(sans titre)",
                     30, C_PRIMARY, bold=True)
            add_bullets(slide, lines)

    prs.save(out_path)


# ---------------------------------------------------------------------------
# Boucle principale
# ---------------------------------------------------------------------------
def generate_for(seance_dir: Path) -> None:
    slides_file = seance_dir / "slides.md"
    out_file = seance_dir / "presentation.pptx"
    if not slides_file.exists():
        print(f"⏭  {seance_dir.name} : pas de slides.md → ignoré.")
        return
    slides = split_slides(slides_file.read_text(encoding="utf-8"))
    build_pptx(slides, out_file)
    print(f"✓ {seance_dir.name} → {out_file.name} ({len(slides)} diapositives)")


def main() -> None:
    targets = sys.argv[1:]
    seances = [BASE / t for t in targets] if targets else sorted(BASE.glob("seance-*"))
    done = 0
    for seance in seances:
        if seance.is_dir():
            generate_for(seance)
            done += 1
    if done == 0:
        print("Aucune séance traitée. Lancez : python3 generate_pptx.py")
    print("Terminé.")


if __name__ == "__main__":
    main()