#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insère un bouton dépliant « explication détaillée » sous chaque astuce.

Le bouton est un <details>/<summary> natif : il marche sans JavaScript, au
clavier, et reste lisible même si js/main.v2.js ne se charge pas. Le
contenu déplié vient de scripts/astuces_detail.py.

Seules les astuces qui ont une explication reçoivent un bouton : un
bouton vide devant 151 astuces sans texte donnerait l'impression que le
travail est fait.

Le script est idempotent : relancer ne duplique rien.
Usage : python3 ajouter_boutons_astuces.py
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from astuces_detail import ASTUCES                     # noqa: E402

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "seances", "astuces-ia.html")

DEBUT = re.compile(r'^<h3><span class="tip-num">(\d+)</span>')
FIN = re.compile(r"^<h[23][ >]")
MARQUEUR = "astuce-detail"
# un bloc deja insere, pour pouvoir le remplacer quand l'explication change
EXISTANT = re.compile(
    r'\n?<details class="%s">.*?</details>\n' % MARQUEUR, re.S)

STYLE = """
/* ---- bouton « explication détaillée » d'une astuce ------------------ */
.astuce-detail { margin: .8rem 0 1.6rem; }
.astuce-detail > summary {
  display: inline-block; cursor: pointer; list-style: none;
  background: var(--primary); color: #fff; font-family: var(--font-heading);
  font-weight: 600; font-size: .82rem; padding: .4rem 1rem; border-radius: 999px;
  border: 1px solid var(--primary); transition: background .2s;
}
.astuce-detail > summary::-webkit-details-marker { display: none; }
.astuce-detail > summary:hover { background: var(--primary-hover); }
.astuce-detail > summary:focus-visible {
  outline: 2px solid var(--primary-dark); outline-offset: 2px;
}
.astuce-detail[open] > summary { background: var(--green); border-color: var(--green); }
.astuce-detail-corps {
  margin-top: .8rem; padding: 1.1rem 1.3rem;
  background: var(--bg-alt); border: 1px solid var(--border);
  border-left: 4px solid var(--primary); border-radius: var(--radius);
}
.astuce-detail-corps h4 {
  font-family: var(--font-heading); font-size: 1rem; color: var(--navy);
  margin: 1.2rem 0 .4rem;
}
.astuce-detail-corps h4:first-child { margin-top: 0; }
.astuce-detail-corps ul, .astuce-detail-corps ol { margin: .4rem 0 .6rem 1.2rem; }
.astuce-detail-corps li { margin: .22rem 0; line-height: 1.7; }
.astuce-detail-corps pre {
  background: var(--bg-card); border: 1px solid var(--border);
  border-radius: var(--radius); padding: .8rem .9rem; margin: .6rem 0;
  overflow-x: auto; font-size: .85rem; line-height: 1.6;
  font-family: var(--font-mono);
}
.astuce-detail-corps pre code { background: none; padding: 0; }
.astuce-detail-corps table {
  width: 100%; border-collapse: collapse; margin: .7rem 0; font-size: .9rem;
}
.astuce-detail-corps th, .astuce-detail-corps td {
  border: 1px solid var(--border); padding: .45rem .55rem; text-align: left;
}
.astuce-detail-corps th { background: var(--bg-card); font-family: var(--font-heading); }
"""


def bloc(numero, corps):
    return (
        '\n<details class="%s">\n'
        '  <summary>🔍 Comprendre l\'astuce %s en détail</summary>\n'
        '  <div class="%s-corps">%s  </div>\n'
        '</details>\n' % (MARQUEUR, numero, MARQUEUR, corps.strip() + "\n")
    )


def main():
    with open(PAGE, encoding="utf-8") as f:
        lignes = f.readlines()

    # la feuille de style du bouton
    if ".astuce-detail" not in "".join(lignes):
        for i, l in enumerate(lignes):
            if l.strip() == "</style>":
                lignes.insert(i, STYLE)
                break
        else:
            print("Aucune balise </style> : le bouton marcherait sans mise en forme.")
            return 1

    sorties, inserees, remplacees, ignorees = [], 0, 0, []
    sortie = sorties                     # raccourci de lecture
    i = 0
    while i < len(lignes):
        ligne = lignes[i]
        m = DEBUT.match(ligne)
        if not m:
            sortie.append(ligne)
            i += 1
            continue

        numero = int(m.group(1))
        # fin de l'astuce : prochaine balise h2 ou h3
        j = i + 1
        while j < len(lignes) and not FIN.match(lignes[j]):
            j += 1
        contenu = lignes[i:j]
        sortie += contenu

        if numero in ASTUCES:
            nouveau = bloc(numero, ASTUCES[numero])
            # un bloc deja present occupe PLUSIEURS lignes : de <details> a
            # </details>. Il faut retirer toutes ces lignes, pas seulement la
            # premiere, sinon l'ancien corps reste et casse l'imbrication.
            ouverture = fermeture = None
            for k, l in enumerate(contenu):
                if ouverture is None and "<details" in l:
                    ouverture = k
                if ouverture is not None and "</details>" in l:
                    fermeture = k
                    break
            if ouverture is None:
                sortie.append(nouveau)
                inserees += 1
            else:
                debut = len(sortie) - len(contenu) + ouverture
                sortie[debut:debut + (fermeture - ouverture + 1)] = [nouveau]
                remplacees += 1
        elif not any(MARQUEUR in l for l in contenu):
            ignorees.append(numero)
        i = j

    with open(PAGE, "w", encoding="utf-8") as f:
        f.writelines(sortie)

    total = sum(1 for l in lignes if DEBUT.match(l))
    print("Astuces sur la page      : %d" % total)
    print("Boutons insérés          : %d" % inserees)
    print("Boutons mis à jour       : %d" % remplacees)
    print("Explications rédigées    : %d" % len(ASTUCES))
    print("Encore à rédiger         : %d" % len(ignorees))
    if ignorees:
        apercu = ", ".join(str(n) for n in ignorees[:20])
        print("   sans explication : %s%s" % (apercu, "…" if len(ignorees) > 20 else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
