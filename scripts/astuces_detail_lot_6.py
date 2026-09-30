#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 6 : les astuces 102 à 121.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Deux blocs : API et développement (102 à 110), puis recherche et veille
(111 à 120), et l'ouverture du bloc business (121).

Le bloc API est le plus technique du module : chaque explication indique
le niveau réel de la tâche, parce que c'est là que l'étudiant perd le plus
de temps sans comprendre pourquoi.
"""

LOT_6 = {}

LOT_6[102] = """
<h4>Pourquoi ça marche</h4>
<p>Une clé d'API est un mot de passe. Écrit dans le code, elle part avec le code : dans un
dépôt Git, elle devient publique en quelques minutes, même sur un dépôt privé, et un robot la
trouve. Le fichier <code>.env</code> la sort du code et la laisse uniquement dans ta
machine.</p>
<h4>Comment faire</h4>
<div class="prompt-box"># fichier .env  (jamais versionné)
OPENAI_API_KEY=sk-...

# dans le code Python
import os
from dotenv import load_dotenv
load_dotenv()
CLE = os.getenv("OPENAI_API_KEY")</div>
<p>Et ajoute <code>.env</code> au fichier <code>.gitignore</code>.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Si la clé est déjà partie dans un dépôt, <strong>changer la clé</strong> est
obligatoire : supprimer le fichier ne suffit pas, l'historique conserve tout. Et stocke-la
dans un gestionnaire de mots de passe, jamais dans un fichier de configuration versionné.</div>
"""

LOT_6[103] = """
<h4>Pourquoi ça marche</h4>
<p>Le prix dépend des tokens <strong>d'entrée et de sortie</strong>. Beaucoup de gens
l'oublient et calculent mal. Une réponse de 2 000 tokens coûte plusieurs fois plus qu'une
réponse de 200, même si la question est identique.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Réponds en 200 mots maximum.
Pas de préambule, pas de conclusion : va directement à la réponse.
Si j'ai besoin de plus de détail, je le demanderai.</div>
<p>Sur ton tableau de bord, chaque appel indique : tokens en entrée, tokens en sortie, coût.
C'est là que se trouve la vraie réponse.</p>
<h4>Le piège à éviter</h4>
<div class="tip">Écris « pas de préambule » dans tes prompts de script : une IApolie ajoute
souvent trois lignes de courtesy qui coûtent des tokens pour rien. En automatisation, cette
pol boiledevient le premier poste de dépense.</div>
"""

LOT_6[104] = """
<h4>Pourquoi ça marche</h4>
<p>Sans streaming, l'utilisateur attend en Blanc pendant que le modèle écrit. Avec
streaming, le texte apparaît mot à mot : la perception d'attente est divisée par dix, même
si le temps total est identique.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Écris la fonction d'appel à l'API avec :
1) stream=True
2) une boucle qui affiche chaque morceau au fur et à mesure
3) la gestion de l'erreur si le stream se coupe</div>
<h4>Le piège à éviter</h4>
<div class="warn">Avec le streaming, une erreur peut apparaître <strong>au milieu</strong>
du texte affiché : l'utilisateur a déjà lu un début de réponse incomplet. Ajoute toujours un
test <code>if not stream.choices</code> avant d'afficher, sinon l'application plante sur une
réponse vide.</div>
"""

LOT_6[105] = """
<h4>Pourquoi ça marche</h4>
<p>L'erreur 429 (« trop de requêtes ») est normale et temporaire : une seconde plus tard,
ça marche. Mais gérée naïvement, elle casse tout le script. Un <strong>retry avec backoff
exponentiel</strong> transforme une panne de dix secondes en attente invisible.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris une fonction Python qui appelle une API IA avec :
- retry automatique sur erreur 429
- backoff exponentiel (1s, 2s, 4s, 8s, avec un maximum)
- un plafond de 5 tentatives
- un log des erreurs dans un fichier</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le backoff exponentiel existe pour une raison : réessayer
<strong>immédiatement</strong> aggrave la saturation. Respecte les délais, et arrête après le
plafond — sinon tu obtiens une boucle infinie qui coûte des tokens.</div>
"""

LOT_6[106] = """
<h4>Pourquoi ça marche</h4>
<p>Poser la même question coûte des tokens à chaque fois. Un cache simple — un fichier qui
associe le prompt à la réponse — supprime les répétitions. Sur un script qui analyse
50 documents, c'est souvent la division du coût par dix.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Écris un script qui :
1) calcule une empreinte (hash) du prompt
2) cherche cette empreinte dans un fichier cache.json
3) si elle existe → renvoie la réponse enregistrée
4) sinon → appelle l'API et enregistre le résultat</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un cache sans clé de contexte renvoie des réponses <strong>obsolètes</strong> :
si le modèle a changé, ou si ton prompt a changé, tu ressers une vieille réponse. Vide le
cache après chaque changement de modèle, et vérifie qu'il n'est pas versionné dans Git.</div>
"""

LOT_6[107] = """
<h4>Pourquoi ça marche</h4>
<p>Choisir un modèle au hasard coûte cher : le modèle cher n'est pas forcément le meilleur
pour ta tâche. Ce script répond à une question concrète — <strong>lequel est le moins cher
pour mon usage réel</strong> — avec des chiffres au lieu d'opinions.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un script qui envoie la même question à 3 modèles différents,
compare les réponses, et affiche un tableau :
| Modèle | Longueur | Temps | Coût estimé | Qualité (note manuelle) |</div>
<h4>Le piège à éviter</h4>
<div class="tip">La colonne « qualité » ne peut pas être filled automatiquement de façon
fiable : c'est toi qui notes, à l'aveugle (sans savoir quel modèle a répondu). Sinon tu
notes le style, pas la justesse.</div>
"""

LOT_6[108] = """
<h4>Pourquoi ça marche</h4>
<p>Au-delà de deux ou trois appels, gérer le contexte à la main devient ingérable : la
fenêtre de contexte est limitée, l'ordre des messages compte, et l forgets. Un framework
gère tout ça — c'est sa raison d'être.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Mon projet fait 4 étapes : extraction → résumé → comparaison →
rédaction finale.
Écris-le avec LangChain, avec :
- gestion de la mémoire entre les étapes
- relance automatique sur erreur
- un fichier de sortie par étape</div>
<h4>Le piège à éviter</h4>
<div class="warn">N'utilise pas un framework pour un projet de deux appels : la
configuration coûte plus de temps que le script qu'il remplace. Et <strong>le framework ne
supprime pas les hallucinations</strong> : il orchestre les appels, il ne vérifie rien.</div>
"""

LOT_6[109] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA qui calcule de mémoire se trompe. Une IA qui a un outil à disposition
<strong>l'appelle</strong> et lit le vrai résultat. C'est la différence entre une réponse
approximative et une réponse exacte, et c'est le mécanisme derrière tout assistant fiable.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Donne à cette IA trois outils :
1) une calculatrice (effectuer un calcul)
2) une recherche web (chercher une information actuelle)
3) l'accès à mon fichier CSV (lire des données)
Décris pour chaque outil : nom, description, paramètres, ce qu'il renvoie.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La <strong>description</strong> de l'outil compte autant que le code : si
elle est vague (« permet de calculer »), l'IA choisit l'outil au hasard. Et vérifie toujours
le résultat d'un outil côté serveur : l'IA peut mal former l'appel et transmettre de
mauvaises données.</div>
"""

LOT_6[110] = """
<h4>Pourquoi ça marche</h4>
<p>Un bug qui se produit une fois sur cent est presque impossible à diagnostiquer. Un log
complet — ce que tu as envoyé, ce que tu as reçu, combien de tokens, combien de temps — permet
de reproduire le cas exact en une minute.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Ajoute un logging à chaque appel d'API. Pour chacun, enregistre :
- timestamp
- modèle utilisé
- prompt envoyé
- réponse reçue
- tokens d'entrée et de sortie
- durée
- erreur éventuelle
Format : un fichier JSONL, une ligne par appel.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Journalise les <strong>réponses complètes</strong>, pas seulement un résumé
d'erreur : « ça ne marche pas » ne dit rien, la réponse exacte dit tout. Mais attention à ne
pas journaliser de données personnelles dans un log partagé.</div>
"""

LOT_6[111] = """
<h4>Pourquoi ça marche</h4>
<p>Une revue de littérature écrite d'un seul jet est une liste d'articles lus en diagonale.
Le découpage en trois étapes — identifier, résumer, classer — force à passer chaque article
<strong>une seule fois mais vraiment</strong>, et c'est la dernière étape qui produit la
synthèse.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Étape 1 : liste 10 articles clés sur [sujet] avec auteurs et années.
Étape 2 : pour chacun, résume la thèse en 2 phrases.
Étape 3 : classe-les par courant théorique et identifie les débats.
Fais une étape à la fois, j'attends ma validation.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les articles proposés <strong>existent peut-être pas</strong> ou ne parlent
pas du sujet annoncé. Vérifie chaque titre sur Google Scholar avant d'aller plus loin, et
télécharge les PDF : résumer un article à partir de son seul titre est un résumé de titre,
pas de contenu.</div>
"""

LOT_6[112] = """
<h4>Pourquoi ça marche</h4>
<p>Connaître les textes fondateurs d'un domaine, c'est connaître ses <strong>conventions</strong>
et les questions qui structurent le débat. Une fois que tu les as lus, tout le reste se situe
plus facilement.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Quels sont les 5 articles fondateurs sur [sujet] ?
Pour chacun : auteur, année, apport principal, nombre de citations approximatif.
Signale clairement ce dont tu n'es pas sûr.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le nombre de citations est le champ le plus souvent <strong>inventé</strong> :
il change chaque année et l'IA ne le connaît pas. Vérifie-le sur Google Scholar, ou supprime
le champ et demande plutôt « quel est l'article le plus cité sur Scholar aujourd'hui ? »,
puis regarde toi-même.</div>
"""

LOT_6[113] = """
<h4>Pourquoi ça marche</h4>
<p>Comparer cinq articles, c'est un travail de tableau : auteur, année, méthode, échantillon,
résultat, limite. Demander le tableau rempli <strong>et rien d'autre</strong> supprime le
texte superflu et rend les lignes directement comparables.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici 5 résumés d'articles. Remplis ce tableau :
| Auteur | Année | Méthode | Échantillon | Résultat principal | Limite |
Ne résume pas, remplis uniquement le tableau.
Laisse « non précisé » si l'information n'est pas dans le résumé.</div>
<h4>Le piège à éviter</h4>
<div class="tip">La colonne « limite » est la plus utile et la plus difficile : une IA
l'<strong>invente</strong> volontiers pour remplir une case. Contre-mesure : demande
explicite la phrase exacte du texte qui l'énonce, ou laisse la case vide.</div>
"""

LOT_6[114] = """
<h4>Pourquoi ça marche</h4>
<p>Une problématique mal formulée donne une étude mal cadrée. Proposer cinq reformulations
d'orientations différentes (précise, ouverte, polémique, opérationnelle, théorique) permet de
voir que le même sujet ouvre plusieurs études.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici ma problématique : [...]
Propose 5 reformulations :
- plus précise
- plus ouverte
- plus polémique
- plus opérationnelle
- plus théorique
Pour chacune, dis en une ligne ce qu'elle promettrait comme résultats.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La reformulation « plus polémique » est la plus séduisante et la plus
risquée : elle promet un débat, alors que la littérature est peut-être unie. Demande les
sources qui montrent le débat, et vérifie-les.</div>
"""

LOT_6[115] = """
<h4>Pourquoi ça marche</h4>
<p>Trouver un <strong>gap</strong> — un angle non traité — demande de lire beaucoup de résumés
et de les superposer. C'est exactement ce qu'une IA fait bien quand on lui demande une
synthèse comparative plutôt qu'un résumé isolé.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici 10 articles sur [sujet]. Identifie :
1) ce qui est déjà bien étudié
2) ce qui est contradictoire
3) ce qui n'a pas été étudié (le gap)
4) 3 questions de recherche possibles
Cite l'article qui soutient chaque affirmation.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un « gap » trouvé par une IA est parfois simplement un sujet dont personne
n'a parlé <strong>parce qu'il est sans intérêt</strong>. Vérifie qu'il y a de la littérature
voisine et un public intéressé : demande les 3 revues qui publieraient un article sur ce gap.</div>
"""

LOT_6[116] = """
<h4>Pourquoi ça marche</h4>
<p>L'abstract est la partie la plus lue et la plus difficile : il doit tenir en 150 mots tout
le raisonnement. Imposer <strong>cinq phrases de rôles différents</strong> empêche l'IA de
produire un texte vague et garantit que rien d'essentiel ne manque.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Écris un abstract de 150 mots en 5 phrases :
1) contexte
2) problème
3) méthode
4) résultat principal
5) implication
Style académique, pas de jargon inutile.
Ne mets aucun chiffre qui ne soit pas dans le texte que je te donne.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA a tendance à gonfler le « résultat principal » en parlant de
« contribution significative » quand tes chiffres sont modestes. Compare la phrase de
résultat mot à mot avec ton article : c'est l'endroit le plus souvent exagéré.</div>
"""

LOT_6[117] = """
<h4>Pourquoi ça marche</h4>
<p>Un jury ne pose pas des questions sur ce que tu as écrit, il cherche les <strong>zones
faibles</strong>. Faire simuler la soutenance en avance, avec une note après chaque réponse,
révèle les trous avant le jour J — c'est le seul moyen de les combler à temps.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu es membre d'un jury de master.
Pose-moi 10 questions difficiles sur mon mémoire, une par une.
Après chaque réponse, donne-moi une note sur 10 et un conseil précis.
Commence par les questions de méthode, puis de résultats, puis de contribution.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Commence par la méthode, pas par le résumé : c'est là que le jury va t.interroger,
et c'est là que tu es le moins préparé. Si tu ne sais pas répondre à une question, dis-le
franchement et propose un plan pour y répondre — c'est valorisé, alors que l'invention ne
l'est pas.</div>
"""

LOT_6[118] = """
<h4>Pourquoi ça marche</h4>
<p>La veille faite en une fois devient un travail qu'on reporte. Dix minutes par jour sont
suffisantes, et elles sont tenables ; trois heures une fois par mois ne le sont pas. Les
alertes automatisées font le tri : tu ne lis que ce qui concerne ton sujet.</p>
<h4>Comment faire</h4>
<div class="prompt-box">1) Google Scholar → créer une alerte sur [sujet + mots-clés]
2) Flux RSS des 3 revues qui te concernent
3) Une fois par semaine, demande un résumé groupé des nouveaux articles</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une alerte trop large remplit ta boîte de 50 articles par jour, et tu la
supprimes en une semaine. Sois <strong>précis</strong> : mets un auteur, un terme technique
exact, ou les deux. Trois alertes bien ciblées valent mieux que trente alertes larges.</div>
"""

LOT_6[119] = """
<h4>Pourquoi ça marche</h4>
<p>Lire dix articles en diagonale ne produit rien de réutilisable. Une fiche de lecture
structurée <strong>force à l'extraction</strong> : la question, la méthode, le résultat, et
surtout ce que tu peux réutiliser. C'est le format qui transforme une lecture en matériau.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">À partir de cet article, remplis une fiche :
- Référence complète
- Question de recherche
- Méthode
- Résultat principal
- 3 citations marquantes (avec pages)
- Ce que je peux réutiliser dans mon travail
Pour les citations, donne le texte exact et le numéro de page.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Les <strong>numéros de page</strong> sont le point critique : sans eux, la
citation est introuvable. Demande « si tu n'es pas sûr de la page, écris [page à vérifier] »
plutôt que d'inventer un numéro — et vérifie les trois citations dans le PDF avant de les
citer.</div>
"""

LOT_6[120] = """
<h4>Pourquoi ça marche</h4>
<p>Traduire un article scientifique sans perdre le sens demande plus qu'un dictionnaire :
il faut garder les <strong>termes techniques en anglais</strong> entre parenthèses la première
fois, et repérer les faux-amis. L'IA fait les deux, et signale les passages ambigus.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Traduis ce passage de l'anglais vers le français académique.
Garde les termes techniques en anglais entre parenthèses la première fois.
Signale les faux-amis et les tournures ambiguës.
Ne reformule pas le sens : traduis fidèlement.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Une « belle » traduction qui change le sens est pire qu'une traduction
maladroite. Compare la version traduite à l'original <strong>phrase par phrase</strong> sur
les passages qui portent une affirmation, et garde l'original à côté : c'est lui qui fait foi
en cas de contestation.</div>
"""

LOT_6[121] = """
<h4>Pourquoi ça marche</h4>
<p>Une offre de service vague — « je fais du design, du SEO, de la rédaction » — ne fait pas
venir de clients. Décrire <strong>le problème du client</strong> en premier attire
seulement ceux qui ont ce problème, et la structure inclus / exclu protège des malentendus.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Rédige une offre de service en 1 page :
- problème du client
- ma solution
- ce qui est inclus / exclu
- délai
- prix (3 formules)
- prochaine étape
Ton : professionnel, direct, sans jargon.
Public : [qui exactement, quel niveau].</div>
<h4>Le piège à éviter</h4>
<div class="tip">La section <strong>« ce qui est exclu »</strong> est celle que les clients
lisent le plus et que les prestataires oublient le plus. C'est elle qui évite les
allers-retours interminables une fois le travail commencé.</div>
"""
