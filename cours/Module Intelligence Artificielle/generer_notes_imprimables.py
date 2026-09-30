#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique le document imprimable des questions / reponses du cours 01.

Les Q/R vivent dans les notes du presentateur du .pptx (Affichage -> Mode
Presentateur). Ce script en sort une version A4 propre, 4 pages, a
emporter/imprimer le jour de la seance.

Il relit le meme HTML que le generateur de diapositives, donc le document
imprime ne peut pas diverger du cours.

Sortie : Presentations_PPTX/QR_IA_01_Introduction_IA_notes.pdf
Usage  : python3 generer_notes_imprimables.py [cours.html] [sortie.pdf]
"""
import importlib.util
import os
import re
import subprocess
import sys
import tempfile

DOSSIER = os.path.dirname(os.path.abspath(__file__))
COURS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    DOSSIER, "QR_IA_01_Introduction_IA.html")
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.join(
    DOSSIER, "Presentations_PPTX", "QR_IA_01_Introduction_IA_notes.pdf")

CSS = """
@page { size: A4; margin: 15mm 14mm 13mm 14mm; }
body { font-family: "DejaVu Serif", Georgia, serif; font-size: 10.5pt;
       line-height: 1.45; color: #1b2433; }
h1 { font-size: 16pt; color: #122a4f; margin: 0 0 2mm; }
.sous { font-size: 9pt; color: #5b6879; margin: 0 0 4mm; }
p.mention { font-size: 8.5pt; color: #5b6879; border-top: 1px solid #d3deea;
            padding-top: 2.5mm; margin: 0 0 4mm; }
h2 { font-size: 12pt; color: #122a4f; margin: 5mm 0 2mm;
     border-left: 4px solid #c26a0a; padding-left: 3mm;
     page-break-after: avoid; }
/* Pastille coloree impossible a rendre fidelement : le convertisseur
   HTML de LibreOffice ignore min-width sur un inline-block et rogne le
   numero. Un simple prefixe en gras tient dans tous les viewers. */
.num { color: #c26a0a; font-weight: bold; margin-right: 1.5mm; }
.expl { font-size: 9.5pt; color: #3d4d61; margin: 0 0 2.5mm; }
.q { font-weight: bold; color: #122a4f; margin: 2.6mm 0 0.8mm; }
.r { margin: 0 0 1.2mm 5mm; text-align: justify; }
.pagebreak { page-break-before: always; }
"""


def charger_idees():
    spec = importlib.util.spec_from_file_location(
        "mk", os.path.join(DOSSIER, "make_pptx_ia01.py"))
    mk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mk)
    return mk.lire_cours_html(COURS)


def html(idees, qa_fr):
    L = Qa_fr = None
    n_q = sum(len(i["qa_fr"]) if qa_fr else len(i["qa_en"]) for i in idees)
    blocs = []
    for k, idee in enumerate(idees, 1):
        paires = idee["qa_fr"] if qa_fr else idee["qa_en"]
        h = ['<h2><span class="num">Idée %d</span>&nbsp; %s</h2>'
             % (k, idee["fr_t"])]
        h.append('<p class="expl">%s</p>' % idee["fr_x"])
        for q, r in paires:
            h.append('<p class="q">%s</p>' % q)
            h.append('<p class="r">%s</p>' % r)
        blocs.append("\n".join(h))
    return """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>Questions / Réponses — Introduction à l'IA</title>
<style>%s</style></head><body>
<h1>Introduction à l'IA — %d questions et réponses</h1>
<p class="sous">Cours 01 · Module Intelligence Artificielle · 2ᵉ année PEP · ENS
Université de Mostaganem — filière Français</p>
<p class="mention">Document de travail du présentateur. Le même contenu se trouve
dans les notes du fichier PowerPoint (Affichage → Mode Présentateur).
Dr. Madani BELACEL — MCB.</p>
%s
</body></html>""" % (CSS, n_q, "\n".join(blocs))


def main():
    idees = charger_idees()
    if not idees:
        print("aucune idee lue dans", COURS)
        return 1
    doc = html(idees, qa_fr=True)
    with tempfile.TemporaryDirectory() as tmp:
        src = os.path.join(tmp, "notes.html")
        open(src, "w", encoding="utf-8").write(doc)
        subprocess.run(["soffice", "--headless", "--convert-to", "pdf",
                        "--outdir", tmp, src], check=True, timeout=600,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        produit = os.path.join(tmp, "notes.pdf")
        if not os.path.exists(produit):
            print("conversion echouee")
            return 1
        os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
        with open(produit, "rb") as a, open(SORTIE, "wb") as b:
            b.write(a.read())

    n_q = sum(len(i["qa_fr"]) for i in idees)
    print("Ecrit :", SORTIE)
    print("  %d idees, %d questions et reponses  |  %.1f Ko"
          % (len(idees), n_q, os.path.getsize(SORTIE) / 1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
