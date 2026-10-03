#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Générateur des pages « explication détaillée » des 152 astuces.

Le générateur prend toute la charpente en charge : en-tête, fil d'Ariane,
pied de page, navigation précédent/suivant, canonical, feuille de style. Le
contenu rédigé à la main arrive en 10 sections, et rien d'autre.

Le but est d'éviter 152 fois la même coquille HTML : une faute invisible
dans le contenu mais qui casse le rendu.

Usage :
    python3 generateur_details_astuces.py            # génère tout
    python3 generateur_details_astuces.py 6 12 23    # seulement celles-là
"""
import os
import re
import sys
import urllib.parse

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEANCES = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                       "seances")
SOURCE = os.path.join(SEANCES, "astuces-ia.html")
MODELE = os.path.join(SEANCES, "seance-11.html")
DEST = os.path.join(SEANCES, "astuces-details")
CONTENU = os.path.join(RACINE, "scripts", "contenus_details")

BASE = ("https://madani-belacel.github.io/site-enseignement-belacel/"
        "cours/Module%20Intelligence%20Artificielle/seances/astuces-details/")

RUBRIQUES = ["1. Le texte source", "2. Explication phrase par phrase",
             "3. Une analogie pour comprendre",
             "4. Les composants décomposés",
             "5. Application pratique — cas complet",
             "6. Le réflexe à retenir", "7. Erreurs fréquentes à éviter",
             "8. Résumé en une image", "9. Ce que tu dois retenir",
             "10. Sans / Avec — comparaison"]

STYLE = """
  /* ── pages « explication détaillée » ───────────────────────────────── */
  .detail-nav { display: flex; justify-content: space-between; flex-wrap: wrap;
    gap: .5rem; margin: 1.5rem 0; }
  .detail-nav a { color: #146fa9; text-decoration: none; font-weight: 600;
    padding: .5rem .9rem; border-radius: 6px; background: #e3f2fd; }
  .detail-nav a:hover { background: #bbdefb; }
  .detail-retour { display: inline-block; margin: 0 0 1.2rem; color: #146fa9;
    font-weight: 600; text-decoration: none; }
  .detail-retour:hover { text-decoration: underline; }
  .detail-retour-haut { display: flex; align-items: center; gap: 1rem;
    flex-wrap: wrap; margin-bottom: 1.4rem; padding-bottom: 1rem;
    border-bottom: 1px solid #e1e8ed; }
  .detail-retour-bas { margin-top: 2.5rem; padding-top: 1.2rem;
    border-top: 1px solid #e1e8ed; display: flex; align-items: center;
    gap: 1rem; flex-wrap: wrap; }
  .detail-retour-bas .detail-nav { flex: 1 1 100%; margin-bottom: .4rem; }
  .detail-corps h2 { margin: 2rem 0 .6rem; padding-bottom: .3rem;
    border-bottom: 1px solid #e1e8ed; }
  .detail-corps pre { background: #1e293b; color: #e2e8f0; padding: 1rem 1.1rem;
    border-radius: 8px; overflow-x: auto; font-size: .84rem; line-height: 1.55; }
  .detail-corps pre code { background: none; color: inherit; padding: 0; }
  .detail-corps table { width: 100%; border-collapse: collapse; margin: .9rem 0;
    font-size: .92rem; }
  .detail-corps th, .detail-corps td { border: 1px solid #e1e8ed; padding: .55rem .7rem;
    text-align: left; vertical-align: top; }
  .detail-corps th { background: #f4f6f8; }
  .detail-corps .reflexe { background: #e8f5e9; border-left: 4px solid #2e7d32;
    padding: .8rem 1.1rem; border-radius: 0 6px 6px 0; margin: 1rem 0; }
  .detail-corps .warn { background: #fff3e0; border-left: 4px solid #ef6c00;
    padding: .8rem 1.1rem; border-radius: 0 6px 6px 0; margin: 1rem 0; }
  .detail-corps .ok { background: #e8f5e9; border-left: 4px solid #00875b;
    padding: .8rem 1.1rem; border-radius: 0 6px 6px 0; margin: 1rem 0; }
  .detail-corps .phrase { border-left: 3px solid #e1e8ed; padding-left: .9rem;
    margin: .9rem 0; }
  .detail-corps .phrase strong { color: #146fa9; }
  .detail-corps .schema { background: #f8fafc; border: 1px solid #e1e8ed;
    padding: 1rem; border-radius: 8px; overflow-x: auto; }
"""


def lire(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def titres_astuces():
    t = lire(SOURCE)
    out = {}
    for b in re.split(r'(?=<h3><span class="tip-num">\d+<)', t):
        m = re.match(r'<h3><span class="tip-num">(\d+)</span>([^<]*)</h3>', b)
        if m:
            out[int(m.group(1))] = m.group(2).strip()
    return out


def source_astuce(n):
    """Le bloc HTML de l'astuce, recopié depuis la page des astuces.

    On retire le bouton « explication détaillée » : il a été ajouté à la page
    des astuces par ajouter_boutons_details.py, et le recopier ici produirait
    un lien vers soi-même, cassé une fois le bloc déplacé dans ce dossier.
    """
    t = lire(SOURCE)
    for b in re.split(r'(?=<h3><span class="tip-num">\d+<)', t):
        if re.match(r'<h3><span class="tip-num">%d<' % n, b):
            b = re.sub(r'\n\s*<a class="btn-detail"[^>]*>.*?</a>', "", b)
            b = re.sub(r'\n\s*<span class="detail-indispo"[^>]*>.*?</span>', "", b)
            return re.sub(r"\n\s*\n", "\n", b.rstrip()) + "\n"
    return None


ATTRIBUTS_RELATIFS = re.compile(
    r'((?:href|src|srcset)=")(?!#|[a-zA-Z][a-zA-Z0-9+.-]*:|//)([^"]*)(")')


def approfondir(html, niveaux=1):
    """Recule chaque chemin relatif d'un niveau de dossier.

    Le gabarit vit dans seances/ ; les pages de détail vivent dans
    seances/astuces-details/, soit un niveau plus bas. Tous les chemins
    relatifs doivent donc gagner un « ../ », qu'ils soient déjà relatifs
    (« ../../../css/… », « ../index.html ») ou siblings (« index.html »).

    srcset est traité comme les autres attributs : une seule URL par valeur
    dans ce gabarit, donc pas de descripteur à préserver.

    Les URLs absolues, les ancres et les liens protocol-relative sont
    laissés intacts.
    """
    def repl(m):
        return m.group(1) + ("../" * niveaux) + m.group(2) + m.group(3)
    return ATTRIBUTS_RELATIFS.sub(repl, html)


def gabarit():
    """En-tête et pied de page, pris sur la séance 11.

    La découpe s'arrête à la fin de <header>, et non au debut de <main>.
    Entre les deux, la séance 11 porte un bandeau « page-header-tic » avec
    son propre <h1> et son fil d'Ariane. Le recopier dans une page de détail
    affichait « Séance 11 — OpenCode + DeepSeek » au-dessus de chaque astuce,
    et laissait deux <h1> sur la page. Ces deux blocs sont propres à la
    séance : le gabarit de détail fournit les siens.
    """
    src = lire(MODELE)
    fin_header = src.find("</header>")
    footer_d = src.find('<footer class="footer"')
    if fin_header < 0 or footer_d < 0:
        raise SystemExit("Gabarit seance-11.html : <header> ou <footer> introuvable.")
    tete = src[:fin_header + len("</header>")]
    pied = src[footer_d:]
    return approfondir(tete), approfondir(pied)


def titre_page(numero, titre):
    """Titre SEO : 15 a 70 caracteres, comme l'exige l'audit du site.

    Le suffixe « | Module IA » apporte le nom du module dans les resultats
    de recherche, mais il n'est pas gratuit : sur quelques titres longs
    (astuce 6 : « Formule magique : Role + Contexte + Tache + Format +
    Contraintes ») il pousse au-dela de 70. On le retire alors, et si le
    titre reste trop long on coupe au dernier espace plutot qu'au milieu
    d'un mot.
    """
    base = "Astuce %d — %s" % (numero, titre)
    for suffixe in (" | Module IA", ""):
        if len(base + suffixe) <= 70:
            return base + suffixe
    return base[:70].rsplit(" ", 1)[0].rstrip(" ,;:·-") + "…"


def construire(numero, titre, sections, dispo):
    tete, pied = gabarit()
    fichier = "astuce-%03d.html" % numero

    canon = BASE + fichier
    # 60 a 165 caracteres : borne de l'audit du site. On construit la phrase
    # puis on coupe proprement, sans laisser un mot en Suspens.
    meta = ("Explication détaillée de l'astuce %d du module Intelligence "
            "Artificielle (%s) : comprendre, appliquer, éviter les erreurs. "
            "2e année PEP, ENS Université de Mostaganem." % (numero, titre))
    meta = re.sub(r"\s+", " ", meta).strip()
    if len(meta) > 165:
        meta = meta[:165].rsplit(" ", 1)[0].rstrip(" ,;:·-") + "…"
    t = titre_page(numero, titre)

    tete = re.sub(r"<title>.*?</title>",
                  "<title>%s</title>" % html_ech(t), tete, flags=re.S)
    tete = re.sub(r'<meta name="description"[^>]*>', "", tete)
    for balise in ('<meta property="og:title"[^>]*>',
                   '<meta property="og:description"[^>]*>',
                   '<meta property="og:url"[^>]*>',
                   '<meta name="twitter:title"[^>]*>',
                   '<meta name="twitter:description"[^>]*>'):
        tete = re.sub(balise, "", tete)
    tete = re.sub(r'<link[^>]*canonical[^>]*>', "", tete)
    tete = re.sub(r'<meta charset="[^"]*">',
                  '<meta charset="UTF-8">\n  <meta name="description" content="%s">'
                  '\n  <link rel="canonical" href="%s">'
                  '\n  <meta property="og:title" content="%s">'
                  '\n  <meta property="og:url" content="%s">'
                  % (html_ech(meta), canon, html_ech(t), canon),
                  tete, count=1)
    tete = tete.replace("</style>", STYLE + "</style>", 1)

    nav = []
    # On ne propose un voisin que si sa page existe : un lien vers une page
    # absente est un 404, ce qui est pire que pas de lien du tout.
    if numero > 1 and (numero - 1) in dispo:
        nav.append('<a href="astuce-%03d.html">← Astuce %d</a>'
                   % (numero - 1, numero - 1))
    if numero < 152 and (numero + 1) in dispo:
        nav.append('<a href="astuce-%03d.html">Astuce %d →</a>'
                   % (numero + 1, numero + 1))
    # Le retour à la liste est traité à part : il figure en haut ET en bas de
    # la page, et il ne doit pas être répété dans la nav, sinon deux liens
    # identiques se suivent à trois lignes d'écart.
    nav_html = "\n      ".join(nav)
    # Un astuce isolé (aucun voisin disponible) n'aurait sinon aucune nav :
    # on lui laisse au moins le retour et l'ancre vers le haut.
    if not nav:
        nav_html = '<a href="../astuces-ia.html">← Retour aux 152 astuces</a>'
    retour = ('<a class="detail-retour" href="../astuces-ia.html">'
              '← Retour aux 152 astuces</a>')
    haut = '<a href="#main-content">↑ Haut de page</a>'

    milieu = """
<main class="page-content" id="main-content">
  <div class="container">
    <nav aria-label="Fil d'Ariane">
      <ol class="breadcrumb">
        <li><a href="../../../../index.html">Accueil</a></li>
        <li><a href="../../../../enseignement.html">Enseignement</a></li>
        <li><a href="../../index.html">Intelligence Artificielle</a></li>
        <li><a href="../astuces-ia.html">Astuces</a></li>
        <li class="current">Astuce %d</li>
      </ol>
    </nav>

    <div class="page-header">
      <h1>🔍 Astuce %d — %s</h1>
      <p>Explication détaillée · Module Intelligence Artificielle — 2e année PEP</p>
    </div>

    <div class="detail-retour-haut">
      %s
      <div class="detail-nav">%s</div>
    </div>

    <div class="detail-corps">
%s
    </div>

    <div class="detail-retour-bas">
      <div class="detail-nav">%s</div>
      %s
      %s
    </div>
  </div>
</main>
""" % (numero, numero, html_ech(titre),
       retour, nav_html,
       "\n".join(sections),
       nav_html, retour, haut)

    return tete + milieu + "\n" + pied


def html_ech(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace('"', "&quot;"))


def decouper(corps):
    """Découpe un texte en 10 sections, sur les titres <h2>N. …</h2>.

    Le contenu est rédigé d'un bloc :.writer, le découper ici évite
    d'imposer une liste de 10 chaînes à la main, qui serait pénible à relire
    et facile à désynchroniser d'un lot à l'autre.
    """
    morceaux = re.split(r"(?m)^(?=<h2>\s*\d+\.\s)", corps.strip())
    # si le premier morceau est vide (le texte commence par un <h2>), on retire
    if morceaux and not morceaux[0].strip():
        morceaux = morceaux[1:]
    return morceaux


def charger_contenus():
    """Charge les fichiers de contenu du dossier scripts/contenus_details/.

    Le module est lu puis exécuté directement, sans passer par
    __import__ : le cache .pyc renverrait l'ancienne version d'un fichier
    que l'on vient de corriger, et le générateur réécrirait des pages avec
    un texte périmé sans aucun signe dans la sortie.
    """
    tous = {}
    if not os.path.isdir(CONTENU):
        return tous
    for nom in sorted(os.listdir(CONTENU)):
        if not nom.endswith(".py"):
            continue
        with open(os.path.join(CONTENU, nom), encoding="utf-8") as f:
            source = f.read()
        espace = {}
        exec(compile(source, nom, "exec"), espace)
        # Deux conventions acceptées :
        #   ASTUCE_12 = {"titre":…, "sections":[…]}   (une entrée par astuce)
        #   LOT_1 = {} ; LOT_1[12] = "…"               (regroupement par lot)
        for cle, val in espace.items():
            if cle.startswith("ASTUCE_") and isinstance(val, dict):
                tous[cle] = val
        for cle, val in espace.items():
            if (cle.startswith("LOT_") and isinstance(val, dict)
                    and val and isinstance(next(iter(val.values())), str)):
                for n, corps in val.items():
                    tous["ASTUCE_%s" % n] = {"sections": decouper(corps)}
    return tous


def verifier(page, numero, sections):
    """Contrôle qualité AVANT écriture. Retourne la liste des problèmes.

    On valide la page finie, pas seulement le contenu : c'est ce qui permet
    d'attraper un </p> au lieu d'un </div>, ou un chemin CSS resté à trois
    niveaux au lieu de quatre. Ces deux erreurs sont invisibles à la lecture
    mais cassent le rendu.
    """
    pb = []
    if len(sections) != 10:
        pb.append("%d sections au lieu de 10" % len(sections))
    for i, s in enumerate(sections, 1):
        # Le libellé varie d'une astuce à l'autre (« 5. Application pratique —
        # préparer un exposé » ou « … — cas complet ») : c'est le numéro qui
        # doit être juste, pas l'intitulé.
        m = re.search(r"<h2[^>]*>\s*(\d+)\.", s)
        if not m:
            pb.append("section %d : pas de titre <h2>N. …</h2>" % i)
        elif int(m.group(1)) != i:
            pb.append("section %d : titre numéroté %s" % (i, m.group(1)))

    # HTML bien formé. La liste des balises auto-fermantes doit être complète :
    # le gabarit contient <source> (dans <picture>), qui est auto-fermant et
    # n'a pas de </source>. Oublier cette famille fausse le décompte de 6
    # par page et faisait refuser des pages parfaitement correctes.
    VOID = {"br", "hr", "img", "meta", "link", "input", "area", "base",
            "col", "embed", "source", "track", "wbr"}
    o = len([m for m in re.finditer(r"<(\w+)\b", page)
             if m.group(1).lower() not in VOID])
    f = len(re.findall(r"</(\w+)>", page))
    if o != f:
        pb.append("balises non equilibrees : %d ouvertes, %d fermees" % (o, f))

    if "</br>" in page:
        pb.append("balise </br> orpheline")

    if re.search(r"[\u3000-\u9fff\uac00-\ud7af]", page):
        pb.append("caracteres non latins (chinois ou coreen)")

    # Chemins relatifs : on les résout réellement sur le disque plutôt que de
    # vérifier une liste figée. C'est ce qui a laissé passer 270 liens morts
    # dans une version précédente (le gabarit est écrit pour seances/, les
    # pages vivent un niveau plus bas).
    for chemin in sorted(set(ATTRIBUTS_RELATIFS.findall(page))):
        brut = chemin[1]
        if not brut or brut.startswith("#"):
            continue
        cible = os.path.normpath(
            os.path.join(DEST, urllib.parse.unquote(brut.split("#")[0])))
        if os.path.isdir(cible):
            cible = os.path.join(cible, "index.html")
        if not os.path.exists(cible):
            pb.append("chemin mort : %s" % brut)

    # navigation
    fichier = "astuce-%03d.html" % numero
    if 'href="../../index.html"' not in page:
        pb.append("fil d'Ariane incomplet")
    if 'rel="canonical"' not in page or fichier not in page:
        pb.append("canonical incorrect")
    # Le voisin n'est lié que si sa page existe : on ne peut donc pas exiger
    # sa présence. On vérifie l'inverse — qu'aucun lien ne pointe vers une
    # page absente.
    for l in re.findall(r'href="(astuce-\d+\.html)"', page):
        if not os.path.isfile(os.path.join(DEST, l)):
            pb.append("lien vers une page absente : %s" % l)
    if '../astuces-ia.html' not in page:
        pb.append("lien de retour absent")

    mots = len(re.sub(r"<[^>]+>", " ", page).split())
    if mots < 1800:
        pb.append("trop court : %d mots" % mots)
    return pb


def main():
    os.makedirs(DEST, exist_ok=True)
    titres = titres_astuces()
    contenus = charger_contenus()

    cibles = [int(a) for a in sys.argv[1:]] or sorted(
        int(k.split("_")[1]) for k in contenus)
    # pages déjà présentes : une page peut viser un voisin produit plus tôt,
    # même si son contenu n'est pas dans le lot en cours
    dispo = set(cibles)
    if os.path.isdir(DEST):
        for f in os.listdir(DEST):
            m = re.match(r"astuce-(\d+)\.html$", f)
            if m:
                dispo.add(int(m.group(1)))
    if not cibles:
        print("Aucun contenu dans scripts/contenus_details/ — rien a generer.")
        return 1

    ecrites, refusees = [], []
    for n in cibles:
        cle = "ASTUCE_%d" % n
        if cle not in contenus:
            refusees.append((n, "pas de contenu redige"))
            continue
        sections = contenus[cle]["sections"]
        src = source_astuce(n)
        if src is None:
            refusees.append((n, "introuvable dans la page des astuces"))
            continue
        sections = list(sections)
        sections[0] = sections[0].replace("<!--SOURCE-->", src)
        if "<!--SOURCE-->" not in contenus[cle]["sections"][0]:
            sections[0] = sections[0] + "\n" + src
        page = construire(n, titres.get(n, "Astuce %d" % n), sections, dispo)

        # Le décalage de profondeur est déjà fait dans gabarit() ; on ne le
        # refait pas ici, sinon on ajouterait un niveau de trop.

        # contrôles automatiques, avant écriture
        pb = verifier(page, n, sections)
        if pb:
            refusees.append((n, "; ".join(pb)))
            print("  [%d] REFUSE : %s" % (n, "; ".join(pb)))
            continue

        with open(os.path.join(DEST, "astuce-%03d.html" % n), "w",
                  encoding="utf-8") as f:
            f.write(page)
        ecrites.append(n)

    print("Pages ecrites   : %d" % len(ecrites))
    if ecrites:
        print("   %s" % ", ".join(str(x) for x in ecrites))
    if refusees:
        print("Pages refusees  : %d" % len(refusees))
        for n, why in refusees:
            print("   astuce %d : %s" % (n, why))
    return 0


if __name__ == "__main__":
    sys.exit(main())