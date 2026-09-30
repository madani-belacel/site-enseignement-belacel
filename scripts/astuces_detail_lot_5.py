#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 5 : les astuces 82 à 101.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Ce lot passe de l'{outillage} créatif à l'apprentissage, puis à la
sécurité et aux premières API. Les explications signalent les endroits où
l'IA est le mauvais outil (l'astuce 85, la carte mentale) et les endroits où
elle est fiable (le code, la relecture).
"""

LOT_5 = {}

LOT_5[82] = """
<h4>Pourquoi ça marche</h4>
<p>Le blocage numéro un avec Python, c'est l'installation : les erreurs de version, les
bibliothèques manquantes, les chemins. Google Colab supprime complètement cette étape — le
code s'exécute dans le navigateur, sur une machine distante, avec les bibliothèques déjà
installées. Tu testes une idée en trente secondes.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Écris un script Python pour analyser un fichier CSV.
Ajoute en commentaire en haut :
1) le lien pour importer pandas
2) une ligne pour installer ce qui manque (pip)
Je le collerai dans Google Colab.</div>
<p>Colab : <code>colab.research.google.com</code> → nouveau notebook → coller → lecture.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Ton travail <strong>disparaît</strong> quand tu fermes l'onglet. Exporte
le fichier <code>.ipynb</code> avant, ou copie le code dans un fichier local. Et vérifie
que le GPU est activé (Runtime → Change runtime type) si tu fais du traitement lourd.</div>
"""

LOT_5[83] = """
<h4>Pourquoi ça marche</h4>
<p>Demander « comment réussir ? » produit des généralités. Demander <strong>« comment
échouer ? »</strong> produit du concret, parce que les causes d'échec sont connues et
nominables. En inversant chaque cause, on obtient une bonne pratique justifiée au lieu
d'un slogan.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Comment garantir l'échec total de ce projet ?
Liste 10 causes d'échec réalistes.
Puis inverse chaque cause pour obtenir 10 bonnes pratiques.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Les causes listées ne sont pas spécifiques à <em>ton</em> projet. Ajoute
« Voici mon projet : [description en 3 lignes] » avant de demander. Sans ça, tu obtiens
une liste générique applicable à n'importe quoi.</div>
"""

LOT_5[84] = """
<h4>Pourquoi ça marche</h4>
<p>Une contrainte forte produit une écriture personnelle : l'IA ne peut pas sortir son texte
par défaut. « Pas de cliché » et « une seule métaphore filée » obligent à construire, et le
résultat est souvent meilleur que ce qu'on aurait écrit librement.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un texte de 100 mots sur [sujet moderne] dans le style de
Victor Hugo. Contraintes : pas de cliché, une seule métaphore filée, chute surprenante.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le style imité est une <strong>approximation</strong>, pas une
imitation. Si l'exercice demande de citer un auteur, cite-le toi-même dans le texte et
précise que l'IA a servi de brouillon : c'est la seule façon d'être honnête et de ne pas
produire un texte qui « sonne faux » à la lecture.</div>
"""

LOT_5[85] = """
<h4>Pourquoi ça marche</h4>
<p>Une carte mentale en texte hiérarchique sert surtout de <strong>plan de structuration</strong> :
tu obtiens l'arborescence d'un sujet en une commande, et tu vois immédiatement ce qui manque
comme branche. C'est utile avant de rédiger.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne une carte mentale en texte hiérarchique avec 3 niveaux.
Format :
- Thème central
  - Branche 1
    - Sous-branche
    - Sous-branche
  - Branche 2</div>
<h4>Le piège à éviter</h4>
<div class="tip">N'utilise pas le résultat comme carte mentale finale : la hiérarchie
proposée par l'IA est <strong>logique, pas mnémotechnique</strong>. Elle ne tient pas compte
de ton fonctionnement visuel. Sers-t-en pour vérifier que tu n'as rien oublié, puis fais ta
vraie carte à la main.</div>
"""

LOT_5[86] = """
<h4>Pourquoi ça marche</h4>
<p>Le tableau temps / visuel / texte est le format le plus efficace pour un script vidéo :
il force à tenir un <strong>calage</strong> entre ce qu'on voit et ce qu'on dit. La colonne
« Visuel » empêche le scénario de devenir un texte récité face à une caméra vide.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un script vidéo de 2 minutes sur [sujet].
Format :
| Temps | Visuel | Texte à dire |
| 0:00 | ... | ... |
Ton : dynamique mais clair.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Compte les mots à voix haute : <strong>150 mots par minute</strong> en
français. Deux minutes = 300 mots maximum. Si ton script en fait 500, tu vas accélérer ou
couper, et ça s'entend.</div>
"""

LOT_5[87] = """
<h4>Pourquoi ça marche</h4>
<p>Un persona transforme un public abstrait en <strong>personne précise</strong> : dès que
l'IA écrit « Étienne, 34 ans, cadre, sceptique », le message et les arguments deviennent
concrets. On ne parle plus « au marché », on parle à quelqu'un.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Crée 3 personas pour [produit/service]. Pour chacun :
- âge, profession, situation
- douleurs
- désirs
- objections
- canaux préférés
- message qui les convainc</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les personas sont des <strong>hypothèses</strong>, pas des données. Si tu
as une vraie enquête, ses résultats priment sur les personas inventés. Et n'utilise jamais
un persona pour décrire un groupe minoritaire : il sera systématiquement caricatural.</div>
"""

LOT_5[88] = """
<h4>Pourquoi ça marche</h4>
<p>Un sujet seul donne une image moyenne. Décomposer en <strong>style, composition,
lumière, objectif, palette</strong> donne un résultat contrôlable et modifiable champ par
champ : tu changes un seul élément à la fois au lieu de tout recommencer.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Sujet : [X]
Style : [peinture / photo / 3D / croquis]
Composition : [centrée / règle des tiers / contre-plongée]
Lumière : [naturelle / studio / contre-jour]
Objectif : [publicité / pédagogique / documentation]
Format : [carré / 16:9 / vertical]
Palette : [sèche / chaude / monochrome]</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les systèmes qui génèrent des images sont encorelicted sur les <strong>textes
dans l'image</strong> : ils écrivent n'importe quoi. Ajoute le texte après coup, dans un outil
d'édition, et vérifie chaque lettre.</div>
"""

LOT_5[89] = """
<h4>Pourquoi ça marche</h4>
<p>Découper une vidéo en plans avant de filmer évite l'erreur la plus fréquente : un plan trop
long ou deux plans de suite qui se ressemblent. La colonne <strong>émotion</strong> force à
varier l'intention, pas seulement l'image.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Décris 6 plans pour une vidéo de 30 secondes.
Pour chaque plan : cadrage, action, texte à l'écran, émotion recherchée.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Vérifie que l'<strong>émotion change</strong> d'un plan à l'autre : six plans
tous « informatifs » donnent une vidéo plate. Si deux plansJobs demandent la même émotion,
fusionne-les — il ne reste que cinq plans utiles.</div>
"""

LOT_5[90] = """
<h4>Pourquoi ça marche</h4>
<p>Un article n'est pas réutilisable tel quel sur d'autres plateformes : le format décide de
ce qui passe. En transformant depuis un texte unique, tu gardes le message cohérent partout
au lieu de réécrire cinq versions qui se contredisent.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Transforme cet article en :
1) post LinkedIn (150 mots)
2) tweet (280 caractères)
3) script TikTok (30 secondes)
4) newsletter (200 mots)
Garde le message principal, adapte le ton et le format.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Vérifie les règles de chaque plateforme : LinkedIn limite à 3 000 caractères,
TikTok à une minute, X à 280. Et n'y colle jamais une donnée personnelle que tu aurais
anonymisée dans l'article.</div>
"""

LOT_5[91] = """
<h4>Pourquoi ça marche</h4>
<p>Les flashcards sont efficaces quand elles sollicitent la <strong>rappel actif</strong> : pas
la relecture, mais l'effort de retrouver la réponse. Générées automatiquement, elles couvrent
le chapitre entier en quelques minutes — c'est le meilleur rapport temps / acquisition.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Génère 20 cartes question/réponse à partir de ce chapitre.
Format :
Q : ... / R : ...
Classe-les par difficulté croissante.
Évite les cartes trop longues : une idée par carte.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une carte dont la réponse est une phrase entière ne fonctionne pas : tu
reconnais le début et tu te crois savoir. Limite la réponse à <strong>5 mots maximum</strong>,
et reformule les questions du chapitre en questions (« Comment s'appelle… ? »).</div>
"""

LOT_5[92] = """
<h4>Pourquoi ça marche</h4>
<p>La méthode Feynman tient en une idée : si tu n'arrives pas à l'expliquer simplement,
c'est que tu n'as pas compris. En réexpliquant toi-même et en te faisant corriger, tu
<strong>révèles ton angle mort</strong> — ce que la lecture passive ne fait jamais.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Explique-moi [concept] simplement.
Ensuite, je te le réexplique.
Corrige mes erreurs, simplifie ce qui reste flou, et propose une analogie.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Ne recopie <strong>jamais</strong> l'explication de l'IA à la place de la
tienne. Si tu n'as pas écrit le premier jet toi-même, la méthode ne t'apprend rien : tu
mesures la mémoire de l'IA, pas la tienne.</div>
"""

LOT_5[93] = """
<h4>Pourquoi ça marche</h4>
<p>Un QCM à difficulté fixe teste ce que tu sais déjà. Un quiz adaptatif trouve
<strong>exactement ta limite</strong> : il monte quand tu réussis, il redescend quand tu
échoues. Dix questions bien placées valent mieux que trente au hasard.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Pose-moi 5 questions de difficulté croissante sur [sujet].
Adapte la question suivante selon ma réponse précédente.
À la fin, donne-moi un score et 3 conseils ciblés.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Vérifie chaque bonne réponse avec ton cours : un quiz peut avoir une
réponse attendue fausse, et tu retiens alors une erreur. Signale à l'IA : « la réponse B
est-elle vraiment correcte ? Justifie avec le cours. »</div>
"""

LOT_5[94] = """
<h4>Pourquoi ça marche</h4>
<p>Un plan d'étude sans <strong>révisions espacées</strong> est inutile : on relit trois fois
le soir et on oublie tout une semaine après. En demandant explicitement des rappels espacés
et un jour de repos, on obtient un planning qui tient.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Crée un planning sur 14 jours, 1h/jour, pour apprendre [sujet].
Inclus : objectifs quotidiens, révisions espacées, un jour de repos,
et une auto-évaluation finale.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Le jour de repos n'est pas facultatif : c'est lui qui consolide. Et un
planning de 14 jours ne suffit pas pour un examen dans trois mois — répète le cycle, en
allongeant les intervalles entre les révisions.</div>
"""

LOT_5[95] = """
<h4>Pourquoi ça marche</h4>
<p>Des erreurs dispersées n'apprennent rien. Ce qui apprend, c'est le <strong>schéma
commun</strong> derrière elles. En donnant ta liste d'erreurs, tu obtiens un diagnostic
unique, trois exercices ciblés, et une liste de vérifications à faire avant de rendre — c'est
exactement ce qui manque à une auto-correction.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mes erreurs : [liste]
Identifie le pattern commun.
Donne 3 exercices ciblés pour corriger ce pattern.
Explique ce que je dois vérifier avant de rendre.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne donne que les erreurs <strong>réelles</strong> de la correction, pas
celles que tu crois avoir commises. Le schéma sort d'un vrai échantillon, sinon il est
faux. Et refais ce diagnostic à chaque copie, pas une fois pour toutes.</div>
"""

LOT_5[96] = """
<h4>Pourquoi ça marche</h4>
<p>Anonymiser avant de coller réduit le risque même si l'outil est fiable. Le principe est
simple : tu ne donnes à personne une information que tu ne mettrais pas en ligne. Les
identifiants sont souvent reconstituables à partir d'un contexte.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Remplace les noms, emails, IBAN, adresses et dates de naissance
par [NOM], [EMAIL], [IBAN], [ADRESSE], [DATE].
Garde la structure du texte pour que je puisse l'analyser.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'anonymisation incomplete est plus dangereuse que l'absence
d'anonymisation : elle donne un <strong>faux sentiment de sécurité</strong>. « Mohamed B. de la
promo B, note 4/20 » suffit à identifier quelqu'un. Cherche les initiales, les dates, les
lieux, les noms de rue — tout ce qui rend la personne identifiable.</div>
"""

LOT_5[97] = """
<h4>Pourquoi ça marche</h4>
<p>Une extension navigateur a, par défaut, accès à <strong>tout ce que tu vois</strong> : tes
onglets, tes mails ouverts, tes documents, et ta session bancaire si tu laisses l'onglet
ouvert. L'extension affiche la réponse dans la page, donc elle a besoin de ce droit pour
fonctionner — c'est le prix de la flexibilité.</p>
<h4>Comment vérifier</h4>
<div class="prompt-box">Chrome → extensions → ⋮ → « Détails »
→ lire la liste des permissions
→ « Permissions du site » : restreindre à « Sur clicked »
Révoque celles que tu n'utilises plus.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Révoque les permissions trop larges, ou supprime l'extension sur ton
compte bancaire. Le risque principal n'est pas le piratage, c'est l'extension récupérée
par quelqu'un d'autre après la revente de l'extension.</div>
"""

LOT_5[98] = """
<h4>Pourquoi ça marche</h4>
<p>Le code d'un employeur ou d'un projet académique contient souvent la logique métier, les
identifiants de serveur, ou des données non publiées. Même sans intention malveillante,
coller ce code dans un service en ligne le transmet à un tiers. La règle est Administrative
avant d'être technique.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Avant de t'écrire du code, liste ce dont tu aurais besoin
(functionnalités, langage, structure).
Ne demande pas d'exemplesMF si tu ne peux pas les donner : donne-moi
la structure du problème, je construirai un exemple générique.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Enseigne la notion sans donner le fichier. Un exemple =
<code>def calculer_moyenne(notes)</code> apprend la logique sans
divulguer <code>notes_etudiants_2026.csv</code>. Vérifie aussi ce qui traîne dans ton
historique shell et tes fichiers temporaires avant de partager l'écran.</div>
"""

LOT_5[99] = """
<h4>Pourquoi ça marche</h4>
<p>Les licences d'usage varient : certains modèles sont libres pour l'usage
<strong>personnel</strong> mais pas commercial ; d'autres interdisent toute génération
d'images d'une personne réelle. Publier sans vérifier, c'est risquer un retrait de contenu
ou des poursuites.</p>
<h4>Comment vérifier</h4>
<ul>
  <li>La page « Terms of Service » de l'outil, section licence ou usage.</li>
  <li>Les conditions de la plateforme de diffusion (YouTube, Instagram).</li>
  <li>La politique de la revue, si c'est un article.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="warn">Une image générée d'une <strong>personne réelle</strong> est interdite sur
la plupart des plateformes, même gratuite. Et pour un usage commercial, la règle est
souvent inverse : il faut un abonnement payant. Vérifie avant de générer, pas après la
publication.</div>
"""

LOT_5[100] = """
<h4>Pourquoi ça marche</h4>
<p>Ne pas déclarer est plus risqué que déclarer : les éditeurs partagent leurs signalements,
et un usage découverte après publication mène à la <strong>rétractation</strong>. Déclarer
n'affaiblit pas le travail — c'est un signe de rigueur, et de plus en plus attendu.</p>
<h4>Phrase type à adapter</h4>
<div class="prompt-box">« ChatGPT (version GPT-4o) et DeepL ont été utilisés pour reformuler
certains paragraphes et pour la traduction. Aucune donnée ni analyse n'a été générée par
l'IA. L'auteur assume l'entière responsabilité du contenu scientifique. »</div>
<h4>Le piège à éviter</h4>
<div class="warn">Trois erreurs fréquentes : l'IA est nommée <strong>co-auteur</strong>
(interdit partout), la <strong>version</strong> est omise (« ChatGPT » ne suffit pas), et la
déclaration est mise après la bibliographie au lieu de la section Methods ou
Acknowledgements. Regarde les instructions de ta revue, pas celles d'une autre.</div>
"""

LOT_5[101] = """
<h4>Pourquoi ça marche</h4>
<p>Confondre le chat et l'API est la source d'erreur la plus fréquente chez un débutant.
Le chat est une <strong>interface de conversation</strong> : tu tapes, tu lis. L'API est une
<strong>interface de programme</strong> : ton code envoie une requête, reçoit une réponse
automatiquement. Les prix, les quotas et les limites ne sont pas les mêmes.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je veux automatiser cette tâche : [description].
Faut-il que j'utilise le chat ou une API ?
Explique les deux options en 5 lignes, avec le coût estimé pour 1000 appels.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le chat n'a pas de quota fiable : impossible d'en dépendre pour un script,
ni de l'automatiser. Si la tâche est répétitive, il faut une API. Et une API se facture à
l'appel : mets toujours une <strong>limite de dépenses</strong> dans le tableau de bord
avant de lancer un script, sinon la facture peut être surprise.</div>
"""
