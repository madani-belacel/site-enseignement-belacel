# -*- coding: utf-8 -*-
"""
ajouter_ai_studio.py — ajoute Google AI Studio à l'astuce n° 2
« Alterner ChatGPT · Gemini · Claude · DeepSeek ».

Demande : ajouter l'outil et le lien https://aistudio.google.com/.

Ce que fait le correctif, dans chaque page de l'astuce 2 :
  1. le titre liste désormais AI Studio ;
  2. l'étape 1 cite AI Studio ;
  3. une section « Accès direct » donne les liens cliquables ;
  4. un style `.tool-link` est ajouté au <style> inline de la page,
     car `a { color: inherit }` rendrait les liens invisibles.

Pourquoi le style est mis dans la page et non dans css/style.css ?
    Deux des trois copies pointent vers un chemin CSS cassé
    (cours/css/style.css n'existe pas) : elles s'affichent donc sans
    feuille de style. Un style inline fonctionne dans tous les cas, et
    ne touche pas aux 2 764 références valides du site.

Ancre par contenu exact, jamais par numéro de ligne.
"""
import io
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CIBLE = "cours/Module Intelligence Artificielle/seances/astuces-ia.html"
COPIE = "cours/IA/Grok-Module_Intelligence_Artificielle_Final/seances/astuces-ia.html"

# ── 1) le titre ────────────────────────────────────────────────────────
OLD_TITRE = u"Alterner ChatGPT · Gemini · Claude · DeepSeek</h3>"
NEW_TITRE = u"Alterner ChatGPT · Gemini · Claude · DeepSeek · AI Studio</h3>"

# ── 2) l'étape 1 ───────────────────────────────────────────────────────
OLD_ETAPE = u"<li>Ouvre 3 outils dans des onglets épinglés (par exemple ChatGPT, Gemini, Claude).</li>"
NEW_ETAPE = (u"<li>Ouvre 3 outils dans des onglets épinglés (par exemple ChatGPT, "
             u"Gemini, Claude).</li>")

# ── 3) la section « Accès direct » ─────────────────────────────────────
OLD_OL = (
    u"<ol>\n"
    u"<li>Ouvre 3 outils dans des onglets épinglés (par exemple ChatGPT, Gemini, Claude).</li>\n"
    u"<li>Prépare une seule question, identique mot pour mot.</li>\n"
    u"<li>Colle-la dans chaque onglet, compare, garde la réponse la plus claire, "
    u"vérifie les faits importants.</li>\n"
    u"</ol>"
)

OUTILS = [
    ("ChatGPT", "https://chatgpt.com/",
     u"assistant généraliste d'OpenAI"),
    ("Gemini", "https://gemini.google.com/",
     u"assistant généraliste de Google"),
    ("Claude", "https://claude.ai/",
     u"assistant généraliste d'Anthropic"),
    ("DeepSeek", "https://chat.deepseek.com/",
     u"modèle ouvert, utile pour comparer"),
    ("AI Studio", "https://aistudio.google.com/",
     u"atelier de Google pour tester des prompts et les modèles Gemini"),
]


def bloc_liens():
    items = []
    for nom, url, desc in OUTILS:
        items.append(
            u'<li><a class="tool-link" href="%s" target="_blank" '
            u'rel="noopener noreferrer"><strong>%s</strong> '
            u'<span class="tool-url">%s</span></a> — %s</li>'
            % (url, nom, url, desc))
    return (u"<h4>Accès direct</h4>\n"
            u'<ul class="tool-links">\n'
            + u"\n".join(items) + u"\n</ul>\n")

NEW_OL = OLD_OL + u"\n" + bloc_liens()

# ── 4) le style inline ─────────────────────────────────────────────────
ANCRE_STYLE = u".avertissement-corps h3 {"
CSS = u"""/* Liens vers les outils IA (astuce « Alterner… »).
   Necessaires car « a { color: inherit } » : sans cela un lien
   serait invisible — meme couleur que le texte, aucun soulignement. */
.tool-links { list-style: none; margin: .6rem 0 0; padding: 0; }
.tool-links li { margin: .38rem 0; line-height: 1.5; }
a.tool-link {
  display: inline-block;
  color: var(--primary);
  font-weight: 600;
  text-decoration: underline;
  text-underline-offset: 2px;
  word-break: break-word;
}
a.tool-link:hover { color: var(--primary-hover); }
a.tool-link:focus-visible { outline: 2px solid var(--primary); outline-offset: 2px; }
a.tool-link .tool-url {
  display: block;
  font-family: 'JetBrains Mono', ui-monospace, monospace;
  font-size: .82em;
  font-weight: 400;
  opacity: .78;
}
@media (prefers-color-scheme: dark) {
  a.tool-link { color: var(--primary-hover); }
}
"""


def patch(path):
    full = os.path.join(BASE, path)
    s = io.open(full, encoding="utf-8").read()
    if "aistudio.google.com" in s:
        print(u"   déjà fait : %s" % path)
        return 0

    etapes = []
    for nom, old, new in ((u"titre", OLD_TITRE, NEW_TITRE),
                          (u"étape", OLD_ETAPE, NEW_ETAPE),
                          (u"liste", OLD_OL, NEW_OL)):
        n = s.count(old)
        assert n == 1, u"ancre %s : %d occurrence(s) dans %s" % (nom, n, path)
        s = s.replace(old, new, 1)
        etapes.append(nom)

    assert s.count(ANCRE_STYLE) == 1, u"ancre style introuvable dans %s" % path
    s = s.replace(ANCRE_STYLE, CSS + ANCRE_STYLE, 1)
    etapes.append(u"style")

    io.open(full, "w", encoding="utf-8").write(s)
    print(u"   ✔ %s  (%s)" % (path, u", ".join(etapes)))
    return 1


def main():
    n = 0
    for p in (CIBLE, COPIE):
        n += patch(p)
    print(u"  fichiers modifiés : %d / 2" % n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
