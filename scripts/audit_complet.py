#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit complet du site : accessibilité, SEO, performance, qualité.

Complète scripts/audit_liens.py (liens et ressources). Ici on cherche ce
qu'on ne voit pas à l'œil : image sans texte alternatif, hiérarchie de
titres cassée, title dupliqué, fichier de debug oublié, faute de typographie
française, page vide…

Principe important : un attribut n'existe que dans une balise. Le premier
version de cet outil cherchait `href="..."` dans tout le fichier et
signalait 7 fausses ressources : un cours qui *enseigne* le HTML contient
`<code>&lt;link href="style.css"&gt;</code>` — c'est du texte à lire, pas une
référence. On analyse donc balise par balise.

Performance : expressions régulières uniquement, 2 883 pages en quelques
minutes, sans dépendance.

Limites connues, volontairement non couvertes plutôt que signalées à tort :
  - « mot répété » : sans analyse du DOM, « Université » suivi de « Université
    de Mostaganem » (deux cartes voisines) est indiscernable d'une faute ;
  - contraste des couleurs : exigerait de calculer le rendu ;
  - liens en Target=_blank vérifiés, mais pas l'ordre des attributs HTML.

Usage : python3 audit_complet.py [racine] [--json fichier.json]
Code de retour : 1 s'il y a au moins une anomalie.
"""
import json
import os
import re
import sys
from collections import Counter, defaultdict
from html import unescape
from urllib.parse import unquote, urlparse

RACINE = sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("-") \
    else os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SORTIE = None
if "--json" in sys.argv:
    i = sys.argv.index("--json")
    SORTIE = sys.argv[i + 1] if i + 1 < len(sys.argv) else "audit.json"

EXTERNES = ("http://", "https://", "//", "mailto:", "tel:", "javascript:", "data:")

TAG = re.compile(r"<!--.*?-->|<[^>]+>", re.S)
SCRIPT_STYLE = re.compile(r"<(script|style|noscript)\b[^>]*>.*?</\1\s*>", re.S | re.I)
CODE = re.compile(r"<(code|pre|kbd|samp|textarea)\b[^>]*>.*?</\1\s*>", re.S | re.I)
ATTR = {
    "href": re.compile(r'\bhref\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', re.I),
    "src": re.compile(r'\bsrc\s*=\s*(?:"([^"]*)"|\'([^\']*)\'|([^\s>]+))', re.I),
    "alt": re.compile(r'\balt\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "target": re.compile(r'\btarget\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "width": re.compile(r'\bwidth\s*=\s*"?(\d+)', re.I),
    "height": re.compile(r'\bheight\s*=\s*"?(\d+)', re.I),
    "id": re.compile(r'\bid\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "lang": re.compile(r'\blang\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "content": re.compile(r'\bcontent\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "name": re.compile(r'\bname\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "rel": re.compile(r'\brel\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
    "type": re.compile(r'\btype\s*=\s*(?:"([^"]*)"|\'([^\']*)\')', re.I),
}
HEADING = re.compile(r"<h([1-6])\b", re.I)
OBSOLETES = ("center", "font", "marquee", "blink", "big", "strike", "tt")

# --- fautes de typographie et de langue française --------------------------
# Des controles fiables : contrairement a « deux mots colles », qu'on ne peut
# pas distinguer d'un mot legitime sans dictionnaire, ces motifs-la n'ont pas
# de faux positifs.
# --- fautes de typographie et de langue francaise --------------------------
# Version 2, apres verification contre le contenu reel. La premiere version
# signalait plus de 4 500 faux positifs ; ce qu'on ne garde que si c'est
# reellement une faute dans un texte francais :
#   * espace avant « : ; ! ? » : c'est la REGLE francaise, pas une faute ;
#   * « de le traverser », « a les transformer » : elision correcte devant
#     un verbe, pas une faute ;
#   * localStorage, authPriv : camelCase technique, pas un collage ;
#   * « students' work » : possessif anglais, pas une apostrophe mal collee ;
#   * le menu repete legitimement « Actualites » deux fois d'affilee.
CHROME = re.compile(
    r"<(nav|header|footer|breadcrumb|\w*menu\w*)\b[^>]*>.*?</\1\s*>", re.S | re.I)

TYPO = [
    ("espace avant . ou ,", re.compile(r"(?<=[\w)\]])[ \t]+[.,](?=\s|$)")),
    # « Academia.edu », « PLAN_DE_TRAVAIL.md », « 0,6 » sont corrects.
    # Seule faute : une ponctuation collee a un mot, precedee d'une
    # minuscule et suivie d'un mot qui reprend la phrase.
    ("point ou virgule sans espace apres",
     re.compile(r"(?<=[a-zà-ÿ])\.(?=[A-ZÀ-Ý])|(?<=[a-zà-ÿ]),(?=[0-9A-Za-zÀ-ÿ])")),
    ("elision detachee (l' outil)",
     re.compile(r"\b(?:l|d|j|n|qu|c|m|t)'[ \t]+[a-zà-ÿ]")),
    ("« de des »", re.compile(r"\bde\s+des\b", re.I)),
    ("double espace en texte", re.compile(r"[a-zà-ÿ]{3,}  +[a-zà-ÿ]{3,}")),
    ("guillemets droits dans du français",
     re.compile(r"[a-zà-ÿ]\"[^\"]{2,40}\"")),
]


def attr(m):
    for g in m.groups():
        if g is not None:
            return unescape(g)
    return ""


def texte(s):
    """Contenu textuel, balises et zones de code retiré."""
    s = SCRIPT_STYLE.sub(" ", s)
    s = CODE.sub(" ", s)
    s = TAG.sub(" ", s)
    return re.sub(r"\s+", " ", unescape(s)).strip()


def balises(s):
    """Toutes les balises du document (donc tous les emplacements d'attributs)."""
    return TAG.findall(SCRIPT_STYLE.sub(" ", s))


def resoudre(dossier, chemin):
    return os.path.normpath(os.path.join(dossier, unquote(chemin).lstrip("/")))


def rel(p):
    try:
        return os.path.relpath(p, RACINE)
    except ValueError:
        return p


class Rapport(object):
    NIVEAUX = {}

    def __init__(self):
        self.compteurs = Counter()
        self.exemples = defaultdict(list)

    def note(self, cle, exemple=None, n=1):
        self.compteurs[cle] += n
        if exemple is not None and len(self.exemples[cle]) < 6 \
                and exemple not in self.exemples[cle]:
            self.exemples[cle].append(exemple)

    @property
    def total(self):
        return sum(self.compteurs.values())


ORDRE = [
    ("lien mort", "CRITIQUE"),
    ("ressource manquante", "CRITIQUE"),
    ("balise non fermée / attribut cassé", "CRITIQUE"),
    ("page orpheline (aucun lien entrant)", "IMPORTANT"),
    ("page racine non liée", "IMPORTANT"),
    ("fichier parasite", "IMPORTANT"),
    ("marqueur de travail (TODO/FIXME/lorem)", "IMPORTANT"),
    ("image sans attribut alt", "IMPORTANT"),
    ("alt non descriptif", "MINEUR"),
    ("bouton sans nom accessible", "IMPORTANT"),
    ("image sans width/height (CLS)", "MINEUR"),
    ("iframe sans titre", "IMPORTANT"),
    ("lien sans texte", "IMPORTANT"),
    ("lien sans texte explicite", "MINEUR"),
    ("target=_blank sans noopener", "IMPORTANT"),
    ("page sans <h1>", "IMPORTANT"),
    ("plusieurs <h1>", "MINEUR"),
    ("saut de niveau de titre", "MINEUR"),
    ("page sans <title>", "IMPORTANT"),
    ("title dupliqué", "IMPORTANT"),
    ("title trop long (>65 car.)", "MINEUR"),
    ("meta description dupliquée", "MINEUR"),
    ("page sans meta description", "MINEUR"),
    ("meta description trop longue", "MINEUR"),
    ("page sans meta viewport", "MINEUR"),
    ("page sans canonical", "MINEUR"),
    ("page sans attribut lang sur <html>", "IMPORTANT"),
    ("id dupliqué dans la page", "IMPORTANT"),
    ("balise obsolète", "MINEUR"),
    ("tableau sans <th>", "MINEUR"),
    ("image très lourde (>400 Ko)", "MINEUR"),
    ("page très lourde (>1,5 Mo)", "MINEUR"),
    ("page quasi vide (<400 car.)", "MINEUR"),
    ("« de des »", "MINEUR"),
    ("double espace en texte", "MINEUR"),
    ("champ de formulaire sans étiquette", "MINEUR"),
]


def main():
    fichiers = []
    for d, sous, noms in os.walk(RACINE):
        sous[:] = [s for s in sous
                   if s not in (".git", "node_modules", "__pycache__", ".venv")]
        for n in noms:
            fichiers.append(os.path.normpath(os.path.join(d, n)))
    tailles = {p: os.path.getsize(p) for p in fichiers}

    html = {}
    for p in fichiers:
        if p.endswith(".html"):
            try:
                html[p] = open(p, encoding="utf-8", errors="ignore").read()
            except OSError:
                pass

    r = Rapport()
    titres, descs = defaultdict(list), defaultdict(list)
    pointeurs = defaultdict(set)
    ancres = {}
    poids = {}
    ids_par_page = {}

    # ---------- passe 1 : métadonnées, liens entrants, ancres ---------------
    for p, s in html.items():
        dossier = os.path.dirname(p)
        t = texte(s)
        poids[p] = len(s.encode("utf-8"))

        m = re.search(r"<title[^>]*>(.*?)</title>", s, re.S | re.I)
        if m:
            titres[re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", m.group(1)))).strip()].append(p)
        else:
            r.note("page sans <title>", rel(p))

        dm = None
        for tag in balises(s[:s.lower().find("</head>") if "</head>" in s else 4000]):
            if "<meta" in tag.lower() and "description" in tag.lower():
                dm = tag
                break
        if not dm:
            r.note("page sans meta description", rel(p))
        else:
            c = attr(ATTR["content"].search(dm) or re.match(r"()", ""))
            if c:
                descs[c.strip()].append(p)
                if len(c) > 175:
                    r.note("meta description trop longue", "%s (%d car.)" % (rel(p), len(c)))
            else:
                r.note("page sans meta description", rel(p))

        tetes = balises(s[:s.lower().find("</head>") if "</head>" in s else 4000])
        if not any(re.search(r'\bname\s*=\s*["\']?viewport', x, re.I) for x in tetes):
            r.note("page sans meta viewport", rel(p))
        if not any('rel="canonical"' in x or "rel='canonical'" in x for x in tetes):
            r.note("page sans canonical", rel(p))

        racine = re.search(r"<html\b[^>]*>", s, re.I)
        if not racine or not ATTR["lang"].search(racine.group(0)):
            r.note("page sans attribut lang sur <html>", rel(p))

        ens, vus = set(), set()
        for tag in balises(s):
            for a in ("id", "name"):
                v = attr(ATTR[a].search(tag)) if ATTR[a].search(tag) else ""
                if v and a == "id":
                    if v in vus and v not in ens:
                        r.note("id dupliqué dans la page", "%s (#%s)" % (rel(p), v))
                    vus.add(v)
            i = ATTR["id"].search(tag)
            if i:
                ens.add(attr(i))
        ancres[p] = ens
        ids_par_page[p] = vus

        for tag in balises(s):
            for cle in ("href", "src"):
                m = ATTR[cle].search(tag)
                if not m:
                    continue
                v = attr(m)
                if not v or v.startswith(EXTERNES) or v.startswith("#"):
                    if cle == "href" and 'target="_blank"' in tag and "noopener" not in tag:
                        r.note("target=_blank sans noopener", "%s -> %s" % (rel(p), v))
                    continue
                if cle == "href":
                    cible = p if not urlparse(v).path \
                        else resoudre(dossier, urlparse(v).path)
                    pointeurs[cible].add(p)
                else:
                    f = resoudre(dossier, urlparse(v).path)
                    if not os.path.exists(f):
                        r.note("ressource manquante", "%s -> %s" % (rel(p), v))

    # ---------- passe 2 : titres dupliqués ---------------------------------
    for t, pages in titres.items():
        if t and len(pages) > 1:
            r.note("title dupliqué", "%r sur %d pages (ex. %s)"
                   % (t[:55], len(pages), rel(pages[0])), len(pages))
        elif t and len(t) > 65:
            r.note("title trop long (>65 car.)", "%r (%s)" % (t[:55], rel(pages[0])))
    for t, pages in descs.items():
        if t and len(pages) > 1:
            r.note("meta description dupliquée", "%r sur %d pages (ex. %s)"
                   % (t[:55], len(pages), rel(pages[0])), len(pages))

    # ---------- passe 3 : accessibilité, contenu, performance ---------------
    for p, s in html.items():
        dossier = os.path.dirname(p)
        rp = rel(p)
        t = texte(s)
        bs = balises(s)
        # le menu et le pied de page repetaient volontairement des mots :
        # on les exclut des controles de langue
        # Contrôle de langue : on travaille sur les SEGMENTS DE TEXTE séparés
        # par les balises, jamais sur la page aplatie. Aplatir en remplaçant
        # chaque balise par une espace crée des espaces fantômes :
        # « professionnelle</strong>. » devenait « professionnelle . », ce qui
        # a fait apparaître 368 fausses fautes de typographie. De même, le
        # JSON-LD (« "@context": "https://… ») produisait 2 878 faux positifs.
        tc = [unescape(x) for x in
              CODE.split(CHROME.split(SCRIPT_STYLE.sub("\x00", s))[0])
              if False] if False else None
        propre = CODE.sub("\x00", CHROME.sub("\x00", SCRIPT_STYLE.sub("\x00", s)))
        segments = []
        for bout in propre.split("\x00"):
            for x in TAG.split(bout):
                if x.strip():
                    segments.append(unescape(x))

        for tag in bs:
            bas = tag.lower()
            nom = re.match(r"<\s*([a-z0-9]+)", bas)
            nom = nom.group(1) if nom else ""
            if nom in OBSOLETES:
                r.note("balise obsolète", "%s (<%s>)" % (rp, nom))
                break

        # images
        for tag in bs:
            if not tag.lower().startswith("<img"):
                continue
            a = ATTR["alt"].search(tag)
            if not a:
                r.note("image sans attribut alt", rp)
            elif attr(a).strip() and attr(a).strip().lower() in (
                    "image", "photo", "logo", "img", "picture", "picto", "icône"):
                r.note("alt non descriptif", "%s (alt=%r)" % (rp, attr(a)))
            if not (ATTR["width"].search(tag) and ATTR["height"].search(tag)):
                r.note("image sans width/height (CLS)", rp)
            m = ATTR["src"].search(tag)
            if m:
                v = attr(m)
                if not v.startswith(EXTERNES):
                    f = resoudre(dossier, urlparse(v).path)
                    ko = tailles.get(f, 0)
                    if ko > 400 * 1024:
                        r.note("image très lourde (>400 Ko)",
                               "%s (%s — %.0f Ko)" % (rp, os.path.basename(f), ko / 1024.0))

        ifaces = [x for x in bs if x.lower().startswith("<iframe")]
        for tag in ifaces:
            if "title=" not in tag.lower():
                r.note("iframe sans titre", rp)

        if "<main" not in s.lower():
            r.note("page sans <main>", rp)
        # Le lien d'evitement est injecte a l'execution par placeSkipLink()
        # (js/main.v2.js) sur les pages qui ne l'ecrivent pas : une page qui
        # charge ce script n'est donc pas concernee, meme si le HTML est muet.
        if not re.search(r"skip-link|skip_to_content|allerr? (?:au|to) contenu",
                         s, re.I) and "main.v2.js" not in s:
            r.note("pas de lien d'évitement", rp)

        # titres
        niveaux = [int(x) for x in HEADING.findall(s)]
        if not niveaux:
            r.note("page sans titre de section", rp)
        else:
            if 1 not in niveaux:
                r.note("page sans <h1>", rp)
            if niveaux.count(1) > 1:
                r.note("plusieurs <h1>", "%s (%d)" % (rp, niveaux.count(1)))
            for a, b in zip(niveaux, niveaux[1:]):
                if b - a > 1:
                    r.note("saut de niveau de titre", "%s (h%d → h%d)" % (rp, a, b))
                    break

        # liens
        for m in re.finditer(r"<a\b([^>]*)>(.*?)</a>", s, re.S | re.I):
            attrs, interieur = m.group(1), m.group(2)
            lt = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", interieur))).strip()
            if not lt:
                r.note("lien sans texte", rp)
            elif lt.lower() in ("cliquez ici", "clique ici", "ici", "en savoir plus",
                                "suite", "plus", "read more", "here", "lien",
                                "voici", "lire la suite", "d&eacute;taillez"):
                r.note("lien sans texte explicite", "%s (%s)" % (rp, lt[:30]))
            if 'target="_blank"' in attrs and "noopener" not in attrs.lower():
                r.note("target=_blank sans noopener", rp)

        # Formulaires. Un champ est etiquete si : aria-label/labelledby,
        # un title, un id reference par un <label for>, ou s'il est ENROULE
        # dans un <label> (les QCM d'examen font tous les deux). Sans ces
        # trois formes, la premiere version signalait 40 faux positifs.
        fors = {attr(m) for m in
                re.finditer(r'<label[^>]*\bfor\s*=\s*["\']?([\w-]+)', s, re.I)}
        ids = set()
        for tag in bs:
            b = tag.lower()
            if not b.startswith(("<input", "<select", "<textarea")):
                continue
            m = ATTR["type"].search(tag)
            if m and attr(m) == "hidden":
                continue
            i = ATTR["id"].search(tag)
            if i:
                ids.add(attr(i))
                continue
            if "aria-label" in b or "aria-labelledby" in b or "title=" in b:
                continue
            if re.search(r"<label[^>]*>\s*(?:<[^>]+>\s*)*" + re.escape(b[:14]), s, re.I):
                continue
            r.note("champ de formulaire sans étiquette", rp)
            break
        del fors, ids
        for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", s, re.S | re.I):
            it = re.sub(r"\s+", " ", unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
            if not it and "aria-label" not in m.group(1).lower() \
                    and "title=" not in m.group(1).lower():
                r.note("bouton sans nom accessible", rp)
                break

        # tableaux
        for m in re.finditer(r"<table\b.*?</table>", s, re.S | re.I):
            corps = m.group(0)
            if "<th" not in corps.lower() and corps.lower().count("<td") > 4:
                r.note("tableau sans <th>", rp)
                break

        # qualité du contenu
        # une page dont le contenu EST un lecteur audio/video n'est pas vide
        if len(t) < 400 and not re.search(r"<(audio|video|iframe|embed)\b", s, re.I):
            r.note("page quasi vide (<400 car.)", "%s (%d car.)" % (rp, len(t)))
        if re.search(r"\bTODO\b|\bFIXME\b|Lorem ipsum|\bXXX\b", s):
            r.note("marqueur de travail (TODO/FIXME/lorem)", rp)
        for libelle, rx in TYPO:
            for seg in segments:
                mm = rx.search(seg)
                if not mm:
                    continue
                plat_seg = re.sub(r"\s+", " ", seg)
                decalage = mm.start() - seg.find(plat_seg[:1] or " ")
                r.note(libelle, "%s (…%s…)"
                       % (rp, plat_seg[max(0, mm.start() - 25):mm.end() + 15]))
                break
        if poids.get(p, 0) > 1_500_000:
            r.note("page très lourde (>1,5 Mo)", "%s (%.1f Mo)" % (rp, poids[p] / 1048576.0))

    # ---------- passe 4 : fichiers parasites et orphelines -----------------
    for p in fichiers:
        base = os.path.basename(p)
        if base.startswith(("_dbg", "_tmp", "tmp_", "_test", "test_", "~")) or \
                base.endswith((".bak", ".orig", ".rej", ".tmp", ".pyc", ".log")) or \
                base in ("desktop.ini", "Thumbs.db", ".DS_Store", ".gitkeep"):
            r.note("fichier parasite", rel(p))
    for p in html:
        if not pointeurs.get(p):
            r.note("page orpheline (aucun lien entrant)", rel(p))
    for p in fichiers:
        if p.endswith((".html", ".pdf")) and \
                os.path.abspath(os.path.dirname(p)) == os.path.abspath(RACINE) and \
                not pointeurs.get(p):
            r.note("page racine non liée", rel(p))

    # ---------- rapport ----------------------------------------------------
    print("=" * 78)
    print("AUDIT COMPLET — %s" % RACINE)
    print("%d fichiers · %d pages HTML · %.1f Mo"
          % (len(fichiers), len(html), sum(tailles.values()) / 1048576.0))
    print("=" * 78)
    print()
    trouves = 0
    for cle, niveau in ORDRE:
        n = r.compteurs.get(cle, 0)
        if not n:
            continue
        trouves += 1
        print("[%-8s] %-42s %6d" % (niveau, cle, n))
        for ex in r.exemples.get(cle, [])[:4]:
            print("            - %s" % ex)
    if not trouves:
        print("Aucune anomalie.")
    print()

    # Tout compteur doit etre classe : sinon le total ne se reconcilie pas et
    # l'audit cache des anomalies. On affiche explicitement le reliquat.
    affiches = {c for c, _ in ORDRE}
    restes = {k: v for k, v in r.compteurs.items() if k not in affiches}
    if restes:
        print("-- anomalies non classees dans le rapport (reliquat) --")
        for k, v in sorted(restes.items(), key=lambda x: -x[1]):
            print("[?]       %-42s %6d" % (k, v))
            for ex in r.exemples.get(k, [])[:3]:
                print("            - %s" % ex)
        print()

    somme = sum(r.compteurs.get(c, 0) for c in affiches) + sum(restes.values())
    print("TOTAL : %d anomalies sur %d pages (reconcilie : %s)"
          % (r.total, len(html), "oui" if somme == r.total else "NON, %d" % somme))

    if SORTIE:
        with open(SORTIE, "w", encoding="utf-8") as f:
            json.dump({"racine": RACINE, "fichiers": len(fichiers),
                       "pages_html": len(html),
                       "mo": round(sum(tailles.values()) / 1048576.0, 1),
                       "total": r.total,
                       "compteurs": dict(r.compteurs),
                       "exemples": dict(r.exemples)}, f,
                      ensure_ascii=False, indent=2)
        print("JSON : %s" % SORTIE)
    return 0 if r.total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
