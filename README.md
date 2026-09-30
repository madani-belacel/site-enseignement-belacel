# site-enseignement-belacel

Site web académique professionnel de **Dr. Madani BELACEL**, Maître de Conférences B à l'Université de Mostaganem.

**URL :** https://madani-belacel.github.io/site-enseignement-belacel/

---

## Structure

```
site-enseignement-belacel/
├── index.html                 # Accueil
├── enseignement.html           # Catalogue (ordre canonique des modules)
├── tic.html                    # Module TIC
├── informatique-ens.html       # Module Informatique ENS
├── recherche-documentaire.html # Module Recherche Documentaire
├── reseaux.html                # Module Réseaux Mostaganem
├── recherche.html              # Activités de recherche
├── habilitation.html           # Dossier d'habilitation
├── ressources.html             # Ressources et outils
├── contact.html                # Contact (Formspree)
├── 404.html                    # Page d'erreur
├── sitemap-index.xml           # Index des sitemaps
├── sitemap-*.xml               # Sitemaps par module
├── robots.txt                  # Règles d'exploration
├── css/
│   ├── style.css               # Charte, thèmes clair/sombre, responsive
│   └── fonts/                  # Poppins + JetBrains Mono auto-hébergées (woff2)
├── js/
│   ├── main.v2.js              # Thème, navigation, recherche, audio
│   ├── data-loader.js          # Chargement des données JSON
│   ├── generated_courses.json  # Données générées (cours + actualités)
│   └── data.js                 # Données historicisées
├── scripts/
│   ├── generer_sitemap.py      # Régénère les 14 sitemaps
│   ├── generer_stats.py        # Recalcule les compteurs de l'accueil
│   ├── convert_images.py       # AVIF/WebP et variantes responsives
│   ├── convert_tables_to_doclist.py
│   ├── fix_grammar_nav.py
│   └── minifier.py
├── cours/                      # 2 883 pages de cours et ressources
│   ├── Module TIC/
│   ├── Module Intelligence Artificielle/  # 5 cours Q/R + 15 séances + 34 astuces
│   ├── ...
├── ia-pep-2/                  # Redirections de compatibilité
├── ia-pep-2-archive/          # Ancienne version, explicitement noindex
├── images/                     # Photos, logos, variantes responsives
└── README.md
```

---

## Déploiement

### Option 1 — GitHub Pages (recommandé, gratuit)

1. Créer un dépôt GitHub : `madani-belacel/site-enseignement-belacel`
2. Pousser les fichiers :
   ```bash
   cd site-enseignement-belacel
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/madani-belacel/site-enseignement-belacel.git
   git branch -M main
   git push -u origin main
   ```
3. Dans GitHub → Settings → Pages → Source : `main` → `/ (root)`
4. Le site est en ligne sur `https://madani-belacel.github.io/site-enseignement-belacel/`

### Option 2 — Netlify (gratuit)

1. Glisser-déposer le dossier `site-enseignement-belacel` sur https://app.netlify.com/drop
2. Obtenir une URL `nom-sitearchive.netlify.app`

### Option 3 — Hébergement FTP (OVH, etc.)

1. Copier tous les fichiers vers la racine de votre serveur via FTP

---

## Personnalisation

### Ajouter ou mettre à jour un cours

1. Placer les fichiers `.html`, `.pdf`, `.pptx`, `.mp3` ou `.md` dans le dossier du module approprié.
2. Ajouter ou modifier le lien dans la page d’index du module et, si nécessaire, dans `js/generated_courses.json`.
3. Régénérer les statistiques et le sitemap :
   ```bash
   python3 scripts/generer_stats.py
   python3 scripts/generer_sitemap.py
   ```
4. Contrôler que chaque nouvelle page et chaque ressource renvoie un statut HTTP 200.

### Ajouter un niveau de grammaire anglaise

1. Ajouter le niveau dans `cours/Grammaire Anglaise/data_levels_*.py` (liste agrégée dans `data_grammaire.py`)
2. Lancer `python3 generer_grammaire.py` pour régénérer `index.html` et les pages `niveaux/Niveau X.html`
3. Les fichiers audio MP3 manquants sont générés automatiquement (edge-tts)

### Changer les couleurs

Éditer les variables CSS dans `css/style.css` :
```css
:root {
  --primary: #146fa9;        /* Bleu académique — contraste AA sur fond clair */
  --primary-light: #3d95d4;
  --accent: #00875b;         /* Vert d'accent */
}
```
Les valeurs de `--primary`, `--text-muted` et `--text-secondary` sont calées pour
respecter WCAG AA (≥ 4,5:1) sur les trois fonds clairs du thème
(`--bg`, `--bg-alt`, `--bg-card`). Le thème sombre est défini juste après dans
`[data-theme="dark"]`.

### Ajouter une photo de profil

Placer `photo.jpg` (carré, 300×300px min) dans `images/` et modifier `index.html` :
```html
<img loading="lazy" src="images/photo.jpg" alt="Dr. Madani BELACEL" class="hero-photo">
```

---

## Ordre des modules

L'ordre public est **TIC → Intelligence Artificielle → Licence 1 Anglais →
Informatique ENS → Recherche Documentaire → Réseaux Mostaganem →
Recherche & Articles**. Il est appliqué de façon identique sur :

| Emplacement | Ordre |
| --- | --- |
| Menu « Domaines d'expertise » (1 451 pages) | ✅ |
| Grille « Modules d'enseignement » de l'accueil | ✅ |
| Filtres de `enseignement.html` (`data-module`) | ✅ |
| Liste de `cours/index.html` | ✅ |
| `js/generated_courses.json` | ✅ |

L'accueil ne liste **qu'une seule fois** chaque module : la grille
« Modules d'enseignement » fait foi, la section voisine ne présente que les
ressources complémentaires (Examens TIC, Grammaire Anglaise, Dialogues).

---

## Polices

Les polices sont **auto-hébergées** dans `css/fonts/` (sous-ensembles `latin` et
`latin-ext` de Poppins et JetBrains Mono, SIL Open Font 1.1). Les déclarations
`@font-face` sont en tête de `css/style.css` ; les pages qui n'utilisent pas
`css/style.css` chargent `css/fonts/fonts.css` directement.

Deux réglages sont importants pour les performances :

- `font-display: optional` — évite le re-saut de texte quand la police arrive
  après le premier rendu (CLS 0,24 → 0) ;
- `<link rel="preload">` des graisses 400 et 700 sur les 1 451 pages qui
  utilisent la feuille de style partagée.

> Pourquoi l'auto-hébergement : la feuille Google Fonts était la ressource
> bloquante la plus lourde du site (jusqu'à 6,5 s de gaspillage mesurées par
> Lighthouse). Aucune requête n'est faite vers `fonts.googleapis.com` ni
> `fonts.gstatic.com`.

---

## Validation avant publication

```bash
node --check js/main.v2.js
node --check js/data-loader.js
python3 -m py_compile scripts/*.py
python3 scripts/generer_stats.py
python3 scripts/generer_sitemap.py
```

Puis, dans un terminal, un serveur local et un audit Lighthouse :

```bash
python3 -m http.server 4173 --bind 127.0.0.1
lighthouse "http://127.0.0.1:4173/" --only-categories=performance,accessibility,best-practices,seo \
  --chrome-flags="--headless=new --no-sandbox --disable-gpu" --view
```

### Audit automatique

`audit_site.py` (dans `/tmp/opencode/`) parcourt les 2 883 pages et vérifie :
équilibre des balises, liens et ancres internes, ressources, `title`,
`description`, `canonical`, `<main>`, favicon, ordre des titres, `alt`,
`type="button"`, `target="_blank"`, doublons d'`id`, liens désactivés.

État au dernier passage :

```
2 883 HTML · 0 erreur de parsing · 0 lien mort · 0 ancre cassée
0 ressource manquante · 0 target=_blank sans noopener · 0 saut de titre
2 883 / 2 883 avec <main> et favicon
```

### Scores Lighthouse (14 pages, moyenne)

| | Performance | Accessibilité | Bonnes pratiques | SEO |
| --- | --- | --- | --- | --- |
| Moyenne | **99** | **100** | **100** | **98** |

> Le SEO de `404.html` est volontairement plus bas : la page porte
> `noindex`, ce qu'un moteur de recherche doit respecter.

---

## Fonctionnalités

- ✅ Design responsive (mobile, tablette, desktop)
- ✅ Thème clair/sombre (mémorisé)
- ✅ Barre de recherche avec filtres (module, type, langue)
- ✅ Readers audio pour les dialogues et la grammaire anglaise
- ✅ Fil d'Ariane (breadcrumb)
- ✅ Badges FR/EN/Cours/TD/TP/PDF/PPTX
- ✅ Animations au défilement
- ✅ Accessibilité (ARIA, contraste AA, navigation clavier, landmarks)
- ✅ Polices auto-hébergées (aucune requête vers un tiers)
- ✅ Prêt SEO (balises meta, sitemap, robots.txt)
- ✅ Aucune dépendance (HTML/CSS/JS pur)

---

## Licence

© 2026 Dr. Madani BELACEL — Université de Mostaganem. Supports pédagogiques librement téléchargeables.
