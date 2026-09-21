# -*- coding: utf-8 -*-
"""Séance 02 — Rechercher et comprendre l'information avec l'IA (PEP 2A — ENS)."""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 2,
    "slug": "seance-02",
    "icon": "🔎",
    "titles": L(
        "Rechercher et comprendre l'information avec l'IA",
        "Searching and understanding information with AI",
        "البحث عن المعلومات وفهمها بالذكاء الاصطناعي",
    ),
    "descriptions": L(
        "Apprendre à formuler des requêtes efficaces et à utiliser ChatGPT, Perplexity, Google Scholar et Consensus pour trouver et comprendre de l'information fiable pour tes études.",
        "Learn to write effective queries and to use ChatGPT, Perplexity, Google Scholar and Consensus to find and understand reliable information for your studies.",
        "أن تتعلّم صياغة طلبات بحث فعّالة واستعمال ChatGPT وPerplexity وGoogle Scholar وConsensus لإيجاد معلومات موثوقة وفهمها في دراستك.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Distinguer un chatbot conversationnel, un moteur de recherche et une base de données académiques.",
            "Distinguish a conversational chatbot, a search engine and an academic database.",
            "أن تميّز بين روبوت المحادثة، ومحرّك البحث، وقاعدة البيانات الأكاديمية.",
        ),
        L(
            "Formuler une requête précise en 4 composantes : contexte, objectif, format et contrainte.",
            "Write a precise query with 4 components: context, goal, format and constraint.",
            "أن تصوغ طلباً دقيقاً من أربعة عناصر: السياق، والهدف، والصيغة، والقيود.",
        ),
        L(
            "Utiliser Perplexity pour obtenir une réponse accompagnée de sources citées.",
            "Use Perplexity to get an answer with cited sources.",
            "أن تستعمل Perplexity للحصول على إجابة مرفقة بمصادر مذكورة.",
        ),
        L(
            "Chercher de la littérature scientifique avec Google Scholar et Consensus (mots-clés, tri, résumé).",
            "Search scientific literature with Google Scholar and Consensus (keywords, sorting, abstracts).",
            "أن تبحث في الأدبيات العلمية بواسطة Google Scholar وConsensus (كلمات مفتاحية، ترتيب، ملخصات).",
        ),
        L(
            "Évaluer la fiabilité d'une information en croisant au moins deux sources.",
            "Assess the reliability of information by cross-checking at least two sources.",
            "أن تقيّم موثوقية معلومة عبر تطابق مصدرين على الأقل.",
        ),
    ],
    "prerequis": L(
        "Séance 1 suivie. Savoir ouvrir un navigateur et avoir (si possible) un compte gratuit sur un outil d'IA.",
        "Session 1 completed. Know how to open a browser and, if possible, have a free account on an AI tool.",
        "إتمام الحصة الأولى. معرفة فتح متصفّح، وإن أمكن امتلاك حساب مجاني على أداة ذكاء اصطناعي.",
    ),
    "plan": [
        {
            "time": "00–10",
            **L(
                "Accueil, rappel et tour de table",
                "Welcome, recap and round table",
                "استقبال ومراجعة وجولة",
            ),
            "detail": L(
                "Rappel des 3 règles d'or. Sondage : « Où cherchez-vous une information aujourd'hui ? ».",
                "Recap of the 3 golden rules. Survey: \"Where do you look for information today?\".",
                "مراجعة القواعد الذهبية الثلاث. استطلاع: « أين تبحثون عن معلومة اليوم؟ ».",
            ),
        },
        {
            "time": "10–30",
            **L(
                "Partie 1 : 4 outils pour 4 besoins",
                "Part 1: 4 tools for 4 needs",
                "الجزء الأوّل: أربع أدوات لأربع حاجات",
            ),
            "detail": L(
                "Chatbot (comprendre), Perplexity (réponses sourcées), Google Scholar (articles), Consensus (consensus scientifique).",
                "Chatbot (understand), Perplexity (sourced answers), Google Scholar (articles), Consensus (scientific consensus).",
                "روبوت المحادثة (الفهم)، Perplexity (إجابات بمصادر)، Google Scholar (مقالات)، Consensus (إجماع علمي).",
            ),
        },
        {
            "time": "30–45",
            **L(
                "Partie 2 : Formuler une bonne requête",
                "Part 2: Writing a good query",
                "الجزء الثاني: صياغة طلب جيد",
            ),
            "detail": L(
                "Les 4 composantes (contexte, objectif, format, contrainte) + exemples avant/après.",
                "The 4 components (context, goal, format, constraint) + before/after examples.",
                "العناصر الأربعة (سياق، هدف، صيغة، قيد) + أمثلة قبل/بعد.",
            ),
        },
        {
            "time": "45–65",
            **L(
                "Partie 3 : La littérature scientifique",
                "Part 3: Scientific literature",
                "الجزء الثالث: الأدبيات العلمية",
            ),
            "detail": L(
                "Google Scholar et Consensus : mots-clés, filtres, lire un résumé, repérer la revue et l'année.",
                "Google Scholar and Consensus: keywords, filters, reading an abstract, spotting the journal and the year.",
                "Google Scholar وConsensus: كلمات مفتاحية، فلاتر، قراءة الملخص، تمييز المجلة والسنة.",
            ),
        },
        {
            "time": "65–80",
            **L(
                "Activité : compétition de requêtes",
                "Activity: query competition",
                "نشاط: مسابقة الصياغات",
            ),
            "detail": L(
                "Par binômes : même question, meilleure requête pour 2 outils, puis comparaison des résultats.",
                "In pairs: same question, best query for 2 tools, then comparison of results.",
                "في مجموعات ثنائية: نفس السؤال، أفضل صياغة لأداتين، ثم مقارنة النتائج.",
            ),
        },
        {
            "time": "80–90",
            **L(
                "Synthèse et annonce de la séance 3",
                "Wrap-up and preview of session 3",
                "خلاصة وتقديم الحصة الثالثة",
            ),
"detail": L(
                "« À retenir », questions. Annonce : approfondir la recherche avec Perplexity et vérifier la fiabilité des sources.",
                "Key takeaways, Q&A. Preview: going deeper with Perplexity and checking source reliability.",
                "« ما يجب تذكّره » والأسئلة. تقديم: تعميق البحث بـ Perplexity والتحقق من موثوقية المصادر.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "4 outils pour 4 besoins différents",
                "4 tools for 4 different needs",
                "أربع أدوات لأربع حاجات مختلفة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Le réflexe du bon étudiant : choisir l'outil selon le besoin, pas l'inverse. Une même question peut recevoir des réponses très différentes selon l'outil.",
                        "The good student's reflex: choose the tool according to the need, not the other way round. The same question can get very different answers depending on the tool.",
                        "من سلوك الطالب الجيّد: اختيار الأداة حسب الحاجة، لا العكس. قد تتلقّى نفس السؤال إجابات مختلفة جداً حسب الأداة.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["Besoin", "Outil", "Ce qu'il fait", "Limite"],
                        ["Need", "Tool", "What it does", "Limit"],
                        ["حاجة", "أداة", "ما تفعله", "حدّها"],
                    ),
                    "rows": L(
                        [
                            ["Comprendre un concept", "ChatGPT / Gemini", "Explique, reformule, résume", "Peut halluciner, pas de sources"],
                            ["Réponse + sources", "Perplexity", "Répond avec des liens cités", "Sources pas toujours de qualité"],
                            ["Trouver des articles", "Google Scholar", "Indexe des articles et citations", "Pas de synthèse, outil brut"],
                            ["Savoir ce que dit la science", "Consensus", "Résume des études sur une question", "Anglais + sciences avant tout"],
                        ],
                        [
                            ["Understanding a concept", "ChatGPT / Gemini", "Explains, rephrases, summarises", "Can hallucinate, no sources"],
                            ["Answer + sources", "Perplexity", "Answers with cited links", "Sources not always high-quality"],
                            ["Finding articles", "Google Scholar", "Indexes papers and citations", "No synthesis, raw tool"],
                            ["Knowing what science says", "Consensus", "Summarises studies on a question", "English + science first"],
                        ],
                        [
                            ["فهم مفهوم", "ChatGPT / Gemini", "يشرح ويعيد الصياغة ويلخّص", "قد يهلوس، بلا مصادر"],
                            ["إجابة + مصادر", "Perplexity", "يجيب مع روابط مذكورة", "المصادر ليست دائماً عالية الجودة"],
                            ["إيجاد مقالات", "Google Scholar", "يفهرس المقالات والاستشهادات", "لا تلخيص، أداة خام"],
                            ["معرفة ما تقوله الدراسات", "Consensus", "يلخّص دراسات حول سؤال", "إنجليزية + علوم بالأساس"],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Règle du bon réflexe :</strong> pour « comprendre », un chatbot ; pour « vérifier », Perplexity ; pour « citer un article », Google Scholar ; pour « connaître le consensus », Consensus.",
                        "<strong>Good-reflex rule:</strong> to \"understand\", a chatbot; to \"check\", Perplexity; to \"cite a paper\", Google Scholar; to \"know the consensus\", Consensus.",
                        "<strong>قاعدة السلوك الجيّد:</strong> لـ « الفهم » روبوت محادثة؛ لـ « التثبّت » Perplexity؛ لـ « الاستشهاد بمقال » Google Scholar؛ لـ « معرفة الإجماع » Consensus.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Formuler une requête efficace : 4 composantes",
                "Writing an effective query: 4 components",
                "صياغة طلب فعّال: أربعة عناصر",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "La qualité de la réponse dépend de la qualité de la question. Ajoute du contexte et de la précision : l'IA n'est pas dans ta tête.",
                        "The quality of the answer depends on the quality of the question. Add context and precision: AI is not inside your head.",
                        "جودة الإجابة تتوقف على جودة السؤال. أضف السياق والدقّة: الذكاء الاصطناعي ليس داخل رأسك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1. Contexte</strong> : qui tu es, de quel cours il s'agit, ton niveau.",
                            "<strong>2. Objectif</strong> : que veux-tu faire de la réponse (comprendre, citer, réviser) ?",
                            "<strong>3. Format</strong> : liste, tableau, résumé, plan, 5 lignes…",
                            "<strong>4. Contrainte</strong> : sources à privilégier, langue, ton, date de fraîcheur.",
                        ],
                        [
                            "<strong>1. Context</strong>: who you are, which lesson it concerns, your level.",
                            "<strong>2. Goal</strong>: what will you do with the answer (understand, cite, revise)?",
                            "<strong>3. Format</strong>: list, table, summary, outline, 5 lines…",
                            "<strong>4. Constraint</strong>: preferred sources, language, tone, freshness date.",
                        ],
                        [
                            "<strong>1. السياق</strong>: من أنت، أي درس، ما مستواك.",
                            "<strong>2. الهدف</strong>: ماذا ستفعل بالإجابة (فهم، استشهاد، مراجعة)؟",
                            "<strong>3. الصيغة</strong>: قائمة، جدول، ملخص، خطة، خمس أسطر…",
                            "<strong>4. القيود</strong>: مصادر مفضلة، لغة، نبرة، تاريخ حداثة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Exemple « avant » :</strong> « parle-moi de Piaget ». <br><strong>Exemple « après » :</strong> « Je suis étudiant en 2ème année PEP, cours de psychologie de l'enfant niveau licence. Explique-moi en 10 lignes la théorie du développement cognitif de Piaget, avec 3 exemples concrets utilisables en classe de primaire. »",
                        "<strong>\"Before\" example:</strong> \"Tell me about Piaget\". <br><strong>\"After\" example:</strong> \"I am a 2nd-year PEP student, bachelor-level child psychology course. Explain in 10 lines Piaget's theory of cognitive development, with 3 concrete examples usable in primary class.\"",
                        "<strong>مثال « قبل »:</strong> « حدّثني عن بياجيه ». <br><strong>مثال « بعد »:</strong> « أنا طالب في الثانية PEP، درس علم نفس الطفل بمستوى ليسانس. اشرح لي في عشرة أسطر نظرية بياجيه في النمو المعرفي، مع ثلاثة أمثلة ملموسة قابلة للاستعمال في قسم الابتدائي ».",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Chercher et lire de la littérature scientifique",
                "Searching and reading scientific literature",
                "البحث في الأدبيات العلمية وقراءتها",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Pour ton mémoire, un exposé ou un dossier, Google Scholar et Consensus donnent accès à des études vérifiables. Apprends à les interroger comme un chercheur débutant.",
                        "For your thesis, a presentation or a portfolio, Google Scholar and Consensus give access to verifiable studies. Learn to query them like a beginner researcher.",
                        "لمذكّرتك أو عرضك أو ملفّك، يمنحك Google Scholar وConsensus الوصول إلى دراسات قابلة للتحقق. تعلّم الاستعلام فيها كباحث مبتدئ.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Choisis tes mots-clés</strong> : traduis-les en anglais (la science s'écrit surtout en anglais) et ajoute des synonymes.",
                            "<strong>Utilise les filtres</strong> : année, langue, auteur, « depuis 2015 » pour des données récentes.",
                            "<strong>Lis le résumé (abstract)</strong> avant de lire l'article : question, méthode, résultat.",
                            "<strong>Repère la revue et la date</strong> : une revue à comité de lecture est plus fiable qu'un site commercial.",
                            "<strong>Consensus</strong> : pose une question claire, lis le « consensus meter » et compare 2-3 études.",
                        ],
                        [
                            "<strong>Choose your keywords</strong>: translate them into English (science is mostly written in English) and add synonyms.",
                            "<strong>Use filters</strong>: year, language, author, \"since 2015\" for recent data.",
                            "<strong>Read the abstract</strong> before the full paper: question, method, result.",
                            "<strong>Spot the journal and the date</strong>: a peer-reviewed journal is more reliable than a commercial site.",
                            "<strong>Consensus</strong>: ask a clear question, read the \"consensus meter\" and compare 2-3 studies.",
                        ],
                        [
                            "<strong>اختر كلماتك المفتاحية</strong>: ترجمها إلى الإنجليزية (العلم يُكتب غالباً بالإنجليزية) وأضف مترادفات.",
                            "<strong>استعمل الفلاتر</strong>: السنة، اللغة، المؤلف، « منذ 2015 » للحصول على بيانات حديثة.",
                            "<strong>اقرأ الملخص</strong> قبل قراءة المقال: السؤال، المنهج، النتيجة.",
                            "<strong>ميّز المجلة والتاريخ</strong>: مجلة محكّمة أوثق من موقع تجاري.",
                            "<strong>Consensus</strong>: اطرح سؤالاً واضحاً، اقرأ « مقياس الإجماع » وقارن 2-3 دراسات.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>Piège fréquent :</strong> demander à un chatbot de « citer des sources » peut produire des références inventées. Toujours vérifier dans Google Scholar qu'elle existe réellement (titre, auteurs, année).",
                        "<strong>Common trap:</strong> asking a chatbot to \"cite sources\" can produce invented references. Always check in Google Scholar that it really exists (title, authors, year).",
                        "<strong>مصيدة شائعة:</strong> طلب « مصادر » من روبوت محادثة قد يولّد مراجع مختلقة. تحقّق دائماً في Google Scholar من وجودها فعلاً (العنوان، المؤلفون، السنة).",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Évaluer et croiser les sources",
                "Evaluating and cross-checking sources",
                "تقييم المصادر وتطابقها",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une information répétée est plus fiable qu'une information isolée. Confronte toujours l'IA à ton cours, tes polycopiés et au moins une source officielle.",
                        "Information that is repeated is more reliable than isolated information. Always confront AI with your lesson, your handouts and at least one official source.",
                        "المعلومة المتكررة أوثق من المعلومة المنعزلة. قارن دائماً الذكاء الاصطناعي بدرسك وطبقاتك ومصدر رسمي واحد على الأقل.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Qui ?</strong> L'auteur est-il identifiable ? est-il qualifié (université, organisme) ?",
                            "<strong>Quand ?</strong> La date : une info de 2019 sur un sujet qui évolue vite (IA, politique) peut être périmée.",
                            "<strong>Quoi ?</strong> Fait vérifiable, analyse sourcée, ou simple opinion ?",
                            "<strong>Vérifiable ?</strong> Peux-tu retrouver la même info ailleurs (Perplexity + Google Scholar + cours) ?",
                            "<strong>Pourquoi ?</strong> Le but du document : informer, vendre, convaincre, tromper ?",
                        ],
                        [
                            "<strong>Who?</strong> Is the author identifiable? Are they qualified (university, organisation)?",
                            "<strong>When?</strong> The date: 2019 information on a fast-moving topic (AI, politics) may be outdated.",
                            "<strong>What?</strong> Verifiable fact, sourced analysis, or mere opinion?",
                            "<strong>Checkable?</strong> Can you find the same information elsewhere (Perplexity + Google Scholar + lesson)?",
                            "<strong>Why?</strong> The document's purpose: inform, sell, persuade, deceive?",
                        ],
                        [
                            "<strong>من؟</strong> هل المؤلف محدّد؟ وهل هو مؤهّل (جامعة، مؤسسة)؟",
                            "<strong>متى؟</strong> التاريخ: معلومة 2019 في موضوع سريع التغيّر (الذكاء الاصطناعي، السياسة) قد تكون قديمة.",
                            "<strong>ماذا؟</strong> حقيقة قابلة للتحقق، تحليل بمصادر، أم رأي فقط؟",
                            "<strong>قابل للتحقق؟</strong> هل تجد المعلومة نفسها في مكان آخر (Perplexity + Google Scholar + درسك)؟",
                            "<strong>لماذا؟</strong> غاية الوثيقة: إعلام، بيع، إقناع، تضليل؟",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>À retenir :</strong> « 2 sources indépendantes qui concordent » est une base saine. Une seule source = doute raisonnable.",
                        "<strong>Remember:</strong> \"two independent sources that agree\" is a sound basis. A single source = reasonable doubt.",
                        "<strong>تذكّر:</strong> « مصدران مستقلان يتفقان » أساس سليم. مصدر واحد = شكّ معقول.",
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
                        "La règle ici est simple : jamais un seul outil pour tout, jamais un outil sans vérification. Combinez les familles (texte + recherche + quiz) et gardez toujours le dernier mot.",
                        "The rule here is simple: never one single tool for everything, never a tool without checking. Combine families (text + search + quiz) and always keep the final word.",
                        "القاعدة هنا بسيطة: لا أداة واحدة لكل شيء أبداً، ولا أداة دون تحقّق. اجمع بين العائلات (نصّ + بحث + اختبار) واحتفظ دائماً بكلمة الفصل.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Choisir selon la tâche :</strong> rédiger → assistant de texte ; illustrer → générateur d'images ; vérifier → Perplexity / Scholar ; présenter → Gamma.",
                            "<strong>✅ Tester avant la classe :</strong> version gratuite, langue, publicité, âge minimum des élèves.",
                            "<strong>✅ Gérer ses données :</strong> ne jamais donner de données personnelles d'élèves ni de documents confidentiels.",
                            "<strong>✅ Comparer 2 outils :</strong> poser la même question à deux IA et regarder les différences.",
                        ],
                        [
                            "<strong>✅ Choose by task:</strong> write → text assistant; illustrate → image generator; check → Perplexity / Scholar; present → Gamma.",
                            "<strong>✅ Test before class:</strong> free version, language, advertising, minimum pupil age.",
                            "<strong>✅ Manage your data:</strong> never feed pupils' personal data or confidential documents.",
                            "<strong>✅ Compare 2 tools:</strong> ask the same question to two AIs and look at the differences.",
                        ],
                        [
                            "<strong>✅ اختر حسب المهمّة:</strong> الكتابة → مساعد نصّي؛ التوضيح → مولّد صور؛ التحقق → Perplexity / Scholar؛ العرض → Gamma.",
                            "<strong>✅ جرّب قبل القسم:</strong> النسخة المجانية، اللغة، الإعلانات، السنّ الأدنى للتلاميذ.",
                            "<strong>✅ دبّر بياناتك:</strong> لا تُدخل أبداً بيانات تلاميذ شخصية ولا وثائق سرّية.",
                            "<strong>✅ قارن أداتين:</strong> اطرح السؤال نفسه على ذكاءين اصطناعيين ولاحظ الفروق.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> utiliser le premier outil trouvé sans vérifier sa politique de données, croire qu'une réponse « gratuite » est sans publicité, et surtout <strong>montrer aux élèves un contenu jamais relu</strong>. L'IA propose, l'enseignant dispose.",
                        "<strong>❌ Mistakes to avoid:</strong> using the first tool found without checking its data policy, believing that a \"free\" tool has no advertising, and above all <strong>showing pupils content never proofread</strong>. AI proposes, the teacher disposes.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> استعمال أول أداة دون فحص سياسة بياناتها، والاعتقاد أن الأداة « المجانية » خالية من الإعلانات، وخصوصاً <strong>عرض محتوى غير مراجَع على التلاميذ</strong>. الذكاء الاصطناعي يقترح والمعلّم يقرّر.",
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
                            ["Demande", "« Donne-moi une leçon sur la forêt. »", "« Tu es un enseignant de CP. Pour ma leçon de découverte, propose-moi 3 activités courtes sur la forêt, avec le matériel et la durée de chacune. »"],
                            ["Outil", "Un seul chatbot, réponse non relue.", "ChatGPT pour rédiger + Perplexity pour vérifier + Canva pour l'affiche."],
                        ],
                        [
                            ["Request", "\"Give me a lesson about the forest.\"", "\"You are a Year-1 teacher. For my discovery lesson, suggest 3 short forest activities with materials and timings.\""],
                            ["Tool", "A single chatbot, unproofread answer.", "ChatGPT to write + Perplexity to check + Canva for the poster."],
                        ],
                        [
                            ["الطلب", "« أعطني درساً عن الغابة »", "« أنت معلّم تحضيري. لدرس اكتشافي، اقترح 3 أنشطة قصيرة عن الغابة مع الأدوات ومددها »"],
                            ["الأداة", "روبوت واحد، جواب غير مراجَع.", "ChatGPT للكتابة + Perplexity للتحقق + Canva للملصق."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce de sélection :</strong> créez un petit tableau « besoin → outil → version gratuite ? → RGPD ? » dans vos notes. Vous le réutiliserez pour chaque préparation de cours.",
                        "<strong>Selection tip:</strong> keep a small table \"need → tool → free version? → GDPR?\" in your notes. You will reuse it for every lesson preparation.",
                        "<strong>نصيحة للاختيار:</strong> احتفظ بجدول صغير « الحاجة → الأداة → نسخة مجانية؟ → حماية البيانات؟ » في ملاحظاتك. ستعيد استعماله في كل تحضير درس.",
                    ),
                },
            ],
        },
    ],
    "activites": [
        L(
            "Avant/après : transformer 3 mauvaises questions en requêtes complètes (contexte, objectif, format, contrainte).",
            "Before/after: turn 3 poor questions into complete queries (context, goal, format, constraint).",
            "قبل/بعد: حوّل ثلاث أسئلة سيئة إلى طلبات كاملة (سياق، هدف، صيغة، قيد).",
        ),
        L(
            "Comparaison : poser la même question à un chatbot et à Perplexity ; noter les différences de sources et de précision.",
            "Comparison: ask the same question to a chatbot and to Perplexity; note the differences in sources and precision.",
            "مقارنة: اطرح السؤال نفسه على روبوت محادثة وPerplexity؛ سجّل اختلافات المصادر والدقّة.",
        ),
        L(
            "Missions Scholar : trouver 3 articles sur un thème du programme (année, revue, auteur) et rédiger une fiche de lecture de 5 lignes chacun.",
            "Scholar missions: find 3 papers on a curriculum topic (year, journal, author) and write a 5-line reading sheet for each.",
            "مهام Scholar: ابحث عن ثلاث مقالات حول موضوع من البرنامج (سنة، مجلة، مؤلف) واكتب بطاقة قراءة من خمسة أسطر لكل منها.",
        ),
        L(
            "Défi « source fantôme » : demander à un chatbot un article sur un thème, vérifier dans Google Scholar s'il existe vraiment, puis corriger la référence.",
            "\"Ghost source\" challenge: ask a chatbot for a paper on a topic, check in Google Scholar whether it really exists, then fix the reference.",
            "تحدّي « المصدر الوهمي »: اطلب من روبوت محادثة مقالاً حول موضوع، تحقّق في Google Scholar من وجوده فعلاً، ثم صحّح المرجع.",
        ),
    ],
    "retenir": [
        L(
            "Choisir l'outil selon le besoin : comprendre (chatbot), vérifier (Perplexity), citer (Scholar), consensus (Consensus).",
            "Choose the tool by need: understand (chatbot), check (Perplexity), cite (Scholar), consensus (Consensus).",
            "اختر الأداة حسب الحاجة: الفهم (روبوت محادثة)، التثبّت (Perplexity)، الاستشهاد (Scholar)، الإجماع (Consensus).",
        ),
        L(
            "Une bonne requête a 4 composantes : contexte, objectif, format, contrainte.",
            "A good query has 4 components: context, goal, format, constraint.",
            "الطلب الجيد له أربعة عناصر: سياق، هدف، صيغة، قيد.",
        ),
        L(
            "La science s'écrit surtout en anglais : traduis tes mots-clés et utilise les filtres (année, revue).",
            "Science is mostly written in English: translate your keywords and use filters (year, journal).",
            "العلم يُكتب غالباً بالإنجليزية: ترجم كلماتك المفتاحية واستعمل الفلاتر (سنة، مجلة).",
        ),
        L(
            "Les références générées peuvent être inventées : vérifie dans Google Scholar avant de citer.",
            "Generated references can be invented: check in Google Scholar before citing.",
            "المراجع المولَّدة قد تكون مختلقة: تحقّق في Google Scholar قبل الاستشهاد.",
        ),
        L(
            "2 sources indépendantes qui concordent = base saine. Une seule source = doute.",
            "2 independent sources that agree = sound basis. A single source = doubt.",
            "مصدران مستقلان يتفقان = أساس سليم. مصدر واحد = شكّ.",
        ),
    ],
    "glossaire": [
        {
            "term": "Moteur de recherche",
            "term_en": "Search engine",
            "def_fr": "Outil qui indexe des pages web et renvoie une liste de liens selon des mots-clés (Google, Bing).",
            "def_en": "A tool that indexes web pages and returns a list of links according to keywords (Google, Bing).",
            "def_ar": "أداة تفهرس صفحات الويب وتعرض قائمة روابط حسب كلمات مفتاحية (جوجل، بينغ).",
        },
        {
            "term": "Perplexity",
            "term_en": "Perplexity",
            "def_fr": "Assistant de recherche qui répond avec des sources citées en bas de réponse.",
            "def_en": "A research assistant that answers with sources cited at the bottom of the answer.",
            "def_ar": "مساعد بحث يجيب مع مصادر مذكورة أسفل الإجابة.",
        },
        {
            "term": "Google Scholar",
            "term_en": "Google Scholar",
            "def_fr": "Moteur spécialisé dans les articles scientifiques, les thèses et les citations.",
            "def_en": "A search engine specialised in scientific papers, theses and citations.",
            "def_ar": "محرّك متخصّص في المقالات العلمية والأطروحات والاستشهادات.",
        },
        {
            "term": "Consensus",
            "term_en": "Consensus",
            "def_fr": "Outil qui synthétise les conclusions d'études scientifiques sur une question.",
            "def_en": "A tool that synthesises the conclusions of scientific studies on a question.",
            "def_ar": "أداة تلخّص استنتاجات الدراسات العلمية حول سؤال.",
        },
        {
            "term": "Résumé (abstract)",
            "term_en": "Abstract",
            "def_fr": "Court paragraphe résumant question, méthode et résultats d'un article.",
            "def_en": "A short paragraph summarising a paper's question, method and results.",
            "def_ar": "فقرة قصيرة تلخّص سؤال المقال ومنهجه ونتائجه.",
        },
        {
            "term": "Source primaire / secondaire",
            "term_en": "Primary / secondary source",
            "def_fr": "Primaire : document original (étude, loi, texte de loi). Secondaire : document qui commente le primaire.",
            "def_en": "Primary: original document (study, law, legal text). Secondary: a document that comments on the primary.",
            "def_ar": "أولي: وثيقة أصلية (دراسة، قانون، نص تشريعي). ثانوي: وثيقة تعلّق على الأوّلي.",
        },
    ],
    "dialogues_fr": """# Séance 02 — Dialogues pédagogiques (Français)

## Dialogue A — « Google dit quoi, mais moi je dis quoi ? » (25 min)

**Personnages :** Salima (étudiante PEP 2A), Karim (camarade), l'assistante IA (jouée par la formatrice).

---

Salima : Karim, tu rédiges ton exposé sur « les écrans et le sommeil des enfants » ?

Karim : Oui… j'ai demandé à ChatGPT et il m'a donné plein de chiffres. Je vais les copier.

Salima : Attends ! Tu as vérifié ces chiffres d'où ils viennent ?

Karim : Euh… non. Il avait l'air sûr de lui.

Salima : Justement, c'est le piège ! Les références peuvent être inventées. On doit vérifier dans Google Scholar.

IA : Bonjour vous deux ! Je peux aider. Donnez-moi la question précise et je vous trouve des études, avec auteurs et années.

Salima : Parfait ! Question précise : « Quel est l'impact des écrans sur le sommeil chez l'enfant de 6 à 10 ans ? » — Tu peux me donner deux études récentes ?

IA : Voici deux études. Mais utilisez Google Scholar pour confirmer, puis lisez le résumé de chacune.

Karim : Et Perplexity, il ne sert à rien alors ?

Salima : Si ! Pour une réponse avec des sources citées tout de suite. ChatGPT pour comprendre, Perplexity pour vérifier, Scholar pour citer.

Karim : Et si ChatGPT et Perplexity se contredisent ?

Salima : Là, tu ouvres ton cours et tu cherches une troisième source. Deux sources indépendantes qui concordent…

Karim : … c'est une base saine ! Je commence à comprendre.

Salima : Et retiens : on ne copie pas un chiffre sans l'avoir retrouvé dans l'étude.

---

## Dialogue B — « Aide-moi, mais pas n'importe comment ! » (15 min)

**Personnages :** Lina (étudiante), le formateur (qui joue l'IA maladroite).

---

Lina : Je veux une réponse sur Vygotsky pour mon devoir.

IA : Bien sûr ! Vygotsky disait… [réponse vague et longue]

Lina : Hmm, tu me donnes tout sauf ce que je veux. Je suis en licence, cours de psychologie. Je veux une fiche : 3 idées-clés, 1 exemple de classe, 1 question d'examen possible.

IA : Ah, maintenant je comprends mieux ! [réponse structurée exactement comme demandée]

Lina : Là, c'est utile ! Le contexte et le format changeaient tout.

IA : Exactement. Contexte, objectif, format, contrainte. Retenez ces 4 mots.

Lina : Je note : « Je suis étudiant… », « je veux une fiche pour réviser… », « sous forme de tableau… », « avec un exemple de primaire ». Et ensuite je vérifie dans mon cours.

IA : Tu es une étudiante modèle !

Lina : Non, une étudiante critique. C'est encore mieux.

---

## Mini-rôle à jouer (3 min par binôme)
L'un de vous joue un étudiant qui veut recopier la première réponse d'un chatbot pour son devoir ; l'autre lui rappelle la méthode : infléchir la requête (contexte-objectif-format-contrainte), vérifier les sources, croiser avec le cours, et ne citer que ce qui a été vérifié.
""",
    "dialogues_en": """# Session 02 — Classroom dialogues (English)

## Dialogue A — "Google says what, but what do I say?" (25 min)

**Characters:** Salima (PEP 2A student), Karim (classmate), the AI assistant (played by the trainer).

---

Salima: Karim, you are writing your presentation on "screens and children's sleep", right?

Karim: Yes… I asked ChatGPT and it gave me lots of figures. I will copy them.

Salima: Wait! Did you check where those figures come from?

Karim: Hmm… no. It seemed so sure of itself.

Salima: Exactly, that is the trap! References can be invented. We must check in Google Scholar.

AI: Hello both of you! I can help. Give me your precise question and I find studies for you, with authors and years.

Salima: Perfect! Precise question: "What is the impact of screens on sleep in children aged 6 to 10?" — Can you give me two recent studies?

AI: Here are two studies. But use Google Scholar to confirm, then read the abstract of each.

Karim: And Perplexity? Is it useless then?

Salima: No! It is for an answer with cited sources right away. ChatGPT to understand, Perplexity to check, Scholar to cite.

Karim: And if ChatGPT and Perplexity contradict each other?

Salima: Then you open your lesson and look for a third source. Two independent sources that agree…

Karim: … are a sound basis! I'm starting to understand.

Salima: And remember: we never copy a figure without finding it again in the study.

---

## Dialogue B — "Help me, but not anyhow!" (15 min)

**Characters:** Lina (student), the trainer (playing a clumsy AI).

---

Lina: I want an answer about Vygotsky for my assignment.

AI: Of course! Vygotsky said… [vague, long answer]

Lina: Hmm, you give me everything except what I want. I am an undergraduate, psychology course. I want a sheet: 3 key ideas, 1 classroom example, 1 possible exam question.

AI: Ah, now I understand better! [answer structured exactly as requested]

Lina: Now that is useful! The context and the format changed everything.

AI: Exactly. Context, goal, format, constraint. Remember these 4 words.

Lina: I note: "I am a student…", "I want a sheet to revise…", "as a table…", "with a primary example". And afterwards I check with my lesson.

AI: You are a model student!

Lina: No, a critical student. That is even better.

---

## Mini role-play (3 min per pair)
One of you plays a student who wants to copy a chatbot's first answer for their assignment; the other reminds them of the method: refine the query (context-goal-format-constraint), check the sources, cross-check with the lesson, and cite only what has been verified.
""",
}