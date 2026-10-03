#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lot 3 — explications détaillées des astuces 1, 7, 8, 9 et 10.

Contenu rédigé à la main par le professeur, 10 sections par astuce.
"""

LOT_3 = {}

# ===================================================================== 1
LOT_3[1] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Quand ChatGPT affiche « limite atteinte » : ne panique pas.
1. Regroupe 5 petits messages en UN SEUL prompt avec tout le contexte.
2. Si c'est encore bloqué, décale (les quotas se réinitialisent en quelques heures).
3. Puis alterne (utilise un autre outil, astuce 2).</div>
<p><strong>Réflexe :</strong> avant d'envoyer, demande-toi « est-ce que je peux regrouper 3 questions en 1 message ? »</p>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Quand ChatGPT affiche limite atteinte »</strong> → Les versions gratuites imposent un nombre maximal d'échanges sur une période. Ce message arrive plus vite qu'on ne le pense : 15-20 messages dans l'heure et vous y êtes. Ce n'est pas un bug, c'est une limite commerciale.</p>
<p><strong>« Regroupe 5 petits messages en UN SEUL prompt »</strong> → C'est le geste principal. Au lieu d'envoyer 5 questions séparées qui consomment 5 échanges, tu envoies UN message contenant les 5 questions. Résultat : 1 échange consommé, 5 réponses obtenues.</p>
<p><strong>« Avec tout le contexte »</strong> → Le contexte (qui tu es, ton niveau, ton objectif) n'est écrit qu'une seule fois. Pas besoin de le répéter à chaque question. Cela évite aussi que l'IA « perde le fil » entre deux messages.</p>
<p><strong>« Si c'est encore bloqué, décale »</strong> → Le mot « décale » veut dire : attends. Les quotas se rechargent automatiquement (l'interface affiche généralement quand). Tu n'as rien à faire, juste patienter 30 minutes à quelques heures.</p>
<p><strong>« Puis alterne »</strong> → En dernier recours, tu ouvres un autre outil (Gemini, Claude, DeepSeek). Leurs quotas sont indépendants : ce qui bloque sur ChatGPT fonctionne sur Gemini.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu paies ton plein d'essence à la pompe.</p>
<p><strong>Cas 1 :</strong> tu fais 5 petits trajets séparés de 10 km chacun, et à chaque fois tu refais la queue et tu retapes ton code de carte. Tu consommes du temps et de l'énergie pour rien.</p>
<p><strong>Cas 2 :</strong> tu regroupes tout dans un seul trajet de 50 km. Même distance, mais une seule queue, un seul paiement, un seul code.</p>
<p>Avec ChatGPT, c'est pareil. Cinq messages séparés consomment cinq fois le quota, et donnent cinq réponses déconnectées. Un seul message bien structuré consomme un quota et donne une réponse cohérente qui couvre tout.</p>
<p>Et si la pompe est fermée (limite atteinte), tu peux soit attendre la réouverture (décaler), soit aller à la station d'en face (alterner).</p>

<h2>4. Les 3 gestes décomposés</h2>
<table>
<tr><th>Geste</th><th>Quand</th><th>Ce que tu fais concrètement</th></tr>
<tr><td><strong>Regrouper</strong></td><td>Toujours, en prévention</td><td>Fusionner 3 à 5 questions liées en un seul prompt structuré</td></tr>
<tr><td><strong>Décaler</strong></td><td>Limite atteinte, pas urgent</td><td>Attendre la recharge du quota (30 min à quelques heures)</td></tr>
<tr><td><strong>Alterner</strong></td><td>Limite atteinte + urgent</td><td>Ouvrir un autre outil : Gemini, Claude, DeepSeek, Copilot</td></tr>
</table>

<h2>5. Application pratique — préparer une fiche de révision</h2>
<p><strong>Sans regrouper (mauvais) :</strong></p>
<div class="prompt-box">Message 1 : Explique-moi la différence entre past simple et present perfect.
Message 2 : Donne-moi 3 exemples.
Message 3 : Quelles erreurs font les étudiants ?
Message 4 : Comment les retenir ?
Message 5 : Fais-moi un résumé.</div>
<p>5 échanges consommés. 5 réponses séparées à recopier. 5 minutes perdues à relire chaque fragment.</p>
<p><strong>Avec regroupement (bon) :</strong></p>
<div class="prompt-box">Contexte : je suis étudiant en 2e année PEP, niveau B2 en anglais. Je prépare un contrôle sur les temps du passé.
Tâches :
1) Explique la différence past simple / present perfect en 5 phrases.
2) Donne 3 exemples concrets avec traduction.
3) Liste 3 erreurs fréquentes d'étudiants.
4) Donne 2 astuces pour les distinguer rapidement.
5) Résume le tout en un tableau à 2 colonnes.
Format : titres courts, français clair.</div>
<p><strong>Résultat :</strong> 1 échange consommé, une réponse complète et cohérente. Tu as ta fiche de révision en un seul bloc.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Avant chaque envoi : « Est-ce que je peux regrouper 3 questions en 1 message ? »</strong></div>
<p>Cette question, posée en 2 secondes, économise 60 à 80 % du quota. Appliquée systématiquement, elle transforme l'usage de ChatGPT : tu passes de 15 messages frustrants à 3 messages productifs par session.</p>
<p><strong>Règle de tri :</strong> regroupe par <em>thème</em>. Ne mélange pas une question sur la grammaire anglaise et une question sur un script Python dans le même message — le contexte deviendrait confus.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Regrouper 20 questions sans lien.</strong> L'IA se perd, la réponse devient floue. Bonne pratique : 3 à 5 questions <em>liées au même thème</em>.</li>
<li><strong>Répéter le contexte dans chaque message.</strong> Tu consommes du quota pour rien. Écris-le une seule fois, au début du prompt regroupé.</li>
<li><strong>Ne pas profiter du regroupement pour améliorer le prompt.</strong> Regrouper, c'est l'occasion d'appliquer la formule magique (astuce 6) : rôle + contexte + tâches + format + contraintes.</li>
<li><strong>Créer plusieurs comptes pour contourner la limite.</strong> Cela viole les conditions d'utilisation, et tu peux te faire bannir. Alterne entre outils : c'est légal et efficace.</li>
<li><strong>Ne pas écrire le prompt dans un fichier avant d'envoyer.</strong> Un prompt regroupé de 10 lignes se prépare à l'avance. L'écrire dans un fichier te permet de le réutiliser et de l'améliorer.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   5 petites questions
        │
        ├──▶ [Séparé] ──▶ 5 échanges consommés
        │                  réponses fragmentées
        │
        └──▶ [Regroupé] ─▶ 1 échange consommé
                           réponse cohérente

   Si limite atteinte :
        │
        ├──▶ [Décaler] ──▶ attendre la recharge
        │
        └──▶ [Alterner] ─▶ ouvrir un autre outil
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Regrouper = le geste n° 1.</strong> 3 à 5 questions liées en un seul message.</li>
<li><strong>Décaler = attendre.</strong> Les quotas se rechargent seuls.</li>
<li><strong>Alterner = changer d'outil.</strong> ChatGPT, Gemini, Claude ont des quotas indépendants.</li>
<li><strong>Regrouper par thème.</strong> Pas 20 questions sans lien.</li>
<li><strong>Jamais de faux comptes.</strong> Alterner entre outils est légal, créer des comptes ne l'est pas.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>5 messages séparés</td><td>1 message regroupé</td></tr>
<tr><td>5 échanges consommés</td><td>1 échange consommé</td></tr>
<tr><td>Limite atteinte en 20 min</td><td>Session productive d'1 heure</td></tr>
<tr><td>Réponses fragmentées</td><td>Réponse cohérente et complète</td></tr>
<tr><td><strong>Bilan : frustration</strong></td><td><strong>Bilan : efficacité</strong></td></tr>
</table>"""

# ===================================================================== 7
LOT_3[7] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Mon besoin : [2 lignes].
Avant de répondre, pose-moi exactement 3 questions pour clarifier mon besoin.
N'écris pas la réponse tant que je n'ai pas répondu.</div>
<p>Force l'IA à comprendre avant d'écrire. La qualité monte d'un cran immédiatement.</p>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Mon besoin : [2 lignes] »</strong> → Tu donnes une première esquisse de ce que tu veux. Deux lignes suffisent : ni trop vague (« aide-moi »), ni trop précis (sinon les questions n'ont plus d'utilité).</p>
<p><strong>« Avant de répondre, pose-moi exactement 3 questions »</strong> → Tu demandes à l'IA de <em>retarder sa réponse</em> pour mieux comprendre. C'est contre-intuitif : on veut une réponse vite. Mais une réponse précise vaut mieux qu'une réponse rapide.</p>
<p><strong>« Exactement 3 »</strong> → Le nombre 3 est important. Sans nombre, l'IA pose 1 question (insuffisant) ou 10 (trop). Avec 3, elle cible les 3 points les plus importants.</p>
<p><strong>« Pour clarifier mon besoin »</strong> → Tu précises l'objectif des questions. Pas des questions pour questionner, mais des questions pour mieux répondre.</p>
<p><strong>« N'écris pas la réponse tant que je n'ai pas répondu »</strong> → Tu bloques la tentation de l'IA de répondre quand même. Sans cette phrase, elle pose 3 questions puis enchaîne avec une réponse « au cas où ».</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine un médecin.</p>
<p><strong>Médecin pressé :</strong> tu entres, tu dis « j'ai mal », il te prescrit un antidouleur avant même de savoir où tu as mal. Il a répondu en 10 secondes. Et probablement à côté.</p>
<p><strong>Bon médecin :</strong> tu entres, tu dis « j'ai mal ». Il pose 3 questions : « où ? depuis quand ? est-ce que ça irradie ? ». Puis il te prescrit le bon traitement.</p>
<p>L'astuce 7 transforme l'IA en bon médecin. Le coût : 2 minutes de questions. Le gain : une réponse ciblée au lieu d'une réponse à côté.</p>

<h2>4. Les 3 types de questions utiles</h2>
<table>
<tr><th>Type de question</th><th>Exemple</th><th>Ce que ça clarifie</th></tr>
<tr><td><strong>Contexte manquant</strong></td><td>« Quel est ton niveau ? »</td><td>Le registre, la complexité</td></tr>
<tr><td><strong>Objectif</strong></td><td>« Pour quel usage final ? (exposé, devoir, oral) »</td><td>La structure, la longueur</td></tr>
<tr><td><strong>Contraintes</strong></td><td>« Combien de temps / de mots / d'exemples ? »</td><td>Le format, la densité</td></tr>
</table>
<p>Les 3 questions de l'IA couvrent généralement ces 3 axes. Tu réponds, puis tu obtiens une réponse taillée sur mesure.</p>

<h2>5. Application pratique — préparer un exposé</h2>
<p><strong>Sans l'astuce :</strong></p>
<div class="prompt-box">Aide-moi pour un exposé sur le théâtre de Shakespeare.</div>
<p>Réponse : 800 mots généralistes sur Shakespeare, sa vie, ses œuvres, son influence. Utile pour rien. Tu passes 15 minutes à trier pour en tirer 3 idées.</p>
<p><strong>Avec l'astuce :</strong></p>
<div class="prompt-box">Mon besoin : je prépare un exposé sur le théâtre de Shakespeare.
Avant de répondre, pose-moi exactement 3 questions pour clarifier mon besoin.
N'écris pas la réponse tant que je n'ai pas répondu.</div>
<p><strong>Réponse de l'IA :</strong></p>
<ol>
<li>Quelle est la durée de ton exposé et quel est ton niveau (L1, L2, L3) ?</li>
<li>Souhaites-tu un panorama de son théâtre, l'analyse d'une œuvre précise, ou un angle thématique particulier ?</li>
<li>Quel est le public (étudiants, professeur, jury) et quel est le ton attendu (académique, pédagogique, créatif) ?</li>
</ol>
<p><strong>Tes réponses :</strong></p>
<ul>
<li>10 minutes, niveau L2.</li>
<li>Analyse d'une œuvre : Macbeth.</li>
<li>Public : étudiant + professeur. Ton académique mais accessible.</li>
</ul>
<p><strong>Réponse finale de l'IA :</strong> un plan en 3 parties sur Macbeth, avec 2 exemples par partie, adapté à un exposé de 10 minutes. Directement utilisable. Zéro temps perdu.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Quand le besoin est vague : « Pose-moi 3 questions avant de répondre. »</strong></div>
<p>Ce réflexe couvre tous les cas où tu ne sais pas exactement quoi demander :</p>
<ul>
<li>Au début d'un projet (avant de connaître la structure).</li>
<li>Quand tu découvres un sujet (avant d'avoir les idées claires).</li>
<li>Pour les exposés, mémoires, articles (avant d'avoir le plan).</li>
</ul>
<p>Ne l'utilise pas pour des questions factuelles simples (« quelle heure est-il à Alger ? ») : ce serait 3 questions pour rien.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Répondre « comme tu veux ».</strong> Sans précision, l'IA retombe dans une réponse générique. Prends le temps de répondre aux 3 questions.</li>
<li><strong>Ne pas répondre aux questions.</strong> Certains prompts posent les questions puis enchaînent directement. Réponds-y dans un message séparé.</li>
<li><strong>Demander 10 questions.</strong> Trop de questions = tu perds du temps. 3 est le nombre optimal : assez pour cadrer, pas trop pour bloquer.</li>
<li><strong>Poser la question sans contexte initial.</strong> Si tu écris juste « pose-moi 3 questions », l'IA ne sait pas de quel sujet. Donne au moins le thème.</li>
<li><strong>Utiliser l'astuce pour des questions simples.</strong> « Quelle est la capitale de la France ? » → pas besoin de questions clarifiantes.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Ton besoin (2 lignes)
        │
        ▼
   ┌─────────────────────┐
   │ IA : 3 questions    │
   │ 1. Contexte ?       │
   │ 2. Objectif ?       │
   │ 3. Contraintes ?    │
   └──────────┬──────────┘
              │
              ▼
   Tes réponses précises
              │
              ▼
   ┌─────────────────────┐
   │ Réponse ciblée      │
   │ (mieux que 10       │
   │  échanges flous)    │
   └─────────────────────┘
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>3 questions, pas plus, pas moins.</strong> Assez pour cadrer, pas trop pour bloquer.</li>
<li><strong>Réponds précisément aux 3 questions.</strong> Ne dis pas « comme tu veux ».</li>
<li><strong>Utilise-le quand le besoin est vague.</strong> Exposé, mémoire, projet.</li>
<li><strong>Combinaison gagnante :</strong> astuce 7 (questions) + astuce 6 (formule magique) = réponse parfaite.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>Prompt de 2 lignes vague</td><td>Prompt + 3 questions ciblées</td></tr>
<tr><td>Réponse générique</td><td>Réponse précise</td></tr>
<tr><td>Tu tries 10 minutes</td><td>Tu utilises tout de suite</td></tr>
<tr><td>Tu dois relancer 3 fois</td><td>Une seule réponse suffisante</td></tr>
<tr><td><strong>Bilan : temps perdu</strong></td><td><strong>Bilan : temps gagné</strong></td></tr>
</table>"""

# ===================================================================== 8
LOT_3[8] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Explique [notion] en deux niveaux :
Niveau 1 : comme à un enfant de 10 ans, 4 phrases maximum.
Niveau 2 : pour un étudiant de licence, avec le vocabulaire technique et un exemple.
Sépare bien les deux niveaux.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Explique en deux niveaux »</strong> → Tu demandes la même notion sous deux formes. C'est la clé de l'astuce : ce n'est pas une explication, ce sont <em>deux explications juxtaposées</em>.</p>
<p><strong>« Niveau 1 : comme à un enfant de 10 ans, 4 phrases maximum »</strong> → Tu demandes une version ultra-simple. En 4 phrases, il faut éliminer tout le superflu et ne garder que l'image mentale de base. C'est ce niveau qui te fait <em>comprendre</em>.</p>
<p><strong>« Niveau 2 : pour un étudiant de licence, avec le vocabulaire technique »</strong> → Tu demandes la version exacte, celle que tu utiliseras dans une copie ou un examen. C'est ce niveau qui te fait <em>savoir formuler</em>.</p>
<p><strong>« Sépare bien les deux niveaux »</strong> → Sans séparation claire, l'IA mélange les deux et tu ne sais plus quel niveau tu lis. La séparation te permet de mémoriser les deux versions côte à côte.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu apprends à nager.</p>
<p><strong>Niveau 1 (image simple) :</strong> « Tu écartes les bras, tu mets la tête sous l'eau, tu souffles. » C'est ce que tu retiens le premier jour.</p>
<p><strong>Niveau 2 (vocabulaire exact) :</strong> « Tu synchronises la rotation des bras avec la respiration latérale en trois temps, le battement de jambes part du bassin et non du genou. » C'est ce que tu apprends quand tu veux perfectionner.</p>
<p>Les deux niveaux coexistent dans la tête d'un bon nageur. Le premier donne l'image mentale qui ne s'oublie pas. Le second donne la précision technique qui fait progresser.</p>
<p>Pour une notion de cours, c'est pareil : le niveau 1 est la <em>version mémoire</em>, le niveau 2 est la <em>version copie</em>.</p>

<h2>4. Les deux niveaux décomposés</h2>
<table>
<tr><th>Niveau</th><th>Public visé</th><th>Caractéristiques</th><th>Utilisation</th></tr>
<tr><td><strong>Niveau 1</strong></td><td>Enfant de 10 ans</td><td>4 phrases, image simple, pas de jargon</td><td>Mémoriser le concept, expliquer à un ami</td></tr>
<tr><td><strong>Niveau 2</strong></td><td>Étudiant de licence</td><td>Vocabulaire technique, exemple précis, rigueur</td><td>Répondre en examen, rédiger une copie</td></tr>
</table>

<h2>5. Application pratique — expliquer la phonologie</h2>
<p><strong>Prompt :</strong></p>
<div class="prompt-box">Explique la notion de phonème en deux niveaux :
Niveau 1 : comme à un enfant de 10 ans, 4 phrases maximum.
Niveau 2 : pour un étudiant de licence de linguistique, avec le vocabulaire technique et un exemple.
Sépare bien les deux niveaux.</div>
<p><strong>Réponse de l'IA :</strong></p>
<p><strong>Niveau 1 :</strong> Les phonèmes sont les plus petits sons d'une langue qui changent le sens des mots. Par exemple, « pain » et « bain » ne se ressemblent pas à cause d'un seul son. Ce son, c'est un phonème. C'est comme une brique : avec peu de briques différentes, on construit des milliers de mots.</p>
<p><strong>Niveau 2 :</strong> Un phonème est la plus petite unité distinctive dépourvue de sens propre, dont la substitution dans un contexte donné entraîne un changement de sens. Les phonèmes se définissent par opposition dans le système d'une langue donnée (les paires minimales, comme /pɛ̃/ et /bɛ̃/, en fournissent la preuve empirique). Ils se réalisent en surface sous forme d'allophones, qui sont des variantes contextuelles non distinctives (par exemple, le /p/ français se réalise [p] ou [pʰ] selon le contexte sans changer le sens).</p>
<p><strong>Ce que tu fais ensuite :</strong></p>
<ul>
<li><strong>Tu retiens le niveau 1</strong> à voix haute. Tu peux l'expliquer à n'importe qui.</li>
<li><strong>Tu apprends le niveau 2</strong> comme matériau à recopier en examen.</li>
<li><strong>Tu relies les deux</strong> : la brique et l'unité distinctive.</li>
</ul>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Deux niveaux, deux usages : niveau 1 pour comprendre, niveau 2 pour rendre.</strong></div>
<p>La règle concrète : pour chaque nouvelle notion, demande les 2 niveaux. Cela te donne :</p>
<ul>
<li><strong>Une image mentale</strong> qui ne s'oublie pas (niveau 1).</li>
<li><strong>Un vocabulaire technique</strong> que le correcteur attend (niveau 2).</li>
<li><strong>Une liaison</strong> entre les deux, qui prouve ta compréhension.</li>
</ul>
<p>Cette astuce vaut plus que la relecture de 3 pages de cours. C'est du temps bien investi.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>S'arrêter au niveau 1.</strong> Tu comprends, mais tu ne sais pas formuler en examen. Le niveau 2 est obligatoire.</li>
<li><strong>Sauter au niveau 2 directement.</strong> Tu copies du jargon sans comprendre. Tu peux réciter, mais tu ne peux pas expliquer.</li>
<li><strong>Ne pas faire le lien entre les deux.</strong> Le niveau 1 et le niveau 2 doivent se répondre. Si tu ne vois pas le lien, c'est que tu n'as pas bien compris.</li>
<li><strong>Demander 3 niveaux ou plus.</strong> Au-delà de 2, l'IA perd en clarté. Reste à 2 : simple + technique.</li>
<li><strong>Ne pas s'entraîner à dire le niveau 1 à voix haute.</strong> L'image mentale se construit en la <em>disant</em>, pas en la lisant.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Une notion
        │
        ├──▶ Niveau 1 : image simple (4 phrases)
        │    ├─▶ Pour COMPRENDRE
        │    └─▶ Pour EXPLIQUER à un ami
        │
        └──▶ Niveau 2 : vocabulaire technique
             ├─▶ Pour RÉDIGER en examen
             └─▶ Pour PRÉCISER à l'écrit
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Deux niveaux, pas un.</strong> Le niveau 1 sans le 2 = tu comprends sans savoir formuler. Le 2 sans le 1 = tu répètes sans comprendre.</li>
<li><strong>Niveau 1 à dire à voix haute.</strong> L'image mentale se fixe en la prononçant.</li>
<li><strong>Niveau 2 à écrire.</strong> C'est ce qui apparaît sur ta copie.</li>
<li><strong>Le lien entre les deux</strong> est la preuve que tu as vraiment compris.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>Une seule explication</td><td>Deux niveaux complémentaires</td></tr>
<tr><td>Soit trop simple, soit trop technique</td><td>Les deux à la fois</td></tr>
<tr><td>Tu répètes du jargon</td><td>Tu comprends et tu formules</td></tr>
<tr><td>Révision superficielle</td><td>Révision en profondeur</td></tr>
<tr><td><strong>Bilan : illusion de savoir</strong></td><td><strong>Bilan : vraie maîtrise</strong></td></tr>
</table>"""

# ===================================================================== 9
LOT_3[9] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Réponds UNIQUEMENT sous forme de tableau à 3 colonnes :
| Étape | Action concrète | Temps estimé |
5 lignes maximum. Rien d'autre avant ou après le tableau.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Réponds UNIQUEMENT »</strong> → Le mot « uniquement » en majuscules est un signal fort. Sans lui, l'IA ajoute toujours une introduction (« Voici un tableau qui… ») et une conclusion (« J'espère que ce tableau vous aidera… »). Tu veux juste le tableau, rien de plus.</p>
<p><strong>« Sous forme de tableau à 3 colonnes »</strong> → Tu imposes la structure. Sans cette précision, tu obtiens soit un paragraphe, soit une liste à puces, soit un tableau à 2 ou 5 colonnes. Tu veux 3 colonnes, tu demandes 3 colonnes.</p>
<p><strong>« | Étape | Action concrète | Temps estimé | »</strong> → Tu montres le gabarit exact. C'est encore mieux que « 3 colonnes » : tu montres à l'IA <em>quel contenu</em> va dans chaque colonne. Le résultat est immédiatement exploitable.</p>
<p><strong>« 5 lignes maximum »</strong> → Tu bornes la longueur. Sans cette limite, l'IA peut produire 15 lignes quand tu en veux 5. La contrainte t'oblige à ne garder que l'essentiel.</p>
<p><strong>« Rien d'autre avant ou après le tableau »</strong> → Tu interdis les formules de politesse. C'est la phrase qui transforme une réponse « polie » en réponse « copiable ».</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu commandes un meuble en kit.</p>
<p><strong>Cas 1 (mauvais) :</strong> tu dis « envoie-moi les instructions ». Tu reçois une lettre de 3 pages avec des blablas (« Nous sommes ravis de vous compter parmi nos clients… »), puis les étapes noyées dans le texte.</p>
<p><strong>Cas 2 (bon) :</strong> tu dis « je veux un tableau de montage : Étape | Pièce | Outil | Temps ». Tu reçois exactement ça, sur une page, collable sur le mur à côté du meuble.</p>
<p>Avec l'IA, c'est pareil. Un format imposé = une réponse utilisable. Pas de format = une réponse à retravailler.</p>

<h2>4. Les formats courants et leur usage</h2>
<table>
<tr><th>Format</th><th>Syntaxe à écrire</th><th>Cas d'usage</th></tr>
<tr><td><strong>Tableau</strong></td><td>| Col 1 | Col 2 | Col 3 |</td><td>Comparer, organiser, résumer</td></tr>
<tr><td><strong>Liste numérotée</strong></td><td>1. … 2. … 3. …</td><td>Étapes dans l'ordre</td></tr>
<tr><td><strong>Liste à puces</strong></td><td>- … - … - …</td><td>Éléments sans ordre</td></tr>
<tr><td><strong>JSON</strong></td><td>{ "clé": "valeur" }</td><td>Traitement par un script</td></tr>
<tr><td><strong>YAML</strong></td><td>clé: valeur</td><td>Configuration lisible</td></tr>
<tr><td><strong>Checklist</strong></td><td>☐ … ☐ … ☐ …</td><td>Suivi de tâches</td></tr>
<tr><td><strong>Markdown pur</strong></td><td># Titre ## Sous-titre</td><td>Document structuré</td></tr>
</table>

<h2>5. Application pratique — préparer un oral d'anglais</h2>
<p><strong>Sans format imposé :</strong></p>
<div class="prompt-box">Comment préparer un oral d'anglais de 10 minutes ?</div>
<p>Réponse : 600 mots de conseils généraux en paragraphes. Tu dois extraire 5 étapes à la main.</p>
<p><strong>Avec format imposé :</strong></p>
<div class="prompt-box">Réponds UNIQUEMENT sous forme de tableau à 3 colonnes :
| Étape | Action concrète | Temps estimé |
5 lignes maximum. Rien d'autre avant ou après le tableau.</div>
<p><strong>Réponse obtenue :</strong></p>
<table>
<tr><th>Étape</th><th>Action concrète</th><th>Temps estimé</th></tr>
<tr><td>1</td><td>Choisir le sujet et formuler la problématique</td><td>20 min</td></tr>
<tr><td>2</td><td>Rédiger le plan en 3 parties</td><td>30 min</td></tr>
<tr><td>3</td><td>Écrire l'intro et la conclusion</td><td>40 min</td></tr>
<tr><td>4</td><td>S'enregistrer et écouter</td><td>20 min</td></tr>
<tr><td>5</td><td>Répéter à voix haute chronométré</td><td>30 min</td></tr>
</table>
<p><strong>Tu peux coller ce tableau dans ton cahier de préparation</strong>, ou dans ton Google Docs. Aucune reformulation. Aucun tri. Utilisation immédiate.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Avant d'envoyer, demande-toi : « Sous quelle forme je veux la réponse ? »</strong></div>
<p>Puis impose ce format. Trois formats couvrent 90 % des cas :</p>
<ul>
<li><strong>Tableau</strong> : quand tu compares ou organises.</li>
<li><strong>Liste numérotée</strong> : quand il y a un ordre.</li>
<li><strong>Liste à puces</strong> : quand il n'y a pas d'ordre.</li>
</ul>
<p>Ajoute toujours : « Rien d'autre avant ou après ». Cela élimine les politesses inutiles.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Oublier « Rien d'autre ».</strong> Sans cette phrase, l'IA ajoute toujours un paragraphe d'introduction et de conclusion. Tu perds 5 secondes à les supprimer à chaque fois.</li>
<li><strong>Ne pas préciser les colonnes.</strong> Tu écris « fais un tableau », tu obtiens 3 colonnes quand tu en voulais 4. Précise : « tableau à 4 colonnes : A | B | C | D ».</li>
<li><strong>Ne pas limiter la longueur.</strong> Un tableau sans limite de lignes devient illisible. Ajoute « 5 lignes max » ou « 10 lignes max ».</li>
<li><strong>Ne pas écrire le format entre balises.</strong> « tableau à 3 colonnes : | Étape | Action | Temps | » est plus clair que « tableau à 3 colonnes avec étape, action et temps ». Le gabarit montre, l'énoncé décrit.</li>
<li><strong>Changer le format en cours de conversation.</strong> Si tu demandes un tableau, puis une liste, puis un JSON, l'IA s'y perd. Un format par demande.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Ta demande
        │
        ▼
   ┌──────────────────────┐
   │  Quel format ?       │
   │  - Tableau           │
   │  - Liste             │
   │  - JSON              │
   │  - Checklist         │
   └──────────┬───────────┘
              │
              ▼
   Prompt avec gabarit :
   | Col A | Col B | Col C |
   + « 5 lignes max »
   + « Rien d'autre »
              │
              ▼
   Réponse copiable
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Impose le format explicitement.</strong> Sinon tu obtiens des paragraphes par défaut.</li>
<li><strong>Montre le gabarit</strong> : | Col 1 | Col 2 | Col 3 |.</li>
<li><strong>Limite la longueur</strong> : 5 lignes, 10 lignes.</li>
<li><strong>Termine par « Rien d'autre avant ou après »</strong> pour supprimer les politesses.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Fais un résumé »</td><td>« Tableau 3 colonnes, 5 lignes, rien d'autre »</td></tr>
<tr><td>Paragraphe de 400 mots</td><td>Tableau de 5 lignes</td></tr>
<tr><td>Tu extrais à la main</td><td>Tu copies-colles</td></tr>
<tr><td>Format incontrôlé</td><td>Format exact</td></tr>
<tr><td><strong>Bilan : 5 min de tri</strong></td><td><strong>Bilan : 5 sec d'utilisation</strong></td></tr>
</table>"""

# ===================================================================== 10
LOT_3[10] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Donne-moi 3 exemples corrects de [notion] et 3 contre-exemples (erreurs que des étudiants font réellement), avec une phrase d'explication pour chaque.</div>

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Donne-moi 3 exemples corrects »</strong> → Les exemples corrects montrent ce qu'il faut <em>faire</em>. Ils donnent le modèle à reproduire. Trois suffisent : au-delà, l'IA commence à répéter.</p>
<p><strong>« Et 3 contre-exemples »</strong> → Les contre-exemples montrent ce qu'il ne faut <em>pas</em> faire. C'est la partie la plus utile : la plupart des erreurs d'examen sont des <em>erreurs de frontière</em> — tu appliques bien la règle dans 90 % des cas, mais tu te trompes sur les cas limites. Les contre-exemples révèlent ces cas limites.</p>
<p><strong>« Erreurs que des étudiants font réellement »</strong> → Cette précision est cruciale. Sans elle, l'IA invente des erreurs absurdes que personne ne commet. Avec, elle puise dans les erreurs typiques, celles que tu risques réellement de faire.</p>
<p><strong>« Avec une phrase d'explication pour chaque »</strong> → Chaque exemple doit être <em>expliqué</em>. Sinon tu retiens l'exemple mais pas la règle. L'explication transforme l'exemple en leçon.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu apprends à conduire.</p>
<p><strong>Le moniteur te montre le bon geste :</strong> « Tourne le volant à 10h-14h pour un virage serré, 9h-15h pour un virage doux. » Tu comprends la règle.</p>
<p><strong>Mais le moniteur te montre aussi les erreurs :</strong> « Attention, si tu tiens le volant à 12h-6h, tu ne peux pas tourner rapidement. Et si tu croises les bras au lieu de les faire glisser, tu perds le contrôle. »</p>
<p>Ces deux informations sont complémentaires. Le bon geste te montre <em>quoi faire</em>, les erreurs te montrent <em>quoi éviter</em>. Sans les erreurs, tu penses savoir — jusqu'à ce que tu doives réagir vite et que tu reproduises le mauvais geste.</p>
<p>Pour une notion de cours, c'est pareil. Les exemples corrects te donnent la cible. Les contre-exemples te donnent les pièges.</p>

<h2>4. Les deux composants décomposés</h2>
<table>
<tr><th>Type</th><th>Rôle</th><th>Exemple pour la notion « accord sujet-verbe »</th></tr>
<tr><td><strong>Exemple correct</strong></td><td>Montrer le modèle</td><td>« Les étudiants travaillent » (accord pluriel)</td></tr>
<tr><td><strong>Contre-exemple</strong></td><td>Montrer le piège</td><td>« Les étudiants travaille » (erreur fréquente)</td></tr>
<tr><td><strong>Explication</strong></td><td>Fixer la règle</td><td>« Le sujet est au pluriel, le verbe doit prendre la marque -ent »</td></tr>
</table>

<h2>5. Application pratique — les connecteurs logiques</h2>
<p><strong>Prompt :</strong></p>
<div class="prompt-box">Donne-moi 3 exemples corrects de l'usage des connecteurs logiques dans une dissertation, et 3 contre-exemples (erreurs que des étudiants font réellement), avec une phrase d'explication pour chaque.</div>
<p><strong>Réponse de l'IA :</strong></p>
<p><strong>Exemples corrects :</strong></p>
<ol>
<li><em>« La littérature populaire est accessible ; cependant, elle peut porter une réelle valeur littéraire. »</em><br>Explication : « cependant » introduit une opposition claire entre deux propositions.</li>
<li><em>« Non seulement le roman populaire touche un large public, mais il influence aussi la production savante. »</em><br>Explication : « non seulement… mais aussi » ajoute un second argument sans opposer.</li>
<li><em>« Si l'hypothèse d'une littérature mineure est séduisante, elle reste contestable. »</em><br>Explication : « si » introduit une concession, suivie d'une réfutation.</li>
</ol>
<p><strong>Contre-exemples (erreurs réelles) :</strong></p>
<ol>
<li><em>« La littérature populaire est accessible, par contre elle est aussi mineure. »</em><br>Explication : « par contre » est familier et n'a pas sa place dans un registre académique. Remplacer par « cependant » ou « en revanche ».</li>
<li><em>« D'abord, l'auteur affirme que… Ensuite, il en va de même pour… »</em><br>Explication : « ensuite » annonce un ordre chronologique, pas un enchaînement d'arguments. Utiliser « de plus » ou « en outre ».</li>
<li><em>« Donc, comme on peut le voir, l'œuvre est populaire parce que c'est évident. »</em><br>Explication : « parce que c'est évident » est un raisonnement circulaire. On n'argumente pas par l'évidence.</li>
</ol>
<p><strong>Ce que tu fais ensuite :</strong> tu copies ces 6 cas dans ta fiche. Le jour de la dissertation, tu reconnais les pièges et tu utilises les bons connecteurs.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Demande toujours des contre-exemples « que des étudiants font réellement ».</strong></div>
<p>Sans cette précision, l'IA invente des erreurs absurdes (qu'elle appelle « erreurs », mais que personne ne commet). Avec la précision, elle puise dans les erreurs typiques — celles qui te coûteront des points.</p>
<p>La règle complète : <strong>exemples corrects + contre-exemples réels + explication pour chacun.</strong></p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Ne demander que des exemples corrects.</strong> Tu connais la règle mais tu ne vois pas les pièges. Le jour J, tu tombes dans un cas limite.</li>
<li><strong>Accepter des contre-exemples invraisemblables.</strong> Une « erreur » que personne ne fait ne t'apprend rien. Demande « des erreurs que des étudiants font réellement ».</li>
<li><strong>Ne pas exiger l'explication.</strong> Sans explication, tu retiens l'exemple mais pas la règle. Le lendemain, tu ne peux pas reproduire.</li>
<li><strong>Trop demander (10 exemples au lieu de 3).</strong> Au-delà de 3, l'IA répète les mêmes idées sous d'autres formes. La qualité baisse.</li>
<li><strong>Ne pas relier exemple et contre-exemple.</strong> Le contre-exemple doit être la <em>négation directe</em> de l'exemple. Sinon tu compares deux choses qui n'ont pas de lien.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   Une notion
        │
        ├──▶ Exemple correct ───▶ Quoi FAIRE
        │       + explication
        │
        └──▶ Contre-exemple ────▶ Quoi ÉVITER
                + explication
                (erreurs réelles)
        │
        ▼
   Compréhension complète
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>3 exemples + 3 contre-exemples.</strong> Pas plus, pas moins.</li>
<li><strong>Contre-exemples « que des étudiants font réellement ».</strong> Cette précision change tout.</li>
<li><strong>Une explication pour chaque.</strong> Sans explication, tu retiens l'exemple mais pas la règle.</li>
<li><strong>Exemple et contre-exemple doivent se répondre.</strong> Le contre-exemple nie l'exemple.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Donne-moi des exemples »</td><td>« 3 exemples + 3 contre-exemples réels + explication »</td></tr>
<tr><td>Tu vois la cible, pas les pièges</td><td>Tu vois cible + pièges</td></tr>
<tr><td>Tu tombes dans les cas limites</td><td>Tu les repères à l'avance</td></tr>
<tr><td>Révision partielle</td><td>Révision complète</td></tr>
<tr><td><strong>Bilan : faux sentiment de maîtrise</strong></td><td><strong>Bilan : vraie préparation</strong></td></tr>
</table>"""