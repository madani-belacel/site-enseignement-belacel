# -*- coding: utf-8 -*-
"""Séance 09 — Organisation, gestion du temps et projets universitaires (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 9,
    "slug": "seance-09",
    "icon": "🗂️",
    "titles": L(
        "Organisation, gestion du temps et projets universitaires",
        "Organisation, time management and university projects",
        "التنظيم وتدبير الوقت والمشاريع الجامعية",
    ),
    "descriptions": L(
        "Planifier ses révisions sur 4 semaines, suivre 6 modules sans rien oublier, piloter un exposé en équipe : Notion AI, Gemini et Trello au service de l'étudiant organisé.",
        "Plan revisions over 4 weeks, track 6 modules forgetting nothing, run a team presentation: Notion AI, Gemini and Trello serving the organised student.",
        "تخطيط المراجعات على 4 أسابيع، وتتبّع 6 وحدات دون نسيان، وقيادة عرض جماعي: Notion AI وGemini وTrello في خدمة الطالب المنظَّم.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Construire un planning de révisions sur 4 semaines avec l'IA.",
            "Build a 4-week revision schedule with AI.",
            "أن يبني مخطط مراجعات على 4 أسابيع بالذكاء الاصطناعي.",
        ),
        L(
            "Créer un tableau de suivi de 6 modules (cours, fiches, exposés, examens).",
            "Create a 6-module tracking board (lessons, sheets, talks, exams).",
            "أن ينشئ لوحة تتبّع لست وحدات (دروس، بطاقات، عروض، امتحانات).",
        ),
        L(
            "Utiliser Notion AI : résumer, planifier, transformer des notes en tâches.",
            "Use Notion AI: summarise, plan, turn notes into tasks.",
            "أن يستعمل Notion AI: يلخّص ويخطّط ويحوّل الملاحظات إلى مهام.",
        ),
        L(
            "Piloter un projet d'exposé en équipe avec Trello : listes, cartes, délais.",
            "Run a team presentation project with Trello: lists, cards, deadlines.",
            "أن يقود مشروع عرض جماعي بـ Trello: قوائم وبطاقات وآجال.",
        ),
        L(
            "Appliquer la méthode des blocs (timeboxing) : 25 min de travail + 5 min de pause.",
            "Apply timeboxing: 25 min work + 5 min break.",
            "أن يطبّق منهجية الكتل الزمنية: 25 دقيقة عمل + 5 دقائق راحة.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 8 suivies. Venir avec la liste de ses modules et leurs dates d'examen.",
        "Sessions 1 to 8 completed. Come with your module list and exam dates.",
        "إتمام الحصص من 1 إلى 8. الإتيان بقائمة الوحدات وتواريخ الامتحانات.",
    ),
    "accroche": {
        "question": L(
            "Combien d'exposés avez-vous commencés la veille au soir ? Le problème n'est pas la paresse : c'est l'absence de tableau de bord.",
            "How many presentations did you start the night before? The problem is not laziness: it is the missing dashboard.",
            "كم عرضاً بدأتموه ليلة التسليم؟ المشكلة ليست الكسل: بل غياب لوحة القيادة.",
        ),
        "analogie": L(
            "🍳 S'organiser sans outil, c'est comme cuisiner un couscous de 6 plats en retenant tout dans sa tête : on oublie le sel, on brûle la viande. Avec un tableau de bord, chaque plat a sa minuterie.",
            "🍳 Organising without a tool is like cooking a 6-dish couscous keeping everything in mind: you forget the salt, burn the meat. With a dashboard, each dish has its timer.",
            "🍳 التنظيم دون أداة كطهي كسكس بستة أطباق مع حفظ كل شيء في الرأس: تنسى الملح وتحرق اللحم. وبلوحة قيادة، لكل طبق مؤقّته.",
        ),
        "phrase": L(
            "💡 L'IA n'ajoute pas des heures à votre journée : elle transforme vos notes en désordre en un plan clair, avec des rappels au bon moment.",
            "💡 AI does not add hours to your day: it turns messy notes into a clear plan, with reminders at the right time.",
            "💡 لا يضيف الذكاء ساعات إلى يومك: بل يحوّل ملاحظاتك المبعثرة إلى خطة واضحة، مع تذكيرات في وقتها.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : le couscous des 6 plats",
                "Hook: the 6-dish couscous",
                "انطلاقة: كسكس الأطباق الستة",
            ),
            "detail": L(
                "Sondage : « qui a déjà tout fait la veille ? » + analogie du tableau de bord.",
                "Survey: \"who already did everything the night before?\" + dashboard analogy.",
                "استطلاع: « من أنجز كل شيء ليلة التسليم؟ » + تشبيه لوحة القيادة.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : timeboxing + planning 4 semaines",
                "Explanation: timeboxing + 4-week plan",
                "شرح: الكتل الزمنية + مخطط 4 أسابيع",
            ),
            "detail": L(
                "3 idées : blocs 25+5, semaine type, règle « 1 grosse tâche par jour ».",
                "3 ideas: 25+5 blocks, typical week, \"1 big task per day\" rule.",
                "3 أفكار: كتل 25+5، وأسبوع نموذجي، وقاعدة « مهمة كبيرة واحدة يومياً ».",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : planning généré + tableau Notion",
                "Demo: generated schedule + Notion board",
                "عرض: مخطط مولّد + لوحة Notion",
            ),
            "detail": L(
                "Mauvais prompt vs bon prompt : de la liste des modules au planning daté.",
                "Bad prompt vs good prompt: from module list to dated schedule.",
                "صياغة ضعيفة مقابل قوية: من قائمة الوحدات إلى مخطط مؤرَّخ.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : ma semaine type",
                "Guided exercise: my typical week",
                "تمرين موجّه: أسبوعي النموذجي",
            ),
            "detail": L(
                "Chaque étudiant génère sa semaine : 6 modules, créneaux, pauses, sport.",
                "Each student generates their week: 6 modules, slots, breaks, sport.",
                "يولّد كل طالب أسبوعه: 6 وحدات، وحصص، وراحات، ورياضة.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : Trello pour l'exposé en équipe",
                "Demo 2: Trello for team presentations",
                "عرض 2: Trello للعرض الجماعي",
            ),
            "detail": L(
                "Listes À faire / En cours / Fait + cartes + responsables + délais.",
                "To-do / Doing / Done lists + cards + owners + deadlines.",
                "قوائم للقيام / جارٍ / تم + بطاقات + مسؤولون + آجال.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et annonce de la séance 10",
                "Wrap-up, quiz and preview of session 10",
                "خلاصة واختبار وتقديم الحصة العاشرة",
            ),
            "detail": L(
                "« À retenir ». Annonce : esprit critique, charte et construire son IA.",
                "Key takeaways. Preview: critical thinking, charter and building your AI.",
                "« ما يجب تذكّره ». تقديم: الحس النقدي والميثاق وبناء الذكاء.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Le timeboxing : votre journée en blocs de 25 minutes",
                "Timeboxing: your day in 25-minute blocks",
                "الكتل الزمنية: يومك في كتل من 25 دقيقة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Le cerveau se fatigue comme un muscle : 25 minutes d'effort intense + 5 minutes de vraie pause (marcher, eau, pas d'écran) = 4 blocs productifs par heure et demie.",
                        "The brain tires like a muscle: 25 minutes of intense effort + 5 minutes of real break (walk, water, no screen) = 4 productive blocks per hour and a half.",
                        "الدماغ يتعب كالعضلة: 25 دقيقة جهد مركّز + 5 دقائق راحة حقيقية (مشي، ماء، لا شاشة) = 4 كتل منتجة في ساعة ونصف.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Semaine type :</strong> créneaux fixes par module + 1 jour tampon pour les retards.",
                            "<strong>Règle d'or :</strong> 1 grosse tâche (exposé, chapitre) par jour, jamais 3.",
                            "<strong>Tampon :</strong> prévoir 20 % de vide : l'imprévu (panne, maladie) arrive toujours.",
                            "<strong>Sommeil non négociable :</strong> aucun planning sérieux ne vole les heures de nuit.",
                        ],
                        [
                            "<strong>Typical week:</strong> fixed slots per module + 1 buffer day for delays.",
                            "<strong>Golden rule:</strong> 1 big task (talk, chapter) per day, never 3.",
                            "<strong>Buffer:</strong> keep 20% empty: the unexpected (breakdown, illness) always comes.",
                            "<strong>Non-negotiable sleep:</strong> no serious schedule steals night hours.",
                        ],
                        [
                            "<strong>أسبوع نموذجي:</strong> حصص ثابتة لكل وحدة + يوم احتياطي للتأخر.",
                            "<strong>قاعدة ذهبية:</strong> مهمة كبيرة واحدة (عرض، فصل) يومياً، لا ثلاث أبداً.",
                            "<strong>هامش:</strong> اترك 20٪ فارغاً: الطارئ (عطل، مرض) يأتي دائماً.",
                            "<strong>نوم غير قابل للتفاوض:</strong> لا مخطط جدّي يسرق ساعات الليل.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séance 6 :</strong> la répétition espacée (J+1, J+3, J+7) disait QUAND revoir ; le planning 4 semaines dit QUAND EXACTEMENT (jour + heure). Même méthode, passée au calendrier.",
                        "<strong>🔗 Reminder of session 6:</strong> spaced repetition (D+1, D+3, D+7) said WHEN to review; the 4-week schedule says WHEN EXACTLY (day + hour). Same method, put on calendar.",
                        "<strong>🔗 تذكير بالحصة 6:</strong> التكرار المتباعد (اليوم+1، +3، +7) قال متى تراجع؛ ومخطط الأسابيع الأربعة يقول متى بالضبط (يوم + ساعة). نفس المنهجية على التقويم.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Le planning 4 semaines : de la liste au calendrier daté",
                "The 4-week plan: from list to dated calendar",
                "مخطط الأسابيع الأربعة: من القائمة إلى تقويم مؤرَّخ",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Donnez à l'IA vos contraintes (modules, dates, heures libres) et exigez un calendrier daté, pas des conseils vagues.",
                        "Give AI your constraints (modules, dates, free hours) and demand a dated calendar, not vague advice.",
                        "أعطِ الذكاء قيودك (وحدات، تواريخ، ساعات فراغ) واطلب تقويماً مؤرَّخاً لا نصائح عامة.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt planning :</strong> « 6 modules [lister], examens le [dates], libre [créneaux]. Fais un planning daté sur 4 semaines : révisions espacées J+3/J+7, 1 exposé/semaine, dimanche tampon. »",
                            "<strong>Exigez du daté :</strong> « semaine 1 : lundi 14h psycho chapitre 2… » — sinon, redemandez.",
                            "<strong>Révision hebdo :</strong> chaque dimanche, 20 min : cocher, reporter, régénérer la semaine.",
                        ],
                        [
                            "<strong>Schedule prompt:</strong> \"6 modules [list], exams on [dates], free [slots]. Make a dated 4-week plan: spaced reviews D+3/D+7, 1 talk/week, buffer Sunday.\"",
                            "<strong>Demand dated:</strong> \"week 1: Monday 2pm psycho chapter 2…\" — else, ask again.",
                            "<strong>Weekly review:</strong> each Sunday, 20 min: tick, postpone, regenerate the week.",
                        ],
                        [
                            "<strong>صياغة المخطط:</strong> « 6 وحدات [اعرض]، امتحانات في [تواريخ]، فراغ في [حصص]. ضع مخططاً مؤرَّخاً على 4 أسابيع: مراجعات متباعدة يوم+3/+7، وعرض أسبوعياً، وأحد احتياطي ».",
                            "<strong>اطلب المؤرَّخ:</strong> « الأسبوع 1: الاثنين 14:00 علم النفس الفصل 2… » — وإلا أعد الطلب.",
                            "<strong>مراجعة أسبوعية:</strong> كل أحد 20 دقيقة: علّم، أجّل، وأعد توليد الأسبوع.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> Yacine, 6 modules, partiels dans 1 mois, libre 2 h/jour → semaine 1 : « lun 14h psycho ch.2 (3 blocs), mar 10h anglais temps, mer 16h didactique fiche… dim : tampon ». Affiché au mur, coché chaque soir.",
                        "<strong>🧪 Concrete example:</strong> Yacine, 6 modules, midterms in 1 month, 2h/day free → week 1: \"Mon 2pm psycho ch.2 (3 blocks), Tue 10am English tenses, Wed 4pm didactics sheet… Sun: buffer\". On the wall, ticked nightly.",
                        "<strong>🧪 مثال ملموس:</strong> ياسين، 6 وحدات، فروض بعد شهر، فراغ ساعتين/يوم ← الأسبوع 1: « اثنين 14:00 علم النفس ف2 (3 كتل)، ثلاثاء 10:00 الأزمنة، أربعاء 16:00 بطاقة الديداكتيك… أحد: احتياطي ». معلَّق على الجدار ويؤشَّر كل مساء.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Notion AI : le deuxième cerveau de l'étudiant",
                "Notion AI: the student's second brain",
                "Notion AI: الدماغ الثاني للطالب",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Notion = cahiers + tableaux + calendrier au même endroit, gratuit pour les étudiants. Son IA résume vos notes et les transforme en tâches.",
                        "Notion = notebooks + boards + calendar in one place, free for students. Its AI summarises your notes and turns them into tasks.",
                        "Notion = دفاتر + لوحات + تقويم في مكان واحد، مجاني للطلبة. وذكاؤه يلخّص ملاحظاتك ويحوّلها إلى مهام.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Base Modules :</strong> une base de données avec 6 lignes (modules) : progression %, prochaine échéance, fiche liée.",
                            "<strong>Ask AI :</strong> « résume ces 3 pages de cours en 5 puces » / « transforme ces notes en liste de tâches datées ».",
                            "<strong>Modèles :</strong> « fiche de séance », « plan d'exposé », « carnet d'erreurs » — créés une fois, réutilisés partout.",
                        ],
                        [
                            "<strong>Modules database:</strong> one database with 6 rows (modules): progress %, next deadline, linked sheet.",
                            "<strong>Ask AI:</strong> \"summarise these 3 lesson pages in 5 bullets\" / \"turn these notes into a dated task list\".",
                            "<strong>Templates:</strong> \"session sheet\", \"talk plan\", \"mistake notebook\" — created once, reused everywhere.",
                        ],
                        [
                            "<strong>قاعدة الوحدات:</strong> قاعدة بيانات بستة أسطر (وحدات): نسبة تقدّم، واستحقاق قادم، وبطاقة مرتبطة.",
                            "<strong>اسأل الذكاء:</strong> « لخّص صفحات الدرس الثلاث في 5 نقاط » / « حوّل هذه الملاحظات إلى قائمة مهام مؤرَّخة ».",
                            "<strong>قوالب:</strong> « بطاقة حصة »، « خطة عرض »، « دفتر أخطاء » — تُنشَأ مرة وتُستعمَل دائماً.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> photographiez vos notes papier → Notion les rend cherchables → Ask AI les résume. Le papier et le numérique cessent de se faire la guerre.",
                        "<strong>Tip:</strong> photograph your paper notes → Notion makes them searchable → Ask AI summarises them. Paper and digital stop fighting.",
                        "<strong>نصيحة:</strong> صوّر ملاحظاتك الورقية ← يجعلها Notion قابلة للبحث ← ويلخّصها الذكاء. فيتصالح الورق والرقمي.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Trello : piloter l'exposé en équipe sans dispute",
                "Trello: run team presentations without fights",
                "Trello: قيادة العرض الجماعي دون خلاف",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Tout exposé en groupe échoue pour la même raison : « je croyais que c'était toi qui le faisais ». Trello rend visible qui fait quoi, pour quand.",
                        "Every group presentation fails for the same reason: \"I thought you were doing it\". Trello shows who does what, by when.",
                        "كل عرض جماعي يفشل للسبب نفسه: « ظننت أنك أنت من يفعله ». يجعل Trello ظاهراً من يفعل ماذا ومتى.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>3 listes :</strong> À faire → En cours → Fait. Une carte = une micro-tâche (pas « l'exposé », mais « intro 8 lignes »).",
                            "<strong>Chaque carte :</strong> 1 responsable, 1 date, 1 pièce jointe (fichier/lien).",
                            "<strong>Rituel :</strong> 10 min debout chaque semaine : chaque membre déplace ses cartes et annonce la suite.",
                            "<strong>Prompt Gemini :</strong> « Découpe cet exposé [sujet] en 12 micro-tâches avec durées pour 3 personnes en 2 semaines. »",
                        ],
                        [
                            "<strong>3 lists:</strong> To-do → Doing → Done. One card = one micro-task (not \"the talk\", but \"8-line intro\").",
                            "<strong>Each card:</strong> 1 owner, 1 date, 1 attachment (file/link).",
                            "<strong>Ritual:</strong> 10 min standing weekly: each member moves cards and announces next.",
                            "<strong>Gemini prompt:</strong> \"Split this talk [topic] into 12 micro-tasks with durations for 3 people in 2 weeks.\"",
                        ],
                        [
                            "<strong>3 قوائم:</strong> للقيام ← جارٍ ← تم. بطاقة = مهمة دقيقة (لا « العرض » بل « مقدمة 8 أسطر »).",
                            "<strong>كل بطاقة:</strong> مسؤول واحد، وتاريخ واحد، ومرفق واحد (ملف/رابط).",
                            "<strong>طقس:</strong> 10 دقائق وقوفاً أسبوعياً: كل عضو يحرّك بطاقاته ويعلن التالي.",
                            "<strong>صياغة Gemini:</strong> « قسّم هذا العرض [الموضوع] إلى 12 مهمة دقيقة بمدد لثلاثة أشخاص في أسبوعين ».",
                        ],
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
                        "L'organisation est un système, pas un effort : un planning daté + un tableau suivi chaque dimanche + des micro-tâches visibles par tous.",
                        "Organisation is a system, not an effort: a dated schedule + a board reviewed each Sunday + micro-tasks visible to all.",
                        "التنظيم نظام لا جهد: مخطط مؤرَّخ + لوحة تُراجَع كل أحد + مهام دقيقة ظاهرة للجميع.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 10 :</strong> un étudiant organisé vérifie tout : la grille VÉRIF et la Charte en 10 points (séance 10) sont le contrôle qualité de votre système.",
                        "<strong>➡️ Bridge to session 10:</strong> an organised student verifies everything: the VÉRIF grid and 10-point Charter (session 10) are your system's quality control.",
                        "<strong>➡️ جسر إلى الحصة 10:</strong> الطالب المنظَّم يتحقق من كل شيء: شبكة التحقق وميثاق النقاط العشر (الحصة 10) هما ضبط جودة نظامك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Tout est daté :</strong> une tâche sans date est un vœu, pas un plan.",
                            "<strong>✅ Dimanche 20 min :</strong> le rendez-vous hebdo qui sauve le semestre.",
                            "<strong>✅ 1 outil maître :</strong> Notion OU papier + photo — jamais 4 applis en même temps.",
                            "<strong>✅ Pauses planifiées :</strong> sport, famille, sommeil écrits dans le planning comme des cours.",
                        ],
                        [
                            "<strong>✅ Everything dated:</strong> a task without a date is a wish, not a plan.",
                            "<strong>✅ Sunday 20 min:</strong> the weekly meeting saving the semester.",
                            "<strong>✅ 1 master tool:</strong> Notion OR paper + photo — never 4 apps at once.",
                            "<strong>✅ Planned breaks:</strong> sport, family, sleep written in the schedule like lessons.",
                        ],
                        [
                            "<strong>✅ كل شيء مؤرَّخ:</strong> مهمة بلا تاريخ أمنية لا خطة.",
                            "<strong>✅ الأحد 20 دقيقة:</strong> الموعد الأسبوعي الذي ينقذ الفصل.",
                            "<strong>✅ أداة رئيسية واحدة:</strong> Notion أو ورق + صورة — لا 4 تطبيقات معاً أبداً.",
                            "<strong>✅ راحات مخططة:</strong> رياضة وعائلة ونوم مكتوبة في المخطط كالدروس.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> planning irréaliste (10 h/jour), 4 applis à la fois, reporter sans reprogrammer, sacrifier le sommeil la veille.",
                        "<strong>❌ Mistakes to avoid:</strong> unrealistic schedule (10h/day), 4 apps at once, postponing without rescheduling, sacrificing sleep the day before.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> مخطط خيالي (10 ساعات/يوم)، و4 تطبيقات معاً، والتأجيل دون إعادة برمجة، والتضحية بالنوم ليلة الامتحان.",
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
                            ["Demande", "« Organise mes révisions. »", "« 6 modules [liste], examens le [dates], libre 2 h/jour. Planning daté 4 semaines + 1 dimanche tampon. »"],
                            ["Résultat", "Conseils vagues jamais appliqués.", "Calendrier daté, suivi chaque dimanche."],
                        ],
                        [
                            ["Prompt", "\"Organise my revisions.\"", "\"6 modules [list], exams on [dates], 2h/day free. Dated 4-week plan + 1 buffer Sunday.\""],
                            ["Result", "Vague advice never applied.", "Dated calendar, tracked each Sunday."],
                        ],
                        [
                            ["الطلب", "« نظّم مراجعاتي »", "« 6 وحدات [اعرض]، امتحانات في [تواريخ]، فراغ ساعتين/يوم. مخطط مؤرَّخ 4 أسابيع + أحد احتياطي »"],
                            ["النتيجة", "نصائح عامة لا تُطبَّق أبداً.", "تقويم مؤرَّخ يُتابَع كل أحد."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Pourquoi une tâche sans date n'est-elle pas un plan ?",
                "Why is a task without a date not a plan?",
                "لماذا المهمة بلا تاريخ ليست خطة؟",
            ),
            "r": L(
                "Parce que sans date ni créneau, elle flotte et sera toujours repoussée par l'urgent. Datée, elle devient un rendez-vous avec vous-même.",
                "Because without date or slot, it floats and will always be pushed by the urgent. Dated, it becomes an appointment with yourself.",
                "لأنها دون تاريخ وحصة تطفو ويدفعها العاجل دائماً. ومؤرَّخةً تصبح موعداً مع نفسك.",
            ),
        },
        {
            "q": L(
                "Que contient le rendez-vous du dimanche (20 min) ?",
                "What does the Sunday meeting (20 min) contain?",
                "ماذا يحوي موعد الأحد (20 دقيقة)؟",
            ),
            "r": L(
                "Cocher ce qui est fait, reporter ce qui ne l'est pas avec une nouvelle date, régénérer la semaine avec l'IA.",
                "Tick what is done, postpone the rest with a new date, regenerate the week with AI.",
                "التأشير على المنجَز، وتأجيل الباقي بتاريخ جديد، وإعادة توليد الأسبوع بالذكاء.",
            ),
        },
        {
            "q": L(
                "Qui fait quoi dans Trello : comment l'échec « je croyais que c'était toi » est-il évité ?",
                "Who does what in Trello: how is the \"I thought it was you\" failure avoided?",
                "من يفعل ماذا في Trello: كيف يُتجنَّب فشل « ظننت أنك أنت »؟",
            ),
            "r": L(
                "Chaque carte a 1 responsable + 1 date visibles par tous, et le rituel hebdo de 10 min synchronise l'équipe.",
                "Each card has 1 owner + 1 date visible to all, and the 10-min weekly ritual syncs the team.",
                "كل بطاقة فيها مسؤول واحد + تاريخ واحد ظاهران للجميع، والطقس الأسبوعي (10 دقائق) يزامن الفريق.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "Avec votre liste de modules : 1) générez votre semaine type (créneaux + pauses) ; 2) créez la base « Modules » (6 lignes : %, échéance, fiche) ; 3) découpez votre prochain exposé en 8 micro-tâches datées.",
            "With your module list: 1) generate your typical week (slots + breaks); 2) create the \"Modules\" base (6 rows: %, deadline, sheet); 3) split your next talk into 8 dated micro-tasks.",
            "بقائمة وحداتك: 1) ولّد أسبوعك النموذجي (حصص + راحات)؛ 2) أنشئ قاعدة « الوحدات » (6 أسطر: نسبة، استحقاق، بطاقة)؛ 3) قسّم عرضك القادم إلى 8 مهام دقيقة مؤرَّخة.",
        ),
        "demarche": L(
            "1) Listez modules + dates + heures libres. 2) Prompt planning → exigez du daté. 3) Reportez dans Notion (ou papier + photo). 4) Test 25+5 sur un vrai chapitre. 5) Montrez à votre voisin : comprend-il votre semaine en 30 secondes ?",
            "1) List modules + dates + free hours. 2) Schedule prompt → demand dated. 3) Copy into Notion (or paper + photo). 4) Try 25+5 on a real chapter. 5) Show your neighbour: do they grasp your week in 30 seconds?",
            "1) اعرض الوحدات + التواريخ + ساعات الفراغ. 2) صياغة المخطط ← اطلب المؤرَّخ. 3) انقل إلى Notion (أو ورق + صورة). 4) جرّب 25+5 على فصل حقيقي. 5) اعرض على جارك: هل يفهم أسبوعك في 30 ثانية؟",
        ),
        "solution": L(
            "Réussi si : semaine datée affichée (cours, pauses, sommeil, sport), base 6 lignes remplie, 8 micro-tâches avec responsables et dates, et le voisin comprend tout en 30 secondes sans explication.",
            "Success if: dated week displayed (lessons, breaks, sleep, sport), 6-row base filled, 8 micro-tasks with owners and dates, and the neighbour grasps everything in 30 seconds unexplained.",
            "نجاح إذا: أسبوع مؤرَّخ معروض (دروس، راحات، نوم، رياضة)، وقاعدة الأسطر الستة مملوءة، و8 مهام دقيقة بمسؤولين وتواريخ، والجار يفهم كل شيء في 30 ثانية دون شرح.",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Notion pour étudiants : organiser cours et révisions (tutoriel)",
                "Notion for students: organise lessons and revisions (tutorial)",
                "Notion للطلبة: تنظيم الدروس والمراجعات (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=notion+etudiant+organiser+cours+tutoriel+francais",
            "langue": "fr",
            "concept": L(
                "Créer la base « Modules » et vos modèles (fiche, exposé) pas à pas.",
                "Create the \"Modules\" base and your templates (sheet, talk) step by step.",
                "إنشاء قاعدة « الوحدات » وقوالبك (بطاقة، عرض) خطوة بخطوة.",
            ),
        },
        {
            "titre": L(
                "كيف تخطط أسبوعك الدراسي؟ إدارة الوقت للطلبة",
                "How to plan your study week? Time management for students",
                "كيف تخطط أسبوعك الدراسي؟ إدارة الوقت للطلبة",
            ),
            "url": "https://www.youtube.com/results?search_query=ادارة+الوقت+للطلبة+تنظيم+الدراسة",
            "langue": "ar",
            "concept": L(
                "La méthode des blocs et la semaine type expliquées aux étudiants.",
                "The block method and typical week explained to students.",
                "منهجية الكتل والأسبوع النموذجي مشروحة للطلبة.",
            ),
        },
        {
            "titre": L(
                "Trello en 10 minutes : piloter un projet en équipe",
                "Trello in 10 minutes: run a team project",
                "Trello في 10 دقائق: قيادة مشروع جماعي",
            ),
            "url": "https://www.youtube.com/results?search_query=trello+tutoriel+francais+projet+equipe",
            "langue": "fr",
            "concept": L(
                "Listes, cartes, délais : le rituel hebdo qui évite les disputes.",
                "Lists, cards, deadlines: the weekly ritual avoiding fights.",
                "قوائم وبطاقات وآجال: الطقس الأسبوعي الذي يمنع الخلافات.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "25 + 5 : le bloc de base (effort + vraie pause sans écran).",
                "25 + 5: the basic block (effort + real screen-free break).",
                "25 + 5: الكتلة الأساسية (جهد + راحة حقيقية دون شاشة).",
            ),
            L(
                "1 grosse tâche par jour + 20 % de vide + dimanche tampon.",
                "1 big task per day + 20% empty + buffer Sunday.",
                "مهمة كبيرة واحدة يومياً + 20٪ فارغ + أحد احتياطي.",
            ),
            L(
                "Planning daté sur 4 semaines, suivi 20 min chaque dimanche.",
                "Dated 4-week schedule, 20-min tracking each Sunday.",
                "مخطط مؤرَّخ على 4 أسابيع، ومتابعة 20 دقيقة كل أحد.",
            ),
            L(
                "Notion : 1 base Modules + modèles + Ask AI.",
                "Notion: 1 Modules base + templates + Ask AI.",
                "Notion: قاعدة وحدات واحدة + قوالب + اسأل الذكاء.",
            ),
            L(
                "Trello : 1 carte = 1 micro-tâche + 1 responsable + 1 date.",
                "Trello: 1 card = 1 micro-task + 1 owner + 1 date.",
                "Trello: بطاقة = مهمة دقيقة + مسؤول + تاريخ.",
            ),
        ],
        "analogies": [
            L(
                "Le couscous des 6 plats : chaque plat a sa minuterie.",
                "The 6-dish couscous: each dish has its timer.",
                "كسكس الأطباق الستة: لكل طبق مؤقّته.",
            ),
            L(
                "Le rendez-vous avec vous-même : daté, on l'honore.",
                "The appointment with yourself: dated, you honour it.",
                "الموعد مع نفسك: مؤرَّخاً تُكرِمه.",
            ),
            L(
                "Le tableau de bord : voyant rouge = module en danger.",
                "The dashboard: red light = module in danger.",
                "لوحة القيادة: ضوء أحمر = وحدة في خطر.",
            ),
        ],
        "exemples": [
            L(
                "« Lundi 14h : psycho ch.2 (bloc 25+5 ×3) » au lieu de « réviser psycho ».",
                "\"Monday 2pm: psycho ch.2 (25+5 blocks ×3)\" instead of \"revise psycho\".",
                "« الاثنين 14:00: علم النفس ف2 (كتل 25+5 ×3) » بدل « راجع علم النفس ».",
            ),
            L(
                "Carte Trello : « Intro 8 lignes — Sara — vendredi ».",
                "Trello card: \"8-line intro — Sara — Friday\".",
                "بطاقة Trello: « مقدمة 8 أسطر — سارة — الجمعة ».",
            ),
            L(
                "Photo des notes papier → Notion → résumé en 5 puces.",
                "Paper notes photo → Notion → 5-bullet summary.",
                "صورة الملاحظات الورقية ← Notion ← ملخص في 5 نقاط.",
            ),
        ],
        "analogie_finale": L(
            "🏁 S'organiser avec l'IA, c'est comme avoir un copilote de rallye : il lit la carte, annonce les virages (les échéances) et recalcule après chaque détour — mais c'est vous qui tenez le volant.",
            "🏁 Organising with AI is like having a rally co-driver: he reads the map, calls corners (deadlines) and recalculates after each detour — but you hold the wheel.",
            "🏁 التنظيم بالذكاء كمساعد سائق رالي: يقرأ الخريطة، ويعلن المنعطفات (الاستحقاقات)، ويعيد الحساب بعد كل انحراف — لكنك أنت من يمسك المقود.",
        ),
        "quiz": [
            {
                "q": L(
                    "Que vaut une tâche sans date ?",
                    "What is a task without a date worth?",
                    "ما قيمة مهمة بلا تاريخ؟",
                ),
                "options": L(
                    ["Un vœu, pas un plan", "Un plan parfait", "Une urgence", "Une pause"],
                    ["A wish, not a plan", "A perfect plan", "An emergency", "A break"],
                    ["أمنية لا خطة", "خطة مثالية", "أمر عاجل", "راحة"],
                ),
                "answer": 0,
                "exp": L(
                    "Sans date ni créneau, la tâche sera repoussée par l'urgent : datée, elle devient rendez-vous.",
                    "Without date or slot, the task will be pushed by the urgent: dated, it becomes an appointment.",
                    "دون تاريخ وحصة سيدفعها العاجل: ومؤرَّخةً تصبح موعداً.",
                ),
            },
            {
                "q": L(
                    "Que fait-on le dimanche en 20 min ?",
                    "What do we do on Sunday in 20 min?",
                    "ماذا نفعل يوم الأحد في 20 دقيقة؟",
                ),
                "options": L(
                    ["Rien", "Cocher, reporter avec nouvelle date, régénérer la semaine", "Tout recommencer", "Supprimer le planning"],
                    ["Nothing", "Tick, postpone with new date, regenerate the week", "Restart everything", "Delete the schedule"],
                    ["لا شيء", "التأشير والتأجيل بتاريخ جديد وإعادة توليد الأسبوع", "إعادة كل شيء", "حذف المخطط"],
                ),
                "answer": 1,
                "exp": L(
                    "Le suivi hebdo transforme le planning en système vivant au lieu d'un vœu mort.",
                    "Weekly tracking turns the schedule into a living system instead of a dead wish.",
                    "المتابعة الأسبوعية تحوّل المخطط إلى نظام حي بدل أمنية ميتة.",
                ),
            },
            {
                "q": L(
                    "Que contient une bonne carte Trello ?",
                    "What does a good Trello card contain?",
                    "ماذا تحوي بطاقة Trello الجيدة؟",
                ),
                "options": L(
                    ["Tout l'exposé", "1 micro-tâche + 1 responsable + 1 date", "Seulement un titre", "Les disputes"],
                    ["The whole talk", "1 micro-task + 1 owner + 1 date", "Only a title", "The fights"],
                    ["العرض كله", "مهمة دقيقة + مسؤول + تاريخ", "عنوان فقط", "الخلافات"],
                ),
                "answer": 1,
                "exp": L(
                    "Micro-tâche + responsable + date = fini le « je croyais que c'était toi ».",
                    "Micro-task + owner + date = over with \"I thought it was you\".",
                    "مهمة دقيقة + مسؤول + تاريخ = انتهى « ظننت أنك أنت ».",
                ),
            },
            {
                "q": L(
                    "Pourquoi 20 % de vide dans le planning ?",
                    "Why 20% empty in the schedule?",
                    "لماذا 20٪ فارغ في المخطط؟",
                ),
                "options": L(
                    ["Paresse", "L'imprévu arrive toujours : le vide absorbe les retards", "Pour décorer", "C'est interdit"],
                    ["Laziness", "The unexpected always comes: emptiness absorbs delays", "For decoration", "It is forbidden"],
                    ["كسل", "الطارئ يأتي دائماً: الفراغ يمتص التأخر", "للزينة", "ممنوع"],
                ),
                "answer": 1,
                "exp": L(
                    "Un planning plein à 100 % casse au premier imprévu ; le tampon le rend robuste.",
                    "A 100%-full schedule breaks at the first surprise; the buffer makes it robust.",
                    "مخطط ممتلئ 100٪ ينكسر عند أول طارئ؛ والهامش يجعله متيناً.",
                ),
            },
            {
                "q": L(
                    "Quel prompt donne un VRAI planning ?",
                    "Which prompt gives a REAL schedule?",
                    "أي صياغة تعطي مخططاً حقيقياً؟",
                ),
                "options": L(
                    ["« Organise mes révisions »", "« 6 modules [liste], examens le [dates], 2h/jour : planning daté 4 semaines »", "« Motive-moi »", "« Fais tout »"],
                    ["\"Organise my revisions\"", "\"6 modules [list], exams on [dates], 2h/day: dated 4-week plan\"", "\"Motivate me\"", "\"Do everything\""],
                    ["« نظّم مراجعاتي »", "« 6 وحدات [اعرض]، امتحانات في [تواريخ]، ساعتان/يوم: مخطط مؤرَّخ 4 أسابيع »", "« حفّزني »", "« افعل كل شيء »"],
                ),
                "answer": 1,
                "exp": L(
                    "Contraintes concrètes + exigence de daté = calendrier applicable ; le vague donne du vague.",
                    "Concrete constraints + dated demand = applicable calendar; vague gives vague.",
                    "قيود ملموسة + طلب المؤرَّخ = تقويم قابل للتطبيق؛ والعام يعطي عاماً.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Ma semaine type : générer, afficher, faire valider en 30 secondes par le voisin.",
            "My typical week: generate, display, get validated in 30 seconds by neighbour.",
            "أسبوعي النموذجي: ولّد واعرض واجعل الجار يصادق في 30 ثانية.",
        ),
        L(
            "Base Modules : 6 lignes remplies (% , échéance, fiche liée) dans Notion ou sur papier.",
            "Modules base: 6 filled rows (%, deadline, linked sheet) in Notion or on paper.",
            "قاعدة الوحدات: 6 أسطر مملوءة (نسبة، استحقاق، بطاقة) في Notion أو على ورق.",
        ),
        L(
            "Défi Trello : découper l'exposé du groupe en 12 micro-tâches avec responsables et dates.",
            "Trello challenge: split the group talk into 12 micro-tasks with owners and dates.",
            "تحدّي Trello: تقسيم عرض المجموعة إلى 12 مهمة دقيقة بمسؤولين وتواريخ.",
        ),
        L(
            "Test 25+5 : un vrai chapitre en 3 blocs, téléphone loin, pause marchée.",
            "25+5 test: a real chapter in 3 blocks, phone away, walked break.",
            "اختبار 25+5: فصل حقيقي في 3 كتل، والهاتف بعيد، وراحة مشياً.",
        ),
    ],
    "retenir": [
        L(
            "25 + 5, 1 grosse tâche/jour, sommeil intouchable.",
            "25 + 5, 1 big task/day, untouchable sleep.",
            "25 + 5، ومهمة كبيرة/يوم، ونوم لا يُمَس.",
        ),
        L(
            "Planning daté 4 semaines + dimanche 20 min.",
            "Dated 4-week plan + Sunday 20 min.",
            "مخطط مؤرَّخ 4 أسابيع + أحد 20 دقيقة.",
        ),
        L(
            "Notion : base Modules + modèles + Ask AI.",
            "Notion: Modules base + templates + Ask AI.",
            "Notion: قاعدة الوحدات + قوالب + اسأل الذكاء.",
        ),
        L(
            "Trello : micro-tâche + responsable + date.",
            "Trello: micro-task + owner + date.",
            "Trello: مهمة دقيقة + مسؤول + تاريخ.",
        ),
        L(
            "20 % de vide : le tampon absorbe l'imprévu.",
            "20% empty: the buffer absorbs surprises.",
            "20٪ فارغ: الهامش يمتص الطارئ.",
        ),
    ],
    "glossaire": [
        {
            "term": "Timeboxing",
            "term_en": "Timeboxing",
            "def_fr": "Travailler en blocs fixes (25 min) suivis de pauses courtes, au lieu d'un temps flou.",
            "def_en": "Working in fixed blocks (25 min) followed by short breaks, instead of blurry time.",
            "def_ar": "العمل في كتل ثابتة (25 دقيقة) تليها راحات قصيرة، بدل وقت ضبابي.",
        },
        {
            "term": "Jour tampon",
            "term_en": "Buffer day",
            "def_fr": "Journée volontairement vide pour absorber retards et imprévus.",
            "def_en": "A deliberately empty day absorbing delays and surprises.",
            "def_ar": "يوم فارغ عمداً لامتصاص التأخر والطوارئ.",
        },
        {
            "term": "Base de données (Notion)",
            "term_en": "Database (Notion)",
            "def_fr": "Tableau vivant : chaque ligne (module) porte progression, échéance, fichiers.",
            "def_en": "A living table: each row (module) carries progress, deadline, files.",
            "def_ar": "جدول حي: كل سطر (وحدة) يحمل تقدماً واستحقاقاً وملفات.",
        },
        {
            "term": "Carte (Trello)",
            "term_en": "Card (Trello)",
            "def_fr": "Micro-tâche avec responsable, date et pièces jointes, déplacée entre listes.",
            "def_en": "A micro-task with owner, date and attachments, moved across lists.",
            "def_ar": "مهمة دقيقة بمسؤول وتاريخ ومرفقات، تُنقَل بين القوائم.",
        },
        {
            "term": "Ask AI",
            "term_en": "Ask AI",
            "def_fr": "Fonction de Notion qui résume et transforme vos notes en tâches datées.",
            "def_en": "Notion's feature summarising and turning your notes into dated tasks.",
            "def_ar": "خاصية Notion التي تلخّص ملاحظاتك وتحوّلها إلى مهام مؤرَّخة.",
        },
    ],
    "dialogues_fr": """# Séance 09 — Dialogues pédagogiques (Français)

## Dialogue A — « Mon semestre tient sur une page » (25 min)

**Personnages :** Yacine (étudiant débordé), Sara (camarade organisée), M. Amine (enseignant).

---

Yacine : Six modules, deux exposés, des partiels dans un mois… Je suis noyé !

Sara : Montre-moi ton planning.

Yacine : Quel planning ? Tout est dans ma tête.

Sara : Voilà la noyade. Donne ta liste à l'IA : modules, dates, 2 h libres par jour. Exige un planning DATÉ sur 4 semaines.

Yacine (lit) : « Semaine 1 : lundi 14h psycho ch.2, mardi 10h anglais temps… dimanche tampon. » C'est précis !

M. Amine : Et le rituel qui va avec : chaque dimanche, 20 minutes — cocher, reporter, régénérer. Sans ce rendez-vous, tout planning meurt en une semaine.

Yacine : Et mes notes papier en vrac ?

Sara : Photo → Notion → Ask AI : « transforme en tâches datées ». Ton bazar devient un tableau de bord.

---

## Dialogue B — « Qui fait quoi ? » (15 min)

**Personnages :** Trois étudiants (Nesrine, Bilal, Anis) devant un tableau Trello.

---

Nesrine : L'exposé est dans 10 jours et personne n'a commencé. Classique.

Bilal : On s'y met comment ? « Chacun fait sa partie » comme d'habitude ?

Anis : Non : comme d'habitude, ça finit en dispute. Trello : 3 listes, 12 micro-cartes. « Intro 8 lignes — Nesrine — vendredi », « Slides 5-8 — Bilal — lundi »…

Nesrine : Et le rituel : 10 minutes debout chaque semaine, chacun déplace ses cartes.

Bilal : Je croyais que c'était Anis qui faisait la conclusion…

Anis : Regarde la carte : « Conclusion — Bilal — mercredi ». Fini le « je croyais » : tout est écrit, daté, signé.

Nesrine : Un exposé sans dispute ? On aura tout vu !

---

## Mini-rôle à jouer (3 min par binôme)
L'un récite sa semaine « dans sa tête », l'autre la transforme en 5 lignes datées affichables. Échangez, puis affichez la semaine la plus claire de la classe.
""",
    "dialogues_en": """# Session 09 — Classroom dialogues (English)

## Dialogue A — "My semester fits on one page" (25 min)

**Characters:** Yacine (an overwhelmed student), Sara (an organised classmate), Mr Amine (teacher).

---

Yacine: Six modules, two talks, midterms in a month… I am drowning!

Sara: Show me your schedule.

Yacine: What schedule? Everything is in my head.

Sara: There is the drowning. Give your list to AI: modules, dates, 2 free hours a day. Demand a DATED 4-week plan.

Yacine (reading): "Week 1: Monday 2pm psycho ch.2, Tuesday 10am English tenses… buffer Sunday." That is precise!

Mr Amine: And the ritual with it: each Sunday, 20 minutes — tick, postpone, regenerate. Without this meeting, every schedule dies within a week.

Yacine: And my messy paper notes?

Sara: Photo → Notion → Ask AI: "turn into dated tasks". Your mess becomes a dashboard.

---

## Dialogue B — "Who does what?" (15 min)

**Characters:** Three students (Nesrine, Bilal, Anis) in front of a Trello board.

---

Nesrine: The talk is in 10 days and nobody started. Classic.

Bilal: How do we start? "Everyone does their part" as usual?

Anis: No: as usual ends in a fight. Trello: 3 lists, 12 micro-cards. "8-line intro — Nesrine — Friday", "Slides 5-8 — Bilal — Monday"…

Nesrine: And the ritual: 10 minutes standing weekly, everyone moves their cards.

Bilal: I thought Anis was doing the conclusion…

Anis: Look at the card: "Conclusion — Bilal — Wednesday". Over with "I thought": everything is written, dated, signed.

Nesrine: A talk without a fight? We will have seen everything!

---

## Mini role-play (3 min per pair)
One recites their week "in their head", the other turns it into 5 displayable dated lines. Swap, then display the class's clearest week.
""",
}
