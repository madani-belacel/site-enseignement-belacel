# -*- coding: utf-8 -*-
"""Séance 07 — IA et programmation : mini-projet Python avec une API d'IA (PEP 2A — ENS).
Pédagogie : accroche → explication pas à pas → démonstration → exercice → résumé.
"""


def L(fr, en, ar):
    return {"fr": fr, "en": en, "ar": ar}


CODE_ASSISTANT = """# assistant_chat.py -- mini assistant IA (projet seance 07)
# Installation : python -m pip install google-generativeai
import google.generativeai as genai

# 1. Cle gratuite sur https://ai.google.dev (ne jamais la partager !)
genai.configure(api_key="COLLE_TA_CLE_ICI")

# 2. Choix du modele (rapide et gratuit)
model = genai.GenerativeModel("gemini-2.0-flash")

print("Assistant IA pour etudiant (tape 'quit' pour sortir)")
while True:
    question = input("\\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    reponse = model.generate_content(question)
    print("IA   >", reponse.text)"""

CODE_HISTORIQUE = """# assistant_memoire.py -- meme assistant, AVEC memoire de conversation
import google.generativeai as genai

genai.configure(api_key="COLLE_TA_CLE_ICI")
model = genai.GenerativeModel("gemini-2.0-flash")

# Nouveaute : l'historique garde le contexte des questions precedentes
historique = []

print("Assistant avec memoire (tape 'quit' pour sortir)")
while True:
    question = input("\\nToi > ")
    if question.lower() in ("quit", "exit"):
        break
    historique.append("Etudiant : " + question)
    prompt = "\\n".join(historique[-6:])  # les 6 derniers echanges
    reponse = model.generate_content(prompt)
    historique.append("IA : " + reponse.text)
    print("IA   >", reponse.text)"""


SEANCE = {
    "num": 7,
    "slug": "seance-07",
    "icon": "🐍",
    "titles": L(
        "IA et programmation — mini-projet Python",
        "AI and programming — Python mini-project",
        "الذكاء الاصطناعي والبرمجة — مشروع بايثون مصغّر",
    ),
    "descriptions": L(
        "Comprendre le code, déboguer avec l'IA, puis construire un vrai assistant Python qui appelle l'API Gemini : clé gratuite, script commenté, exécution et modification.",
        "Understand code, debug with AI, then build a real Python assistant calling the Gemini API: free key, commented script, run and modification.",
        "فهم الكود، وتصحيح الأخطاء بالذكاء الاصطناعي، ثم بناء مساعد بايثون حقيقي يستدعي واجهة Gemini: مفتاح مجاني، وبرنامج مشروح، وتشغيل وتعديل.",
    ),
    "duration": "1 h 30",
    "objectifs": [
        L(
            "Expliquer un algorithme simple avec l'aide de l'IA, ligne par ligne.",
            "Explain a simple algorithm with AI help, line by line.",
            "أن يشرح خوارزمية بسيطة بمساعدة الذكاء الاصطناعي، سطراً سطراً.",
        ),
        L(
            "Déboguer un script Python : lire l'erreur, demander un diagnostic, corriger.",
            "Debug a Python script: read the error, ask for a diagnosis, fix.",
            "أن يصحّح برنامج بايثون: يقرأ الخطأ، ويطلب تشخيصاً، ويصلح.",
        ),
        L(
            "Obtenir une clé API gratuite (Gemini) et l'utiliser sans la partager.",
            "Get a free API key (Gemini) and use it without sharing it.",
            "أن يحصل على مفتاح API مجاني (Gemini) ويستعمله دون مشاركته.",
        ),
        L(
            "Exécuter le script assistant_chat.py et dialoguer avec sa propre IA.",
            "Run the assistant_chat.py script and chat with your own AI.",
            "أن يشغّل برنامج assistant_chat.py ويحاور ذكاءه الخاص.",
        ),
        L(
            "Modifier le script (mémoire de conversation) et expliquer chaque ajout.",
            "Modify the script (conversation memory) and explain each addition.",
            "أن يعدّل البرنامج (ذاكرة المحادثة) ويشرح كل إضافة.",
        ),
    ],
    "prerequis": L(
        "Séances 1 à 6 suivies. Python installé (ou VS Code). Aucun niveau avancé requis.",
        "Sessions 1 to 6 completed. Python installed (or VS Code). No advanced level required.",
        "إتمام الحصص من 1 إلى 6. بايثون مثبّتة (أو VS Code). لا مستوى متقدم مطلوب.",
    ),
    "accroche": {
        "question": L(
            "Et si votre prochain exercice de programmation se corrigeait tout seul… en vous expliquant vos propres erreurs ? C'est exactement ce qu'on va construire aujourd'hui.",
            "What if your next programming exercise corrected itself… while explaining your own mistakes? That is exactly what we will build today.",
            "ماذا لو صحّح تمرينك البرمجي نفسه… شارحاً أخطاءك؟ هذا بالضبط ما سنبنيه اليوم.",
        ),
        "analogie": L(
            "🍳 Programmer avec l'IA, c'est comme cuisiner avec un commis : c'est vous le chef (vous décidez du plat), le commis épluche et coupe (il écrit le code répétitif), mais vous goûtez chaque étape — sinon le plat est raté.",
            "🍳 Programming with AI is like cooking with a helper: you are the chef (you decide the dish), the helper peels and chops (it writes repetitive code), but you taste every step — otherwise the dish fails.",
            "🍳 البرمجة مع الذكاء الاصطناعي كالطبخ مع مساعد: أنت الطباخ الرئيسي (تقرّر الطبق)، والمساعد يقشّر ويقطّع (يكتب الكود المتكرر)، لكنك تتذوّق كل مرحلة — وإلا فشل الطبق.",
        ),
        "phrase": L(
            "💡 Une API, c'est un guichet : votre petit script Python y dépose une question, et le grand modèle d'IA y répond. Aujourd'hui, vous construisez le guichet.",
            "💡 An API is a counter: your small Python script drops a question there, and the big AI model answers. Today, you build the counter.",
            "💡 الواجهة API كشبّاك: برنامجك الصغير يضع سؤالاً، والنموذج الكبير يجيب. اليوم ستبني الشبّاك.",
        ),
    },
    "plan": [
        {
            "time": "00–05",
            "badge": "🎬 A",
            **L(
                "Accroche : le commis cuisinier",
                "Hook: the kitchen helper",
                "انطلاقة: مساعد الطباخ",
            ),
            "detail": L(
                "Question d'ouverture + analogie du chef et du commis.",
                "Opening question + chef-and-helper analogy.",
                "سؤال الافتتاح + تشبيه الطباخ والمساعد.",
            ),
        },
        {
            "time": "05–25",
            "badge": "🧱 B",
            **L(
                "Explication : comprendre et déboguer avec l'IA",
                "Explanation: understand and debug with AI",
                "شرح: الفهم والتصحيح بالذكاء الاصطناعي",
            ),
            "detail": L(
                "3 idées : faire expliquer le code ligne par ligne ; lire les messages d'erreur ; demander un diagnostic avant la solution.",
                "3 ideas: have code explained line by line; read error messages; ask for a diagnosis before the solution.",
                "3 أفكار: شرح الكود سطراً سطراً؛ قراءة رسائل الخطأ؛ طلب التشخيص قبل الحل.",
            ),
        },
        {
            "time": "25–50",
            "badge": "🛠️ C",
            **L(
                "Démo : la clé API + le premier script",
                "Demo: the API key + the first script",
                "عرض: مفتاح API + أول برنامج",
            ),
            "detail": L(
                "ai.google.dev → clé gratuite → pip install → assistant_chat.py qui répond.",
                "ai.google.dev → free key → pip install → assistant_chat.py answering.",
                "ai.google.dev ← مفتاح مجاني ← تثبيت ← assistant_chat.py يجيب.",
            ),
        },
        {
            "time": "50–70",
            "badge": "✏️ D",
            **L(
                "Exercice guidé : ajoutez la mémoire",
                "Guided exercise: add the memory",
                "تمرين موجّه: أضف الذاكرة",
            ),
            "detail": L(
                "Transformer le script : garder les 6 derniers échanges pour le contexte.",
                "Transform the script: keep the last 6 exchanges for context.",
                "تحويل البرنامج: الاحتفاظ بآخر 6 تبادلات للسياق.",
            ),
        },
        {
            "time": "70–80",
            "badge": "🛠️ C",
            **L(
                "Démo 2 : Cursor / Copilot en action",
                "Demo 2: Cursor / Copilot in action",
                "عرض 2: Cursor / Copilot عملياً",
            ),
            "detail": L(
                "Auto-complétion en direct : écrire un commentaire, laisser l'outil compléter, vérifier.",
                "Live auto-completion: write a comment, let the tool complete, verify.",
                "إكمال تلقائي مباشر: اكتب تعليقاً، ودع الأداة تكمل، وتحقّق.",
            ),
        },
        {
            "time": "80–90",
            "badge": "📋 E",
            **L(
                "Synthèse, quiz et annonce de la séance 8",
                "Wrap-up, quiz and preview of session 8",
                "خلاصة واختبار وتقديم الحصة الثامنة",
            ),
            "detail": L(
                "« À retenir ». Annonce : rédaction académique et anti-plagiat.",
                "Key takeaways. Preview: academic writing and anti-plagiarism.",
                "« ما يجب تذكّره ». تقديم: الكتابة الأكاديمية ومكافحة الانتحال.",
            ),
        },
    ],
    "sections": [
        {
            "id": "s1",
            "titre": L(
                "Comprendre le code : l'IA comme professeur particulier",
                "Understand code: AI as a private teacher",
                "فهم الكود: الذكاء الاصطناعي كمدرّس خصوصي",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Ne demandez jamais « fais mon TP » : demandez « explique-moi ». Un étudiant qui comprend 10 programmes expliqués progresse ; celui qui rend 10 programmes générés stagne.",
                        "Never ask \"do my assignment\": ask \"explain to me\". A student who understands 10 explained programs progresses; one who submits 10 generated programs stagnates.",
                        "لا تطلب « أنجز واجبي » أبداً: اطلب « اشرح لي ». الطالب الذي يفهم عشرة برامج مشروحة يتقدّم؛ ومن يسلّم عشرة برامج مولّدة يراوح.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Prompt explication :</strong> « Explique ce code ligne par ligne, comme à un débutant : [coller le code]. »",
                            "<strong>Prompt algorithme :</strong> « Explique la recherche du maximum dans une liste avec un exemple chiffré pas à pas. »",
                            "<strong>Prompt comparaison :</strong> « Quelle est la différence entre une boucle for et while ? Un exemple chacun. »",
                        ],
                        [
                            "<strong>Explanation prompt:</strong> \"Explain this code line by line, like to a beginner: [paste code].\"",
                            "<strong>Algorithm prompt:</strong> \"Explain finding the maximum in a list with a step-by-step number example.\"",
                            "<strong>Comparison prompt:</strong> \"What is the difference between for and while loops? One example each.\"",
                        ],
                        [
                            "<strong>صياغة الشرح:</strong> « اشرح هذا الكود سطراً سطراً كمبتدئ: [الصق الكود] ».",
                            "<strong>صياغة الخوارزمية:</strong> « اشرح البحث عن أكبر عنصر في قائمة بمثال رقمي خطوة بخطوة ».",
                            "<strong>صياغة المقارنة:</strong> « ما الفرق بين حلقتي for وwhile؟ مثال لكل منهما ».",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🔗 Rappel séance 6 :</strong> le tuteur socratique posait des questions au lieu de donner les réponses. Aujourd'hui, on le CODE : notre script posera des questions à Gemini au lieu de tout faire à notre place.",
                        "<strong>🔗 Reminder of session 6:</strong> the Socratic tutor asked questions instead of giving answers. Today, we CODE it: our script will ask Gemini questions instead of doing everything for us.",
                        "<strong>🔗 تذكير بالحصة 6:</strong> المدرّس السقراطي كان يطرح أسئلة بدل إعطاء الأجوبة. اليوم سنبرمجه: برنامجنا سيطرح أسئلة على Gemini بدل فعل كل شيء بدلاً منا.",
                    ),
                },
            ],
        },
        {
            "id": "s2",
            "titre": L(
                "Déboguer : lire l'erreur avant de la réparer",
                "Debug: read the error before fixing it",
                "تصحيح الأخطاء: اقرأ الخطأ قبل إصلاحه",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Un message d'erreur n'est pas une insulte : c'est une adresse (le numéro de ligne) et un diagnostic (le type d'erreur). Montrez les deux à l'IA, et demandez d'abord le POURQUOI.",
                        "An error message is not an insult: it is an address (the line number) and a diagnosis (the error type). Show both to AI, and ask for the WHY first.",
                        "رسالة الخطأ ليست إهانة: بل عنوان (رقم السطر) وتشخيص (نوع الخطأ). اعرضهما على الذكاء الاصطناعي، واطلب لماذا أولاً.",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Méthode en 3 temps :</strong> 1) lire la dernière ligne de l'erreur ; 2) demander « pourquoi cette erreur ? » ; 3) seulement ensuite « comment corriger ? ».",
                            "<strong>Prompt modèle :</strong> « Voici mon code [coller] et l'erreur [coller]. Explique la cause en 2 phrases, puis propose UNE correction. »",
                            "<strong>Erreurs classiques PEP :</strong> indentation, deux-points oubliés, variable non définie, mélange de types.",
                        ],
                        [
                            "<strong>3-step method:</strong> 1) read the last line of the error; 2) ask \"why this error?\"; 3) only then \"how to fix?\"",
                            "<strong>Model prompt:</strong> \"Here is my code [paste] and the error [paste]. Explain the cause in 2 sentences, then suggest ONE fix.\"",
                            "<strong>Classic PEP mistakes:</strong> indentation, missing colons, undefined variable, mixed types.",
                        ],
                        [
                            "<strong>منهجية بثلاث خطوات:</strong> 1) اقرأ آخر سطر من الخطأ؛ 2) اسأل « لماذا هذا الخطأ؟ »؛ 3) ثم فقط « كيف أصلح؟ ».",
                            "<strong>صياغة نموذجية:</strong> « هذا كودي [الصق] والخطأ [الصق]. اشرح السبب في جملتين، ثم اقترح تصحيحاً واحداً ».",
                            "<strong>أخطاء PEP الكلاسيكية:</strong> المسافة البادئة، نقطتان منسيتان، متغير غير معرّف، خلط الأنواع.",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "tip",
                    **L(
                        "<strong>Astuce :</strong> après la correction, demandez « donne-moi un mini-exercice similaire pour vérifier que j'ai compris ». La boucle est bouclée : erreur → cause → correction → vérification.",
                        "<strong>Tip:</strong> after the fix, ask \"give me a similar mini-exercise to check I understood\". The loop is closed: error → cause → fix → check.",
                        "<strong>نصيحة:</strong> بعد التصحيح اطلب « أعطني تمريناً مصغّراً مشابهاً لأتحقق أني فهمت ». الحلقة مكتملة: خطأ ← سبب ← تصحيح ← تحقق.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "idea",
                    **L(
                        "<strong>🧪 Exemple concret :</strong> moyenne = total / nombre. Une TypeError mélangeant texte et nombres → cause : un âge lu comme texte → correction : int(age). Demandez ensuite un exercice similaire avec des notes.",
                        "<strong>🧪 Concrete example:</strong> average = total / count. A TypeError mixing text and numbers → cause: an age read as text → fix: int(age). Then ask for a similar exercise with grades.",
                        "<strong>🧪 مثال ملموس:</strong> المعدل = المجموع / العدد. خطأ نوع يخلط نصاً وأعداداً ← السبب: عمر مقروء كنص ← التصحيح: int(age). ثم اطلب تمريناً مشابهاً بالعلامات.",
                    ),
                },
            ],
        },
        {
            "id": "s3",
            "titre": L(
                "Le mini-projet : votre assistant qui appelle Gemini",
                "The mini-project: your assistant calling Gemini",
                "المشروع المصغّر: مساعدك الذي يستدعي Gemini",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Une API (interface de programmation) est un guichet : votre script envoie du texte, le modèle géant répond. Avec une clé gratuite, 15 lignes de Python suffisent pour avoir VOTRE chatbot.",
                        "An API (programming interface) is a counter: your script sends text, the giant model answers. With a free key, 15 lines of Python are enough for YOUR chatbot.",
                        "الواجهة API كشبّاك: برنامجك يرسل نصاً، والنموذج العملاق يجيب. بمفتاح مجاني، تكفي 15 سطراً من بايثون لامتلاك روبوتك.",
                    ),
                },
                {
                    "t": "ol",
                    **L(
                        [
                            "<strong>Clé gratuite :</strong> aller sur ai.google.dev → « Get API key » → copier (comme un mot de passe, jamais partagée).",
                            "<strong>Installer :</strong> <strong>python -m pip install google-generativeai</strong> dans le terminal.",
                            "<strong>Copier</strong> le script assistant_chat.py ci-dessous, coller la clé, exécuter : <strong>python assistant_chat.py</strong>.",
                            "<strong>Tester :</strong> poser 3 questions de révision de votre module préféré.",
                        ],
                        [
                            "<strong>Free key:</strong> go to ai.google.dev → \"Get API key\" → copy (like a password, never shared).",
                            "<strong>Install:</strong> <strong>python -m pip install google-generativeai</strong> in the terminal.",
                            "<strong>Copy</strong> the assistant_chat.py script below, paste the key, run: <strong>python assistant_chat.py</strong>.",
                            "<strong>Test:</strong> ask 3 revision questions from your favourite module.",
                        ],
                        [
                            "<strong>مفتاح مجاني:</strong> ادخل ai.google.dev ← « Get API key » ← انسخ (ككلمة مرور، لا يُشارَك أبداً).",
                            "<strong>ثبّت:</strong> <strong>python -m pip install google-generativeai</strong> في الطرفية.",
                            "<strong>انسخ</strong> برنامج assistant_chat.py أدناه، والصق المفتاح، وشغّل: <strong>python assistant_chat.py</strong>.",
                            "<strong>جرّب:</strong> اطرح 3 أسئلة مراجعة من وحدتك المفضلة.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": CODE_ASSISTANT,
                    "en": CODE_ASSISTANT,
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>🔒 Sécurité :</strong> la clé API, c'est un mot de passe payant. Jamais dans un devoir rendu, jamais sur GitHub, jamais en photo. Si elle fuite, la régénérer sur ai.google.dev.",
                        "<strong>🔒 Security:</strong> the API key is a paying password. Never in a submitted assignment, never on GitHub, never in a photo. If leaked, regenerate it on ai.google.dev.",
                        "<strong>🔒 أمان:</strong> مفتاح API كلمة مرور مدفوعة. لا في واجب مسلَّم، ولا على GitHub، ولا في صورة. إذا تسرّب، أعد توليده في ai.google.dev.",
                    ),
                },
            ],
        },
        {
            "id": "s4",
            "titre": L(
                "Aller plus loin : Copilot, Cursor et la mémoire",
                "Go further: Copilot, Cursor and memory",
                "للمضي أبعد: Copilot وCursor والذاكرة",
            ),
            "blocks": [
                {
                    "t": "p",
                    **L(
                        "Deuxième étage de la fusée : les assistants intégrés à l'éditeur (complétion pendant la frappe) et l'historique (le chatbot qui se souvient).",
                        "Second stage of the rocket: assistants built into the editor (completion while typing) and history (the chatbot that remembers).",
                        "المرحلة الثانية: مساعدات مدمجة في المحرر (إكمال أثناء الكتابة) والذاكرة (روبوت يتذكّر).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>Cursor / Copilot :</strong> écrivez un commentaire « # fonction qui calcule la moyenne », laissez l'outil proposer le code, LISEZ-LE avant d'accepter.",
                            "<strong>Mémoire :</strong> la version assistant_memoire.py garde les 6 derniers échanges : testez « et en arabe ? » après une question.",
                            "<strong>Limite :</strong> l'assistant écrit vite mais ne comprend pas votre TP — seul votre test (exécution + cas limites) valide.",
                        ],
                        [
                            "<strong>Cursor / Copilot:</strong> write a comment \"# function computing the average\", let the tool suggest code, READ it before accepting.",
                            "<strong>Memory:</strong> the assistant_memoire.py version keeps the last 6 exchanges: try \"and in Arabic?\" after a question.",
                            "<strong>Limit:</strong> the assistant writes fast but does not understand your assignment — only your test (run + edge cases) validates.",
                        ],
                        [
                            "<strong>Cursor / Copilot:</strong> اكتب تعليقاً « # دالة تحسب المعدل »، ودع الأداة تقترح الكود، واقرأه قبل القبول.",
                            "<strong>الذاكرة:</strong> نسخة assistant_memoire.py تحتفظ بآخر 6 تبادلات: جرّب « وبالعربية؟ » بعد سؤال.",
                            "<strong>حدّ:</strong> المساعد يكتب بسرعة لكنه لا يفهم واجبك — اختبارك وحده (تشغيل + حالات حدّية) يوثّق.",
                        ],
                    ),
                },
                {
                    "t": "pre",
                    "fr": CODE_HISTORIQUE,
                    "en": CODE_HISTORIQUE,
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
                        "Le programmeur augmenté : l'IA propose, vous disposez. Chaque ligne générée est relue, exécutée et testée — c'est ce qui distingue l'étudiant de l'opérateur de copier-coller.",
                        "The augmented programmer: AI proposes, you decide. Every generated line is reread, run and tested — that is what distinguishes a student from a copy-paste operator.",
                        "المبرمج المعزَّز: الذكاء يقترح وأنت تقرّر. كل سطر مولّد يُقرأ ويُشغَّل ويُختبَر — وهذا ما يميّز الطالب عن ناسخ لاصق.",
                    ),
                },
                {
                    "t": "note",
                    "kind": "goal",
                    **L(
                        "<strong>➡️ Pont vers la séance 8 :</strong> un programme qui écrit bien impressionne, mais un étudiant qui écrit bien convainc : votre assistant servira aussi à relire vos textes (correction expliquée, séance 8).",
                        "<strong>➡️ Bridge to session 8:</strong> a program writing well impresses, but a student writing well convinces: your assistant will also proofread your texts (explained correction, session 8).",
                        "<strong>➡️ جسر إلى الحصة 8:</strong> برنامج يكتب جيداً يُبهر، لكن طالباً يكتب جيداً يُقنِع: مساعدك سيصلح نصوصك أيضاً (تصحيح مفسَّر، الحصة 8).",
                    ),
                },
                {
                    "t": "ul",
                    **L(
                        [
                            "<strong>✅ Explique-moi d'abord :</strong> toujours comprendre avant de rendre.",
                            "<strong>✅ Une erreur = une leçon :</strong> noter la cause dans un carnet de bugs.",
                            "<strong>✅ Versionnez :</strong> garder assistant_chat.py puis assistant_memoire.py (voir la progression).",
                            "<strong>✅ Testez les limites :</strong> question vide, très longue, en arabe dialectal — que se passe-t-il ?",
                        ],
                        [
                            "<strong>✅ Explain-first:</strong> always understand before submitting.",
                            "<strong>✅ One error = one lesson:</strong> note the cause in a bug notebook.",
                            "<strong>✅ Version:</strong> keep assistant_chat.py then assistant_memoire.py (see progress).",
                            "<strong>✅ Test limits:</strong> empty question, very long, dialectal Arabic — what happens?",
                        ],
                        [
                            "<strong>✅ اشرح أولاً:</strong> افهم دائماً قبل التسليم.",
                            "<strong>✅ خطأ = درس:</strong> سجّل السبب في دفتر أخطاء.",
                            "<strong>✅ نسّخ:</strong> احتفظ بـ assistant_chat.py ثم assistant_memoire.py (لاحظ التقدّم).",
                            "<strong>✅ اختبر الحدود:</strong> سؤال فارغ، طويل جداً، بالدارجة — ماذا يحدث؟",
                        ],
                    ),
                },
                {
                    "t": "note",
                    "kind": "warn",
                    **L(
                        "<strong>❌ Erreurs à éviter :</strong> rendre du code non exécuté, partager sa clé API, croire que « ça marche une fois » = « c'est correct » (tester les cas limites).",
                        "<strong>❌ Mistakes to avoid:</strong> submitting unrun code, sharing your API key, believing \"it works once\" = \"it is correct\" (test edge cases).",
                        "<strong>❌ أخطاء يجب تجنّبها:</strong> تسليم كود غير مشغَّل، مشاركة مفتاح API، الظن أن « يعمل مرة » = « صحيح » (اختبر الحالات الحدّية).",
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
                            ["Demande", "« Fais mon TP de tri. »", "« Explique le tri par sélection avec un exemple [7, 2, 9], puis donne-moi un exercice similaire. »"],
                            ["Résultat", "Code rendu, rien compris, zéro le jour de l'examen.", "Compréhension + entraînement, autonome le jour J."],
                        ],
                        [
                            ["Prompt", "\"Do my sorting assignment.\"", "\"Explain selection sort with an example [7, 2, 9], then give me a similar exercise.\""],
                            ["Result", "Submitted code, nothing understood, zero on exam day.", "Understanding + training, autonomous on D-day."],
                        ],
                        [
                            ["الطلب", "« أنجز واجب الترتيب »", "« اشرح الترتيب بالاختيار بمثال [7، 2، 9]، ثم أعطني تمريناً مشابهاً »"],
                            ["النتيجة", "كود مسلَّم، لا فهم، وصفر يوم الامتحان.", "فهم + تدريب، واستقلالية يوم الامتحان."],
                        ],
                    ),
                },
            ],
        },
    ],
    "verifications": [
        {
            "q": L(
                "Qu'est-ce qu'une clé API et pourquoi la protéger ?",
                "What is an API key and why protect it?",
                "ما مفتاح API ولماذا نحميه؟",
            ),
            "r": L(
                "C'est le mot de passe qui identifie votre compte auprès du modèle et peut être facturé. Partagée = quelqu'un dépense à votre place.",
                "It is the password identifying your account to the model and it can be billed. Shared = someone spends on your behalf.",
                "هو كلمة المرور التي تعرّف حسابك لدى النموذج وقد تُفوتر. مشاركته = شخص ينفق على حسابك.",
            ),
        },
        {
            "q": L(
                "Pourquoi demander le POURQUOI de l'erreur avant la correction ?",
                "Why ask for the WHY of the error before the fix?",
                "لماذا نطلب سبب الخطأ قبل التصحيح؟",
            ),
            "r": L(
                "Comprendre la cause évite de répéter l'erreur ; copier la correction sans comprendre la garantit au prochain TP.",
                "Understanding the cause prevents repeating the mistake; copying the fix without understanding guarantees it next time.",
                "فهم السبب يمنع تكرار الخطأ؛ ونسخ التصحيح دون فهم يضمنه في الواجب القادم.",
            ),
        },
        {
            "q": L(
                "Que change l'historique dans assistant_memoire.py ?",
                "What does history change in assistant_memoire.py?",
                "ماذا يغيّر الاحتفاظ بالذاكرة في assistant_memoire.py؟",
            ),
            "r": L(
                "Les 6 derniers échanges sont renvoyés au modèle : il comprend les suites comme « et en arabe ? » sans répéter la question.",
                "The last 6 exchanges are resent to the model: it understands follow-ups like \"and in Arabic?\" without repeating the question.",
                "تُرسَل آخر 6 تبادلات إلى النموذج: فيفهم التتمات مثل « وبالعربية؟ » دون إعادة السؤال.",
            ),
        },
    ],
    "exercise_guide": {
        "enonce": L(
            "1) Exécutez assistant_chat.py et posez 3 questions de cours. 2) Créez assistant_memoire.py (ajout de l'historique). 3) Testez la mémoire : question puis « résume ta réponse précédente en 1 phrase ».",
            "1) Run assistant_chat.py and ask 3 lesson questions. 2) Create assistant_memoire.py (add history). 3) Test memory: ask then \"summarise your previous answer in 1 sentence\".",
            "1) شغّل assistant_chat.py واطرح 3 أسئلة درس. 2) أنشئ assistant_memoire.py (أضف الذاكرة). 3) اختبر الذاكرة: اسأل ثم « لخّص جوابك السابق في جملة ».",
        ),
        "demarche": L(
            "1) Vérifiez Python : python --version. 2) Installez la bibliothèque. 3) Collez la clé SANS la montrer à votre voisin d'écran. 4) Lancez, testez, puis ajoutez la liste historique. 5) Comparez les deux versions sur la même question de suivi.",
            "1) Check Python: python --version. 2) Install the library. 3) Paste the key WITHOUT showing your screen neighbour. 4) Run, test, then add the historique list. 5) Compare both versions on the same follow-up question.",
            "1) تحقق من بايثون: python --version. 2) ثبّت المكتبة. 3) الصق المفتاح دون إظهاره لجارك. 4) شغّل وجرّب ثم أضف قائمة الذاكرة. 5) قارن النسختين على نفس سؤال المتابعة.",
        ),
        "solution": L(
            "Version 1 répond à chaque question isolément (oublie le contexte). Version 2 avec historique répond correctement aux suites (« et en arabe ? », « résume »). Si erreur d'API : vérifier la clé, le Wi-Fi et le nom du modèle (gemini-2.0-flash).",
            "Version 1 answers each question in isolation (forgets context). Version 2 with history correctly answers follow-ups (\"and in Arabic?\", \"summarise\"). On API error: check the key, Wi-Fi and model name (gemini-2.0-flash).",
            "النسخة 1 تجيب كل سؤال معزولاً (تنسى السياق). النسخة 2 بالذاكرة تجيب التتمات صحيحاً (« وبالعربية؟ »، « لخّص »). عند خطأ API: تحقق من المفتاح والشبكة واسم النموذج (gemini-2.0-flash).",
        ),
    },
    "videos": [
        {
            "titre": L(
                "Playlist IA de Mohammad Dawoud (introduction, ML, réseaux de neurones)",
                "Mohammad Dawoud's AI playlist (intro, ML, neural networks)",
                "سلسلة محمد داود في الذكاء الاصطناعي (مدخل، تعلم آلي، شبكات عصبية)",
            ),
            "url": "https://www.youtube.com/watch?v=H5WUwwivEaI&list=PLbR_CTcUs1088jfqbbO5AqwODO9MgYA85",
            "langue": "ar",
            "concept": L(
                "La référence du module : comprendre ce qu'il y a SOUS le guichet API (neurones, apprentissage).",
                "The module's reference: understand what is UNDER the API counter (neurons, learning).",
                "مرجع الوحدة: فهم ما تحت شبّاك API (خلايا، تعلّم).",
            ),
        },
        {
            "titre": L(
                "But what is a neural network? (3Blue1Brown)",
                "But what is a neural network? (3Blue1Brown)",
                "ما الشبكة العصبية؟ (3Blue1Brown)",
            ),
            "url": "https://www.youtube.com/watch?v=aircAruvnKk",
            "langue": "en",
            "concept": L(
                "Visualiser comment un réseau apprend — sous-titres FR disponibles.",
                "Visualise how a network learns — FR subtitles available.",
                "تصوّر كيف تتعلم الشبكة — ترجمة فرنسية متاحة.",
            ),
        },
        {
            "titre": L(
                "Apprendre Python + utiliser l'API Gemini (tutoriel)",
                "Learn Python + use the Gemini API (tutorial)",
                "تعلّم بايثون + استعمال واجهة Gemini (شرح)",
            ),
            "url": "https://www.youtube.com/results?search_query=gemini+api+python+tutorial+debutant",
            "langue": "fr",
            "concept": L(
                "Voir chaque étape (clé, pip install, premier appel) faite en vidéo avant de la refaire.",
                "See each step (key, pip install, first call) done on video before redoing it.",
                "شاهد كل خطوة (مفتاح، تثبيت، أول استدعاء) بالفيديو قبل إعادتها.",
            ),
        },
    ],
    "fiche_synthese": {
        "points": [
            L(
                "Explique-moi > fais-moi : comprendre avant de rendre.",
                "Explain-to-me > do-for-me: understand before submitting.",
                "اشرح لي > أنجز عني: افهم قبل التسليم.",
            ),
            L(
                "Débogage : lire l'erreur, demander le POURQUOI, puis corriger.",
                "Debugging: read the error, ask WHY, then fix.",
                "التصحيح: اقرأ الخطأ، واسأل لماذا، ثم صحّح.",
            ),
            L(
                "API = guichet : clé gratuite sur ai.google.dev, jamais partagée.",
                "API = counter: free key on ai.google.dev, never shared.",
                "API = شبّاك: مفتاح مجاني من ai.google.dev، لا يُشارَك أبداً.",
            ),
            L(
                "15 lignes suffisent : assistant_chat.py dialogue avec Gemini.",
                "15 lines are enough: assistant_chat.py chats with Gemini.",
                "تكفي 15 سطراً: assistant_chat.py يحاور Gemini.",
            ),
            L(
                "Mémoire = renvoyer les 6 derniers échanges au modèle.",
                "Memory = resend the last 6 exchanges to the model.",
                "الذاكرة = إعادة إرسال آخر 6 تبادلات إلى النموذج.",
            ),
        ],
        "analogies": [
            L(
                "Le commis cuisinier : il prépare, vous goûtez et décidez.",
                "The kitchen helper: he prepares, you taste and decide.",
                "مساعد الطباخ: يحضّر، وأنت تتذوّق وتقرّر.",
            ),
            L(
                "Le guichet API : vous déposez une question, le géant répond.",
                "The API counter: you drop a question, the giant answers.",
                "شبّاك API: تضع سؤالاً، والعملاق يجيب.",
            ),
            L(
                "Le carnet de bugs : chaque erreur notée est un piège désamorcé.",
                "The bug notebook: each noted error is a defused trap.",
                "دفتر الأخطاء: كل خطأ مسجَّل فخ مُعطَّل.",
            ),
        ],
        "exemples": [
            L(
                "« Explique ce tri ligne par ligne » → l'étudiant comprend et refait seul.",
                "\"Explain this sort line by line\" → the student understands and redoes alone.",
                "« اشرح هذا الترتيب سطراً سطراً » ← الطالب يفهم ويعيد وحده.",
            ),
            L(
                "IndentationError → cause comprise → correction + mini-exercice de vérification.",
                "IndentationError → cause understood → fix + verification mini-exercise.",
                "IndentationError ← السبب مفهوم ← تصحيح + تمرين تحقق مصغّر.",
            ),
            L(
                "« Et en arabe ? » compris grâce à l'historique des 6 échanges.",
                "\"And in Arabic?\" understood thanks to the 6-exchange history.",
                "« وبالعربية؟ » مفهوم بفضل ذاكرة التبادلات الستة.",
            ),
        ],
        "analogie_finale": L(
            "🏁 Programmer avec l'IA, c'est comme apprendre à conduire avec un moniteur : au début il tient le volant avec vous, mais l'examen, c'est vous seul qui le passez — et la route ensuite aussi.",
            "🏁 Programming with AI is like learning to drive with an instructor: at first he holds the wheel with you, but you take the exam alone — and drive the road after, too.",
            "🏁 البرمجة مع الذكاء الاصطناعي كتعلّم القيادة مع مدرّب: في البداية يمسك المقود معك، لكن الامتحان تجتازه وحدك — والطريق بعده أيضاً.",
        ),
        "quiz": [
            {
                "q": L(
                    "Quel est le meilleur premier prompt face à un code incompris ?",
                    "What is the best first prompt facing misunderstood code?",
                    "ما أفضل صياغة أولى أمام كود غير مفهوم؟",
                ),
                "options": L(
                    ["« Fais mon TP »", "« Explique ce code ligne par ligne, comme à un débutant »", "« C'est nul, recommence »", "« Donne-moi un autre code »"],
                    ["\"Do my assignment\"", "\"Explain this code line by line, like to a beginner\"", "\"It is bad, redo it\"", "\"Give me another code\""],
                    ["« أنجز واجبي »", "« اشرح هذا الكود سطراً سطراً كمبتدئ »", "« سيئ، أعد »", "« أعطني كوداً آخر »"],
                ),
                "answer": 1,
                "exp": L(
                    "L'explication construit la compréhension ; le code tout fait la contourne.",
                    "Explanation builds understanding; ready-made code bypasses it.",
                    "الشرح يبني الفهم؛ والكود الجاهز يلتف عليه.",
                ),
            },
            {
                "q": L(
                    "Face à une erreur Python, quel est le bon ordre ?",
                    "Facing a Python error, what is the right order?",
                    "أمام خطأ بايثون، ما الترتيب الصحيح؟",
                ),
                "options": L(
                    ["Corriger puis comprendre", "Lire l'erreur → demander le POURQUOI → corriger → vérifier", "Supprimer le fichier", "Changer de langage"],
                    ["Fix then understand", "Read the error → ask WHY → fix → verify", "Delete the file", "Change language"],
                    ["صحّح ثم افهم", "اقرأ الخطأ ← اسأل لماذا ← صحّح ← تحقق", "احذف الملف", "غيّر اللغة"],
                ),
                "answer": 1,
                "exp": L(
                    "La cause comprise + un mini-exercice de vérification ferment la boucle d'apprentissage.",
                    "The understood cause + a verification mini-exercise close the learning loop.",
                    "السبب المفهوم + تمرين تحقق مصغّر يغلقان حلقة التعلّم.",
                ),
            },
            {
                "q": L(
                    "Où obtenir une clé Gemini et comment la traiter ?",
                    "Where to get a Gemini key and how to treat it?",
                    "أين تحصل على مفتاح Gemini وكيف تعامله؟",
                ),
                "options": L(
                    ["Sur Google, à partager", "Sur ai.google.dev, comme un mot de passe jamais partagé", "Dans le script d'un ami", "Pas besoin de clé"],
                    ["On Google, to share", "On ai.google.dev, like a never-shared password", "In a friend's script", "No key needed"],
                    ["في جوجل، للمشاركة", "في ai.google.dev، ككلمة مرور لا تُشارَك أبداً", "في برنامج صديق", "لا حاجة لمفتاح"],
                ),
                "answer": 1,
                "exp": L(
                    "La clé est gratuite sur ai.google.dev mais facturable : fuite = quelqu'un dépense à votre place.",
                    "The key is free on ai.google.dev but billable: a leak = someone spends on your behalf.",
                    "المفتاح مجاني في ai.google.dev لكنه قابل للفوترة: تسرّبه = شخص ينفق على حسابك.",
                ),
            },
            {
                "q": L(
                    "Que fait la liste historique dans assistant_memoire.py ?",
                    "What does the historique list do in assistant_memoire.py?",
                    "ماذا تفعل قائمة الذاكرة في assistant_memoire.py؟",
                ),
                "options": L(
                    ["Elle sauvegarde sur disque", "Elle renvoie les 6 derniers échanges pour garder le contexte", "Elle accélère Internet", "Elle traduit le code"],
                    ["It saves to disk", "It resends the last 6 exchanges to keep context", "It speeds up Internet", "It translates code"],
                    ["تحفظ على القرص", "تعيد إرسال آخر 6 تبادلات للحفاظ على السياق", "تسرّع الإنترنت", "تترجم الكود"],
                ),
                "answer": 1,
                "exp": L(
                    "Le modèle est sans mémoire : c'est le script qui lui rappelle la conversation à chaque appel.",
                    "The model is memoryless: the script reminds it of the conversation on each call.",
                    "النموذج بلا ذاكرة: البرنامج هو من يذكّره بالمحادثة في كل استدعاء.",
                ),
            },
            {
                "q": L(
                    "Pourquoi tester les cas limites (question vide, très longue) ?",
                    "Why test edge cases (empty, very long question)?",
                    "لماذا نختبر الحالات الحدّية (سؤال فارغ، طويل جداً)؟",
                ),
                "options": L(
                    ["Pour perdre du temps", "Parce que « marche une fois » n'est pas « correct » : seul le test valide", "Pour impressionner", "C'est interdit"],
                    ["To waste time", "Because \"works once\" is not \"correct\": only testing validates", "To impress", "It is forbidden"],
                    ["لتضييع الوقت", "لأن « يعمل مرة » ليس « صحيحاً »: الاختبار وحده يوثّق", "للإبهار", "ممنوع"],
                ),
                "answer": 1,
                "exp": L(
                    "Un programme se juge sur les cas normaux ET limites : c'est la marque du programmeur, pas du copieur.",
                    "A program is judged on normal AND edge cases: that is the programmer's mark, not the copier's.",
                    "يُحكَم على البرنامج بالحالات العادية والحدّية: هذه سمة المبرمج لا الناسخ.",
                ),
            },
        ],
    },
    "activites": [
        L(
            "Explication croisée : l'IA explique un tri, chaque binôme le réexplique sans écran.",
            "Cross-explanation: AI explains a sort, each pair re-explains it without screen.",
            "شرح متبادل: الذكاء يشرح ترتيباً، وكل ثنائي يعيد شرحه دون شاشة.",
        ),
        L(
            "Chasse au bug : 3 scripts piégés (indentation, variable, type) à diagnostiquer avant de corriger.",
            "Bug hunt: 3 trapped scripts (indentation, variable, type) to diagnose before fixing.",
            "صيد الأخطاء: 3 برامج مفخخة (مسافة، متغير، نوع) للتشخيص قبل التصحيح.",
        ),
        L(
            "Premier appel : clé + pip install + assistant_chat.py → 3 questions de révision.",
            "First call: key + pip install + assistant_chat.py → 3 revision questions.",
            "أول استدعاء: مفتاح + تثبيت + assistant_chat.py ← 3 أسئلة مراجعة.",
        ),
        L(
            "Défi mémoire : ajouter l'historique puis réussir le test « résume ta réponse précédente ».",
            "Memory challenge: add history then pass the \"summarise your previous answer\" test.",
            "تحدّي الذاكرة: أضف الذاكرة ثم انجح في اختبار « لخّص جوابك السابق ».",
        ),
    ],
    "retenir": [
        L(
            "Explique-moi > fais-moi : la compréhension d'abord.",
            "Explain-to-me > do-for-me: understanding first.",
            "اشرح لي > أنجز عني: الفهم أولاً.",
        ),
        L(
            "Déboguer : lire, POURQUOI, corriger, vérifier.",
            "Debug: read, WHY, fix, verify.",
            "صحّح: اقرأ، لماذا، صحّح، تحقق.",
        ),
        L(
            "Clé sur ai.google.dev, jamais partagée, jamais sur GitHub.",
            "Key on ai.google.dev, never shared, never on GitHub.",
            "المفتاح من ai.google.dev، لا يُشارَك أبداً، ولا على GitHub أبداً.",
        ),
        L(
            "assistant_chat.py : 15 lignes pour parler à Gemini.",
            "assistant_chat.py: 15 lines to talk to Gemini.",
            "assistant_chat.py: خمسة عشر سطراً لمحاورة Gemini.",
        ),
        L(
            "La mémoire, c'est le script qui rappelle la conversation au modèle.",
            "Memory is the script reminding the model of the conversation.",
            "الذاكرة هي البرنامج الذي يذكّر النموذج بالمحادثة.",
        ),
    ],
    "glossaire": [
        {
            "term": "API",
            "term_en": "API",
            "def_fr": "Guichet logiciel : votre programme envoie une demande, le service (Gemini) répond.",
            "def_en": "A software counter: your program sends a request, the service (Gemini) answers.",
            "def_ar": "شبّاك برمجي: برنامجك يرسل طلباً، والخدمة (Gemini) تجيب.",
        },
        {
            "term": "Clé API",
            "term_en": "API key",
            "def_fr": "Mot de passe personnel qui identifie vos appels au service ; gratuite mais facturable, à protéger.",
            "def_en": "A personal password identifying your calls to the service; free but billable, protect it.",
            "def_ar": "كلمة مرور شخصية تعرّف استدعاءاتك للخدمة؛ مجانية لكن قابلة للفوترة، احمها.",
        },
        {
            "term": "Débogage",
            "term_en": "Debugging",
            "def_fr": "Art de trouver la cause d'une erreur (lire, diagnostiquer) avant de la corriger.",
            "def_en": "The art of finding an error's cause (read, diagnose) before fixing it.",
            "def_ar": "فن إيجاد سبب الخطأ (اقرأ، شخّص) قبل تصحيحه.",
        },
        {
            "term": "Bibliothèque (package)",
            "term_en": "Library (package)",
            "def_fr": "Code prêt à l'emploi qu'on installe (pip install) pour utiliser un service comme Gemini.",
            "def_en": "Ready-to-use code you install (pip install) to use a service like Gemini.",
            "def_ar": "كود جاهز يُثبَّت (pip install) لاستعمال خدمة مثل Gemini.",
        },
        {
            "term": "Historique de conversation",
            "term_en": "Conversation history",
            "def_fr": "Échanges précédents renvoyés au modèle pour qu'il garde le contexte.",
            "def_en": "Previous exchanges resent to the model so it keeps context.",
            "def_ar": "تبادلات سابقة تُعاد إلى النموذج ليحافظ على السياق.",
        },
    ],
    "dialogues_fr": """# Séance 07 — Dialogues pédagogiques (Français)

## Dialogue A — « Mon programme ne marche pas… et c'est une bonne nouvelle » (25 min)

**Personnages :** Anis (étudiant bloqué), Lina (camarade débogueuse), M. Karim (enseignant).

---

Anis : Mon script affiche une erreur rouge de 10 lignes. Je suis nul en Python.

Lina : Montre la DERNIÈRE ligne. Que dit-elle ?

Anis : « IndentationError: unexpected indent, line 7 ».

Lina : Parfait, on a l'adresse (ligne 7) et le diagnostic (indentation inattendue). Demande à l'IA le POURQUOI, pas la correction.

Anis (à l'IA) : Pourquoi « unexpected indent » ligne 7 dans mon code [colle] ?

IA : Parce que la ligne 7 est décalée sans qu'une ligne finissant par « : » la précède. Python attend un bloc après « : ».

M. Karim : Tu vois ? L'erreur parlait. Maintenant corrige TOI-MÊME, puis demande un mini-exercice similaire.

Anis : Corrigé… et l'exercice similaire réussi ! Le bug était un professeur déguisé.

---

## Dialogue B — « Ma première IA à moi » (15 min)

**Personnages :** Sara (étudiante), son frère Yacine, l'écran (joué par un camarade).

---

Sara : Regarde, Yacine : je tape une question, et C'EST MON programme qui répond !

Yacine : Attends… c'est toi qui as programmé ChatGPT ?!

Sara : Non ! Mon script envoie ma question au guichet Gemini avec ma clé, et affiche la réponse. Quinze lignes seulement.

Écran : Toi > Explique-moi la photosynthèse en 3 points. / IA > 1)… 2)… 3)…

Yacine : Et si je veux qu'il se souvienne de ce qu'on a dit ?

Sara : J'ajoute une liste « historique » : à chaque appel, je renvoie les 6 derniers échanges. Essaie : demande-lui « et en arabe ? ».

Yacine : Il a compris ! Sans que je répète la question… C'est ça, la mémoire ?

Sara : Exactement : le modèle oublie tout, c'est MON script qui lui rappelle. Je suis devenue constructrice d'IA !

---

## Mini-rôle à jouer (3 min par binôme)
L'un colle un code avec une erreur classique, l'autre formule le prompt de diagnostic (« pourquoi », pas « corrige »). Échangez, puis votez pour le meilleur diagnostic de la classe.
""",
    "dialogues_en": """# Session 07 — Classroom dialogues (English)

## Dialogue A — "My program does not work… and that is good news" (25 min)

**Characters:** Anis (a stuck student), Lina (a debugger classmate), Mr Karim (teacher).

---

Anis: My script shows a 10-line red error. I am hopeless at Python.

Lina: Show the LAST line. What does it say?

Anis: "IndentationError: unexpected indent, line 7".

Lina: Perfect, we have the address (line 7) and the diagnosis (unexpected indentation). Ask AI for the WHY, not the fix.

Anis (to AI): Why "unexpected indent" on line 7 of my code [pastes]?

AI: Because line 7 is shifted without a line ending with ":" before it. Python expects a block after ":".

Mr Karim: You see? The error was talking. Now fix it YOURSELF, then ask for a similar mini-exercise.

Anis: Fixed… and the similar exercise passed! The bug was a teacher in disguise.

---

## Dialogue B — "My very own AI" (15 min)

**Characters:** Sara (student), her brother Yacine, the screen (played by a classmate).

---

Sara: Look, Yacine: I type a question, and it is MY program answering!

Yacine: Wait… did you program ChatGPT?!

Sara: No! My script sends my question to the Gemini counter with my key, and displays the answer. Only fifteen lines.

Screen: You > Explain photosynthesis in 3 points. / AI > 1)… 2)… 3)…

Yacine: And if I want it to remember what we said?

Sara: I add a "history" list: on each call, I resend the last 6 exchanges. Try: ask it "and in Arabic?".

Yacine: It understood! Without me repeating the question… That is memory?

Sara: Exactly: the model forgets everything, it is MY script reminding it. I became an AI builder!

---

## Mini role-play (3 min per pair)
One pastes a code with a classic mistake, the other phrases the diagnosis prompt ("why", not "fix"). Swap, then vote for the class's best diagnosis.
""",
}
