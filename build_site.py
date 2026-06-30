#!/usr/bin/env python3
"""
build_site.py — Convertit tous les supports MD en pages HTML +
copie les PDF/PPTX dans le site, puis régénère generated_courses.json.

Usage:
    python build_site.py [--source CHEMIN] [--site CHEMIN]
"""

import os, sys, json, argparse, re, shutil
from datetime import datetime
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

# ── Configuration ──
SOURCE_DIR = Path(__file__).resolve().parent.parent  # Supports de Cours/
SITE_DIR   = Path(__file__).resolve().parent          # site-enseignement-belacel/

HEADER_HTML = """<!DOCTYPE html><html lang="fr" data-theme="light"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — Dr. Madani BELACEL</title>
<meta name="description" content="{description}">
<link rel="stylesheet" href="{root_path}css/style.css">
<link rel="icon" href="{root_path}images/Université_de_Mostaganem.png">
<style>
  .md-content {{ max-width: 900px; margin: 0 auto; padding: 2rem 1.5rem; }}
  .md-content h1 {{ font-family: var(--font-heading); color: var(--primary); margin: 1.5rem 0 0.5rem; font-size: 1.6rem; }}
  .md-content h2 {{ font-family: var(--font-heading); color: var(--primary); margin: 1.3rem 0 0.4rem; font-size: 1.3rem; border-bottom: 1px solid var(--border); padding-bottom: 0.3rem; }}
  .md-content h3 {{ font-family: var(--font-heading); margin: 1rem 0 0.3rem; font-size: 1.1rem; }}
  .md-content p {{ margin: 0.5rem 0; line-height: 1.8; }}
  .md-content ul, .md-content ol {{ margin: 0.5rem 0 0.5rem 1.5rem; }}
  .md-content li {{ margin: 0.25rem 0; line-height: 1.7; }}
  .md-content blockquote {{ border-left: 4px solid var(--primary-light); padding: 0.5rem 1rem; margin: 0.75rem 0; background: var(--bg-alt); border-radius: 0 var(--radius) var(--radius) 0; }}
  .md-content blockquote p {{ margin: 0.2rem 0; }}
  .md-content code {{ background: var(--bg-alt); padding: 0.15rem 0.4rem; border-radius: 4px; font-size: 0.88em; }}
  .md-content pre {{ background: var(--bg-alt); padding: 1rem; border-radius: var(--radius); overflow-x: auto; border: 1px solid var(--border); margin: 0.75rem 0; }}
  .md-content pre code {{ background: none; padding: 0; }}
  .md-content table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
  .md-content th, .md-content td {{ border: 1px solid var(--border); padding: 0.5rem; text-align: left; }}
  .md-content th {{ background: var(--bg-alt); font-family: var(--font-heading); }}
  .md-content hr {{ border: none; border-top: 1px solid var(--border); margin: 1.5rem 0; }}
  .md-content img {{ max-width: 100%; border-radius: var(--radius); }}
  .md-content em {{ font-style: italic; }}
  .md-content strong {{ font-weight: 700; }}
  .md-meta {{ background: var(--bg-alt); border: 1px solid var(--border); border-radius: var(--radius); padding: 1rem; margin-bottom: 1.5rem; font-size: 0.9rem; }}
  .md-meta strong {{ font-family: var(--font-heading); }}
  .download-bar {{ display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }}
  .download-link {{ display: inline-flex; align-items: center; gap: 0.4rem; padding: 0.5rem 1rem; border-radius: var(--radius); font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: opacity 0.2s; }}
  .download-link:hover {{ opacity: 0.85; }}
  .download-pdf {{ background: #e74c3c; color: #fff; }}
  .download-pptx {{ background: #d24726; color: #fff; }}
</style>
</head><body>

<header class="header" role="banner">
  <div class="header-inner">
    <div class="header-left">
      <a href="{root_path}index.html" class="header-logo">
        <img src="{root_path}images/Université_de_Mostaganem.png" alt="Université de Mostaganem">
        <div class="header-logo-text">Dr. BELACEL Madani<small>MCB — Université de Mostaganem</small></div>
      </a>
      <div class="header-faculty">
        <img src="{root_path}images/LOGO-FLE-UNIV-Mosta.jpeg" alt="Faculté des Lettres et des Arts">
      </div>
    </div>
    <img src="{root_path}images/alg_drap.gif" alt="Algérie" class="flag-corner">
    <button id="nav-toggle" class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <nav role="navigation" aria-label="Navigation principale">
      <ul id="nav-list" class="nav-list">
        <li><a href="{root_path}index.html">Accueil</a></li>
        <li><a href="{root_path}enseignement.html">Enseignement</a></li>
        <li><a href="{root_path}recherche.html">Recherche</a></li>
        <li><a href="{root_path}habilitation.html">Habilitation</a></li>
        <li><a href="{root_path}ressources.html">Ressources</a></li>
        <li><a href="{root_path}contact.html">Contact</a></li>
        <li><button id="theme-toggle" class="theme-toggle" aria-label="Changer le thème">☾</button></li>
      </ul>
    </nav>
  </div>
</header>"""

FOOTER_HTML = """<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer-logos">
      <img src="{root_path}images/Université_de_Mostaganem.png" alt="Université de Mostaganem" class="footer-logo">
      <img src="{root_path}images/alg_drap.gif" alt="Algérie" class="footer-logo">
    </div>
    <div class="footer-infos">
      <span>📧 madani.belacel@univ-mosta.dz</span>
      <span>📍 Université de Mostaganem</span>
      <span>📅 2025-2026</span>
    </div>
    <p>© 2026 Dr. Madani BELACEL — Tous droits réservés.</p>
  </div>
</footer>
<script src="{root_path}js/data.js"></script>
<script src="{root_path}js/main.js"></script>
</body></html>"""


def slugify(text):
    return re.sub(r'[^\w\-]', '_', text.replace(' ', '_')).strip('_')


def extract_title(md_text, filename):
    """Extract first H1 from markdown, or use filename."""
    m = re.search(r'^#\s+(.+)$', md_text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return Path(filename).stem.replace('_', ' ')


def extract_description(md_text):
    """Extract first paragraph after H1."""
    lines = md_text.split('\n')
    capture = False
    for line in lines:
        if line.startswith('# '):
            capture = True
            continue
        if capture and line.strip() and not line.startswith('>') and not line.startswith('---'):
            desc = re.sub(r'\*\*(.+?)\*\*', r'\1', line.strip()[:200])
            return desc
    return "Support de cours — Dr. Madani BELACEL"


def classify_doc(filepath):
    """Determine module, language, type from path/filename."""
    parts = filepath.parts
    fname = filepath.name
    fpath_str = str(filepath)

    # Module — use first matching path component (top-level dir is most reliable)
    module = "Racine"
    for p in parts:
        pl = p.lower()
        if 'tic' in pl:
            module = "Module TIC"
            break
        elif 'informatique ens' in pl or 'informatique_ens' in pl:
            module = "Module Informatique ENS"
            break
        elif 'recherche documentaire' in pl or 'recherche_documentaire' in pl:
            module = "Module Recherche Documentaire"
            break
        elif 'réseau' in pl or 'reseau' in pl:
            module = "Module_Réseau_Mostaganem"
            break

    # Language
    lang = 'fr'
    if 'Anglais' in parts or '_EN' in fname:
        lang = 'en'
    elif 'Français' in parts or '_FR' in fname:
        lang = 'fr'

    # Type
    dtype = 'cours'
    if re.search(r'\bTD[_-]', fname) or 'TD_' in fname or '_TD' in fname or '/TD/' in fpath_str:
        dtype = 'td'
    elif re.search(r'\bTP[_-]', fname) or 'TP_' in fname or '_TP' in fname or '/TP/' in fpath_str:
        dtype = 'tp'
    elif 'Examen' in fname or 'Sujet' in fname:
        dtype = 'examen'

    return module, lang, dtype


def md_to_html(md_text, title, description):
    """Convert markdown to styled HTML content."""
    extras = ['fenced_code', 'tables', 'codehilite']
    html_body = markdown.markdown(md_text, extensions=extras)
    return html_body


def build_page(md_text, filename, rel_path, downloads=None):
    """Build a full HTML page from markdown content."""
    title = extract_title(md_text, filename)
    description = extract_description(md_text)
    html_body = md_to_html(md_text, title, description)

    meta_lines = []
    for line in md_text.split('\n'):
        stripped = line.strip()
        if stripped.startswith('**') and ':' in stripped:
            meta_lines.append(stripped)
        elif stripped.startswith('- **') and ':' in stripped:
            meta_lines.append(stripped)

    meta_html = ""
    if meta_lines:
        def boldify(line):
            return re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', line)
        items = "".join(f"<li>{boldify(l)}</li>" for l in meta_lines[:10])
        meta_html = f'<div class="md-meta"><strong>Informations :</strong><ul>{items}</ul></div>'

    download_html = ""
    if downloads:
        links = "".join(
            f'<a href="{fn}" download class="download-link download-{ext.lower()}">⬇ {ext}</a>'
            for ext, fn in downloads
        )
        download_html = f'<div class="download-bar">{links}</div>'

    root_path = "../" * (rel_path.count('/') + 1)

    header = HEADER_HTML.format(title=title, description=description, root_path=root_path)
    footer = FOOTER_HTML.format(root_path=root_path)

    module_name = ""
    for p in Path(rel_path).parts:
        if 'Module' in p:
            module_name = p
            break

    breadcrumb_links = ""
    if module_name:
        module_file = ""
        ml = module_name.lower()
        if 'tic' in ml:
            module_file = "tic.html"
        elif 'informatique ens' in ml:
            module_file = "informatique-ens.html"
        elif 'recherche' in ml:
            module_file = "recherche-documentaire.html"
        elif 'reseau' in ml:
            module_file = "reseaux.html"
        if module_file:
            breadcrumb_links = f'<li><a href="{root_path}{module_file}">{module_name}</a></li>\n    '

    breadcrumb = f'''<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="{root_path}index.html">Accueil</a></li>
    <li><a href="{root_path}enseignement.html">Enseignement</a></li>
    {breadcrumb_links}<li class="current">{title}</li>
  </ol>
</nav>'''

    page = f"""{header}

{breadcrumb}

<main class="page-content">
  <div class="md-content">
    {meta_html}
    {download_html}
    {html_body}
  </div>
</main>

{footer}"""
    return page


def scan_and_convert(source_dir, site_dir):
    """Main conversion function."""
    source = Path(source_dir)
    site   = Path(site_dir)
    cours_dir = site / 'cours'

    all_docs = []
    converted = 0
    copied_pdf = 0
    copied_pptx = 0
    copied_images = 0

    # Module dirs to scan
    module_dirs = [
        source / 'Module TIC',
        source / 'Module Informatique ENS',
        source / 'Module Recherche Documentaire',
        source / 'Module_Réseau_Mostaganem',
    ]

    # Also scan root .md files
    root_mds = list(source.glob('*.md'))
    root_mds = [f for f in root_mds if not f.name.startswith('_') and 'site-enseignement' not in str(f)]

    # Build total file list
    all_files = list(root_mds)
    image_exts = ('*.png', '*.svg', '*.jpg', '*.jpeg', '*.gif')
    for md_dir in module_dirs:
        if md_dir.exists():
            for ext in ('*.md', '*.pdf', '*.pptx') + image_exts:
                all_files.extend(md_dir.rglob(ext))

    print(f"📦 Scanning {len(all_files)} files...")

    for fpath in all_files:
        if '/suivi/' in str(fpath) or '/latex/' in str(fpath) or '/_build_' in str(fpath) or '/_scripts/' in str(fpath) or '/__pycache__/' in str(fpath):
            continue

        if str(fpath).startswith(str(source / '_archives')):
            continue

        rel = fpath.relative_to(source)
        ext = fpath.suffix.lower()
        module, lang, dtype = classify_doc(fpath)

        mtime = os.path.getmtime(fpath)
        date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')

        if ext == '.md':
            # Convert to HTML
            target_rel = Path(str(rel).replace('.md', '.html'))
            target_path = cours_dir / target_rel

            try:
                md_text = fpath.read_text(encoding='utf-8', errors='replace')
                # Find sibling PDF/PPTX for download links
                downloads = []
                for sib_ext in ['.pdf', '.pptx']:
                    sib = fpath.with_suffix(sib_ext)
                    if sib.exists():
                        downloads.append((sib_ext[1:].upper(), sib.name))
                html_page = build_page(md_text, fpath.name, str(target_rel), downloads)
                target_path.parent.mkdir(parents=True, exist_ok=True)
                target_path.write_text(html_page, encoding='utf-8')
                converted += 1
                doc_path = str(target_rel)
            except Exception as e:
                print(f"  ❌ {rel}: {e}")
                doc_path = str(rel)
        else:
            # Copy PDF/PPTX
            target_path = cours_dir / rel
            target_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(fpath, target_path)
                if ext == '.pdf':
                    copied_pdf += 1
                elif ext == '.pptx':
                    copied_pptx += 1
                elif ext in ('.png', '.svg', '.jpg', '.jpeg', '.gif'):
                    copied_images += 1
                doc_path = str(target_rel) if ext == '.md' else str(rel)
            except Exception as e:
                print(f"  ❌ {rel}: {e}")
                doc_path = str(rel)

        doc_rel = target_rel if ext == '.md' else rel
        display_ext = 'html' if ext == '.md' else ext[1:]
        all_docs.append({
            'path': 'cours/' + str(doc_rel),
            'file': fpath.name,
            'module': module,
            'lang': lang,
            'type': dtype,
            'date': date,
            'ext': display_ext,
        })

    # Write generated_courses.json
    json_path = site / 'js' / 'generated_courses.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_docs, f, ensure_ascii=False, indent=2)

    print(f"\n✅ Done!")
    print(f"   • {converted} MD → HTML")
    print(f"   • {copied_pdf} PDF copied")
    print(f"   • {copied_pptx} PPTX copied")
    print(f"   • {copied_images} images copied")
    print(f"   • {len(all_docs)} total entries in generated_courses.json")
    return all_docs


def generate_module_indexes(site_dir, docs):
    """Génère une page HTML d'index pour chaque module."""
    modules = {}
    for d in docs:
        mod = d['module']
        if mod == 'Racine':
            continue
        if mod not in modules:
            modules[mod] = []
        modules[mod].append(d)

    for mod_name, mod_docs in modules.items():
        slug = slugify(mod_name)
        filepath = site_dir / f'cours/_index_{slug}.html'

        title = f"Index — {mod_name}"
        header = HEADER_HTML.format(title=title, description=f"Tous les documents du {mod_name}", root_path="../")
        footer = FOOTER_HTML.format(root_path="../")

        items = []
        for d in sorted(mod_docs, key=lambda x: x['file']):
            lang_badge = 'badge-fr' if d['lang'] == 'fr' else 'badge-en'
            lang_label = 'FR' if d['lang'] == 'fr' else 'EN'
            type_label = d['type'].upper()
            ext_label = d['ext'].upper() if d['ext'] in ('pdf', 'pptx') else ''
            icon = "📘" if d['type'] == 'cours' else "📝" if d['type'] == 'td' else "⚙️" if d['type'] == 'tp' else "📄"

            badges = f'<span class="badge {lang_badge}">{lang_label}</span><span class="badge badge-{d["type"]}">{type_label}</span>'
            if ext_label:
                badges += f'<span class="badge badge-{d["ext"]}">{ext_label}</span>'

            link = d['path'].removeprefix('cours/')
            items.append(f'''<a href="{link}" class="doc-item">
  <span class="doc-icon">{icon}</span>
  <div class="doc-info">
    <div class="doc-title">{d['file']}</div>
    <div class="doc-date">Mise à jour : {d['date']}</div>
  </div>
  <div class="doc-badges">{badges}</div>
</a>''')

        content = f'''<main class="page-content">
  <div class="container">
    <h1 class="section-title">{mod_name}</h1>
    <p class="section-subtitle">{len(mod_docs)} documents</p>
    <div class="doc-list">{"".join(items)}</div>
  </div>
</main>'''

        page = f"""{header}
<div class="page-header">
  <div class="container"><h1>{mod_name}</h1><p>Index des documents — {len(mod_docs)} fichiers</p></div>
</div>
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="../index.html">Accueil</a></li>
    <li><a href="../enseignement.html">Enseignement</a></li>
    <li class="current">{mod_name}</li>
  </ol>
</nav>
{content}
{footer}"""

        filepath.write_text(page, encoding='utf-8')
        print(f"   • Generated index: _index_{slug}.html ({len(mod_docs)} docs)")


def main():
    parser = argparse.ArgumentParser(description='Build site from course materials')
    parser.add_argument('--source', default=str(SOURCE_DIR), help='Source directory (Supports de Cours)')
    parser.add_argument('--site', default=str(SITE_DIR), help='Site directory')
    args = parser.parse_args()

    source = Path(args.source)
    site = Path(args.site)

    if not source.exists():
        print(f"❌ Source directory not found: {source}")
        sys.exit(1)
    if not site.exists():
        print(f"❌ Site directory not found: {site}")
        sys.exit(1)

    print(f"🔧 Source: {source}")
    print(f"🔧 Site:   {site}")
    print()

    docs = scan_and_convert(source, site)
    generate_module_indexes(site, docs)

    print(f"\n🎉 Site updated at: {site}")


if __name__ == '__main__':
    main()
