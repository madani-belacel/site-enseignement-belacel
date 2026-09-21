# -*- coding: utf-8 -*-
"""Séance 05 — Préparer un exposé de A à Z avec l'IA (PEP 2A — ENS)."""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 5,
    "slug": "seance-05",
    "icon": "🎤",
    "titles": L(
        "Préparer un exposé de A à Z avec l'IA",
        "Preparing a presentation from A to Z with AI",
        "تحضير عرض من الألف إلى الياء بالذكاء الاصطناعي",
    ),
    "descriptions": L(
        "Cadrer le sujet, bâtir un plan critique, trouver des sources réelles, générer des slides avec Gamma ou Canva et écrire un script à dire — étape par étape.",
        "Frame the topic, build a critical outline, find real sources, generate slides with Gamma or Canva and write a script to be spoken — step by step.",
        "تأطير الموضوع، وبناء خطة نقدية، وإيجاد مصادر حقيقية، وتوليد شرائح بـ Gamma أو Canva، وكتابة نصّ يُقال — خطوة بخطوة.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Découper un exposé en 6 étapes gérables.",
            "Break a presentation into 6 manageable steps.",
            "أن تقسّم عرضاً إلى ست خطوات قابلة للإدارة.",
        ),
        L(
            "Demander à l'IA un squelette de plan, puis le critiquer et le réorganiser.",
            "Ask AI for an outline skeleton, then critique and reorganise it.",
            "أن تطلب من الذكاء الاصطناعي هيكلاً لخطة، ثم تنقّده وتعيد تنظيمه.",
        ),
        L(
            "Trouver des sources réelles (Perplexity, Google Scholar) et vérifiables.",
            "Find real, verifiable sources (Perplexity, Google Scholar).",
            "أن تجد مصادر حقيقية وقابلة للتحقق (Perplexity, Google Scholar).",
        ),
        L(
            "Générer des slides avec un outil de présentation IA et imposer un style cohérent.",
            "Generate slides with an AI presentation tool and impose a consistent style.",
            "أن تولّد شرائح بأداة عروض ذكية وتفرض أسلوباً منسجماً.",
        ),
        L(
            "Rédiger un script oral, le minuter et se l'approprier par la répétition.",
            "Write an oral script, time it and own it through rehearsal.",
            "أن تكتب نصاً شفوياً، وتضبط مدته، وتمتلكه عبر التكرار.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 4 suivies. Venir avec le sujet de son prochain exposé (ou en choisir un en classe).",
        "Sessions 1 to 4 completed. Come with the topic of your next presentation (or choose one in class).",
        "إتمام الحصص من 1 إلى 4. الإتيان بموضوع العرض القادم (أو اختياره في القسم).",
    ),
    "plan": [
        {
            "time": "00–10",
            **L(
                "Accueil et méthode",
                "Welcome and method",
                "استقبال ومنهج",
            ),
            "detail": L(
                "Question : « Comment préparez-vous un exposé aujourd'hui ? » Présenter la méthode en 6 étapes.",
                "Question: \"How do you prepare a presentation today?\" Present the 6-step method.",
                "سؤال: « كيف تحضّرون عرضاً اليوم؟ » وعرض منهجية الخطوات الست.",
            ),
        },
        {
            "time": "10–30",
            **L(
                "Partie 1 : Cadrage et plan",
                "Part 1: Framing and outline",
                "الجزء الأوّل: التأطير والخطة",
            ),
            "detail": L(
                "Message-clé, public, durée. Demander un squelette à l'IA puis le critiquer.",
                "Key message, audience, duration. Ask AI for a skeleton, then critique it.",
                "الرسالة الرئيسية، الجمهور، المدة. طلب هيكل من الذكاء الاصطناعي ثم نقده.",
            ),
        },
        {
            "time": "30–50",
            **L(
                "Partie 2 : Sources et contenus",
                "Part 2: Sources and content",
                "الجزء الثاني: المصادر والمحتوى",
            ),
            "detail": L(
                "Feuille de notes : 3 sources vérifiées par partie. Perplexity + Scholar.",
                "Notes sheet: 3 verified sources per part. Perplexity + Scholar.",
                "ورقة ملاحظات: ثلاثة مصادر موثقة لكل جزء. Perplexity + Scholar.",
            ),
        },
        {
            "time": "50–70",
            **L(
                "Partie 3 : Slides avec Gamma / Canva",
                "Part 3: Slides with Gamma / Canva",
                "الجزء الثالث: الشرائح بـ Gamma / Canva",
            ),
            "detail": L(
                "Générer un projet, choisir un style, corriger le texte (peu de mots par slide).",
                "Generate a draft, pick a style, fix the text (few words per slide).",
                "توليد مسودة، اختيار أسلوب، تصحيح النص (كلمات قليلة لكل شريحة).",
            ),
        },
        {
            "time": "70–80",
            **L(
                "Partie 4 : Script et répétition",
                "Part 4: Script and rehearsal",
                "الجزء الرابع: النص والتكرار",
            ),
            "detail": L(
                "Transforme les slides en script oral ; chrono ; brouillon de la première phrase.",
                "Turn the slides into an oral script; time it; draft the first sentence.",
                "تحويل الشرائح إلى نص شفهي؛ ضبط المؤقّت؛ مسودّة الجملة الأولى.",
            ),
        },
        {
            "time": "80–90",
            **L(
                "Synthèse et annonce de la séance 6",
                "Wrap-up and preview of session 6",
                "خلاصة وتقديم الحصة السادسة",
            ),
            "detail": L(
                "« À retenir ». Annonce : programmer avec l'IA et créer son premier assistant Python.",
                "Key takeaways. Preview: programming with AI and building your first Python assistant.",
                "« ما يجب تذكّره ». تقديم: البرمجة مع الذكاء الاصطناعي وإنشاء أول مساعد بايثون.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "La méthode en 6 étapes — le squelette de l'exposé",
                "The 6-step method — the presentation skeleton",
                "منهجية الخطوات الست — هيكل العرض",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Un exposé ne se fait pas en une nuit, et ne se génère pas en un prompt. On le construit en étapes ; l'IA accélère les étapes 2, 3 et 4, mais jamais les étapes 1 et 6, qui sont les vôtres.",
                        "A presentation is not made in one night, and not generated in one prompt. You build it in steps; AI speeds up steps 2, 3 and 4, but never steps 1 and 6, which are yours.",
                        "العرض لا يُنجز في ليلة، ولا يُولَّد في تعليمة واحدة. يُبنى خطوة بخطوة؛ يسرّع الذكاء الاصطناعي الخطوات 2 و3 و4، ولا يسرّع أبداً الخطوتين 1 و6، وهما لك.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>1. Cadrer :</strong> un message-clé en une phrase, un public, une durée, un plan de bord.",
                            "<strong>2. Plan :</strong> squelette généré + critique et réorganisation par vous.",
                            "<strong>3. Sources :</strong> 1 source vérifiée par idée (Perplexity, Scholar, cours).",
                            "<strong>4. Slides :</strong> Gamma ou Canva, puis nettoyage du texte.",
                            "<strong>5. Script :</strong> ce que VOUS direz, pas ce que vous lirez.",
                            "<strong>6. Répéter :</strong> à voix haute, chronomètre, devant un miroir ou un ami.",
                        ],
                        [
                            "<strong>1. Frame:</strong> one key message in one sentence, an audience, a duration, a roadmap.",
                            "<strong>2. Outline:</strong> generated skeleton + your critique and reorganisation.",
                            "<strong>3. Sources:</strong> 1 verified source per idea (Perplexity, Scholar, lesson).",
                            "<strong>4. Slides:</strong> Gamma or Canva, then text cleanup.",
                            "<strong>5. Script:</strong> what YOU will say, not what you will read.",
                            "<strong>6. Rehearse:</strong> aloud, timed, in front of a mirror or a friend.",
                        ],
                        [
                            "<strong>1. تأطير:</strong> رسالة رئيسية في جملة، جمهور، مدة، خارطة طريق.",
                            "<strong>2. خطة:</strong> هيكل مولّد + نقده وإعادة ترتيبه منك.",
                            "<strong>3. مصادر:</strong> مصدر موثق واحد لكل فكرة (Perplexity, Scholar, درس).",
                            "<strong>4. شرائح:</strong> Gamma أو Canva، ثم تنظيف النص.",
                            "<strong>5. نص:</strong> ما ستقوله أنت، لا ما ستقرؤه.",
                            "<strong>6. تكرار:</strong> جهراً، مع مؤقّت، أمام مرآة أو صديق.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> demandez un squelette « en 3 parties, 2 sections chacune », puis supprimez, fusionnez et déplacez. Un plan que l'on n'a pas réorganisé soi-même ne nous appartient pas.",
                        "<strong>Tip:</strong> ask for a skeleton \"in 3 parts, 2 sections each\", then delete, merge and move. An outline you have not reorganised does not belong to you.",
                        "<strong>نصيحة:</strong> اطلب هيكلاً « من ثلاثة أجزاء، قسمان لكل جزء »، ثم احذف وادمج ونقل. الخطة التي لا تعيد تنظيمها بنفسك لا تخصّك.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Le plan : générer, critiquer, réorganiser",
                "The outline: generate, critique, reorganise",
                "الخطة: توليد، نقد، إعادة تنظيم",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "L'IA fournit une matière première : une liste d'idées classées. C'est vous qui décidez de l'ordre logique, de ce qui manque et de ce qui est superflu — selon le message que vous voulez porter.",
                        "AI provides raw material: a list of sorted ideas. You decide the logical order, what is missing and what is superfluous — according to the message you want to carry.",
                        "يوفّر الذكاء الاصطناعي مادة أولية: قائمة أفكار مصنّفة. وأنت من يحدّد الترتيب المنطقي، وما ينقص، وما زائد — تبعاً للرسالة التي تريد حملها.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt squelette :</strong> « Sujet : [X]. Public : [enseignants/étudiants]. Durée : 10 min. Propose un plan en 3 parties et 2 sections, avec un objectif par partie. »",
                            "<strong>Skeleton prompt:</strong> \"Topic: [X]. Audience: [teachers/students]. Duration: 10 min. Suggest an outline in 3 parts and 2 sections, with one goal per part.\"",
                            "<strong>تعليمة الهيكل:</strong> « الموضوع: [X]. الجمهور: [أساتذة/طلبة]. المدة: 10 دقائق. اقترح خطة بثلاثة أجزاء وقسمين، بهدف لكل جزء »",
                            "<strong>Critique :</strong> « où est la partie la plus faible ? Que manque-t-il pour un étudiant PEP 2A ? »",
                            "<strong>Critique:</strong> \"which part is the weakest? What is missing for a PEP 2A student?\"",
                            "<strong>النقد:</strong> « ما أضعف جزء؟ ما الذي ينقص طالب PEP 2A؟ »",
                            "<strong>Budgété :</strong> « attribue un temps à chaque partie pour 10 minutes ».",
                            "<strong>Budgeted:</strong> \"allocate a time to each part for 10 minutes\".",
                            "<strong>بالأزمنة:</strong> « وزّع مدة لكل جزء في عشر دقائق »",
                        ],
                        [
                            "<strong>Plan :</strong> « Sujet : [X]. Public : [professeurs/étudiants]. Durée : 10 min. Proposes un plan en 3 parties et 2 sections, avec un objectif par partie. »",
                            "<strong>4e partie :</strong> « où est la partie la plus faible ? Qu'est-ce qui manque pour un étudiant PEP 2A ? »",
                            "<strong>Budget :</strong> « attribue un temps à chaque partie pour 10 minutes ».",
                        ]
                        if False
                        else [
                            "<strong>Plan :</strong> \"Topic: [X]. Audience: [teachers/students]. Duration: 10 min. Suggest an outline in 3 parts and 2 sections, with one goal per part.\"",
                            "<strong>Critique:</strong> \"which part is the weakest? What is missing for a PEP 2A student?\"",
                            "<strong>Timing:</strong> \"allocate a time to each part for 10 minutes\".",
                        ],
                        [
                            "<strong>الهيكل:</strong> « الموضوع: [X]. الجمهور: [أساتذة/طلبة]. المدة: 10 دقائق. اقترح خطة بثلاثة أجزاء وقسمين، بهدف لكل جزء »",
                            "<strong>النقد:</strong> « ما أضعف جزء؟ وما الذي ينقص طالب PEP 2A؟ »",
                            "<strong>بالأزمنة:</strong> « وزّع مدة لكل جزء لتقديم في عشر دقائق »",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Sources et contenus : la feuille de notes",
                "Sources and content: the notes sheet",
                "المصادر والمحتوى: ورقة الملاحظات",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Chaque partie de l'exposé s'appuie sur au moins une source réelle. Préparez une « feuille de notes » : une page par partie avec les idées, une question, les sources et un exemple.",
                        "Each part of the presentation relies on at least one real source. Prepare a \"notes sheet\": one page per part with ideas, a question, the sources and an example.",
                        "يعتمد كل جزء من العرض على مصدر حقيقي واحد على الأقل. حضّر « ورقة ملاحظات »: صفحة لكل جزء بتفاصيل الأفكار، سؤال، المصادر، ومثال.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Perplexity :</strong> une synthèse sourcée par question (« quelles études 2021-2026 sur X ? »).",
                            "<strong>Google Scholar :</strong> retrouver les articles cités et leurs dates.",
                            "<strong>Consensus :</strong> question factuelle sur l'efficacité d'une méthode.",
                            "<strong>Cours et polycopiés :</strong> la base que l'IA ne connaît pas — recouperz.",
                        ],
                        [
                            "<strong>Perplexity:</strong> a sourced synthesis per question (\"which 2021-2026 studies on X?\").",
                            "<strong>Google Scholar:</strong> find back the cited papers and their dates.",
                            "<strong>Consensus:</strong> factual question about the effectiveness of a method.",
                            "<strong>Lessons and handouts:</strong> the base AI does not know — cross-check.",
                        ],
                        [
                            "<strong>Perplexity:</strong> تركيب بمصادر لكل سؤال (« ما الدراسات 2021-2026 حول X؟ »).",
                            "<strong>Google Scholar:</strong> إيجاد المقالات المذكورة وتواريخها.",
                            "<strong>Consensus:</strong> سؤال واقعي عن فعالية منهجية.",
                            "<strong>الدرس والطبقات:</strong> الأساس الذي لا يعرفه الذكاء الاصطناعي — قارن به.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Règle des 3 sources :</strong> avant de finaliser l'exposé, vérifiez qu'au moins 3 sources citées existent réellement (titre, auteurs, année retrouvés dans Scholar ou le site officiel).",
                        "<strong>Rule of 3 sources:</strong> before finalising the presentation, check that at least 3 cited sources really exist (title, authors, year found in Scholar or the official site).",
                        "<strong>قاعدة المصادر الثلاثة:</strong> قبل إنهاء العرض، تأكّد أن ثلاثة مصادر مذكورة على الأقل موجودة فعلاً (عنوان، مؤلفون، سنة في Scholar أو الموقع الرسمي).",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Slides et script : moins de mots, plus de sens",
                "Slides and script: fewer words, more meaning",
                "الشرائح والنص: كلمات أقل ومعنى أكثر",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Un diaporama n'est pas le support de lecture du public : c'est l'appui visuel de VOTRE parole. Une slide = une idée = peu de mots. Le détail est dans votre script oral.",
                        "A slideshow is not the audience's reading support: it is the visual support of YOUR speech. One slide = one idea = few words. The detail lives in your oral script.",
                        "العرض التقديمي ليس دعامة قراءة للجمهور: إنه السند البصري لكلامك. شريحة = فكرة = كلمات قليلة. والتفاصيل في نصك الشفهي.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Gamma :</strong> saisir le plan + les notes → générer un projet → choisir un thème sobre → corriger.",
                            "<strong>Canva :</strong> modèles et « Magic Design » pour les visuels ; attention à la lisibilité.",
                            "<strong>Nettoyage :</strong> supprimer la moitié des mots générés ; <strong>1 idée par slide</strong>, une image, un graphique si utile.",
                            "<strong>Script oral :</strong> « transforme le contenu de cette slide en 45 secondes de parole naturelle » puis répétez.",
                        ],
                        [
                            "<strong>Gamma:</strong> enter the outline + notes → generate a draft → pick a sober theme → fix.",
                            "<strong>Canva:</strong> templates and \"Magic Design\" for visuals; mind readability.",
                            "<strong>Cleanup:</strong> delete half the generated words; <strong>1 idea per slide</strong>, one image, a chart if useful.",
                            "<strong>Oral script:</strong> \"turn this slide's content into 45 seconds of natural speech\" then rehearse.",
                        ],
                        [
                            "<strong>Gamma:</strong> أدخل الخطة + الملاحظات → ولّد مسودة → اختر موضوعاً هادئاً → صحّح.",
                            "<strong>Canva:</strong> قوالب و « Magic Design » للصور؛ انتبه للوضوح.",
                            "<strong>تنظيف:</strong> احذف نصف الكلمات المولّدة؛ <strong>فكرة واحدة لكل شريحة</strong>، صورة واحدة، مخطط عند الحاجة.",
                            "<strong>نص شفهي:</strong> « حوّل محتوى هذه الشريحة إلى 45 ثانية كلاماً طبيعياً » ثم كرّر.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Test du « téléprompteur » :</strong> si votre public doit lire la slide pour comprendre, la slide est ratée. Votre slide doit marquer l'idée ; votre parole fait le reste.",
                        "<strong>The \"teleprompter\" test:</strong> if your audience must read the slide to understand, the slide has failed. Your slide should highlight the idea; your speech does the rest.",
                        "<strong>اختبار « الملقن »:</strong> إذا كان على جمهورك قراءة الشريحة لفهمها، فقد فشلت الشريحة. شريحتك تُبرز الفكرة، وكلامك يتولى الباقي.",
                    ),
                },
            ],
        },
        {
            "id": "s5",
            "titre": L(
                "La répétition : le tuteur qui vous écoute",
                "Rehearsal: the tutor who listens to you",
                "التكرار: المدرّس الذي يستمع إليك",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Vous pouvez aussi demander à l'IA de jouer le public : répondre aux questions, pointer les passages confus, reformuler votre introduction.",
                        "You can also ask AI to play the audience: answer questions, point out confusing passages, rephrase your introduction.",
                        "يمكنك أيضاً أن تطلب من الذكاء الاصطناعي أن يلعب دور الجمهور: يجيب على الأسئلة، ويشير إلى المقاطع المربكة، ويعيد صياغة مقدمتك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Brouillon :</strong> « Voici mon script [coller]. Joue le professeur qui pose des questions. »",
                            "<strong>Feedback :</strong> « quelles phrases sont trop longues ? où ai-je oublié un exemple ? »",
                            "<strong>Répétition chronométrée :</strong> lisez à voix haute, notez les 10 premières secondes — elles donnent le ton.",
                            "<strong>Mémorisation :</strong> cachez le script, retrouvez chaque slide avec une phrase clé.",
                        ],
                        [
                            "<strong>Draft:</strong> \"Here is my script [paste]. Play the teacher asking questions.\"",
                            "<strong>Feedback:</strong> \"which sentences are too long? where did I forget an example?\"",
                            "<strong>Timed rehearsal:</strong> read aloud, master the first 10 seconds — they set the tone.",
                            "<strong>Memorisation:</strong> hide the script, recall each slide with one key sentence.",
                        ],
                        [
                            "<strong>مسودة:</strong> « هذا نصي [الصق]. مثّل دور الأستاذ الذي يطرح الأسئلة ».",
                            "<strong>تغذية راجعة:</strong> « ما الجمل الطويلة؟ أين نسيت مثالاً؟ »",
                            "<strong>تكرار بمؤقّت:</strong> اقرأ جهراً، وأتقن أول عشر ثوانٍ — فهي تحدد النبرة.",
                            "<strong>حفظ:</strong> أخفِ النص، واسترجع كل شريحة بجملة مفتاحية.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce anti-stress :</strong> préparez les 2 questions d'ouverture (« Comment X a changé ? ») et la conclusion en une phrase. Le reste, chacun l'oublie : ce qui compte, c'est le fil rouge et la conviction.",
                        "<strong>Anti-stress tip:</strong> prepare the 2 opening hooks (\u00abHow has X changed?\u00bb) and a one-sentence conclusion. The rest is forgotten anyway: what matters is the red thread and your conviction.",
                        "<strong>نصيحة ضد التوتر:</strong> حضّر سؤالَي التمهيد (« كيف تغيّر X؟ ») وخاتمة من جملة واحدة. الباقي يُنسى: المهم هو الخيط الرابط والاقتناع.",
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
                        "L'IA est excellente pour produire de la matière (squelettes, textes, slides) ; elle est mauvaise pour décider de votre message. Profitez-en en inversant la charge : c'est vous qui critiquez, l'IA qui régénère.",
                        "AI is excellent at producing material (skeletons, texts, slides); it is bad at deciding your message. Profit from it by reversing the load: you critique, AI regenerates.",
                        "يجيد الذكاء الاصطناعي إنتاج المادة (هياكل، نصوص، شرائح)؛ وهو سيئ في تقرير رسالتك. استفد منه بعكس العبء: أنت تنقّد وتبدّل، وهو يعيد التوليد.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Cachez le public :</strong> « pour des professeurs de CP non informaticiens » évite le jargon.",
                            "<strong>✅ Nourrissez le modèle :</strong> collez vos notes et vos sources ; donnez une slide d'exemple.",
                            "<strong>✅ Traitez le plan comme un post-it :</strong> on le déplace, on l'abandonne, on en crée d'autres.",
                            "<strong>✅ Réutilisez vos présentations :</strong> « résume ces 10 slides en une fiche de révision ».",
                        ],
                        [
                            "<strong>✅ Define the audience:</strong> \"for non-IT Year-1 teachers\" avoids jargon.",
                            "<strong>✅ Feed the model:</strong> paste your notes and sources; give a sample slide.",
                            "<strong>✅ Treat the outline like a post-it:</strong> move it, drop it, create new ones.",
                            "<strong>✅ Reuse your presentations:</strong> \"summarise these 10 slides into a revision sheet\".",
                        ],
                        [
                            "<strong>✅ حدّد الجمهور:</strong> « لأساتذة التحضيري غير متخصصين في الإعلام الآلي » يتجنّب المصطلحات.",
                            "<strong>✅ غذِّ النموذج:</strong> الصق ملاحظاتك ومصادرك؛ وقدّم مثال شريحة.",
                            "<strong>✅ عامل الخطة كملصقة:</strong> ينقل، يُحذف، ويُنشأ غيرها.",
                            "<strong>✅ أعد استعمال عروضك:</strong> « لخّص هذه الشرائح العشر في بطاقة مراجعة »",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> présenter des slides générés sans les avoir relus (erreurs, dates fausses), lire son script au lieu de le dire, et — plus grave — <strong>garder un graphique ou une statistique jamais vérifiée</strong> devant la classe.",
                        "<strong>❌ Mistakes to avoid:</strong> presenting unproofread generated slides (errors, wrong dates), reading your script instead of delivering it, and — worse — <strong>keeping an unverified chart or statistic</strong> in front of the class.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> عرض شرائح مولّدة دون مراجعتها (أخطاء، تواريخ خاطئة)، وقراءة النص بدل إلقائه، وخصوصاً <strong>الإبقاء على رسم أو إحصائية غير موثقة</strong> أمام القسم.",
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
                            ["Demande", "« Fais-moi un exposé sur la pédagogie. »", "« Voici mon sujet et 3 sources [coller]. Propose un squelette en 3 parties, 2 sections, avec un temps moteur par partie. »"],
                            ["Résultat", "Un diaporama tout fait, impersonnel, sans sources.", "Un plan que vous critiquez, alimenté par des sources vérifiables."],
                        ],
                        [
                            ["Prompt", "\"Make me a presentation on pedagogy.\"", "\"Here is my topic and 3 sources [paste]. Suggest a 3-part, 2-section outline with a timing per part.\""],
                            ["Result", "A ready-made, impersonal, sourceless slideshow.", "An outline you critique, fed by verifiable sources."],
                        ],
                        [
                            ["الطلب", "« اعمل لي عرضاً عن البيداغوجيا »", "« هذا موضوعي وثلاثة مصادر [الصق]. اقترح هيكلاً من ثلاثة أجزاء وقسمين مع مدة لكل جزء »"],
                            ["النتيجة", "شرائح جاهزة، شخصية، بلا مصادر.", "خطة تنقّدها أنت وتغذّيها مصادر قابلة للتحقق."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce gain de temps :</strong> la même chaine de 4 invites (cadrer → plan → slides → script) s'adapte à tous vos modules. Enregistrez-la dans un modèle : vous économiserez des heures chaque semestre.",
                        "<strong>Time-saving tip:</strong> the same chain of 4 prompts (frame → outline → slides → script) adapts to every module. Save it as a template: you will save hours every semester.",
                        "<strong>نصيحة لكسب الوقت:</strong> سلسلة الصياغات الأربع نفسها (تأطير → خطة → شرائح → نص) تتكيّف مع كل وحداتك. احفظها قالباً: ستوفّر ساعات كل فصل.",
                    ),
                },
            ],
        },
    ],
    "activites": [
        L(
            "Prompt squelette : chaque étudiant génère un plan pour son sujet, puis l'échange avec un voisin qui le critique (ajouter/supprimer/déplacer).",
            "Skeleton prompt: each student generates an outline for their topic, then swaps it with a neighbour who critiques it (add/remove/move).",
            "تعليمة الهيكل: يولّد كل طالب خطة لموضوعه، ثم يتبادلها مع جاره الذي ينقّدها (إضافة/حذف/نقل).",
        ),
        L(
            "Atelier sources : pour 2 parties de son exposé, trouver 3 sources vérifiables et rédiger la citation exacte.",
            "Sources workshop: for 2 parts of the presentation, find 3 verifiable sources and write the exact citation.",
            "ورشة المصادر: لجزءين من العرض، إيجاد ثلاثة مصادر قابلة للتحقق وكتابة الاستشهاد الدقيق.",
        ),
        L(
            "Défi Gamma : produire 5 slides propres à partir de son plan, puis les réduire à la moitié des mots (nettoyage).",
            "Gamma challenge: produce 5 clean slides from the outline, then cut them down to half the words (cleanup).",
            "تحدّي Gamma: إنتاج خمس شرائح نظيفة من خطتك، ثم تقليص كلماتها إلى النصف (تنظيف).",
        ),
        L(
            "Flash de présentation : 90 secondes chacun, script chronométré, l'auditoire note une qualité et une amélioration.",
            "Presentation flash: 90 seconds each, timed script, the audience notes one strength and one improvement.",
            "إلقاء خاطف: 90 ثانية لكل طالب، نص مضبوط المدة، والجمهور يسجّل جودة واحدة وتحسيناً واحداً.",
        ),
    ],
    "retenir": [
        L(
            "6 étapes : cadrer, plan, sources, slides, script, répéter.",
            "6 steps: frame, outline, sources, slides, script, rehearse.",
            "6 خطوات: تأطير، خطة، مصادر، شرائح، نص، تكرار.",
        ),
        L(
            "Le plan généré par l'IA doit être réorganisé par vous : il devient alors le vôtre.",
            "The AI-generated outline must be reorganised by you: it then becomes yours.",
            "الخطة التي يولّدها الذكاء الاصطناعي يجب أن تعيد تنظيمها: عندها تصبح لك.",
        ),
        L(
            "Une slide = une idée = très peu de mots ; le détail est dans le script oral.",
            "One slide = one idea = very few words; the detail lives in the oral script.",
            "شريحة = فكرة = كلمات قليلة جداً؛ والتفاصيل في النص الشفهي.",
        ),
        L(
            "Répéter à voix haute et chronométré : la seule manière de posséder son exposé.",
            "Rehearse aloud and timed: the only way to own your presentation.",
            "الكرّ بمؤقّت وجهراً: الطريقة الوحيدة لامتلاك عرضك.",
        ),
        L(
            "Aucune statistique ou graphique généré sans source vérifiée ne monte en cours.",
            "No generated statistic or chart without a verified source goes into the class.",
            "لا يُعرض رسم أو إحصائية مولّدة دون مصدر موثق أمام القسم.",
        ),
    ],
    "glossaire": [
        {
            "term": "Message-clé",
            "term_en": "Key message",
            "def_fr": "L'idée centrale que le public doit retenir, formulée en une phrase.",
            "def_en": "The central idea the audience must remember, phrased in one sentence.",
            "def_ar": "الفكرة المركزية التي يجب أن يتذكرها الجمهور، في جملة واحدة.",
        },
        {
            "term": "Squelette de plan",
            "term_en": "Outline skeleton",
            "def_fr": "Structure brute (parties, sections) proposée par l'IA, à critiquer et réorganiser.",
            "def_en": "A raw structure (parts, sections) proposed by AI, to critique and reorganise.",
            "def_ar": "هيكل خام (أجزاء، أقسام) يقترحه الذكاء الاصطناعي، يُنقّد ويُعاد ترتيبه.",
        },
        {
            "term": "Script oral",
            "term_en": "Oral script",
            "def_fr": "Texte des phrases que l'on prononce, court, naturel et chronométré.",
            "def_en": "The text of the sentences you speak: short, natural and timed.",
            "def_ar": "نص الجمل التي تنطقها: قصير، طبيعي، ومضبوط المدة.",
        },
        {
            "term": "Diaporama",
            "term_en": "Slideshow",
            "def_fr": "Série de slides qui appuie visuellement l'exposé, sans contenir tout le texte.",
            "def_en": "A series of slides that visually support the talk, without containing all the text.",
            "def_ar": "سلسلة شرائح تدعم العرض بصرياً، دون أن تحوي النص كله.",
        },
        {
            "term": "Feuille de notes",
            "term_en": "Notes sheet",
            "def_fr": "Page de travail par partie : idées, question, sources vérifiées, exemple.",
            "def_en": "A working page per part: ideas, question, verified sources, example.",
            "def_ar": "صفحة عمل لكل جزء: أفكار، سؤال، مصادر موثقة، مثال.",
        },
    ],
    "dialogues_fr": """# Séance 05 — Dialogues pédagogiques (Français)

## Dialogue A — « Un exposé en un clic ? » (25 min)

**Personnages :** Yacine (étudiant pressé), l'IA (jouée par un camarade), Lina (camarade exigeante).

---

Yacine : Lina, regarde : j'ai demandé à l'IA de me faire tout mon exposé. Il est prêt en 2 minutes !

Lina : Il est prêt, ou il est fini ? Ils sont différents.

Yacine : Comment ça ?

Lina : Un exposé, c'est porter un message. L'IA a écrit un message, mais pas TON message. Qu'est-ce que TU veux dire à ta classe ?

Yacine : Eh bien… je n'y ai pas pensé.

Lina : Alors reprenons la méthode : 1) tu cadres — 10 minutes, pour des professeurs de primaire ; 2) tu demandes un squelette ; 3) tu critiques ; 4) tu cherches 3 vraies sources ; 5) tu écris ce que TU diras ; 6) tu répètes.

IA : Je peux accélérer 2, 3 et 4. Mais 1 et 6 sont à toi, Yacine.

Yacine : Et si je présente tel quel, sans vérifier ?

IA : C'est un risque : dates fausses, statistiques inventées… En tant qu'étudiant, tu en es responsable.

Yacine fixe l'IA : Promets-moi de me donner des sources vérifiables.

---

## Dialogue B — « La répétition qui sauve » (15 min)

**Personnages :** Nesrine (étudiante), le miroir (joué par un camarade), son frère Anis.

---

Nesrine (devant le miroir) : « Bonjour. Aujourd'hui, je vous parle de… » Non, c'est trop lent.

Anis : Recommence. La première phrase donne le ton.

Nesrine : « Qu'est-ce qu'un bon répétiteur ? Une IA bien utilisée. » Pas mal !

Anis : Chronomètre maintenant : 90 secondes par partie ?

Nesrine : Je lis mon script devant le miroir… 2 minutes pour la partie 1. Trop long.

Anis : Demande à l'IA de condenser la partie en 5 phrases. Puis répète sans l'écran.

Nesrine : Sans l'écran ?!

Anis : La slide rappelle l'idée ; ta parole développe. Si tu dépends du script, c'est que tu ne le possèdes pas encore.

Nesrine : Donc : miroir, chrono, sans script, encore et encore. Compris, Anis !

---

## Mini-rôle à jouer (3 min par binôme)
Un étudiant demande à l'IA « 3 statistiques impressionnantes » pour son exposé. L'autre, qui a vérifié, découvre qu'une statistique est fausse. Trouvez ensemble la formule pour annoncer le problème devant la classe : « L'IA m'a donné ce chiffre, mais votre recherche montre que… ».
""",
    "dialogues_en": """# Session 05 — Classroom dialogues (English)

## Dialogue A — "A presentation in one click?" (25 min)

**Characters:** Yacine (a rushed student), the AI (played by a classmate), Lina (a demanding classmate).

---

Yacine: Lina, look: I asked AI to do my whole presentation. Ready in 2 minutes!

Lina: Ready, or finished? They are different.

Yacine: What do you mean?

Lina: A presentation is carrying a message. AI wrote a message, but not YOUR message. What do YOU want to say to your class?

Yacine: Well… I had not thought about that.

Lina: Then let us go back to the method: 1) you frame — 10 minutes, for primary teachers; 2) you ask for a skeleton; 3) you critique; 4) you find 3 real sources; 5) you write what YOU will say; 6) you rehearse.

AI: I can speed up 2, 3 and 4. But 1 and 6 are yours, Yacine.

Yacine: And if I present it as is, without checking?

AI: That is a risk: wrong dates, invented statistics… As a student, you are responsible for it.

Yacine (to AI): Promise me to give verifiable sources.

---

## Dialogue B — "The rehearsal that saves" (15 min)

**Characters:** Nesrine (student), the mirror (played by a classmate), her brother Anis.

---

Nesrine (in front of the mirror): "Hello. Today I will talk to you about…" No, that is too slow.

Anis: Start again. The first sentence sets the tone.

Nesrine: "What is a good coach? A well-used AI." Not bad!

Anis: Now time it: 90 seconds per part?

Nesrine: I read my script in front of the mirror… 2 minutes for part 1. Too long.

Anis: Ask AI to condense the part into 5 sentences. Then rehearse without the screen.

Nesrine: Without the screen?!

Anis: The slide recalls the idea; your speech develops it. If you depend on the script, you do not own it yet.

Nesrine: So: mirror, timer, no script, again and again. Got it, Anis!

---

## Mini role-play (3 min per pair)
One student asks AI for "3 impressive statistics" for their presentation. The other, who checked, discovers one statistic is false. Together, find the formula to announce the problem in class: "AI gave me this figure, but your research shows that…".
""",
}