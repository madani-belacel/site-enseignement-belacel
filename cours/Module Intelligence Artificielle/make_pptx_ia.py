#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genere les presentations PowerPoint des cours Q/R du module
Intelligence Artificielle.

Contenu RELU dans les pages HTML (scripts/lecteur_qr.py) : titres,
explications, questions/reponses et schemas. La presentation ne peut donc
pas diverger du cours.

Une diapositive par idee :
  - le pastille « Idee n », le titre ;
  - l'explication francaise, en gros (jusqu'a TAILLE_TEXTE_MAX) ;
  - le schema de l'idee s'il existe ;
  - sinon les questions de la seance, en bas de diapo (les reponses restent
    dans les notes : les cours 02 a 05 n'ont aucun schema, sans cela la
    diapo serait vide).
Les questions ET reponses sont dans les notes du presentateur.

La presentation est en francais seul : le module est destine a la 2eme
annee PEP (ENS, filiere Francais). Mettre LANGUES = ("fr", "en") pour la
version bilingue.

Usage :
  python3 make_pptx_ia.py                    # cours 02 a 05
  python3 make_pptx_ia.py --tous             # y compris le cours 01
  python3 make_pptx_ia.py --cours QR_IA_03_Exemples_Simples_IA
"""
import os
import re
import sys

RACINE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                       "..", ".."))
sys.path.insert(0, os.path.join(RACINE, "scripts"))

import pptx_commun as C          # noqa: E402
import lecteur_qr as L           # noqa: E402

DOSSIER = os.path.dirname(os.path.abspath(__file__))
SORTIE = os.path.join(DOSSIER, "Presentations_PPTX")
LOGO_UNIV = os.path.join(RACINE, "images", "Université_de_Mostaganem.png")
LOGO_FLE = os.path.join(RACINE, "images", "LOGO-FLE-UNIV-Mosta.jpeg")
CACHE_LOGOS = os.path.join(DOSSIER, "logos_pptx")

# Langues affichees. Le module est en 2eme annee PEP (ENS, filiere Francais) :
# la seance se donne en francais. Mettre ("fr", "en") pour le bilingue.
LANGUES = ("fr",)
BILINGUE = len(LANGUES) > 1

COURS = {
    "QR_IA_01_Introduction_IA": "Introduction à l'IA",
    "QR_IA_02_Comment_Fonctionne_IA": "Comment fonctionne l'IA",
    "QR_IA_03_Exemples_Simples_IA": "Exemples simples d'IA",
    "QR_IA_04_Realiser_IA": "Comment réaliser une IA",
    "QR_IA_05_Premier_Projet_IA": "Ton premier projet IA",
}

TITRES = {
    "QR_IA_01_Introduction_IA": "Introduction à l'Intelligence Artificielle",
    "QR_IA_02_Comment_Fonctionne_IA": "Comment fonctionne l'IA",
    "QR_IA_03_Exemples_Simples_IA": "Exemples simples d'IA",
    "QR_IA_04_Realiser_IA": "Comment réaliser une IA",
    "QR_IA_05_Premier_Projet_IA": "Ton premier projet IA",
}

ACCROCHES = {
    "QR_IA_01_Introduction_IA":
        "Comprendre l'IA, ses usages et ses limites — puis réaliser sa première IA",
    "QR_IA_02_Comment_Fonctionne_IA":
        "Données, exemple, régularité : pourquoi une IA répond juste — ou se trompe",
    "QR_IA_03_Exemples_Simples_IA":
        "L'IA au quotidien : téléphone, courriel, cartes, santé, jeux, véhicules",
    "QR_IA_04_Realiser_IA":
        "La méthode en 6 étapes, du problème bien posé à l'IA qui fonctionne",
    "QR_IA_05_Premier_Projet_IA":
        "Un projet complet, gratuit et simple, avec du vrai code",
}


def pied(slide, n):
    C.add_footer(slide, n,
                 "IA %s  |  Dr. Madani BELACEL — Université de Mostaganem"
                 % os.environ.get("IA_NUM", "01"))


def bloc_questions(slide, y, questions, largeur=C.CONTENU_D):
    """Encadre « Questions de la seance » ; renvoie la hauteur utilisee."""
    if not questions:
        return 0.0
    t = 15.0
    while t > 11.0:
        h = 0.44 + sum(C.hauteur_requise(q, largeur - 0.60, t) + 0.06
                       for q in questions)
        if h <= 2.30:
            break
        t -= 0.5
    h = 0.44 + sum(C.hauteur_requise(q, largeur - 0.60, t) + 0.08
                   for q in questions) + 0.10
    C.add_shape(slide, C.MSO_SHAPE.ROUNDED_RECTANGLE, 0.85, y, largeur, h,
                fill=C.GREY_L, line=C.LINE_C, line_w=1.0, radius=0.05)
    C.add_paragraph(C.add_textbox(slide, 1.05, y + 0.13, largeur - 0.40, 0.3),
                    [("Questions de la séance", {"size": 12.5, "bold": True,
                                                  "color": C.BLUE})],
                    space_after=0)
    yy = y + 0.44
    for i, q in enumerate(questions, 1):
        hh = C.hauteur_requise(q, largeur - 0.60, t)
        C.add_paragraph(C.add_textbox(slide, 1.05, yy, largeur - 0.40, hh + 0.04),
                        [("%d. " % i, {"size": t, "bold": True, "color": C.AMBER}),
                         (re.sub(r"^Q\d+\.\s*", "", q), {"size": t, "color": C.DARK})],
                        line_spacing=1.15, space_after=0)
        yy += hh + 0.08
    return h


def diapo_idee(slide, idee, n, schema, questions, page):
    """Une diapositive : titre, explication, schema ou questions."""
    # --- pastille et titre ---
    C.add_shape(slide, C.MSO_SHAPE.ROUNDED_RECTANGLE, 0.75, 0.58, 1.42, 0.42,
                fill=C.AMBER, radius=0.45)
    C.add_paragraph(C.add_textbox(slide, 0.75, 0.58, 1.42, 0.42,
                                  anchor=C.MSO_ANCHOR.MIDDLE),
                    [("IDÉE %d" % idee["n"], {"size": C.TAILLE_PASTILLE,
                                              "bold": True, "color": C.NAVY})],
                    align=C.PP_ALIGN.CENTER, space_after=0)

    titre = idee["fr_t"]
    t_titre = C.taille_qui_tient(titre, 9.5, 0.80, maxi=C.TAILLE_TITRE, mini=19)
    lg = C.lignes_requises(titre, 9.5, t_titre)
    h_titre = lg * t_titre * 1.1 / 72.0 + 0.10
    C.add_paragraph(C.add_textbox(slide, 2.30, 0.58, 9.9, h_titre),
                    [(titre, {"size": t_titre, "bold": True, "color": C.NAVY})],
                    line_spacing=1.0, space_after=0)

    y = max(h_titre + 0.10, 1.02) + 0.14

    # --- explication, taille ajustee ---
    # Sans schema (cours 02 a 05), la diapo n'a que l'explication et les
    # questions : on peut donc grossir le texte bien au-dela de
    # TAILLE_TEXTE_MAX, sinon la moitie de la diapo reste vide.
    h_schema = 0.0
    if schema:
        h_schema = 1.34 if len(schema) <= 6 else 1.16
    bloc_bas = 2.30 if not schema else h_schema
    budget = 6.68 - y - (bloc_bas + 0.18)
    maxi = C.TAILLE_TEXTE_MAX if schema else 26.0
    t_txt = C.taille_qui_tient(idee["fr_x"], C.CONTENU_D, max(1.0, budget),
                               maxi=maxi, mini=12.0)
    h_txt = max(0.60, C.hauteur_requise(idee["fr_x"], C.CONTENU_D, t_txt))

    if schema:
        C.add_shape(slide, C.MSO_SHAPE.ROUNDED_RECTANGLE, 0.55, y,
                    12.23, h_txt + 0.30, fill=C.GREY_L, line=C.LINE_C,
                    line_w=0.75, radius=0.04)
        C.add_paragraph(C.add_textbox(slide, 0.85, y + 0.15, C.CONTENU_D, h_txt),
                        [(idee["fr_x"], {"size": t_txt, "color": C.DARK})],
                        line_spacing=1.15, space_after=0)
        y += h_txt + 0.30 + 0.18
        y += max(0.0, (6.68 - y - h_schema) / 2)
        C.draw_flow(slide, schema, 0.75, y, 11.83, h_schema)
    else:
        # bloc centre verticalement : explication puis questions
        h_q = 0.44 + sum(C.hauteur_requise(re.sub(r"^Q\d+\.\s*", "", q),
                                          C.CONTENU_D - 0.60, 15.0) + 0.06
                         for q in questions) if questions else 0.0
        haut = h_txt + 0.34 + (h_q + 0.24 if questions else 0.0)
        y += max(0.0, (6.62 - y - haut) / 2)
        C.add_paragraph(C.add_textbox(slide, 0.85, y, C.CONTENU_D, h_txt),
                        [(idee["fr_x"], {"size": t_txt, "color": C.DARK})],
                        line_spacing=1.15, space_after=0)
        y += h_txt + 0.24
        if questions:
            bloc_questions(slide, y, questions)
    pied(slide, page)


def construire(nom, chemin_html):
    idees = L.lire_idees(chemin_html)
    if not idees:
        return None
    os.environ["IA_NUM"] = nom.split("_")[1]

    prs, vide = C.nouveau_conteneur()

    # ---- couverture ----
    s = prs.slides.add_slide(vide)
    n_qr = sum(len(i["qa_fr"]) for i in idees)
    n_sch = sum(len(i["schemas"]) for i in idees)
    C.couverture(
        s, LOGO_UNIV, LOGO_FLE,
        titre=TITRES[nom],
        sous_titre=ACCROCHES[nom],
        badge="Questions & Réponses — Cours %s" % nom.split("_")[1],
        auteur="Dr. Madani BELACEL — MCB",
        mention="2ᵉ année PEP  ·  Année universitaire 2026 – 2027",
        adresse="Cours en ligne : madani-belacel.github.io/site-enseignement-belacel",
        cache=CACHE_LOGOS)
    C.ecrire_notes(s,
                   "Cours %s — %s.\n%d idées, %d questions et réponses.\n"
                   "Les Q/R sont dans les notes : mode Présentateur "
                   "(Diaporama → Mode Présentateur) pour les lire pendant la "
                   "séance." % (nom.split("_")[1], TITRES[nom], len(idees), n_qr))

    # ---- plan : deux colonnes, 5 idées par colonne -------------------------
    # Une seule colonne ne tient pas : 10 x 0,56" débordait sur le pied.
    s = prs.slides.add_slide(vide)
    C.add_paragraph(C.add_textbox(s, 0.75, 0.55, 12.0, 0.7),
                    [("Plan du cours", {"size": C.TAILLE_TITRE, "bold": True,
                                        "color": C.NAVY})], space_after=0)
    for c, lot in enumerate([idees[:5], idees[5:]]):
        x = 0.85 + c * 6.05
        y = 1.50
        for idee in lot:
            h = 0.86
            C.add_shape(s, C.MSO_SHAPE.ROUNDED_RECTANGLE, x, y, 5.75, h,
                        fill=C.GREY_L, line=C.LINE_C, line_w=0.75, radius=0.08)
            b = C.add_shape(s, C.MSO_SHAPE.OVAL, x + 0.14, y + 0.18, 0.46, 0.46,
                            fill=C.BLUE)
            tf = b.text_frame
            tf.vertical_anchor = C.MSO_ANCHOR.MIDDLE
            # marges a zero et pas de retour a la ligne : dans un cercle de
            # 0,46 po il ne restait que 0,26 po utiles, et un nombre a deux
            # chiffres etait considere comme tenant sur deux lignes
            tf.margin_left = tf.margin_right = 0
            tf.margin_top = tf.margin_bottom = 0
            tf.word_wrap = False
            p = tf.paragraphs[0]
            p.text = str(idee["n"])
            p.alignment = C.PP_ALIGN.CENTER
            for run in p.runs:
                run.font.size = C.Pt(13)
                run.font.bold = True
                run.font.color.rgb = C.WHITE
                run.font.name = C.FONT
            t_i = C.taille_qui_tient(idee["fr_t"], 3.95, 0.46, maxi=15, mini=10)
            C.add_paragraph(C.add_textbox(s, x + 0.68, y + 0.12, 4.00, 0.44),
                            [(idee["fr_t"], {"size": t_i, "color": C.DARK})],
                            space_after=0)
            C.add_paragraph(C.add_textbox(s, x + 0.68, y + 0.54, 4.00, 0.26),
                            [("%d questions et réponses" % len(idee["qa_fr"]),
                              {"size": 11, "color": C.GREY})], space_after=0)
            y += 0.98
    C.add_paragraph(C.add_textbox(s, 0.85, 6.44, C.CONTENU_D, 0.48),
                    [("%d idées  ·  %d questions et réponses  ·  %d schémas"
                      % (len(idees), n_qr, n_sch),
                      {"size": 13, "bold": True, "color": C.NAVY})], space_after=0)
    pied(s, 2)

    # ---- une diapositive par idee ----
    for k, idee in enumerate(idees, 3):
        s = prs.slides.add_slide(vide)
        schemas = idee["schemas"]
        # le premier schema de l'idee va sur la diapo ; les suivants aussi
        # s'il y en a un seul, sinon on garde le plus parlant (3 boites ou plus)
        schema = None
        if schemas:
            schema = max(schemas, key=lambda e: sum(1 for x in e if x[0] == "box"))
            if sum(1 for x in schema if x[0] == "box") < 3:
                schema = None
        diapo_idee(s, idee, k, schema, [q for q, _ in idee["qa_fr"]], k)

        notes = ["IDÉE %d — %s" % (idee["n"], idee["fr_t"]), "",
                 "── QUESTIONS & RÉPONSES ──"]
        for q, r in idee["qa_fr"]:
            notes += [q, r, ""]
        C.ecrire_notes(s, "\n".join(notes).strip())

    os.makedirs(SORTIE, exist_ok=True)
    chemin = os.path.join(SORTIE, nom + ".pptx")
    prs.save(chemin)
    return {"idees": len(idees), "qr": n_qr, "schemas": n_sch,
            "diapos": len(prs.slides._sldIdLst),
            "ko": os.path.getsize(chemin) / 1024.0, "chemin": chemin}


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--tous" in sys.argv:
        cibles = list(COURS)
    elif argv:
        cibles = argv
    else:
        cibles = [c for c in COURS if c != "QR_IA_01_Introduction_IA"]

    for nom in cibles:
        html = os.path.join(DOSSIER, nom + ".html")
        if not os.path.exists(html):
            print("ABSENT :", nom)
            continue
        r = construire(nom, html)
        if not r:
            print("aucune idee lue :", nom)
            continue
        print("%-32s %2d diapos · %2d idées · %2d Q/R · %2d schémas · %.0f Ko"
              % (nom, r["diapos"], r["idees"], r["qr"], r["schemas"], r["ko"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
