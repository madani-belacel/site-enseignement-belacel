#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fusionne le contenu et les questions du Cours 01 en une seule présentation.

Le module IA avait deux pièces pour le cours 01 : la présentation (30
diapositives de contenu, sans questions) et la page Q/R (10 idées, 31
questions, en français et en anglais). L'enseignant devait les faire
tourner cote a cote.

Ce script ajoute les questions a la fin du deck de contenu, sous la forme
d'un cahier de questions : une diapositive de questions par idee, une
diapositive de reponses. Les reponses restent sur une diapositive separee
pour que la classe puisse repondre avant la correction — c'est tout l'interet
d'un exercise.

Les 31 couples Q/R sont lus dans la page Q/R, jamais recopiés a la main :
ils ne peuvent pas diverger de la page.

Usage : python3 scripts/fusionner_qr_cours01.py sortie.pptx
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt

from pptx_commun import (DARK, GREY, GREY_L, GREEN_L, LINE_C, NAVY, WHITE,
                         add_footer, add_paragraph, add_shape, add_textbox,
                         dbox, ecrire_notes, taille_qui_tient)

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle")
PAGE_QR = os.path.join(MODULE, "QR_IA_01_Introduction_IA.html")
SOURCE = os.path.join(RACINE, "scripts", "contenus_details_qr",
                      "qr_cours01.json")
PIED = ("Cours 01 · Introduction à l'IA   |   "
        "Dr. Madani BELACEL — Université de Mostaganem")


def charger():
    return json.loads(open(SOURCE, encoding="utf-8").read())


def separateur(slide, numero, titre, chapeau):
    """Diapositive de séparation du cahier de questions.

    Le fond s'arrete a 6.62 pouces, comme les autres diapositives de
    separation du cours 01 : un fond perdu jusqu'en bas traverserait le filet
    de pied de page, que verifier_pptx.py signale.
    """
    add_shape(slide, MSO_SHAPE.RECTANGLE, 0, 0.26, 13.333, 6.36, fill=NAVY)
    add_shape(slide, MSO_SHAPE.RECTANGLE, 0, 0, 13.333, 0.26, fill=GREEN_L)
    tf = add_textbox(slide, 1.1, 2.35, 11.1, 0.85, anchor=MSO_ANCHOR.MIDDLE)
    add_paragraph(tf, titre, size=36, bold=True, color=WHITE, space_after=0)
    add_shape(slide, MSO_SHAPE.RECTANGLE, 1.1, 3.45, 2.2, 0.05, fill=WHITE)
    tf = add_textbox(slide, 1.1, 3.80, 10.6, 1.5)
    add_paragraph(tf, chapeau, size=17, color=WHITE, space_after=10,
                  line_spacing=1.28)
    return numero


def questions(slide, idee, numero):
    tf = add_textbox(slide, 0.75, 0.52, 11.85, 0.42)
    add_paragraph(tf, "%s — %s" % (idee["tag"], idee["titre"]),
                  size=13, bold=True, color=GREY, space_after=0)
    tf = add_textbox(slide, 0.75, 0.98, 11.85, 0.66)
    add_paragraph(tf, "Posez ces questions, puis ouvrez les réponses.",
                  size=27, bold=True, color=NAVY, space_after=0)
    y = 1.95
    for n, qa in enumerate(idee["qa"], 1):
        numero_q = re.sub(r"<[^>]+>", "", qa["q"]).strip()
        numero_q = re.sub(r"^Q\d+\.\s*", "", numero_q)
        h = 0.62 if len(numero_q) < 95 else 0.86
        add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.75, y, 0.46, h,
                  fill=NAVY, line=None, radius=0.28)
        tf = add_textbox(slide, 0.75, y, 0.46, h, anchor=MSO_ANCHOR.MIDDLE)
        add_paragraph(tf, str(n), size=15, bold=True, color=WHITE,
                      align=PP_ALIGN.CENTER, space_after=0)
        tf = add_textbox(slide, 1.36, y, 11.25, h, anchor=MSO_ANCHOR.MIDDLE)
        taille = taille_qui_tient(numero_q, 11.1, h - 0.08, maxi=16, mini=11)
        add_paragraph(tf, numero_q, size=taille, color=DARK, space_after=0,
                      line_spacing=1.16)
        y += h + 0.14
    return y


def reponses(slide, idee, numero):
    tf = add_textbox(slide, 0.75, 0.52, 11.85, 0.42)
    add_paragraph(tf, "%s — %s" % (idee["tag"], idee["titre"]),
                  size=13, bold=True, color=GREY, space_after=0)
    tf = add_textbox(slide, 0.75, 0.98, 11.85, 0.66)
    add_paragraph(tf, "Réponses", size=27, bold=True, color=NAVY,
                  space_after=0)
    y = 1.90
    for n, qa in enumerate(idee["qa"], 1):
        r = re.sub(r"^R\d+\.\s*", "", re.sub(r"<[^>]+>", "", qa["r"]).strip())
        h = 0.60 if len(r) < 110 else 0.84
        add_shape(slide, MSO_SHAPE.ROUNDED_RECTANGLE, 0.75, y, 0.46, h,
                  fill=GREEN_L, line=None, radius=0.28)
        tf = add_textbox(slide, 0.75, y, 0.46, h, anchor=MSO_ANCHOR.MIDDLE)
        add_paragraph(tf, str(n), size=15, bold=True, color=NAVY,
                      align=PP_ALIGN.CENTER, space_after=0)
        tf = add_textbox(slide, 1.36, y, 11.25, h, anchor=MSO_ANCHOR.MIDDLE)
        taille = taille_qui_tient(r, 11.1, h - 0.08, maxi=15, mini=10.5)
        add_paragraph(tf, r, size=taille, color=DARK, space_after=0,
                      line_spacing=1.16)
        y += h + 0.13
    return y


def main():
    sortie = sys.argv[1] if len(sys.argv) > 1 else None
    idees = charger()
    prs = Presentation(sys.argv[2]) if len(sys.argv) > 2 else None
    if prs is None:
        print("Usage : fusionner_qr_cours01.py sortie.pptx deck_de_contenu.pptx")
        return 1

    vide = prs.slide_layouts[6]
    n = len(prs.slides._sldIdLst)

    # 1. la page de garde du cahier de questions
    s = prs.slides.add_slide(vide)
    n += 1
    separateur(s, n, "Cahier de questions",
               "31 questions et réponses, classées par idée. Elles sont "
               "aussi sur la page Q/R du module, en français et en anglais.")
    add_footer(s, n, PIED)

    # 2. une idee = une diapositive de questions + une de reponses
    for idee in idees:
        s = prs.slides.add_slide(vide)
        n += 1
        questions(s, idee, n)
        add_footer(s, n, PIED)
        ecrire_notes(s, notes_idee(idee))

        s = prs.slides.add_slide(vide)
        n += 1
        reponses(s, idee, n)
        add_footer(s, n, PIED)
        ecrire_notes(s, notes_reponses(idee))

    prs.save(sortie)
    print("  diapositives de contenu   : %d" % (n - 1 - 2 * len(idees)))
    print("  idees ajoutees            : %d" % len(idees))
    print("  questions                 : %d"
          % sum(len(i["qa"]) for i in idees))
    print("  total                     : %d" % n)
    print("  ecrit                     : %s" % sortie)
    return 0


def notes_idee(idee):
    qs = "\n".join("Q%d. %s" % (i + 1, nettoyer(q["q"]))
                   for i, q in enumerate(idee["qa"]))
    return """CAHIER DE QUESTIONS — %s

🎯 OBJECTIF
Faire formuler les réponses par la classe avant de les dévoiler.

🗣️ CE QUE JE DIS
Je lis les trois questions une par une, sans répondre. Je laisse la
classe chercher trente secondes, puis je demande à deux ou trois
étudiants de proposer une réponse. Je note les formulations au tableau :
ce sont elles que je comparerai aux réponses de la diapositive suivante.

❓ QUESTIONS DE LA DIAPOSITIVE
%s

⚠️ PIÈGE À ÉVITER
Les réponses de cette page sont volontairement courtes : ce sont des
réponses de trente secondes, pas un cours. Si un étudiant demande « et
pourquoi ? », c'est bon signe : on bascule alors sur le contenu.""" % (
        idee["titre"], qs)


def notes_reponses(idee):
    rs = "\n".join("R%d. %s" % (i + 1, nettoyer(q["r"]))
                   for i, q in enumerate(idee["qa"]))
    return """CAHIER DE RÉPONSES — %s

🎯 OBJECTIF
Corriger, et surtout montrer où les réponses de la classe s'écartent des
réponses attendues.

🗣️ CE QUE JE DIS
Je confronte les réponses notées au tableau avec celles de la page. Je
souligne les formulations justes mais mal dites : elles valent mieux que la
réponse type. Quand une réponse manque, je ne la lis pas immédiatement, je
demande d'abord à la classe.

❓ RÉPONSES ATTENDUES
%s

⚠️ PIÈGE À ÉVITER
Ne pas lire les réponses d'une traite. Une réponse lue trop vite n'est pas
retenue, et l'étudiant qui avait trouvé mieux reconnaît rarement qu'il avait
raison.""" % (idee["titre"], rs)


def nettoyer(s):
    return re.sub(r"^Q\\d+\\.\\s*|^R\\d+\\.\\s*", "", s).strip()


if __name__ == "__main__":
    sys.exit(main())