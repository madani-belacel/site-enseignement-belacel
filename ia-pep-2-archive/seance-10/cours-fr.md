# Séance 10 — Esprit critique + Charte de l'étudiant + Construire son IA

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Biais, hallucinations, fiabilité : penser contre la machine quand il faut. Adopter la Charte en 10 points et découvrir les 3 voies pour construire sa propre IA.

## Objectifs pédagogiques
- Expliquer biais et hallucinations avec un exemple chacun.
- Appliquer la grille VÉRIF (Vérifier, Évaluer, Recouper, Interroger, Formuler) à une réponse d'IA.
- Réciter et signer la Charte de l'étudiant en 10 points.
- Comparer les 3 voies pour construire son IA : Dify, API Python, Ollama.
- Choisir sa voie et formuler son premier projet personnel d'IA.

## Déroulé de la séance (1 h 30)
- **00–05 — Accroche : le poisson sans odeur** : Sondage : « qui s'est déjà fait avoir ? » + analogie du nez.
- **05–25 — Explication : biais + hallucinations + grille VÉRIF** : 3 idées : pourquoi l'IA biaise, pourquoi elle invente, comment vérifier en 5 gestes.
- **25–50 — Démo : piéger l'IA puis la vérifier** : Mauvais prompt vs bon prompt : demander une référence, la voir inventée, la démasquer sur Scholar.
- **50–70 — Exercice guidé : audit VÉRIF + signature de la Charte** : Auditer une réponse en binôme, noter le verdict, signer la Charte en 10 points.
- **70–80 — Démo 2 : les 3 voies pour construire son IA** : Dify (no-code), API Python (séance 7), Ollama (local) : choisir sa voie.
- **80–90 — Synthèse, quiz et clôture du module** : « À retenir », quiz final, tour des 10 séances et remise des chartes signées.

## A. Accroche et analogie (5 min)
- **Question :** L'IA vous a-t-elle déjà affirmé quelque chose de faux… avec un aplomb total ? Aujourd'hui, on apprend à ne plus jamais se faire avoir — puis à construire sa propre machine.
- **Analogie :** 🍳 Croire l'IA sur parole, c'est comme acheter du poisson sans le sentir : parfois c'est frais, parfois non — et c'est votre nez (votre esprit critique) qui décide, pas le vendeur.
- **En une phrase :** 💡 L'esprit critique, c'est le muscle du diplôme : l'IA propose toujours, vous disposez à la fin — et un jour, vous construirez la machine au lieu de la subir.

## B + C. Explication pas à pas et démonstration
### Biais : l'IA apprend nos préjugés en même temps que nos savoirs
L'IA apprend sur des textes humains : elle hérite de leurs stéréotypes (métiers genrés, accents moqués, histoire racontée par les vainqueurs). La connaître, c'est pouvoir la contredire.

- <strong>Exemple métier :</strong> « donne un prénom à : infirmier, pilote, ministre » — observez les genres choisis, puis demandez la version équilibrée.
- <strong>Exemple histoire :</strong> « raconte la colonisation » sans précision : de quel point de vue ? Demandez-en deux.
- <strong>Contre-prompt :</strong> « Donne-moi les deux points de vue opposés sur [sujet], avec leurs arguments. »
> 💡 **<strong>🔗 Rappel séances 1, 3 et 8 :</strong> l'acteur brillant qui invente (séance 1), les sources à vérifier sur Scholar (séance 3), la citation honnête (séance 8) — aujourd'hui on boucle la boucle : penser CONTRE la machine quand il faut.**

### Hallucinations : pourquoi la machine invente avec aplomb
Rappel séance 1 : le chatbot prédit des mots plausibles, pas des vérités. Quand il ne sait pas, il ne dit pas « je ne sais pas » : il invente une réponse qui SONNE vrai (fausse référence, fausse date, faux chiffre).

- <strong>Test piège :</strong> « Donne-moi 3 articles de 2023 sur X avec liens » → vérifier chaque lien (la moitié mène nulle part).
- <strong>Test chiffre :</strong> « Quel est le taux de… ? » → exiger la source exacte, puis l'ouvrir.
- <strong>Test aveu :</strong> « Es-tu sûr ? Quelles sont tes sources ? » — une bonne IA cite, une mauvaise s'excuse en boucle.
> 💡 **<strong>Grille VÉRIF en 5 gestes :</strong> <strong>V</strong>érifier la source (existe-t-elle ?) · <strong>É</strong>valuer l'auteur (qui parle ?) · <strong>R</strong>ecouper (2e source ?) · <strong>I</strong>nterroger l'IA (« tes sources ? ») · <strong>F</strong>ormuler soi-même (réécrire, citer).**
> 💡 **<strong>🧪 Exemple vécu :</strong> « Donne-moi 3 articles 2023 sur la différenciation avec liens » → 2 liens morts, 1 vrai (retrouvé sur Scholar). Verdict écrit : « réponse douteuse, 1/3 vérifié ». C'est l'audit VÉRIF en action.**

### La Charte de l'étudiant : 10 engagements à signer
Le module se termine par un engagement solennel : utiliser l'IA en étudiant responsable. Lisez, discutez, signez — et affichez la charte dans votre chambre.

- <strong>Je vérifie</strong> toute information importante avant de l'utiliser (grille VÉRIF).
- <strong>Je cite</strong> mes vraies sources (auteur, année) ; jamais de référence inventée.
- <strong>J'écris d'abord</strong> moi-même : l'IA corrige, elle ne signe pas à ma place.
- <strong>Je refuse</strong> la triche (sujet photographié, devoir 100 % généré).
- <strong>Je protège</strong> ma clé API et mes données comme mes mots de passe.
- <strong>Je questionne</strong> les biais : je demande l'autre point de vue.
- <strong>Je révise</strong> en me testant (rappel actif), pas en relisant.
- <strong>Je planifie</strong> : planning daté, suivi du dimanche, sommeil protégé.
- <strong>J'aide</strong> mes camarades à utiliser l'IA honnêtement.
- <strong>Je construis</strong> : mon premier projet d'IA personnelle avant la fin du semestre.

### Construire son IA : les 3 voies (et la vôtre)
Après 9 séances à UTILISER l'IA, la dernière étape est de la CONSTRUIRE. Détail complet sur la page « Construire son IA » : voici la carte des 3 voies.

- <strong>🧩 Voie 1 — Dify, sans code (⭐, 30-45 min) :</strong> chatbot qui répond depuis VOS PDF de cours. Idéal : « assistant du module de psycho » pour tout le groupe.
- <strong>🐍 Voie 2 — API Python (⭐⭐, ~1 h, prérequis : séance 7) :</strong> assistant_chat.py puis mémoire, fonctions, sauvegarde. Idéal : projet personnel noté.
- <strong>🐋 Voie 3 — Ollama en local (⭐⭐, 45 min) :</strong> <strong>ollama run llama3.2</strong>, hors-ligne, gratuit, privé. Idéal : réviser sans connexion.
- <strong>Futur enseignant :</strong> imaginez un chatbot entraîné sur VOS fiches pour vos futurs élèves de primaire — c'est le pont entre vos études et votre métier.
> 💡 **<strong>Projet de fin de module :</strong> choisissez UNE voie et livrez en 3 semaines : le lien (Dify), le script (API) ou la capture (Ollama) + 1 page expliquant vos choix et vos vérifications.**

### Comment en profiter au maximum
L'étudiant accompli : il vérifie tout, cite tout, écrit d'abord — et construit. La machine propose, l'humain dispose, le diplôme couronne.
> 💡 **<strong>➡️ Après le module :</strong> page « Construire son IA » + votre voie choisie (Dify, API, Ollama) + date de livraison dans 3 semaines. Le module finit, votre projet commence.**

- <strong>✅ Réflexe VÉRIF :</strong> 5 gestes avant tout usage important d'une réponse.
- <strong>✅ Charte signée :</strong> affichée, relue avant chaque devoir.
- <strong>✅ Une voie choisie :</strong> Dify, API ou Ollama — avec date de livraison.
- <strong>✅ Transmission :</strong> expliquer à un camarade = maîtriser deux fois.
> 💡 **<strong>❌ Erreurs à éviter :</strong> croire sur parole, signer du 100 % IA, partager sa clé, abandonner son projet de construction.**

|  | Mauvais usage | Bon usage |
|---|---|---|
| Demande | « C'est vrai ? » (sans vérifier) | « Donne 3 articles avec liens. Je vérifie sur Scholar puis je cite. » |
| Résultat | Dépendant de la machine, fragile le jour J. | Autonome, sourcé, futur constructeur. |

## 📺 Ressources vidéo
- **Biais et hallucinations de l'IA : comprendre pour se protéger** (fr): https://www.youtube.com/results?search_query=biais+hallucinations+IA+expliques+simplement — Voir des hallucinations réelles capturées en vidéo et les réflexes VÉRIF.
- **هل نثق بالذكاء الاصطناعي؟ التفكير النقدي للطلبة** (ar): https://www.youtube.com/results?search_query=التفكير+النقدي+الذكاء+الاصطناعي+الطلبة — Le débat confiance/méfiance posé simplement, avec des exemples de classe.
- **Créer son chatbot sans coder avec Dify (tutoriel)** (fr): https://www.youtube.com/results?search_query=dify+tutoriel+creer+chatbot+sans+code — La voie 1 filmée : compte, PDF importé, premier chatbot en 30 minutes.

## D. Exercice guidé (15 min)
**Énoncé :** En binôme : 1) demandez une référence à l'IA et auditez-la avec VÉRIF (verdict : fiable / douteuse / fausse) ; 2) lisez la Charte à voix haute et signez ; 3) choisissez votre voie de construction + date de livraison.
**Méthode :** 1) Prompt piège : « 3 articles 2023 sur X avec liens ». 2) Pour chaque : existe ? auteur ? recoupé ? 3) Verdict écrit en 1 phrase. 4) Charte : discuter du point le plus dur, signer. 5) Projet : 3 lignes (voie, sujet, date).
**Solution :** Audit réussi : au moins 1 référence démasquée (lien mort ou article inexistant) avec preuve Scholar, verdict écrit, Charte signée par les deux, projet formulé (ex : « Dify : assistant du module d'anglais, livré le 15/12 »).

## 💭 As-tu bien compris ?
- **Q1.** D'où viennent les biais de l'IA ?
  *Réponse :* Des textes humains d'entraînement : l'IA hérite de nos stéréotypes. La parade : demander l'autre point de vue.
- **Q2.** Citez 3 gestes de la grille VÉRIF.
  *Réponse :* Vérifier que la source existe, évaluer l'auteur, recouper avec une 2e source, interroger l'IA sur ses sources, formuler soi-même en citant.
- **Q3.** Quelle voie de construction pour quel profil ?
  *Réponse :* Dify : pressé, sans code, chatbot sur PDF. API Python : programmeur en herbe (séance 7). Ollama : autonome, hors-ligne, privé.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- Biais = préjugés hérités des textes humains ; demander l'autre point de vue.
- Hallucination = invention confiante ; jamais de chiffre sans source ouverte.
- VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.
- Charte 10 points : signée, affichée, relue avant chaque devoir.
- 3 voies : Dify (PDF, sans code), API Python (séance 7), Ollama (local).
### Analogies utilisées
- 🍳 Le nez et le poisson : on sent avant d'acheter, on vérifie avant d'utiliser.
- 🍳 L'acteur brillant (séance 1) : convaincant ne veut pas dire vrai.
- 🍳 Le permis de conduire : la charte signée, c'est le code de la route de l'IA.
### Exemples concrets
- ✏️ « Prénom pour infirmier/pilote » → biais genré démasqué puis corrigé.
- ✏️ 3 liens demandés → 2 morts → verdict « douteuse » + sources Scholar.
- ✏️ Projet : « Dify : assistant d'anglais, livré le 15/12 ».
> 🏁 **Analogie finale :** 🏁 Vous et l'IA, c'est comme le cavalier et le cheval : le cheval est puissant et rapide, mais c'est le cavalier qui tient les rênes, choisit la direction — et un jour, élève ses propres chevaux.
### Quiz — vérifie ta compréhension
**Q1.** D'où viennent les biais de l'IA ?
   - 🔘 D'un complot
   - ✅ Des textes humains d'entraînement, avec leurs stéréotypes
   - 🔘 Du hasard
   - 🔘 De l'ordinateur
   *Explication :* L'IA hérite des préjugés de ses données : la parade est le contre-point de vue.
**Q2.** Une réponse avec des chiffres mais sans source : que faire ?
   - 🔘 L'utiliser vite
   - ✅ Exiger la source exacte, l'ouvrir, recouper (VÉRIF)
   - 🔘 La recopier joliment
   - 🔘 La traduire
   *Explication :* Chiffre sans source ouverte = rumeur : VÉRIF avant tout usage important.
**Q3.** Que signifie le V de VÉRIF ?
   - 🔘 Vite
   - ✅ Vérifier que la source existe vraiment
   - 🔘 Voter
   - 🔘 Vendre
   *Explication :* Premier geste : la source existe-t-elle (Scholar, site officiel) ? Sinon, tout s'écroule.
**Q4.** Quel engagement NE figure PAS dans la Charte ?
   - 🔘 Je vérifie et je cite
   - ✅ Je laisse l'IA signer à ma place
   - 🔘 Je refuse la triche
   - 🔘 Je construis mon projet
   *Explication :* Point 3 : J'écris d'abord moi-même — l'IA corrige, elle ne signe jamais à ma place.
**Q5.** Quel chemin pour un chatbot sur vos PDF sans coder ?
   - 🔘 Ollama
   - ✅ Dify : compte, Knowledge, PDF importé, publier
   - 🔘 L'API Python
   - 🔘 Aucun
   *Explication :* Dify = voie no-code sur vos documents ; API = code (séance 7) ; Ollama = local hors-ligne.

## Activités et exercices
- Piège collectif : demander 3 références, projeter la vérification Scholar en direct.
- Audit VÉRIF en binôme : verdict écrit + preuve (capture Scholar).
- Signature solennelle : lecture à voix haute de la Charte, signatures, photo de groupe.
- Choix de voie : 3 lignes (voie, sujet, date) + premier pas fait en classe (compte Dify / test Ollama).

## À retenir
- Biais hérités : demander l'autre point de vue.
- Hallucination : aucun chiffre sans source ouverte.
- VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.
- Charte 10 points : signée et affichée.
- Construire : Dify, API (S07), Ollama — projet daté.

## Glossaire
- **Biais** : Déformation héritée des données d'entraînement (stéréotypes de genre, de culture, d'histoire).
- **Hallucination** : Information inventée affirmée avec assurance par l'IA ; fréquente, pas un bug.
- **Grille VÉRIF** : 5 gestes : Vérifier, Évaluer, Recouper, Interroger, Formuler soi-même.
- **Charte de l'étudiant** : 10 engagements d'usage honnête et vérifié de l'IA, signés en fin de module.
- **Dify / Ollama** : Dify : plateforme no-code de chatbots sur vos PDF. Ollama : modèles open source en local, hors-ligne.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)