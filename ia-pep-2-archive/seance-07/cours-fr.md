# Séance 07 — IA et programmation — mini-projet Python

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Comprendre le code, déboguer avec l'IA, puis construire un vrai assistant Python qui appelle l'API Gemini : clé gratuite, script commenté, exécution et modification.

## Objectifs pédagogiques
- Expliquer un algorithme simple avec l'aide de l'IA, ligne par ligne.
- Déboguer un script Python : lire l'erreur, demander un diagnostic, corriger.
- Obtenir une clé API gratuite (Gemini) et l'utiliser sans la partager.
- Exécuter le script assistant_chat.py et dialoguer avec sa propre IA.
- Modifier le script (mémoire de conversation) et expliquer chaque ajout.

## Déroulé de la séance (1 h 30)
- **00–05 — Accroche : le commis cuisinier** : Question d'ouverture + analogie du chef et du commis.
- **05–25 — Explication : comprendre et déboguer avec l'IA** : 3 idées : faire expliquer le code ligne par ligne ; lire les messages d'erreur ; demander un diagnostic avant la solution.
- **25–50 — Démo : la clé API + le premier script** : ai.google.dev → clé gratuite → pip install → assistant_chat.py qui répond.
- **50–70 — Exercice guidé : ajoutez la mémoire** : Transformer le script : garder les 6 derniers échanges pour le contexte.
- **70–80 — Démo 2 : Cursor / Copilot en action** : Auto-complétion en direct : écrire un commentaire, laisser l'outil compléter, vérifier.
- **80–90 — Synthèse, quiz et annonce de la séance 8** : « À retenir ». Annonce : rédaction académique et anti-plagiat.

## A. Accroche et analogie (5 min)
- **Question :** Et si votre prochain exercice de programmation se corrigeait tout seul… en vous expliquant vos propres erreurs ? C'est exactement ce qu'on va construire aujourd'hui.
- **Analogie :** 🍳 Programmer avec l'IA, c'est comme cuisiner avec un commis : c'est vous le chef (vous décidez du plat), le commis épluche et coupe (il écrit le code répétitif), mais vous goûtez chaque étape — sinon le plat est raté.
- **En une phrase :** 💡 Une API, c'est un guichet : votre petit script Python y dépose une question, et le grand modèle d'IA y répond. Aujourd'hui, vous construisez le guichet.

## B + C. Explication pas à pas et démonstration
### Comprendre le code : l'IA comme professeur particulier
Ne demandez jamais « fais mon TP » : demandez « explique-moi ». Un étudiant qui comprend 10 programmes expliqués progresse ; celui qui rend 10 programmes générés stagne.

- <strong>Prompt explication :</strong> « Explique ce code ligne par ligne, comme à un débutant : [coller le code]. »
- <strong>Prompt algorithme :</strong> « Explique la recherche du maximum dans une liste avec un exemple chiffré pas à pas. »
- <strong>Prompt comparaison :</strong> « Quelle est la différence entre une boucle for et while ? Un exemple chacun. »
> 💡 **<strong>🔗 Rappel séance 6 :</strong> le tuteur socratique posait des questions au lieu de donner les réponses. Aujourd'hui, on le CODE : notre script posera des questions à Gemini au lieu de tout faire à notre place.**

### Déboguer : lire l'erreur avant de la réparer
Un message d'erreur n'est pas une insulte : c'est une adresse (le numéro de ligne) et un diagnostic (le type d'erreur). Montrez les deux à l'IA, et demandez d'abord le POURQUOI.

- <strong>Méthode en 3 temps :</strong> 1) lire la dernière ligne de l'erreur ; 2) demander « pourquoi cette erreur ? » ; 3) seulement ensuite « comment corriger ? ».
- <strong>Prompt modèle :</strong> « Voici mon code [coller] et l'erreur [coller]. Explique la cause en 2 phrases, puis propose UNE correction. »
- <strong>Erreurs classiques PEP :</strong> indentation, deux-points oubliés, variable non définie, mélange de types.
> 💡 **<strong>Astuce :</strong> après la correction, demandez « donne-moi un mini-exercice similaire pour vérifier que j'ai compris ». La boucle est bouclée : erreur → cause → correction → vérification.**
> 💡 **<strong>🧪 Exemple concret :</strong> moyenne = total / nombre. Une TypeError mélangeant texte et nombres → cause : un âge lu comme texte → correction : int(age). Demandez ensuite un exercice similaire avec des notes.**

### Le mini-projet : votre assistant qui appelle Gemini
Une API (interface de programmation) est un guichet : votre script envoie du texte, le modèle géant répond. Avec une clé gratuite, 15 lignes de Python suffisent pour avoir VOTRE chatbot.

- <strong>Clé gratuite :</strong> aller sur ai.google.dev → « Get API key » → copier (comme un mot de passe, jamais partagée).
- <strong>Installer :</strong> <strong>python -m pip install google-generativeai</strong> dans le terminal.
- <strong>Copier</strong> le script assistant_chat.py ci-dessous, coller la clé, exécuter : <strong>python assistant_chat.py</strong>.
- <strong>Tester :</strong> poser 3 questions de révision de votre module préféré.

```
# assistant_chat.py -- mini assistant IA (projet seance 07)
# Installation : python -m pip install google-generativeai
import google.generativeai as genai

# 1. Cle gratuite sur https://ai.google.dev (ne jamais la partager !)
genai.configure(api_key="COLLE_TA_CLE_ICI")

# 2. Choix du modele (rapide et gratuit)
model = genai.GenerativeModel("gemini-2.0-flash")

print("Assistant IA pour etudiant (tape 'quit' pour sortir)")
while True:
    question = input("\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    reponse = model.generate_content(question)
    print("IA   >", reponse.text)
```
> 💡 **<strong>🔒 Sécurité :</strong> la clé API, c'est un mot de passe payant. Jamais dans un devoir rendu, jamais sur GitHub, jamais en photo. Si elle fuite, la régénérer sur ai.google.dev.**

### Aller plus loin : Copilot, Cursor et la mémoire
Deuxième étage de la fusée : les assistants intégrés à l'éditeur (complétion pendant la frappe) et l'historique (le chatbot qui se souvient).

- <strong>Cursor / Copilot :</strong> écrivez un commentaire « # fonction qui calcule la moyenne », laissez l'outil proposer le code, LISEZ-LE avant d'accepter.
- <strong>Mémoire :</strong> la version assistant_memoire.py garde les 6 derniers échanges : testez « et en arabe ? » après une question.
- <strong>Limite :</strong> l'assistant écrit vite mais ne comprend pas votre TP — seul votre test (exécution + cas limites) valide.

```
# assistant_memoire.py -- meme assistant, AVEC memoire de conversation
import google.generativeai as genai

genai.configure(api_key="COLLE_TA_CLE_ICI")
model = genai.GenerativeModel("gemini-2.0-flash")

# Nouveaute : l'historique garde le contexte des questions precedentes
historique = []

print("Assistant avec memoire (tape 'quit' pour sortir)")
while True:
    question = input("\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    historique.append("Etudiant : " + question)
    prompt = "\n".join(historique[-6:])  # les 6 derniers echanges
    reponse = model.generate_content(prompt)
    historique.append("IA : " + reponse.text)
    print("IA   >", reponse.text)
```

### Comment en profiter au maximum
Le programmeur augmenté : l'IA propose, vous disposez. Chaque ligne générée est relue, exécutée et testée — c'est ce qui distingue l'étudiant de l'opérateur de copier-coller.
> 💡 **<strong>➡️ Pont vers la séance 8 :</strong> un programme qui écrit bien impressionne, mais un étudiant qui écrit bien convainc : votre assistant servira aussi à relire vos textes (correction expliquée, séance 8).**

- <strong>✅ Explique-moi d'abord :</strong> toujours comprendre avant de rendre.
- <strong>✅ Une erreur = une leçon :</strong> noter la cause dans un carnet de bugs.
- <strong>✅ Versionnez :</strong> garder assistant_chat.py puis assistant_memoire.py (voir la progression).
- <strong>✅ Testez les limites :</strong> question vide, très longue, en arabe dialectal — que se passe-t-il ?
> 💡 **<strong>❌ Erreurs à éviter :</strong> rendre du code non exécuté, partager sa clé API, croire que « ça marche une fois » = « c'est correct » (tester les cas limites).**

|  | Mauvais usage | Bon usage |
|---|---|---|
| Demande | « Fais mon TP de tri. » | « Explique le tri par sélection avec un exemple [7, 2, 9], puis donne-moi un exercice similaire. » |
| Résultat | Code rendu, rien compris, zéro le jour de l'examen. | Compréhension + entraînement, autonome le jour J. |

## 📺 Ressources vidéo
- **Playlist IA de Mohammad Dawoud (introduction, ML, réseaux de neurones)** (ar): https://www.youtube.com/watch?v=H5WUwwivEaI&list=PLbR_CTcUs1088jfqbbO5AqwODO9MgYA85 — La référence du module : comprendre ce qu'il y a SOUS le guichet API (neurones, apprentissage).
- **But what is a neural network? (3Blue1Brown)** (en): https://www.youtube.com/watch?v=aircAruvnKk — Visualiser comment un réseau apprend — sous-titres FR disponibles.
- **Apprendre Python + utiliser l'API Gemini (tutoriel)** (fr): https://www.youtube.com/results?search_query=gemini+api+python+tutorial+debutant — Voir chaque étape (clé, pip install, premier appel) faite en vidéo avant de la refaire.

## D. Exercice guidé (15 min)
**Énoncé :** 1) Exécutez assistant_chat.py et posez 3 questions de cours. 2) Créez assistant_memoire.py (ajout de l'historique). 3) Testez la mémoire : question puis « résume ta réponse précédente en 1 phrase ».
**Méthode :** 1) Vérifiez Python : python --version. 2) Installez la bibliothèque. 3) Collez la clé SANS la montrer à votre voisin d'écran. 4) Lancez, testez, puis ajoutez la liste historique. 5) Comparez les deux versions sur la même question de suivi.
**Solution :** Version 1 répond à chaque question isolément (oublie le contexte). Version 2 avec historique répond correctement aux suites (« et en arabe ? », « résume »). Si erreur d'API : vérifier la clé, le Wi-Fi et le nom du modèle (gemini-2.0-flash).

## 💭 As-tu bien compris ?
- **Q1.** Qu'est-ce qu'une clé API et pourquoi la protéger ?
  *Réponse :* C'est le mot de passe qui identifie votre compte auprès du modèle et peut être facturé. Partagée = quelqu'un dépense à votre place.
- **Q2.** Pourquoi demander le POURQUOI de l'erreur avant la correction ?
  *Réponse :* Comprendre la cause évite de répéter l'erreur ; copier la correction sans comprendre la garantit au prochain TP.
- **Q3.** Que change l'historique dans assistant_memoire.py ?
  *Réponse :* Les 6 derniers échanges sont renvoyés au modèle : il comprend les suites comme « et en arabe ? » sans répéter la question.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- Explique-moi > fais-moi : comprendre avant de rendre.
- Débogage : lire l'erreur, demander le POURQUOI, puis corriger.
- API = guichet : clé gratuite sur ai.google.dev, jamais partagée.
- 15 lignes suffisent : assistant_chat.py dialogue avec Gemini.
- Mémoire = renvoyer les 6 derniers échanges au modèle.
### Analogies utilisées
- 🍳 Le commis cuisinier : il prépare, vous goûtez et décidez.
- 🍳 Le guichet API : vous déposez une question, le géant répond.
- 🍳 Le carnet de bugs : chaque erreur notée est un piège désamorcé.
### Exemples concrets
- ✏️ « Explique ce tri ligne par ligne » → l'étudiant comprend et refait seul.
- ✏️ IndentationError → cause comprise → correction + mini-exercice de vérification.
- ✏️ « Et en arabe ? » compris grâce à l'historique des 6 échanges.
> 🏁 **Analogie finale :** 🏁 Programmer avec l'IA, c'est comme apprendre à conduire avec un moniteur : au début il tient le volant avec vous, mais l'examen, c'est vous seul qui le passez — et la route ensuite aussi.
### Quiz — vérifie ta compréhension
**Q1.** Quel est le meilleur premier prompt face à un code incompris ?
   - 🔘 « Fais mon TP »
   - ✅ « Explique ce code ligne par ligne, comme à un débutant »
   - 🔘 « C'est nul, recommence »
   - 🔘 « Donne-moi un autre code »
   *Explication :* L'explication construit la compréhension ; le code tout fait la contourne.
**Q2.** Face à une erreur Python, quel est le bon ordre ?
   - 🔘 Corriger puis comprendre
   - ✅ Lire l'erreur → demander le POURQUOI → corriger → vérifier
   - 🔘 Supprimer le fichier
   - 🔘 Changer de langage
   *Explication :* La cause comprise + un mini-exercice de vérification ferment la boucle d'apprentissage.
**Q3.** Où obtenir une clé Gemini et comment la traiter ?
   - 🔘 Sur Google, à partager
   - ✅ Sur ai.google.dev, comme un mot de passe jamais partagé
   - 🔘 Dans le script d'un ami
   - 🔘 Pas besoin de clé
   *Explication :* La clé est gratuite sur ai.google.dev mais facturable : fuite = quelqu'un dépense à votre place.
**Q4.** Que fait la liste historique dans assistant_memoire.py ?
   - 🔘 Elle sauvegarde sur disque
   - ✅ Elle renvoie les 6 derniers échanges pour garder le contexte
   - 🔘 Elle accélère Internet
   - 🔘 Elle traduit le code
   *Explication :* Le modèle est sans mémoire : c'est le script qui lui rappelle la conversation à chaque appel.
**Q5.** Pourquoi tester les cas limites (question vide, très longue) ?
   - 🔘 Pour perdre du temps
   - ✅ Parce que « marche une fois » n'est pas « correct » : seul le test valide
   - 🔘 Pour impressionner
   - 🔘 C'est interdit
   *Explication :* Un programme se juge sur les cas normaux ET limites : c'est la marque du programmeur, pas du copieur.

## Activités et exercices
- Explication croisée : l'IA explique un tri, chaque binôme le réexplique sans écran.
- Chasse au bug : 3 scripts piégés (indentation, variable, type) à diagnostiquer avant de corriger.
- Premier appel : clé + pip install + assistant_chat.py → 3 questions de révision.
- Défi mémoire : ajouter l'historique puis réussir le test « résume ta réponse précédente ».

## À retenir
- Explique-moi > fais-moi : la compréhension d'abord.
- Déboguer : lire, POURQUOI, corriger, vérifier.
- Clé sur ai.google.dev, jamais partagée, jamais sur GitHub.
- assistant_chat.py : 15 lignes pour parler à Gemini.
- La mémoire, c'est le script qui rappelle la conversation au modèle.

## Glossaire
- **API** : Guichet logiciel : votre programme envoie une demande, le service (Gemini) répond.
- **Clé API** : Mot de passe personnel qui identifie vos appels au service ; gratuite mais facturable, à protéger.
- **Débogage** : Art de trouver la cause d'une erreur (lire, diagnostiquer) avant de la corriger.
- **Bibliothèque (package)** : Code prêt à l'emploi qu'on installe (pip install) pour utiliser un service comme Gemini.
- **Historique de conversation** : Échanges précédents renvoyés au modèle pour qu'il garde le contexte.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)