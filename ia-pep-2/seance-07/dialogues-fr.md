# Séance 07 — Dialogues pédagogiques (Français)

## Dialogue A — « Mon programme ne marche pas… et c'est une bonne nouvelle » (25 min)

**Personnages :** Anis (étudiant bloqué), Lina (camarade débogueuse), M. Karim (enseignant).

---

Anis : Mon script affiche une erreur rouge de 10 lignes. Je suis nul en Python.

Lina : Montre la DERNIÈRE ligne. Que dit-elle ?

Anis : « IndentationError: unexpected indent, line 7 ».

Lina : Parfait, on a l'adresse (ligne 7) et le diagnostic (indentation inattendue). Demande à l'IA le POURQUOI, pas la correction.

Anis (à l'IA) : Pourquoi « unexpected indent » ligne 7 dans mon code [colle] ?

IA : Parce que la ligne 7 est décalée sans qu'une ligne finissant par « : » la précède. Python attend un bloc après « : ».

M. Karim : Tu vois ? L'erreur parlait. Maintenant corrige TOI-MÊME, puis demande un mini-exercice similaire.

Anis : Corrigé… et l'exercice similaire réussi ! Le bug était un professeur déguisé.

---

## Dialogue B — « Ma première IA à moi » (15 min)

**Personnages :** Sara (étudiante), son frère Yacine, l'écran (joué par un camarade).

---

Sara : Regarde, Yacine : je tape une question, et C'EST MON programme qui répond !

Yacine : Attends… c'est toi qui as programmé ChatGPT ?!

Sara : Non ! Mon script envoie ma question au guichet Gemini avec ma clé, et affiche la réponse. Quinze lignes seulement.

Écran : Toi > Explique-moi la photosynthèse en 3 points. / IA > 1)… 2)… 3)…

Yacine : Et si je veux qu'il se souvienne de ce qu'on a dit ?

Sara : J'ajoute une liste « historique » : à chaque appel, je renvoie les 6 derniers échanges. Essaie : demande-lui « et en arabe ? ».

Yacine : Il a compris ! Sans que je répète la question… C'est ça, la mémoire ?

Sara : Exactement : le modèle oublie tout, c'est MON script qui lui rappelle. Je suis devenue constructrice d'IA !

---

## Mini-rôle à jouer (3 min par binôme)
L'un colle un code avec une erreur classique, l'autre formule le prompt de diagnostic (« pourquoi », pas « corrige »). Échangez, puis votez pour le meilleur diagnostic de la classe.
