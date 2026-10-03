#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lot 2 — explications détaillées des astuces 36, 43, 44, 91 et 100.

Contenu rédigé à la main par le professeur, 10 sections par astuce.
Le générateur ajoute la charpente : en-tête, fil d'Ariane, pied de page,
navigation précédent/suivant, canonical.
"""

LOT_2 = {}

# ===================================================================== 36
LOT_2[36] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Dans Cursor ou OpenCode : demande d'abord le plan (« montre-moi les fichiers que tu vas toucher et pourquoi »). Valide le plan, puis lance l'écriture.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Demande d'abord le plan »</strong> → Avant que l'agent modifie le moindre fichier, tu lui demandes de te dire <em>ce qu'il compte faire</em>. C'est une étape où rien n'est encore écrit sur le disque.</p>
<p><strong>« Montre-moi les fichiers que tu vas toucher »</strong> → Tu exiges la liste précise des fichiers concernés. Si la liste est trop longue, tu peux arrêter et réduire le périmètre. C'est ton garde-fou contre les modifications massives.</p>
<p><strong>« Et pourquoi »</strong> → Tu obliges l'agent à justifier chaque action. Cela révèle les faux pas : « je vais modifier <code>config.py</code> pour changer le port » — mais tu ne voulais pas toucher au port.</p>
<p><strong>« Valide le plan, puis lance l'écriture »</strong> → Tu sépares les deux moments : réfléchir, puis exécuter. Tu ne mélanges jamais les deux, sinon tu perds le contrôle.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu fais construire une maison.</p>
<p><strong>Sans plan :</strong> tu dis à l'ouvrier « construis-moi une maison ». Il commence par les fondations, mais il a oublié la salle de bain, il met la cuisine au premier étage, il n'y a pas de fenêtres au sud. À la fin, il faut tout casser.</p>
<p><strong>Avec plan :</strong> tu dis « montre-moi les plans ». L'ouvrier te présente les 4 pièces, leur emplacement, l'orientation des fenêtres. Tu vois une erreur : la cuisine au premier étage. Tu la signales. Il corrige le plan. Puis il construit.</p>
<p>Les agents IA fonctionnent pareil. Le mode Plan évite de casser 8 fichiers pour un résultat qui ne te convient pas.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Élément du plan</th><th>Ce que ça te dit</th><th>Ce que tu vérifies</th></tr>
<tr><td><strong>Liste des fichiers</strong></td><td>Où l'agent va écrire</td><td>Aucun fichier sensible ? Aucun fichier inutile ?</td></tr>
<tr><td><strong>Raison de chaque action</strong></td><td>Le « pourquoi » derrière chaque modification</td><td>La raison correspond-elle à ton besoin ?</td></tr>
<tr><td><strong>Ordre des étapes</strong></td><td>Ce qui se fait avant quoi</td><td>Y a-t-il un risque de casser avant de créer ?</td></tr>
<tr><td><strong>Estimation</strong></td><td>Combien de fichiers, combien de temps</td><td>Est-ce proportionné à ta demande ?</td></tr>
</table>

<h2>5. Application pratique — ajouter une fonctionnalité à un site</h2>
<p><strong>Sans mode Plan :</strong></p>
<div class="prompt-box">Ajoute un formulaire de contact à mon site.</div>
<p>L'agent modifie <code>index.html</code>, crée <code>contact.php</code>, ajoute du CSS dans <code>style.css</code>, modifie <code>main.js</code>, touche au <code>config.php</code> pour ajouter une adresse e-mail, et — au passage — renomme une variable dans 3 autres fichiers. Tu ne sais plus ce qui a changé, ni pourquoi.</p>
<p><strong>Avec mode Plan :</strong></p>
<div class="prompt-box">Demande : ajouter un formulaire de contact à mon site.
AVANT TOUTE ÉCRITURE : donne-moi le plan.
Format attendu :
- Fichiers à créer
- Fichiers à modifier
- Raison pour chacun
- Estimation (temps, risque)</div>
<p>L'agent te renvoie :</p>
<ul>
<li>Créer <code>contact.html</code> (page de contact)</li>
<li>Modifier <code>index.html</code> (ajout du lien vers la page)</li>
<li>Ajouter CSS dans <code>style.css</code> (nouvelle section)</li>
<li><em>Ne touche à aucun fichier PHP ou JS pour le moment.</em></li>
</ul>
<p>Tu valides. Il écrit. Tu vérifies. <strong>4 fichiers annoncés, 4 fichiers modifiés</strong> — pas de surprise.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Plan d'abord, écriture ensuite. Jamais les deux en même temps.</strong></div>
<p>La règle à appliquer à chaque nouvelle tâche : quand tu demandes quelque chose à un agent, termine toujours ton prompt par :</p>
<div class="prompt-box">Donne-moi d'abord le plan. J'attends ma validation avant que tu écrives.</div>
<p>Cette phrase seule transforme un agent imprévisible en collaborateur fiable.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Valider le plan sans le lire.</strong> Le plan n'a de valeur que si tu le lis. 30 secondes de lecture économisent 30 minutes de correction.</li>
<li><strong>Accepter un plan trop large.</strong> Si l'agent annonce 15 fichiers modifiés, réduis. « Commence par les 3 premiers, montre-moi le résultat, on continue après. »</li>
<li><strong>Modifier le plan au fur et à mesure.</strong> Si tu changes d'avis en cours d'exécution, arrête l'agent et refais un plan propre.</li>
<li><strong>Utiliser le mode Plan pour tout.</strong> Pour une modification d'une ligne, pas besoin. Réserve le Plan aux tâches qui touchent 2 fichiers ou plus.</li>
<li><strong>Ne pas sauvegarder avant.</strong> Même avec un plan validé, garde une copie (ou un <code>git init</code>) pour pouvoir revenir en arrière.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>  Ta demande
       │
       ▼
  ┌──────────────┐
  │  MODE PLAN   │  ← L'agent réfléchit, ne touche à rien
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐   Non
  │  Plan OK ?   ├──────▶ Corriger le plan
  └──────┬───────┘
         │ Oui
         ▼
  ┌──────────────┐
  │  MODE BUILD  │  ← L'agent écrit
  └──────────────┘
         │
         ▼
  ┌──────────────┐
  │  Vérifier     │
  └──────────────┘
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Plan avant écriture.</strong> La phrase magique : « Donne-moi d'abord le plan. »</li>
<li><strong>Lire le plan.</strong> Vérifier les fichiers, les raisons, l'ordre.</li>
<li><strong>Réduire si trop large.</strong> 3 fichiers par étape, pas 15.</li>
<li><strong>Sauvegarder avant.</strong> Un plan ne remplace pas un filet de sécurité.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans mode Plan</th><th>Avec mode Plan</th></tr>
<tr><td>« Ajoute un formulaire »</td><td>« Donne-moi le plan d'abord »</td></tr>
<tr><td>8 fichiers modifiés en vrac</td><td>4 fichiers annoncés et contrôlés</td></tr>
<tr><td>Tu découvres après coup</td><td>Tu valides avant</td></tr>
<tr><td>Correction difficile</td><td>Zéro surprise</td></tr>
<tr><td><strong>Bilan : perte de contrôle</strong></td><td><strong>Bilan : collaboration fiable</strong></td></tr>
</table>"""

# ===================================================================== 43
LOT_2[43] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Pour chaque affirmation factuelle ou référence citée dans ta réponse, indique la source exacte. Si tu n'as pas de source vérifiable, écris explicitement « Source non vérifiable » et ne l'invente pas.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Pour chaque affirmation factuelle »</strong> → Tu obliges l'IA à distinguer les faits (dates, chiffres, noms) des opinions. Une IA mélange souvent les deux. Cette consigne la force à catégoriser.</p>
<p><strong>« Ou référence citée »</strong> → Les références bibliographiques sont le domaine où les IA hallucinent le plus. Elles inventent des auteurs plausibles, des titres crédibles, des DOI qui ressemblent à de vrais DOI — mais qui n'existent pas.</p>
<p><strong>« Indique la source exacte »</strong> → Tu exiges un lien, un titre, une page. Pas « selon des études », mais « Black &amp; William (1998), p. 7 ».</p>
<p><strong>« Si tu n'as pas de source vérifiable, écris explicitement "Source non vérifiable" »</strong> → Tu donnes à l'IA une porte de sortie honnête. Sans cette phrase, elle préfère inventer plutôt que d'admettre qu'elle ne sait pas.</p>
<p><strong>« Et ne l'invente pas »</strong> → Tu l'interdis explicitement. C'est la phrase qui bloque le comportement par défaut.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine un étudiant qui doit rédiger une dissertation.</p>
<p><strong>Scénario A :</strong> il cite « Selon Durkheim (1897), le suicide est un fait social ». L'enseignant vérifie : existe. Note correcte.</p>
<p><strong>Scénario B :</strong> il cite « Selon Durkheim (1895), le suicide est un fait social ». L'enseignant vérifie : c'est bien Durkheim, mais l'année est fausse (c'est 1897). Note réduite.</p>
<p><strong>Scénario C :</strong> il cite « Selon Durkheim &amp; Mauss (1903), le suicide est un fait social ». L'enseignant vérifie : cet article existe, mais il ne parle pas de suicide. Note très basse.</p>
<p><strong>Scénario D :</strong> il cite « Selon Durkheim (1897), <em>Le Suicide</em>, Paris, Alcan ». L'enseignant vérifie : tout est bon. Note maximale.</p>
<p>L'IA hallucine comme le scénario C : une référence parfaite en apparence, mais qui ne parle pas du sujet ou qui n'existe pas. La consigne de l'astuce 43 force l'IA à dire « je ne sais pas » plutôt qu'à inventer.</p>

<h2>4. Les types d'hallucinations</h2>
<table>
<tr><th>Type</th><th>Exemple</th><th>Comment détecter</th></tr>
<tr><td><strong>Référence fictive</strong></td><td>« Dupont (2018), article X » qui n'existe pas</td><td>Chercher le titre exact sur Google Scholar</td></tr>
<tr><td><strong>Auteur mal attribué</strong></td><td>Attribuer une citation à Einstein</td><td>Vérifier sur Wikiquote ou un recueil officiel</td></tr>
<tr><td><strong>Date décalée</strong></td><td>Un événement de 1969 daté 1972</td><td>Vérifier sur une encyclopédie</td></tr>
<tr><td><strong>Chiffre inventado</strong></td><td>« 78 % des étudiants » sans source</td><td>Chercher la source, sinon supprimer</td></tr>
<tr><td><strong>Confusion d'entités</strong></td><td>Mélanger deux auteurs de même nom</td><td>Vérifier les initiales, la discipline</td></tr>
<tr><td><strong>Citation tronquée</strong></td><td>Une phrase sortie de son contexte</td><td>Retrouver la source originale complète</td></tr>
</table>

<h2>5. Application pratique — vérifier une bibliographie d'article</h2>
<p>Tu demandes à ChatGPT :</p>
<div class="prompt-box">Donne-moi 5 références d'études sur l'apprentissage des langues avec l'IA, publiées après 2020.</div>
<p><strong>Réponse probable de l'IA :</strong> 5 références en format APA parfait, avec auteurs, titres de revues, volumes, pages et DOI. Très convaincant.</p>
<p><strong>Test de vérification :</strong> pour chaque référence, copie le titre exact entre guillemets dans Google Scholar. Résultats possibles :</p>
<ul>
<li><strong>3 références existent</strong> → tu les gardes.</li>
<li><strong>1 référence existe mais parle d'autre chose</strong> → tu la remplaces.</li>
<li><strong>1 référence n'existe nulle part</strong> → tu la supprimes.</li>
</ul>
<p>Résultat : sur 5 références proposées, tu en as gardé 3 valides. Sans vérification, tu aurais cité 2 références fantômes.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Une référence sans vérification est une référence suspecte. Toujours vérifier, jamais supposer.</strong></div>
<p>La règle concrète : <strong>30 secondes par référence</strong>. Copie le titre exact, colle dans Google Scholar, ouvre le DOI si présent. Trois cas :</p>
<ul>
<li><strong>Titre exact + auteur + année correspondent</strong> → valide.</li>
<li><strong>Auteurs ou année différents</strong> → suspecte, remplace.</li>
<li><strong>Aucun résultat</strong> → supprime.</li>
</ul>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Croire qu'un DOI valide = référence valide.</strong> L'IA peut inventer un DOI qui, au clic, donne une page d'erreur ou une page différente.</li>
<li><strong>Ne pas vérifier les références des IA.</strong> Le format impeccable trompe : une fausse référence a souvent un format parfait.</li>
<li><strong>Demander à l'IA de vérifier ses propres références.</strong> Elle a tendance à confirmer ses inventions. Il faut un outil externe (Scholar, DOI, éditeur).</li>
<li><strong>Garder une référence « probable ».</strong> Si tu n'es pas sûr à 100 %, supprime. Un article sans cette référence vaut mieux qu'un article rétracté.</li>
<li><strong>Oublier de dater la vérification.</strong> Note la date à laquelle tu as vérifié. Une référence valide aujourd'hui peut avoir été rétractée dans 6 mois.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>  Référence proposée par l'IA
          │
          ▼
  ┌──────────────────────┐
  │ Copier le titre      │
  │ dans Google Scholar  │
  └──────────┬───────────┘
             │
             ▼
  ┌──────────────────────┐  Non  ┌─────────────┐
  │  Existe + contenu    ├──────▶│ Supprimer   │
  │  correspond ?        │       │ la réf.     │
  └──────────┬───────────┘       └─────────────┘
             │ Oui
             ▼
  ┌──────────────────────┐  Non  ┌─────────────┐
  │  DOI ouvre une page  ├──────▶│ Vérifier    │
  │  officielle ?        │       │ manuellement│
  └──────────┬───────────┘       └─────────────┘
             │ Oui
             ▼
        Référence valide
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Demande toujours les sources.</strong> Sinon l'IA invente.</li>
<li><strong>Donne-lui une porte de sortie honnête :</strong> « si tu n'es pas sûr, écris "Source non vérifiable" ».</li>
<li><strong>Vérifie toi-même dans un outil externe</strong> (Scholar, DOI). L'IA ne se vérifie pas bien elle-même.</li>
<li><strong>30 secondes par référence</strong> : chercher le titre, ouvrir le DOI, juger.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Donne-moi 5 références »</td><td>« Avec sources vérifiables, sinon dis-le »</td></tr>
<tr><td>5 références, 2 inventées</td><td>3 références vérifiées</td></tr>
<tr><td>Belle bibliographie, note catastrophique</td><td>Bibliographie courte mais solide</td></tr>
<tr><td>Risque de rétractation</td><td>Zéro risque</td></tr>
<tr><td><strong>Bilan : trahison académique</strong></td><td><strong>Bilan : travail honnête</strong></td></tr>
</table>"""

# ===================================================================== 44
LOT_2[44] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Voici un problème complexe : [décrire le problème]. Donne ton analyse détaillée et propose une solution argumentée.</div>
<p><em>(À poser à 2 ou 3 modèles différents, puis comparer.)</em></p>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Poser à 2 ou 3 modèles différents »</strong> → Chaque IA a ses forces et ses angles morts. ChatGPT, Claude, Gemini, DeepSeek ne raisonnent pas de la même manière. Un modèle peut voir une solution que les autres ratent.</p>
<p><strong>« Le même prompt mot pour mot »</strong> → Le point clé. Si tu changes un mot entre les deux, la comparaison n'a plus de sens. Le seul moyen de juger correctement est de tout garder identique.</p>
<p><strong>« Compare les approches »</strong> → Tu regardes trois choses : ce qui est <em>commun</em> aux 3 (probablement juste), ce qui est <em>unique</em> à un seul (à vérifier), ce qui est <em>contradictoire</em> (au moins un des trois se trompe).</p>
<p><strong>« Synthétise le meilleur »</strong> → À la fin, tu ne recopies aucun modèle : tu prends ce qui est confirmé par plusieurs, et tu intègres les nuances uniques qui te convainquent.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu demandes un diagnostic médical à trois médecins différents.</p>
<p><strong>Médecin 1 :</strong> « C'est une angine, prenez des antibiotiques. »<br>
<strong>Médecin 2 :</strong> « C'est une angine virale, pas d'antibiotiques, du repos. »<br>
<strong>Médecin 3 :</strong> « Peut-être une angine, il faut un test. »</p>
<p>Trois diagnostics. Que faire ?</p>
<ul>
<li>Deux médecins sur trois disent « angine » → c'est très probablement une angine.</li>
<li>L'un dit « virale », l'autre « bactérienne » → il faut un test pour trancher.</li>
<li>Un seul mentionne le test → c'est le plus prudent, tu le retiens.</li>
</ul>
<p>Les IA fonctionnent pareil. Croiser 3 modèles, c'est comme demander un second, puis un troisième avis médical. Tu ne prends pas la réponse majoritaire aveuglément, tu cherches à comprendre <em>pourquoi</em> elles divergent.</p>

<h2>4. Les 5 patterns de comparaison</h2>
<table>
<tr><th>Pattern</th><th>Interprétation</th><th>Action</th></tr>
<tr><td>Les 3 modèles disent la même chose</td><td>Fort consensus</td><td>Utiliser, mais vérifier les faits</td></tr>
<tr><td>2 sur 3, le 3e dit autre chose</td><td>Un modèle a probablement une erreur</td><td>Chercher la version qui a une source</td></tr>
<tr><td>Chacun dit quelque chose de différent</td><td>Sujet ambigu ou mal cadré</td><td>Reformuler le prompt, réduire la question</td></tr>
<tr><td>Un modèle donne plus de détails</td><td>Ce modèle connaît mieux le sujet</td><td>Garder sa version enrichie</td></tr>
<tr><td>Un modèle refuse de répondre</td><td>La question est sensible ou mal posée</td><td>Examiner pourquoi et reformuler</td></tr>
</table>

<h2>5. Application pratique — comparer trois modèles sur un même sujet</h2>
<p><strong>Prompt à coller dans ChatGPT, Claude et Gemini :</strong></p>
<div class="prompt-box">Explique la différence entre apprentissage supervisé et non supervisé, en 5 phrases pour un étudiant de 2e année PEP. Donne 1 exemple concret pour chacun.</div>
<p><strong>Réponses obtenues :</strong></p>
<ul>
<li><strong>ChatGPT :</strong> 5 puces claires, exemples : photos de chats/chiens et regroupement de clients.</li>
<li><strong>Claude :</strong> 2 paragraphes courts, exemples : détection de spam et segmentation d'images.</li>
<li><strong>Gemini :</strong> 5 puces + proposition de continuer, exemples : spam et catégories Netflix.</li>
</ul>
<p><strong>Analyse :</strong></p>
<ul>
<li>Les 3 sont d'accord sur la définition → tu peux la retenir.</li>
<li>Les exemples varient → tu peux en prendre 3 (un par modèle) pour enrichir ta réponse.</li>
<li>Gemini propose de continuer → utile si tu veux approfondir.</li>
<li>Aucune contradiction → la matière est solide.</li>
</ul>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Même prompt, mot pour mot, sur 2-3 modèles. Puis comparer, pas choisir.</strong></div>
<p>Tu ne choisis pas « le meilleur modèle ». Tu prends ce qui est confirmé par plusieurs (base solide) et tu intègres les nuances uniques qui te convainquent. Résultat : une réponse plus complète que n'importe lequel des modèles pris seul.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Modifier le prompt entre les modèles.</strong> Si tu changes un mot, la comparaison n'a plus de valeur. Le même mot pour mot est une règle absolue.</li>
<li><strong>Choisir le modèle qui donne la réponse la plus longue.</strong> Long ne veut pas dire juste. Un modèle peut noyer une erreur dans beaucoup de texte.</li>
<li><strong>Croire que consensus = vérité.</strong> Deux IA peuvent partager le même biais, ou halluciner la même fausse référence. Le consensus réduit le risque, il ne l'élimine pas.</li>
<li><strong>Croiser sur une question simple.</strong> Pour « quelle heure est-il », un seul modèle suffit. Réserve le croisement aux questions complexes ou importantes.</li>
<li><strong>Ne pas noter les divergences.</strong> Écris-les dans un tableau. Ce sont elles qui t'apprennent le plus.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>     Un prompt unique
           │
     ┌─────┼─────┐
     ▼     ▼     ▼
   GPT  Claude  Gemini
     │     │     │
     ▼     ▼     ▼
  Réponse A B C
           │
           ▼
   ┌───────────────────┐
   │ Comparer          │
   │ - Consensus ?     │
   │ - Divergences ?   │
   │ - Erreurs ?       │
   └────────┬──────────┘
            │
            ▼
    Réponse synthétisée
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Même prompt, mot pour mot.</strong> Sinon la comparaison n'a pas de valeur.</li>
<li><strong>Consensus = base solide.</strong> Divergences = zones à vérifier.</li>
<li><strong>Un modèle peut halluciner, deux aussi.</strong> Le croisement réduit le risque, il ne l'élimine pas.</li>
<li><strong>Réserve le croisement aux questions complexes.</strong> Pas pour tout.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans croisement</th><th>Avec croisement</th></tr>
<tr><td>Une seule réponse</td><td>2-3 réponses comparées</td></tr>
<tr><td>Erreur invisible</td><td>Erreurs repérables par divergence</td></tr>
<tr><td>Tu fais confiance aveuglément</td><td>Tu juges avec recul</td></tr>
<tr><td>Réponse rapide mais fragile</td><td>Réponse un peu plus lente mais solide</td></tr>
<tr><td><strong>Bilan : risque d'erreur</strong></td><td><strong>Bilan : fiabilité accrue</strong></td></tr>
</table>"""

# ===================================================================== 91
LOT_2[91] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Génère 20 cartes question/réponse à partir de ce chapitre.
Format strict :
Q : ...
R : ...
Classe-les par difficulté croissante. Réponse de 5 mots maximum. Une seule notion par carte.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Génère 20 cartes question/réponse »</strong> → Tu produis un ensemble utilisable dans Anki ou Quizlet. 20 cartes couvrent un chapitre de taille moyenne.</p>
<p><strong>« À partir de ce chapitre »</strong> → Tu fournis le texte source. L'IA ne connaît pas ton cours, elle a besoin de le lire. Sans le texte, elle invente.</p>
<p><strong>« Format strict : Q : / R : »</strong> → Tu imposes un format qui se copie directement dans Anki. Sans ça, tu reçois un texte en paragraphes qu'il faut retravailler.</p>
<p><strong>« Classe-les par difficulté croissante »</strong> → Tu répartis les cartes du facile au difficile. Cela te permet de réviser dans un ordre logique, et d'abandonner plus facilement si tu es fatigué.</p>
<p><strong>« Réponse de 5 mots maximum »</strong> → La règle la plus importante. Une réponse courte force le rappel actif : tu ne peux pas te contenter de reconnaître la réponse, tu dois la produire.</p>
<p><strong>« Une seule notion par carte »</strong> → Une carte = une idée. Deux notions sur une même carte te font perdre du temps : si tu rates la carte, tu ne sais pas laquelle des deux notions tu as oubliée.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu révises avec un jeu de cartes à jouer.</p>
<p><strong>Carte mal conçue :</strong> une carte qui contient un paragraphe entier. Tu retournes la carte, tu lis le paragraphe, tu te dis « oui, je vois ». Mais au moment du contrôle, tu ne sauras pas reproduire le paragraphe — tu l'as seulement reconnu.</p>
<p><strong>Carte bien conçue :</strong> une carte avec une question courte et une réponse de 5 mots. Tu essaies de la produire de mémoire, sans regarder. Si tu ne peux pas, tu sais exactement quelle notion travailler.</p>
<p>Le but des flashcards n'est pas de te faire relire, c'est de te forcer à <em>produire</em>. La règle des 5 mots est là pour ça.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Composant</th><th>Pourquoi</th><th>Conséquence si mal fait</th></tr>
<tr><td><strong>20 cartes</strong></td><td>Couverture complète d'un chapitre</td><td>Trop peu = tu manques des notions ; trop = surcharge</td></tr>
<tr><td><strong>Format Q/R strict</strong></td><td>Import direct dans Anki/Quizlet</td><td>Tu passes 30 minutes à reformater</td></tr>
<tr><td><strong>Réponse en 5 mots</strong></td><td>Force le rappel actif</td><td>Tu « reconnais » au lieu d'apprendre</td></tr>
<tr><td><strong>Une notion par carte</strong></td><td>Diagnostic précis</td><td>Tu ne sais pas quoi réviser</td></tr>
<tr><td><strong>Difficulté croissante</strong></td><td>Progression logique</td><td>Tu commences par le dur, tu décroches</td></tr>
</table>

<h2>5. Application pratique — flashcards sur la phonétique anglaise</h2>
<p><strong>Prompt :</strong></p>
<div class="prompt-box">Génère 20 cartes question/réponse à partir de ce chapitre de phonétique anglaise.
Format strict :
Q : [question courte]
R : [réponse de 5 mots maximum]
Classe par difficulté croissante. Une seule notion par carte.
Chapitre : « Un phonème est la plus petite unité distinctive... » [texte complet]</div>
<p><strong>Extrait de réponse :</strong></p>
<ul>
<li><strong>Q1 :</strong> Unité distinctive minimale ? <strong>R :</strong> Le phonème.</li>
<li><strong>Q2 :</strong> Le phonème /p/ a combien d'allophones ? <strong>R :</strong> Deux : [p] et [pʰ].</li>
<li><strong>Q3 :</strong> Paire minimale /pɪt/ /bɪt/ ? <strong>R :</strong> Distingue /p/ et /b/.</li>
<li><strong>Q4 :</strong> Que teste une paire minimale ? <strong>R :</strong> Statut de phonème.</li>
<li><strong>Q5 :</strong> Un allophone modifie-t-il le sens ? <strong>R :</strong> Non, jamais.</li>
</ul>
<p><strong>Utilisation dans Anki :</strong> tu copies les 20 lignes Q/R, tu les importes via le modèle « Basic ». Anki sépare Q et R automatiquement. Résultat : 20 cartes prêtes à réviser.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Une notion par carte, réponse en 5 mots maximum. Une carte qu'on ne peut pas réciter de mémoire n'est pas une flashcard.</strong></div>
<p>La règle de vérification : si tu regardes le recto, essaie de formuler la réponse <strong>à voix haute</strong> avant de retourner la carte. Si tu ne peux pas en 10 secondes, la carte est trop dense ou la réponse trop longue.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Réponse trop longue.</strong> Une réponse en 3 phrases te laisse reconnaître au lieu de rappeler. Coupe à 5 mots.</li>
<li><strong>Deux notions par carte.</strong> Si tu rates, tu ne sais pas quoi réviser. Sépare en deux cartes.</li>
<li><strong>Ne pas importer dans Anki.</strong> Les flashcards restent dans un chat = tu ne les révises pas. Copie-les dans Anki dès la génération.</li>
<li><strong>Ne pas réviser régulièrement.</strong> Anki utilise la répétition espacée. Une carte vue 3 fois en une semaine s'oublie. Une carte vue selon le programme d'Anki reste des mois.</li>
<li><strong>Cartes sur des notions vagues.</strong> « Explique la grammaire générative » n'est pas une carte, c'est une dissertation. Découpe en notions précises.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Ton chapitre
        │
        ▼
   ┌─────────────────┐
   │ IA : 20 cartes  │
   │ Format Q/R      │
   │ Réponse ≤ 5 mots│
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Import dans     │
   │ Anki / Quizlet  │
   └────────┬────────┘
            │
            ▼
   ┌─────────────────┐
   │ Révision        │
   │ espacée :       │
   │ J+1, J+3, J+7…  │
   └─────────────────┘
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Format strict Q/R.</strong> Copie directe dans Anki.</li>
<li><strong>Réponse en 5 mots.</strong> Force le rappel actif.</li>
<li><strong>Une notion par carte.</strong> Permet un diagnostic précis.</li>
<li><strong>Import immédiat.</strong> Un jeu de cartes qui reste dans un chat ne sert à rien.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Fais-moi des flashcards »</td><td>« Format Q/R, réponse 5 mots, 1 notion »</td></tr>
<tr><td>Réponses longues → reconnaissance</td><td>Réponses courtes → rappel actif</td></tr>
<tr><td>Format à retravailler</td><td>Import direct</td></tr>
<tr><td>Révision désordonnée</td><td>Progression par difficulté</td></tr>
<tr><td><strong>Bilan : illusion de maîtrise</strong></td><td><strong>Bilan : mémorisation réelle</strong></td></tr>
</table>"""

# ===================================================================== 100
LOT_2[100] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Formule une phrase de déclaration transparente et académique indiquant que [nom de l'outil, version] a été utilisé pour [reformuler / traduire / proposer un plan], sans générer le contenu scientifique. La responsabilité du contenu reste à l'auteur.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Formule une phrase de déclaration »</strong> → Tu prépares une phrase à insérer dans ton mémoire, ton article, ou ta soutenance. Ce n'est pas une note interne, c'est un texte public.</p>
<p><strong>« Transparente et académique »</strong> → Deux qualités obligatoires. Transparente = tu dis la vérité, sans minimiser. Académique = dans le registre formel utilisé dans les publications.</p>
<p><strong>« Nom de l'outil, version »</strong> → Tu précises <em>quel</em> outil, et <em>quelle version</em>. « ChatGPT (GPT-4o) » et non juste « une IA ». Les versions changent, et la version citée doit être celle qui a servi.</p>
<p><strong>« Pour [reformuler / traduire / proposer un plan] »</strong> → Tu précises <em>la tâche exacte</em>. Pas « l'IA a aidé » mais « l'IA a reformulé le paragraphe 3 ». La nature de l'aide doit être claire.</p>
<p><strong>« Sans générer le contenu scientifique »</strong> → Tu établis la frontière. Le contenu scientifique (hypothèses, méthode, résultats, discussion) est <em>ton</em> travail. L'IA a seulement touché à la forme.</p>
<p><strong>« La responsabilité du contenu reste à l'auteur »</strong> → Tu assumes. C'est la phrase qui dit : « je signe, donc je suis responsable ». C'est l'engagement que les éditeurs attendent.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu écris un livre.</p>
<p><strong>Sans déclaration :</strong> tu remets ton manuscrit. Quelqu'un découvre que tu as fait corriger l'orthographe par un logiciel. Tu passes pour quelqu'un qui cache ses outils. Aucun problème si tu l'avais dit — un problème si tu l'as caché.</p>
<p><strong>Avec déclaration :</strong> tu ajoutes une note en début d'ouvrage : « Ce manuscrit a été corrigé orthographiquement par Antidote. Les idées, la structure et le contenu sont de l'auteur. » Personne ne t'accuse de rien. Tu es honnête.</p>
<p>La déclaration d'usage de l'IA fonctionne exactement comme ça. Ce n'est pas un aveu, c'est une preuve de sérieux.</p>

<h2>4. Les composants d'une bonne déclaration</h2>
<table>
<tr><th>Élément</th><th>Obligatoire ?</th><th>Exemple</th></tr>
<tr><td>Nom de l'outil</td><td>Oui</td><td>ChatGPT</td></tr>
<tr><td>Version ou modèle</td><td>Oui</td><td>GPT-4o, Claude 3.5 Sonnet, Gemini 1.5</td></tr>
<tr><td>Tâche exacte</td><td>Oui</td><td>Reformulation, traduction, correction linguistique</td></tr>
<tr><td>Sections concernées</td><td>Recommandé</td><td>« dans le paragraphe 3 de l'introduction »</td></tr>
<tr><td>Clause de responsabilité</td><td>Oui</td><td>« L'auteur assume la responsabilité du contenu »</td></tr>
<tr><td>Date d'utilisation</td><td>Optionnel</td><td>« utilisé en octobre 2026 »</td></tr>
</table>

<h2>5. Application pratique — déclaration pour un mémoire de master</h2>
<p><strong>Phrase à insérer dans la section Méthodologie ou Remerciements :</strong></p>
<div class="ok">« Dans le cadre de ce travail, ChatGPT (version GPT-4o) et DeepL ont été utilisés pour la reformulation linguistique de certains paragraphes et la traduction de citations en langue étrangère. Aucune donnée, hypothèse, analyse ou résultat n'a été produit par ces outils. L'auteur assume l'entière responsabilité du contenu scientifique et des conclusions présentées dans ce mémoire. »</div>
<p><strong>Pourquoi cette phrase fonctionne :</strong></p>
<ul>
<li><strong>Outil nommé</strong> → pas de « une IA » vague.</li>
<li><strong>Version précisée</strong> → GPT-4o, pas juste ChatGPT.</li>
<li><strong>Tâche exacte</strong> → reformulation + traduction, pas « aide à la rédaction ».</li>
<li><strong>Frontière claire</strong> → « aucune donnée, hypothèse, analyse ou résultat ».</li>
<li><strong>Responsabilité</strong> → « l'auteur assume ».</li>
</ul>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Déclarer n'est pas un aveu, c'est une preuve de sérieux. La déclaration doit nommer l'outil, la version et la tâche.</strong></div>
<p>Une déclaration floue (« l'IA a aidé ») est suspecte. Une déclaration précise (« ChatGPT 4o a reformulé 3 paragraphes de l'introduction ») est sérieuse. La différence : la précision.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Ne rien déclarer.</strong> Aujourd'hui, c'est la faute la plus grave. Les revues exigent la transparence depuis 2023-2024, et les éditeurs partagent leurs signalements.</li>
<li><strong>Nommer l'IA comme co-auteur.</strong> Interdit par Nature, Science, Elsevier et la plupart des éditeurs. L'IA ne peut pas assumer la responsabilité.</li>
<li><strong>Déclaration floue.</strong> « Une IA a aidé à améliorer le texte » n'est pas une déclaration, c'est un évitement. Nomme l'outil et la version.</li>
<li><strong>Déclaration exagérée.</strong> « L'IA a écrit tout le texte » alors qu'elle a seulement corrigé l'orthographe — tu te pénalises toi-même sans raison.</li>
<li><strong>Oublier la version.</strong> Les modèles évoluent. La version citée doit être celle qui a réellement servi. Note-la au moment de l'usage, pas à la fin du travail.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Usage réel de l'IA
        │
        ▼
   ┌──────────────────────┐
   │ Quoi ?  (outil)      │  → ChatGPT, DeepL, Claude…
   │ Qui ?   (version)    │  → GPT-4o, 3.5 Sonnet…
   │ Comment ? (tâche)    │  → reformulation, traduction…
   │ Où ?    (sections)   │  → introduction, p. 3…
   │ Qui assume ?         │  → l'auteur
   └──────────┬───────────┘
              │
              ▼
      Déclaration honnête
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Déclarer est obligatoire</strong> dans la plupart des revues depuis 2023.</li>
<li><strong>Nommer l'outil + la version + la tâche.</strong> Pas de déclaration vague.</li>
<li><strong>L'IA ne peut pas être co-auteur.</strong> Jamais.</li>
<li><strong>La responsabilité reste à l'auteur.</strong> C'est la phrase-clé.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans déclaration</th><th>Avec déclaration</th></tr>
<tr><td>Risque de rétractation</td><td>Sécurité éditoriale</td></tr>
<tr><td>Perte de crédibilité si découvert</td><td>Crédibilité renforcée</td></tr>
<tr><td>Soupçon de plagiat</td><td>Preuve de rigueur</td></tr>
<tr><td>Rejet possible de l'article</td><td>Acceptation facilitée</td></tr>
<tr><td><strong>Bilan : risque majeur</strong></td><td><strong>Bilan : sérénité</strong></td></tr>
</table>"""