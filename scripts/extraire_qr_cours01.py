#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extrait les questions/reponses du Cours 01 depuis la page Q/R.

Le contenu vient de la page, jamais recopie : le cahier de questions du deck
et la page Q/R du site ne peuvent ainsi pas diverger.

Usage : python3 scripts/extraire_qr_cours01.py
Ecrit  scripts/contenus_details_qr/qr_cours01.json
"""
import html
import json
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "QR_IA_01_Introduction_IA.html")
SORTIE = os.path.join(RACINE, "scripts", "contenus_details_qr",
                      "qr_cours01.json")


def txt(s):
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def main():
    t = open(PAGE, encoding="utf-8").read()
    idees = []
    for im in re.finditer(r'<article class="qr-idea">(.*?)</article>', t, re.S):
        b = im.group(1)
        tag = re.search(r'<span class="qr-tag">(.*?)</span>', b, re.S)
        fr = re.search(r'<span class="lang-fr">(.*?)</span>', b, re.S)
        expl = re.search(r'<p class="qr-expl lang-fr">(.*?)</p>', b, re.S)
        qa = []
        for qm in re.finditer(
                r'<div class="qr-item">(.*?)</div>\s*(?=<div class="qr-item">|</div>)',
                b, re.S):
            qb = qm.group(1)
            paires = {}
            for langue in ("fr", "en"):
                q = re.search(r'class="qr-q lang-%s"[^>]*>(.*?)</p>' % langue,
                              qb, re.S)
                r = re.search(r'class="qr-r lang-%s"[^>]*>(.*?)</p>' % langue,
                              qb, re.S)
                if q and r:
                    paires[langue] = (txt(q.group(1)), txt(r.group(1)))
            if "fr" in paires:
                qa.append({"q": paires["fr"][0], "r": paires["fr"][1],
                           "qen": paires.get("en", ("", ""))[0],
                           "ren": paires.get("en", ("", ""))[1]})
        idees.append({"tag": txt(tag.group(1)) if tag else "",
                      "titre": txt(fr.group(1)) if fr else "",
                      "explication": txt(expl.group(1)) if expl else "",
                      "qa": qa})
    os.makedirs(os.path.dirname(SORTIE), exist_ok=True)
    with open(SORTIE, "w", encoding="utf-8") as f:
        json.dump(idees, f, ensure_ascii=False, indent=1)
    print("  idees     : %d" % len(idees))
    print("  questions : %d" % sum(len(i["qa"]) for i in idees))
    print("  ecrit     : %s" % SORTIE)


if __name__ == "__main__":
    main()