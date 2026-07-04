#!/usr/bin/env python3
"""Met à jour les chemins dans les fichiers HTML pour référencer les codes sources locaux."""

import os
import re
import glob

BASE = "/home/madani/Bureau/Habilitation_Universitaire/08 - Preuves des Activités/Supports de Cours/site-enseignement-belacel/cours/Module_Recherche_Articles"
CONTIKI_EXAMPLES = "/home/madani/contiki-ng/examples"
LOCAL_NOTE = "\n\n<p class=\"note-local\" style=\"background:#e8f5e9;border-left:4px solid #2e7d32;padding:0.8rem 1rem;border-radius:4px;margin:1rem 0;\"><strong>📂 Codes sources disponibles localement :</strong> Ces codes sont déjà présents sur votre machine dans le dossier <code>{}</code>. Vous pouvez également les cloner depuis GitHub si nécessaire.</p>\n"

CHANGES = {
    "RPLMQOS": {
        "github_url": "https://github.com/madani-belacel/RPLCB.git",
        "local_path": os.path.join(CONTIKI_EXAMPLES, "projet_madani/RPLMQoS_BELACEL"),
        "pattern_git_clone": r"git clone https://github\.com/madani-belacel/RPLCB\.git",
    },
    "AER-RPL": {
        "github_url": "https://github.com/madani-belacel/RPL-AER.git",
        "local_path": os.path.join(CONTIKI_EXAMPLES, "projet_madani/RPL-AER-main"),
        "pattern_git_clone": r"git clone https://github\.com/madani-belacel/RPL-AER\.git",
    },
    "AER-MQoS": {
        "github_url": "https://github.com/madani-belacel/AER-MQoS.git",
        "local_path": os.path.join(CONTIKI_EXAMPLES, "AER-MQoS"),
        "pattern_git_clone": r"git clone https://github\.com/madani-belacel/AER-MQoS\.git",
    },
    "IDS-IOT": {
        "github_url": "https://github.com/madani-belacel/IDS-IOT.git",
        "local_path": os.path.join(CONTIKI_EXAMPLES, "IDS_IOT"),
        "pattern_git_clone": r"git clone https://github\.com/madani-belacel/IDS-IOT\.git",
    },
}

def update_rplmqos_paths(content, local_path):
    """Remplacer les chemins GitHub par des chemins locaux pour RPLMQOS."""
    # Remplacer les commandes git clone par une mention du chemin local + optionnel git
    content = re.sub(
        r'git clone https://github\.com/madani-belacel/RPLCB\.git',
        '# Les codes sont déjà présents localement\n# Si nécessaire, cloner depuis GitHub:\n# git clone https://github.com/madani-belacel/RPLCB.git',
        content
    )
    content = re.sub(
        r'cd RPLCB',
        f'# Aller dans le dossier des codes locaux\ncd {local_path}',
        content
    )
    content = re.sub(
        r'projet-RPLCB/',
        f'{local_path}/',
        content
    )
    # Ajouter une note locale après les sections de clonage
    content = re.sub(
        r'(<h2>1\. Cloner le dépôt</h2>.*?</pre>)',
        lambda m: m.group(1) + LOCAL_NOTE.format(local_path),
        content,
        flags=re.DOTALL
    )
    return content

def update_aer_paths(content, local_path):
    """Remplacer les chemins GitHub par des chemins locaux pour AER-RPL."""
    content = re.sub(
        r'git clone https://github\.com/madani-belacel/RPL-AER\.git',
        '# Les codes sont déjà présents localement\n# Si nécessaire, cloner depuis GitHub:\n# git clone https://github.com/madani-belacel/RPL-AER.git',
        content
    )
    content = content.replace('cd RPL-AER', f'cd {local_path}')
    # Ajouter une note locale
    content = re.sub(
        r'(<h2>1\. Cloner le dépôt GitHub</h2>.*?</code></pre>)',
        lambda m: m.group(1) + LOCAL_NOTE.format(local_path),
        content,
        flags=re.DOTALL
    )
    return content

def update_aermqos_paths(content, local_path):
    """Remplacer les chemins GitHub par des chemins locaux pour AER-MQoS."""
    content = re.sub(
        r'git clone https://github\.com/madani-belacel/AER-MQoS\.git',
        '# Les codes sont déjà présents localement\n# Si nécessaire, cloner depuis GitHub:\n# git clone https://github.com/madani-belacel/AER-MQoS.git',
        content
    )
    content = content.replace('cd AER-MQoS', f'cd {local_path}')
    content = re.sub(
        r'(<h2>1\. Cloner le dépôt</h2>.*?</code></pre>)',
        lambda m: m.group(1) + LOCAL_NOTE.format(local_path),
        content,
        flags=re.DOTALL
    )
    return content

def update_ids_paths(content, local_path):
    """Remplacer les chemins GitHub par des chemins locaux pour IDS-IOT."""
    content = re.sub(
        r'git clone https://github\.com/madani-belacel/IDS-IOT\.git',
        '# Les codes sont déjà présents localement\n# Si nécessaire, cloner depuis GitHub:\n# git clone https://github.com/madani-belacel/IDS-IOT.git',
        content
    )
    content = content.replace('cd IDS-IOT', f'cd {local_path}')
    content = re.sub(
        r'(<h2>1\. Cloner le dépôt</h2>.*?</code></pre>)',
        lambda m: m.group(1) + LOCAL_NOTE.format(local_path),
        content,
        flags=re.DOTALL
    )
    return content

# Update all files in each subfolder
for folder, info in CHANGES.items():
    folder_path = os.path.join(BASE, folder)
    if not os.path.isdir(folder_path):
        print(f"Dossier introuvable : {folder_path}")
        continue
    
    html_files = glob.glob(os.path.join(folder_path, "*.html"))
    print(f"Traitement de {folder} ({len(html_files)} fichiers)...")
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        if folder == "RPLMQOS":
            content = update_rplmqos_paths(content, info["local_path"])
        elif folder == "AER-RPL":
            content = update_aer_paths(content, info["local_path"])
        elif folder == "AER-MQoS":
            content = update_aermqos_paths(content, info["local_path"])
        elif folder == "IDS-IOT":
            content = update_ids_paths(content, info["local_path"])
        
        # Common replacements
        content = content.replace('href="https://github.com/madani-belacel/RPLCB"', 'href="file://' + os.path.join(CONTIKI_EXAMPLES, "projet_madani/RPLMQoS_BELACEL") + '"')
        
        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  + Modifié : {os.path.basename(filepath)}")
    
    print(f"  ✓ {folder} terminé")

# Update Base_Cooja_RPL_IOT for Contiki-NG paths
base_path = os.path.join(BASE, "Base_Cooja_RPL_IOT")
if os.path.isdir(base_path):
    html_files = glob.glob(os.path.join(base_path, "*.html"))
    print(f"\nTraitement de Base_Cooja_RPL_IOT ({len(html_files)} fichiers)...")
    
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Ajouter la note sur l'environnement local Contiki-NG
        contiki_note = '''
<div class="md-meta" style="background:#e8f5e9;border-color:#2e7d32;">
<strong>💻 Environnement local</strong>
<ul>
<li><strong>Contiki-NG installé dans :</strong> <code>/home/madani/contiki-ng/</code></li>
<li><strong>Exemples additionnels dans :</strong> <code>/home/madani/contiki-ng/examples/</code></li>
<li><strong>Protocoles de recherche dans :</strong>
<ul>
<li>RPLMQOS → <code>examples/projet_madani/RPLMQoS_BELACEL/</code></li>
<li>RPL-AER → <code>examples/projet_madani/RPL-AER-main/</code></li>
<li>AER-MQoS → <code>examples/AER-MQoS/</code></li>
<li>IDS-IOT → <code>examples/IDS_IOT/</code></li>
</ul>
</li>
</ul>
</div>'''
        
        # Ajouter la note après le breadcrumb
        content = content.replace(
            '</nav>',
            '</nav>\n' + contiki_note
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  + Modifié : {os.path.basename(filepath)}")

print("\n✅ Mise à jour terminée !")
