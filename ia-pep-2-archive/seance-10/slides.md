---
marp: true
theme: default
paginate: true
size: 16:9
title: Séance 10 — Esprit critique + Charte de l'étudiant + Construire son IA
---

# ⚖️ Séance 10 — Esprit critique + Charte de l'étudiant + Construire son IA

*Critical thinking + Student charter + Build your AI*

**Module Intelligence Artificielle — 2ème année PEP · ENS**

Dr. Madani BELACEL — Université de Mostaganem

---

## ⏱️ Déroulé de la séance (1 h 30)

- **00–05** — Accroche : le poisson sans odeur
- **05–25** — Explication : biais + hallucinations + grille VÉRIF
- **25–50** — Démo : piéger l'IA puis la vérifier
- **50–70** — Exercice guidé : audit VÉRIF + signature de la Charte
- **70–80** — Démo 2 : les 3 voies pour construire son IA
- **80–90** — Synthèse, quiz et clôture du module

---

## 🎯 Objectifs pédagogiques

- Expliquer biais et hallucinations avec un exemple chacun.
- Appliquer la grille VÉRIF (Vérifier, Évaluer, Recouper, Interroger, Formuler) à une réponse d'IA.
- Réciter et signer la Charte de l'étudiant en 10 points.
- Comparer les 3 voies pour construire son IA : Dify, API Python, Ollama.
- Choisir sa voie et formuler son premier projet personnel d'IA.

---

## 🎬 Accroche (5 min)

❓ L'IA vous a-t-elle déjà affirmé quelque chose de faux… avec un aplomb total ? Aujourd'hui, on apprend à ne plus jamais se faire avoir — puis à construire sa propre machine.

🍳 **Analogie :** 🍳 Croire l'IA sur parole, c'est comme acheter du poisson sans le sentir : parfois c'est frais, parfois non — et c'est votre nez (votre esprit critique) qui décide, pas le vendeur.

💡 💡 L'esprit critique, c'est le muscle du diplôme : l'IA propose toujours, vous disposez à la fin — et un jour, vous construirez la machine au lieu de la subir.

---

## Biais : l'IA apprend nos préjugés en même temps que nos savoirs

- L'IA apprend sur des textes humains : elle hérite de leurs stéréotypes (métiers genrés, accents moqués, histoire racontée par les vainqueurs). La connaître, c'est pouvoir la contredire.
- **Exemple métier :** « donne un prénom à : infirmier, pilote, ministre » — observez les genres choisis, puis demandez la version équilibrée.
- **Exemple histoire :** « raconte la colonisation » sans précision : de quel point de vue ? Demandez-en deux.
- **Contre-prompt :** « Donne-moi les deux points de vue opposés sur [sujet], avec leurs arguments. »
- 💡 **🔗 Rappel séances 1, 3 et 8 :** l'acteur brillant qui invente (séance 1), les sources à vérifier sur Scholar (séance 3), la citation honnête (séance 8) — aujourd'hui on boucle la boucle : penser CONTRE la machine quand il faut.

*Bias: AI learns our prejudices along with our knowledge*

---

## Hallucinations : pourquoi la machine invente avec aplomb

- Rappel séance 1 : le chatbot prédit des mots plausibles, pas des vérités. Quand il ne sait pas, il ne dit pas « je ne sais pas » : il invente une réponse qui SONNE vrai (fausse référence, fausse date, faux chiffre).
- **Test piège :** « Donne-moi 3 articles de 2023 sur X avec liens » → vérifier chaque lien (la moitié mène nulle part).
- **Test chiffre :** « Quel est le taux de… ? » → exiger la source exacte, puis l'ouvrir.
- **Test aveu :** « Es-tu sûr ? Quelles sont tes sources ? » — une bonne IA cite, une mauvaise s'excuse en boucle.
- 💡 **Grille VÉRIF en 5 gestes :** **V**érifier la source (existe-t-elle ?) · **É**valuer l'auteur (qui parle ?) · **R**ecouper (2e source ?) · **I**nterroger l'IA (« tes sources ? ») · **F**ormuler soi-même (réécrire, citer).
- 💡 **🧪 Exemple vécu :** « Donne-moi 3 articles 2023 sur la différenciation avec liens » → 2 liens morts, 1 vrai (retrouvé sur Scholar). Verdict écrit : « réponse douteuse, 1/3 vérifié ». C'est l'audit VÉRIF en action.

*Hallucinations: why the machine invents confidently*

---

## La Charte de l'étudiant : 10 engagements à signer

- Le module se termine par un engagement solennel : utiliser l'IA en étudiant responsable. Lisez, discutez, signez — et affichez la charte dans votre chambre.
- **Je vérifie** toute information importante avant de l'utiliser (grille VÉRIF).
- **Je cite** mes vraies sources (auteur, année) ; jamais de référence inventée.
- **J'écris d'abord** moi-même : l'IA corrige, elle ne signe pas à ma place.
- **Je refuse** la triche (sujet photographié, devoir 100 % généré).
- **Je protège** ma clé API et mes données comme mes mots de passe.

*The Student Charter: 10 commitments to sign*

---

## Construire son IA : les 3 voies (et la vôtre)

- Après 9 séances à UTILISER l'IA, la dernière étape est de la CONSTRUIRE. Détail complet sur la page « Construire son IA » : voici la carte des 3 voies.
- **🧩 Voie 1 — Dify, sans code (⭐, 30-45 min) :** chatbot qui répond depuis VOS PDF de cours. Idéal : « assistant du module de psycho » pour tout le groupe.
- **🐍 Voie 2 — API Python (⭐⭐, ~1 h, prérequis : séance 7) :** assistant_chat.py puis mémoire, fonctions, sauvegarde. Idéal : projet personnel noté.
- **🐋 Voie 3 — Ollama en local (⭐⭐, 45 min) :** **ollama run llama3.2**, hors-ligne, gratuit, privé. Idéal : réviser sans connexion.
- **Futur enseignant :** imaginez un chatbot entraîné sur VOS fiches pour vos futurs élèves de primaire — c'est le pont entre vos études et votre métier.
- 💡 **Projet de fin de module :** choisissez UNE voie et livrez en 3 semaines : le lien (Dify), le script (API) ou la capture (Ollama) + 1 page expliquant vos choix et vos vérifications.

*Build your AI: 3 paths (and yours)*

---

## Comment en profiter au maximum

- L'étudiant accompli : il vérifie tout, cite tout, écrit d'abord — et construit. La machine propose, l'humain dispose, le diplôme couronne.
- 💡 **➡️ Après le module :** page « Construire son IA » + votre voie choisie (Dify, API, Ollama) + date de livraison dans 3 semaines. Le module finit, votre projet commence.
- **✅ Réflexe VÉRIF :** 5 gestes avant tout usage important d'une réponse.
- **✅ Charte signée :** affichée, relue avant chaque devoir.
- **✅ Une voie choisie :** Dify, API ou Ollama — avec date de livraison.
- **✅ Transmission :** expliquer à un camarade = maîtriser deux fois.

*How to get the most out of it*

---

## 📺 À regarder après la classe

- **Biais et hallucinations de l'IA : comprendre pour se protéger** (fr) — https://www.youtube.com/results?search_query=biais+hallucinations+IA+expliques+simplement
- **هل نثق بالذكاء الاصطناعي؟ التفكير النقدي للطلبة** (ar) — https://www.youtube.com/results?search_query=التفكير+النقدي+الذكاء+الاصطناعي+الطلبة
- **Créer son chatbot sans coder avec Dify (tutoriel)** (fr) — https://www.youtube.com/results?search_query=dify+tutoriel+creer+chatbot+sans+code

---

## ✏️ Exercice guidé (15 min)

**Énoncé :** En binôme : 1) demandez une référence à l'IA et auditez-la avec VÉRIF (verdict : fiable / douteuse / fausse) ; 2) lisez la Charte à voix haute et signez ; 3) choisissez votre voie de construction + date de livraison.

**Solution :** Audit réussi : au moins 1 référence démasquée (lien mort ou article inexistant) avec preuve Scholar, verdict écrit, Charte signée par les deux, projet formulé (ex : « Dify : assistant du module d'anglais, livré le 15/12 »).

---

## 💭 As-tu bien compris ?

- **D'où viennent les biais de l'IA ?**
   - ✅ Des textes humains d'entraînement : l'IA hérite de nos stéréotypes. La parade : demander l'autre point de vue.
- **Citez 3 gestes de la grille VÉRIF.**
   - ✅ Vérifier que la source existe, évaluer l'auteur, recouper avec une 2e source, interroger l'IA sur ses sources, formuler soi-même en citant.
- **Quelle voie de construction pour quel profil ?**
   - ✅ Dify : pressé, sans code, chatbot sur PDF. API Python : programmeur en herbe (séance 7). Ollama : autonome, hors-ligne, privé.

---

## 🧠 Fiche de synthèse — points clés

- Biais = préjugés hérités des textes humains ; demander l'autre point de vue.
- Hallucination = invention confiante ; jamais de chiffre sans source ouverte.
- VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.
- Charte 10 points : signée, affichée, relue avant chaque devoir.
- 3 voies : Dify (PDF, sans code), API Python (séance 7), Ollama (local).

> 🏁 🏁 Vous et l'IA, c'est comme le cavalier et le cheval : le cheval est puissant et rapide, mais c'est le cavalier qui tient les rênes, choisit la direction — et un jour, élève ses propres chevaux.

---

## ✅ Quiz éclair (1 min)

**Q1. D'où viennent les biais de l'IA ?**
   - 🔘 D'un complot
   - ✅ Des textes humains d'entraînement, avec leurs stéréotypes
   - 🔘 Du hasard
   - 🔘 De l'ordinateur
**Q2. Une réponse avec des chiffres mais sans source : que faire ?**
   - 🔘 L'utiliser vite
   - ✅ Exiger la source exacte, l'ouvrir, recouper (VÉRIF)
   - 🔘 La recopier joliment
   - 🔘 La traduire
**Q3. Que signifie le V de VÉRIF ?**
   - 🔘 Vite
   - ✅ Vérifier que la source existe vraiment
   - 🔘 Voter
   - 🔘 Vendre

---

## ✏️ Activités et exercices

1. Piège collectif : demander 3 références, projeter la vérification Scholar en direct.
1. Audit VÉRIF en binôme : verdict écrit + preuve (capture Scholar).
1. Signature solennelle : lecture à voix haute de la Charte, signatures, photo de groupe.
1. Choix de voie : 3 lignes (voie, sujet, date) + premier pas fait en classe (compte Dify / test Ollama).

---

## 🧠 À retenir

- Biais hérités : demander l'autre point de vue.
- Hallucination : aucun chiffre sans source ouverte.
- VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.
- Charte 10 points : signée et affichée.
- Construire : Dify, API (S07), Ollama — projet daté.

---

# 🎓 Merci de votre attention

**Séance 10 — Esprit critique + Charte de l'étudiant + Construire son IA**

*Prochaine séance : venez avec un ordinateur ou un smartphone.*

Dr. Madani BELACEL — ENS Université de Mostaganem