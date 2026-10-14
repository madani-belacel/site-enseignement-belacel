#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dans les sections « Travaux Dirigés », remplace la carte Présentation PPTX
par une pastille PDF.

Pourquoi : chaque TD dispose de trois fichiers — le HTML, le PDF et le PPTX —
mais la page ne proposait que le HTML et le PPTX. Le PDF, version la plus
pratique à imprimer, n'était lié nulle part : un fichier orphelin.

Deux precautions :

  * la pastille PDF est posee en frere de la carte, jamais a l'interieur. Un
    <a> dans un <a> est invalide, et le navigateur peut alors telecharger le
    mauvais fichier ;
  * le traitement se fait ligne par ligne, en suivant la profondeur des <div>,
    pour ne pas toucher aux lignes de la section « Serie Officielle » qui
    Contains exactement les memes balises.

La pastille reutilise .access-badge, deja definie dans css/style.css.

Idempotent : relancer ne duplique rien.
Usage : python3 td_html_et_pdf.py tic.html [autre.html ...]
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUT_LIGNE = '<div class="doc-row">'
CARTE_PPTX = '<a class="doc-item doc-item--pptx"'
PASTILLE = ('<a class="access-badge td-pdf" href="%s" target="_blank" '
            'rel="noopener" download title="TD en PDF">PDF</a>')


def fin_ligne(t, depart):
    """Index de la balise </div> qui ferme le doc-row ouvert avant."""
    prof = 1
    for m in re.finditer(r"<div\b[^>]*>|</div>", t[depart:]):
        prof += -1 if m.group(0).startswith("</") else 1
        if prof == 0:
            return depart + m.start()
    return -1


def traiter_ligne(ligne):
    """Sur une seule ligne de TD : retire le PPTX, ajoute le PDF."""
    if CARTE_PPTX not in ligne:
        return ligne, False, False
    m = re.search(r'href="([^"]*_FR\.html)"', ligne)
    if not m:
        return ligne, False, False
    pdf = m.group(1)[:-5] + ".pdf"
    if not os.path.isfile(os.path.join(RACINE, pdf)):
        # pas de PDF : on retire quand meme la carte PPTX
        nouveau = re.sub(r"\s*" + re.escape(CARTE_PPTX) + r"[^>]*>.*?</a>",
                         "", ligne, flags=re.S)
        return nouveau, True, False
    # la carte PPTX est la derniere avant la fermeture de la ligne
    nouveau = re.sub(r"\s*" + re.escape(CARTE_PPTX) + r"[^>]*>.*?</a>\s*(?=</div>)",
                     "", ligne, flags=re.S)
    if "td-pdf" not in nouveau:
        nouveau = re.sub(r"(\s*</div>\s*)$",
                         "\n  " + (PASTILLE % pdf) + r"\1", nouveau)
    return nouveau, True, True


def traiter(chemin, section):
    with open(chemin, encoding="utf-8") as f:
        t = f.read()
    i = t.find('id="%s"' % section)
    if i < 0:
        return 0, 0
    j = t.find("<h2", i + 10)
    if j < 0:
        j = len(t)
    bloc, pos, n_pptx, n_pdf = [], i, 0, 0
    for m in re.finditer(re.escape(DEBUT_LIGNE), t[i:j]):
        # finditer rend des positions relatives a la tranche : on rebascule en
        # absolu, sinon l'on decoupe au mauvais endroit et rien ne change.
        debut = i + m.start()
        if debut < pos:
            continue
        fin = fin_ligne(t, i + m.end())
        if fin < 0 or fin > j:
            continue
        # fin_ligne renvoie la position de la balise fermante : il faut
        # l'inclure, sinon la tranche s'arrete avant le </div> et les
        # deux substitutions ne peuvent plus s'appliquer.
        ligne, a, b = traiter_ligne(t[debut:fin + len("</div>")])
        n_pptx += a
        n_pdf += b
        bloc.append(t[pos:debut])
        bloc.append(ligne)
        pos = fin + len("</div>")
    if not n_pptx and not n_pdf:
        return 0, 0
    bloc.append(t[pos:j])
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(t[:i] + "".join(bloc) + t[j:])
    return n_pptx, n_pdf


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    for chemin in sys.argv[1:]:
        if not os.path.isfile(chemin):
            print("  %s : absent" % chemin)
            continue
        avant = open(chemin, encoding="utf-8").read()
        n_pptx, n_pdf = traiter(chemin, "td-title")
        apres = open(chemin, encoding="utf-8").read()
        etat = "deja a jour" if avant == apres else \
            "cartes PPTX retirees %d, pastilles PDF ajoutees %d" % (n_pptx, n_pdf)
        print("  %-22s : %s" % (os.path.basename(chemin), etat))
    return 0


if __name__ == "__main__":
    sys.exit(main())