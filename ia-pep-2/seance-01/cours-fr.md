# Séance 01 — Qu'est-ce que l'IA ? Introduction et démystification

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Comprendre ce qu'est l'IA en mots simples — avec des comparaisons de la vie quotidienne — pour t'en servir dès aujourd'hui dans tes études, sans naïveté, sans peur et avec ton esprit critique.

## Objectifs pédagogiques
- Définir avec tes mots : IA, modèle de langage et prompt.
- Expliquer simplement comment un chatbot répond (il prédit le mot le plus probable à partir d'exemples).
- Citer 5 usages de l'IA utiles à tes études (rechercher, résumer, rédiger, réviser, organiser).
- Identifier 3 limites : erreurs, hallucinations, biais.
- Appliquer les 3 règles d'or : vérifier, citer, garder ton jugement.

## Déroulé de la séance (1 h 30)
- **00–05 — Accroche et sondage** : La question « ton téléphone utilise l'IA ? » + tour de table sur les usages déjà vus.
- **05–20 — Explication pas à pas : 3 idées clés** : 1) L'IA apprend sur des exemples (apprenti cuisinier). 2) Un chatbot prédit le mot suivant. 3) IA faible / générale / super-IA.
- **20–40 — Démonstration : un résumé de cours** : Mauvais prompt vs bon prompt, puis piège de l'hallucination : la même question posée à un chatbot et à un moteur sourcé.
- **40–55 — Exercice guidé : vrai ou faux ?** : 6 affirmations sur l'IA à classer + correction collective.
- **55–60 — Résumé visuel et quiz éclair** : Fiche de synthèse (+3 points) et quiz éclair de 3 questions.
- **60–90 — Atelier : dialogues et rôles** : Jouer les dialogues A et B en binômes, puis mini-rôle de 3 min.

## A. Accroche et analogie (5 min)
- **Question :** Savez-vous que votre téléphone utilise l'IA des dizaines de fois par jour, sans que vous vous en rendiez compte ? Verrouillage du visage, traduction, correction du clavier, recommandation de vidéos…
- **Analogie :** 🍳 L'IA, c'est comme un apprenti cuisinier : il goûte des milliers de plats (les exemples), remarque des régularités (le sucre c'est sucré, le citron c'est acide) et finit par pouvoir créer sa propre recette. Il ne sait pas POURQUOI ça marche, il a appris QUE ça marche.
- **En une phrase :** 💡 L'IA, c'est un programme informatique qui apprend à partir d'exemples pour imiter certaines capacités humaines : comprendre, parler, traduire, voir, décider.

## B + C. Explication pas à pas et démonstration
### Idée clé 1 — L'IA apprend sur des exemples
Une IA n'est pas programmée « à la main » comme une calculatrice. On lui montre des milliers d'exemples, et elle en tire des régularités. C'est une énorme machine à généraliser.
> 💡 **<strong>Analogie pour te souvenir :</strong> comment un enfant reconnaît-il un chien ? Il en a vu beaucoup. Il n'apprend pas une définition : il reconnaît des ressemblances. L'IA fait pareil, à grande échelle.**

- <strong>Données d'entraînement :</strong> les exemples qu'on montre à l'IA (textes, images, sons).
- <strong>Modèle :</strong> le résultat de l'apprentissage — un « cerveau » numérique qui généralise à partir des exemples.
- <strong>Prédiction :</strong> quand tu lui poses une question, il ne « cherche » pas la réponse : il la reconstruit à partir de ce qu'il a appris.

```
Schéma simple — comment l'IA apprend :

    EXEMPLES (milliers)          APPRENTISSAGE              MODÈLE
    "ceci est un chat"     ──►  régularités trouvées  ──►  "reconnaît" un chat
    "ceci est un chien"         poids chiffrés ajustés      puis répond / prédit
```

### Idée clé 2 — Un chatbot prédit le mot suivant
ChatGPT, Gemini ou Copilot sont des « modèles de langage » (LLM). Leur secret : ils ont été entraînés sur des milliards de phrases, et ils ont appris une seule chose — quel mot vient le plus probablement après celui-ci.

- « Hier, je suis allé … » → le modèle propose « au marché » parce que c'est très fréquent dans ses données.
- Il génère mot après mot, jusqu'à former une phrase entière. Résultat : un texte qui paraît très naturel.
- Il est entraîné à être <strong>convaincant</strong>, pas à être <strong>vrai</strong>. D'où les erreurs et les hallucinations.
> 💡 **<strong>Hallucination =</strong> quand l'IA affirme avec assurance un fait inventé (une référence, un chiffre, une date). Ce n'est pas un bug rare : c'est un comportement fréquent. Toujours vérifier.**

```
Jeu de devinettes — prédire la suite :

    « L'IA, c'est un programme qui ______ »
    Probabilités : apprend(?) > calcule(?) > ...
    → le modèle choisit le mot le plus probable, puis recommence.
```

### Idée clé 3 — Trois familles d'IA
Il faut savoir classer ce dont on parle : tout ce que tu utilises aujourd'hui appartient à la première famille.

- <strong>1. IA faible (étroite)</strong> : excellente dans UNE tâche (traduire, trier, générer du texte). → Tout ce qui existe aujourd'hui.
- <strong>2. IA générale</strong> : égalerait l'humain dans TOUTES les tâches. → N'existe pas encore.
- <strong>3. Super-IA</strong> : dépasserait l'humain. → Scénario hypothétique qui alimente les films et les débats.
> 💡 **<strong>Schéma pour la classe :</strong> écrire les trois familles au tableau comme trois escaliers. On monte les marches : le dernier étage (super-IA) n'existe QUE dans les films.**

### Démonstration — un résumé de cours, du mauvais au bon prompt
Étudiant : « Je dois préparer mon exposé de psychologie de l'enfant. Je colle mon cours et je demande à l'IA de l'aider. » Regardons la différence entre une question paresseuse et une question qui guide.

|  | Mauvais prompt | Bon prompt |
|---|---|---|
| Requête | Résume ce cours. | Je suis étudiant en 2ème année PEP. Résume ce cours de psychologie en 5 idées clés, avec un exemple concret pour le primaire à chaque idée, et sans rien inventer : dis-moi ce qui manque. |
| Résultat | Générique, trop long, aucun lien avec l'exposé. | Ciblé, structuré, réutilisable pour l'exposé, limites signalées. |
> 💡 **<strong>Le piège du jour :</strong> posons la même question « Donne-moi 2 études sur Piaget » à un chatbot puis à un outil sourcé. Le chatbot peut inventer des références avec assurance ; l'outil sourcé affiche des liens à ouvrir. C'est une raison d'apprendre à vérifier (séance 02).**

### Comment en profiter au maximum
Dès la première séance, retenez l'essentiel : l'IA vaut ce que vaut la question posée, et la réponse vaut ce que vaut la vérification. Utilisée ainsi, elle devient un tuteur personnel disponible 24 h/24 — jamais un remplaçant de ta mémoire.

- <strong>✅ Commencez petit :</strong> une tâche précise (résumer, expliquer, reformuler), jamais « fais tout mon travail ».
- <strong>✅ Donnez du contexte :</strong> matière, niveau, objectif, format attendu et longueur.
- <strong>✅ Vérifiez systématiquement :</strong> chaque date, chiffre et référence doit être confirmé dans ton cours.
- <strong>✅ Demandez la méthode :</strong> « explique comment tu arrives à cette conclusion » pour apprendre, pas seulement subir.
> 💡 **<strong>❌ Erreurs à éviter :</strong> recopier une réponse sans la relire ; faire confiance à un chatbot parce qu'il paraît sûr de lui (la confiance n'est pas la vérité) ; devenir dépendant (demander l'IA avant de réfléchir une seule minute) ; et le plagiat — déposer un texte généré comme s'il était de vous, sans le citer ni l'arranger.**

|  | Mauvais prompt | Bon prompt |
|---|---|---|
| Requête | Résume ce cours. | Je suis étudiant 2A PEP. Résume ce cours de psychologie en 5 idées clés avec un exemple pour le primaire à chaque idée, et dis-moi ce qui manque. |
| Résultat | Générique, trop long, vérifications impossibles. | Ciblé, réutilisable pour l'exposé, limites signalées. |
> 💡 **<strong>Astuce gain de temps :</strong> créez dès maintenant un fichier « mémo prompts » (dans Notion ou un simple bloc-notes) et enregistrez-y chaque invitation réussie. Posez la question d'abord, réfléchissez-y une minute, puis lisez la réponse comme un livre que vous devez critiquer.**

## 📺 Ressources vidéo
- **ما هو الذكاء الاصطناعي؟ شرح مبسط للمبتدئين (AI بالعربي)** (ar): https://www.youtube.com/watch?v=wdbb-X5qH4w — Idéale pour revoir la définition de l'IA avec des exemples de la vie quotidienne.
- **ما هو الذكاء الاصطناعي؟ شرح مبسط** (ar): https://www.youtube.com/watch?v=vCKHeYQp8nk — Deuxième regard, très pédagogique : l'IA dans le téléphone et dans la classe.
- **The Age of A.I. (Kurzgesagt)** (en): https://www.youtube.com/watch?v=UwsrzCVZAb8 — Ce que l'IA peut et ne peut pas faire — pour rester lucide (sous-titres FR disponibles).

## D. Exercice guidé (15 min)
**Énoncé :** Classe les 6 affirmations suivantes en Vrai (V) ou Faux (F), puis justifie en une ligne : 1) L'IA pense comme un humain. 2) L'IA a été entraînée sur des textes. 3) L'IA donne toujours des bonnes réponses. 4) L'IA peut inventer une référence. 5) L'IA remplace le professeur. 6) L'IA peut t'aider à réviser si tu vérifies.
**Méthode :** 1) Lis chaque affirmation. 2) Demande-toi : « Qu'ai-je appris sur la façon dont l'IA produit une réponse ? ». 3) Note V ou F puis une justification. 4) Compare avec ton voisin avant la correction collective.
**Solution :** 1) F — l'IA calcule des probabilités, elle n'a ni conscience ni pensées. 2) V — c'est son apprentissage. 3) F — elle peut se tromper et même inventer (halluciner). 4) V — c'est très fréquent, d'où la règle « vérifie ». 5) F — elle assiste l'étudiant, l'évaluation et le dialogue restent humains. 6) V — à condition de vérifier le contenu avec ton cours et tes sources.

## 💭 As-tu bien compris ?
- **Q1.** Le chatbot « cherche » la réponse dans une grande bibliothèque ?
  *Réponse :* Non. Il reconstitue la réponse mot après mot, selon les probabilités apprises sur ses données. Il n'a pas accès à « la vérité ».
- **Q2.** Pourquoi peut-il inventer une référence quand il a l'air si sûr de lui ?
  *Réponse :* Parce qu'il est entraîné à produire des phrases plausibles et convaincantes. La confiance n'est PAS un indicateur de vérité.
- **Q3.** ChatGPT appartient à quelle famille d'IA : faible, générale ou super-IA ?
  *Réponse :* IA faible : excellente dans la génération de texte, mais incapable de faire « n'importe quelle tâche » comme un humain.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- L'IA est un programme qui apprend à partir d'exemples pour imiter des capacités humaines.
- Un chatbot est une machine à prédire le mot suivant, entraînée à être convaincante — pas vraie.
- Hallucination = invention confiante. C'est fréquent, pas un bug.
- 3 familles : IA faible (tout ce qu'on utilise), générale (future), super-IA (films).
- 3 règles d'or : vérifier, citer, garder ton jugement.
### Analogies utilisées
- 🍳 L'apprenti cuisinier qui goûte des milliers de plats avant de créer sa recette.
- 🍳 L'enfant qui reconnaît un chien parce qu'il en a déjà vu beaucoup.
- 🍳 Le jeu de devinettes : deviner le mot suivant d'une phrase.
### Exemples concrets
- ✏️ Ton téléphone utilise l'IA pour déverrouiller (reconnaissance faciale) et corriger ta frappe.
- ✏️ « Hier je suis allé… » → l'IA propose « au marché » car c'est probable.
- ✏️ Demander 2 études sur Piaget : le chatbot peut en inventer, l'outil sourcé affiche des liens.
> 🏁 **Analogie finale :** 🏁 L'IA, c'est comme un excellent acteur : il peut jouer brillamment n'importe quel rôle de manière convaincante, mais ce qu'il raconte n'est pas forcément vrai. À toi de vérifier le scénario.
### Quiz — vérifie ta compréhension
**Q1.** Comment un chatbot produit-il sa réponse ?
   - 🔘 Il la copie d'une bibliothèque
   - ✅ Il prédit le mot le plus probable, mot après mot
   - 🔘 Il demande à un humain
   - 🔘 Il la cherche sur Google
   *Explication :* Le chatbot reconstruit la réponse mot après mot selon les probabilités apprises pendant l'entraînement.
**Q2.** Qu'est-ce qu'une « hallucination » d'IA ?
   - 🔘 Un bug très rare
   - 🔘 Une certitude dans la réponse
   - ✅ Une information inventée dite avec assurance
   - 🔘 Une panne d'ordinateur
   *Explication :* L'IA peut affirmer des faits faux avec assurance. C'est un comportement courant : vérifie toujours.
**Q3.** ChatGPT, aujourd'hui, c'est…
   - 🔘 Une IA générale
   - 🔘 Une super-IA
   - ✅ Une IA faible (étroite)
   - 🔘 Un cerveau humain
   *Explication :* Il est excellent dans une tâche (le texte) mais ne fait pas « tout » comme un humain.
**Q4.** Laquelle de ces phrases est une bonne règle d'or ?
   - 🔘 Copier la réponse et la déposer
   - ✅ Vérifier, citer, garder son jugement
   - 🔘 Faire confiance à 100 %
   - 🔘 Ne jamais utiliser l'IA
   *Explication :* Les 3 règles d'or protègent ta note ET ta compréhension : l'IA propose, tu disposes.
**Q5.** Comment apprend une IA ?
   - 🔘 On lui écrit toutes les règles à la main
   - ✅ En voyant des milliers d'exemples et en trouvant des régularités
   - 🔘 En lisant les journaux chaque matin
   - 🔘 En copiant les réponses de ses camarades
   *Explication :* L'apprentissage sur exemples (comme l'apprenti cuisinier) : c'est la base de l'IA moderne.

## Activités et exercices
- Nuage de mots : chaque étudiant donne un mot associé à « IA », on le note au tableau, puis on regroupe par thème.
- Sondage « mes usages » à main levée : as-tu déjà utilisé un chatbot ? pour quoi ? avec quel résultat ?
- Démo guidée (si connexion) : résumer un paragraphe du cours, puis vérifier : l'IA invente-t-elle quelque chose ?
- Jeu « vrai ou faux » (exercice guidé) : 6 idées reçues sur l'IA départagées collectivement.

## À retenir
- L'IA = programme qui apprend à partir d'exemples pour imiter des capacités humaines.
- Un chatbot prédit le mot suivant ; il peut être convaincant sans être vrai. Hallucinations : fréquentes.
- 5 usages pour tes études : rechercher, résumer, rédiger, réviser, organiser.
- L'IA ne pense pas, ne ressent pas, n'apprend rien à ta place : la compréhension reste ton travail.
- 3 règles d'or : vérifier, citer, garder ton jugement.

## Glossaire
- **Intelligence Artificielle (IA)** : Programme informatique qui apprend à partir de données pour accomplir des tâches habituellement « intelligentes ».
- **Modèle de langage (LLM)** : Modèle d'IA entraîné sur d'énormes corpus de textes, capable de prédire et de générer du langage.
- **Prompt** : La question, l'instruction ou le contexte que tu donnes à l'IA pour orienter sa réponse.
- **Hallucination** : Réponse fausse ou inventée donnée avec assurance par une IA générative.
- **Données d'entraînement** : Les textes, images et exemples utilisés pour apprendre au modèle à fonctionner.
- **IA générative** : Catégorie d'IA qui crée du contenu nouveau (texte, image, audio) à partir d'une consigne.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)