# -*- coding: utf-8 -*-
"""Séance 01 — Qu'est-ce que l'IA ? Introduction et démystification (PEP 2A — ENS).
Pédagogie revisitée : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar=None):
    return {"fr": fr, "en": en, "ar": ar if ar is not None else en}


SEANCE = {
    "num": 1,
    "slug": "seance-01",
    "icon": "🤖",
    "titles": L(
        "Qu'est-ce que l'IA ? Introduction et démystification",
        "What is AI? Introduction and demystification",
        "ما هو الذكاء الاصطناعي؟ مدخل وإزالة الغموض",
    ),
    "descriptions": L(
        "Ouvrir un chatbot, poser tes 2 premières questions avec des prompts prêts, juger les réponses et repartir avec ta première fiche d'usage — ta toute première interaction avec une IA, guidée pas à pas.",
        "Open a chatbot, ask your first 2 questions with ready prompts, judge the answers and leave with your first usage sheet — your very first AI interaction, guided step by step.",
        "افتح روبوت دردشة واطرح أول سؤالين بصياغات جاهزة واحكم على الأجوبة واخرج بأول بطاقة استعمال — أول تفاعل لك مع الذكاء الاصطناعي خطوة بخطوة.",
    ),
    "duration": "1 h 30",
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "💡 Pourquoi c'est utile pour toi",
                "💡 Why it is useful for you",
                "💡 لماذا هو مفيد لك",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "L'IA va te servir tous les jours à l'université : comprendre un cours difficile, préparer un exposé, réviser un examen. Mais si tu lui parles mal, elle te donne des réponses inutiles. Cette séance t'apprend à bien lui parler dès le départ — en 15 minutes, avec tes doigts, pas avec de la théorie.",
                        "AI will serve you every day at university: understanding a hard lesson, preparing a talk, revising an exam. But if you talk to it badly, it gives useless answers. This session teaches you to talk to it well from the start — in 15 minutes, with your fingers, not theory.",
                        "سيخدمك الذكاء كل يوم في الجامعة: فهم درس صعب وتحضير عرض ومراجعة امتحان. لكن إن حدّثته بسوء أعطاك أجوبة لا تنفع. تعلّمك هذه الحصة مخاطبته جيداً من البداية — في 15 دقيقة وبأصابعك لا بالنظرية.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "🧠 Les 3 idées essentielles",
                "🧠 The 3 key ideas",
                "🧠 الأفكار الأساسية الثلاث",
            ),
            "blocks": [
                {
                    "t": "ul",
                    **L(
                        [
                            "L'IA ne « cherche » pas une réponse : elle prédit le mot suivant, mot après mot, d'après des milliards d'exemples.",
                            "Elle peut être très convaincante et se tromper complètement : on appelle ça une « hallucination ».",
                            "La qualité de sa réponse dépend de la qualité de ta question : précis + format + public visé.",
                        ],
                        [
                            "AI does not \"look up\" an answer: it predicts the next word, word after word, from billions of examples.",
                            "It can be very convincing and completely wrong: this is called a \"hallucination\".",
                            "Its answer quality depends on your question quality: precise + format + audience.",
                        ],
                        [
                            "لا « يبحث » الذكاء عن جواب: بل يتنبأ بالكلمة التالية كلمة كلمة من مليارات الأمثلة.",
                            "قد يكون مقنعاً جداً ومخطئاً تماماً: تسمى هذه « الهلوسة ».",
                            "جودة جوابه تتوقف على جودة سؤالك: دقيق + صيغة + جمهور مستهدَف.",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "🛠️ Comment faire — pas à pas",
                "🛠️ How to do it — step by step",
                "🛠️ كيف تفعل — خطوة بخطوة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "<strong>Étape 1 — Ouvre ChatGPT (2 min) :</strong> va sur chatgpt.com → clique « Sign up » → crée un compte gratuit (e-mail suffit) → clique « New chat ». Tu vois une grande barre vide en bas : c'est là qu'on tape.",
                        "<strong>Step 1 — Open ChatGPT (2 min):</strong> go to chatgpt.com → click \"Sign up\" → create a free account (e-mail is enough) → click \"New chat\". You see a big empty bar below: that is where you type.",
                        "<strong>الخطوة 1 — افتح ChatGPT (دقيقتان):</strong> ادخل chatgpt.com ← انقر « Sign up » ← أنشئ حساباً مجانياً (يكفي بريد) ← انقر « New chat ». ترى شريطاً فارغاً كبيراً أسفل: هناك تكتب.",
                    ),
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Étape 2 — Pose ta première question :</strong> copie-colle exactement ceci, puis appuie sur Envoyer.",
                        "<strong>Step 2 — Ask your first question:</strong> copy-paste exactly this, then press Send.",
                        "<strong>الخطوة 2 — اطرح أول سؤال:</strong> انسخ والصق هذا حرفياً ثم اضغط إرسال.",
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Explique-moi ce qu'est l'intelligence artificielle comme si j'avais 12 ans, en 3 phrases.",
                    "en": "Explain to me what artificial intelligence is as if I were 12 years old, in 3 sentences.",
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Ce que tu vas voir :</strong> une réponse courte et simple. Si elle fait 20 lignes, ce n'est pas grave : c'est parce que tu n'as pas précisé le format. On corrige ça à l'étape suivante.",
                        "<strong>What you will see:</strong> a short, simple answer. If it is 20 lines, no problem: you did not specify the format. We fix that next.",
                        "<strong>ما ستراه:</strong> جواباً قصيراً بسيطاً. إذا كان 20 سطراً فلا بأس: لأنك لم تحدد الصيغة. سنصحح ذلك تالياً.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> ajoute toujours à la fin de ton prompt « en X phrases » ou « en X lignes ». L'IA obéit au format que tu imposes.",
                        "<strong>Tip:</strong> always add at the end of your prompt \"in X sentences\" or \"in X lines\". AI obeys the format you set.",
                        "<strong>نصيحة:</strong> أضف دائماً في نهاية صياغتك « في X جمل » أو « في X أسطر ». يطيع الذكاء الصيغة التي تفرضها.",
                    ),
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Étape 3 — Pose une 2e question</strong> (dans le MÊME chat) :",
                        "<strong>Step 3 — Ask a 2nd question</strong> (in the SAME chat):",
                        "<strong>الخطوة 3 — اطرح سؤالاً ثانياً</strong> (في نفس الدردشة):",
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Donne-moi 3 exemples d'IA que j'utilise sans le savoir dans ma vie quotidienne.",
                    "en": "Give me 3 examples of AI I use without knowing it in my daily life.",
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Ce que tu vas voir :</strong> probablement la reconnaissance faciale du téléphone, les recommandations Netflix/YouTube, le correcteur d'orthographe. Ce sont des IA que tu utilises tous les jours.",
                        "<strong>What you will see:</strong> probably phone face recognition, Netflix/YouTube recommendations, the spellchecker. These are AIs you use every day.",
                        "<strong>ما ستراه:</strong> غالباً التعرّف على الوجه في الهاتف وتوصيات Netflix/YouTube ومصحح الإملاء. هذه ذكاءات تستعملها كل يوم.",
                    ),
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Étape 4 — Vérifie si l'IA invente :</strong> demande-lui « Donne-moi les sources de tes informations. » S'il donne des liens, clique dessus. S'il n'en donne pas ou s'ils ne marchent pas, tu viens de découvrir une « hallucination » : l'IA a inventé avec assurance.",
                        "<strong>Step 4 — Check whether AI invents:</strong> ask it \"Give me the sources of your information.\" If it gives links, click them. If it gives none or they do not work, you just discovered a \"hallucination\": AI invented confidently.",
                        "<strong>الخطوة 4 — تحقق هل يختلق الذكاء:</strong> اسأله « أعطني مصادر معلوماتك ». إذا أعطى روابط فانقرها. وإذا لم يعطِ أو لم تعمل فقد اكتشفت « هلوسة »: اختلق الذكاء بثقة.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "📌 Exemples réels",
                "📌 Real examples",
                "📌 أمثلة حقيقية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "<strong>Exemple 1 — Résumer un cours difficile :</strong> ce que tu tapes :",
                        "<strong>Example 1 — Summarise a hard lesson:</strong> what you type:",
                        "<strong>المثال 1 — تلخيص درس صعب:</strong> ما تكتبه:",
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Résume ce paragraphe en 5 points clés pour un étudiant de 2ème année : [colle ton paragraphe]",
                    "en": "Summarise this paragraph in 5 key points for a 2nd-year student: [paste your paragraph]",
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Ce que l'IA répond :</strong> une liste de 5 points courts et clairs.",
                        "<strong>What AI answers:</strong> a list of 5 short, clear points.",
                        "<strong>ما يجيبه الذكاء:</strong> قائمة من 5 نقاط قصيرة واضحة.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> commence par « Tu es un professeur qui explique à des débutants » → la réponse sera plus pédagogique.",
                        "<strong>Tip:</strong> start with \"You are a teacher explaining to beginners\" → the answer will be more didactic.",
                        "<strong>نصيحة:</strong> ابدأ بـ « أنت أستاذ يشرح للمبتدئين » ← سيكون الجواب أكثر بيداغوجية.",
                    ),
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Exemple 2 — Comprendre un mot inconnu :</strong> ce que tu tapes :",
                        "<strong>Example 2 — Understand an unknown word:</strong> what you type:",
                        "<strong>المثال 2 — فهم كلمة مجهولة:</strong> ما تكتبه:",
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Explique-moi le mot « scaffolding » en pédagogie, avec un exemple concret de classe.",
                    "en": "Explain to me the word \"scaffolding\" in pedagogy, with a concrete classroom example.",
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Ce que l'IA répond :</strong> définition + exemple.",
                        "<strong>What AI answers:</strong> definition + example.",
                        "<strong>ما يجيبه الذكاء:</strong> تعريف + مثال.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> si tu ne comprends toujours pas, ajoute « reformule encore plus simplement ».",
                        "<strong>Tip:</strong> if you still do not get it, add \"rephrase even more simply\".",
                        "<strong>نصيحة:</strong> إذا لم تفهم بعدُ فأضف « أعد الصياغة ببساطة أكبر ».",
                    ),
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Exemple 3 — Trouver une erreur dans ton texte :</strong> ce que tu tapes :",
                        "<strong>Example 3 — Find a mistake in your text:</strong> what you type:",
                        "<strong>المثال 3 — إيجاد خطأ في نصك:</strong> ما تكتبه:",
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Corrige les fautes dans ce texte et explique chaque correction : [ton texte]",
                    "en": "Fix the mistakes in this text and explain each correction: [your text]",
                },
                {
                    "t": "p",
                    **L(
                        "<strong>Ce que l'IA répond :</strong> le texte corrigé + la liste des corrections expliquées.",
                        "<strong>What AI answers:</strong> the corrected text + the explained corrections list.",
                        "<strong>ما يجيبه الذكاء:</strong> النص المصحّح + قائمة التصحيحات مفسَّرة.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> demande toujours « explique chaque correction » — sinon tu ne progresses pas.",
                        "<strong>Tip:</strong> always ask \"explain each correction\" — else you do not progress.",
                        "<strong>نصيحة:</strong> اطلب دائماً « اشرح كل تصحيح » — وإلا فلن تتقدّم.",
                    ),
                },
            ],
        },
        {
            "id": "s5",
            "titre": L(
                "🤫 Les astuces que personne ne dit",
                "🤫 Tricks nobody tells you",
                "🤫 حيل لا يخبرك بها أحد",
            ),
            "blocks": [
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Sois précis :</strong> « explique X en 3 phrases pour un étudiant de 2ème année » marche mieux que « explique X ».",
                            "<strong>Donne un rôle :</strong> « Tu es un professeur de maths » → la réponse sera plus adaptée.",
                            "<strong>Impose le format :</strong> « sous forme de tableau », « en 5 puces », « en 3 paragraphes ».",
                            "<strong>Vérifie les faits :</strong> demande toujours les sources quand c'est factuel.",
                            "<strong>Reformule :</strong> « reformule plus simplement » ou « donne un exemple concret ».",
                            "<strong>Garde le même chat :</strong> l'IA se souvient du contexte, tu peux affiner sans tout répéter.",
                            "<strong>Ne demande jamais tout d'un coup :</strong> découpe ta question en plusieurs étapes.",
                        ],
                        [
                            "<strong>Be precise:</strong> \"explain X in 3 sentences for a 2nd-year student\" beats \"explain X\".",
                            "<strong>Give a role:</strong> \"You are a maths teacher\" → a better-fitted answer.",
                            "<strong>Set the format:</strong> \"as a table\", \"in 5 bullets\", \"in 3 paragraphs\".",
                            "<strong>Check facts:</strong> always ask for sources when factual.",
                            "<strong>Rephrase:</strong> \"rephrase more simply\" or \"give a concrete example\".",
                            "<strong>Keep the same chat:</strong> AI remembers context, refine without repeating all.",
                            "<strong>Never ask everything at once:</strong> split your question into steps.",
                        ],
                        [
                            "<strong>كن دقيقاً:</strong> « اشرح X في 3 جمل لطالب سنة ثانية » خير من « اشرح X ».",
                            "<strong>أعطِ دوراً:</strong> « أنت أستاذ رياضيات » ← جواب أنسب.",
                            "<strong>افرض الصيغة:</strong> « في جدول »، « في 5 نقاط »، « في 3 فقرات ».",
                            "<strong>تحقق من الحقائق:</strong> اطلب المصادر دائماً عندما يكون الأمر واقعياً.",
                            "<strong>أعد الصياغة:</strong> « أعد ببساطة أكبر » أو « أعطِ مثالاً ملموساً ».",
                            "<strong>ابقَ في نفس الدردشة:</strong> يتذكر الذكاء السياق فحسّن دون إعادة كل شيء.",
                            "<strong>لا تطلب كل شيء دفعة واحدة أبداً:</strong> قسّم سؤالك إلى خطوات.",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s6",
            "titre": L(
                "⛔ Erreurs à éviter",
                "⛔ Mistakes to avoid",
                "⛔ أخطاء يجب تجنّبها",
            ),
            "blocks": [
                {
                    "t": "ul",
                    **L(
                        [
                            "❌ « Explique-moi tout sur l'IA » → réponse de 20 lignes inutilisable. ✅ Précise sujet + format + public.",
                            "❌ Croire l'IA sur parole → elle invente. ✅ Vérifie toujours les faits importants.",
                            "❌ Demander sans réfléchir d'abord → ton cerveau s'éteint. ✅ Devine la réponse, PUIS compare.",
                        ],
                        [
                            "❌ \"Explain everything about AI to me\" → unusable 20-line answer. ✅ Specify topic + format + audience.",
                            "❌ Believing AI at face value → it invents. ✅ Always check important facts.",
                            "❌ Asking without thinking first → your brain switches off. ✅ Guess the answer, THEN compare.",
                        ],
                        [
                            "❌ « اشرح لي كل شيء عن الذكاء » ← جواب من 20 سطراً لا يُستعمَل. ✅ حدّد الموضوع + الصيغة + الجمهور.",
                            "❌ تصديق الذكاء حرفياً ← إنه يختلق. ✅ تحقق دائماً من الحقائق المهمة.",
                            "❌ السؤال دون تفكير أولاً ← دماغك ينطفئ. ✅ خمّن الجواب ثم قارن.",
                        ],
                    ),
                },
            ],
        },
    ],
    "videos": [
        {
            "titre": L(
                "ما هو الذكاء الاصطناعي؟ شرح مبسط للمبتدئين (AI بالعربي)",
                "What is AI? Simple explanation for beginners (AI بالعربي)",
                "ما هو الذكاء الاصطناعي؟ شرح مبسط للمبتدئين (AI بالعربي)",
            ),
            "url": "https://www.youtube.com/watch?v=wdbb-X5qH4w",
            "langue": "ar",
            "concept": L(
                "Idéale pour revoir la définition de l'IA avec des exemples de la vie quotidienne.",
                "Great to revise the definition of AI with everyday examples.",
                "مثالية لمراجعة تعريف الذكاء الاصطناعي بأمثلة يومية.",
            ),
        },
        {
            "titre": L(
                "ما هو الذكاء الاصطناعي؟ شرح مبسط",
                "What is AI? A simple explanation",
                "ما هو الذكاء الاصطناعي؟ شرح مبسط",
            ),
            "url": "https://www.youtube.com/watch?v=vCKHeYQp8nk",
            "langue": "ar",
            "concept": L(
                "Deuxième regard, très pédagogique : l'IA dans le téléphone et dans la classe.",
                "A second, very didactic look: AI in the phone and in the classroom.",
                "نظرة ثانية تعليمية جداً: الذكاء الاصطناعي في الهاتف وفي القسم.",
            ),
        },
        {
            "titre": L(
                "The Age of A.I. (Kurzgesagt)",
                "The Age of A.I. (Kurzgesagt)",
                "عصر الذكاء الاصطناعي (Kurzgesagt)",
            ),
            "url": "https://www.youtube.com/watch?v=UwsrzCVZAb8",
            "langue": "en",
            "concept": L(
                "Ce que l'IA peut et ne peut pas faire — pour rester lucide (sous-titres FR disponibles).",
                "What AI can and cannot do — to stay clear-headed (FR subtitles available).",
                "ما يستطيع الذكاء الاصطناعي فعله وما لا يستطيع — للبقاء صاحياً (ترجمة فرنسية متاحة).",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "J'ai ouvert un chatbot et posé 2 vraies questions (prompts 1 et 2).",
                "I opened a chatbot and asked 2 real questions (prompts 1 and 2).",
                "فتحت روبوت دردشة وطرحت سؤالين حقيقيين (الصياغتان 1 و2).",
            ),
            L(
                "Je sais juger une réponse : 1 chose claire + 1 chose confuse ou douteuse.",
                "I can judge an answer: 1 clear + 1 confusing or doubtful thing.",
                "أعرف الحكم على جواب: شيء واضح + شيء مربك أو مشكوك.",
            ),
            L(
                "Je connais les 3 erreurs qui tuent un bon usage (vague, confiance aveugle, zéro réflexion).",
                "I know the 3 mistakes killing good use (vague, blind trust, zero thinking).",
                "أعرف الأخطاء الثلاثة القاتلة للاستعمال الجيد (الغموض والثقة العمياء وانعدام التفكير).",
            ),
            L(
                "J'ai produit ma fiche d'usage : prompts + réponses + avis en 3 lignes.",
                "I produced my usage sheet: prompts + answers + 3-line review.",
                "أنتجت بطاقة استعمالي: الصياغات + الأجوبة + الرأي في 3 أسطر.",
            ),
            L(
                "3 règles d'or : vérifier, citer, garder ton jugement.",
                "3 golden rules: verify, cite, keep your judgement.",
                "3 قواعد ذهبية: تحقّق، استشهد، حافظ على حكمك.",
            ),
        ],
        "analogies": [
            L(
                "L'apprenti cuisinier qui goûte des milliers de plats avant de créer sa recette.",
                "The apprentice chef who tastes thousands of dishes before creating his recipe.",
                "الطبّاخ المبتدئ يتذوّق آلاف الأطباق قبل إبداع وصفته.",
            ),
            L(
                "L'enfant qui reconnaît un chien parce qu'il en a déjà vu beaucoup.",
                "The child who recognises a dog because he has already seen many.",
                "الطفل يتعرّف على الكلب لأنه رآه مرات كثيرة.",
            ),
            L(
                "Le jeu de devinettes : deviner le mot suivant d'une phrase.",
                "The guessing game: guess the next word of a sentence.",
                "لعبة التخمين: خمّن الكلمة التالية في الجملة.",
            ),
        ],
        "exemples": [
            L(
                "Ton téléphone utilise l'IA pour déverrouiller (reconnaissance faciale) et corriger ta frappe.",
                "Your phone uses AI to unlock (face recognition) and fix your typing.",
                "هاتفك يستعمل الذكاء الاصطناعي لفتح الوجه وتصحيح الكتابة.",
            ),
            L(
                "« Hier je suis allé… » → l'IA propose « au marché » car c'est probable.",
                "\"Yesterday I went…\" → AI suggests \"to the market\" because it is probable.",
                "« بالأمس ذهبت… » → يقترح الذكاء الاصطناعي « إلى السوق » لأنها الحتملة.",
            ),
            L(
                "Demander 2 études sur Piaget : le chatbot peut en inventer, l'outil sourcé affiche des liens.",
                "Asking for 2 studies on Piaget: the chatbot may invent them, the sourced tool shows links.",
                "طلب دراستين عن بياجيه: قد يختلقهما روبوت المحادثة، والأداة الموجّهة تعرض روابط.",
            ),
        ],
        "analogie_finale": L(
            "🏁 L'IA, c'est comme un excellent acteur : il peut jouer brillamment n'importe quel rôle de manière convaincante, mais ce qu'il raconte n'est pas forcément vrai. À toi de vérifier le scénario.",
            "🏁 AI is like a brilliant actor: it can brilliantly play any role convincingly, but what it says is not necessarily true. You check the script.",
            "🏁 الذكاء الاصطناعي كممثل بارع: يلعب أي دور بشكل مقنع، لكن ما يقوله ليس صحيحاً بالضرورة. وأنت تتحقق من السيناريو.",
        ),
        "quiz": [
            {
                "q": L(
                    "Comment un chatbot produit-il sa réponse ?",
                    "How does a chatbot produce its answer?",
                    "كيف يُنتج روبوت الدردشة إجابته؟",
                ),
                "options": L(
                    ["Il la copie d'une bibliothèque", "Il prédit le mot le plus probable, mot après mot", "Il demande à un humain", "Il la cherche sur Google"],
                    ["He copies it from a library", "He predicts the most probable word, word after word", "He asks a human", "He searches Google"],
                    ["ينسخها من مكتبة", "يتنبأ بالكلمة الأكثر احتمالاً كلمة كلمة", "يسأل إنساناً", "يبحث عنها في جوجل"],
                ),
                "answer": 1,
                "exp": L(
                    "Le chatbot reconstruit la réponse mot après mot selon les probabilités apprises pendant l'entraînement.",
                    "The chatbot rebuilds the answer word by word, based on probabilities learned during training.",
                    "يعيد روبوت الدردشة بناء الجواب كلمة كلمة حسب الاحتمالات المتعلّمة أثناء التدريب.",
                ),
            },
            {
                "q": L(
                    "Qu'est-ce qu'une « hallucination » d'IA ?",
                    "What is an AI \"hallucination\"?",
                    "ما هي « هلوسة » الذكاء الاصطناعي؟",
                ),
                "options": L(
                    ["Un bug très rare", "Une certitude dans la réponse", "Une information inventée dite avec assurance", "Une panne d'ordinateur"],
                    ["A very rare bug", "A certainty in the answer", "An invented fact stated with confidence", "A computer crash"],
                    ["خلل نادر جداً", "اليقين في الإجابة", "معلومة مختلقة تُقال بثقة", "عطل في الحاسوب"],
                ),
                "answer": 2,
                "exp": L(
                    "L'IA peut affirmer des faits faux avec assurance. C'est un comportement courant : vérifie toujours.",
                    "AI can confidently state false facts. It is common behaviour: always check.",
                    "قد يؤكد الذكاء الاصطناعي حقائق خاطئة بثقة. سلوك شائع: تحقق دائماً.",
                ),
            },
            {
                "q": L(
                    "ChatGPT, aujourd'hui, c'est…",
                    "ChatGPT, today, is…",
                    "ChatGPT اليوم هو…",
                ),
                "options": L(
                    ["Une IA générale", "Une super-IA", "Une IA faible (étroite)", "Un cerveau humain"],
                    ["A general AI", "A super-AI", "A narrow AI", "A human brain"],
                    ["ذكاء عام", "ذكاء فائق", "ذكاء ضيّق", "دماغ بشري"],
                ),
                "answer": 2,
                "exp": L(
                    "Il est excellent dans une tâche (le texte) mais ne fait pas « tout » comme un humain.",
                    "It is excellent at one task (text) but does not do \"everything\" like a human.",
                    "بارع في مهمة واحدة (النص) لكنه لا يفعل « كل شيء » كالإنسان.",
                ),
            },
            {
                "q": L(
                    "Laquelle de ces phrases est une bonne règle d'or ?",
                    "Which of these is a good golden rule?",
                    "أي جملة قاعدة ذهبية جيدة؟",
                ),
                "options": L(
                    ["Copier la réponse et la déposer", "Vérifier, citer, garder son jugement", "Faire confiance à 100 %", "Ne jamais utiliser l'IA"],
                    ["Copy the answer and submit it", "Verify, cite, keep your judgement", "Trust it 100%", "Never use AI"],
                    ["انسخ الجواب وسلّمه", "تحقّق، استشهد، حافظ على حكمك", "ثِق به 100%", "لا تستعمل الذكاء الاصطناعي أبداً"],
                ),
                "answer": 1,
                "exp": L(
                    "Les 3 règles d'or protègent ta note ET ta compréhension : l'IA propose, tu disposes.",
                    "The 3 golden rules protect your grade AND your understanding: AI proposes, you dispose.",
                    "القواعد الذهبية تحمي علامتك وفهمك: الذكاء الاصطناعي يقترح وأنت تقرر.",
                ),
            },
            {
                "q": L(
                    "Comment apprend une IA ?",
                    "How does AI learn?",
                    "كيف يتعلم الذكاء الاصطناعي؟",
                ),
                "options": L(
                    ["On lui écrit toutes les règles à la main", "En voyant des milliers d'exemples et en trouvant des régularités", "En lisant les journaux chaque matin", "En copiant les réponses de ses camarades"],
                    ["By handwriting all the rules", "By seeing thousands of examples and finding patterns", "By reading newspapers every morning", "By copying classmates' answers"],
                    ["بكتابة كل القواعد يدوياً", "بمشاهدة آلاف الأمثلة وإيجاد الانتظامات", "بقراءة الجرائد كل صباح", "بنسخ أجوبة زملائه"],
                ),
                "answer": 1,
                "exp": L(
                    "L'apprentissage sur exemples (comme l'apprenti cuisinier) : c'est la base de l'IA moderne.",
                    "Learning from examples (like the apprentice chef): that is the basis of modern AI.",
                    "التعلم من الأمثلة (كطبّاخ مبتدئ): أساس الذكاء الاصطناعي الحديث.",
                ),
            },
        ],
    },
    "retenir": [
        L(
            "L'IA prédit le mot suivant ; elle peut être convaincante et fausse.",
            "AI predicts the next word; it can be convincing and wrong.",
            "يتنبأ الذكاء بالكلمة التالية؛ وقد يكون مقنعاً ومخطئاً.",
        ),
        L(
            "La qualité de la réponse dépend de la qualité du prompt.",
            "Answer quality depends on prompt quality.",
            "جودة الجواب تتوقف على جودة الصياغة.",
        ),
        L(
            "Toujours préciser : sujet + format + public.",
            "Always specify: topic + format + audience.",
            "حدّد دائماً: الموضوع + الصيغة + الجمهور.",
        ),
        L(
            "Toujours vérifier les faits importants.",
            "Always check important facts.",
            "تحقق دائماً من الحقائق المهمة.",
        ),
        L(
            "Les 3 règles d'or : vérifier, citer, garder ton jugement.",
            "The 3 golden rules: verify, cite, keep your judgement.",
            "القواعد الذهبية الثلاث: تحقّق واستشهد وحافظ على حكمك.",
        ),
    ],
    "glossaire": [
        {
            "term": "Intelligence Artificielle (IA)",
            "term_en": "Artificial Intelligence (AI)",
            "def_fr": "Programme informatique qui apprend à partir de données pour accomplir des tâches habituellement « intelligentes ».",
            "def_en": "A computer program that learns from data to perform tasks that are usually \"intelligent\".",
            "def_ar": "برنامج حاسوبي يتعلم من البيانات لإنجاز مهام عادة ما تكون « ذكية ».",
        },
        {
            "term": "Modèle de langage (LLM)",
            "term_en": "Large Language Model (LLM)",
            "def_fr": "Modèle d'IA entraîné sur d'énormes corpus de textes, capable de prédire et de générer du langage.",
            "def_en": "An AI model trained on huge text corpora, able to predict and generate language.",
            "def_ar": "نموذج ذكاء اصطناعي مدرَّب على كمّ هائل من النصوص، قادر على التنبؤ باللغة وتوليدها.",
        },
        {
            "term": "Prompt",
            "term_en": "Prompt",
            "def_fr": "La question, l'instruction ou le contexte que tu donnes à l'IA pour orienter sa réponse.",
            "def_en": "The question, instruction or context you give AI to steer its answer.",
            "def_ar": "السؤال أو التعليمات أو السياق الذي تقدّمه للذكاء الاصطناعي لتوجيه إجابته.",
        },
        {
            "term": "Hallucination",
            "term_en": "Hallucination",
            "def_fr": "Réponse fausse ou inventée donnée avec assurance par une IA générative.",
            "def_en": "A false or invented answer confidently given by a generative AI.",
            "def_ar": "إجابة خاطئة أو مختلقة تُعطى بثقة من الذكاء الاصطناعي التوليدي.",
        },
        {
            "term": "Données d'entraînement",
            "term_en": "Training data",
            "def_fr": "Les textes, images et exemples utilisés pour apprendre au modèle à fonctionner.",
            "def_en": "The texts, images and examples used to teach the model to work.",
            "def_ar": "النصوص والصور والأمثلة المستعملة لتعليم النموذج كيفية العمل.",
        },
        {
            "term": "IA générative",
            "term_en": "Generative AI",
            "def_fr": "Catégorie d'IA qui crée du contenu nouveau (texte, image, audio) à partir d'une consigne.",
            "def_en": "A category of AI that creates new content (text, image, audio) from a prompt.",
            "def_ar": "فئة من الذكاء الاصطناعي تُنشئ محتوى جديداً (نصاً، صورة، صوتاً) انطلاقاً من تعليمات.",
        },
    ],
    "dialogues_fr": """# Séance 01 — Dialogues pédagogiques (Français)

## Dialogue A — « L'IA, ma nouvelle collègue d'études » (25 min)

**Personnages :** Amine (étudiant PEP 2A), l'assistant IA (joué par le formateur), Sofia (camarade).

---

Amine : Bonjour ! Je dois réviser mon cours de psychologie de l'enfant, mais je suis submergé. Tu peux m'aider ?

IA : Bien sûr. Donne-moi le chapitre ou le sujet, et dis-moi ce que tu veux : un résumé, des questions, une explication simple ?

Sofia : Attention Amine ! Tu ne vas pas lui confier TOUT le travail ?

Amine : Non ! Je veux qu'il m'explique les idées difficiles, que je vérifie ensuite dans mon cours.

Sofia : Et comment tu sais que ce qu'il raconte est juste ?

Amine : Je le vérifie. Et toi, tu proposes, je dispose. C'est la règle n°1 !

IA : Bonne attitude. Je te propose une fiche avec trois idées-clés. Mais préviens-toi : je peux me tromper, vérifie les dates avec ton polycopié.

Sofia : Donc il avoue lui-même se tromper !

Amine : Justement : c'est pour ça que personne ne doit copier une réponse sans la relire. L'IA prédit des mots, pas la vérité.

Sofia : Tu m'expliques ? Parce que moi, quand elle écrit, ça paraît tellement vrai…

Amine : Oui, c'est son métier : être convaincante ! Un mot après l'autre. Mais parfois elle invente. Alors on vérifie toujours.

Sofia : D'accord… Et si je l'utilise pour traduire mon résumé en arabe avant de le réciter ?

Amine : Excellente idée ! Traduis, relis, corrige, et entraîne-toi à l'oral. L'IA t'aide à travailler, pas à travailler à ta place.

---

## Dialogue B — « Papa, pourquoi tu parles avec un robot ? » (15 min)

**Personnages :** Yacine (étudiant), son père, Nour (petite sœur de 7 ans).

---

Nour : Yacine, pourquoi tu poses des questions à ton téléphone au lieu d'étudier ?

Yacine : Je lui fais corriger la grammaire de mon devoir d'anglais, Nour.

Papa : Et c'est permis, à l'université ?

Yacine : Oui, si on reste honnête. Je ne lui fais pas écrire à ma place : je lui demande de repérer mes fautes et de m'expliquer pourquoi. Ensuite je corrige moi-même.

Nour : C'est comme la maîtresse qui marque en rouge ?

Yacine : Oui, presque. Mais elle, elle ne se trompe pas toujours…

Papa : Hmm, donc le téléphone peut se tromper ?

Yacine : Souvent ! Il faut vérifier. Et moi, quand il se trompe, c'est moi le responsable de ma copie.

Nour : Et moi, est-ce que je peux lui demander d'écrire mon exercice ?

Yacine : Non ! Parce que toi, tu dois apprendre. Si tu lui demandes de faire ton devoir, tu n'apprends rien. C'est comme si tu n'allais pas à l'école.

Papa : Bien dit. Quand tu seras professeur, tu comprendras encore mieux pourquoi il faut apprendre par soi-même.

---

## Mini-rôle à jouer (3 min par binôme)
Ton camarade croit que « l'IA est interdite à l'université parce qu'elle triche ». Explique-lui : ce qui est interdit, c'est le plagiat, pas l'usage honnête et vérifié. Reformule les 3 règles d'or.
""",
    "dialogues_en": """# Session 01 — Classroom dialogues (English)

## Dialogue A — "AI, my new study buddy" (25 min)

**Characters:** Amine (PEP 2A student), the AI assistant (played by the trainer), Sofia (classmate).

---

Amine: Hello! I have to revise my child-psychology lesson, but I am overwhelmed. Can you help me?

AI: Of course. Give me the chapter or the topic, and tell me what you want: a summary, questions, a simple explanation?

Sofia: Careful, Amine! You're not going to hand over ALL the work, are you?

Amine: No! I want it to explain the difficult ideas, and I will check them afterwards in my lesson.

Sofia: And how do you know what it says is true?

Amine: I check it. And you propose, I dispose. That is rule #1!

AI: Good attitude. Let me give you a one-page sheet with three key ideas. But be warned: I can be wrong, check the dates with your handout.

Sofia: So it admits itself that it makes mistakes!

Amine: Exactly: that is why nobody should copy an answer without re-reading it. AI predicts words, not truth.

Sofia: Explain to me? Because when it writes, it seems so true…

Amine: Yes, that's its job: being convincing! One word after another. But sometimes it invents. So we always check.

Sofia: OK… And what if I use it to translate my summary into Arabic before reciting it?

Amine: Great idea! Translate, re-read, correct, and practise out loud. AI helps you work, not work in your place.

---

## Dialogue B — "Dad, why are you talking to a robot?" (15 min)

**Characters:** Yacine (student), his father, Nour (7-year-old sister).

---

Nour: Yacine, why are you asking questions to your phone instead of studying?

Yacine: I'm asking it to correct the grammar of my English assignment, Nour.

Dad: And is that allowed at university?

Yacine: Yes, if we stay honest. I don't write for it: I ask it to spot my mistakes and explain why. Then I correct them myself.

Nour: It's like the teacher who marks in red?

Yacine: Yes, almost. But she is not always wrong…

Dad: Hmm, so the phone can be wrong?

Yacine: Often! You have to check. And when it is wrong, I am the one responsible for my paper.

Nour: And me, can I ask it to do my homework?

Yacine: No! Because you have to learn. If you ask it to do your homework, you learn nothing. It is like not going to school.

Dad: Well said. When you become a teacher, you will understand even better why learning by yourself matters.

---

## Mini role-play (3 min per pair)
Your classmate believes "AI is forbidden at university because it cheats". Explain to him/her: what is forbidden is plagiarism, not honest, verified use. Repeat the 3 golden rules.
""",
}