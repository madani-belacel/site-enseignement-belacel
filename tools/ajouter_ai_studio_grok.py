# -*- coding: utf-8 -*-
"""
ajouter_ai_studio_grok.py — même ajout, mais dans la variante « Grok »
qui a une structure différente (titre déjà «… · Grok », pas de
<div class="astuce-bloc">, étapes numérotées).

Ancre par contenu exact. Idempotent.
"""
import io
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIBLE = "cours/IA/COURS IA Grok/Module_IA_Ameliore/seances/astuces-ia.html"

OLD_TITRE = u"Alterner ChatGPT · Gemini · Claude · DeepSeek · Grok</h3>"
NEW_TITRE = u"Alterner ChatGPT · Gemini · Claude · DeepSeek · Grok · AI Studio</h3>"

OLD_P = (u"<p>Leurs quotas sont indépendants. Ouvre les 4–5 en onglets "
         u"permanents. Même question → 4 réponses en 30 secondes → tu vois "
         u"immédiatement qui est le plus précis aujourd’hui.</p>")

OUTILS = [
    ("ChatGPT", "https://chatgpt.com/", u"assistant généraliste d'OpenAI"),
    ("Gemini", "https://gemini.google.com/", u"assistant généraliste de Google"),
    ("Claude", "https://claude.ai/", u"assistant généraliste d'Anthropic"),
    ("DeepSeek", "https://chat.deepseek.com/",
     u"modèle ouvert, utile pour comparer"),
    ("Grok", "https://grok.com/", u"assistant de xAI"),
    ("AI Studio", "https://aistudio.google.com/",
     u"atelier de Google pour tester des prompts et les modèles Gemini"),
]

CSS_ANCRES = (u".avertissement-corps h3 {", u".astuce-detail-corps {",
              u".tip-num {")
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


def bloc():
    items = [
        u'<li><a class="tool-link" href="%s" target="_blank" '
        u'rel="noopener noreferrer"><strong>%s</strong> '
        u'<span class="tool-url">%s</span></a> — %s</li>' % (u, n, u, d)
        for n, u, d in OUTILS]
    return (u"<h4>Accès direct</h4>\n"
            u'<ul class="tool-links">\n' + u"\n".join(items) + u"\n</ul>\n")


def main():
    full = os.path.join(BASE, CIBLE)
    s = io.open(full, encoding="utf-8").read()
    if "aistudio.google.com" in s:
        print(u"   déjà fait")
        return 0

    etapes = []
    for nom, old, new in (
            (u"titre", OLD_TITRE, NEW_TITRE),
            (u"liste", OLD_P, OLD_P + u"\n" + bloc())):
        n = s.count(old)
        assert n == 1, u"ancre %s : %d occurrence(s)" % (nom, n)
        s = s.replace(old, new, 1)
        etapes.append(nom)

    for a in CSS_ANCRES:
        if s.count(a) == 1 and "a.tool-link" not in s.split(a)[0][-400:]:
            s = s.replace(a, CSS + a, 1)
            etapes.append(u"style")
            break
    else:
        assert "a.tool-link" in s, u"aucun point d'insertion pour le style"

    io.open(full, "w", encoding="utf-8").write(s)
    print(u"   ✔ %s  (%s)" % (CIBLE, u", ".join(etapes)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
