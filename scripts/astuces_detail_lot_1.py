#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 1 : les astuces 2 à 21.

Fichier séparé pour garder des lots maniables. `astuces_detail.py` charge
tous les lots présents dans ce dossier et les fusionne en un seul
dictionnaire, ce qui permet d'écrire les explications parseries sans
ouvrir un fichier qui devient énorme.

Format court (≈ 300 mots), trois parties dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter
"""

LOT_1 = {}

LOT_1[2] = """
<h4>Pourquoi ça marche</h4>
<p>Chaque fournisseur compte ses quotas <strong>séparément</strong>. Ta limite chez ChatGPT
n'a aucun rapport avec celle de Gemini ou de DeepSeek. Si tu as quatre outils ouverts en
onglets permanents, il devient très difficile de rester bloqué : au pire, tu perds une
minute le temps que l'autre modèle réponde.</p>
<p>Le bénéfice secondaire est souvent plus important que le quota : plusieurs réponses sur
la même question permettent de voir <strong>immédiatement</strong> quel modèle se trompe,
lequel reste flou et lequel va droit au but.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explique [sujet] en 5 points concrets, avec 1 exemple réel pour
chaque point. Si tu n'es pas sûr d'un fait, dis-le clairement plutôt que d'inventer.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne compare pas les réponses sur la <em>longueur</em> mais sur la
<strong>justesse</strong>. Un modèle qui écrit trois paragraphes et se trompe vaut moins
qu'un modèle qui écrit une phrase juste. Et si les trois réponses se contredisent, ce
n'est pas l'IA qui a raison : c'est qu'il faut vérifier la source.</div>
"""

LOT_1[3] = """
<h4>Pourquoi ça marche</h4>
<p>Le quota de l'application mobile et celui du site web sont souvent comptés
<strong>différemment</strong> par le même fournisseur. Quand le site web refuse un message,
l'appli peut encore accepter le même message. C'est souvent le contournement le plus
rapide, et il ne casse rien.</p>
<p>Bonus : l'application mobile est plus rapide pour les petites questions, parce que tu
n'as pas à passer par le navigateur.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Garde la question en brouillon (copiée dans le presse-papier).
Si le site affiche « limite atteinte », ouvre l'application et colle le même texte.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne multiplie pas les fenêtres au point de déclencher toi-même la
limite « usage inhabituel » de ton compte. Deux outils simultanés suffisent. Et vérifie
le nom du modèle affiché en bas : l'application mobile n'utilise pas toujours le même
modèle que le site web.</div>
"""

LOT_1[4] = """
<h4>Pourquoi ça marche</h4>
<p>Les quotas sont calculés en moyenne glissante sur une journée. La nuit, le trafic
diminue : les quotas se relâchent. Entre 23h et 7h, tu as beaucoup plus de marge qu'à
18h, heure de pointe où tout le monde pose ses questions en même temps.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Travail lourd : 2h de rédaction d'exposé.
Placer la session à 6h du matin plutôt qu'à 18h.
Ordre : (1) la recherche, (2) le plan, (3) la rédaction, (4) la relecture.</div>
<div class="tip"><strong>Bonus :</strong> le premier message du matin et le dernier de la
nuit sont les moments où les modèles les plus puissants sont les plus disponibles. Si tu
as besoin d'un modèle fort (et non d'un modèle rapide), réserve-le à ces heures-là.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Évite de tout planifier après minuit : la fatigue fait baisser ta
vigilance et tu vas copier des erreurs sans les voir. La nuit, prépare les prompts ;
le matin, fais le travail.</div>
"""

LOT_1[5] = """
<h4>Pourquoi ça marche</h4>
<p>Plusieurs entreprises offrent gratuitement leurs formules premium aux étudiants, mais
uniquement si tu les demandes. L'offre est rarement visible : il faut la chercher avec une
adresse universitaire ou une carte d'étudiant. Une heure de recherche peut te donner
plusieurs mois d'accès sans limite.</p>
<h4>Offres à vérifier une seule fois</h4>
<ul>
  <li><strong>GitHub Student Pack</strong> — Copilot, Codespaces, et beaucoup d'outils payants.</li>
  <li><strong>Google Workspace for Education</strong> — Gemini et Drive avec plus de marge.</li>
  <li><strong>Notion, Canva, Adobe</strong> — formules Étudiant gratuites.</li>
  <li><strong>OpenRouter, Groq, Hugging Face</strong> — accès gratuit à des modèles modernes.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="warn">Méfie-toi des faux comptes Étudiants : certains sites annoncent des quotas
« premium » mais collectent tes données. N'utilise que les sites officiels
(<code>github.com/education</code>, <code>notion.so</code>, <code>canva.com/education</code>)
et vérifie le nom de domaine avant de t'inscrire avec ton adresse universitaire.</div>
"""

LOT_1[6] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA ne devine pas ce que tu veux : elle complète ce qui manque. Si tu ne précises ni
ton niveau, ni le format, ni la longueur, elle choisit pour elle — et tu obtiens une
réponse générique, écrite pour la moyenne de tout le monde.</p>
<p>Les cinq champs servent à supprimer les hypothèses :</p>
<ul>
  <li><strong>Rôle</strong> — à qui tu parles (professeur, correcteur, vulgarisateur).</li>
  <li><strong>Contexte</strong> — qui tu es, quel niveau, pour quel objectif.</li>
  <li><strong>Tâche</strong> — une seule action, formulée à l'infinitif.</li>
  <li><strong>Format</strong> — liste, tableau, code, 5 puces, 150 mots.</li>
  <li><strong>Contraintes</strong> — langue, longueur, ce qu'il ne faut pas inventer.</li>
</ul>
<h4>Exemple à copier</h4>
<div class="prompt-box">Rôle : professeur de français pour des étudiants de langues.
Contexte : 2e année PEP, niveau C1, prépare une analyse de texte.
Tâche : analyse ce passage.
Format : 5 puces, puis 2 phrases de conclusion.
Contraintes : français simple, 200 mots maximum, nomme les figures de style.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si la réponse est générique, c'est qu'un des cinq champs manque. Ne
réécris pas tout : ajoute <em>un seul</em> champ manquant et relance. C'est toujours plus
rapide que de repartir de zéro.</div>
"""

LOT_1[7] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA répond plus vite qu'elle ne pose de questions. Résultat : elle produit une
réponse correcte en apparence mais mal ciblée, et tu perds du temps à corriger. En lui
demandant de poser trois questions d'abord, tu obtiens un <strong>mini-cadrage écrit</strong>,
que tu peux corriger en une ligne si sa compréhension est fausse.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Avant de répondre, pose-moi exactement 3 questions pour clarifier
mon besoin. Ensuite seulement, donne la réponse complète.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si tu réponds aux trois questions de manière vague (« un peu comme ça »,
« en général »), l'IA ne pourra pas faire mieux. Sois précis sur le niveau, la longueur
et l'usage final. Deux minutes de réponses claires valent mieux que dix minutes de
reformulation d'une réponse fausse.</div>
"""

LOT_1[8] = """
<h4>Pourquoi ça marche</h4>
<p>« Explique-moi la photosynthèse » produit une réponse que tu ne comprends pas
totalement, mais que tu n'oses pas dire. En demandant deux niveaux successifs, tu obtiens
d'abord une image mentale simple, puis le vocabulaire exact. Tu peux alors relier les
deux : c'est là que la notion devient vraiment acquise.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explique [notion] comme à un enfant de 10 ans, en 4 phrases maximum.
Puis remonte d'un cran : version étudiant de licence, toujours en français simple.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne reste pas au niveau enfant si tu passes un examen. L'astuce sert à
comprendre, pas à rester dans la simplicité. C'est la deuxième version, avec le vocabulaire
technique, que tu notes dans ta fiche de révision.</div>
"""

LOT_1[9] = """
<h4>Pourquoi ça marche</h4>
<p>Une réponse en prose est difficile à réutiliser : il faut la relire pour en extraire
les étapes. Un tableau se copie directement dans une fiche, une présentation ou un
carnet. En imposant le format, tu transformes une conversation en matériau de travail.</p>
<h4>Exemples à copier</h4>
<div class="prompt-box">Réponds UNIQUEMENT sous forme de tableau markdown à 3 colonnes :
| Étape | Action concrète | Temps estimé |
Rien d'autre avant ou après le tableau.</div>
<div class="prompt-box">Retourne-moi un tableau : | Problème | Cause probable |
Comment vérifier |, avec 5 lignes maximum.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le format demandé n'est pas toujours respecté. Si l'IA ajoute du texte
autour du tableau, réponds : « Réponds uniquement avec le tableau, rien autour. » Et
précise toujours le nombre de colonnes : sans cela, tu recevras 3 colonnes quand tu en
voulais 4.</div>
"""

LOT_1[10] = """
<h4>Pourquoi ça marche</h4>
<p>Un exemple seul ne suffit pas : tu ne sais pas à quoi ressemble l'erreur, donc tu ne
sais pas quand tu la fais toi-même. Les contre-exemples dessinent la <strong>frontière</strong>
entre ce qui est correct et ce qui ne l'est pas. C'est ce qui fait passer une règle du
savoir à la pratique.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne-moi 3 exemples corrects de [chose] et 3 contre-exemples
(ce qu'il ne faut PAS faire), avec une phrase d'explication pour chaque.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Vérifie que les contre-exemples sont vraiment <em>plausibles</em> : une
IA peut inventer des erreurs que personne ne commettrait. Demande explicitement
« des erreurs que les étudiants font réellement », sinon tu retiendras des règles qui ne
servent à rien.</div>
"""

LOT_1[11] = """
<h4>Pourquoi ça marche</h4>
<p>En obligant l'IA à écrire son raisonnement avant la réponse, tu obtiens deux choses :
la réponse est souvent meilleure, et surtout tu <strong>vois où elle se trompe</strong>. Une
erreur dans une étape intermédiaire est bien plus facile à repérer qu'une erreur dans une
conclusion. C'est la meilleure méthode pour apprendre un raisonnement.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Réfléchis étape par étape. Pour chaque étape, écris :
1) ce que tu penses  2) pourquoi  3) ce que tu conclus
À la fin seulement, donne la réponse finale en 3 lignes.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Utilise cette méthode pour <strong>comprendre et vérifier</strong>, pas
pour produire un texte à rendre. Un exposé doit contenir ton raisonnement, pas celui de
l'IA. Si tu recopies le raisonnement mot pour mot, tu n'auras rien appris et tu ne sauras
pas défendre ton travail le jour de l'oral.</div>
"""

LOT_1[12] = """
<h4>Pourquoi ça marche</h4>
<p>Une demande vague de correction (« corrige mon texte ») donne un texte « un peu
mieux ». En demandant un <strong>professeur sévère</strong> avec un format imposé — la
faute, la correction, la règle, puis une note — tu obtiens une correction complète, qui
enseigne la règle au lieu de seulement l'appliquer.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mon texte. Corrige-le comme un professeur de français très
exigeant. Pour chaque erreur : (a) la faute, (b) la correction, (c) la règle en 1 phrase.
À la fin : note sur 20 + 3 conseils prioritaires.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une note de 14/20 donnée par une IA ne veut rien dire academicement.
Sers-t'en pour corriger tes fautes récurrentes, jamais pour juger ton niveau réel. Et si tu
ne comprends pas une correction, demande « pourquoi c'est une faute ? » — c'est là que
t'apprends vraiment.</div>
"""

LOT_1[13] = """
<h4>Pourquoi ça marche</h4>
<p>La reformulation est l'un des usages les plus sûrs de l'IA : elle ne touche ni aux
faits, ni aux idées. En posant des limites claires — « même sens, mêmes faits, aucune
information en plus » — tu obtiens un texte plus fluide sans risquer une déformation.
C'est aussi le meilleur moyen de supprimer les tournures qui ressemblent trop à d'autres
textes.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Reformule ce texte en gardant EXACTEMENT le même sens et les mêmes
faits. Change uniquement le style : plus fluide, plus professionnel, phrases plus courtes.
Ne rajoute aucune information. Signale si un passage me semble ambigu.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA « améliore » parfois le texte en ajoutant des idées qu'elle croit
utiles. Relis ligne à ligne contre ton original. Si une phrase est apparue, supprime-la :
c'est le seul moyen fiable de garder 100 % de ton propos.</div>
"""

LOT_1[14] = """
<h4>Pourquoi ça marche</h4>
<p>Utiliser le mauvais outil est la perte de temps la plus courante. On demande à
Perplexity d'écrire un texte (il le fait mal) et à ChatGPT de donner des sources (il en
invente). Chaque modèle a une <strong>spécialité</strong> : le reconnaître évite dix
minutes d'essais ratés.</p>
<h4>La règle en quatre lignes</h4>
<ul>
  <li><strong>Écrire, expliquer, corriger</strong> → ChatGPT ou Claude.</li>
  <li><strong>Lire un PDF, une image, un document Google</strong> → Gemini.</li>
  <li><strong>Vérifier un fait, trouver une source</strong> → Perplexity.</li>
  <li><strong>Code et mathématiques</strong> → DeepSeek (gratuit) ou Claude.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="warn">Ne demande jamais des <strong>sources</strong> à un modèle qui ne fournit
pas de liens : il en inventera avec un format parfait. Et ne demande pas d'analyser un PDF
à un modèle qui ne lit pas les PDF — il répondra à partir du titre du fichier.</div>
"""

LOT_1[15] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA ne sait pas qu'elle se trompe : elle écrit la même chose avec la même assurance
qu'elle a raison. Mais une <strong>autre</strong> IA, elle, n'a pas le même angle mort. En
lui donnant la première réponse à vérifier, tu obtiens une deuxième lecture indépendante :
c'est le principe de la double correction.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici la réponse de ChatGPT : [colle la réponse]
Tu es un fact-checker strict. Liste :
1) les affirmations exactes
2) les affirmations douteuses ou fausses
3) ce qui manque
Ne reformule pas, juge seulement.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les deux IA peuvent se tromper de la même façon, surtout sur les
statistiques. La vérification par une autre IA sert à repérer les <em>incohérences</em>,
pas à prouver la vérité. Pour un chiffre ou une date, il faut toujours une source
cliquable.</div>
"""

LOT_1[16] = """
<h4>Pourquoi ça marche</h4>
<p>L'accord entre trois modèles est un indice de fiabilité, pas une preuve. En pratique, si
trois IA indépendantes donnent la même information, la probabilité qu'elles aient inventé
la même chose est très faible. Si elles divergent, c'est un signal clair : il faut
vérifier, pas choisir.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Question : [fait à vérifier]
Compare ma question à Perplexity, ChatGPT et Gemini.
Si vos réponses divergent, dis-le explicitement et indique laquelle donne une source.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une IA qui cite ses sources a parfois lu un article critique et l'a
interprété à l'opposé. Ouvre <strong>le lien</strong> : ne te contente jamais du résumé. Et
si une seule des trois a une source cliquable, c'est elle qui fait foi.</div>
"""

LOT_1[17] = """
<h4>Pourquoi ça marche</h4>
<p>Par défaut, comparer deux IA demande d'ouvrir deux onglets, de copier la question deux
fois, de lire deux réponses et de revenir en arrière. Une extension barre latérale envoie
la même question à plusieurs modèles en un clic : tu vois les réponses côte à côte, et le
gain de temps est réel sur une comparaison répétée.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Rédige une seule question complète dans la barre latérale.
Sélectionne 3 modèles, clique sur « comparer ».
Note dans un tableau : modèle | exactitude | ton | longueur | source.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ces extensions ont accès à <strong>toutes les pages que tu visites</strong> :
elles lisent tes mails, tes documents, et même tes comptes bancaires si tu ouvres l'onglet
pendant. Installe-les uniquement si tu en as besoin, révoque-les sinon, et jamais sur un
ordinateur qui contient des données sensibles.</div>
"""

LOT_1[18] = """
<h4>Pourquoi ça marche</h4>
<p>Réécrire un prompt qui a marché est du temps perdu, et les chances de le refaire moins
bien sont élevées. Un fichier unique où tu ranges tes prompts transforme une correction
répétée en <strong>ressource réutilisable</strong>. C'est l'un des gestes les plus
rentables : en deux semaines, tu as ta bibliothèque personnelle.</p>
<h4>Comment faire</h4>
<div class="prompt-box"># Prompts qui marchent

## Fiche de révision à partir d'un PDF
Contexte : étudiant 2e année PEP.
Tâche : transforme ce PDF en fiche de révision.
Format : 10 titres, 3 points sous chacun, 1 exemple par point.
Contrainte : ne pas inventer, signaler les passages illisibles.</div>
<h4>Le piège à éviter</h4>
<div class="tip"><strong>Réflexe :</strong> dès qu'une réponse te plaît, copie le prompt
<em>avant</em> de fermer l'onglet. Après, il est trop tard — et tu ne sauras plus
exactement ce qui avait marché.</div>
"""

LOT_1[19] = """
<h4>Pourquoi ça marche</h4>
<p>Les conversations importantes disparaissent : un nettoyage automatique, un changement
de compte, ou une limite atteinte qui les coupe. L'export te donne un fichier que tu
possèdes, hors ligne, que tu peux relire dans un an et citer dans un travail.</p>
<h4>Comment faire</h4>
<ul>
  <li><strong>ChatGPT</strong> → menu <code>⋯</code> de la conversation → <em>Exporter</em>.</li>
  <li><strong>Claude</strong> → bouton <em>Share</em> → copie ou export.</li>
  <li><strong>Gemini</strong> → bouton de partage → copie le texte.</li>
</ul>
<p>Ranges les fichiers dans un dossier daté : <code>2026-09-29-expose-photosynthese</code>.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Une conversation exportée contient tout : tes questions, mais aussi
les extraits de documents que tu as collés. Vérifie le contenu avant de partager le
fichier, et ne le mets jamais en ligne tel quel.</div>
"""

LOT_1[20] = """
<h4>Pourquoi ça marche</h4>
<p>Une liste de conversations intitulée « Nouvelle discussion », « Nouvelle discussion »,
« Nouvelle discussion » devient inutilisable au bout de deux semaines. Nommer et épingler
transforme l'historique en bibliothèque consultable : tu retrouves en dix secondes le
prompt qui t'avait servi pour le cours de mardi.</p>
<h4>Comment faire</h4>
<div class="prompt-box">28/09 — Fiche révision linguistique appliquée
28/09 — 10 QCM chapitre 4 + réponses
27/09 — Rédaction exposé : plan validé</div>
<h4>Le piège à éviter</h4>
<div class="tip"><strong>Règle de nommage simple :</strong> date + type de travail + sujet.
Ne mets jamais le contenu de la conversation dans le titre, il devient illisible. Et
supprime régulièrement les conversations ratées : une liste de 200 discussions dont 20
utiles est une liste où l'on ne trouve plus rien.</div>
"""

LOT_1[21] = """
<h4>Pourquoi ça marche</h4>
<p>Sans réglages préalables, tu répètes à chaque conversation ton niveau, ta langue et la
longueur que tu veux. Les <strong>Instructions personnalisées</strong> sont écrites une
fois et appliquées automatiquement à toutes les réponses. Tu économises du temps et,
surtout, tu obtiens des réponses cohérentes d'un bout à l'autre de tes travaux.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je suis étudiant en 2e année PEP (filière Langues).
Niveau : français C1, anglais B2, arabe FLE débutant.
Réponds en français sauf demande contraire.
Format préféré : listes numérotées, titres courts, phrases simples.
Quand tu n'es pas sûr d'un fait, dis-le au lieu d'inventer.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne mets pas 30 consignes dans les instructions permanentes : elles sont
appliquées à chaque message, et l'IA finira par en ignorer la moitié. Cinq consignes
suffisent : langue, niveau, format, longueur, honnêteté sur les sources.</div>
"""
