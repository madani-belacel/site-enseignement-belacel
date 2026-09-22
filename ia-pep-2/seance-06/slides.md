---
marp: true
theme: default
paginate: true
size: 16:9
title: Séance 06 — Réviser efficacement et simuler des examens
---

# 📝 Séance 06 — Réviser efficacement et simuler des examens

*Revise efficiently and simulate exams*

**Module Intelligence Artificielle — 2ème année PEP · ENS**

Dr. Madani BELACEL — Université de Mostaganem

---

## ⏱️ Déroulé de la séance (1 h 30)

- **00–05** — Accroche : relire ne marche pas
- **05–25** — Explication : rappel actif + répétition espacée
- **25–50** — Démo : flashcards + QCM + tuteur socratique
- **50–70** — Exercice guidé : mon premier paquet de flashcards
- **70–80** — Démo 2 : examen blanc chronométré
- **80–90** — Synthèse, quiz et annonce de la séance 7

---

## 🎯 Objectifs pédagogiques

- Expliquer pourquoi relire ne suffit pas : rappel actif et répétition espacée.
- Transformer une fiche de cours en 10 flashcards avec l'IA.
- Générer un QCM corrigé à partir d'un chapitre et analyser ses erreurs.
- Utiliser un tuteur socratique : l'IA pose des questions au lieu de donner les réponses.
- Simuler un examen blanc chronométré à partir d'annales.

---

## 🎬 Accroche (5 min)

❓ Qui a déjà relu 10 fois un cours… pour tout oublier le jour de l'examen ? Le problème n'est pas votre mémoire : c'est la méthode.

🍳 **Analogie :** 🍳 Relire son cours, c'est comme regarder quelqu'un faire du sport en espérant devenir musclé. Réviser avec rappel actif, c'est soulever soi-même les haltères : c'est l'effort de se souvenir qui muscle la mémoire.

💡 💡 L'IA devient votre coach de révision : elle vous interroge, corrige et reprogramme — mais c'est votre cerveau qui fait le travail.

---

## Pourquoi relire ne suffit pas : les 3 idées qui changent tout

- La recherche en psychologie cognitive est claire : les étudiants qui se testent retiennent 2 fois plus que ceux qui relisent. L'IA est parfaite pour fabriquer ces tests — à condition de comprendre la méthode.
- **1. Rappel actif :** fermer le cours et essayer de redire l'essentiel. L'effort de recherche en mémoire crée la trace.
- **2. Répétition espacée :** revoir à J+1, J+3, J+7, J+14 — pas 5 fois la veille.
- **3. Mélange (interleaving) :** alterner les chapitres au lieu de finir l'un avant l'autre.
- **Le sommeil :** c'est la nuit que le cerveau consolide. Réviser tard sans dormir est contre-productif.
- 💡 **Schéma à dessiner au tableau :** courbe de l'oubli — sans révision on oublie 70 % en 24 h ; chaque rappel espacé remonte la courbe plus haut et plus longtemps.

*Why rereading is not enough: 3 game-changing ideas*

---

## Les flashcards : 10 cartes qui valent 10 relectures

- Une flashcard = une question d'un côté, la réponse de l'autre. On se teste, on trie (su / pas su), on revoit seulement les ratées. L'IA génère le paquet en 1 minute depuis votre fiche.
- **Prompt modèle :** « Voici ma fiche [coller]. Crée 10 flashcards : une question courte + réponse en 1 phrase. Numérote-les. »
- **Règle d'or :** 1 carte = 1 fait. Si la réponse fait 5 lignes, découpez en 3 cartes.
- **Outils gratuits :** Anki (répétition espacée automatique), Quizlet, ou simple papier.
- **En arabe aussi :** l'IA génère les cartes dans la langue de votre fiche.
- 💡 **🧪 Exemple concret :** fiche « Present perfect » → carte 3 : Q « Quelle forme après have/has ? » / R « Le participe passé — ex : I have **eaten**. » Testez votre voisin : il répond sans regarder, vous montrez la réponse.

*Flashcards: 10 cards worth 10 rereads*

---

## QCM corrigés et annales : s'entraîner comme le jour J

- Demandez à l'IA un QCM avec correction expliquée, puis faites-le SANS regarder le cours, chronomètre en main. L'analyse des erreurs vaut plus que le score.
- **Prompt QCM :** « Chapitre [coller]. 10 QCM à 4 choix, 1 seule bonne réponse, puis correction avec la phrase du cours qui justifie. »
- **Prompt annale :** « Voici le sujet 2024 [coller]. Propose un sujet 2025 du même style + barème sur 20. »
- **Rituel d'analyse :** pour chaque erreur, écrire la bonne règle en 1 phrase dans un carnet.
- **Piège :** refaire le même QCM de mémoire donne une fausse confiance — demandez une version mélangée.
- 💡 **⚠️ Ligne rouge :** générer un QCM pour réviser = excellent. Photographier le sujet pendant l'examen pour le faire résoudre par l'IA = tricherie, sanction disciplinaire. Le diplôme obtenu en trichant ne vaut rien.

*Corrected quizzes and past papers: train like exam day*

---

## Le tuteur socratique : une IA qui vous interroge

- Au lieu de demander la réponse, demandez des questions : l'IA devient un professeur particulier infatigable qui ne donne la solution qu'après vos essais.
- **Prompt tuteur :** « Tu es mon tuteur de [module]. Pose-moi une question à la fois sur [chapitre]. Si je me trompe, donne un indice, pas la réponse. 10 questions. »
- **Variante exposé :** « Joue le jury : pose-moi 5 questions pièges sur mon sujet. »
- **Variante langue :** « Corrige mon anglais phrase par phrase et explique chaque faute. »

*The Socratic tutor: an AI that questions you*

---

## Comment en profiter au maximum

- Le cycle gagnant : générer → se tester SANS le cours → corriger → noter les erreurs → reprogrammer la révision des ratées à J+3.
- 💡 **➡️ Pont vers la séance 7 :** le tuteur socratique qui vous interroge deviendra un VRAI programme Python (assistant_chat.py) qui appelle Gemini. Vous passerez d'utilisateur à constructeur.
- **✅ Mélangez :** flashcards + QCM + tuteur, jamais un seul format.
- **✅ Chronométrez :** toujours avec le temps de l'examen réel.
- **✅ Carnet d'erreurs :** 1 phrase par erreur, relu la veille.
- **✅ Demandez des variantes :** « même chapitre, 10 questions différentes ».

*How to get the most out of it*

---

## 📺 À regarder après la classe

- **Réviser avec les flashcards et Anki (tutoriel)** (fr) — https://www.youtube.com/results?search_query=anki+flashcards+tutoriel+francais+revision
- **كيف تراجع بذكاء؟ الاستدعاء النشط والتكرار المتباعد** (ar) — https://www.youtube.com/results?search_query=active+recall+spaced+repetition+study+technique
- **Générer des QCM avec ChatGPT pour réviser** (fr) — https://www.youtube.com/results?search_query=generer+QCM+chatgpt+reviser+examen

---

## ✏️ Exercice guidé (15 min)

**Énoncé :** Avec votre fiche de cours : 1) générez 10 flashcards avec le prompt modèle ; 2) testez votre voisin (il répond sans regarder) ; 3) notez les cartes ratées et reprogrammez-les à J+3.

**Solution :** Exemple de paquet réussi : 10 cartes numérotées, questions courtes (« Quelle est la règle d'accord du participe avec avoir ? »), réponses d'1 phrase, 2 cartes jugées trop longues découpées en 4, planning noté : revoir les 3 ratées à J+3.

---

## 💭 As-tu bien compris ?

- **Pourquoi se tester est-il plus efficace que relire ?**
   - ✅ Parce que l'effort de retrouver l'information en mémoire crée une trace durable, alors que relire donne seulement une impression de familiarité.
- **Que faire après un QCM raté à 6/10 ?**
   - ✅ Noter chaque erreur en 1 phrase dans le carnet, revoir les points ratés à J+3, puis demander une version mélangée du QCM.
- **Quelle est la différence entre demander la réponse et demander à être interrogé ?**
   - ✅ Demander la réponse = lecture passive. Demander à être interrogé (tuteur socratique) = rappel actif : c'est votre cerveau qui travaille.

---

## 🧠 Fiche de synthèse — points clés

- Se tester bat relire : le rappel actif crée la mémoire.
- Espacer : J+1, J+3, J+7, J+14 — jamais tout la veille.
- 1 flashcard = 1 question + 1 réponse courte.
- QCM chronométré sans le cours + carnet d'erreurs (1 phrase par erreur).
- Tuteur socratique : l'IA interroge, vous répondez, elle indice.

> 🏁 🏁 Réviser avec l'IA, c'est comme avoir un coach sportif personnel : il prépare les exercices, compte les répétitions et vous encourage — mais les muscles, c'est vous qui les construisez.

---

## ✅ Quiz éclair (1 min)

**Q1. Pourquoi relire 5 fois donne une fausse confiance ?**
   - 🔘 Parce que le texte change
   - ✅ Parce que la familiarité ressemble au savoir sans être la mémoire
   - 🔘 Parce que c'est interdit
   - 🔘 Parce que c'est trop rapide
**Q2. Quel est le bon planning de révision espacée ?**
   - 🔘 Tout la veille
   - ✅ J+1, J+3, J+7, J+14
   - 🔘 Une fois par mois
   - 🔘 Jamais, c'est inutile
**Q3. Que contient une bonne flashcard ?**
   - 🔘 Tout un chapitre
   - ✅ 1 question + 1 réponse courte
   - 🔘 Seulement une image
   - 🔘 La correction complète

---

## ✏️ Activités et exercices

1. Fabrique de flashcards : générer 10 cartes depuis sa fiche, tester son voisin, trier su/pas su.
1. QCM chrono : générer un QCM de 10 questions, le faire en 15 min sans le cours, analyser les erreurs.
1. Duo socratique : l'un joue le tuteur-IA (questions + indices), l'autre répond ; puis on inverse.
1. Examen blanc : sujet généré depuis une annale, 30 min chrono, correction croisée en binôme.

---

## 🧠 À retenir

- Tester > relire : le rappel actif construit la mémoire.
- Espacer J+1, J+3, J+7, J+14 ; dormir consolide.
- Flashcards : 1 carte = 1 question + 1 réponse courte.
- QCM chronométré sans cours + carnet d'erreurs.
- Tuteur socratique : jamais de réponse directe, toujours une question d'abord.

---

# 🎓 Merci de votre attention

**Séance 06 — Réviser efficacement et simuler des examens**

*Prochaine séance : venez avec un ordinateur ou un smartphone.*

Dr. Madani BELACEL — ENS Université de Mostaganem