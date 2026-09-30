#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit des liens et des ressources du site.

Pour chaque page HTML :
  - verifie que chaque lien interne pointe vers un fichier existant ;
  - verifie que chaque ancre (#id) existe dans la page visee ;
  - verifie que chaque ressource (img, script, css, lien de telechargement,
    url() de <style>) existe sur le disque ;
  - signale les target="_blank" sans rel="noopener".

Les chemins sont resolus comme un navigateur le ferait : une URL absolue
(http/https) est comptee a part, une ancre seule est verifiee dans la page
elle-meme, le reste est teste sur le disque (un repertoire compte comme
present : href="." est valide).

Usage : python3 audit_liens.py [racine]
Sortie : JSON sur stdout.
"""
import json
import os
import re
import sys
from collections import Counter
from html import unescape
from urllib.parse import unquote, urlparse

RACINE = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

HREF = re.compile(r'<a\b[^>]*?\bhref\s*=\s*("([^"]*)"|\'([^\']*)\'|([^\s>]+))', re.I)
SRC = re.compile(r'<(?:img|script|source|iframe|video|audio|embed)\b[^>]*?\bsrc\s*=\s*'
                 r'("([^"]*)"|\'([^\']*)\'|([^\s>]+))', re.I)
SRCSET = re.compile(r'\bsrcset\s*=\s*("([^"]*)"|\'([^\']*)\')', re.I)
LINK = re.compile(r'<link\b[^>]*?\bhref\s*=\s*("([^"]*)"|\'([^\']*)\')', re.I)
CSSURL = re.compile(r'url\(\s*(["\']?)([^)"\']+)\1\s*\)', re.I)
ID = re.compile(r'\bid\s*=\s*("([^"]*)"|\'([^\']*)\')', re.I)
STYLE = re.compile(r"<style[^>]*>(.*?)</style>", re.S | re.I)

EXTERNES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:", "data:")


def val(m):
    """Valeur d'un attribut, quel que soit le guillemet utilise."""
    for g in m.groups()[1:]:
        if g is not None:
            return unescape(g)
    return ""


def resoudre(dossier, chemin):
    return os.path.normpath(os.path.join(dossier, unquote(chemin).lstrip("/")))


def main():
    fichiers = []
    for d, sous, noms in os.walk(RACINE):
        sous[:] = [s for s in sous if s not in (".git", "node_modules", "__pycache__")]
        for n in noms:
            fichiers.append(os.path.normpath(os.path.join(d, n)))

    html = {}
    for p in fichiers:
        if not p.endswith(".html"):
            continue
        try:
            html[p] = open(p, encoding="utf-8", errors="ignore").read()
        except OSError:
            pass

    ancres = {}
    for p, s in html.items():
        ens = set()
        for m in ID.finditer(s):
            v = m.group(2) if m.group(2) is not None else m.group(1)
            if v:
                ens.add(unescape(v))
        ancres[p] = ens

    def ancres_de(cible):
        """Ancres de la page cible, lue sur place si elle est hors du dossier
        audite. Sans cela, un lien vers ../../index.html#about est declare mort
        alors que le fichier existe : le cache ne contient que les pages
        balayees, pas leurs cibles."""
        if cible not in ancres and os.path.isfile(cible):
            ens = set()
            try:
                with open(cible, encoding="utf-8", errors="replace") as f:
                    for m in ID.finditer(f.read()):
                        v = m.group(2) if m.group(2) is not None else m.group(1)
                        if v:
                            ens.add(unescape(v))
            except OSError:
                pass
            ancres[cible] = ens
        return ancres.get(cible, ())

    liens = liens_morts = ressources = manquantes = externes = 0
    sans_noopener = 0
    familles = Counter()
    exemples = {}

    def note(famille, detail):
        familles[famille] += 1
        exemples.setdefault(famille, detail)

    for p, s in html.items():
        dossier = os.path.dirname(p)

        for m in HREF.finditer(s):
            brut = val(m)
            if not brut:
                continue
            if brut.startswith(EXTERNES):
                externes += 1
                if 'target="_blank"' in m.group(0) and "noopener" not in m.group(0):
                    sans_noopener += 1
                    note("target_blank sans noopener", "%s -> %s" % (p, brut))
                continue
            liens += 1
            if brut.startswith("#"):
                cible, ancre = p, brut[1:]
            else:
                u = urlparse(brut)
                chemin, ancre = unquote(u.path), unquote(u.fragment)
                cible = p if not chemin else resoudre(dossier, chemin)
            if not os.path.exists(cible):
                liens_morts += 1
                note("lien mort", "%s -> %s" % (p, brut))
            elif ancre and ancre not in ancres_de(cible):
                liens_morts += 1
                note("ancre morte", "%s -> %s" % (p, brut))

        for rx in (SRC, SRCSET):
            for m in rx.finditer(s):
                if rx is SRCSET:
                    brut = m.group(2) if m.group(2) is not None else m.group(3)
                    valeurs = [unescape(x.strip().split()[0])
                               for x in (brut or "").split(",") if x.strip()]
                else:
                    valeurs = [val(m)]
                for v in valeurs:
                    v = v.strip() if isinstance(v, str) else ""
                    if not v or v.startswith(EXTERNES):
                        if v.startswith(("http://", "https://", "//")):
                            externes += 1
                        continue
                    ressources += 1
                    if not os.path.exists(resoudre(dossier, urlparse(v).path)):
                        manquantes += 1
                        note("ressource manquante", "%s -> %s" % (p, v))

        for m in LINK.finditer(s):
            v = unescape(m.group(2) if m.group(2) is not None else (m.group(3) or ""))
            if not v or v.startswith(EXTERNES):
                if v.startswith(("http://", "https://", "//")):
                    externes += 1
                continue
            ressources += 1
            if not os.path.exists(resoudre(dossier, urlparse(v).path)):
                manquantes += 1
                note("ressource manquante (link)", "%s -> %s" % (p, v))

        for m in STYLE.finditer(s):
            for u in CSSURL.finditer(m.group(1)):
                v = u.group(2).strip()
                if not v or v.startswith(EXTERNES) or v.startswith("data:"):
                    continue
                ressources += 1
                if not os.path.exists(resoudre(dossier, urlparse(v).path)):
                    manquantes += 1
                    note("ressource manquante (css)", "%s -> %s" % (p, v))

    print(json.dumps({
        "html_files": len(html),
        "liens_verifies": liens,
        "liens_morts": liens_morts,
        "ressources_verifiees": ressources,
        "ressources_manquantes": manquantes,
        "liens_externes": externes,
        "target_blank_sans_noopener": sans_noopener,
        "familles_d_anomalies": len(familles),
        "exemples": dict(exemples),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
