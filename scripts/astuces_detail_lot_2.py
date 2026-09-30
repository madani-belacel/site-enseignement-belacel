#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Explications détaillées des astuces, lot 2 : les astuces 22 à 41.

Format court (≈ 150 mots), trois parties toujours dans le même ordre :
  1. pourquoi ça marche   2. un exemple à copier   3. le piège à éviter

Le format long reste réservé aux astuces que le professeur rédige
lui-même (voir les ASTUCES[1] et ASTUCES[2] de astuces_detail.py) :
il n'est pas écrasé par les lots, grâce au setdefault du chargeur.
"""

LOT_2 = {}

LOT_2[22] = """
<h4>Pourquoi ça marche</h4>
<p>Par défaut, tes conversations peuvent servir à améliorer le modèle. Ce n'est pas
nulle part dans le texte affiché : c'est une case à cocher, souvent activée d'office.
La désactiver prend trente secondes et ne change rien à la qualité des réponses.</p>
<h4>Comment faire</h4>
<div class="prompt-box">ChatGPT → Paramètres → Contrôles des données →
désactive « Améliorer le modèle pour tout le monde ».
Claude et Gemini ont des options similaires dans leurs réglages de confidentialité.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Désactiver l'entraînement <strong>ne supprime pas</strong> l'historique de
tes conversations : il reste visible dans ton compte, et tu peux le supprimer à part.
Fais les deux : désactiver l'entraînement, puis effacer l'historique.</div>
"""

LOT_2[23] = """
<h4>Pourquoi ça marche</h4>
<p>Une IA en ligne envoie ce que tu colles à un serveur, qui peut le stocker, le relire,
voire le transmettre à un humain pour l'améliorer. Le risque n'est pas qu'elle « pense »
à tes données : c'est qu'<strong>un humain les voie</strong> dans certains cas, et qu'un
mauvais Ricochet te coûte cher.</p>
<h4>La règle à appliquer</h4>
<div class="reflexe">« Si je ne mettrais pas ce texte sur un forum public, je ne le colle
pas dans une IA en ligne. »</div>
<p>Concrètement, on ne colle jamais : un mot de passe, un IBAN, un numéro de carte, une
copie d'un sujet d'examen, un nom de patient, un document interne non publié.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Le cas le plus courant n'est pas le mot de passe obvious, c'est
l'<strong>anonymisation incomplète</strong> : « voici le texte de mon camarade
Mohamed B. de la promo B, note 4/20 ». Ça suffit à l'identifier. Remplace les noms,
les notes, les dates et les lieux par <code>[NOM]</code>, <code>[NOTE]</code> avant de
coller.</div>
"""

LOT_2[24] = """
<h4>Pourquoi ça marche</h4>
<p>Ollama fait tourner un modèle <strong>sur ton propre ordinateur</strong>, sans
internet. Rien ne sort de ta machine : pas de serveur, pas de compte, pas d'historique.
C'est la seule façon de travailler sur un document vraiment confidentiel.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Installer Ollama (ollama.com), puis :
ollama pull llama3
puis : ollama run llama3
Le modèle est prêt. Llama, Mistral et DeepSeek sont les plus utilisés.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un modèle local est <strong>moins bon</strong> qu'un modèle en ligne sur
les tâches complexes, et il faut un bon ordinateur (8 Go de mémoire vive minimum, 16 Go
idéal). Commence par l'IA en ligne, et réserve le local aux sujets vraiment sensibles.</div>
"""

LOT_2[25] = """
<h4>Pourquoi ça marche</h4>
<p>Les gestes répétés cent fois par jour sont ceux qui font gagner le plus de temps. Trois
raccourcis couvrent l'essentiel du travail quotidien avec l'IA.</p>
<h4>Les trois à connaître</h4>
<ul>
  <li><strong>Navigateur</strong> — <code>Ctrl + L</code> puis tape le début de l'URL : tu
      vas directement à l'outil, sans passer par un moteur de recherche.</li>
  <li><strong>Ton fichier de prompts</strong> — <code>Ctrl + F</code> puis le nom : tu
      retrouves un prompt en une seconde.</li>
  <li><strong>Dictée</strong> — <code>Win + H</code> sur Windows, touche
      <kbd>Fn</kbd> deux fois sur Mac.</li>
</ul>
<h4>Le piège à éviter</h4>
<div class="tip">Apprends-en <strong>un par semaine</strong>, pas les trois d'un coup.
Un raccourci appris aujourd'hui et jamais utilisé est un raccourci inexistant.</div>
"""

LOT_2[26] = """
<h4>Pourquoi ça marche</h4>
<p>Un PDF de 40 pages ne se révise pas en le lisant. Il se révise en <strong>3 objets</strong> :
un résumé, des questions d'examen, et la liste de ce qu'il faut savoir par cœur. C'est
exactement ce que l'IA peut produire en une minute.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mon PDF de cours.
1) Résume en 10 points maximum
2) Crée 8 questions type examen avec réponses
3) Liste les 5 notions les plus importantes à retenir par cœur</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un PDF mal numérisé ou contenant des images de tableaux sera mal lu :
l'IA dira « le document ne contient pas de texte exploitable ». Utilise Gemini pour les
PDF (il lit les images), ou fais un OCR d'abord. Et <strong>vérifie les questions</strong> :
elles viennent du document, mais la réponse peut être fausse.</div>
"""

LOT_2[27] = """
<h4>Pourquoi ça marche</h4>
<p>Tu ne peux pas relire 30 pages dans le bus. Tu <strong>peux</strong> les écouter. Un
texte de cours devient un audio de 25 minutes, et tu révises en marchant, dans le bus, en
attendant. C'est le geste qui change le plus ton temps de révision.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Lis-moi ce texte à voix haute.
Puis : « Répète la partie sur les finances en insistant sur les chiffres. »</div>
<p>Si l'IA ne le fait pas, utilise la synthèse vocale de ton navigateur (touche
<kbd>F12</kbd>, onglet <em>Lecture vocale</em>) ou l'option <em>Écouter</em> de vos notes.</p>
<h4>Le piège à éviter</h4>
<div class="warn">L'audio ne remplace pas la lecture pour <strong>apprendre une
définition</strong> : on retient mal un mot nouveau entendu mais pas vu. Écoute pour
répéter, lis pour apprendre.</div>
"""

LOT_2[28] = """
<h4>Pourquoi ça marche</h4>
<p>Taper est lent, surtout sur un sujet où les idées ne sont pas encore formées. Dicter
transforme ta pensée brute en texte : tu écris 3 fois plus vite, et l'IA peut ensuite
mettre en forme ce que tu n'arrivais pas à formuler.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Je vais dicter un texte sans ponctuation.
[texte dicté]
Récris-le proprement, garde mes mots et mon sens, ne rajoute aucune idée.</div>
<h4>Le piège à éviter</h4>
<div class="warn">La dictée se trompe sur les noms propres, les termes techniques et les
nombres. <strong>Toujours relire</strong> avant d'envoyer : une faute de dictée dans un
nom de personne ou une date passe inaperçue et fausse tout le travail.</div>
"""

LOT_2[29] = """
<h4>Pourquoi ça marche</h4>
<p>« Je dois rendre ça vendredi » ne produit aucun plan. Une demande avec une <strong>date
et un tableau imposé</strong> produit un découpage jour par jour. La différence tient
entièrement au format demandé.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je dois [objectif] d'ici [date].
Donne-moi un plan jour par jour en tableau :
| Jour | Tâche précise | Durée | Résultat attendu |
Sois réaliste : maximum 2h par jour.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le plan sera trop optimiste : l'IA ne connaît pas tes autres cours ni tes
heures de travail. Impose une limite basse (2h/jour), puis ajoute toi-même les jours où tu
n'as pas le temps. Un plan réaliste qu'on suit vaut mieux qu'un plan parfait qu'on abandonne
au bout de deux jours.</div>
"""

LOT_2[30] = """
<h4>Pourquoi ça marche</h4>
<p>Demander à une IA ses propres limites est contre-intuitif, mais très efficace : sur un
sujet précis, elle sait quelles zones sont hors de sa zone de fiabilité. C'est
particulièrement utile pour les chiffres, les dates et le droit, où l'invention est
fréquente et discrète.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Sur ce sujet précis, quelles sont tes limites connues ?
Quelles informations pourrais-tu inventer ou déformer ?
Comment dois-je vérifier ta réponse ?</div>
<h4>Le piège à éviter</h4>
<div class="tip">Ne prends pas sa réponse pour une garantie : une IA peut se déclarer
« fiable » sur un sujet où elle se trompe. Mais poser la question t'oblige à savoir
<em>ce qu'il faut vérifier</em>, et c'est exactement l'objectif.</div>
"""

LOT_2[31] = """
<h4>Pourquoi ça marche</h4>
<p>Changer d'IA quand tu ne comprends pas revient à tirage au sort : tu obtiens une
autre réponse, souvent aussi incompréhensible. Demander <strong>pourquoi</strong> fait
révéler le raisonnement, et c'est le raisonnement qui te manque.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je ne comprends pas cette phrase. Explique-moi pourquoi tu as
écrit ça, mot par mot. Puis dis-moi ce que je dois retenir de cette idée.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si après deux explications la notion reste floue, le problème n'est pas
l'IA : c'est que la notion est plus difficile que tu ne le pensais. Demande alors un
exemple concret, ou passe à la notion simple qui la sous-tend. Descendre d'un niveau
difficulty vaut mieux que changer d'outil.</div>
"""

LOT_2[32] = """
<h4>Pourquoi ça marche</h4>
<p>Les mêmes prompts ne conviennent pas à tout : un prompt qui réussit sur un exposé
échoue sur un QCM, un prompt qui date bien un article invente des références. Sans
journal, tu refais les mêmes erreurs pendant des mois.</p>
<h4>Comment faire</h4>
<div class="prompt-box">Dans mon fichier de prompts, après chaque essai, j'ajoute :
- Prompt X → excellent pour Y
- Prompt Z → hallucine toujours sur les dates
- Prompt W → trop long, demander une version courte</div>
<h4>Le piège à éviter</h4>
<div class="tip">Note ce qui <strong>échoue</strong> autant que ce qui réussit : une note
« ce prompt se trompe sur les chiffres » vous fera gagner plus de temps qu'une note
« bon prompt ».</div>
"""

LOT_2[33] = """
<h4>Pourquoi ça marche</h4>
<p>Quand plusieurs IA ont répondu, c'est la partie la plus dur : choisir laquelle croire.
Une IA utilisée comme <strong>directeur de projet</strong> fait ce tri à ta place, et te
donne le prompt exact pour la suite. Tu ne joues plus le rôle de SELECTeur, tu joues celui
de décideur.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Tu es mon directeur de projet. Je vais coller les réponses de
plusieurs IA. À chaque fois, dis-moi :
1) laquelle est la plus fiable et pourquoi
2) ce qu'il faut garder et ce qu'il faut jeter
3) le prochain prompt exact à envoyer</div>
<h4>Le piège à éviter</h4>
<div class="warn">Le directeur de projet n'a pas accès à Internet : il juge sur la
cohérence du texte, pas sur la vérité. S'il choisit la réponse la plus détaillée, ce n'est
pas forcément la bonne. Vérifie toujours la source finale avant de l'utiliser.</div>
"""

LOT_2[34] = """
<h4>Pourquoi ça marche</h4>
<p>Une réponse est»: plusiexpository difficile à évaluer sansRepère. En imposant un
niveau de confiance, tu obtiens une réponse qui se <strong>qualifie elle-même</strong> : tu
sais ce qui est solide et ce qui est fragile, sans refaire tout le travail de vérification.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">À la fin de ta réponse, ajoute :
- Sources (liens ou références) si tu en as
- Ou « Niveau de confiance : élevé / moyen / faible » + la raison</div>
<h4>Le piège à éviter</h4>
<div class="warn">Un « confiance : élevée » ne veut rien dire si le modèle n'a pas de
sources : il peut être sûr de lui avec une invention. <strong>Un lien vérifiable vaut
mille fois plus qu'un niveau de confiance auto-déclaré.</strong> S'il n'y a pas de source,
traite la réponse comme un niveau « faible ».</div>
"""

LOT_2[35] = """
<h4>Pourquoi ça marche</h4>
<p>Décrire ton besoin <strong>en français, en phrases</strong> est plus efficace qu'une
liste de mots-clés techniques. L'IA comprend « lis un fichier CSV et calcule la moyenne »
mieux qu'un jargon maladroit, et elle choisit la bonne méthode toute seule.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Je veux un script Python qui :
1) lit un fichier CSV
2) calcule la moyenne de la colonne « note »
3) affiche les 5 meilleures lignes
Écris le code complet, commenté en français, prêt à coller.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Décrire le résultat, pas la méthode. Si tu écris « utilise pandas et la
fonction groupby », tu figes une solution et tu perds le bénéfice de l'IA, qui sait
parfois faire plus simple. Demande le résultat, accepte la méthode qu'elle choisit.</div>
"""

LOT_2[36] = """
<h4>Pourquoi ça marche</h4>
<p>Un agent qui écrit directement peut modifier dix fichiers avant que tu comprennes ce
qui se passe. Le <strong>mode Plan</strong> inverse l'ordre : l'agent expose son plan,
tu valides, puis seulement il agit. Le risque passe de «innombrable » à « prévisible ».</p>
<h4>Comment faire</h4>
<div class="prompt-box">Montre-moi les fichiers que tu vas toucher et pourquoi.
N'écris rien tant que je n'ai pas validé.</div>
<p>Dans Cursor : touche <kbd>Tab</kbd> pour basculer Plan → Build. Dans OpenCode : la
même bascule existe en début de session.</p>
<h4>Le piège à éviter</h4>
<div class="warn">Un plan peut être correct dans son intention et faux dans ses détails.
Lis les <strong>noms de fichiers</strong>, pas seulement l'intention : si l'agent veut
toucher un fichier que tu n'as pas nommé, arrête-le.</div>
"""

LOT_2[37] = """
<h4>Pourquoi ça marche</h4>
<p><code>@fichier</code> restreint le contexte à ce dont l'agent a réellement besoin, et
<code>/undo</code> permet de revenir en arrière instantanément. Les deux transforment un
agent dangereux en agent contrôlable : on limite la portée, on garde la marche arrière.</p>
<h4>Comment faire</h4>
<div class="prompt-box">@index.html Ajoute une carte « Tarifs » après le titre,
au même style que les cartes existantes.
Si tu as besoin d'un autre fichier, arrête-toi et dis-le moi.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Ne lance jamais une modification sur tout un dossier d'un coup. Un seul
fichier à la fois, relire le diff, puis valider. Et travaille dans un dossier de sauvegarde
ou une branche Git : c'est la seule sécurité réelle quand un agent modifie des fichiers.</div>
"""

LOT_2[38] = """
<h4>Pourquoi ça marche</h4>
<p>Copier un code sans le comprendre est la principale cause de blocage en TP : quand
ça plante, tu ne sais même pas où chercher. L'explication ligne par ligne, avec la question
« que se passerait-il si on l'enlevait », transforme une ligne mysterious en une ligne
comprise.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Voici mon code. Explique-le ligne par ligne en français simple.
Pour chaque ligne importante : à quoi elle sert, et ce qui se passerait si on l'enlevait.</div>
<h4>Le piège à éviter</h4>
<div class="tip">Ne t'arrête pas à la première explication. Demande ensuite : « quelle
ligne peut-on supprimer sans rien casser ? » — c'est ce tri qui te fait comprendre
vraiment le programme.</div>
"""

LOT_2[39] = """
<h4>Pourquoi ça marche</h4>
<p>Coller une erreur à une IA sans structure produit une réponse générique. En imposant
trois étapes — <strong>signification, cause, correctif exact</strong> — tu obtiens un
diagnostic, et surtout tu reçois le code à remplacer plutôt qu'une reformulation.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">J'ai cette erreur : [colle l'erreur complète]
1) Dis-moi en 1 phrase ce que signifie l'erreur
2) Donne la cause la plus probable
3) Propose le correctif exact (le code à remplacer)</div>
<h4>Le piège à éviter</h4>
<div class="warn">Colle <strong>tout</strong> le message, jusqu'à la dernière ligne : les
lignes <code>Note:</code> et <code>Caused by:</code> contiennent la cause réelle. Et
précise l'environnement (Python 3.11, Windows 11) : la même erreur a souvent plusieurs
causes selon la version.</div>
"""

LOT_2[40] = """
<h4>Pourquoi ça marche</h4>
<p>Une correction « propre » sans explication ne t'apprend rien : tu acceptes la version
corrigée sans savoir pourquoi. En demandant <strong>la phrase d'origine, la phrase
corrigée et la règle</strong>, tu obtiens une leçon, et la faute ne se reproduira plus.</p>
<h4>Exemple à copier</h4>
<div class="prompt-box">Corrige ce texte. Pour chaque correction :
- phrase originale
- phrase corrigée
- règle grammaticale ou stylistique en 1 ligne
À la fin : version propre complète.</div>
<h4>Le piège à éviter</h4>
<div class="warn">L'IA peut « corriger » un choix de style qui était deliberation. Si tu
doutes d'un changement, demande « pourquoi ce changement est-il obligatoire ? » avant
de l'accepter.</div>
"""

LOT_2[41] = """
<h4>Pourquoi ça marche</h4>
<p>Un moteur de traduction produit du texte correct mais parfois artificiel, et il
connait mal les faux-amis entre le français et l'anglais. Une IA, elle, repère les
tournures naturelles et signale les pièges. Les deux ensemble donnent un bon résultat.</p>
<h4>Comment faire</h4>
<ol>
  <li>Traduis avec DeepL (la meilleure base).</li>
  <li>Colle le résultat dans ChatGPT ou Claude et demande :</li>
</ol>
<div class="prompt-box">Vérifie cette traduction FR → EN.
Signale les faux-amis et les tournures non naturelles.
Propose 2 alternatives pour les passages douteux.</div>
<h4>Le piège à éviter</h4>
<div class="warn">Si tu publies ou rends un travail, <strong>relis chaque phrase</strong> :
l'IA ne dit pas toujours quand elle n'est pas sûre. Et attention aux termes juridiques ou
scientifiques traduits littéralement : ils doivent être vérifiés par un humain du métier.</div>
"""
