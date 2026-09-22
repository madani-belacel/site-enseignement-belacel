# Séance 07 — AI and programming — Python mini-project

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Understand code, debug with AI, then build a real Python assistant calling the Gemini API: free key, commented script, run and modification.

## Objectifs pédagogiques
- Explain a simple algorithm with AI help, line by line.
- Debug a Python script: read the error, ask for a diagnosis, fix.
- Get a free API key (Gemini) and use it without sharing it.
- Run the assistant_chat.py script and chat with your own AI.
- Modify the script (conversation memory) and explain each addition.

## Déroulé de la séance (1 h 30)
- **00–05 — Hook: the kitchen helper** : Opening question + chef-and-helper analogy.
- **05–25 — Explanation: understand and debug with AI** : 3 ideas: have code explained line by line; read error messages; ask for a diagnosis before the solution.
- **25–50 — Demo: the API key + the first script** : ai.google.dev → free key → pip install → assistant_chat.py answering.
- **50–70 — Guided exercise: add the memory** : Transform the script: keep the last 6 exchanges for context.
- **70–80 — Demo 2: Cursor / Copilot in action** : Live auto-completion: write a comment, let the tool complete, verify.
- **80–90 — Wrap-up, quiz and preview of session 8** : Key takeaways. Preview: academic writing and anti-plagiarism.

## A. Accroche et analogie (5 min)
- **Question :** What if your next programming exercise corrected itself… while explaining your own mistakes? That is exactly what we will build today.
- **Analogie :** 🍳 Programming with AI is like cooking with a helper: you are the chef (you decide the dish), the helper peels and chops (it writes repetitive code), but you taste every step — otherwise the dish fails.
- **En une phrase :** 💡 An API is a counter: your small Python script drops a question there, and the big AI model answers. Today, you build the counter.

## B + C. Explication pas à pas et démonstration
### Understand code: AI as a private teacher
Never ask "do my assignment": ask "explain to me". A student who understands 10 explained programs progresses; one who submits 10 generated programs stagnates.

- <strong>Explanation prompt:</strong> "Explain this code line by line, like to a beginner: [paste code]."
- <strong>Algorithm prompt:</strong> "Explain finding the maximum in a list with a step-by-step number example."
- <strong>Comparison prompt:</strong> "What is the difference between for and while loops? One example each."
> 💡 **<strong>🔗 Reminder of session 6:</strong> the Socratic tutor asked questions instead of giving answers. Today, we CODE it: our script will ask Gemini questions instead of doing everything for us.**

### Debug: read the error before fixing it
An error message is not an insult: it is an address (the line number) and a diagnosis (the error type). Show both to AI, and ask for the WHY first.

- <strong>3-step method:</strong> 1) read the last line of the error; 2) ask "why this error?"; 3) only then "how to fix?"
- <strong>Model prompt:</strong> "Here is my code [paste] and the error [paste]. Explain the cause in 2 sentences, then suggest ONE fix."
- <strong>Classic PEP mistakes:</strong> indentation, missing colons, undefined variable, mixed types.
> 💡 **<strong>Tip:</strong> after the fix, ask "give me a similar mini-exercise to check I understood". The loop is closed: error → cause → fix → check.**
> 💡 **<strong>🧪 Concrete example:</strong> average = total / count. A TypeError mixing text and numbers → cause: an age read as text → fix: int(age). Then ask for a similar exercise with grades.**

### The mini-project: your assistant calling Gemini
An API (programming interface) is a counter: your script sends text, the giant model answers. With a free key, 15 lines of Python are enough for YOUR chatbot.

- <strong>Free key:</strong> go to ai.google.dev → "Get API key" → copy (like a password, never shared).
- <strong>Install:</strong> <strong>python -m pip install google-generativeai</strong> in the terminal.
- <strong>Copy</strong> the assistant_chat.py script below, paste the key, run: <strong>python assistant_chat.py</strong>.
- <strong>Test:</strong> ask 3 revision questions from your favourite module.

```
# assistant_chat.py -- mini assistant IA (projet seance 07)
# Installation : python -m pip install google-generativeai
import google.generativeai as genai

# 1. Cle gratuite sur https://ai.google.dev (ne jamais la partager !)
genai.configure(api_key="COLLE_TA_CLE_ICI")

# 2. Choix du modele (rapide et gratuit)
model = genai.GenerativeModel("gemini-2.0-flash")

print("Assistant IA pour etudiant (tape 'quit' pour sortir)")
while True:
    question = input("\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    reponse = model.generate_content(question)
    print("IA   >", reponse.text)
```
> 💡 **<strong>🔒 Security:</strong> the API key is a paying password. Never in a submitted assignment, never on GitHub, never in a photo. If leaked, regenerate it on ai.google.dev.**

### Go further: Copilot, Cursor and memory
Second stage of the rocket: assistants built into the editor (completion while typing) and history (the chatbot that remembers).

- <strong>Cursor / Copilot:</strong> write a comment "# function computing the average", let the tool suggest code, READ it before accepting.
- <strong>Memory:</strong> the assistant_memoire.py version keeps the last 6 exchanges: try "and in Arabic?" after a question.
- <strong>Limit:</strong> the assistant writes fast but does not understand your assignment — only your test (run + edge cases) validates.

```
# assistant_memoire.py -- meme assistant, AVEC memoire de conversation
import google.generativeai as genai

genai.configure(api_key="COLLE_TA_CLE_ICI")
model = genai.GenerativeModel("gemini-2.0-flash")

# Nouveaute : l'historique garde le contexte des questions precedentes
historique = []

print("Assistant avec memoire (tape 'quit' pour sortir)")
while True:
    question = input("\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    historique.append("Etudiant : " + question)
    prompt = "\n".join(historique[-6:])  # les 6 derniers echanges
    reponse = model.generate_content(prompt)
    historique.append("IA : " + reponse.text)
    print("IA   >", reponse.text)
```

### How to get the most out of it
The augmented programmer: AI proposes, you decide. Every generated line is reread, run and tested — that is what distinguishes a student from a copy-paste operator.
> 💡 **<strong>➡️ Bridge to session 8:</strong> a program writing well impresses, but a student writing well convinces: your assistant will also proofread your texts (explained correction, session 8).**

- <strong>✅ Explain-first:</strong> always understand before submitting.
- <strong>✅ One error = one lesson:</strong> note the cause in a bug notebook.
- <strong>✅ Version:</strong> keep assistant_chat.py then assistant_memoire.py (see progress).
- <strong>✅ Test limits:</strong> empty question, very long, dialectal Arabic — what happens?
> 💡 **<strong>❌ Mistakes to avoid:</strong> submitting unrun code, sharing your API key, believing "it works once" = "it is correct" (test edge cases).**

|  | Bad use | Good use |
|---|---|---|
| Prompt | "Do my sorting assignment." | "Explain selection sort with an example [7, 2, 9], then give me a similar exercise." |
| Result | Submitted code, nothing understood, zero on exam day. | Understanding + training, autonomous on D-day. |

## 📺 Ressources vidéo
- **Mohammad Dawoud's AI playlist (intro, ML, neural networks)** (ar): https://www.youtube.com/watch?v=H5WUwwivEaI&list=PLbR_CTcUs1088jfqbbO5AqwODO9MgYA85 — The module's reference: understand what is UNDER the API counter (neurons, learning).
- **But what is a neural network? (3Blue1Brown)** (en): https://www.youtube.com/watch?v=aircAruvnKk — Visualise how a network learns — FR subtitles available.
- **Learn Python + use the Gemini API (tutorial)** (fr): https://www.youtube.com/results?search_query=gemini+api+python+tutorial+debutant — See each step (key, pip install, first call) done on video before redoing it.

## D. Exercice guidé (15 min)
**Énoncé :** 1) Run assistant_chat.py and ask 3 lesson questions. 2) Create assistant_memoire.py (add history). 3) Test memory: ask then "summarise your previous answer in 1 sentence".
**Méthode :** 1) Check Python: python --version. 2) Install the library. 3) Paste the key WITHOUT showing your screen neighbour. 4) Run, test, then add the historique list. 5) Compare both versions on the same follow-up question.
**Solution :** Version 1 answers each question in isolation (forgets context). Version 2 with history correctly answers follow-ups ("and in Arabic?", "summarise"). On API error: check the key, Wi-Fi and model name (gemini-2.0-flash).

## 💭 As-tu bien compris ?
- **Q1.** What is an API key and why protect it?
  *Réponse :* It is the password identifying your account to the model and it can be billed. Shared = someone spends on your behalf.
- **Q2.** Why ask for the WHY of the error before the fix?
  *Réponse :* Understanding the cause prevents repeating the mistake; copying the fix without understanding guarantees it next time.
- **Q3.** What does history change in assistant_memoire.py?
  *Réponse :* The last 6 exchanges are resent to the model: it understands follow-ups like "and in Arabic?" without repeating the question.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- Explain-to-me > do-for-me: understand before submitting.
- Debugging: read the error, ask WHY, then fix.
- API = counter: free key on ai.google.dev, never shared.
- 15 lines are enough: assistant_chat.py chats with Gemini.
- Memory = resend the last 6 exchanges to the model.
### Analogies utilisées
- 🍳 The kitchen helper: he prepares, you taste and decide.
- 🍳 The API counter: you drop a question, the giant answers.
- 🍳 The bug notebook: each noted error is a defused trap.
### Exemples concrets
- ✏️ "Explain this sort line by line" → the student understands and redoes alone.
- ✏️ IndentationError → cause understood → fix + verification mini-exercise.
- ✏️ "And in Arabic?" understood thanks to the 6-exchange history.
> 🏁 **Analogie finale :** 🏁 Programming with AI is like learning to drive with an instructor: at first he holds the wheel with you, but you take the exam alone — and drive the road after, too.
### Quiz — vérifie ta compréhension
**Q1.** What is the best first prompt facing misunderstood code?
   - 🔘 "Do my assignment"
   - ✅ "Explain this code line by line, like to a beginner"
   - 🔘 "It is bad, redo it"
   - 🔘 "Give me another code"
   *Explication :* Explanation builds understanding; ready-made code bypasses it.
**Q2.** Facing a Python error, what is the right order?
   - 🔘 Fix then understand
   - ✅ Read the error → ask WHY → fix → verify
   - 🔘 Delete the file
   - 🔘 Change language
   *Explication :* The understood cause + a verification mini-exercise close the learning loop.
**Q3.** Where to get a Gemini key and how to treat it?
   - 🔘 On Google, to share
   - ✅ On ai.google.dev, like a never-shared password
   - 🔘 In a friend's script
   - 🔘 No key needed
   *Explication :* The key is free on ai.google.dev but billable: a leak = someone spends on your behalf.
**Q4.** What does the historique list do in assistant_memoire.py?
   - 🔘 It saves to disk
   - ✅ It resends the last 6 exchanges to keep context
   - 🔘 It speeds up Internet
   - 🔘 It translates code
   *Explication :* The model is memoryless: the script reminds it of the conversation on each call.
**Q5.** Why test edge cases (empty, very long question)?
   - 🔘 To waste time
   - ✅ Because "works once" is not "correct": only testing validates
   - 🔘 To impress
   - 🔘 It is forbidden
   *Explication :* A program is judged on normal AND edge cases: that is the programmer's mark, not the copier's.

## Activités et exercices
- Cross-explanation: AI explains a sort, each pair re-explains it without screen.
- Bug hunt: 3 trapped scripts (indentation, variable, type) to diagnose before fixing.
- First call: key + pip install + assistant_chat.py → 3 revision questions.
- Memory challenge: add history then pass the "summarise your previous answer" test.

## À retenir
- Explain-to-me > do-for-me: understanding first.
- Debug: read, WHY, fix, verify.
- Key on ai.google.dev, never shared, never on GitHub.
- assistant_chat.py: 15 lines to talk to Gemini.
- Memory is the script reminding the model of the conversation.

## Glossaire
- **API** : A software counter: your program sends a request, the service (Gemini) answers.
- **Clé API** : A personal password identifying your calls to the service; free but billable, protect it.
- **Débogage** : The art of finding an error's cause (read, diagnose) before fixing it.
- **Bibliothèque (package)** : Ready-to-use code you install (pip install) to use a service like Gemini.
- **Historique de conversation** : Previous exchanges resent to the model so it keeps context.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)