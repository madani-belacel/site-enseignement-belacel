#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met à jour les statistiques de contenu affichées dans index.html.

Compte les fichiers réellement présents sous ``cours/`` puis remplace les
valeurs associées à leur libellé. Le script ne modifie plus le fichier si
au moins une statistique attendue est introuvable.

Usage :
    python3 scripts/generer_stats.py
"""
from pathlib import Path
import re
import sys

RACINE = Path(__file__).resolve().parent.parent
COURS = RACINE / "cours"
INDEX = RACINE / "index.html"

STATISTIQUES = [
    ("html", "Pages de cours"),
    ("mp3", "Fichiers audio"),
    ("pptx", "Présentations PPTX"),
]


def compter(extension: str) -> int:
    return sum(1 for p in COURS.rglob(f"*.{extension}") if p.is_file())


def formater(nombre: int) -> str:
    return f"{nombre:,}".replace(",", " ")


def main() -> int:
    texte = INDEX.read_text(encoding="utf-8")
    nouveau_texte = texte
    erreurs: list[str] = []

    for extension, libelle in STATISTIQUES:
        nombre = formater(compter(extension))
        motif = re.compile(
            r'(<span class="footer-stat-number">)[^<]+'
            r'(</span>\s*<span class="footer-stat-label">' + re.escape(libelle) + r'</span>)'
        )
        nouveau_texte, remplacements = motif.subn(
            rf'\g<1>{nombre}\g<2>', nouveau_texte, count=1
        )
        if remplacements != 1:
            erreurs.append(f"{libelle}: statistique introuvable dans index.html")
            continue
        print(f"✓ {libelle}: {nombre}")

    if erreurs:
        for erreur in erreurs:
            print(f"⚠ {erreur}", file=sys.stderr)
        print("Aucune modification écrite.", file=sys.stderr)
        return 1

    INDEX.write_text(nouveau_texte, encoding="utf-8")
    print("index.html mis à jour.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
