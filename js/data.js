/**
 * BELACEL Madani — Données des cours
 * Structure centralisée pour génération dynamique des pages
 */

const COURSES_DATA = {
  tic: {
    name: "Module TIC",
    icon: "\uD83D\uDCBB",
    description: "Technologies de l'Information et de la Communication — cours, TD et TP pour tous niveaux",
    levels: {
      "Série Officielle": {
        path: "serie-officielle",
        courses: ["Cours_TIC_01", "Cours_TIC_02", "Cours_TIC_03", "Cours_TIC_04", "Cours_TIC_05",
                  "Cours_TIC_06", "Cours_TIC_07", "Cours_TIC_08", "Cours_TIC_09", "Cours_TIC_10"],
        tds: ["TD_TIC_01", "TD_TIC_02", "TD_TIC_03", "TD_TIC_04", "TD_TIC_05",
              "TD_TIC_06", "TD_TIC_07", "TD_TIC_08", "TD_TIC_09", "TD_TIC_10"]
      },
      "Département Français (7 niveaux)": {
        path: "departement-francais",
        sublevels: ["Licence 1", "Licence 2", "ENS 1ère année", "ENS 2ème année",
                    "Master 1 - DLE", "Master 1 - Langue et Culture", "Master 2 - DLE"]
      },
      "Département Anglais (7 niveaux)": {
        path: "departement-anglais",
        sublevels: ["Licence 1", "Licence 2", "ENS 1ère année", "ENS 2ème année",
                    "Master 1 - DLE", "Master 1 - Langue et Culture", "Master 2 - DLE"]
      }
    }
  },
  ens: {
    name: "Module Informatique ENS",
    icon: "\uD83D\uDCDA",
    description: "Informatique pour l'École Normale Supérieure — algorithmique, programmation, bases de données, Web",
    levels: {
      "ENS 1ère année (FR)": { path: "ens-1a-fr", count: "9 cours + 9 TD" },
      "ENS 1ère année (EN)": { path: "ens-1a-en", count: "9 cours + 9 TD" },
      "ENS 2ème année (FR)": { path: "ens-2a-fr", count: "9 cours + 9 TD" },
      "ENS 2ème année (EN)": { path: "ens-2a-en", count: "9 cours + 9 TD" }
    }
  },
  rd: {
    name: "Module Recherche Documentaire",
    icon: "\uD83D\uDD0D",
    description: "Méthodologie de recherche documentaire — Zotero, APA 7, synthèse bibliographique",
    levels: {
      "M2 DLE – Français": { path: "m2-dle-fr", count: "10 cours" },
      "M2 DLE – Anglais": { path: "m2-dle-en", count: "10 cours" }
    }
  },
  reseaux: {
    name: "Module Réseaux Mostaganem",
    icon: "\uD83C\uDF10",
    description: "Réseaux informatiques — ISIL-S4, SI-S5, Ingénieur, Master RSID",
    levels: {
      "ISIL-S4": { path: "isil-s4", count: "8 cours + 8 TD + 6 TP" },
      "SI-S5": { path: "si-s5", count: "9 cours + 9 TD + 7 TP" },
      "Ingénieur S5→S9": { path: "ingenieur", count: "20+ cours/TD/TP" },
      "Master RSID M1-S1": { path: "rsid-m1s1", count: "4 cours + 2 TD + 1 TP" },
      "Master RSID M1-S2": { path: "rsid-m1s2", count: "4 cours + 2 TD + 1 TP" },
      "Master RSID M2": { path: "rsid-m2", count: "4 cours + 2 TD + 1 TP" }
    }
  }
};

const NEWS_DATA = [
  {
    date: "Juin 2026",
    title: "Finalisation des supports pour l'habilitation universitaire",
    desc: "L'ensemble des cours, TD et TP des 4 modules (TIC, ENS, Recherche Doc, Réseaux) a été révisé et enrichi."
  },
  {
    date: "Juin 2026",
    title: "18 cours ENS FR réécrits",
    desc: "Contenu CS réel (algo, Python, POO, BD, Web, Git, Scratch, projet) pour ENS 1ère et 2ème année."
  },
  {
    date: "Juin 2026",
    title: "10 cours Recherche Documentaire enrichis",
    desc: "Passage de ~30 à ~150 lignes avec contenu pédagogique complet (problématique, Zotero, APA 7, synthèse)."
  },
  {
    date: "Juin 2026",
    title: "Variantes TIC par niveau créées",
    desc: "14 variantes (7 FR + 7 EN) de Cours_TIC_01 adaptées par niveau : Licence, ENS, Master."
  },
  {
    date: "Mai 2026",
    title: "Audit zéro anomalie terminé",
    desc: "Audit exhaustif de ~1200 fichiers avec 4 rapports de revue pédagogique."
  }
];

const RESEARCH_DATA = {
  thesis: {
    title: "Thèse de Doctorat",
    topic: "Sécurité des réseaux et Cloud Computing",
    keywords: ["SDN", "Cloud Security", "Zero Trust", "Network Automation"],
    year: "2024"
  },
  publications: [
    { title: "Titre de publication 1", journal: "Revue / Conférence", year: "2023" },
    { title: "Titre de publication 2", journal: "Revue / Conférence", year: "2024" }
  ],
  projects: [
    { title: "Projet de recherche 1", description: "Description du projet", status: "En cours" }
  ],
  supervisions: [
    { student: "Étudiant 1", level: "Master", topic: "Sujet de mémoire", year: "2025-2026" }
  ]
};
