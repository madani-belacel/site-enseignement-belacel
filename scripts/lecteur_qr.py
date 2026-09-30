#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lecteur des cours « Questions / Réponses » du module Intelligence Artificielle.

Ces cours ont tous la meme structure :

    <article class="qr-idea">
      <h3><span class="qr-tag">Idée N</span>
          <span class="lang-en">…</span><span class="lang-fr">…</span></h3>
      <p class="qr-expl lang-en">…</p>
      <p class="qr-expl lang-fr">…</p>
      <div class="qr-item">
        <p class="qr-q lang-en">…</p><p class="qr-r lang-en">…</p>
        <p class="qr-q lang-fr">…</p><p class="qr-r lang-fr">…</p>
      </div>
      <div class="diagram">
        <div class="dbox"><span class="lang-fr">…</span></div>
        <span class="arrow">→</span>
        <div class="dbox alt">…</div>
      </div>
    </article>

Les generateurs de presentation s'en servent pour ne jamais recopier le
contenu : si le cours change, la presentation suit.
"""
import re
from html import unescape
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}


def texte(fragment):
    """Balisage HTML -> texte brut, balise par balise."""
    t = re.sub(r"<br\s*/?>", " ", fragment)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", unescape(t)).strip()


# ---------------------------------------------------------------------------
# 1. Idées
# ---------------------------------------------------------------------------
def lire_idees(chemin):
    """Renvoie la liste des idées : titres, explications, Q/R, schémas."""
    s = open(chemin, encoding="utf-8").read()
    idees = []
    for art in re.findall(r'<article class="qr-idea">.*?</article>', s, re.S):

        def un(regex, defaut=""):
            m = re.search(regex, art, re.S)
            return texte(m.group(1)) if m else defaut

        idee = {
            "n": int(un(r'<span class="qr-tag">Idée\s*(\d+)', "0") or 0),
            "fr_t": un(r'<span class="lang-fr">(.*?)</span>\s*</h3>'),
            "en_t": un(r'<h3>.*?<span class="lang-en">(.*?)</span>'),
            "fr_x": un(r'<p class="qr-expl lang-fr">(.*?)</p>'),
            "en_x": un(r'<p class="qr-expl lang-en">(.*?)</p>'),
            "qa_fr": [],
            "qa_en": [],
            "schemas": lire_schemas(art),
        }

        # une <div class="qr-item"> peut contenir plusieurs paires
        for item in re.findall(r'<div class="qr-item">(.*?)</div>', art, re.S):
            for langue, cle in (("fr", "qa_fr"), ("en", "qa_en")):
                qs = [texte(x) for x in
                      re.findall(r'<p class="qr-q lang-%s">(.*?)</p>' % langue,
                                 item, re.S)]
                rs = [texte(x) for x in
                      re.findall(r'<p class="qr-r lang-%s">(.*?)</p>' % langue,
                                 item, re.S)]
                for q, r in zip(qs, rs):
                    idee[cle].append((q, r))
        idees.append(idee)
    return idees


# ---------------------------------------------------------------------------
# 2. Schémas
# ---------------------------------------------------------------------------
class _LignesFR(HTMLParser):
    """Ne garde que le texte « lang-fr » d'un fragment, ligne par ligne.

    Le cours ecrit les deux langues dans la meme balise : une
    <span class="lang-en"> puis une <span class="lang-fr">. Un simple
    « supprimer les balises » melangerait les deux ; il faut donc suivre
    l'imbrication des <span class="lang-*">.
    """

    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.lignes = []
        self.cur = []
        self.actif = False      # dans la bonne langue ?
        self.saut = 0           # profondeur du <span> ecarte

    def handle_starttag(self, tag, attrs):
        classes = (dict(attrs).get("class") or "").split()
        if tag == "br":
            self._nl()
            return
        if self.saut:
            self.saut += 1
            return
        if "lang-fr" in classes:
            self._nl()
            self.actif = True
            return
        if "lang-en" in classes:
            self._nl()
            self.actif = False
            self.saut = 1
            return
        if tag in ("div", "p", "li", "span"):
            self._nl()

    def handle_endtag(self, tag):
        if self.saut:
            self.saut -= 1
            if not self.saut:
                self.actif = True
            return
        if tag in ("div", "p", "li", "span"):
            self._nl()

    def handle_data(self, d):
        if self.actif and not self.saut:
            self.cur.append(d)

    def _nl(self):
        l = " ".join("".join(self.cur).split())
        if l:
            self.lignes.append(l)
        self.cur = []

    def resultat(self):
        self._nl()
        return self.lignes


def lignes_fr(fragment):
    p = _LignesFR()
    p.feed(fragment)
    return p.resultat()


def lire_schemas(art):
    """Schémas d'un article, dans l'ordre du document.

    Chaque schéma est une suite :
        [('box', 'Exemples', 'Données', 'primary'), ('arrow', '→'), …]
    """
    schemas = []
    for m in re.finditer(r'<div class="diagram"[^>]*>', art):
        i = m.end()
        prof, j = 1, i
        while prof > 0 and j < len(art):
            n = re.compile(r"<div\b|</div\s*>").search(art, j)
            if not n:
                break
            prof += -1 if n.group(0).startswith("</") else 1
            j = n.end()
        elements = []
        for mm in re.finditer(
                r'<div class="(dbox[^"]*)"[^>]*>(.*?)</div>'
                r'|<span class="arrow"[^>]*>(.*?)</span>', art[i:j], re.S):
            if mm.group(2) is not None:
                classes = (mm.group(1) or "").split()
                style = ("alt" if "alt" in classes else
                         "warnb" if "warnb" in classes else
                         "ghost" if "ghost" in classes else "primary")
                lignes = lignes_fr(mm.group(2))
                if not lignes:
                    continue
                elements.append(("box", lignes[0],
                                 lignes[1] if len(lignes) > 1 else "", style))
            elif mm.group(3) is not None:
                elements.append(("arrow", texte(mm.group(3)) or "→"))
        if elements:
            schemas.append(elements)
    return schemas


# ---------------------------------------------------------------------------
# 3. Équilibre des balises d'une page
# ---------------------------------------------------------------------------
class _Equilibre(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self, convert_charrefs=True)
        self.pile = []
        self.erreurs = []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.pile.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.pile and self.pile[-1][0] == tag:
            self.pile.pop()
        elif any(t == tag for t, _ in self.pile):
            while self.pile and self.pile[-1][0] != tag:
                t, l = self.pile.pop()
                self.erreurs.append("<%s> ouvert ligne %d" % (t, l))
            if self.pile:
                self.pile.pop()
        else:
            self.erreurs.append("</%s> orpheline ligne %d"
                                % (tag, self.getpos()[0]))


def equilibre(chemin):
    """Renvoie (balises non fermees, erreurs) pour une page HTML."""
    b = _Equilibre()
    b.feed(open(chemin, encoding="utf-8", errors="ignore").read())
    return [t for t, _ in b.pile], b.erreurs
