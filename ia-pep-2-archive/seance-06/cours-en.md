# Séance 06 — Revise efficiently and simulate exams

**Module : Intelligence Artificielle — 2ème année PEP (ENS)**  
**Auteur : Dr. Madani BELACEL — Université de Mostaganem**  
**Durée : 1 h 30**  

Turn your sheets into flashcards, generate corrected quizzes, get questioned by a Socratic tutor and train on past papers — without cheating, by understanding.

## Objectifs pédagogiques
- Explain why rereading is not enough: active recall and spaced repetition.
- Turn a lesson sheet into 10 flashcards with AI.
- Generate a corrected quiz from a chapter and analyse your mistakes.
- Use a Socratic tutor: AI asks questions instead of giving answers.
- Simulate a timed mock exam from past papers.

## Déroulé de la séance (1 h 30)
- **00–05 — Hook: rereading does not work** : Survey: "how many times do you reread?" + the sport analogy.
- **05–25 — Explanation: active recall + spaced repetition** : 3 ideas: testing beats rereading; spacing beats cramming; sleep consolidates.
- **25–50 — Demo: flashcards + quiz + Socratic tutor** : Bad prompt vs good prompt: generate 10 flashcards and a corrected quiz from a sheet.
- **50–70 — Guided exercise: my first flashcard deck** : Each student generates 10 flashcards from their sheet and tests their neighbour.
- **70–80 — Demo 2: timed mock exam** : Turn a past paper into a timed paper + marking scheme.
- **80–90 — Wrap-up, quiz and preview of session 7** : Key takeaways. Preview: programming with AI and the Python mini-project.

## A. Accroche et analogie (5 min)
- **Question :** Who has already reread a lesson 10 times… only to forget everything on exam day? The problem is not your memory: it is the method.
- **Analogie :** 🍳 Rereading your lesson is like watching someone do sport and hoping to get muscles. Revising with active recall is lifting the weights yourself: the effort of remembering is what builds memory.
- **En une phrase :** 💡 AI becomes your revision coach: it questions you, corrects and reschedules — but your brain does the work.

## B + C. Explication pas à pas et démonstration
### Why rereading is not enough: 3 game-changing ideas
Cognitive psychology research is clear: students who test themselves remember twice as much as those who reread. AI is perfect for making these tests — provided you understand the method.

- <strong>1. Active recall:</strong> close the lesson and try to restate the essentials. The effort of searching memory creates the trace.
- <strong>2. Spaced repetition:</strong> review at D+1, D+3, D+7, D+14 — not 5 times the day before.
- <strong>3. Interleaving:</strong> alternate chapters instead of finishing one before the other.
- <strong>Sleep:</strong> the brain consolidates at night. Revising late without sleep is counter-productive.
> 💡 **<strong>Diagram to draw on the board:</strong> the forgetting curve — without review we forget 70% in 24h; each spaced recall lifts the curve higher and longer.**
> 💡 **<strong>🔗 Reminder of sessions 4 and 5:</strong> your Cornell sheets (session 4) become flashcards, and your presentation AI-jury (session 5) becomes a tutor questioning you. Each session reuses previous tools.**

### Flashcards: 10 cards worth 10 rereads
A flashcard = a question on one side, the answer on the other. You test yourself, sort (known / failed), and review only the failed ones. AI generates the deck in 1 minute from your sheet.

- <strong>Model prompt:</strong> "Here is my sheet [paste]. Create 10 flashcards: one short question + 1-sentence answer. Number them."
- <strong>Golden rule:</strong> 1 card = 1 fact. If the answer is 5 lines, split into 3 cards.
- <strong>Free tools:</strong> Anki (automatic spaced repetition), Quizlet, or plain paper.
- <strong>In Arabic too:</strong> AI generates the cards in your sheet's language.
> 💡 **<strong>🧪 Concrete example:</strong> "Present perfect" sheet → card 3: Q "Which form after have/has?" / A "The past participle — e.g. I have <strong>eaten</strong>." Test your neighbour: they answer without looking, you show the answer.**

### Corrected quizzes and past papers: train like exam day
Ask AI for a quiz with explained answers, then take it WITHOUT looking at the lesson, timer on. Analysing mistakes is worth more than the score.

- <strong>Quiz prompt:</strong> "Chapter [paste]. 10 MCQs with 4 options, 1 correct answer, then correction with the lesson sentence that justifies it."
- <strong>Past-paper prompt:</strong> "Here is the 2024 paper [paste]. Propose a 2025 paper in the same style + marking out of 20."
- <strong>Analysis ritual:</strong> for each mistake, write the correct rule in 1 sentence in a notebook.
- <strong>Trap:</strong> redoing the same quiz from memory gives false confidence — ask for a shuffled version.
> 💡 **<strong>⚠️ Red line:</strong> generating a quiz to revise = excellent. Photographing the paper during the exam to have AI solve it = cheating, disciplinary sanction. A cheated diploma is worthless.**

### The Socratic tutor: an AI that questions you
Instead of asking for the answer, ask for questions: AI becomes an tireless private tutor who only gives the solution after your attempts.

- <strong>Tutor prompt:</strong> "You are my [module] tutor. Ask me one question at a time about [chapter]. If I am wrong, give a hint, not the answer. 10 questions."
- <strong>Presentation variant:</strong> "Play the jury: ask me 5 tricky questions about my topic."
- <strong>Language variant:</strong> "Correct my English sentence by sentence and explain each mistake."

### How to get the most out of it
The winning cycle: generate → test yourself WITHOUT the lesson → correct → note mistakes → reschedule failed items at D+3.
> 💡 **<strong>➡️ Bridge to session 7:</strong> the Socratic tutor questioning you will become a REAL Python program (assistant_chat.py) calling Gemini. You will move from user to builder.**

- <strong>✅ Mix:</strong> flashcards + quiz + tutor, never a single format.
- <strong>✅ Time yourself:</strong> always with real exam timing.
- <strong>✅ Mistake notebook:</strong> 1 sentence per mistake, reread the day before.
- <strong>✅ Ask for variants:</strong> "same chapter, 10 different questions".
> 💡 **<strong>❌ Mistakes to avoid:</strong> revising with the answers in front of you, redoing the same memorised quiz, revising 6h straight without breaks (25 min work + 5 min break).**

|  | Bad use | Good use |
|---|---|---|
| Prompt | "Give me the chapter 3 answers." | "Quiz me on chapter 3, one question at a time, without giving answers." |
| Result | Passive reading, illusion of knowledge. | Active recall, real memory traces. |

## 📺 Ressources vidéo
- **Revise with flashcards and Anki (tutorial)** (fr): https://www.youtube.com/results?search_query=anki+flashcards+tutoriel+francais+revision — To install Anki and create your first deck from AI-generated cards.
- **How to revise smartly? Active recall and spaced repetition** (ar): https://www.youtube.com/results?search_query=active+recall+spaced+repetition+study+technique — The science of memory simply explained, with student examples.
- **Generate quizzes with ChatGPT to revise** (fr): https://www.youtube.com/results?search_query=generer+QCM+chatgpt+reviser+examen — See the "sheet → corrected quiz → mistake analysis" method on video.

## D. Exercice guidé (15 min)
**Énoncé :** With your lesson sheet: 1) generate 10 flashcards with the model prompt; 2) test your neighbour (they answer without looking); 3) note failed cards and reschedule them at D+3.
**Méthode :** 1) Copy the model prompt and paste your sheet. 2) Check each card has 1 question + 1 short answer (split otherwise). 3) Hide answers and quiz yourself aloud. 4) Sort: known / failed.
**Solution :** Example of a good deck: 10 numbered cards, short questions ("What is the past participle agreement rule with avoir?"), 1-sentence answers, 2 overlong cards split into 4, schedule noted: review the 3 failed at D+3.

## 💭 As-tu bien compris ?
- **Q1.** Why is testing yourself more effective than rereading?
  *Réponse :* Because the effort of retrieving information from memory creates a lasting trace, while rereading only gives a feeling of familiarity.
- **Q2.** What to do after a failed 6/10 quiz?
  *Réponse :* Write each mistake in 1 sentence in the notebook, review failed points at D+3, then ask for a shuffled version of the quiz.
- **Q3.** What is the difference between asking for the answer and asking to be questioned?
  *Réponse :* Asking for the answer = passive reading. Asking to be questioned (Socratic tutor) = active recall: your brain works.

## E. Résumé visuel et mémorable (5 min)
### Points clés
- Testing beats rereading: active recall builds memory.
- Space out: D+1, D+3, D+7, D+14 — never everything the day before.
- 1 flashcard = 1 question + 1 short answer.
- Timed quiz without the lesson + mistake notebook (1 sentence per mistake).
- Socratic tutor: AI questions, you answer, it hints.
### Analogies utilisées
- 🍳 Sport: watching does not build muscle, lifting does — revising is lifting.
- 🍳 The mistake notebook is the first-aid kit of exam eve.
- 🍳 The Socratic tutor is a sparring partner: it hits softly to train you.
### Exemples concrets
- ✏️ Psychology sheet → 10 flashcards → neighbour test → 3 failed at D+3.
- ✏️ 2024 past paper copied → 2025 paper generated + marking → 1h timed.
- ✏️ "Quiz me on English tenses, one by one" → 10 questions, 2 hints.
> 🏁 **Analogie finale :** 🏁 Revising with AI is like having a personal sports coach: it prepares exercises, counts reps and cheers you on — but you build the muscles.
### Quiz — vérifie ta compréhension
**Q1.** Why does rereading 5 times give false confidence?
   - 🔘 Because the text changes
   - ✅ Because familiarity feels like knowledge without being memory
   - 🔘 Because it is forbidden
   - 🔘 Because it is too fast
   *Explication :* Rereading makes text familiar, but only retrieval effort (testing without the lesson) creates a lasting trace.
**Q2.** What is the right spaced revision schedule?
   - 🔘 Everything the day before
   - ✅ D+1, D+3, D+7, D+14
   - 🔘 Once a month
   - 🔘 Never, it is useless
   *Explication :* Reviewing just before forgetting (D+1, D+3, D+7, D+14) consolidates memory with little effort.
**Q3.** What does a good flashcard contain?
   - 🔘 A whole chapter
   - ✅ 1 question + 1 short answer
   - 🔘 Only a picture
   - 🔘 The full correction
   *Explication :* 1 card = 1 fact. Long answers must be split into several cards.
**Q4.** What to do with a quiz mistake?
   - 🔘 Ignore it
   - ✅ Write it in 1 sentence in the notebook and review at D+3
   - 🔘 Redo the same quiz at once
   - 🔘 Blame AI
   *Explication :* A mistake is information: noted and reviewed at D+3, it will not happen again.
**Q5.** Which prompt makes YOUR brain work?
   - 🔘 "Give me the answers"
   - ✅ "Quiz me one question at a time, without giving answers"
   - 🔘 "Summarise everything"
   - 🔘 "Do my homework"
   *Explication :* The Socratic tutor (questions + hints) triggers active recall; asking for answers = passive reading.

## Activités et exercices
- Flashcard factory: generate 10 cards from your sheet, test your neighbour, sort known/failed.
- Timed quiz: generate a 10-question quiz, take it in 15 min without the lesson, analyse mistakes.
- Socratic duo: one plays the AI-tutor (questions + hints), the other answers; then swap.
- Mock exam: paper generated from a past paper, 30 min timed, cross-correction in pairs.

## À retenir
- Testing > rereading: active recall builds memory.
- Space D+1, D+3, D+7, D+14; sleep consolidates.
- Flashcards: 1 card = 1 question + 1 short answer.
- Timed quiz without lesson + mistake notebook.
- Socratic tutor: never a direct answer, always a question first.

## Glossaire
- **Rappel actif** : The effort of retrieving information from memory without looking at the lesson; the most effective revision method.
- **Répétition espacée** : Reviewing a notion at increasing intervals (D+1, D+3, D+7…) to fight forgetting.
- **Flashcard** : A question/answer card for quick self-testing, ideal with Anki.
- **Tuteur socratique** : An AI use where it asks questions and gives hints instead of delivering answers.
- **Annale** : A previous year's exam paper, the ideal base to simulate exam day.

## Ressources de la séance
- fiche-synthese.md (fiche de synthèse + quiz corrigé)
- presentation.pptx (support de cours)
- slides.md (diapositives Marp)
- dialogues-fr.md / dialogues-en.md (scripts à jouer en classe)
- outils-ia.html / construire-ia.html (boîte à outils du module)