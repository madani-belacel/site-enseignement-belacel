#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liste les ancres mortes d'un dossier de pages HTML.

audit_liens.py compte les liens morts sans les detailler. Ici on veut la
liste exacte : page source, cible, ancre manquante. Sert a reparer les
menus et les boutons « retour » qui pointent vers un #id inexistant.

Usage : python3 lister_ancres_mortes.py [racine]
"""
import os
import re
import sys
from collections import defaultdict
from html import unescape

BALISE = re.compile(r"<(a|button|span|li|td|th|div)\b([^>]*)>", re.I)
LIEN = re.compile(r"""(?:href|data-href|onclick\s*=)\s*=?\s*["']([^"']+)["']""", re.I)
ID_HTML = re.compile(r"""\bid\s*=\s*["']([^"']+)["']""", re.I)
NOM_ANCRE = re.compile(r"""<a\b[^>]*\bname\s*=\s*["']([^"']+)["']""", re.I)


def ids_de(page):
    with open(page, encoding="utf-8", errors="replace") as f:
        texte = f.read()
    return (set(ID_HTML.findall(texte)) |
            set(NOM_ANCRE.findall(texte)) |
            {i.lower() for i in ID_HTML.findall(texte)})


def main():
    racine = sys.argv[1] if len(sys.argv) > 1 else "."
    pages = []
    for dossier, _, fichiers in os.walk(racine):
        pages += [os.path.join(dossier, f) for f in fichiers
                  if f.lower().endswith(".html")]
    if not pages:
        print("Aucune page HTML trouvee dans %s" % racine)
        return 1

    cache = {p: {i.lower() for i in ids_de(p)} for p in pages}
    problemes = defaultdict(list)

    def ids_cible(chemin):
        # La cible peut sortir du dossier audite (ex. ../../index.html) :
        # on lit alors le fichier sur place plutot que de le declarer mort.
        if chemin not in cache and os.path.isfile(chemin):
            cache[chemin] = {i.lower() for i in ids_de(chemin)}
        return cache.get(chemin)

    for page in pages:
        with open(page, encoding="utf-8", errors="replace") as f:
            texte = f.read()
        for balise in BALISE.finditer(texte):
            brut = unescape(balise.group(2))
            for cible in LIEN.findall(brut):
                if "#" not in cible:
                    continue
                fichier, _, ancre = cible.partition("#")
                if not ancre:
                    continue
                ancre = ancre.lower()
                # « #ancre » : la page elle-meme
                if not fichier:
                    if ancre not in cache[page]:
                        problemes[page].append(cible)
                    continue
                # « autre/page.html#ancre » : resoudre comme un navigateur
                if re.match(r"^[a-z]+://|^//|^mailto:", fichier, re.I):
                    continue
                if fichier.endswith("/"):
                    fichier += "index.html"
                cible_page = os.path.normpath(
                    os.path.join(os.path.dirname(page), fichier))
                if not os.path.isfile(cible_page):
                    continue          # fichier absent : deja signale ailleurs
                if ancre not in (ids_cible(cible_page) or ()):
                    problemes[page].append(cible)

    total = sum(len(v) for v in problemes.values())
    if not total:
        print("OK — aucune ancre morte dans %d pages (%s)" % (len(pages), racine))
        return 0

    print("ANCRES MORTES : %d dans %d pages\n" % (total, len(problemes)))
    for page in sorted(problemes):
        print("%s" % page)
        for a in sorted(set(problemes[page])):
            print("    %s   (%d fois)" % (a, problemes[page].count(a)))
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
