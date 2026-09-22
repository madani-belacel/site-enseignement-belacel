# -*- coding: utf-8 -*-
"""Séance 08 — Rédaction académique, traduction et correction avec l'IA (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


SEANCE = {
    "num": 8,
    "slug": "seance-08",
    "icon": "✍️",
    "titles": L(
        "Rédaction académique, traduction et correction",
        "Academic writing, translation and proofreading",
        "الكتابة الأكاديمية والترجمة والتصحيح",
    ),
    "descriptions": L(
        "Améliorer un texte en français, anglais ou arabe, traduire sans trahir, corriger vite — et surtout éviter le plagiat en citant correctement.",
        "Improve a text in French, English or Arabic, translate without betraying, proofread fast — and above all avoid plagiarism by citing correctly.",
        "تحسين نص بالفرنسية أو الإنجليزية أو العربية، والترجمة دون خيانة، والتصحيح بسرعة — وتجنّب الانتحال خصوصاً بالاستشهاد الصحيح.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Faire relire un texte par l'IA : fautes, lourdeurs, registre académique.",
            "Have a text proofread by AI: mistakes, heaviness, academic register.",
            "أن يجعل الذكاء الاصطناعي يراجع نصاً: أخطاء، وركاكة، وسجل أكاديمي.",
        ),
        L(
            "Traduire FR ↔ EN ↔ AR en gardant le sens et en signalant les doutes.",
            "Translate FR ↔ EN ↔ AR keeping meaning and flagging doubts.",
            "أن يترجم فرنسية ↔ إنجليزية ↔ عربية محافظاً على المعنى ومشيراً للشكوك.",
        ),
        L(
            "Distinguer aider à écrire et faire écrire : la règle des 3 couches.",
            "Tell helping to write from writing for you: the 3-layer rule.",
            "أن يميّز بين المساعدة على الكتابة والكتابة بدلاً منه: قاعدة الطبقات الثلاث.",
        ),
        L(
            "Définir le plagiat et le paraphrasage, et savoir citer une source.",
            "Define plagiarism and paraphrasing, and know how to cite a source.",
            "أن يعرّف الانتحال وإعادة الصياغة، ويعرف كيف يستشهد بمصدر.",
        ),
        L(
            "Produire un paragraphe personnel vérifiable : idée + source + formulation.",
            "Produce a verifiable personal paragraph: idea + source + wording.",
            "أن ينتج فقرة شخصية قابلة للتحقق: فكرة + مصدر + صياغة.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 7 suivies. Venir avec un brouillon de texte (exposé, TD, mémoire).",
        "Sessions 1 to 7 completed. Come with a text draft (presentation, tutorial, thesis).",
        "إتمام الحصص من 1 إلى 7. الإتيان بمسودة نص (عرض، أعمال موجهة، مذكرة).",
    ),
    "accroche": {
        "question": L(
            "Si l'IA écrit votre introduction à votre place, à qui appartient votre note : à vous ou à la machine ? Et si elle se contente de corriger vos fautes ?",
            "If AI writes your introduction for you, whose grade is it: yours or the machine's? And if it only fixes your mistakes?",
            "إذا كتب الذكاء الاصطناعي مقدمتك بدلاً منك، فلمن العلامة: لك أم للآلة؟ وماذا لو اكتفى بتصحيح أخطائك؟",
        ),
        "analogie": L(
            "🍳 L'IA et votre texte, c'est comme le correcteur et le devoir : le correcteur souligne les fautes au crayon, mais c'est l'élève qui réécrit au propre. Si le correcteur écrit tout le devoir, ce n'est plus le vôtre.",
            "🍳 AI and your text is like the proofreader and the homework: the proofreader underlines mistakes in pencil, but the pupil rewrites neatly. If the proofreader writes all the homework, it is no longer yours.",
            "🍳 الذكاء الاصطناعي ونصّك كالمصحّح والواجب: المصحّح يضع خطاً تحت الأخطاء بالقلم، لكن التلميذ هو من يعيد الكتابة نظيفة. فإذا كتب المصحّح الواجب كله، لم يعد لك.",
        ),
        "phrase": L(
            "💡 Règle des 3 couches : l'IA peut corriger la forme (couche 1) et suggérer le plan (couche 2), mais les idées et les sources (couche 3) restent VOS responsabilités.",
            "💡 3-layer rule: AI may fix the form (layer 1) and suggest the outline (layer 2), but ideas and sources (layer 3) stay YOUR responsibilities.",
            "💡 قاعدة الطبقات الثلاث: يجوز للذكاء تصحيح الشكل (الطبقة 1) واقتراح الخطة (الطبقة 2)، لكن الأفكار والمصادر (الطبقة 3) تبقى مسؤوليتك أنت.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : à qui la note ?",
                "Hook: whose grade?",
                "انطلاقة: لمن العلامة؟",
            ),
            "detail": L(
                "Débat éclair : corriger vs écrire à ma place.",
                "Flash debate: fixing vs writing for me.",
                "نقاش خاطف: التصحيح مقابل الكتابة بدلاً مني.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : les 3 couches + le plagiat",
                "Explanation: 3 layers + plagiarism",
                "شرح: الطبقات الثلاث + الانتحال",
            ),
            "detail": L(
                "Forme, plan, idées-sources. Plagiat, paraphrase, citation : définitions et exemples.",
                "Form, outline, idea-sources. Plagiarism, paraphrase, citation: definitions and examples.",
                "الشكل، والخطة، والأفكار-المصادر. الانتحال وإعادة الصياغة والاستشهاد: تعريفات وأمثلة.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : corriger + traduire un vrai brouillon",
                "Demo: fix + translate a real draft",
                "عرض: تصحيح + ترجمة مسودة حقيقية",
            ),
            "detail": L(
                "Mauvais prompt vs bon prompt sur le brouillon d'un étudiant (FR/EN/AR).",
                "Bad prompt vs good prompt on a student's draft (FR/EN/AR).",
                "صياغة ضعيفة مقابل قوية على مسودة طالب (فرنسية/إنجليزية/عربية).",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : mon paragraphe vérifiable",
                "Guided exercise: my verifiable paragraph",
                "تمرين موجّه: فقرتي القابلة للتحقق",
            ),
            "detail": L(
                "Écrire 8 lignes : idée + source citée + formulation personnelle relue par l'IA.",
                "Write 8 lines: idea + cited source + personal wording proofread by AI.",
                "اكتب ثمانية أسطر: فكرة + مصدر مستشهَد + صياغة شخصية راجعها الذكاء.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : détecter le texte 100 % IA",
                "Demo 2: spot 100% AI text",
                "عرض 2: كشف النص المولّد كلياً",
            ),
            "detail": L(
                "Indices : généralités, aucune source, style lisse. Test collectif sur 2 paragraphes.",
                "Clues: generalities, no source, smooth style. Collective test on 2 paragraphs.",
                "القرائن: عموميات، لا مصادر، أسلوب أملس. اختبار جماعي على فقرتين.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et annonce de la séance 9",
                "Wrap-up, quiz and preview of session 9",
                "خلاصة واختبار وتقديم الحصة التاسعة",
            ),
            "detail": L(
                "« À retenir ». Annonce : organisation et gestion du temps avec l'IA.",
                "Key takeaways. Preview: organisation and time management with AI.",
                "« ما يجب تذكّره ». تقديم: التنظيم وتدبير الوقت بالذكاء الاصطناعي.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "La règle des 3 couches : ce que l'IA peut et ne peut pas",
                "The 3-layer rule: what AI can and cannot do",
                "قاعدة الطبقات الثلاث: ما يجوز للذكاء وما لا يجوز",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Tout texte académique a 3 couches. L'IA est excellente sur les deux premières, interdite sur la troisième sans votre travail.",
                        "Every academic text has 3 layers. AI is excellent on the first two, forbidden on the third without your work.",
                        "لكل نص أكاديمي ثلاث طبقات. يجيدها الذكاء في الأوليين، وممنوع في الثالثة دون جهدك.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Couche 1 — Forme (autorisée) :</strong> orthographe, grammaire, ponctuation, fluidité. « Corrige mes fautes et explique chacune. »",
                            "<strong>Couche 2 — Plan (autorisée avec contrôle) :</strong> suggestions d'ordre, transitions, titres. Vous choisissez.",
                            "<strong>Couche 3 — Idées + sources (VOTRE travail) :</strong> l'argument, l'exemple, la référence vérifiée. L'IA ne les invente pas pour vous.",
                        ],
                        [
                            "<strong>Layer 1 — Form (allowed):</strong> spelling, grammar, punctuation, flow. \"Fix my mistakes and explain each.\"",
                            "<strong>Layer 2 — Outline (allowed with control):</strong> order suggestions, transitions, headings. You choose.",
                            "<strong>Layer 3 — Ideas + sources (YOUR work):</strong> the argument, the example, the verified reference. AI does not invent them for you.",
                        ],
                        [
                            "<strong>الطبقة 1 — الشكل (مسموحة):</strong> إملاء، نحو، ترقيم، سلاسة. « صحّح أخطائي واشرح كل واحد ».",
                            "<strong>الطبقة 2 — الخطة (مسموحة بضبط):</strong> اقتراحات ترتيب وانتقالات وعناوين. وأنت تختار.",
                            "<strong>الطبقة 3 — الأفكار + المصادر (عملك أنت):</strong> الحجة والمثال والمرجع الموثق. لا يختلقها الذكاء بدلاً منك.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séances 3 et 5 :</strong> une idée sans source vérifiée (séance 3) ne rentre pas dans votre texte, et un script oral (séance 5) ne se lit pas comme un paragraphe écrit. Le texte académique marie les deux : idées sourcées + forme propre.",
                        "<strong>🔗 Reminder of sessions 3 and 5:</strong> an idea without a verified source (session 3) does not enter your text, and an oral script (session 5) does not read like a written paragraph. Academic text marries both: sourced ideas + clean form.",
                        "<strong>🔗 تذكير بالحصتين 3 و5:</strong> فكرة دون مصدر موثق (الحصة 3) لا تدخل نصّك، ونص شفهي (الحصة 5) لا يُقرَأ كفقرة مكتوبة. النص الأكاديمي يجمع الاثنين: أفكار موثقة + شكل سليم.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Corriger et améliorer : le crayon, pas la main",
                "Fix and improve: the pencil, not the hand",
                "التصحيح والتحسين: القلم لا اليد",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Envoyez votre brouillon, exigez des explications : chaque correction comprise est une faute en moins pour toujours.",
                        "Send your draft, demand explanations: each understood correction is one less mistake forever.",
                        "أرسل مسودتك، واطلب تفسيرات: كل تصحيح مفهوم خطأ أقل للأبد.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt correction :</strong> « Corrige ce texte [coller]. Liste chaque faute : règle + correction. Ne réécris pas tout. »",
                            "<strong>Prompt registre :</strong> « Transforme ce paragraphe oral en style académique, sans changer les idées : [coller]. »",
                            "<strong>Prompt concision :</strong> « Réduis ce texte de moitié en gardant les 3 idées : [coller]. »",
                            "<strong>En arabe :</strong> « صحّح الهمزات والتاء المربوطة واشرح كل قاعدة » — l'IA gère bien l'arabe standard.",
                        ],
                        [
                            "<strong>Fix prompt:</strong> \"Correct this text [paste]. List each mistake: rule + fix. Do not rewrite everything.\"",
                            "<strong>Register prompt:</strong> \"Turn this oral paragraph into academic style, keeping ideas: [paste].\"",
                            "<strong>Concision prompt:</strong> \"Halve this text keeping the 3 ideas: [paste].\"",
                            "<strong>In Arabic:</strong> ask for hamza and taa marbuta fixes with each rule — AI handles standard Arabic well.",
                        ],
                        [
                            "<strong>صياغة التصحيح:</strong> « صحّح هذا النص [الصق]. اعرض كل خطأ: القاعدة + التصحيح. لا تعِد كتابة كل شيء ».",
                            "<strong>صياغة السجل:</strong> « حوّل هذه الفقرة الشفهية إلى أسلوب أكاديمي دون تغيير الأفكار: [الصق] ».",
                            "<strong>صياغة الإيجاز:</strong> « اختصر هذا النص إلى النصف مع الحفاظ على الأفكار الثلاث: [الصق] ».",
                            "<strong>بالعربية:</strong> « صحّح الهمزات والتاء المربوطة واشرح كل قاعدة » — يجيد الذكاء العربية الفصحى.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> brouillon « les enfants apprend mieux quand il joue » → fautes : accord (apprennent), pronom (ils) → version propre. Puis traduction EN avec [doute] sur « étayage » → glossaire : « scaffolding ».",
                        "<strong>🧪 Concrete example:</strong> draft \"les enfants apprend mieux quand il joue\" → mistakes: agreement (apprennent), pronoun (ils) → clean version. Then EN translation with [doubt] on \"étayage\" → glossary: \"scaffolding\".",
                        "<strong>🧪 مثال ملموس:</strong> مسودة « les enfants apprend mieux quand il joue » ← أخطاء: المطابقة (apprennent) والضمير (ils) ← نسخة سليمة. ثم ترجمة إنجليزية مع [شك] على « étayage » ← المسرد: « scaffolding ».",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Traduire sans trahir : FR ↔ EN ↔ AR",
                "Translate without betraying: FR ↔ EN ↔ AR",
                "الترجمة دون خيانة: فرنسية ↔ إنجليزية ↔ عربية",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Traduire, c'est décider : mot à mot (fidèle mais lourd) ou sens à sens (fluide mais risqué). L'IA fait les deux — demandez-lui de signaler ses doutes.",
                        "Translating is deciding: word for word (faithful but heavy) or sense for sense (fluent but risky). AI does both — ask it to flag doubts.",
                        "الترجمة قرار: حرفية (أمينة لكن ثقيلة) أو معنوية (سلسة لكن محفوفة). يجيد الذكاء الاثنتين — اطلب منه الإشارة إلى شكوكه.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt traduction :</strong> « Traduis en anglais académique. Mets [doute] sur les termes incertains et propose 2 options : [coller]. »",
                            "<strong>Retour obligatoire :</strong> retraduire vers la langue d'origine pour vérifier que le sens a survécu.",
                            "<strong>Termes pédagogiques :</strong> « différenciation », « étayage », « évaluation formative » — vérifier dans un glossaire, pas seulement l'IA.",
                        ],
                        [
                            "<strong>Translation prompt:</strong> \"Translate into academic English. Mark [doubt] on uncertain terms and suggest 2 options: [paste].\"",
                            "<strong>Mandatory back-check:</strong> translate back to the source language to verify meaning survived.",
                            "<strong>Pedagogy terms:</strong> \"differentiation\", \"scaffolding\", \"formative assessment\" — check a glossary, not only AI.",
                        ],
                        [
                            "<strong>صياغة الترجمة:</strong> « ترجم إلى إنجليزية أكاديمية. ضع [شك] على المصطلحات غير المؤكدة واقترح خيارين: [الصق] ».",
                            "<strong>المراجعة العكسية إلزامية:</strong> أعد الترجمة إلى لغة الأصل للتحقق من بقاء المعنى.",
                            "<strong>مصطلحات بيداغوجية:</strong> « التفريد »، « السقالة التعليمية »، « التقييم التكويني » — تحقق في مسرد لا بالذكاء وحده.",
                        ],
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Plagiat, paraphrase, citation : les définitions qui protègent",
                "Plagiarism, paraphrase, citation: the definitions that protect",
                "الانتحال وإعادة الصياغة والاستشهاد: تعريفات تحميك",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Le plagiat, c'est présenter le travail d'autrui comme le vôtre — y compris un texte 100 % généré par l'IA que vous signez. La parade : paraphraser + citer.",
                        "Plagiarism is presenting others' work as yours — including a 100% AI-generated text you sign. The shield: paraphrase + cite.",
                        "الانتحال تقديم عمل الغير كأنه لك — بما فيه نص مولّد كلياً بالذكاء توقّعه. والدرع: إعادة الصياغة + الاستشهاد.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Copier-coller :</strong> même 3 phrases sans guillemets ni source = plagiat.",
                            "<strong>Paraphrase honnête :</strong> redire l'idée avec VOS mots + citer l'auteur (nom, année).",
                            "<strong>Citation :</strong> « … » + (Auteur, année, page). Vérifier que la source existe (Scholar).",
                            "<strong>Texte IA :</strong> s'il a écrit le paragraphe, ce n'est pas votre formulation — réécrivez et citez vos VRAIES sources.",
                        ],
                        [
                            "<strong>Copy-paste:</strong> even 3 sentences without quotes or source = plagiarism.",
                            "<strong>Honest paraphrase:</strong> restate the idea in YOUR words + cite the author (name, year).",
                            "<strong>Citation:</strong> \"…\" + (Author, year, page). Check the source exists (Scholar).",
                            "<strong>AI text:</strong> if it wrote the paragraph, it is not your wording — rewrite and cite your REAL sources.",
                        ],
                        [
                            "<strong>النسخ واللصق:</strong> حتى ثلاث جمل دون تنصيص أو مصدر = انتحال.",
                            "<strong>إعادة الصياغة النزيهة:</strong> أعد الفكرة بكلماتك + استشهد بالمؤلف (اسم، سنة).",
                            "<strong>الاستشهاد:</strong> « … » + (المؤلف، السنة، الصفحة). تحقق أن المصدر موجود (Scholar).",
                            "<strong>نص الذكاء:</strong> إذا كتب الفقرة فليست صياغتك — أعد الكتابة واستشهد بمصادرك الحقيقية.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>⚠️ Sanctions réelles :</strong> zéro au devoir, conseil de discipline, exclusion. Les détecteurs repèrent le style « lisse et sans source » typique de l'IA.",
                        "<strong>⚠️ Real sanctions:</strong> zero on the assignment, disciplinary board, expulsion. Detectors spot the typical \"smooth and sourceless\" AI style.",
                        "<strong>⚠️ عقوبات حقيقية:</strong> صفر في الواجب، مجلس تأديبي، فصل. الكواشف تلتقط أسلوب الذكاء « الأملس بلا مصادر ».",
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
                        "Boucle vertueuse : brouillon personnel → correction expliquée → réécriture → traduction vérifiée → citation des sources.",
                        "Virtuous loop: personal draft → explained correction → rewrite → verified translation → source citation.",
                        "حلقة فاضلة: مسودة شخصية ← تصحيح مفسَّر ← إعادة كتابة ← ترجمة موثقة ← استشهاد بالمصادر.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 9 :</strong> un bon texte arrive à l'heure : le planning 4 semaines (séance 9) réservera des créneaux « rédaction + relecture + citation » pour chaque devoir.",
                        "<strong>➡️ Bridge to session 9:</strong> a good text arrives on time: the 4-week schedule (session 9) will book \"writing + proofreading + citation\" slots for each assignment.",
                        "<strong>➡️ جسر إلى الحصة 9:</strong> النص الجيد يصل في وقته: مخطط الأسابيع الأربعة (الحصة 9) سيحجز حصص « كتابة + مراجعة + استشهاد » لكل واجب.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Brouillon d'abord :</strong> toujours écrire vous-même avant de solliciter l'IA.",
                            "<strong>✅ Explications exigées :</strong> chaque correction doit s'accompagner de sa règle.",
                            "<strong>✅ Double sens :</strong> toute traduction est vérifiée par retour.",
                            "<strong>✅ Sources réelles :</strong> chaque idée empruntée est citée et vérifiée.",
                        ],
                        [
                            "<strong>✅ Draft first:</strong> always write yourself before calling AI.",
                            "<strong>✅ Explanations required:</strong> each fix must come with its rule.",
                            "<strong>✅ Both directions:</strong> every translation is back-checked.",
                            "<strong>✅ Real sources:</strong> each borrowed idea is cited and verified.",
                        ],
                        [
                            "<strong>✅ المسودة أولاً:</strong> اكتب بنفسك دائماً قبل استدعاء الذكاء.",
                            "<strong>✅ تفسيرات إلزامية:</strong> كل تصحيح مع قاعدته.",
                            "<strong>✅ الاتجاهان:</strong> كل ترجمة تُراجَع عكسياً.",
                            "<strong>✅ مصادر حقيقية:</strong> كل فكرة مقترَضة مستشهَدة وموثقة.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> signer un texte 100 % IA, traduire sans vérification retour, citer une référence inventée par le chatbot.",
                        "<strong>❌ Mistakes to avoid:</strong> signing a 100% AI text, translating without back-check, citing a chatbot-invented reference.",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> توقيع نص مولّد كلياً، والترجمة دون مراجعة عكسية، والاستشهاد بمرجع مختلَق.",
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
                            ["Demande", "« Écris mon introduction de 20 lignes. »", "« Voici mon brouillon [coller]. Corrige les fautes, explique chaque règle, suggère 2 transitions. »"],
                            ["Résultat", "Texte signé mais pas écrit : plagiat de machine.", "Mon texte, amélioré et compris, avec mes sources."],
                        ],
                        [
                            ["Prompt", "\"Write my 20-line introduction.\"", "\"Here is my draft [paste]. Fix mistakes, explain each rule, suggest 2 transitions.\""],
                            ["Result", "Signed but unwritten text: machine plagiarism.", "My text, improved and understood, with my sources."],
                        ],
                        [
                            ["الطلب", "« اكتب مقدمتي من عشرين سطراً »", "« هذه مسودتي [الصق]. صحّح الأخطاء واشرح كل قاعدة واقترح رابطين »"],
                            ["النتيجة", "نص موقَّع غير مكتوب: انتحال آلي.", "نصّي محسّناً ومفهوماً، مع مصادري."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Que dit la règle des 3 couches ?",
                "What does the 3-layer rule say?",
                "ماذا تقول قاعدة الطبقات الثلاث؟",
            ),
            "r": L(
                "Forme : l'IA corrige. Plan : elle suggère, vous choisissez. Idées + sources : votre travail exclusif.",
                "Form: AI fixes. Outline: it suggests, you choose. Ideas + sources: your exclusive work.",
                "الشكل: الذكاء يصحّح. الخطة: يقترح وأنت تختار. الأفكار + المصادر: عملك الخالص.",
            ),
        },
        {
            "q": L(
                "Pourquoi la traduction retour est-elle obligatoire ?",
                "Why is back-translation mandatory?",
                "لماذا الترجمة العكسية إلزامية؟",
            ),
            "r": L(
                "Parce qu'elle révèle les glissements de sens : si le retour diffère de l'original, la traduction a trahi.",
                "Because it reveals meaning shifts: if the return differs from the original, the translation betrayed.",
                "لأنها تكشف انزلاقات المعنى: إذا اختلف العائد عن الأصل، فقد خانت الترجمة.",
            ),
        },
        {
            "q": L(
                "Signer un texte 100 % généré par l'IA, c'est… ?",
                "Signing a 100% AI-generated text is…?",
                "توقيع نص مولّد كلياً بالذكاء هو…؟",
            ),
            "r": L(
                "Du plagiat (de machine) : sanction zéro + discipline. La parade : écrire soi-même, faire corriger, citer ses sources.",
                "Plagiarism (by machine): zero sanction + discipline. The shield: write yourself, get corrected, cite sources.",
                "انتحال (آلي): عقوبته الصفر والتأديب. والدرع: اكتب بنفسك، وصحّح، واستشهد بمصادرك.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "Prenez votre brouillon : 1) faites-le corriger (fautes + règles) ; 2) traduisez un paragraphe avec balises [doute] ; 3) vérifiez par retour ; 4) ajoutez 1 citation réelle vérifiée sur Scholar.",
            "Take your draft: 1) have it corrected (mistakes + rules); 2) translate a paragraph with [doubt] tags; 3) back-check; 4) add 1 real citation verified on Scholar.",
            "خذ مسودتك: 1) صحّحها (أخطاء + قواعد)؛ 2) ترجم فقرة مع وسم [شك]؛ 3) راجع عكسياً؛ 4) أضف استشهاداً حقيقياً موثقاً في Scholar.",
        ),
        "demarche": L(
            "1) Coller le brouillon + prompt correction. 2) Recopier 3 règles apprises dans le carnet. 3) Traduire avec doutes signalés. 4) Retraduire et comparer. 5) Chercher la source sur Scholar et formater (Auteur, année).",
            "1) Paste draft + correction prompt. 2) Copy 3 learned rules into the notebook. 3) Translate with flagged doubts. 4) Translate back and compare. 5) Find the source on Scholar and format (Author, year).",
            "1) الصق المسودة + صياغة التصحيح. 2) انسخ 3 قواعد متعلَّمة في الدفتر. 3) ترجم مع شكوك موسومة. 4) أعد الترجمة وقارن. 5) جد المصدر في Scholar ونسّق (المؤلف، السنة).",
        ),
        "solution": L(
            "Réussi si : 3 règles notées et comprises, traduction retour identique au sens, 1 citation (auteur, année, page) retrouvée sur Scholar, et le texte final reste le vôtre (vos idées, vos exemples).",
            "Success if: 3 rules noted and understood, back-translation identical in meaning, 1 citation (author, year, page) found on Scholar, and the final text stays yours (your ideas, your examples).",
            "نجاح إذا: 3 قواعد مدوّنة ومفهومة، وترجمة عكسية مطابقة المعنى، واستشهاد واحد (مؤلف، سنة، صفحة) موجود في Scholar، والنص النهائي يبقى لك (أفكارك وأمثلتك).",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Éviter le plagiat : citer et paraphraser (tutoriel)",
                "Avoid plagiarism: cite and paraphrase (tutorial)",
                "تجنّب الانتحال: الاستشهاد وإعادة الصياغة (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=eviter+plagiat+universite+citer+paraphraser",
            "langue": "fr",
            "concept": L(
                "Les règles universitaires du « citer juste » avec des exemples concrets.",
                "University rules of \"citing right\" with concrete examples.",
                "قواعد الجامعة في « الاستشهاد الصحيح » بأمثلة ملموسة.",
            ),
        },
        {
            "titre": L(
                "الكتابة الأكاديمية: كيف تكتب فقرة علمية سليمة",
                "Academic writing: how to write a sound scholarly paragraph",
                "الكتابة الأكاديمية: كيف تكتب فقرة علمية سليمة",
            ),
            "url": "https://www.youtube.com/results?search_query=الكتابة+الأكاديمية+الفقرة+العلمية+شرح",
            "langue": "ar",
            "concept": L(
                "Structure d'une فقرة : idée, preuve, exemple, transition.",
                "Structure of a paragraph: idea, proof, example, transition.",
                "بنية الفقرة: فكرة، دليل، مثال، انتقال.",
            ),
        },
        {
            "titre": L(
                "Traduire avec l'IA sans trahir le sens (méthode)",
                "Translate with AI without betraying meaning (method)",
                "الترجمة بالذكاء دون خيانة المعنى (منهجية)",
            ),
            "url": "https://www.youtube.com/results?search_query=traduire+deepl+chatgpt+sans+erreur+methode",
            "langue": "fr",
            "concept": L(
                "La vérification retour démontrée pas à pas sur un texte réel.",
                "Back-checking demonstrated step by step on a real text.",
                "المراجعة العكسية موضّحة خطوة بخطوة على نص حقيقي.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "3 couches : forme (IA corrige), plan (elle suggère), idées-sources (vous).",
                "3 layers: form (AI fixes), outline (it suggests), idea-sources (you).",
                "3 طبقات: الشكل (الذكاء يصحّح)، والخطة (يقترح)، والأفكار-المصادر (أنت).",
            ),
            L(
                "Correction : toujours exiger la règle avec la faute.",
                "Correction: always demand the rule with the mistake.",
                "التصحيح: اطلب القاعدة مع الخطأ دائماً.",
            ),
            L(
                "Traduction : baliser les doutes + vérification retour obligatoire.",
                "Translation: flag doubts + mandatory back-check.",
                "الترجمة: وسم الشكوك + مراجعة عكسية إلزامية.",
            ),
            L(
                "Paraphrase honnête = vos mots + citation (auteur, année).",
                "Honest paraphrase = your words + citation (author, year).",
                "إعادة الصياغة النزيهة = كلماتك + استشهاد (مؤلف، سنة).",
            ),
            L(
                "Texte 100 % IA signé = plagiat = zéro + discipline.",
                "100% AI text signed = plagiarism = zero + discipline.",
                "نص مولّد كلياً موقَّع = انتحال = صفر + تأديب.",
            ),
        ],
        "analogies": [
            L(
                "Le correcteur au crayon : il souligne, vous réécrivez.",
                "The pencil proofreader: he underlines, you rewrite.",
                "المصحّح بالقلم: يضع خطاً، وأنت تعيد الكتابة.",
            ),
            L(
                "La traduction comme un pont : on le teste dans les deux sens avant de le traverser.",
                "Translation like a bridge: tested both ways before crossing.",
                "الترجمة كجسر: يُختبَر في الاتجاهين قبل عبوره.",
            ),
            L(
                "La citation comme une adresse : sans elle, l'idée est perdue.",
                "Citation like an address: without it, the idea is lost.",
                "الاستشهاد كعنوان: بدونه تضيع الفكرة.",
            ),
        ],
        "exemples": [
            L(
                "« Corrige et explique chaque faute, ne réécris pas tout » → 3 règles apprises.",
                "\"Fix and explain each mistake, do not rewrite everything\" → 3 rules learned.",
                "« صحّح واشرح كل خطأ، لا تعِد كتابة كل شيء » ← 3 قواعد متعلَّمة.",
            ),
            L(
                "« différenciation » traduit puis vérifié en glossaire + retour.",
                "\"Differentiation\" translated then checked in glossary + back.",
                "« التفريد » مترجَم ثم موثق في مسرد + عكسياً.",
            ),
            L(
                "(Vygotsky, 1978) retrouvé sur Scholar avant d'être cité.",
                "(Vygotsky, 1978) found on Scholar before being cited.",
                "(فيغوتسكي، 1978) موجود في Scholar قبل الاستشهاد به.",
            ),
        ],
        "analogie_finale": L(
            "🏁 Votre texte et l'IA, c'est comme votre maison et le peintre : il peut repeindre les murs (la forme), suggérer une couleur (le plan), mais les fondations et les meubles (vos idées, vos sources), c'est vous qui les avez bâtis — et la maison reste la vôtre.",
            "🏁 Your text and AI is like your house and the painter: he may repaint walls (form), suggest a colour (outline), but foundations and furniture (your ideas, sources) were built by you — and the house stays yours.",
            "🏁 نصّك والذكاء كبيتك والدهّان: يجوز أن يعيد طلاء الجدران (الشكل)، ويقترح لوناً (الخطة)، لكن الأساسات والأثاث (أفكارك ومصادرك) بنيتَها أنت — والبيت يبقى بيتك.",
        ),
        "quiz": [
            {
                "q": L(
                    "Que permet la couche 1 (forme) ?",
                    "What does layer 1 (form) allow?",
                    "ماذا تجيز الطبقة 1 (الشكل)؟",
                ),
                "options": L(
                    ["Corriger fautes et fluidité avec explications", "Inventer vos idées", "Créer de fausses sources", "Écrire tout le devoir"],
                    ["Fix mistakes and flow with explanations", "Invent your ideas", "Create fake sources", "Write the whole assignment"],
                    ["تصحيح الأخطاء والسلاسة مع تفسيرات", "اختلاق أفكارك", "خلق مصادر مزيفة", "كتابة الواجب كله"],
                ),
                "answer": 0,
                "exp": L(
                    "La forme est le domaine légitime de l'IA ; les idées et sources restent les vôtres.",
                    "Form is AI's legitimate domain; ideas and sources stay yours.",
                    "الشكل هو المجال المشروع للذكاء؛ والأفكار والمصادر تبقى لك.",
                ),
            },
            {
                "q": L(
                    "Que faire des termes marqués [doute] en traduction ?",
                    "What to do with [doubt]-marked terms in translation?",
                    "ماذا تفعل بالمصطلحات الموسومة [شك] في الترجمة؟",
                ),
                "options": L(
                    ["Les ignorer", "Les vérifier en glossaire + traduction retour", "Les supprimer", "Changer de langue"],
                    ["Ignore them", "Check them in a glossary + back-translation", "Delete them", "Change language"],
                    ["تجاهلها", "تحقق منها في مسرد + ترجمة عكسية", "احذفها", "غيّر اللغة"],
                ),
                "answer": 1,
                "exp": L(
                    "Le doute signalé + la vérification retour transforment le risque en contrôle qualité.",
                    "Flagged doubt + back-check turn risk into quality control.",
                    "الشك الموسوم + المراجعة العكسية يحوّلان الخطر إلى ضبط جودة.",
                ),
            },
            {
                "q": L(
                    "Qu'est-ce qu'une paraphrase honnête ?",
                    "What is an honest paraphrase?",
                    "ما إعادة الصياغة النزيهة؟",
                ),
                "options": L(
                    ["Copier 3 phrases", "Redire l'idée avec vos mots + citer (auteur, année)", "Changer 2 mots", "Traduire sans citer"],
                    ["Copy 3 sentences", "Restate the idea in your words + cite (author, year)", "Change 2 words", "Translate without citing"],
                    ["نسخ 3 جمل", "إعادة الفكرة بكلماتك + الاستشهاد (مؤلف، سنة)", "تغيير كلمتين", "الترجمة دون استشهاد"],
                ),
                "answer": 1,
                "exp": L(
                    "Vos mots + la source = honnête. Mêmes mots sans source = plagiat, même avec 2 mots changés.",
                    "Your words + source = honest. Same words without source = plagiarism, even with 2 words changed.",
                    "كلماتك + المصدر = نزيه. نفس الكلمات دون مصدر = انتحال، ولو غُيّرت كلمتان.",
                ),
            },
            {
                "q": L(
                    "Une référence inventée par le chatbot, citée dans votre devoir : quel risque ?",
                    "A chatbot-invented reference cited in your work: what risk?",
                    "مرجع مختلَق من الروبوت مستشهَد في واجبك: ما الخطر؟",
                ),
                "options": L(
                    ["Aucun", "Zéro + accusation de fraude : la source n'existe pas", "Bonus d'originalité", "Rien, personne ne vérifie"],
                    ["None", "Zero + fraud accusation: the source does not exist", "Originality bonus", "Nothing, nobody checks"],
                    ["لا شيء", "صفر + اتهام بالغش: المصدر غير موجود", "مكافأة أصالة", "لا شيء، لا أحد يتحقق"],
                ),
                "answer": 1,
                "exp": L(
                    "Vérifier chaque citation sur Scholar avant de la citer : 2 minutes qui sauvent un semestre.",
                    "Check each citation on Scholar before citing: 2 minutes saving a semester.",
                    "تحقق من كل استشهاد في Scholar قبل ذكره: دقيقتان تنقذان فصلاً.",
                ),
            },
            {
                "q": L(
                    "Quel est l'ordre de la boucle vertueuse ?",
                    "What is the virtuous loop order?",
                    "ما ترتيب الحلقة الفاضلة؟",
                ),
                "options": L(
                    ["IA d'abord, moi jamais", "Brouillon personnel → correction expliquée → réécriture → citation", "Copier → signer → rendre", "Traduire → plagier"],
                    ["AI first, me never", "Personal draft → explained correction → rewrite → citation", "Copy → sign → submit", "Translate → plagiarise"],
                    ["الذكاء أولاً وأنا أبداً", "مسودة شخصية ← تصحيح مفسَّر ← إعادة كتابة ← استشهاد", "انسخ ← وقّع ← سلّم", "ترجم ← انتحل"],
                ),
                "answer": 1,
                "exp": L(
                    "Vous écrivez, l'IA corrige et explique, vous réécrivez et citez : le texte final est le vôtre.",
                    "You write, AI corrects and explains, you rewrite and cite: the final text is yours.",
                    "أنت تكتب، والذكاء يصحّح ويفسّر، وأنت تعيد الكتابة وتستشهد: النص النهائي لك.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Correction croisée : brouillon corrigé par l'IA, règles expliquées au voisin sans écran.",
            "Cross-correction: AI-corrected draft, rules explained to neighbour without screen.",
            "تصحيح متبادل: مسودة صحّحها الذكاء، والقواعد تُشرَح للجار دون شاشة.",
        ),
        L(
            "Défi traduction : même paragraphe en EN puis retour FR, comparer les glissements.",
            "Translation challenge: same paragraph to EN then back to FR, compare shifts.",
            "تحدّي الترجمة: نفس الفقرة إلى الإنجليزية ثم عكسياً، وقارن الانزلاقات.",
        ),
        L(
            "Chasse à la source : 2 citations à vérifier sur Scholar, dont 1 inventée par l'IA.",
            "Source hunt: 2 citations to check on Scholar, including 1 AI-invented.",
            "صيد المصادر: استشهادان للتحقق في Scholar، أحدهما مختلَق من الذكاء.",
        ),
        L(
            "Paragraphe vérifiable : 8 lignes (idée + source + formulation) relues par l'IA.",
            "Verifiable paragraph: 8 lines (idea + source + wording) proofread by AI.",
            "فقرة قابلة للتحقق: ثمانية أسطر (فكرة + مصدر + صياغة) راجعها الذكاء.",
        ),
    ],
    "retenir": [
        L(
            "3 couches : forme OK, plan contrôlé, idées-sources à vous.",
            "3 layers: form OK, outline controlled, idea-sources yours.",
            "3 طبقات: الشكل مسموح، والخطة مضبوطة، والأفكار-المصادر لك.",
        ),
        L(
            "Correction = faute + règle, jamais de réécriture totale.",
            "Correction = mistake + rule, never total rewrite.",
            "التصحيح = خطأ + قاعدة، لا إعادة كتابة كلية أبداً.",
        ),
        L(
            "Traduction = doutes balisés + retour obligatoire.",
            "Translation = flagged doubts + mandatory back-check.",
            "الترجمة = شكوك موسومة + مراجعة عكسية إلزامية.",
        ),
        L(
            "Paraphrase = vos mots + (auteur, année) vérifiée.",
            "Paraphrase = your words + verified (author, year).",
            "إعادة الصياغة = كلماتك + (مؤلف، سنة) موثقة.",
        ),
        L(
            "100 % IA signé = plagiat = zéro.",
            "100% AI signed = plagiarism = zero.",
            "المولّد كلياً الموقَّع = انتحال = صفر.",
        ),
    ],
    "glossaire": [
        {
            "term": "Plagiat",
            "term_en": "Plagiarism",
            "def_fr": "Présenter le travail d'autrui (ou d'une machine) comme le vôtre, sans citer.",
            "def_en": "Presenting others' (or a machine's) work as yours, without citing.",
            "def_ar": "تقديم عمل الغير (أو الآلة) كأنه لك دون استشهاد.",
        },
        {
            "term": "Paraphrase",
            "term_en": "Paraphrase",
            "def_fr": "Redire une idée avec vos propres mots, en citant toujours la source.",
            "def_en": "Restating an idea in your own words, always citing the source.",
            "def_ar": "إعادة قول فكرة بكلماتك الخاصة، مع الاستشهاد بالمصدر دائماً.",
        },
        {
            "term": "Citation",
            "term_en": "Citation",
            "def_fr": "Reprise exacte entre guillemets + référence (auteur, année, page).",
            "def_en": "Exact borrowing in quotes + reference (author, year, page).",
            "def_ar": "نقل حرفي بين علامتي تنصيص + مرجع (مؤلف، سنة، صفحة).",
        },
        {
            "term": "Registre académique",
            "term_en": "Academic register",
            "def_fr": "Style formel et précis des travaux universitaires (pas d'oral, pas de familiarités).",
            "def_en": "The formal, precise style of university work (no spoken language, no slang).",
            "def_ar": "الأسلوب الرسمي الدقيق للأعمال الجامعية (لا شفهية ولا عامية).",
        },
        {
            "term": "Traduction retour",
            "term_en": "Back-translation",
            "def_fr": "Retraduire vers la langue d'origine pour vérifier que le sens a survécu.",
            "def_en": "Translating back to the source language to verify meaning survived.",
            "def_ar": "إعادة الترجمة إلى لغة الأصل للتحقق من بقاء المعنى.",
        },
    ],
    "dialogues_fr": """# Séance 08 — Dialogues pédagogiques (Français)

## Dialogue A — « Le correcteur au crayon » (25 min)

**Personnages :** Rania (étudiante), M. Yacine (enseignant), l'IA (jouée par un camarade).

---

Rania : Monsieur, l'IA a écrit mon introduction. Elle est magnifique !

M. Yacine : Magnifique… mais de qui ? Lis-moi ta phrase préférée et explique-moi le mot « épistémologique » que tu as employé.

Rania : Euh… je ne sais pas ce qu'il veut dire exactement.

M. Yacine : Alors ce n'est pas ton texte. Reprenons : écris TOI 8 lignes, puis demande seulement correction + explications.

Rania (nouveau brouillon) : « Voici mon texte. Corrige les fautes, explique chaque règle, ne réécris pas tout. »

IA : Faute 1 : accord du participe… Règle : … Faute 2 : …

Rania : Cette fois, chaque correction est une leçon. Et les idées sont les miennes !

M. Yacine : Exactement : le crayon souligne, la main réécrit. La main, c'est toi.

---

## Dialogue B — « La référence fantôme » (15 min)

**Personnages :** Karim (étudiant), Sara (camarade vérificatrice), l'écran Scholar (joué par un camarade).

---

Karim : Ma bibliographie est impressionnante : 5 références données par le chatbot !

Sara : Vérifions sur Scholar. Référence 1… introuvable. Référence 2… l'auteur existe mais l'article n'existe pas !

Karim : Mais le chatbot avait l'air si sûr…

Sara : Confiance n'est pas vérité (séance 1, tu te souviens ?). Une référence non retrouvée = une référence inventée = fraude si tu la cites.

Karim : Je supprime les 5 et je recommence : Perplexity pour trouver, Scholar pour vérifier, puis je cite (auteur, année, page).

Sara : Et cette fois, ta bibliographie sera courte… mais réelle. Un lion réel vaut mieux que cinq licornes.

---

## Mini-rôle à jouer (3 min par binôme)
L'un présente un paragraphe « parfait » mais sans source, l'autre joue le jury : « Quelle est votre source ? Prouvez qu'elle existe. » Échangez, puis listez les 3 questions d'un bon jury.
""",
    "dialogues_en": """# Session 08 — Classroom dialogues (English)

## Dialogue A — "The pencil proofreader" (25 min)

**Characters:** Rania (student), Mr Yacine (teacher), the AI (played by a classmate).

---

Rania: Sir, AI wrote my introduction. It is magnificent!

Mr Yacine: Magnificent… but whose? Read me your favourite sentence and explain the word "epistemological" you used.

Rania: Er… I do not know exactly what it means.

Mr Yacine: Then it is not your text. Start over: write 8 lines YOURSELF, then ask only for correction + explanations.

Rania (new draft): "Here is my text. Fix mistakes, explain each rule, do not rewrite everything."

AI: Mistake 1: participle agreement… Rule:… Mistake 2:…

Rania: This time, each correction is a lesson. And the ideas are mine!

Mr Yacine: Exactly: the pencil underlines, the hand rewrites. The hand is you.

---

## Dialogue B — "The ghost reference" (15 min)

**Characters:** Karim (student), Sara (checker classmate), the Scholar screen (played by a classmate).

---

Karim: My bibliography is impressive: 5 references from the chatbot!

Sara: Let us check on Scholar. Reference 1… not found. Reference 2… the author exists but the paper does not!

Karim: But the chatbot looked so sure…

Sara: Confidence is not truth (session 1, remember?). An unfound reference = an invented reference = fraud if you cite it.

Karim: I delete all 5 and restart: Perplexity to find, Scholar to verify, then I cite (author, year, page).

Sara: And this time, your bibliography will be short… but real. A real lion beats five unicorns.

---

## Mini role-play (3 min per pair)
One presents a "perfect" paragraph with no source, the other plays the jury: "What is your source? Prove it exists." Swap, then list a good jury's 3 questions.
""",
}
