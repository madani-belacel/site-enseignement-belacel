#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resserre la carte « Présentation PPTX » des cours IA.

Deux problemes corriges d'un coup :

1. La carte contient « 11 diapositives · notes du presentateur (PDF) ».
   La carte PPTX est bornee a 180px par .doc-item--pptx ; ce texte ne tient
   pas et returned sur deux ou trois lignes, ce qui gonfle toute la ligne du
   tableau. Sur la page TIC, la meme carte ne porte que « 21 diapositives ».

2. Le lien des notes est un <a> place dans le <a> de la presentation : deux
   balises <a> imbriquees, ce qui est invalide en HTML. Les navigateurs
   ferment l'ancre externe avant le lien interne, et le clic sur « notes »
   peut telecharger le PPTX au lieu du PDF.

Le lien notes devient donc un frere de la carte, en pastille compacte
 reutilisant .access-badge, deja defini dans css/style.css. Aucune regle
ajoutee, aucun autre page touchee.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "index.html")

DEBUT = re.compile(r'<a class="doc-item doc-item--pptx"')
NOTES = re.compile(r'\s*·\s*<a href="([^"]*_notes\.pdf)"[^>]*>[^<]*</a>')


def fermer(t, depart):
    """Index du </a> qui ferme l'ancre ouverte juste avant."""
    prof = 1
    for m in re.finditer(r"<a\b[^>]*>|</a>", t[depart:]):
        prof += -1 if m.group(0).startswith("</") else 1
        if prof == 0:
            return depart + m.start()
    return -1


def main():
    t = open(PAGE, encoding="utf-8").read()
    if 'class="access-badge"' in t:
        print("Pastilles notes deja en place : rien a faire.")
        return 0

    out, pos, n = [], 0, 0
    for m in DEBUT.finditer(t):
        fin = fermer(t, m.end())
        if fin < 0:
            continue
        carte = t[m.start():fin]
        note = NOTES.search(carte)
        if not note:
            out.append(t[pos:fin])
            pos = fin
            continue
        pdf, avant = note.group(1), note.group(0)
        # doc-date ne garde que le nombre de diapositives
        nouvelle = carte[:note.start()] + carte[note.end():]
        # le lien devient un frere, plus un imbrique
        pastille = ('<a class="access-badge" href="%s" target="_blank" '
                    'rel="noopener" download title="Notes du présentateur '
                    '(PDF)">PDF</a>' % pdf)
        out.append(t[pos:m.start()])
        out.append(nouvelle)
        out.append("</a>" + pastille)
        pos = fin + len("</a>")
        n += 1
    out.append(t[pos:])
    ouvert = open(PAGE, encoding="utf-8").read()
    if len(ouvert) != len(t) and not out:
        raise SystemExit("Transformation incomplete : abandon.")
    open(PAGE, "w", encoding="utf-8").write("".join(out))
    print("Cartes PPTX resserrees : %d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
