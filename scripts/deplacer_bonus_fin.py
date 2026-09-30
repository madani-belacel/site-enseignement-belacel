#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remet les deux « gestes bonus » (astuces 151 et 152) à la fin de la page.

Pourquoi : à la fusion, ces deux astuces ont été ajoutées dans la catégorie
« Sécurité » pour ne pas casser la numérotation existante. Résultat, un
lecteur rencontrait « 100 », puis « 151 », « 152 », puis « 101 ».

Le correctif est un déplacement, pas une renumérotation : renuméroter
152 astuces casserait les renvois, les ancres et les boutons déjà posés.
Déplacer le bloc suffit à rendre la lecture monotone.

La catégorie porte déjà son titre (« Deux gestes qui font gagner du
temps ») : elle reste compréhable même à la fin.

Idempotent.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "seances", "astuces-ia.html")

DEBUT = '<h2 id="bonus">'
FIN = '<h2 id="api-dev">'


def main():
    with open(PAGE, encoding="utf-8") as f:
        t = f.read()

    i = t.find(DEBUT)
    if i < 0:
        print("Bloc « bonus » introuvable : rien à faire.")
        return 0
    j = t.find(FIN, i)
    if j < 0:
        print("Catégorie suivante introuvable : abandon.")
        return 1

    bloc = t[i:j].rstrip() + "\n\n"
    reste = t[:i] + t[j:]

    # on le réinsère juste avant la liste des 15 séances
    ancre = '<h2 id="seances">'
    k = reste.find(ancre)
    if k < 0:
        print("Section « 15 séances » introuvable : abandon.")
        return 1

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(reste[:k] + bloc + reste[k:])

    print("Bloc déplacé à la fin de la liste des astuces.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
