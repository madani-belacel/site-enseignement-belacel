# Message à envoyer à Grok (ou autre IA génératrice de PPTX)

---

Crée une présentation PowerPoint professionnelle en **30 diapositives**, format 16:9,
destinée à un cours d'introduction à l'Intelligence Artificielle.

## 1. Contexte de la formation

- **Public** : étudiants de 2ᵉ année PEP (Parcours Enseignement Primaire), Faculté des
  Sciences de l'Éducation, Université de Mostaganem, Algérie.
- **Niveau en informatique** : ils ont étudié la **didactique de l'anglais langue
  étrangère (FLE)**. Ce ne sont pas des informaticiens. Leurs réflexes sont
  **pédagogiques et pratiques** : ils veulent du concret, un résultat immédiat,
  et une méthode qu'ils peuvent reproduire le lendemain.
- **Durée du cours** : 90 minutes.
- **Professeur** : Dr. Madani Belacel.
- **Langue** : français. Vocabulaire simple, phrases courtes, aucun jargon non expliqué.

## 2. Objectif pédagogique central

L'étudiant doit répondre à trois questions avant la fin du cours :

1. **Où est-ce que j'utilise déjà de l'IA sans le savoir ?** (dans son téléphone, sa
   tablette, son navigateur, ses réseaux sociaux, sa banque, l'université)
2. **Comment ça marche vraiment ?** (données → motif → prédiction → décision)
3. **Qu'est-ce que je peux en faire dès demain, concrètement ?**

## 3. Principe de construction — IMPORTANT

**Commencer par les exemples, jamais par la théorie.**

Interdiction formelle de commencer par « l'IA est une discipline qui… » ou par une
définition académique. La diapositive 1 doit être un **problème concret** tiré de la
vie réelle de l'étudiant.

Méthode à appliquer : **un exemple d'abord, le concept ensuite.**

| Bloc | On commence par | On explique le concept après |
|---|---|---|
| Fonctionnement | « Mon téléphoneريrecommande une vidéo, pourquoi ? » | données → motif → prédiction |
| Outils | « Voici 6 problèmes que j'ai réellement ce soir » | familles d'outils |
| Agents | « Faire réparer un téléphone avec une IA » | boucle agent / plan / exécution |
| Limites | « L'IA a inventé une référence qui n'existe pas » | hallucination, vérification |

Chaque concept abstrait doit toujours être **ancré par un exemple vécu** immédiatement
avant ou immédiatement après.

## 4. Plan demandé — 30 diapositives

### Ouverture (1-4)

1. **Diapositive d'accroche** — titre : « L'IA est déjà dans ta poche ». Image centrale :
   un étudiant, son téléphone, 6 applications. Aucun texte. Une seule question :
   « Combien de fois aujourd'hui l'IA a décidé quelque chose pour toi ? »
2. **Le défi** — « Ce soir, 6 problèmes. Tu en résous 5 en 20 minutes ? » Lister les 6 :
   téléphone qui ne charge plus · Motorcycle qui cale · Devoir à rendre demain · Site web
   pour le club · Photo floue à restaurer · Fichier Word perdu.
3. **Objectif du cours** — les 3 questions du point 2, en clair.
4. **Le programme** — 5 parties, 5 icônes.

### Partie 1 — Où l'IA est déjà là (5-9)

5. **Dans le téléphone** — schéma du téléphone avec les zones IA surlignées :
   déblocage facial, correction photo, prédiction de mots, GPS, correction d'écriture,
   recommendation de contenu. Chiffres à jour et sourcés.
6. **Sur le web et les réseaux sociaux** — fil d mathematicien, feed Facebook/TikTok,
   traduction automatique, vérification d'e-mail.
7. **Dans l'université et l'administration** — inscription, notes, plagiarism
   (détection), archives, coût, transport, úgyem, Dzirie.
8. **Chez le technicien : réparation et flashage** — diagnostic de panne, schémas de
   câblage,uesto du micrologiciel, datasheets de composants,multimètre и IA.
9. **Partie 1 — synthèse** : une seule diapositive, 12 logos d'outils du quotidien.

### Partie 2 — Comment ça marche vraiment (10-15)

10. **L'idée centrale en une phrase** — « Une machine qui a vu beaucoup de cas
    identiques et qui devine le suivant. »
11. **Le schéma central** — **schéma obligatoire** : 4 blocs
    `DONNÉES → MOTIF → PRÉDICTION → DÉCISION`, avec sous chaque bloc 2 exemples
    concrets issus du téléphone (diapo 5).
12. **Exemple chiffré** — tableau : 5 exemples concrets, colonnes
    « Données vues » / « Motif appris » / « Prédiction faite ».
13. **Pourquoi l'IA se trompe** — schéma : une donnée fausse ou un cas rare → mauvaise
    prédiction. Exemple : photos de chats roux uniquement → l'IA ne reconnaît pas un chat
    noir. →transition vers « l'humain doit vérifier ».
14. **Ce que l'IA ne fait pas** — pas de compréhension, pas de conscience, pas de
    garage : elle calcule des probabilités. 4 cases avec icônes.
15. **Partie 2 — synthèse** : le schéma central en plus grand, seul à l'écran.

### Partie 3 — Les 6 familles d'outils (16-20)

Grille 6 cases, une par famille, avec pour chacune : à quoi ça sert / exemple étudiant /
outil Leader / ce que ça ne fait pas.

16. **Grille des 6 familles**
17. **Zoom sur les agents** — **schéma obligatoire** de la boucle agent :
    `DEMANDE → PLAN → OUTILS → ÉCRITURE → VÉRIFICATION` avec les deux agents en
    exemple : **Cursor** (dans l'éditeur) et **OpenCode** (en ligne de commande).
    Message clé : « l'agent ne répond pas, il agit ».
18. **Comparaison claire** — tableau `ChatGPT / Claude / Gemini / Cursor / OpenCode /
    DeepSeek` × `ce qu'il fait / où il travaille / pour qui`.
19. **Les 5 modèles de raisonnement** — Chaîne de pensée, arbre de thoughts,
    Croiser plusieurs modèles, Décomposition de la tâche, Agent.
20. **Partie 3 — synthèse**.

### Partie 4 — Les cas concrets (21-26)

21. **Cas 1 — Réparer et flasher un appareil** — tableau de 5 lignes :
    besProblem → question à poser à l'IA → gain de temps réel. Inclure
    vérification de schéma, datasheet de composant, erreur de micrologiciel.
22. **Cas 2 — Créer un site web en 20 minutes** — 4 étapes, avec le schéma du
    projet (HTML/CSS/JS/base de données) et le rôle de l'IA à chaque étape.
23. **Cas 3 — Réviser un examen** — méthode Feynman, cartes mémoire Anki, QCM
    auto-générés.
24. **Cas 4 — Rédiger, corriger, traduire** — les 3 langues de l'étudiant
    (FR / EN / AR), avec les limites à connaître pour l'arabe.
25. **Cas 5 — Ce que l'étudiant peut utiliser dès demain** — 10 actions concrètes,
    numérotées, classées par temps gagné.
26. **Les vraies astuces du terrain** — **tableau obligatoire** : 7 lignes, colonnes
    « Problème réel » / « Solution qui marche » :
    - Quota atteint → regrouper 5 questions en 1 message
    - Quota atteint → changer d'outil (ChatGPT, Gemini, Claude, DeepSeek)
    - Version gratuite bloquée → l'application mobile
    - Serveur lent aux heures de pointe → travailler aux heures creuses
    - Offre étudiante gratuite → chercher l'offre officielle de son université
    - Outil qui coupe → sauvegarder le résultat avant de perdre la session
    - Réponse trop générique → la formule magique : Rôle + Contexte + Tâche + Format + Contraintes

### Partie 5 — Les limites et les règles (27-29)

27. **Les 4 pièges** — hallucination · vie privée · plagiat et honnêteté
    académique · dépendance. Un exemple réel par piège.
28. **La charte en 7 lignes** — à photographier et à retenir. Thèse courte :
    « L'IA propose, l'humain décide, l'étudiant assume. »
29. **Les 5 gestes à retenir** — récapitulatif visuel, une phrase par geste.

### Clôture (30)

30. **Défi de la semaine + Questions** — 3 actions à faire avant le prochain cours,
    puis « Questions » en grand.

## 5. Exigences de conception

- **30 diapositives exactement.** Le plan ci-dessus fait 30 ; s'il faut couper,
   fusionner uniquement les diapositives 9, 15 et 20 (les synthèses).
- **16:9**, fond **blanc**, texte **sombre**. Une seule couleur d'accent
  (bleu petroleum) + une couleur d'alerte (rouge sombre). Pas de dégradés.
- **Zéro mur de texte.** Maximum 6 lignes par diapositive, 12 mots par ligne.
- **1 idée par diapositive.** Le titre annonce l'idée, il ne la répète pas.
- **Schémas obligatoires** (vectoriels, pas des images de Google) : diapos 5, 8, 11, 15,
  17, 22. Utilise des formes et des flèches.
- **1 chiffre par diapositive maximum**, et toujours avec sa source.
- **Icônes** : emojis ou formes simples, cohérents.
- **Numérotation** des diapositives en bas à droite.
- **Notes du présentateur OBLIGATOIRES sur les 30 diapositives.** Voir point 6.
- **Police** : une seule famille, taille 28 minimum pour le corps.

## 6. Notes du présentateur — format imposé

Pour **chaque** diapositive, les notes doivent contenir **exactement** ces trois
sections, séparées, dans cet ordre :

```
🎯 OBJECTIF
(une phrase : ce que l'étudiant doit retenir de cette diapositive)

🗣️ CE QUE JE DIS
(le discours à dire, 80 à 120 mots, à dire à l'oral, ton naturel)

❓ Q/R ATTENDUES
(question probable d'un étudiant → réponse courte, 2 à 4 phrases)
(question probable d'un étudiant → réponse courte)
(2 à 3 questions par diapositive)

⚠️ PIÈGE À ÉVITER
(ce qu'un étudiant va mal comprendre, ou la faute classique)
```

Rédige les notes **en français**, avec le même niveau de langue que le cours :
des phrases qu'on peut lire à voix haute sans les réécrire.

## 7. Contraintes de fond — à respecter strictement

- **Aucun exemple hors de la vie réelle d'un étudiant algérien de 20 ans.**
  Pas de.startup de San Francisco, pas de trader, pas de cas d'entreprise.
- **Le contexte FLE doit être respecté** : ils ont appris à enseigner l'anglais,
  donc certains seront eux-mêmes enseignants. Prévois **une diapositive ou
  un passage** qui leur montre comment utiliser l'IA pour préparer un cours, une
  fiche de FLE, une activité de classe.
- **Les 6 problèmes de la diapositive 2 doivent être résolus** au moins une fois
  chacun dans le cours. C'est le fil rouge.
- **Ne présente jamais l'IA comme une autorité.** Présente-la comme un
  collaborateur rapide mais faillible.
- **Ne pas donner de conseil sur la création de comptes multiples, ni sur le contournement
  des quotas par des scripts.** Les solutions présentées sont : regrouper,
  changer d'outil, application mobile, heures creuses, offres étudiantes
  officielles. C'est volontaire.
- **Langage** : français simple. Chaque terme technique est expliqué en une ligne
  à sa première occurrence.

## 8. Livraison attendue

- Un fichier **.pptx** téléchargeable.
- Les 30 diapositives, notes comprises.
- Vérifie avant de livrer : **aucune diapositive vide**, **aucune diapositive
  qui déborde**, **aucun texte coupé**.
- Signale-moi à la fin : le nombre de diapositives livrées, le nombre de schémas,
  le nombre de diapositives portant des notes.