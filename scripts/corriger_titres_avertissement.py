#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige le saut de niveau de titre dans l'avertissement.

L'avertissement commence en <h2> et enchaînait directement en <h4> : le
niveau <h3> était sauté, ce qui casse la navigation au clavier et la
structure annoncée par les lecteurs d'écran.

On passe donc ses titres en <h3>, et on leur donne un style : ils n'ont pas
la classe du bloc « astuce-detail » et seraient sinon en taille de paragraphe.

Idempotent : ne touche que le bloc situé entre les deux ancres.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "seances", "astuces-ia.html")

DEBUT = '<h2 id="avertissement-article">'
FIN = '<h2 id="limites">'

STYLE = """  .avertissement-corps h3 {
    font-family: var(--font-heading); font-size: 1.05rem; color: var(--navy);
    margin: 1.5rem 0 .5rem; padding-bottom: .3rem;
    border-bottom: 1px solid var(--border);
  }
  .avertissement-corps h3:first-of-type { margin-top: 1rem; }
"""


def main():
    with open(PAGE, encoding="utf-8") as f:
        t = f.read()

    i = t.find(DEBUT)
    j = t.find(FIN, i) if i >= 0 else -1
    if i < 0 or j < 0:
        print("Avertissement introuvable : rien à faire.")
        return 0

    bloc = t[i:j]
    if "<h3>" in bloc:
        print("Titres déjà corrigés.")
    else:
        bloc = re.sub(r"<h4>", "<h3>", bloc)
        bloc = re.sub(r"</h4>", "</h3>", bloc)
        # une classe pour pouvoir styler ces titres
        bloc = bloc.replace(DEBUT, DEBUT, 1)
        bloc = re.sub(
            r'(<h2 id="avertissement-article">[^<]*</h2>)',
            r'\1\n<div class="avertissement-corps">', bloc, count=1)
        bloc = bloc.rstrip() + "\n</div>\n\n"

        if ".avertissement-corps h3" not in t:
            bloc_style = STYLE
        else:
            bloc_style = ""

        t = t[:i] + bloc + t[j:]

        if bloc_style:
            k = t.find("</style>")
            t = t[:k] + bloc_style + t[k:]

        with open(PAGE, "w", encoding="utf-8") as f:
            f.write(t)
        print("Titres de l'avertissement passés en <h3>.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
