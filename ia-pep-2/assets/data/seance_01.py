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
    "objectifs": [
        L(
            "Ouvrir ChatGPT ou Gemini et poser ta première question avec un prompt prêt à copier.",
            "Open ChatGPT or Gemini and ask your first question with a ready-to-copy prompt.",
            "أن تفتح ChatGPT أو Gemini وتطرح أول سؤال بصياغة جاهزة للنسخ.",
        ),
        L(
            "Obtenir une explication simple de l'IA + 3 exemples que tu utilises sans le savoir.",
            "Get a simple explanation of AI + 3 examples you already use unknowingly.",
            "أن تحصل على شرح مبسّط للذكاء + 3 أمثلة تستعملها دون أن تدري.",
        ),
        L(
            "Juger une réponse d'IA : noter ce qui est clair, confus ou douteux.",
            "Judge an AI answer: note what is clear, confusing or doubtful.",
            "أن تحكم على جواب ذكاء: وتسجّل الواضح والمربك والمشكوك.",
        ),
        L(
            "Expliquer l'IA en 1 phrase à un enfant de 12 ans.",
            "Explain AI in 1 sentence to a 12-year-old.",
            "أن تشرح الذكاء في جملة واحدة لطفل في الثانية عشرة.",
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
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "🚀 Action immédiate : ta première question",
                "🚀 Instant action: your first question",
                "🚀 إجراء فوري: سؤالك الأول",
            ),
            "detail": L(
                "Ouvrir ChatGPT ou Gemini, copier le prompt 1, lire la réponse et noter 1 chose claire + 1 confuse.",
                "Open ChatGPT or Gemini, paste prompt 1, read the answer and note 1 clear + 1 confusing thing.",
                "افتح ChatGPT أو Gemini والصق الصياغة 1 واقرأ الجواب وسجّل شيئاً واضحاً وآخر مربكاً.",
            ),
        },
        {
            "time": "05–20",
            "badge": "🧱 B",
            **L(
                "📋 Recette pas à pas : 2e question et comparaison",
                "📋 Step-by-step recipe: 2nd question and comparison",
                "📋 وصفة خطوة بخطوة: السؤال الثاني والمقارنة",
            ),
            "detail": L(
                "Prompt 2 (3 exemples du quotidien), comparaison avec la liste du cours, et ce qui se passe quand tu tapes (prédiction du mot suivant).",
                "Prompt 2 (3 everyday examples), comparison with the lesson list, and what happens when you type (next-word prediction).",
                "الصياغة 2 (3 أمثلة يومية) ومقارنة مع قائمة الدرس وما يحدث عندما تكتب (تنبؤ الكلمة التالية).",
            ),
        },
        {
            "time": "20–40",
            "badge": "🛠️ C",
            **L(
                "🛠️ Démo : erreurs fréquentes et 2e avis",
                "🛠️ Demo: frequent mistakes and 2nd opinion",
                "🛠️ عرض: أخطاء شائعة ورأي ثانٍ",
            ),
            "detail": L(
                "Les 3 erreurs de débutant en direct + piège de l'hallucination : la même question au chatbot et au moteur sourcé.",
                "3 beginner mistakes live + the hallucination trap: same question to chatbot and sourced engine.",
                "3 أخطاء مبتدئة مباشرة + مصيدة الهلوسة: نفس السؤال لروبوت الدردشة والمحرّك بمصادر.",
            ),
        },
        {
            "time": "40–55",
            "badge": "✏️ D",
            **L(
                "🧪 Mission : ta première fiche d'usage",
                "🧪 Mission: your first usage sheet",
                "🧪 المهمة: أول بطاقة استعمال",
            ),
            "detail": L(
                "Produire le livrable : prompts utilisés + réponses + ton avis en 3 lignes.",
                "Produce the deliverable: used prompts + answers + your 3-line review.",
                "إنتاج المطلوب: الصياغات المستعملة + الأجوبة + رأيك في 3 أسطر.",
            ),
        },
        {
            "time": "55–60",
            "badge": "🧠 E",
            **L(
                "✅ Checklist et quiz éclair",
                "✅ Checklist and quick quiz",
                "✅ قائمة تحقق واختبار خاطف",
            ),
            "detail": L(
                "Cocher les 4 cases (outil ouvert, 3 questions, résultat utilisable, limite repérée) + quiz de 5 questions.",
                "Tick the 4 boxes (tool opened, 3 questions, usable result, spotted limit) + 5-question quiz.",
                "علّم على الخانات الأربع (الأداة مفتوحة و3 أسئلة ونتيجة صالحة وحد مرصود) + اختبار من 5 أسئلة.",
            ),
        },
        {
            "time": "60–90",
            "badge": "🤝 Atelier",
            **L(
                "🤝 Atelier : mission et dialogues",
                "🤝 Workshop: mission and dialogues",
                "🤝 ورشة: المهمة والحوارات",
            ),
            "detail": L(
                "Finaliser la fiche d'usage, jouer les dialogues A et B en binômes, puis mini-rôle de 3 min.",
                "Finalise the usage sheet, act out dialogues A and B in pairs, then a 3-minute mini role-play.",
                "أنهِ بطاقة الاستعمال ومثّل الحوارين A وB ثنائياً ثم دوراً مصغّراً من 3 دقائق.",
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
                        "Pas de cours magistral : dans 10 minutes, tu auras déjà parlé à une IA. Voici les 3 résultats concrets que tu produiras pendant cette séance.",
                        "No lecture: in 10 minutes, you will already have talked to an AI. Here are the 3 concrete results you will produce during this session.",
                        "لا محاضرة: بعد 10 دقائق ستكون قد تحدثت إلى ذكاء اصطناعي. هذه النتائج الملموسة الثلاث التي ستنتجها خلال هذه الحصة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1.</strong> Poser 2 questions à un chatbot (prompts prêts ci-dessous) et obtenir 2 réponses utilisables.",
                            "<strong>2.</strong> Juger chaque réponse : noter 1 chose claire + 1 chose confuse ou douteuse.",
                            "<strong>3.</strong> Expliquer l'IA en 1 phrase à un enfant de 12 ans — et prouver que tu as compris.",
                        ],
                        [
                            "<strong>1.</strong> Ask a chatbot 2 questions (ready prompts below) and get 2 usable answers.",
                            "<strong>2.</strong> Judge each answer: note 1 clear + 1 confusing or doubtful thing.",
                            "<strong>3.</strong> Explain AI in 1 sentence to a 12-year-old — proving you understood.",
                        ],
                        [
                            "<strong>1.</strong> طرح سؤالين على روبوت دردشة (صياغات جاهزة أدناه) والحصول على جوابين صالحين.",
                            "<strong>2.</strong> الحكم على كل جواب: تسجيل شيء واضح + شيء مربك أو مشكوك.",
                            "<strong>3.</strong> شرح الذكاء في جملة واحدة لطفل في الثانية عشرة — إثباتاً لفهمك.",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "🚀 Action immédiate — ta première fois (5 minutes)",
                "🚀 Instant action — your first time (5 minutes)",
                "🚀 إجراء فوري — مرتك الأولى (5 دقائق)",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Sors ton téléphone. Dans 5 minutes, tu auras posé ta première question à une IA. Suis les étapes, ne saute rien.",
                        "Take out your phone. In 5 minutes, you will have asked an AI your first question. Follow the steps, skip nothing.",
                        "أخرج هاتفك. بعد 5 دقائق ستكون قد طرحت أول سؤال على ذكاء اصطناعي. اتبع الخطوات ولا تتجاوز شيئاً.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Ouvre</strong> chatgpt.com (ou gemini.google.com) → bouton « S'inscrire » → compte gratuit (1 minute, e-mail suffit).",
                            "<strong>Clique</strong> « Nouveau chat » : tu vois une grande barre vide en bas. C'est là qu'on tape.",
                            "<strong>Copie-colle EXACTEMENT</strong> le prompt 1 ci-dessous, puis appuie sur Envoyer (▶ ou Entrée).",
                            "<strong>Lis</strong> la réponse : note sur papier 1 phrase CLAIRE (tu as compris) + 1 phrase CONFUSE (tu n'as pas compris).",
                            "<strong>Montre</strong> ton papier au voisin : comparez vos phrases confuses.",
                        ],
                        [
                            "<strong>Open</strong> chatgpt.com (or gemini.google.com) → \"Sign up\" button → free account (1 minute, e-mail is enough).",
                            "<strong>Click</strong> \"New chat\": you see a big empty bar at the bottom. That is where you type.",
                            "<strong>Copy-paste EXACTLY</strong> prompt 1 below, then press Send (▶ or Enter).",
                            "<strong>Read</strong> the answer: write down 1 CLEAR sentence (you got it) + 1 CONFUSING one (you did not).",
                            "<strong>Show</strong> your paper to your neighbour: compare your confusing sentences.",
                        ],
                        [
                            "<strong>افتح</strong> chatgpt.com (أو gemini.google.com) ← زر « التسجيل » ← حساب مجاني (دقيقة، يكفي بريد).",
                            "<strong>انقر</strong> « دردشة جديدة »: ترى شريطاً فارغاً كبيراً أسفل. هناك تكتب.",
                            "<strong>انسخ والصق حرفياً</strong> الصياغة 1 أدناه ثم اضغط إرسال (▶ أو Enter).",
                            "<strong>اقرأ</strong> الجواب: سجّل جملة واضحة (فهمتَها) + جملة مربكة (لم تفهمها).",
                            "<strong>اعرض</strong> ورقتك على جارك: قارنا جمليكما المربكتين.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Explique-moi ce qu'est l'intelligence artificielle comme si j'avais 12 ans, en 3 phrases.",
                    "en": "Explain to me what artificial intelligence is as if I were 12 years old, in 3 sentences.",
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>✅ Résultat attendu :</strong> une réponse courte (3 phrases simples, sans jargon). Si tu reçois 20 lignes compliquées : c'est normal, la séance 2 t'apprendra à cadrer tes demandes.",
                        "<strong>✅ Expected result:</strong> a short answer (3 simple sentences, no jargon). If you get 20 complicated lines: normal, session 2 will teach you to frame requests.",
                        "<strong>✅ النتيجة المنتظرة:</strong> جواب قصير (3 جمل بسيطة دون مصطلحات). إذا تلقيت 20 سطراً معقداً: عادي، الحصة 2 ستعلّمك تأطير طلباتك.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "📋 Recette pas à pas : 2e question et comparaison",
                "📋 Step-by-step recipe: 2nd question and comparison",
                "📋 وصفة خطوة بخطوة: السؤال الثاني والمقارنة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Reste dans le MÊME chat. Tu vas poser une 2e question, observer ce qui change, puis comparer avec la liste du cours.",
                        "Stay in the SAME chat. You will ask a 2nd question, watch what changes, then compare with the lesson list.",
                        "ابقَ في نفس الدردشة. ستطرح سؤالاً ثانياً وتلاحظ ما يتغيّر ثم تقارن مع قائمة الدرس.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Tape</strong> le prompt 2 ci-dessous et envoie. <strong>Observe :</strong> la réponse est-elle plus longue ? Donne-t-elle des exemples ? Quel ton (simple, savant) ?",
                            "<strong>Compare</strong> avec la liste du cours : téléphone (déverrouillage), GPS, anti-spam, Netflix, traducteur. Coche ✓ ce que l'IA a trouvé, ✗ ce qu'elle a raté.",
                            "<strong>Note</strong> dans ton cahier : 1 chose apprise + 1 question qui te reste.",
                            "<strong>Retiens le mécanisme :</strong> quand tu appuies sur Envoyer, le chatbot ne CHERCHE pas la réponse — il PRÉDIT le mot suivant, mot après mot, d'après des milliards d'exemples. C'est pour ça qu'il faut vérifier.",
                        ],
                        [
                            "<strong>Type</strong> prompt 2 below and send. <strong>Watch:</strong> is the answer longer? Does it give examples? What tone (simple, scholarly)?",
                            "<strong>Compare</strong> with the lesson list: phone (unlock), GPS, spam filter, Netflix, translator. Tick ✓ what AI found, ✗ what it missed.",
                            "<strong>Write</strong> in your notebook: 1 thing learned + 1 remaining question.",
                            "<strong>Keep the mechanism in mind:</strong> when you press Send, the chatbot does NOT LOOK UP the answer — it PREDICTS the next word, word after word, from billions of examples. That is why you must check.",
                        ],
                        [
                            "<strong>اكتب</strong> الصياغة 2 أدناه وأرسل. <strong>لاحظ:</strong> هل الجواب أطول؟ هل يعطي أمثلة؟ ما النبرة (بسيطة، علمية)؟",
                            "<strong>قارن</strong> مع قائمة الدرس: الهاتف (الفتح) ونظام الملاحة وفلتر الرسائل وNetflix والمترجم. علّم ✓ ما وجده الذكاء و✗ ما فاته.",
                            "<strong>سجّل</strong> في دفترك: شيئاً تعلمتَه + سؤالاً بقي لك.",
                            "<strong>احفظ الآلية:</strong> عندما تضغط إرسال لا يبحث الروبوت عن الجواب — بل يتنبأ بالكلمة التالية كلمة كلمة من مليارات الأمثلة. لهذا يجب التحقق.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": "Donne-moi 3 exemples d'intelligence artificielle que j'utilise sans le savoir dans ma vie quotidienne, avec 1 phrase d'explication pour chacun.",
                    "en": "Give me 3 examples of artificial intelligence I use without knowing it in my daily life, with 1 explanatory sentence for each.",
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>✅ Résultat attendu :</strong> 3 exemples (souvent : assistant vocal, recommandations, correcteur). Si un exemple te surprend (« mon téléphone me reconnaît ?! »), c'est gagné : tu viens de découvrir l'IA invisible.",
                        "<strong>✅ Expected result:</strong> 3 examples (often: voice assistant, recommendations, spellchecker). If one surprises you (\"my phone recognises me?!\"), you win: you just discovered invisible AI.",
                        "<strong>✅ النتيجة المنتظرة:</strong> 3 أمثلة (غالباً: مساعد صوتي وتوصيات ومصحح). إذا فاجأك مثال (« هاتفي يتعرّف عليّ؟! ») فقد ربحت: اكتشفتَ الذكاء الخفي.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "⚠️ Erreurs fréquentes des débutants",
                "⚠️ Frequent beginner mistakes",
                "⚠️ أخطاء المبتدئين الشائعة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Regarde ton écran : as-tu fait l'une de ces 3 erreurs ? Chacune a sa correction immédiate — teste-la tout de suite.",
                        "Look at your screen: did you make one of these 3 mistakes? Each has its instant fix — try it right now.",
                        "انظر إلى شاشتك: هل وقعت في أحد هذه الأخطاء الثلاثة؟ لكل منها تصحيح فوري — جرّبه الآن.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>❌ « Explique-moi tout sur l'IA »</strong> → réponse de 20 lignes inutilisable. <strong>✅ Dis plutôt :</strong> sujet + format + pour qui (« explique X en 5 phrases pour un étudiant de 2e année »).",
                            "<strong>❌ Croire parce que ça a l'air sûr</strong> → la confiance n'est pas la vérité : l'IA invente parfois (hallucination). <strong>✅ Vérifie</strong> 1 fait avec ton cours avant de l'utiliser.",
                            "<strong>❌ Demander AVANT de réfléchir</strong> → ton cerveau s'éteint. <strong>✅ Pense 1 minute</strong>, devine la réponse, PUIS compare avec l'IA.",
                        ],
                        [
                            "<strong>❌ \"Explain everything about AI to me\"</strong> → unusable 20-line answer. <strong>✅ Say instead:</strong> topic + format + for whom (\"explain X in 5 sentences for a 2nd-year student\").",
                            "<strong>❌ Believing because it sounds sure</strong> → confidence is not truth: AI sometimes invents (hallucination). <strong>✅ Check</strong> 1 fact against your lesson before using it.",
                            "<strong>❌ Asking BEFORE thinking</strong> → your brain switches off. <strong>✅ Think 1 minute</strong>, guess the answer, THEN compare with AI.",
                        ],
                        [
                            "<strong>❌ « اشرح لي كل شيء عن الذكاء »</strong> ← جواب من 20 سطراً لا يُستعمَل. <strong>✅ قل بدلاً:</strong> الموضوع + الصيغة + لمن (« اشرح X في 5 جمل لطالب سنة ثانية »).",
                            "<strong>❌ التصديق لأنه يبدو واثقاً</strong> ← الثقة ليست صدقاً: يختلق الذكاء أحياناً (هلوسة). <strong>✅ تحقق</strong> من معلومة مع درسك قبل استعمالها.",
                            "<strong>❌ السؤال قبل التفكير</strong> ← دماغك ينطفئ. <strong>✅ فكّر دقيقة</strong> وخمّن الجواب ثم قارن مع الذكاء.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Teste maintenant :</strong> reprends ta 1re réponse et demande « résume ta réponse en 1 phrase simple ». Observe : l'IA obéit au format que TU imposes.",
                        "<strong>Try now:</strong> take your 1st answer and ask \"summarise your answer in 1 simple sentence\". Watch: AI obeys the format YOU set.",
                        "<strong>جرّب الآن:</strong> خذ جوابك الأول واطلب « لخّص جوابك في جملة بسيطة واحدة ». لاحظ: الذكاء يطيع الصيغة التي تفرضها أنت.",
                    ),
                },
            ],
        },
        {
            "id": "s5",
            "titre": L(
                "🧪 Votre mission — le livrable",
                "🧪 Your mission — the deliverable",
                "🧪 مهمتك — المطلوب",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "En binôme, produisez UNE page (papier ou document) : c'est ce que vous rendrez au début de la séance 2.",
                        "In pairs, produce ONE page (paper or document): you will hand it in at the start of session 2.",
                        "ثنائياً أنتجا صفحة واحدة (ورق أو مستند): ستسلّمانها بداية الحصة 2.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>1.</strong> Les 2 prompts utilisés, copiés mot pour mot.",
                            "<strong>2.</strong> Les 2 réponses, résumées en 2 phrases chacune.",
                            "<strong>3.</strong> Votre avis en 3 lignes : qu'est-ce qui est clair ? utile ? douteux ?",
                            "<strong>4.</strong> Votre phrase de 12 ans : « L'IA, c'est… ».",
                        ],
                        [
                            "<strong>1.</strong> The 2 used prompts, copied word for word.",
                            "<strong>2.</strong> The 2 answers, summarised in 2 sentences each.",
                            "<strong>3.</strong> Your review in 3 lines: what is clear? useful? doubtful?",
                            "<strong>4.</strong> Your 12-year-old sentence: \"AI is…\".",
                        ],
                        [
                            "<strong>1.</strong> الصياغتان المستعملتان منسوختين حرفياً.",
                            "<strong>2.</strong> الجوابان ملخّصين في جملتين لكل منهما.",
                            "<strong>3.</strong> رأيكما في 3 أسطر: ما الواضح؟ المفيد؟ المشكوك؟",
                            "<strong>4.</strong> جملتكما لذي 12 سنة: « الذكاء هو… ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>🎯 Pour aller plus loin (séance 2) :</strong> gardez vos 2 prompts : vous apprendrez à les transformer en requêtes précises (contexte, objectif, format, contrainte).",
                        "<strong>🎯 Going further (session 2):</strong> keep your 2 prompts: you will learn to turn them into precise queries (context, goal, format, constraint).",
                        "<strong>🎯 للمضي أبعد (الحصة 2):</strong> احتفظا بصياغتيكما: ستتعلمان تحويلهما إلى طلبات دقيقة (سياق وهدف وصيغة وقيد).",
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
                            "☐ J'ai ouvert ChatGPT ou Gemini (outil ouvert, compte créé).",
                            "☐ J'ai posé au moins 2 questions (prompts 1 et 2 envoyés).",
                            "☐ J'ai obtenu un résultat utilisable (1 chose claire notée).",
                            "☐ J'ai identifié 1 erreur ou limite (trop long, exemple raté, doute sur un fait).",
                        ],
                        [
                            "☐ I opened ChatGPT or Gemini (tool open, account created).",
                            "☐ I asked at least 2 questions (prompts 1 and 2 sent).",
                            "☐ I got a usable result (1 clear thing noted).",
                            "☐ I spotted 1 mistake or limit (too long, missed example, doubt on a fact).",
                        ],
                        [
                            "☐ فتحت ChatGPT أو Gemini (الأداة مفتوحة والحساب منشأ).",
                            "☐ طرحت سؤالين على الأقل (الصياغتان 1 و2 مرسلتان).",
                            "☐ حصلت على نتيجة صالحة (شيء واضح مسجَّل).",
                            "☐ رصدت خطأ أو حداً (طول مفرط أو مثال فائت أو شك في معلومة).",
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