# -*- coding: utf-8 -*-
"""Séance 04 — Résumer, synthétiser et créer des fiches de révision (PEP 2A — ENS)."""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 4,
    "slug": "seance-04",
    "icon": "📝",
    "titles": L(
        "Résumer, synthétiser et créer des fiches de révision",
        "Summarising, synthesising and making revision sheets",
        "التلخيص والتركيب وإنشاء بطاقات المراجعة",
    ),
    "descriptions": L(
        "Transformer n'importe quel cours en fiches de révision efficaces avec l'aide de l'IA — sans déléguer la compréhension : méthodes Cornell, protocole AIDE et prompts de synthèse.",
        "Turn any lesson into effective revision sheets with AI help — without delegating understanding: Cornell method, the AIDE protocol and synthesis prompts.",
        "أن تحوّل أي درس إلى بطاقات مراجعة فعّالة بمساعدة الذكاء الاصطناعي — دون تفويض الفهم: منهج كورنيل، بروتوكول AIDE، وصياغات تركيب.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Distinguer résumer (réduire un texte) et synthétiser (croiser plusieurs textes).",
            "Distinguish summarising (reducing a text) from synthesising (mixing several texts).",
            "أن تميّز بين التلخيص (تقليص نص) والتركيب (مزج عدة نصوص).",
        ),
        L(
            "Connaître la structure d'une fiche de révision efficace (idées-clés, schéma, questions, exemples).",
            "Know the structure of an effective revision sheet (key ideas, diagram, questions, examples).",
            "أن تعرف بنية بطاقة مراجعة فعّالة (أفكار رئيسية، مخطط، أسئلة، أمثلة).",
        ),
        L(
            "Utiliser des prompts de synthèse : niveau, format, fidélité au cours, ton.",
            "Use synthesis prompts: level, format, faithfulness to the lesson, tone.",
            "أن تستعمل صياغات تركيب: المستوى، الصيغة، الوفاء بالدرس، النبرة.",
        ),
        L(
            "Appliquer le protocole AIDE : Analyser, Interroger, Double-vérifier, Exposer.",
            "Apply the AIDE protocol: Analyse, Interrogate, Double-check, Expose.",
            "أن تطبّق بروتوكول AIDE: حلّل، استجوب، تحقّق مرتين، اعرض.",
        ),
        L(
            "Produire sa propre fiche finale : l'IA propose, tu structures.",
            "Produce your own final sheet: AI proposes, you structure.",
            "أن تنتج بطاقتك النهائية بنفسك: الذكاء الاصطناعي يقترح وأنت تنظّم.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 3 suivies. Apporter un polycopié ou un chapitre de cours à résumer.",
        "Sessions 1 to 3 completed. Bring a handout or a lesson chapter to summarise.",
        "إتمام الحصص من 1 إلى 3. إحضار ورقة درس أو فصلاً للتلخيص.",
    ),
    "accroche": {
        "question": L(
            "Un résumé copié-collé qui ne rentre pas dans la tête, ou une fiche d'une page qui fait réfléchir ? Aujourd'hui, on fabrique des fiches qui restent.",
            "A copy-pasted summary that never enters memory, or a one-page sheet that makes you think? Today, we craft sheets that stick.",
            "ملخص منسوخ لا يدخل الرأس، أم بطاقة صفحة واحدة تُفكِّر؟ اليوم نصنع بطاقات تبقى.",
        ),
        "analogie": L(
            "🍳 Résumer, c'est presser une orange : garder le jus (l'essentiel), jeter la pulpe (le remplissage). Synthétiser, c'est un cocktail de plusieurs fruits AVEC votre recette : le mélange n'existait pas avant vous.",
            "🍳 Summarising is squeezing an orange: keep the juice (the essentials), throw the pulp (the filler). Synthesising is a multi-fruit cocktail WITH your recipe: the mix never existed before you.",
            "🍳 التلخيص عصر برتقالة: الاحتفاظ بالعصير (الأساس) ورمي اللب (الحشو). والتركيب كوكتيل فواكه متعددة مع وصفتك: المزيج لم يوجد قبلك.",
        ),
        "phrase": L(
            "💡 Une bonne fiche = 1 page, vos mots, une structure fixe (idées, questions, exemples) — fabriquée AVEC l'IA, jamais À LA PLACE de vous.",
            "💡 A good sheet = 1 page, your words, a fixed structure (ideas, questions, examples) — made WITH AI, never INSTEAD of you.",
            "💡 البطاقة الجيدة = صفحة واحدة وكلماتك وهيكل ثابت (أفكار وأسئلة وأمثلة) — مصنوعة مع الذكاء أبداً بدلاً منك.",
        ),
    },
    "plan": [
        {
            "time": "00–10",
            **L(
                "Accueil et mise en route",
                "Welcome and warm-up",
                "استقبال وتمهيد",
            ),
            "detail": L(
                "Rappel séance 2. Question : « Comment faites-vous vos fiches aujourd'hui ? ».",
                "Recap of session 2. Question: \"How do you make your sheets today?\".",
                "مراجعة الحصة الثانية. سؤال: « كيف تعدّون بطاقاتكم اليوم؟ ».",
            ),
        },
        {
            "time": "10–25",
            **L(
                "Partie 1 : Résumer vs synthétiser",
                "Part 1: Summarising vs synthesising",
                "الجزء الأوّل: التلخيص مقابل التركيب",
            ),
            "detail": L(
                "Définitions, des exemples, et pourquoi l'étudiant doit savoir faire les deux (avec et sans IA).",
                "Definitions, examples, and why the student must know how to do both (with and without AI).",
                "تعريفات وأمثلة، ولماذا يجب على الطالب إتقان الاثنين (مع الذكاء الاصطناعي وبدونه).",
            ),
        },
        {
            "time": "25–45",
            **L(
                "Partie 2 : La structure d'une bonne fiche",
                "Part 2: The structure of a good sheet",
                "الجزء الثاني: بنية بطاقة جيدة",
            ),
            "detail": L(
                "Méthode Cornell : colonne idées / colonne questions / zone résumé. Exemple affiché.",
                "Cornell method: notes column / questions column / summary zone. Example displayed.",
                "منهج كورنيل: عمود أفكار / عمود أسئلة / منطقة ملخص. عرض مثال.",
            ),
        },
        {
            "time": "45–65",
            **L(
                "Partie 3 : Les prompts de synthèse",
                "Part 3: Synthesis prompts",
                "الجزء الثالث: صياغات التركيب",
            ),
            "detail": L(
                "Construire une consigne : rôle, source scannée ou collée, niveau, format, interdits.",
                "Building a prompt: role, scanned or pasted source, level, format, prohibitions.",
                "بناء تعليمات: الدور، المصدر المماسوح أو الملصق، المستوى، الصيغة، الممنوعات.",
            ),
        },
        {
            "time": "65–80",
            **L(
                "Activité : protocole AIDE en atelier",
                "Activity: AIDE protocol workshop",
                "نشاط: ورشة بروتوكول AIDE",
            ),
            "detail": L(
                "Chaque binôme résume un paragraphe du cours, vérifie, puis prépare une fiche Cornell individuelle.",
                "Each pair summarises a paragraph of the lesson, checks it, then makes an individual Cornell sheet.",
                "لكل مجموعة ثنائية تلخيص فقرة من الدرس، ثم التحقق، ثم إعداد بطاقة كورنيل فردية.",
            ),
        },
        {
            "time": "80–90",
            **L(
                "Synthèse et annonce de la séance 5",
                "Wrap-up and preview of session 5",
                "خلاصة وتقديم الحصة الخامسة",
            ),
            "detail": L(
                "« À retenir ». Annonce : préparer un exposé de A à Z avec l'IA.",
                "Key takeaways. Preview: preparing a presentation from A to Z with AI.",
                "« ما يجب تذكّره ». تقديم: تحضير عرض من الألف إلى الياء بالذكاء الاصطناعي.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Résumer, ce n'est pas synthétiser",
                "Summarising is not synthesising",
                "التلخيص ليس تركيباً",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Résumer = réduire un seul texte à ses idées principales. Synthétiser = assembler et comparer plusieurs textes sur un même thème, en dégageant des idées nouvelles. L'IA excelle dans les deux, mais elle perd le contexte : plus tu lui donnes de matière, plus elle te rend un résultat fidèle.",
                        "Summarising = reducing a single text to its main ideas. Synthesising = assembling and comparing several texts on one theme to bring out new ideas. AI excels at both, but it loses context: the more material you give it, the more faithful the result.",
                        "التلخيص = اختصار نص واحد إلى أفكاره الرئيسية. التركيب = جمع ومقارنة عدة نصوص حول موضوع واحد واستخراج أفكار جديدة. يجيد الذكاء الاصطناعي الاثنين، لكنه يفقد السياق: كلما أعطيته مادة أكثر، كانت النتيجة أوفى.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["", "Résumer", "Synthétiser"],
                        ["", "Summarise", "Synthesise"],
                        ["", "تلخيص", "تركيب"],
                    ),
                    "rows": L(
                        [
                            ["Source", "Un texte", "Plusieurs textes"],
                            ["But", "Réduire sans déformer", "Comparer, organiser, créer un point de vue"],
                            ["Longueur", "Souvent 1/3 à 1/5 du texte", "Variable, fonction des sources"],
                            ["Exemple", "Le résumé d'un chapitre", "La revue de littérature d'un mémoire"],
                        ],
                        [
                            ["Source", "One text", "Several texts"],
                            ["Goal", "Reduce without distorting", "Compare, organise, create a viewpoint"],
                            ["Length", "Often 1/3 to 1/5 of the text", "Variable, depends on the sources"],
                            ["Example", "A chapter summary", "A thesis literature review"],
                        ],
                        [
                            ["المصدر", "نص واحد", "عدة نصوص"],
                            ["الهدف", "الاختزال دون تشويه", "مقارنة وتنظيم وبناء رؤية"],
                            ["الطول", "غالباً ثلث أو خمس النص", "متغيّر حسب المصادر"],
                            ["مثال", "ملخص فصل", "الاستعراض النظري لمذكرة"],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séance 3 :</strong> on ne fiche que du VÉRIFIÉ : les sources validées sur Scholar/Perplexity deviennent la matière première des fiches. Un résumé de texte douteux reste douteux, même bien présenté.",
                        "<strong>🔗 Reminder of session 3:</strong> we only sheet VERIFIED material: Scholar/Perplexity-validated sources become the raw material of sheets. A summary of a dubious text stays dubious, however well presented.",
                        "<strong>🔗 تذكير بالحصة 3:</strong> لا نلخّص إلا الموثَّق: المصادر المعتمدة في Scholar وPerplexity تصبح المادة الأولية للبطاقات. ملخص نص مشكوك يبقى مشكوكاً مهما حَسُن عرضه.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "La structure d'une fiche de révision efficace",
                "The structure of an effective revision sheet",
                "بنية بطاقة مراجعة فعّالة",
            ),
            "blocks": [
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1. En-tête</strong> : module, chapitre, date d'examen, durée de révision estimée.",
                            "<strong>2. Idées-clés</strong> : 3 à 7 concepts, chacun en une ou deux lignes.",
                            "<strong>3. Schéma ou tableau</strong> : une représentation visuelle qui « vend » la page.",
                            "<strong>4. Questions d'auto-test</strong> : sur la colonne de gauche (méthode Cornell).",
                            "<strong>5. Exemples concrets</strong> : un exemple par idée, idéalement relié à ta future classe.",
                            "<strong>6. Zone résumé</strong> : 3 phrases en bas de page qui tiennent tout.",
                        ],
                        [
                            "<strong>1. Header</strong>: module, chapter, exam date, estimated revision time.",
                            "<strong>2. Key ideas</strong>: 3 to 7 concepts, each in one or two lines.",
                            "<strong>3. Diagram or table</strong>: a visual representation that \"sells\" the page.",
                            "<strong>4. Self-test questions</strong>: in the left column (Cornell method).",
                            "<strong>5. Concrete examples</strong>: one example per idea, ideally linked to your future class.",
                            "<strong>6. Summary zone</strong>: 3 sentences at the bottom that hold everything.",
                        ],
                        [
                            "<strong>1. الترويسة</strong>: الوحدة، الفصل، تاريخ الامتحان، المدة التقديرية للمراجعة.",
                            "<strong>2. الأفكار الرئيسية</strong>: من 3 إلى 7 مفاهيم، كل منها في سطر أو سطرين.",
                            "<strong>3. مخطط أو جدول</strong>: تمثيل بصري « يروّج » للصفحة.",
                            "<strong>4. أسئلة الاختبار الذاتي</strong>: في العمود الأيسر (منهج كورنيل).",
                            "<strong>5. أمثلة ملموسة</strong>: مثال لكل فكرة، مرتبط إن أمكن بقسمك المستقبلي.",
                            "<strong>6. منطقة الملخص</strong>: ثلاث جمل أسفل الصفحة تحمل كل شيء.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Méthode Cornell en 1 ligne :</strong> première colonne = questions que tu te poseras ; deuxième colonne = tes notes ; bas de page = résumé de toute la fiche. Se cacher la deuxième colonne = s'auto-tester.",
                        "<strong>Cornell in one line:</strong> first column = questions you will ask yourself; second column = your notes; bottom = summary of the whole sheet. Hiding the second column = self-testing.",
                        "<strong>كورنيل في سطر:</strong> العمود الأول = أسئلة تسألها لنفسك؛ العمود الثاني = ملاحظاتك؛ أسفل الصفحة = ملخص البطاقة كلها. إخفاء العمود الثاني = اختبار ذاتي.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> chapitre « les stades de Piaget » → fiche 1 page : 4 stades en tableau (âge, nom, exemple), question Cornell « à quel stade un enfant de 5 ans qui croit que la lune le suit ? » → réponse : préopératoire.",
                        "<strong>🧪 Concrete example:</strong> \"Piaget's stages\" chapter → 1-page sheet: 4 stages in a table (age, name, example), Cornell question \"at which stage is a 5-year-old believing the moon follows him?\" → answer: preoperational.",
                        "<strong>🧪 مثال ملموس:</strong> فصل « مراحل بياجيه » ← بطاقة صفحة: 4 مراحل في جدول (عمر، اسم، مثال)، وسؤال كورنيل « في أي مرحلة طفل 5 سنوات يظن القمر يتبعه؟ » ← الجواب: ما قبل الإجرائية.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Les prompts de synthèse : guider l'IA",
                "Synthesis prompts: guiding AI",
                "صياغات التركيب: توجيه الذكاء الاصطناعي",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Pour qu'une synthèse soit fidèle, donne à l'IA la matière (le texte collé ou scanné) et des consignes de format précises. Sans matière, elle résume… ce qu'elle croit savoir.",
                        "For a faithful synthesis, give AI the material (pasted or scanned text) and precise formatting instructions. Without material, it summarises… what it thinks it knows.",
                        "لكي يكون التركيب وفياً، أعطِ الذكاء الاصطناعي المادة (النص الملصق أو المماسوح) وتعليمات صياغة دقيقة. دون مادة، يلخّص… ما يظن أنه يعرفه.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Rôle</strong> : « Tu es un tuteur de licence… »",
                            "<strong>Source</strong> : « Voici le texte de mon cours [coller] ».",
                            "<strong>Niveau</strong> : « Explique pour un étudiant de 2ème année ».",
                            "<strong>Format</strong> : « Donne-moi 5 idées-clés, un tableau, 1 question par idée ».",
                            "<strong>Interdits</strong> : « N'ajoute aucune information absente du texte ».",
                        ],
                        [
                            "<strong>Role</strong>: \"You are an undergraduate tutor…\"",
                            "<strong>Source</strong>: \"Here is the text of my lesson [paste]\".",
                            "<strong>Level</strong>: \"Explain for a 2nd-year student\".",
                            "<strong>Format</strong>: \"Give me 5 key ideas, a table, 1 question per idea\".",
                            "<strong>Prohibitions</strong>: \"Add no information absent from the text\".",
                        ],
                        [
                            "<strong>الدور</strong>: « أنت مدرّس في مستوى ليسانس… »",
                            "<strong>المصدر</strong>: « هذا نص درسي [الصق] ».",
                            "<strong>المستوى</strong>: « اشرح لطالب السنة الثانية ».",
                            "<strong>الصيغة</strong>: « أعطني خمس أفكار رئيسية، جدولاً، وسؤالاً لكل فكرة ».",
                            "<strong>الممنوعات</strong>: « لا تضف أي معلومة غير موجودة في النص ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce de relance :</strong> après la première synthèse, demande « Qu'est-ce que j'ai oublié de préciser ? » ou « Compare ta synthèse à ce paragraphe. » L'IA vérifie mieux quand on lui demande de comparer.",
                        "<strong>Follow-up tip:</strong> after the first synthesis, ask \"What did I forget to specify?\" or \"Compare your synthesis to this paragraph.\" AI checks better when asked to compare.",
                        "<strong>نصيحة للمتابعة:</strong> بعد التركيب الأول، اسأل « ما الذي نسيتُ تحديده؟ » أو « قارن تركيبك بهذه الفقرة ». يتحقق الذكاء الاصطناعي أفضل عندما نطلب منه المقارنة.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Le protocole AIDE : garder la main",
                "The AIDE protocol: keeping control",
                "بروتوكول AIDE: الاحتفاظ بالسيطرة",
            ),
            "blocks": [
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>A — Analyser la source</strong> : lire le texte une fois, surligner 5 idées avant d'ouvrir un outil.",
                            "<strong>I — Interroger l'IA</strong> : envoyer la source complète avec format et interdits.",
                            "<strong>D — Double-vérifier</strong> : reprendre chaque idée retournée et la retrouver dans le texte source.",
                            "<strong>E — Exposer (restituer)</strong> : réécrire la fiche à ta façon, sans l'écran, pour t'approprier le contenu.",
                        ],
                        [
                            "<strong>A — Analyse the source</strong>: read the text once, highlight 5 ideas before opening any tool.",
                            "<strong>I — Interrogate AI</strong>: send the full source with format and prohibitions.",
                            "<strong>D — Double-check</strong>: take each returned idea and find it again in the source text.",
                            "<strong>E — Expose (restate)</strong>: rewrite the sheet your own way, without the screen, to own the content.",
                        ],
                        [
                            "<strong>أ — حلّل المصدر</strong>: اقرأ النص مرة، وظلّل خمس أفكار قبل فتح أي أداة.",
                            "<strong>س — استجوب الذكاء الاصطناعي</strong>: أرسل المصدر كاملاً مع الصيغة والممنوعات.",
                            "<strong>ت — تحقّق مرتين</strong>: خذ كل فكرة عادت بها وطابقها في النص الأصلي.",
                            "<strong>ع — اعرضها</strong>: أعد كتابة البطاقة بطريقتك دون شاشة لتمتلك المحتوى.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>Le danger du copier-coller :</strong> une fiche qui n'est pas « la tienne » ne sert à rien pour l'examen. La mémorisation passe par l'action : écrire, reformuler, se cacher la réponse.",
                        "<strong>The copy-paste danger:</strong> a sheet that is not \"yours\" is useless for the exam. Memorisation goes through action: write, rephrase, hide the answer.",
                        "<strong>خطر النسخ واللصق:</strong> بطاقة ليست « بطاقتك » لا تنفع للامتحان. الحفظ يمرّ عبر الفعل: الكتابة، إعادة الصياغة، إخفاء الإجابة.",
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
                        "Une fiche ne vaut que par ce que l'IA a reçu : sans source collée, elle résume ce qu'elle croit savoir. Donnez-lui TOUJOURS votre texte, puis gardez la main avec le protocole AIDE.",
                        "A sheet is only as good as what AI received: without the pasted source, it summarises what it thinks it knows. ALWAYS give it your text, then keep control with the AIDE protocol.",
                        "لا قيمة للبطاقة إلا بما تلقّاه الذكاء الاصطناعي: دون لصق المصدر، يلخّص ما يظن أنه يعرفه. أعطِه نصك دائماً، ثم احتفظ بالسيطرة عبر بروتوكول AIDE.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 5 :</strong> vos fiches Cornell deviennent le carburant de l'exposé : 3 fiches = 3 parties du plan, exemples inclus (séance 5).",
                        "<strong>➡️ Bridge to session 5:</strong> your Cornell sheets become presentation fuel: 3 sheets = 3 parts of the outline, examples included (session 5).",
                        "<strong>➡️ جسر إلى الحصة 5:</strong> بطاقات كورنيل تصبح وقود العرض: 3 بطاقات = 3 أجزاء من الخطة، بالأمثلة (الحصة 5).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Coller la matière :</strong> le texte source complet, même long ; l'IA est meilleure avec 10 pages qu'avec une consigne vague.",
                            "<strong>✅ Imposer le format :</strong> « 5 idées-clés, un tableau, une question par idée, un exemple par idée ».",
                            "<strong>✅ Demander la fidélité :</strong> « n'ajoute rien qui ne soit pas dans le texte ».",
                            "<strong>✅ Réécrire soi-même :</strong> la version finalisée du fichier est la vôtre, pas celle du robot.",
                        ],
                        [
                            "<strong>✅ Paste the material:</strong> the full source text, even long; AI is better with 10 pages than with a vague prompt.",
                            "<strong>✅ Impose a format:</strong> \"5 key ideas, a table, one question per idea, one example per idea\".",
                            "<strong>✅ Ask for faithfulness:</strong> \"add nothing that is not in the text\".",
                            "<strong>✅ Rewrite it yourself:</strong> the final sheet is yours, not the robot's.",
                        ],
                        [
                            "<strong>✅ الصق المادة:</strong> نص المصدر كاملاً ولو طال؛ فالمساعد أفضل مع عشر صفحات من مع تعليمة غامضة.",
                            "<strong>✅ فرض الصيغة:</strong> « خمس أفكار رئيسية، جدول، سؤال لكل فكرة، مثال لكل فكرة ».",
                            "<strong>✅ اطلب الوفاء:</strong> « لا تضف شيئاً غير موجود في النص ».",
                            "<strong>✅ أعد الكتابة بنفسك:</strong> النسخة النهائية للبطاقة هي لك أنت، لا للروبوت.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> demander un résumé <em>sans donner le texte</em> (illusion de fidélité), accepter des idées ajoutées sans vérification, et surtout <strong>apprendre une fiche qu'on n'a pas écrite</strong> — elle ne restera pas en mémoire.",
                        "<strong>❌ Mistakes to avoid:</strong> asking for a summary <em>without giving the text</em> (false sense of faithfulness), accepting added ideas unchecked, and above all <strong>studying a sheet you have not written</strong> — it will not stick.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> طلب ملخص <em>دون إعطاء النص</em> (وهم الوفاء)، وقبول أفكار مضافة دون تحقق، وخصوصاً <strong>مراجعة بطاقة لم تكتبها بنفسك</strong> — لن تثبت في الذاكرة.",
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
                            ["Requête", "« Résume-moi mon cours. »", "« Voici mon cours [coller]. Résume-le en 5 idées-clés, une question d'auto-test par idée, un exemple par idée. N'ajoute rien d'absent du texte. »"],
                            ["Résultat", "Résumé inventé, hors contexte.", "Fiche exacte, fidèle au polycopié, prête à réviser."],
                        ],
                        [
                            ["Prompt", "\"Summarise my lesson.\"", "\"Here is my lesson [paste]. Summarise it in 5 key ideas, one self-test question per idea, one example per idea. Add nothing absent from the text.\""],
                            ["Result", "Invented summary, out of context.", "An exact, faithful sheet, ready to revise."],
                        ],
                        [
                            ["الطلب", "« لخّص لي درسي »", "« هذا درسي [الصق]. لخّصه في خمس أفكار رئيسية، وسؤال اختبار ذاتي لكل فكرة، ومثال لكل فكرة. لا تضف شيئاً غير موجود في النص »"],
                            ["النتيجة", "ملخص مختلق خارج السياق.", "بطاقة دقيقة وفيّة بالطبقة، جاهزة للمراجعة."],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce de vérification :</strong> après la synthèse, demandez « compare ta réponse paragraphe par paragraphe au texte » — l'IA retrouve elle-même ses écarts, c'est le double-check le plus rapide.",
                        "<strong>Verification tip:</strong> after the synthesis, ask \"compare your answer paragraph by paragraph to the text\" — AI finds its own gaps, the fastest double-check.",
                        "<strong>نصيحة للتحقق:</strong> بعد التركيب، اطلب « قارن جوابك فقرة فقرة بالنص » — يجد المساعد أخطاءه بنفسه، وهي أسرع طريقة للتحقق المزدوج.",
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Quelle est la différence entre résumer et synthétiser ?",
                "What is the difference between summarising and synthesising?",
                "ما الفرق بين التلخيص والتركيب؟",
            ),
            "r": L(
                "Résumer = réduire UN texte sans le déformer. Synthétiser = croiser PLUSIEURS textes pour créer un point de vue nouveau.",
                "Summarising = shortening ONE text without distorting it. Synthesising = crossing SEVERAL texts to create a new viewpoint.",
                "التلخيص = اختزال نص واحد دون تشويه. والتركيب = تقاطع عدة نصوص لبناء رؤية جديدة.",
            ),
        },
        {
            "q": L(
                "Comment la méthode Cornell permet-elle l'auto-test ?",
                "How does the Cornell method enable self-testing?",
                "كيف تتيح منهجية كورنيل الاختبار الذاتي؟",
            ),
            "r": L(
                "Colonne gauche = questions, colonne droite = notes : on cache la droite et on répond aux questions de gauche.",
                "Left column = questions, right column = notes: hide the right side and answer the left questions.",
                "العمود الأيسر = أسئلة والأيمن = ملاحظات: أخفِ الأيمن وأجب عن أسئلة الأيسر.",
            ),
        },
        {
            "q": L(
                "Pourquoi coller son texte source à l'IA avant de demander un résumé ?",
                "Why paste your source text to AI before asking for a summary?",
                "لماذا تلصق نص المصدر للذكاء قبل طلب الملخص؟",
            ),
            "r": L(
                "Sans le texte, l'IA résume ce qu'elle CROIT savoir (risque d'invention). Avec le texte, elle travaille sur du réel et reste fidèle.",
                "Without the text, AI summarises what it BELIEVES it knows (invention risk). With the text, it works on reality and stays faithful.",
                "دون النص يلخّص الذكاء ما يظن معرفته (خطر الاختلاق). ومع النص يعمل على الواقع ويلتزم الأمانة.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "Avec votre polycopié : 1) collez 2 pages à l'IA + prompt Cornell ; 2) recevez la fiche ; 3) vérifiez chaque idée contre le texte (cochez ✓ ou corrigez).",
            "With your handout: 1) paste 2 pages to AI + Cornell prompt; 2) receive the sheet; 3) check each idea against the text (tick ✓ or fix).",
            "بمطبوعتك: 1) الصق صفحتين للذكاء + صياغة كورنيل؛ 2) استلم البطاقة؛ 3) تحقق من كل فكرة مقابل النص (علّم ✓ أو صحّح).",
        ),
        "demarche": L(
            "1) Prompt : « Voici 2 pages [coller]. Fiche Cornell : idées-clés, tableau, 3 questions d'auto-test, 1 exemple, résumé 3 phrases. » 2) Comparer au texte, ligne par ligne. 3) Réécrire 1 idée avec vos mots.",
            "1) Prompt: \"Here are 2 pages [paste]. Cornell sheet: key ideas, table, 3 self-test questions, 1 example, 3-sentence summary.\" 2) Compare with the text, line by line. 3) Rewrite 1 idea in your words.",
            "1) الصياغة: « هاتان صفحتان [الصق]. بطاقة كورنيل: أفكار رئيسية وجدول و3 أسئلة اختبار ومثال وملخص 3 جمل ». 2) قارن بالنص سطراً سطراً. 3) أعد كتابة فكرة بكلماتك.",
        ),
        "solution": L(
            "Réussi si : fiche 1 page (6 zones remplies), chaque idée cochée ✓ contre le texte, 1 idée réécrite personnellement, et 1 erreur de l'IA repérée et corrigée (il y en a presque toujours une).",
            "Success if: 1-page sheet (6 zones filled), each idea ticked ✓ against the text, 1 idea personally rewritten, and 1 AI mistake spotted and fixed (there is almost always one).",
            "نجاح إذا: بطاقة صفحة (6 مناطق مملوءة)، وكل فكرة مؤشَّرة ✓ مقابل النص، وفكرة معاد كتابتها شخصياً، وخطأ للذكاء مرصود ومصحَّح (يوجد دائماً تقريباً).",
        ),
    },
    "videos": [
        {
            "titre": L(
                "La méthode Cornell pour des fiches qui marchent (tutoriel)",
                "The Cornell method for sheets that work (tutorial)",
                "منهجية كورنيل لبطاقات ناجحة (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=methode+cornell+fiche+revision+tutoriel",
            "langue": "fr",
            "concept": L(
                "Tracer sa première fiche Cornell et s'auto-tester en la cachant.",
                "Draw your first Cornell sheet and self-test by hiding it.",
                "ارسم أول بطاقة كورنيل واختبر نفسك بإخفائها.",
            ),
        },
        {
            "titre": L(
                "كيف تلخّص درساً بالذكاء الاصطناعي دون أخطاء؟",
                "How to summarise a lesson with AI without mistakes?",
                "كيف تلخّص درساً بالذكاء الاصطناعي دون أخطاء؟",
            ),
            "url": "https://www.youtube.com/results?search_query=تلخيص+الدروس+بالذكاء+الاصطناعي+للطلبة",
            "langue": "ar",
            "concept": L(
                "Coller la source, guider avec un prompt, vérifier ligne par ligne.",
                "Paste the source, guide with a prompt, check line by line.",
                "الصق المصدر ووجّه بصياغة وتحقق سطراً سطراً.",
            ),
        },
        {
            "titre": L(
                "Transformer un PDF en carte mentale (méthode)",
                "Turn a PDF into a mind map (method)",
                "تحويل PDF إلى خريطة ذهنية (منهجية)",
            ),
            "url": "https://www.youtube.com/results?search_query=pdf+carte+mentale+revision+methode",
            "langue": "fr",
            "concept": L(
                "Du chapitre à la carte visuelle qui « vend » la page.",
                "From chapter to the visual map that \"sells\" the page.",
                "من الفصل إلى الخريطة البصرية التي « تروّج » للصفحة.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "Résumer = 1 texte réduit. Synthétiser = plusieurs textes croisés + votre point de vue.",
                "Summarise = 1 text shortened. Synthesise = several texts crossed + your viewpoint.",
                "التلخيص = اختزال نص واحد. والتركيب = تقاطع نصوص + وجهة نظرك.",
            ),
            L(
                "Fiche Cornell : questions à gauche, notes à droite, résumé en bas.",
                "Cornell sheet: questions left, notes right, summary bottom.",
                "بطاقة كورنيل: أسئلة يساراً وملاحظات يميناً وملخص أسفل.",
            ),
            L(
                "Toujours coller le texte source avant de demander.",
                "Always paste the source text before asking.",
                "الصق نص المصدر دائماً قبل الطلب.",
            ),
            L(
                "Vérifier chaque idée contre le texte (✓ ou corriger).",
                "Check each idea against the text (✓ or fix).",
                "تحقق من كل فكرة مقابل النص (✓ أو صحّح).",
            ),
            L(
                "Protocole AIDE : garder la main du début à la fin.",
                "AIDE protocol: keep control from start to finish.",
                "بروتوكول AIDE: حافظ على السيطرة من البداية للنهاية.",
            ),
        ],
        "analogies": [
            L(
                "Le jus d'orange : garder l'essentiel, jeter la pulpe.",
                "Orange juice: keep the essentials, throw the pulp.",
                "عصير البرتقال: احتفظ بالأساس وارمِ اللب.",
            ),
            L(
                "Le cocktail : plusieurs fruits + VOTRE recette.",
                "The cocktail: several fruits + YOUR recipe.",
                "الكوكتيل: فواكه عدة + وصفتك أنت.",
            ),
            L(
                "Le miroir : la fiche doit refléter le texte, pas l'inventer.",
                "The mirror: the sheet must reflect the text, not invent it.",
                "المرآة: البطاقة تعكس النص ولا تختلقه.",
            ),
        ],
        "exemples": [
            L(
                "Chapitre Piaget → tableau 4 stades + question lune → préopératoire.",
                "Piaget chapter → 4-stage table + moon question → preoperational.",
                "فصل بياجيه ← جدول 4 مراحل + سؤال القمر ← ما قبل الإجرائية.",
            ),
            L(
                "2 pages collées → fiche 6 zones → 1 erreur d'IA corrigée.",
                "2 pasted pages → 6-zone sheet → 1 AI mistake fixed.",
                "صفحتان ملصقتان ← بطاقة 6 مناطق ← خطأ ذكاء مصحَّح.",
            ),
            L(
                "Fiche relue à J+3 : cacher la droite, répondre à gauche.",
                "Sheet reviewed at D+3: hide right, answer left.",
                "بطاقة تُراجَع اليوم+3: أخفِ اليمين وأجب عن اليسار.",
            ),
        ],
        "analogie_finale": L(
            "🏁 Votre fiche et l'IA, c'est comme votre cuisine et le robot : il épluche et coupe vite (le brouillon), mais l'assaisonnement final (vos mots, votre structure, votre vérification), c'est vous — sinon le plat n'a aucun goût.",
            "🏁 Your sheet and AI is like your kitchen and the food processor: it peels and chops fast (the draft), but final seasoning (your words, structure, check) is you — else the dish tastes of nothing.",
            "🏁 بطاقتك والذكاء كمطبخك ومحضّرة الطعام: تقشّر وتقطّع بسرعة (المسودة)، لكن التتبيلة النهائية (كلماتك وهيكلك وتحققك) أنت — وإلا كان الطبق بلا طعم.",
        ),
        "quiz": [
            {
                "q": L(
                    "Résumer ou synthétiser : que choisir pour 3 articles ?",
                    "Summarise or synthesise: what for 3 papers?",
                    "التلخيص أم التركيب: ماذا لثلاثة مقالات؟",
                ),
                "options": L(
                    ["Résumer chacun séparément seulement", "Synthétiser : croiser les 3 + ajouter votre point de vue", "Copier le plus long", "Ne rien faire"],
                    ["Summarise each separately only", "Synthesise: cross all 3 + add your viewpoint", "Copy the longest", "Do nothing"],
                    ["لخّص كلاًّ على حدة فقط", "ركّب: قاطع الثلاثة + أضف وجهة نظرك", "انسخ الأطول", "لا تفعل شيئاً"],
                ),
                "answer": 1,
                "exp": L(
                    "Plusieurs sources = synthèse : comparaison + organisation + votre lecture.",
                    "Several sources = synthesis: comparison + organisation + your reading.",
                    "مصادر عدة = تركيب: مقارنة + تنظيم + قراءتك.",
                ),
            },
            {
                "q": L(
                    "Où vont les questions d'auto-test dans Cornell ?",
                    "Where do self-test questions go in Cornell?",
                    "أين أسئلة الاختبار الذاتي في كورنيل؟",
                ),
                "options": L(
                    ["En bas", "Colonne de gauche (on cache la droite pour se tester)", "Nulle part", "Dans la marge du voisin"],
                    ["At the bottom", "Left column (hide the right to test yourself)", "Nowhere", "In the neighbour's margin"],
                    ["أسفل", "العمود الأيسر (أخفِ الأيمن لتختبر نفسك)", "لا مكان", "في هامش الجار"],
                ),
                "answer": 1,
                "exp": L(
                    "Gauche = questions, droite = notes : caché la droite, la fiche devient un interrogateur.",
                    "Left = questions, right = notes: hiding the right turns the sheet into a questioner.",
                    "اليسار = أسئلة واليمين = ملاحظات: إخفاء اليمين يحوّل البطاقة إلى مستجوب.",
                ),
            },
            {
                "q": L(
                    "Pourquoi coller le texte source à l'IA ?",
                    "Why paste the source text to AI?",
                    "لماذا تلصق نص المصدر للذكاء؟",
                ),
                "options": L(
                    ["Pour décorer", "Pour qu'elle travaille sur du réel au lieu d'inventer", "Pour ralentir", "Inutile"],
                    ["For decoration", "So it works on reality instead of inventing", "To slow down", "Useless"],
                    ["للزينة", "ليعمل على الواقع بدل الاختلاق", "للإبطاء", "لا فائدة"],
                ),
                "answer": 1,
                "exp": L(
                    "Sans source collée, l'IA résume ses souvenirs approximatifs : hallucinations garanties.",
                    "Without pasted source, AI summarises approximate memories: guaranteed hallucinations.",
                    "دون مصدر ملصق يلخّص الذكاء ذكرياته التقريبية: هلوسات مضمونة.",
                ),
            },
            {
                "q": L(
                    "Que faire d'une idée de la fiche non retrouvée dans le texte ?",
                    "What to do with a sheet idea missing from the text?",
                    "ماذا تفعل بفكرة في البطاقة غير موجودة في النص؟",
                ),
                "options": L(
                    ["La garder, elle est jolie", "La corriger ou la supprimer : c'est une invention de l'IA", "L'encadrer", "L'ignorer"],
                    ["Keep it, it is pretty", "Fix or delete it: it is an AI invention", "Frame it", "Ignore it"],
                    ["أبقها فهي جميلة", "صحّحها أو احذفها: إنها اختلاق ذكاء", "أطّرها", "تجاهلها"],
                ),
                "answer": 1,
                "exp": L(
                    "Vérification ligne par ligne : toute idée sans ancrage texte = hallucination à éliminer.",
                    "Line-by-line check: any idea without text anchor = hallucination to remove.",
                    "التحقق سطراً سطراً: كل فكرة دون مرساة نصية = هلوسة تُزال.",
                ),
            },
            {
                "q": L(
                    "Quel est le rôle du protocole AIDE ?",
                    "What is the AIDE protocol for?",
                    "ما دور بروتوكول AIDE؟",
                ),
                "options": L(
                    ["Tout déléguer", "Garder la main : vous décidez, l'IA exécute sous contrôle", "Appeler à l'aide", "Éviter l'IA"],
                    ["Delegate everything", "Keep control: you decide, AI executes under supervision", "Call for help", "Avoid AI"],
                    ["تفويض كل شيء", "الحفاظ على السيطرة: أنت تقرّر والذكاء ينفذ تحت إشراف", "طلب النجدة", "تجنّب الذكاء"],
                ),
                "answer": 1,
                "exp": L(
                    "AIDE = vous pilotez chaque étape : source collée, consignes précises, vérification finale.",
                    "AIDE = you drive each step: pasted source, precise instructions, final check.",
                    "AIDE = أنت تقود كل خطوة: مصدر ملصق وتعليمات دقيقة وتحقق نهائي.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Démo guidée : résumer un paragraphe du cours avec un prompt complet (rôle, source, niveau, format, interdits), puis comparer avec la version sans source.",
            "Guided demo: summarise a lesson paragraph with a full prompt (role, source, level, format, prohibitions), then compare with the version without a source.",
            "عرض موجَّه: تلخيص فقرة من الدرس بصياغة كاملة (دور، مصدر، مستوى، صيغة، ممنوعات)، ثم المقارنة مع النسخة دون مصدر.",
        ),
        L(
            "Atelier Cornell : chaque étudiant transforme sa synthèse IA en fiche Cornell (questions à gauche, notes à droite, résumé en bas).",
            "Cornell workshop: each student turns their AI synthesis into a Cornell sheet (questions left, notes right, summary at the bottom).",
            "ورشة كورنيل: يحوّل كل طالب تركيب الذكاء الاصطناعي إلى بطاقة كورنيل (أسئلة يساراً، ملاحظات يميناً، ملخص أسفل).",
        ),
        L(
            "Jeu des « 2 sources » : croiser la synthèse de ChatGPT avec celle de Perplexity sur le même texte et relever les différences.",
            "\"2 sources\" game: cross ChatGPT's synthesis with Perplexity's on the same text and spot the differences.",
            "لعبة « المصدرين »: قارن تركيب ChatGPT بتركيب Perplexity على النص نفسه وسجّل الفروق.",
        ),
        L(
            "Test de fidélité : ajouter une fausse idée dans le texte source et vérifier si l'IA la reprend dans sa synthèse.",
            "Fidelity test: add a false idea to the source text and check whether AI repeats it in its synthesis.",
            "اختبار الوفاء: أضف فكرة خاطئة في النص، وتحقّق هل يكرّرها الذكاء الاصطناعي في تركيبه.",
        ),
    ],
    "retenir": [
        L(
            "Résumer = réduire un texte ; synthétiser = croiser plusieurs textes.",
            "Summarising = reducing a text; synthesising = cross-checking several texts.",
            "التلخيص = اختصار نص؛ التركيب = تطابق عدة نصوص.",
        ),
        L(
            "Une bonne fiche : idées-clés, schéma, questions d'auto-test, exemples, résumé final.",
            "A good sheet: key ideas, diagram, self-test questions, examples, final summary.",
            "البطاقة الجيدة: أفكار رئيسية، مخطط، أسئلة اختبار ذاتي، أمثلة، ملخص نهائي.",
        ),
        L(
            "Prompt de synthèse = rôle + source + niveau + format + interdits.",
            "Synthesis prompt = role + source + level + format + prohibitions.",
            "صياغة التركيب = دور + مصدر + مستوى + صيغة + ممنوعات.",
        ),
        L(
            "Protocole AIDE : Analyser, Interroger, Double-vérifier, Exposer.",
            "AIDE protocol: Analyse, Interrogate, Double-check, Expose.",
            "بروتوكول AIDE: حلّل، استجوب، تحقّق مرتين، اعرض.",
        ),
        L(
            "Une fiche n'est utile que si elle devient « la tienne » : réécris-la toi-même.",
            "A sheet is useful only if it becomes \"yours\": rewrite it yourself.",
            "البطاقة لا تنفع إلا إذا أصبحت « بطاقتك »: أعد كتابتها بنفسك.",
        ),
    ],
    "glossaire": [
        {
            "term": "Résumé",
            "term_en": "Summary",
            "def_fr": "Version réduite d'un texte unique, fidèle aux idées principales.",
            "def_en": "A reduced version of a single text, faithful to the main ideas.",
            "def_ar": "نسخة مختصرة لنص واحد، وفيّة بالأفكار الرئيسية.",
        },
        {
            "term": "Synthèse",
            "term_en": "Synthesis",
            "def_fr": "Croisement de plusieurs documents pour construire une vue d'ensemble.",
            "def_en": "Crossing several documents to build an overview.",
            "def_ar": "تطابق عدة وثائق لبناء نظرة عامة.",
        },
        {
            "term": "Fiche de révision",
            "term_en": "Revision sheet",
            "def_fr": "Document court qui concentre l'essentiel d'un cours pour le réviser rapidement.",
            "def_en": "A short document that concentrates the essentials of a lesson for quick revision.",
            "def_ar": "وثيقة قصيرة تركّز أساسيات درس لمراجعته بسرعة.",
        },
        {
            "term": "Méthode Cornell",
            "term_en": "Cornell method",
            "def_fr": "Structure de prise de notes en trois zones : questions, notes, résumé.",
            "def_en": "A note-taking structure in three zones: questions, notes, summary.",
            "def_ar": "بنية تدوين في ثلاث مناطق: أسئلة، ملاحظات، ملخص.",
        },
        {
            "term": "Protocole AIDE",
            "term_en": "AIDE protocol",
            "def_fr": "Méthode en 4 étapes pour travailler avec l'IA sans perdre le contrôle : Analyser, Interroger, Double-vérifier, Exposer.",
            "def_en": "A 4-step method to work with AI without losing control: Analyse, Interrogate, Double-check, Expose.",
            "def_ar": "منهج من أربع خطوات للعمل مع الذكاء الاصطناعي دون فقدان السيطرة: حلّل، استجوب، تحقّق مرتين، اعرض.",
        },
    ],
    "dialogues_fr": """# Séance 04 — Dialogues pédagogiques (Français)

## Dialogue A — « La fiche qui n'était pas la mienne » (25 min)

**Personnages :** Sara (étudiante), l'IA (jouée par un camarade), Karim (camarade qui aide).

---

Sara : J'ai demandé à l'IA de résumer mon cours de didactique. Regarde, c'est parfait !

Karim : Parfait ? Tu l'as relu, comparé au texte ?

Sara : Non… il écrit tellement bien.

Karim : Sara, une fiche que tu n'as pas réécrite, tu ne la retiendras pas. Surtout, vérifie qu'il n'a rien ajouté.

Sara : Comment je vérifie, moi ?

Karim : Le protocole AIDE ! D'abord, tu lis le cours une fois et tu surlignes tes 5 idées. Ensuite, tu interroges l'IA avec le texte collé. Ensuite tu revérifies idée par idée.

IA : Je peux aussi me corriger. Donne-moi ta liste de 5 idées et je compare avec ma synthèse.

Sara : Bon, je tente. Mes 5 idées : 1) la transposition didactique, 2) le contrat didactique…

IA : Attention : j'ai bien la 1, mais la 2 n'apparaît pas dans ton texte. Je l'ai ajoutée d'après mes connaissances. Tu avais dit « n'ajoute rien » : donc mea culpa.

Sara : Tu vois, Karim ? Il a inventé une phrase et je l'aurais apprise !

Karim : C'est exactement pour ça qu'on vérifie. Maintenant, réécris la fiche à ta façon, sans l'écran, en t'aidant de tes questions Cornell.

Sara : Et si je n'arrive pas à reformuler ?

Karim : Alors tu n'as pas encore compris — et c'est justement là que l'IA est utile : elle explique, tu comprends, tu reformules. Jamais l'inverse.

---

## Dialogue B — « Maman, c'est une note de cours ! » (15 min)

**Personnages :** Yacine (étudiant), sa mère, le petit frère Anis (9 ans).

---

Yacine : Je colle mes notes de cours et je demande : « transforme ça en fiche Cornell ».

Anis : Tu triches, non ?

Yacine : Non ! Pour tricher, il faudrait que je ne comprenne pas. Moi je comprends, je vérifie, et je réécris.

Maman : Et l'ordinateur, il fait quoi exactement ?

Yacine : Il organise mes notes en tableau, il propose des questions, il connaît la mise en forme de Cornell. Moi, je contrôle tout.

Anis : Alors c'est comme le concierge qui range ta chambre ?

Yacine : Presque ! Sauf que le concierge, il ne doit pas déplacer mes affaires sans me dire où. Si l'IA déplace une idée, je dois la retrouver.

Maman : Et si tu ne la retrouves pas ?

Yacine : Je lui demande de comparer avec le texte. C'est le « double-check ».

Anis : Et pourquoi tu réécris ensuite dans le cahier ?

Yacine : Parce que c'est en écrivant que je mémorise. L'ordinateur range, c'est moi qui apprends.

---

## Mini-rôle à jouer (3 min par binôme)
Un étudiant montre une synthèse IA très belle mais où une idée a été ajoutée. Avec l'autre, trouvez l'idée inventée (en comparant au texte source) et reformulez la règle : « la synthèse ne doit contenir que ce qui est dans la source ».
""",
    "dialogues_en": """# Session 04 — Classroom dialogues (English)

## Dialogue A — "The sheet that was not mine" (25 min)

**Characters:** Sara (student), the AI (played by a classmate), Karim (classmate who helps).

---

Sara: I asked AI to summarise my teaching-method course. Look, it's perfect!

Karim: Perfect? Did you re-read it and compare it with the text?

Sara: No… it writes so well.

Karim: Sara, a sheet you have not rewritten, you will not remember. Above all, check that it added nothing.

Sara: How do I check?

Karim: The AIDE protocol! First, read the lesson once and highlight your 5 ideas. Then interrogate AI with the pasted text. Then re-check idea by idea.

AI: I can also correct myself. Give me your list of 5 ideas and I will compare it with my synthesis.

Sara: OK, let me try. My 5 ideas: 1) didactic transposition, 2) the didactic contract…

AI: Careful: I have idea 1, but idea 2 does not appear in your text. I added it from my own knowledge. You had said "add nothing", so mea culpa.

Sara: You see, Karim? It invented a sentence and I would have learned it!

Karim: That is exactly why we check. Now, rewrite the sheet your own way, without the screen, using your Cornell questions.

Sara: And if I cannot rephrase?

Karim: Then you have not understood yet — and that is exactly where AI helps: it explains, you understand, you rephrase. Never the other way round.

---

## Dialogue B — "Mum, it's a course note!" (15 min)

**Characters:** Yacine (student), his mother, little brother Anis (age 9).

---

Yacine: I paste my course notes and ask: "turn this into a Cornell sheet".

Anis: You cheat, right?

Yacine: No! To cheat I would have to not understand. I understand, I check, and I rewrite.

Mum: And the computer, what exactly does it do?

Yacine: It organises my notes into a table, suggests questions, knows the Cornell layout. I control everything.

Anis: So it is like the janitor who tidies your room?

Yacine: Almost! Except the janitor must not move my things without telling me where. If AI moves an idea, I must find it again.

Mum: And if you don't find it?

Yacine: I ask it to compare with the text. That is the "double-check".

Anis: And why do you rewrite it in the notebook afterwards?

Yacine: Because it is by writing that I remember. The computer tidies, but I learn.

---

## Mini role-play (3 min per pair)
A student shows a very nice AI synthesis in which one idea was added. With your partner, find the invented idea (by comparing with the source text) and rephrase the rule: "the synthesis may only contain what is in the source".
""",
}