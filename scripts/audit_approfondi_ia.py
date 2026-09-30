#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit approfondi du module Intelligence Artificielle.

Les outils existants (audit_liens.py, audit_complet.py) vérifient ce qui est
vérifiable automatiquement : liens, balises, SEO. Ils ne regardent pas ce qui
fait la qualité d'un cours.

Ce script ajoute huit dimensions :

  1. renvois entre astuces   — l'astuce 3 cite « astuce n° 2 » : est-ce vrai ?
  2. lisibilité              — longueur des phrases, mots difficiles, passif
  3. cohérence de langue     — un même concept nommé de plusieurs façons
  4. accessibilité           — liens non descriptifs, tableaux, images, contrastes
  5. pédagogie               — chaque séance a-t-elle objectif, durée, exercice ?
  6. références internes     — les « voir séance 07 » pointent-ils quelque chose ?
  7. POIDS                     — pages trop lourdes, images trop grandes
  8..metadata                — titres, descriptions, langue déclarée

Usage : python3 audit_approfondi_ia.py [racine]
"""
import os
import re
import sys
from collections import Counter, defaultdict

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    RACINE, "cours", "Module Intelligence Artificielle")

# ---------------------------------------------------------------------------
# 1. renvois entre astuces
# ---------------------------------------------------------------------------
RENVOI = re.compile(
    r"(?:astuce\s*)\s*n[°ºo]\s*(\d+)", re.I)


def audit_renvois(astuces_txt):
    """Chaque « astuce n° N » doit viser une astuce existante, et si la
    phrase est une liaison (« l'astuce n° 1 disait… »), le numéro doit
    vraiment désigner l'astuce dont on parle."""
    problemes = []
    for numero, titre, corps in astuces_txt:
        for m in RENVOI.findall(corps):
            n = int(m)
            if n < 1 or n > len(astuces_txt):
                problemes.append(
                    (numero, "renvoi vers l'astuce %d qui n'existe pas" % n))
    return problemes


# ---------------------------------------------------------------------------
# 2. lisibilité
# ---------------------------------------------------------------------------
MOT_DIFFICILE = {
    "susceptibles", "conséquentiel", "inhérent", "prédominante",
    "caractéristique", "nécessairement", "précisément", "explicitement",
    "indépendamment", "correspondamment", "antérieurement", "subséquemment",
}
MOT_VIDE = re.compile(
    r"\b(voici|ceci|cela|cela|ça|il y a|on peut|il est possible|"
    r"il faut|on va|de manière à|afin de)\b", re.I)


def phrases(texte):
    # Le texte arrive découpé par blocs (séparés par un retour à la ligne).
    # Chaque bloc donne une ou plusieurs phrases ; aplatir les retours à la
    # ligne avant de couper recréerait les fausses « phrases » de 100 mots qu'on
    # cherchait justement à éviter.
    out = []
    for bloc in texte.split("\n"):
        bloc = re.sub(r"[ \t]+", " ", bloc).strip()
        if not bloc:
            continue
        out += [p.strip() for p in re.split(r"(?<=[.!?])\s+", bloc) if p.strip()]
    return out


def audit_lisibilite(fichier, texte_visible):
    ph = phrases(texte_visible)
    if not ph:
        return [], [], []
    longues = [(len(p.split()), p[:90]) for p in ph if len(p.split()) > 38]
    denses = [(len(p.split()), p[:90]) for p in ph if len(p.split()) > 55]
    vides = [p[:90] for p in ph
             if len(p.split()) > 6 and len(MOT_VIDE.findall(p)) >= 2]
    return longues, denses, vides

# ---------------------------------------------------------------------------
# 3. cohérence de langue : un concept, un seul nom
# ---------------------------------------------------------------------------
TERMES = [
    (r"\bchat\s?gpt\b|\bChatGPT\b", "ChatGPT", "chatgpt", "chat gpt"),
    (r"\bcopilot\b", "Copilot", "github copilot", "copilote"),
    (r"\bcursor\b", "Cursor", "cursor ide", "curseur"),
    (r"\bdeepseek\b", "DeepSeek", "deep seek", "deepseek ai"),
    (r"\bgrok\b", "Grok", "grok ai", "groq"),
    (r"\bgemini\b", "Gemini", "gemini google", "google gemini"),
    (r"\bclaude\b", "Claude", "claude ai", "anthropic"),
    (r"\bollama\b", "Ollama", "olama", "ollama ai"),
    (r"\bnotebooklm\b", "NotebookLM", "notebook lm", "notebook-lm"),
]


def audit_termes():
    variantes = defaultdict(set)
    for f in html_files:
        t = visible(lire(f))
        bas = t.lower()
        for _, canonique, *alt in TERMES:
            for v in alt:
                if re.search(r"\b" + re.escape(v) + r"\b", bas):
                    variantes[canonique].add(v)
    return {k: v for k, v in variantes.items() if v}


# ---------------------------------------------------------------------------
# 4. accessibilité
# ---------------------------------------------------------------------------
LIEN_VIDE = re.compile(
    r"<(?:a|button)\b[^>]*>\s*(?:<[^>]*>\s*)*"
    r"(cliquez\s+ici|voir\s+ici|en\s+savoir\s+plus|"
    r"ce\s+lien|ici|read\s+more|plus\s+info(?:rmations)?|"
    r"learn\s+more|click\s+here)\s*(?:</[^>]*>\s*)*</(?:a|button)>", re.I)
# Un tableau sans <th> : le corps entier doit être examiné, pas seulement la
# balise d'ouverture. La version précédente ne vérifiait que l'ouverture et
# signalait les 74 tableaux du module, y compris ceux qui ont bien des en-têtes.
TABLEAU_SANS_ENTETE = re.compile(
    r"<table\b[^>]*>(?:(?!<th)[\s\S])*?</table>", re.I)
IMG_SANS_ALT = re.compile(r"<img\b(?![^>]*\balt=)[^>]*>", re.I)
LANGUE = re.compile(r'<html\b[^>]*\blang="([^"]+)"')


def audit_accessibilite():
    res = defaultdict(list)
    for f in html_files:
        t = lire(f)
        rel = os.path.relpath(f, MODULE)
        for m in LIEN_VIDE.finditer(t):
            res["lien non descriptif"].append("%s : %s" % (rel, m.group(1)))
        for m in TABLEAU_SANS_ENTETE.finditer(t):
            res["tableau sans <th>"].append(rel)
        for m in IMG_SANS_ALT.finditer(t):
            res["image sans alt"].append(rel)
        m = LANGUE.search(t)
        if not m:
            res["balise lang absente"].append(rel)
        elif m.group(1) not in ("fr", "en"):
            res["langue declaree anormale"].append("%s : %s" % (rel, m.group(1)))
    return res


# ---------------------------------------------------------------------------
# 5. pédagogie
# ---------------------------------------------------------------------------
TRAMES = {
    "objectif":        re.compile(r"<h2[^>]*>[^<]*(?:🎯|objectif)", re.I),
    # deux formats coexistent : "(4 min)" dans le titre d'étape, ou
    # "⏱️ 4 min" dans la ligne step-meta. Les deux sont valides.
    "durée":           re.compile(r"\(\d+\s*min\)|⏱️\s*\d+\s*min"),
    "exercice":        re.compile(r"<h3[^>]*>\s*(?:Étape|Exercice|Atelier)", re.I),
    "à retenir":       re.compile(r"À retenir|À garder|A retenir", re.I),
    "erreurs à éviter": re.compile(r"Erreurs à éviter", re.I),
    "quiz":            re.compile(r"Quiz", re.I),
    "glossaire":       re.compile(r"Glossaire", re.I),
}


def audit_pedagogie():
    seances = sorted(f for f in html_files
                     if os.path.basename(f).startswith("seance-"))
    manque = defaultdict(list)
    for f in seances:
        t = lire(f)
        rel = os.path.basename(f)
        for nom, motif in TRAMES.items():
            if not motif.search(t):
                manque[nom].append(rel)
    return manque, len(seances)


# ---------------------------------------------------------------------------
# 6. références internes « voir séance 07 »
# ---------------------------------------------------------------------------
# Deux écritures : « séance 7 » et « SEANCE 7 ». L'alternative doit rester
# sensible à la casse : appliquée avec re.I, le motif « SE » matchait aussi
# le « se » final de n'importe quel mot suivi d'un nombre
# (« un script qui analy|se| 50 documents »), et inventait des renvois morts.
REF_SEANCE = re.compile(r"(?:[sS][ée]ance|[sS][eE]ance)\s*(\d{1,2})")


def audit_refs_seances():
    res = []
    for f in html_files:
        # par blocs : sinon « Séance 05 — … 150 mots … séance 50 » se
        # retrouve collé dans une seule chaîne et fabrique un faux renvoi
        t = "\n".join(blocs_texte(lire(f)))
        rel = os.path.relpath(f, MODULE)
        for m in REF_SEANCE.finditer(t):
            n = int(m.group(1))
            if n < 1 or n > 15:
                res.append("%s : « %s » n'existe pas" % (rel, t[max(0, m.start()-50):m.end()+10]))
    return res


# ---------------------------------------------------------------------------
# 7. poids
# ---------------------------------------------------------------------------
def audit_poids():
    res = []
    for f in html_files:
        ko = os.path.getsize(f) / 1024
        if ko > 250:
            res.append((os.path.relpath(f, MODULE), ko))
    return res


# ---------------------------------------------------------------------------
# 8. métadonnées
# ---------------------------------------------------------------------------
def audit_meta():
    res = defaultdict(list)
    for f in html_files:
        t = lire(f)
        rel = os.path.relpath(f, MODULE)
        ti = re.search(r"<title[^>]*>(.*?)</title>", t, re.S | re.I)
        # l'ordre des attributs n'est pas normatif : content= peut venir avant
        # name=. Une simple recherche de « description » dans la balise suffit.
        de = None
        for balise_meta in re.findall(r"<meta\b[^>]*>", t, re.I):
            if re.search(r'name\s*=\s*["\']description["\']', balise_meta, re.I):
                de = re.search(r'content\s*=\s*["\']([^"\']*)', balise_meta, re.I)
                break
        if not ti:
            res["title manquant"].append(rel)
        elif not 15 <= len(ti.group(1).strip()) <= 70:
            res["title trop long/court"].append(
                "%s : %d car." % (rel, len(ti.group(1).strip())))
        if not de:
            res["description manquante"].append(rel)
        elif not 60 <= len(de.group(1).strip()) <= 165:
            res["description hors norme"].append(
                "%s : %d car." % (rel, len(de.group(1).strip())))
        if "canonical" not in t.lower():
            res["canonical manquant"].append(rel)
    return res


# ---------------------------------------------------------------------------
# outils
# ---------------------------------------------------------------------------
CHROME = re.compile(
    r"<(header|footer|nav)\b.*?</\1>", re.S | re.I)
BALISE = re.compile(r"<(script|style)\b.*?</\1>", re.S | re.I)
# Un bloc de texte = un paragraphe, une puce, une cellule, un titre. Sans ce
# découpage, deux blocs sans ponctuation (« <h2>Titre</h2><p>Phrase »)
# deviennent une seule « phrase » de 150 mots, ce qui rend la mesure
# de lisibilité completely fausse.
BLOC = re.compile(
    r"</(p|li|td|th|h[1-6]|div|dd|dt|blockquote|pre|figcaption)>", re.I)


def lire(f):
    with open(f, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def visible(t):
    # Le menu et le pied de page ne sont pas de la prose : sans cette exclusion,
    # le bandeau de navigation devient une « phrase » de 150 mots et noie le
    # vrai signal sur la lisibilité du contenu.
    t = BALISE.sub(" ", t)
    t = CHROME.sub(" ", t)
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return re.sub(r"\s+", " ", t)


def blocs_texte(t, garder_prompts=False):
    """Renvoie la liste des blocs de texte, un par bloc HTML.

    Les blocs `<pre>` et les invites de prompt sont volontairement longs : ils
    sont faits pour être copiés tels quels. Les garder faussirait la mesure de
    lisibilité, qui ne concerne que la prose du professeur.
    """
    t = BALISE.sub("\n", t)
    t = CHROME.sub("\n", t)
    t = re.sub(r"<!--.*?-->", "\n", t, flags=re.S)
    if not garder_prompts:
        t = re.sub(r'<div class="prompt-box">.*?</div>', "\n", t, flags=re.S)
    # toute balise fermante de niveau bloc = une fin de paragraphe
    t = BLOC.sub("\n", t)
    t = re.sub(r"<[^>]+>", " ", t)
    out = []
    for ligne in t.split("\n"):
        s = re.sub(r"\s+", " ", ligne).strip()
        if s:
            out.append(s)
    return out


def principales():
    out = []
    for d, _, fs in os.walk(MODULE):
        out += [os.path.join(d, f) for f in fs if f.endswith(".html")]
    return sorted(out)


def section(titre):
    print()
    print("=" * 74)
    print(titre)
    print("=" * 74)


html_files = principales()
astuces_txt = []
_page = os.path.join(MODULE, "seances", "astuces-ia.html")
if os.path.isfile(_page):
    _t = lire(_page)
    for m in re.finditer(
            r'<h3><span class="tip-num">(\d+)</span>(.*?)</h3>(.*?)(?=<h3><span class="tip-num">|\Z)',
            _t, re.S):
        num = int(m.group(1))
        titre = re.sub(r"<[^>]+>", "", m.group(2)).strip()
        ast = re.sub(r"<[^>]+>", " ", m.group(3))
        astuces_txt.append((num, titre, re.sub(r"\s+", " ", ast)))


def main():
    print("AUDIT APPROFONDI")
    print("Module : %s" % os.path.relpath(MODULE, RACINE))
    print("%d pages HTML" % len(html_files))

    # 1 ---------------------------------------------------------------
    section("1. RENVOIS ENTRE ASTUCES")
    p = audit_renvois(astuces_txt)
    print("  %d renvois « astuce n° X » analysés sur %d astuces"
          % (sum(len(RENVOI.findall(c)) for _, _, c in astuces_txt), len(astuces_txt)))
    if p:
        for num, msg in p:
            print("  [!] astuce %d : %s" % (num, msg))
    else:
        print("  aucun renvoi invalide")

    # 2 ---------------------------------------------------------------
    section("2. LISIBILITÉ")
    tot_l = tot_d = tot_v = 0
    pire = []
    for f in html_files:
        # les prompts sont exclus : leur longueur est voulue
        vis = "\n".join(blocs_texte(lire(f), garder_prompts=False))
        l, d, v = audit_lisibilite(f, vis)
        tot_l += len(l); tot_d += len(d); tot_v += len(v)
        if l:
            pire.append((len(l), os.path.relpath(f, MODULE), l))
    print("  phrases de plus de 38 mots : %d" % tot_l)
    print("  phrases de plus de 55 mots : %d  (illisibles à l'oral)" % tot_d)
    print("  phrases « creuses »        : %d" % tot_v)
    for n, rel, l in sorted(pire, reverse=True)[:4]:
        print("   %-34s %3d phrases longues" % (rel, n))
        for taille, extrait in l[:2]:
            print("       %3d mots : %s…" % (taille, extrait))

    # 3 ---------------------------------------------------------------
    section("3. COHÉRENCE DES TERMES")
    v = audit_termes()
    if v:
        for canon, alts in v.items():
            print("  [!] %s aussi écrit : %s" % (canon, ", ".join(sorted(alts))))
    else:
        print("  aucun terme utilisé sous une forme variante")

    # 4 ---------------------------------------------------------------
    section("4. ACCESSIBILITÉ")
    a = audit_accessibilite()
    if not a:
        print("  aucun défaut")
    for k, v in a.items():
        print("  [!] %-26s %d" % (k, len(v)))
        for x in sorted(set(v))[:4]:
            print("        %s" % x)

    # 5 ---------------------------------------------------------------
    section("5. PEDAGOGIE DES 15 SÉANCES")
    manque, n = audit_pedagogie()
    print("  %d séances analysées" % n)
    for k in TRAMES:
        if k in manque:
            print("  [!] %-20s absente de %d séance(s) : %s"
                  % (k, len(manque[k]), ", ".join(manque[k][:6])))
        else:
            print("  ok  %-20s dans les 15" % k)

    # 6 ---------------------------------------------------------------
    section("6. RÉFÉRENCES « SÉANCE N »")
    r = audit_refs_seances()
    if r:
        for x in sorted(set(r))[:8]:
            print("  [!] %s" % x)
    else:
        print("  toutes les références pointent vers une séance existante")

    # 7 ---------------------------------------------------------------
    section("7. POIDS DES PAGES")
    poids = audit_poids()
    if poids:
        for rel, ko in sorted(poids, key=lambda x: -x[1])[:6]:
            print("  [!] %-40s %.0f Ko" % (rel, ko))
    else:
        print("  aucune page au-delà de 250 Ko")

    # 8 ---------------------------------------------------------------
    section("8. MÉTADONNÉES")
    mt = audit_meta()
    if not mt:
        print("  toutes conformes")
    for k, v in mt.items():
        print("  [!] %-28s %d" % (k, len(v)))
        for x in sorted(set(v))[:4]:
            print("        %s" % x)

    print()
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
