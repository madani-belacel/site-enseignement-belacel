#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sors l'avertissement « l'IA et l'article scientifique » de la page des
astuces, et donne-lui sa propre page.

Pourquoi : le texte était collé en tête de la liste des 152 astuces, ce qui
le faisait lire comme une astuce parmi d'autres alors qu'il concerne
uniquement la rédaction d'un article. Il deserveait sa propre adresse,
consultable depuis le sommaire du module.

Ce que fait le script :
  1. retire le bloc de la page des astuces (entre <h2 id="avertissement-article">
     et le <h2 id="limites"> suivant) ;
  2. crée « article-scientifique.html » à la racine du module, avec le même
     en-tête et le même pied de page que les autres pages du site ;
  3. ajoute un lien vers cette page dans le sommaire du module.

Idempotent.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle")
ASTUCES = os.path.join(MODULE, "seances", "astuces-ia.html")
INDEX = os.path.join(MODULE, "index.html")
NOUVELLE = os.path.join(MODULE, "article-scientifique.html")
MODELE = os.path.join(MODULE, "seances", "seance-11.html")

TITRE = "L'IA et l'article scientifique — le risque à connaître"
CANON = ("https://madani-belacel.github.io/site-enseignement-belacel/"
         "cours/Module%20Intelligence%20Artificielle/article-scientifique.html")
DESCRIPTION = ("Ce que l'IA peut changer dans un article scientifique sans "
               "qu'on s'en aperçoive : chiffres inventés, références fictives, "
               "formules modifiées. La règle d'or, la méthode de travail sûre "
               "et les prompts à utiliser. Module Intelligence Artificielle, "
               "2e année PEP.")


def lire(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def ecrire(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


def extraire_bloc(t):
    i = t.find('<h2 id="avertissement-article">')
    if i < 0:
        return None
    j = t.find('<h2 id="limites">', i)
    if j < 0:
        return None
    bloc = t[i:j]
    # le <div class="avertissement-corps"> ouvert par le script d'insertion
    return re.sub(r"</?div[^>]*>", "", bloc).rstrip() + "\n"


def construire_page(corps, chrome):
    # chrome : l'en-tête et le pied de page d'une page existante du site
    return chrome.replace("<title>", "<title>%s</title>" % TITRE) \
        .replace("<main class=\"page-content\" id=\"main-content\">",
                 "<main class=\"page-content\" id=\"main-content\">"
                 "<div class=\"content-wrapper\">"
                 '<nav class="breadcrumb" aria-label="Fil d\'Ariane">'
                 '<ol><li><a href="index.html">Module IA</a></li>'
                 '<li class="current">Article scientifique</li></ol></nav>'
                 "%s</div>" % corps)


def main():
    if not os.path.isfile(ASTUCES):
        print("Page des astuces introuvable.")
        return 1

    t = lire(ASTUCES)
    bloc = extraire_bloc(t)
    if not bloc:
        print("Le bloc n'est plus dans la page des astuces : rien à faire.")
        return 0

    # 1. retrait de la page des astuces
    i = t.find('<h2 id="avertissement-article">')
    j = t.find('<h2 id="limites">', i)
    t = t[:i] + t[j:]
    ecrire(ASTUCES, t)
    print("1. bloc retiré de la page des astuces")

    # 2. page dédiée, avec l'en-tête et le pied de page du site
    if not os.path.isfile(NOUVELLE):
        src = lire(MODELE)
        d = src.find('<header class="header"')
        f = src.find('<footer class="footer"')
        if d < 0 or f < 0:
            print("2. en-tête ou pied de page introuvable : abandon")
            return 1
        chrome = src[d:f]
        # on retablit le <main> et le </main> autour de la zone de contenu
        main_o = src.find('<main class="page-content" id="main-content">')
        main_f = src.find("</main>")
        chrome = ('<main class="page-content" id="main-content">\n'
                  + chrome + "\n</main>\n")
        page = construire_page(bloc, chrome)
        # métadonnées propres à la page
        head = (src[:main_o])
        head = re.sub(r"<title>.*?</title>", "<title>%s</title>" % TITRE,
                      head, flags=re.S)
        head = re.sub(r'<meta name="description"[^>]*>', "", head)
        head = re.sub(r'<link rel="canonical"[^>]*>',
                      '<link rel="canonical" href="%s">' % CANON, head)
        head = head.replace("<main", "<main", 1)
        # insère la description juste après <title>
        head = head.replace(
            "<title>%s</title>" % TITRE,
            '<title>%s</title>\n<meta name="description" content="%s">'
            % (TITRE, DESCRIPTION), 1)
        # remplace la partie <main> du gabarit par la nôtre
        idx = head.find('<main class="page-content" id="main-content">')
        head = head[:idx] + page
        ecrire(NOUVELLE, head)
        print("2. page creee : article-scientifique.html")
    else:
        print("2. page deja presente")

    # 3. lien depuis le sommaire du module
    idx = lire(INDEX)
    ancre = '<a class="level-item" href="#seances">'
    if 'article-scientifique.html' not in idx and ancre in idx:
        lien = ('<a class="level-item" href="article-scientifique.html">'
                '<span class="level-name">📄 Article scientifique — '
                'ce que l’IA peut fausser</span>'
                '<span class="level-count">Avertissement + méthode</span></a>\n    ')
        idx = idx.replace(ancre, lien + ancre, 1)
        ecrire(INDEX, idx)
        print("3. lien ajoute au sommaire du module")
    else:
        print("3. lien deja present ou ancre introuvable")
    return 0


if __name__ == "__main__":
    sys.exit(main())
