# Fiche de synthèse — Séance 07 : IA et programmation — mini-projet Python

**AI and programming — Python mini-project**

> Comprendre le code, déboguer avec l'IA, puis construire un vrai assistant Python qui appelle l'API Gemini : clé gratuite, script commenté, exécution et modification.

## Points clés
1. Explique-moi > fais-moi : comprendre avant de rendre.
> EN: Explain-to-me > do-for-me: understand before submitting.
> AR: اشرح لي > أنجز عني: افهم قبل التسليم.
1. Débogage : lire l'erreur, demander le POURQUOI, puis corriger.
> EN: Debugging: read the error, ask WHY, then fix.
> AR: التصحيح: اقرأ الخطأ، واسأل لماذا، ثم صحّح.
1. API = guichet : clé gratuite sur ai.google.dev, jamais partagée.
> EN: API = counter: free key on ai.google.dev, never shared.
> AR: API = شبّاك: مفتاح مجاني من ai.google.dev، لا يُشارَك أبداً.
1. 15 lignes suffisent : assistant_chat.py dialogue avec Gemini.
> EN: 15 lines are enough: assistant_chat.py chats with Gemini.
> AR: تكفي 15 سطراً: assistant_chat.py يحاور Gemini.
1. Mémoire = renvoyer les 6 derniers échanges au modèle.
> EN: Memory = resend the last 6 exchanges to the model.
> AR: الذاكرة = إعادة إرسال آخر 6 تبادلات إلى النموذج.

## Analogies utilisées
- 🍳 Le commis cuisinier : il prépare, vous goûtez et décidez.
- 🍳 Le guichet API : vous déposez une question, le géant répond.
- 🍳 Le carnet de bugs : chaque erreur notée est un piège désamorcé.

## Exemples concrets
- ✏️ « Explique ce tri ligne par ligne » → l'étudiant comprend et refait seul.
- ✏️ IndentationError → cause comprise → correction + mini-exercice de vérification.
- ✏️ « Et en arabe ? » compris grâce à l'historique des 6 échanges.

> 🏁 **Analogie finale :** 🏁 Programmer avec l'IA, c'est comme apprendre à conduire avec un moniteur : au début il tient le volant avec vous, mais l'examen, c'est vous seul qui le passez — et la route ensuite aussi.
> EN: 🏁 Programming with AI is like learning to drive with an instructor: at first he holds the wheel with you, but you take the exam alone — and drive the road after, too. / AR: 🏁 البرمجة مع الذكاء الاصطناعي كتعلّم القيادة مع مدرّب: في البداية يمسك المقود معك، لكن الامتحان تجتازه وحدك — والطريق بعده أيضاً.

## Quiz (5 questions) — réponses cachées

<details>
<summary>Réponses du quiz</summary>

**Q1. Quel est le meilleur premier prompt face à un code incompris ?**
- 🔘 « Fais mon TP »
- ✅ « Explique ce code ligne par ligne, comme à un débutant »
- 🔘 « C'est nul, recommence »
- 🔘 « Donne-moi un autre code »
*Explication : L'explication construit la compréhension ; le code tout fait la contourne.*

**Q2. Face à une erreur Python, quel est le bon ordre ?**
- 🔘 Corriger puis comprendre
- ✅ Lire l'erreur → demander le POURQUOI → corriger → vérifier
- 🔘 Supprimer le fichier
- 🔘 Changer de langage
*Explication : La cause comprise + un mini-exercice de vérification ferment la boucle d'apprentissage.*

**Q3. Où obtenir une clé Gemini et comment la traiter ?**
- 🔘 Sur Google, à partager
- ✅ Sur ai.google.dev, comme un mot de passe jamais partagé
- 🔘 Dans le script d'un ami
- 🔘 Pas besoin de clé
*Explication : La clé est gratuite sur ai.google.dev mais facturable : fuite = quelqu'un dépense à votre place.*

**Q4. Que fait la liste historique dans assistant_memoire.py ?**
- 🔘 Elle sauvegarde sur disque
- ✅ Elle renvoie les 6 derniers échanges pour garder le contexte
- 🔘 Elle accélère Internet
- 🔘 Elle traduit le code
*Explication : Le modèle est sans mémoire : c'est le script qui lui rappelle la conversation à chaque appel.*

**Q5. Pourquoi tester les cas limites (question vide, très longue) ?**
- 🔘 Pour perdre du temps
- ✅ Parce que « marche une fois » n'est pas « correct » : seul le test valide
- 🔘 Pour impressionner
- 🔘 C'est interdit
*Explication : Un programme se juge sur les cas normaux ET limites : c'est la marque du programmeur, pas du copieur.*

</details>

---

**À retenir :** Explique-moi > fais-moi : la compréhension d'abord. ; Déboguer : lire, POURQUOI, corriger, vérifier. ; Clé sur ai.google.dev, jamais partagée, jamais sur GitHub. ; assistant_chat.py : 15 lignes pour parler à Gemini. ; La mémoire, c'est le script qui rappelle la conversation au modèle.
