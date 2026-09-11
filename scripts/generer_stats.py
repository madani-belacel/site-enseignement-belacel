#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Met à jour les statistiques du footer dans index.html.

Compte les fichiers réellement présents sous cours/ et remplace les
nombres en dur du footer (anomalie B6 de l'audit). À relancer à
chaque ajout de contenu :
    python3 scripts/generer_stats.py
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
COURS = RACINE / "cours"
INDEX = RACINE / "index.html"

REMPLACEMENTS = [
    ("2 764", "html", "Pages de cours"),
    ("10 466", "mp3", "Fichiers audio"),
    ("1 475", "pptx", "Présentations PPTX"),
]


def compter(ext):
    return sum(1 for p in COURS.rglob(f"*.{ext}") if p.is_file())


def formater(n):
    return f"{n:,}".replace(",", " ")


def main():
    texte = INDEX.read_text(encoding="utf-8")
    for ancien, ext, label in REMPLACEMENTS:
        nouveau = formater(compter(ext))
        balise = f'<span class="footer-stat-number">{ancien}</span>'
        if balise not in texte:
            print(f"⚠  {label}: balise '{balise}' introuvable, ignoré")
            continue
        texte = texte.replace(balise, f'<span class="footer-stat-number">{nouveau}</span>')
        print(f"✓ {label}: {nouveau}")
    INDEX.write_text(texte, encoding="utf-8")
    print("index.html mis à jour.")


if __name__ == "__main__":
    main()