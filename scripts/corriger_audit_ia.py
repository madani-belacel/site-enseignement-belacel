#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige les défauts trouvés par l'audit approfondi du module IA.

Quatre corrections, toutes vérifiables :

  1. « Curseur » → « Cursor » dans la séance 10. Curseur est le mot français
     pour le pointeur de souris ; ici c'est le nom de l'éditeur, qui ne
     s'écrit jamais avec un e.
  2. « Groq » Pradesh est le nom d'une société qui n'a rien à voir avec Grok.
     On précise, parce que les étudiants confondent les deux.
  3. Les titres d'étape qui n'affichaient pas leur durée la portent désormais,
     comme les 10 autres séances. Le professeur lit la liste des étapes sans
     avoir à calculer le temps.
  4. La description de la séance 01 dépasse la limite recommendée (168
     caractères) : Google la tronque dans les résultats.

Idempotent : chaque correction est ignorée si elle est déjà faite.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEANCES = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                       "seances")


def lire(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def ecrire(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


# 1 ---------------------------------------------------------------
def corriger_curseur():
    p = os.path.join(SEANCES, "seance-10.html")
    t = lire(p)
    if "Curseur" not in t:
        return 0
    t = t.replace("📍 Curseur →", "📍 Cursor →")
    ecrire(p, t)
    return t.count("📍 Cursor →")


# 2 ---------------------------------------------------------------
def preciser_groq():
    p = os.path.join(SEANCES, "astuces-ia.html")
    t = lire(p)
    if "Groq</strong> — accès gratuit" in t:
        return 0
    avant = ("<li><strong>OpenRouter, Groq, Hugging Face</strong> — accès gratuit "
             "à des modèles modernes.</li>")
    apres = ("<li><strong>OpenRouter, Groq, Hugging Face</strong> — accès gratuit "
             "à des modèles modernes. Attention : <strong>Groq</strong> (avec un q) "
             "n'est pas <strong>Grok</strong> (avec un k) : ce sont deux sociétés "
             "différentes.</li>")
    if avant not in t:
        return 0
    ecrire(p, t.replace(avant, apres, 1))
    return 1


# 3 ---------------------------------------------------------------
ETAPE = re.compile(
    r'(<h3>Étape[^<(]*?)(</h3>\s*<div class="step-meta">\s*<span>[^<]*</span>\s*'
    r'<span>⏱️\s*(\d+)\s*min\s*</span>)', re.S)


def ajouter_durees():
    n = 0
    for nom in sorted(os.listdir(SEANCES)):
        if not nom.startswith("seance-") or not nom.endswith(".html"):
            continue
        p = os.path.join(SEANCES, nom)
        t = lire(p)

        def ajouter(m):
            nonlocal n
            titre, suite, minutes = m.group(1), m.group(2), m.group(3)
            n += 1
            return "%s (%s min)%s" % (titre.rstrip(), minutes, suite)

        nouvelle = ETAPE.sub(ajouter, t)
        if nouvelle != t:
            ecrire(p, nouvelle)
    return n


# 4 ---------------------------------------------------------------
def raccourcir_description():
    p = os.path.join(SEANCES, "seance-01.html")
    t = lire(p)
    longue = ("Séance 01 pratique : ouvrir ChatGPT/Gemini, 5 prompts prêts à coller, "
              "formule magique du prompt, vérifier les hallucinations, comparer "
              "2 outils. Module IA 2e année PEP.")
    courte = ("Séance 01 : ouvrir ChatGPT ou Gemini, 5 prompts prêts à coller, "
              "formule du prompt, vérifier une réponse, comparer 2 outils.")
    if longue not in t:
        return 0
    ecrire(p, t.replace(longue, courte))
    return 1


def main():
    print("CORRECTIONS DE L'AUDIT APPROFONDI\n")
    print("  Curseur → Cursor        : %d" % corriger_curseur())
    print("  Groq vs Grok précisé     : %d" % preciser_groq())
    print("  Durées ajoutées aux titres : %d étapes" % ajouter_durees())
    print("  Description séance 01    : %d" % raccourcir_description())
    return 0


if __name__ == "__main__":
    sys.exit(main())
