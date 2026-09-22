# -*- coding: utf-8 -*-
"""Séance 06 — Réviser efficacement et simuler des examens avec l'IA (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 6,
    "slug": "seance-06",
    "icon": "📝",
    "titles": L(
        "Réviser efficacement et simuler des examens",
        "Revise efficiently and simulate exams",
        "المراجعة الفعّالة ومحاكاة الامتحانات",
    ),
    "descriptions": L(
        "Transformer ses fiches en flashcards, générer des QCM corrigés, se faire interroger par un tuteur socratique et s'entraîner sur des annales — sans tricher, en comprenant.",
        "Turn your sheets into flashcards, generate corrected quizzes, get questioned by a Socratic tutor and train on past papers — without cheating, by understanding.",
        "تحويل بطاقاتك إلى بطاقات استذكار، وتوليد اختبارات مصحّحة، وجعل مدرّس سقراطي يستجوبك، والتدرب على مواضيع سابقة — دون غشّ، بل بفهم.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Expliquer pourquoi relire ne suffit pas : rappel actif et répétition espacée.",
            "Explain why rereading is not enough: active recall and spaced repetition.",
            "أن يفسّر لماذا لا تكفي إعادة القراءة: الاستدعاء النشط والتكرار المتباعد.",
        ),
        L(
            "Transformer une fiche de cours en 10 flashcards avec l'IA.",
            "Turn a lesson sheet into 10 flashcards with AI.",
            "أن يحوّل بطاقة درس إلى عشر بطاقات استذكار بالذكاء الاصطناعي.",
        ),
        L(
            "Générer un QCM corrigé à partir d'un chapitre et analyser ses erreurs.",
            "Generate a corrected quiz from a chapter and analyse your mistakes.",
            "أن يولّد اختباراً مصحّحاً من فصل ويحلّل أخطاءه.",
        ),
        L(
            "Utiliser un tuteur socratique : l'IA pose des questions au lieu de donner les réponses.",
            "Use a Socratic tutor: AI asks questions instead of giving answers.",
            "أن يستعمل مدرّساً سقراطياً: الذكاء الاصطناعي يطرح أسئلة بدل إعطاء الأجوبة.",
        ),
        L(
            "Simuler un examen blanc chronométré à partir d'annales.",
            "Simulate a timed mock exam from past papers.",
            "أن يحاكي امتحاناً أبيض بمؤقّت انطلاقاً من مواضيع سابقة.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 5 suivies. Venir avec une fiche de cours d'un module au choix.",
        "Sessions 1 to 5 completed. Come with a lesson sheet from any module.",
        "إتمام الحصص من 1 إلى 5. الإتيان ببطاقة درس من أي وحدة.",
    ),
    "accroche": {
        "question": L(
            "Qui a déjà relu 10 fois un cours… pour tout oublier le jour de l'examen ? Le problème n'est pas votre mémoire : c'est la méthode.",
            "Who has already reread a lesson 10 times… only to forget everything on exam day? The problem is not your memory: it is the method.",
            "من أعاد قراءة درس عشر مرات… لينسى كل شيء يوم الامتحان؟ المشكلة ليست ذاكرتك: بل المنهجية.",
        ),
        "analogie": L(
            "🍳 Relire son cours, c'est comme regarder quelqu'un faire du sport en espérant devenir musclé. Réviser avec rappel actif, c'est soulever soi-même les haltères : c'est l'effort de se souvenir qui muscle la mémoire.",
            "🍳 Rereading your lesson is like watching someone do sport and hoping to get muscles. Revising with active recall is lifting the weights yourself: the effort of remembering is what builds memory.",
            "🍳 إعادة قراءة الدرس كمشاهدة شخص يمارس الرياضة على أمل أن تصبح عضلياً. المراجعة بالاستدعاء النشط كرفع الأثقال بنفسك: جهد التذكّر هو ما يقوّي الذاكرة.",
        ),
        "phrase": L(
            "💡 L'IA devient votre coach de révision : elle vous interroge, corrige et reprogramme — mais c'est votre cerveau qui fait le travail.",
            "💡 AI becomes your revision coach: it questions you, corrects and reschedules — but your brain does the work.",
            "💡 يصبح الذكاء الاصطناعي مدرّب مراجعتك: يستجوبك ويصحّح ويعيد البرمجة — لكن دماغك هو من يعمل.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : relire ne marche pas",
                "Hook: rereading does not work",
                "انطلاقة: إعادة القراءة لا تنفع",
            ),
            "detail": L(
                "Sondage : « combien de fois relisez-vous ? » + analogie du sport.",
                "Survey: \"how many times do you reread?\" + the sport analogy.",
                "استطلاع: « كم مرة تعيدون القراءة؟ » + تشبيه الرياضة.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : rappel actif + répétition espacée",
                "Explanation: active recall + spaced repetition",
                "شرح: الاستدعاء النشط + التكرار المتباعد",
            ),
            "detail": L(
                "3 idées : se tester bat relire ; espacer bat bachoter ; dormir consolide.",
                "3 ideas: testing beats rereading; spacing beats cramming; sleep consolidates.",
                "3 أفكار: الاختبار يغلب إعادة القراءة؛ التباعد يغلب الحشو؛ النوم يرسّخ.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : flashcards + QCM + tuteur socratique",
                "Demo: flashcards + quiz + Socratic tutor",
                "عرض: بطاقات + اختبار + مدرّس سقراطي",
            ),
            "detail": L(
                "Mauvais prompt vs bon prompt : générer 10 flashcards et un QCM corrigé depuis une fiche.",
                "Bad prompt vs good prompt: generate 10 flashcards and a corrected quiz from a sheet.",
                "صياغة ضعيفة مقابل قوية: توليد عشر بطاقات واختبار مصحّح من بطاقة.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : mon premier paquet de flashcards",
                "Guided exercise: my first flashcard deck",
                "تمرين موجّه: أول حزمة بطاقات",
            ),
            "detail": L(
                "Chaque étudiant génère 10 flashcards depuis sa fiche et teste son voisin.",
                "Each student generates 10 flashcards from their sheet and tests their neighbour.",
                "يولّد كل طالب عشر بطاقات من بطاقته ويختبر جاره.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : examen blanc chronométré",
                "Demo 2: timed mock exam",
                "عرض 2: امتحان أبيض بمؤقّت",
            ),
            "detail": L(
                "Transformer une annale en sujet chronométré + grille de correction.",
                "Turn a past paper into a timed paper + marking scheme.",
                "تحويل موضوع سابق إلى امتحان بمؤقّت + شبكة تصحيح.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et annonce de la séance 7",
                "Wrap-up, quiz and preview of session 7",
                "خلاصة واختبار وتقديم الحصة السابعة",
            ),
            "detail": L(
                "« À retenir ». Annonce : programmer avec l'IA et le mini-projet Python.",
                "Key takeaways. Preview: programming with AI and the Python mini-project.",
                "« ما يجب تذكّره ». تقديم: البرمجة مع الذكاء الاصطناعي والمشروع المصغّر.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Pourquoi relire ne suffit pas : les 3 idées qui changent tout",
                "Why rereading is not enough: 3 game-changing ideas",
                "لماذا لا تكفي إعادة القراءة: ثلاث أفكار تغيّر كل شيء",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "La recherche en psychologie cognitive est claire : les étudiants qui se testent retiennent 2 fois plus que ceux qui relisent. L'IA est parfaite pour fabriquer ces tests — à condition de comprendre la méthode.",
                        "Cognitive psychology research is clear: students who test themselves remember twice as much as those who reread. AI is perfect for making these tests — provided you understand the method.",
                        "أبحاث علم النفس المعرفي واضحة: الطلبة الذين يختبرون أنفسهم يتذكرون ضعف ما يتذكره من يعيدون القراءة. والذكاء الاصطناعي مثالي لصنع هذه الاختبارات — بشرط فهم المنهجية.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1. Rappel actif :</strong> fermer le cours et essayer de redire l'essentiel. L'effort de recherche en mémoire crée la trace.",
                            "<strong>2. Répétition espacée :</strong> revoir à J+1, J+3, J+7, J+14 — pas 5 fois la veille.",
                            "<strong>3. Mélange (interleaving) :</strong> alterner les chapitres au lieu de finir l'un avant l'autre.",
                            "<strong>Le sommeil :</strong> c'est la nuit que le cerveau consolide. Réviser tard sans dormir est contre-productif.",
                        ],
                        [
                            "<strong>1. Active recall:</strong> close the lesson and try to restate the essentials. The effort of searching memory creates the trace.",
                            "<strong>2. Spaced repetition:</strong> review at D+1, D+3, D+7, D+14 — not 5 times the day before.",
                            "<strong>3. Interleaving:</strong> alternate chapters instead of finishing one before the other.",
                            "<strong>Sleep:</strong> the brain consolidates at night. Revising late without sleep is counter-productive.",
                        ],
                        [
                            "<strong>1. الاستدعاء النشط:</strong> أغلق الدرس وحاول إعادة الأساس. جهد البحث في الذاكرة يصنع الأثر.",
                            "<strong>2. التكرار المتباعد:</strong> راجع في اليوم+1، +3، +7، +14 — لا خمس مرات ليلة الامتحان.",
                            "<strong>3. المزج:</strong> نوّع الفصول بدل إنهاء واحد قبل الآخر.",
                            "<strong>النوم:</strong> الدماغ يرسّخ ليلاً. المراجعة المتأخرة دون نوم عكسية.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Schéma à dessiner au tableau :</strong> courbe de l'oubli — sans révision on oublie 70 % en 24 h ; chaque rappel espacé remonte la courbe plus haut et plus longtemps.",
                        "<strong>Diagram to draw on the board:</strong> the forgetting curve — without review we forget 70% in 24h; each spaced recall lifts the curve higher and longer.",
                        "<strong>مخطط ارسمه على السبورة:</strong> منحنى النسيان — دون مراجعة ننسى 70٪ في 24 ساعة؛ وكل استدعاء متباعد يرفع المنحنى أعلى وأطول.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séances 4 et 5 :</strong> vos fiches Cornell (séance 4) deviennent des flashcards, et le jury-IA de votre exposé (séance 5) devient un tuteur qui vous interroge. Chaque séance réutilise les outils des précédentes.",
                        "<strong>🔗 Reminder of sessions 4 and 5:</strong> your Cornell sheets (session 4) become flashcards, and your presentation AI-jury (session 5) becomes a tutor questioning you. Each session reuses previous tools.",
                        "<strong>🔗 تذكير بالحصتين 4 و5:</strong> بطاقات كورنيل (الحصة 4) تتحوّل إلى بطاقات استذكار، ولجنة تحكيم عرضك (الحصة 5) تتحوّل إلى مدرّس يستجوبك. كل حصة تعيد استعمال أدوات السابقات.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Les flashcards : 10 cartes qui valent 10 relectures",
                "Flashcards: 10 cards worth 10 rereads",
                "بطاقات الاستذكار: عشر بطاقات تساوي عشر قراءات",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une flashcard = une question d'un côté, la réponse de l'autre. On se teste, on trie (su / pas su), on revoit seulement les ratées. L'IA génère le paquet en 1 minute depuis votre fiche.",
                        "A flashcard = a question on one side, the answer on the other. You test yourself, sort (known / failed), and review only the failed ones. AI generates the deck in 1 minute from your sheet.",
                        "بطاقة الاستذكار = سؤال في جهة وجواب في الجهة الأخرى. تختبر نفسك، وتصنّف (عرفت / أخفقت)، وتراجع المخفَق فقط. يولّد الذكاء الاصطناعي الحزمة في دقيقة من بطاقتك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt modèle :</strong> « Voici ma fiche [coller]. Crée 10 flashcards : une question courte + réponse en 1 phrase. Numérote-les. »",
                            "<strong>Règle d'or :</strong> 1 carte = 1 fait. Si la réponse fait 5 lignes, découpez en 3 cartes.",
                            "<strong>Outils gratuits :</strong> Anki (répétition espacée automatique), Quizlet, ou simple papier.",
                            "<strong>En arabe aussi :</strong> l'IA génère les cartes dans la langue de votre fiche.",
                        ],
                        [
                            "<strong>Model prompt:</strong> \"Here is my sheet [paste]. Create 10 flashcards: one short question + 1-sentence answer. Number them.\"",
                            "<strong>Golden rule:</strong> 1 card = 1 fact. If the answer is 5 lines, split into 3 cards.",
                            "<strong>Free tools:</strong> Anki (automatic spaced repetition), Quizlet, or plain paper.",
                            "<strong>In Arabic too:</strong> AI generates the cards in your sheet's language.",
                        ],
                        [
                            "<strong>صياغة نموذجية:</strong> « هذه بطاقتي [الصق]. أنشئ عشر بطاقات: سؤال قصير + جواب في جملة. رقّمها ».",
                            "<strong>قاعدة ذهبية:</strong> بطاقة = معلومة واحدة. إذا كان الجواب خمسة أسطر، قسّمه إلى ثلاث بطاقات.",
                            "<strong>أدوات مجانية:</strong> Anki (تكرار متباعد تلقائي)، Quizlet، أو ورق بسيط.",
                            "<strong>بالعربية أيضاً:</strong> يولّد الذكاء الاصطناعي البطاقات بلغة بطاقتك.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> fiche « Present perfect » → carte 3 : Q « Quelle forme après have/has ? » / R « Le participe passé — ex : I have <strong>eaten</strong>. » Testez votre voisin : il répond sans regarder, vous montrez la réponse.",
                        "<strong>🧪 Concrete example:</strong> \"Present perfect\" sheet → card 3: Q \"Which form after have/has?\" / A \"The past participle — e.g. I have <strong>eaten</strong>.\" Test your neighbour: they answer without looking, you show the answer.",
                        "<strong>🧪 مثال ملموس:</strong> بطاقة « المضارع التام » ← بطاقة 3: س « ما الصيغة بعد have/has؟ » / ج « التصريف الثالث — مثال: I have <strong>eaten</strong> ». اختبر جارك: يجيب دون نظر وأنت تعرض الجواب.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "QCM corrigés et annales : s'entraîner comme le jour J",
                "Corrected quizzes and past papers: train like exam day",
                "اختبارات مصحّحة ومواضيع سابقة: تدرّب كيوم الامتحان",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Demandez à l'IA un QCM avec correction expliquée, puis faites-le SANS regarder le cours, chronomètre en main. L'analyse des erreurs vaut plus que le score.",
                        "Ask AI for a quiz with explained answers, then take it WITHOUT looking at the lesson, timer on. Analysing mistakes is worth more than the score.",
                        "اطلب من الذكاء الاصطناعي اختباراً مع تصحيح مفسَّر، ثم أجزه دون النظر إلى الدرس، بالمؤقّت. تحليل الأخطاء أهم من العلامة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt QCM :</strong> « Chapitre [coller]. 10 QCM à 4 choix, 1 seule bonne réponse, puis correction avec la phrase du cours qui justifie. »",
                            "<strong>Prompt annale :</strong> « Voici le sujet 2024 [coller]. Propose un sujet 2025 du même style + barème sur 20. »",
                            "<strong>Rituel d'analyse :</strong> pour chaque erreur, écrire la bonne règle en 1 phrase dans un carnet.",
                            "<strong>Piège :</strong> refaire le même QCM de mémoire donne une fausse confiance — demandez une version mélangée.",
                        ],
                        [
                            "<strong>Quiz prompt:</strong> \"Chapter [paste]. 10 MCQs with 4 options, 1 correct answer, then correction with the lesson sentence that justifies it.\"",
                            "<strong>Past-paper prompt:</strong> \"Here is the 2024 paper [paste]. Propose a 2025 paper in the same style + marking out of 20.\"",
                            "<strong>Analysis ritual:</strong> for each mistake, write the correct rule in 1 sentence in a notebook.",
                            "<strong>Trap:</strong> redoing the same quiz from memory gives false confidence — ask for a shuffled version.",
                        ],
                        [
                            "<strong>صياغة الاختبار:</strong> « الفصل [الصق]. عشر أسئلة بأربعة اختيارات، جواب صحيح واحد، ثم تصحيح مع جملة الدرس المبرِّرة ».",
                            "<strong>صياغة الموضوع:</strong> « هذا موضوع 2024 [الصق]. اقترح موضوع 2025 بنفس الأسلوب + سلّم من 20 ».",
                            "<strong>طقس التحليل:</strong> لكل خطأ، اكتب القاعدة الصحيحة في جملة بدفتر.",
                            "<strong>فخ:</strong> إعادة نفس الاختبار من الذاكرة تعطي ثقة كاذبة — اطلب نسخة مخلوطة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>⚠️ Ligne rouge :</strong> générer un QCM pour réviser = excellent. Photographier le sujet pendant l'examen pour le faire résoudre par l'IA = tricherie, sanction disciplinaire. Le diplôme obtenu en trichant ne vaut rien.",
                        "<strong>⚠️ Red line:</strong> generating a quiz to revise = excellent. Photographing the paper during the exam to have AI solve it = cheating, disciplinary sanction. A cheated diploma is worthless.",
                        "<strong>⚠️ خط أحمر:</strong> توليد اختبار للمراجعة = ممتاز. تصوير الموضوع أثناء الامتحان ليحلّه الذكاء الاصطناعي = غشّ وعقوبة تأديبية. شهادة بالغش لا تساوي شيئاً.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Le tuteur socratique : une IA qui vous interroge",
                "The Socratic tutor: an AI that questions you",
                "المدرّس السقراطي: ذكاء اصطناعي يستجوبك",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Au lieu de demander la réponse, demandez des questions : l'IA devient un professeur particulier infatigable qui ne donne la solution qu'après vos essais.",
                        "Instead of asking for the answer, ask for questions: AI becomes an tireless private tutor who only gives the solution after your attempts.",
                        "بدل طلب الجواب، اطلب أسئلة: يصبح الذكاء الاصطناعي مدرّساً خصوصياً لا يكلّ، لا يعطي الحل إلا بعد محاولاتك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt tuteur :</strong> « Tu es mon tuteur de [module]. Pose-moi une question à la fois sur [chapitre]. Si je me trompe, donne un indice, pas la réponse. 10 questions. »",
                            "<strong>Variante exposé :</strong> « Joue le jury : pose-moi 5 questions pièges sur mon sujet. »",
                            "<strong>Variante langue :</strong> « Corrige mon anglais phrase par phrase et explique chaque faute. »",
                        ],
                        [
                            "<strong>Tutor prompt:</strong> \"You are my [module] tutor. Ask me one question at a time about [chapter]. If I am wrong, give a hint, not the answer. 10 questions.\"",
                            "<strong>Presentation variant:</strong> \"Play the jury: ask me 5 tricky questions about my topic.\"",
                            "<strong>Language variant:</strong> \"Correct my English sentence by sentence and explain each mistake.\"",
                        ],
                        [
                            "<strong>صياغة المدرّس:</strong> « أنت مدرّسي في [الوحدة]. اسألني سؤالاً واحداً كل مرة عن [الفصل]. إذا أخطأت فأعطِ تلميحاً لا الجواب. عشرة أسئلة ».",
                            "<strong>نسخة العرض:</strong> « مثّل لجنة التحكيم: اطرح عليّ خمسة أسئلة صعبة عن موضوعي ».",
                            "<strong>نسخة اللغة:</strong> « صحّح إنجليزيتي جملة جملة واشرح كل خطأ ».",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "profiter",
            "titre": L(
                "Comment en profiter au maximum",
                "How to get the most out of it",
                "كيف تستفيد إلى أقصى حد",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Le cycle gagnant : générer → se tester SANS le cours → corriger → noter les erreurs → reprogrammer la révision des ratées à J+3.",
                        "The winning cycle: generate → test yourself WITHOUT the lesson → correct → note mistakes → reschedule failed items at D+3.",
                        "الدورة الرابحة: ولّد → اختبر نفسك دون الدرس → صحّح → سجّل الأخطاء → أعد برمجة المخفَق لليوم+3.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 7 :</strong> le tuteur socratique qui vous interroge deviendra un VRAI programme Python (assistant_chat.py) qui appelle Gemini. Vous passerez d'utilisateur à constructeur.",
                        "<strong>➡️ Bridge to session 7:</strong> the Socratic tutor questioning you will become a REAL Python program (assistant_chat.py) calling Gemini. You will move from user to builder.",
                        "<strong>➡️ جسر إلى الحصة 7:</strong> المدرّس السقراطي الذي يستجوبك سيصبح برنامج بايثون حقيقياً (assistant_chat.py) يستدعي Gemini. ستنتقل من مستعمِل إلى بانٍ.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Mélangez :</strong> flashcards + QCM + tuteur, jamais un seul format.",
                            "<strong>✅ Chronométrez :</strong> toujours avec le temps de l'examen réel.",
                            "<strong>✅ Carnet d'erreurs :</strong> 1 phrase par erreur, relu la veille.",
                            "<strong>✅ Demandez des variantes :</strong> « même chapitre, 10 questions différentes ».",
                        ],
                        [
                            "<strong>✅ Mix:</strong> flashcards + quiz + tutor, never a single format.",
                            "<strong>✅ Time yourself:</strong> always with real exam timing.",
                            "<strong>✅ Mistake notebook:</strong> 1 sentence per mistake, reread the day before.",
                            "<strong>✅ Ask for variants:</strong> \"same chapter, 10 different questions\".",
                        ],
                        [
                            "<strong>✅ نوّع:</strong> بطاقات + اختبار + مدرّس، لا صيغة واحدة أبداً.",
                            "<strong>✅ اضبط الوقت:</strong> دائماً بتوقيت الامتحان الحقيقي.",
                            "<strong>✅ دفتر الأخطاء:</strong> جملة لكل خطأ، يُراجَع ليلة الامتحان.",
                            "<strong>✅ اطلب بدائل:</strong> « نفس الفصل، عشرة أسئلة مختلفة ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> réviser avec le corrigé sous les yeux, refaire le même QCM appris par cœur, réviser 6 h d'affilée sans pause (25 min de travail + 5 min de pause).",
                        "<strong>❌ Mistakes to avoid:</strong> revising with the answers in front of you, redoing the same memorised quiz, revising 6h straight without breaks (25 min work + 5 min break).",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> المراجعة والتصحيح أمامك، إعادة نفس الاختبار المحفوظ، مراجعة 6 ساعات متواصلة دون توقف (25 دقيقة عمل + 5 دقائق راحة).",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["", "Mauvais usage", "Bon usage"],
                        ["", "Bad use", "Good use"],
                        ["", "استعمال سيئ", "استعمال جيد"],
                    ),
                    "rows": L(
                        [
                            ["Demande", "« Donne-moi les réponses du chapitre 3. »", "« Interroge-moi sur le chapitre 3, une question à la fois, sans donner les réponses. »"],
                            ["Résultat", "Lecture passive, illusion de savoir.", "Rappel actif, vraies traces en mémoire."],
                        ],
                        [
                            ["Prompt", "\"Give me the chapter 3 answers.\"", "\"Quiz me on chapter 3, one question at a time, without giving answers.\""],
                            ["Result", "Passive reading, illusion of knowledge.", "Active recall, real memory traces."],
                        ],
                        [
                            ["الطلب", "« أعطني أجوبة الفصل الثالث »", "« استجوبني في الفصل الثالث، سؤالاً واحداً كل مرة، دون إعطاء الأجوبة »"],
                            ["النتيجة", "قراءة سلبية ووهم المعرفة.", "استدعاء نشط وآثار حقيقية في الذاكرة."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Pourquoi se tester est-il plus efficace que relire ?",
                "Why is testing yourself more effective than rereading?",
                "لماذا اختبار النفس أنفع من إعادة القراءة؟",
            ),
            "r": L(
                "Parce que l'effort de retrouver l'information en mémoire crée une trace durable, alors que relire donne seulement une impression de familiarité.",
                "Because the effort of retrieving information from memory creates a lasting trace, while rereading only gives a feeling of familiarity.",
                "لأن جهد استرجاع المعلومة من الذاكرة يصنع أثراً دائماً، بينما إعادة القراءة تعطي إحساساً بالألفة فقط.",
            ),
        },
        {
            "q": L(
                "Que faire après un QCM raté à 6/10 ?",
                "What to do after a failed 6/10 quiz?",
                "ماذا تفعل بعد اختبار مخفَق 6/10؟",
            ),
            "r": L(
                "Noter chaque erreur en 1 phrase dans le carnet, revoir les points ratés à J+3, puis demander une version mélangée du QCM.",
                "Write each mistake in 1 sentence in the notebook, review failed points at D+3, then ask for a shuffled version of the quiz.",
                "سجّل كل خطأ في جملة بالدفتر، وراجع النقاط المخفَقة في اليوم+3، ثم اطلب نسخة مخلوطة من الاختبار.",
            ),
        },
        {
            "q": L(
                "Quelle est la différence entre demander la réponse et demander à être interrogé ?",
                "What is the difference between asking for the answer and asking to be questioned?",
                "ما الفرق بين طلب الجواب وطلب الاستجواب؟",
            ),
            "r": L(
                "Demander la réponse = lecture passive. Demander à être interrogé (tuteur socratique) = rappel actif : c'est votre cerveau qui travaille.",
                "Asking for the answer = passive reading. Asking to be questioned (Socratic tutor) = active recall: your brain works.",
                "طلب الجواب = قراءة سلبية. طلب الاستجواب (المدرّس السقراطي) = استدعاء نشط: دماغك هو من يعمل.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "Avec votre fiche de cours : 1) générez 10 flashcards avec le prompt modèle ; 2) testez votre voisin (il répond sans regarder) ; 3) notez les cartes ratées et reprogrammez-les à J+3.",
            "With your lesson sheet: 1) generate 10 flashcards with the model prompt; 2) test your neighbour (they answer without looking); 3) note failed cards and reschedule them at D+3.",
            "ببطاقة درسك: 1) ولّد عشر بطاقات بالصياغة النموذجية؛ 2) اختبر جارك (يجيب دون نظر)؛ 3) سجّل البطاقات المخفَقة وأعد برمجتها لليوم+3.",
        ),
        "demarche": L(
            "1) Copiez le prompt modèle et collez votre fiche. 2) Vérifiez que chaque carte a 1 question + 1 réponse courte (découpez sinon). 3) Cachez les réponses et interrogez-vous à voix haute. 4) Triez : su / pas su.",
            "1) Copy the model prompt and paste your sheet. 2) Check each card has 1 question + 1 short answer (split otherwise). 3) Hide answers and quiz yourself aloud. 4) Sort: known / failed.",
            "1) انسخ الصياغة النموذجية والصق بطاقتك. 2) تحقق أن كل بطاقة فيها سؤال + جواب قصير (قسّم وإلا). 3) أخفِ الأجوبة واستجوب نفسك جهراً. 4) صنّف: عرفت / أخفقت.",
        ),
        "solution": L(
            "Exemple de paquet réussi : 10 cartes numérotées, questions courtes (« Quelle est la règle d'accord du participe avec avoir ? »), réponses d'1 phrase, 2 cartes jugées trop longues découpées en 4, planning noté : revoir les 3 ratées à J+3.",
            "Example of a good deck: 10 numbered cards, short questions (\"What is the past participle agreement rule with avoir?\"), 1-sentence answers, 2 overlong cards split into 4, schedule noted: review the 3 failed at D+3.",
            "مثال حزمة ناجحة: عشر بطاقات مرقّمة، أسئلة قصيرة، أجوبة من جملة، بطاقتان طويلتان قُسّمتا إلى 4، وجدولة مدوّنة: مراجعة الثلاث المخفَقة في اليوم+3.",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Réviser avec les flashcards et Anki (tutoriel)",
                "Revise with flashcards and Anki (tutorial)",
                "المراجعة بالبطاقات وAnki (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=anki+flashcards+tutoriel+francais+revision",
            "langue": "fr",
            "concept": L(
                "Pour installer Anki et créer votre premier paquet depuis les cartes générées par l'IA.",
                "To install Anki and create your first deck from AI-generated cards.",
                "لتثبيت Anki وإنشاء أول حزمة من البطاقات المولّدة بالذكاء الاصطناعي.",
            ),
        },
        {
            "titre": L(
                "كيف تراجع بذكاء؟ الاستدعاء النشط والتكرار المتباعد",
                "How to revise smartly? Active recall and spaced repetition",
                "كيف تراجع بذكاء؟ الاستدعاء النشط والتكرار المتباعد",
            ),
            "url": "https://www.youtube.com/results?search_query=active+recall+spaced+repetition+study+technique",
            "langue": "ar",
            "concept": L(
                "La science de la mémoire expliquée simplement, avec des exemples d'étudiants.",
                "The science of memory simply explained, with student examples.",
                "علم الذاكرة مبسّطاً، مع أمثلة من الطلبة.",
            ),
        },
        {
            "titre": L(
                "Générer des QCM avec ChatGPT pour réviser",
                "Generate quizzes with ChatGPT to revise",
                "توليد اختبارات بـ ChatGPT للمراجعة",
            ),
            "url": "https://www.youtube.com/results?search_query=generer+QCM+chatgpt+reviser+examen",
            "langue": "fr",
            "concept": L(
                "Voir en vidéo la méthode « fiche → QCM corrigé → analyse d'erreurs ».",
                "See the \"sheet → corrected quiz → mistake analysis\" method on video.",
                "شاهد بالفيديو منهجية « بطاقة → اختبار مصحّح → تحليل الأخطاء ».",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "Se tester bat relire : le rappel actif crée la mémoire.",
                "Testing beats rereading: active recall builds memory.",
                "الاختبار يغلب إعادة القراءة: الاستدعاء النشط يبني الذاكرة.",
            ),
            L(
                "Espacer : J+1, J+3, J+7, J+14 — jamais tout la veille.",
                "Space out: D+1, D+3, D+7, D+14 — never everything the day before.",
                "باعد: اليوم+1، +3، +7، +14 — لا كل شيء ليلة الامتحان.",
            ),
            L(
                "1 flashcard = 1 question + 1 réponse courte.",
                "1 flashcard = 1 question + 1 short answer.",
                "بطاقة = سؤال + جواب قصير.",
            ),
            L(
                "QCM chronométré sans le cours + carnet d'erreurs (1 phrase par erreur).",
                "Timed quiz without the lesson + mistake notebook (1 sentence per mistake).",
                "اختبار بمؤقّت دون الدرس + دفتر أخطاء (جملة لكل خطأ).",
            ),
            L(
                "Tuteur socratique : l'IA interroge, vous répondez, elle indice.",
                "Socratic tutor: AI questions, you answer, it hints.",
                "المدرّس السقراطي: الذكاء يستجوب، وأنت تجيب، وهو يلمّح.",
            ),
        ],
        "analogies": [
            L(
                "Le sport : regarder ne muscle pas, soulever oui — réviser, c'est soulever.",
                "Sport: watching does not build muscle, lifting does — revising is lifting.",
                "الرياضة: المشاهدة لا تبني العضلات، الرفع نعم — والمراجعة رفع.",
            ),
            L(
                "Le carnet d'erreurs, c'est la trousse de secours de la veille d'examen.",
                "The mistake notebook is the first-aid kit of exam eve.",
                "دفتر الأخطاء هو حقيبة الإسعاف ليلة الامتحان.",
            ),
            L(
                "Le tuteur socratique, c'est un sparring-partner : il frappe doucement pour vous entraîner.",
                "The Socratic tutor is a sparring partner: it hits softly to train you.",
                "المدرّس السقراطي شريك تدريب: يضرب بلطف ليدرّبك.",
            ),
        ],
        "exemples": [
            L(
                "Fiche de psycho → 10 flashcards → test du voisin → 3 ratées à J+3.",
                "Psychology sheet → 10 flashcards → neighbour test → 3 failed at D+3.",
                "بطاقة علم النفس → عشر بطاقات → اختبار الجار → 3 مخفَقة لليوم+3.",
            ),
            L(
                "Annale 2024 recopiée → sujet 2025 généré + barème → 1 h chrono.",
                "2024 past paper copied → 2025 paper generated + marking → 1h timed.",
                "موضوع 2024 منسوخ → موضوع 2025 مولّد + سلّم → ساعة بمؤقّت.",
            ),
            L(
                "« Interroge-moi sur les temps anglais, un par un » → 10 questions, 2 indices.",
                "\"Quiz me on English tenses, one by one\" → 10 questions, 2 hints.",
                "« استجوبني في الأزمنة الإنجليزية واحداً واحداً » → عشرة أسئلة وتلميحان.",
            ),
        ],
        "analogie_finale": L(
            "🏁 Réviser avec l'IA, c'est comme avoir un coach sportif personnel : il prépare les exercices, compte les répétitions et vous encourage — mais les muscles, c'est vous qui les construisez.",
            "🏁 Revising with AI is like having a personal sports coach: it prepares exercises, counts reps and cheers you on — but you build the muscles.",
            "🏁 المراجعة بالذكاء الاصطناعي كمدرّب رياضي شخصي: يحضّر التمارين، ويعدّ التكرارات، ويشجّعك — لكن العضلات أنت من يبنيها.",
        ),
        "quiz": [
            {
                "q": L(
                    "Pourquoi relire 5 fois donne une fausse confiance ?",
                    "Why does rereading 5 times give false confidence?",
                    "لماذا إعادة القراءة خمس مرات تعطي ثقة كاذبة؟",
                ),
                "options": L(
                    ["Parce que le texte change", "Parce que la familiarité ressemble au savoir sans être la mémoire", "Parce que c'est interdit", "Parce que c'est trop rapide"],
                    ["Because the text changes", "Because familiarity feels like knowledge without being memory", "Because it is forbidden", "Because it is too fast"],
                    ["لأن النص يتغيّر", "لأن الألفة تشبه المعرفة دون أن تكون ذاكرة", "لأنه ممنوع", "لأنه سريع جداً"],
                ),
                "answer": 1,
                "exp": L(
                    "Relire rend le texte familier, mais seul l'effort de rappel (se tester sans le cours) crée une trace durable.",
                    "Rereading makes text familiar, but only retrieval effort (testing without the lesson) creates a lasting trace.",
                    "إعادة القراءة تجعل النص مألوفاً، لكن جهد الاسترجاع وحده (الاختبار دون الدرس) يصنع أثراً دائماً.",
                ),
            },
            {
                "q": L(
                    "Quel est le bon planning de révision espacée ?",
                    "What is the right spaced revision schedule?",
                    "ما الجدولة الصحيحة للمراجعة المتباعدة؟",
                ),
                "options": L(
                    ["Tout la veille", "J+1, J+3, J+7, J+14", "Une fois par mois", "Jamais, c'est inutile"],
                    ["Everything the day before", "D+1, D+3, D+7, D+14", "Once a month", "Never, it is useless"],
                    ["كل شيء ليلة الامتحان", "اليوم+1، +3، +7، +14", "مرة في الشهر", "أبداً، لا فائدة"],
                ),
                "answer": 1,
                "exp": L(
                    "Revoir juste avant d'oublier (J+1, J+3, J+7, J+14) consolide la mémoire avec peu d'effort.",
                    "Reviewing just before forgetting (D+1, D+3, D+7, D+14) consolidates memory with little effort.",
                    "المراجعة قبيل النسيان (اليوم+1، +3، +7، +14) ترسّخ الذاكرة بجهد قليل.",
                ),
            },
            {
                "q": L(
                    "Que contient une bonne flashcard ?",
                    "What does a good flashcard contain?",
                    "ماذا تحوي بطاقة الاستذكار الجيدة؟",
                ),
                "options": L(
                    ["Tout un chapitre", "1 question + 1 réponse courte", "Seulement une image", "La correction complète"],
                    ["A whole chapter", "1 question + 1 short answer", "Only a picture", "The full correction"],
                    ["فصلاً كاملاً", "سؤالاً + جواباً قصيراً", "صورة فقط", "التصحيح الكامل"],
                ),
                "answer": 1,
                "exp": L(
                    "1 carte = 1 fait. Les réponses longues doivent être découpées en plusieurs cartes.",
                    "1 card = 1 fact. Long answers must be split into several cards.",
                    "بطاقة = معلومة واحدة. الأجوبة الطويلة تُقسَّم إلى عدة بطاقات.",
                ),
            },
            {
                "q": L(
                    "Que faire d'une erreur de QCM ?",
                    "What to do with a quiz mistake?",
                    "ماذا تفعل بخطأ في الاختبار؟",
                ),
                "options": L(
                    ["L'ignorer", "L'écrire en 1 phrase dans le carnet et revoir le point à J+3", "Refaire le même QCM aussitôt", "Accuser l'IA"],
                    ["Ignore it", "Write it in 1 sentence in the notebook and review at D+3", "Redo the same quiz at once", "Blame AI"],
                    ["تجاهله", "اكتبه في جملة بالدفتر وراجع النقطة في اليوم+3", "أعد نفس الاختبار فوراً", "لُم الذكاء الاصطناعي"],
                ),
                "answer": 1,
                "exp": L(
                    "L'erreur est une information : notée et revue à J+3, elle ne se reproduit plus.",
                    "A mistake is information: noted and reviewed at D+3, it will not happen again.",
                    "الخطأ معلومة: مسجَّلاً ومُراجَعاً في اليوم+3، لن يتكرر.",
                ),
            },
            {
                "q": L(
                    "Quel prompt fait travailler VOTRE cerveau ?",
                    "Which prompt makes YOUR brain work?",
                    "أي صياغة تُشغّل دماغك أنت؟",
                ),
                "options": L(
                    ["« Donne-moi les réponses »", "« Interroge-moi une question à la fois, sans donner les réponses »", "« Résume tout »", "« Fais mon devoir »"],
                    ["\"Give me the answers\"", "\"Quiz me one question at a time, without giving answers\"", "\"Summarise everything\"", "\"Do my homework\""],
                    ["« أعطني الأجوبة »", "« استجوبني سؤالاً واحداً كل مرة دون إعطاء الأجوبة »", "« لخّص كل شيء »", "« أنجز واجبي »"],
                ),
                "answer": 1,
                "exp": L(
                    "Le tuteur socratique (questions + indices) déclenche le rappel actif ; demander les réponses = lecture passive.",
                    "The Socratic tutor (questions + hints) triggers active recall; asking for answers = passive reading.",
                    "المدرّس السقراطي (أسئلة + تلميحات) يطلق الاستدعاء النشط؛ وطلب الأجوبة = قراءة سلبية.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Fabrique de flashcards : générer 10 cartes depuis sa fiche, tester son voisin, trier su/pas su.",
            "Flashcard factory: generate 10 cards from your sheet, test your neighbour, sort known/failed.",
            "مصنع البطاقات: ولّد عشر بطاقات من بطاقتك، واختبر جارك، وصنّف عرفت/أخفقت.",
        ),
        L(
            "QCM chrono : générer un QCM de 10 questions, le faire en 15 min sans le cours, analyser les erreurs.",
            "Timed quiz: generate a 10-question quiz, take it in 15 min without the lesson, analyse mistakes.",
            "اختبار بمؤقّت: ولّد اختباراً من عشرة أسئلة، وأجزه في 15 دقيقة دون الدرس، وحلّل الأخطاء.",
        ),
        L(
            "Duo socratique : l'un joue le tuteur-IA (questions + indices), l'autre répond ; puis on inverse.",
            "Socratic duo: one plays the AI-tutor (questions + hints), the other answers; then swap.",
            "ثنائي سقراطي: أحدهما يمثّل المدرّس-الذكاء (أسئلة + تلميحات) والآخر يجيب؛ ثم يتبادلان.",
        ),
        L(
            "Examen blanc : sujet généré depuis une annale, 30 min chrono, correction croisée en binôme.",
            "Mock exam: paper generated from a past paper, 30 min timed, cross-correction in pairs.",
            "امتحان أبيض: موضوع مولّد من سابق، 30 دقيقة بمؤقّت، وتصحيح متبادل ثنائياً.",
        ),
    ],
    "retenir": [
        L(
            "Tester > relire : le rappel actif construit la mémoire.",
            "Testing > rereading: active recall builds memory.",
            "الاختبار > إعادة القراءة: الاستدعاء النشط يبني الذاكرة.",
        ),
        L(
            "Espacer J+1, J+3, J+7, J+14 ; dormir consolide.",
            "Space D+1, D+3, D+7, D+14; sleep consolidates.",
            "باعد اليوم+1، +3، +7، +14؛ والنوم يرسّخ.",
        ),
        L(
            "Flashcards : 1 carte = 1 question + 1 réponse courte.",
            "Flashcards: 1 card = 1 question + 1 short answer.",
            "البطاقات: بطاقة = سؤال + جواب قصير.",
        ),
        L(
            "QCM chronométré sans cours + carnet d'erreurs.",
            "Timed quiz without lesson + mistake notebook.",
            "اختبار بمؤقّت دون درس + دفتر أخطاء.",
        ),
        L(
            "Tuteur socratique : jamais de réponse directe, toujours une question d'abord.",
            "Socratic tutor: never a direct answer, always a question first.",
            "المدرّس السقراطي: لا جواب مباشر أبداً، بل سؤال أولاً دائماً.",
        ),
    ],
    "glossaire": [
        {
            "term": "Rappel actif",
            "term_en": "Active recall",
            "def_fr": "Effort de retrouver une information en mémoire sans regarder le cours ; la méthode de révision la plus efficace.",
            "def_en": "The effort of retrieving information from memory without looking at the lesson; the most effective revision method.",
            "def_ar": "جهد استرجاع معلومة من الذاكرة دون النظر إلى الدرس؛ أنجع طريقة مراجعة.",
        },
        {
            "term": "Répétition espacée",
            "term_en": "Spaced repetition",
            "def_fr": "Revoir une notion à intervalles croissants (J+1, J+3, J+7…) pour contrer l'oubli.",
            "def_en": "Reviewing a notion at increasing intervals (D+1, D+3, D+7…) to fight forgetting.",
            "def_ar": "مراجعة المعلومة بفواصل متزايدة (اليوم+1، +3، +7…) لمقاومة النسيان.",
        },
        {
            "term": "Flashcard",
            "term_en": "Flashcard",
            "def_fr": "Carte question/réponse pour se tester rapidement, idéale avec Anki.",
            "def_en": "A question/answer card for quick self-testing, ideal with Anki.",
            "def_ar": "بطاقة سؤال/جواب للاختبار السريع، مثالية مع Anki.",
        },
        {
            "term": "Tuteur socratique",
            "term_en": "Socratic tutor",
            "def_fr": "Usage de l'IA qui pose des questions et donne des indices au lieu de livrer les réponses.",
            "def_en": "An AI use where it asks questions and gives hints instead of delivering answers.",
            "def_ar": "استعمال للذكاء الاصطناعي يطرح أسئلة ويعطي تلميحات بدل تقديم الأجوبة.",
        },
        {
            "term": "Annale",
            "term_en": "Past paper",
            "def_fr": "Sujet d'examen d'une année précédente, base idéale pour simuler le jour J.",
            "def_en": "A previous year's exam paper, the ideal base to simulate exam day.",
            "def_ar": "موضوع امتحان سنة سابقة، الأساس المثالي لمحاكاة يوم الامتحان.",
        },
    ],
    "dialogues_fr": """# Séance 06 — Dialogues pédagogiques (Français)

## Dialogue A — « Je connais mon cours… ou je le reconnais ? » (25 min)

**Personnages :** Sara (étudiante sûre d'elle), Karim (camarade coach), Mme Amel (enseignante).

---

Sara : J'ai relu le chapitre 4 trois fois. Je le connais par cœur !

Karim : Test éclair : ferme le cahier. C'est quoi, la différence entre révision espacée et bachotage ?

Sara : Euh… attends… c'est… (silence) Bon, je reconnais le mot, mais je ne sais plus le dire.

Mme Amel : Voilà la différence entre reconnaître et connaître. Relire fabrique de la reconnaissance. Se tester fabrique de la connaissance.

Karim : Demande à l'IA 10 flashcards du chapitre, et on rejoue dans 10 minutes. Sans regarder, cette fois !

Sara : Et si je rate ?

Mme Amel : Rater, c'est le plan ! Chaque carte ratée reprogrammée à J+3, c'est une faute en moins le jour J.

---

## Dialogue B — « Le tuteur qui ne donne jamais la réponse » (15 min)

**Personnages :** Bilal (étudiant), l'IA-tuteur (jouée par une camarade), son amie Rania.

---

Bilal : Donne-moi la réponse à la question 3 du TD.

IA-tuteur : Non. Qu'as-tu essayé d'abord ?

Bilal : Rien… c'est pour ça que je demande !

IA-tuteur : Alors voici un indice : relis la définition de la page 2, et dis-moi quel mot-clé manque dans ta réponse.

Bilal (réfléchit) : … « espacée » ? La répétition doit être espacée ?

Rania : Tu vois ? Tu savais presque. Le tuteur socratique ne te vole pas l'effort — il te le rend.

Bilal : D'accord : désormais, j'interdis à mon IA de me donner la réponse du premier coup !

---

## Mini-rôle à jouer (3 min par binôme)
L'un demande « les réponses du chapitre », l'autre reformule en prompt de tuteur socratique (« interroge-moi, un indice à la fois »). Échangez, puis choisissez la meilleure reformulation à afficher en classe.
""",
    "dialogues_en": """# Session 06 — Classroom dialogues (English)

## Dialogue A — "I know my lesson… or do I recognise it?" (25 min)

**Characters:** Sara (a confident student), Karim (a coach classmate), Mrs Amel (teacher).

---

Sara: I reread chapter 4 three times. I know it by heart!

Karim: Quick test: close the notebook. What is the difference between spaced review and cramming?

Sara: Er… wait… it is… (silence) Well, I recognise the word, but I cannot say it any more.

Mrs Amel: That is the difference between recognising and knowing. Rereading builds recognition. Testing builds knowledge.

Karim: Ask AI for 10 flashcards on the chapter, and we play again in 10 minutes. Without looking, this time!

Sara: And if I fail?

Mrs Amel: Failing is the plan! Each failed card rescheduled at D+3 is one less mistake on exam day.

---

## Dialogue B — "The tutor who never gives the answer" (15 min)

**Characters:** Bilal (student), the AI-tutor (played by a classmate), his friend Rania.

---

Bilal: Give me the answer to tutorial question 3.

AI-tutor: No. What did you try first?

Bilal: Nothing… that is why I am asking!

AI-tutor: Then here is a hint: reread the definition on page 2, and tell me which keyword is missing from your answer.

Bilal (thinking): … "spaced"? Repetition must be spaced?

Rania: You see? You almost knew. The Socratic tutor does not steal your effort — it gives it back to you.

Bilal: Agreed: from now on, I forbid my AI from giving me the answer straight away!

---

## Mini role-play (3 min per pair)
One asks for "the chapter answers", the other reformulates as a Socratic tutor prompt ("quiz me, one hint at a time"). Swap, then pick the best reformulation to display in class.
""",
}
