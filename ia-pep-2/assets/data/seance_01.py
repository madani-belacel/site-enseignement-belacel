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
        "Comprendre ce qu'est l'IA en mots simples — avec des comparaisons de la vie quotidienne — pour t'en servir dès aujourd'hui dans tes études, sans naïveté, sans peur et avec ton esprit critique.",
        "Understand what AI is in simple words — with everyday comparisons — to use it today in your studies, without naivety, without fear and with your critical thinking.",
        "أن تفهم ما هو الذكاء الاصطناعي بكلمات بسيطة — مع تشبيهات من الحياة اليومية — لتستعمله اليوم في دراستك، دون سذاجة، دون خوف، ومع التفكير النقدي.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Définir avec tes mots : IA, modèle de langage et prompt.",
            "Define in your own words: AI, language model and prompt.",
            "أن تعرّف بعباراتك الخاصة: الذكاء الاصطناعي، ونموذج اللغة، والصياغة (Prompt).",
        ),
        L(
            "Expliquer simplement comment un chatbot répond (il prédit le mot le plus probable à partir d'exemples).",
            "Explain simply how a chatbot answers (it predicts the most probable word from examples).",
            "أن تشرح ببساطة كيف يجيب روبوت الدردشة (يتنبأ بالكلمة الأكثر احتمالاً انطلاقاً من أمثلة).",
        ),
        L(
            "Citer 5 usages de l'IA utiles à tes études (rechercher, résumer, rédiger, réviser, organiser).",
            "List 5 AI uses helpful for your studies (search, summarise, write, revise, organise).",
            "أن تذكر خمسة استعمالات للذكاء الاصطناعي مفيدة لدراستك (بحث، تلخيص، كتابة، مراجعة، تنظيم).",
        ),
        L(
            "Identifier 3 limites : erreurs, hallucinations, biais.",
            "Identify 3 limits: errors, hallucinations, biases.",
            "أن تحدّد ثلاث حدود: الأخطاء، والهلوسة، والتحيّزات.",
        ),
        L(
            "Appliquer les 3 règles d'or : vérifier, citer, garder ton jugement.",
            "Apply the 3 golden rules: verify, cite, keep your judgement.",
            "أن تطبّق القواعد الذهبية الثلاث: تثبّت، استشهد، وحافظ على حكمك.",
        ),
    ],
    "prerequis": L(
        "Aucun prérequis technique. Savoir ouvrir un navigateur et utiliser un smartphone suffit.",
        "No technical prerequisite. Knowing how to open a browser and use a smartphone is enough.",
        "لا توجد مكتسبات تقنية. يكفي معرفة فتح متصفّح واستعمال الهاتف الذكي.",
    ),
    "accroche": {
        "question": L(
            "Savez-vous que votre téléphone utilise l'IA des dizaines de fois par jour, sans que vous vous en rendiez compte ? Verrouillage du visage, traduction, correction du clavier, recommandation de vidéos…",
            "Did you know your phone uses AI dozens of times a day, without you noticing? Face unlock, translation, keyboard correction, video recommendations…",
            "هل تعلم أن هاتفك يستعمل الذكاء الاصطناعي عشرات المرات يومياً دون أن تنتبه؟ فتح الوجه، الترجمة، تصحيح لوحة المفاتيح، التوصية بالفيديوهات…",
        ),
        "analogie": L(
            "🍳 L'IA, c'est comme un apprenti cuisinier : il goûte des milliers de plats (les exemples), remarque des régularités (le sucre c'est sucré, le citron c'est acide) et finit par pouvoir créer sa propre recette. Il ne sait pas POURQUOI ça marche, il a appris QUE ça marche.",
            "🍳 AI is like an apprentice chef: he tastes thousands of dishes (the examples), notices patterns (sugar is sweet, lemon is sour) and ends up able to create his own recipe. He does not know WHY it works, he just learned THAT it works.",
            "🍳 الذكاء الاصطناعي كطبّاخ مبتدئ: يتذوّق آلاف الأطباق (الأمثلة)، ويلاحظ انتظامات (السكر حلو، الليمون حامض)، وينتهي به الأمر قادراً على إبداع وصفته الخاصة. لا يعرف لماذا ينجح، لكنه تعلّم أنّه ينجح.",
        ),
        "phrase": L(
            "💡 L'IA, c'est un programme informatique qui apprend à partir d'exemples pour imiter certaines capacités humaines : comprendre, parler, traduire, voir, décider.",
            "💡 AI is a computer program that learns from examples to imitate certain human abilities: understanding, speaking, translating, seeing, deciding.",
            "💡 الذكاء الاصطناعي برنامج حاسوبي يتعلّم من الأمثلة ليحاكي بعض القدرات البشرية: الفهم، والتحدث، والترجمة، والرؤية، واتخاذ القرار.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche et sondage",
                "Hook and survey",
                "انطلاقة واستطلاع",
            ),
            "detail": L(
                "La question « ton téléphone utilise l'IA ? » + tour de table sur les usages déjà vus.",
                "The \"does your phone use AI?\" question + round table on uses already seen.",
                "سؤال « هل يستعمل هاتفك الذكاء الاصطناعي؟ » + جولة على المجموعة حول الاستعمالات.",
            ),
        },
        {
            "time": "05–20",
            "badge": "🧱 B",
            **L(
                "Explication pas à pas : 3 idées clés",
                "Step-by-step: 3 key ideas",
                "شرح خطوة بخطوة: ثلاث أفكار رئيسية",
            ),
            "detail": L(
                "1) L'IA apprend sur des exemples (apprenti cuisinier). 2) Un chatbot prédit le mot suivant. 3) IA faible / générale / super-IA.",
                "1) AI learns from examples (apprentice chef). 2) A chatbot predicts the next word. 3) Narrow / general / super AI.",
                "1) يتعلم الذكاء الاصطناعي من الأمثلة. 2) روبوت الدردشة يتنبأ بالكلمة التالية. 3) ذكاء ضيّق / عام / فائق.",
            ),
        },
        {
            "time": "20–40",
            "badge": "🛠️ C",
            **L(
                "Démonstration : un résumé de cours",
                "Demonstration: a lesson summary",
                "عرض تطبيقي: تلخيص درس",
            ),
            "detail": L(
                "Mauvais prompt vs bon prompt, puis piège de l'hallucination : la même question posée à un chatbot et à un moteur sourcé.",
                "Bad prompt vs good prompt, then the hallucination trap: the same question asked to a chatbot and to a sourced engine.",
                "صياغة ضعيفة مقابل صياغة قوية، ثم مصيدة الهلوسة: نفس السؤال لروبوت محادثة ومحرّك بمصادر.",
            ),
        },
        {
            "time": "40–55",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : vrai ou faux ?",
                "Guided exercise: true or false?",
                "تمرين موجّه: صحيح أم خطأ؟",
            ),
            "detail": L(
                "6 affirmations sur l'IA à classer + correction collective.",
                "6 statements about AI to classify + collective correction.",
                "6 جمل حول الذكاء الاصطناعي تُصنَّف + تصحيح جماعي.",
            ),
        },
        {
            "time": "55–60",
            "badge": "🧠 E",
            **L(
                "Résumé visuel et quiz éclair",
                "Visual summary and quick quiz",
                "ملخص بصري واختبار خاطف",
            ),
            "detail": L(
                "Fiche de synthèse (+3 points) et quiz éclair de 3 questions.",
                "Summary sheet (+3 points) and a 3-question quick quiz.",
                "بطاقة تركيب (نقاط +3) واختبار خاطف من ثلاثة أسئلة.",
            ),
        },
        {
            "time": "60–90",
            "badge": "🤝 Atelier",
            **L(
                "Atelier : dialogues et rôles",
                "Workshop: dialogues and role-play",
                "ورشة: الحوارات والأدوار",
            ),
            "detail": L(
                "Jouer les dialogues A et B en binômes, puis mini-rôle de 3 min.",
                "Act out dialogues A and B in pairs, then a 3-minute mini role-play.",
                "تمثيل الحوارين A وB في مجموعات ثنائية، ثم دور مصغّر من 3 دقائق.",
            ),
        },
    ],
    "sections": [
        {
            "id": "b1",
            "titre": L(
                "Idée clé 1 — L'IA apprend sur des exemples",
                "Key idea 1 — AI learns from examples",
                "الفكرة الأولى — يتعلم الذكاء الاصطناعي من الأمثلة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une IA n'est pas programmée « à la main » comme une calculatrice. On lui montre des milliers d'exemples, et elle en tire des régularités. C'est une énorme machine à généraliser.",
                        "AI is not hand-programmed like a calculator. We show it thousands of examples, and it extracts patterns. It is a huge generalisation machine.",
                        "الذكاء الاصطناعي لا يُبرمج يدوياً كالآلة الحاسبة. نريه آلاف الأمثلة فيستخرج انتظامات. إنه آلة تعميم هائلة.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>Analogie pour te souvenir :</strong> comment un enfant reconnaît-il un chien ? Il en a vu beaucoup. Il n'apprend pas une définition : il reconnaît des ressemblances. L'IA fait pareil, à grande échelle.",
                        "<strong>Analogy to remember:</strong> how does a child recognise a dog? He has seen many. He does not learn a definition: he recognises similarities. AI does the same, at scale.",
                        "<strong>تشبيه للتذكّر:</strong> كيف يتعرّف الطفل على الكلب؟ رآه مرات كثيرة. لا يتعلم تعريفاً، بل يتعرّف على أوجه الشبه. الذكاء الاصطناعي يفعل ذلك على نطاق واسع.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Données d'entraînement :</strong> les exemples qu'on montre à l'IA (textes, images, sons).",
                            "<strong>Modèle :</strong> le résultat de l'apprentissage — un « cerveau » numérique qui généralise à partir des exemples.",
                            "<strong>Prédiction :</strong> quand tu lui poses une question, il ne « cherche » pas la réponse : il la reconstruit à partir de ce qu'il a appris.",
                        ],
                        [
                            "<strong>Training data:</strong> the examples shown to AI (texts, images, sounds).",
                            "<strong>Model:</strong> the result of learning — a digital \"brain\" that generalises from examples.",
                            "<strong>Prediction:</strong> when you ask a question, it does not \"look up\" the answer: it rebuilds it from what it learned.",
                        ],
                        [
                            "<strong>بيانات التدريب:</strong> الأمثلة المعروضة على الذكاء الاصطناعي (نصوص، صور، أصوات).",
                            "<strong>النموذج:</strong> نتيجة التعلم — « دماغ » رقمي يعمّم انطلاقاً من الأمثلة.",
                            "<strong>التنبؤ:</strong> عندما تسأله، لا « يبحث » عن الجواب بل يعيد بناءه مما تعلّمه.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    **L(
                        """Schéma simple — comment l'IA apprend :

    EXEMPLES (milliers)          APPRENTISSAGE              MODÈLE
    "ceci est un chat"     ──►  régularités trouvées  ──►  "reconnaît" un chat
    "ceci est un chien"         poids chiffrés ajustés      puis répond / prédit""",
                        """Simple diagram — how AI learns:

    EXAMPLES (thousands)         LEARNING                   MODEL
    "this is a cat"        ──►  patterns found        ──►  "recognises" a cat
    "this is a dog"             tuned numeric weights      then answers / predicts""",
                    ),
                },
            ],
        },
        {
            "id": "b2",
            "titre": L(
                "Idée clé 2 — Un chatbot prédit le mot suivant",
                "Key idea 2 — A chatbot predicts the next word",
                "الفكرة الثانية — روبوت الدردشة يتنبأ بالكلمة التالية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "ChatGPT, Gemini ou Copilot sont des « modèles de langage » (LLM). Leur secret : ils ont été entraînés sur des milliards de phrases, et ils ont appris une seule chose — quel mot vient le plus probablement après celui-ci.",
                        "ChatGPT, Gemini or Copilot are \"language models\" (LLMs). Their secret: they were trained on billions of sentences, and they learned one thing — which word most probably comes after this one.",
                        "ChatGPT أو Gemini أو Copilot هي « نماذج لغة » (LLM). سرّها: درّبت على مليارات الجمل وتعلّمت شيئاً واحداً — ما الكلمة الأكثر احتمالاً بعد هذه.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "« Hier, je suis allé … » → le modèle propose « au marché » parce que c'est très fréquent dans ses données.",
                            "Il génère mot après mot, jusqu'à former une phrase entière. Résultat : un texte qui paraît très naturel.",
                            "Il est entraîné à être <strong>convaincant</strong>, pas à être <strong>vrai</strong>. D'où les erreurs et les hallucinations.",
                        ],
                        [
                            "\"Yesterday I went to …\" → the model suggests \"the market\" because it is very frequent in its data.",
                            "It generates word after word, until a whole sentence forms. Result: text that looks very natural.",
                            "It is trained to be <strong>convincing</strong>, not <strong>true</strong>. Hence errors and hallucinations.",
                        ],
                        [
                            "« بالأمس ذهبت … » → يقترح النموذج « إلى السوق » لأنه متكرر جداً في بياناته.",
                            "يولّد الكلمة بعد الكلمة حتى تتكوّن جملة كاملة. النتيجة: نص يبدو طبيعياً جداً.",
                            "دُرِّب على <strong>الإقناع</strong> لا على <strong>الصدق</strong>. من هنا تأتي الأخطاء والهلوسة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>Hallucination =</strong> quand l'IA affirme avec assurance un fait inventé (une référence, un chiffre, une date). Ce n'est pas un bug rare : c'est un comportement fréquent. Toujours vérifier.",
                        "<strong>Hallucination =</strong> when AI confidently states an invented fact (a reference, a figure, a date). It is not a rare bug: it is common behaviour. Always check.",
                        "<strong>الهلوسة =</strong> أن يؤكد الذكاء الاصطناعي حقيقة مختلقة بثقة (مرجعاً، رقماً، تاريخاً). ليست خللاً نادراً بل سلوكاً شائعاً. تحقّق دائماً.",
                    ),
                },
                {
                    "t": "pre",
                    **L(
                        """Jeu de devinettes — prédire la suite :

    « L'IA, c'est un programme qui ______ »
    Probabilités : apprend(?) > calcule(?) > ...
    → le modèle choisit le mot le plus probable, puis recommence.""",
                        """Guessing game — predict the rest:

    \"AI is a program that ______\"
    Probabilities: learns(?) > computes(?) > ...
    → the model picks the most probable word, then starts again.""",
                    ),
                },
            ],
        },
        {
            "id": "b3",
            "titre": L(
                "Idée clé 3 — Trois familles d'IA",
                "Key idea 3 — Three families of AI",
                "الفكرة الثالثة — ثلاث عائلات للذكاء الاصطناعي",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Il faut savoir classer ce dont on parle : tout ce que tu utilises aujourd'hui appartient à la première famille.",
                        "You should know how to classify what we talk about: everything you use today belongs to the first family.",
                        "يجب أن تعرف كيف تصنّف ما نتحدث عنه: كل ما تستعمله اليوم ينتمي إلى العائلة الأولى.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1. IA faible (étroite)</strong> : excellente dans UNE tâche (traduire, trier, générer du texte). → Tout ce qui existe aujourd'hui.",
                            "<strong>2. IA générale</strong> : égalerait l'humain dans TOUTES les tâches. → N'existe pas encore.",
                            "<strong>3. Super-IA</strong> : dépasserait l'humain. → Scénario hypothétique qui alimente les films et les débats.",
                        ],
                        [
                            "<strong>1. Narrow AI</strong>: excellent at ONE task (translating, sorting, generating text). → Everything that exists today.",
                            "<strong>2. General AI</strong>: would equal humans at ALL tasks. → Does not exist yet.",
                            "<strong>3. Super-intelligence</strong>: would surpass humans. → Hypothetical scenario that fuels films and debates.",
                        ],
                        [
                            "<strong>1. الذكاء الضيّق</strong>: بارع في مهمة واحدة (ترجمة، فرز، توليد نص). → كل ما هو موجود اليوم.",
                            "<strong>2. الذكاء العام</strong>: يساوي الإنسان في كل المهام. → غير موجود بعد.",
                            "<strong>3. الذكاء الفائق</strong>: يفوق الإنسان. → سيناريو افتراضي يغذّي الأفلام والنقاشات.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Schéma pour la classe :</strong> écrire les trois familles au tableau comme trois escaliers. On monte les marches : le dernier étage (super-IA) n'existe QUE dans les films.",
                        "<strong>Diagram for the class:</strong> draw the three families as three stairs. We climb the steps: the top floor (super-AI) exists ONLY in films.",
                        "<strong>مخطط للقسم:</strong> ارسم العائلات الثلاث كثلاث درجات. نصعد الدرجات: الطابق الأخير (الذكاء الفائق) موجود في الأفلام فقط.",
                    ),
                },
            ],
        },
        {
            "id": "demo",
            "titre": L(
                "Démonstration — un résumé de cours, du mauvais au bon prompt",
                "Demonstration — a course summary, from bad to good prompt",
                "عرض تطبيقي — تلخيص درس، من صياغة ضعيفة إلى قوية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Étudiant : « Je dois préparer mon exposé de psychologie de l'enfant. Je colle mon cours et je demande à l'IA de l'aider. » Regardons la différence entre une question paresseuse et une question qui guide.",
                        "Student: \"I must prepare my child-psychology presentation. I paste my lesson and ask AI to help.\" Look at the difference between a lazy question and a guiding one.",
                        "طالب: « يجب أن أحضر عرضي في علم نفس الطفل. ألصق درسي وأطلب من الذكاء الاصطناعي مساعدتي ». لاحظوا الفرق بين سؤال كسول وسؤال موجّه.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["", "Mauvais prompt", "Bon prompt"],
                        ["", "Bad prompt", "Good prompt"],
                        ["", "صياغة ضعيفة", "صياغة قوية"],
                    ),
                    "rows": L(
                        [
                            ["Requête", "Résume ce cours.", "Je suis étudiant en 2ème année PEP. Résume ce cours de psychologie en 5 idées clés, avec un exemple concret pour le primaire à chaque idée, et sans rien inventer : dis-moi ce qui manque."],
                            ["Résultat", "Générique, trop long, aucun lien avec l'exposé.", "Ciblé, structuré, réutilisable pour l'exposé, limites signalées."],
                        ],
                        [
                            ["Prompt", "Summarise this lesson.", "I am a 2nd-year PEP student. Summarise this psychology lesson in 5 key ideas, with a concrete primary-class example per idea, and without inventing anything: tell me what is missing."],
                            ["Result", "Generic, too long, no link to the presentation.", "Targeted, structured, reusable for the presentation, limits flagged."],
                        ],
                        [
                            ["الطلب", "لخّص هذا الدرس.", "أنا طالب السنة الثانية PEP. لخّص درس علم النفس هذا في خمس أفكار رئيسية، مع مثال ملموس للمرحلة الابتدائية في كل فكرة، ودون اختلاق: حدّد ما هو ناقص."],
                            ["النتيجة", "عام، طويل، بلا صلة بالعرض.", "محدد، منظم، قابل لإعادة الاستعمال، مع تنبيه إلى الحدود."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>Le piège du jour :</strong> posons la même question « Donne-moi 2 études sur Piaget » à un chatbot puis à un outil sourcé. Le chatbot peut inventer des références avec assurance ; l'outil sourcé affiche des liens à ouvrir. C'est une raison d'apprendre à vérifier (séance 02).",
                        "<strong>Today's trap:</strong> let's ask the same question \"Give me 2 studies on Piaget\" to a chatbot then to a sourced tool. The chatbot may invent references with confidence; the sourced tool shows links to open. That is a reason to learn to verify (session 02).",
                        "<strong>مصيدة اليوم:</strong> لنطرح السؤال نفسه « أعطني دراستين عن بياجيه » على روبوت محادثة ثم على أداة بمصادر. قد يختلق الروبوت مراجع بثقة؛ والأداة الموجّهة تعرض روابط تفتحها. لهذا نتعلّم التحقق (الحصة 2).",
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
                        "Dès la première séance, retenez l'essentiel : l'IA vaut ce que vaut la question posée, et la réponse vaut ce que vaut la vérification. Utilisée ainsi, elle devient un tuteur personnel disponible 24 h/24 — jamais un remplaçant de ta mémoire.",
                        "From the very first session, remember the key idea: AI is only as good as the question you ask, and the answer is only as good as your verification. Used this way, it becomes a personal tutor available 24/7 — never a substitute for your memory.",
                        "من الحصة الأولى تذكّر الجوهر: الذكاء الاصطناعي بقدر السؤال الذي تطرحه، والإجابة بقدر تحققك منها. بهذا الاستعمال يصبح معلماً شخصياً متاحاً على مدار الساعة — لا بديلاً عن ذاكرتك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Commencez petit :</strong> une tâche précise (résumer, expliquer, reformuler), jamais « fais tout mon travail ».",
                            "<strong>✅ Donnez du contexte :</strong> matière, niveau, objectif, format attendu et longueur.",
                            "<strong>✅ Vérifiez systématiquement :</strong> chaque date, chiffre et référence doit être confirmé dans ton cours.",
                            "<strong>✅ Demandez la méthode :</strong> « explique comment tu arrives à cette conclusion » pour apprendre, pas seulement subir.",
                        ],
                        [
                            "<strong>✅ Start small:</strong> one precise task (summarise, explain, rephrase), never \"do all my work\".",
                            "<strong>✅ Give context:</strong> subject, level, goal, expected format and length.",
                            "<strong>✅ Check systematically:</strong> every date, figure and reference must be confirmed in your lesson.",
                            "<strong>✅ Ask for the method:</strong> \"explain how you reach this conclusion\" to learn, not just to receive.",
                        ],
                        [
                            "<strong>✅ ابدأ صغيراً:</strong> مهمة واحدة دقيقة (تلخيص، شرح، إعادة صياغة)، وليس « أنجز كل عملي ».",
                            "<strong>✅ قدّم السياق:</strong> المادة، المستوى، الهدف، الصيغة المطلوبة، والطول.",
                            "<strong>✅ تحقّق دائماً:</strong> كل تاريخ ورقم ومرجع يجب أن يتأكد في درسك.",
                            "<strong>✅ اطلب المنهجية:</strong> « اشرح كيف تصل إلى هذه النتيجة » لتتعلم لا لتتلقى فقط.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> recopier une réponse sans la relire ; faire confiance à un chatbot parce qu'il paraît sûr de lui (la confiance n'est pas la vérité) ; devenir dépendant (demander l'IA avant de réfléchir une seule minute) ; et le plagiat — déposer un texte généré comme s'il était de vous, sans le citer ni l'arranger.",
                        "<strong>❌ Mistakes to avoid:</strong> copying an answer without reading it; trusting a chatbot because it sounds sure (confidence is not truth); becoming dependent (asking AI before thinking for one minute); and plagiarism — submitting a generated text as your own, without citing or editing it.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> نسخ إجابة دون قراءتها؛ الثقة بروبوت لأنّه يبدو واثقاً (الثقة ليست صدقاً)؛ الاعتماد المفرط (سؤال الذكاء الاصطناعي قبل التفكير لمدة دقيقة)؛ والغش — تسليم نص مولّد كأنه لك دون استشهاد أو مراجعة.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["", "Mauvais prompt", "Bon prompt"],
                        ["", "Bad prompt", "Good prompt"],
                        ["", "صياغة ضعيفة", "صياغة قوية"],
                    ),
                    "rows": L(
                        [
                            ["Requête", "Résume ce cours.", "Je suis étudiant 2A PEP. Résume ce cours de psychologie en 5 idées clés avec un exemple pour le primaire à chaque idée, et dis-moi ce qui manque."],
                            ["Résultat", "Générique, trop long, vérifications impossibles.", "Ciblé, réutilisable pour l'exposé, limites signalées."],
                        ],
                        [
                            ["Prompt", "Summarise this lesson.", "I am a 2nd-year PEP student. Summarise this psychology lesson in 5 key ideas with a primary-class example per idea, and tell me what is missing."],
                            ["Result", "Generic, too long, impossible to check.", "Targeted, reusable for the presentation, limits flagged."],
                        ],
                        [
                            ["الطلب", "لخّص هذا الدرس.", "أنا طالب السنة الثانية PEP. لخّص درس علم النفس هذا في خمس أفكار رئيسية مع مثال للمرحلة الابتدائية لكل فكرة، وحدّد ما ينقص."],
                            ["النتيجة", "عام، طويل، تعذر التحقق منه.", "محدد، قابل لإعادة الاستعمال، مع تنبيه إلى الحدود."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce gain de temps :</strong> créez dès maintenant un fichier « mémo prompts » (dans Notion ou un simple bloc-notes) et enregistrez-y chaque invitation réussie. Posez la question d'abord, réfléchissez-y une minute, puis lisez la réponse comme un livre que vous devez critiquer.",
                        "<strong>Time-saving tip:</strong> create a \"prompt memo\" file right now (in Notion or a simple notepad) and save every successful prompt. Ask the question first, think about it for one minute, then read the answer like a book you must critique.",
                        "<strong>نصيحة لكسب الوقت:</strong> أنشئ الآن ملف « مذكرة الصيغ » (في Notion أو دفتر بسيط) وسجّل فيه كل صياغة ناجحة. اطرح السؤال أولاً، فكّر فيه لدقيقة، ثم اقرأ الجواب ككتاب يجب أن تنقّده.",
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Le chatbot « cherche » la réponse dans une grande bibliothèque ?",
                "Does a chatbot \"look up\" the answer in a big library?",
                "هل « يبحث » روبوت الدردشة عن الجواب في مكتبة كبيرة؟",
            ),
            "r": L(
                "Non. Il reconstitue la réponse mot après mot, selon les probabilités apprises sur ses données. Il n'a pas accès à « la vérité ».",
                "No. It rebuilds the answer word by word, according to probabilities learned from its data. It has no access to \"the truth\".",
                "لا. يعيد بناء الجواب كلمة كلمة حسب الاحتمالات المتعلَّمة من بياناته. ليس لديه وصول إلى « الحقيقة ».",
            ),
        },
        {
            "q": L(
                "Pourquoi peut-il inventer une référence quand il a l'air si sûr de lui ?",
                "Why can it invent a reference when it looks so confident?",
                "لماذا يختلق مرجعاً رغم أنه يبدو واثقاً جداً؟",
            ),
            "r": L(
                "Parce qu'il est entraîné à produire des phrases plausibles et convaincantes. La confiance n'est PAS un indicateur de vérité.",
                "Because it is trained to produce plausible, convincing sentences. Confidence is NOT an indicator of truth.",
                "لأنه مدرَّب على إنتاج جُمل محتملة ومقنعة. الثقة ليست مؤشراً على الصدق.",
            ),
        },
        {
            "q": L(
                "ChatGPT appartient à quelle famille d'IA : faible, générale ou super-IA ?",
                "Which AI family does ChatGPT belong to: narrow, general or super-AI?",
                "إلى أي عائلة ينتمي ChatGPT: ضيّقة، أم عامة، أم فائقة؟",
            ),
            "r": L(
                "IA faible : excellente dans la génération de texte, mais incapable de faire « n'importe quelle tâche » comme un humain.",
                "Narrow AI: excellent at text generation, but unable to do \"any task\" like a human.",
                "ذكاء ضيّق: بارع في توليد النصوص، لكنه غير قادر على أداء « أي مهمة » كالإنسان.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "Classe les 6 affirmations suivantes en Vrai (V) ou Faux (F), puis justifie en une ligne : 1) L'IA pense comme un humain. 2) L'IA a été entraînée sur des textes. 3) L'IA donne toujours des bonnes réponses. 4) L'IA peut inventer une référence. 5) L'IA remplace le professeur. 6) L'IA peut t'aider à réviser si tu vérifies.",
            "Classify the 6 statements as True (T) or False (F), then justify in one line: 1) AI thinks like a human. 2) AI was trained on texts. 3) AI always gives good answers. 4) AI can invent a reference. 5) AI replaces the teacher. 6) AI can help you revise if you check.",
            "صنّف الجمل الست صحيح (ص) أو خطأ (خ)، ثم برّر في سطر واحد: 1) يفكر الذكاء الاصطناعي كالإنسان. 2) دُرِّب الذكاء الاصطناعي على نصوص. 3) يعطي الذكاء الاصطناعي إجابات صحيحة دائماً. 4) يمكن للذكاء الاصطناعي اختلاق مرجع. 5) يعوّض الذكاء الاصطناعي الأستاذ. 6) يساعدك الذكاء الاصطناعي على المراجعة إذا تحققت.",
        ),
        "demarche": L(
            "1) Lis chaque affirmation. 2) Demande-toi : « Qu'ai-je appris sur la façon dont l'IA produit une réponse ? ». 3) Note V ou F puis une justification. 4) Compare avec ton voisin avant la correction collective.",
            "1) Read each statement. 2) Ask yourself: \"What did I learn about how AI produces an answer?\". 3) Write T or F plus a justification. 4) Compare with your neighbour before the collective correction.",
            "1) اقرأ كل جملة. 2) اسأل نفسك: « ماذا تعلمت عن طريقة إنتاج الذكاء الاصطناعي للإجابة؟ ». 3) سجّل ص أو خ ثم تبريراً. 4) قارن مع زميلك قبل التصحيح الجماعي.",
        ),
        "solution": L(
            "1) F — l'IA calcule des probabilités, elle n'a ni conscience ni pensées. 2) V — c'est son apprentissage. 3) F — elle peut se tromper et même inventer (halluciner). 4) V — c'est très fréquent, d'où la règle « vérifie ». 5) F — elle assiste l'étudiant, l'évaluation et le dialogue restent humains. 6) V — à condition de vérifier le contenu avec ton cours et tes sources.",
            "1) F — AI computes probabilities; it has neither consciousness nor thoughts. 2) T — that is its training. 3) F — it can err and even invent (hallucinate). 4) T — very common, hence the \"verify\" rule. 5) F — it assists the student; assessment and dialogue remain human. 6) T — provided you check the content against your lesson and sources.",
            "1) خ — يحسب الاحتمالات، لا وعي ولا أفكار. 2) ص — ذلك هو تدريبه. 3) خ — يخطئ وقد يختلق (يهلوس). 4) ص — شائع جداً، ومن هنا قاعدة « تحقّق ». 5) خ — يساعد الطالب؛ التقييم والحوار يبقيان بشريين. 6) ص — بشرط التحقق بالمقارنة مع درسك ومصادرك.",
        ),
    },
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
                "L'IA est un programme qui apprend à partir d'exemples pour imiter des capacités humaines.",
                "AI is a program that learns from examples to imitate human abilities.",
                "الذكاء الاصطناعي برنامج يتعلم من الأمثلة ليحاكي قدرات بشرية.",
            ),
            L(
                "Un chatbot est une machine à prédire le mot suivant, entraînée à être convaincante — pas vraie.",
                "A chatbot is a next-word prediction machine, trained to be convincing — not true.",
                "روبوت الدردشة آلة تتنبأ بالكلمة التالية، مدرَّبة على الإقناع — لا على الصدق.",
            ),
            L(
                "Hallucination = invention confiante. C'est fréquent, pas un bug.",
                "Hallucination = confident invention. It is common, not a bug.",
                "الهلوسة = اختلاق بثقة. شائعة، وليست خللاً.",
            ),
            L(
                "3 familles : IA faible (tout ce qu'on utilise), générale (future), super-IA (films).",
                "3 families: narrow AI (everything we use), general (future), super-AI (films).",
                "3 عائلات: ضيّق (كل ما نستعمله)، عام (مستقبلي)، فائق (أفلام).",
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
    "activites": [
        L(
            "Nuage de mots : chaque étudiant donne un mot associé à « IA », on le note au tableau, puis on regroupe par thème.",
            "Word cloud: each student gives a word linked to \"AI\", it is written on the board, then grouped by theme.",
            "خريطة كلمات: كل طالب يعطي كلمة عن « الذكاء الاصطناعي »، تُكتب على السبورة ثم تصنَّف.",
        ),
        L(
            "Sondage « mes usages » à main levée : as-tu déjà utilisé un chatbot ? pour quoi ? avec quel résultat ?",
            "Show-of-hands \"my uses\" survey: have you used a chatbot? for what? with what result?",
            "استطلاع « استعمالاتي » برفع اليد: هل استعملت روبوت دردشة؟ لماذا؟ وبنيتجة ؟",
        ),
        L(
            "Démo guidée (si connexion) : résumer un paragraphe du cours, puis vérifier : l'IA invente-t-elle quelque chose ?",
            "Guided demo (if online): summarise a paragraph of the lesson, then check: does AI invent anything?",
            "عرض موجّه (إن توفرت الشبكة): تلخيص فقرة، ثم تحقّق: هل يختلق الذكاء الاصطناعي شيئاً؟",
        ),
        L(
            "Jeu « vrai ou faux » (exercice guidé) : 6 idées reçues sur l'IA départagées collectivement.",
            "True/false game (guided exercise): 6 common beliefs about AI, sorted collectively.",
            "لعبة « صحيح أم خطأ » (تمرين موجّه): 6 أفكار شائعة تُحسم جماعياً.",
        ),
    ],
    "retenir": [
        L(
            "L'IA = programme qui apprend à partir d'exemples pour imiter des capacités humaines.",
            "AI = a program that learns from examples to imitate human abilities.",
            "الذكاء الاصطناعي = برنامج يتعلم من الأمثلة ليحاكي قدرات بشرية.",
        ),
        L(
            "Un chatbot prédit le mot suivant ; il peut être convaincant sans être vrai. Hallucinations : fréquentes.",
            "A chatbot predicts the next word; it can be convincing without being true. Hallucinations: common.",
            "روبوت الدردشة يتنبأ بالكلمة التالية؛ مقنع دون أن يكون صادقاً. الهلوسة: شائعة.",
        ),
        L(
            "5 usages pour tes études : rechercher, résumer, rédiger, réviser, organiser.",
            "5 uses for your studies: search, summarise, write, revise, organise.",
            "5 استعمالات لدراستك: بحث، تلخيص، كتابة، مراجعة، تنظيم.",
        ),
        L(
            "L'IA ne pense pas, ne ressent pas, n'apprend rien à ta place : la compréhension reste ton travail.",
            "AI does not think, does not feel, learns nothing for you: understanding remains your work.",
            "الذكاء الاصطناعي لا يفكر ولا يشعر ولا يتعلم مكانك: الفهم يبقى عملك.",
        ),
        L(
            "3 règles d'or : vérifier, citer, garder ton jugement.",
            "3 golden rules: verify, cite, keep your judgement.",
            "3 قواعد ذهبية: تحقّق، استشهد، حافظ على حكمك.",
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