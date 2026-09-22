# Séance 06 — Réviser efficacement et simuler des examens

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Transformer ses fiches en flashcards, générer des QCM corrigés, se faire interroger par un tuteur socratique et s'entraîner sur des annales — sans tricher, en comprenant.

## Objectifs pédagogiques
- Expliquer pourquoi relire ne suffit pas : rappel actif et répétition espacée.
- Transformer une fiche de cours en 10 flashcards avec l'IA.
- Générer un QCM corrigé à partir d'un chapitre et analyser ses erreurs.
- Utiliser un tuteur socratique : l'IA pose des questions au lieu de donner les réponses.
- Simuler un examen blanc chronométré à partir d'annales.

## Déroulé de la séance (1 h 30)
- **00–05 — Accroche : relire ne marche pas** : Sondage : « combien de fois relisez-vous ? » + analogie du sport.
- **05–25 — Explication : rappel actif + répétition espacée** : 3 idées : se tester bat relire ; espacer bat bachoter ; dormir consolide.
- **25–50 — Démo : flashcards + QCM + tuteur socratique** : Mauvais prompt vs bon prompt : générer 10 flashcards et un QCM corrigé depuis une fiche.
- **50–70 — Exercice guidé : mon premier paquet de flashcards** : Chaque étudiant génère 10 flashcards depuis sa fiche et teste son voisin.
- **70–80 — Démo 2 : examen blanc chronométré** : Transformer une annale en sujet chronométré + grille de correction.
- **80–90 — Synthèse, quiz et annonce de la séance 7** : « À retenir ». Annonce : programmer avec l'IA et le mini-projet Python.

## A. Accroche et analogie (5 min)
- **Question :** Qui a déjà relu 10 fois un cours… pour tout oublier le jour de l'examen ? Le problème n'est pas votre mémoire : c'est la méthode.
- **Analogie :** 🍳 Relire son cours, c'est comme regarder quelqu'un faire du sport en espérant devenir musclé. Réviser avec rappel actif, c'est soulever soi-même les haltères : c'est l'effort de se souvenir qui muscle la mémoire.
- **En une phrase :** 💡 L'IA devient votre coach de révision : elle vous interroge, corrige et reprogramme — mais c'est votre cerveau qui fait le travail.

## B + C. Explication pas à pas et démonstration
### Pourquoi relire ne suffit pas : les 3 idées qui changent tout
La recherche en psychologie cognitive est claire : les étudiants qui se testent retiennent 2 fois plus que ceux qui relisent. L'IA est parfaite pour fabriquer ces tests — à condition de comprendre la méthode.

- <strong>1. Rappel actif :</strong> fermer le cours et essayer de redire l'essentiel. L'effort de recherche en mémoire crée la trace.
- <strong>2. Répétition espacée :</strong> revoir à J+1, J+3, J+7, J+14 — pas 5 fois la veille.
- <strong>3. Mélange (interleaving) :</strong> alterner les chapitres au lieu de finir l'un avant l'autre.
- <strong>Le sommeil :</strong> c'est la nuit que le cerveau consolide. Réviser tard sans dormir est contre-productif.
> 💡 **<strong>Schéma à dessiner au tableau :</strong> courbe de l'oubli — sans révision on oublie 70 % en 24 h ; chaque rappel espacé remonte la courbe plus haut et plus longtemps.**
> 💡 **<strong>🔗 Rappel séances 4 et 5 :</strong> vos fiches Cornell (séance 4) deviennent des flashcards, et le jury-IA de votre exposé (séance 5) devient un tuteur qui vous interroge. Chaque séance réutilise les outils des précédentes.**

### Les flashcards : 10 cartes qui valent 10 relectures
Une flashcard = une question d'un côté, la réponse de l'autre. On se teste, on trie (su / pas su), on revoit seulement les ratées. L'IA génère le paquet en 1 minute depuis votre fiche.

- <strong>Prompt modèle :</strong> « Voici ma fiche [coller]. Crée 10 flashcards : une question courte + réponse en 1 phrase. Numérote-les. »
- <strong>Règle d'or :</strong> 1 carte = 1 fait. Si la réponse fait 5 lignes, découpez en 3 cartes.
- <strong>Outils gratuits :</strong> Anki (répétition espacée automatique), Quizlet, ou simple papier.
- <strong>En arabe aussi :</strong> l'IA génère les cartes dans la langue de votre fiche.
> 💡 **<strong>🧪 Exemple concret :</strong> fiche « Present perfect » → carte 3 : Q « Quelle forme après have/has ? » / R « Le participe passé — ex : I have <strong>eaten</strong>. » Testez votre voisin : il répond sans regarder, vous montrez la réponse.**

### QCM corrigés et annales : s'entraîner comme le jour J
Demandez à l'IA un QCM avec correction expliquée, puis faites-le SANS regarder le cours, chronomètre en main. L'analyse des erreurs vaut plus que le score.

- <strong>Prompt QCM :</strong> « Chapitre [coller]. 10 QCM à 4 choix, 1 seule bonne réponse, puis correction avec la phrase du cours qui justifie. »
- <strong>Prompt annale :</strong> « Voici le sujet 2024 [coller]. Propose un sujet 2025 du même style + barème sur 20. »
- <strong>Rituel d'analyse :</strong> pour chaque erreur, écrire la bonne règle en 1 phrase dans un carnet.
- <strong>Piège :</strong> refaire le même QCM de mémoire donne une fausse confiance — demandez une version mélangée.
> 💡 **<strong>⚠️ Ligne rouge :</strong> générer un QCM pour réviser = excellent. Photographier le sujet pendant l'examen pour le faire résoudre par l'IA = tricherie, sanction disciplinaire. Le diplôme obtenu en trichant ne vaut rien.**

### Le tuteur socratique : une IA qui vous interroge
Au lieu de demander la réponse, demandez des questions : l'IA devient un professeur particulier infatigable qui ne donne la solution qu'après vos essais.

- <strong>Prompt tuteur :</strong> « Tu es mon tuteur de [module]. Pose-moi une question à la fois sur [chapitre]. Si je me trompe, donne un indice, pas la réponse. 10 questions. »
- <strong>Variante exposé :</strong> « Joue le jury : pose-moi 5 questions pièges sur mon sujet. »
- <strong>Variante langue :</strong> « Corrige mon anglais phrase par phrase et explique chaque faute. »

### Comment en profiter au maximum
Le cycle gagnant : générer → se tester SANS le cours → corriger → noter les erreurs → reprogrammer la révision des ratées à J+3.
> 💡 **<strong>➡️ Pont vers la séance 7 :</strong> le tuteur socratique qui vous interroge deviendra un VRAI programme Python (assistant_chat.py) qui appelle Gemini. Vous passerez d'utilisateur à constructeur.**

- <strong>✅ Mélangez :</strong> flashcards + QCM + tuteur, jamais un seul format.
- <strong>✅ Chronométrez :</strong> toujours avec le temps de l'examen réel.
- <strong>✅ Carnet d'erreurs :</strong> 1 phrase par erreur, relu la veille.
- <strong>✅ Demandez des variantes :</strong> « même chapitre, 10 questions différentes ».
> 💡 **<strong>❌ Erreurs à éviter :</strong> réviser avec le corrigé sous les yeux, refaire le même QCM appris par cœur, réviser 6 h d'affilée sans pause (25 min de travail + 5 min de pause).**

|  | Mauvais usage | Bon usage |
|---|---|---|
| Demande | « Donne-moi les réponses du chapitre 3. » | « Interroge-moi sur le chapitre 3, une question à la fois, sans donner les réponses. » |
| Résultat | Lecture passive, illusion de savoir. | Rappel actif, vraies traces en mémoire. |

## 📺 Ressources vidéo
- **Réviser avec les flashcards et Anki (tutoriel)** (fr): https://www.youtube.com/results?search_query=anki+flashcards+tutoriel+francais+revision — Pour installer Anki et créer votre premier paquet depuis les cartes générées par l'IA.
- **كيف تراجع بذكاء؟ الاستدعاء النشط والتكرار المتباعد** (ar): https://www.youtube.com/results?search_query=active+recall+spaced+repetition+study+technique — La science de la mémoire expliquée simplement, avec des exemples d'étudiants.
- **Générer des QCM avec ChatGPT pour réviser** (fr): https://www.youtube.com/results?search_query=generer+QCM+chatgpt+reviser+examen — Voir en vidéo la méthode « fiche → QCM corrigé → analyse d'erreurs ».

## D. Exercice guidé (15 min)
**Énoncé :** Avec votre fiche de cours : 1) générez 10 flashcards avec le prompt modèle ; 2) testez votre voisin (il répond sans regarder) ; 3) notez les cartes ratées et reprogrammez-les à J+3.
**Méthode :** 1) Copiez le prompt modèle et collez votre fiche. 2) Vérifiez que chaque carte a 1 question + 1 réponse courte (découpez sinon). 3) Cachez les réponses et interrogez-vous à voix haute. 4) Triez : su / pas su.
**Solution :** Exemple de paquet réussi : 10 cartes numérotées, questions courtes (« Quelle est la règle d'accord du participe avec avoir ? »), réponses d'1 phrase, 2 cartes jugées trop longues découpées en 4, planning noté : revoir les 3 ratées à J+3.

## 💭 As-tu bien compris ?
- **Q1.** Pourquoi se tester est-il plus efficace que relire ?
  *Réponse :* Parce que l'effort de retrouver l'information en mémoire crée une trace durable, alors que relire donne seulement une impression de familiarité.
- **Q2.** Que faire après un QCM raté à 6/10 ?
  *Réponse :* Noter chaque erreur en 1 phrase dans le carnet, revoir les points ratés à J+3, puis demander une version mélangée du QCM.
- **Q3.** Quelle est la différence entre demander la réponse et demander à être interrogé ?
  *Réponse :* Demander la réponse = lecture passive. Demander à être interrogé (tuteur socratique) = rappel actif : c'est votre cerveau qui travaille.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- Se tester bat relire : le rappel actif crée la mémoire.
- Espacer : J+1, J+3, J+7, J+14 — jamais tout la veille.
- 1 flashcard = 1 question + 1 réponse courte.
- QCM chronométré sans le cours + carnet d'erreurs (1 phrase par erreur).
- Tuteur socratique : l'IA interroge, vous répondez, elle indice.
### Analogies utilisées
- 🍳 Le sport : regarder ne muscle pas, soulever oui — réviser, c'est soulever.
- 🍳 Le carnet d'erreurs, c'est la trousse de secours de la veille d'examen.
- 🍳 Le tuteur socratique, c'est un sparring-partner : il frappe doucement pour vous entraîner.
### Exemples concrets
- ✏️ Fiche de psycho → 10 flashcards → test du voisin → 3 ratées à J+3.
- ✏️ Annale 2024 recopiée → sujet 2025 généré + barème → 1 h chrono.
- ✏️ « Interroge-moi sur les temps anglais, un par un » → 10 questions, 2 indices.
> 🏁 **Analogie finale :** 🏁 Réviser avec l'IA, c'est comme avoir un coach sportif personnel : il prépare les exercices, compte les répétitions et vous encourage — mais les muscles, c'est vous qui les construisez.
### Quiz — vérifie ta compréhension
**Q1.** Pourquoi relire 5 fois donne une fausse confiance ?
   - 🔘 Parce que le texte change
   - ✅ Parce que la familiarité ressemble au savoir sans être la mémoire
   - 🔘 Parce que c'est interdit
   - 🔘 Parce que c'est trop rapide
   *Explication :* Relire rend le texte familier, mais seul l'effort de rappel (se tester sans le cours) crée une trace durable.
**Q2.** Quel est le bon planning de révision espacée ?
   - 🔘 Tout la veille
   - ✅ J+1, J+3, J+7, J+14
   - 🔘 Une fois par mois
   - 🔘 Jamais, c'est inutile
   *Explication :* Revoir juste avant d'oublier (J+1, J+3, J+7, J+14) consolide la mémoire avec peu d'effort.
**Q3.** Que contient une bonne flashcard ?
   - 🔘 Tout un chapitre
   - ✅ 1 question + 1 réponse courte
   - 🔘 Seulement une image
   - 🔘 La correction complète
   *Explication :* 1 carte = 1 fait. Les réponses longues doivent être découpées en plusieurs cartes.
**Q4.** Que faire d'une erreur de QCM ?
   - 🔘 L'ignorer
   - ✅ L'écrire en 1 phrase dans le carnet et revoir le point à J+3
   - 🔘 Refaire le même QCM aussitôt
   - 🔘 Accuser l'IA
   *Explication :* L'erreur est une information : notée et revue à J+3, elle ne se reproduit plus.
**Q5.** Quel prompt fait travailler VOTRE cerveau ?
   - 🔘 « Donne-moi les réponses »
   - ✅ « Interroge-moi une question à la fois, sans donner les réponses »
   - 🔘 « Résume tout »
   - 🔘 « Fais mon devoir »
   *Explication :* Le tuteur socratique (questions + indices) déclenche le rappel actif ; demander les réponses = lecture passive.

## Activités et exercices
- Fabrique de flashcards : générer 10 cartes depuis sa fiche, tester son voisin, trier su/pas su.
- QCM chrono : générer un QCM de 10 questions, le faire en 15 min sans le cours, analyser les erreurs.
- Duo socratique : l'un joue le tuteur-IA (questions + indices), l'autre répond ; puis on inverse.
- Examen blanc : sujet généré depuis une annale, 30 min chrono, correction croisée en binôme.

## À retenir
- Tester > relire : le rappel actif construit la mémoire.
- Espacer J+1, J+3, J+7, J+14 ; dormir consolide.
- Flashcards : 1 carte = 1 question + 1 réponse courte.
- QCM chronométré sans cours + carnet d'erreurs.
- Tuteur socratique : jamais de réponse directe, toujours une question d'abord.

## Glossaire
- **Rappel actif** : Effort de retrouver une information en mémoire sans regarder le cours ; la méthode de révision la plus efficace.
- **Répétition espacée** : Revoir une notion à intervalles croissants (J+1, J+3, J+7…) pour contrer l'oubli.
- **Flashcard** : Carte question/réponse pour se tester rapidement, idéale avec Anki.
- **Tuteur socratique** : Usage de l'IA qui pose des questions et donne des indices au lieu de livrer les réponses.
- **Annale** : Sujet d'examen d'une année précédente, base idéale pour simuler le jour J.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)