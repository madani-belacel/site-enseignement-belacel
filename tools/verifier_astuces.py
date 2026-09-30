# -*- coding: utf-8 -*-
"""
verifier_astuces.py — empêche le nombre « N astuces » de dériver.

Pourquoi cet outil ?
    Le 29/09/2026, les pages d'accueil annonçaient « 34 astuces » alors
    que la page en contenait 152. Personne ne l'avait vu : le nombre
    est écrit à la main dans 10 fichiers différents.

    Cet outil, lui, COMPTE les vraies astuces et vérifie chaque
    mention. Il n'accepte que les nombres réellement constatés.

Deux modules coexistent (le dossier a été cloné puis enrichi) :
    cours/Module Intelligence Artificielle      → 152
    cours/Module_IA_Ameliore_150_astuces       → 150
Chacun a donc SON nombre, et les pages d'accueil citent celui du
module IA.

Usage :
    python3 verifier_astuces.py            # contrôle (code 1 si écart)
    python3 verifier_astuces.py --verbose  # affiche chaque mention
"""

import io
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RE_TIP = re.compile(r'class="tip-num"[^>]*>\s*(\d+)')
# Entre le nombre et le mot, il peut y avoir des balises :
#   « <strong>34</strong> Astuces »  ou  « &nbsp;34&nbsp;astuces »
# D'où les {0,3} alternatives (sinon \s+ ne matchait pas <strong>).
RE_MENTION = re.compile(
    r"(\d{1,4})(?:\s|</?[a-zA-Z][a-zA-Z0-9]*>|&nbsp;|&#160;){0,3}"
    r"(astuces|Astuces)\b")

# Une mention n'est un COMPTE que si elle est affirmative.
# « 152 astuces pour mieux profiter », « page des 152 astuces »,
# « + 34 astuces », « <strong>34</strong> Astuces »  → compte.
# « Prends 5 astuces aujourd'hui »                    → conseil, pas un compte.
RE_CLAIM = re.compile(
    r"(des\s*$|les\s*$|page\s+des\s*$|l'ensemble\s+des\s*$|\+\s*$|"
    r"<strong>\s*$|pour\s+(mieux|profit|apprendre|utiliser)\w*\s*$|"
    r"cumule\w*\s*$|total\s*$|contient\s+$)",
    re.I)


def html_files():
    for root, dirs, files in os.walk(BASE):
        dirs[:] = [d for d in dirs
                   if d not in (".git", "node_modules", "__pycache__",
                                ".backup-temp", "rapports-archives")]
        for f in sorted(files):
            if f.endswith(".html"):
                yield os.path.join(root, f)


def module_of(path):
    """Dossier du module IA auquel appartient `path`, ou None."""
    p = os.path.dirname(os.path.abspath(path))
    while p.startswith(BASE) and p != BASE:
        if os.path.isfile(os.path.join(p, "seances", "astuces-ia.html")):
            return p
        p = os.path.dirname(p)
    return None


def real_counts():
    """{dossier_module: nombre_réel}"""
    out = {}
    for root, dirs, files in os.walk(BASE):
        # « seances » est un sous-dossier : on le cherche dans dirs
        if "seances" not in dirs:
            continue
        p = os.path.join(root, "seances", "astuces-ia.html")
        if not os.path.isfile(p):
            continue
        s = io.open(p, encoding="utf-8").read()
        nums = [int(n) for n in RE_TIP.findall(s)]
        if nums:
            out[root] = len(set(nums))
    return out


def main():
    verbose = "--verbose" in sys.argv
    counts = real_counts()

    print("Compte réel des astuces, par module :")
    if not counts:
        print("   aucun module trouvé — rien à vérifier")
        return 1
    for path, n in sorted(counts.items()):
        rel = os.path.relpath(path, BASE)
        p = os.path.join(path, "seances", "astuces-ia.html")
        s = io.open(p, encoding="utf-8").read()
        nums = sorted(int(x) for x in RE_TIP.findall(s))
        holes = [i for i in range(1, len(nums) + 1) if i not in nums]
        dups = sorted({i for i in nums if nums.count(i) > 1})
        flag = "" if not (holes or dups) else \
            "  ATTENTION trous=%s doublons=%s" % (holes[:5], dups[:5])
        print("   %-46s %3d astuces (1→%d)%s"
              % (rel, n, max(nums) if nums else 0, flag))
        if holes or dups:
            print("      → le module lui-même est incohérent")
            return 1

    valides = set(counts.values())
    print()
    print("Mentions « N astuces » :")

    erreurs = 0
    for f in html_files():
        s = io.open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, BASE)
        mod = module_of(f)
        attendu = counts.get(mod) if mod else None
        for m in RE_MENTION.finditer(s):
            n, mot = int(m.group(1)), m.group(2)
            ligne = s.count("\n", 0, m.start()) + 1
            avant = s[max(0, m.start() - 70):m.start()]
            ctx = re.sub(r"<[^>]+>", "", s[max(0, m.start() - 45):m.end() + 15])
            ctx = re.sub(r"\s+", " ", ctx).strip()
            compte = bool(RE_CLAIM.search(avant))
            if not compte:
                # conseil (« Prends 5 astuces »), pas un total annoncé
                if verbose:
                    print("   L%-4d %-52s %3d  (mention, pas un compte)"
                          % (ligne, rel, n))
                continue
            if n not in valides:
                erreurs += 1
                print("   L%-4d %-52s %3d  <-- INVALIDE" % (ligne, rel, n))
                if verbose:
                    print("          …%s…" % ctx)
            elif verbose:
                cible = "OK" if (attendu is None or n == attendu) else \
                        "ATTENTION (module=%s)" % attendu
                print("   L%-4d %-52s %3d  %s" % (ligne, rel, n, cible))
                print("          …%s…" % ctx)

    print()
    if erreurs:
        print("%d mention(s) annoncent un nombre qui n'existe pas." % erreurs)
        print("Comptes réels disponibles :", sorted(valides))
        print()
        print("Le nombre doit être recopié depuis le compte réel du module,")
        print("pas écrit de mémoire. Corrige puis relance ce script.")
        return 1
    n_mentions = 0
    for f in html_files():
        n_mentions += len(RE_MENTION.findall(
            io.open(f, encoding="utf-8").read()))
    print("OK — %d mention(s) dans le site, toutes cohérentes avec un "
          "compte réel." % n_mentions)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
