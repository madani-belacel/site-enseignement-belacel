#!/usr/bin/env python3
"""
import_courses.py — Importation automatique des cours
Scanne l'arborescence des supports et génère les pages HTML de cours.

Usage:
    python import_courses.py --source "C:/chemin/vers/Supports de Cours"
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

def scan_courses(source_dir):
    """Parcourt les dossiers et collecte les métadonnées des cours."""
    courses = []
    source = Path(source_dir)
    
    for root, dirs, files in os.walk(source):
        for f in files:
            fpath = Path(root) / f
            ext = fpath.suffix.lower()
            if ext not in ('.md', '.pdf', '.pptx'):
                continue
            
            rel = fpath.relative_to(source)
            parts = rel.parts
            
            # Déterminer le module
            module = parts[0] if parts else ""
            
            # Déterminer la langue
            lang = 'fr'
            if 'Anglais' in parts or 'EN' in f or '_EN' in f or '_AN' in f:
                lang = 'en'
            elif 'Français' in parts or '_FR' in f:
                lang = 'fr'
            
            # Déterminer le type
            dtype = 'cours'
            if 'TD_' in f or '_TD' in f or '/TD/' in str(fpath) or '\\TD\\' in str(fpath):
                dtype = 'td'
            elif 'TP_' in f or '_TP' in f or '/TP/' in str(fpath) or '\\TP\\' in str(fpath):
                dtype = 'tp'
            
            # Date de modification
            mtime = os.path.getmtime(fpath)
            date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            
            courses.append({
                'path': str(rel),
                'file': f,
                'module': module,
                'lang': lang,
                'type': dtype,
                'date': date,
                'ext': ext[1:],
            })
    
    return courses

def generate_module_page(module_name, courses):
    """Génère la section HTML pour un module donné."""
    lines = []
    lines.append(f'<section aria-labelledby="{module_name}-title" style="margin-bottom:2rem;">')
    lines.append(f'  <h2 id="{module_name}-title" class="section-title">{module_name}</h2>')
    lines.append(f'  <p class="section-subtitle">{len(courses)} documents trouvés</p>')
    lines.append(f'  <div class="doc-list">')
    
    for c in sorted(courses, key=lambda x: x['file']):
        lang_badge = 'badge-fr' if c['lang'] == 'fr' else 'badge-en'
        lang_label = 'FR' if c['lang'] == 'fr' else 'EN'
        type_badge = f'badge-{c["type"]}'
        type_label = c['type'].upper()
        ext_badge = f'badge-{c["ext"]}' if c['ext'] in ('pdf', 'pptx') else ''
        ext_label = c['ext'].upper() if c['ext'] in ('pdf', 'pptx') else ''
        
        lines.append(f'    <a href="{c["path"]}" class="doc-item" data-module="{c["module"]}" data-level="">')
        lines.append(f'      <span class="doc-icon">{"📘" if c["type"]=="cours" else "📝" if c["type"]=="td" else "⚙️"}</span>')
        lines.append(f'      <div class="doc-info">')
        lines.append(f'        <div class="doc-title">{c["file"]}</div>')
        lines.append(f'        <div class="doc-date">Mise à jour : {c["date"]}</div>')
        lines.append(f'      </div>')
        lines.append(f'      <div class="doc-badges">')
        lines.append(f'        <span class="badge {lang_badge}">{lang_label}</span>')
        lines.append(f'        <span class="badge {type_badge}">{type_label}</span>')
        if ext_label:
            lines.append(f'        <span class="badge {ext_badge}">{ext_label}</span>')
        lines.append(f'      </div>')
        lines.append(f'    </a>')
    
    lines.append('  </div>')
    lines.append('</section>')
    return '\n'.join(lines)

def main():
    parser = argparse.ArgumentParser(description='Importation automatique des cours')
    parser.add_argument('--source', required=True, help='Chemin du dossier Supports de Cours')
    parser.add_argument('--output', default='.', help='Dossier de sortie (site)')
    args = parser.parse_args()
    
    print(f"Scanning: {args.source}")
    courses = scan_courses(args.source)
    
    # Regrouper par module
    modules = {}
    for c in courses:
        mod = c['module']
        if mod not in modules:
            modules[mod] = []
        modules[mod].append(c)
    
    print(f"Found {len(courses)} documents in {len(modules)} modules:")
    for mod, mod_courses in sorted(modules.items()):
        print(f"  - {mod}: {len(mod_courses)} docs")
    
    # Générer le fichier JSON pour le site
    output_path = Path(args.output)
    data_file = output_path / 'js' / 'generated_courses.json'
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)
    print(f"\nGenerated: {data_file}")

if __name__ == '__main__':
    main()
