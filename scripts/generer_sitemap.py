#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère le sitemap du site (format Google).

Résout les anomalies C3, C4, M8, M9 de l'audit :
  - inclut les pages principales manquantes (C3),
  - découpe en sitemaps par module + index sitemap (C4),
  - priorités réalistes (index=1.0, pages=0.8, séries=0.6, feuilles=0.4) (M8),
  - lastmod = vraie date de dernière modification des fichiers (M9).

Usage :  python3 scripts/generer_sitemap.py
"""
import datetime
import os
import re
import urllib.parse
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
BASE = "https://madani-belacel.github.io/site-enseignement-belacel"

PAGES_PRINCIPALES = [
    ("index.html", 1.0),
    ("enseignement.html", 0.8),
    ("tic.html", 0.8),
    ("informatique-ens.html", 0.8),
    ("recherche-documentaire.html", 0.8),
    ("reseaux.html", 0.8),
    ("recherche.html", 0.8),
    ("habilitation.html", 0.8),
    ("ressources.html", 0.8),
    ("contact.html", 0.8),
]

MODULES = {
    "dialogues-anglais": "cours/Dialogues_Anglais",
    "dialogues-tice": "cours/Dialogues_TICE",
    "examen-tic": "cours/Examen-TIC",
    "grammaire-anglaise": "cours/Grammaire Anglaise",
    "licence-1-anglais": "cours/Licence 1 Anglais",
    "informatique-ens": "cours/Module Informatique ENS",
    "intelligence-artificielle": "cours/Module Intelligence Artificielle",
    "recherche-articles": "cours/Module_Recherche_Articles",
    "recherche-documentaire": "cours/Module Recherche Documentaire",
    "reseaux-mostaganem": "cours/Module_Réseau_Mostaganem",
    "tic": "cours/Module TIC",
    "presentations": "cours/Présentations",
}


def lastmod(path):
    mtime = datetime.date.fromtimestamp(path.stat().st_mtime)
    return mtime.isoformat()


def urlset(entries):
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, lm, prio in entries:
        lignes.append("  <url>")
        lignes.append(f"    <loc>{loc}</loc>")
        lignes.append(f"    <lastmod>{lm}</lastmod>")
        lignes.append(f"    <priority>{prio}</priority>")
        lignes.append("  </url>")
    lignes.append("</urlset>")
    return "\n".join(lignes) + "\n"


def priorite(rel):
    segments = Path(rel).parts
    if segments[-1] == "index.html":
        return "0.6"
    if re.search(r"Niveau\s?\d", rel):
        return "0.5"
    return "0.4"


def collecter_module(repertoire):
    """Retourne les URLs HTML d'un module avec lastmod et priorité."""
    entrees = []
    if not repertoire.exists():
        return entrees
    for p in sorted(repertoire.rglob("*.html")):
        loc = urllib.parse.quote(str(p.relative_to(RACINE)).replace("\\", "/"))
        entrees.append((f"{BASE}/{loc}", lastmod(p), priorite(str(p.relative_to(RACINE)))))
    return entrees


def main():
    sitemaps = []

    # Pages principales : un seul sitemap
    entrees = [(BASE + "/" + f, lastmod(RACINE / f), str(p)) for f, p in PAGES_PRINCIPALES]
    nom = "sitemap-pages-main.xml"
    (RACINE / nom).write_text(urlset(entrees), encoding="utf-8")
    sitemaps.append(nom)
    print(f"{nom}: {len(entrees)} URLs")

    # Pages racine de cours/ (index et _index_*)
    entrees_cours = []
    for p in sorted((RACINE / "cours").glob("*.html")):
        loc = urllib.parse.quote(str(p.relative_to(RACINE)).replace("\\", "/"))
        entrees_cours.append((f"{BASE}/{loc}", lastmod(p), "0.6"))
    nom = "sitemap-cours-root.xml"
    (RACINE / nom).write_text(urlset(entrees_cours), encoding="utf-8")
    sitemaps.append(nom)
    print(f"{nom}: {len(entrees_cours)} URLs")

    # Un sitemap par module
    for cle, chemin in MODULES.items():
        entrees = collecter_module(RACINE / chemin)
        if not entrees:
            continue
        nom = f"sitemap-{cle}.xml"
        (RACINE / nom).write_text(urlset(entrees), encoding="utf-8")
        sitemaps.append(nom)
        print(f"{nom}: {len(entrees)} URLs")

    # Index sitemap
    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for nom in sitemaps:
        lignes.append("  <sitemap>")
        lignes.append(f"    <loc>{BASE}/{nom}</loc>")
        lignes.append(f"    <lastmod>{datetime.date.today().isoformat()}</lastmod>")
        lignes.append("  </sitemap>")
    lignes.append("</sitemapindex>")
    (RACINE / "sitemap-index.xml").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print("sitemap-index.xml:", len(sitemaps), "sitemaps")


if __name__ == "__main__":
    main()