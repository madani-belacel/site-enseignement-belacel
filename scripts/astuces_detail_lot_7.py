#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 7 : les astuces 122 à 141.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Trois blocs : business et freelance (122 à 130), enseignement (131 à 140),
puis l'ouverture du bloc productivité (141).

Le bloc enseignement est le plus important pour l'usage réel du module :
il sépare ce que l'IA peut préparer (structure, variété, grille) de ce qu'elle
ne peut pas juger (la copies d'un élève, l'évaluation d'un travail réel).
"""

LOT_7 = {}

LOT_7[122] = """
<h4>Pourquoi ça marche</h4>
<p>Le blocage le plus fréquent en communication, ce n'est pas l'écriture, c'est
<strong>l'absence d'idées</strong>. Trente idées en une commande lèvent le blocage ; les
formats variés évitent la repetition, et le tableau rend le calendrier directement
utilisable.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je suis [métier] et je m'adresse à [public].
Donne 20 idées de posts pour 1 mois.
Format : | Jour | Format | Titre | Angle |
Varie les formats : story, conseil, coulisses, opinion, tutoriel.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une ideegeneree ne vaut pas une idée vécue. Prends les 5 premières comme
<strong>structure</strong> et remplace-les par des faits que toi seul as : un client, un
échec, un détail observé. C'est ce qui rend le contenu crédible.</div>
"""

LOT_7[123] = """
<h4>Pourquoi ça marche</h4>
<p>Un rendez-vous client se prépare en trois choses : des questions qui montrent que tu as
compris son besoin, des réponses aux objections, et un signal qui te dit quand proposer. Les
avoir par écrit évite les trois blancs de cinq minutes.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">J'ai un rendez-vous avec [type de client] sur [sujet].
Prépare :
- 5 questions à poser
- 3 objections probables + réponses
- 3 signaux d'achat à repérer
- la phrase de conclusion à utiliser</div>
<h4>Le piège à éviter</h4>
<div class="tip">Les questions préparées trop arrêtées sonnent faux. Prépare les <strong>axes</strong>
(problème actuel, budget, échéance, décisionnel) plutôt que les phrases exactes : tu
reformules avec tes mots, et l'entretien reste naturel.</div>
"""

LOT_7[124] = """
<h4>Pourquoi ça marche</h4>
<p>Un email difficile — retard, reclamation, rupture — se rate sur la structure, pas sur le
ton. Imposer <strong>objet, contexte en 2 phrases, demande précise, prochaine étape</strong>
et une limite de mots supprime les paragraphes défensifs qui agacent le destinataire.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un email pour [situation délicate].
Ton : respectueux, factuel, sans excuses excessives.
Structure : objet clair, contexte en 2 phrases, demande précise, prochaine étape.
Maximum 150 mots.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Supprime toute excuse : « je suis désolé, je n'ai pas eu le temps, je n'ai
pas vu… » transforme un retard en faute personnelle. Dis ce qui s'est passé, ce que tu
proposes, et ce que tu attends — trois phrases, pas plus.</div>
"""

LOT_7[125] = """
<h4>Pourquoi ça marche</h4>
<p>Un contrat se lit enCherchant les <strong>obligations, les dates, et ce qui manque</strong>.
C'est une tâche de repérage, adaptée à l'IA. La méthode en dix points évite l'oubli, et le
rappel final évite l'erreur de foi aveugle.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici un contrat. Résume en 10 points :
- obligations de chaque partie
- dates clés
- clauses à risque
- ce qui manque
Ce n'est pas un avis juridique : signale les points à vérifier avec un avocat.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une clause peut être <strong>absente</strong> sans que l'IA le signale : elle
ne cherche que ce qu'on lui demande de chercher. Ajoute « cite la clause exacte et son
article pour chaque point à risque » — sans la citation, tu ne peux rien vérifier.</div>
"""

LOT_7[126] = """
<h4>Pourquoi ça marche</h4>
<p>Une étude de marché demande quatre données : la taille, les acteurs, les tendances, les
risques. L'IA donne une <strong>structure</strong> immédiate, ce qui est exactement ce qui
manque quand on démarre. Les chiffres, eux, demandent une vérification.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Marché : [secteur] dans [pays].
Donne : taille approximative, 5 acteurs principaux, tendances 2024–2025,
3 opportunités, 3 menaces.
Signale les sources et les incertitudes.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les <strong>chiffres de marché</strong> sont le point le plus sensible : ils
sortent souvent d'un rapport marketing verbeux, et les sources citées sont parfois
inaccessibles. Ne cite un chiffre que si tu as ouvert la source. Écris « [à vérifier : X] »
plutôt que de recopier un chiffre invérifiable.</div>
"""

LOT_7[127] = """
<h4>Pourquoi ça marche</h4>
<p>Le business plan d'une page est un <strong>exercice de synthèse</strong> : chaque section
se déduit de la précédente. L'ordre imposé (problème → solution → marché → modèle → coûts →
prévisions → risques) force à cette logique et évite de commencer par les coûts.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Rédige un business plan d'une page :
problème, solution, marché cible, modèle économique, coûts principaux,
prévisions à 12 mois (fourchettes, pas de faux chiffres précis), risques principaux.
Si une information manque, écris [à compléter] — n'invente aucun chiffre.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un plan avec des « fourchettes » entièrement inventées est pire qu'un plan
avec des trous. Demande explicitement les fourchettes <em>et</em> la base de calcul : une
fourchette qui sort de nulle part n'est pas une prévision, c'est une invention bien habillée.</div>
"""

LOT_7[128] = """
<h4>Pourquoi ça marche</h4>
<p>Une proposition commerciale répond à une seule question du client : <strong>« pourquoi
toi ? »</strong>. Commencer par rappeler le besoin, pas par présenter son service, est ce qui
distingue une proposition qui obtient une réponse d'une brochure.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Structure une proposition commerciale :
1) rappel du besoin
2) ma compréhension du problème
3) solution proposée
4) planning
5) tarif
6) prochaines étapes
Ton : confiant, pas arrogant.
Client : [qui, quel secteur, quel niveau de maturité].</div>
<h4>Le piège à éviter</h4>
<div class="tip">Le point 2 est le plus important et le plus souvent bâclé : c'est là que le
client décide s'il continue. Si le besoin est mal reformulé, tout le reste est ignoré.
Relis-le à voix haute : « est-ce que c'est bien <em>mon</em> problème ? »</div>
"""

LOT_7[129] = """
<h4>Pourquoi ça marche</h4>
<p>Préparer un entretien, c'est surtout préparer les <strong>réponses aux questions
inattendues</strong>. Le feedback en trois points après chaque réponse est ce qui rend
l'exercice utile : il montre l'écart entre ce que tu voulais dire et ce qui a été entendu.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu es recruteur pour un poste de [poste].
Pose-moi 10 questions progressives.
Après chaque réponse : feedback en 3 points (ce qui va, ce qui manque, comment améliorer).
Note finale sur 10 et 3 conseils prioritaires.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le feedback est <strong>flatteur</strong> par défaut : l'IA note rarement
moins de 7/10. Prends ses critiques au sérieux quand même — ce sont les « ce qui manque »
qui comptent, pas la note. Et ne lui demande jamais de simuler un entretien à ta place
en entretien réel.</div>
"""

LOT_7[130] = """
<h4>Pourquoi ça marche</h4>
<p>Un CV est filtré par <strong>mots-clés</strong> et par <strong>réussites chiffrées</strong>.
Les mettre en regard de l'offre révèle les écarts avant l'envoi, et c'est la seule façon de
savoir qu'un CV « parfait » sur le papier ne correspond pas à l'offre.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mon CV et l'offre d'emploi.
Propose :
- les 5 compétences à mettre en avant
- les formulations à ajuster (mots-clés de l'offre)
- ce qu'il faut retirer
- les 3 réalisations à ajouter si possible
Ne mens pas : reformule uniquement ce que j'ai déjà fait.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'écart le plus courant est une <strong>compétence exagérée</strong> : l'IA te
suggère d'écrire « gestion de projet » parce que c'est dans l'offre, alors que tu n'as fait
que participer. Ne le fais pas : en entretien, la question de fond arrive en dix minutes.</div>
"""

LOT_7[131] = """
<h4>Pourquoi ça marche</h4>
<p>Un plan de cours demande cinq éléments articulés entre eux. L'IA les produit
<strong>dans le bon ordre</strong> et garantit qu'aucun n'est oublié — c'est l'avantage le
plus immédiat, avant même la qualité du contenu.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Cours : [titre], niveau [X], durée [Y] heures.
Donne : objectifs pédagogiques, plan en séances, activités par séance,
évaluation formative et finale, ressources recommandées.
Précise pour chaque séance : durée, objectif, activité, production attendue.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les « objectifs » doivent être <strong>vérifiables</strong> : « comprendre »
n'est pas un objectif, « être capable d'analyser un texte et de l'argumenter » en est un. Et
garde la durée : un plan de 4 heures qu'il faut 12 heures pour faire est un plan qu'on
n'IRA pas jusqu'au bout.</div>
"""

LOT_7[132] = """
<h4>Pourquoi ça marche</h4>
<p>Une seule activité pour toute une classe est injuste : les élèves en difficulté décrochent
et les avancés s'ennuient. La <strong>différenciation à trois niveaux</strong> avec le même
objectif évite l'effet de cours paresseux : ce qui change, c'est la complexité, pas la
cible.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici une activité. Adapte-la pour :
- élèves en difficulté
- élèves moyens
- élèves avancés
Mêmes objectifs, niveaux de complexité différents.
Pour chaque version, dis ce que l'élève doit produire.</div>
<h4>Le piège à éviter</h4>
<div class="tip">La version « difficulté » ne doit pas être un <strong> exercice plus court</strong> :
c'est un exercice plus guidé, avec une étape decomposée en plus. Sinon l'élève en difficulté
fait moins de choses et apprend moins.</div>
"""

LOT_7[133] = """
<h4>Pourquoi ça marche</h4>
<p>Générer des QCM demande du volume et de l'équilibre : c'est un travail répétitif où la
variété compte. Imposer la <strong>répartition par difficulté</strong> et l'explication de
chaque réponse produit un QCM utilisable comme auto-évaluation.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Crée 20 QCM sur [sujet].
Format : question + 4 propositions + bonne réponse + explication.
Équilibre les niveaux : 7 faciles, 7 moyens, 6 difficiles.
Évite les distracteurs absurds : chaque mauvaise proposition doit être
plausible pour un élève qui a mal compris.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Trois erreurs classiques : des distracteurs <strong>absurdes</strong>
(facile à deviner), la bonne réponse toujours en position A, et une explication qui
« justifie » une réponse fausse. Fais randomiser les positions, et vérifie la réponse en
la cherchant toi-même dans le cours avant de publier.</div>
"""

LOT_7[134] = """
<h4>Pourquoi ça marche</h4>
<p>Une grille d'évaluation sépare <strong>les critères</strong> des <strong>niveaux</strong>.
C'est la seule façon d'avoir des notes comparables entre deux copies : sans niveaux
décrits, deux enseignants notent différemment, et l'étudiant n'apprend rien de la note.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Crée une grille d'évaluation pour [type de travail].
Format : critère | indicateur | niveau 1 | niveau 2 | niveau 3 | pondération.
Total sur 20.
Décris les niveaux en actions observables, pas en adjectifs
(« ne cite aucune source » plutôt que « travail superficiel »).</div>
<h4>Le piège à éviter</h4>
<div class="tip">Décrire les niveaux avec des <strong>adjectifs</strong> (« moyen », « correct »,
« bon ») est la cause numéro un des notes incohérentes. Décris ce que l'élève <em>a fait</em> :
« 2 sources citées et vérifiées » contre « aucune source », c'est vérifiable par n'importe qui.</div>
"""

LOT_7[135] = """
<h4>Pourquoi ça marche</h4>
<p>Un feedback qui dit « bien joué » n'apprend rien. Un feedback structuré en <strong>3 points
précis + 3 axes avec exemples + 1 conseil prioritaire</strong> est lu, compris et utilisé —
parce qu'il dit où et comment s'améliorer, pas seulement ce qui a manqué.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici la copie d'un élève. Rédige un feedback :
- 3 points positifs précis (cite la phrase exacte de la copie)
- 3 axes d'amélioration avec un exemple avant / après
- 1 conseil prioritaire
Ton : bienveillant mais exigeant.
Maximum 200 mots.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le risque n'est pas le ton, c'est l'<strong>anonymat</strong> : un feedback
générique (« bon travail, continue ») s'applique à n'importe quel élève. Citer la phrase
exacte est ce qui rend le message personnel — et vérifiable, donc honnête.</div>
"""

LOT_7[136] = """
<h4>Pourquoi ça marche</h4>
<p>Un escape game est un <strong>scénario à contraintes</strong> : un récit, des énigmes, un
temps imparti. L'IA produit cette architecture en une commande, ce qui prendrait une heure
à construire à la main.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Conçois un escape game pédagogique sur [sujet] pour [niveau].
Structure : scénario, 5 énigmes liées au cours, matériel nécessaire,
durée, solution de chaque énigme.
Chaque énigme doit tester une notion précise du cours, et sa solution
doit être vérifiable par l'enseignant en moins de 2 minutes.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le test est là : si l'énigme exige une connaissance que le cours n'a pas
encore vue, la séance est perdue. Vérifie chaque énigme contre ta progression réelle, et
prévoyoi une <strong>solution de secours écrite</strong> pour chaque — un groupe bloqué est
toujours possible.</div>
"""

LOT_7[137] = """
<h4>Pourquoi ça marche</h4>
<p>Transformer un écrit en oral demande <strong>des transitions</strong> : c'est là que les
deux écritures diffèrent. L'IA produit une accroche et des transitions, et le bloc
« 5 questions au public » évite le moment gênant du silence à la fin.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Transforme ce cours en présentation orale de 15 minutes.
Structure : accroche, plan en 3 parties, transitions, conclusion.
Ajoute 5 questions à poser au public.
150 mots par partie maximum. Signale si une partie dépasse le temps imparti.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Compte les mots à voix haute : <strong>150 mots par minute</strong>. Un plan
de 15 minutes = 2 200 mots, pas 4 000. L'erreur classique est un texte écrit trop riche qu'on
lit à toute vitesse : le public ne retient alors plus rien.</div>
"""

LOT_7[138] = """
<h4>Pourquoi ça marche</h4>
<p>Une fiche méthode en <strong>5 étapes + 3 erreurs + 1 phrase à retenir</strong> est le
format le plus efficace qui soit pour un élève : les étapes lui donnent une procédure, les
erreurs lui donnent la raison d'y faire attention, et la phrase finale lui donne un repère
mémorable.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Crée une fiche méthode « Comment [compétence] » pour des élèves de [niveau].
Format : 5 étapes, 1 exemple, 3 erreurs à éviter, 1 phrase à retenir.
Écris à la 2e personne (« tu places », « tu relis »), en phrases courtes.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Les étapes doivent être <strong>vérifiables à la fin</strong> : « relis ta
copie » est une étape, «sois rigoureux » n'en est pas une. Teste la fiche en la suivant
toi-même : si tu ne peux pas savoir si une étape est faite, elle est mal écrite.</div>
"""

LOT_7[139] = """
<h4>Pourquoi ça marche</h4>
<p>Corriger trente copies à la main fatigue : l'exigence baisse au bout de la vingtième. La
méthode en deux temps — <strong>d'abord la grille, ensuite l'application</strong> — garantit
la même exigence du début à la fin, et la grille sert ensuite aux élèves pour s'auto-évaluer.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Étape 1 : rédige la grille d'évaluation de ce devoir,
avec des critères et des niveaux observables.
Étape 2 : tu appliqueras cette grille à chaque copie, sans l'expliquer à chaque fois.
Pour chaque copie, je veux : grille complétée + 3 points positifs + 1 conseil prioritaire.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Sans la grille d'abord, l'IA notera différemment chaque copie, et tu n'auras
pas de notes comparables. Et <strong>relis toujours manuellement</strong> : sur trente copies,
l'IA se tromperait au moins une fois sur un élément de la grille, et ce sera celle de
l'élève qui compte le plus.</div>
"""

LOT_7[140] = """
<h4>Pourquoi ça marche</h4>
<p>Un projet interdisciplinaire est difficile à concevoir parce qu'il faut <strong>aligner deux
disciplines sur une même problématique</strong>, pas les juxtaposer. Imposer « problématique »
comme premier élément empêche le projet de dégénérer en deux travaux collés.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Conçois un projet qui relie [discipline 1] et [discipline 2] pour [niveau].
Inclus : problématique commune, étapes, livrables, évaluation, durée.
La problématique doit être traiteable avec les deux disciplines,
pas l'une puis l'autre.
Propose 3 projets différents.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Attention au projet « à côté » : discipline 1 traitée dans la première moitié,
discipline 2 dans la seconde, sans lien. Demande explicitement « à quel moment les deux
disciplines sont-elles utilisées <strong>ensemble</strong> ? » — si tu ne trouves pas la réponse,
le projet est à refaire.</div>
"""

LOT_7[141] = """
<h4>Pourquoi ça marche</h4>
<p>Une tâche paralysante est paralysante parce qu'elle n'a pas de <strong>premier pas
physique</strong>. En découpant en micro-étapes de quinze minutes et en donnant le premier
geste, on supprime la part de la tâche qui demande de la réflexion — c'est là qu'on bloque.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je dois [tâche qui me bloque].
Décompose-la en micro-étapes de 15 minutes maximum.
Pour chaque étape : action concrète + premier geste physique.
Commence par la plus simple et donne-moi le geste à faire maintenant.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Le découpage doit rester <strong>physique</strong> : « ouvrir le document »
est une action, « réfléchir au plan » n'en est pas une. Si une étape ne peut pas être
commencée sans décision, elle est trop grande — coupe-la encore.</div>
"""
