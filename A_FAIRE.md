# A faire — site-enseignement-belacel

Suivi des tâches ouvertes. Mis à jour au fil des travaux.
Dernière mise à jour : 2026-09-30

---

## En cours

_(rien — les trois demandes sont traitées, voir « Terminé ».)_

---

## Terminé — audit, présentations, cours

### Module IA fusionné et corrigé

Deux versions du module coexistaient. La fusion a gardé le meilleur de chacune.

| On a gardé | De qui | Pourquoi |
|---|---|---|
| 5 cours Q/R, 5 PPTX, notes PDF | les deux | fichiers **identiques** au bit près |
| 74 831 mots dans les 15 séances | version détaillée | 3,7 fois plus riche |
| 12 sections par séance (checklist, gestes, quiz, glossaire) | version 150 | absentes de la version détaillée |
| Séance 01 enrichie (12 prompts, 5 étapes, 5 gestes) | version 150 | plus riche que la nôtre |
| « ✅ À retenir » de la séance 01 | version détaillée | **absente** de la version 150 |
| Les 152 astuces + 25 catégories | version 150 | au lieu de 42 |

Le script `scripts/fusionner_modules_ia.py` refait l'opération ; il est
idempotent. `scripts/remplacer_seance_01.py` remet la séance 01 en place sans
perdre « À retenir » — un simple `cp` l'aurait perdu.

**152 explications détaillées**, une par astuce, dans un bouton dépliant :

| Version | Astuces | Longueur |
|---|---|---|
| Longue (rédigée à la main) | 1, 2, 3, 4 | 700 à 1 250 mots |
| Courte (format de travail) | 5 à 152 | 126 mots en moyenne |

Le bouton est un `<details>/<summary>` natif : **aucun JavaScript** à charger,
fonctionnel au clavier, lisible par les lecteurs d'écran, et il survit à une
panne de `main.v2.js`.

- Contenu : `scripts/astuces_detail_lot_1.py` … `lot_8.py` (+ `astuces_detail.py`)
- Pose des boutons : `scripts/ajouter_boutons_astuces.py` (remplace un bloc
  existant si l'explication évolue, ne duplique jamais)
- **Avertissement en tête de page** — « l'IA peut transformer un article vrai
  en article faux » — ancre `#avertissement-article`, avant les 152 astuces.
  Script : `scripts/ajouter_avertissement_ia.py`

### Audit approfondi du module IA — `scripts/audit_approfondi_ia.py`

Huit dimensions que `audit_liens.py` et `audit_complet.py` ne regardent pas :
renvois entre astuces, lisibilité, cohérence du vocabulaire, accessibilité,
pédagogie des séances, références internes, poids, métadonnées.

**Résultat : 4 défauts réels corrigés.**

| Défaut | Correction |
|---|---|
| `Curseur` au lieu de `Cursor` (séance 10) | corrigé — « curseur » est le mot français pour le pointeur de souris |
| `Groq` cité à côté de `Grok` | précision ajoutée — ce sont **deux sociétés différentes** |
| 31 étapes sans durée dans le titre | **77/77** étapes portent leur durée |
| description de la séance 01 à 168 car. | ramenée à 139 (Google tronquait) |

Script de correction : `scripts/corriger_audit_ia.py` (idempotent).

**L'audit lui-même a produit 4 faux positifs**, tous corrigés — c'était la
moitié du travail, l'outil mentait :

| Bug | Faux signal |
|---|---|
| `phrases()` aplatissait les séparateurs de blocs | 153 « phrases » de 100 mots |
| menu et pied de page comptés comme prose | idem |
| le regex des tableaux ne vérifiait pas le corps | **74** tableaux « sans `<th>` » |
| `re.I` sur le motif `SE` | « analy**se** 50 documents » → renvoi mort imaginaire |

Chacun est vérifié : injecter une vraie faute (une référence à la séance 42,
inexistante) est toujours détecté, puis retiré.

**Bilan final** : 0 phrase de plus de 55 mots · 0 défaut d'accessibilité ·
15/15 séances complètes sur 7 critères · métadonnées conformes · 0 renvoi
mort · 0 lien mort · HTML valide sur 23 pages · 253 Ko brut, **67 Ko compressé**.

### Deux bugs corrigés dans les outils existants

- **`audit_liens.py`** déclarait **46 liens morts** sur le module. Il ne lisait
  pas les pages situées hors du dossier audité : un lien vers
  `../../index.html#about` était signalé mort alors que l'ancre existe.
  Vérifié en injectant une ancre factice, toujours détectée.
  → Site entier : **2 906 pages, 64 789 liens, 0 lien mort.**
- **`lister_ancres_mortes.py`** (nouveau) ne résolvait que les ancres internes.
  Corrigé pour lire la cible sur place.

### Audit complet du site — `scripts/audit_complet.py`

Audit **rejouable** : liens, ancres, accessibilité, SEO, performance et
qualité du contenu, sur 2 883 pages. Résultat : **1 660 anomalies**, dont
l'essentiel est sans gravité.

| Anomalie | Nb | Gravité | État |
|---|---|---|---|
| page orpheline (aucun lien entrant) | 96 | important | à traiter |
| marqueur de travail `TODO` (dans un commentaire) | 9 | important | à traiter |
| page racine non liée (`404.html`, volontaire) | 1 | — | sans objet |
| `title` trop long (> 65 car.) | 15 | mineur | à traiter |
| page quasi vide (< 400 car.) | 3 | mineur | à traiter |
| champ de formulaire sans étiquette | 1 | mineur | à traiter |
| guillemets droits dans du français | 89 | mineur | style voulu |
| pas de lien d'évitement | 1 428 | mineur | voir plus bas |
| espace avant `.` ou `,` | 10 | mineur | exercices à trous, pas une faute |
| point sans espace après | 7 | mineur | réel |
| élision détachée | 1 | mineur | faux positif (anglais) |

**Zéro** sur tous ces points, et c'est le vrai résultat : lien mort,
ressource manquante, image sans `alt`, page sans `<h1>`, `title` dupliqué,
page sans `lang`, sans `canonical`, sans `viewport`, sans meta description,
`target=_blank` sans `noopener`, balise obsolète, `id` dupliqué, page trop
lourde, image trop lourde.

**Corrections apportées**
- `tmp_sign.txt` supprimé (fragment Python oublié à la racine).
- **Lien d'évitement sur 2 806 pages** : `placeSkipLink()` dans
  `js/main.v2.js` l'injecte là où il manquait (77 pages l'avaient en dur).
  L'id `main-content` est posé sur `<main>` s'il manque. Vérifié :
  `skip-link -> #main-content`, cible créée, masqué jusqu'au focus.

**L'audit a dû être corrigé trois fois avant d'être fiable** — c'est le
point important de ce chantier :
1. il cherchait `href=` dans tout le document et signalait 7 fausses
   ressources : un cours qui *enseigne* le HTML contient
   `<code>&lt;link href="style.css"&gt;</code>`, qui est du texte à lire ;
2. il signalait 4 500 « fautes » de typographie inexistantes — « de le
   traverser » et « à les transformer » sont du français correct,
   `localStorage` est du camelCase, l'espace avant `:` est la règle
   française, `students' work` est un possessif anglais ;
3. il signalait 368 « espaces avant le point » **créés par lui-même** : en
   remplaçant chaque balise par une espace, `professionnelle</strong>.`
   devenait « professionnelle . ». Le contrôle se fait désormais sur les
   segments de texte, pas sur la page aplatie.

Le rapport **réconcilie** son total : un compteur non classé est affiché
plutôt que caché. Limites assumées et documentées (mot répété, contraste,
ordre des attributs HTML).

### Présentations : les 5 cours IA + le cours 01 TIC

| Fichier | Diapos | Contenu |
|---|---|---|
| `Module IA/…/QR_IA_01_Introduction_IA.pptx` | 11 | 32 Q/R, 14 schémas |
| `Module IA/…/QR_IA_02_Comment_Fonctionne_IA.pptx` | 12 | 30 Q/R |
| `Module IA/…/QR_IA_03_Exemples_Simples_IA.pptx` | 12 | 30 Q/R |
| `Module IA/…/QR_IA_04_Realiser_IA.pptx` | 12 | 30 Q/R |
| `Module IA/…/QR_IA_05_Premier_Projet_IA.pptx` | 12 | 30 Q/R |
| `Module TIC/…/Cours_TIC_01_Introduction_aux_TIC_FR_pptx.pptx` | 30 | 9 sections + QCM |

+ un PDF de notes imprimables pour chacun (`scripts/notes_en_pdf.py`).

Générateurs : `make_pptx_ia.py` (IA, 5 cours), `make_pptx_tic01.py` (TIC),
`make_pptx_ia01.py` (deck IA 01, schémas simplifiés). Tous relisent le
cours HTML : la présentation ne peut pas diverger de la page.

**Les cours 02 à 05 n'ont aucun schéma** dans leur HTML. Plutôt que de
livrer des diapos à moitié vides, la diapo affiche l'explication agrandie
(jusqu'à 26 pt au lieu de 19) et les **questions de la séance** ; les
réponses restent dans les notes. Rien n'est inventé.

Contrôle automatique `scripts/verifier_pptx.py` : **0 problème** sur les
6 présentations (77 diapos au total).

Liens ajoutés : bouton « 📊 Présentation (PPTX) » dans la barre des 5
cours IA, cartes PPTX + lien vers les notes sur l'index du module.

---

## À faire

### 1. 1 428 pages sans lien d'évitement
Ces pages (dont tout `ia-pep-2/` et `ia-pep-2-archive/`) ne chargent
**ni** `js/main.v2.js` **ni** `css/style.css` : elles sont autonomes.
L'injection JavaScript ne peut pas les atteindre, et y ajouter le lien à la
main afficherait du texte non stylé en haut de la page, puisque le CSS
`.skip-link` n'y existe pas. Il faudrait leur faire charger la feuille de
style du site, ou leur donner un style local. **Décision à prendre.**

### 2. 96 pages orphelines
`série_Officielle/ING-S5|S7|S9/index.html` et quelques autres : publiées
mais non liées depuis leur section. À relier ou à retirer.

### 3. 9 marqueurs `TODO`
Dans `ia-pep-2-archive/seance-03/05/07/08/10/index.html` :
`<!-- TODO: remplacer par lien définitif -->`. Invisibles pour le lecteur,
mais le lien de remplacement manque.

### 4. 7 points sans espace après
Réels, dans 3 pages : « obsolète,ThickNet », « micrologiciel,shareware ».
Correction triviale si vous la voulez.

### 5. Bascule de langue sur les pages de module
`tic.html` et la page du module IA n'ont **aucun** sélecteur de langue, alors
que les cours Q/R en ont un (`.qr-tabs` + `.lang-en`/`.lang-fr` + JS inline).
Question en attente : traduire toute la page, ou seulement les titres et
libellés ? (réponse non encore donnée)

### 6. Menu de l'en-tête : deux liens de trop sur les pages IA
Sur les pages du module Intelligence Artificielle, la barre de navigation
contient **deux entrées de plus** que sur `tic.html` : « Ressources » (107 px)
et « Contact » (85 px). Le menu mesure donc 1 022 px alors qu'il n'y a que
805 px de place dans `.header-inner` (1 210 px moins le logo et la faculté) :
il déborde de 182 px, `body` est en `overflow-x:hidden`, donc « Ressources »,
« Contact » et le bouton clair/sombre **sortent de l'écran**. Un bouton `<`
apparaît pour faire défiler le menu, mais le bouton thème reste hors champ.
Pistes : aligner la navigation IA sur celle de `tic.html` (7 entrées), ou
réduire `.nav-list a` (padding / font-size) sous 1 300 px.
Vérifié : ce défaut est **antérieur** à mes travaux (`git diff` = 0 ligne
touchant `nav-list` sur ces pages).

### 7. En-tête : le nom chevauche le menu
Sur les 2 883 pages, `.header-logo-text` (« Dr. BELACEL Madani / MCB —
Université de Mostaganem ») **recouvre** le lien « À propos » de la barre de
navigation. Visible sur toutes les pages, y compris `tic.html`. Correctif
possible : réduire la taille du nom sur `.header-inner`, ou passer la barre de
navigation sous le logo au-dessus de 1 100 px.

---

## Journal des travaux

- [x] **Présentation du cours 01 refaite : 11 diapositives, Q/R dans les notes**
      `cours/Module Intelligence Artificielle/make_pptx_ia01.py` →
      `Presentations_PPTX/QR_IA_01_Introduction_IA.pptx` (73,6 Ko)
      - 1 couverture + 10 idées, une idée par diapositive, 16:9.
      - **Les Q/R sont dans les notes du présentateur** (32 paires FR + 32 EN),
        pas sur la diapositive : la diapo reste lisible de loin.
      - **Le script relit `QR_IA_01_Introduction_IA.html`** : titres,
        explications et Q/R viennent du cours, donc le PPTX ne peut plus
        diverger du HTML. Seuls les schémas sont dessinés dans le script.
        (La version initiale recopiait les textes en dur : elle était en
        retard sur le cours et perdait 11 éléments, dont la formulation Excel
        « 4 dans une cellule, 8 dans la suivante » et la phrase sur les
        chiens mal étiquetés.)
      - **Cadre et schémas dimensionnés sur le texte réel** : la hauteur du
        cadre suit le nombre de lignes, et la taille de police s'ajuste pour
        que rien ne déborde. Sur l'idée 3 — la plus longue du cours — le texte
        FR et EN se chevauchaient avec des hauteurs fixes.
      - Largeur moyenne d'un caractère calibrée sur le rendu réel
        (11 pt → 0,65 ; 38 pt → 0,42) au lieu d'une valeur unique.
      - Contrôle automatisé `/tmp/opencode/verifier_pptx.py` : aucune forme
        hors cadre, aucun chevauchement du pied de page, aucun texte trop
        grand. 11 diapositives, 0 problème.
      - Contrôle de cohérence `/tmp/opencode/comparer_pptx_html.py` :
        **0 écart** entre le PPTX et le cours HTML.
      - Ancienne version 14 diapositives (avec plan et « 6 points à retenir »,
        Q/R affichées sur les diapos) : `/tmp/opencode/avant_14_diapos.pptx`
- [x] **Présentation du cours 01 en français seul, couverture améliorée**
      Destinataire : **2ᵉ année PEP · ENS, filière Français** — la séance se
      donne en français, la présentation n'affiche donc plus d'anglais.
      - `LANGUES = ("fr",)` en tête de `make_pptx_ia01.py` : remettre
        `("fr", "en")` rebascule la version bilingue (titre EN, explication
        EN, Q/R EN dans les notes).
      - Sans l'anglais, le texte français passe de 13,5 pt à **17 pt** et le
        titre de 25 à 28 pt : plus lisible depuis le fond de la salle.
      - **Couverture refaite** : bandeau blanc en haut avec les deux logos —
        `Université_de_Mostaganem.png` et `LOGO-FLE-UNIV-Mosta.jpeg` — séparés
        par un filet, puis « Université de Mostaganem · Faculté des Langues
        Étrangères / 2ᵉ année PEP · Année universitaire 2026 – 2027 ».
        Le logo de la FLE est un JPEG **à fond blanc** : le bandeau blanc est
        ce qui évite un rectangle gris visible sur le fond marine.
      - python-pptx ne lit ni le `.webp` ni l'`.avif` du site : on prend le PNG
        de l'université et le JPEG de la faculté.
      - Logos allégés dans `logos_pptx/` (328 × 318 px pour 1,06 po, soit
        300 ppp) : le PNG d'origine fait 960 × 931 px et 255 Ko. Le `.pptx` est
        passé de 377 Ko à **144 Ko**, sans perte visible à la projection.
      - Ajout d'une accroche sous le titre et de l'adresse du cours en bas.
      - Contrôle automatisé : **0 problème** de mise en page sur 11 diapos.
- [x] **Textes des diapositives agrandis + notes imprimables**
      - **Réglages de lisibilité regroupés en tête de `make_pptx_ia01.py`** :
        `TAILLE_TITRE = 30`, `TAILLE_TEXTE_MAX = 19.0`, `TAILLE_PASTILLE = 12`,
        `TAILLE_BOITE = 15.5`, `TAILLE_BOITE_SUB = 12.0`. On les ajuste sans
        toucher au reste du script.
        | | avant | maintenant |
        |---|---|---|
        | Explication FR | 17 pt | **19 pt** |
        | Titre d'idée | 28 pt | **30 pt** |
        | Texte des schémas | 13 pt | **15,5 pt** |
        | Légende des schémas | 10,5 pt | **12 pt** |
        | Flèches | 19 pt | 21 pt |
        - La taille du texte des schémas **s'adapte à la largeur de la boîte** :
          six boîtes sur une rangée (idée 4) ne peuvent pas prendre 15,5 pt,
          le script y descend à 12,5 pt au lieu de tout rapetisser.
      - **Notes imprimables** : `generer_notes_imprimables.py` →
        `Presentations_PPTX/QR_IA_01_Introduction_IA_notes.pdf`
        (5 pages A4, 96 Ko, les 32 Q/R avec l'explication de chaque idée).
        Le même contenu reste dans les notes du .pptx ; ce PDF est la version
        à imprimer. Lien ajouté dans la barre du cours (« 📄 Notes (PDF) »)
        et sur la carte de l'index du module.
      - Contrôle : **0 problème** de mise en page, 0 lien mort, 0 ressource
        manquante sur les 2 883 pages.
- [x] **Présentation PowerPoint du cours 01 du module TIC** (30 diapositives)
      `cours/Module TIC/Série Officielle 01-10/Cours_TIC_01_Introduction_aux_TIC_FR_pptx.pptx`
      (193 Ko, 16:9) — générateur `make_pptx_tic01.py` dans le même dossier.
      **Le générateur relit `Cours_TIC_01_Introduction_aux_TIC_FR.html`** :
      titres, listes, tableaux, encadrés « À retenir » et QCM viennent du cours,
      donc la présentation ne peut pas diverger de la page. Le cours 01 du
      module IA suit le même principe — d'où le module partagé
      `scripts/pptx_commun.py` (palette, calibres, couverture, schémas).
      - Plan du cours avec la durée de chaque section (**100 min** au total),
        puis 1 à 4 diapositives par section selon sa densité, puis
        l'auto-évaluation (2 diapos de questions + 3 de corrigé, paginées).
      - Notes du présentateur sur les 30 diapositives (section, durée, consigne
        de correction du QCM).
      - **Lien ajouté dans la barre du cours** : « 📊 Présentation (PPTX) ».
      - Un ancien deck existait déjà (`Cours_TIC_01_Introduction_aux_TIC_FR.pptx`,
        21 diapos, **4:3**, lié depuis `tic.html`). Il n'a pas été supprimé ;
        voir « En attente de votre décision ».

      Défauts corrigés au passage (le contrôle automatique
      `scripts/verifier_pptx.py` les a fait apparaître un par un) :
        - QCM : 5 questions × 4 propositions débordaient jusqu'à 8,8 po sur une
          diapo de 7,5 → **paginé** ;
        - hauteurs de lignes de tableau sous-estimées (cas du texte sur 2 lignes)
          → le contenu suivant passait **sous** le tableau ;
        - titre de section sur 2 lignes qui percutait le tableau → hauteur
          mesurée avec une marge de sécurité ;
        - « À retenir — À retenir : … » (le cours écrit déjà le préfixe) ;
        - titre de partie orphelin en bas de diapositive, séparé de son tableau ;
        - pastille de durée posée sur le titre au lieu d'à sa droite.
      Résultat : **0 problème** de mise en page sur les 30 diapositives.
- [x] **Outils de contrôle déplacés dans `scripts/`** (ils vivaient dans `/tmp`,
      vidé au redémarrage) : `audit_liens.py` · `verifier_pptx.py` ·
      `check_balance.py` · `pptx_commun.py`.
- [x] **Présentation PPTX affichée comme sur le module TIC** —
      `cours/Module Intelligence Artificielle/index.html` : le cours 01 est
      maintenant dans un `.doc-row` avec, à sa droite, une carte
      `.doc-item--pptx` (📊 « Présentation PPTX », « 14 diapositives », badge
      `PPT`) — markup identique à `tic.html`. La section « 📊 Support de
      présentation » qui faisait doublon a été retirée (elle annonçait
      13 diapositives, le PPTX en a 14).
- [x] **Navigation d'un cours à l'autre** sur les 20 pages du module IA
      (5 cours Q/R + 15 séances) : barre `← Module · ◀ Précédent · Suivant ▶ ·
      📊 Présentation (PPTX)`, même aspect que les pages de cours du module TIC.
      Le CSS `.navbar` vivait dans les `<style>` inline des seules pages TIC :
      il est passé dans `css/style.css` (avec variante sombre et mobile).
      La barre est placée **dans `<main>`**, au-dessus du `<h1>` du cours —
      une première tentative l'avait mise avant l'en-tête du site.
- [x] **Drapeau posé en bout de la barre de langue** — `placeLanguageAndFlag()`
      crée la `.lang-bar` sous le menu sur **toutes** les pages et y pose le
      drapeau à droite (`margin-left:auto`, marge 32 px). L'en-tête, elle, est
      pleine : le drapeau y recouvrait « Dernières Actualités » et était coupé
      par le bord. `alignCornerFlag()` supprimé (il réécrivait `className` après
      le positionnement et annulait l'effet). Chevauchement drapeau/menu : **NON**.
- [x] Audit du site : 64 016 liens / **0 mort** · 47 007 ressources /
      **0 manquante** · 0 famille d'anomalie · 0 `target=_blank` sans `noopener`.
- [x] **Présentation PowerPoint du cours 01**
      `cours/Module Intelligence Artificielle/Presentations_PPTX/QR_IA_01_Introduction_IA.pptx`
      - **14 diapositives** 16:9, charte couleur du site (navy / bleu / vert / ambre)
      - couverture, plan du cours, **une diapositive par idée** avec le schéma
        vectoriel dessiné en formes PowerPoint (donc éditable, pas une image),
        puis les 3 questions/réponses, et enfin « les 6 points à retenir »
      - générateur versionné : `cours/Module Intelligence Artificielle/generer_presentation_ia01.py`
        (il relit le HTML, donc le PPTX suit les modifications du cours)
      - lien de téléchargement ajouté sur l'index du module
- [x] **Schémas explicatifs dans le cours 01** — 10 schémas `.diagram` bilingues
      (Exemples → Régularités → Réponse ; analogie Excel 4+8=12 ; 1 000 chats /
      1 000 chiens ; les deux familles ; où rencontre-t-on l'IA ; pourquoi c'est
      possible ; qualité des données ; l'IA à l'éducation ; formes vs sens ;
      les 3 questions éthiques ; frise 1950→2022).
      Les libellés FR/EN basculent avec les onglets de langue.
      CSS porté depuis vos fiches BAC-2026 (`.diagram .dbox .dbox.alt .dbox.warnb
      .arrow .figure-block`), Clearing **le contraste à AA** après correction
      des teintes (Lighthouse : accessibilité 100).
- [x] **Image Excel insérée** (`figures/exemple-excel.png`) dans un
      `<figure class="figure-block">` avec légende bilingue, sous la réponse qui
      explique l'analogie Excel (idée 2, question 1).
- [x] **Sélecteur de langue toujours visible** : le bloc est déplacé par
      `placeLanguageSwitcher()` dans une barre `.lang-bar` sous l'en-tête
      (l'en-tête est `sticky`) — il ne défile plus et ne masque plus le menu.
      13 pages à 3 langues (FR/EN/AR) + 16 cours Q/R à 2 langues.
- [x] **Chevauchement de l'en-tête corrigé** : le nom « Dr. BELACEL Madani »
      recouvrait le lien « À propos » (151 px de recouvrement mesurés).
      `.header-left` en `flex:0 0 auto`, `.nav-list` en `min-width:0`,
      `.header-inner` en `min-height` + `gap`.
- [x] **Drapeau : le flottement est supprimé.** Il était en `position:absolute`
      dans un `<header>` `sticky` : il flottait donc au-dessus du contenu pendant
      tout le défilement, et l'en-tête (fond opaque, `z-index:1000`) le cachait
      ensuite. Aucun emplacement libre n'existe (l'en-tête est déjà plein).
      Il reste **au pied de chaque page** (`.footer-logo`), où il ne recouvre rien.
      Dites-moi si vous le voulez dans un coin précis et je le fixe là.

- [x] **Drapeau d'Algérie affiché correctement** (`css/style.css`)
  - Cause trouvée : `.flag-corner` était déclarée 3 fois, et la 3ᵉ
    (`.flag-corner{top:68px;right:12px;width:36px}`) était **hors media query** —
    elle écrasait donc la taille sur tous les écrans. Supprimée.
  - Le drapeau est aussi passé de `position:fixed` à `position:absolute` :
    `.header` porte `backdrop-filter`, ce qui en fait le bloc conteneur des
    enfants `position:fixed` — le drapeau se positionnait donc par rapport à
    l'en-tête de 72 px et non par rapport à la fenêtre.
  - Taille 36 px → **64 × 46 px** (le GIF animé fait 132 × 95 : à 36 px il était
    illisible), position descendue à `top:148px` pour ne plus recouvrir le fil
    d'Ariane, ombre et fond blanc pour le détacher du fond.
  - Version mobile : 32 px → 44 × 32 px.
  - Le GIF **animé** `images/alg_drap.gif` est conservé (choix du site).
  - Vérifié par capture sur `tic.html`, la page du module IA et le cours 01 :
    le drapeau est net, lisible et ne chevauche plus rien.
- [x] **Cours 01 complété** (`QR_IA_01_Introduction_IA.html`)
  - *Idée 2, Q1* : analogie **Excel** — « 4 dans une cellule, 8 dans la
    suivante, on tire la poignée en bas à droite, Excel calcule 12 tout seul ».
  - *Idée 2, Q2* : exemple concret — **1 000 photos de chats + 1 000 photos de
    chiens** étiquetées, l'IA classe une photo nouvelle en « chat » ou « chien » ;
    même idée pour un dossier de factures / CV / sujets d'examen.
  - *Idée 2, Q3* : exemples de mauvaise qualité ; si des chiens non étiquetés
    se glissent dans le dossier des chats, le programme s'embrouille.
  - *Idée 3, explication* : ajout du fait qu'**OpenCode, Cursor et GitHub
    Copilot travaillent sur les fichiers du disque dur** — ils les lisent, en
    créent, les modifient et analysent un dossier entier.
  - *Idée 3, Q2* : « peuvent-ils toucher à mes fichiers ? » → oui, avec la
    consigne de toujours commencer dans un dossier de test et de ne jamais
    laisser un assistant toucher aux documents personnels.
  - Mots collés réparés : « exemplesmediocres », « réponsesmediocres ».

- [x] **Cours 01 réécrit** (`QR_IA_01_Introduction_IA.html`)
  - *Idée 2* « AI, Machine Learning and Deep Learning » →
    « How does AI work, in simple words? » / « Comment l'IA travaille-t-elle,
    en mots simples ? » : plus aucun terme technique, on explique qu'un
    programme retrouve ses règles dans les exemples.
  - *Idée 3* « Narrow AI vs General AI » → « Two families of AI: talking to
    it, or coding with it » / « Deux familles d'IA : lui parler, ou coder
    avec elle » : les assistants de conversation (ChatGPT, Grok, DeepSeek)
    d'un côté, les assistants de code (OpenCode, Cursor, GitHub Copilot)
    de l'autre.
  - Les deux idées sont rédigées en FR **et** EN (3 Q/R par langue).
  - Contrôle : 0 occurrence de *Machine Learning*, *Deep Learning*,
    *apprentissage automatique/profond*, *réseaux de neurones*, *IA faible*,
    *IA générale* dans les 5 cours Q/R du module.
  - Les 10 idées restent symétriques EN/FR (8/8 balises, 3 Q/R chacune) :
    la bascule 🇬🇧/🇫🇷 continue de fonctionner.
  - Index du module mis à jour (la description du cours 01 et la liste
    « pourquoi apprendre » ne mentionnent plus l'IA faible/générale).
- [x] Page du module IA remise dans la forme de `tic.html`
      (bandeau, fil d'Ariane, `info-box`, `level-list`, `doc-list`/`doc-item`
      avec badges, sections titrées) — 21 `doc-item`, 2 `level-item`, 52 badges.
- [x] Ancres `#cours-qr` et `#seances` vérifiées, 0 lien mort.
- [x] Ordre des blocs aligné sur `tic.html` (page-header puis fil d'Ariane).
- [x] `<button type="button">` dupliqué retiré sur
      `cours/Dialogues_Anglais/index.html` et `cours/Dialogues_TICE/index.html`.
- [x] Audit du site : 63 958 liens / 0 mort · 33 990 ressources / 0 manquante.
- [x] Audit profond : 5 anomalies bénignes (4 modèles de courriel, `404.html`).
- [x] Lighthouse page IA : perf 99 · accessibilité 100 · best practices 100 · SEO 100.
- [x] SVG de drapeau corrigé généré par `scripts/generer_drapeau.py`
      (croissant + étoile centrés) — **non utilisé**, le GIF est conservé.

---

## En attente de votre décision

### Trois dossiers en double, hors du site

Aucun n'est lié depuis une page du site. Ils alourdissent le dépôt et
faussent l'audit.

| Dossier | Pages | Poids | Nature |
|---|---|---|---|
| `cours/Module_IA_Ameliore_150_astuces` | 23 | 1,9 Mo | source de la fusion, à garder ou supprimer |
| `cours/Module_IA_Ameliore_150_astuces.zip` | — | 1,2 Mo | copie du même dossier |
| `ia-pep-2-archive` | 13 | 3,4 Mo | **ancienne version du parcours IA** : cours FR/EN/AR, PPTX, fiches |
| `ia-pep-2` | 3 | 16 Ko | 3 pages de redirection + un **dépôt Git imbriqué** (2,9 Mo) |

Tant que ces dossiers existent, l'audit du site signale des anomalies qui
ne sont pas réelles : **14 titres dupliqués** et **1 page sans `canonical`**
viennent uniquement des copies du dossier 150.

- **Supprimer** le dossier 150 + le zip fait disparaître ces faux positifs.
- `ia-pep-2` ne sert plus à rien : ses 3 pages ne sont que des redirections
  vers le module principal, et son dépôt Git imbriqué n'est pas suivi.
- `ia-pep-2-archive` est le **seul** dossier qui contient encore du contenu
  non repris ailleurs (cours en arabe notamment). À garder s'il sert.

### Jeton GitHub

Le jeton retiré doit être **révoqué manuellement** depuis les paramètres du
compte GitHub. Aucun autre jeton n'a été trouvé dans le dépôt ni dans
l'historique shell (vérifié par `scripts/scanner_secrets.py`).

### Mise en ligne

**Aucun commit ni push** n'a été effectué. Le site en ligne est encore à la
version d'avant-hier : les 152 astuces, la fusion du module, l'avertissement
et les présentations PPTX **ne sont pas publiés**. Tout est local et
fonctionnel. Dites-le quand vous voudrez que je fasse le commit.
