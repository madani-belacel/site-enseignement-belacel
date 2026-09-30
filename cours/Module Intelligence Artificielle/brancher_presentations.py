#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Branche les presentations PowerPoint sur les pages des cours Q/R du
module Intelligence Artificielle.

Deux endroits :
  - la barre de navigation de chaque page de cours (bouton de telechargement) ;
  - la carte du cours sur l'index du module (comme la carte « Présentation
    PPTX » du cours 01).

Ne touche qu'aux pages IA. Idempotent : relancer ne duplique rien.
"""
import os
import re

DOSSIER = os.path.dirname(os.path.abspath(__file__))
SORTIE_REL = "Presentations_PPTX"

COURS = [
    ("QR_IA_01_Introduction_IA", "11 diapositives"),
    ("QR_IA_02_Comment_Fonctionne_IA", "12 diapositives"),
    ("QR_IA_03_Exemples_Simples_IA", "12 diapositives"),
    ("QR_IA_04_Realiser_IA", "12 diapositives"),
    ("QR_IA_05_Premier_Projet_IA", "12 diapositives"),
]

BTN = ('  <a class="btn pdf" href="%s/%s.pptx" download>'
       '📊 Présentation (PPTX)</a>\n')


COMPTEUR = [0]


def dans_la_barre(s, nom):
    """Ajoute le bouton de presentation dans la barre de navigation du cours."""
    if "%s/%s.pptx" % (SORTIE_REL, nom) in s:
        return s, False
    m = re.search(r'(<nav class="navbar"[^>]*>.*?)(</nav>)', s, re.S)
    if not m:
        return s, False
    bloc = m.group(1)
    # juste avant la fermeture de la barre, apres le bouton precedent/suivant
    if 'class="btn pdf"' in bloc:
        nouveau = re.sub(r'((?:  <a class="btn pdf".*?</a>\n)+)',
                          lambda x: x.group(1) + BTN % (SORTIE_REL, nom),
                          bloc, count=1)
    else:
        nouveau = bloc + BTN % (SORTIE_REL, nom)
    COMPTEUR[0] += 1
    return s[:m.start(1)] + nouveau + s[m.end(1):], True


def carte_index(s, nom, n_diapos):
    """Ajoute une carte PPTX a la ligne du cours sur l'index du module."""
    if "%s/%s.pptx" % (SORTIE_REL, nom) in s:
        return s, False
    m = re.search(r'<a class="doc-item" href="%s\.html">.*?</a>' % re.escape(nom),
                  s, re.S)
    if not m:
        return s, False
    item = m.group(0)
    carte = ('<a class="doc-item doc-item--pptx" href="%s/%s.pptx" '
             'target="_blank" rel="noopener" download>'
             '<span class="doc-icon">📊</span><div class="doc-info">'
             '<div class="doc-title">Présentation PPTX</div>'
             '<div class="doc-date">%s</div></div>'
             '<div class="doc-badges">'
             '<span class="badge badge-pptx">PPT</span></div></a>'
             % (SORTIE_REL, nom, n_diapos))
    if nom == "QR_IA_01_Introduction_IA":
        # le cours 01 a deja sa carte, avec un lien vers les notes
        return s, False
    COMPTEUR[0] += 1
    return s[:m.start()] + '<div class="doc-row">' + item + carte + '</div>' \
        + s[m.end():], True


def main():
    for nom, n in COURS:
        p = os.path.join(DOSSIER, nom + ".html")
        pptx = os.path.join(DOSSIER, SORTIE_REL, nom + ".pptx")
        if not os.path.exists(pptx):
            print("  pas de présentation, page ignorée :", nom)
            continue
        s = open(p, encoding="utf-8").read()
        s, a = dans_la_barre(s, nom)
        open(p, "w", encoding="utf-8").write(s)
        print("  %-32s barre%s" % (nom, " +" if a else " (déjà là)"))

    idx = os.path.join(DOSSIER, "index.html")
    s = open(idx, encoding="utf-8").read()
    total = COMPTEUR[0]
    for nom, n in COURS:
        s, _ = carte_index(s, nom, n)
    open(idx, "w", encoding="utf-8").write(s)
    print("  index mis a jour : %d ajout(s)" % (COMPTEUR[0] - total))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
