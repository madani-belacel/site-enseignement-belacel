#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fusionne les deux versions du module Intelligence Artificielle.

Deux dossiers existent :
  « Module Intelligence Artificielle »      → 42 astuces, seances tres detaillees
  « Module_IA_Ameliore_150_astuces »        → 150 astuces, seances alleglees

Objectif : garder la richestesse de chaque cote.

  - la page des astuces : on part de la version 42 (elle a l'en-tete du site,
    la feuille de style, le drapeau, le lien d'evitement et la liste des 15
    seances) et on remplace le corps des 42 astuces par les 150 de l'autre ;
  - les seances : on garde la version detaillee et on y ajoute la « Checklist »
    de la version 150, absente des deux autres.

Le script est idempotent : le relancer ne fait rien de plus.
"""
import os
import re
import shutil
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURS = os.path.join(RACINE, "cours")
SRC = os.path.join(COURS, "Module Intelligence Artificielle")
AUTRE = os.path.join(COURS, "Module_IA_Ameliore_150_astuces")

ASTUCES = os.path.join("seances", "astuces-ia.html")
MARQUEUR = "tip-num"          # present seulement apres la fusion


def lire(chemin):
    with open(chemin, encoding="utf-8") as f:
        return f.read()


def ecrire(chemin, texte):
    with open(chemin, "w", encoding="utf-8") as f:
        f.write(texte)


def bloc_entre(texte, debut, fin, avant_fin=True):
    """Retourne le texte situe entre deux reperes, ou None."""
    i = texte.find(debut)
    if i < 0:
        return None
    j = texte.find(fin, i + len(debut))
    if j < 0:
        return None
    return texte[i:j] if avant_fin else texte[i:j + len(fin)]


# --------------------------------------------------------------------------
# 1. la page des astuces
# --------------------------------------------------------------------------
def fusionner_astuces():
    chemin = os.path.join(SRC, ASTUCES)
    mien = lire(chemin)
    sien = lire(os.path.join(AUTRE, ASTUCES))

    if MARQUEUR in mien:
        print("   astuce : deja fusionne, ignore")
        return 0

    # le bloc 150, de la 1re categorie au dernier réflexe (avant son pied de page)
    corps_150 = bloc_entre(sien, '<h2 id="limites">', '<footer class="page-footer">')
    if corps_150 is None:
        print("   astuce : bloc 150 introuvable, abandon")
        return 1

    # mes 42, du titre au sommaire des 15 seances (que l'on garde intact)
    debut_mien = mien.find('<h2>💡 42 astuces')
    fin_mien = mien.find('<h2 id="seances">')
    if debut_mien < 0 or fin_mien < 0 or fin_mien < debut_mien:
        print("   astuce : bornes du fichier actuel introuvables, abandon")
        return 1
    prologue = mien[:debut_mien]      # head + en-tete du site
    epilogue = mien[fin_mien:]        # liste des 15 seances + pied de page

    # le sommaire des 21 categories, reconstruit depuis la version 150
    categories = re.findall(r'<h2 id="([a-z0-9-]+)">([^<]+)</h2>', corps_150)
    if not categories:
        print("   astuce : aucune categorie trouvee, abandon")
        return 1
    liens = " ·\n    ".join(
        '<a href="#%s">%s</a>' % (i, t.strip().split(" ", 1)[-1]) for i, t in categories)

    # les 2 gestes de la version 42 absents des 150, places dans leur categorie
    gains = '''
<h2 id="bonus">⏱️ Deux gestes qui font gagner du temps</h2>
<h3><span class="tip-num">151</span> Transformer un texte en fichier audio MP3</h3>
<p>L'IA ne parle pas, mais certains sites savent le faire. Demande : <strong>« Transforme ce texte en fichier audio MP3 que je puisse écouter dans le bus. »</strong> Tu obtiens un fichier à écouter en marchant, au lieu de lire.</p>
<div class="prompt-box">Ce texte :
[colle ton texte]
Transforme-le en audio MP3, vitesse normale, sans ajouté ni commentaire.</div>
<div class="tip"><strong>Pourquoi :</strong> un cours de 45 minutes s'écoute en 40 minutes dans les transports. C'est le meilleur usage de l'IA pour un étudiant.</div>
<h3><span class="tip-num">152</span> Dicter au lieu d'écrire</h3>
<p>Écrire au clavier est lent. Tous les claviers de téléphone ont un micro : dicte ton idée à l'IA, puis demande-lui de la mettre en forme.</p>
<div class="prompt-box">Voici ce que j'ai dicté, mal ponctué :
[texte brut]
Récris-le proprement, garde mes mots, ne rajoute aucune idée.</div>
<div class="warn"><strong>Attention :</strong> dicter est plus rapide que taper, mais relis toujours. Une dictée mal comprise devient une erreur que tu ne vois plus.</div>
'''
    corps_150 = corps_150.replace(
        '<h2 id="api-dev">', gains.strip() + '\n<h2 id="api-dev">', 1)

    corps = (
        '  <h2>💡 152 astuces pour mieux profiter de l\'IA</h2>\n'
        '  <p class="subtitle">Module Intelligence Artificielle — 2ème année PEP '
        '· ENS Université de Mostaganem</p>\n'
        '\n'
        '  <div class="info-box">\n'
        '    <p><strong>Objectif unique</strong> : reconnaître chaque astuce et '
        'l\'utiliser. Zéro théorie, uniquement des gestes et des prompts à coller.</p>\n'
        '    <p>Prends 5 astuces aujourd\'hui, applique-les 7 jours, puis reviens '
        'en prendre 5 autres. Une astuce <em>faite</em> vaut mieux que 150 lues.</p>\n'
        '    <p><strong>%d catégories :</strong></p>\n'
        '    <p>    %s</p>\n'
        '  </div>\n\n'
        '%s\n%s' % (len(categories) + 1, liens, corps_150.rstrip(), epilogue)
    )

    # les 6 classes que la version 150 declare et que la 42 ne connait pas
    if ".tip-num" not in mien:
        styles = '''  .tip-num { display: inline-block; background: #146fa9; color: #fff;
    font-weight: 700; font-size: .85rem; padding: .15rem .5rem;
    border-radius: 4px; margin-right: .45rem; vertical-align: middle; }
  .reflexe { background: #e8f5e9; border-left: 4px solid #2e7d32;
    padding: .65rem 1rem; margin: .6rem 0 1rem; border-radius: 0 6px 6px 0;
    font-size: .95rem; }
  .reflexe strong { color: #1b5e20; }
  .sommaire { background: #f0f7fc; border: 1px solid #c5dff0;
    border-radius: 10px; padding: 1rem 1.2rem; margin: 1.2rem 0 2rem; }
  .sommaire a { color: #146fa9; text-decoration: none; margin-right: .6rem; }
  .sommaire a:hover { text-decoration: underline; }
  .nav-top { font-size: .9rem; margin-bottom: 1.2rem; }
  .nav-top a { color: #146fa9; }
'''
        prologue = prologue.replace("</style>", styles + "</style>", 1)

    ecrire(chemin, prologue + corps)
    return 2


# --------------------------------------------------------------------------
# 2. la checklist de chaque seance
# --------------------------------------------------------------------------
CHECKLIST = re.compile(
    r'<h2>✅ Checklist[^<]*</h2>\s*\n<div class="retenir">\s*\n<ul>.*?</ul>\s*\n</div>',
    re.S)


def extraire_checklist(texte):
    m = CHECKLIST.search(texte)
    return m.group(0) if m else None


def inserer_checklist(texte, bloc):
    """Place la checklist juste avant le quiz de la seance."""
    for repere in ("<h2>🧠 Quiz", "<h2>📚 Quiz", "<div class=\"nav-footer\">"):
        i = texte.find(repere)
        if i >= 0:
            return texte[:i] + "  " + bloc.replace("\n", "\n  ") + "\n\n" + texte[i:]
    return None


def fusionner_seances():
    ajoutees, sans = 0, []
    for n in range(1, 16):
        nom = "seance-%02d.html" % n
        chemin = os.path.join(SRC, "seances", nom)
        if not os.path.isfile(chemin):
            continue
        mien = lire(chemin)
        if "✅ Checklist" in mien:
            continue
        sien = lire(os.path.join(AUTRE, "seances", nom))
        bloc = extraire_checklist(sien)
        if not bloc:
            sans.append(nom)
            continue
        fusion = inserer_checklist(mien, bloc)
        if fusion is None:
            sans.append(nom)
            continue
        ecrire(chemin, fusion)
        ajoutees += 1
    return ajoutees, sans


# --------------------------------------------------------------------------
# 3. les liens des seances vers la page des astuces
# --------------------------------------------------------------------------
def corriger_liens():
    n = 0
    for seance in range(1, 16):
        chemin = os.path.join(SRC, "seances", "seance-%02d.html" % seance)
        if not os.path.isfile(chemin):
            continue
        t = lire(chemin)
        if "astuces-ia.html#cat-9" in t:
            ecrire(chemin, t.replace("astuces-ia.html#cat-9",
                                     "astuces-ia.html#code"))
            n += 1
    return n


def main():
    if not os.path.isdir(AUTRE):
        print("Dossier source introuvable : %s" % AUTRE)
        return 1
    print("FUSION DU MODULE INTELLIGENCE ARTIFICIELLE\n")
    r = fusionner_astuces()
    print("   astuce : %s" % ("150 + 2 integrates" if r == 2 else
                              "deja fait" if r == 0 else "ECHEC"))
    a, s = fusionner_seances()
    print("   seances : %d checklist(s) ajoutee(s)" % a)
    if s:
        print("   sans checklist : %s" % ", ".join(s))
    print("   liens : %d corriges (#cat-9 -> #code)" % corriger_liens())
    return 0


if __name__ == "__main__":
    sys.exit(main())
