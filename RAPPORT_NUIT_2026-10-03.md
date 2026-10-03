# Rapport de nuit — 03/10/2026

## Mission

Ajouter au module Intelligence Artificielle une page de détail pour chacune des
152 astuces, contenant une explication longue et pédagogique en 10 sections.

Le contenu HTML est rédigé par le professeur, lot par lot. L'agent intègre,
teste et commite en local. L'auto-génération du texte avait été écartée : elle
produisait du texte parasite (des caractères coréens glissés dans les phrases
françaises).

---

## Résultat

**15 pages de détail créées** — lots 1, 2 et 3.

| Lot | Astuces | Pages |
|-----|---------|-------|
| 1 | 6, 12, 23, 35, 37 | 5 |
| 2 | 36, 43, 44, 91, 100 | 5 |
| 3 | 1, 7, 8, 9, 10 | 5 |

Progression : **15 / 152 (9,9 %)**. Restent les lots 4 à 30 (137 astuces).

Emplacement : `cours/Module Intelligence Artificielle/seances/astuces-details/`

---

## Ce qui a été fait

### 1. Intégration des trois lots

`scripts/contenus_details/lot_{1,2,3}.py` contiennent le contenu rédigé, découpé
automatiquement en 10 sections par le générateur. Le gabarit fournit le `<h1>`,
le fil d'Ariane, la navigation et le pied de page ; le contenu n'apporte que les
10 sections.

La section 1 (« Le texte source ») est recopiée automatiquement depuis la page des
152 astuces : elle ne peut pas se désynchroniser.

### 2. Bouton d'accès

`scripts/ajouter_boutons_details.py` insère sous chaque astuce :

- un bouton **« 🔍 Voir l'explication détaillée »** pour les 15 astuces traitées,
- un simple libellé **« 🔍 Explication détaillée — en préparation »** pour les 137
  autres.

Un bouton vers une page absente est pire qu'aucun bouton : chaque lien a été vérifié.
Le script est idempotent, il peut être relancé après chaque nouveau lot.

### 3. Corrections dans les outils de contrôle

Deux bugs d'audit, qui auraient produit des faux résultats à chaque exécution :

| Fichier | Problème | Effet |
|---------|----------|-------|
| `audit_approfondi_ia.py` | regex `content="([^"']*)"` s'arrêtait à l'apostrophe de « l'astuce » | descriptions mesurées à 26 caractères au lieu de 163 : 15 faux positifs |
| `audit_liens.py` | parcourait les dossiers `backup_2026-10-0{2,3}` | 90 fausses alertes, les copies étant à la mauvaise profondeur |

### 4. Défauts corrigés dans les pages générées

| Défaut | Portée | Cause |
|--------|--------|-------|
| Liens morts | **270** | Le gabarit est écrit pour `seances/`, les pages vivent un niveau plus bas. Le décalage n'était appliqué qu'à `css/` et `js/`. |
| `srcset` non traité | 4 par page | Le logo du pied de page pointait vers `../../../images/…` au lieu de 4 niveaux |
| Lien vers soi-même | 15 | La section « texte source » recopiait le bouton, dont l'URL relative est fausse une fois déplacé |
| Voisins inexistants | 15 liens en 404 | La navigation proposait astuce N-1 et N+1 même sans page |
| Titres hors norme | 2 | 73 et 87 caractères, au lieu de 70 maximum |
| Retour en bas dupliqué | 15 | Deux liens identiques à trois lignes d'écart en haut de page |

Le décalage de profondeur est désormais général (sur `href`, `src` et `srcset`) et
porte sur toute la charpente. Le validateur résout désormais chaque chemin sur le
disque au lieu de vérifier une liste figée — c'est ce contrôle qui avait laissé
passer les 270 liens morts.

---

## Tests

| Test | Résultat |
|------|----------|
| Pages de détail en HTTP 200 | 15 / 15 |
| Liens relatifs + `srcset` résolus | **419 / 419**, 0 en erreur |
| Sections `<h2>` numérotées 1 à 10 | 15 / 15 |
| Section « Le texte source » présente | 15 / 15 |
| HTML équilibré (parseur complet) | 15 / 15 |
| Caractères non latins (coréen, chinois) | 0 |
| `</br>` orphelin | 0 |
| Lien de retour en haut et en bas | 15 / 15 |
| Navigation vers un voisin existant | 14 liens, 0 en 404 |
| Boutons actifs pointant vers un fichier absent | 0 |
| Blocs d'astuce dans la page des 152 | 152 / 152 |
| Séquences de 10 mots partagées entre pages | 0 |
| Titres dans 15-70 car. / descriptions dans 60-165 car. | 15 / 15 |
| Non-régression : 15 séances, index racine, index module | HTTP 200 |
| Audit des liens du site public | 0 anomalie hors `cours/IA/` (non publié) |

---

## Point non atteint — volumétrie

La cible était de **2 000 à 2 800 mots** par page. Les pages font **848 à 1 092
mots**, soit 942 en moyenne : **environ la moitié de la cible**.

Ce n'est pas un défaut technique mais un point de contenu. Les 15 pages respectent
intégralement le gabarit en 10 sections, et chacune est cohérente et utilisable telle
quelle. Rien n'a été ajouté pour gonler le volume : le contenu est votre rédaction,
et le compléter par de la génération automatique avait été écarté pour cause de
texte parasite.

Trois voies possibles, à trancher :

1. **Accepter la profondeur actuelle** — 10 sections completes, ~950 mots.
2. **Envoyer des lots enrichis** — le gabarit s'enrichit sans changer de code.
3. **Ajouter une 11ᵉ section** (« Aller plus loin », cas limites, exercices),
   distincte du contenu rédigé, qui resterait votre.

Dans tous les cas, il faut **137 pages de plus** pour couvrir le module.

---

## Deux points préexistants, non touchés

Signalés par l'audit, hors périmètre de cette mission :

- `seances/astuces-ia.html` : 288 Ko. La page dépassait déjà 274 Ko avant les
  boutons ; les 152 libellés « en préparation » y ajoutent environ 8 Ko.
- `seances/article-scientifique.html` : meta description à 169 caractères, pour une
  norme de 165.

---

## Fichiers

**Créés**

```
scripts/generateur_details_astuces.py      générateur + validation
scripts/ajouter_boutons_details.py         insertion des boutons (idempotent)
scripts/contenus_details/lot_1.py          contenu, 5 astuces
scripts/contenus_details/lot_2.py          contenu, 5 astuces
scripts/contenus_details/lot_3.py          contenu, 5 astuces
cours/.../seances/astuces-details/*.html   15 pages de détail
```

**Modifiés**

```
cours/.../seances/astuces-ia.html          15 boutons + 137 libellés + CSS
scripts/audit_approfondi_ia.py             regex de description
scripts/audit_liens.py                     exclusion des sauvegardes
.gitignore                                 backup_2026-10-03/ et liste-astuces.txt
```

**Sauvegardes** — `backup_2026-10-02/` (45 fichiers) et `backup_2026-10-03/`
(2 fichiers) conservées, et désormais ignorées par Git pour ne jamais être
publiées.

---

## Publication

Commit local : **`b93879516`**, en attente de push.

Aucun jeton n'est disponible : le remote est en HTTPS sans identifiants et `gh`
n'est pas installé. **Le push n'a pas été effectué.**

Pour publier, fournissez un jeton, ou poussez vous-même :

```
git push origin main
```

> Si un jeton a déjà été transmis pendant cette session, pense à le révoquer sur
> https://github.com/settings/tokens

Après le push, GitHub Pages met 1 à 3 minutes à publier. Contrôle :
`https://madani-belacel.github.io/site-enseignement-belacel/cours/Module%20Intelligence%20Artificielle/seances/astuces-details/astuce-001.html`

---

## Suite

1. Valider la profondeur voulue (voir « Point non atteint »).
2. Envoyer le lot 4 (astuces 11, 13, 14, 15, 16).
3. Pour chaque nouveau lot : `rm -rf scripts/contenus_details/__pycache__`,
   puis `python3 scripts/generateur_details_astuces.py`,
   puis `python3 scripts/ajouter_boutons_details.py`.
   Les pages manquantes font passer leurs boutons de « en préparation » à actifs
   automatiquement.
4. Pousser une fois les 30 lots reçus, ou par lots si vous préférez publier au fil
   de l'eau.