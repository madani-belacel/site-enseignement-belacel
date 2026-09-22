---
marp: true
theme: default
paginate: true
size: 16:9
title: Séance 07 — IA et programmation — mini-projet Python
---

# 🐍 Séance 07 — IA et programmation — mini-projet Python

*AI and programming — Python mini-project*

**Module Intelligence Artificielle — 2ème année PEP · ENS**

Dr. Madani BELACEL — Université de Mostaganem

---

## ⏱️ Déroulé de la séance (1 h 30)

- **00–05** — Accroche : le commis cuisinier
- **05–25** — Explication : comprendre et déboguer avec l'IA
- **25–50** — Démo : la clé API + le premier script
- **50–70** — Exercice guidé : ajoutez la mémoire
- **70–80** — Démo 2 : Cursor / Copilot en action
- **80–90** — Synthèse, quiz et annonce de la séance 8

---

## 🎯 Objectifs pédagogiques

- Expliquer un algorithme simple avec l'aide de l'IA, ligne par ligne.
- Déboguer un script Python : lire l'erreur, demander un diagnostic, corriger.
- Obtenir une clé API gratuite (Gemini) et l'utiliser sans la partager.
- Exécuter le script assistant_chat.py et dialoguer avec sa propre IA.
- Modifier le script (mémoire de conversation) et expliquer chaque ajout.

---

## 🎬 Accroche (5 min)

❓ Et si votre prochain exercice de programmation se corrigeait tout seul… en vous expliquant vos propres erreurs ? C'est exactement ce qu'on va construire aujourd'hui.

🍳 **Analogie :** 🍳 Programmer avec l'IA, c'est comme cuisiner avec un commis : c'est vous le chef (vous décidez du plat), le commis épluche et coupe (il écrit le code répétitif), mais vous goûtez chaque étape — sinon le plat est raté.

💡 💡 Une API, c'est un guichet : votre petit script Python y dépose une question, et le grand modèle d'IA y répond. Aujourd'hui, vous construisez le guichet.

---

## Comprendre le code : l'IA comme professeur particulier

- Ne demandez jamais « fais mon TP » : demandez « explique-moi ». Un étudiant qui comprend 10 programmes expliqués progresse ; celui qui rend 10 programmes générés stagne.
- **Prompt explication :** « Explique ce code ligne par ligne, comme à un débutant : [coller le code]. »
- **Prompt algorithme :** « Explique la recherche du maximum dans une liste avec un exemple chiffré pas à pas. »
- **Prompt comparaison :** « Quelle est la différence entre une boucle for et while ? Un exemple chacun. »
- 💡 **🔗 Rappel séance 6 :** le tuteur socratique posait des questions au lieu de donner les réponses. Aujourd'hui, on le CODE : notre script posera des questions à Gemini au lieu de tout faire à notre place.

*Understand code: AI as a private teacher*

---

## Déboguer : lire l'erreur avant de la réparer

- Un message d'erreur n'est pas une insulte : c'est une adresse (le numéro de ligne) et un diagnostic (le type d'erreur). Montrez les deux à l'IA, et demandez d'abord le POURQUOI.
- **Méthode en 3 temps :** 1) lire la dernière ligne de l'erreur ; 2) demander « pourquoi cette erreur ? » ; 3) seulement ensuite « comment corriger ? ».
- **Prompt modèle :** « Voici mon code [coller] et l'erreur [coller]. Explique la cause en 2 phrases, puis propose UNE correction. »
- **Erreurs classiques PEP :** indentation, deux-points oubliés, variable non définie, mélange de types.
- 💡 **Astuce :** après la correction, demandez « donne-moi un mini-exercice similaire pour vérifier que j'ai compris ». La boucle est bouclée : erreur → cause → correction → vérification.
- 💡 **🧪 Exemple concret :** moyenne = total / nombre. Une TypeError mélangeant texte et nombres → cause : un âge lu comme texte → correction : int(age). Demandez ensuite un exercice similaire avec des notes.

*Debug: read the error before fixing it*

---

## Le mini-projet : votre assistant qui appelle Gemini

- Une API (interface de programmation) est un guichet : votre script envoie du texte, le modèle géant répond. Avec une clé gratuite, 15 lignes de Python suffisent pour avoir VOTRE chatbot.
- **Clé gratuite :** aller sur ai.google.dev → « Get API key » → copier (comme un mot de passe, jamais partagée).
- **Installer :** **python -m pip install google-generativeai** dans le terminal.
- **Copier** le script assistant_chat.py ci-dessous, coller la clé, exécuter : **python assistant_chat.py**.
- **Tester :** poser 3 questions de révision de votre module préféré.
- 💡 **🔒 Sécurité :** la clé API, c'est un mot de passe payant. Jamais dans un devoir rendu, jamais sur GitHub, jamais en photo. Si elle fuite, la régénérer sur ai.google.dev.

*The mini-project: your assistant calling Gemini*

---

## Aller plus loin : Copilot, Cursor et la mémoire

- Deuxième étage de la fusée : les assistants intégrés à l'éditeur (complétion pendant la frappe) et l'historique (le chatbot qui se souvient).
- **Cursor / Copilot :** écrivez un commentaire « # fonction qui calcule la moyenne », laissez l'outil proposer le code, LISEZ-LE avant d'accepter.
- **Mémoire :** la version assistant_memoire.py garde les 6 derniers échanges : testez « et en arabe ? » après une question.
- **Limite :** l'assistant écrit vite mais ne comprend pas votre TP — seul votre test (exécution + cas limites) valide.

*Go further: Copilot, Cursor and memory*

---

## Comment en profiter au maximum

- Le programmeur augmenté : l'IA propose, vous disposez. Chaque ligne générée est relue, exécutée et testée — c'est ce qui distingue l'étudiant de l'opérateur de copier-coller.
- 💡 **➡️ Pont vers la séance 8 :** un programme qui écrit bien impressionne, mais un étudiant qui écrit bien convainc : votre assistant servira aussi à relire vos textes (correction expliquée, séance 8).
- **✅ Explique-moi d'abord :** toujours comprendre avant de rendre.
- **✅ Une erreur = une leçon :** noter la cause dans un carnet de bugs.
- **✅ Versionnez :** garder assistant_chat.py puis assistant_memoire.py (voir la progression).
- **✅ Testez les limites :** question vide, très longue, en arabe dialectal — que se passe-t-il ?

*How to get the most out of it*

---

## 📺 À regarder après la classe

- **Playlist IA de Mohammad Dawoud (introduction, ML, réseaux de neurones)** (ar) — https://www.youtube.com/watch?v=H5WUwwivEaI&list=PLbR_CTcUs1088jfqbbO5AqwODO9MgYA85
- **But what is a neural network? (3Blue1Brown)** (en) — https://www.youtube.com/watch?v=aircAruvnKk
- **Apprendre Python + utiliser l'API Gemini (tutoriel)** (fr) — https://www.youtube.com/results?search_query=gemini+api+python+tutorial+debutant

---

## ✏️ Exercice guidé (15 min)

**Énoncé :** 1) Exécutez assistant_chat.py et posez 3 questions de cours. 2) Créez assistant_memoire.py (ajout de l'historique). 3) Testez la mémoire : question puis « résume ta réponse précédente en 1 phrase ».

**Solution :** Version 1 répond à chaque question isolément (oublie le contexte). Version 2 avec historique répond correctement aux suites (« et en arabe ? », « résume »). Si erreur d'API : vérifier la clé, le Wi-Fi et le nom du modèle (gemini-2.0-flash).

---

## 💭 As-tu bien compris ?

- **Qu'est-ce qu'une clé API et pourquoi la protéger ?**
   - ✅ C'est le mot de passe qui identifie votre compte auprès du modèle et peut être facturé. Partagée = quelqu'un dépense à votre place.
- **Pourquoi demander le POURQUOI de l'erreur avant la correction ?**
   - ✅ Comprendre la cause évite de répéter l'erreur ; copier la correction sans comprendre la garantit au prochain TP.
- **Que change l'historique dans assistant_memoire.py ?**
   - ✅ Les 6 derniers échanges sont renvoyés au modèle : il comprend les suites comme « et en arabe ? » sans répéter la question.

---

## 🧠 Fiche de synthèse — points clés

- Explique-moi > fais-moi : comprendre avant de rendre.
- Débogage : lire l'erreur, demander le POURQUOI, puis corriger.
- API = guichet : clé gratuite sur ai.google.dev, jamais partagée.
- 15 lignes suffisent : assistant_chat.py dialogue avec Gemini.
- Mémoire = renvoyer les 6 derniers échanges au modèle.

> 🏁 🏁 Programmer avec l'IA, c'est comme apprendre à conduire avec un moniteur : au début il tient le volant avec vous, mais l'examen, c'est vous seul qui le passez — et la route ensuite aussi.

---

## ✅ Quiz éclair (1 min)

**Q1. Quel est le meilleur premier prompt face à un code incompris ?**
   - 🔘 « Fais mon TP »
   - ✅ « Explique ce code ligne par ligne, comme à un débutant »
   - 🔘 « C'est nul, recommence »
   - 🔘 « Donne-moi un autre code »
**Q2. Face à une erreur Python, quel est le bon ordre ?**
   - 🔘 Corriger puis comprendre
   - ✅ Lire l'erreur → demander le POURQUOI → corriger → vérifier
   - 🔘 Supprimer le fichier
   - 🔘 Changer de langage
**Q3. Où obtenir une clé Gemini et comment la traiter ?**
   - 🔘 Sur Google, à partager
   - ✅ Sur ai.google.dev, comme un mot de passe jamais partagé
   - 🔘 Dans le script d'un ami
   - 🔘 Pas besoin de clé

---

## ✏️ Activités et exercices

1. Explication croisée : l'IA explique un tri, chaque binôme le réexplique sans écran.
1. Chasse au bug : 3 scripts piégés (indentation, variable, type) à diagnostiquer avant de corriger.
1. Premier appel : clé + pip install + assistant_chat.py → 3 questions de révision.
1. Défi mémoire : ajouter l'historique puis réussir le test « résume ta réponse précédente ».

---

## 🧠 À retenir

- Explique-moi > fais-moi : la compréhension d'abord.
- Déboguer : lire, POURQUOI, corriger, vérifier.
- Clé sur ai.google.dev, jamais partagée, jamais sur GitHub.
- assistant_chat.py : 15 lignes pour parler à Gemini.
- La mémoire, c'est le script qui rappelle la conversation au modèle.

---

# 🎓 Merci de votre attention

**Séance 07 — IA et programmation — mini-projet Python**

*Prochaine séance : venez avec un ordinateur ou un smartphone.*

Dr. Madani BELACEL — ENS Université de Mostaganem