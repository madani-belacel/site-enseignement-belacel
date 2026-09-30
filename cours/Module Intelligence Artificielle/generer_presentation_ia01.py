#!/usr/bin/env python3
"""Genere la presentation PowerPoint du cours « Introduction a l'IA » (cours 01).

Le contenu est repris de QR_IA_01_Introduction_IA.html : 10 idees, chacune
avec son explication et ses 3 questions/reponses, plus un schema vectoriel
dessine avec des formes PowerPoint (donc editable, pas une image).

Sortie : cours/Module Intelligence Artificielle/Presentations_PPTX/
         QR_IA_01_Introduction_IA.pptx
"""
import os
import re
from html import unescape

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Inches, Pt

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
COURS = os.path.join(ROOT, "cours", "Module Intelligence Artificielle",
                     "QR_IA_01_Introduction_IA.html")
SORTIE = os.path.join(ROOT, "cours", "Module Intelligence Artificielle",
                      "Presentations_PPTX")
SORTIE_FICHIER = os.path.join(SORTIE, "QR_IA_01_Introduction_IA.pptx")

# --- charte graphique (couleurs du site) ------------------------------------
PRIMARY = RGBColor(0x14, 0x6F, 0xA9)
NAVY = RGBColor(0x16, 0x2B, 0x40)
GREEN = RGBColor(0x00, 0x87, 0x5B)
GOLD = RGBColor(0xF0, 0xB4, 0x29)
RED = RGBColor(0xD2, 0x10, 0x34)
BLANC = RGBColor(0xFF, 0xFF, 0xFF)
GRIS_CLAIR = RGBColor(0xF4, 0xF6, 0xF8)
GRIS = RGBColor(0x5F, 0x6E, 0x80)
GRIS_BORD = RGBColor(0xDF, 0xE5, 0xEA)
TEXTE = RGBColor(0x22, 0x34, 0x4A)

POLICE = "Poppins"
POLICE_SOUS = "Calibri"

LARGEUR, HAUTEUR = Inches(13.333), Inches(7.5)


def texte(s):
    """Nettoie le HTML d'une page et renvoie du texte brut."""
    s = re.sub(r"<br\s*/?>", " ", s)
    s = re.sub(r"<[^>]+>", "", s)
    return re.sub(r"\s+", " ", unescape(s)).strip()


# ===========================================================================
# 1. Extraction du contenu depuis la page HTML
# ===========================================================================
ART = re.compile(r'<article class="qr-idea"><h3><span class="qr-tag">Idée (\d+)</span>'
                 r'\s*<span class="lang-en">(.*?)</span>'
                 r'<span class="lang-fr">(.*?)</span></h3>(.*?)</article>', re.S)
QA = re.compile(r'<div class="qr-item">(.*?)</div>', re.S)
FR = re.compile(r'<p class="qr-(?:expl|q|r) lang-fr">(.*?)</p>', re.S)


def lire_cours():
    s = open(COURS, encoding="utf-8").read()
    idees = []
    for m in ART.finditer(s):
        numero, en, fr, corps = m.group(1), m.group(2), m.group(3), m.group(4)
        expl = ""
        me = re.search(r'<p class="qr-expl lang-fr">(.*?)</p>', corps, re.S)
        if me:
            expl = texte(me.group(1))
        paires = []
        qs = re.findall(r'<p class="qr-q lang-fr">(.*?)</p>', corps, re.S)
        rs = re.findall(r'<p class="qr-r lang-fr">(.*?)</p>', corps, re.S)
        for q, r in zip(qs, rs):
            paires.append((texte(q), texte(r)))
        qa = [paires]
        idees.append({
            "n": int(numero),
            "titre": texte(fr),
            "titre_en": texte(en),
            "expl": expl,
            "qa": qa[0] if qa else [],
        })
    return idees


# ===========================================================================
# 2. Primitives de mise en page
# ===========================================================================
prs = Presentation()
prs.slide_width, prs.slide_height = LARGEUR, HAUTEUR
VIDE = prs.slide_layouts[6]


def rect(slide, x, y, w, h, couleur, forme=MSO_SHAPE.ROUNDED_RECTANGLE,
         ligne=None, epaisseur=1.25):
    f = slide.shapes.add_shape(forme, x, y, w, h)
    f.fill.solid()
    f.fill.fore_color.rgb = couleur
    if ligne is None:
        f.line.fill.background()
    else:
        f.line.color.rgb = ligne
        f.line.width = Pt(epaisseur)
    f.shadow.inherit = False
    if forme == MSO_SHAPE.ROUNDED_RECTANGLE:
        try:
            f.adjustments[0] = 0.12
        except Exception:
            pass
    return f


def ecrire(slide, x, y, w, h, contenu, taille=18, gras=False, couleur=TEXTE,
           align=PP_ALIGN.LEFT, police=POLICE, interligne=1.0, ancrage=MSO_ANCHOR.TOP):
    z = slide.shapes.add_textbox(x, y, w, h)
    tf = z.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = ancrage
    lignes = contenu.split("\n") if isinstance(contenu, str) else list(contenu)
    for i, ligne in enumerate(lignes):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = ligne
        p.alignment = align
        p.line_spacing = interligne
        for r in p.runs:
            r.font.size = Pt(taille)
            r.font.bold = gras
            r.font.color.rgb = couleur
            r.font.name = police
    return z


def bandeau(slide, titre, sous_titre=""):
    """Bandeau de titre commun a toutes les diapositives de contenu."""
    rect(slide, 0, 0, LARGEUR, Inches(1.02), NAVY, MSO_SHAPE.RECTANGLE)
    rect(slide, 0, Inches(1.02), LARGEUR, Inches(0.055), GREEN, MSO_SHAPE.RECTANGLE)
    # le titre s'auto-reduit : il doit tenir sur une seule ligne
    n = len(titre)
    taille = 25 if n <= 46 else (22 if n <= 54 else (19 if n <= 62 else 17))
    ecrire(slide, Inches(0.5), Inches(0.18), Inches(11.5), Inches(0.46), titre,
           taille=taille, gras=True, couleur=BLANC)
    if sous_titre:
        ecrire(slide, Inches(0.52), Inches(0.63), Inches(10.6), Inches(0.34),
               sous_titre, taille=12.5, couleur=RGBColor(0xC3, 0xCB, 0xD4))
    return Inches(1.25)


def pied(slide, num):
    ecrire(slide, Inches(0.5), Inches(6.95), Inches(9.5), Inches(0.3),
           "Dr. Madani BELACEL — Université de Mostaganem — Module Intelligence Artificielle",
           taille=9, couleur=GRIS, police=POLICE_SOUS)
    ecrire(slide, Inches(12.2), Inches(6.95), Inches(0.7), Inches(0.3),
           str(num), taille=9, couleur=GRIS, align=PP_ALIGN.RIGHT, police=POLICE_SOUS)


def dbox(slide, x, y, w, h, titre, legende="", couleur=PRIMARY, fond=None):
    """Boite de schema : titre + legende, tontee lisible."""
    c = fond or GRIS_CLAIR
    f = rect(slide, x, y, w, h, c, ligne=couleur, epaisseur=1.75)
    tf = f.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    tf.margin_left = tf.margin_right = Inches(0.06)
    tf.margin_top = tf.margin_bottom = Inches(0.03)
    p = tf.paragraphs[0]
    p.text = titre
    p.alignment = PP_ALIGN.CENTER
    for r in p.runs:
        r.font.size = Pt(13)
        r.font.bold = True
        r.font.color.rgb = couleur
        r.font.name = POLICE
    if legende:
        p2 = tf.add_paragraph()
        p2.text = legende
        p2.alignment = PP_ALIGN.CENTER
        for r in p2.runs:
            r.font.size = Pt(9.5)
            r.font.color.rgb = GRIS
            r.font.name = POLICE_SOUS
    return f


def fleche(slide, x, y, w=Inches(0.36), glyphe="→", taille=20, couleur=GRIS):
    ecrire(slide, x, y, w, Inches(0.4), glyphe, taille=taille, gras=True,
           couleur=couleur, align=PP_ALIGN.CENTER, police=POLICE_SOUS)


def schema(slide, y, etapes, couleur=PRIMARY, couleur_alt=GREEN,
           couleur_fin=GOLD, separateur="→", legende=None):
    """Dessine une chaine de boites centree, avec des fleches entre elles.

    etapes : liste de (titre, legende, role) ou role dans {'normal','alt','fin'}
    """
    n = len(etapes)
    if n == 0:
        return
    larg = Inches(2.15)
    gap = Inches(0.42)
    total = n * larg + (n - 1) * gap
    x0 = int((LARGEUR - total) / 2)
    for i, etape in enumerate(etapes):
        titre, leg = etape[0], etape[1]
        role = etape[2] if len(etape) > 2 else "normal"
        c, fond = (couleur, None)
        if role == "alt":
            c = couleur_alt
        elif role == "fin":
            c = couleur_fin
        dbox(slide, x0 + i * (larg + gap), y, larg, Inches(0.92), titre, leg, c, fond)
        if i < n - 1:
            fleche(slide, x0 + i * (larg + gap) + larg, y + Inches(0.24), gap,
                   separateur)
    if legende:
        ecrire(slide, Inches(1), y + Inches(1.0), LARGEUR - Inches(2), Inches(0.3),
               legende, taille=10, couleur=GRIS, align=PP_ALIGN.CENTER,
               police=POLICE_SOUS)


# ===========================================================================
# 3. Les diapositives
# ===========================================================================
idees = lire_cours()
print("idees extraites :", len(idees))

# ---- 1. Couverture --------------------------------------------------------
s = prs.slides.add_slide(VIDE)
rect(s, 0, 0, LARGEUR, HAUTEUR, NAVY, MSO_SHAPE.RECTANGLE)
rect(s, 0, Inches(4.62), LARGEUR, Inches(0.06), GREEN, MSO_SHAPE.RECTANGLE)
ecrire(s, Inches(0.9), Inches(1.55), Inches(11.5), Inches(0.5),
       "MODULE INTELLIGENCE ARTIFICIELLE", taille=15, gras=True,
       couleur=RGBColor(0x7E, 0xC4, 0xF0))
ecrire(s, Inches(0.9), Inches(2.15), Inches(11.5), Inches(1.4),
       "Introduction à l'Intelligence Artificielle", taille=44, gras=True,
       couleur=BLANC)
ecrire(s, Inches(0.9), Inches(3.55), Inches(11.5), Inches(0.6),
       "10 idées · 30 questions et réponses · français / anglais", taille=19,
       couleur=RGBColor(0xC3, 0xCB, 0xD4))
ecrire(s, Inches(0.9), Inches(5.0), Inches(11.5), Inches(0.4),
       "Dr. Madani BELACEL", taille=21, gras=True, couleur=BLANC)
ecrire(s, Inches(0.9), Inches(5.45), Inches(11.5), Inches(0.9),
       "Maître de Conférences B — Université de Mostaganem\nFaculté des langues étrangères",
       taille=13.5, couleur=RGBColor(0xA9, 0xB6, 0xC6), interligne=1.25)
ecrire(s, Inches(0.9), Inches(6.55), Inches(11.5), Inches(0.35),
       "Année universitaire 2026-2027", taille=11.5,
       couleur=RGBColor(0x8A, 0x99, 0xAE), police=POLICE_SOUS)

# ---- 2. Plan du cours ------------------------------------------------------
s = prs.slides.add_slide(VIDE)
y = bandeau(s, "Plan du cours", "Les 10 idées, dans l'ordre")
colonnes = [idees[:5], idees[5:]]
for c, lot in enumerate(colonnes):
    x = Inches(0.6) + c * Inches(6.3)
    y0 = y
    for idee in lot:
        rect(s, x, y0, Inches(5.95), Inches(0.86), GRIS_CLAIR,
             ligne=GRIS_BORD, epaisseur=0.75)
        badge = rect(s, x + Inches(0.12), y0 + Inches(0.19), Inches(0.48),
                     Inches(0.48), PRIMARY, MSO_SHAPE.OVAL)
        tf = badge.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.paragraphs[0]
        p.text = str(idee["n"])
        p.alignment = PP_ALIGN.CENTER
        for r in p.runs:
            r.font.size = Pt(14)
            r.font.bold = True
            r.font.color.rgb = BLANC
            r.font.name = POLICE
        ecrire(s, x + Inches(0.72), y0 + Inches(0.12), Inches(5.1), Inches(0.62),
               idee["titre"], taille=12.5,gras=False, couleur=TEXTE,
               ancrage=MSO_ANCHOR.MIDDLE, interligne=0.95)
        y0 += Inches(0.98)
pied(s, 2)

# ---- 3. Une diapositive par idee -----------------------------------------
SCHEMAS = {
    1: [("Exemples", "Données étiquetées", "normal"),
        ("Régularités", "Les règles trouvées", "alt"),
        ("Une réponse", "Sur un cas nouveau", "fin")],
    2: [("1 000 photos de chats", "étiquetées « chat »", "normal"),
        ("1 000 photos de chiens", "étiquetées « chien »", "normal"),
        ("Une photo nouvelle", "Jamais vue", "alt"),
        ("chat ou chien", "La réponse", "fin")],
    3: [("📦 La même règle", "des exemples → une règle", "normal"),
        ("📦 Le même principe", "puis une application sur un cas nouveau", "alt"),
        ("🖥️ ChatGPT", "ne lit rien chez vous", "normal"),
        ("💻 Cursor", "lit vos fichiers, puis applique la même règle", "fin")],
    4: [("Téléphone", "photo, voix, clavier", "normal"),
        ("Courriel", "filtre anti-spam", "normal"),
        ("Cartes", "itinéraires", "normal"),
        ("Météo", "prévisions", "normal"),
        ("Médecine", "diagnostic", "normal")],
    5: [("Plus de données", "sur Internet", "normal"),
        ("Plus de puissance", "GPU, serveurs", "normal"),
        ("Outils gratuits", "dans le navigateur", "normal"),
        ("L'IA pour tous", "dès aujourd'hui", "fin")],
    6: [("500 exemples propres", "qualité", "alt"),
        ("Réponse fiable", "✓", "fin")],
    7: [("Préparer", "résumé, plan", "normal"),
        ("S'entraîner", "QCM, fiches", "normal"),
        ("Rédiger", "corriger, traduire", "normal"),
        ("Toujours vérifier", "✓", "fin")],
    8: [("Texte", "ce qu'il lit", "normal"),
        ("Formes & statistiques", "ce qu'il calcule", "alt"),
        ("Du sens", "ce qu'il n'a pas", "fin")],
    9: [("Est-ce vrai ?", "vérifier la source", "normal"),
        ("Ai-je cité ?", "plagiat", "normal"),
        ("Est-ce le mien ?", "travail personnel", "normal")],
    10: [("1950", "Test de Turing", "normal"),
         ("1997", "Deep Blue", "normal"),
         ("2011", "Siri", "normal"),
         ("2022…", "ChatGPT, Copilot", "fin")],
}

# les idees les plus denses sont reparties sur deux diapositives
DENSES = {3: 3}          # idee -> nb de Q/R sur la 1re diapositive

num_diapo = 2
for idee in idees:
    tranche = DENSES.get(idee["n"])
    if tranche and len(idee["qa"]) > tranche:
        lots = [idee["qa"][:tranche], idee["qa"][tranche:]]
    else:
        lots = [idee["qa"]]

    for n_lot, qa_lot in enumerate(lots):
        num_diapo += 1
        s = prs.slides.add_slide(VIDE)
        suffixe = "" if n_lot == 0 else " (suite)"
        y = bandeau(s, "Idée %d — %s%s" % (idee["n"], idee["titre"], suffixe),
                    idee["titre_en"])
        # pastille d'idee
        rect(s, Inches(12.35), Inches(0.2), Inches(0.72), Inches(0.72), PRIMARY,
             MSO_SHAPE.OVAL)
        ecrire(s, Inches(12.35), Inches(0.31), Inches(0.72), Inches(0.5),
               str(idee["n"]), taille=22, gras=True, couleur=BLANC,
               align=PP_ALIGN.CENTER)

        # explication
        hauteur_expl = Inches(1.16) if len(idee["expl"]) > 240 else Inches(0.88)
        rect(s, Inches(0.5), y, Inches(12.33), hauteur_expl, GRIS_CLAIR,
             ligne=GRIS_BORD, epaisseur=0.75)
        ecrire(s, Inches(0.72), y + Inches(0.08), Inches(11.9),
               hauteur_expl - Inches(0.16), idee["expl"],
               taille=11.5 if len(idee["expl"]) > 240 else 12.5, couleur=TEXTE,
               ancrage=MSO_ANCHOR.MIDDLE, police=POLICE_SOUS, interligne=1.06)

        # schema (seulement sur la premiere diapositive de l'idee)
        ysch = y + hauteur_expl + Inches(0.16)
        if n_lot == 0 and idee["n"] in SCHEMAS:
            etapes = SCHEMAS[idee["n"]]
            separateur = "❚" if len(etapes) == 2 else "→"
            schema(s, ysch, etapes, separateur=separateur)
            ysch += Inches(1.12)

        # questions / reponses : la hauteur s'adapte au nombre de paires
        yq = ysch + Inches(0.06)
        n = max(1, len(qa_lot))
        place = Inches(6.62) - yq
        h_boite = max(Inches(0.52), (place - Inches(0.10) * (n - 1)) / n)
        h_q = Inches(0.24) if n <= 3 else Inches(0.21)
        t_q = 12 if n <= 3 else 10.5
        t_r = 11 if n <= 3 else 9.5
        for q, r in qa_lot:
            rect(s, Inches(0.5), yq, Inches(12.33), h_boite, BLANC,
                 ligne=GRIS_BORD, epaisseur=0.75)
            rect(s, Inches(0.5), yq, Inches(0.055), h_boite, PRIMARY,
                 MSO_SHAPE.RECTANGLE)
            ecrire(s, Inches(0.72), yq + Inches(0.05), Inches(11.9), h_q,
                   q, taille=t_q, gras=True, couleur=NAVY)
            ecrire(s, Inches(0.72), yq + h_q + Inches(0.05), Inches(11.9),
                   h_boite - h_q - Inches(0.10), r, taille=t_r, couleur=TEXTE,
                   police=POLICE_SOUS, interligne=1.02)
            yq += h_boite + Inches(0.10)
        pied(s, num_diapo)

# ---- derniere : points cles ----------------------------------------------
s = prs.slides.add_slide(VIDE)
y = bandeau(s, "Les 6 points à retenir", "Résumé du cours 01")
pts = [
    ("1", "L'IA est un programme", "Elle ne comprend pas : elle calcule des formes et des statistiques."),
    ("2", "Elle trouve ses règles seule", "Comme Excel qui calcule 12 quand vous tirez la poignée."),
    ("3", "Deux familles", "Conversation (ChatGPT, Grok, DeepSeek) et Code (OpenCode, Cursor, Copilot)."),
    ("4", "Les exemples sont tout", "1 000 chats étiquetés suffisent pour classer une photo nouvelle."),
    ("5", "La qualité avant la quantité", "Des exemples propres valent mieux que beaucoup d'exemples sales."),
    ("6", "Toujours vérifier", "Vrai ? Cité ? Votre ? Trois questions avant de croire une réponse."),
]
for i, (num, titre, detail) in enumerate(pts):
    yy = y + Inches(0.12) + Inches(0.87) * (i % 3)
    xx = Inches(0.5) if i < 3 else Inches(6.85)
    rect(s, xx, yy, Inches(5.95), Inches(0.76), GRIS_CLAIR, ligne=GRIS_BORD,
         epaisseur=0.75)
    b = rect(s, xx + Inches(0.1), yy + Inches(0.15), Inches(0.46), Inches(0.46),
             GREEN, MSO_SHAPE.OVAL)
    tf = b.text_frame
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = num
    p.alignment = PP_ALIGN.CENTER
    for r in p.runs:
        r.font.size = Pt(14)
        r.font.bold = True
        r.font.color.rgb = BLANC
        r.font.name = POLICE
    ecrire(s, xx + Inches(0.66), yy + Inches(0.07), Inches(5.2), Inches(0.28),
           titre, taille=13, gras=True, couleur=NAVY)
    ecrire(s, xx + Inches(0.66), yy + Inches(0.36), Inches(5.2), Inches(0.34),
           detail, taille=10.5, couleur=GRIS, police=POLICE_SOUS, interligne=1.0)
pied(s, num_diapo + 1)

# ===========================================================================
os.makedirs(SORTIE, exist_ok=True)
prs.save(SORTIE_FICHIER)
print("presentation ecrite :", SORTIE_FICHIER)
print("  diapositives :", len(prs.slides.__iter__.__self__._sldIdLst))
print("  taille : %.1f Ko" % (os.path.getsize(SORTIE_FICHIER) / 1024))
