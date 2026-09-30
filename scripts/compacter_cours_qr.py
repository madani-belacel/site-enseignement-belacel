#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compacte le bloc des 5 cours Q/R de la page du module IA.

Le bloc utilisait la même structure que `tic.html` (carte + carte PPTX côte
à côte) mais chaque cours affichait une description de deux lignes. Sur un
écran ordinary, la carte du cours poussait celle de la présentation hors du
cadre : la section prenait une demi-page de plus que celle du module TIC.

On garde la structure identique à `tic.html` — même ordre de badges, même
« Mise à jour » — et on ramène chaque description à une ligne courte. Les
descriptions détaillées restent dans les pages de cours elles-mêmes.

Idempotent : ne retouche rien si le format court est déjà en place.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "index.html")

DATE = "Mise à jour : Septembre 2026"

# numéro -> description courte (une ligne, sans point final)
COURTS = {
    "QR_IA_01_Introduction_IA.html":      "Les deux familles d'IA et comment elle travaille",
    "QR_IA_02_Comment_Fonctionne_IA.html": "Données, exemple, régularité : pourquoi elle se trompe",
    "QR_IA_03_Exemples_Simples_IA.html":  "Anti-spam, météo, recommandations, traduction, véhicules",
    "QR_IA_04_Realiser_IA.html":           "La méthode en 6 étapes, de l'idée au modèle entraîné",
    "QR_IA_05_Premier_Projet_IA.html":     "Mini-projet gratuit : classer des fleurs avec Colab",
}

# Une carte de cours = le fragment qui va de son href jusqu'au </a> qui la
# ferme. On travaille fragment par fragment plutôt qu'avec une seule
# expression régulière sur toute la page : la version précédente
# regroupait mal les groupes et laissait passer le nom de fichier dans le
# texte affiché.
CARTE = re.compile(
    r'<a class="doc-item" href="(?P<f>QR_IA_\d+[^"]*\.html)">(?P<corps>.*?)</a>',
    re.S)
DATE_DIV = re.compile(r'(<div class="doc-date">)(?P<texte>.*?)(</div>)', re.S)


def main():
    with open(PAGE, encoding="utf-8") as f:
        t = f.read()

    if DATE in t:
        print("Format court déjà en place : rien à faire.")
        return 0

    changes, erreurs = [], []

    def traiter(m):
        nom = os.path.basename(m.group("f"))
        court = COURTS.get(nom)
        if not court:
            return m.group(0)
        corps = m.group("corps")

        def date(d):
            # ne remplace que la date, sans toucher au reste du fragment
            if DATE in d.group("texte"):
                return d.group(0)
            return d.group(1) + court + d.group(3)

        nouveau, n = DATE_DIV.subn(date, corps)
        if n != 1:
            erreurs.append(nom)
            return m.group(0)
        changes.append(nom)
        return '<a class="doc-item" href="%s">%s</a>' % (m.group("f"), nouveau)

    nouvelle = CARTE.sub(traiter, t)

    # ordre des badges comme dans tic.html : FR, EN, puis le type
    nouvelle = re.sub(
        r'(<span class="badge badge-cours">Cours</span>)'
        r'(<span class="badge badge-qr">Q/R</span>)'
        r'(<span class="badge badge-fr">FR</span>)(<span class="badge badge-en">EN</span>)',
        r'\3\4\2\1', nouvelle)
    nouvelle = re.sub(
        r'(<span class="badge badge-tp">TP</span>)'
        r'(<span class="badge badge-qr">Q/R</span>)'
        r'(<span class="badge badge-fr">FR</span>)(<span class="badge badge-en">EN</span>)',
        r'\3\4\2\1', nouvelle)

    # Garde-fou : le nom du fichier ne doit pas apparaître comme TEXTE
    # affiché. Il est légitime dans les href, il ne l'est pas dans le texte —
    # c'est exactement le défaut que causedait la version précédente, donc on
    # contrôle le texte rendu et pas le HTML brut.
    rendered = re.sub(r"<[^>]+>", " ", nouvelle)
    for nom in changes:
        if os.path.basename(nom) in rendered:
            erreurs.append(nom)

    if erreurs:
        print("ÉCHEC — rien n'est écrit. Problème sur : %s" % ", ".join(erreurs))
        return 1

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(nouvelle)

    print("%d cartes compactées :" % len(changes))
    for c in changes:
        print("   %s" % c)
    print("Badges réordonnés comme dans tic.html (FR, EN, puis type).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
