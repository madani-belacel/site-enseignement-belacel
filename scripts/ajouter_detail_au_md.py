#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute au fichier de travail la version publiee des pages de detail.

Le fichier contient un brouillon condense du Lot 1 (sections de 3 a 5 lignes).
La version publiee est nettement plus riche. On ne supprime rien : on ajoute
une section complete, en fin de fichier, avec le contenu tel qu'il est en
ligne — c'est la seule facon de disposer dans ce document de la reference
reelle du site.

Idempotent : si la section est deja presente, on ne fait rien.
"""
import html
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD = os.path.join(RACINE, "cours", "IA", "astuces-détaille",
                  "astuces-détaille.md")
DET = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                   "seances", "astuces-details")
MARQUEUR = "# VERSION PUBLIÉE DES PAGES DE DÉTAIL"

LOTS = [(1, [6, 12, 23, 35, 37]),
        (2, [36, 43, 44, 91, 100]),
        (3, [1, 7, 8, 9, 10])]


def corps(n):
    """Le contenu des 10 sections, tel qu'il est publié."""
    p = os.path.join(DET, "astuce-%03d.html" % n)
    if not os.path.isfile(p):
        return None, None
    t = open(p, encoding="utf-8").read()
    a = t.find('<div class="detail-corps">')
    b = t.find('<div class="detail-retour-bas">')
    if a < 0 or b < 0:
        return None, None
    # Le titre est le seul <h1> situe DANS le main : chercher le premier
    # <h1> du fichier attrapait celui de l'en-tete du site.
    main = t[t.find("<main"):]
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", main, re.S)
    if not h1:
        return None, None
    titre = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).strip()
    return titre, t[a + len('<div class="detail-corps">'):b].strip()


def bloc(n):
    titre, c = corps(n)
    if c is None:
        return None
    # Le h1 generator devient un titre de niveau 2, comme le brouillon du
    # fichier, et l'on retire l'emoji pour garder le meme rendu.
    titre = re.sub(r"^\W*\s*Astuce\s+\d+\s*—\s*", "Astuce %d — " % n, titre)
    return "## %s\n\n%s\n" % (titre, c)


def main():
    t = open(MD, encoding="utf-8").read()
    if MARQUEUR in t:
        print("Section deja presente : rien a faire.")
        return 0
    parties = []
    for n_lot, nums in LOTS:
        blocs = []
        for n in nums:
            b = bloc(n)
            if b:
                blocs.append(b)
        if blocs:
            parties.append("## Lot %d — astuces %s\n\n%s"
                           % (n_lot, ", ".join(str(x) for x in nums),
                              "\n---\n\n".join(blocs)))
    total = sum(len(blocs) for blocs in
                [[b for b in (bloc(n) for n in nums) if b] for _, nums in LOTS])
    entete = [
        MARQUEUR,
        "",
        "Ce qui suit est le contenu **exactement publié** sur le site, extrait",
        "des pages de `seances/astuces-details/`. C'est la version longue ; le",
        "Lot 1 plus haut dans ce fichier en est un brouillon condensé, conservé",
        "tel quel pour la trace.",
        "",
        "| Lot | Astuces | État |",
        "|-----|---------|------|",
        "| 1 | 6, 12, 23, 35, 37 | publié |",
        "| 2 | 36, 43, 44, 91, 100 | publié |",
        "| 3 | 1, 7, 8, 9, 10 | publié |",
        "",
        "Progression : **%d / 152** (%.1f %%). Restent les lots 4 a 30."
        % (total, 100.0 * total / 152),
        "",
        "Chaque page du site est a l'adresse :",
        "`cours/Module Intelligence Artificielle/seances/astuces-details/astuce-NNN.html`",
        "",
        "---",
        "",
    ]
    ajout = "\n".join(entete) + "\n".join(parties) + "\n"
    if not t.endswith("\n"):
        t += "\n"
    open(MD, "w", encoding="utf-8").write(t + "\n" + ajout)
    print("Pages ajoutees : %d" % total)
    print("Fichier       : %d octets" % os.path.getsize(MD))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
