# site-enseignement-belacel

Site web académique professionnel de **Dr. Madani BELACEL**, Maître de Conférences B à l'Université de Mostaganem.

**URL :** https://madani-belacel.github.io/site-enseignement-belacel/

---

## Structure

```
site-enseignement-belacel/
├── index.html                 # Accueil
├── enseignement.html          # Présentation des modules
├── tic.html                   # Module TIC
├── informatique-ens.html      # Module Informatique ENS
├── recherche-documentaire.html# Module Recherche Documentaire
├── reseaux.html               # Module Réseaux Mostaganem
├── recherche.html             # Page Recherche
├── habilitation.html          # Dossier d'habilitation
├── ressources.html            # Ressources et outils
├── contact.html               # Contact (formulaire Formspree)
├── 404.html                   # Page d'erreur
├── sitemap.xml                # Plan du site (SEO)
├── robots.txt                 # Règles d'exploration
├── css/
│   └── style.css              # Styles (clair/sombre, responsive)
├── js/
│   ├── main.v2.js             # Thème, nav, recherche, audio, conversion
│   ├── data-loader.js         # Chargement asynchrone des cours
│   ├── generated_courses.json # Index des cours généré
│   └── data.js                # Données centralisées des cours
├── scripts/
│   ├── convert_tables_to_doclist.py   # Conversion des tableaux
│   └── fix_grammar_nav.py             # Navigation des bouts de grammaire
├── cours/                     # Supports de cours (modules, dialogues, grammaire)
├── images/                    # Photos, logos
└── README.md                  # Ce fichier
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

### Ajouter un cours

1. Placer le fichier `.md`, `.pdf` ou `.pptx` dans le dossier approprié sous `cours/`
2. La page correspondante sera automatiquement listée (les pages racine se basent sur `js/generated_courses.json`)

### Ajouter un niveau de grammaire anglaise

1. Ajouter le niveau dans `cours/Grammaire Anglaise/data_levels_*.py` (liste agrégée dans `data_grammaire.py`)
2. Lancer `python3 generer_grammaire.py` pour régénérer `index.html` et les pages `niveaux/Niveau X.html`
3. Les fichiers audio MP3 manquants sont générés automatiquement (edge-tts)

### Changer les couleurs

Éditer les variables CSS dans `css/style.css` :
```css
:root {
  --primary: #1a5276;        /* Bleu académique */
  --primary-light: #2e86c1;
  --accent: #e67e22;          /* Orange */
}
```

### Ajouter une photo de profil

Placer `photo.jpg` (carré, 300×300px min) dans `images/` et modifier `index.html` :
```html
<img loading="lazy" src="images/photo.jpg" alt="Dr. Madani BELACEL" class="hero-photo">
```

---

## Fonctionnalités

- ✅ Design responsive (mobile, tablette, desktop)
- ✅ Thème clair/sombre (mémorisé)
- ✅ Barre de recherche avec filtres (module, type, langue)
- ✅ Readers audio pour les dialogues et la grammaire anglaise
- ✅ Fil d'Ariane (breadcrumb)
- ✅ Badges FR/EN/Cours/TD/TP/PDF/PPTX
- ✅ Animations au défilement
- ✅ Accessibilité (ARIA, contraste, navigation clavier)
- ✅ Prêt SEO (balises meta, sitemap, robots.txt)
- ✅ Aucune dépendance (HTML/CSS/JS pur)

---

## Licence

© 2026 Dr. Madani BELACEL — Université de Mostaganem. Supports pédagogiques librement téléchargeables.
