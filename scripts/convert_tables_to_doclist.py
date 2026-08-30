#!/usr/bin/env python3
from bs4 import BeautifulSoup
from pathlib import Path

TARGETS = [
    'cours/Dialogues_Anglais/index.html',
    'cours/Dialogues_TICE/index.html',
]

ROOT = Path(__file__).resolve().parents[1]

for rel in TARGETS:
    path = ROOT / rel
    if not path.exists():
        print(f"Skip missing: {path}")
        continue
    s = path.read_text(encoding='utf-8')
    soup = BeautifulSoup(s, 'html.parser')
    # find the section with heading containing 'Niveaux disponibles'
    sections = soup.find_all('section')
    target_section = None
    for sec in sections:
        h = sec.find(['h2','h3'])
        if h and 'Niveaux disponibles' in h.get_text():
            target_section = sec
            break
    if not target_section:
        print(f"No target section in {rel}")
        continue
    table = target_section.find('table')
    if not table:
        print(f"No table found in section of {rel}")
        continue
    # build new doc-list container
    doc_list = soup.new_tag('div', **{'class':'doc-list'})
    tbody = table.find('tbody')
    if not tbody:
        print(f"No tbody in table of {rel}")
        continue
    for tr in tbody.find_all('tr'):
        tds = tr.find_all('td')
        if len(tds) < 7:
            continue
        num = tds[0].get_text(strip=True)
        title = tds[1].get_text(strip=True)
        desc = tds[2].get_text(strip=True)
        dialogues = tds[3].get_text(strip=True)
        phrases = tds[4].get_text(strip=True)
        pptx = tds[5].get_text(strip=True)
        links_td = tds[6]
        # create doc-row
        doc_row = soup.new_tag('div', **{'class':'doc-row'})
        # main doc-item (links to audio if present)
        # find first audio link if exists
        audio_a = links_td.find('a')
        href_audio = audio_a['href'] if audio_a and audio_a.has_attr('href') else '#'
        main_a = soup.new_tag('a', **{'class':'doc-item', 'href': href_audio})
        icon = soup.new_tag('span', **{'class':'doc-icon'})
        icon.string = '📘'
        main_a.append(icon)
        info = soup.new_tag('div', **{'class':'doc-info'})
        title_div = soup.new_tag('div', **{'class':'doc-title'})
        title_div.string = f"{num}. {title}"
        info.append(title_div)
        date_div = soup.new_tag('div', **{'class':'doc-date'})
        date_div.string = f"{desc} · {dialogues} dialogues · {phrases} phrases · {pptx} PPTX"
        info.append(date_div)
        main_a.append(info)
        # extras (access links)
        extras = soup.new_tag('div', **{'class':'doc-extras'})
        for a in links_td.find_all('a'):
            a_clone = soup.new_tag('a', href=a.get('href'))
            a_clone.string = a.get_text()
            a_clone['class'] = 'access-badge'
            extras.append(a_clone)
        main_a.append(extras)
        doc_row.append(main_a)
        doc_list.append(doc_row)
    # replace table with doc_list
    table.replace_with(doc_list)
    # write back
    path.write_text(str(soup), encoding='utf-8')
    print(f"Converted table -> doc-list in {rel}")
