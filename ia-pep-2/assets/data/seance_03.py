# -*- coding: utf-8 -*-
"""Séance 03 — Rechercher et comprendre l'information avec l'IA (PEP 2A — ENS)."""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 3,
    "slug": "seance-03",
    "icon": "🔎",
    "titles": L(
        "Approfondir la recherche : Perplexity, Scholar et fiabilité des sources",
        "Deeper research: Perplexity, Scholar and source reliability",
        "تعميق البحث: Perplexity وScholar وموثوقية المصادر",
    ),
    "descriptions": L(
        "Trouver vite l'information juste pour ses modules : formuler une bonne question de recherche, utiliser Perplexity (sources citées), Google Scholar et Consensus, puis croiser les sources.",
        "Find the right information fast for your modules: formulate a good research question, use Perplexity (cited sources), Google Scholar and Consensus, then cross-check the sources.",
        "أن تجد بسرعة المعلومة الصحيحة لوحداتك: صياغة سؤال بحثي جيد، واستعمال Perplexity (بمصادر مذكورة)، وGoogle Scholar وConsensus، ثم تطابق المصادر.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Transformer un sujet vague en question de recherche précise.",
            "Turn a vague topic into a precise research question.",
            "أن تحوّل موضوعاً غامضاً إلى سؤال بحثي دقيق.",
        ),
        L(
            "Utiliser Perplexity pour comprendre une notion avec des sources citées.",
            "Use Perplexity to understand a concept with cited sources.",
            "أن تستعمل Perplexity لفهم مفهوم بمصادر مذكورة.",
        ),
        L(
            "Chercher de la littérature scientifique avec Google Scholar et Consensus.",
            "Search scientific literature with Google Scholar and Consensus.",
            "أن تبحث في الأدبيات العلمية بـ Google Scholar وConsensus.",
        ),
        L(
            "Évaluer et croiser les sources avant de les utiliser dans un travail.",
            "Evaluate and cross-check sources before using them in an assignment.",
            "أن تقيّم المصادر وتطابقها قبل استعمالها في عمل.",
        ),
        L(
            "Citer correctement : nom, année, titre, éditeur ou revue.",
            "Cite correctly: author, year, title, publisher or journal.",
            "أن تستشهد بشكل صحيح: الاسم، السنة، العنوان، الناشر أو المجلة.",
        ),
    ],
    "prerequis": L(
        "Séances 1 et 2 suivies. Savoir ouvrir un navigateur et créer un compte gratuit. Venir avec un thème de module à rechercher.",
        "Sessions 1 and 2 completed. Know how to open a browser and create a free account. Come with a module topic to search.",
        "إتمام الحصتين 1 و2. معرفة فتح متصفّح وإنشاء حساب مجاني. الإتيان بموضوع وحدة للبحث فيه.",
    ),
    "plan": [
        {
            "time": "00–10",
            **L(
                "Accueil et sondage",
                "Welcome and survey",
                "استقبال واستطلاع",
            ),
            "detail": L(
                "« Comment cherchez-vous une information aujourd'hui ? Google ? Un ami ? L'IA ? » Noter les réponses.",
                "\"How do you search for information today? Google? A friend? AI?\" Write the answers down.",
                "« كيف تبحثون عن معلومة اليوم؟ جوجل؟ صديق؟ ذكاء اصطناعي؟ » تسجيل الإجابات.",
            ),
        },
        {
            "time": "10–30",
            **L(
                "Partie 1 : Formuler sa question de recherche",
                "Part 1: Formulating your research question",
                "الجزء الأوّل: صياغة السؤال البحثي",
            ),
            "detail": L(
                "Du sujet vague à la question précise : mots-clés, type de source, date, langues.",
                "From vague topic to precise question: keywords, source type, date, languages.",
                "من الموضوع الغامض إلى السؤال الدقيق: كلمات مفتاحية، نوع المصدر، التاريخ، اللغات.",
            ),
        },
        {
            "time": "30–50",
            **L(
                "Partie 2 : Perplexity en démonstration",
                "Part 2: Perplexity demo",
                "الجزء الثاني: عرض Perplexity",
            ),
            "detail": L(
                "Recherches guidées : sources affichées, bibliographies, bouton « follow-up ». Comparer avec un chatbot classique.",
                "Guided searches: displayed sources, bibliographies, follow-up button. Compare with a regular chatbot.",
                "بحوث موجّهة: المصادر المعروضة، قوائم المراجع، زر المتابعة. مقارنة مع روبوت دردشة عادي.",
            ),
        },
        {
            "time": "50–70",
            **L(
                "Partie 3 : Google Scholar et Consensus",
                "Part 3: Google Scholar and Consensus",
                "الجزء الثالث: Google Scholar وConsensus",
            ),
            "detail": L(
                "Recherche d'articles, filtres par année, citation, DOI. Consensus : synthèse scientifique assistée.",
                "Article search, year filters, citation, DOI. Consensus: AI-assisted scientific synthesis.",
                "البحث عن مقالات، تصفية حسب السنة، الاستشهاد، DOI. Consensus: تركيب علمي بمساعدة الذكاء الاصطناعي.",
            ),
        },
        {
            "time": "70–80",
            **L(
                "Activité : défis « je vérifie »",
                "Activity: \"I check\" challenges",
                "نشاط: تحدّيات « أتحقّق »",
            ),
            "detail": L(
                "En binômes : 3 sources trouvées, 1 citation vérifiée dans Scholar, 1 source fantôme détectée.",
                "In pairs: 3 sources found, 1 citation checked in Scholar, 1 ghost source detected.",
                "في مجموعات ثنائية: 3 مصادر مُلتَقطة، استشهاد واحد تم التحقق منه في Scholar، ومصدر وهمي واحد مكتشف.",
            ),
        },
        {
            "time": "80–90",
            **L(
                "Synthèse et annonce de la séance 4",
                "Wrap-up and preview of session 4",
                "خلاصة وتقديم الحصة الرابعة",
            ),
            "detail": L(
                "« À retenir ». Annonce : résumer et créer des fiches de révision.",
                "Key takeaways. Preview: summarising and making revision sheets.",
                "« ما يجب تذكّره ». تقديم: التلخيص وإنشاء بطاقات المراجعة.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Formuler une bonne question de recherche",
                "Formulating a good research question",
                "صياغة سؤال بحثي جيد",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une recherche commence toujours par une question, pas par des mots tapés au hasard. La question détermine les outils, les mots-clés, la date et le nombre de sources nécessaires.",
                        "A search always starts with a question, not with random typed words. The question determines the tools, the keywords, the date and the number of sources needed.",
                        "يبدأ البحث دائماً بسؤال، لا بكلمات مكتوبة عشوائياً. فالسؤال يحدّد الأدوات والكلمات المفتاحية والتاريخ وعدد المصادر المطلوبة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1. Préciser le sujet :</strong> pas « l'IA » mais « les limites de l'IA générative pour l'enseignant du primaire ».",
                            "<strong>2. Fixer la forme :</strong> définition, comparaison, données chiffrées, exemple d'application ?",
                            "<strong>3. Borner :</strong> période (les 5 dernières années ?), pays, niveau scolaire.",
                            "<strong>4. Choisir le type de source :</strong> cours, article scientifique, rapport officiel, presse.",
                            "<strong>5. Poser la question à l'IA ET à un moteur :</strong> les deux réponses se complètent.",
                        ],
                        [
                            "<strong>1. Narrow the topic:</strong> not \"AI\" but \"the limits of generative AI for the primary teacher\".",
                            "<strong>2. Set the form:</strong> definition, comparison, figures, application example?",
                            "<strong>3. Bound it:</strong> period (last 5 years?), country, school level.",
                            "<strong>4. Choose the source type:</strong> course, scientific paper, official report, press.",
                            "<strong>5. Ask both AI and a search engine:</strong> the two answers complement each other.",
                        ],
                        [
                            "<strong>1. حدّد الموضوع:</strong> لا « الذكاء الاصطناعي » بل « حدود الذكاء الاصطناعي التوليدي لمعلّم الابتدائي ».",
                            "<strong>2. حدّد الشكل:</strong> تعريف، مقارنة، أرقام، مثال تطبيقي؟",
                            "<strong>3. ضع الحدود:</strong> الفترة (آخر خمس سنوات؟)، البلد، المستوى الدراسي.",
                            "<strong>4. اختر نوع المصدر:</strong> درس، مقال علمي، تقرير رسمي، صحافة.",
                            "<strong>5. اسأل الذكاء الاصطناعي ومحرك البحث معاً:</strong> إجابتاهما تكملان بعضهما.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        """<strong>Astuce :</strong> tapez d'abord votre question dans Perplexity pour une synthèse sourcée, puis ouvrez 2 sources signalées.

Une bonne question de recherche = une réponse vérifiable en 3 clics.""",
                        """<strong>Tip:</strong> first type your question into Perplexity for a sourced synthesis, then open 2 flagged sources.

A good research question = an answer verifiable in 3 clicks.""",
                        """<strong>نصيحة:</strong> اكتب سؤالك أولاً في Perplexity لتحصل على تركيب بمصادر، ثم افتح مصدرين مذكورين.

سؤال بحثي جيد = إجابة قابلة للتحقق في ثلاث نقرات.""",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Perplexity : la recherche avec sources citées",
                "Perplexity: search with cited sources",
                "Perplexity: البحث بمصادر مذكورة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Perplexity est un moteur de réponses : il lit le web, rédige une réponse et affiche les sources à côté de chaque affirmation. C'est l'outil idéal pour comprendre vite une notion en vérifiant l'origine de l'information.",
                        "Perplexity is an answer engine: it reads the web, writes a response and shows the sources next to each claim. It is the ideal tool to understand a concept fast while checking where the information comes from.",
                        "Perplexity محرّك إجابات: يقرأ الويب، يكتب جواباً، ويعرض المصادر بجانب كل معلومة. إنها الأداة المثالية لفهم مفهوم بسرعة مع التحقق من أصل المعلومة.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>J'écris ma question</strong> en langue naturelle (« Qu'est-ce que la didactique ? »).",
                            "<strong>Je choisis le mode</strong> (recherche, académique, vidéo) et la région/la langue si besoin.",
                            "<strong>Je lis la réponse</strong> et je survole les numéros qui pointent vers les sources.",
                            "<strong>J'ouvre les sources</strong> : je vérifie que l'information vient bien d'un texte sérieux.",
                            "<strong>Je clique « follow-up »</strong> : « approfondis », « donne un exemple », « quelles études ? ».",
                        ],
                        [
                            "<strong>I write my question</strong> in natural language (\u201cWhat is didactics?\u201d).",
                            "<strong>I choose the mode</strong> (search, academic, video) and the region/language if needed.",
                            "<strong>I read the answer</strong> and hover over the numbers pointing to the sources.",
                            "<strong>I open the sources</strong>: I check the information really comes from a serious text.",
                            "<strong>I click follow-up</strong>: \"go deeper\", \"give an example\", \"which studies?\".",
                        ],
                        [
                            "<strong>أكتب سؤالي</strong> باللغة الطبيعية (« ما هي الديداكتيك؟ »).",
                            "<strong>أختار الوضع</strong> (بحث، أكاديمي، فيديو) والمنطقة/اللغة عند الحاجة.",
                            "<strong>أقرأ الجواب</strong> وأمرّر على الأرقام التي تشير إلى المصادر.",
                            "<strong>أفتح المصادر</strong>: أتحقّق أن المعلومة أتت فعلاً من نصّ جاد.",
                            "<strong>أنقر المتابعة</strong>: « عمّق »، « أعطني مثالاً »، « أي دراسات؟ ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>À retenir :</strong> la réponse de Perplexity n'est qu'un point de départ. La valeur est dans les sources citées : c'est elles que vous lisez, citez et jugez.",
                        "<strong>Remember:</strong> Perplexity's answer is only a starting point. The value lies in the cited sources: they are what you read, cite and judge.",
                        "<strong>تذكّر:</strong> جواب Perplexity مجرّد نقطة انطلاق. القيمة في المصادر المذكورة: هي ما تقرؤه وتستشهد به وتقيّمه.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Google Scholar et Consensus : la littérature scientifique",
                "Google Scholar and Consensus: the scientific literature",
                "Google Scholar وConsensus: الأدبيات العلمية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Pour un exposé ou un travail universitaire sérieux, les sources fiables sont les articles scientifiques. Deux outils vous y mènent : Google Scholar (moteur d'articles) et Consensus (synthèse de résultats d'études).",
                        "For a serious presentation or academic work, the reliable sources are scientific papers. Two tools take you there: Google Scholar (article engine) and Consensus (synthesis of study results).",
                        "من أجل عرض أو عمل جامعي جاد، فإن المصادر الموثوقة هي المقالات العلمية. أداتان توصلانك إليها: Google Scholar (محرك مقالات) وConsensus (تركيب نتائج الدراسات).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Google Scholar :</strong> chercher par mots-clés, filtrer par année, voir « cité par », lire le résumé, trouver le DOI.",
                            "<strong>Consensus :</strong> poser une question factuelle (« le jeu vidéo aide-t-il l'apprentissage ? ») et obtenir un « consensus » sourcé d'études.",
                            "<strong>Le DOI :</strong> numéro unique d'un article — il prouve que l'article existe et permet de le retrouver.",
                            "<strong>La citation :</strong> notez toujours auteur, année, titre, revue. Scholar fournit la citation « Cite ».",
                        ],
                        [
                            "<strong>Google Scholar:</strong> search by keywords, filter by year, see \"cited by\", read the abstract, find the DOI.",
                            "<strong>Consensus:</strong> ask a factual question (\u201cdoes video gaming help learning?\u201d) and get a \"consensus\" sourced from studies.",
                            "<strong>The DOI:</strong> a paper's unique number — it proves the paper exists and lets you find it back.",
                            "<strong>The citation:</strong> always note author, year, title, journal. Scholar gives you the \"Cite\" citation.",
                        ],
                        [
                            "<strong>Google Scholar:</strong> ابحث بالكلمات المفتاحية، صفِّ حسب السنة، راقب « استُشهد به »، اقرأ الملخص، ابحث عن DOI.",
                            "<strong>Consensus:</strong> اطرح سؤالاً واقعياً (« هل تساعد ألعاب الفيديو على التعلّم؟ ») واحصل على « إجماع » مسنود بدراسات.",
                            "<strong>DOI:</strong> رقم فريد للمقال — يثبت وجود المقال ويتيح إيجاده مجدداً.",
                            "<strong>الاستشهاد:</strong> سجّل دائماً الاسم، السنة، العنوان، المجلة. يوفّره Scholar عبر زر « Cite ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>Piège classique :</strong> demander des « références » à un chatbot conversationnel peut produire des articles inventés. Vérifiez TOUJOURS chaque référence dans Google Scholar (titre, auteurs, année) avant de la citer.",
                        "<strong>Classic trap:</strong> asking a conversational chatbot for \"references\" can produce invented papers. ALWAYS check each reference in Google Scholar (title, authors, year) before citing it.",
                        "<strong>فخّ شائع:</strong> طلب « مراجع » من روبوت محادثة قد يولّد مقالات مختلقة. تحقّق دائماً من كل مرجع في Google Scholar (العنوان، المؤلفون، السنة) قبل الاستشهاد به.",
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
                        "Une information répétée par deux sources indépendantes est plus fiable qu'une information isolée. Confrontez l'IA à votre cours, vos polycopiés et au moins une source officielle.",
                        "Information repeated by two independent sources is more reliable than isolated information. Confront AI with your lesson, your handouts and at least one official source.",
                        "المعلومة المتكررة في مصدرين مستقلين أوثق من المعلومة المنعزلة. قارن الذكاء الاصطناعي بدرسك وطبقاتك وبمصدر رسمي واحد على الأقل.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Qui ?</strong> L'auteur est-il identifiable et qualifié (université, organisme) ?",
                            "<strong>Quand ?</strong> La date : une info de 2019 sur un sujet qui évolue vite peut être périmée.",
                            "<strong>Quoi ?</strong> Fait vérifiable, analyse sourcée, ou simple opinion ?",
                            "<strong>Vérifiable ?</strong> La retrouvez-vous ailleurs (Perplexity + Google Scholar + cours) ?",
                            "<strong>Pourquoi ?</strong> Le but du document : informer, vendre, convaincre, tromper ?",
                        ],
                        [
                            "<strong>Who?</strong> Is the author identifiable and qualified (university, organisation)?",
                            "<strong>When?</strong> The date: 2019 information on a fast-moving topic may be outdated.",
                            "<strong>What?</strong> Verifiable fact, sourced analysis, or mere opinion?",
                            "<strong>Checkable?</strong> Can you find it elsewhere (Perplexity + Google Scholar + lesson)?",
                            "<strong>Why?</strong> The document's purpose: inform, sell, persuade, deceive?",
                        ],
                        [
                            "<strong>من؟</strong> هل المؤلف محدّد ومؤهّل (جامعة، مؤسسة)؟",
                            "<strong>متى؟</strong> التاريخ: معلومة 2019 في موضوع متغيّر بسرعة قد تكون قديمة.",
                            "<strong>ماذا؟</strong> حقيقة قابلة للتحقق، تحليل بمصادر، أم رأي فقط؟",
                            "<strong>قابل للتحقق؟</strong> هل تجده في مكان آخر (Perplexity + Google Scholar + درسك)؟",
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
                        "La recherche gagne un temps considérable dès que l'on combine les outils : Perplexity pour comprendre, Scholar/Consensus pour les sources, le cours pour recouper. Le réflexe clé : toujours savoir D'OÙ vient une information.",
                        "Searching saves a huge amount of time as soon as you combine the tools: Perplexity to understand, Scholar/Consensus for sources, the lesson to cross-check. The key reflex: always know WHERE information comes from.",
                        "يوفّر البحث وقتاً كبيراً بمجرد الجمع بين الأدوات: Perplexity للفهم، Scholar/Consensus للمصادر، والدرس للتحقق. السلوك المفتاحي: معرفة دائماً من أين تأتي المعلومة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Coupler IA et moteur :</strong> la question part dans Perplexity, les sources s'ouvrent dans Scholar.",
                            "<strong>✅ Préciser la session :</strong> « académique », « les 5 dernières années », la langue des sources.",
                            "<strong>✅ Enregistrer ses recherches :</strong> copier la question + les 2 meilleures sources dans une note (Notion, Word, carnet).",
                            "<strong>✅ Citer au fil de l'eau :</strong> notez auteur, année, titre dès que vous lisez la source.",
                        ],
                        [
                            "<strong>✅ Pair AI and engine:</strong> the question goes into Perplexity, the sources open in Scholar.",
                            "<strong>✅ Specify the session:</strong> \"academic\", \"last 5 years\", the language of the sources.",
                            "<strong>✅ Save your searches:</strong> copy the question + the 2 best sources into a note (Notion, Word, notebook).",
                            "<strong>✅ Cite as you go:</strong> note author, year, title as soon as you read the source.",
                        ],
                        [
                            "<strong>✅ اجمع الذكاء الاصطناعي والمحرك:</strong> اطرح السؤال في Perplexity وافتح المصادر في Scholar.",
                            "<strong>✅ حدّد الجلسة:</strong> « أكاديمي »، « آخر خمس سنوات »، لغة المصادر.",
                            "<strong>✅ احفظ بحوثك:</strong> انسخ السؤال وأفضل مصدرين في ملاحظة (Notion، Word، كرّاس).",
                            "<strong>✅ استشهد أثناء القراءة:</strong> سجّل الاسم والسنة والعنوان فور قراءة المصدر.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> recopier la réponse de Perplexity sans ouvrir les sources, citer des références jamais vérifiées (<strong>sources fantômes</strong>), et chercher « vite » sans jamais noter l'origine de l'information.",
                        "<strong>❌ Mistakes to avoid:</strong> copying Perplexity's answer without opening the sources, citing never-checked references (<strong>ghost sources</strong>), and searching \"fast\" without ever noting where the information comes from.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> نسخ جواب Perplexity دون فتح المصادر، والاستشهاد بمراجع لم تُتحقّق (<strong>مصادر وهمية</strong>)، والبحث « بسرعة » دون تسجيل أصل المعلومة.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["", "Mauvaise recherche", "Bonne recherche"],
                        ["", "Bad search", "Good search"],
                        ["", "بحث سيئ", "بحث جيد"],
                    ),
                    "rows": L(
                        [
                            ["Question", "« L'IA à l'école, c'est bien ? »", "« Quelles sont les limites documentées de l'IA générative pour des élèves de primaire (études 2021-2026) ? »"],
                            ["Démarche", "Un chatbot, aucune source ouverte.", "Perplexity + 3 sources Scholar + recoupement avec le cours."],
                        ],
                        [
                            ["Question", "\"Is AI in school good?\"", "\"What are the documented limits of generative AI for primary pupils (studies 2021-2026)?\""],
                            ["Process", "One chatbot, no source opened.", "Perplexity + 3 Scholar sources + cross-check with the lesson."],
                        ],
                        [
                            ["السؤال", "« هل الذكاء الاصطناعي في المدرسة جيّد؟ »", "« ما الحدود الموثّقة للذكاء الاصطناعي التوليدي مع تلاميذ الابتدائي (دراسات 2021-2026)؟ »"],
                            ["المنهج", "روبوت واحد، دون فتح أي مصدر.", "Perplexity + 3 مصادر من Scholar + تطابق مع الدرس."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce de gain de temps :</strong> créez un modèle de question réutilisable : « [Notion] — sources officielles et récentes pour un exposé de [niveau] en [langue] ». Vous l'adaptez en 10 secondes à chaque module.",
                        "<strong>Time-saving tip:</strong> build a reusable question template: \"[Topic] — official and recent sources for a [level] presentation in [language]\". Adapt it in 10 seconds for each module.",
                        "<strong>نصيحة لكسب الوقت:</strong> أنشئ قالب سؤال قابلاً لإعادة الاستعمال: « [الموضوع] — مصادر رسمية وحديثة لعرض [المستوى] بـ [اللغة] ». تكيّفه في عشر ثوانٍ لكل وحدة.",
                    ),
                },
            ],
        },
    ],
    "activites": [
        L(
            "Avant/après : transformer 3 mauvaises recherches en questions complètes (contexte, objectif, format, borne de date).",
            "Before/after: turn 3 poor searches into complete questions (context, goal, format, date bound).",
            "قبل/بعد: حوّل ثلاث عمليات بحث سيئة إلى أسئلة كاملة (سياق، هدف، صيغة، حدّ زمني).",
        ),
        L(
            "Comparaison : poser la même question à un chatbot et à Perplexity ; noter les différences de sources et de précision.",
            "Comparison: ask the same question to a chatbot and to Perplexity; note the differences in sources and precision.",
            "مقارنة: اطرح السؤال نفسه على روبوت محادثة وعلى Perplexity؛ سجّل اختلافات المصادر والدقة.",
        ),
        L(
            "Missions Scholar : trouver 3 articles sur un thème du programme (année, revue, auteurs) et rédiger une fiche de lecture de 5 lignes chacun.",
            "Scholar missions: find 3 papers on a curriculum topic (year, journal, authors) and write a 5-line reading sheet for each.",
            "مهام Scholar: ابحث عن ثلاث مقالات حول موضوع من البرنامج (سنة، مجلة، مؤلفون) واكتب بطاقة قراءة من خمسة أسطر لكل منها.",
        ),
        L(
            "Défi « source fantôme » : demander à un chatbot un article sur un thème, vérifier dans Google Scholar s'il existe vraiment, puis corriger la référence.",
            "\"Ghost source\" challenge: ask a chatbot for a paper on a topic, check in Google Scholar whether it really exists, then fix the reference.",
            "تحدّي « المصدر الوهمي »: اطلب من روبوت محادثة مقالاً حول موضوع، تحقّق في Google Scholar من وجوده فعلاً، ثم صحّح المرجع.",
        ),
    ],
    "retenir": [
        L(
            "Une recherche commence par une question précise, pas par des mots au hasard.",
            "A search starts with a precise question, not random words.",
            "يبدأ البحث بسؤال دقيق، لا بكلمات عشوائية.",
        ),
        L(
            "Perplexity répond AVEC les sources ; toujours ouvrir et vérifier ces sources.",
            "Perplexity answers WITH sources; always open and check them.",
            "يجيب Perplexity بالمصادر؛ افتحها وتحقّق منها دائماً.",
        ),
        L(
            "Google Scholar et Consensus mènent à la littérature scientifique ; le DOI prouve qu'un article existe.",
            "Google Scholar and Consensus lead to the scientific literature; the DOI proves a paper exists.",
            "يوصلانك Google Scholar وConsensus إلى الأدبيات العلمية؛ وDOI يثبت وجود مقال.",
        ),
        L(
            "Croiser 2 sources indépendantes avant de considérer une information fiable.",
            "Cross-check 2 independent sources before considering information reliable.",
            "طابق مصدرين مستقلين قبل اعتبار معلومة موثوقة.",
        ),
        L(
            "Jamais de citation sans vérification : sources fantômes = fraude involontaire mais sanctionnée.",
            "Never cite without checking: ghost sources = unintentional but sanctioned fraud.",
            "لا استشهاد دون تحقق: المصادر الوهمية = غشّ غير مقصود لكنه يعاقَب.",
        ),
    ],
    "glossaire": [
        {
            "term": "Moteur de recherche",
            "term_en": "Search engine",
            "def_fr": "Outil qui explore le web à partir de mots-clés (Google, Perplexity web…).",
            "def_en": "A tool that explores the web from keywords (Google, Perplexity web…).",
            "def_ar": "أداة تستكشف الويب انطلاقاً من كلمات مفتاحية (جوجل، Perplexity web…).",
        },
        {
            "term": "Source citée",
            "term_en": "Cited source",
            "def_fr": "Document affiché comme origine d'une information, souvent numéroté dans la réponse.",
            "def_en": "A document shown as the origin of a piece of information, usually numbered in the answer.",
            "def_ar": "وثيقة تُعرض كمصدر لمعلومة، مرقَّمة غالباً في الجواب.",
        },
        {
            "term": "Article scientifique",
            "term_en": "Scientific paper",
            "def_fr": "Texte validé par une revue ou un comité scientifique, décrivant une étude.",
            "def_en": "A text validated by a journal or scientific committee, describing a study.",
            "def_ar": "نص مُحكَّم من مجلة أو لجنة علمية، يصف دراسة.",
        },
        {
            "term": "DOI",
            "term_en": "DOI",
            "def_fr": "Numéro unique et permanent attribué à un article, qui permet de le retrouver en ligne.",
            "def_en": "A unique and permanent number assigned to a paper, allowing you to find it online.",
            "def_ar": "رقم فريد ودائم يمنح للمقال، ويتيح إيجاده على الإنترنت.",
        },
        {
            "term": "Consensus",
            "term_en": "Consensus",
            "def_fr": "Outil d'IA qui génère des synthèses sourcées à partir d'études scientifiques.",
            "def_en": "An AI tool that generates sourced syntheses from scientific studies.",
            "def_ar": "أداة ذكاء اصطناعي تولّد تركيبات مسنودة من دراسات علمية.",
        },
        {
            "term": "Source fantôme",
            "term_en": "Ghost source",
            "def_fr": "Référence inventée, souvent créée par un chatbot, qui ressemble à un vrai article.",
            "def_en": "An invented reference, often created by a chatbot, that looks like a real paper.",
            "def_ar": "مرجع مختلق، يولّده غالباً روبوت محادثة، يشبه مقالاً حقيقياً.",
        },
    ],
    "qcm": [
        {
            "fr": "Quel outil affiche les sources de sa réponse à côté de chaque affirmation ?",
            "en": "Which tool shows the sources of its answer next to each claim?",
            "ar": "أي أداة تعرض مصادر جوابها بجانب كل معلومة؟",
            "options": ["ChatGPT", "Perplexity", "Midjourney", "Ollama"],
            "answer": 1,
        },
        {
            "fr": "Avant de citer un article trouvé dans une réponse IA, il faut…",
            "en": "Before citing a paper found in an AI answer, you must…",
            "ar": "قبل الاستشهاد بمقال وُجد في جواب ذكاء اصطناعي، يجب…",
            "options": ["Le vérifier dans Google Scholar", "L'oublier", "Le copier tel quel", "Cacher la source"],
            "answer": 0,
        },
    ],
    "dialogues_fr": """# Séance 03 — Dialogues pédagogiques (Français)

## Dialogue A — « Cherche, mais vérifie ! » (25 min)

**Personnages :** Amina (étudiante), le Chatbot (joué par un camarade), Walid (camarade qui vérifie).

---

Amina : J'ai besoin d'un article récent sur l'intelligence artificielle à l'école. Je demande au chat.

Chatbot : Voici trois références : Bennani (2023), Ziani (2022), et un rapport UNESCO (2021). Ce sont des sources excellentes !

Amina : Parfait, je les mets dans mon exposé.

Walid : Attends ! Tu les as vérifiées ? Ouvre Google Scholar et cherche « Ziani 2022 »…

Amina : Hmm, je ne trouve rien. Et « Bennani 2023 » non plus !

Walid : Ce sont des sources fantômes : inventées par le chatbot. Il a peut-être mélangé des vrais auteurs avec de fausses dates.

Amina : Heureusement que je n'ai rien recopié ! Et le rapport UNESCO ?

Walid : Lui, il existe. Mais vérifie la version exacte, l'année et l'organisation. Utilise toujours Scholar ou le site officiel.

Chatbot : Mea culpa. Prochaine fois, je vous conseille de me demander : « cite uniquement des articles vérifiables, avec DOI ».

Amina : Donc la règle, c'est : je croise Perplexity pour comprendre, Scholar pour vérifier, et le cours pour recouper. C'est noté !

---

## Dialogue B — « Trois clics » (15 min)

**Personnages :** Sofiane (étudiant), sa sœur Sarah (étudiante en médecine), leur père.

---

Sofiane : Papa, on débat en classe : « Le jeu vidéo aide-t-il à apprendre ? »

Père : Et comment tu vas trancher ça ?

Sofiane : Je pose la question dans Consensus. Il répond avec des études réelles.

Sarah : Moi en médecine on utilise aussi des outils comme ça. Mais toujours avec un regard critique.

Sofiane : Je regarde le consensus, j'ouvre 2 études, je note les années et les revues, et je compare avec mon cours de psychologie.

Sarah : Et si deux études disent le contraire ?

Sofiane : C'est ça la science : je présente les deux résultats honnêtement. L'IA m'aide à trouver, pas à trancher à ma place.

Père : « Trouver, pas trancher »… J'aime bien cette phrase.

---

## Mini-rôle à jouer (3 min par binôme)
Un étudiant demande à un chatbot « 3 références sur un thème ». L'autre joue le robot et invente une référence plausible. Le binôme vérifie dans Google Scholar et corrige. Reformulez la règle : « une source que je n'ai pas ouverte et vérifiée ne se cite pas ».
""",
    "dialogues_en": """# Session 03 — Classroom dialogues (English)

## Dialogue A — "Search, but check!" (25 min)

**Characters:** Amina (student), the Chatbot (played by a classmate), Walid (classmate who checks).

---

Amina: I need a recent paper on AI in schools. I will ask the chat.

Chatbot: Here are three references: Bennani (2023), Ziani (2022), and a UNESCO report (2021). Excellent sources!

Amina: Perfect, I will put them in my presentation.

Walid: Wait! Have you checked them? Open Google Scholar and search "Ziani 2022"…

Amina: Hmm, I find nothing. And "Bennani 2023" neither!

Walid: Those are ghost sources: invented by the chatbot. It may have mixed real authors with false dates.

Amina: Good thing I copied nothing! And the UNESCO report?

Walid: That one exists. But check the exact version, the year and the organisation. Always use Scholar or the official site.

Chatbot: Mea culpa. Next time, I suggest you ask me: "cite only verifiable papers, with DOI".

Amina: So the rule is: I use Perplexity to understand, Scholar to check, and the lesson to cross-check. Noted!

---

## Dialogue B — "Three clicks" (15 min)

**Characters:** Sofiane (student), his sister Sarah (medical student), their father.

---

Sofiane: Dad, we debate in class: "Does video gaming help learning?"

Father: And how will you settle this?

Sofiane: I ask Consensus. It answers with real studies.

Sarah: In medicine we also use tools like that. But always with a critical eye.

Sofiane: I look at the consensus, I open 2 studies, I note the years and journals, and I compare with my psychology course.

Sarah: And if two studies say the opposite?

Sofiane: That is science: I present both results honestly. AI helps me find, not decide for me.

Father: "Find, not decide"… I like that sentence.

---

## Mini role-play (3 min per pair)
One student asks a chatbot for "3 references on a topic". The other plays the robot and invents a plausible reference. The pair checks in Google Scholar and corrects it. Rephrase the rule: "a source I have not opened and checked is not cited".
""",
}