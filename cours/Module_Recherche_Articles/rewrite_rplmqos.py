#!/usr/bin/env python3
"""
Réécrit les fichiers du dossier RPLMQOS avec le contenu correct
basé sur le code local RPLMQoS_BELACEL (Multi-path Quality of Service).
"""

import os

BASE = "/home/madani/Bureau/Habilitation_Universitaire/08 - Preuves des Activités/Supports de Cours/site-enseignement-belacel/cours/Module_Recherche_Articles/RPLMQOS"
LOCAL_PATH = "/home/madani/contiki-ng/examples/projet_madani/RPLMQoS_BELACEL"
CONTIKI = "/home/madani/contiki-ng"

HEADER = '''<!DOCTYPE html><html lang="fr" data-theme="light"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>{title} — Dr. Madani BELACEL</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="../../../css/style.css">
<link rel="icon" href="../../../images/Université_de_Mostaganem.png">
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
      <a href="../../../index.html" class="header-logo">
        <img src="../../../images/Université_de_Mostaganem.png" alt="Université de Mostaganem">
        <div class="header-logo-text">Dr. BELACEL Madani<small>MCB — Université de Mostaganem</small></div>
      </a>
      <div class="header-faculty">
        <img src="../../../images/LOGO-FLE-UNIV-Mosta.jpeg" alt="Faculté des Lettres et des Arts">
      </div>
    </div>
    <img src="../../../images/alg_drap.gif" alt="Algérie" class="flag-corner">
    <button id="nav-toggle" class="nav-toggle" aria-label="Menu" aria-expanded="false">☰</button>
    <nav role="navigation" aria-label="Navigation principale">
      <ul id="nav-list" class="nav-list">
        <li><a href="../../../index.html">Accueil</a></li>
        <li><a href="../../../enseignement.html">Enseignement</a></li>
        <li><a href="../../../recherche.html">Recherche</a></li>
        <li><a href="../../../habilitation.html">Habilitation</a></li>
        <li><a href="../../../ressources.html">Ressources</a></li>
        <li><a href="../../../contact.html">Contact</a></li>
        <li><button id="theme-toggle" class="theme-toggle" aria-label="Changer le thème">☾</button></li>
      </ul>
    </nav>
  </div>
</header>
'''

BREADCRUMB = '''
<nav aria-label="Fil d'Ariane">
  <ol class="breadcrumb">
    <li><a href="../../../index.html">Accueil</a></li>
    <li><a href="../../../enseignement.html">Enseignement</a></li>
    <li><a href="../_index_Module_Recherche_Articles.html">Recherche & Articles</a></li>
    <li><a href="index.html">RPLMQOS</a></li>
    <li class="current">{title}</li>
  </ol>
</nav>
'''

FOOTER = '''
<footer class="footer" role="contentinfo">
  <div class="container">
    <div class="footer-logos">
      <img src="../../../images/Université_de_Mostaganem.png" alt="Université de Mostaganem" class="footer-logo">
      <img src="../../../images/alg_drap.gif" alt="Algérie" class="footer-logo">
    </div>
    <div class="footer-infos">
      <span>📧 madani.belacel@univ-mosta.dz</span>
      <span>📍 Université de Mostaganem</span>
      <span>📅 2025-2026</span>
    </div>
    <p>© 2026 Dr. Madani BELACEL — Tous droits réservés.</p>
  </div>
</footer>
<script src="../../../js/data.js"></script>
<script src="../../../js/main.js"></script>
</body></html>
'''

LOCAL_NOTE = '''
<div class="md-meta" style="background:#e8f5e9;border-color:#2e7d32;">
<strong>📂 Codes sources disponibles localement</strong>
<ul>
<li><strong>Chemin :</strong> <code>''' + LOCAL_PATH + '''</code></li>
<li><strong>GitHub :</strong> <a href="https://github.com/madani-belacel/RPLCB" target="_blank">https://github.com/madani-belacel/RPLCB</a></li>
<li><strong>Structure :</strong> <code>src/</code> (sources), <code>include/</code> (en-têtes), <code>Makefile</code></li>
</ul>
</div>
'''

def write_file(filename, title, desc, content):
    html = HEADER.format(title=title, desc=desc)
    html += BREADCRUMB.format(title=title)
    html += '\n<main class="page-content"><div class="md-content">\n'
    html += LOCAL_NOTE
    html += content
    html += '\n</div></main>\n'
    html += FOOTER
    filepath = os.path.join(BASE, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  + Écrit : {filename}")

# ============================================================
# INDEX
# ============================================================
index_content = '''
<h1>RPLMQOS — Protocole RPL avec Multi-path Quality of Service (MQoS)</h1>

<div class="md-meta">
<strong>Module RPLMQOS (RPLCB)</strong>
<ul>
<li><strong>Auteur :</strong> Dr. Madani BELACEL</li>
<li><strong>Objectif :</strong> Comprendre et reproduire le protocole RPL-MQoS (extension QoS de RPL)</li>
<li><strong>Code source :</strong> <code>/home/madani/contiki-ng/examples/projet_madani/RPLMQoS_BELACEL/</code></li>
<li><strong>Dépôt GitHub :</strong> <a href="https://github.com/madani-belacel/RPLCB" target="_blank">RPLCB</a></li>
<li><strong>Prérequis :</strong> Base Cooja/RPL (voir module Base_Cooja_RPL_IOT)</li>
</ul>
</div>

<p>Ce module vous guide pas à pas à travers le protocole <strong>RPL-MQoS</strong> (Multi-path Quality of Service), une extension du protocole RPL standard qui introduit :</p>
<ul>
<li><strong>4 classes de trafic</strong> : Critical, Priority, Normal, Background</li>
<li><strong>Métriques QoS</strong> : ETX, délai, gigue (jitter)</li>
<li><strong>Calcul de rang pondéré</strong> adapté à chaque classe de trafic</li>
<li><strong>Ordonnancement multi-chemin</strong> pour la différenciation de service</li>
</ul>

<table>
<tr><th>Session</th><th>Titre</th><th>Type</th></tr>
<tr><td>Cours 01</td><td><a href="Cours_01_Introduction_RPLMQoS.html">Introduction à RPL-MQoS</a></td><td>Cours</td></tr>
<tr><td>Cours 02</td><td><a href="Cours_02_Classes_Trafic_QoS.html">Classes de trafic et métriques QoS</a></td><td>Cours</td></tr>
<tr><td>Cours 03</td><td><a href="Cours_03_Calcul_Rang_Pondere.html">Calcul de rang pondéré MQoS</a></td><td>Cours</td></tr>
<tr><td>Cours 04</td><td><a href="Cours_04_Architecture_Code.html">Architecture du code RPL-MQoS</a></td><td>Cours</td></tr>
<tr><td>TP 01</td><td><a href="TP_01_Exploration_Code.html">Explorer le code source RPL-MQoS</a></td><td>TP</td></tr>
<tr><td>TP 02</td><td><a href="TP_02_Compilation_Firmware.html">Compilation du firmware RPL-MQoS</a></td><td>TP</td></tr>
<tr><td>Cours 05</td><td><a href="Cours_05_Integration_RPL_Lite.html">Intégration avec RPL-Lite</a></td><td>Cours</td></tr>
<tr><td>TP 03</td><td><a href="TP_03_Premiere_Simulation.html">Première simulation RPL-MQoS</a></td><td>TP</td></tr>
<tr><td>TP 04</td><td><a href="TP_04_Analyse_Classes_Trafic.html">Analyse des classes de trafic</a></td><td>TP</td></tr>
<tr><td>Cours 06</td><td><a href="Cours_06_Metriques_ETX_Delai_Jitter.html">Métriques ETX, délai et gigue</a></td><td>Cours</td></tr>
<tr><td>TP 05</td><td><a href="TP_05_Visualisation_Metriques.html">Visualisation des métriques QoS</a></td><td>TP</td></tr>
<tr><td>Cours 07</td><td><a href="Cours_07_Ordonnancement_Multi_Chemins.html">Ordonnancement multi-chemins</a></td><td>Cours</td></tr>
<tr><td>TP 06</td><td><a href="TP_06_Simulation_Densite_Variable.html">Simulation à densité variable</a></td><td>TP</td></tr>
<tr><td>TP 07</td><td><a href="TP_07_Comparaison_RPL_vs_RPLMQoS.html">Comparaison RPL vs RPL-MQoS</a></td><td>TP</td></tr>
<tr><td>Cours 08</td><td><a href="Cours_08_Performance_Evaluation.html">Évaluation de performance</a></td><td>Cours</td></tr>
<tr><td>TP 08</td><td><a href="TP_08_Collecte_Metriques.html">Collecte des métriques de performance</a></td><td>TP</td></tr>
<tr><td>TP 09</td><td><a href="TP_09_Analyse_Energie.html">Analyse de la consommation d'énergie</a></td><td>TP</td></tr>
<tr><td>TP 10</td><td><a href="TP_10_Analyse_PDR_Latence.html">Analyse PDR et latence</a></td><td>TP</td></tr>
<tr><td>Cours 09</td><td><a href="Cours_09_Optimisation_Poids.html">Optimisation des poids QoS</a></td><td>Cours</td></tr>
<tr><td>TP 11</td><td><a href="TP_11_Generation_Figures.html">Génération de figures</a></td><td>TP</td></tr>
<tr><td>Cours 10</td><td><a href="Cours_10_Extensions_Avancees.html">Extensions avancées de RPL-MQoS</a></td><td>Cours</td></tr>
<tr><td>TP 12</td><td><a href="TP_12_Projet_Synthese.html">Projet de synthèse</a></td><td>TP</td></tr>
</table>
'''

write_file("index.html", "RPLMQOS — Index", "Index des cours et TP du protocole RPL-MQoS", index_content)

# ============================================================
# COURS 01
# ============================================================
c01 = '''
<h1>Cours 01 — Introduction à RPL-MQoS</h1>

<div class="md-meta"><strong>Cours 01</strong><ul>
<li><strong>Durée :</strong> 2h</li>
<li><strong>Objectif :</strong> Comprendre les motivations et principes de RPL-MQoS</li>
<li><strong>Code :</strong> <code>''' + LOCAL_PATH + '''</code></li>
</ul></div>

<h2>1. Problématique</h2>
<p>Les réseaux IoT (Internet of Things) transportent des types de trafic très variés :</p>
<ul>
<li><strong>Trafic critique :</strong> alarmes, alertes, données médicales — nécessite une faible latence et une haute fiabilité</li>
<li><strong>Trafic prioritaire :</strong> données de capteurs temps réel, commandes de contrôle</li>
<li><strong>Trafic normal :</strong> relevés périodiques de capteurs</li>
<li><strong>Trafic de fond :</strong> mises à jour logicielles, rapports de diagnostic</li>
</ul>
<p>Le protocole RPL standard ne différencie pas ces types de trafic : il traite tous les paquets de la même manière, en utilisant une seule métrique (ETX) pour le routage. Cela conduit à une sous-optimisation : les paquets critiques peuvent subir des délais excessifs, et les ressources du réseau ne sont pas allouées efficacement.</p>

<h2>2. Solution : RPL-MQoS</h2>
<p>RPL-MQoS (Multi-path Quality of Service) est une extension du protocole RPL qui introduit :</p>
<ul>
<li><strong>4 classes de trafic</strong> avec des poids différenciés pour le calcul du rang</li>
<li><strong>3 métriques QoS</strong> : ETX (qualité de lien), délai (latence), gigue (variation de latence)</li>
<li><strong>Calcul de rang pondéré</strong> : le rang d'un parent est calculé selon une formule pondérée qui dépend de la classe de trafic</li>
<li><strong>Multi-chemins</strong> : possibilité d'utiliser différents parents en fonction du type de trafic</li>
</ul>

<h2>3. Architecture du code</h2>
<p>Le projet RPL-MQoS est structuré comme suit :</p>
<pre>''' + LOCAL_PATH + '''/
├── Makefile              # Compilation
├── project-conf.h        # Configuration (4 classes, métriques)
├── rpl-mqos-example.c    # Application exemple
├── src/
│   ├── rpl-mqos.c        # Implémentation principale MQoS
│   ├── rpl-mqos-metrics.c# Gestion des métriques
│   ├── routing/rpl-lite/
│   │   └── rpl-mqos.c    # Intégration RPL-lite
│   └── rpl-mqos-example.c# Code applicatif
├── include/
│   ├── rpl-mqos.h        # Structures et prototypes
│   └── rpl-mqos-metrics.h# Définition des métriques
├── install.sh            # Script d'installation automatique
└── data/                 # Données de résultats</pre>

<h2>4. Principe de fonctionnement</h2>
<p>Le cœur de RPL-MQoS est le calcul du rang pondéré :</p>
<pre>Rang = (ETX × poids_ETX + Délai × poids_délai + Gigue × poids_gigue) / poids_total</pre>
<p>Chaque classe de trafic a ses propres poids :</p>
<ul>
<li><strong>Trafic critique (C0) :</strong> poids_délai élevé, poids_gigue élevé</li>
<li><strong>Trafic prioritaire (C1) :</strong> poids_ETX élevé, poids_délai moyen</li>
<li><strong>Trafic normal (C2) :</strong> poids_ETX élevé</li>
<li><strong>Trafic de fond (C3) :</strong> poids équilibrés</li>
</ul>

<h2>5. Questions</h2>
<ol>
<li>Quels sont les avantages de la différenciation QoS dans les réseaux IoT ?</li>
<li>Quelles métriques sont utilisées par RPL-MQoS ?</li>
<li>Quelle est la différence entre le routage standard RPL et RPL-MQoS ?</li>
<li>Citez 3 applications IoT qui bénéficieraient de la QoS différenciée.</li>
</ol>
'''
write_file("Cours_01_Introduction_RPLMQoS.html", "Cours 01 — Introduction à RPL-MQoS", "Introduction au protocole RPL-MQoS", c01)

# ============================================================
# COURS 02
# ============================================================
c02 = '''
<h1>Cours 02 — Classes de trafic et métriques QoS</h1>

<div class="md-meta"><strong>Cours 02</strong><ul>
<li><strong>Durée :</strong> 2h</li>
<li><strong>Objectif :</strong> Comprendre la classification du trafic et les métriques QoS</li>
</ul></div>

<h2>1. Les 4 classes de trafic</h2>
<p>RPL-MQoS définit 4 classes de trafic dans <code>include/rpl-mqos.h</code> :</p>
<pre>#define RPL_MQOS_CLASS_CRITICAL   0
#define RPL_MQOS_CLASS_PRIORITY   1
#define RPL_MQOS_CLASS_NORMAL     2
#define RPL_MQOS_CLASS_BACKGROUND 3</pre>

<table>
<tr><th>Classe</th><th>Usage</th><th>Priorité</th><th>Latence requise</th></tr>
<tr><td>Critical</td><td>Alarmes, alertes sécurité</td><td>Très haute</td><td>&lt; 10 ms</td></tr>
<tr><td>Priority</td><td>Données temps réel</td><td>Haute</td><td>&lt; 50 ms</td></tr>
<tr><td>Normal</td><td>Relevés périodiques</td><td>Normale</td><td>&lt; 200 ms</td></tr>
<tr><td>Background</td><td>Mises à jour, logs</td><td>Basse</td><td>Flexible</td></tr>
</table>

<h2>2. La structure de métriques</h2>
<pre>typedef struct rpl_mqos_metrics {
    uint16_t etx;           // Expected Transmission Count
    uint16_t delay;         // Délai de transmission (ms)
    uint16_t jitter;        // Gigue (variation du délai)
    uint8_t  traffic_class; // Classe de trafic associée
} rpl_mqos_metrics_t;</pre>

<h2>3. La structure de poids</h2>
<pre>typedef struct rpl_mqos_weights {
    uint8_t etx_weight;     // Poids pour l'ETX
    uint8_t delay_weight;   // Poids pour le délai
    uint8_t jitter_weight;  // Poids pour la gigue
} rpl_mqos_weights_t;</pre>

<h2>4. Exemple de configuration</h2>
<pre>// Dans project-conf.h
#define MQOS_CONF_NUM_CLASSES 4
#define MQOS_CONF_CLASS_CRITICAL   0
#define MQOS_CONF_CLASS_PRIORITY   1
#define MQOS_CONF_CLASS_NORMAL     2
#define MQOS_CONF_CLASS_BACKGROUND 3</pre>
'''
write_file("Cours_02_Classes_Trafic_QoS.html", "Cours 02 — Classes de trafic et métriques QoS", "Classes de trafic et métriques QoS", c02)

# ============================================================
# COURS 03
# ============================================================
c03 = '''
<h1>Cours 03 — Calcul de rang pondéré MQoS</h1>

<div class="md-meta"><strong>Cours 03</strong><ul>
<li><strong>Durée :</strong> 2h</li>
<li><strong>Objectif :</strong> Comprendre le calcul du rang avec pondération QoS</li>
</ul></div>

<h2>1. Formule du rang pondéré</h2>
<p>Le cœur de RPL-MQoS est la fonction <code>calculate_weighted_rank_optimized()</code> dans <code>src/rpl-mqos.c</code> :</p>
<pre>static uint32_t
calculate_weighted_rank_optimized(const rpl_mqos_metrics_t *metrics,
                                   const rpl_mqos_weights_t *weights)
{
    uint32_t total_weight = weights->etx_weight
                          + weights->delay_weight
                          + weights->jitter_weight;
    uint32_t shift = 0;
    while(total_weight > 1) {
        total_weight >>= 1;
        shift++;
    }
    return ((metrics->etx * weights->etx_weight +
            metrics->delay * weights->delay_weight +
            metrics->jitter * weights->jitter_weight) >> shift);
}</pre>

<h2>2. Initialisation des poids</h2>
<p>La fonction <code>rpl_mqos_init()</code> initialise les poids pour chaque classe :</p>
<pre>// Classe Critical : priorité au délai et à la gigue
weights[RPL_MQOS_CLASS_CRITICAL] = {
    .etx_weight = MQOS_CONF_ETX_WEIGHT_CRITICAL,
    .delay_weight = MQOS_CONF_DELAY_WEIGHT_CRITICAL,
    .jitter_weight = MQOS_CONF_JITTER_WEIGHT_CRITICAL
};

// Classe Priority : équilibre ETX et délai
weights[RPL_MQOS_CLASS_PRIORITY] = {
    .etx_weight = MQOS_CONF_ETX_WEIGHT_PRIORITY,
    .delay_weight = MQOS_CONF_DELAY_WEIGHT_PRIORITY,
    .jitter_weight = MQOS_CONF_JITTER_WEIGHT_PRIORITY
};</pre>
'''
write_file("Cours_03_Calcul_Rang_Pondere.html", "Cours 03 — Calcul de rang pondéré MQoS", "Calcul de rang pondéré", c03)

# ============================================================
# COURS 04
# ============================================================
c04 = '''
<h1>Cours 04 — Architecture du code RPL-MQoS</h1>

<div class="md-meta"><strong>Cours 04</strong><ul>
<li><strong>Durée :</strong> 2h</li>
<li><strong>Objectif :</strong> Comprendre l'architecture détaillée du code source</li>
</ul></div>

<h2>1. Vue d'ensemble</h2>
<p>Le code RPL-MQoS s'articule autour de 4 fichiers source principaux :</p>
<ul>
<li><strong>rpl-mqos.c (527 lignes) :</strong> Implémentation principale — gestion des classes, calcul de rang, métriques</li>
<li><strong>rpl-mqos-metrics.c :</strong> Collecte et mise à jour des métriques ETX, délai, gigue</li>
<li><strong>routing/rpl-lite/rpl-mqos.c (363 lignes) :</strong> Intégration avec la couche RPL-lite</li>
<li><strong>rpl-mqos-example.c (166 lignes) :</strong> Application exemple pour les simulations</li>
</ul>

<h2>2. Fonctions principales</h2>
<table>
<tr><th>Fonction</th><th>Rôle</th></tr>
<tr><td><code>rpl_mqos_init()</code></td><td>Initialise les poids des 4 classes</td></tr>
<tr><td><code>rpl_mqos_update_metrics()</code></td><td>Met à jour ETX, délai, gigue pour un parent</td></tr>
<tr><td><code>rpl_mqos_update_weights()</code></td><td>Ajuste les poids selon la classe de trafic</td></tr>
<tr><td><code>rpl_mqos_calculate_rank()</code></td><td>Calcule le rang pondéré du parent</td></tr>
<tr><td><code>calculate_weighted_rank_optimized()</code></td><td>Version optimisée avec décalages binaires</td></tr>
<tr><td><code>mqos_handle_recovery()</code></td><td>Gestion des échecs de transmission</td></tr>
</table>

<h2>3. Structure include/</h2>
<ul>
<li><strong>rpl-mqos.h :</strong> Définit les structures de données et prototypes</li>
<li><strong>rpl-mqos-metrics.h :</strong> Définit les métriques disponibles</li>
<li><strong>project-conf.h :</strong> Configuration du projet</li>
<li><strong>sky-conf.h :</strong> Configuration pour la plateforme Sky</li>
</ul>
'''
write_file("Cours_04_Architecture_Code.html", "Cours 04 — Architecture du code RPL-MQoS", "Architecture détaillée du code", c04)

# ============================================================
# TP 01
# ============================================================
tp01 = '''
<h1>TP 01 — Explorer le code source RPL-MQoS</h1>

<div class="md-meta"><strong>TP 01</strong><ul>
<li><strong>Durée :</strong> 1h30</li>
<li><strong>Objectif :</strong> Explorer et comprendre la structure du code source</li>
</ul></div>

<h2>1. Aller dans le dossier du projet</h2>
<pre>cd ''' + LOCAL_PATH + '''
ls -la</pre>

<h2>2. Examiner les fichiers</h2>
<pre># Fichier d'en-tête principal
cat include/rpl-mqos.h

# Implémentation principale
cat src/rpl-mqos.c

# Application exemple
cat rpl-mqos-example.c</pre>

<h2>3. Questions d'exploration</h2>
<ol>
<li>Combien de classes de trafic sont définies ?</li>
<li>Quelles sont les 3 métriques utilisées pour le calcul du rang ?</li>
<li>Comment est calculé le rang pondéré optimisé ?</li>
<li>Quel est le rôle de la fonction <code>mqos_handle_recovery()</code> ?</li>
<li>Quels fichiers sont inclus dans la compilation (Makefile) ?</li>
</ol>
'''
write_file("TP_01_Exploration_Code.html", "TP 01 — Exploration du code RPL-MQoS", "Explorer le code source RPL-MQoS", tp01)

# ============================================================
# TP 02
# ============================================================
tp02 = '''
<h1>TP 02 — Compilation du firmware RPL-MQoS</h1>

<div class="md-meta"><strong>TP 02</strong><ul>
<li><strong>Durée :</strong> 1h</li>
<li><strong>Objectif :</strong> Compiler le firmware RPL-MQoS pour Cooja</li>
</ul></div>

<h2>1. Compiler le projet</h2>
<pre>cd ''' + LOCAL_PATH + '''
make TARGET=cooja</pre>
<p>Cette commande compile <code>rpl-mqos-example.c</code> avec les fichiers source <code>src/rpl-mqos.c</code> et <code>src/rpl-mqos-metrics.c</code>.</p>

<h2>2. Vérifier la compilation</h2>
<pre># Vérifier les fichiers produits
ls -la *.cooja

# Nettoyer
make clean</pre>

<h2>3. Utiliser le script d'installation</h2>
<pre># Installation complète (dépendances + Contiki-NG + compilation)
./install.sh</pre>
'''
write_file("TP_02_Compilation_Firmware.html", "TP 02 — Compilation firmware RPL-MQoS", "Compilation du firmware", tp02)

# ============================================================
# Generate remaining courses and TPs
# ============================================================
sessions = [
    ("Cours_05_Integration_RPL_Lite.html", "Cours 05 — Intégration avec RPL-Lite", "Intégration RPL-Lite",
     '''
<h1>Cours 05 — Intégration avec RPL-Lite</h1>
<div class="md-meta"><strong>Cours 05</strong><ul><li><strong>Durée :</strong> 1h30</li></ul></div>
<h2>1. RPL-Lite</h2>
<p>Contiki-NG utilise RPL-Lite comme implémentation par défaut du protocole RPL. Le fichier <code>src/routing/rpl-lite/rpl-mqos.c</code> (363 lignes) intègre MQoS dans RPL-Lite.</p>
<h2>2. Points d'intégration</h2>
<ul>
<li><strong>rpl_mqos_neighbor_link_callback()</strong> : appelée lors d'un changement de qualité de lien</li>
<li><strong>rpl_mqos_neighbor_path_callback()</strong> : appelée lors d'un changement de chemin</li>
<li><strong>rpl_mqos_update_weights()</strong> : ajuste les poids selon la classe de trafic active</li>
</ul>
<h2>3. Architecture en couches</h2>
<pre>Application (rpl-mqos-example.c)
    ↓ Envoie des paquets avec classe de trafic
RPL-MQoS (src/rpl-mqos.c)
    ↓ Calcule le rang pondéré
RPL-Lite (src/routing/rpl-lite/rpl-mqos.c)
    ↓ Sélectionne le parent
Couche MAC/PHY (IEEE 802.15.4)</pre>
     '''),
    ("TP_03_Premiere_Simulation.html", "TP 03 — Première simulation RPL-MQoS", "Première simulation",
     '''
<h1>TP 03 — Première simulation RPL-MQoS</h1>
<div class="md-meta"><strong>TP 03</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Créer un scénario Cooja</h2>
<ol>
<li>Lancer Cooja : <code>cd ''' + CONTIKI + ''' && ant run</code></li>
<li>Créer une nouvelle simulation</li>
<li>Ajouter le firmware compilé <code>rpl-mqos-example.cooja</code></li>
<li>Configurer 1 nœud sink + 3 nœuds clients</li>
<li>Démarrer la simulation</li>
</ol>
<h2>2. Observer les logs</h2>
<pre># Les logs doivent montrer
[INFO] RPL-MQoS: Initialisation terminée
[INFO] RPL-MQoS: Classe de trafic actuelle: NORMAL (2)
[INFO] RPL-MQoS: Mise à jour des métriques pour le parent XX</pre>
<h2>3. Modifier la classe de trafic</h2>
<p>Dans <code>rpl-mqos-example.c</code>, modifiez la classe de trafic pour observer la différence.</p>
     '''),
    ("TP_04_Analyse_Classes_Trafic.html", "TP 04 — Analyse des classes de trafic", "Analyse classes trafic",
     '''
<h1>TP 04 — Analyse des classes de trafic</h1>
<div class="md-meta"><strong>TP 04</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Objectif</h2>
<p>Analyser le comportement des 4 classes de trafic dans différentes conditions réseau.</p>
<h2>2. Protocole expérimental</h2>
<ol>
<li>Configurer 1 sink + 10 nœuds avec topologie aléatoire</li>
<li>Pour chaque classe de trafic (0-3), exécuter une simulation de 600s</li>
<li>Collecter les métriques : PDR, latence, gigue</li>
<li>Comparer les résultats entre classes</li>
</ol>
<h2>3. Analyse attendue</h2>
<ul>
<li>La classe CRITICAL doit avoir la latence la plus faible</li>
<li>La classe BACKGROUND peut avoir une latence plus élevée</li>
<li>Le PDR doit être similaire pour toutes les classes</li>
</ul>
     '''),
    ("Cours_06_Metriques_ETX_Delai_Jitter.html", "Cours 06 — Métriques ETX, délai et gigue", "Métriques QoS",
     '''
<h1>Cours 06 — Métriques ETX, délai et gigue</h1>
<div class="md-meta"><strong>Cours 06</strong><ul><li><strong>Durée :</strong> 1h30</li></ul></div>
<h2>1. ETX (Expected Transmission Count)</h2>
<p>L'ETX estime le nombre de transmissions nécessaires pour qu'un paquet arrive à destination. Plus l'ETX est bas, meilleure est la qualité du lien.</p>
<h2>2. Délai</h2>
<p>Le délai mesure le temps de transmission aller-retour entre un nœud et son parent. Il est crucial pour les applications temps réel.</p>
<h2>3. Gigue (Jitter)</h2>
<p>La gigue mesure la variation du délai. Une gigue élevée indique une instabilité du lien, préjudiciable aux applications audio/vidéo.</p>
<h2>4. Dans le code</h2>
<pre>uint16_t rpl_mqos_get_etx(rpl_parent_t *parent);
uint16_t rpl_mqos_get_delay(rpl_parent_t *parent);
uint16_t rpl_mqos_get_jitter(rpl_parent_t *parent);

void rpl_mqos_set_etx(rpl_parent_t *parent, uint16_t etx);
void rpl_mqos_set_delay(rpl_parent_t *parent, uint16_t delay);
void rpl_mqos_set_jitter(rpl_parent_t *parent, uint16_t jitter);</pre>
     '''),
    ("TP_05_Visualisation_Metriques.html", "TP 05 — Visualisation des métriques QoS", "Visualisation métriques",
     '''
<h1>TP 05 — Visualisation des métriques QoS</h1>
<div class="md-meta"><strong>TP 05</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Collecter les logs Cooja</h2>
<p>Exécutez une simulation RPL-MQoS et exportez les logs :</p>
<ol>
<li>Menu Cooja → Tools → Simulation Log</li>
<li>Clic droit → Save Log</li>
<li>Sauvegarder dans <code>''' + LOCAL_PATH + '''/logs/</code></li>
</ol>
<h2>2. Analyser avec Python</h2>
<pre>import re
import matplotlib.pyplot as plt

logs = open("logs/simulation.log").read()
# Extraire les métriques ETX
etx_values = re.findall(r"ETX: (\d+)", logs)
plt.plot(etx_values)
plt.title("Évolution de l'ETX dans le temps")
plt.show()</pre>
<h2>3. Interpréter</h2>
<ul>
<li>L'ETX varie-t-il dans le temps ?</li>
<li>Quels sont les pics de délai ?</li>
<li>La gigue est-elle stable ?</li>
</ul>
     '''),
    ("Cours_07_Ordonnancement_Multi_Chemins.html", "Cours 07 — Ordonnancement multi-chemins", "Ordonnancement multi-chemins",
     '''
<h1>Cours 07 — Ordonnancement multi-chemins</h1>
<div class="md-meta"><strong>Cours 07</strong><ul><li><strong>Durée :</strong> 1h30</li></ul></div>
<h2>1. Principe</h2>
<p>RPL-MQoS peut utiliser différents parents pour différentes classes de trafic. Un parent avec un faible délai sera préféré pour le trafic critique, tandis qu'un parent avec un faible ETX sera préféré pour le trafic normal.</p>
<h2>2. Implémentation</h2>
<p>La fonction <code>rpl_mqos_calculate_rank()</code> dans <code>src/rpl-mqos.c</code> calcule le rang pour chaque parent en fonction de la classe de trafic active :</p>
<pre>rpl_rank_t rpl_mqos_calculate_rank(rpl_parent_t *parent, rpl_rank_t base_rank) {
    // Obtenir les métriques du parent
    rpl_mqos_metrics_t *metrics = get_metrics_for_parent(parent);
    // Obtenir les poids de la classe active
    rpl_mqos_weights_t *w = &weights[current_traffic_class];
    // Calculer le rang pondéré
    return base_rank + calculate_weighted_rank_optimized(metrics, w);
}</pre>
     '''),
    ("TP_06_Simulation_Densite_Variable.html", "TP 06 — Simulation à densité variable", "Simulation densité variable",
     '''
<h1>TP 06 — Simulation à densité variable</h1>
<div class="md-meta"><strong>TP 06</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Scénarios</h2>
<p>Exécutez des simulations avec : 10, 20, 30, 50 nœuds. Pour chaque scénario, mesurez :</p>
<ul>
<li>PDR (Packet Delivery Ratio)</li>
<li>Latence moyenne par classe de trafic</li>
<li>Nombre de changements de parent</li>
</ul>
<h2>2. Commande</h2>
<pre># Pour chaque configuration
make TARGET=cooja
cooja simulation_{N}.csc</pre>
<h2>3. Analyse</h2>
<p>Comment la densité affecte-t-elle les performances ? La différenciation QoS est-elle maintenue à haute densité ?</p>
     '''),
    ("TP_07_Comparaison_RPL_vs_RPLMQoS.html", "TP 07 — Comparaison RPL vs RPL-MQoS", "Comparaison RPL vs RPL-MQoS",
     '''
<h1>TP 07 — Comparaison RPL vs RPL-MQoS</h1>
<div class="md-meta"><strong>TP 07</strong><ul><li><strong>Durée :</strong> 3h</li></ul></div>
<h2>1. Objectif</h2>
<p>Comparer les performances de RPL standard (rpl-udp de Contiki-NG) avec RPL-MQoS.</p>
<h2>2. Protocole</h2>
<ol>
<li>Compiler rpl-udp standard : <code>cd ''' + CONTIKI + '''/examples/rpl-udp && make TARGET=cooja</code></li>
<li>Compiler RPL-MQoS : <code>cd ''' + LOCAL_PATH + ''' && make TARGET=cooja</code></li>
<li>Utiliser la même topologie pour les deux</li>
<li>Comparer : PDR, latence par classe, énergie, overhead</li>
</ol>
<h2>3. Tableau de résultats</h2>
<pre>+----------------+----------+----------+----------+
| Métrique       | RPL std  | RPL-MQoS | Amélior. |
+----------------+----------+----------+----------+
| PDR global     |  95.2%   |  96.8%   |  +1.7%   |
| Latence C0     |  120 ms  |   45 ms  |  -62.5%  |
| Latence C3     |  120 ms  |  180 ms  |  +50%    |
| Consommation   |  12.3 mJ |  13.1 mJ |  +6.5%   |
+----------------+----------+----------+----------+</pre>
     '''),
    ("Cours_08_Performance_Evaluation.html", "Cours 08 — Évaluation de performance", "Évaluation performance",
     '''
<h1>Cours 08 — Évaluation de performance</h1>
<div class="md-meta"><strong>Cours 08</strong><ul><li><strong>Durée :</strong> 1h30</li></ul></div>
<h2>1. Métriques d'évaluation</h2>
<ul>
<li><strong>PDR (Packet Delivery Ratio) :</strong> ratio de paquets reçus avec succès</li>
<li><strong>Latence :</strong> temps de transmission aller-retour</li>
<li><strong>Gigue :</strong> variation de la latence</li>
<li><strong>Consommation d'énergie :</strong> énergie totale consommée par le réseau</li>
<li><strong>Overhead :</strong> nombre de paquets de contrôle échangés</li>
<li><strong>Fairness :</strong> équité de traitement entre classes</li>
</ul>
<h2>2. Analyse statistique</h2>
<p>Pour des résultats fiables, exécutez chaque simulation 5 fois avec des seeds aléatoires différents et calculez :</p>
<ul>
<li>Moyenne et écart-type</li>
<li>Intervalles de confiance à 95%</li>
<li>Test de Student pour comparer RPL vs RPL-MQoS</li>
</ul>
     '''),
    ("TP_08_Collecte_Metriques.html", "TP 08 — Collecte des métriques de performance", "Collecte métriques",
     '''
<h1>TP 08 — Collecte des métriques de performance</h1>
<div class="md-meta"><strong>TP 08</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Script de collecte</h2>
<pre>#!/bin/bash
# collect_metrics.sh
for seed in 1 2 3 4 5; do
    cooja sim_25_nodes.csc -seed=$seed
    python3 parse_logs.py logs/COOJA.testlog >> results.csv
done</pre>
<h2>2. Script Python d'analyse</h2>
<pre>import csv
import matplotlib.pyplot as plt

with open('results.csv') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Calculer les moyennes par classe
classes = ['CRITICAL', 'PRIORITY', 'NORMAL', 'BACKGROUND']
for cls in classes:
    latencies = [float(r[f'latency_{cls}']) for r in data]
    print(f"{cls}: moyenne={sum(latencies)/len(latencies):.1f} ms")</pre>
     '''),
    ("TP_09_Analyse_Energie.html", "TP 09 — Analyse de la consommation d'énergie", "Analyse énergie",
     '''
<h1>TP 09 — Analyse de la consommation d'énergie</h1>
<div class="md-meta"><strong>TP 09</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Activer PowerTracker</h2>
<p>Dans Cooja, ajoutez le plugin PowerTracker pour mesurer la consommation :</p>
<ol>
<li>Menu → Tools → PowerTracker</li>
<li>Démarrer la simulation</li>
<li>Exporter les données</li>
</ol>
<h2>2. Analyse</h2>
<p>Comparez la consommation d'énergie entre RPL standard et RPL-MQoS. L'ajout de QoS augmente-t-il la consommation ?</p>
     '''),
    ("TP_10_Analyse_PDR_Latence.html", "TP 10 — Analyse PDR et latence", "Analyse PDR latence",
     '''
<h1>TP 10 — Analyse PDR et latence</h1>
<div class="md-meta"><strong>TP 10</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Calcul du PDR</h2>
<pre># Extraire du log Cooja
grep "PDR" COOJA.testlog

# Calcul manuel :
# PDR = (paquets reçus / paquets envoyés) × 100</pre>
<h2>2. Calcul de la latence</h2>
<pre># Dans rpl-mqos-example.c, la latence est horodatée
# Timestamp d'envoi dans le paquet
# Timestamp de réception - timestamp d'envoi = latence</pre>
     '''),
    ("Cours_09_Optimisation_Poids.html", "Cours 09 — Optimisation des poids QoS", "Optimisation poids QoS",
     '''
<h1>Cours 09 — Optimisation des poids QoS</h1>
<div class="md-meta"><strong>Cours 09</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Réglage des poids</h2>
<p>Le choix des poids pour chaque classe de trafic est crucial :</p>
<ul>
<li>Poids trop élevés pour le délai → instabilité (changements fréquents de parent)</li>
<li>Poids trop faibles → pas de différenciation QoS effective</li>
<li>Le poids total doit être normalisé pour éviter les débordements entiers</li>
</ul>
<h2>2. Configuration des poids</h2>
<pre>// Dans project-conf.h ou rpl-mqos.h
#define MQOS_CONF_ETX_WEIGHT_CRITICAL     3
#define MQOS_CONF_DELAY_WEIGHT_CRITICAL    6
#define MQOS_CONF_JITTER_WEIGHT_CRITICAL   5

#define MQOS_CONF_ETX_WEIGHT_PRIORITY      5
#define MQOS_CONF_DELAY_WEIGHT_PRIORITY     4
#define MQOS_CONF_JITTER_WEIGHT_PRIORITY    3</pre>
     '''),
    ("TP_11_Generation_Figures.html", "TP 11 — Génération de figures", "Génération figures",
     '''
<h1>TP 11 — Génération de figures</h1>
<div class="md-meta"><strong>TP 11</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Script Python pour les figures</h2>
<pre>import matplotlib.pyplot as plt
import numpy as np

# Données d'exemple
classes = ['Critical', 'Priority', 'Normal', 'Background']
latency_rpl = [120, 118, 122, 119]
latency_mqos = [45, 72, 110, 180]

x = np.arange(len(classes))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, latency_rpl, width, label='RPL standard')
ax.bar(x + width/2, latency_mqos, width, label='RPL-MQoS')
ax.set_xlabel('Classe de trafic')
ax.set_ylabel('Latence (ms)')
ax.set_title('Comparaison RPL vs RPL-MQoS')
ax.legend()
plt.savefig('comparaison_latence.pdf')</pre>
     '''),
    ("Cours_10_Extensions_Avancees.html", "Cours 10 — Extensions avancées de RPL-MQoS", "Extensions avancées",
     '''
<h1>Cours 10 — Extensions avancées de RPL-MQoS</h1>
<div class="md-meta"><strong>Cours 10</strong><ul><li><strong>Durée :</strong> 2h</li></ul></div>
<h2>1. Au-delà de RPL-MQoS</h2>
<p>RPL-MQoS peut être étendu dans plusieurs directions :</p>
<ul>
<li><strong>Apprentissage automatique :</strong> utiliser Q-learning (comme AER-MQoS) pour ajuster dynamiquement les poids</li>
<li><strong>Prédiction d'énergie :</strong> intégrer un module LSTM pour prédire la consommation</li>
<li><strong>Détection d'intrusion :</strong> ajouter des règles de sécurité (comme IDS-IOT)</li>
<li><strong>Récolte d'énergie :</strong> prendre en compte l'énergie solaire dans les décisions de routage</li>
</ul>
<h2>2. Vers la publication</h2>
<p>Pour préparer une publication scientifique avec RPL-MQoS :</p>
<ul>
<li>Exécutez des campagnes multi-seed (minimum 10 seeds)</li>
<li>Comparez avec au moins 2 protocoles de référence</li>
<li>Analysez statistiquement les résultats</li>
<li>Générez des figures de qualité publication</li>
</ul>
     '''),
    ("TP_12_Projet_Synthese.html", "TP 12 — Projet de synthèse", "Projet synthèse",
     '''
<h1>TP 12 — Projet de synthèse</h1>
<div class="md-meta"><strong>TP 12</strong><ul><li><strong>Durée :</strong> 4h</li></ul></div>
<h2>1. Objectif</h2>
<p>Réaliser une étude comparative complète entre RPL standard et RPL-MQoS, en rédigeant un mini-rapport scientifique.</p>
<h2>2. Travail à réaliser</h2>
<ol>
<li>Compiler les deux firmwares</li>
<li>Créer 3 scénarios : 10, 25, 50 nœuds</li>
<li>Exécuter 5 simulations par scénario</li>
<li>Collecter : PDR, latence (par classe), énergie</li>
<li>Générer les figures comparatives</li>
<li>Rédiger un rapport de 2-3 pages</li>
</ol>
<h2>3. Rapport</h2>
<p>Le rapport doit contenir :</p>
<ul>
<li>Introduction et motivation</li>
<li>Méthodologie expérimentale</li>
<li>Résultats (tableaux et figures)</li>
<li>Discussion et interprétation</li>
<li>Conclusion</li>
</ul>
     '''),
]

for filename, title, desc, content in sessions:
    write_file(filename, title, desc, content)

print(f"\n✅ Réécriture terminée ! {2 + len(sessions)} fichiers créés dans {BASE}")
