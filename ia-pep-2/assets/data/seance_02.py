# -*- coding: utf-8 -*-
"""Séance 02 — Panorama des 12+ outils d'IA pour l'étudiant (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 2,
    "slug": "seance-02",
    "icon": "🧰",
    "titles": L(
        "Panorama des 12+ outils d'IA pour l'étudiant",
        "Overview of 12+ AI tools for students",
        "نظرة عامة على أكثر من 12 أداة ذكاء اصطناعي للطالب",
    ),
    "descriptions": L(
        "Vue d'ensemble des outils d'IA : à quoi sert chacun, comment les classer en 4 familles, démonstration rapide de 3 outils et méthode pour toujours choisir le bon.",
        "Overview of AI tools: what each is for, how to sort them into 4 families, quick demo of 3 tools and a method to always pick the right one.",
        "نظرة شاملة على أدوات الذكاء: وظيفة كل منها وكيفية تصنيفها في 4 عائلات وعرض سريع لثلاث أدوات ومنهجية لاختيار المناسب دائماً.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Classer les outils d'IA en 4 familles : comprendre, chercher, créer, organiser-coder.",
            "Sort AI tools into 4 families: understand, search, create, organise-code.",
            "أن يصنّف أدوات الذكاء في 4 عائلات: الفهم والبحث والإنشاء والتنظيم-البرمجة.",
        ),
        L(
            "Décrire en une phrase l'usage de chacun des 12 outils du module.",
            "Describe in one sentence the use of each of the module's 12 tools.",
            "أن يصف بجملة استعمال كل أداة من أدوات الوحدة الاثنتي عشرة.",
        ),
        L(
            "Comparer 3 outils en démonstration : assistant, moteur sourcé, création visuelle.",
            "Compare 3 tools in a demo: assistant, sourced engine, visual creation.",
            "أن يقارن 3 أدوات عملياً: مساعد ومحرّك بمصادر وإنشاء بصري.",
        ),
        L(
            "Choisir le bon outil pour une tâche avec l'arbre de décision.",
            "Pick the right tool for a task with the decision tree.",
            "أن يختار الأداة المناسبة لمهمة بشجرة القرار.",
        ),
        L(
            "Éviter les 3 erreurs de débutant : tout demander au même outil, croire sans vérifier, payer avant d'essayer le gratuit.",
            "Avoid 3 beginner mistakes: asking everything to one tool, believing without checking, paying before trying free.",
            "أن يتجنّب 3 أخطاء مبتدئة: طلب كل شيء من أداة واحدة والتصديق دون تحقق والدفع قبل تجربة المجاني.",
        ),
    ],
    "prerequis": L(
        "Séance 1 suivie. Savoir ouvrir un navigateur et avoir (si possible) un compte gratuit sur un outil d'IA.",
        "Session 1 completed. Know how to open a browser and, if possible, have a free account on an AI tool.",
        "إتمام الحصة الأولى. معرفة فتح متصفّح، وإن أمكن امتلاك حساب مجاني على أداة ذكاء اصطناعي.",
    ),
    "accroche": {
        "question": L(
            "ChatGPT, Gemini, Perplexity, Canva, Notion… 12 noms sur le tableau : qui peut dire à quoi sert chacun ? Aujourd'hui, on range cette jungle.",
            "ChatGPT, Gemini, Perplexity, Canva, Notion… 12 names on the board: who can say what each is for? Today, we tidy this jungle.",
            "ChatGPT وGemini وPerplexity وCanva وNotion… 12 اسماً على السبورة: من يقول وظيفة كل منها؟ اليوم نرتّب هذه الغابة.",
        ),
        "analogie": L(
            "🍳 Les outils d'IA, c'est comme la pharmacie : on ne soigne pas tout avec le même sirop. Le pharmacien (vous, bientôt) lit l'ordonnance (la tâche) puis choisit le bon flacon.",
            "🍳 AI tools are like the pharmacy: you do not cure everything with the same syrup. The pharmacist (you, soon) reads the prescription (the task) then picks the right bottle.",
            "🍳 أدوات الذكاء كالصيدلية: لا نداوي كل شيء بنفس الشراب. والصيدلي (أنت قريباً) يقرأ الوصفة (المهمة) ثم يختار القارورة المناسبة.",
        ),
        "phrase": L(
            "💡 12 outils, 4 familles : COMPRENDRE (assistants), CHERCHER (moteurs sourcés), CRÉER (slides, images, voix), ORGANISER-CODER (notes, code, local).",
            "💡 12 tools, 4 families: UNDERSTAND (assistants), SEARCH (sourced engines), CREATE (slides, images, voice), ORGANISE-CODE (notes, code, local).",
            "💡 12 أداة و4 عائلات: الفهم (مساعدات) والبحث (محرّكات بمصادر) والإنشاء (عروض وصور وصوت) والتنظيم-البرمجة (ملاحظات وكود ومحلي).",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : la jungle des 12 noms",
                "Hook: the 12-name jungle",
                "انطلاقة: غابة الأسماء الاثني عشر",
            ),
            "detail": L(
                "Sondage : qui utilise quoi ? + analogie de la pharmacie.",
                "Survey: who uses what? + pharmacy analogy.",
                "استطلاع: من يستعمل ماذا؟ + تشبيه الصيدلية.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : les 4 familles",
                "Explanation: the 4 families",
                "شرح: العائلات الأربع",
            ),
            "detail": L(
                "Comprendre, chercher, créer, organiser-coder : 1 exemple étudiant par famille.",
                "Understand, search, create, organise-code: 1 student example per family.",
                "الفهم والبحث والإنشاء والتنظيم-البرمجة: مثال طلابي لكل عائلة.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : 3 outils en action",
                "Demo: 3 tools in action",
                "عرض: 3 أدوات عملياً",
            ),
            "detail": L(
                "Même question à ChatGPT, Perplexity et Canva : comparer les réponses.",
                "Same question to ChatGPT, Perplexity and Canva: compare answers.",
                "نفس السؤال لـ ChatGPT وPerplexity وCanva: قارن الأجوبة.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : le bon pharmacien",
                "Guided exercise: the good pharmacist",
                "تمرين موجّه: الصيدلي الجيد",
            ),
            "detail": L(
                "8 situations d'étudiant → prescrire le bon outil avec l'arbre de décision.",
                "8 student situations → prescribe the right tool with the decision tree.",
                "8 حالات طلابية ← اصرف الأداة المناسبة بشجرة القرار.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : mauvais vs bon prompt",
                "Demo 2: bad vs good prompt",
                "عرض 2: صياغة ضعيفة مقابل قوية",
            ),
            "detail": L(
                "« Fais mon exposé » contre la requête en 4 composantes : le fossé en direct.",
                "“Do my talk” vs the 4-component query: the gap, live.",
                "« أنجز عرضي » مقابل الصياغة بالعناصر الأربعة: الهوة مباشرة.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et annonce de la séance 3",
                "Wrap-up, quiz and preview of session 3",
                "خلاصة واختبار وتقديم الحصة الثالثة",
            ),
            "detail": L(
                "« À retenir ». Annonce : la recherche approfondie avec Perplexity et Scholar.",
                "Key takeaways. Preview: deep research with Perplexity and Scholar.",
                "« ما يجب تذكّره ». تقديم: البحث المعمَّق بـ Perplexity وScholar.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Les 4 familles : rangez la jungle",
                "The 4 families: tidy the jungle",
                "العائلات الأربع: رتّب الغابة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Retenez 4 tiroirs, pas 12 noms. Devant chaque tâche, demandez-vous : est-ce que je veux COMPRENDRE, CHERCHER, CRÉER ou ORGANISER-CODER ? Le tiroir désigne l'outil.",
                        "Remember 4 drawers, not 12 names. Before each task, ask: do I want to UNDERSTAND, SEARCH, CREATE or ORGANISE-CODE? The drawer points to the tool.",
                        "احفظ 4 أدراج لا 12 اسماً. أمام كل مهمة اسأل: هل أريد الفهم أم البحث أم الإنشاء أم التنظيم-البرمجة؟ الدرج يدل على الأداة.",
                    ),
                },
                {
                    "t": "table",
                    "header": L(
                        ["Famille", "Outils", "Exemple étudiant"],
                        ["Family", "Tools", "Student example"],
                        ["العائلة", "الأدوات", "مثال طلابي"],
                    ),
                    "rows": L(
                        [
                            ["🔵 COMPRENDRE", "ChatGPT, Gemini, Claude", "« Explique-moi Piaget en 5 points »"],
                            ["🟢 CHERCHER", "Perplexity, Scholar, Consensus, NotebookLM", "« Quelles études 2020-2026 sur les écrans ? »"],
                            ["🟠 CRÉER", "Gamma, Canva IA, DALL·E, ElevenLabs", "« 5 slides + 1 affiche pour mon exposé »"],
                            ["🟣 ORGANISER-CODER", "Notion AI, Copilot/Cursor, Ollama, Dify", "« Planning 4 semaines + script Python »"],
                        ],
                        [
                            ["🔵 UNDERSTAND", "ChatGPT, Gemini, Claude", "\"Explain Piaget in 5 points\""],
                            ["🟢 SEARCH", "Perplexity, Scholar, Consensus, NotebookLM", "\"Which 2020-2026 studies on screens?\""],
                            ["🟠 CREATE", "Gamma, Canva AI, DALL·E, ElevenLabs", "\"5 slides + 1 poster for my talk\""],
                            ["🟣 ORGANISE-CODE", "Notion AI, Copilot/Cursor, Ollama, Dify", "\"4-week schedule + Python script\""],
                        ],
                        [
                            ["🔵 الفهم", "ChatGPT وGemini وClaude", "« اشرح لي بياجيه في 5 نقاط »"],
                            ["🟢 البحث", "Perplexity وScholar وConsensus وNotebookLM", "« ما دراسات 2020-2026 عن الشاشات؟ »"],
                            ["🟠 الإنشاء", "Gamma وCanva IA وDALL·E وElevenLabs", "« 5 شرائح + ملصق لعرضي »"],
                            ["🟣 التنظيم-البرمجة", "Notion AI وCopilot/Cursor وOllama وDify", "« مخطط 4 أسابيع + برنامج بايثون »"],
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séance 1 :</strong> les 3 règles d'or (vérifier, citer, garder son jugement) s'appliquent aux 4 familles. Et souvenez-vous de l'acteur brillant : convaincant ne veut pas dire vrai — dans AUCUNE famille.",
                        "<strong>🔗 Reminder of session 1:</strong> the 3 golden rules (verify, cite, keep judgement) apply to all 4 families. And remember the brilliant actor: convincing does not mean true — in NO family.",
                        "<strong>🔗 تذكير بالحصة 1:</strong> القواعد الذهبية الثلاث (تحقّق واستشهد وحافظ على حكمك) تنطبق على العائلات الأربع. وتذكّر الممثل البارع: المقنع لا يعني الصحيح — في أي عائلة.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Les 12 outils en fiches express",
                "The 12 tools in flash sheets",
                "الأدوات الاثنتا عشرة في بطاقات سريعة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une phrase par outil, à connaître par cœur. Le détail complet (étapes, forces, limites) est sur la page « Outils IA » du module : chaque outil y a sa fiche.",
                        "One sentence per tool, to know by heart. Full detail (steps, strengths, limits) is on the module's \"AI Tools\" page: each tool has its sheet there.",
                        "جملة لكل أداة تُحفَظ. والتفصيل الكامل (خطوات ومزايا وحدود) في صفحة « أدوات الذكاء » للوحدة: لكل أداة بطاقتها.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>ChatGPT :</strong> l'assistant généraliste qui explique, résume et rédige.",
                            "<strong>Gemini :</strong> comme ChatGPT + lit images et PDF.",
                            "<strong>Claude :</strong> le champion des longs textes en bon français.",
                            "<strong>Perplexity :</strong> répond AVEC les sources à ouvrir.",
                            "<strong>Scholar / Consensus :</strong> la bibliothèque scientifique (articles, consensus).",
                            "<strong>NotebookLM :</strong> interroge VOS propres PDF de cours.",
                            "<strong>Gamma :</strong> transforme un plan en diaporama.",
                            "<strong>Canva IA :</strong> affiches et visuels magnifiques.",
                            "<strong>Copilot / Cursor :</strong> le copilote du programmeur.",
                            "<strong>Notion AI :</strong> notes, plannings et tableaux intelligents.",
                            "<strong>DALL·E :</strong> dessine ce que vous décrivez.",
                            "<strong>ElevenLabs / Whisper :</strong> voix de synthèse et transcription.",
                            "<strong>Ollama :</strong> une IA chez vous, hors-ligne et gratuite.",
                            "<strong>Dify :</strong> votre chatbot sans coder.",
                        ],
                        [
                            "<strong>ChatGPT:</strong> the generalist assistant explaining, summarising, writing.",
                            "<strong>Gemini:</strong> like ChatGPT + reads images and PDFs.",
                            "<strong>Claude:</strong> the champion of long texts in good French.",
                            "<strong>Perplexity:</strong> answers WITH sources to open.",
                            "<strong>Scholar / Consensus:</strong> the scientific library (papers, consensus).",
                            "<strong>NotebookLM:</strong> questions YOUR own course PDFs.",
                            "<strong>Gamma:</strong> turns an outline into slides.",
                            "<strong>Canva AI:</strong> gorgeous posters and visuals.",
                            "<strong>Copilot / Cursor:</strong> the programmer's copilot.",
                            "<strong>Notion AI:</strong> smart notes, schedules and boards.",
                            "<strong>DALL·E:</strong> draws what you describe.",
                            "<strong>ElevenLabs / Whisper:</strong> synthetic voice and transcription.",
                            "<strong>Ollama:</strong> an AI at home, offline and free.",
                            "<strong>Dify:</strong> your chatbot without coding.",
                        ],
                        [
                            "<strong>ChatGPT:</strong> المساعد العام الذي يشرح ويلخّص ويكتب.",
                            "<strong>Gemini:</strong> مثل ChatGPT + يقرأ الصور وPDF.",
                            "<strong>Claude:</strong> بطل النصوص الطويلة بفرنسية جيدة.",
                            "<strong>Perplexity:</strong> يجيب مع مصادر تُفتَح.",
                            "<strong>Scholar / Consensus:</strong> المكتبة العلمية (مقالات وإجماع).",
                            "<strong>NotebookLM:</strong> يستجوب ملفات دروسك الخاصة.",
                            "<strong>Gamma:</strong> يحوّل الخطة إلى شرائح.",
                            "<strong>Canva IA:</strong> ملصقات وصور رائعة.",
                            "<strong>Copilot / Cursor:</strong> مساعد المبرمج.",
                            "<strong>Notion AI:</strong> ملاحظات ومخططات ولوحات ذكية.",
                            "<strong>DALL·E:</strong> يرسم ما تصفه.",
                            "<strong>ElevenLabs / Whisper:</strong> صوت اصطناعي ونسخ.",
                            "<strong>Ollama:</strong> ذكاء عندك دون اتصال ومجاناً.",
                            "<strong>Dify:</strong> روبوتك دون برمجة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce mémoire :</strong> 4 couleurs = 4 familles (🔵🟢🟠🟣). Demandez à un camarade : « cite-moi les 3 outils verts » — celui qui hésite révise la fiche !",
                        "<strong>Memory tip:</strong> 4 colours = 4 families (🔵🟢🟠🟣). Ask a classmate: \"name the 3 green tools\" — whoever hesitates revises the sheet!",
                        "<strong>نصيحة حفظ:</strong> 4 ألوان = 4 عائلات (🔵🟢🟠🟣). اسأل زميلك: « سمِّ الأدوات الخضراء الثلاث » — من يتردد يراجع البطاقة!",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Démo : la même question à 3 outils",
                "Demo: the same question to 3 tools",
                "عرض: نفس السؤال لثلاث أدوات",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Question test : « Explique la différenciation pédagogique avec un exemple de primaire. » Regardez ce que CHAQUE outil apporte — aucun ne fait tout.",
                        "Test question: \"Explain pedagogical differentiation with a primary example.\" Watch what EACH tool brings — none does everything.",
                        "السؤال الاختباري: « اشرح التفريد البيداغوجي بمثال ابتدائي ». لاحظ ما يقدمه كل أداة — لا واحدة تفعل كل شيء.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>ChatGPT (🔵) :</strong> explication claire + exemple, sans sources. Parfait pour COMPRENDRE vite.",
                            "<strong>Perplexity (🟢) :</strong> réponse plus courte MAIS avec 3 liens : parfait pour VÉRIFIER et citer.",
                            "<strong>Canva IA (🟠) :</strong> une affiche « différenciation » pour la classe : parfait pour MONTRER.",
                            "<strong>Leçon :</strong> comprendre → bleu ; prouver → vert ; montrer → orange. Trois outils, trois métiers.",
                        ],
                        [
                            "<strong>ChatGPT (🔵):</strong> clear explanation + example, no sources. Perfect to UNDERSTAND fast.",
                            "<strong>Perplexity (🟢):</strong> shorter answer BUT with 3 links: perfect to CHECK and cite.",
                            "<strong>Canva AI (🟠):</strong> a \"differentiation\" poster for class: perfect to SHOW.",
                            "<strong>Lesson:</strong> understand → blue; prove → green; show → orange. Three tools, three jobs.",
                        ],
                        [
                            "<strong>ChatGPT (🔵):</strong> شرح واضح + مثال، دون مصادر. مثالي للفهم السريع.",
                            "<strong>Perplexity (🟢):</strong> جواب أقصر لكن مع 3 روابط: مثالي للتحقق والاستشهاد.",
                            "<strong>Canva IA (🟠):</strong> ملصق « التفريد » للقسم: مثالي للعرض.",
                            "<strong>العبرة:</strong> للفهم ← أزرق؛ للإثبات ← أخضر؛ للعرض ← برتقالي. ثلاث أدوات وثلاث مهن.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> Karim prépare un exposé sur l'eau : ChatGPT lui donne le plan en 1 minute, Perplexity lui trouve 3 sources datées, Canva lui dessine l'affiche du cycle. Trois pharmaciens, une ordonnance : l'exposé.",
                        "<strong>🧪 Concrete example:</strong> Karim prepares a talk on water: ChatGPT gives the outline in 1 minute, Perplexity finds 3 dated sources, Canva draws the cycle poster. Three pharmacists, one prescription: the talk.",
                        "<strong>🧪 مثال ملموس:</strong> كريم يحضّر عرضاً عن الماء: ChatGPT يعطيه الخطة في دقيقة وPerplexity يجد 3 مصادر مؤرَّخة وCanva يرسم ملصق الدورة. ثلاثة صيادلة ووصفة واحدة: العرض.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Bien choisir : l'arbre de décision du pharmacien",
                "Choose well: the pharmacist's decision tree",
                "أحسِن الاختيار: شجرة قرار الصيدلي",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Trois questions suffisent pour ne plus jamais se tromper d'outil.",
                        "Three questions are enough to never pick the wrong tool again.",
                        "تكفي ثلاثة أسئلة لئلا تخطئ الأداة أبداً.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>1. Ai-je besoin de SOURCES ?</strong> Oui → 🟢 (Perplexity, Scholar). Non → question 2.",
                            "<strong>2. Est-ce que je CRÉE quelque chose à montrer ?</strong> Oui → 🟠 (Gamma, Canva, DALL·E). Non → question 3.",
                            "<strong>3. Est-ce que j'ORGANISE ou je CODE ?</strong> Oui → 🟣 (Notion, Copilot, Ollama, Dify). Non → 🔵 (ChatGPT, Gemini, Claude).",
                        ],
                        [
                            "<strong>1. Do I need SOURCES?</strong> Yes → 🟢 (Perplexity, Scholar). No → question 2.",
                            "<strong>2. Am I CREATING something to show?</strong> Yes → 🟠 (Gamma, Canva, DALL·E). No → question 3.",
                            "<strong>3. Am I ORGANISING or CODING?</strong> Yes → 🟣 (Notion, Copilot, Ollama, Dify). No → 🔵 (ChatGPT, Gemini, Claude).",
                        ],
                        [
                            "<strong>1. هل أحتاج مصادر؟</strong> نعم ← 🟢 (Perplexity وScholar). لا ← السؤال 2.",
                            "<strong>2. هل أُنشئ شيئاً للعرض؟</strong> نعم ← 🟠 (Gamma وCanva وDALL·E). لا ← السؤال 3.",
                            "<strong>3. هل أنظّم أم أبرمج؟</strong> نعم ← 🟣 (Notion وCopilot وOllama وDify). لا ← 🔵 (ChatGPT وGemini وClaude).",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Les 4 composantes d'une bonne requête :</strong> contexte (qui tu es, quel cours), objectif (comprendre, citer, réviser), format (liste, tableau, 5 lignes), contrainte (sources, langue, dates). La démo 2 les applique en direct.",
                        "<strong>The 4 components of a good query:</strong> context (who you are, which course), goal (understand, cite, revise), format (list, table, 5 lines), constraint (sources, language, dates). Demo 2 applies them live.",
                        "<strong>عناصر الصياغة الجيدة الأربعة:</strong> السياق (من أنت وأي درس) والهدف (فهم واستشهاد ومراجعة) والصيغة (قائمة وجدول و5 أسطر) والقيد (مصادر ولغة وتواريخ). العرض 2 يطبّقها مباشرة.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ 3 erreurs de débutant :</strong> 1) tout demander au même outil (le sirop unique) ; 2) croire sans ouvrir les sources ; 3) payer un abonnement avant d'avoir épuisé le gratuit étudiant.",
                        "<strong>❌ 3 beginner mistakes:</strong> 1) asking everything to one tool (the single syrup); 2) believing without opening sources; 3) paying before exhausting free student tiers.",
                        "<strong>❌ 3 أخطاء مبتدئة:</strong> 1) طلب كل شيء من أداة واحدة (الشراب الوحيد)؛ 2) التصديق دون فتح المصادر؛ 3) الدفع قبل استنفاد المجاني الطلابي.",
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
                        "Le bon pharmacien ne connaît pas 12 sirops par cœur le premier jour : il connaît 4 tiroirs, 1 outil préféré par tiroir, et la page « Outils IA » pour le reste.",
                        "The good pharmacist does not memorise 12 syrups on day one: he knows 4 drawers, 1 favourite tool per drawer, and the \"AI Tools\" page for the rest.",
                        "الصيدلي الجيد لا يحفظ 12 شراباً أول يوم: يعرف 4 أدراج وأداة مفضلة لكل درج وصفحة « أدوات الذكاء » للباقي.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 3 :</strong> la famille verte (CHERCHER) mérite une séance entière : Perplexity en profondeur, Scholar comme un chercheur, et l'art de vérifier (séance 3).",
                        "<strong>➡️ Bridge to session 3:</strong> the green family (SEARCH) deserves a whole session: Perplexity in depth, Scholar like a researcher, and the art of checking (session 3).",
                        "<strong>➡️ جسر إلى الحصة 3:</strong> العائلة الخضراء (البحث) تستحق حصة كاملة: Perplexity بعمق وScholar كباحث وفن التحقق (الحصة 3).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ 1 favori par tiroir :</strong> choisissez vos 4 outils de tous les jours cette semaine.",
                            "<strong>✅ Gratuit d'abord :</strong> comptes étudiants gratuits avant tout abonnement.",
                            "<strong>✅ Fiche outils :</strong> gardez la page « Outils IA » en favori du navigateur.",
                            "<strong>✅ Testez à deux :</strong> même question, deux outils, comparez — le meilleur exercice.",
                        ],
                        [
                            "<strong>✅ 1 favourite per drawer:</strong> pick your 4 everyday tools this week.",
                            "<strong>✅ Free first:</strong> free student accounts before any subscription.",
                            "<strong>✅ Tools sheet:</strong> bookmark the \"AI Tools\" page in your browser.",
                            "<strong>✅ Test in pairs:</strong> same question, two tools, compare — the best exercise.",
                        ],
                        [
                            "<strong>✅ مفضلة لكل درج:</strong> اختر أدواتك الأربع اليومية هذا الأسبوع.",
                            "<strong>✅ المجاني أولاً:</strong> حسابات طلابية مجانية قبل أي اشتراك.",
                            "<strong>✅ بطاقة الأدوات:</strong> احفظ صفحة « أدوات الذكاء » في متصفحك.",
                            "<strong>✅ جرّب ثنائياً:</strong> نفس السؤال وأداتان وقارن — أفضل تمرين.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> collectionner 12 comptes qu'on n'ouvre jamais, demander des sources à un outil bleu, demander un poème à un outil vert.",
                        "<strong>❌ Mistakes to avoid:</strong> collecting 12 accounts you never open, asking a blue tool for sources, asking a green tool for a poem.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> جمع 12 حساباً لا تُفتَح أبداً وطلب المصادر من أداة زرقاء وطلب قصيدة من أداة خضراء.",
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
                            ["Demande", "« Fais tout pour mon exposé » à un seul outil.", "« Plan (bleu) + sources (vert) + affiche (orange) » : 3 outils, 3 métiers."],
                            ["Résultat", "Un seul sirop pour tous les maux.", "Le bon flacon pour chaque symptôme."],
                        ],
                        [
                            ["Prompt", "\"Do everything for my talk\" to a single tool.", "\"Outline (blue) + sources (green) + poster (orange)\": 3 tools, 3 jobs."],
                            ["Result", "One syrup for all ills.", "The right bottle for each symptom."],
                        ],
                        [
                            ["الطلب", "« افعل كل شيء لعرضي » لأداة واحدة.", "« خطة (أزرق) + مصادر (أخضر) + ملصق (برتقالي) »: 3 أدوات و3 مهن."],
                            ["النتيجة", "شراب واحد لكل الأدواء.", "القارورة المناسبة لكل عرَض."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Que faire si vous avez besoin de SOURCES ?",
                "What to do if you need SOURCES?",
                "ماذا تفعل إذا احتجت مصادر؟",
            ),
            "r": L(
                "Tiroir vert : Perplexity pour une réponse sourcée rapide, Scholar/Consensus pour des articles vérifiables.",
                "Green drawer: Perplexity for a fast sourced answer, Scholar/Consensus for verifiable papers.",
                "الدرج الأخضر: Perplexity لجواب مسنَد سريع وScholar/Consensus لمقالات قابلة للتحقق.",
            ),
        },
        {
            "q": L(
                "NotebookLM appartient à quelle famille, et pourquoi ?",
                "Which family is NotebookLM in, and why?",
                "إلى أي عائلة ينتمي NotebookLM ولماذا؟",
            ),
            "r": L(
                "CHERCHER (vert) : il répond à partir de VOS documents, sources affichées — c'est un moteur sur vos PDF.",
                "SEARCH (green): it answers from YOUR documents, sources shown — an engine over your PDFs.",
                "البحث (أخضر): يجيب من وثائقك مع عرض المصادر — محرّك فوق ملفاتك.",
            ),
        },
        {
            "q": L(
                "Ollama et Dify : quelle différence en une phrase ?",
                "Ollama and Dify: what difference in one sentence?",
                "Ollama وDify: ما الفرق في جملة؟",
            ),
            "r": L(
                "Ollama fait tourner un modèle chez vous hors-ligne ; Dify construit un chatbot sur vos PDF sans coder.",
                "Ollama runs a model at home offline; Dify builds a chatbot on your PDFs without coding.",
                "يشغّل Ollama نموذجاً عندك دون اتصال؛ ويبني Dify روبوتاً على ملفاتك دون برمجة.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "8 situations d'étudiant : prescrivez le bon outil avec l'arbre de décision (sources ? créer ? organiser-coder ?). Justifiez en 1 phrase.",
            "8 student situations: prescribe the right tool with the decision tree (sources? create? organise-code?). Justify in 1 sentence.",
            "8 حالات طلابية: اصرف الأداة المناسبة بشجرة القرار (مصادر؟ إنشاء؟ تنظيم-برمجة؟). برّر في جملة.",
        ),
        "demarche": L(
            "1) Lire la situation. 2) Poser les 3 questions de l'arbre dans l'ordre. 3) Nommer l'outil + la famille (couleur). 4) Comparer avec le voisin avant correction.",
            "1) Read the situation. 2) Ask the tree's 3 questions in order. 3) Name the tool + family (colour). 4) Compare with neighbour before correction.",
            "1) اقرأ الحالة. 2) اطرح أسئلة الشجرة الثلاثة بالترتيب. 3) سمِّ الأداة + العائلة (اللون). 4) قارن مع الجار قبل التصحيح.",
        ),
        "solution": L(
            "1) Expliquer une notion → 🔵 ChatGPT. 2) Citer 2 études → 🟢 Perplexity/Scholar. 3) Slides d'exposé → 🟠 Gamma. 4) Affiche → 🟠 Canva. 5) Planning révisions → 🟣 Notion. 6) Bug Python → 🟣 Copilot. 7) Résumer VOS PDF → 🟢 NotebookLM. 8) Chatbot sans code → 🟣 Dify.",
            "1) Explain a notion → 🔵 ChatGPT. 2) Cite 2 studies → 🟢 Perplexity/Scholar. 3) Talk slides → 🟠 Gamma. 4) Poster → 🟠 Canva. 5) Revision plan → 🟣 Notion. 6) Python bug → 🟣 Copilot. 7) Summarise YOUR PDFs → 🟢 NotebookLM. 8) No-code chatbot → 🟣 Dify.",
            "1) شرح مفهوم ← 🔵 ChatGPT. 2) الاستشهاد بدراستين ← 🟢 Perplexity/Scholar. 3) شرائح عرض ← 🟠 Gamma. 4) ملصق ← 🟠 Canva. 5) مخطط مراجعات ← 🟣 Notion. 6) خطأ بايثون ← 🟣 Copilot. 7) تلخيص ملفاتك ← 🟢 NotebookLM. 8) روبوت دون كود ← 🟣 Dify.",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Playlist IA de Mohammad Dawoud (référence du module)",
                "Mohammad Dawoud's AI playlist (module reference)",
                "سلسلة محمد داود في الذكاء الاصطناعي (مرجع الوحدة)",
            ),
            "url": "https://www.youtube.com/watch?v=H5WUwwivEaI&list=PLbR_CTcUs1088jfqbbO5AqwODO9MgYA85",
            "langue": "ar",
            "concept": L(
                "Comprendre ce qu'il y a SOUS les outils : introduction, ML, réseaux de neurones.",
                "Understand what is UNDER the tools: intro, ML, neural networks.",
                "فهم ما تحت الأدوات: مدخل وتعلم آلي وشبكات عصبية.",
            ),
        },
        {
            "titre": L(
                "Comparatif assistants IA 2026 : lequel choisir ?",
                "2026 AI assistants compared: which to pick?",
                "مقارنة مساعدي الذكاء 2026: أيها تختار؟",
            ),
            "url": "https://www.youtube.com/results?search_query=comparatif+chatgpt+gemini+claude+2026+francais",
            "langue": "fr",
            "concept": L(
                "Voir les différences bleu contre bleu avant de choisir votre favori.",
                "See blue-vs-blue differences before picking your favourite.",
                "شاهد فروق الأزرق ضد الأزرق قبل اختيار مفضّلتك.",
            ),
        },
        {
            "titre": L(
                "10 outils IA pour étudiants : panorama guidé",
                "10 AI tools for students: guided tour",
                "10 أدوات ذكاء للطلبة: جولة موجّهة",
            ),
            "url": "https://www.youtube.com/results?search_query=outils+ia+etudiants+universite+tutoriel",
            "langue": "fr",
            "concept": L(
                "Le panorama en vidéo : quand passer du tiroir bleu au vert puis à l'orange.",
                "The panorama on video: when to move from blue to green to orange drawer.",
                "النظرة العامة بالفيديو: متى تنتقل من الدرج الأزرق إلى الأخضر ثم البرتقالي.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "4 tiroirs : 🔵 comprendre, 🟢 chercher, 🟠 créer, 🟣 organiser-coder.",
                "4 drawers: 🔵 understand, 🟢 search, 🟠 create, 🟣 organise-code.",
                "4 أدراج: 🔵 الفهم و🟢 البحث و🟠 الإنشاء و🟣 التنظيم-البرمجة.",
            ),
            L(
                "Arbre : sources ? → créer ? → organiser-coder ? → sinon bleu.",
                "Tree: sources? → create? → organise-code? → else blue.",
                "الشجرة: مصادر؟ ← إنشاء؟ ← تنظيم-برمجة؟ ← وإلا أزرق.",
            ),
            L(
                "1 favori par tiroir + page Outils IA en favori.",
                "1 favourite per drawer + AI Tools page bookmarked.",
                "مفضلة لكل درج + صفحة أدوات الذكاء محفوظة.",
            ),
            L(
                "Gratuit étudiant d'abord, jamais d'abonnement aveugle.",
                "Student free first, never a blind subscription.",
                "المجاني الطلابي أولاً ولا اشتراك أعمى أبداً.",
            ),
            L(
                "3 règles d'or partout : vérifier, citer, juger.",
                "3 golden rules everywhere: verify, cite, judge.",
                "القواعد الذهبية الثلاث دائماً: تحقّق واستشهد واحكم.",
            ),
        ],
        "analogies": [
            L(
                "La pharmacie : l'ordonnance (tâche) désigne le flacon (outil).",
                "The pharmacy: the prescription (task) points to the bottle (tool).",
                "الصيدلية: الوصفة (المهمة) تدل على القارورة (الأداة).",
            ),
            L(
                "Les 4 tiroirs valent mieux que 12 noms en vrac.",
                "4 drawers beat 12 loose names.",
                "4 أدراج خير من 12 اسماً مبعثراً.",
            ),
            L(
                "Le sirop unique : l'erreur du débutant pressé.",
                "The single syrup: the rushed beginner's mistake.",
                "الشراب الوحيد: خطأ المبتدئ المستعجل.",
            ),
        ],
        "exemples": [
            L(
                "Exposé eau : plan (bleu) + sources (vert) + affiche (orange).",
                "Water talk: outline (blue) + sources (green) + poster (orange).",
                "عرض الماء: خطة (أزرق) + مصادر (أخضر) + ملصق (برتقالي).",
            ),
            L(
                "« Différenciation » : ChatGPT explique, Perplexity prouve, Canva montre.",
                "\"Differentiation\": ChatGPT explains, Perplexity proves, Canva shows.",
                "« التفريد »: ChatGPT يشرح وPerplexity يثبت وCanva يعرض.",
            ),
            L(
                "Planning + bug + PDF : Notion, Copilot, NotebookLM (violet et vert).",
                "Schedule + bug + PDFs: Notion, Copilot, NotebookLM (purple and green).",
                "مخطط + خطأ + ملفات: Notion وCopilot وNotebookLM (بنفسجي وأخضر).",
            ),
        ],
        "analogie_finale": L(
            "🏁 Les outils d'IA et vous, c'est comme l'orchestre et le chef : chaque instrument (outil) a son timbre, mais c'est le chef (vous, et votre arbre de décision) qui décide qui joue, quand — et la musique, c'est vos études.",
            "🏁 AI tools and you is like orchestra and conductor: each instrument (tool) has its tone, but the conductor (you, and your decision tree) decides who plays, when — and the music is your studies.",
            "🏁 أدوات الذكاء وأنت كالأوركسترا والقائد: لكل آلة (أداة) صوتها، لكن القائد (أنت وشجرة قرارك) يقرّر من يعزف ومتى — والموسيقى دراستك.",
        ),
        "quiz": [
            {
                "q": L(
                    "Besoin de SOURCES : quel tiroir ?",
                    "Need SOURCES: which drawer?",
                    "تحتاج مصادر: أي درج؟",
                ),
                "options": L(
                    ["🔵 Bleu", "🟢 Vert (Perplexity, Scholar)", "🟠 Orange", "🟣 Violet"],
                    ["🔵 Blue", "🟢 Green (Perplexity, Scholar)", "🟠 Orange", "🟣 Purple"],
                    ["🔵 أزرق", "🟢 أخضر (Perplexity وScholar)", "🟠 برتقالي", "🟣 بنفسجي"],
                ),
                "answer": 1,
                "exp": L(
                    "Sources = tiroir vert : Perplexity pour vite, Scholar pour citer des articles.",
                    "Sources = green drawer: Perplexity for fast, Scholar to cite papers.",
                    "المصادر = الدرج الأخضر: Perplexity للسرعة وScholar للاستشهاد بمقالات.",
                ),
            },
            {
                "q": L(
                    "Slides d'exposé : quel outil ?",
                    "Talk slides: which tool?",
                    "شرائح العرض: أي أداة؟",
                ),
                "options": L(
                    ["Ollama", "Perplexity", "Gamma (créer à montrer)", "Whisper"],
                    ["Ollama", "Perplexity", "Gamma (create to show)", "Whisper"],
                    ["Ollama", "Perplexity", "Gamma (إنشاء للعرض)", "Whisper"],
                ),
                "answer": 2,
                "exp": L(
                    "Créer à montrer = tiroir orange : Gamma transforme un plan en diaporama.",
                    "Create to show = orange drawer: Gamma turns an outline into slides.",
                    "الإنشاء للعرض = الدرج البرتقالي: يحوّل Gamma الخطة إلى شرائح.",
                ),
            },
            {
                "q": L(
                    "Interroger VOS propres PDF : quel outil ?",
                    "Question YOUR own PDFs: which tool?",
                    "استجواب ملفاتك الخاصة: أي أداة؟",
                ),
                "options": L(
                    ["DALL·E", "NotebookLM (vert : chercher dans vos documents)", "Canva", "ElevenLabs"],
                    ["DALL·E", "NotebookLM (green: search your documents)", "Canva", "ElevenLabs"],
                    ["DALL·E", "NotebookLM (أخضر: البحث في وثائقك)", "Canva", "ElevenLabs"],
                ),
                "answer": 1,
                "exp": L(
                    "NotebookLM répond depuis VOS fichiers avec sources : le moteur de vos cours.",
                    "NotebookLM answers from YOUR files with sources: your lessons' engine.",
                    "يجيب NotebookLM من ملفاتك مع المصادر: محرّك دروسك.",
                ),
            },
            {
                "q": L(
                    "Réviser sans connexion dans le bus : quelle solution ?",
                    "Revise offline on the bus: which solution?",
                    "مراجعة دون اتصال في الحافلة: أي حل؟",
                ),
                "options": L(
                    ["ChatGPT en ligne", "Ollama en local (violet : gratuit, privé, hors-ligne)", "Gamma", "Perplexity"],
                    ["Online ChatGPT", "Local Ollama (purple: free, private, offline)", "Gamma", "Perplexity"],
                    ["ChatGPT متصل", "Ollama محلياً (بنفسجي: مجاني وخاص ودون اتصال)", "Gamma", "Perplexity"],
                ),
                "answer": 1,
                "exp": L(
                    "Ollama fait tourner un modèle sur votre PC : gratuit, privé, sans Internet.",
                    "Ollama runs a model on your PC: free, private, no Internet.",
                    "يشغّل Ollama نموذجاً على جهازك: مجاني وخاص ودون إنترنت.",
                ),
            },
            {
                "q": L(
                    "Chatbot sur vos fiches SANS coder : quel outil ?",
                    "Chatbot on your sheets WITHOUT coding: which tool?",
                    "روبوت على بطاقاتك دون برمجة: أي أداة؟",
                ),
                "options": L(
                    ["Python", "Dify (violet : no-code sur vos PDF)", "Ollama", "Scholar"],
                    ["Python", "Dify (purple: no-code on your PDFs)", "Ollama", "Scholar"],
                    ["بايثون", "Dify (بنفسجي: دون كود على ملفاتك)", "Ollama", "Scholar"],
                ),
                "answer": 1,
                "exp": L(
                    "Dify = voie no-code : compte, Knowledge, PDF importé, publier (séance 10).",
                    "Dify = no-code path: account, Knowledge, imported PDF, publish (session 10).",
                    "Dify = مسار دون كود: حساب ومعرفة وملف مستورَد ونشر (الحصة 10).",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Ordonnance express : 8 situations → outil + famille + 1 phrase de justification.",
            "Express prescription: 8 situations → tool + family + 1 justification sentence.",
            "وصفة سريعة: 8 حالات ← أداة + عائلة + جملة تبرير.",
        ),
        L(
            "Duel d'outils : même question à 2 outils de familles différentes, comparer en tableau.",
            "Tool duel: same question to 2 tools from different families, compare in a table.",
            "مبارزة أدوات: نفس السؤال لأداتين من عائلتين وقارن في جدول.",
        ),
        L(
            "Mes 4 favoris : choisir 1 outil par tiroir et justifier devant la classe.",
            "My 4 favourites: pick 1 tool per drawer and justify in class.",
            "مفضلاتي الأربع: اختر أداة لكل درج وبرّر أمام القسم.",
        ),
        L(
            "Chasse à l'erreur : 3 prescriptions volontairement fausses à corriger (ex : sources → DALL·E).",
            "Mistake hunt: 3 deliberately wrong prescriptions to fix (e.g. sources → DALL·E).",
            "صيد الأخطاء: 3 وصفات خاطئة عمداً للتصحيح (مثال: مصادر ← DALL·E).",
        ),
    ],
    "retenir": [
        L(
            "4 tiroirs : 🔵🟢🟠🟣 valent mieux que 12 noms.",
            "4 drawers: 🔵🟢🟠🟣 beat 12 names.",
            "4 أدراج: 🔵🟢🟠🟣 خير من 12 اسماً.",
        ),
        L(
            "Arbre : sources ? créer ? organiser-coder ? sinon bleu.",
            "Tree: sources? create? organise-code? else blue.",
            "الشجرة: مصادر؟ إنشاء؟ تنظيم-برمجة؟ وإلا أزرق.",
        ),
        L(
            "Démo : même question, 3 outils, 3 métiers.",
            "Demo: same question, 3 tools, 3 jobs.",
            "العرض: نفس السؤال و3 أدوات و3 مهن.",
        ),
        L(
            "Gratuit étudiant d'abord ; 3 règles d'or partout.",
            "Student free first; 3 golden rules everywhere.",
            "المجاني الطلابي أولاً؛ والقواعد الذهبية دائماً.",
        ),
        L(
            "Page Outils IA en favori : la pharmacie de poche.",
            "AI Tools page bookmarked: the pocket pharmacy.",
            "صفحة أدوات الذكاء محفوظة: الصيدلية الجيبية.",
        ),
    ],
    "glossaire": [
        {
            "term": "Famille d'outils",
            "term_en": "Tool family",
            "def_fr": "Regroupement par besoin : comprendre, chercher, créer, organiser-coder.",
            "def_en": "Grouping by need: understand, search, create, organise-code.",
            "def_ar": "تجميع حسب الحاجة: الفهم والبحث والإنشاء والتنظيم-البرمجة.",
        },
        {
            "term": "Moteur sourcé",
            "term_en": "Sourced engine",
            "def_fr": "Outil qui répond en affichant ses sources (Perplexity, Consensus).",
            "def_en": "A tool answering while showing its sources (Perplexity, Consensus).",
            "def_ar": "أداة تجيب عارضة مصادرها (Perplexity وConsensus).",
        },
        {
            "term": "Arbre de décision",
            "term_en": "Decision tree",
            "def_fr": "3 questions (sources ? créer ? organiser ?) pour choisir le bon outil.",
            "def_en": "3 questions (sources? create? organise?) to pick the right tool.",
            "def_ar": "3 أسئلة (مصادر؟ إنشاء؟ تنظيم؟) لاختيار الأداة المناسبة.",
        },
        {
            "term": "Version gratuite",
            "term_en": "Free tier",
            "def_fr": "Offre gratuite (souvent étudiante) à épuiser avant tout abonnement.",
            "def_en": "Free (often student) offer to exhaust before any subscription.",
            "def_ar": "عرض مجاني (طلابي غالباً) يُستنفَد قبل أي اشتراك.",
        },
        {
            "term": "Fiche express",
            "term_en": "Flash sheet",
            "def_fr": "Résumé d'un outil en une phrase : usage + limite.",
            "def_en": "A one-sentence tool summary: use + limit.",
            "def_ar": "ملخص أداة في جملة: استعمال + حد.",
        },
    ],
    "dialogues_fr": """# Séance 02 — Dialogues pédagogiques (Français)

## Dialogue A — « Docteur, quel sirop ? » (25 min)

**Personnages :** Sara (étudiante perdue), Karim (camarade pharmacien), Mme Amel (enseignante).

---

Sara : Douze outils… Je suis perdue ! Pour mon exposé sur l'eau, je prends lequel ?

Karim : Calme-toi, future pharmacienne. D'abord l'ordonnance : que dois-tu FAIRE ? Un plan ? Des sources ? Une affiche ?

Sara : Les trois ! Un plan, des preuves et quelque chose à montrer.

Karim : Alors trois flacons : 🔵 ChatGPT pour le plan (comprendre), 🟢 Perplexity pour les sources datées (chercher), 🟠 Canva pour l'affiche du cycle (créer).

Sara : Et si je demandais tout à ChatGPT ?

Karim : Le sirop unique ! Il inventerait des sources et dessinerait mal. Chaque famille a son métier.

Mme Amel : Exactement. Et les 3 règles d'or de la séance 1 (vérifier, citer, juger) s'appliquent aux 4 tiroirs. Rangez d'abord, prescrivez ensuite.

---

## Dialogue B — « Le duel » (15 min)

**Personnages :** Yacine (étudiant), Lina (camarade arbitre), l'écran (joué par un camarade).

---

Yacine : « Explique la photosynthèse » : ChatGPT répond en 10 lignes claires. Perplexity répond en 5 lignes + 3 liens. Lequel gagne ?

Lina : Ça dépend du match ! Pour COMPRENDRE vite : ChatGPT. Pour CITER dans ton devoir : Perplexity, avec les liens ouverts.

Yacine : Et Canva dans tout ça ?

Lina : Il ne joue pas le même match : il MONTRERA ta photosynthèse en affiche. Trois outils, trois métiers, un seul exposé.

Yacine : Donc je ne choisis plus UN outil, je compose une ÉQUIPE ?

Lina : Voilà le pharmacien : bleu + vert + orange, et l'ordonnance est remplie !

---

## Mini-rôle à jouer (3 min par binôme)
L'un énonce une situation (« résumer MES pdf », « bug Python », « affiche A3 »), l'autre prescrit outil + famille + 1 phrase. Échangez, puis le jury vérifie avec l'arbre de décision.
""",
    "dialogues_en": """# Session 02 — Classroom dialogues (English)

## Dialogue A — "Doctor, which syrup?" (25 min)

**Characters:** Sara (a lost student), Karim (a pharmacist classmate), Mrs Amel (teacher).

---

Sara: Twelve tools… I am lost! For my talk on water, which one do I take?

Karim: Calm down, future pharmacist. First the prescription: what must you DO? An outline? Sources? A poster?

Sara: All three! An outline, proofs and something to show.

Karim: Then three bottles: 🔵 ChatGPT for the outline (understand), 🟢 Perplexity for dated sources (search), 🟠 Canva for the cycle poster (create).

Sara: And if I asked everything to ChatGPT?

Karim: The single syrup! It would invent sources and draw badly. Each family has its job.

Mrs Amel: Exactly. And session 1's 3 golden rules (verify, cite, judge) apply to all 4 drawers. Sort first, prescribe next.

---

## Dialogue B — "The duel" (15 min)

**Characters:** Yacine (student), Lina (referee classmate), the screen (played by a classmate).

---

Yacine: "Explain photosynthesis": ChatGPT answers in 10 clear lines. Perplexity answers in 5 lines + 3 links. Which wins?

Lina: Depends on the match! To UNDERSTAND fast: ChatGPT. To CITE in your homework: Perplexity, with open links.

Yacine: And Canva in all this?

Lina: It plays another match: it will SHOW your photosynthesis as a poster. Three tools, three jobs, one talk.

Yacine: So I no longer pick ONE tool, I build a TEAM?

Lina: There is the pharmacist: blue + green + orange, and the prescription is filled!

---

## Mini role-play (3 min per pair)
One states a situation ("summarise MY pdfs", "Python bug", "A3 poster"), the other prescribes tool + family + 1 sentence. Swap, then the jury checks with the decision tree.
""",
}
