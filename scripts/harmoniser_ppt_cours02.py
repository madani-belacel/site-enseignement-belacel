#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harmonise la présentation « Utiliser l'IA » avec la charte du site.

Trois écarts avec les cinq autres cours du module :

  1. l'accent est orange (#FF8A00), couleur qui n'existe nulle part sur le
     site ; il faut le vert de la charte (#1B7A52) ;
  2. la couverture ne porte aucun logo de l'institution ;
  3. le pied de page dit seulement « Module IA - 2e année PEP », sans le nom
     de l'auteur ni l'université, et le numéro de page est à gauche alors
     que les autres cours l'ont à droite.

Le contenu, les notes et la mise en page de fond ne sont pas touchés : seule
la couleur d'accent, la couverture et le pied de page changent.

Usage : python3 scripts/harmoniser_ppt_cours02.py source.pptx sortie.pptx
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

from pptx_commun import (GREY, NAVY, add_paragraph, add_shape, add_textbox,
                         hauteur_requise, logo, ratio_texte)

# Dernier point utilisable : le filet de pied de page est à 6.92.
LIMITE_BAS = 6.92

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_UNIV = os.path.join(RACINE, "images", "Université_de_Mostaganem.png")
IMG_FLE = os.path.join(RACINE, "images", "LOGO-FLE-UNIV-Mosta.jpeg")

ORANGE = "FF8A00"        # accent d'origine, à remplacer
VERT_FONCE = "1E8E4E"    # vert déjà présent dans le deck
VERT_CHARTE = "1B7A52"   # vert des autres cours du module

PIED = ("Cours 02 · Utiliser l'IA au quotidien   |   "
        "Dr. Madani BELACEL — Université de Mostaganem")

cache = {}


def recolorer(prs):
    """Remplace l'orange et unifie les deux verts sur le vert de la charte."""
    n = 0
    for s in prs.slides:
        for sh in s.shapes:
            cibles = []
            try:
                if sh.fill.type == 1:
                    cibles.append(("fill", sh.fill.fore_color))
            except Exception:
                pass
            try:
                if sh.line.fill.type == 1:
                    cibles.append(("line", sh.line.color))
            except Exception:
                pass
            for quoi, couleur in cibles:
                try:
                    if str(couleur.rgb) in (ORANGE, VERT_FONCE):
                        couleur.rgb = RGBColor.from_string(VERT_CHARTE)
                        n += 1
                except Exception:
                    pass
            if sh.has_text_frame:
                for para in sh.text_frame.paragraphs:
                    for r in para.runs:
                        try:
                            c = r.font.color
                            if c and c.type == 1 and str(c.rgb) in (ORANGE,
                                                                    VERT_FONCE):
                                c.rgb = RGBColor.from_string(VERT_CHARTE)
                                n += 1
                        except Exception:
                            pass
    return n


def logos_couverture(slide):
    """Les deux logos de l'institution, sur un cartouche blanc.

    Le logo de la faculté est un JPEG à fond blanc : sans le cartouche, il
    laisserait un rectangle gris sur le fond marine.
    """
    x0, y0, w, h = 8.95, 0.52, 3.90, 1.02
    add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, x0, y0, w, h,
              fill=RGBColor(0xFF, 0xFF, 0xFF), line=None, radius=0.12)
    x = x0 + 0.22
    h_logo = 0.74
    y_logo = y0 + (h - h_logo) / 2
    for chemin in (IMG_UNIV, IMG_FLE):
        if os.path.isfile(chemin):
            x += logo(slide, chemin, x, y_logo, h_logo, cache=cache) + 0.26


def auteur_couverture(slide):
    """Nom et université sur la page de garde, comme les autres cours."""
    tf = add_textbox(slide, 1.00, 6.52, 7.6, 0.40, anchor=MSO_ANCHOR.MIDDLE)
    add_paragraph(tf, "Dr. Madani BELACEL — Université de Mostaganem",
                  size=13, bold=True, color=RGBColor(0xFF, 0xFF, 0xFF),
                  space_after=0)


def _pouces(valeur):
    """python-pptx renvoie les marges en EMU ; le vérificateur les convertit."""
    return Emu(valeur).inches if valeur is not None else 0.0


def _besoin(sh):
    """Hauteur max requise par un paragraphe, selon la mesure du vérificateur.

    scripts/verifier_pptx.py raisonne paragraphe par paragraphe contre la
    hauteur utile (boîte moins marges) : c'est cette convention qu'il faut
    reprendre, sinon l'ajustement passe à côté du problème.
    """
    tf = sh.text_frame
    # Tout en pouces : les deux termes doivent etre dans la meme unite.
    dispo_h = (sh.height / 914400.0 - _pouces(tf.margin_top)
               - _pouces(tf.margin_bottom))
    dispo_w = (sh.width / 914400.0 - _pouces(tf.margin_left)
               - _pouces(tf.margin_right))
    if dispo_h <= 0.05 or dispo_w <= 0.05:
        return None, 0.0
    pire = 0.0
    for p in tf.paragraphs:
        txt = "".join(r.text for r in p.runs)
        tailles = [r.font.size.pt for r in p.runs if r.font.size]
        if not txt.strip() or not tailles:
            continue
        t = max(tailles)
        car = max(1.0, (dispo_w * 72.0) / (ratio_texte(t) * t))
        lignes = max(1, int(math.ceil(len(txt) / car)))
        pire = max(pire, lignes * t * 1.15 / 72.0)
    return pire, dispo_h


def _retrecir(tf, facteur):
    for para in tf.paragraphs:
        for r in para.runs:
            if r.font.size:
                r.font.size = Pt(max(8.0, r.font.size.pt * facteur))


def ajuster_textes(prs):
    """Répare les débordements hérités du deck d'origine.

    Deux gestes, dans l'ordre : agrandir la boîte si la place manque jusqu'au
    filet de pied, sinon réduire la police jusqu'à ce qu'elle tienne. Les
    boîtes qui dépassent le filet sont d'abord ramenées à sa hauteur.
    """
    ajustes = 0
    for s in prs.slides:
        for sh in s.shapes:
            if not sh.has_text_frame or not sh.text_frame.text.strip():
                continue
            if sh.top is None or sh.top / 914400 > 6.9:   # pieds de page
                continue
            tf = sh.text_frame
            marge = _pouces(tf.margin_top) + _pouces(tf.margin_bottom)
            y = sh.top / 914400
            h = sh.height / 914400

            # une boîte qui franchit le filet de pied est ramenée dessus
            if h > 0.20 and y + h > LIMITE_BAS + 0.03 and y < LIMITE_BAS:
                sh.height = Inches(max(0.30, LIMITE_BAS - y))
                h = sh.height / 914400
                ajustes += 1

            for _ in range(14):
                pire, dispo_h = _besoin(sh)
                if pire is None or pire <= dispo_h + 0.04:
                    break
                _retrecir(tf, 0.93)
            else:
                besoin, dispo_h = _besoin(sh)
                if besoin and besoin <= (LIMITE_BAS - y) - marge:
                    sh.height = Inches(besoin + marge + 0.06)
                    ajustes += 1
    return ajustes


def pied_de_page(slide, numero):
    """Pied de page réaligné : texte à gauche, numéro à droite.

    Le deck d'origine avait le numéro à gauche et le libellé à droite, sans
    le nom de l'auteur. On remet les deux dans l'ordre des autres cours.
    """
    for sh in slide.shapes:
        if not sh.has_text_frame:
            continue
        t = sh.text_frame.text.strip()
        if not t:
            continue
        if t.isdigit():
            sh.left, sh.top = Inches(11.40), Inches(7.05)
            sh.width, sh.height = Inches(1.70), Inches(0.36)
            for para in sh.text_frame.paragraphs:
                para.alignment = PP_ALIGN.RIGHT
        elif "Module IA" in t and "année" in t:
            sh.left, sh.top = Inches(0.40), Inches(7.05)
            sh.width, sh.height = Inches(10.80), Inches(0.36)
            tf = sh.text_frame
            tf.clear()
            add_paragraph(tf, PIED, size=9, color=RGBColor(0x9F, 0xB6, 0xD0),
                          space_after=0)


def main():
    src, dst = sys.argv[1], sys.argv[2]
    prs = Presentation(src)
    n = recolorer(prs)
    couverture = prs.slides[0]
    logos_couverture(couverture)
    auteur_couverture(couverture)
    for i, s in enumerate(prs.slides, 1):
        if i > 1:
            pied_de_page(s, i)
    a = ajuster_textes(prs)
    prs.save(dst)
    print("  couleurs remplacees : %d" % n)
    print("  textes ajustes      : %d" % a)
    print("  diapositives        : %d" % len(prs.slides))
    print("  ecrit               : %s" % dst)


if __name__ == "__main__":
    main()