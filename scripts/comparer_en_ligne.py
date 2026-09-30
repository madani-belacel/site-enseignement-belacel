#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare le site en ligne (GitHub Pages) avec la version locale.

Repond a une question simple : « est-ce que le site en ligne est bon, et
est-il a jour de ce que j'ai fait sur mon ordinateur ? »
"""
import subprocess
import sys
import urllib.request

BASE = "https://madani-belacel.github.io/site-environnement-belacel"
BASE = "https://madani-belacel.github.io/site-enseignement-belacel"

PAGES = [
    ("Page d'accueil", "/"),
    ("Index du module IA",
     "/cours/Module%20Intelligence%20Artificielle/index.html"),
    ("Cours IA 01",
     "/cours/Module%20Intelligence%20Artificielle/QR_IA_01_Introduction_IA.html"),
    ("Présentation PPTX du cours IA 01",
     "/cours/Module%20Intelligence%20Artificielle/Presentations_PPTX/"
     "QR_IA_01_Introduction_IA.pptx"),
    ("Présentation PPTX du cours IA 02",
     "/cours/Module%20Intelligence%20Artificielle/Presentations_PPTX/"
     "QR_IA_02_Comment_Fonctionne_IA.pptx"),
    ("Page 404", "/page-qui-nexiste-pas.html"),
]

MARQUEURS = [
    ("lien vers la présentation PPTX", "Presentations_PPTX/"),
    ("lien vers les notes PDF", "_notes.pdf"),
    ("barre de navigation entre cours", 'class="navbar"'),
    ("sélecteur de langue", "lang-bar"),
]


def http(url):
    req = urllib.request.Request(url, headers={"User-Agent": "audit-site"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:
        return 0, str(e).encode()


def main():
    print("Site en ligne : %s" % BASE)
    print()
    for libelle, chemin in PAGES:
        code, corps = http(BASE + chemin)
        etat = {200: "en ligne", 404: "introuvable", 403: "interdit",
                0: "pas de reponse"}.get(code, "code %d" % code)
        print("  %-42s %s" % (libelle, etat))
        if code == 200 and chemin.endswith(".html"):
            page = corps.decode("utf-8", "ignore")
            for nom, sig in MARQUEURS:
                if sig in page:
                    print("        contient : %s" % nom)
    print()
    etat_commits = subprocess.run(["git", "log", "--oneline", "-1"],
                                  capture_output=True, text=True)
    nb = subprocess.run(["git", "rev-list", "--count", "HEAD"],
                        capture_output=True, text=True).stdout.strip()
    modifie = subprocess.run(["git", "status", "--porcelain"],
                             capture_output=True, text=True).stdout.count("\n")
    print("Sur votre ordinateur :")
    print("  dernier commit   : %s" % (etat_commits.stdout.strip() or "aucun"))
    print("  commits au total : %s" % nb)
    print("  fichiers modifies non envoyes : %d" % modifie)
    return 0


if __name__ == "__main__":
    sys.exit(main())
