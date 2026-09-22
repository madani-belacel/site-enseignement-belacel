### 1. Résumé du projet

- Nom du module : Intelligence Artificielle en Éducation — PEP 2A
- Public : étudiants de 2e année PEP (ENS), futurs professeurs des écoles primaires
- Objectif final en 3 lignes : permettre à un étudiant de savoir utiliser concrètement l’IA dans ses études, de produire des résultats utiles sans jargon, et de développer un esprit critique face aux réponses générées.

Ce qui a été fait :
- le module IA a été construit en 10 séances, avec pages HTML trilingues FR/EN/AR, documents markdown, quiz, PowerPoint et onglets de langue ;
- le module contient déjà un socle de contenu pédagogique (outils, démonstrations, support de cours, synthèse, ressources).

Ce qui ne marche pas :
- le contenu est écris comme un plan de cours pour l’enseignant, pas comme un guide concret pour l’étudiant ;
- les pages privilégient la théorie, les définitions et les questions-réponses au lieu de montrer des actions réelles dans des outils ;
- l’étudiant ne sort pas de la page avec un vrai comportement d’usage : ouvrir un outil, poser un bon prompt, vérifier, corriger, comparer, reprendre.

Ce qui reste à faire :
- refondre la structure pédagogique de chaque séance selon un modèle « action → démonstration → application » ;
- garder les éléments de design et de navigation du site, mais supprimer les sections pédagogiques inutiles ;
- réécrire les pages de séance de manière directe, pratique et exploitable sans enseignant.

### 2. Diagnostic du contenu actuel

Problèmes concrets observés dans le module IA actuel :

1. Théorie dominante, pratique absente
   - La page de séance 01 contient encore les sections typiques de plan de cours : « Objectifs pédagogiques », « Prérequis », « Déroulé de la séance (1 h 30) », « Mission — le livrable », « Checklist de validation », « Atelier ».
   - Ces éléments sont utiles à un enseignant qui prépare sa séance, mais inutiles à un étudiant qui veut comprendre comment faire.
   - Exemple de phrases actuelles :
     - « Déroulé de la séance (1 h 30) »
     - « Objectifs pédagogiques »
     - « Action immédiate »
     - « Votre mission — le livrable »
     - « Checklist de validation »

2. Pas d’usage réel des outils
   - Le contenu explique ce que c’est l’IA, mais ne montre pas assez le réel comportement de l’étudiant : ouvrir ChatGPT, taper un prompt, relire la réponse, tester, corriger, comparer.
   - L’étudiant peut lire des définitions, mais n’est pas guidé vers un premier vrai usage concret.

3. Structure trop « Q/R » et trop longue
   - Le module présente beaucoup de définitions, de vocabulaire, de quiz, de synthèse, mais peu de micro-tâches concrètes exécutables.
   - L’effet est intellectuel plutôt que pratique : l’étudiant sait « parler de l’IA », mais pas encore l’utiliser.

4. Sélecteur FR/EN/AR OK, mais contenu pédagogique parfois encore orienté enseignant
   - Le mécanisme trilingue est bien présent et doit être conservé.
   - Le problème n’est pas la langue, mais la logique didactique : le texte parle à l’enseignant, pas à l’étudiant.

5. Le module a de bonnes briques techniques, mais pas le bon angle
   - Le site a déjà : header, breadcrumb, footer, navigation, styles, ressources, quiz, vidéos, glossaire, génération automatique via Python.
   - Il manque surtout un angle de lecture étudiant : « tu ouvres cet outil, tu tapes cela, tu vois ça, tu vérifies ça ».

Exemples précis à corriger :
- « Objectifs pédagogiques » : section très proche d’un plan d’enseignement.
- « Déroulé de la séance (1 h 30) » : découpage en phases A/B/C/D/E, précis pour un formateur, inutile pour l’étudiant.
- « Mission — le livrable » : objectif de production, mais pas de véritable guide d’usage.
- « Atelier », « en binôme », « au tableau », « le formateur » : termes qui doivent être supprimés.

Autre point crucial : la charte actuelle du module IA est intéressante dans sa logique globale, mais la pédagogie actuelle n’est pas centrée sur l’étudiant. Le consultant devra réécrire le module en gardant la mécanique du site, mais en changeant complètement l’angle d’écriture.

### 3. Format cible (basé sur TIC)

> Le format TIC sert uniquement de référence pour le header, breadcrumb, footer, navigation et cohérence visuelle du site. Le contenu du module IA sera complètement différent : long, pratique, avec prompts copiables et captures décrites. Ne pas chercher à reproduire la concision du TIC.

Le but n’est pas de copier le module TIC. Le but est de garder sa rigueur visuelle et de remplacer son contenu théorique par un vrai guide d’usage pour l’étudiant.

Ce qu’on garde :
- header du site ;
- breadcrumb ;
- footer ;
- sélecteur FR/EN/AR ;
- navigation claire ;
- design cohérent avec le reste du site.

Ce qu’on change :
- on quitte la logique de dossier statique et de liste de ressources ;
- on remplace la logique du cours par une logique d’action ;
- on parle à l’étudiant, pas au formateur ;
- on utilise des prompts réels, des étapes claires et des observations concrètes.

### 4. Structure pédagogique imposée pour chaque séance

Chaque séance doit suivre exactement cette structure, dans l’ordre suivant :

1. Titre clair
   - Format : `Séance XX — [Titre clair]`
   - Exemple : `Séance 01 — Comprendre l'IA et lui parler pour la première fois`

2. En une phrase
   - Une seule phrase qui dit ce que l’étudiant va apprendre à faire.
   - Exemple : « À la fin de cette séance, tu sauras ouvrir ChatGPT, lui poser une question utile et juger sa réponse. »

3. Pourquoi c’est utile pour toi
   - 3 à 4 lignes concrètes.
   - L’angle doit être : « cela te servira à … »

4. Les 3 idées essentielles
   - 3 puces, 1 à 2 phrases chacune.

5. Comment faire — pas à pas
   - 3 à 6 étapes.
   - Pour chaque étape :
     - Où : URL ou chemin exact ;
     - Quoi taper : prompt complet dans un bloc `<pre><code>` ;
     - Ce que tu vas voir : résultat réel et observable ;
     - Astuce : conseil utile.

6. Exemples réels
   - 2 à 3 exemples concrets ;
   - chacun avec prompt, réponse attendue, astuce.

7. Les astuces que personne ne dit
   - 5 à 7 astuces courtes et directes.

8. Erreurs à éviter
   - 3 erreurs en format : `❌ erreur → ✅ correction`

9. À retenir
   - 3 à 5 puces ultra-courtes.

10. Vidéos
   - Garder tel quel.

11. Quiz
   - Garder tel quel.

12. Glossaire
   - Garder tel quel.

13. Ressources téléchargeables
   - Garder tel quel.

14. Navigation
   - Garder tel quel.

Longueur cible :
- Par séance HTML : 800 à 1200 mots maximum.
- Par prompt copiable : 1 à 3 lignes.
- Par astuce : 1 à 2 lignes.
- Page entière : lisible en 10 minutes de lecture active.

À supprimer de façon définitive :
- « Déroulé de la séance (1 h 30) »
- « Objectifs pédagogiques »
- « Prérequis »
- « Action immédiate »
- « Recette pas à pas »
- « Mission — le livrable »
- « Checklist de validation »
- « Activités et exercices »
- « Atelier »
- « Démo »
- toute mention de « en binôme », « ton voisin », « au tableau », « le formateur »

À conserver :
- header, breadcrumb, footer, sélecteur FR/EN/AR ;
- titre, vidéos, quiz, glossaire, ressources, navigation, CSS existant ;
- trilinguisme FR/EN/AR ;
- design du site.

### 5. Liste des 10 séances avec objectifs d'action

| # | Titre définitif | Action concrète |
|---|---|---|
| S01 | Comprendre l'IA et lui parler pour la première fois | Ouvrir ChatGPT, poser 2 questions, identifier une hallucination |
| S02 | Panorama des 14 outils d'IA pour l'étudiant | Tester 3 outils (ChatGPT, Perplexity, Gemini) sur la même question, comparer |
| S03 | Chercher et vérifier l'information avec l'IA | Trouver 5 sources fiables sur un sujet de cours réel |
| S04 | Résumer, synthétiser et créer des fiches de révision | Transformer un chapitre réel en fiche de 1 page |
| S05 | Préparer un exposé de A à Z avec l'IA | Générer plan + slides + script oral d'un exposé réel |
| S06 | Réviser efficacement et simuler des examens | Générer 10 QCM + flashcards sur un chapitre réel |
| S07 | Programmer avec l'IA — mini-projet Python | Écrire un script Python qui interroge une API IA |
| S08 | Rédiger, corriger et traduire un texte académique | Rédiger un paragraphe + corriger + traduire en anglais |
| S09 | Organiser sa vie d'étudiant avec l'IA | Créer un planning de révision réel dans Notion AI |
| S10 | Construire son IA + Charte d'usage responsable | Créer un chatbot Dify sur ses propres cours + rédiger sa charte |

Pour chaque séance, on ajoute 3 prompts prêts à copier :

- S01
  - `Explique-moi ce qu'est l'intelligence artificielle comme si j'avais 12 ans, en 3 phrases.`
  - `Donne-moi 3 exemples d'IA que j'utilise sans le savoir dans ma vie quotidienne.`
  - `Donne-moi les sources de tes informations.`

- S02
  - `Réponds à cette question de cours avec 3 outils différents : ChatGPT, Perplexity et Gemini. Compare les réponses en 5 points.`
  - `Donne-moi 3 promps pour trouver des sources fiables sur ce sujet.`
  - `Explique-moi, en 3 niveaux de difficulté, ce que fait cet outil d'IA.`

- S03
  - `Trouve 5 sources fiables sur le thème [sujet] et résume chacune en 2 lignes.`
  - `Compare ces 3 sources et dis-moi laquelle est la plus fiable pour un étudiant.`
  - `Explique-moi la différence entre une source fiable et une source trop vague.`

- S04
  - `Résume ce chapitre en 5 points clés pour un étudiant de 2e année.`
  - `Crée une fiche de révision de 1 page sur ce chapitre.`
  - `Donne-moi 10 flashcards sur ces notions.`

- S05
  - `Crée un plan d'exposé de 6 parties sur [sujet].`
  - `Rédige un script oral de 2 minutes pour présenter ce sujet.`
  - `Génère 6 diapositives claires pour ce plan.`

- S06
  - `Crée 10 QCM sur ce chapitre avec 4 options et une bonne réponse.`
  - `Explique chaque bonne réponse avec une phrase du cours.`
  - `Transforme ce chapitre en 12 flashcards.`

- S07
  - `Écris un script Python simple qui lit un fichier CSV et calcule une moyenne.`
  - `Explique ce code ligne par ligne, puis donne une version plus claire.`
  - `Utilise l'API de [outil IA] pour envoyer une demande simple.`

- S08
  - `Corrige ce paragraphe et explique chaque correction.`
  - `Réécris ce texte de façon plus claire et plus académique.`
  - `Traduis ce paragraphe en anglais, puis vérifie le vocabulaire académique.`

- S09
  - `Crée un planning de révision sur 7 jours pour mon examen de [matière].`
  - `Fais-moi un planning avec 3 priorités, 2 blocs de travail et 1 révision finale.`
  - `Aide-moi à organiser mes tâches de la semaine avec des délais réalistes.`

- S10
  - `Crée un chatbot Dify qui m'aide à réviser mes cours de [matière].`
  - `Rédige ma charte d'usage responsable de l'IA pour l'université.`
  - `Explique quelles limites de l'IA je dois toujours vérifier avant de l'utiliser.`

### 6. Liste des 14 outils d’IA à présenter

1. ChatGPT
   - Type : chatbot généraliste
   - Usage concret : répondre, expliquer, reformuler, corriger, générer des idées
   - Exemple d’exercice : « Explique-moi ce chapitre en 5 points pour un étudiant de 2e année »

2. Gemini
   - Type : chatbot multimodal
   - Usage concret : recherche, résumé, synthèse, aide à la préparation de cours
   - Exemple d’exercice : « Résume ce texte et donne 3 idées pour le reformuler en français standard »

3. Perplexity
   - Type : moteur de recherche assisté par IA
   - Usage concret : trouver des sources, vérifier les faits, comparer réponses
   - Exemple d’exercice : « Donne-moi 5 sources fiables sur le thème X et résume chacune »

4. NotebookLM
   - Type : assistant de documents
   - Usage concret : lire, explorer et synthétiser un PDF ou un chapitre donné
   - Exemple d’exercice : « Analyse ce PDF et donne-moi un plan de révision en 7 points »

5. Claude
   - Type : assistant de rédaction
   - Usage concret : reformuler, clarifier, mettre en forme, aider à la rédaction académique
   - Exemple d’exercice : « Réécris ce paragraphe pour qu’il soit plus clair et plus fluide »

6. Copilot (Microsoft / GitHub)
   - Type : assistant de code / productivité
   - Usage concret : aider à écrire du code, corriger des erreurs, expliquer des commandes
   - Exemple d’exercice : « Écris un script Python pour lire un fichier CSV et calculer les moyennes »

7. DeepSeek
   - Type : modèle de raisonnement, code et aide générale
   - Usage concret : assistance de code, démonstration de logique, explication technique
   - Exemple d’exercice : « Explique étape par étape ce code Python, puis propose une version plus propre »

8. Cursor
   - Type : éditeur de code avec IA
   - Usage concret : écrire, corriger, expliquer et relire des scripts en contexte
   - Exemple d’exercice : « Corrige ce script et explique chaque erreur »

9. Gamma
   - Type : générateur de présentations
   - Usage concret : construction de slides rapides et lisibles
   - Exemple d’exercice : « Crée une présentation de 6 diapositives sur le thème X »

10. Canva Magic Studio
   - Type : création visuelle assistée par IA
   - Usage concret : visuels, cartes mentales, affiches, supports de cours
   - Exemple d’exercice : « Crée une affiche de 1 page pour présenter les 3 avantages de l’IA en éducation »

11. Grammarly / Language tools
   - Type : correcteur de langue
   - Usage concret : vérifier le français, corriger les fautes, améliorer le style
   - Exemple d’exercice : « Corrige ce texte et propose 3 versions : simple, académique, concise »

12. DeepL
   - Type : traducteur assisté
   - Usage concret : traduire des textes, vérifier les nuances, améliorer la qualité
   - Exemple d’exercice : « Traduis ce texte en français standard et corrige les formulations trop littérales »

13. Notion AI / planification assistée
   - Type : organisation / planning
   - Usage concret : organiser les tâches, créer des listes de travail, planifier la semaine
   - Exemple d’exercice : « Fais-moi un planning de révision sur 7 jours pour cet examen »

14. Dify / Ollama / mini-AI locale
   - Type : IA personnalisée / locale
   - Usage concret : créer un assistant simple pour un usage précis, sans dépendre d’un service externe
   - Exemple d’exercice : « Crée un assistant qui me propose des fiches de révision à partir de mon chapitre »

### 7. Pages annexes

#### `outils-ia.html`
Contenu attendu :
- page pratique et comparative des outils ;
- 14 outils présentés avec : type, usage, exemple d’exercice, forces, limites ;
- un style de page « boîte à outils » plus orientée utilité que théorie ;
- une mise en page avec catégories claires : recherche, écriture, présentation, étude, code, organisation ;
- exemples rapides à copier-coller, adaptés à un étudiant PEP 2A.

#### `construire-ia.html`
Contenu attendu :
- 3 approches concrètes :
  1. utiliser un assistant IA prêt à l’emploi ;
  2. construire un flux simple avec Python et API ;
  3. utiliser une IA locale / mini-agent ;
- explication de la logique sans jargon excessif ;
- exemple de mini-projet concret ;
- liens vers des ressources de base ;
- section « ce que tu peux construire toi-même dès maintenant ».

#### `premier-contact.html`
Contenu attendu :
- tutoriel 15 minutes pour un étudiant qui n’a jamais utilisé d’IA ;
- objectif : ouvrir un compte, poser 3 questions types, comparer les réponses, vérifier une hallucination ;
- mini-guide de démarrage très visuel et très simple ;
- un seul message : « je pose une question, je vérifie, je reformule ».

#### `piloter-opencode.html`
Contenu attendu :
- guide pour piloter un agent de code avec DeepSeek ou un modèle équivalent ;
- objectif : transformer l’IA en assistant de travail ;
- étapes : ouvrir le terminal, lancer le bon outil, donner une consigne claire, relire le résultat, demander les corrections ;
- mettre l’accent sur le contrôle humain et l’esprit critique ;
- ne pas faire de la théorie abstraite ; parler comme un étudiant qui veut coder sans se perdre.

### 8. Plan de travail étape par étape

### Étape 1 — Analyser le format TIC et figer le modèle
**Objectif** : comprendre le format TIC, extraire la structure exacte du site et identifier ce qui doit être conservé.
**Fichiers concernés** : `cours/Module TIC/index.html`, `cours/Module Informatique ENS/index.html`, `ia-pep-2/index.html`
**Ce qu’on produit** : un diagnostic de structure écrit dans ce plan.
**Comment on sait que c’est bon** : header, breadcrumb, navigation, style, lisibilité, logique de ressources identifiées.
**Après quoi** : aucune.

### Étape 2 — Diagnostiquer le module IA actuel et identifier les écarts
**Objectif** : comparer le module actuel avec le format de référence et isoler les éléments pédagogiquement inutiles.
**Fichiers concernés** : `ia-pep-2/index.html`, `ia-pep-2/seance-01/index.html`, `ia-pep-2/assets/generer_seances.py`
**Ce qu’on produit** : liste des éléments à supprimer, garder, adapter.
**Comment on sait que c’est bon** : chaque bloc problématique est explicité et transformé en action corrective.
**Après quoi** : étape 1.

### Étape 3 — Figer la structure cible des séances
**Objectif** : décider précisément de la structure de chaque page : titre, en une phrase, pourquoi, idées, comment faire, exemples, astuces, erreurs, à retenir.
**Fichiers concernés** : plan de refonte, modèle de séance S01 en cours de production
**Ce qu’on produit** : un schéma de page réutilisable pour S01 à S10.
**Comment on sait que c’est bon** : structure exacte, ordre validé, contenu orienté étudiant.
**Après quoi** : étape 2.

### Étape 4 — Refaire S01 selon le modèle étudiant (pilote)
**Objectif** : produire une séance pilote, entièrement refondue, qui sert de modèle pour toutes les autres.
**Fichiers concernés** : `ia-pep-2/seance-01/index.html`
**Ce qu’on produit** : page S01 entièrement réécrite selon la structure imposée.
**Comment on sait que c’est bon** : suppression des sections enseignant, présence de prompts copiables, instructions concrètes, structure exacte.
**Après quoi** : étape 3.

### Étape 5 — Valider S01 puis figer la règle de rédaction pour les autres séances
**Objectif** : vérifier que le modèle S01 est conforme et qu’il peut être répliqué sans déviation.
**Fichiers concernés** : `ia-pep-2/seance-01/index.html`
**Ce qu’on produit** : checklist de validation de séance.
**Comment on sait que c’est bon** : tout est conforme à la structure demandée, sans jargon académique, sans formateur.
**Après quoi** : étape 4.

### Étape 6 — Refaire S02 selon le même modèle
**Objectif** : appliquer la structure cible à la séance suivante, en gardant l’angle pratique.
**Fichiers concernés** : `ia-pep-2/seance-02/index.html`
**Ce qu’on produit** : page S02 refondue.
**Comment on sait que c’est bon** : prompts, résultats, bloc d’erreurs, points à retenir, sans sections pédagogiques inutiles.
**Après quoi** : étape 5.

### Étape 7 — Refaire S03 à S05, une par une, en suivant la même logique
**Objectif** : poursuivre la refonte en gardant le même standard de qualité.
**Fichiers concernés** : `ia-pep-2/seance-03/index.html`, `ia-pep-2/seance-04/index.html`, `ia-pep-2/seance-05/index.html`
**Ce qu’on produit** : 3 séances refondues et validées individuellement.
**Comment on sait que c’est bon** : même structure, même ton, même niveau de praticité.
**Après quoi** : étape 6.

### Étape 8 — Refaire S06 à S08, une par une, puis validation
**Objectif** : compléter la seconde moitié du module avec le même modèle de page étudiant.
**Fichiers concernés** : `ia-pep-2/seance-06/index.html`, `ia-pep-2/seance-07/index.html`, `ia-pep-2/seance-08/index.html`
**Ce qu’on produit** : 3 séances refondues.
**Comment on sait que c’est bon** : action concrète, prompts exacts, outils réels, exemples exploitables.
**Après quoi** : étape 7.

### Étape 9 — Refaire S09 et S10, conclure le module
**Objectif** : finaliser le module et compléter la logique de fin de parcours : organisation, esprit critique, usage responsable.
**Fichiers concernés** : `ia-pep-2/seance-09/index.html`, `ia-pep-2/seance-10/index.html`
**Ce qu’on produit** : S09 et S10 réécrites selon le modèle validé.
**Comment on sait que c’est bon** : cohérence globale, progression pédagogique, fin de module claire.
**Après quoi** : étape 8.

### Étape 10 — Créer les pages annexes pratiques
**Objectif** : compléter le module avec les pages annexes qui manquent et qui servent réellement l’étudiant.
**Fichiers concernés** : `ia-pep-2/outils-ia.html`, `ia-pep-2/construire-ia.html`, `ia-pep-2/premier-contact.html`, `ia-pep-2/piloter-opencode.html`
**Ce qu’on produit** : pages annexes réécrites en mode pratique et étudiant.
**Comment on sait que c’est bon** : elles répondent bien au besoin concret, sans balivernes pédagogiques.
**Après quoi** : étape 9.

### Étape 11 — Mettre à jour l’index du module IA
**Objectif** : harmoniser la page d’accueil du module avec le nouveau message pédagogique.
**Fichiers concernés** : `ia-pep-2/index.html`
**Ce qu’on produit** : page d’accueil cohérente avec la nouvelle pédagogie.
**Comment on sait que c’est bon** : le module apparaît comme un guide pratique, pas comme un plan de cours.
**Après quoi** : étape 10.

### Étape 12 — Mettre à jour les sources Markdown
**Objectif** : aligner les documents sources FR/EN/AR, fiches synthèse et slides avec la nouvelle pédagogie.
**Fichiers concernés** : `ia-pep-2/seance-01/cours-fr.md`, `cours-en.md`, `cours-ar.md`, `fiche-synthese.md`, `slides.md`, `dialogues-fr.md`, `dialogues-en.md` et les autres séances
**Ce qu’on produit** : fichiers markdown cohérents avec la refonte.
**Comment on sait que c’est bon** : même angle pédagogique, même logique pratique, même structure.
**Après quoi** : étape 11.

### Étape 13 — Régénérer les PPTX et vérifier la cohérence globale
**Objectif** : remettre les supports de cours en cohérence avec la nouvelle version pédagogique.
**Fichiers concernés** : `ia-pep-2/generate_pptx.py` et les fichiers `presentation.pptx`
**Ce qu’on produit** : supports PowerPoint générés de nouveau.
**Comment on sait que c’est bon** : aucun fichier visuellement incohérent ou désaligné avec les pages HTML.
**Après quoi** : étape 12.

### Étape 14 — Vérification finale du site
**Objectif** : contrôler le module entier avant validation finale.
**Fichiers concernés** : module IA complet
**Ce qu’on produit** : contrôle des liens, langues, responsive, navigation, CSS, ressources.
**Comment on sait que c’est bon** : pas de liens cassés, pas de section enseignant restante, pas de contenu inutile, trilingue OK, design inchangé.
**Après quoi** : étape 13.

### 9. Contraintes globales

- Design identique au format TIC.
- Sélecteur flottant FR/EN/AR visible sur toutes les pages.
- Trilingue obligatoire (FR/EN/AR).
- Commit Git après chaque étape validée.
- Ne pas toucher aux autres modules.
- Ne pas générer plusieurs séances d’un coup.
- Une seule séance à la fois, validation après chaque étape.
- Si blocage : arrêter, diagnostiquer, puis signaler précisément le point bloquant.
- Conserver les éléments du site déjà solides : header, footer, breadcrumb, navigation, styles.

### 10. Journal de progression (à remplir au fur et à mesure)

| Étape | Statut | Date | Commit Git | Remarques |
|---|---|---|---|---|
| 1 | ⬜ | | | |
| 2 | ⬜ | | | |
| 3 | ⬜ | | | |
| 4 | ⬜ | | | |
| 5 | ⬜ | | | |
| 6 | ⬜ | | | |
| 7 | ⬜ | | | |
| 8 | ⬜ | | | |
| 9 | ⬜ | | | |
| 10 | ⬜ | | | |
| 11 | ⬜ | | | |
| 12 | ⬜ | | | |
| 13 | ⬜ | | | |
| 14 | ⬜ | | | |

### 11. Exemple canonique complet de S01

# Séance 01 — Comprendre l'IA et lui parler pour la première fois

## En une phrase
À la fin de cette séance, tu sauras ouvrir ChatGPT, lui poser une question utile et juger sa réponse.

## Pourquoi c'est utile pour toi
L'IA va te servir tous les jours à l'université : comprendre un cours difficile, préparer un exposé, réviser un examen. Mais si tu lui parles mal, elle te donne des réponses inutiles. Cette séance t'apprend à bien lui parler dès le départ.

## Les 3 idées essentielles
- L'IA ne « cherche » pas une réponse : elle prédit le mot suivant, mot après mot.
- Elle peut être très convaincante et se tromper complètement : c'est une hallucination.
- La qualité de sa réponse dépend de la qualité de ta question.

## Comment faire — pas à pas

### Étape 1 : Ouvre ChatGPT
- **Où** : chatgpt.com
- **Quoi taper** :
<pre><code>Crée un compte gratuit puis ouvre un nouveau chat.</code></pre>
- **Ce que tu vas voir** : une grande zone vide où tu peux écrire.
- **Astuce** : si ChatGPT ne marche pas, ouvre Gemini ou Perplexity.

### Étape 2 : Pose ta première question
- **Où** : dans le même chat
- **Quoi taper** :
<pre><code>Explique-moi ce qu'est l'intelligence artificielle comme si j'avais 12 ans, en 3 phrases.</code></pre>
- **Ce que tu vas voir** : une réponse courte et simple.
- **Astuce** : ajoute toujours « en 3 phrases », « en 5 points » ou « en 1 paragraphe ».

### Étape 3 : Pose une deuxième question
- **Où** : dans le même chat
- **Quoi taper** :
<pre><code>Donne-moi 3 exemples d'IA que j'utilise sans le savoir dans ma vie quotidienne.</code></pre>
- **Ce que tu vas voir** : des exemples que tu utilises tous les jours.
- **Astuce** : note les exemples qui te surprennent. C'est souvent là que tu comprends le mieux.

### Étape 4 : Vérifie si l'IA invente
- **Où** : dans le même chat
- **Quoi taper** :
<pre><code>Donne-moi les sources de tes informations.</code></pre>
- **Ce que tu vas voir** : soit des liens, soit rien.
- **Astuce** : si rien n'est sourcé, tu viens de voir une hallucination.

## Exemples réels

### Exemple 1 : Résumer un cours difficile
- **Ce que tu tapes** :
<pre><code>Résume ce paragraphe en 5 points clés pour un étudiant de 2e année : [colle ton paragraphe]</code></pre>
- **Ce que l'IA répond** : une liste courte, utile et claire.
- **Astuce** : ajoute « comme si tu expliques à un débutant ».

### Exemple 2 : Comprendre un mot inconnu
- **Ce que tu tapes** :
<pre><code>Explique-moi le mot "scaffolding" en pédagogie, avec un exemple concret de classe.</code></pre>
- **Ce que l'IA répond** : définition + exemple + explication simple.
- **Astuce** : ajoute « reformule plus simplement » si tu n'as pas compris.

### Exemple 3 : Corriger ton texte
- **Ce que tu tapes** :
<pre><code>Corrige les fautes dans ce texte et explique chaque correction : [ton texte]</code></pre>
- **Ce que l'IA répond** : texte corrigé + explication des corrections.
- **Astuce** : demande toujours « explique chaque correction ».

## Les astuces que personne ne dit
- Sois précis : sujet + format + public.
- Donne toujours un rôle à l'IA : « tu es un professeur ».
- Demande une réponse courte si tu veux une réponse claire.
- Vérifie les faits importants.
- Reformule la question si la réponse est confuse.
- Garde le même chat pour garder le contexte.
- Découpe ta demande en petites parties.

## Erreurs à éviter
- ❌ « Explique-moi tout sur l'IA » → ✅ « Explique-moi l'IA en 5 phrases pour un étudiant de 2e année »
- ❌ Croire l'IA sans vérifier → ✅ Vérifie les faits importants avant de les utiliser
- ❌ Demander sans réfléchir → ✅ Devine la réponse puis compare avec l'IA

## À retenir
- L'IA prédit le mot suivant, mot après mot.
- La qualité de la réponse dépend de la qualité du prompt.
- Une réponse peut être jolie et fausse.
- Tu dois vérifier les faits importants.
- Le bon usage vient de ta réflexion, pas de l'IA.

## Vidéos
Garder tel quel.

## Quiz
Garder tel quel.

## Glossaire
Garder tel quel.

## Ressources téléchargeables
Garder tel quel.

## Navigation
Garder tel quel.

### 12. Règles de voix (style d'écriture)

- Toujours écrire à la 2e personne du singulier : tu.
- Jamais « l'étudiant », « le formateur », « vous ».
- Phrases courtes, maximum 20 mots.
- Zéro jargon pédagogique : pas de « objectifs », « prérequis », « déroulé ».
- Chaque phrase doit dire quoi faire ou quoi regarder.
- Si une phrase ne dit ni action ni observation, elle est supprimée.
- Chaque section doit aider l’étudiant à agir, pas à écouter.

Ce plan doit servir de base canonique pour la refonte. Il est conçu pour être clair, concret et directement exploitable par un assistant externe qui doit comprendre le vrai problème et la vraie solution.
