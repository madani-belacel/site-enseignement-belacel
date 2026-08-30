#!/usr/bin/env python3
"""
Fix sidebar nav in Grammaire Anglaise niveaux pages to match index single-line layout.
Usage: python3 scripts/fix_grammar_nav.py
"""
import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
NIVEAUX = ROOT / 'cours' / 'Grammaire Anglaise' / 'niveaux'

# Load reference nav from index.html
index_file = ROOT / 'cours' / 'Grammaire Anglaise' / 'index.html'
index_html = index_file.read_text(encoding='utf-8')
# Extract the nav.side-menu block from index
m = re.search(r"<nav class=\"side-menu\">([\s\S]*?)</nav>", index_html)
if not m:
    print('Reference nav not found in index.html')
    raise SystemExit(1)
ref_nav = '<nav class="side-menu">' + m.group(1) + '</nav>'

# Extract the side-section block from index (single-line links)
ms = re.search(r"<div class=\"side-section\">([\s\S]*?)</div>", index_html)
if not ms:
    print('Reference side-section not found in index.html')
    raise SystemExit(1)
ref_side = '<div class="side-section">' + ms.group(1) + '</div>'

# Desired CSS for side menu (match index.html behaviour)
desired_side_css = '''.side-menu,
.side-section {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
}
.side-section {
    margin-top: 12px;
}
'''

# Regex to find existing side-menu / side-section css rules in niveaux files
pattern_css = re.compile(r"\.side-menu[\s\S]*?\.side-section\s*\{[\s\S]*?\}\s*", re.IGNORECASE)

pattern = re.compile(r"<nav class=\"side-menu\">[\s\S]*?</nav>", re.IGNORECASE)
pattern_side = re.compile(r"<div class=\"side-section\">[\s\S]*?</div>", re.IGNORECASE)

fixed = []
count = 0
for f in sorted(NIVEAUX.glob('*.html')):
    text = f.read_text(encoding='utf-8')
    if pattern.search(text):
        new_text = pattern.sub(ref_nav, text, count=1)
        if new_text != text:
            text = new_text
            f.write_text(text, encoding='utf-8')
            fixed.append(str(f.relative_to(ROOT)))
            count += 1
    # replace side-section, but adjust paths: in index links use 'niveaux/Niveau%20X',
    # in files inside 'niveaux/' we want 'Niveau%20X' (no 'niveaux/' prefix)
    if pattern_side.search(text):
        target_side = ref_side.replace('niveaux/', '')
        new_text2 = pattern_side.sub(target_side, text, count=1)
        if new_text2 != text:
            f.write_text(new_text2, encoding='utf-8')
            if str(f.relative_to(ROOT)) not in fixed:
                fixed.append(str(f.relative_to(ROOT)))
            count += 1
    # Normalize CSS for side-menu/side-section to use flex (so links stay on one line)
    if pattern_css.search(text):
        new_text3 = pattern_css.sub(desired_side_css, text, count=1)
        if new_text3 != text:
            f.write_text(new_text3, encoding='utf-8')
            if str(f.relative_to(ROOT)) not in fixed:
                fixed.append(str(f.relative_to(ROOT)))
            count += 1

print(f'Patched {count} files')
for p in fixed[:50]:
    print(p)

