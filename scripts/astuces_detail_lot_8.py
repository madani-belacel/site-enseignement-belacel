#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 8 : les astuces 142 à 152.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Dernier lot : la catégorie « Méta-compétences & stratégie » (142 à 150)
puis les deux gestes bonus (151 et 152) qui ferment la page. L'astuce 150
« Créer son propre système d'astuces » ferme la boucle de tout le reste :
c'est celle qui fait le lien avec les 149 précédentes.
"""

LOT_8 = {}

LOT_8[142] = """
<h4>Pourquoi ça marche</h4>
<p>Une hésitation vient presque toujours de <strong>critères flous</strong> : on compare deux
options sans savoir ce qu'on optimise. Demander les questions qui clarifient les critères
les fait apparaître — et souvent, la décision devient évidente avant même les arguments.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">J'hésite entre [option A] et [option B].
Pose-moi 5 questions pour clarifier mes critères (poids de chacun).
Puis aide-moi à écrire une décision argumentée en 10 lignes,
avec le critère qui l'emporte et pourquoi.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne demande pas « laquelle est la meilleure ? » : la question est mal posée et
la réponse sera un avis. Demande « <strong>selon quel critère</strong> ? » — c'est la seule
forme qui produit une décision défendable devant quelqu'un d'autre.</div>
"""

LOT_8[143] = """
<h4>Pourquoi ça marche</h4>
<p>Sans revue, on répète les mêmes erreurs sans le savoir. Dix questions guidées
transforment une semaine en <strong>matériau</strong> : ce qui a marché se reproduit, ce qui a
bloqué se nomme, et la semaine suivante commence avec trois priorités au lieu de dix.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Guide-moi pour une revue hebdomadaire en 10 questions :
- ce qui a marché
- ce qui a bloqué
- ce que j'ai appris
- ce que je garde / ce que j’abandonne
- 3 priorités pour la semaine prochaine
Pose-les une par une.</div>
<h4>Le piège à éviter</h4>
<div class="tip">« Ce que j'ai appris » est la question la plus rentable et la plus
négligée. Réponds par des <strong>faits</strong> (« j'ai compris que la ligne était le
problème »), pas par des Loebres (« j'ai beaucoup appris »). Et « ce que j’abandonne » doit
contenir au moins un élément : une semaine sans rien abandonner est un mois perdu.</div>
"""

LOT_8[144] = """
<h4>Pourquoi ça marche</h4>
<p>Le moment le plus difficile n'est pas le travail, c'est le <strong>passage à l'acte</strong>.
Un rituel court et identique chaque jour supprime la décision : on ne se demande plus
« par quoi commencer », on commence. Trois actions, cinq minutes, c'est la limite — au-delà,
le rituel est(reporté.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Aide-moi à créer un rituel de 5 minutes avant de travailler sur [tâche].
3 actions simples, dans l'ordre, sans écran si possible.
La première doit être physique (ouvrir, poser, écrire),
sinon le rituel saute.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un rituel qui contient un écran démarre sur une autre application, et tu
fais autre chose. Si tu ne peux pas travailler sans écran (écran partagé, machine de la
salle), remplace-le par une action physique : ouvrir le cahier, écrire la date.</div>
"""

LOT_8[145] = """
<h4>Pourquoi ça marche</h4>
<p>La procrastination n'est pas de la paresse : c'est une <strong>réponse à une cause
précise</strong> — peur de mal faire, ennui, flou, fatigue. Identifier la cause change la
solution. Contre l'ennui, on découpe ; contre la peur, on commence par un essai sans importance.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je procrastine sur [tâche].
Pose-moi 3 questions pour identifier la cause (peur, ennui, flou, fatigue).
Puis propose 3 stratégies concrètes adaptées à MA cause,
pas des conseils génériques.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Les conseils génériques (« fais un Pomodoro », « commence par 5 minutes »)
échouent précisément parce qu'ils ignorent la cause. Si c'est la peur, compter le temps
aggrave le malaise : il faut d'abord réduire l'enjeu, pas la durée.</div>
"""

LOT_8[146] = """
<h4>Pourquoi ça marche</h4>
<p>Mélanger fait, opinion et hypothèse est la cause principale des discussions qui ne
progressent pas. Trier chaque affirmation force à nommer ce qui est <strong>vérifiable</strong> —
et ce qui ne l'est pas devient un simple point de vue, pas un fait.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Relis ce texte. Classe chaque affirmation en :
- fait vérifiable
- opinion
- hypothèse
Signale ce qui manque pour trancher.
Pour chaque fait, dis quelle source permettrait de le vérifier.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une affirmation à laquelle l'IA trouve une source n'est pas forcément
vérifiée : elle peut avoir mal lu l'article. Fais toi-même la recherche avant de traiter
quelque chose comme un fait établi.</div>
"""

LOT_8[147] = """
<h4>Pourquoi ça marche</h4>
<p>Un sujet mal connu donne une sensation de « tout est important ». En demandant
explicitement <strong>5 concepts, 5 acteurs, 3 débats, 3 ressources</strong>, on impose un
découpage : on sait ce qui est central, et surtout ce qui ne l'est pas.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Sujet : [X]. Donne :
- 5 concepts clés
- 5 acteurs ou auteurs majeurs
- 3 débats du domaine
- 3 ressources pour aller plus loin
- 3 questions à creuser</div>
<h4>Le piège à éviter</h4>
<div class="tip">« 5 ressources » ne veut pas dire « 5 articles de blog » : demande des
<strong>types de sources différentes</strong> (un manuel, un article de revue, une
thèse) et vérifie qu'ils existent. Les « acteurs majeurs » sont souvent inventés si le
domaine est rare : exige le nom complet et l'année.</div>
"""

LOT_8[148] = """
<h4>Pourquoi ça marche</h4>
<p>Apprendre sans structure, c'est accumuler sans consolider. Un plan en paliers avec
<strong>auto-évaluation régulière</strong> est ce qui distingue l'apprentissage qui tient
dans six mois de celui qu'on a oublié en trois semaines. La contrainte « 1h/jour » rend le
plan exécutable.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je veux apprendre [compétence] en 30 jours, 1h/jour.
Donne un plan avec : progression par paliers, exercices pratiques,
auto-évaluations à J7, J14, J21, J30, et ressources gratuites prioritaires.
Décris la production attendue de chaque séance (pas seulement le thème).</div>
<h4>Le piège à éviter</h4>
<div class="warn">« Apprendre » sans <strong>produire</strong> ne marche pas : lire sur
l'IA, regarder une vidéo ou refaire un exercice qu'on maîtrisait déjà, ce n'est pas
progresser. Chaque séance doit se terminer par quelque chose de nouveau que tu ne savais
pas faire au départ.</div>
"""

LOT_8[149] = """
<h4>Pourquoi ça marche</h4>
<p>Faire défendre sa thèse par une IA prépare l'objection <strong>avant</strong> l'oral.
C'est la préparation la plus rentable quand on a un jury : on découvre la contre-argumentation
dans un environnement où l'on peut recommencer dix fois.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Débat : [sujet / ta thèse].
Joue deux rôles alternativement : défenseur, puis critique.
Après 3 échanges, résume les points de convergence et de divergence.
Puis donne ta synthèse nuancée en 5 lignes.
Sois exigeant : ne m'accorde pas un point facile.</div>
<h4>Le piège à éviter</h4>
<div class="tip">L'IA en mode « critique » reste <strong>polie</strong> : elle manque
volontairement les objections évite. Demande explicitement « les 3 objections les plus
fortes, y compris celles qui remettraient ma thèse en cause ». Et cherche les sources
réelles derrière chaque objection.</div>
"""

LOT_8[150] = """
<h4>Pourquoi ça marche</h4>
<p>Une bibliothèque de prompts se construit <strong>par usage</strong>, pas par théorie.
Demander à l'IA de synthétiser ce que vous avez déjà fait — vos prompts, vos outils, vos
règles — produit une fiche en dix minutes au lieu de trois heures de tri.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Aide-moi à créer mon système personnel d'usage de l'IA :
- mes 10 prompts les plus utiles
- mes 5 outils préférés
- mes 3 règles personnelles
- mon rituel hebdomadaire de mise à jour
Format : fiche d'une page, prête à imprimer.
Demande-moi d'abord mes prompts existants.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA ne connaît pas vos usages : <strong>collez-lui d'abord vos prompts
existants</strong> (astuce 18), sinon elle vous fera un système générique qui ne vous ressemble
pas. Et la mise à jour est la partie qu'on saute : sans mise à jour mensuelle, la fiche
devient fausse au bout de deux mois.</div>
"""

LOT_8[151] = """
<h4>Pourquoi ça marche</h4>
<p>On ne relit pas 30 pages dans le bus, mais on <strong>écoute</strong> 25 minutes en se
déplaçant. C'est le geste qui change le plus le temps de révision réel, parce qu'il
supprime la friction du temps et du lieu.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Ce texte :
[colle ton texte]
Transforme-le en audio MP3, vitesse normale, sans commentaire ni ajout.
Puis résume-le en 5 points que je pourrai noter au crayon.</div>
<h4>Le piège à éviter</h4>
<div class="tip">L'audio ne sert pas à <strong>apprendre une définition</strong> : on retient
mal un mot nouveau entendu mais pas vu. Écoute pour répéter et mémoriser la structure ;
lis pour apprendre le vocabulaire. Et réécoute le résumé écrit, pas seulement l'audio.</div>
"""

LOT_8[152] = """
<h4>Pourquoi ça marche</h4>
<p>Taper est lent quand les idées ne sont pas encore formées : on bloque devant le clavier.
Dicter supprime cette friction — on parle, l'IA met en forme. On écrit trois fois plus vite,
et surtout on ne perd plus l'idée au moment de la formuler.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici ce que j'ai dicté, mal ponctué :
[texte brut]
Récris-le proprement, garde mes mots et mon sens, ne rajoute aucune idée.
Signale si une phrase n'est pas claire.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La dictée se trompe sur les <strong>noms propres, les termes techniques et
les nombres</strong> — et personne ne s'en rend compte. Relis toujours avant d'envoyer : un
nom de personne ou une date mal dictés fausse tout le travail sans qu'on le voie.</div>
"""
