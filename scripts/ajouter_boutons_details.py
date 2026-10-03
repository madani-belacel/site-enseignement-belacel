#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ajoute le bouton « Voir l'explication détaillée » sous chaque astuce
qui dispose d'une page dans le dossier astuces-details/.

Deux pièges corrigés dans cette version :

  * la structure est  <h3><span class="tip-num">N</span> Titre</h3>
                       <div class="astuce-bloc"> … </div>
    Le numéro est donc dans le h3 qui précède le div, pas à l'intérieur.
    Une première version cherchait `tip-num` dans le bloc et attrapait le
    numéro de l'astuce suivante — d'où un bouton mal placé et une astuce
    sans bouton.

  * le bloc contient des <div> imbriqués (prompt-box, exemple, warn, ok) :
    on ne peut pas chercher le dernier </div> du fragment, il faut suivre la
    profondeur pour trouver celui qui ferme vraiment le astuce-bloc.

Idempotent : relancer ne duplique rien.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEANCES = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                       "seances")
PAGE = os.path.join(SEANCES, "astuces-ia.html")
DETAILS = os.path.join(SEANCES, "astuces-details")

CSS = """
  /* bouton « explication détaillée » */
  .btn-detail {
    display: inline-block; padding: .5rem 1rem;
    background: var(--primary, #146fa9); color: #fff; text-decoration: none;
    border-radius: 6px; font-weight: 600; font-size: .88rem;
    margin-top: .9rem; border: 1px solid var(--primary, #146fa9);
    transition: background .2s;
  }
  .btn-detail:hover { background: #0d5a8a; border-color: #0d5a8a; }
  .detail-indispo {
    display: inline-block; margin-top: .9rem; padding: .5rem 1rem;
    background: var(--bg-alt, #f4f6f8); color: var(--text-muted, #5f6e80);
    border-radius: 6px; font-size: .85rem;
    border: 1px dashed var(--border, #dfe5ea);
  }
"""

DEBUT_ASTUCE = re.compile(
    r'(<h3><span class="tip-num">(\d+)</span>.*?</h3>\s*'
    r'<div class="astuce-bloc">)')


def pages_disponibles():
    return {int(m.group(1))
            for m in (re.match(r"astuce-(\d+)\.html$", f)
                       for f in os.listdir(DETAILS)) if m}


def trouver_fermeture(t, depart):
    """Index du </div> qui ferme le astuce-bloc ouvert juste avant."""
    profondeur = 1
    for m in re.finditer(r"<div\b[^>]*>|</div>", t[depart:]):
        profondeur += -1 if m.group(0).startswith("</") else 1
        if profondeur == 0:
            return depart + m.start()
    return -1


def main():
    if not os.path.isdir(DETAILS):
        print("Dossier astuces-details/ absent : rien a faire.")
        return 0

    dispo = pages_disponibles()
    with open(PAGE, encoding="utf-8") as f:
        t = f.read()

    if ".btn-detail" not in t:
        if "</style>" not in t:
            print("Aucun bloc <style> : ajout impossible.")
            return 1
        t = t.replace("</style>", CSS + "</style>", 1)

    out, pos = [], 0
    actifs = en_prep = deja = 0
    for m in DEBUT_ASTUCE.finditer(t):
        n = int(m.group(2))
        fin = trouver_fermeture(t, m.end())
        if fin < 0:
            continue
        out.append(t[pos:m.end()])
        corps = t[m.end():fin]
        if "btn-detail" in corps or "detail-indispo" in corps:
            deja += 1
        elif n in dispo:
            corps += ('\n  <a class="btn-detail" '
                      'href="astuces-details/astuce-%03d.html">'
                      '🔍 Voir l\'explication détaillée</a>\n' % n)
            actifs += 1
        else:
            corps += ('\n  <span class="detail-indispo">'
                      '🔍 Explication détaillée — en préparation</span>\n'
                      % ())
            en_prep += 1
        out.append(corps)
        pos = fin
    out.append(t[pos:])

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write("".join(out))

    print("Astuces traitees        : %d / 152" % (actifs + en_prep + deja))
    print("Boutons actifs          : %d" % actifs)
    print("Boutons « en préparation » : %d" % en_prep)
    print("Deja en place           : %d" % deja)
    print("Pages de detail         : %d" % len(dispo))
    return 0


if __name__ == "__main__":
    sys.exit(main())