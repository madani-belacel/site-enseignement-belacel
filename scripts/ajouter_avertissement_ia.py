#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insère l'avertissement « l'IA et l'article scientifique » en tête de page.

Ce texte n'appartient à aucune astuce numérotée : c'est un avertissement
d'ensemble, et il doit être lu **avant** de commencer les 152 astuces, pas
noyé au milieu. Il est placé juste après le sommaire des catégories.

Il est aussi accessible par ancre (#avertissement-article), ce qui permet
d'y renvoyer depuis une séance ou un autre document.

Idempotent : relancer ne duplique rien.
"""
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(RACINE, "cours", "Module Intelligence Artificielle",
                    "seances", "astuces-ia.html")

ANCRE = "avertissement-article"
AVANT = '<h2 id="limites">'

BLOC = """
<h2 id="avertissement-article">⚠️ Avertissement — l'IA peut transformer un article vrai en article faux</h2>
<p><strong>Réponse courte : OUI, c'est un risque réel et sérieux.</strong> Mais avec la bonne
méthode, ce risque devient contrôlable. Voici pourquoi, comment, et comment se protéger.</p>

<h4>1. Le risque est réel : l'IA peut introduire des erreurs</h4>
<p>Quand vous demandez à une IA « améliore mon article », « vérifie mes résultats » ou
« identifie les anomalies », elle ne <strong>connaît pas</strong> votre travail. Elle ne sait
pas ce que vous avez réellement mesuré, ce que contiennent vos données, ni ce que vos
protocoles ont produit.</p>
<p>Elle va donc <strong>deviner</strong> ce qui est plausible, et parfois remplacer une
information correcte par une information fausse mais plausible.</p>
<div class="warn">
  <strong>Le piège principal : l'IA ne dit pas « je ne sais pas » — elle invente une réponse
  crédible.</strong>
</div>

<h4>2. Les 7 types d'erreurs que l'IA peut introduire</h4>
<table>
  <tr><th>Type d'erreur</th><th>Exemple concret</th></tr>
  <tr><td><strong>1. Chiffres inventés</strong></td><td>Vous avez mesuré 87,3 %. L'IA écrit « environ 90 % » ou « 85 % ».</td></tr>
  <tr><td><strong>2. Références fictives</strong></td><td>L'IA ajoute « (Winter et al., 2012) » alors que cet article n'existe pas.</td></tr>
  <tr><td><strong>3. Termes techniques déformés</strong></td><td>Elle écrit « RPL utilise AODV » alors que RPL utilise son propre mécanisme.</td></tr>
  <tr><td><strong>4. Formules modifiées</strong></td><td>Elle « simplifie » une équation et la rend fausse.</td></tr>
  <tr><td><strong>5. Conclusions exagérées</strong></td><td>Vos résultats montrent une amélioration de 5 %. L'IA écrit « amélioration significative ».</td></tr>
  <tr><td><strong>6. Unités changées</strong></td><td>Vous parlez en millisecondes, elle écrit en secondes.</td></tr>
  <tr><td><strong>7. Contexte inventé</strong></td><td>Elle ajoute une comparaison avec un protocole que vous n'avez jamais testé.</td></tr>
</table>
<p><strong>Conséquence :</strong> un article scientifiquement correct peut devenir faux, non
vérifiable, voire frauduleux — sans que vous vous en rendiez compte.</p>

<h4>3. Pourquoi l'IA fait cela ?</h4>
<p>Parce qu'elle fonctionne par <strong>prédiction de texte</strong>, pas par vérification de
vérité.</p>
<ul>
  <li>Elle ne « lit » pas vos données. Elle lit votre texte.</li>
  <li>Elle ne « sait » pas ce qui est vrai. Elle sait ce qui <em>sonne bien</em>.</li>
  <li>Elle ne « vérifie » pas. Elle <strong>reformule</strong>.</li>
</ul>
<p>Donc quand vous lui demandez « vérifie mon article », elle fait en réalité :</p>
<div class="prompt-box">« Je vais écrire une réponse qui ressemble à une vérification. »</div>
<p>Ce n'est pas de la malveillance. C'est sa nature.</p>

<h4>4. Les cas où l'IA est <strong>dangereuse</strong></h4>
<table>
  <tr><th>Situation</th><th>Risque</th></tr>
  <tr><td>Vous lui demandez de « réécrire » vos résultats</td><td>Elle peut modifier les chiffres</td></tr>
  <tr><td>Vous lui demandez de « compléter » vos références</td><td>Elle peut inventer des articles</td></tr>
  <tr><td>Vous lui demandez de « corriger » vos formules</td><td>Elle peut les casser</td></tr>
  <tr><td>Vous lui demandez de « résumer » vos conclusions</td><td>Elle peut exagérer</td></tr>
  <tr><td>Vous lui demandez de « vérifier » sans lui donner vos données brutes</td><td>Elle devine</td></tr>
  <tr><td>Vous copiez-collez sa réponse sans relire</td><td>Catastrophe</td></tr>
</table>

<h4>5. Les cas où l'IA est <strong>utile et sûre</strong></h4>
<table>
  <tr><th>Tâche</th><th>Pourquoi c'est sûr</th></tr>
  <tr><td>Corriger orthographe et grammaire</td><td>L'IA ne touche pas au sens</td></tr>
  <tr><td>Améliorer le style (phrases plus claires)</td><td>Vous relisez après</td></tr>
  <tr><td>Reformuler une phrase sans changer le sens</td><td>Vous comparez</td></tr>
  <tr><td>Vérifier la structure (intro, méthode, résultats, discussion)</td><td>L'IA ne touche pas aux données</td></tr>
  <tr><td>Proposer un plan</td><td>Vous validez</td></tr>
  <tr><td>Traduire un passage</td><td>Vous vérifiez avec un second outil</td></tr>
  <tr><td>Détecter des répétitions</td><td>L'IA signale, vous décidez</td></tr>
  <tr><td>Vérifier la cohérence des temps verbaux</td><td>L'IA ne touche pas aux chiffres</td></tr>
</table>

<h4>6. La règle d'or : ne jamais laisser l'IA toucher à vos données</h4>
<div class="reflexe">
  <strong>L'IA peut toucher aux mots. Elle ne doit JAMAIS toucher aux chiffres, aux formules,
  aux figures, aux résultats, aux références.</strong>
</div>
<p>Si vous suivez cette règle, vous êtes protégé à 90 %.</p>

<h4>7. Méthode de travail sécurisée pour un article de 20 pages</h4>
<ol>
  <li><strong>Sauvegardez une version originale.</strong> Avant toute utilisation de l'IA :
      <code>article_v1_original.docx</code> et <code>article_v1_original.pdf</code>. C'est votre
      référence, et elle vous permet de comparer.</li>
  <li><strong>Travaillez par sections</strong>, jamais sur tout l'article d'un coup.
      Introduction, état de l'art, méthodologie, résultats, discussion, conclusion.</li>
  <li><strong>Ne demandez jamais de « vérifier » vos résultats.</strong> Demandez plutôt :</li>
</ol>
<div class="prompt-box">Voici mes résultats. Ne les modifie pas. Ne les reformule pas.
Dis-moi seulement :
1) si la présentation est claire
2) s'il manque une information pour comprendre
3) si les unités sont cohérentes
Ne touche à aucun chiffre.</div>
<ol start="4">
  <li><strong>Vérifiez chaque chiffre manuellement.</strong> Chiffre par chiffre, formule par
      formule, référence par référence. Si un chiffre a changé, remettez-le.</li>
  <li><strong>Vérifiez les références</strong> : Google Scholar, DOI, site de la revue. Si elle
      n'existe pas, supprimez-la.</li>
  <li><strong>Gardez une trace des modifications</strong> : mode « suivi des modifications » de
      Word, ou comparaison de versions.</li>
  <li><strong>Ne publiez jamais sans relecture humaine finale.</strong> Vous êtes l'auteur,
      vous êtes responsable. L'IA n'est qu'un outil.</li>
</ol>

<h4>8. Exemple concret</h4>
<p>Votre article contient :</p>
<div class="prompt-box">« Le protocole RPL réduit la consommation d'énergie de 23,7 % par
rapport à AODV dans un réseau de 50 nœuds. »</div>
<p><strong>Ce qu'il ne faut pas faire :</strong> <code>Améliore cette phrase.</code></p>
<p><strong>Ce que l'IA pourrait écrire :</strong> « Le protocole RPL réduit la consommation
d'énergie d'environ 25 % par rapport à AODV. »</p>
<p>➡️ Le chiffre a changé. L'article devient faux.</p>
<p><strong>Ce qu'il faut faire :</strong></p>
<div class="prompt-box">Voici une phrase de mon article :
« Le protocole RPL réduit la consommation d'énergie de 23,7 % par rapport à AODV
dans un réseau de 50 nœuds. »

Reformule UNIQUEMENT le style, sans changer AUCUN chiffre, AUCUN nom de protocole,
AUCUNE unité. Donne-moi 2 versions.</div>
<p>➡️ L'IA garde 23,7 %, AODV, 50 nœuds. Vous relisez. C'est sûr.</p>

<h4>9. Prompts dangereux contre prompts sûrs</h4>
<table>
  <tr><th>Prompt dangereux</th><th>Pourquoi</th><th>Prompt sûr</th></tr>
  <tr><td>« Améliore mon article »</td><td>Elle peut tout changer</td><td>« Améliore le style de cette phrase sans changer les chiffres »</td></tr>
  <tr><td>« Vérifie mes résultats »</td><td>Elle invente</td><td>« Vérifie si mes résultats sont clairement présentés, sans les modifier »</td></tr>
  <tr><td>« Complète mes références »</td><td>Elle invente</td><td>« Voici mes références. Vérifie si le format est correct. »</td></tr>
  <tr><td>« Corrige mes formules »</td><td>Elle casse</td><td>« Explique-moi cette formule, ne la modifie pas »</td></tr>
  <tr><td>« Résume mes conclusions »</td><td>Elle exagère</td><td>« Reformule mes conclusions sans changer le sens »</td></tr>
</table>

<h4>10. Ce que l'IA ne doit <strong>jamais</strong> faire</h4>
<ul>
  <li>Modifier un chiffre, une formule, une figure.</li>
  <li>Ajouter une référence.</li>
  <li>Changer un résultat ou inventer une comparaison.</li>
  <li>Reformuler une conclusion sans votre validation.</li>
  <li>Résumer vos données ou « corriger » vos mesures.</li>
</ul>

<h4>11. La règle des 3 vérifications</h4>
<table>
  <tr><th>Vérification</th><th>Question à se poser</th></tr>
  <tr><td><strong>1. Chiffres</strong></td><td>Tous les chiffres sont-ils identiques à l'original ?</td></tr>
  <tr><td><strong>2. Références</strong></td><td>Toutes les références existent-elles vraiment ?</td></tr>
  <tr><td><strong>3. Sens</strong></td><td>Le sens général est-il identique à l'original ?</td></tr>
</table>
<p>Trois « oui » → vous pouvez continuer. Un seul « non » → vous corrigez ou supprimez.</p>

<h4>12. Réponse directe</h4>
<p><strong>« Est-ce qu'une IA peut transformer un article vrai en article faux ? »</strong></p>
<p><strong>Oui, c'est possible.</strong> Cela arrive surtout si vous lui demandez de toucher
aux données, si vous ne relisez pas, ou si vous lui demandez de « compléter » ou « vérifier »
sans lui donner vos données brutes.</p>
<p><strong>Non, ce n'est pas inévitable.</strong> Si vous travaillez section par section, si
elle ne touche jamais aux chiffres, si vous vérifiez chaque référence et si vous gardez une
version originale, l'IA devient un <strong>assistant utile et sûr</strong>.</p>

<h4>13. Le réflexe à retenir</h4>
<div class="reflexe">
  <strong>« Avant de demander à l'IA de toucher à mon article : est-ce que cette demande peut
  modifier mes chiffres, mes formules ou mes références ? »</strong>
</div>
<p>Si oui → reformulez la demande pour l'interdire explicitement. Si non → vous pouvez
continuer.</p>

<h4>14. La phrase de protection à mettre dans tous vos prompts</h4>
<div class="prompt-box">RÈGLES ABSOLUES :
- Ne modifie AUCUN chiffre.
- Ne modifie AUCUNE formule.
- Ne modifie AUCUNE référence.
- Ne modifie AUCUN nom de protocole.
- Ne modifie AUCUNE unité.
- Si tu n'es pas sûr, dis « je ne suis pas certain » au lieu d'inventer.
- Signale clairement ce que tu changes et pourquoi.</div>
<p>Cette phrase, à elle seule, réduit énormément le risque.</p>

<h4>15. Résumé final</h4>
<table>
  <tr><th>Question</th><th>Réponse</th></tr>
  <tr><td>L'IA peut-elle introduire des erreurs ?</td><td>Oui</td></tr>
  <tr><td>Peut-elle transformer un article vrai en faux ?</td><td>Oui, si vous la laissez toucher aux données</td></tr>
  <tr><td>Peut-on l'éviter ?</td><td>Oui, avec une méthode stricte</td></tr>
  <tr><td>Que ne doit-elle jamais toucher ?</td><td>Chiffres, formules, figures, références, résultats</td></tr>
  <tr><td>Que peut-elle faire sans danger ?</td><td>Style, orthographe, structure, clarté</td></tr>
  <tr><td>Quelle est la règle d'or ?</td><td>L'IA touche aux mots, jamais aux données</td></tr>
  <tr><td>Qui est responsable ?</td><td>Vous, l'auteur</td></tr>
</table>
"""


def main():
    with open(PAGE, encoding="utf-8") as f:
        t = f.read()

    if 'id="%s"' % ANCRE in t:
        print("Avertissement déjà présent — rien à faire.")
        return 0

    i = t.find(AVANT)
    if i < 0:
        print("Point d'insertion introuvable (%s absent) : abandon." % AVANT)
        return 1

    bloc = BLOC.strip()
    # garde-fou : un %s oublié produirait une ancre littérale cassée
    if "%s" in bloc or "%d" in bloc:
        print("Le bloc contient un marqueur non substitué : abandon.")
        return 1

    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(t[:i] + bloc + "\n\n" + t[i:])

    print("Avertissement inséré en tête de page.")
    print("   ancre : astuces-ia.html#%s" % ANCRE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
