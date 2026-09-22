# -*- coding: utf-8 -*-
"""Séance 10 — Esprit critique, Charte de l'étudiant et Construire son IA (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 10,
    "slug": "seance-10",
    "icon": "⚖️",
    "titles": L(
        "Esprit critique + Charte de l'étudiant + Construire son IA",
        "Critical thinking + Student charter + Build your AI",
        "الحس النقدي + ميثاق الطالب + بناء ذكائك",
    ),
    "descriptions": L(
        "Biais, hallucinations, fiabilité : penser contre la machine quand il faut. Adopter la Charte en 10 points et découvrir les 3 voies pour construire sa propre IA.",
        "Bias, hallucinations, reliability: thinking against the machine when needed. Adopt the 10-point Charter and discover 3 ways to build your own AI.",
        "التحيزات والهلوسات والموثوقية: التفكير ضد الآلة عند الحاجة. واعتماد الميثاق في 10 نقاط واكتشاف المسارات الثلاثة لبناء ذكائك الخاص.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Expliquer biais et hallucinations avec un exemple chacun.",
            "Explain bias and hallucinations with one example each.",
            "أن يفسّر التحيزات والهلوسات بمثال لكل منهما.",
        ),
        L(
            "Appliquer la grille VÉRIF (Vérifier, Évaluer, Recouper, Interroger, Formuler) à une réponse d'IA.",
            "Apply the VÉRIF grid (Verify, Evaluate, Cross-check, Question, Phrase) to an AI answer.",
            "أن يطبّق شبكة تحقّق على جواب ذكاء اصطناعي.",
        ),
        L(
            "Réciter et signer la Charte de l'étudiant en 10 points.",
            "Recite and sign the 10-point Student Charter.",
            "أن يستظهر ميثاق الطالب في 10 نقاط ويوقّعه.",
        ),
        L(
            "Comparer les 3 voies pour construire son IA : Dify, API Python, Ollama.",
            "Compare 3 ways to build your AI: Dify, Python API, Ollama.",
            "أن يقارن المسارات الثلاثة لبناء ذكائه: Dify وواجهة بايثون وOllama.",
        ),
        L(
            "Choisir sa voie et formuler son premier projet personnel d'IA.",
            "Choose your path and phrase your first personal AI project.",
            "أن يختار مساره ويصوغ مشروعه الشخصي الأول في الذكاء.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 9 suivies. Venir avec un avis tranché : « l'IA est-elle digne de confiance ? »",
        "Sessions 1 to 9 completed. Come with a firm opinion: \"is AI trustworthy?\"",
        "إتمام الحصص من 1 إلى 9. الإتيان برأي حاسم: « هل الذكاء الاصطناعي جدير بالثقة؟ »",
    ),
    "accroche": {
        "question": L(
            "L'IA vous a-t-elle déjà affirmé quelque chose de faux… avec un aplomb total ? Aujourd'hui, on apprend à ne plus jamais se faire avoir — puis à construire sa propre machine.",
            "Has AI ever stated something false to you… with total confidence? Today, we learn to never be fooled again — then to build our own machine.",
            "هل أكّد لك الذكاء يوماً شيئاً خاطئاً… بثقة تامة؟ اليوم نتعلّم ألا نُخدَع أبداً — ثم نبني آلتنا الخاصة.",
        ),
        "analogie": L(
            "🍳 Croire l'IA sur parole, c'est comme acheter du poisson sans le sentir : parfois c'est frais, parfois non — et c'est votre nez (votre esprit critique) qui décide, pas le vendeur.",
            "🍳 Believing AI at face value is like buying fish without smelling it: sometimes fresh, sometimes not — and it is your nose (your critical mind) deciding, not the seller.",
            "🍳 تصديق الذكاء دون تحقق كشراء السمك دون شمّه: أحياناً طازج وأحياناً لا — وأنفك (حسّك النقدي) هو من يقرّر لا البائع.",
        ),
        "phrase": L(
            "💡 L'esprit critique, c'est le muscle du diplôme : l'IA propose toujours, vous disposez à la fin — et un jour, vous construirez la machine au lieu de la subir.",
            "💡 Critical thinking is the diploma's muscle: AI always proposes, you decide in the end — and one day, you will build the machine instead of enduring it.",
            "💡 الحس النقدي عضلة الشهادة: الذكاء يقترح دائماً وأنت تقرّر أخيراً — ويوماً ما ستبني الآلة بدل أن تخضع لها.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : le poisson sans odeur",
                "Hook: the unsmelled fish",
                "انطلاقة: السمك دون شمّ",
            ),
            "detail": L(
                "Sondage : « qui s'est déjà fait avoir ? » + analogie du nez.",
                "Survey: \"who was already fooled?\" + nose analogy.",
                "استطلاع: « من خُدِع من قبل؟ » + تشبيه الأنف.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : biais + hallucinations + grille VÉRIF",
                "Explanation: bias + hallucinations + VÉRIF grid",
                "شرح: تحيزات + هلوسات + شبكة تحقق",
            ),
            "detail": L(
                "3 idées : pourquoi l'IA biaise, pourquoi elle invente, comment vérifier en 5 gestes.",
                "3 ideas: why AI biases, why it invents, how to check in 5 moves.",
                "3 أفكار: لماذا يتحيّز الذكاء ولماذا يختلق وكيف تتحقق في 5 خطوات.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : piéger l'IA puis la vérifier",
                "Demo: trap AI then verify it",
                "عرض: استدراج الذكاء ثم التحقق منه",
            ),
            "detail": L(
                "Mauvais prompt vs bon prompt : demander une référence, la voir inventée, la démasquer sur Scholar.",
                "Bad prompt vs good prompt: ask for a reference, see it invented, unmask it on Scholar.",
                "صياغة ضعيفة مقابل قوية: طلب مرجع ورؤيته مختلَقاً وكشفه في Scholar.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : audit VÉRIF + signature de la Charte",
                "Guided exercise: VÉRIF audit + Charter signing",
                "تمرين موجّه: تدقيق بالشبكة + توقيع الميثاق",
            ),
            "detail": L(
                "Auditer une réponse en binôme, noter le verdict, signer la Charte en 10 points.",
                "Audit an answer in pairs, note the verdict, sign the 10-point Charter.",
                "دقّق جواباً ثنائياً وسجّل الحكم ووقّع الميثاق في 10 نقاط.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : les 3 voies pour construire son IA",
                "Demo 2: 3 ways to build your AI",
                "عرض 2: المسارات الثلاثة لبناء ذكائك",
            ),
            "detail": L(
                "Dify (no-code), API Python (séance 7), Ollama (local) : choisir sa voie.",
                "Dify (no-code), Python API (session 7), Ollama (local): choose your path.",
                "Dify (دون كود) وواجهة بايثون (الحصة 7) وOllama (محلي): اختر مسارك.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et clôture du module",
                "Wrap-up, quiz and module closing",
                "خلاصة واختبار واختتام الوحدة",
            ),
            "detail": L(
                "« À retenir », quiz final, tour des 10 séances et remise des chartes signées.",
                "Key takeaways, final quiz, tour of the 10 sessions and signed charters handover.",
                "« ما يجب تذكّره » واختبار نهائي وجولة في الحصص العشر وتسليم المواثيق الموقعة.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Biais : l'IA apprend nos préjugés en même temps que nos savoirs",
                "Bias: AI learns our prejudices along with our knowledge",
                "التحيز: يتعلّم الذكاء أحكامنا المسبقة مع معارفنا",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "L'IA apprend sur des textes humains : elle hérite de leurs stéréotypes (métiers genrés, accents moqués, histoire racontée par les vainqueurs). La connaître, c'est pouvoir la contredire.",
                        "AI learns from human texts: it inherits their stereotypes (gendered jobs, mocked accents, history told by winners). Knowing this lets you contradict it.",
                        "يتعلّم الذكاء من نصوص بشرية: فيرث قوالبها (مهن مؤنثة، ولهجات مسخور منها، وتاريخ يرويه المنتصرون). ومعرفتك بذلك تمكّنك من معارضته.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Exemple métier :</strong> « donne un prénom à : infirmier, pilote, ministre » — observez les genres choisis, puis demandez la version équilibrée.",
                            "<strong>Exemple histoire :</strong> « raconte la colonisation » sans précision : de quel point de vue ? Demandez-en deux.",
                            "<strong>Contre-prompt :</strong> « Donne-moi les deux points de vue opposés sur [sujet], avec leurs arguments. »",
                        ],
                        [
                            "<strong>Job example:</strong> \"give a first name to: nurse, pilot, minister\" — watch chosen genders, then ask for the balanced version.",
                            "<strong>History example:</strong> \"tell colonisation\" with no detail: from whose viewpoint? Ask for two.",
                            "<strong>Counter-prompt:</strong> \"Give me both opposite views on [topic], with their arguments.\"",
                        ],
                        [
                            "<strong>مثال المهنة:</strong> « أعطِ اسماً لـ: ممرّض، طيّار، وزير » — لاحظ الأجناس المختارة ثم اطلب النسخة المتوازنة.",
                            "<strong>مثال التاريخ:</strong> « احكِ الاستعمار » دون تحديد: من أي وجهة نظر؟ اطلب اثنتين.",
                            "<strong>صياغة مضادة:</strong> « أعطني وجهتي النظر المتعارضتين في [موضوع] مع حججهما ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séances 1, 3 et 8 :</strong> l'acteur brillant qui invente (séance 1), les sources à vérifier sur Scholar (séance 3), la citation honnête (séance 8) — aujourd'hui on boucle la boucle : penser CONTRE la machine quand il faut.",
                        "<strong>🔗 Reminder of sessions 1, 3 and 8:</strong> the brilliant actor inventing (session 1), sources to check on Scholar (session 3), honest citation (session 8) — today we close the loop: thinking AGAINST the machine when needed.",
                        "<strong>🔗 تذكير بالحصص 1 و3 و8:</strong> الممثل البارع المختلِق (الحصة 1) والمصادر الموثقة في Scholar (الحصة 3) والاستشهاد النزيه (الحصة 8) — اليوم نغلق الحلقة: التفكير ضد الآلة عند الحاجة.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Hallucinations : pourquoi la machine invente avec aplomb",
                "Hallucinations: why the machine invents confidently",
                "الهلوسات: لماذا تختلق الآلة بثقة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Rappel séance 1 : le chatbot prédit des mots plausibles, pas des vérités. Quand il ne sait pas, il ne dit pas « je ne sais pas » : il invente une réponse qui SONNE vrai (fausse référence, fausse date, faux chiffre).",
                        "Reminder from session 1: the chatbot predicts plausible words, not truths. When it does not know, it does not say \"I don't know\": it invents an answer that SOUNDS true (fake reference, fake date, fake figure).",
                        "تذكير من الحصة 1: روبوت الدردشة يتنبأ بكلمات محتملة لا بحقائق. وعندما لا يعرف لا يقول « لا أعرف »: بل يختلق جواباً يبدو صحيحاً (مرجع مزيف، تاريخ مزيف، رقم مزيف).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Test piège :</strong> « Donne-moi 3 articles de 2023 sur X avec liens » → vérifier chaque lien (la moitié mène nulle part).",
                            "<strong>Test chiffre :</strong> « Quel est le taux de… ? » → exiger la source exacte, puis l'ouvrir.",
                            "<strong>Test aveu :</strong> « Es-tu sûr ? Quelles sont tes sources ? » — une bonne IA cite, une mauvaise s'excuse en boucle.",
                        ],
                        [
                            "<strong>Trap test:</strong> \"Give me 3 papers from 2023 on X with links\" → check each link (half lead nowhere).",
                            "<strong>Figure test:</strong> \"What is the rate of…?\" → demand the exact source, then open it.",
                            "<strong>Confession test:</strong> \"Are you sure? What are your sources?\" — a good AI cites, a bad one apologises in loops.",
                        ],
                        [
                            "<strong>اختبار الفخ:</strong> « أعطني 3 مقالات 2023 عن X مع روابط » ← تحقق من كل رابط (نصفها لا يؤدي لشيء).",
                            "<strong>اختبار الرقم:</strong> « ما نسبة…؟ » ← اطلب المصدر الدقيق ثم افتحه.",
                            "<strong>اختبار الاعتراف:</strong> « هل أنت متأكد؟ ما مصادرك؟ » — الجيد يستشهد والسيئ يعتذر تكراراً.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>Grille VÉRIF en 5 gestes :</strong> <strong>V</strong>érifier la source (existe-t-elle ?) · <strong>É</strong>valuer l'auteur (qui parle ?) · <strong>R</strong>ecouper (2e source ?) · <strong>I</strong>nterroger l'IA (« tes sources ? ») · <strong>F</strong>ormuler soi-même (réécrire, citer).",
                        "<strong>VÉRIF grid in 5 moves:</strong> <strong>V</strong>erify the source (does it exist?) · <strong>E</strong>valuate the author (who speaks?) · <strong>C</strong>ross-check (2nd source?) · <strong>Q</strong>uestion AI (\"your sources?\") · <strong>P</strong>hrase yourself (rewrite, cite).",
                        "<strong>شبكة التحقق في 5 خطوات:</strong> تحقّق من المصدر (هل هو موجود؟) · قيّم المؤلف (من يتكلم؟) · قارن (مصدر ثانٍ؟) · استجوب الذكاء (« مصادرك؟ ») · صِغ بنفسك (أعد الكتابة واستشهد).",
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple vécu :</strong> « Donne-moi 3 articles 2023 sur la différenciation avec liens » → 2 liens morts, 1 vrai (retrouvé sur Scholar). Verdict écrit : « réponse douteuse, 1/3 vérifié ». C'est l'audit VÉRIF en action.",
                        "<strong>🧪 Lived example:</strong> \"Give me 3 papers from 2023 on differentiation with links\" → 2 dead links, 1 real (found on Scholar). Written verdict: \"doubtful answer, 1/3 verified\". That is the VÉRIF audit in action.",
                        "<strong>🧪 مثال معيش:</strong> « أعطني 3 مقالات 2023 عن التفريد مع روابط » ← رابطان ميتان وواحد حقيقي (موجود في Scholar). الحكم مكتوباً: « جواب مشكوك، 1/3 موثق ». هذا تدقيق الشبكة عملياً.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "La Charte de l'étudiant : 10 engagements à signer",
                "The Student Charter: 10 commitments to sign",
                "ميثاق الطالب: 10 التزامات للتوقيع",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Le module se termine par un engagement solennel : utiliser l'IA en étudiant responsable. Lisez, discutez, signez — et affichez la charte dans votre chambre.",
                        "The module ends with a solemn commitment: using AI as a responsible student. Read, discuss, sign — and display the charter in your room.",
                        "تُختَم الوحدة بالتزام رسمي: استعمال الذكاء كطالب مسؤول. اقرأ وناقش ووقّع — وعلّق الميثاق في غرفتك.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Je vérifie</strong> toute information importante avant de l'utiliser (grille VÉRIF).",
                            "<strong>Je cite</strong> mes vraies sources (auteur, année) ; jamais de référence inventée.",
                            "<strong>J'écris d'abord</strong> moi-même : l'IA corrige, elle ne signe pas à ma place.",
                            "<strong>Je refuse</strong> la triche (sujet photographié, devoir 100 % généré).",
                            "<strong>Je protège</strong> ma clé API et mes données comme mes mots de passe.",
                            "<strong>Je questionne</strong> les biais : je demande l'autre point de vue.",
                            "<strong>Je révise</strong> en me testant (rappel actif), pas en relisant.",
                            "<strong>Je planifie</strong> : planning daté, suivi du dimanche, sommeil protégé.",
                            "<strong>J'aide</strong> mes camarades à utiliser l'IA honnêtement.",
                            "<strong>Je construis</strong> : mon premier projet d'IA personnelle avant la fin du semestre.",
                        ],
                        [
                            "<strong>I verify</strong> every important fact before using it (VÉRIF grid).",
                            "<strong>I cite</strong> my real sources (author, year); never an invented reference.",
                            "<strong>I write first</strong> myself: AI corrects, it never signs for me.",
                            "<strong>I refuse</strong> cheating (photographed paper, 100% generated homework).",
                            "<strong>I protect</strong> my API key and data like my passwords.",
                            "<strong>I question</strong> bias: I ask for the other viewpoint.",
                            "<strong>I revise</strong> by testing myself (active recall), not rereading.",
                            "<strong>I plan</strong>: dated schedule, Sunday tracking, protected sleep.",
                            "<strong>I help</strong> classmates use AI honestly.",
                            "<strong>I build</strong>: my first personal AI project before semester end.",
                        ],
                        [
                            "<strong>أتحقق</strong> من كل معلومة مهمة قبل استعمالها (شبكة التحقق).",
                            "<strong>أستشهد</strong> بمصادري الحقيقية (مؤلف، سنة)؛ لا مرجع مختلَق أبداً.",
                            "<strong>أكتب أولاً</strong> بنفسي: الذكاء يصحّح ولا يوقّع بدلي.",
                            "<strong>أرفض</strong> الغش (تصوير الموضوع، وواجب مولّد كلياً).",
                            "<strong>أحمي</strong> مفتاح API وبياناتي ككلمات مروري.",
                            "<strong>أستجوب</strong> التحيزات: أطلب وجهة النظر الأخرى.",
                            "<strong>أراجع</strong> باختبار نفسي (استدعاء نشط) لا بإعادة القراءة.",
                            "<strong>أخطط</strong>: مخطط مؤرَّخ ومتابعة الأحد ونوم محمي.",
                            "<strong>أساعد</strong> زملائي على استعمال نزيه للذكاء.",
                            "<strong>أبني</strong>: مشروعي الشخصي الأول في الذكاء قبل نهاية الفصل.",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Construire son IA : les 3 voies (et la vôtre)",
                "Build your AI: 3 paths (and yours)",
                "بناء ذكائك: المسارات الثلاثة (ومسارك)",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Après 9 séances à UTILISER l'IA, la dernière étape est de la CONSTRUIRE. Détail complet sur la page « Construire son IA » : voici la carte des 3 voies.",
                        "After 9 sessions USING AI, the last step is to BUILD it. Full detail on the \"Build your AI\" page: here is the 3-path map.",
                        "بعد 9 حصص في استعمال الذكاء، الخطوة الأخيرة بناؤه. التفصيل الكامل في صفحة « بناء ذكائك »: وهذه خريطة المسارات الثلاثة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>🧩 Voie 1 — Dify, sans code (⭐, 30-45 min) :</strong> chatbot qui répond depuis VOS PDF de cours. Idéal : « assistant du module de psycho » pour tout le groupe.",
                            "<strong>🐍 Voie 2 — API Python (⭐⭐, ~1 h, prérequis : séance 7) :</strong> assistant_chat.py puis mémoire, fonctions, sauvegarde. Idéal : projet personnel noté.",
                            "<strong>🐋 Voie 3 — Ollama en local (⭐⭐, 45 min) :</strong> <strong>ollama run llama3.2</strong>, hors-ligne, gratuit, privé. Idéal : réviser sans connexion.",
                            "<strong>Futur enseignant :</strong> imaginez un chatbot entraîné sur VOS fiches pour vos futurs élèves de primaire — c'est le pont entre vos études et votre métier.",
                        ],
                        [
                            "<strong>🧩 Path 1 — Dify, no-code (⭐, 30-45 min):</strong> chatbot answering from YOUR course PDFs. Ideal: a \"psycho module assistant\" for the whole group.",
                            "<strong>🐍 Path 2 — Python API (⭐⭐, ~1h, prerequisite: session 7):</strong> assistant_chat.py then memory, functions, saving. Ideal: graded personal project.",
                            "<strong>🐋 Path 3 — Local Ollama (⭐⭐, 45 min):</strong> <strong>ollama run llama3.2</strong>, offline, free, private. Ideal: revise without connection.",
                            "<strong>Future teacher:</strong> imagine a chatbot trained on YOUR sheets for your future primary pupils — the bridge between your studies and your job.",
                        ],
                        [
                            "<strong>🧩 المسار 1 — Dify دون كود (⭐، 30-45 دقيقة):</strong> روبوت يجيب من ملفات دروسك. مثالي: « مساعد وحدة علم النفس » للمجموعة.",
                            "<strong>🐍 المسار 2 — واجهة بايثون (⭐⭐، ~ساعة، المتطلب: الحصة 7):</strong> assistant_chat.py ثم ذاكرة ووظائف وحفظ. مثالي: مشروع شخصي منقَّط.",
                            "<strong>🐋 المسار 3 — Ollama محلياً (⭐⭐، 45 دقيقة):</strong> <strong>ollama run llama3.2</strong>، دون اتصال، مجاني، خاص. مثالي: مراجعة دون شبكة.",
                            "<strong>معلّم المستقبل:</strong> تخيّل روبوتاً مدرَّباً على بطاقاتك لتلاميذك مستقبلاً في الابتدائي — جسر بين دراستك ومهنتك.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Projet de fin de module :</strong> choisissez UNE voie et livrez en 3 semaines : le lien (Dify), le script (API) ou la capture (Ollama) + 1 page expliquant vos choix et vos vérifications.",
                        "<strong>End-of-module project:</strong> pick ONE path and deliver in 3 weeks: the link (Dify), the script (API) or the screenshot (Ollama) + 1 page explaining choices and checks.",
                        "<strong>مشروع نهاية الوحدة:</strong> اختر مساراً واحداً وسلّم في 3 أسابيع: الرابط (Dify) أو البرنامج (API) أو اللقطة (Ollama) + صفحة تشرح خياراتك وتحقيقاتك.",
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
                        "L'étudiant accompli : il vérifie tout, cite tout, écrit d'abord — et construit. La machine propose, l'humain dispose, le diplôme couronne.",
                        "The accomplished student: verifies everything, cites everything, writes first — and builds. The machine proposes, the human decides, the diploma crowns.",
                        "الطالب المكتمل: يتحقق من كل شيء ويستشهد بكل شيء ويكتب أولاً — ويبني. الآلة تقترح والإنسان يقرّر والشهادة تتوّج.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Après le module :</strong> page « Construire son IA » + votre voie choisie (Dify, API, Ollama) + date de livraison dans 3 semaines. Le module finit, votre projet commence.",
                        "<strong>➡️ After the module:</strong> the \"Build your AI\" page + your chosen path (Dify, API, Ollama) + delivery date in 3 weeks. The module ends, your project begins.",
                        "<strong>➡️ بعد الوحدة:</strong> صفحة « بناء ذكائك » + مسارك المختار (Dify وواجهة وOllama) + تاريخ تسليم بعد 3 أسابيع. تنتهي الوحدة ويبدأ مشروعك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Réflexe VÉRIF :</strong> 5 gestes avant tout usage important d'une réponse.",
                            "<strong>✅ Charte signée :</strong> affichée, relue avant chaque devoir.",
                            "<strong>✅ Une voie choisie :</strong> Dify, API ou Ollama — avec date de livraison.",
                            "<strong>✅ Transmission :</strong> expliquer à un camarade = maîtriser deux fois.",
                        ],
                        [
                            "<strong>✅ VÉRIF reflex:</strong> 5 moves before any important use of an answer.",
                            "<strong>✅ Signed charter:</strong> displayed, reread before each assignment.",
                            "<strong>✅ One path chosen:</strong> Dify, API or Ollama — with delivery date.",
                            "<strong>✅ Transmission:</strong> explaining to a classmate = mastering twice.",
                        ],
                        [
                            "<strong>✅ منعكس التحقق:</strong> 5 خطوات قبل أي استعمال مهم لجواب.",
                            "<strong>✅ ميثاق موقَّع:</strong> معلَّق ويُعاد قراءته قبل كل واجب.",
                            "<strong>✅ مسار مختار:</strong> Dify أو API أو Ollama — مع تاريخ تسليم.",
                            "<strong>✅ نقل:</strong> الشرح لزميل = إتقان مضاعف.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> croire sur parole, signer du 100 % IA, partager sa clé, abandonner son projet de construction.",
                        "<strong>❌ Mistakes to avoid:</strong> believing at face value, signing 100% AI, sharing your key, dropping your build project.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> التصديق دون تحقق، وتوقيع المولّد كلياً، ومشاركة المفتاح، والتخلي عن مشروع البناء.",
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
                            ["Demande", "« C'est vrai ? » (sans vérifier)", "« Donne 3 articles avec liens. Je vérifie sur Scholar puis je cite. »"],
                            ["Résultat", "Dépendant de la machine, fragile le jour J.", "Autonome, sourcé, futur constructeur."],
                        ],
                        [
                            ["Prompt", "\"Is it true?\" (no check)", "\"Give 3 papers with links. I check on Scholar then cite.\""],
                            ["Result", "Machine-dependent, fragile on D-day.", "Autonomous, sourced, future builder."],
                        ],
                        [
                            ["الطلب", "« هل هذا صحيح؟ » (دون تحقق)", "« أعطِ 3 مقالات بروابط. أتحقق في Scholar ثم أستشهد »"],
                            ["النتيجة", "تابع للآلة وهش يوم الامتحان.", "مستقل وموثَّق وبانٍ مستقبلي."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "D'où viennent les biais de l'IA ?",
                "Where does AI bias come from?",
                "من أين تأتي تحيزات الذكاء؟",
            ),
            "r": L(
                "Des textes humains d'entraînement : l'IA hérite de nos stéréotypes. La parade : demander l'autre point de vue.",
                "From human training texts: AI inherits our stereotypes. The shield: ask for the other viewpoint.",
                "من النصوص البشرية التدريبية: يرث الذكاء قوالبنا. والدرع: طلب وجهة النظر الأخرى.",
            ),
        },
        {
            "q": L(
                "Citez 3 gestes de la grille VÉRIF.",
                "Name 3 moves of the VÉRIF grid.",
                "اذكر 3 خطوات من شبكة التحقق.",
            ),
            "r": L(
                "Vérifier que la source existe, évaluer l'auteur, recouper avec une 2e source, interroger l'IA sur ses sources, formuler soi-même en citant.",
                "Verify the source exists, evaluate the author, cross-check with a 2nd source, question AI on its sources, phrase yourself while citing.",
                "التحقق من وجود المصدر، وتقييم المؤلف، والمقارنة بمصدر ثانٍ، واستجواب الذكاء عن مصادره، والصياغة الذاتية مع الاستشهاد.",
            ),
        },
        {
            "q": L(
                "Quelle voie de construction pour quel profil ?",
                "Which build path for which profile?",
                "أي مسار بناء لأي شخصية؟",
            ),
            "r": L(
                "Dify : pressé, sans code, chatbot sur PDF. API Python : programmeur en herbe (séance 7). Ollama : autonome, hors-ligne, privé.",
                "Dify: in a hurry, no-code, chatbot on PDFs. Python API: budding programmer (session 7). Ollama: autonomous, offline, private.",
                "Dify: مستعجل ودون كود وروبوت على PDF. واجهة بايثون: مبرمج ناشئ (الحصة 7). Ollama: مستقل ودون اتصال وخاص.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "En binôme : 1) demandez une référence à l'IA et auditez-la avec VÉRIF (verdict : fiable / douteuse / fausse) ; 2) lisez la Charte à voix haute et signez ; 3) choisissez votre voie de construction + date de livraison.",
            "In pairs: 1) ask AI for a reference and audit it with VÉRIF (verdict: reliable / doubtful / false); 2) read the Charter aloud and sign; 3) choose your build path + delivery date.",
            "ثنائياً: 1) اطلب مرجعاً من الذكاء ودقّقه بالشبكة (الحكم: موثوق / مشكوك / مزيف)؛ 2) اقرأ الميثاق جهراً ووقّع؛ 3) اختر مسار البناء + تاريخ التسليم.",
        ),
        "demarche": L(
            "1) Prompt piège : « 3 articles 2023 sur X avec liens ». 2) Pour chaque : existe ? auteur ? recoupé ? 3) Verdict écrit en 1 phrase. 4) Charte : discuter du point le plus dur, signer. 5) Projet : 3 lignes (voie, sujet, date).",
            "1) Trap prompt: \"3 papers from 2023 on X with links\". 2) For each: exists? author? cross-checked? 3) Verdict in 1 sentence. 4) Charter: discuss the hardest point, sign. 5) Project: 3 lines (path, topic, date).",
            "1) صياغة الفخ: « 3 مقالات 2023 عن X مع روابط ». 2) لكل منها: موجود؟ مؤلف؟ مقارَن؟ 3) الحكم في جملة. 4) الميثاق: ناقش أصعب نقطة ووقّع. 5) المشروع: 3 أسطر (مسار، موضوع، تاريخ).",
        ),
        "solution": L(
            "Audit réussi : au moins 1 référence démasquée (lien mort ou article inexistant) avec preuve Scholar, verdict écrit, Charte signée par les deux, projet formulé (ex : « Dify : assistant du module d'anglais, livré le 15/12 »).",
            "Successful audit: at least 1 unmasked reference (dead link or inexistent paper) with Scholar proof, written verdict, Charter signed by both, project phrased (e.g. \"Dify: English module assistant, due 15/12\").",
            "تدقيق ناجح: مرجع واحد مكشوف على الأقل (رابط ميت أو مقال غير موجود) بدليل Scholar، وحكم مكتوب، وميثاق موقَّع من الاثنين، ومشروع مصوغ (مثال: « Dify: مساعد وحدة الإنجليزية، تسليم 15/12 »).",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Biais et hallucinations de l'IA : comprendre pour se protéger",
                "AI bias and hallucinations: understand to protect yourself",
                "تحيزات الذكاء وهلوساته: افهم لتحمِ نفسك",
            ),
            "url": "https://www.youtube.com/results?search_query=biais+hallucinations+IA+expliques+simplement",
            "langue": "fr",
            "concept": L(
                "Voir des hallucinations réelles capturées en vidéo et les réflexes VÉRIF.",
                "See real hallucinations caught on video and the VÉRIF reflexes.",
                "شاهد هلوسات حقيقية ملتقطة بالفيديو ومنعكسات التحقق.",
            ),
        },
        {
            "titre": L(
                "هل نثق بالذكاء الاصطناعي؟ التفكير النقدي للطلبة",
                "Should we trust AI? Critical thinking for students",
                "هل نثق بالذكاء الاصطناعي؟ التفكير النقدي للطلبة",
            ),
            "url": "https://www.youtube.com/results?search_query=التفكير+النقدي+الذكاء+الاصطناعي+الطلبة",
            "langue": "ar",
            "concept": L(
                "Le débat confiance/méfiance posé simplement, avec des exemples de classe.",
                "The trust/distrust debate simply put, with classroom examples.",
                "نقاش الثقة والحذر مبسّطاً، مع أمثلة صفّية.",
            ),
        },
        {
            "titre": L(
                "Créer son chatbot sans coder avec Dify (tutoriel)",
                "Create your chatbot without coding with Dify (tutorial)",
                "أنشئ روبوتك دون برمجة مع Dify (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=dify+tutoriel+creer+chatbot+sans+code",
            "langue": "fr",
            "concept": L(
                "La voie 1 filmée : compte, PDF importé, premier chatbot en 30 minutes.",
                "Path 1 on film: account, imported PDF, first chatbot in 30 minutes.",
                "المسار 1 مصوَّر: حساب وملف مستورَد وأول روبوت في 30 دقيقة.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "Biais = préjugés hérités des textes humains ; demander l'autre point de vue.",
                "Bias = prejudices inherited from human texts; ask for the other viewpoint.",
                "التحيز = أحكام موروثة من النصوص البشرية؛ اطلب وجهة النظر الأخرى.",
            ),
            L(
                "Hallucination = invention confiante ; jamais de chiffre sans source ouverte.",
                "Hallucination = confident invention; never a figure without an opened source.",
                "الهلوسة = اختلاق واثق؛ لا رقم دون مصدر مفتوح أبداً.",
            ),
            L(
                "VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.",
                "VÉRIF: Verify, Evaluate, Cross-check, Question, Phrase.",
                "تحقق: تحقّق وقيّم وقارن واستجوب وصِغ.",
            ),
            L(
                "Charte 10 points : signée, affichée, relue avant chaque devoir.",
                "10-point Charter: signed, displayed, reread before each assignment.",
                "ميثاق النقاط العشر: موقَّع ومعلَّق ويُعاد قراءته قبل كل واجب.",
            ),
            L(
                "3 voies : Dify (PDF, sans code), API Python (séance 7), Ollama (local).",
                "3 paths: Dify (PDFs, no-code), Python API (session 7), Ollama (local).",
                "3 مسارات: Dify (ملفات، دون كود) وواجهة بايثون (الحصة 7) وOllama (محلي).",
            ),
        ],
        "analogies": [
            L(
                "Le nez et le poisson : on sent avant d'acheter, on vérifie avant d'utiliser.",
                "Nose and fish: smell before buying, verify before using.",
                "الأنف والسمك: شُمّ قبل الشراء وتحقّق قبل الاستعمال.",
            ),
            L(
                "L'acteur brillant (séance 1) : convaincant ne veut pas dire vrai.",
                "The brilliant actor (session 1): convincing does not mean true.",
                "الممثل البارع (الحصة 1): المقنع لا يعني الصحيح.",
            ),
            L(
                "Le permis de conduire : la charte signée, c'est le code de la route de l'IA.",
                "The driving licence: the signed charter is AI's highway code.",
                "رخصة السياقة: الميثاق الموقَّع هو قانون سير الذكاء.",
            ),
        ],
        "exemples": [
            L(
                "« Prénom pour infirmier/pilote » → biais genré démasqué puis corrigé.",
                "\"First name for nurse/pilot\" → gender bias unmasked then fixed.",
                "« اسم لممرّض/طيّار » ← تحيز جندري مكشوف ثم مصحَّح.",
            ),
            L(
                "3 liens demandés → 2 morts → verdict « douteuse » + sources Scholar.",
                "3 links asked → 2 dead → \"doubtful\" verdict + Scholar sources.",
                "3 روابط مطلوبة ← 2 ميتة ← حكم « مشكوك » + مصادر Scholar.",
            ),
            L(
                "Projet : « Dify : assistant d'anglais, livré le 15/12 ».",
                "Project: \"Dify: English assistant, due 15/12\".",
                "المشروع: « Dify: مساعد الإنجليزية، تسليم 15/12 ».",
            ),
        ],
        "analogie_finale": L(
            "🏁 Vous et l'IA, c'est comme le cavalier et le cheval : le cheval est puissant et rapide, mais c'est le cavalier qui tient les rênes, choisit la direction — et un jour, élève ses propres chevaux.",
            "🏁 You and AI is like rider and horse: the horse is strong and fast, but the rider holds the reins, chooses direction — and one day, raises his own horses.",
            "🏁 أنت والذكاء كالفارس والحصان: الحصان قوي سريع، لكن الفارس يمسك اللجام ويختار الاتجاه — ويوماً ما يربّي خيوله الخاصة.",
        ),
        "quiz": [
            {
                "q": L(
                    "D'où viennent les biais de l'IA ?",
                    "Where does AI bias come from?",
                    "من أين تأتي تحيزات الذكاء؟",
                ),
                "options": L(
                    ["D'un complot", "Des textes humains d'entraînement, avec leurs stéréotypes", "Du hasard", "De l'ordinateur"],
                    ["From a plot", "From human training texts, with their stereotypes", "From chance", "From the computer"],
                    ["من مؤامرة", "من النصوص البشرية التدريبية وقوالبها", "من الصدفة", "من الحاسوب"],
                ),
                "answer": 1,
                "exp": L(
                    "L'IA hérite des préjugés de ses données : la parade est le contre-point de vue.",
                    "AI inherits its data's prejudices: the shield is the counter-viewpoint.",
                    "يرث الذكاء أحكام بياناته المسبقة: والدرع وجهة النظر المضادة.",
                ),
            },
            {
                "q": L(
                    "Une réponse avec des chiffres mais sans source : que faire ?",
                    "An answer with figures but no source: what to do?",
                    "جواب بأرقام دون مصدر: ماذا تفعل؟",
                ),
                "options": L(
                    ["L'utiliser vite", "Exiger la source exacte, l'ouvrir, recouper (VÉRIF)", "La recopier joliment", "La traduire"],
                    ["Use it fast", "Demand the exact source, open it, cross-check (VÉRIF)", "Copy it nicely", "Translate it"],
                    ["استعمله بسرعة", "اطلب المصدر الدقيق وافتحه وقارن", "انسخه بجميل", "ترجمه"],
                ),
                "answer": 1,
                "exp": L(
                    "Chiffre sans source ouverte = rumeur : VÉRIF avant tout usage important.",
                    "Figure without opened source = rumour: VÉRIF before any important use.",
                    "رقم دون مصدر مفتوح = إشاعة: تحقق قبل أي استعمال مهم.",
                ),
            },
            {
                "q": L(
                    "Que signifie le V de VÉRIF ?",
                    "What does the V of VÉRIF mean?",
                    "ماذا تعني أول شبكة التحقق؟",
                ),
                "options": L(
                    ["Vite", "Vérifier que la source existe vraiment", "Voter", "Vendre"],
                    ["Fast", "Verify the source really exists", "Vote", "Sell"],
                    ["بسرعة", "التحقق من وجود المصدر فعلاً", "صوّت", "بِع"],
                ),
                "answer": 1,
                "exp": L(
                    "Premier geste : la source existe-t-elle (Scholar, site officiel) ? Sinon, tout s'écroule.",
                    "First move: does the source exist (Scholar, official site)? Else everything collapses.",
                    "الخطوة الأولى: هل المصدر موجود (Scholar، موقع رسمي)؟ وإلا انهار كل شيء.",
                ),
            },
            {
                "q": L(
                    "Quel engagement NE figure PAS dans la Charte ?",
                    "Which commitment is NOT in the Charter?",
                    "أي التزام ليس في الميثاق؟",
                ),
                "options": L(
                    ["Je vérifie et je cite", "Je laisse l'IA signer à ma place", "Je refuse la triche", "Je construis mon projet"],
                    ["I verify and cite", "I let AI sign for me", "I refuse cheating", "I build my project"],
                    ["أتحقق وأستشهد", "أدع الذكاء يوقّع بدلي", "أرفض الغش", "أبني مشروعي"],
                ),
                "answer": 1,
                "exp": L(
                    "Point 3 : J'écris d'abord moi-même — l'IA corrige, elle ne signe jamais à ma place.",
                    "Point 3: I write first myself — AI corrects, it never signs for me.",
                    "النقطة 3: أكتب أولاً بنفسي — الذكاء يصحّح ولا يوقّع بدلي أبداً.",
                ),
            },
            {
                "q": L(
                    "Quel chemin pour un chatbot sur vos PDF sans coder ?",
                    "Which path for a chatbot on your PDFs without coding?",
                    "أي مسار لروبوت على ملفاتك دون برمجة؟",
                ),
                "options": L(
                    ["Ollama", "Dify : compte, Knowledge, PDF importé, publier", "L'API Python", "Aucun"],
                    ["Ollama", "Dify: account, Knowledge, imported PDF, publish", "The Python API", "None"],
                    ["Ollama", "Dify: حساب ومعرفة وملف مستورَد ونشر", "واجهة بايثون", "لا شيء"],
                ),
                "answer": 1,
                "exp": L(
                    "Dify = voie no-code sur vos documents ; API = code (séance 7) ; Ollama = local hors-ligne.",
                    "Dify = no-code path on your documents; API = code (session 7); Ollama = offline local.",
                    "Dify = مسار دون كود على وثائقك؛ وAPI = كود (الحصة 7)؛ وOllama = محلي دون اتصال.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Piège collectif : demander 3 références, projeter la vérification Scholar en direct.",
            "Collective trap: ask for 3 references, project live Scholar verification.",
            "فخ جماعي: طلب 3 مراجع وعرض التحقق في Scholar مباشرة.",
        ),
        L(
            "Audit VÉRIF en binôme : verdict écrit + preuve (capture Scholar).",
            "Paired VÉRIF audit: written verdict + proof (Scholar screenshot).",
            "تدقيق ثنائي بالشبكة: حكم مكتوب + دليل (لقطة Scholar).",
        ),
        L(
            "Signature solennelle : lecture à voix haute de la Charte, signatures, photo de groupe.",
            "Solemn signing: Charter read aloud, signatures, group photo.",
            "توقيع رسمي: قراءة الميثاق جهراً وتوقيعات وصورة جماعية.",
        ),
        L(
            "Choix de voie : 3 lignes (voie, sujet, date) + premier pas fait en classe (compte Dify / test Ollama).",
            "Path choice: 3 lines (path, topic, date) + first step done in class (Dify account / Ollama test).",
            "اختيار المسار: 3 أسطر (مسار، موضوع، تاريخ) + خطوة أولى في القسم (حساب Dify / تجربة Ollama).",
        ),
    ],
    "retenir": [
        L(
            "Biais hérités : demander l'autre point de vue.",
            "Inherited bias: ask for the other viewpoint.",
            "تحيزات موروثة: اطلب وجهة النظر الأخرى.",
        ),
        L(
            "Hallucination : aucun chiffre sans source ouverte.",
            "Hallucination: no figure without opened source.",
            "الهلوسة: لا رقم دون مصدر مفتوح.",
        ),
        L(
            "VÉRIF : Vérifier, Évaluer, Recouper, Interroger, Formuler.",
            "VÉRIF: Verify, Evaluate, Cross-check, Question, Phrase.",
            "تحقق: تحقّق وقيّم وقارن واستجوب وصِغ.",
        ),
        L(
            "Charte 10 points : signée et affichée.",
            "10-point Charter: signed and displayed.",
            "ميثاق النقاط العشر: موقَّع ومعلَّق.",
        ),
        L(
            "Construire : Dify, API (S07), Ollama — projet daté.",
            "Build: Dify, API (S07), Ollama — dated project.",
            "ابنِ: Dify وواجهة (ح7) وOllama — مشروع مؤرَّخ.",
        ),
    ],
    "glossaire": [
        {
            "term": "Biais",
            "term_en": "Bias",
            "def_fr": "Déformation héritée des données d'entraînement (stéréotypes de genre, de culture, d'histoire).",
            "def_en": "Distortion inherited from training data (gender, culture, history stereotypes).",
            "def_ar": "تشوّه موروث من بيانات التدريب (قوالب الجنس والثقافة والتاريخ).",
        },
        {
            "term": "Hallucination",
            "term_en": "Hallucination",
            "def_fr": "Information inventée affirmée avec assurance par l'IA ; fréquente, pas un bug.",
            "def_en": "Invented information confidently stated by AI; common, not a bug.",
            "def_ar": "معلومة مختلقة يؤكدها الذكاء بثقة؛ شائعة وليست خللاً.",
        },
        {
            "term": "Grille VÉRIF",
            "term_en": "VÉRIF grid",
            "def_fr": "5 gestes : Vérifier, Évaluer, Recouper, Interroger, Formuler soi-même.",
            "def_en": "5 moves: Verify, Evaluate, Cross-check, Question, Phrase yourself.",
            "def_ar": "5 خطوات: تحقّق وقيّم وقارن واستجوب وصِغ بنفسك.",
        },
        {
            "term": "Charte de l'étudiant",
            "term_en": "Student Charter",
            "def_fr": "10 engagements d'usage honnête et vérifié de l'IA, signés en fin de module.",
            "def_en": "10 commitments for honest, verified AI use, signed at module end.",
            "def_ar": "10 التزامات لاستعمال نزيه وموثق للذكاء، تُوقَّع نهاية الوحدة.",
        },
        {
            "term": "Dify / Ollama",
            "term_en": "Dify / Ollama",
            "def_fr": "Dify : plateforme no-code de chatbots sur vos PDF. Ollama : modèles open source en local, hors-ligne.",
            "def_en": "Dify: no-code platform for chatbots on your PDFs. Ollama: local offline open-source models.",
            "def_ar": "Dify: منصة دون كود لروبوتات على ملفاتك. Ollama: نماذج مفتوحة محلياً دون اتصال.",
        },
    ],
    "dialogues_fr": """# Séance 10 — Dialogues pédagogiques (Français)

## Dialogue A — « Le lion et les licornes » (25 min)

**Personnages :** Karim (étudiant fier de sa bibliographie), Sara (vérificatrice), M. Amine (enseignant).

---

Karim : Cinq références pour mon exposé, trouvées en 2 minutes. Efficace, non ?

Sara : Vérifions. Référence 1… le lien est mort. Référence 2… l'auteur existe, l'article non. Deux licornes déjà.

Karim : Mais… il avait l'air tellement sûr !

M. Amine : Souviens-toi de la séance 1 : l'acteur brillant joue avec aplomb même quand le scénario est faux. Applique VÉRIF : la source existe-t-elle ? Qui parle ? Une 2e source confirme-t-elle ?

Sara : Référence 3… elle existe sur Scholar ! Un lion réel. On garde celle-là et on cite (auteur, année, page).

Karim : Donc : 1 lion réel vaut mieux que 5 licornes. Je réécris ma bibliographie… courte mais vraie.

---

## Dialogue B — « Je signe » (15 min)

**Personnages :** Toute la classe, l'enseignant, la Charte (jouée par deux étudiants qui la tiennent).

---

Enseignant : Dix séances, dix outils, un projet chacun. Avant de partir, qui s'engage ?

Classe (lit à voix haute) : « Je vérifie… je cite… j'écris d'abord… je refuse la triche… je protège ma clé… je questionne les biais… je révise en me testant… je planifie… j'aide… je construis. »

Lina : Le point le plus dur pour moi : « j'écris d'abord ». La tentation du tout-généré est forte.

Yacine : Pour moi : « je construis ». Mais j'ai choisi Dify : mon assistant d'anglais sera livré le 15 décembre !

Enseignant : Signez, affichez dans vos chambres, et rappelez-vous le cavalier : c'est vous qui tenez les rênes. Bonne route, futurs professeurs… et futurs constructeurs !

---

## Mini-rôle à jouer (3 min par binôme)
L'un défend « l'IA a toujours raison », l'autre attaque avec 2 preuves (1 biais + 1 hallucination vécus dans le module). Le jury (la classe) vote : l'esprit critique a-t-il gagné ?
""",
    "dialogues_en": """# Session 10 — Classroom dialogues (English)

## Dialogue A — "The lion and the unicorns" (25 min)

**Characters:** Karim (a student proud of his bibliography), Sara (a checker), Mr Amine (teacher).

---

Karim: Five references for my talk, found in 2 minutes. Efficient, right?

Sara: Let us check. Reference 1… dead link. Reference 2… the author exists, the paper does not. Two unicorns already.

Karim: But… it looked so sure!

Mr Amine: Remember session 1: the brilliant actor plays confidently even when the script is wrong. Apply VÉRIF: does the source exist? Who speaks? Does a 2nd source confirm?

Sara: Reference 3… it exists on Scholar! A real lion. We keep this one and cite (author, year, page).

Karim: So: 1 real lion beats 5 unicorns. I rewrite my bibliography… short but true.

---

## Dialogue B — "I sign" (15 min)

**Characters:** The whole class, the teacher, the Charter (played by two students holding it).

---

Teacher: Ten sessions, ten tools, one project each. Before leaving, who commits?

Class (reading aloud): "I verify… I cite… I write first… I refuse cheating… I protect my key… I question bias… I revise by testing… I plan… I help… I build."

Lina: The hardest point for me: "I write first". The all-generated temptation is strong.

Yacine: For me: "I build". But I chose Dify: my English assistant ships December 15th!

Teacher: Sign, display in your rooms, and remember the rider: you hold the reins. Good road, future teachers… and future builders!

---

## Mini role-play (3 min per pair)
One defends "AI is always right", the other attacks with 2 proofs (1 bias + 1 hallucination experienced in the module). The jury (the class) votes: did critical thinking win?
""",
}
