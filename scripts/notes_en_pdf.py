#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Transforme les notes du présentateur d'un .pptx en document A4 imprimable.

Pourquoi : pendant la séance, la console du présentateur n'est utilisable
qu'avec deux écrans. Sur un seul écran, la seule façon fiable de lire ses
notes est de les avoir sur papier ou sur une autre machine — d'où ce PDF.

Le script lit les notes telles qu'elles sont stockées dans le fichier (donc
après génération), sans les réécrire : il ne peut pas diverger du deck.

Usage : python3 notes_en_pdf.py fichier.pptx [sortie.pdf]
"""
import os
import re
import subprocess
import sys
import tempfile
from html import escape

from pptx import Presentation

CSS = """
@page { size: A4; margin: 15mm 14mm 13mm 14mm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.5pt;
       line-height: 1.42; color: #1b2433; }
h1 { font-size: 16pt; color: #122a4f; margin: 0 0 2mm; }
.sous { font-size: 9pt; color: #5b6879; margin: 0 0 4mm; }
p.mention { font-size: 8.5pt; color: #5b6879; border-top: 1px solid #d3deea;
            padding-top: 2.5mm; margin: 0 0 3.5mm; }
h2 { font-size: 11.5pt; color: #122a4f; margin: 4.5mm 0 1.5mm;
     border-left: 4px solid #c26a0a; padding-left: 3mm;
     page-break-after: avoid; }
/* Pastille coloree non rendue fidelement par le convertisseur HTML de
   LibreOffice : un prefixe gras passe partout. */
.num { color: #c26a0a; font-weight: bold; margin-right: 1.5mm; }
pre { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt;
      white-space: pre-wrap; margin: 0; }
.diapo { page-break-inside: avoid; margin-bottom: 2mm; }
"""


def notes(slide):
    if not slide.has_notes_slide:
        return ""
    return slide.notes_slide.notes_text_frame.text.strip()


def titre_de(slide):
    """Premier texte non vide de la diapositive (sert d'en-tete)."""
    for sh in slide.shapes:
        if sh.has_text_frame:
            t = sh.text_frame.text.strip().split("\n")[0]
            if t:
                return t
    return ""


def construire(chemin_pptx, chemin_sortie):
    prs = Presentation(chemin_pptx)
    diapos = Presentation(chemin_pptx)
    blocs = []
    n_avec_notes = 0
    for i, s in enumerate(diapos.slides, 1):
        n = notes(s)
        if not n:
            continue
        n_avec_notes += 1
        tete = titre_de(s) or ("Diapositive %d" % i)
        blocs.append(
            '<div class="diapo"><h2><span class="num">%d</span>%s</h2>'
            '<pre>%s</pre></div>'
            % (i, escape(tete[:90]), escape(n)))

    doc = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Notes du présentateur — %s</title>
<style>%s</style></head><body>
<h1>Notes du présentateur — %s</h1>
<p class="sous">%d diapositives · %d pages de notes</p>
<p class="mention">Document de travail. Le même contenu se trouve dans le
fichier PowerPoint, sous chaque diapositive (LibreOffice Impress :
Affichage → Commentaires). Dr. Madani BELACEL — Université de Mostaganem.</p>
%s
</body></html>""" % (escape(os.path.basename(chemin_pptx)), CSS,
                      escape(os.path.basename(chemin_pptx)),
                      len(prs.slides._sldIdLst), n_avec_notes,
                      "\n".join(blocs))

    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "notes.html")
        with open(src, "w", encoding="utf-8") as f:
            f.write(doc)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf",
                        "--outdir", tmp, src], check=True, timeout=600,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        produit = os.path.join(tmp, "notes.pdf")
        if not os.path.exists(produit):
            print("conversion echouee")
            return 1
        d = os.path.dirname(chemin_sortie)
        if d:
            os.makedirs(d, exist_ok=True)
        with open(produit, "rb") as a, open(chemin_sortie, "wb") as b:
            b.write(a.read())
    return n_avec_notes


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = sys.argv[1]
    dst = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.splitext(src)[0] + "_notes.pdf"
    n = construire(src, dst)
    print("Ecrit :", dst)
    print("  %d pages de notes  |  %.1f Ko" % (n, os.path.getsize(dst) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
