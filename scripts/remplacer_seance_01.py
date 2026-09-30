#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Remplace la seance 01 par la version « 150 astuces », en gardant le
section « A retenir » de la version detaillee.

Un simple `cp` ferait perdre « A retenir » : la version courte ne l'a pas.
On la remet donc avant d'ecraser, sinon la seance perd une de ses syntheses.

Idempotent : le marqueur « A retenir » permet de relancer sans rien dupliquer.
"""
import os
import re
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURS = os.path.join(RACINE, "cours")
A = os.path.join(COURS, "Module Intelligence Artificielle", "seances", "seance-01.html")
B = os.path.join(COURS, "Module_IA_Ameliore_150_astuces", "seances", "seance-01.html")

# le bloc a sauver, de « A retenir » jusqu'au h2 suivant
GARDE = re.compile(
    r"[ \t]*<h2>✅ À retenir</h2>.*?(?=\n[ \t]*<h2>)", re.S)


def lire(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def ecrire(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


def main():
    for p in (A, B):
        if not os.path.isfile(p):
            print("Fichier introuvable : %s" % p)
            return 1

    mien = lire(A)
    if "Étape 5" in mien and "A retenir" not in mien.replace("À retenir", ""):
        pass  # deja remplace mais la synthese a bien ete remise

    if "Étape 5" in mien:
        garde = GARDE.search(mien)
        print("Séance 01 déjà remplacée%s."
              % ("" if garde else " — MAIS « À retenir » est absent !"))
        return 0 if garde else 1

    garde = GARDE.search(mien)
    if not garde:
        print("« À retenir » introuvable dans la version actuelle : abandon.")
        return 1
    bloc = garde.group(0)

    shutil.copyfile(B, A)
    fusion = lire(A)
    # on remet la synthese juste avant la checklist de fin de séance
    ancre = "<h2>✅ Checklist de fin de séance"
    i = fusion.find(ancre)
    if i < 0:
        i = fusion.find('<div class="nav-footer">')
    if i < 0:
        print("Point d'insertion introuvable : la copie est faite, "
              "« À retenir » reste à remettre.")
        return 1
    ecrire(A, fusion[:i] + bloc + "\n" + fusion[i:])

    final = lire(A)
    print("Séance 01 remplacée.")
    print("   « À retenir » remise  : %s" % ("oui" if "À retenir" in final else "NON"))
    print("   Étape 5 présente      : %s" % ("oui" if "Étape 5" in final else "NON"))
    print("   prompts conservés      : %d" % final.count("prompt-box"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
