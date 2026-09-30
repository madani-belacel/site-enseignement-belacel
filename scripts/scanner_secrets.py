#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cherche des secrets dans le depot : fichiers de travail ET historique git.

Motifs vises : jetons GitHub (ghp_/gho_/ghu_/ghs_/github_pat_), cles AWS
(AKIA...), mots de passe dans une URL, affectations de type
token = "..." ou password = "...".

Ne se trompe pas sur la sortie : certains echos sont des exemples
pedagogiques (un cours qui explique `api_key = ...`). ChaqueFound est donc
a relire.

Usage : python3 scanner_secrets.py [racine] [--historique]
"""
import os
import re
import subprocess
import sys

RACINE = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") \
    else os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
HISTORIQUE = "--historique" in sys.argv

# Chaque motif : (nom, expression, criticite)
MOTIFS = [
    ("jeton GitHub classique (ghp_/gho_/ghu_/ghs_)",
     re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"), "CRITIQUE"),
    ("jeton GitHub fin (github_pat_)",
     re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"), "CRITIQUE"),
    ("cle AWS (AKIA…)",
     re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "CRITIQUE"),
    ("secret Google (AIza…)",
     re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}\b"), "CRITIQUE"),
    ("mot de passe dans une URL",
     re.compile(r"://[^/\s:@]{1,40}:[^/\s:@]{1,40}@"), "CRITIQUE"),
    ("affectation de secret",
     re.compile(r"(?i)\b(api[_-]?key|secret|passwd|password|mot_de_passe|"
                r"access[_-]?token|bearer[_-]?token)\b\s*[:=]\s*"
                r"[\"'][^\"'\s]{12,}[\"']"), "A VERIFIER"),
]

A_EXCLURE = {".git", "node_modules", "__pycache__", ".venv", "vendor"}
FICHIERS_SENSIBLES = (".env", ".env.local", ".npmrc", ".netrc", "id_rsa",
                      ".htpasswd", "credentials", "secrets.yml", "secrets.yaml")


def Scanner(source, origine, trouve):
    for nom, rx, crit in MOTIFS:
        for m in rx.finditer(source):
            frag = source[max(0, m.start() - 40):m.end() + 20]
            ligne = source.count("\n", 0, m.start()) + 1
            trouve.append((crit, nom, origine, ligne,
                           m.group(0)[:12] + "…" + m.group(0)[-4:],
                           " ".join(frag.split())[:110]))


def main():
    trouve = []
    n_fichiers = 0

    # --- 1. fichiers de travail ---
    for d, sous, noms in os.walk(RACINE):
        sous[:] = [x for x in sous if x not in A_EXCLURE]
        for n in noms:
            p = os.path.join(d, n)
            rel = os.path.relpath(p, RACINE)
            if any(n == f or n.endswith(f) for f in FICHIERS_SENSIBLES):
                trouve.append(("CRITIQUE", "fichier sensible versionné", rel, 0,
                               n, "present dans le depot"))
            if not n.endswith((".html", ".js", ".css", ".py", ".json", ".md",
                               ".txt", ".yml", ".yaml", ".sh", ".xml", ".csv")):
                continue
            try:
                s = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            n_fichiers += 1
            Scanner(s, rel, trouve)

    # --- 2. historique git ---
    n_commits = 0
    if HISTORIQUE:
        try:
            commits = subprocess.run(
                ["git", "-C", RACINE, "log", "--all", "--format=%H"],
                capture_output=True, text=True, timeout=600).stdout.split()
            n_commits = len(commits)
            for c in commits:
                # du contenu binaire peut se cacher dans un diff : on decode
                # en ignorant les octets invalides plutot que d'abandonner
                brut = subprocess.run(
                    ["git", "-C", RACINE, "show", c,
                     "--unified=0", "--no-color"],
                    capture_output=True, timeout=600).stdout
                Scanner(brut.decode("utf-8", "ignore"), "commit %s" % c[:9],
                        trouve)
        except Exception as e:
            print("historique non analyse :", e)

    # --- rapport ---
    if not trouve:
        print("Aucun secret detecte.")
        print("  %d fichiers texte analyses%s"
              % (n_fichiers,
                 " · %d commits" % n_commits if HISTORIQUE else ""))
        return 0

    critiques = [t for t in trouve if t[0] == "CRITIQUE"]
    autres = [t for t in trouve if t[0] != "CRITIQUE"]
    print("=== %d correspondance(s) : %d critique(s), %d a verifier ==="
          % (len(trouve), len(critiques), len(autres)))
    print()
    for titre, lot in (("CRITIQUES", critiques), ("A VERIFIER", autres)):
        if not lot:
            continue
        print("--", titre, "--")
        vus = set()
        for crit, nom, origine, ligne, extrait, ctx in lot:
            cle = (nom, extrait)
            if cle in vus:
                continue
            vus.add(cle)
            print("  [%s] %s" % (crit, nom))
            print("     %s%s" % (origine, " ligne %d" % ligne if ligne else ""))
            print("     extrait : %s" % extrait)
            print("     contexte: %s" % ctx)
        print()
    return 1 if critiques else 0


if __name__ == "__main__":
    sys.exit(main())
