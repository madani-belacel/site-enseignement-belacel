#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 3 : les astuces 42 à 61.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Rédigé pendant les sessions de révision d'examen, pendant les articles et
pendant la préparation des présentations : c'est là que ces techniques
servent vraiment.
"""

LOT_3 = {}

LOT_3[42] = """
<h4>Pourquoi ça marche</h4>
<p>Le même contenu n'a pas la même forme à l'écrit et à l'oral. Demander les deux
versions oblige l'IA à choisir ce qui est essentiel, et te montre ce que tu peux couper
quand le temps de parole est limité.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Réécris ce paragraphe en style académique formel (pour un article).
Puis réécris-le en style oral clair (pour un exposé de 5 minutes).
Garde exactement les mêmes informations.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La version orale d'une IA est souvent trop rapide à réciter : elle
n'attend pas de respiration. Lis-la à voix haute et chronomètre-la. Si tu dépasses, demande
explicitement « 30 % plus court, garde les 3 idées principales ».</div>
"""

LOT_3[43] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA produit des références au format parfait — auteurs, année, revue, pages — sans
avoir l'obligation d'avoir lu l'article. Le piège est là : plus c'est propre, plus c'est
trompeur. Mais <strong>Google Scholar ne bluffe pas</strong> : si le titre n'apparaît pas,
l'article n'existe pas.</p>
<h4>Comment faire</h4>
<ol>
  <li>Copie le <strong>titre exact</strong> dans Google Scholar.</li>
  <li>Rien n'apparaît → la référence est inventée, supprime-la.</li>
  <li>Si elle existe → clique sur <em>Citer</em> pour récupérer la vraie référence.</li>
  <li>Ouvre le <strong>DOI</strong> sur <code>doi.org</code> : s'il ne renvoie rien, elle est fausse.</li>
</ol>
<h4>Le piège à éviter</h4>
<div class="warn">Une référence peut <em>exister</em> et dire autre chose que ce que
l'IA affirme. Vérifie aussi que l'article parle bien de ton sujet : c'est l'erreur la plus
fréquente, et la plus difficile à repérer.</div>
"""

LOT_3[44] = """
<h4>Pourquoi ça marche</h4>
<p>Une réponse longue et fausse coûte dix minutes de relecture. Une réponse qui commence
par « voici trois sources vérifiables » te permet de <strong>valider avant de lire</strong>.
Tu inverses l'ordre : d'abord la preuve, ensuite le développement.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Avant de développer, donne-moi 3 sources fiables (avec liens si
possible) sur ce sujet. Si tu n'en as pas, dis-le clairement. Ensuite seulement, développe.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Des liens inventés sont plus fréquents que des références inventées. Vérifie
que chaque URL s'ouvre <strong>et</strong> qu'elle mène à l'article annoncé, pas vers une
page d'accueil. Si l'IA ne donne aucun lien, ne considère pas la réponse comme sourcée.</div>
"""

LOT_3[45] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA qui invente ne dit pas « je ne sais pas » : elle dit un chiffre précis avec la
même assurance qu'un chiffre vrai. La régularité est donc un signal d'alerte, pas de
fiabilité. Un vrai chiffre est souvent rond, daté, et accompagné d'une source.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu as donné ce chiffre : [X].
Quelle est ta source exacte ? Donne le lien, ou dis clairement que tu n'en as pas.</div>
<h4>Le piège à éviter</h4>
<div class="tip"><strong>Signal d'alerte supplémentaire :</strong> un chiffre trop
précis et trop arrondi à la fois (« 73,7 % des étudiants ») sans source est presque
toujours inventé. Un chiffre crédible s'accompagne d'un auteur, d'une année et d'un lien.</div>
"""

LOT_3[46] = """
<h4>Pourquoi ça marche</h4>
<p>Choisir une revue demande de croiser cinq critères (impact, délai, frais, champ, politique
IA). C'est exactement le type de travail où l'IA compare vite — à condition de lui imposer
un format et de ne rien accepter sans vérification.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je travaille sur [thème précis].
Propose 5 revues Q1 ou Q2 adaptées (Scimago). Pour chacune :
facteur d'impact approximatif, délai de review typique, frais éventuels,
et si elles acceptent l'usage déclaré de l'IA.
Signale clairement ce dont tu n'es pas sûr.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les facteurs d'impact <strong>se contredisent</strong> selon la source
(Journal of Citation Reports, SJR, le site de la revue). Ne cite jamais un facteur
d'impact sans dire d'où il vient, et vérifie les frais de publication sur le site officiel :
beaucoup de revues Q1 facturent 2 000 à 5 000 euros à l'acceptation.</div>
"""

LOT_3[47] = """
<h4>Pourquoi ça marche</h4>
<p>Le plagiat vient rarement d'une copie mot pour mot : il vient d'un texte généré dont les
tournures calquent un article existant. La parade est de garder la <strong>structure et les
données</strong>, et de n'accepter que des <strong>reformulations</strong> que tu peux
réécrire à ta main.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mon plan détaillé et mes résultats. Aide-moi à rédiger la
section [Introduction / Méthode / Discussion] :
- structure claire
- phrases fluides
- AUCUNE phrase copiée d'un autre article
- signale les endroits où je dois absolument mettre une citation</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si tu demandes un article entier, tu obtiens du texte générique qui
ressemble à d'autres articles : c'est ce qui déclenche les alertes des éditeurs. Rédige
section par section, avec <strong>tes</strong> données, et ne garde que les transitions.</div>
"""

LOT_3[48] = """
<h4>Pourquoi ça marche</h4>
<p>Répondre point par point en tableau impose trois choses qu'on oublie toujours : répondre
à <strong>toutes</strong> les remarques, dire <strong>quoi</strong> on a modifié, et
indiquer <strong>où</strong>. C'est exactement ce que le comité vérifie. Un tableau rend
l'oubli visible immédiatement.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici la lettre des reviewers et mon article.
Rédige une réponse point par point en tableau 3 colonnes :
| Remarque du reviewer | Ce que j'ai modifié | Page / ligne exacte |
Ton : respectueux, factuel, sans excuses excessives.
Je réponds à CHAQUE remarque, même celles que je refuse.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si tu refuses une remarque, explique pourquoi calmement — ne supprime
jamais la ligne. Un reviewer qui voit sa remarque supprimée relit l'article avec un œil
hostile. Et ne réponds jamais par un texte généré brut : relis et personnalise.</div>
"""

LOT_3[49] = """
<h4>Pourquoi ça marche</h4>
<p>Depuis 2023, la plupart des revues exigent la déclaration de l'usage de l'IA. Ne pas
déclarer est plus risqué que déclarer : les éditeurs partagent leurs signalements, et un
texte découvert après publication peut mener à la <strong>rétractation</strong>.</p>
<h4>Phrase type à adapter</h4>
<div class="prompt-box">« ChatGPT (version GPT-4o) et DeepL ont été utilisés pour reformuler
certains paragraphes et pour la traduction. Aucune donnée ni analyse n'a été générée par
l'IA. L'auteur assume l'entière responsabilité du contenu scientifique. »</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA ne peut <strong>jamais</strong> être co-auteur (règle commune à Nature,
Science et Elsevier). Note aussi le <strong>numéro de version</strong> : « ChatGPT » seul ne
suffit pas. Et vérifie la politique de ta revue, car certaines interdisent toute écriture
générative, même déclarée.</div>
"""

LOT_3[50] = """
<h4>Pourquoi ça marche</h4>
<p>Un article est refusé le plus souvent pour des raisons formelles : une référence
inexistante, une phrase laissée telle quelle, une figure manquante. Ces erreurs se voient
en quatre minutes avec une liste de contrôle, et se rattrapent définitivement.</p>
<h4>La liste</h4>
<ul>
  <li>Chaque référence existe vraiment (Scholar + DOI ouvert).</li>
  <li>Usage de l'IA déclaré.</li>
  <li>Aucune phrase laissée telle quelle sans relecture humaine.</li>
  <li>Normes de la revue respectées (longueur, style de citation, figures).</li>
  <li>Version « tracked changes » prête pour le comité.</li>
  <li>Figures lisibles en noir et blanc.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="tip">Fais cette liste <strong>la veille</strong>, jamais le matin de l'envoi.
Imprime l'article en PDF et vérifie les numéros de page : c'est là que se cachent les
tableaux qui débordent et les références orphelines.</div>
"""

LOT_3[51] = """
<h4>Pourquoi ça marche</h4>
<p>Quand tout est écrit d'un seul bloc, l'IA ne sait plus ce qui est une instruction et ce
qui est de la donnée à traiter. Les séparateurs <code>###</code> suppriment cette
ambiguïté : c'est le même principe que les titres dans un document, et cela réduit
nettement les réponses décalées.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">### Instructions
Réponds en français, en 5 puces maximum.
### Contexte
Je prépare un exposé de 10 minutes pour des étudiants de 2e année.
### Données
[colle ici ton document]</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne mets jamais tes données dans la section <em>Instructions</em> : l'IA
peut les traiter comme des consignes (« réponds en 5 puces » deviendrait une consigne
contenue dans ta donnée). Sépare toujours, même si ça paraît verbeux.</div>
"""

LOT_3[52] = """
<h4>Pourquoi ça marche</h4>
<p>Montrer deux ou trois exemples du résultat attendu vaut mieux que dix lignes de
description. L'IA apprend <strong>le format</strong> en imitant, et elle ne peut plus se
tromper d'interprétation sur la structure.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Montre le format exact que tu attends.
Entrée : « bonjour » → Sortie : « Salutation »
Entrée : « merci » → Sortie : « Remerciement »
Fais pareil pour ces 10 phrases : [liste]</div>
<h4>Le piège à éviter</h4>
<div class="warn">Tes exemples ne doivent pas contenir d'erreur : l'IA va la reproduire
fidèlement, même si tu lui demandes de l'ignorer. Vérifie que le premier exemple est
rigoureusement correct — c'est lui qui sert de modèle aux dix suivants.</div>
"""

LOT_3[53] = """
<h4>Pourquoi ça marche</h4>
<p>Une seule version, c'est un tirage au sort : tu ne sais pas si c'est la meilleure
possible. En demandant trois versions de longueurs différentes, tu obtiens un <strong>menu
</strong>, et souvent tu découvres que la version « créative » contient la meilleure idée de
la version « détaillée ».</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne-moi 3 versions de ce texte :
1) une version courte (50 mots max)
2) une version détaillée (150 mots)
3) une version créative et originale
Garde le même sens et les mêmes faits.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Prends toujours la <strong>version 1 comme base</strong> et complète
avec la version 2. La version créative est presque toujours plus longue et plus fade : c'est
un point de départ, pas un texte à rendre.</div>
"""

LOT_3[54] = """
<h4>Pourquoi ça marche</h4>
<p>Demander directement une solution te fait tomber sur la première idée venue, qui n'est
pas forcément la meilleure. Explorer trois pistes <strong>avant</strong> de choisir fait
apparaître les compromis, et le tableau comparatif évite un choix aveugle.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explore 3 solutions possibles pour [problème].
Compare-les dans un tableau : avantages, inconvénients, coût, temps.
Puis recommande la meilleure et explique pourquoi.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La recommandation finale est souvent celle qui « a le plus l'air » scraped,
pas la meilleure. Demande explicitement « sur quels critères te bases-tu ? » et tranche
toi-même avec tes propres contraintes (temps, budget, niveau).</div>
"""

LOT_3[55] = """
<h4>Pourquoi ça marche</h4>
<p>Si la première réponse est fausse, la cause est presque toujours une information
manquante. Demander à l'IA quelles questions elle aurait dû te poser identifie cette
information en une ligne — et c'est toi qui décides de la fournir, pas elle qui suppose.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Quelles questions aurais-tu dû me poser pour mieux répondre ?
Pose-les maintenant, puis attends mes réponses avant de continuer.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Ne réponds pas vite aux questions de l'IA : c'est précisément là que tu
révèles tes vraies contraintes. « C'est pour un exposé de 10 minutes devant des étudiants
qui ne connaissent pas le sujet » change complètement la réponse.</div>
"""

LOT_3[56] = """
<h4>Pourquoi ça marche</h4>
<p>Demander une note oblige l'IA à se juger elle-même, et l'explication de la note révèle
les points faibles qu'elle n'aurait pas signalés d'elle-même. La « version 9/10 » est le
vrai intérêt : elle corrige ce qui a été identifié comme faible.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Note ta réponse sur 10.
Explique pourquoi tu ne mets pas 10.
Propose ensuite une version 9/10.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La note est optimiste : une IA trouve rarement moins de 8/10 à sa propre
réponse. Ne la prends pas pour une évaluation. Mais <strong>l'explication de la note</strong>
est fiable : c'est une vraie liste de faiblesses, et c'est la partie qui t'intéresse.</div>
"""

LOT_3[57] = """
<h4>Pourquoi ça marche</h4>
<p>Une thèse n'est solide que si elle résiste aux objections. Demander les meilleurs
arguments <strong>contre</strong> ta idée — et non des arguments en sa faveur — révèle les
angles morts avant le jury. C'est le meilleur exercice de préparation à un oral.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne les 3 meilleurs arguments contre ma thèse :
[ta thèse]
Puis réponds à chacun de ces arguments de façon calme et factuelle.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA aura parfois raison contre toi, et c'est le but. Ne rejette pas un
argument parce qu'il ne t'arrange pas : intègre-le, ou reformule ta thèse pour y répondre.
Un jury finira par poser la question que l'IA vient de te préparer.</div>
"""

LOT_3[58] = """
<h4>Pourquoi ça marche</h4>
<p>Une analogie de la vie quotidienne crée une image mentale durable ; une analogie
technique relie la notion au reste de la matière. Les deux ensemble transforment une
définition abstraite en chose qu'on sait expliquer de bouche à l'oreille.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explique ce concept avec :
1) une analogie de la vie quotidienne
2) une analogie technique
3) une phrase de synthèse de 15 mots</div>
<h4>Le piège à éviter</h4>
<div class="tip">Vérifie que l'analogie ne casse pas : une analogie qui marche pour
l'explication peut donner une <strong>contre-explication</strong> fausse. Demande
« dans quel cas cette analogie cessera-t-elle d'être vraie ? » — c'est là que se trouve la
vraie limite de la notion.</div>
"""

LOT_3[59] = """
<h4>Pourquoi ça marche</h4>
<p>Un glossaire automatique transforme une réponse dense en vocabulaire réutilisable. Tu
obtiens d'un coup les termes à définir dans ton travail, avec une définition calibrée et un
exemple — exactement ce qu'un correcteur attend.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">À la fin de ta réponse, ajoute un glossaire des termes techniques
utilisés. Pour chaque terme : définition en 1 phrase + un exemple concret.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Attention aux faux amis : l'IA peut définir un terme avec un sens différent
du tien dans la discipline (« réseau » en informatique ≠ « réseau » en sociologie). Vérifie
chaque définition dans ton cours avant de la reprendre.</div>
"""

LOT_3[60] = """
<h4>Pourquoi ça marche</h4>
<p>Une notion exige deux compréhension : savoir de quoi ça parle, et savoir où ça ne marche
plus. Le mode débutant installe l'image, le mode expert installe les limites. Le second
est souvent plus utile que le premier pour un travail de recherche.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explique [notion] en deux temps :
- Mode débutant : 5 phrases maximum, sans jargon.
- Mode expert : 10 lignes, avec les nuances et les limites.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'ordre compte : ne demande jamais le mode expert en premier, tu risques
de ne pas comprendre la base. Commence par le débutant, vérifie que tu as compris, puis
demande l'expert.</div>
"""

LOT_3[61] = """
<h4>Pourquoi ça marche</h4>
<p>Un format strict transforme une conversation en <strong>donnée exploitable</strong> :
la réponse peut être copiée dans un tableur, un script ou un programme. C'est la brique de
base de toute automatisation, et la première étape avant d'utiliser l'API.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Réponds uniquement en JSON valide. Aucun texte avant ou après.
Structure attendue :
{ "résumé": "...", "points": ["...", "..."], "confiance": "élevé|moyen|faible" }</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les modèlesadiercent parfois du JSON valide à l'intérieur de
markdown <code>```</code>, ou ajoutent une virgule en trop. Vérifie en collant ta réponse
dans un validateur (un simple <code>JSON.parse</code> dans la console du navigateur
suffit) avant de l'utiliser dans un script.</div>
"""
