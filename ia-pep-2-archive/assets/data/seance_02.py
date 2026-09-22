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
        "Ouvrir Perplexity sans compte, tester 3 outils de 3 familles sur la même question, prescrire le bon outil avec l'arbre de décision et repartir avec tes 4 favoris.",
        "Open Perplexity with no account, test 3 tools from 3 families on the same question, prescribe the right tool with the decision tree and leave with your 4 favourites.",
        "افتح Perplexity دون حساب وجرّب 3 أدوات من 3 عائلات على نفس السؤال واصرف الأداة المناسبة بشجرة القرار واخرج بمفضلاتك الأربع.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Ouvrir Perplexity sans créer de compte et y poser ta première question sourcée.",
            "Open Perplexity with no account and ask your first sourced question there.",
            "أن تفتح Perplexity دون إنشاء حساب وتطرح أول سؤال بمصادر.",
        ),
        L(
            "Tester 3 outils (ChatGPT, Perplexity, Canva) sur la même question et comparer.",
            "Test 3 tools (ChatGPT, Perplexity, Canva) on the same question and compare.",
            "أن تجرّب 3 أدوات (ChatGPT وPerplexity وCanva) على نفس السؤال وتقارن.",
        ),
        L(
            "Prescrire le bon outil pour 3 situations avec l'arbre de décision.",
            "Prescribe the right tool for 3 situations with the decision tree.",
            "أن تصرف الأداة المناسبة لثلاث حالات بشجرة القرار.",
        ),
        L(
            "Choisir tes 4 outils favoris (1 par famille) et justifier chaque choix.",
            "Pick your 4 favourite tools (1 per family) and justify each pick.",
            "أن تختار أدواتك الأربع المفضلة (واحدة لكل عائلة) وتبرّر كل اختيار.",
        ),
        L(
            "Éviter les 3 erreurs de débutant : sirop unique, confiance aveugle, abonnement aveugle.",
            "Avoid 3 beginner mistakes: single syrup, blind trust, blind subscription.",
            "أن تتجنّب 3 أخطاء مبتدئة: الشراب الوحيد والثقة العمياء والاشتراك الأعمى.",
        ),
    ],
    "prerequis": L(
        "Séance 1 suivie. Savoir ouvrir un navigateur et avoir (si possible) un compte gratuit sur un outil d'IA.",
        "Session 1 completed. Know how to open a browser and, if possible, have a free account on an AI tool.",
        "إتمام الحصة الأولى. معرفة فتح متصفّح، وإن أمكن امتلاك حساب مجاني على أداة ذكاء اصطناعي.",
    ),
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "🚀 Action immédiate : Perplexity sans compte",
                "🚀 Instant action: Perplexity with no account",
                "🚀 إجراء فوري: Perplexity دون حساب",
            ),
            "detail": L(
                "Ouvrir perplexity.ai, taper le prompt prêt, observer les sources, cliquer 1 lien.",
                "Open perplexity.ai, type the ready prompt, watch the sources, click 1 link.",
                "افتح perplexity.ai واكتب الصياغة الجاهزة ولاحظ المصادر وانقر رابطاً.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "📋 Recette : tester 3 outils sur 1 question",
                "📋 Recipe: test 3 tools on 1 question",
                "📋 وصفة: تجربة 3 أدوات على سؤال واحد",
            ),
            "detail": L(
                "ChatGPT, Perplexity, Canva : même question, 3 réponses, tableau comparatif.",
                "ChatGPT, Perplexity, Canva: same question, 3 answers, comparison table.",
                "ChatGPT وPerplexity وCanva: نفس السؤال و3 أجوبة وجدول مقارنة.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "🛠️ Démo : l'arbre de décision du pharmacien",
                "🛠️ Demo: the pharmacist's decision tree",
                "🛠️ عرض: شجرة قرار الصيدلي",
            ),
            "detail": L(
                "3 questions (sources ? créer ? organiser ?) + 4 composantes d'une bonne requête.",
                "3 questions (sources? create? organise?) + 4 components of a good query.",
                "3 أسئلة (مصادر؟ إنشاء؟ تنظيم؟) + عناصر الصياغة الجيدة الأربعة.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "🧪 Mission : tableau comparatif + 4 favoris",
                "🧪 Mission: comparison table + 4 favourites",
                "🧪 المهمة: جدول مقارنة + 4 مفضلات",
            ),
            "detail": L(
                "Livrable : 1 question testée sur 3 outils + verdict + tes 4 favoris justifiés.",
                "Deliverable: 1 question tested on 3 tools + verdict + your 4 justified favourites.",
                "المطلوب: سؤال مجرَّب على 3 أدوات + حكم + مفضلاتك الأربع مبرَّرة.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "⚠️ Erreurs : sirop unique et confiance aveugle",
                "⚠️ Mistakes: single syrup and blind trust",
                "⚠️ أخطاء: الشراب الوحيد والثقة العمياء",
            ),
            "detail": L(
                "3 erreurs en direct + mauvais vs bon prompt : le fossé sous vos yeux.",
                "3 mistakes live + bad vs good prompt: the gap before your eyes.",
                "3 أخطاء مباشرة + صياغة ضعيفة مقابل قوية: الهوة أمام أعينكم.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "✅ Checklist, quiz et annonce de la séance 3",
                "✅ Checklist, quiz and preview of session 3",
                "✅ قائمة تحقق واختبار وتقديم الحصة الثالثة",
            ),
            "detail": L(
                "Cocher les 4 cases + quiz de 5 questions. Annonce : la recherche approfondie (séance 3).",
                "Tick the 4 boxes + 5-question quiz. Preview: deep research (session 3).",
                "علّم الخانات الأربع + اختبار 5 أسئلة. تقديم: البحث المعمَّق (الحصة 3).",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "🎯 Ce que vous saurez faire à la fin",
                "🎯 What you will be able to do by the end",
                "🎯 ما ستعرف فعله في النهاية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Aujourd'hui, pas de théorie : tu vas TOUCHER à 3 outils. Voici les 3 résultats concrets de la séance.",
                        "Today, no theory: you will TOUCH 3 tools. Here are the 3 concrete results of the session.",
                        "اليوم لا نظرية: ستلمس 3 أدوات. هذه النتائج الملموسة الثلاث للحصة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1.</strong> Ouvrir Perplexity SANS compte et obtenir une réponse avec des sources cliquables.",
                            "<strong>2.</strong> Tester la même question sur 3 outils (ChatGPT, Perplexity, Canva) et dire lequel fait quoi.",
                            "<strong>3.</strong> Repartir avec tes 4 outils favoris (1 par famille), chacun justifié en 1 phrase.",
                        ],
                        [
                            "<strong>1.</strong> Open Perplexity with NO account and get an answer with clickable sources.",
                            "<strong>2.</strong> Test the same question on 3 tools (ChatGPT, Perplexity, Canva) and say which does what.",
                            "<strong>3.</strong> Leave with your 4 favourite tools (1 per family), each justified in 1 sentence.",
                        ],
                        [
                            "<strong>1.</strong> فتح Perplexity دون حساب والحصول على جواب بمصادر قابلة للنقر.",
                            "<strong>2.</strong> تجربة نفس السؤال على 3 أدوات (ChatGPT وPerplexity وCanva) وقول ماذا تفعل كل منها.",
                            "<strong>3.</strong> المغادرة بأدواتك الأربع المفضلة (واحدة لكل عائلة) مبرَّرة كل منها بجملة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séance 1 :</strong> tu sais déjà poser une question et juger une réponse (clair/confus). Aujourd'hui, tu apprends OÙ la poser : le bon tiroir pour chaque besoin.",
                        "<strong>🔗 Reminder of session 1:</strong> you already ask a question and judge an answer (clear/confusing). Today, you learn WHERE to ask it: the right drawer per need.",
                        "<strong>🔗 تذكير بالحصة 1:</strong> تعرف طرح سؤال والحكم على جواب (واضح/مربك). اليوم تتعلم أين تطرحه: الدرج المناسب لكل حاجة.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "🚀 Action immédiate — Perplexity sans compte (5 minutes)",
                "🚀 Instant action — Perplexity with no account (5 minutes)",
                "🚀 إجراء فوري — Perplexity دون حساب (5 دقائق)",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Bonne nouvelle : Perplexity marche SANS inscription. En 5 minutes, tu obtiendras ta première réponse SOURCÉE.",
                        "Good news: Perplexity works with NO signup. In 5 minutes, you will get your first SOURCED answer.",
                        "خبر سار: يعمل Perplexity دون تسجيل. في 5 دقائق ستحصل على أول جواب بمصادر.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Ouvre</strong> perplexity.ai (téléphone ou PC). Pas de compte, pas de mot de passe : la barre est devant toi.",
                            "<strong>Copie-colle EXACTEMENT</strong> le prompt ci-dessous et envoie.",
                            "<strong>Observe :</strong> la réponse arrive AVEC des petits numéros [1][2][3]. Ce sont des sources cliquables — ChatGPT ne fait pas ça.",
                            "<strong>Clique</strong> sur la source [1] : elle s'ouvre. Vrai article ou page web ? Note-le.",
                            "<strong>Note</strong> sur papier : la réponse + le titre de la source ouverte.",
                        ],
                        [
                            "<strong>Open</strong> perplexity.ai (phone or PC). No account, no password: the bar is in front of you.",
                            "<strong>Copy-paste EXACTLY</strong> the prompt below and send.",
                            "<strong>Watch:</strong> the answer comes WITH small numbers [1][2][3]. These are clickable sources — ChatGPT does not do that.",
                            "<strong>Click</strong> source [1]: it opens. Real paper or web page? Note it.",
                            "<strong>Write down:</strong> the answer + the opened source title.",
                        ],
                        [
                            "<strong>افتح</strong> perplexity.ai (هاتف أو حاسوب). لا حساب ولا كلمة مرور: الشريط أمامك.",
                            "<strong>انسخ والصق حرفياً</strong> الصياغة أدناه وأرسل.",
                            "<strong>لاحظ:</strong> يصل الجواب مع أرقام صغيرة [1][2][3]. هذه مصادر قابلة للنقر — ChatGPT لا يفعل ذلك.",
                            "<strong>انقر</strong> المصدر [1]: سيُفتَح. مقال حقيقي أم صفحة ويب؟ سجّله.",
                            "<strong>دوّن:</strong> الجواب + عنوان المصدر المفتوح.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Quelle est la différence entre l'IA faible et l'IA générale ? Donne 3 exemples concrets pour chacune.",
                    "en": "What is the difference between narrow AI and general AI? Give 3 concrete examples of each.",
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>✅ Résultat attendu :</strong> une réponse courte + 2 à 4 sources numérotées en bas. Clique : au moins 1 lien doit s'ouvrir sur une vraie page. Sinon, repose la question mot pour mot.",
                        "<strong>✅ Expected result:</strong> a short answer + 2 to 4 numbered sources below. Click: at least 1 link must open a real page. Else, ask again word for word.",
                        "<strong>✅ النتيجة المنتظرة:</strong> جواب قصير + 2 إلى 4 مصادر مرقمة أسفل. انقر: رابط واحد على الأقل يجب أن يفتح صفحة حقيقية. وإلا أعد السؤال حرفياً.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "📋 Recette : 3 outils, 1 question, 1 verdict",
                "📋 Recipe: 3 tools, 1 question, 1 verdict",
                "📋 وصفة: 3 أدوات وسؤال واحد وحكم واحد",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Étape 0 — range d'abord : 4 tiroirs, pas 12 noms. Devant chaque tâche : COMPRENDRE, CHERCHER, CRÉER ou ORGANISER-CODER ? Le tiroir désigne l'outil.",
                        "Step 0 — sort first: 4 drawers, not 12 names. Before each task: UNDERSTAND, SEARCH, CREATE or ORGANISE-CODE? The drawer points to the tool.",
                        "الخطوة 0 — رتّب أولاً: 4 أدراج لا 12 اسماً. أمام كل مهمة: فهم أم بحث أم إنشاء أم تنظيم-برمجة؟ الدرج يدل على الأداة.",
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
                    "t": "p",
                    **L(
                        "Détail complet de chaque outil sur la page « Outils IA » du module. Maintenant, teste : même question, 3 outils, 1 verdict.",
                        "Full detail of each tool on the module's \"AI Tools\" page. Now test: same question, 3 tools, 1 verdict.",
                        "التفصيل الكامل لكل أداة في صفحة « أدوات الذكاء ». الآن جرّب: نفس السؤال و3 أدوات وحكم واحد.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>ChatGPT (🔵) :</strong> colle le prompt A ci-dessous → note : explication claire ? exemple donné ? sources ? (réponse attendue : non).",
                            "<strong>Perplexity (🟢) :</strong> colle le MÊME prompt A → note : réponse plus courte ? liens [1][2] présents ? Ouvre-en 1.",
                            "<strong>Canva (🟠, démo projetée) :</strong> suis l'enseignant : canva.com → « Magic Design » → décris « affiche différenciation, style dessin animé » → observe le résultat.",
                            "<strong>Verdict :</strong> remplis 1 ligne par outil : COMPRENDRE / PROUVER / MONTRER. Quel outil pour quel métier ?",
                        ],
                        [
                            "<strong>ChatGPT (🔵):</strong> paste prompt A below → note: clear explanation? example given? sources? (expected: no).",
                            "<strong>Perplexity (🟢):</strong> paste the SAME prompt A → note: shorter answer? [1][2] links present? Open 1.",
                            "<strong>Canva (🟠, projected demo):</strong> follow the teacher: canva.com → \"Magic Design\" → describe \"differentiation poster, cartoon style\" → watch the result.",
                            "<strong>Verdict:</strong> fill 1 line per tool: UNDERSTAND / PROVE / SHOW. Which tool for which job?",
                        ],
                        [
                            "<strong>ChatGPT (🔵):</strong> الصق الصياغة A أدناه ← لاحظ: شرح واضح؟ مثال؟ مصادر؟ (المنتظر: لا).",
                            "<strong>Perplexity (🟢):</strong> الصق نفس الصياغة A ← لاحظ: جواب أقصر؟ روابط [1][2] موجودة؟ افتح واحداً.",
                            "<strong>Canva (🟠، عرض مسقَط):</strong> تابع الأستاذ: canva.com ← « Magic Design » ← صِف « ملصق التفريد بأسلوب كرتوني » ← لاحظ النتيجة.",
                            "<strong>الحكم:</strong> املأ سطراً لكل أداة: فهم / إثبات / عرض. أي أداة لأي مهنة؟",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Explique la différenciation pédagogique avec un exemple de classe primaire, en 8 lignes.",
                    "en": "Explain pedagogical differentiation with a primary-class example, in 8 lines.",
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
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Les 4 composantes d'une bonne requête :</strong> contexte (qui tu es, quel cours), objectif (comprendre, citer, réviser), format (liste, tableau, 5 lignes), contrainte (sources, langue, dates). Teste : ajoute « en 5 phrases » à ton prompt et compare.",
                        "<strong>The 4 components of a good query:</strong> context (who you are, which course), goal (understand, cite, revise), format (list, table, 5 lines), constraint (sources, language, dates). Try: add \"in 5 sentences\" to your prompt and compare.",
                        "<strong>عناصر الصياغة الجيدة الأربعة:</strong> السياق (من أنت وأي درس) والهدف (فهم واستشهاد ومراجعة) والصيغة (قائمة وجدول و5 أسطر) والقيد (مصادر ولغة وتواريخ). جرّب: أضف « في 5 جمل » لصياغتك وقارن.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "⚠️ Erreurs fréquentes des pharmaciens débutants",
                "⚠️ Frequent rookie-pharmacist mistakes",
                "⚠️ أخطاء الصيادلة المبتدئين الشائعة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Vérifie ton tableau comparatif : as-tu commis l'une de ces 3 erreurs ? Corrige-la tout de suite sur ton écran.",
                        "Check your comparison table: did you make one of these 3 mistakes? Fix it right now on your screen.",
                        "راجع جدول مقارنتك: هل وقعت في أحد هذه الأخطاء الثلاثة؟ صحّحه فوراً على شاشتك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>❌ Le sirop unique :</strong> tout demander au même outil. <strong>✅ Prescris</strong> avec l'arbre : sources ? → 🟢 ; créer ? → 🟠 ; organiser-coder ? → 🟣 ; sinon 🔵.",
                            "<strong>❌ Croire sans ouvrir :</strong> la réponse a l'air sûre, mais les liens ? <strong>✅ Ouvre</strong> au moins 1 source avant de noter quoi que ce soit.",
                            "<strong>❌ Payer avant d'essayer :</strong> cliquer « Premium » par impatience. <strong>✅ Épuise</strong> d'abord le gratuit étudiant (largement suffisant pour ce module).",
                        ],
                        [
                            "<strong>❌ The single syrup:</strong> asking everything to one tool. <strong>✅ Prescribe</strong> with the tree: sources? → 🟢; create? → 🟠; organise-code? → 🟣; else 🔵.",
                            "<strong>❌ Believing without opening:</strong> the answer looks sure, but the links? <strong>✅ Open</strong> at least 1 source before noting anything.",
                            "<strong>❌ Paying before trying:</strong> clicking \"Premium\" impatiently. <strong>✅ Exhaust</strong> student free tiers first (plenty for this module).",
                        ],
                        [
                            "<strong>❌ الشراب الوحيد:</strong> طلب كل شيء من أداة واحدة. <strong>✅ اصرف</strong> بالشجرة: مصادر؟ ← 🟢؛ إنشاء؟ ← 🟠؛ تنظيم-برمجة؟ ← 🟣؛ وإلا 🔵.",
                            "<strong>❌ التصديق دون فتح:</strong> الجواب يبدو واثقاً لكن الروابط؟ <strong>✅ افتح</strong> مصدراً واحداً على الأقل قبل تدوين أي شيء.",
                            "<strong>❌ الدفع قبل التجربة:</strong> النقر على « Premium » بتسرّع. <strong>✅ استنفد</strong> المجاني الطلابي أولاً (كافٍ تماماً لهذه الوحدة).",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Teste maintenant :</strong> reprends ta question et ajoute « avec 2 sources datées ». Compare avant/après : le VERT obéit quand on exige des sources.",
                        "<strong>Try now:</strong> take your question back and add \"with 2 dated sources\". Compare before/after: GREEN obeys when you demand sources.",
                        "<strong>جرّب الآن:</strong> خذ سؤالك وأضف « مع مصدرين مؤرَّخين ». قارن قبل/بعد: الأخضر يطيع عندما تطلب المصادر.",
                    ),
                },
            ],
        },
        {
            "id": "s5",
            "titre": L(
                "🧪 Votre mission — ordonnance complète",
                "🧪 Your mission — full prescription",
                "🧪 مهمتك — وصفة كاملة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "En binôme, produisez UNE page : votre ordonnance pour 1 vraie question de cours. À rendre au début de la séance 3.",
                        "In pairs, produce ONE page: your prescription for 1 real lesson question. Hand it in at the start of session 3.",
                        "ثنائياً أنتجا صفحة واحدة: وصفتكما لسؤال درس حقيقي. تُسلَّم بداية الحصة 3.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Choisissez</strong> 1 question de VOTRE cours (ex : « c'est quoi la motivation scolaire ? »).",
                            "<strong>Testez-la</strong> sur 2 outils de familles différentes (ex : 🔵 ChatGPT + 🟢 Perplexity).",
                            "<strong>Remplissez</strong> le tableau : outil | réponse en 1 phrase | + (point fort) | − (limite vue).",
                            "<strong>Prescrivez</strong> avec l'arbre : sources ? → 🟢 ; créer ? → 🟠 ; organiser-coder ? → 🟣 ; sinon 🔵.",
                            "<strong>Choisissez</strong> vos 4 favoris (1 par tiroir), chacun justifié en 1 phrase.",
                        ],
                        [
                            "<strong>Pick</strong> 1 question from YOUR lesson (e.g. \"what is school motivation?\").",
                            "<strong>Test it</strong> on 2 tools from different families (e.g. 🔵 ChatGPT + 🟢 Perplexity).",
                            "<strong>Fill</strong> the table: tool | 1-sentence answer | + (strength) | − (seen limit).",
                            "<strong>Prescribe</strong> with the tree: sources? → 🟢; create? → 🟠; organise-code? → 🟣; else 🔵.",
                            "<strong>Pick</strong> your 4 favourites (1 per drawer), each justified in 1 sentence.",
                        ],
                        [
                            "<strong>اختارا</strong> سؤالاً من درسكما (مثال: « ما الدافعية المدرسية؟ »).",
                            "<strong>جرّباه</strong> على أداتين من عائلتين مختلفتين (مثال: 🔵 ChatGPT + 🟢 Perplexity).",
                            "<strong>املآ</strong> الجدول: الأداة | الجواب في جملة | + (ميزة) | − (حد مرصود).",
                            "<strong>اصرفا</strong> بالشجرة: مصادر؟ ← 🟢؛ إنشاء؟ ← 🟠؛ تنظيم-برمجة؟ ← 🟣؛ وإلا 🔵.",
                            "<strong>اختارا</strong> مفضلاتكما الأربع (واحدة لكل درج) مبرَّرة كل منها بجملة.",
                        ],
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
            ],
        },
        {
            "id": "s6",
            "titre": L(
                "✅ Checklist de validation",
                "✅ Validation checklist",
                "✅ قائمة التحقق",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Avant de partir, coche avec ton binôme. Tout doit être coché :",
                        "Before leaving, tick with your partner. Everything must be ticked:",
                        "قبل المغادرة علّم مع زميلك. يجب تأشير الكل:",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "☐ J'ai ouvert Perplexity SANS compte et obtenu une réponse sourcée.",
                            "☐ J'ai testé 1 question sur 2 outils et rempli le tableau comparatif.",
                            "☐ J'ai prescrit le bon tiroir avec l'arbre (sources ? créer ? organiser ?).",
                            "☐ J'ai repéré 1 limite (pas de sources, réponse inventée, compte exigé).",
                        ],
                        [
                            "☐ I opened Perplexity with NO account and got a sourced answer.",
                            "☐ I tested 1 question on 2 tools and filled the comparison table.",
                            "☐ I prescribed the right drawer with the tree (sources? create? organise?).",
                            "☐ I spotted 1 limit (no sources, invented answer, account required).",
                        ],
                        [
                            "☐ فتحت Perplexity دون حساب وحصلت على جواب بمصادر.",
                            "☐ جرّبت سؤالاً على أداتين وملأت جدول المقارنة.",
                            "☐ صرفت الدرج المناسب بالشجرة (مصادر؟ إنشاء؟ تنظيم؟).",
                            "☐ رصدت حداً واحداً (لا مصادر أو جواب مختلَق أو حساب مطلوب).",
                        ],
                    ),
                },
            ],
        },
    ],
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
                "J'ai ouvert Perplexity SANS compte et obtenu une réponse avec sources cliquables.",
                "I opened Perplexity with NO account and got an answer with clickable sources.",
                "فتحت Perplexity دون حساب وحصلت على جواب بمصادر قابلة للنقر.",
            ),
            L(
                "J'ai testé 1 question sur 2 outils et rempli mon tableau (fort + limite).",
                "I tested 1 question on 2 tools and filled my table (strength + limit).",
                "جرّبت سؤالاً على أداتين وملأت جدولي (ميزة + حد).",
            ),
            L(
                "Je prescris avec l'arbre : sources ? créer ? organiser-coder ? sinon bleu.",
                "I prescribe with the tree: sources? create? organise-code? else blue.",
                "أصرف بالشجرة: مصادر؟ إنشاء؟ تنظيم-برمجة؟ وإلا أزرق.",
            ),
            L(
                "J'ai mes 4 favoris (1 par tiroir), justifiés en 1 phrase chacun.",
                "I have my 4 favourites (1 per drawer), each justified in 1 sentence.",
                "عندي مفضلاتي الأربع (واحدة لكل درج) مبرَّرة كل منها بجملة.",
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
