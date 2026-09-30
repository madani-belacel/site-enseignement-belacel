#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 4 : les astuces 62 à 81.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Ce lot monte en technicité : prompts avancés, workflows, données. Les
explications signalent explicitement ce qui relève du niveau « informatique »
et ce qu'un étudiant peut faire seul dans un tableur.
"""

LOT_4 = {}

LOT_4[62] = """
<h4>Pourquoi ça marche</h4>
<p>Une tâche trop grosse est traitée de travers : l'IA melee tout et le résultat est
moyen partout. En découpant en étapes, chaque étape est précise, et la critique de l'étape
suivante porte sur un travail court et lisible. C'est la même logique qu'un TP en plusieurs
parties.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Étape 1 : résume ce texte en 5 points.
Étape 2 : critique ces 5 points.
Étape 3 : améliore les points faibles.
Je valide chaque étape avant que tu passes à la suivante.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne saute pas d'étape et ne colle pas l'étape 2 sans avoir lu l'étape 1.
L'erreur se propage : si l'étape 1 est mauvaise, l'étape 3 la corrige sans comprendre le
problème. C'est le piège le plus fréquent quand on utilise un agent.</div>
"""

LOT_4[63] = """
<h4>Pourquoi ça marche</h4>
<p>Sans rôle précis, une IA répond comme un généraliste : juste, mais vague. Un rôle
<strong>borné</strong> oblige à un raisonnement spécifique, et surtout à reconnaître ses
limites — ce qui est plus utile qu'une réponse fausse mais assurée.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu es un avocat spécialisé en droit du travail, pas un assistant
généraliste. Tu réponds uniquement dans le cadre du droit français.
Si la question dépasse ton domaine, dis-le.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Sois précis sur le <strong>pays</strong> autant que sur la spécialité :
« droit du travail » sans pays produce un mélange entre droit français, belge et
camerounais, impossible à utiliser dans un travail.</div>
"""

LOT_4[64] = """
<h4>Pourquoi ça marche</h4>
<p>Le même contenu ne s'adresse pas au même lecteur. En nommant le public, l'IA choisit
le vocabulaire, la longueur et le ton. C'est utile pour un cours : la même notion s'explique
en 8 ans, en licence, ou en recherche.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Réécris ce texte pour :
- un enfant de 8 ans
- un PDG pressé
- un chercheur en biologie
Garde les mêmes informations, adapte le vocabulaire et le ton.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un public « expert » ne veut pas dire « jargon » : un chercheur en
biologie n'a pas besoin qu'on lui explique la cellule. Demande plutôt « pour un lecteur
<strong>du même domaine</strong> que moi ».</div>
"""

LOT_4[65] = """
<h4>Pourquoi ça marche</h4>
<p>Les biais ne sautent pas aux yeux quand on est dedans — c'est précisément pour ça qu'ils
passent. Une relecture ciblée sur quatre types de biais (« qu'est-ce que je n'ai pas cité ? »)
les fait apparaître, et la reformulation proposée te donne directement la version neutre.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Relis ton texte. Signale les biais possibles : culturels, de
confirmation, de genre, de sélection. Propose une reformulation plus neutre pour chaque
passage concerné.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Demande aussi les <strong>silences</strong> : « quelles parties du sujet
n'ai-je pas traitées ? » C'est là que se cache le biais de sélection — un article sur un
sujet ne parle que des réussites, jamais des échecs.</div>
"""

LOT_4[66] = """
<h4>Pourquoi ça marche</h4>
<p>Réécrire un prompt à chaque fois est la perte de temps la plus banale. Avec des
<strong>crochets</strong>, tu écris la structure une fois et tu ne remplis que les
variables. Le prompt devient un formulaire, et le résultat devient cohérent d'un travail à
l'autre.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu es [RÔLE].
Contexte : [PUBLIC] + [OBJECTIF].
Tâche : [TÂCHE].
Format : [FORMAT].
Contraintes : [LONGUEUR], [TON], [LANGUE].</div>
<h4>Le piège à éviter</h4>
<div class="warn">Oublie un crochet et l'IA invente ce qui manque. Relis toujours ton prompt
en cherchant les <code>[</code> restants avant d'envoyer : c'est l'erreur numéro un des
templates.</div>
"""

LOT_4[67] = """
<h4>Pourquoi ça marche</h4>
<p>Une conversation longue finit par être noyée : l'IA oublie le début. En gardant chaque
sortie intermédiaire dans un <strong>fichier</strong>, tu peux reprendre le travail plus
tard, changer d'outil, ou revenir sur une étape sans tout refaire. C'est ce qui rend un
travail long réellement reprenable.</p>
<h4>Comment faire</h4>
<div class="prompt-box">projet/
├── etape1-synthese.md
├── etape2-critique.md
├── etape3-version-finale.md
└── sources.md</div>
<p>Chaque étape est un fichier. Le nom dit ce que c'est, l'ordre dit dans quel ordre les
relire.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Ne supprime jamais une étape intermédiaire, même si elle est mauvaise : le
diagnostic part de là. Archive les anciennes versions dans un dossier <code>brouillons/</code>.</div>
"""

LOT_4[68] = """
<h4>Pourquoi ça marche</h4>
<p>Toute tâche répétitive contient un copier-coller qui te fatigue et des oublis. Make et
Zapier branchent un formulaire sur l'IA, puis sur un tableur ou un e-mail : le traitement
devient automatique, et l'erreur humaine disparaît.</p>
<h4>Exemple de scénario</h4>
<div class="prompt-box">Formulaire (question d'un étudiant)
→ IA (réponse en 5 lignes, avec le nom du cours)
→ Google Sheets (archivage automatique)
→ E-mail (réponse envoyée)</div>
<h4>Le piège à éviter</h4>
<div class="warn">Avant d'automatiser, vérifie trois points : l'IA a-t-elle accès à
l'<strong>intégralité</strong> de la question, le résultat est-il relu par un humain au moins
au début, et que se passe-t-il si l'IA se trompe ? Une automatisation qui envoie une
réponse fausse sans contrôle est pire qu'un copier-coller.</div>
"""

LOT_4[69] = """
<h4>Pourquoi ça marche</h4>
<p>Un GPT personnalisé porte en permanence ton prompt système : tu ne le réécris plus, et
toutes les réponses suivent les mêmes règles. Pour une tâche que tu fais chaque semaine —
corriger, générer des QCM, répondre à un client — c'est un gain de temps immédiat.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Nom : « Correcteur Assignments Langues »
Prompt système :
« Tu es correcteur de Assignments de 2e année PEP.
Corrige avec 3 critères :Exactitude, langue, structure.
Table de notation : [ta grille].
Rédige un commentaire court et encouraging pour l'étudiant. »</div>
<h4>Le piège à éviter</h4>
<div class="tip">Mets la <strong>grille de notation complète</strong> dans le prompt
système, pas seulement « corrige ». Sans critères explicites, chaque copie est notée
différemment et l'étudiant ne peut pas progresser.</div>
"""

LOT_4[70] = """
<h4>Pourquoi ça marche</h4>
<p>Un projet Claude regroupe tes documents et tes instructions. Toutes les conversations du
projet en héritent, sans que tu recopies le contexte. C'est le moyen le plus simple de
travailler sur un corpus : 20 PDF de cours, une fois uploadés, deviennent le contexte de
toutes tes questions.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Créer un projet « L3 — Contrôle continu 1 »
→ Uploader les 12 PDFs et les notes de cours.
→ Instructions : « Réponds uniquement à partir des documents du projet.
Cite le document et la page. Si la réponse n'y est pas, dis-le. »</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'instruction « réponds uniquement à partir des documents » est
<strong>indispensable</strong> : sans elle, Claude complète avec ses connaissances et tu ne
sais plus ce qui vient de ton cours. Vérifie toujours la citation avant de citer.</div>
"""

LOT_4[71] = """
<h4>Pourquoi ça marche</h4>
<p>Un bot Telegram utilise une API avec ton propre prompt système : les questions arrivent
partout, et les réponses suivent toujours les mêmes règles. Pour un groupe de travail ou
une petite structure, c'est un assistant disponible en permanence sans application
supplémentaire.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Telegram → BotFather → /newbot → tu reçois un token.
Le token ne se montre qu'une fois : note-le dans un gestionnaire de mots de passe.
Prompt système : « Réponds en 5 lignes, en français, cite tes sources. »</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le token <strong>est une clé</strong> : quiconque l'a peut utiliser ton
compte et te facturer. Garde-le hors du code public, ajoute des limites de dépenses dans le
tableau de bord de l'API, et ferme le service après l'examen.</div>
"""

LOT_4[72] = """
<h4>Pourquoi ça marche</h4>
<p>Un seul passage produit un texte cohérent mais non vérifié. Trois agents qui font trois
tâches différentes produisent un texte <strong>redondant et correct</strong> : la
redaction, la critique et la vérification des faits attrapent des erreurs qu'aucun des trois
n'aurait vues seul. C'est le principe de la double correction, appliqué au travail.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Agent 1 : rédige la section Introduction.
Agent 2 : critique ce texte (les objections d'un lecteur hostile).
Agent 3 : vérifie chaque affirmation et chaque source.
J'arbitre ensuite : je garde, je modifie, ou je supprime.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Tu restes l'arbitre : si tu ne vérifies pas, tu obtiens trois textes qui
se contredisent avec une assurance égale. Relis la critique et tranche — c'est là que se
fait la qualité.</div>
"""

LOT_4[73] = """
<h4>Pourquoi ça marche</h4>
<p>Envoyer 30 PDFs dans une conversation est long et imprécis. Un outil de type RAG les
indexe et répond <strong>avec la citation du passage exact</strong> : tu peux vérifier
immédiatement, et tu ne risques plus la réponse inventée.</p>
<h4>Comment faire</h4>
<div class="prompt-box">NotebookLM (gratuit) ou un projet Claude :
1) uploader les cours
2) poser une question
3) lire la citation
4) cliquer sur la source pour vérifier le passage original</div>
<h4>Le piège à éviter</h4>
<div class="warn">Vérifie <strong>la citation</strong>, pas seulement la réponse. Un RAG peut
citer un passage qui existe tout en résumant de travers. Et un PDF scanné n'est pas lu :
fais un OCR d'abord.</div>
"""

LOT_4[74] = """
<h4>Pourquoi ça marche</h4>
<p>Une recherche par mot-clé échoue dès que tu ne sais pas le mot exact. Un embedding
transforme chaque phrase en vecteur, et la recherche se fait <strong>par le sens</strong> :
« comment améliorer une note ? » trouve « comment augmenter une moyenne ».</p>
<h4>Comment faire</h4>
<div class="prompt-box">1) Rassembler les notes en un seul dossier
2) Générer les embeddings
3) Poser une question en langage naturel
4) Récupérer les 3-5 passages les plus proches</div>
<h4>Le piège à éviter</h4>
<div class="tip">Les embeddingsstonbridge ne comprennent pas le calcul : ils comparent des
sens, pas des nombres. Pour un tableau de notes, c'est un outil de <strong>recherche</strong>,
pas de calcul. Utilise-le pour retrouver une notion oubliée, pas pour faire une moyenne.</div>
"""

LOT_4[75] = """
<h4>Pourquoi ça marche</h4>
<p>Un prompt système long finit par être ignoré partiellement. Quand un format ou un style
revient sans cesse et qu'aucun prompt n'y suffit, l'entraînement du modèle sur tes propres
exemples le rend stable. C'est la solution <strong>de dernier recours</strong>.</p>
<h4>Quand le faire</h4>
<ul>
  <li>Tu as déjà essayé un prompt système détaillé et ça ne tient pas.</li>
  <li>Le format est stable sur des centaines d'exemples.</li>
  <li>Tes exemples sont propres, annotés et en quantité suffisante.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="warn">Le fine-tuning <strong>ne corrige pas une connaissance erronée</strong> et
coûte cher en temps. Avant de l'envisager, teste pendant deux semaines si des instructions
persistantes dans ton outil ne suffisent pas. Dans 95 % des cas d'un étudiant, elles
suffisent.</div>
"""

LOT_4[76] = """
<h4>Pourquoi ça marche</h4>
<p>Écrire une formule Excel ou Sheets à partir d'un besoin en français est exactement le
cas d'usage où l'IA est fiable : la syntaxe est précise, le test est immédiat. En
demandant l'explication de chaque partie, tu <strong>apprends</strong> la formule au lieu
de la recopier.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne-moi la formule qui calcule [X] si [Y] et [Z].
Explique chaque partie de la formule.
Donne un exemple avec des valeurs concrètes.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Fais <strong>toujours</strong> tester la formule sur trois cas : une
valeur normale, une valeur vide, et une valeur qui doit être exclue. Les erreurs
fréquentes sont les références qui se décalent quand on copie la formule vers le bas.</div>
"""

LOT_4[77] = """
<h4>Pourquoi ça marche</h4>
<p>Coller 10 000 lignes est inutile et coûteux. Un <strong>échantillon</strong> suffit pour que
l'IA repère les structure, les valeurs aberrantes et les incohérences de format, et qu'elle
suggère des graphiques pertinents. C'est le bon format pour une première exploration.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici un extrait de mon CSV (10 lignes) :
[colle les lignes, en-tête compris]
Trouve les tendances, les anomalies et les erreurs possibles.
Propose 3 graphiques pertinents et dis ce que chacun doit montrer.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Sur un échantillon, l'IA ne peut pas conclure : elle peut te dire « il y a
des doublons », pas « il y en a 3 % ». Et attention à ne jamais coller de données
personnelles (noms, notes nominatives) dans un outil en ligne : anonymise d'abord.</div>
"""

LOT_4[78] = """
<h4>Pourquoi ça marche</h4>
<p>Décrire un besoin en français et obtenir du SQL structuré est l'un des usages les plus
fiables. En demandant l'explication de chaque clause, tu vérifies que la requête fait ce que
tu crois, et tu peux la relire dans six mois.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris la requête SQL qui permet de [objectif].
Explique chaque clause.
Donne un exemple de résultat attendu avec 3 lignes.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une requête qui marche sur un jeu de test peut effacer des lignes en
production : <strong>toujours tester sur une copie</strong>, jamais sur la base réelle. Et
ajoute <code>LIMIT 10</code> au début tant que tu n'as pas vérifié le résultat.</div>
"""

LOT_4[79] = """
<h4>Pourquoi ça marche</h4>
<p>Nettoyer un CSV à la main prend des heures ; le demander à l'IA prend une minute. Le
vrai bénéfice n'est pas le code : c'est la <strong>liste des anomalies détectées</strong>, qui
révèle souvent un problème de saisie en amont — et qu'il faut corriger à la source.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un script pandas pour nettoyer ces colonnes :
- doublons
- dates mal formatées
- valeurs manquantes
- espaces en trop
Commente chaque étape en français, et dis ce que tu fais des lignes supprimées.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Vérifie le <strong>nombre de lignes avant et après</strong>. Un script qui
supprime 3 % des lignes sans te le dire est dangereux. Fais toujours <code>df.shape</code>
avant et après, et garde le fichier original intact.</div>
"""

LOT_4[80] = """
<h4>Pourquoi ça marche</h4>
<p>Un graphique n'est pas une décoration : c'est un argument. Demander le code
<strong>et</strong> l'interprétation attendue évite le graphiqueBeauty sans signification, et
la palette lisible évite les figures illisibles à l'impression.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne le code matplotlib pour ce graphique : [type]
Ajoute titres, légendes, axes et une palette lisible en niveaux de gris.
Explique comment interpréter le résultat, et ce qu'il ne prouve pas.</div>
<h4>Le piège à éviter</h4>
<div class="tip">La question « <strong>ce qu'il ne prouve pas</strong> » est celle qu'il faut
toujours poser. Un graphique qui montre une tendance n'établit pas une causalité, et le dire
dans la légende est un signe de rigueur.</div>
"""

LOT_4[81] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA fait des calculs qui <strong>ressemblent</strong> à des calculs justes : c'est le
danger. Un total faux avec un format impeccable passe inaperçu. Faire recalculer par un
second outil — ou par du vrai code — est le seul contrôle fiable.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Question : [ton calcul et ses résultats]
1) Refais ce calcul toi-même, pas de mémoire, montre les étapes
2) Donne le petit programme Python qui le vérifie
Si les deux résultats diffèrent, dis-le.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si l'IA se contredit entre deux réponses, <strong>c'est elle qui a tort</strong>,
et les deux réponses sont fausses. Le seul arbitrage fiable reste le calcul par un
programme : c'est court, c'est vérifiable, et ça marche à tous les coups.</div>
"""
