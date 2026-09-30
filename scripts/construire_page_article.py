#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construit « article-scientifique.html » à partir d'une page existante.

Prend une page du module comme squelette (en-tête, pied de page, feuille de
style, script) et n'en garde que la structure, en remplaçant le contenu par
le texte de l'avertissement. Reprend le chemin du modèle tel quel : la page
nouvelle est écrite dans le même dossier que le modèle, donc les chemins
relatifs restent corrects sans rien recalculer.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle")
SEANCES = os.path.join(MODULE, "seances")
MODELE = os.path.join(SEANCES, "seance-11.html")
ASTUCES = os.path.join(SEANCES, "astuces-ia.html")
CIBLE = os.path.join(SEANCES, "article-scientifique.html")

TITRE = "L'IA et l'article scientifique — le risque à connaître"
CANON = ("https://madani-belacel.github.io/site-enseignement-belacel/"
         "cours/Module%20Intelligence%20Artificielle/seances/"
         "article-scientifique.html")
DESCRIPTION = ("Ce que l'IA peut changer dans un article scientifique sans "
               "qu'on s'en aperçoive : chiffres inventés, références "
               "fictives, formules modifiées. La règle d'or, la méthode de "
               "travail sûre et les prompts à copier. Module Intelligence "
               "Artificielle, 2e année PEP.")


def lire(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def ecrire(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


def corps_avertissement():
    """Récupère le bloc depuis le script qui l'avait inséré, plutôt que de
    le couper de la page des astuces : le texte reste ainsi dans une seule
    source, et l'extraction est stable même si la page a déjà été nettoyée."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ajouter_avertissement_ia import BLOC
    return BLOC.strip()


def main():
    src = lire(MODELE)
    corps = corps_avertissement()

    # 1. squelette : tout ce qui précède <main>, puis l'en-tête
    main_o = src.find('<main class="page-content" id="main-content">')
    header_d = src.find('<header class="header"')
    header_f = src.find("</header>") + len("</header>")
    footer_d = src.find('<footer class="footer"')
    if -1 in (main_o, header_d, footer_d):
        print("Le modèle n'a pas la structure attendue.")
        return 1
    footer_f = src.find("</body>")

    tete = src[:main_o]
    tete = re.sub(r"<title>.*?</title>", "<title>%s</title>" % TITRE, tete, flags=re.S)
    tete = re.sub(r'<meta name="description"[^>]*>', "", tete)
    tete = re.sub(r'<link rel="canonical"[^>]*>',
                  '<link rel="canonical" href="%s">' % CANON, tete)
    tete = tete.replace(
        "<title>%s</title>" % TITRE,
        '<title>%s</title>\n  <meta name="description" content="%s">'
        % (TITRE, DESCRIPTION), 1)
    for balise in ('<meta property="og:title"[^>]*>',
                   '<meta property="og:description"[^>]*>',
                   '<meta name="twitter:title"[^>]*>',
                   '<meta name="twitter:description"[^>]*>'):
        tete = re.sub(balise, "", tete)

    # Le gabarit porte déjà un <h1> (« Séance 11 — … ») dans l'en-tête de
    # page. On le remplace : deux <h1> dans une page est une erreur
    # d'accessibilité, et le second serait lu comme un titre concurrent.
    tete = re.sub(r"<h1>[^<]*</h1>", "<h1>%s</h1>" % TITRE, tete, count=1)
    tete = re.sub(r"<h1><div class=\"container\">", "", tete)
    tete = tete.replace(
        '<div class="container"><h1>%s</h1>' % TITRE,
        '<div class="container"><h1>%s</h1>' % TITRE, 1)

    milieu = """
<main class="page-content" id="main-content">
  <div class="content-wrapper">
    <nav class="breadcrumb" aria-label="Fil d'Ariane">
      <ol>
        <li><a href="../index.html">Module IA</a></li>
        <li><a href="index.html">Séances</a></li>
        <li class="current">Article scientifique</li>
      </ol>
    </nav>
%s
  </div>
</main>
""" % ("\n".join("  " + l if l.strip() else l for l in corps.split("\n")))

    # Le bloc de l'avertissement est écrit en <h2> + <h4> parce qu'il devait
    # tenir dans une page de 152 astuces. Sur une page de contenu, le <h1>
    # est déjà celui du titre : l'avertissement reste un <h2>, et ses 15
    # sections passent en <h3>. C'est la hiérarchie attendue par les lecteurs
    # d'écran et par l'audit d'accessibilité.
    milieu = milieu.replace("<h4>", "<h3>").replace("</h4>", "</h3>")

    # style des titres de section, absent du gabarit
    milieu += """
  <style>
    .avertissement-corps h3 {
      font-family: var(--font-heading); font-size: 1.05rem; color: var(--navy);
      margin: 1.6rem 0 .5rem; padding-bottom: .3rem;
      border-bottom: 1px solid var(--border);
    }
    .avertissement-corps h3:first-of-type { margin-top: 1rem; }
  </style>
"""

    ecrire(CIBLE, tete + milieu + src[footer_d:footer_f]
           + "\n</body>\n</html>\n")
    print("Page écrite : %s" % os.path.relpath(CIBLE, RACINE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
