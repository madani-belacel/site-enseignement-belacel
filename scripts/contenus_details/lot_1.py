#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lot 1 — explications détaillées des astuces 6, 12, 23, 35 et 37.

Contenu rédigé à la main par le professeur, selon le gabarit validé en 10
sections. Le générateur ajoute la charpente : en-tête, fil d'Ariane, pied de
page, navigation précédent/suivant, canonical.

Le repère « SOURCE » reçoit le bloc HTML réel de l'astuce, recopié depuis la
page des 152 astuces, afin que la section 1 reste automatiquement à jour.
"""

LOT_1 = {}

# ===================================================================== 6
LOT_1[6] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Tu es [rôle précis].
Contexte : je suis [qui, niveau, objectif].
Tâche : [une seule action].
Format : [liste / tableau / 5 puces / 150 mots].
Contraintes : [langue, longueur, ne pas inventer de sources, dire si tu n'es pas sûr].</div>
<p><strong>Réflexe :</strong> si la réponse est générique, c'est qu'un des 5 champs manque.</p>
<!--SOURCE-->

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Tu es [rôle précis] »</strong> → Tu dis à l'IA qui elle doit être. Sans ça, elle répond comme un généraliste neutre. Un rôle précis active un vocabulaire et un niveau d'exigence.</p>
<p><strong>« Contexte : je suis [qui, niveau, objectif] »</strong> → Tu précises qui tu es. La même notion s'explique différemment à un lycéen, à un L2, à un chercheur. Sans contexte, l'IA choisit un niveau moyen qui ne te correspond pas.</p>
<p><strong>« Tâche : [une seule action] »</strong> → Tu dis exactement ce que tu veux, en une seule action. Une tâche floue donne une réponse floue. Une tâche multiple donne une réponse bâclée.</p>
<p><strong>« Format : [liste / tableau / 5 puces / 150 mots] »</strong> → Tu imposes la forme de la réponse. Sans format, l'IA produit des paragraphes. Avec format, tu obtiens exactement ce dont tu as besoin (tableau à coller, liste à puces, JSON à traiter).</p>
<p><strong>« Contraintes : […] »</strong> → Tu bornes les limites. Sans contraintes, l'IA écrit long, polit, utilise du jargon, et invente des sources. Trois contraintes suffisent à corriger ces travers.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu entres dans un restaurant et que tu dis au serveur : <em>« Donne-moi à manger. »</em> Il te propose n'importe quoi — peut-être une soupe, peut-être un dessert, peut-être un plat trop épicé.</p>
<p>Maintenant imagine que tu dis : <em>« Je suis étudiant, j'ai faim mais pas trop, je voudrais un plat chaud pas trop épicé, pas plus de 500 DA, en plat principal et pas en entrée. »</em> Le serveur sait exactement quoi te proposer.</p>
<p>Avec l'IA, c'est pareil. Le rôle, le contexte, la tâche, le format et les contraintes remplacent les cinq informations que le serveur attend.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Composant</th><th>Rôle</th><th>Exemple</th></tr>
<tr><td><strong>Rôle</strong></td><td>Qui parle ?</td><td>« Professeur de grammaire anglaise pour L2 »</td></tr>
<tr><td><strong>Contexte</strong></td><td>Pour qui ?</td><td>« Étudiant PEP, niveau B2, prépare un exposé »</td></tr>
<tr><td><strong>Tâche</strong></td><td>Quoi faire ?</td><td>« Explique la différence past simple / present perfect »</td></tr>
<tr><td><strong>Format</strong></td><td>Comment ?</td><td>« Tableau 2 colonnes + 3 exemples »</td></tr>
<tr><td><strong>Contraintes</strong></td><td>Avec quelles limites ?</td><td>« 200 mots max, français simple, si tu n'es pas sûr dis-le »</td></tr>
</table>

<h2>5. Application pratique — préparer un exposé sur Shakespeare</h2>
<p><strong>Sans la formule :</strong> tu écris « Aide-moi pour un exposé sur Shakespeare ». Tu reçois 800 mots généralistes sur sa biographie, ses œuvres, son influence. Rien de directement réutilisable. Tu perds 15 minutes à trier.</p>
<p><strong>Avec la formule :</strong></p>
<div class="prompt-box">Tu es professeur d'anglais spécialisé dans la littérature élisabéthaine.
Contexte : je suis étudiant en 2e année PEP, département Anglais, niveau B2. Je prépare un exposé de 10 minutes devant 20 étudiants.
Tâche : propose un plan en 3 parties, avec pour chaque partie un argument principal et 2 exemples.
Format : tableau | Partie | Argument | 2 exemples | + une phrase d'accroche.
Contraintes : français simple, 300 mots max, signale si tu n'es pas sûr d'une date.</div>
<p><strong>Résultat :</strong> un tableau à 3 colonnes, 3 parties équilibrées, une phrase d'accroche prête. Tu commences ton exposé tout de suite.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Si la réponse est générique, cherche le champ manquant avant de rejeter la réponse.</strong></div>
<p>Symptômes et champs manquants :</p>
<table>
<tr><th>Symptôme</th><th>Champ manquant</th></tr>
<tr><td>« Ça pourrait s'appliquer à n'importe qui »</td><td>Rôle ou Contexte</td></tr>
<tr><td>« Elle n'a pas répondu à ma question »</td><td>Tâche (floue ou multiple)</td></tr>
<tr><td>« C'est un pavé de 800 mots »</td><td>Format ou Contraintes</td></tr>
<tr><td>« Elle invente des faits »</td><td>Contraintes (« si tu n'es pas sûr, dis-le »)</td></tr>
</table>
<p>Tu complètes le champ manquant <strong>dans la même conversation</strong>, et tu relances. Pas besoin de tout recommencer.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Mettre 3 tâches dans le champ « Tâche ».</strong> Conséquence : l'IA en bâcle 2 et oublie la 3e. Bonne pratique : une seule tâche par prompt, ou utiliser le chaînage (astuce 62).</li>
<li><strong>Oublier le rôle.</strong> Conséquence : réponse neutre. Bonne pratique : préciser un rôle + un domaine + un niveau.</li>
<li><strong>Accepter le format par défaut (paragraphes).</strong> Conséquence : tu retravailles la réponse. Bonne pratique : imposer le format exact.</li>
<li><strong>Ne pas mettre de contraintes de fiabilité.</strong> Conséquence : hallucinations. Bonne pratique : « si tu n'es pas sûr, dis-le ».</li>
<li><strong>Écrire un rôle trop vague (« expert »).</strong> Conséquence : retour au ton neutre. Bonne pratique : domaine + niveau + contexte.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>QUI PARLE ?       → Rôle
POUR QUI ?        → Contexte
QUOI FAIRE ?      → Tâche
COMMENT ?         → Format
QUELLES LIMITES ? → Contraintes
                      ↓
               Réponse utile
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Les 5 champs sont obligatoires.</strong> Oublier un champ = réponse appauvrie.</li>
<li><strong>Rôle + Contexte personnalisent.</strong> Tâche cible. Format structure. Contraintes sécurisent.</li>
<li><strong>Une seule tâche par prompt.</strong> Pour plusieurs, chaîner.</li>
<li><strong>Le réflexe :</strong> réponse générique → chercher le champ manquant, pas rejeter la réponse.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans la formule</th><th>Avec la formule</th></tr>
<tr><td>Prompt de 4 mots</td><td>Prompt de 60 mots</td></tr>
<tr><td>Écrit en 5 secondes</td><td>Écrit en 90 secondes</td></tr>
<tr><td>800 mots fourre-tout</td><td>Réponse ciblée</td></tr>
<tr><td>15 minutes de tri</td><td>30 secondes d'utilisation</td></tr>
<tr><td><strong>Bilan : 15 min perdues</strong></td><td><strong>Bilan : 12 min gagnées</strong></td></tr>
</table>"""

# ===================================================================== 12
LOT_1[12] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Corrige ce texte comme un professeur de [langue] exigeant.
Tableau : | Faute | Correction | Règle en 1 phrase |
Ne change rien d'autre. À la fin : version propre, puis mes 3 fautes les plus fréquentes.
Texte : [colle ici]</div>
<!--SOURCE-->

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Corrige ce texte »</strong> → Tu demandes une correction. Le mot « corrige » donne une réponse qui te dit <em>où</em> sont les fautes et <em>quoi</em> mettre à la place.</p>
<p><strong>« comme un professeur exigeant »</strong> → Tu fixes le niveau d'exigence. Sans ça, l'IA corrige uniquement l'orthographe. Avec, elle corrige aussi la grammaire, le style, les tournures maladroites — tout ce qu'un vrai professeur ne laisserait pas passer.</p>
<p><strong>« Tableau : Faute | Correction | Règle »</strong> → Tu imposes un format qui te fait progresser. La colonne « Règle » est la plus importante : elle transforme une simple correction en cours de grammaire.</p>
<p><strong>« Ne change rien d'autre »</strong> → Tu bornes les limites. Sans ça, l'IA réécrit le texte entier à sa façon et tu perds ta voix.</p>
<p><strong>« Mes 3 fautes les plus fréquentes »</strong> → Tu transformes une correction ponctuelle en bilan. C'est ce qui te dit où travailler.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine deux professeurs qui te rendent une copie.</p>
<p><strong>Le premier</strong> a entouré les fautes en rouge et écrit la bonne version à côté. Tu lis, tu dis « ah d'accord », et tu referas la même faute la semaine suivante — parce que tu ne sais pas <em>pourquoi</em> c'était faux.</p>
<p><strong>Le second</strong> a écrit à côté de chaque faute : « faute d'accord sujet-verbe : le sujet est au pluriel, le verbe doit l'être aussi ». Tu ne referas plus cette faute, parce que tu as compris la règle.</p>
<p>Le prompt de l'astuce 12 transforme l'IA en second professeur, pas en premier.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Composant</th><th>Rôle</th><th>Effet sur la réponse</th></tr>
<tr><td><strong>« comme un professeur »</strong></td><td>Fixe le niveau d'exigence</td><td>L'IA ne se limite plus aux fautes d'orthographe</td></tr>
<tr><td><strong>Tableau à 3 colonnes</strong></td><td>Impose un format pédagogique</td><td>Chaque faute a sa règle</td></tr>
<tr><td><strong>« Ne change rien d'autre »</strong></td><td>Protège ton style</td><td>L'IA ne réécrit pas ton texte</td></tr>
<tr><td><strong>« 3 fautes les plus fréquentes »</strong></td><td>Force un bilan</td><td>Tu sors avec un plan de progrès</td></tr>
</table>

<h2>5. Application pratique — corriger une lettre de motivation</h2>
<p><strong>Sans l'astuce :</strong></p>
<div class="prompt-box">Corrige cette lettre.</div>
<p>Tu reçois un texte réécrit, propre, mais tu ne sais pas ce qui était faux. Et le texte ne ressemble plus au tien.</p>
<p><strong>Avec l'astuce :</strong></p>
<div class="prompt-box">Corrige cette lettre comme un professeur de français exigeant.
Tableau : | Faute | Correction | Règle en 1 phrase |
Ne change rien d'autre. À la fin : version propre, puis mes 3 fautes les plus fréquentes.
Texte : « Je suis très motivé et très intéressé par votre offre. Malgré que je n'ai pas beaucoup d'expérience, je crois que je serai le bon candidat. »</div>
<p><strong>Réponse obtenue :</strong></p>
<table>
<tr><th>Faute</th><th>Correction</th><th>Règle</th></tr>
<tr><td>« très motivé et très intéressé »</td><td>« vivement intéressé »</td><td>Redondance : un adverbe suffit</td></tr>
<tr><td>« Malgré que je n'ai pas »</td><td>« Bien que je n'aie pas »</td><td>« malgré » ne se construit jamais avec « que »</td></tr>
<tr><td>« je serai le bon candidat »</td><td>« je serais le candidat qu'il vous faut »</td><td>Après « je crois que », le conditionnel atténue la prétention</td></tr>
</table>
<p><strong>+ Version propre</strong> et <strong>3 fautes fréquentes</strong> (registre trop familier, répétitions, abus du futur).</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Exige la règle, pas seulement la correction.</strong></div>
<p>Une correction qu'on ne comprend pas ne se retient pas. Une correction avec sa règle devient un acquis. Recopie chaque règle dans un cahier d'erreurs personnel — la faute qui revient trois fois est <em>ta</em> faute, celle que le correcteur attend de toi au prochain devoir.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Accepter la note sans comprendre.</strong> L'IA note sur 20 — c'est juste un indicateur, pas une évaluation officielle. Ce qui compte, c'est la liste des règles.</li>
<li><strong>Laisser l'IA réécrire tout le texte.</strong> Sans « ne change rien d'autre », elle t'enlève ta voix. Relis toujours la version propre ligne par ligne.</li>
<li><strong>Ne pas recopier les règles.</strong> Sans cahier d'erreurs, tu referas les mêmes fautes. C'est le seul geste qui transforme la correction en progression.</li>
<li><strong>Corriger un texte que l'IA a écrit.</strong> Tu mesures sa correction, pas ton niveau. Corrige uniquement tes propres textes.</li>
<li><strong>Croire que la correction est parfaite.</strong> Vérifie 1-2 règles dans un manuel ou un dictionnaire. L'IA peut se tromper sur des nuances rares.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>Ton texte ──▶ IA « prof sévère » ──▶ Tableau :
                                    | Faute | Correction | Règle |
                                              │
                                              ▼
                                    Cahier d'erreurs
                                              │
                                              ▼
                        Prochain devoir : moins de fautes
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>« Professeur exigeant »</strong> change la qualité de la correction. Sans, l'IA ne fait que l'orthographe.</li>
<li><strong>Le tableau « Faute | Correction | Règle »</strong> est le format qui fait progresser.</li>
<li><strong>« Ne change rien d'autre »</strong> protège ton style.</li>
<li><strong>Recopie les règles dans un cahier d'erreurs.</strong> C'est ce cahier qui fait la différence.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Corrige ce texte »</td><td>« Corrige comme un prof exigeant »</td></tr>
<tr><td>Orthographe seulement</td><td>Orthographe + grammaire + style</td></tr>
<tr><td>Texte réécrit sans toi</td><td>Ton style préservé</td></tr>
<tr><td>0 progrès à long terme</td><td>1 cahier d'erreurs qui se remplit</td></tr>
<tr><td><strong>Bilan : correction passive</strong></td><td><strong>Bilan : progression réelle</strong></td></tr>
</table>"""

# ===================================================================== 23
LOT_1[23] = r"""<h2>1. Le texte source</h2>
<div class="warn"><strong>Règle absolue :</strong> si tu ne le mettrais pas sur un forum public, ne le colle pas dans une IA en ligne.</div>
<!--SOURCE-->

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Si tu ne le mettrais pas sur un forum public »</strong> → C'est le test à faire en 2 secondes. Imagine que tu postes le texte sur un forum. Si ça te gêne, ne le colle pas dans l'IA. Ce test simple remplace tous les raisonnements techniques.</p>
<p><strong>« Ne le colle pas dans une IA en ligne »</strong> → Le mot « en ligne » est important. Il y a deux types d'IA : celles qui envoient ton texte à un serveur étranger (ChatGPT, Gemini, Claude…), et celles qui tournent sur ton ordinateur (Ollama). La règle s'applique aux premières.</p>
<p>Ce qui part : ton texte. Où : sur les serveurs de la société, souvent aux États-Unis ou en Europe. Combien de temps : variable selon les politiques — parfois plusieurs années. Qui peut le lire : les employés de la société, et toute personne qui aurait un accès légal (mandat, réquisition).</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu écris une carte postale. <strong>Ne pas coller de données sensibles dans une IA, c'est comme ne pas écrire un numéro de carte bancaire sur une carte postale.</strong></p>
<p>La carte postale voyage par la poste, passe par plusieurs mains, peut être lue par n'importe qui. Elle peut finir dans une boîte aux lettres qui n'est pas la bonne. Ou être conservée dans un service de tri pendant des années.</p>
<p>Une IA en ligne, c'est pareil. Ton texte fait le voyage, il est stocké, indexé, parfois conservé plusieurs années. Le fait qu'il soit chiffré en transit ne change rien à l'arrivée : sur le serveur, il est lisible.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Type de donnée</th><th>Peut-on la coller ?</th><th>Pourquoi</th></tr>
<tr><td>Mot de passe</td><td>Jamais</td><td>Identifiant + accès = compromission immédiate</td></tr>
<tr><td>Numéro de carte bancaire</td><td>Jamais</td><td>Fraude possible pendant des mois</td></tr>
<tr><td>Carte d'identité / passeport</td><td>Jamais</td><td>Usurpation d'identité</td></tr>
<tr><td>Adresse personnelle précise</td><td>À éviter</td><td>Pas nécessaire pour une correction</td></tr>
<tr><td>Nom complet d'un tiers</td><td>Anonymiser</td><td>Violation du droit à l'image / RGPD</td></tr>
<tr><td>Notes nominatives d'élèves</td><td>Anonymiser</td><td>Données protégées</td></tr>
<tr><td>Question d'étude, texte de cours</td><td>Oui</td><td>Aucun risque</td></tr>
</table>

<h2>5. Application pratique — anonymiser un message reçu</h2>
<p><strong>Texte original à ne pas coller :</strong></p>
<div class="warn">« Mohamed B., promo B, a obtenu 4/20 au contrôle de phonétique. Il habite à la cité 500 logements, appartement 12, à Mostaganem. Son numéro : 05 55 12 34 56. »</div>
<p><strong>Version anonymisée à coller :</strong></p>
<div class="ok">« [NOM] a obtenu [NOTE] au contrôle de [MATIÈRE]. »</div>
<p><strong>Règle :</strong> même les initiales et la promotion doivent partir. « Mohamed B., promo B » ne suffit pas — sur une petite promotion, trois personnes peuvent correspondre, et l'identité devient devinable.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Avant de coller : « Est-ce que je posterais ça sur un forum public ? » Si la réponse est non, je ne colle pas.</strong></div>
<p>Ce test remplace toute une série de questions techniques. Il prend 2 secondes et il couvre 95 % des cas.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Anonymisation incomplète.</strong> Tu retires le nom mais pas les initiales ni la promotion. Cela donne un faux sentiment de sécurité : « Mohamed B., promo B » suffit à identifier dans une petite promo.</li>
<li><strong>Mettre un mot de passe dans un prompt.</strong> « Écris-moi un script qui se connecte avec le mot de passe X ». Le mot de passe part sur un serveur et reste dans l'historique.</li>
<li><strong>Coller un sujet d'examen non public.</strong> Un devoir sur table, un sujet de partiel confidentiel — ce n'est pas « juste un texte », c'est un document protégé.</li>
<li><strong>Croire que « supprimer la conversation » efface tout.</strong> L'historique est aussi dans les sauvegardes. La seule protection réelle est de ne jamais coller.</li>
<li><strong>Utiliser son numéro d'étudiant réel.</strong> Un correcteur qui connaît ta fac peut croiser les informations avec une seule recherche.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>Donnée à coller
       │
       ▼
┌───────────────────────┐    Non
│  Forum public ?       ├────────▶  Ne pas coller
└───────────┬───────────┘
            │ Oui
            ▼
     ┌──────────────┐
     │  OK à coller │
     └──────────────┘
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Le test forum public :</strong> 2 secondes, 95 % des cas couverts.</li>
<li><strong>Ce qui part quitte ton ordinateur.</strong> Supprimer la conversation ne suffit pas.</li>
<li><strong>Anonymiser à fond :</strong> noms, initiales, promotions, lieux, numéros.</li>
<li><strong>Pour les textes vraiment sensibles :</strong> utilise une IA locale (Ollama).</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>Tu colles le message brut</td><td>Tu anonymises d'abord</td></tr>
<tr><td>Noms et numéros partent</td><td>Balises [NOM], [NUMÉRO]</td></tr>
<tr><td>Risque RGPD + faute professionnelle</td><td>Zéro risque identifiable</td></tr>
<tr><td>Tu dois vérifier après coup</td><td>Tu vérifies avant</td></tr>
<tr><td><strong>Bilan : risque permanent</strong></td><td><strong>Bilan : sérénité</strong></td></tr>
</table>"""

# ===================================================================== 35
LOT_1[35] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Je veux un script Python qui :
1) lit un fichier CSV
2) calcule la moyenne de la colonne « note »
3) affiche les 5 meilleures lignes
Écris le code complet, commenté en français, prêt à coller.</div>
<!--SOURCE-->

<h2>2. Explication phrase par phrase</h2>
<p><strong>« Je veux un script qui… »</strong> → Tu décris par le <em>résultat</em>, pas par la technique. Pas « utilise pandas et groupby », mais « calcule la moyenne ». C'est la description qui compte.</p>
<p><strong>« 1) lit un fichier CSV, 2) calcule, 3) affiche »</strong> → Tu découpes en 3 étapes numérotées. L'IA les traite dans l'ordre et produit un code qui fait exactement ces 3 choses. Sans étapes, l'IA devine — et peut se tromper de 50 %.</p>
<p><strong>« Écris le code complet, commenté en français, prêt à coller »</strong> → Tu bornes les limites. Sans « complet », l'IA tronque. Sans « commenté », tu ne comprends pas ce que tu exécutes. Sans « prêt à coller », tu dois recoller des morceaux.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine que tu commandes un repas dans un restaurant.</p>
<p><strong>Cas 1 :</strong> tu dis <em>« faites-moi un truc avec des tomates, une poêle, du feu moyen pendant 8 minutes »</em>. Le cuisinier te regarde bizarrement — il connaît son métier, il n'a pas besoin qu'on lui dicte la recette. Tu risques juste d'avoir un plat qui ne te plaît pas.</p>
<p><strong>Cas 2 :</strong> tu dis <em>« je veux un plat chaud, avec des tomates, pas trop épicé, servi avec du riz »</em>. Le cuisinier sait quoi faire, et tu es sûr du résultat.</p>
<p>Décrire une tâche à une IA de code, c'est pareil. Décris le <strong>résultat final</strong>, pas la recette interne. L'IA connaît la recette mieux que toi.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Composant</th><th>À faire</th><th>À éviter</th></tr>
<tr><td><strong>Décrire le besoin</strong></td><td>Le résultat visible</td><td>Les outils techniques</td></tr>
<tr><td><strong>Découper</strong></td><td>Étapes numérotées</td><td>Une phrase fourre-tout</td></tr>
<tr><td><strong>Spécifier la sortie</strong></td><td>« Code complet, commenté, prêt à coller »</td><td>Rien (l'IA tronque)</td></tr>
<tr><td><strong>Préciser la langue</strong></td><td>« Commentaires en français »</td><td>Laisser par défaut (anglais)</td></tr>
</table>

<h2>5. Application pratique — renommer 200 photos</h2>
<p><strong>Prompt jargon (mauvais) :</strong></p>
<div class="prompt-box">Écris un script qui utilise os.listdir, fait un for avec os.rename, utilise datetime pour extraire la date EXIF, et gère les collisions avec un compteur.</div>
<p>Résultat : l'IA produit un code correct, mais tu ne sais pas s'il fait ce que tu veux, et si un détail cloche (ordre alphabétique, format de date), tu ne peux pas le corriger.</p>
<p><strong>Prompt résultat (bon) :</strong></p>
<div class="prompt-box">Je veux un script Python qui :
1) parcourt les fichiers .jpg du dossier « photos/ »
2) lit la date de chaque photo
3) renomme chaque fichier en « photo_AAAAMMJJ_001.jpg », les 3 derniers chiffres comptant de 1 à N
4) affiche à l'écran chaque renommage
Écris le code complet, commenté en français, prêt à coller.</div>
<p>Résultat : tu obtiens un script qui fait exactement ce que tu voulais. Et si un détail ne te plaît pas, tu peux le demander en français : « mets les 3 chiffres avant la date », et c'est corrigé.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Décris toujours le résultat, jamais la recette.</strong></div>
<p>Une règle : imagine que tu expliques à un ami non-informaticien ce que tu veux obtenir. Si tu utilises des mots comme « listdir », « for », « regex », c'est que tu décris la recette. Si tu utilises « parcourir », « renommer », « afficher », tu décris le résultat. C'est ce dernier qui marche.</p>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Dicter la technique d'entrée.</strong> « Utilise pandas, puis numpy, puis matplotlib » — tu perds du temps et tu obtiens parfois un code bizarre. Laisse l'IA choisir.</li>
<li><strong>Ne pas découper en étapes.</strong> Une phrase fourre-tout donne un code qui mélange les responsabilités. Numérote toujours.</li>
<li><strong>Oublier « code complet ».</strong> L'IA tronque les réponses longues. Tu dois recoller des morceaux.</li>
<li><strong>Laisser les commentaires en anglais.</strong> Par défaut, l'IA commente en anglais. Exige « commentaires en français ».</li>
<li><strong>Ne pas relire avant d'exécuter.</strong> Le jargon peut cacher un bug. Lis chaque ligne, tu comprendras mieux le code.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>   RESULTAT VISIBLE         RECETTE INTERNE
   -----------------         --------------
   « renommer les photos »   « utiliser os.rename »
   « calculer la moyenne »   « faire un groupby »
   « afficher les 5 top »    « trier avec sorted »
           │                          │
           ▼                          ▼
    Ça marche bien          Fragile, dépend du détail
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong>Décris le résultat, pas la recette.</strong> Tu gagnes du temps et tu obtiens un code plus juste.</li>
<li><strong>Numérote les étapes.</strong> 3 à 5 étapes, jamais une phrase fourre-tout.</li>
<li><strong>Exige :</strong> code complet, commentaires en français, prêt à coller.</li>
<li><strong>Relis chaque ligne.</strong> Un code que tu comprends est un code que tu peux corriger.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce (jargon)</th><th>Avec l'astuce (résultat)</th></tr>
<tr><td>« utilise pandas et groupby »</td><td>« calcule la moyenne de cette colonne »</td></tr>
<tr><td>Code qui marche par chance</td><td>Code qui fait exactement ce que tu veux</td></tr>
<tr><td>Débogage difficile</td><td>Débogage en français</td></tr>
<tr><td>Tu dépends du jargon</td><td>Tu restes autonome</td></tr>
<tr><td><strong>Bilan : fragile</strong></td><td><strong>Bilan : robuste</strong></td></tr>
</table>"""

# ===================================================================== 37
LOT_1[37] = r"""<h2>1. Le texte source</h2>
<div class="prompt-box">Dans les agents (Cursor, OpenCode) : @nomdufichier pour cibler, /undo ou diff pour annuler. Ne laisse jamais l'agent modifier 10 fichiers d'un coup sans relire.</div>
<!--SOURCE-->

<h2>2. Explication phrase par phrase</h2>
<p><strong>« @nomdufichier pour cibler »</strong> → Le symbole <code>@</code> sert à dire à l'agent <em>quel fichier lire</em>. Sans <code>@</code>, il devine en parcourant tout le dossier. Avec <code>@meteo.py</code>, il lit uniquement <code>meteo.py</code>. Tu économises des tokens et la réponse est plus juste.</p>
<p><strong>« /undo ou diff pour annuler »</strong> → <code>/undo</code> annule la dernière action de l'agent. <code>diff</code> montre ce qui a changé (lignes vertes ajoutées, lignes rouges supprimées). Ce sont tes deux filets de sécurité : <code>diff</code> pour <em>voir</em>, <code>/undo</code> pour <em>revenir</em>.</p>
<p><strong>« Ne laisse jamais l'agent modifier 10 fichiers d'un coup sans relire »</strong> → Un agent peut toucher plusieurs fichiers pour atteindre son objectif. S'il modifie 10 fichiers et que 2 posent problème, tu dois tout relire. La bonne pratique : un fichier à la fois, ou un sous-ensemble clairement annoncé.</p>

<h2>3. Une analogie pour comprendre</h2>
<p>Imagine un architecte qui travaille sur ta maison.</p>
<p><strong>Sans <code>@</code> :</strong> tu lui dis « refais la maison ». Il touche aux murs, à la toiture, à la plomberie, à l'électricité. Le résultat est imprévisible.</p>
<p><strong>Avec <code>@</code> :</strong> tu lui dis « refais uniquement la cuisine ». Il touche uniquement à la cuisine. Tu vérifies le résultat, c'est propre.</p>
<p><strong>Avec <code>diff</code> et <code>/undo</code> :</strong> c'est comme avoir une caméra qui filme tout et un bouton « annuler ». Tu vois exactement ce qui a changé, et tu peux revenir en arrière en 2 secondes.</p>

<h2>4. Les composants décomposés</h2>
<table>
<tr><th>Commande</th><th>Rôle</th><th>Quand l'utiliser</th></tr>
<tr><td><code>@fichier</code></td><td>Cibler un fichier précis</td><td>Toute demande qui concerne UN fichier connu</td></tr>
<tr><td><code>@dossier/</code></td><td>Cibler un dossier</td><td>Analyse d'un ensemble cohérent</td></tr>
<tr><td><code>diff</code></td><td>Voir les modifications</td><td>AVANT de valider une modification</td></tr>
<tr><td><code>/undo</code></td><td>Annuler la dernière action</td><td>Quand quelque chose ne va pas</td></tr>
<tr><td><code>/init</code></td><td>Analyser le projet entier</td><td>Au premier lancement</td></tr>
</table>

<h2>5. Application pratique — corriger un bug dans un projet</h2>
<p><strong>Sans ciblage :</strong></p>
<div class="prompt-box">Corrige le bug dans mon projet.</div>
<p>L'agent lit 14 fichiers, produit une modification dans 6 d'entre eux, dont 4 inutiles. Tu dois tout relire et tu ne sais pas si le bug est vraiment corrigé.</p>
<p><strong>Avec ciblage :</strong></p>
<div class="prompt-box">@scripts/meteo.py Le script plante à la ligne 12 avec « Cannot load firmware ».
Explique la cause en une phrase, puis propose un correctif à appliquer.
Ne touche à aucun autre fichier.</div>
<p>L'agent lit <em>uniquement</em> <code>meteo.py</code>, propose un correctif à la ligne 12. Tu lis le diff, tu vois la modification, tu valides. Si ça ne marche pas, <code>/undo</code> revient à l'état initial en 2 secondes.</p>

<h2>6. Le réflexe à retenir</h2>
<div class="reflexe"><strong>Un fichier à la fois, ou un sous-ensemble annoncé. Et toujours lire le diff avant de valider.</strong></div>
<p>Les deux réflexes qui vont avec :</p>
<ul>
<li><strong>Si l'agent annonce vouloir toucher 10 fichiers :</strong> demande-lui de commencer par 1, et de te montrer le diff.</li>
<li><strong>Si tu ne comprends pas une ligne du diff :</strong> annule (<code>/undo</code>), puis demande une explication avant de relancer.</li>
</ul>

<h2>7. Erreurs fréquentes à éviter</h2>
<ol>
<li><strong>Ne jamais lire le diff.</strong> Tu valides à l'aveugle, et une ligne supprimée peut être ton seul garde-fou.</li>
<li><strong>Laisser l'agent modifier tout le projet.</strong> 10 fichiers modifiés = 10 fois plus de risque de casser quelque chose.</li>
<li><strong>Ne pas faire de sauvegarde avant.</strong> Si tu ne peux pas revenir à l'état initial, <code>/undo</code> n'aide pas.</li>
<li><strong>Mettre un fichier sensible en contexte.</strong> Un fichier avec des mots de passe dans <code>@</code> part chez le fournisseur du modèle.</li>
<li><strong>Utiliser <code>@</code> pour tout.</strong> Trop de fichiers attachés diluent l'attention de l'agent. 2 fichiers précis valent mieux que tout le dossier.</li>
</ol>

<h2>8. Résumé en une image</h2>
<pre><code>  Demande à l'agent
        │
        ▼
  ┌─────────────────┐
  │  @fichier ?     │  Non ──▶ Ajoute @ pour cibler
  └────────┬────────┘
           │ Oui
           ▼
  ┌─────────────────┐
  │  Lire le diff   │  ← TOUJOURS
  └────────┬────────┘
           │
           ▼
  ┌─────────────────┐    Non
  │  Compris ?      ├────────▶ /undo ──▶ Demande explication
  └────────┬────────┘
           │ Oui
           ▼
     Valider
</code></pre>

<h2>9. Ce que tu dois retenir</h2>
<ul>
<li><strong><code>@fichier</code> cible.</strong> Sans, l'agent devine et touche trop de fichiers.</li>
<li><strong><code>diff</code> montre.</strong> Toujours avant de valider.</li>
<li><strong><code>/undo</code> annule.</strong> C'est ton filet de sécurité. Utilise-le sans hésiter.</li>
<li><strong>Un fichier à la fois.</strong> Ne laisse jamais 10 fichiers être modifiés sans relire un par un.</li>
</ul>

<h2>10. Sans / Avec — comparaison</h2>
<table>
<tr><th>Sans l'astuce</th><th>Avec l'astuce</th></tr>
<tr><td>« Corrige mon projet »</td><td>« @fichier.py corrige la ligne 12 »</td></tr>
<tr><td>6 fichiers modifiés</td><td>1 fichier modifié</td></tr>
<tr><td>Tu ne sais pas ce qui a changé</td><td>Tu lis le diff en 10 secondes</td></tr>
<tr><td>Impossible de revenir</td><td><code>/undo</code> en 2 secondes</td></tr>
<tr><td><strong>Bilan : stress et casse</strong></td><td><strong>Bilan : contrôle total</strong></td></tr>
</table>"""