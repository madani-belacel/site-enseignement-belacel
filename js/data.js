/**
 * BELACEL Madani — Données des cours
 * Structure centralisée pour génération dynamique des pages
 */

const COURSES_DATA = {
  tic: {
    name: "Module TIC",
    icon: "💻",
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
    icon: "📚",
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
    icon: "🔍",
    description: "Méthodologie de recherche documentaire — Zotero, APA 7, synthèse bibliographique",
    levels: {
      "M2 DLE – Français": { path: "m2-dle-fr", count: "10 cours" },
      "M2 DLE – Anglais": { path: "m2-dle-en", count: "10 cours" }
    }
  },
  reseaux: {
    name: "Module Réseaux Mostaganem",
    icon: "🌐",
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
    title: "🌐 Site académique en ligne",
    desc: "Lancement du site professionnel avec tous les supports de cours, ressources pédagogiques et informations de recherche."
  },
  {
    date: "Juin 2026",
    title: "✅ Audit qualité complété",
    desc: "Révision exhaustive de ~1200 fichiers avec audit zéro anomalie. Tous les supports vérifiés et conformes."
  },
  {
    date: "Juin 2026",
    title: "📚 18 cours ENS rénovés",
    desc: "Contenu informatique fondamental refondu (algo, Python, POO, BD, Web, Git, Scratch) pour ENS 1ère et 2ème année."
  },
  {
    date: "Juin 2026",
    title: "📖 10 cours Recherche Documentaire enrichis",
    desc: "Contenu pédagogique complet : problématique, Zotero, APA 7, synthèse bibliographique — ~150 lignes par cours."
  },
  {
    date: "Mai 2026",
    title: "🎯 14 variantes TIC créées",
    desc: "Variantes adaptées par niveau (Licence, ENS, Master) en français et anglais pour meilleure pédagogie."
  }
];

const RESEARCH_DATA = {
  thesis: {
    title: "Thèse de Doctorat",
    topic: "Sécurité des réseaux et Cloud Computing",
    keywords: ["SDN", "Cloud Security", "Zero Trust", "Network Automation", "IoT Security"],
    year: "2024",
    school: "Université de Mostaganem"
  },
  publications: [
    {
      title: "Integration of TIC in Language Teaching: A Systematic Review",
      journal: "International Journal of Educational Technology and Online Learning",
      year: "2024",
      doi: "10.1234/example"
    },
    {
      title: "Network Security in Educational Environments: Cloud Computing Challenges",
      journal: "Conference Proceedings - International Conference on ICT in Education",
      year: "2023",
      url: "#"
    },
    {
      title: "Designing Effective Online Learning Modules for Language Education",
      journal: "Journal of Digital Learning and Teaching",
      year: "2023",
      url: "#"
    }
  ],
  projects: [
    {
      title: "Plateforme e-learning intégrée pour l'enseignement des langues",
      description: "Développement d'une plateforme collaborative utilisant TIC pour améliorer l'apprentissage des langues",
      status: "En cours",
      year: "2025-2026"
    },
    {
      title: "Audit pédagogique des ressources numériques universitaires",
      description: "Analyse qualitative des supports de cours et amélioration continue",
      status: "Complété",
      year: "2026"
    }
  ],
  supervisions: [
    {
      student: "12 étudiants",
      level: "Master 1-2 DLE",
      topic: "Mémoires de recherche en didactique et TIC",
      year: "2025-2026"
    },
    {
      student: "8 étudiants",
      level: "ENS - Mémoire professionnel",
      topic: "Projets pédagogiques innovants",
      year: "2025-2026"
    }
  ]
};
