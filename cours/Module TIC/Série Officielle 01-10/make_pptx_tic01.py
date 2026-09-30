#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère la présentation PowerPoint du cours TIC 01
(Introduction aux Technologies de l'Information et de la Communication).

Le contenu est RELU dans Cours_TIC_01_Introduction_aux_TIC_FR.html : titres,
listes, tableaux et encadrés viennent du cours, donc la présentation ne peut
pas diverger de la page. Seuls les schémas de synthèse sont dessinés ici.

Sortie : Cours_TIC_01_Introduction_aux_TIC_FR_pptx.pptx (16:9)
"""
import os
import re
import sys
from html import unescape

DOSSIER = os.path.dirname(os.path.abspath(__file__))
# cours/Module TIC/Série Officielle 01-10 -> on remonte jusqu'a la racine du site
RACINE = os.path.abspath(os.path.join(DOSSIER, "..", "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "scripts"))

import pptx_commun as C  # noqa: E402

COURS = os.path.join(DOSSIER, "Cours_TIC_01_Introduction_aux_TIC_FR.html")
SORTIE = os.path.join(DOSSIER, "Cours_TIC_01_Introduction_aux_TIC_FR_pptx.pptx")
IMAGES = os.path.join(RACINE, "images")
LOGO_UNIV = os.path.join(IMAGES, "Université_de_Mostaganem.png")
LOGO_FLE = os.path.join(IMAGES, "LOGO-FLE-UNIV-Mosta.jpeg")
CACHE_LOGOS = os.path.join(DOSSIER, "logos_pptx")

PIED = "TIC 01 — Introduction aux TIC  |  Dr. Madani BELACEL — Université de Mostaganem"


# ===========================================================================
# 1. Lecture du cours
# ===========================================================================
def _inner(s, debut_balise):
    """Contenu d'une balise, balise de fermeture comprise."""
    i = s.find(debut_balise, debut_balise and 0)
    return None


def decouper_balises(bloc, balise):
    """Renvoie [(contenu_interne, attributs), ...] pour toutes les <balise>.

    Gere l'imbrication en comptant les ouvertures et fermetures de la meme
    balise : une <li> ne contient pas de <li>, mais un <div> peut contenir
    plusieurs <p>, il faut donc un vrai compteur.
    """
    res = []
    for m in re.finditer(r"<%s\b([^>]*)>" % balise, bloc):
        if m.start() < 0:
            continue
        # on repart de cette ouverture et on compte jusqu'a la fermeture
        # correspondante
        prof = 1
        pos = m.end()
        while prof > 0:
            n = re.compile(r"<%s\b[^>]*>|</%s>" % (balise, balise)).search(bloc, pos)
            if not n:
                break
            if n.group(0).startswith("</"):
                prof -= 1
            elif not n.group(0).endswith("/>"):
                prof += 1
            pos = n.end()
        interne = bloc[m.end():n.start() if n else len(bloc)]
        res.append((interne, m.group(1), m.start()))
    return res


def lire_cours(chemin):
    s = open(chemin, encoding="utf-8").read()
    # le corps commence au <h2> qui PORTE le titre de la section 1, et non au
    # texte du titre : sinon la premiere section est sautee.
    repere = s.find("1. Introduction et Importance des TIC")
    debut = s.rfind("<h2", 0, repere) if repere > 0 else 0
    fin = s.find("Bibliographie", s.find("9. Conclusion"))
    corps = s[debut:fin] if fin > debut else s[debut:]

    sections = []
    for m in re.finditer(r"<h2[^>]*>(.*?)</h2>", corps, re.S):
        titre_html = m.group(1)
        num = re.match(r"\s*(\d+)\.", C.plain(titre_html))
        if not num:
            continue
        n = int(num.group(1))
        fin_sec = corps.find("<h2", m.end())
        contenu = corps[m.end():fin_sec] if fin_sec > 0 else corps[m.end():]
        duree = re.search(r"(\d+)\s*min", C.plain(titre_html))
        # le numero est affiche separement (pastille) : on l'enleve du titre
        titre = re.sub(r"^\s*\d+\.\s*", "", C.plain(titre_html))
        titre = re.sub(r"\s*\(\d+\s*min\)\s*$", "", titre).strip()
        sections.append({
            "n": n,
            "titre": titre,
            "duree": int(duree.group(1)) if duree else None,
            "blocs": lire_blocs(contenu),
        })
    return sections


def lire_blocs(contenu):
    """Decoupe une section en blocs : ('h3', texte), ('p', texte, encadre),
    ('ul'|'ol', [puces]), ('table', entetes, lignes)."""
    blocs = []
    pos = 0
    for m in re.finditer(r"<h3[^>]*>(.*?)</h3>|<ul[^>]*>|<ol[^>]*>|"
                         r"<table[^>]*>|<p[^>]*>(.*?)</p>|<pre[^>]*>", contenu, re.S):
        if m.start() < pos:
            continue
        tag = m.group(0)
        if tag.startswith("<h3"):
            blocs.append(("h3", C.plain(m.group(1))))
        elif tag in ("<ul>", "<ol>") or tag.startswith("<ul") or tag.startswith("<ol"):
            balise = "ul" if tag.startswith("<ul") else "ol"
            fin_balise = decouper_balises(contenu[m.start():], balise)
            if not fin_balise:
                continue
            interne = fin_balise[0][0]
            pos = m.start() + fin_balise[0][2] + len("<%s>" % balise) + len(interne) + len("</%s>" % balise)
            puces = [C.plain(x[0]) for x in decouper_balises(interne, "li")]
            if puces:
                blocs.append((balise, puces))
        elif tag.startswith("<table"):
            pieces = decouper_balises(contenu[m.start():], "table")
            if not pieces:
                continue
            tbl = pieces[0][0]
            pos = m.start() + pieces[0][2] + len("<table>") + len(tbl) + len("</table>")
            lignes = []
            for tr in decouper_balises(tbl, "tr"):
                cells = [C.plain(c[0]) for c in decouper_balises(tr[0], "td")] or \
                        [C.plain(c[0]) for c in decouper_balises(tr[0], "th")]
                if cells:
                    lignes.append(cells)
            if lignes:
                entetes = lignes[0]
                blocs.append(("table", entetes, lignes[1:]))
        elif tag.startswith("<pre"):
            pos = m.end()
        else:
            texte = C.plain(m.group(2) or "")
            if texte:
                encadre = texte.lower().startswith(("à retenir", "a retenir"))
                blocs.append(("p", texte, encadre))
            pos = m.end()
    return blocs


# ===========================================================================
# 2. Rendu
# ===========================================================================
prs, VIDE = C.nouveau_conteneur()


def bullet(slide, x, y, w, items, t, numerote=False, couleur=None):
    """Liste a puces ; renvoie la hauteur occupee."""
    couleur = couleur or C.DARK
    h = 0.0
    for i, item in enumerate(items, 1):
        marque = ("%d." % i) if numerote else "▪"
        lg = C.lignes_requises(marque + "  " + item, w - 0.34, t)
        hh = lg * t * 1.18 / 72.0
        tf = C.add_textbox(slide, x, y, w, hh + 0.04)
        C.add_paragraph(tf, [(marque + "  ", {"size": t, "bold": True, "color": C.BLUE}),
                             (item, {"size": t, "color": couleur})],
                        line_spacing=1.18, space_after=0)
        y += hh + 0.09
        h += hh + 0.09
    return h


def largeurs_colonnes(n, w):
    """30 % pour la premiere colonne, le reste reparti egalement."""
    largeurs = [w * 0.30] + [w * 0.70 / max(1, n - 1)] * (n - 1)
    return largeurs


def hauteur_ligne(cells, largeurs, t):
    """Hauteur d'une ligne de tableau.

    PowerPoint agrandit une ligne dont le texte passe sur deux lignes, et le
    texte suivant se retrouve alors sous le tableau. Il faut donc ESTIMER la
    hauteur au lieu de supposer une hauteur fixe.
    """
    h = 0.0
    for c, txt in enumerate(cells):
        lc = largeurs[c] if c < len(largeurs) else largeurs[-1]
        lg = C.lignes_requises(txt, lc - 0.16, t)
        h = max(h, lg * t * 1.12 / 72.0 + 0.12)
    return max(0.34, h)


def tableau(slide, x, y, w, entetes, lignes, t=13):
    """Tableau PowerPoint natif (donc editable). Renvoie la hauteur reelle."""
    n = len(entetes)
    largeurs = largeurs_colonnes(n, w)
    h_ent = hauteur_ligne(entetes, largeurs, t)
    hauteurs = [h_ent] + [hauteur_ligne(l, largeurs, t) for l in lignes]
    h = sum(hauteurs) + 0.06
    forme = slide.shapes.add_table(len(lignes) + 1, n, C.Inches(x), C.Inches(y),
                                   C.Inches(w), C.Inches(h))
    tbl = forme.table
    for c in range(n):
        tbl.columns[c].width = C.Inches(largeurs[c])
    for r, hh in enumerate(hauteurs):
        tbl.rows[r].height = C.Inches(hh)
    for c, txt in enumerate(entetes):
        cell = tbl.cell(0, c)
        cell.fill.solid()
        cell.fill.fore_color.rgb = C.NAVY
        cell.text = txt
    for r, ligne in enumerate(lignes, 1):
        for c in range(n):
            val = ligne[c] if c < len(ligne) else ""
            cell = tbl.cell(r, c)
            cell.fill.solid()
            cell.fill.fore_color.rgb = C.WHITE if r % 2 else C.GREY_L
            cell.text = val
    for r in range(len(lignes) + 1):
        for c in range(n):
            cell = tbl.cell(r, c)
            cell.margin_left = C.Inches(0.07)
            cell.margin_right = C.Inches(0.07)
            cell.margin_top = C.Inches(0.03)
            cell.margin_bottom = C.Inches(0.03)
            cell.vertical_anchor = C.MSO_ANCHOR.MIDDLE
            for p in cell.text_frame.paragraphs:
                p.line_spacing = 1.0
                for run in p.runs:
                    run.font.size = C.Pt(t)
                    run.font.name = C.FONT
                    run.font.bold = (r == 0)
                    run.font.color.rgb = C.WHITE if r == 0 else C.DARK
    return h


def encadre(slide, x, y, w, texte):
    """Boite « A retenir ».

    Le cours ecrit deja « A retenir : … » dans le paragraphe ; on retire ce
    prefixe, sinon la diapo affiche « A retenir — A retenir : … ».
    """
    texte = re.sub(r"^.{0,16}?retenir\s*[:\u2014-]\s*", "", texte,
                   flags=re.I | re.S).strip()
    t = C.TAILLE_TEXTE_MAX - 1.0
    lg = C.lignes_requises(texte, w - 0.44, t)
    h = lg * t * 1.18 / 72.0 + 0.30
    C.add_shape(slide, C.MSO_SHAPE.ROUNDED_RECTANGLE, x, y, w, h,
                fill=C.AMBER_L, line=C.AMBER, line_w=1.25, radius=0.06)
    C.add_shape(slide, C.MSO_SHAPE.RECTANGLE, x, y, 0.06, h, fill=C.AMBER)
    tf = C.add_textbox(slide, x + 0.24, y + 0.15, w - 0.44, h - 0.30)
    p = tf.paragraphs[0]
    r = p.add_run()
    r.text = "À retenir — "
    r.font.size = C.Pt(t)
    r.font.bold = True
    r.font.color.rgb = C.RGBColor(0x7A, 0x42, 0x05)
    r.font.name = C.FONT
    r2 = p.add_run()
    r2.text = texte
    r2.font.size = C.Pt(t)
    r2.font.color.rgb = C.DARK
    r2.font.name = C.FONT
    p.line_spacing = 1.18
    return h


def sous_titre(slide, y, texte, t=None):
    """Titre de sous-partie a l'interieur d'une diapositive ; renvoie le y suivant."""
    t = t or (C.TAILLE_TEXTE_MAX + 1.5)
    lg = C.lignes_requises(texte, C.CONTENU_D, t)
    h = lg * t * 1.2 / 72.0 + 0.08
    C.add_paragraph(C.add_textbox(slide, 0.85, y, C.CONTENU_D, h),
                    [(texte, {"size": t, "bold": True, "color": C.BLUE})],
                    space_after=0)
    return y + h + 0.06


def hauteur_bloc(bloc, t, largeur=C.CONTENU_D):
    kind = bloc[0]
    if kind == "h3":
        return 0.46
    if kind in ("ul", "ol"):
        h = 0.0
        for item in bloc[1]:
            lg = C.lignes_requises("▪  " + item, largeur - 0.34, t)
            h += lg * t * 1.18 / 72.0 + 0.09
        return h
    if kind == "table":
        lc = largeurs_colonnes(len(bloc[1]), largeur)
        tt = C.TAILLE_TEXTE_MAX - 2.0
        hh = hauteur_ligne(bloc[1], lc, tt)
        for ligne in bloc[2]:
            hh += hauteur_ligne(ligne, lc, tt)
        return hh + 0.06
    if kind == "p":
        lg = C.lignes_requises(bloc[1], largeur - 0.10, t)
        return lg * t * 1.18 / 72.0 + (0.30 if bloc[2] else 0.04)
    return 0.0


def diapo_section(s, section, blocs, num_page, suite=False):
    """Une diapositive de contenu : titre de section + une suites de blocs."""
    titre = section["titre"] + (" (suite)" if suite else "")
    # On mesure sur 9,5 po et non 10,3 : la police est grasse, et un titre
    # mesuré « au pixel près » passait d'une ligne a deux — le tableau
    # commencement alors dessous.
    if suite:
        t_titre = C.TAILLE_TITRE - 4
    else:
        t_titre = C.taille_qui_tient(titre, 9.5, 0.80, maxi=C.TAILLE_TITRE, mini=19)
    y = 0.58
    # un titre long passe sur deux lignes : on mesure pour ne pas percuter
    # le contenu qui suit
    lg = C.lignes_requises(titre, 9.5, t_titre)
    h_titre = lg * t_titre * 1.1 / 72.0 + 0.10
    tf = C.add_textbox(s, 0.75, y, 10.3, h_titre)
    C.add_paragraph(tf, [(titre, {"size": t_titre, "bold": True, "color": C.NAVY})],
                    line_spacing=1.0, space_after=0)
    y += h_titre + 0.12

    if not suite:
        # la pastille de duree est a droite du titre : posee au-dessus, elle le
        # recouvrait (le titre occupe 0.58 -> 1.40 po).
        pastille = ("%d min" % section["duree"]) if section.get("duree") \
            else "Section %d" % section["n"]
        y_p = 0.58 + (h_titre - 0.42) / 2
        C.add_shape(s, C.MSO_SHAPE.ROUNDED_RECTANGLE, 11.15, y_p, 1.42, 0.42,
                    fill=C.AMBER, radius=0.45)
        tfp = C.add_textbox(s, 11.15, y_p, 1.42, 0.42, anchor=C.MSO_ANCHOR.MIDDLE)
        C.add_paragraph(tfp, [(pastille, {"size": C.TAILLE_PASTILLE + 0.5,
                                          "bold": True, "color": C.NAVY})],
                        align=C.PP_ALIGN.CENTER, space_after=0)

    # taille du texte, ajustee pour que tout tienne
    t = C.TAILLE_TEXTE_MAX
    while t > 12.0:
        if sum(hauteur_bloc(b, t) for b in blocs) <= 6.68 - y:
            break
        t -= 0.5

    for bloc in blocs:
        if bloc[0] == "h3":
            y = sous_titre(s, y, bloc[1], t + 1.0)
        elif bloc[0] in ("ul", "ol"):
            y += bullet(s, 0.85, y, C.CONTENU_D, bloc[1], t, numerote=(bloc[0] == "ol"))
        elif bloc[0] == "table":
            y += tableau(s, 0.85, y, C.CONTENU_D, bloc[1], bloc[2], t - 2.0) + 0.14
        elif bloc[0] == "p":
            if bloc[2]:
                y += encadre(s, 0.85, y, C.CONTENU_D, bloc[1]) + 0.16
            else:
                lg = C.lignes_requises(bloc[1], C.CONTENU_D - 0.10, t)
                hh = lg * t * 1.18 / 72.0
                tf = C.add_textbox(s, 0.85, y, C.CONTENU_D, hh + 0.04)
                C.add_paragraph(tf, [(bloc[1], {"size": t, "color": C.DARK})],
                                line_spacing=1.18, space_after=0)
                y += hh + 0.18

    C.add_footer(s, num_page, PIED)
    return notes_de_la_diapo(section, blocs, suite)


def repartir(blocs, t_max, dispo):
    """Decoupe la suite de blocs d'une section en diapositives.

    Une diapositive de fin qui ne contiendrait que deux lignes est inutile :
    diapo_section reduit deja la police pour que tout tienne, on fusionne donc
    le dernier lot avec l'avant-dernier plutot que d'afficher une diapo vide.
    """
    lots, lot, h = [], [], 0.0
    for b in blocs:
        hb = hauteur_bloc(b, t_max)
        if lot and h + hb > dispo:
            lots.append(lot)
            lot, h = [], 0.0
        lot.append(b)
        h += hb + 0.10
    if lot:
        lots.append(lot)
    # un titre de partie seul en bas de diapositive est Separé de son tableau
    # ou de sa liste, qui se retrouvent sur la diapositive suivante : on le
    # rattache au lot suivant.
    for k in range(len(lots) - 1):
        while lots[k] and lots[k][-1][0] == "h3":
            lots[k + 1].insert(0, lots[k].pop())
    if len(lots) >= 2:
        dernier = sum(hauteur_bloc(b, t_max) for b in lots[-1])
        precedent = sum(hauteur_bloc(b, t_max) for b in lots[-2])
        if dernier < dispo * 0.30 and precedent + dernier <= dispo * 1.35:
            lots[-2:] = [lots[-2] + lots[-1]]
    return [lot for lot in lots if lot] or [[]]


def notes_de_la_diapo(section, blocs, suite=False):
    """Notes du presentateur : ce qu'il faut dire sur CETTE diapositive.

    Reprendre seulement le titre de la section ne sert a rien pendant
    l'explication : on y met les sous-parties, les puces et les encadres
    « A retenir » tels qu'ils apparaissent a l'ecran.
    """
    lignes = []
    if suite:
        lignes.append("Suite — %s" % section["titre"])
    else:
        tete = "Section %d — %s" % (section["n"], section["titre"])
        if section.get("duree"):
            tete += "  (%d min)" % section["duree"]
        lignes.append(tete)
    lignes.append("")

    for b in blocs:
        kind = b[0]
        if kind == "h3":
            lignes.append("• %s" % b[1])
        elif kind in ("ul", "ol"):
            for item in b[1]:
                lignes.append("   - %s" % item)
        elif kind == "p":
            if b[2]:
                lignes.append("   A RETENIR : %s"
                              % re.sub(r"^.{0,16}?retenir\s*[:\u2014-]\s*", "", b[1],
                                       flags=re.I | re.S).strip())
            else:
                lignes.append("   %s" % b[1])
        elif kind == "table":
            lignes.append("   Tableau : %s" % " | ".join(b[1]))
            for ligne in b[2]:
                lignes.append("      %s" % " | ".join(ligne))
    return "\n".join(lignes)


# ===========================================================================
# 3. Construction
# ===========================================================================
def main():
    sections = lire_cours(COURS)
    if not sections:
        print("aucune section trouvee dans", COURS)
        return 1
    print("sections lues :", len(sections))

    # ---- couverture ----
    s = prs.slides.add_slide(VIDE)
    C.couverture(
        s, LOGO_UNIV, LOGO_FLE,
        titre="Introduction aux TIC",
        sous_titre="Technologies de l'Information et de la Communication — "
                   "définitions, évolution, usages",
        badge="Cours TIC 01",
        auteur="Dr. Madani BELACEL — MCB",
        mention="Année universitaire 2026 – 2027",
        adresse="Cours en ligne : madani-belacel.github.io/site-enseignement-belacel",
        cache=CACHE_LOGOS)
    C.ecrire_notes(s, "Cours TIC 01 — Introduction aux Technologies de l'Information "
                      "et de la Communication.\nDr. Madani BELACEL — MCB — Université de "
                      "Mostaganem.\n9 sections, durée indicative 105 minutes.\n"
                      "Les QCM d'auto-évaluation sont en fin de présentation.")

    # ---- plan ----
    s = prs.slides.add_slide(VIDE)
    C.add_paragraph(C.add_textbox(s, 0.75, 0.55, 12.0, 0.7), [("Plan du cours", {
        "size": C.TAILLE_TITRE, "bold": True, "color": C.NAVY})], space_after=0)
    total = sum(x.get("duree") or 0 for x in sections)
    y = 1.55
    for sec in sections:
        C.add_shape(s, C.MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, y, C.CONTENU_D, 0.46,
                    fill=C.GREY_L, line=C.LINE_C, line_w=0.75, radius=0.10)
        badge = C.add_shape(s, C.MSO_SHAPE.OVAL, 0.98, y + 0.045, 0.40, 0.40,
                            fill=C.BLUE)
        tfb = badge.text_frame
        tfb.vertical_anchor = C.MSO_ANCHOR.MIDDLE
        tfb.margin_left = tfb.margin_right = 0
        tfb.margin_top = tfb.margin_bottom = 0
        tfb.word_wrap = False
        p = tfb.paragraphs[0]
        p.text = str(sec["n"])
        p.alignment = C.PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = C.Pt(13)
            r.font.bold = True
            r.font.color.rgb = C.WHITE
            r.font.name = C.FONT
        t_sec = C.taille_qui_tient(sec["titre"], 8.6, 0.46, maxi=17, mini=12)
        C.add_paragraph(C.add_textbox(s, 1.48, y, 8.6, 0.46, anchor=C.MSO_ANCHOR.MIDDLE),
                        [(sec["titre"], {"size": t_sec, "color": C.DARK})], space_after=0)
        C.add_paragraph(C.add_textbox(s, 10.3, y, 2.1, 0.46, anchor=C.MSO_ANCHOR.MIDDLE),
                        [("%d min" % sec["duree"] if sec.get("duree") else "",
                         {"size": 13, "bold": True, "color": C.AMBER})],
                        align=C.PP_ALIGN.RIGHT, space_after=0)
        y += 0.53
    C.add_paragraph(C.add_textbox(s, 0.85, y + 0.05, C.CONTENU_D, 0.4),
                    [("Durée indicative totale : %d minutes" % total,
                      {"size": 13, "bold": True, "color": C.NAVY})], space_after=0)
    C.add_footer(s, 2, PIED)

    # ---- une ou plusieurs diapositives par section ----
    page = 2
    for sec in sections:
        blocs = sec["blocs"]
        if not blocs:
            continue
        dispo = 6.68 - 1.72
        lots = repartir(blocs, C.TAILLE_TEXTE_MAX, dispo)
        for k, lot in enumerate(lots):
            page += 1
            s = prs.slides.add_slide(VIDE)
            notes = diapo_section(s, sec, lot, page, suite=(k > 0))
            C.ecrire_notes(s, notes)

    # ---- QCM : pagine, car 5 questions x 4 propositions ne tiennent pas ----
    questions, corriges = lire_qcm(COURS)
    if questions:
        for avec_corrige in (False, True):
            t_q, t_o, t_r = 16.0, 12.5, 12.5
            items = []
            for k, q in enumerate(questions):
                lg = C.lignes_requises("%d. %s" % (q["n"], q["q"]), C.CONTENU_D, t_q)
                h = lg * t_q * 1.2 / 72.0 + 0.06
                lignes = []
                if avec_corrige and k < len(corriges):
                    lettre, motif = corriges[k]
                    txt = "Réponse %s — %s" % (lettre, motif)
                    lg2 = C.lignes_requises(txt, C.CONTENU_D - 0.30, t_r)
                    lignes.append((1.05, C.CONTENU_D - 0.30, txt, t_r, C.GREEN))
                    h += lg2 * t_r * 1.2 / 72.0 + 0.06
                for o in q["opts"]:
                    txt = "      " + o
                    lg3 = C.lignes_requises(txt, C.CONTENU_D, t_o)
                    lignes.append((0.95, C.CONTENU_D, txt, t_o, C.GREY))
                    h += lg3 * t_o * 1.2 / 72.0 + 0.04
                items.append({"q": "%d. %s" % (q["n"], q["q"]), "t": t_q,
                              "h": h + 0.16, "lignes": lignes})

            dispo = 6.68 - 1.50
            lots, lot, h = [], [], 0.0
            for it in items:
                if lot and h + it["h"] > dispo:
                    lots.append(lot)
                    lot, h = [], 0.0
                lot.append(it)
                h += it["h"]
            if lot:
                lots.append(lot)

            for k, lot in enumerate(lots):
                page += 1
                s = prs.slides.add_slide(VIDE)
                base = ("Corrigé de l'auto-évaluation" if avec_corrige
                        else "Auto-évaluation — QCM")
                titre = (base if len(lots) == 1
                         else "%s (%d/%d)" % (base, k + 1, len(lots)))
                C.add_paragraph(C.add_textbox(s, 0.75, 0.55, 12.0, 0.7),
                                [(titre, {"size": C.TAILLE_TITRE, "bold": True,
                                          "color": C.NAVY})], space_after=0)
                y = 1.50
                for it in lot:
                    lg = C.lignes_requises(it["q"], C.CONTENU_D, it["t"])
                    hh = lg * it["t"] * 1.2 / 72.0 + 0.06
                    C.add_paragraph(C.add_textbox(s, 0.85, y, C.CONTENU_D, hh),
                                    [(it["q"], {"size": it["t"], "bold": True,
                                                "color": C.NAVY})],
                                    line_spacing=1.2, space_after=0)
                    y += hh
                    for x, w, txt, t, col in it["lignes"]:
                        lg2 = C.lignes_requises(txt, w, t)
                        h2 = lg2 * t * 1.2 / 72.0 + 0.05
                        C.add_paragraph(C.add_textbox(s, x, y, w, h2),
                                        [(txt, {"size": t, "color": col})],
                                        line_spacing=1.2, space_after=0)
                        y += h2
                    y += 0.10
                C.add_footer(s, page, PIED)
                C.ecrire_notes(s,
                               "Laisser 5 minutes de redaction, puis corriger a "
                               "l'oral : chaque reponse se justifie par le "
                               "contenu de la section concernee (definition, "
                               "trois dimensions, NTIC vs TIC, dimension "
                               "communication).")

    prs.save(SORTIE)
    print("OK ->", SORTIE)
    print("  diapositives :", len(prs.slides._sldIdLst))
    print("  taille : %.1f Ko" % (os.path.getsize(SORTIE) / 1024))
    return 0


def lire_qcm(chemin):
    """Questions et corrige du QCM final, s'il y en a un.

    Le cours les ecrit en paragraphes : « Question 1 : … » suivi des
    propositions « - A) … », puis un <ol> de corrige.
    """
    s = open(chemin, encoding="utf-8").read()
    i = s.find("QCM d'auto")
    if i < 0:
        return [], []
    j = s.find("Corrigé du QCM", i)
    if j < 0:
        return [], []

    questions = []
    for p in re.findall(r"<p[^>]*>(.*?)</p>", s[i:j], re.S):
        texte = C.plain(p)
        m = re.match(r"Question\s*(\d+)\s*:\s*(.*)", texte)
        if not m:
            continue
        corps = m.group(2)
        options = re.findall(r"-\s*([A-D])\)\s*(.*?)(?=\s*-\s*[A-D]\)|$)", corps)
        question = re.split(r"\s*-\s*[A-D]\)", corps)[0].strip() or corps
        propositions = ["%s) %s" % (l, t.strip()) for l, t in options]
        questions.append({"n": int(m.group(1)), "q": question, "opts": propositions})

    corriges = []
    for ol in re.findall(r"<ol[^>]*>(.*?)</ol>", s[j:], re.S):
        for li in decouper_balises(ol, "li"):
            t = C.plain(li[0])
            m = re.match(r"([A-D])\s*[—-]\s*(.*)", t)
            if m:
                corriges.append((m.group(1), m.group(2).strip()))
    return questions, corriges


if __name__ == "__main__":
    sys.exit(main())
