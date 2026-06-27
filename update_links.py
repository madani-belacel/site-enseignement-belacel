#!/usr/bin/env python3
"""
update_links.py — Met à jour les liens des pages modules
pour pointer directement vers les fichiers HTML/PDF générés.
"""

import json, re, sys
from pathlib import Path

SITE = Path(__file__).parent
JSON_PATH = SITE / 'js' / 'generated_courses.json'

with open(JSON_PATH) as f:
    docs = json.load(f)

def resolve(title_text, module_filter=None):
    """Find best match for a title text in the generated_courses.json.
    
    module_filter: if set, only consider docs from this module.
    """
    t = title_text.lower().strip()
    t_no_desc = re.sub(r'[—–\-].*$', '', t).strip()
    
    num = None
    for m in re.finditer(r'(\d+)', t_no_desc):
        num = m.group(1)
        break
    
    prefix = 'cours'
    for p in ['cours', 'td', 'tp', 'examen']:
        if t_no_desc.startswith(p):
            prefix = p
            break
    
    mod_code = ''
    parts = t_no_desc.replace('_', ' ').split()
    for p in parts:
        if len(p) <= 5 and p.isalpha() and p not in ('cours', 'td', 'tp', 'et', 'de', 'des', 'la', 'le', 'les', 'une', 'aux'):
            mod_code = p
            break
    
    if not num:
        return None
    
    guess_stem = f'{prefix}_{mod_code}_{num}'.lower() if mod_code else f'{prefix}_{num}'.lower()
    patterns = [guess_stem, f'_{num}_']
    
    candidates = []
    for d in docs:
        if module_filter and module_filter not in d['module']:
            continue
        stem = Path(d['file']).stem.lower()
        for pat in patterns:
            try:
                if re.search(pat, stem):
                    candidates.append(d)
                    break
            except re.error:
                if pat in stem:
                    candidates.append(d)
                    break
    
    if not candidates:
        for d in docs:
            if module_filter and module_filter not in d['module']:
                continue
            stem = Path(d['file']).stem.lower()
            if f'_{num}_' in stem and prefix in stem:
                candidates.append(d)
    
    if not candidates:
        # Try without module filter
        for d in docs:
            stem = Path(d['file']).stem.lower()
            if f'_{num}_' in stem and prefix in stem:
                candidates.append(d)
    
    if not candidates:
        return None
    
    def score(c):
        s = 0
        stem = Path(c['file']).stem.lower()
        if stem == guess_stem:
            s += 5000
        elif stem.startswith(guess_stem):
            s += 3000
        if c['ext'] == 'html':
            s += 2000
        elif c['ext'] == 'pdf':
            s += 500
        if prefix == 'cours' and c['type'] == 'cours':
            s += 1000
        elif prefix == 'td' and c['type'] == 'td':
            s += 1000
        elif prefix == 'tp' and c['type'] == 'tp':
            s += 1000
        if 'série officielle' in c['path'].lower() or 'serie_officielle' in c['path'].lower():
            s += 800
        if c['lang'] == 'fr':
            s += 200
        depth = len(Path(c['path']).parts)
        if depth > 5:
            s -= 300
        if mod_code and mod_code.lower() in c['path'].lower():
            s += 500
        else:
            # Bonus for having the number close to prefix in path
            if f'{prefix}_{num}' in stem or f'{prefix.title()}_{num}' in stem:
                s += 400
        return s
    
    candidates.sort(key=score, reverse=True)
    return candidates[0]['path']

def update_page(filepath):
    """Update href in .doc-item and .level-item to actual paths."""
    html = filepath.read_text(encoding='utf-8')
    original = html
    
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    changed = False
    
    # Determine module filter from filename
    fname = filepath.name
    module_filter = None
    if 'tic' in fname:
        module_filter = 'Module TIC'
    elif 'informatique-ens' in fname:
        module_filter = 'Module Informatique ENS'
    elif 'recherche-documentaire' in fname:
        module_filter = 'Module Recherche Documentaire'
    elif 'reseaux' in fname:
        module_filter = 'Module_Réseau_Mostaganem'
    
    # Update .doc-item links
    for a in soup.find_all('a', class_='doc-item'):
        title_div = a.find('div', class_='doc-title')
        if not title_div:
            continue
        title = title_div.get_text(strip=True)
        path = resolve(title, module_filter)
        if path:
            a['href'] = path
            changed = True
    
    # Update .level-item links
    for a in soup.find_all('a', class_='level-item'):
        name_span = a.find('span', class_='level-name')
        if not name_span:
            continue
        path = None
        if 'tic' in fname:
            path = 'cours/_index_Module_TIC.html'
        elif 'informatique-ens' in fname:
            path = 'cours/_index_Module_Informatique_ENS.html'
        elif 'recherche-documentaire' in fname:
            path = 'cours/_index_Module_Recherche_Documentaire.html'
        elif 'reseaux' in fname:
            path = 'cours/_index_Module_Réseau_Mostaganem.html'
        if path:
            a['href'] = path
            changed = True
    
    if changed:
        filepath.write_text(str(soup), encoding='utf-8')
        print(f"  ✅ Updated: {filepath.name}")
    else:
        print(f"  ⏭️  No changes: {filepath.name}")

# Update all module pages
pages = ['tic.html', 'informatique-ens.html', 'recherche-documentaire.html', 'reseaux.html']
for p in pages:
    fp = SITE / p
    if fp.exists():
        update_page(fp)
