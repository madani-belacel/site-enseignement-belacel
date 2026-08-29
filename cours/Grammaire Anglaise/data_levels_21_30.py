# -*- coding: utf-8 -*-
"""المستويات 21–30 : ابتدائي (A1/A2) — الهوايات، الضمائر، الحاضر المستمر، الماضي، المستقبل.""" 

LEVELS = [

# ============================ NIVEAU 21 ============================
{
"num": 21, "cefr": "A1",
"category": "Like + -ing",
"category_ar": "أحب + الفعل بصيغة ing",
"title_en": "Like, Love, Hate + -ing",
"title_ar": "أحب / أحب كثيراً / أكره + فعل (ing)",
"ideas": [
{
"en": "Like + verb-ing",
"ar": "like + فعل بـ ing",
"expl_ar": "عندما نحب فعل شيء نقول: like + فعل-ing.\nمثال: I like reading (أحب القراءة)، She likes cooking (تحب الطبخ).\nمع he/she نضيف s للفعل like: likes.",
"expl_en": "To talk about things you enjoy: like + verb-ing. With he/she/it use 'likes'.",
"formula": "subject + like/likes + verb-ing",
"examples": [
("I like reading the Quran.", "أحب قراءة القرآن."),
("She likes listening to music.", "تحب الاستماع إلى الموسيقى."),
("We like watching documentaries.", "نحب مشاهدة الوثائقيات.")]},
{
"en": "Love + verb-ing (strong like)",
"ar": "love + فعل بـ ing (حب شديد)",
"expl_ar": "love (أحب كثيراً) أقوى من like (أحب): I love swimming (أحب السباحة)، He loves football (يحب كرة القدم).\nنستعملها مع الأنشطة التي تمنحنا فرحاً كبيراً.",
"expl_en": "'Love' is a stronger like. Use it with -ing: I love swimming.",
"formula": "subject + love/loves + verb-ing",
"examples": [
("I love swimming in summer.", "أحب السباحة كثيراً في الصيف."),
("He loves playing chess.", "يحب لعب الشطرنج كثيراً."),
("Kids love eating ice cream.", "يحب الأطفال أكل المثلجات.")]},
{
"en": "Hate + verb-ing (dislike)",
"ar": "hate + فعل بـ ing (كره)",
"expl_ar": "hate (أكره) تعبر عن الكره: I hate getting up early (أكره الاستيقاظ مبكراً).\nبين don't like (لا أحب) و hate (أكره) فرق في الشدة.",
"expl_en": "'Hate' expresses strong dislike: I hate getting up early.",
"formula": "subject + hate/hates + verb-ing",
"examples": [
("I hate waiting in long queues.", "أكره الانتظار في الطوابير الطويلة."),
("He hates doing the dishes.", "يكره غسل الأطباق."),
("My sister hates getting up at dawn.", "أختي تكره الاستيقاظ فجرا.")]},
{
"en": "Don't like / doesn't like + verb-ing",
"ar": "لا أحب / لا يحب + فعل بـ ing",
"expl_ar": "للنفي: don't like مع I/you/we/they و doesn't like مع he/she/it:\nI don't like shopping (لا أحب التسوق)، He doesn't like walking (لا يحب المشي).",
"expl_en": "Negative: don't like / doesn't like + verb-ing.",
"formula": "subject + don't/doesn't like + verb-ing",
"examples": [
("I don't like eating very spicy food.", "لا أحب أكل الطعام الحار جدا."),
("She doesn't like going out at night.", "لا تحب الخروج ليلا."),
("They don't like playing video games.", "لا يحبون ألعاب الفيديو.")]},
{
"en": "Hobbies: swimming, reading, hiking...",
"ar": "الهوايات: السباحة، القراءة، المشي...",
"expl_ar": "للتعبير عن هواية أضف ing للفعل: swim→swimming، read→reading، walk→walking، paint→painting، travel→travelling، cook→cooking، play→playing.",
"expl_en": "For hobbies add -ing: reading, swimming, painting, cooking.",
"formula": "hobby = verb-ing (swimming, reading...)",
"examples": [
("My hobby is drawing.", "هوايتي هي الرسم."),
("I enjoy playing football.", "أستمتع بلعب كرة القدم."),
("She likes painting on Sundays.", "تحب الرسم يوم الأحد.")]},
{
"en": "Prefer + verb-ing",
"ar": "prefer + فعل بـ ing (أفضّل)",
"expl_ar": "prefer (أفضّل) تعبر عن الاختيار: I prefer drinking tea (أفضل شرب الشاي).\nنستعملها لمقارنة اختياراتنا.",
"expl_en": "'Prefer' shows a choice: I prefer drinking tea to coffee.",
"formula": "subject + prefer/prefers + verb-ing",
"examples": [
("I prefer reading to watching TV.", "أفضل القراءة على مشاهدة التلفاز."),
("She prefers travelling by train.", "تفضل السفر بالقطار."),
("We prefer eating at home.", "نفضل الأكل في المنزل.")]},
{
"en": "Enjoy + verb-ing",
"ar": "enjoy + فعل بـ ing (أستمتع)",
"expl_ar": "enjoy (أستمتع بـ) تأتي قبل الفعل بـ ing أيضاً: I enjoy cooking (أستمتع بالطبخ)، We enjoy playing (نستمتع باللعب).\nلا نقول enjoy to cook لذلك احفظ: enjoy + ing.",
"expl_en": "'Enjoy' always takes verb-ing: I enjoy cooking. Not 'enjoy to cook'.",
"formula": "subject + enjoy/enjoys + verb-ing",
"examples": [
("I enjoy planting vegetables.", "أستمتع بزرع الخضار."),
("He enjoys solving puzzles.", "يستمتع بحل الألغاز."),
("We enjoy spending time with family.", "نستمتع بقضاء الوقت مع العائلة.")]},
{
"en": "Would like / Would love + to + verb",
"ar": "would like / would love + to + فعل",
"expl_ar": "للرغبة المؤدبة نستعمل would like + to + فعل: I would like to travel (أود السفر).\nهذه ليست like + ing بل قاعدة مختلفة.",
"expl_en": "For polite wishes: would like + to + verb. I would like to travel.",
"formula": "subject + would like/love + to + base verb",
"examples": [
("I would like to visit Makkah.", "أود زيارة مكة."),
("She would love to learn English.", "تحب أن تتعلم الإنجليزية (ستسعد بذلك)."),
("We would like to stay here.", "نود البقاء هنا.")]},
{
"en": "Key verbs with -ing: finish, start, stop",
"ar": "أفعال تأخذ ing: finish, start, stop",
"expl_ar": "بعض الأفعال تأتي بعدها فعل -ing دائماً: finish (ينهي)، start (يبدأ)، stop (يتوقف)، keep (يستمر):\nstop talking (توقف عن الكلام)، start working (ابدأ العمل).",
"expl_en": "Some verbs take -ing after them: finish, start, stop, keep.",
"formula": "start/stop/finish/keep + verb-ing",
"examples": [
("Stop talking, please.", "توقف عن الكلام من فضلك."),
("I finished doing my homework.", "أنهيت واجبي."),
("She started crying.", "بدأت تبكي.")]},
{
"en": "What do you like doing?",
"ar": "ماذا تحب أن تفعل؟",
"expl_ar": "سؤال شائع: What do you like doing? (ماذا تحب أن تفعل؟) أو What is your hobby? (ما هي هوايتك؟).\nالجواب: I like... + ing، ورد بالمثل: And you? (وأنت؟)",
"expl_en": "Question: What do you like doing? Answer: I like + verb-ing.",
"formula": "What do you like doing? → I like + -ing.",
"examples": [
("What do you like doing in your free time?", "ماذا تحب أن تفعل في وقت فراغك؟"),
("I like playing with my friends.", "أحب اللعب مع أصدقائي."),
("What does your brother like doing?", "ماذا يحب أخوك أن يفعل؟")]},
]
},
# ============================ NIVEAU 22 ============================
{
"num": 22, "cefr": "A1",
"category": "Object Pronouns",
"category_ar": "ضمائر المفعول",
"title_en": "Object Pronouns: me, you, him, her, it, us, them",
"title_ar": "ضمائر المفعول",
"ideas": [
{
"en": "What are object pronouns?",
"ar": "ما هي ضمائر المفعول؟",
"expl_ar": "ضمائر المفعول تأتي بعد الفعل أو حرف الجر، وهي مفعول به:\nme (إياي)، you (إياك)، him (إياه)، her (إياها)، it (له/لها)، us (إيانا)، them (إياهم).",
"expl_en": "Object pronouns come after verbs or prepositions: me, you, him, her, it, us, them.",
"formula": "I→me • you→you • he→him • she→her • it→it • we→us • they→them",
"examples": [
("Call me tomorrow.", "اتصل بي غدا."),
("Help them, please.", "ساعدهم من فضلك."),
("We love her very much.", "نحبها كثيرا.")]},
{
"en": "Position: after the verb",
"ar": "المكان: بعد الفعل",
"expl_ar": "ضمير المفعول يأتي بعد الفعل مباشرة: I know him (أعرفه)، She helps us (تساعدنا).\nلا نستعمله في مكان الفاعل.",
"expl_en": "Object pronouns come after the verb: I know him, She helps us.",
"formula": "subject + verb + object pronoun",
"examples": [
("I understand you.", "أفهمك."),
("He sees her every day.", "يراها كل يوم."),
("We invited them to dinner.", "دعوناهم إلى العشاء.")]},
{
"en": "Me vs I",
"ar": "الفرق بين me و I",
"expl_ar": "I ضمير فاعل (قبل الفعل)، و me ضمير مفعول (بعد الفعل أو الجار):\nI love you (أنا أحبك)، You love me (أنت تحبني).",
"expl_en": "'I' = subject (before verb). 'Me' = object (after verb or preposition).",
"formula": "I + verb | verb + me / with me",
"examples": [
("I am from Algeria.", "أنا من الجزائر."),
("Listen to me, please.", "استمع إلي من فضلك."),
("Come with me.", "تعال معي.")]},
{
"en": "Him vs her",
"ar": "him بالمذكر و her بالمؤنث",
"expl_ar": "him للذكر (أمير، الأب، الحصان المذكر)، her للمؤنث (أميرة، الأم).\nأمثلة: Call him (اتصل به)، Visit her (زرها).",
"expl_en": "'Him' = a man. 'Her' = a woman.",
"formula": "verb + him (man) | verb + her (woman)",
"examples": [
("Tell him the news.", "أخبره بالخبر."),
("Ask her about the exam.", "اسألها عن الامتحان."),
("I sent him a message.", "أرسلت له رسالة.")]},
{
"en": "It: for things and animals",
"ar": "it للأشياء والحيوانات",
"expl_ar": "نستعمل it للإشارة إلى شيء أو حيوان سبق ذكره:\nI have a phone (لدي هاتف). I use it every day (أستعمله يومياً).",
"expl_en": "'It' refers to things/animals already mentioned: I use it every day.",
"formula": "verb + it (thing/animal)",
"examples": [
("Here is your book. Take it.", "هذا كتابك. خذه."),
("The dog is nice. I like it.", "الكلب لطيف. أحبه."),
("This food is tasty. Try it.", "هذا الطعام لذيذ. جربه.")]},
{
"en": "Us = we (object), Them = they (object)",
"ar": "us و them (المفعول من نحن وهم)",
"expl_ar": "We→us (نحن/إيانا)، They→them (هم/إياهم):\nThey help us (يساعدوننا)، We visit them (نزورهم).",
"expl_en": "We→us, they→them: They help us, We visit them.",
"formula": "verb + us | verb + them",
"examples": [
("Our friends visit us every week.", "أصدقاؤنا يزوروننا كل أسبوع."),
("The teacher teaches us English.", "يعلمنا الأستاذ الإنجليزية."),
("I called them last night.", "اتصلت بهم الليلة الماضية.")]},
{
"en": "Object pronouns after prepositions",
"ar": "ضمائر المفعول بعد حروف الجر",
"expl_ar": "بعد حروف الجر (with, to, for, at, from) نستعمل ضمير المفعول:\nwith me، to him، for her، at us، from them.",
"expl_en": "After prepositions use object pronouns: with me, for her, to them.",
"formula": "preposition (with/to/for) + object pronoun",
"examples": [
("This gift is for you.", "هذه الهدية لك."),
("I am proud of them.", "أنا فخور بهم."),
("She is talking to us.", "تتحدث إلينا.")]},
{
"en": "Two objects: verb + person + thing",
"ar": "مفعولان: فعل + شخص + شيء",
"expl_ar": "بعض الأفعال تأخذ مفعولين: شخصاً ثم شيئاً:\nGive me the pen (أعطني القلم)، Show us your photos (أرنا صورك)، Tell him the truth (قل له الحقيقة).",
"expl_en": "Some verbs take two objects: Give me the pen. Show us your photos.",
"formula": "verb + someone + something",
"examples": [
("Give me the salt, please.", "أعطني الملح من فضلك."),
("Please bring us some water.", "أحضر لنا بعض الماء من فضلك."),
("I showed her my new bike.", "أريتها دراجتي الجديدة.")]},
{
"en": "Fill in the pronoun",
"ar": "أكمل الضمير الصحيح",
"expl_ar": "تمرين: أنظر للفاعل واختر المفعول المناسب:\nI love (she) → I love her. We need (he) → We need him.\nنستعمل الكلمة الابتدائية لتحديد الضمير.",
"expl_en": "Practise changing subject to object: she→her, he→him, we→us.",
"formula": "she→her • he→him • we→us • they→them",
"examples": [
("I love my mother. I love her.", "أحب أمي. أحبها."),
("He is our friend. We need him.", "هو صديقنا. نحتاجه."),
("The children are here. Feed them.", "الأطفال هنا. أطعمهم.")]},
{
"en": "Object pronouns in everyday speech",
"ar": "ضمائر المفعول في الكلام اليومي",
"expl_ar": "تجدها في كل جملة يومية:\nThank you (شكراً لك)، Excuse me (المعذرة)، Help me (ساعدني)، Call us (اتصل بنا)، I miss you (أشتاق لك)، I trust you (أثق بك).",
"expl_en": "Daily phrases: Thank you, Excuse me, Help me, I miss you.",
"formula": "daily: me/you/us (in requests and thanks)",
"examples": [
("I miss you so much.", "أشتاق إليك كثيرا."),
("Trust me, everything will be fine.", "ثق بي، كل شيء سيكون بخير."),
("Please forgive us.", "سامحنا من فضلك.")]},
]
},
# ============================ NIVEAU 23 ============================
{
"num": 23, "cefr": "A1",
"category": "Possessive Pronouns",
"category_ar": "ضمائر الملكية",
"title_en": "Possessive Pronouns: mine, yours, his, hers, ours, theirs",
"title_ar": "ضمائر الملكية",
"ideas": [
{
"en": "What are possessive pronouns?",
"ar": "ما هي ضمائر الملكية؟",
"expl_ar": "ضمائر الملكية تحل محل اسم + صفة ملكية:\nmy book ← mine (لي)، your book ← yours (لك)، his book ← his، her book ← hers، our ← ours، their ← theirs.",
"expl_en": "Possessive pronouns replace 'possessive adjective + noun': my book → mine.",
"formula": "my→mine • your→yours • his→his • her→hers • our→ours • their→theirs",
"examples": [
("This book is mine.", "هذا الكتاب لي."),
("The blue car is ours.", "السيارة الزرقاء لنا."),
("Which bag is hers?", "أي حقيبة لها؟")]},
{
"en": "Stand alone: no noun after them",
"ar": "تقف وحدها: لا اسم بعدها",
"expl_ar": "ضمير الملكية لا يتبعه اسم أبداً: This pen is mine (هذا القلم لي) ولا نقول mine pen.\nصفة الملكية قبل الاسم والضمير بديل له.",
"expl_en": "Possessive pronouns never take a noun after them: It is mine (not 'mine pen').",
"formula": "subject + be + possessive pronoun",
"examples": [
("Is this phone yours?", "هل هذا الهاتف لك؟"),
("No, it's his.", "لا، إنه له."),
("The green pencils are theirs.", "الأقلام الخضراء لهم.")]},
{
"en": "Mine = my + noun",
"ar": "mine = my + اسم",
"expl_ar": "مثال مقارن: My bag is red → The red bag is mine (حقيبتي حمراء → الحقيبة الحمراء لي).\nmine اختصار لـ my bag دون تكرار الاسم.",
"expl_en": "Mine = my + noun. My bag → The bag is mine.",
"formula": "This is my bag = This bag is mine.",
"examples": [
("My keys are here. These are mine.", "مفاتيحي هنا. هذه مفاتيحي (لي)."),
("Her opinion matters, but mine too.", "رأيها مهم، ورأيي كذلك."),
("Take my pen and leave yours.", "خذ قلمي واترك قلمك.")]},
{
"en": "Yours / His / Hers",
"ar": "yours / his / hers",
"expl_ar": "لاحظ: his و its لا يتغيران (his = له و his = ضمير له كما هو).\nhers للمؤنث، yours لك (مفرد وجمع).",
"expl_en": "Note: 'his' stays the same. 'hers' is for women, 'yours' for you.",
"formula": "his (same) • hers (her + noun) • yours (your + noun)",
"examples": [
("The decision is yours.", "القرار لك."),
("This seat is his.", "هذا المقعد له."),
("That jacket is hers.", "تلك السترة لها.")]},
{
"en": "Ours / Theirs",
"ar": "ours / theirs",
"expl_ar": "ours (لنا) لـ we، theirs (لهم) لـ they:\nThis house is ours (هذا البيت لنا)، Those toys are theirs (تلك الألعاب لهم).",
"expl_en": "Ours = for us; theirs = for them.",
"formula": "our + noun → ours | their + noun → theirs",
"examples": [
("The victory is ours!", "النصر لنا!"),
("This project is theirs, not ours.", "هذا المشروع لهم، ليس لنا."),
("Our garden is bigger than theirs.", "حديقتنا أكبر من حديقتهم.")]},
{
"en": "A friend of mine",
"ar": "صديق لي (من أصدقائي)",
"expl_ar": "تعبير مشهور: a friend of mine (صديق من أصدقائي)، a neighbour of ours (جار من جيراننا).\nنستعمل هذه الصيغة مع ضمير الملكية وليس صفة الملكية.",
"expl_en": "Special pattern: a friend of mine, a neighbour of ours.",
"formula": "a/an + noun + of + possessive pronoun",
"examples": [
("Islem is a friend of mine.", "إسلام صديق من أصدقائي."),
("She is a colleague of hers.", "هي زميلة من زميلاتها."),
("This is a habit of theirs.", "هذه عادة من عاداتهم.")]},
{
"en": "Whose?? mine, yours... in answers",
"ar": "الجواب عن Whose بضمائر الملكية",
"expl_ar": "عند السؤال Whose book is this? (لمن هذا الكتاب؟) نجيب: It's mine / It's yours / It's hers (إنه لي / لك / لها).\nنستعمل ضمير الملكية أو 's أو اسم صاحب.",
"expl_en": "Answer 'Whose...?' with a possessive pronoun or owner's name.",
"formula": "Whose + noun? → It's mine/yours/his/hers/ours/theirs.",
"examples": [
("Whose glasses are these?", "لمن هذه النظارة؟"),
("They are my mother's. They're hers.", "إنها لأمي. إنها لها."),
("Whose turn is it? It's yours.", "لمن الدور الآن؟ إنه لك.")]},
{
"en": "Difference: adjective vs pronoun",
"ar": "الفرق: صفة الملكية مقابل ضمير الملكية",
"expl_ar": "الصفة قبل الاسم: this is my cat (هذه قطتي)، والضمير وحده: this cat is mine (هذه القطة لي).\nلا نستعمل الضمير قبل الاسم أبداً.",
"expl_en": "Adjective + noun (my cat). Pronoun alone (mine). Never together: 'mine cat' is wrong.",
"formula": "my + noun | noun + be + mine",
"examples": [
("This is my phone. This phone is mine.", "هذا هاتفي. هذا الهاتف لي."),
("Our school is near. The one opposite is theirs.", "مدرستنا قريبة. المجاورة لهم."),
("Her idea is good, but ours is better.", "فكرتها جيدة، لكن فكرتنا أفضل.")]},
{
"en": "The pronoun replaces the whole phrase",
"ar": "الضمير يحل محل الجملة كلها",
"expl_ar": "بدل أن نكرر الاسم، نستعمل الضمير: Your car is new → Is yours new? (سيارتك جديدة → هل سيارتك جديدة؟).\nنحذف car ونبقي yours؛ هذا يقلل التكرار في الكلام.",
"expl_en": "Avoid repetition: replace 'your car' with 'yours'.",
"formula": "your car → yours",
"examples": [
("My shoes are old. Yours are new.", "حذائي قديم. حذاؤك جديد."),
("Her exam was hard. His was easy.", "امتحانها صعب. امتحانه سهل."),
("Our plan is clear. What about theirs?", "خطتنا واضحة. ماذا عن خطتهم؟")]},
{
"en": "Context: mine on its own",
"ar": "سياق: mine وحدها",
"expl_ar": "يمكن أن يستخدم الضمير وحده في المواقف، مثل: Whose turn? Mine! (لمن الدور؟ لي!)، It's all mine (كله لي).\nهي عبارات سريعة في الحديث.",
"expl_en": "Possessive pronouns also work alone: Whose turn? Mine!",
"formula": "Whose + noun? → (It's) mine/yours...",
"examples": [
("Whose turn is it? Mine!", "لمن الدور؟ لي!"),
("This cookie is all mine.", "هذه البسكويتة كلها لي."),
("Is that seat taken? No, it's yours.", "هل هذا المقعد محجوز؟ لا، إنه لك.")]},
]
},
# ============================ NIVEAU 24 ============================
{
"num": 24, "cefr": "A1",
"category": "Present Continuous",
"category_ar": "المضارع المستمر",
"title_en": "Present Continuous: am/is/are + -ing",
"title_ar": "المضارع المستمر: الآن يحدث",
"ideas": [
{
"en": "What is present continuous?",
"ar": "ما هو المضارع المستمر؟",
"expl_ar": "المضارع المستمر يصف شيئاً يحدث الآن لحظة الكلام:\nI am writing now (أكتب الآن)، She is sleeping (تنام الآن).\nالتركيب: am/is/are + فعل + ing.",
"expl_en": "Present continuous describes actions happening now: I am writing now.",
"formula": "subject + am/is/are + verb-ing",
"examples": [
("I am reading a book now.", "أقرأ كتابا الآن."),
("She is cooking lunch.", "تطبخ الغداء الآن."),
("They are playing in the garden.", "يلعبون في الحديقة الآن.")]},
{
"en": "Structure: to be + verb-ing",
"ar": "التركيب: فعل كينونة + فعل + ing",
"expl_ar": "لا تنس فعل الكينونة: am مع I، is مع المفرد، are مع الجمع.\nثم الفعل + ing: I am studying (أدرس)، He is listening (يستمع)، We are eating (نأكل).",
"expl_en": "Always use am/is/are + verb-ing. Never skip the verb to be.",
"formula": "I am • he/she/it is • you/we/they are + verb-ing",
"examples": [
("I am studying English now.", "أدرس الإنجليزية الآن."),
("The baby is crying.", "الرضيع يبكي."),
("We are having lunch.", "نتناول الغداء الآن.")]},
{
"en": "Adding -ing: spelling rules",
"ar": "قواعد إضافة ing",
"expl_ar": "معظم الأفعال نضيف ing مباشرة: play→playing.\nفعل ينتهي بـ e نحذفها: make→making، write→writing.\nفعل ينتهي بحرف ساكن والآخر علة نضاعف الساكن: run→running، swim→swimming، sit→sitting.",
"expl_en": "Spelling: play→playing; drop e (make→making); double final consonant (run→running).",
"formula": "+ing | drop-e | double consonant",
"examples": [
("make → making (drop e)", "يصنع ← يصنع الآن."),
("run → running (double n)", "يركض ← يركض الآن."),
("sit → sitting (double t)", "يجلس ← يجلس الآن.")]},
{
"en": "Now, at the moment, today",
"ar": "كلمات الوقت: now, at the moment, today",
"expl_ar": "مظاهر الوقت: now (الآن)، at the moment (في هذه اللحظة)، right now (في هذه اللحظة)، these days (في هذه الفترة).",
"expl_en": "Time words: now, at the moment, right now, these days.",
"formula": "subject + be + verb-ing + (now/at the moment)",
"examples": [
("She is studying at the moment.", "تدرس في هذه اللحظة."),
("They are watching TV right now.", "يشاهدون التلفاز في هذه اللحظة."),
("These days, we are building a house.", "في هذه الفترة نبني منزلا.")]},
{
"en": "Negative: am not / isn't / aren't + -ing",
"ar": "النفي: ليس الآن",
"expl_ar": "النفي بإضافة not بعد be:\nI am not sleeping (لست نائماً)، She isn't working (لا تعمل)، They aren't coming (لا يأتون).\nالاختصارات: isn't و aren't.",
"expl_en": "Negative: am not / isn't / aren't + verb-ing.",
"formula": "subject + be + not + verb-ing",
"examples": [
("I am not joking.", "أنا لا أمزح."),
("It is not raining now.", "لا تمطر الآن."),
("They aren't playing outside.", "لا يلعبون في الخارج.")]},
{
"en": "Questions: Are you ...-ing?",
"ar": "السؤال: هل تفعل الآن؟",
"expl_ar": "نبدأ السؤال بفعل الكينونة:\nAre you listening? (هل تستمع؟)، Is he coming? (هل هو قادم؟)، What are you doing? (ماذا تفعل؟).",
"expl_en": "Question: be + subject + verb-ing? Are you listening?",
"formula": "Am/Is/Are + subject + verb-ing?",
"examples": [
("Are you listening to me?", "هل تستمع إلي؟"),
("Is your father working today?", "هل يعمل والدك اليوم؟"),
("What are you doing there?", "ماذا تفعل هناك؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I am. / No, I'm not.\nمع المفرد: Yes, he is. / No, she isn't.\nالجمع: Yes, they are. / No, they aren't.",
"expl_en": "Short answers: Yes, I am. No, I'm not. Yes, he is. No, they aren't.",
"formula": "Yes, + pronoun + be | No, + pronoun + be + n't",
"examples": [
("Are you busy? Yes, I am.", "هل أنت مشغول؟ نعم."),
("Is she here? No, she isn't.", "هل هي هنا؟ لا."),
("Are they leaving? No, they aren't.", "هل يغادرون؟ لا.")]},
{
"en": "Temporary actions",
"ar": "أفعال مؤقتة",
"expl_ar": "المضارع المستمر يصف أفعالاً مؤقتة حول الآن:\nI'm reading a new book these days (أقرأ كتاباً جديداً في هذه الفترة)، He's living with his uncle this month (يعيش عند عمه هذا الشهر).",
"expl_en": "Present continuous for temporary actions around now: I'm reading a new book these days.",
"formula": "temporary: be + verb-ing + (this week/month)",
"examples": [
("She is staying with her aunt this week.", "تقيم عند خالتها هذا الأسبوع."),
("I am learning to drive these days.", "أتعلم القيادة في هذه الفترة."),
("They are painting the house this week.", "يطلون المنزل هذا الأسبوع.")]},
{
"en": "Plans for near future",
"ar": "خطط المستقبل القريب",
"expl_ar": "نستعمل المضارع المستمر للخطط المقررة مسبقاً:\nWe are going to the beach tomorrow (سنذهب إلى الشاطئ غداً بترتيب)، I'm meeting him at 5 (سأقابله عند الخامسة).",
"expl_en": "Present continuous for arranged future plans: We are going tomorrow.",
"formula": "be + verb-ing + future time (tomorrow) = a plan",
"examples": [
("I am visiting my grandmother tomorrow.", "أزور جدتي غدا."),
("We are having dinner at their house tonight.", "نتناول العشاء عندهم الليلة."),
("She is flying to France next week.", "تسافر إلى فرنسا الأسبوع القادم.")]},
{
"en": "Spelling: -ie verbs change to -ying",
"ar": "إملاء: الأفعال المنتهية بـ ie تتحول إلى ying",
"expl_ar": "الأفعال المنتهية بـ ie تحولها إلى ying: lie→lying (يكذب)، die→dying (يموت)، tie→tying (يربط).\nننتبه: هي فعل يختلف عن lie بمعنى يستلقي.",
"expl_en": "Verbs ending -ie → -ying: lie→lying, die→dying, tie→tying.",
"formula": "lie→lying • die→dying • tie→tying",
"examples": [
("He is lying on the grass.", "مستلق على العشب."),
("The old phone is dying.", "الهاتف القديم قرب الموت."),
("She is tying her shoes.", "تربط حذاءها.")]},
{
"en": "Present continuous with always (habits)",
"ar": "المضارع المستمر مع always (عادة)",
"expl_ar": "أحياناً نستعمل المستمر مع always للتعبير عن عادة متكررة أو مزعجة:\nHe is always complaining (دائماً يشكو).\nالمعنى: يحدث كثيراً وقد ينزعج المتكلم.",
"expl_en": "With 'always', continuous shows a repeated or annoying habit: He's always complaining.",
"formula": "subject + be + always + verb-ing",
"examples": [
("She is always losing her keys.", "دائما تضيع مفاتيحها."),
("He is always talking in class.", "دائما يتكلم في القسم."),
("You are always helping others.", "دائما تساعد الآخرين (مدح).")]},
]
},
# ============================ NIVEAU 25 ============================
{
"num": 25, "cefr": "A1",
"category": "Present Simple vs Continuous",
"category_ar": "المضارع البسيط مقابل المستمر",
"title_en": "Present Simple vs Present Continuous",
"title_ar": "المقارنة بين المضارع البسيط والمستمر",
"ideas": [
{
"en": "Simple = habits, Continuous = now",
"ar": "البسيط للعادات، والمستمر للآن",
"expl_ar": "الفرق الأساسي: المضارع البسيط لعادة دائمة: I eat rice (عادة).\nوالمضارع المستمر لفعل يحدث الآن: I am eating rice (أنا أتناول الآن).",
"expl_en": "Simple = habits (I eat rice every day). Continuous = right now (I am eating now).",
"formula": "habit → Simple | now → Continuous",
"examples": [
("I play football every Friday.", "ألعب كرة القدم كل جمعة (عادة)."),
("I am playing football now.", "ألعب كرة القدم الآن (لحظياً)."),
("She drinks tea in the morning.", "تشرب الشاي صباحا (عادة).")]},
{
"en": "Key words: always/every day vs now/look",
"ar": "كلمات دالة: دائماً/كل يوم مقابل الآن/انظر",
"expl_ar": "البسيط: always (دائماً)، usually (عادةً)، every day (كل يوم)، on Fridays (يوم الجمعة)، twice a week (مرتين في الأسبوع).\nالمستمر: now (الآن)، at the moment (في هذه اللحظة)، Look! (انظر!)، Listen! (استمع!).",
"expl_en": "Simple words: always, usually, every day. Continuous words: now, at the moment, Look!, Listen!.",
"formula": "Simple: always/every day | Continuous: now/at the moment",
"examples": [
("I always go to the mosque at dawn.", "أذهب دائما إلى المسجد فجرا."),
("Look! The teacher is coming.", "انظر! الأستاذ قادم."),
("Listen! Someone is knocking.", "استمع! أحدهم يطرق الباب.")]},
{
"en": "Same verb, different meaning",
"ar": "نفس الفعل، معنى مختلف",
"expl_ar": "لاحظ الفرق: He works in Oran (يعمل هناك عادة)، He is working now (يعمل الآن).\nالفعل يعمل في الموضعين لكن الزمن يحدد المعنى.",
"expl_en": "Watch the difference: He works (habit) vs he is working (now).",
"formula": "state (works) | action now (is working)",
"examples": [
("She teaches at our school.", "تُدرّس في مدرستنا (وظيفتها)."),
("She is teaching right now.", "تدرس الآن (في هذه اللحظة)."),
("They live in Ain Temouchent.", "يعيشون في عين تموشنت (وضع دائم).")]},
{
"en": "Stative verbs: no -ing",
"ar": "الأفعال الحالة: لا ing معها",
"expl_ar": "أفعال الحالة لا تأخذ ing: like (يحب)، love (يحب كثيراً)، hate (يكره)، know (يعرف)، understand (يفهم)، want (يريد)، need (يحتاج)، believe (يؤمن)، remember (يتذكر).\nنقول I know (أعرف) وليس I am knowing.",
"expl_en": "Stative verbs do not use -ing: like, love, know, want, need, understand.",
"formula": "I like/understand/know (no -ing)",
"examples": [
("I know the answer.", "أعرف الجواب (لا: I am knowing)."),
("He wants a new phone.", "يريد هاتفا جديدا."),
("Do you understand the lesson?", "هل تفهم الدرس؟")]},
{
"en": "Present simple: facts; continuous: ongoing",
"ar": "البسيط للحقائق، والمستمر للجاري",
"expl_ar": "الحقائق العلمية دائماً بسيط: Water boils at 100° (يغلي الماء عند 100 درجة).\nالجاري الآن مستمر: The water is boiling (الماء يغلي الآن).",
"expl_en": "Facts: simple (Water boils at 100°). Ongoing now: continuous (The water is boiling).",
"formula": "fact → Simple | happening now → Continuous",
"examples": [
("The sun rises in the east.", "تشرق الشمس من الشرق."),
("Look, the sun is rising!", "انظر، الشمس تشرق الآن!"),
("In winter it rains a lot.", "في الشتاء تمطر كثيرا (عادة).")]},
{
"en": "Building both forms side by side",
"ar": "بناء الشكلين جنباً إلى جنب",
"expl_ar": "درب نفسك بتحويل الجملة: I study (عادة) → I am studying now (الآن).\nغيّر الظرف الزمني وتتغير الصيغة المعتمدة.",
"expl_en": "Convert habits to ongoing: I study → I am studying now.",
"formula": "I study (habit) → I am studying (now)",
"examples": [
("I read the paper daily.", "أقرأ الصحيفة يوميا."),
("I am reading the paper now.", "أقرأ الصحيفة الآن."),
("We pray Fajr at dawn.", "نصلي الفجر عند الفجر.")]},
{
"en": "Questions: both forms",
"ar": "السؤال بالشكلين",
"expl_ar": "السؤال يتبع الحالة:\nعادة: Do you play? (هل تلعب؟) | الآن: Are you playing? (هل تلعب الآن؟)\nحقائق: Does it rain here? (هل تمطر هنا؟) | جارية: Is it raining? (هل تمطر الآن؟)",
"expl_en": "Question forms: Do you play? (habit) Are you playing? (now).",
"formula": "Do/Does + subject + verb? | Am/Is/Are + subject + verb-ing?",
"examples": [
("Do you work on Friday?", "هل تعمل يوم الجمعة (عادة)؟"),
("Are you working right now?", "هل تعمل الآن؟"),
("Does it snow in your city?", "هل تثلج في مدينتك؟")]},
{
"en": "Describing a photo: continuous",
"ar": "وصف صورة",
"expl_ar": "لوصف صورة نستعمل المضارع المستمر بكثرة:\nIn the photo, the children are playing (في الصورة، يلعب الأطفال)، A man is selling fruits (رجل يبيع الفواكه)، Some people are walking (بعض الناس يمشون).",
"expl_en": "To describe a photo use continuous: In the photo, people are walking.",
"formula": "In the picture, + subject + be + verb-ing",
"examples": [
("In the photo, the family is having lunch.", "في الصورة، تتناول العائلة الغداء."),
("A boy is flying a kite.", "يلعب صبي بطائرة ورقية."),
("Some people are sitting under the tree.", "بعض الناس يجلسون تحت الشجرة.")]},
{ 
"en": "Choosing the right tense",
"ar": "اختر الزمن الصحيح",
"expl_ar": "اسأل نفسك: هل الفعل متكرر عادة؟ ← بسيط.\nهل يجري الآن لحظة الكلام؟ ← مستمر.\nانظر إلى الظروف الزمنية قبل الاختيار.",
"expl_en": "Ask: Is it a habit? → Simple. Is it happening now? → Continuous.",
"formula": "repeated → Simple | at this moment → Continuous",
"examples": [
("Every morning I drink milk.", "كل صباح أشرب الحليب."),
("Right now I am drinking tea.", "في هذه اللحظة أشرب الشاي."),
("He often visits his uncle.", "يزور عمه كثيرا.")]},
{
"en": "Common confusion: state verbs + feelings now",
"ar": "الخلط الشائع: أفعال الحالة والمشاعر الآن",
"expl_ar": "عند وصف مشاعر أو تفكير الآن نبقى في البسيط لأنها أفعال حالة: I know now (أعرف الآن)، I want now (أريد الآن)، I love now (أحب الآن).\nلا نقول am knowing أو am loving عادة.",
"expl_en": "Feelings/thoughts use simple even 'now': I know, I want, I love (not 'am knowing').",
"formula": "I/He + know/want/love (state) even now",
"examples": [
("I want some water now.", "أريد ماء الآن."),
("We understand the problem now.", "نفهم المشكلة الآن."),
("Do you know her? Yes, I do.", "هل تعرفها؟ نعم أعرفها.")]},
]
},
# ============================ NIVEAU 26 ============================
{
"num": 26, "cefr": "A1",
"category": "Past Simple: To Be",
"category_ar": "الماضي البسيط: كان",
"title_en": "Past Simple: was / were",
"title_ar": "الماضي البسيط: was / were (كان)",
"ideas": [
{
"en": "Was / Were = to be in the past",
"ar": "was / were: فعل الكينونة في الماضي",
"expl_ar": "في الماضي يتحول am/is إلى was و are إلى were: I/he/she/it + was، you/we/they + were.\nالمثال: I was at home (كنت في البيت).",
"expl_en": "Past of to be: was (I/he/she/it) and were (you/we/they).",
"formula": "I/He/She/It + was | You/We/They + were",
"examples": [
("I was at school yesterday.", "كنت في المدرسة أمس."),
("She was happy to see us.", "كانت سعيدة برؤيتنا."),
("They were at home last night.", "كانوا في البيت الليلة الماضية.")]},
{
"en": "Yesterday, last..., ago",
"ar": "كلمات الماضي: أمس، الماضي، منذ",
"expl_ar": "علامات الماضي: yesterday (أمس)، last week (الأسبوع الماضي)، last year (السنة الماضية)، two days ago (منذ يومين)، in 2020.",
"expl_en": "Past markers: yesterday, last week, ago, in 2020.",
"formula": "past time: yesterday / last + time / time + ago",
"examples": [
("The lesson was easy yesterday.", "كان الدرس سهلا أمس."),
("We were on holiday last week.", "كنا في عطلة الأسبوع الماضي."),
("There was a festival two days ago.", "كان هناك احتفال منذ يومين.")]},
{
"en": "There was / There were",
"ar": "There was / There were في الماضي",
"expl_ar": "في الماضي: There was + مفرد، There were + جمع:\nThere was a man at the door (كان رجل عند الباب)، There were many people at the party (كان هناك كثير من الناس في الحفلة).",
"expl_en": "Past: There was (singular), There were (plural).",
"formula": "There was + singular | There were + plural",
"examples": [
("There was a big storm last night.", "كانت هناك عاصفة كبيرة الليلة الماضية."),
("There were no cars in the village then.", "لم تكن هناك سيارة في القرية آنذاك."),
("There was a beautiful garden behind our old house.", "كانت هناك حديقة جميلة خلف بيتنا القديم.")]},
{
"en": "Negative: was not / were not",
"ar": "النفي: لم يكن",
"expl_ar": "النفي بإضافة not: was not / wasn't، were not / weren't:\nI wasn't tired (لم أكن متعباً)، They weren't angry (لم يكونوا غاضبين).",
"expl_en": "Negatives: wasn't (was not), weren't (were not).",
"formula": "I/he/she/it + wasn't | you/we/they + weren't",
"examples": [
("I wasn't at home when you called.", "لم أكن في البيت عندما اتصلت."),
("It wasn't cold yesterday.", "لم يكن الجو باردا أمس."),
("We weren't late for the lesson.", "لم نتأخر عن الحصة.")]},
{
"en": "Questions: Was he...? Were they...?",
"ar": "السؤال: هل كان؟",
"expl_ar": "نقلب الفعل للسؤال: Was he at school? (هل كان في المدرسة؟)، Were you tired? (هل كنت متعباً؟).",
"expl_en": "Questions: Was + subject? Were + subject?",
"formula": "Was/Were + subject + rest?",
"examples": [
("Was the film good?", "هل كان الفيلم جيدا؟"),
("Were you at the party?", "هل كنت في الحفلة؟"),
("Where was she yesterday?", "أين كانت أمس؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I was. / No, he wasn't. / Yes, they were. / No, we weren't.",
"expl_en": "Short answers: Yes, I was. No, they weren't.",
"formula": "Yes/No + pronoun + was/were (or wasn't/weren't)",
"examples": [
("Were you tired? Yes, I was.", "هل كنت متعبا؟ نعم."),
("Was she at home? No, she wasn't.", "هل كانت في البيت؟ لا."),
("Were they happy? Yes, they were.", "هل كانوا سعداء؟ نعم.")]},
{
"en": "was/were with adjectives and places",
"ar": "was/were مع الصفات والأماكن",
"expl_ar": "نصف الماضي بالصفة أو المكان:\nThe soup was delicious (كان الحساء لذيذاً)، The trip was long (كانت الرحلة طويلة)، He was at the market (كان في السوق).",
"expl_en": "Use was/were with adjectives and places: The soup was delicious.",
"formula": "subject + was/were + adjective/place",
"examples": [
("The hotel was very clean.", "كان الفندق نظيفا جدا."),
("My grandfather was a teacher.", "كان جدي معلما."),
("The seats were comfortable.", "كانت المقاعد مريحة.")]},
{
"en": "born: was born",
"ar": "ولد: was born",
"expl_ar": "نقول عن الميلاد: I was born in 2012 (ولدت في عام 2012).\nنستعمل was born مع المفرد و were born مع الجمع.",
"expl_en": "About birth: was born / were born + in + year.",
"formula": "subject + was/were born + in + year/place",
"examples": [
("I was born in 2012.", "ولدت في عام 2012."),
("She was born in Algeria.", "ولدت في الجزائر."),
("They were born in the summer.", "وُلدوا في فصل الصيف.")]},
{
"en": "was/were + -ing = past continuous (preview)",
"ar": "لمحة عن الماضي المستمر",
"expl_ar": "was/were مع فعل-ing يبني الماضي المستمر (مستوى 51): I was working (كنت أعمل)، They were playing (كانوا يلعبون).\nسنتعمق فيه لاحقاً لكن تذكر التركيب الآن.",
"expl_en": "was/were + -ing builds the past continuous: I was working.",
"formula": "was/were + verb-ing (preview)",
"examples": [
("He was sleeping when I came.", "كان نائما عندما جئت."),
("We were talking about you.", "كنا نتحدث عنك."),
("It was raining all night.", "كانت تمطر طوال الليل.")]},
{
"en": "Talk about the past",
"ar": "تحدث عن الماضي",
"expl_ar": "اكتب فقرة عن أمسك: Yesterday I was... (أمس كنت...)، My friends were... (أصدقائي كانوا...)، There was... (كان هناك...)، wasn't... .\nاستعمل was/were لإتقان التعبير عن الماضي.",
"expl_en": "Write a paragraph about yesterday using was and were.",
"formula": "Yesterday, + past sentence with was/were.",
"examples": [
("Yesterday was a good day.", "كان أمس يوما جيدا."),
("Everything was quiet in the morning.", "كان كل شيء هادئا في الصباح."),
("We were very happy in the evening.", "كنا سعداء جدا في المساء.")]},
]
},
# ============================ NIVEAU 27 ============================
{
"num": 27, "cefr": "A1",
"category": "Past Simple: Regular Verbs",
"category_ar": "الماضي البسيط: الأفعال المنتظمة",
"title_en": "Past Simple: Regular Verbs (-ed)",
"title_ar": "الماضي البسيط: الأفعال المنتظمة",
"ideas": [
{
"en": "Regular past: + ed",
"ar": "الماضي المنتظم: إضافة ed",
"expl_ar": "معظم الأفعال يتحول إلى الماضي بإضافة ed: play→played (لعب)، work→worked (عمل)، open→opened (فتح).\nنفس الصيغة لجميع الفاعلين.",
"expl_en": "Most verbs form the past by adding -ed: play→played, work→worked.",
"formula": "base verb + ed",
"examples": [
("I played football yesterday.", "لعبت كرة القدم أمس."),
("She worked late last night.", "عملت حتى وقت متأخر الليلة الماضية."),
("They opened the shop at eight.", "فتحوا المتجر في الثامنة.")]},
{
"en": "Spelling: verbs ending in -e",
"ar": "التاء الإملاء: الأفعال المنتهية بـ e",
"expl_ar": "الفعل المنتهي بـ e نضيف d فقط: dance→danced (رقص)، love→loved (أحبّ)، like→liked (أحبّ)، smile→smiled (ابتسم).",
"expl_en": "Verbs ending in -e just add -d: dance→danced, like→liked.",
"formula": "verb ending in e + d",
"examples": [
("We danced all night.", "رقصنا طوال الليل."),
("I liked the story very much.", "أعجبني جدا (أحببت) هذه القصة."),
("She smiled at me.", "ابتسمت لي.")]},
{
"en": "Spelling: consonant + y → ied",
"ar": "ساكن + y → ied",
"expl_ar": "الفعل المنتهي بـ ساكن + y نحوّلها إلى ied: study→studied (درس)، try→tried (حاول)، cry→cried (بكى).\nأما مع العلة فنضيف ed: play→played (لعب)، stay→stayed (بقي).",
"expl_en": "Consonant + y → ied: studied, tried. Vowel + y → ed: played.",
"formula": "study→studied • try→tried | play→played • stay→stayed",
"examples": [
("He studied hard for the exam.", "درس بجد من أجل الامتحان."),
("I tried to help him.", "حاولت مساعدته."),
("We stayed at a hotel.", "مكثنا في فندق.")]},
{
"en": "Spelling: double the consonant",
"ar": "مضاعفة الحرف الساكن",
"expl_ar": "الفعل القصير (ساكن + علة + ساكن) نضاعف الحرف الأخير: stop→stopped (توقف)، rob→robbed (سرق)، plan→planned (خطط)، travel→travelled (بريطانيا).",
"expl_en": "Short verbs (CVC) double the final consonant: stop→stopped, plan→planned.",
"formula": "consonant+vowel+consonant → double + ed",
"examples": [
("The bus stopped at the station.", "توقفت الحافلة في المحطة."),
("We planned the trip together.", "خططنا للرحلة معا."),
("He dropped the glass.", "أوقع (أسقط) الكأس.")]},
{
"en": "Pronunciation of -ed: /t/, /d/, /ɪd/",
"ar": "نطق ed: t أو d أو id",
"expl_ar": "ed تنطق بثلاث طرق: /t/ بعد الأصوات الصماء (worked: عمل)، /d/ بعد الأصوات المجهورة (played: لعب).\n/ɪd/ بعد t و d (wanted: أراد، needed: احتاج).",
"expl_en": "How -ed sounds: /t/ (worked), /d/ (played), /ɪd/ (wanted, needed).",
"formula": "voiceless→/t/ • voiced→/d/ • t/d→/ɪd/",
"examples": [
("He worked /t/ in a factory.", "عمل في مصنع."),
("We played /d/ chess.", "لعبنا الشطرنج."),
("They visited /ɪd/ us.", "زارونا.")]},
{
"en": "Past simple: finished actions",
"ar": "أفعال منتهية في الماضي",
"expl_ar": "الماضي البسيط للأفعال المكتملة في زمن محدد ماضٍ:\nThe match ended at 6 (انتهت المباراة في السادسة)، I finished my homework (أنهيت واجبي).",
"expl_en": "Past simple for completed actions at a specific past time.",
"formula": "subject + verb-ed + past time",
"examples": [
("The lesson ended at noon.", "انتهت الحصة عند الظهر."),
("I cleaned my room this morning.", "نظفت غرفتي هذا الصباح."),
("She cooked a delicious meal.", "طبخت وجبة لذيذة.")]},
{
"en": "Time expressions of the past",
"ar": "تعبيرات زمن الماضي",
"expl_ar": "نستعمل: yesterday (أمس)، last night (الليلة الماضية)، last week (الأسبوع الماضي)، last year (السنة الماضية)، ago (منذ)، this morning (هذا الصباح إذا مضى).\nوكذلك: in 2020، when I was young (عندما كنت صغيراً).",
"expl_en": "Past time words: yesterday, last night, ago, in 2020.",
"formula": "past verb + yesterday/last/ago",
"examples": [
("We visited the zoo last week.", "زرنا حديقة الحيوانات الأسبوع الماضي."),
("I called you two hours ago.", "اتصلت بك منذ ساعتين."),
("They arrived in 2020.", "وصلوا عام 2020.")]},
{
"en": "Everyday regular verbs",
"ar": "أفعال منتظمة يومية",
"expl_ar": "احفظ هذه المجموعة الشائعة:\nwatch→watched (شاهد)، clean→cleaned (نظّف)، cook→cooked (طبخ)، help→helped (ساعد).\nlisten→listened (استمع)، wash→washed (غسل)، walk→walked (مشى)، wait→waited (انتظر).",
"expl_en": "Common regular verbs: watch, clean, cook, help, listen, wash, walk, wait.",
"formula": "subject + watched/cleaned/cooked... + rest",
"examples": [
("We watched a film last night.", "شاهدنا فيلما الليلة الماضية."),
("I helped my mother cook dinner.", "ساعدت أمي في طهي العشاء."),
("She walked to the station.", "مشت إلى المحطة.")]},
{
"en": "Careful: verbs ending in 'y' after vowel + ed",
"ar": "انتبه: فعل + علة + y يبقى y",
"expl_ar": "عندما يسبق y حرف علة (a, e, i, o, u) نضيف ed مباشرة دون تغيير: play→played (لعب)، enjoy→enjoyed (استمتع)، stay→stayed (بقي).\nبينما ساكن + y نحولها: carry→carried (حمل).",
"expl_en": "Vowel+y → +ed (played). Consonant+y → ies… in past: carry→carried.",
"formula": "play→played • stay→stayed | carry→carried • try→tried",
"examples": [
("We enjoyed the evening.", "استمتعنا بالمساء."),
("They stayed at the beach till sunset.", "بقوا على الشاطئ حتى الغروب."),
("She carried the bags alone.", "حملت الحقائب وحدها.")]},
{
"en": "Regular past verbs in a short story",
"ar": "الأفعال المنتظمة في قصة قصيرة",
"expl_ar": "ادمج الأفعال المنتظمة في سرد:\nYesterday I woke up, washed my face (غسلت وجهي), prayed (صليت), walked to school (مشيت إلى المدرسة), listened to the lesson (استمعت إلى الدرس), finished my homework (أنهيت واجبي) and watched TV (شاهدت التلفاز).\nكلها أفعال منتظمة.",
"expl_en": "Tell yesterday's story with regular verbs: washed, walked, listened, finished.",
"formula": "Yesterday I ...ed, ...ed, and ...ed.",
"examples": [
("I cleaned my room and helped Mum.", "نظفت غرفتي وساعدت أمي."),
("We watched and discussed the film.", "شاهدنا وناقشنا الفيلم."),
("She posted the letter and waited.", "أرسلت الرسالة وانتظرت.")]},
]
},
# ============================ NIVEAU 28 ============================
{
"num": 28, "cefr": "A1",
"category": "Past Simple: Irregular Verbs",
"category_ar": "الماضي البسيط: الأفعال الشاذة",
"title_en": "Past Simple: Irregular Verbs",
"title_ar": "الماضي البسيط: الأفعال الشاذة",
"ideas": [
{
"en": "What are irregular verbs?",
"ar": "ما هي الأفعال الشاذة؟",
"expl_ar": "على خلاف الأفعال المنتظمة، الشاذة لا تأخذ ed بل تتغير صورتها كلياً أو جزئياً: go→went (ذهب)، eat→ate (أكل)، see→saw (رأى).\nنتعلمها بالحفظ.",
"expl_en": "Irregular verbs do not take -ed. They change form: go→went, eat→ate, see→saw.",
"formula": "irregular: go→went • eat→ate • see→saw",
"examples": [
("I went to the market yesterday.", "ذهبت إلى السوق أمس."),
("We ate couscous on Friday.", "أكلنا الكسكس يوم الجمعة."),
("She saw her friend at the mall.", "رأت صديقها في المركز التجاري.")]},
{
"en": "The most common irregular verbs",
"ar": "أشهر الأفعال الشاذة",
"expl_ar": "قائمة تكرر الحفظ:\nbe→was/were (كان)، have→had (كان لديه)، do→did (فعل)، say→said (قال)، make→made (صنع)، get→got (حصل).\ncome→came (جاء)، know→knew (عرف)، go→went (ذهب)، take→took (أخذ).",
"expl_en": "Top irregulars: be, have, do, say, make, get, come, know, go, take.",
"formula": "have→had • make→made • get→got • come→came • know→knew • take→took",
"examples": [
("I had a good time.", "قضيت وقتا ممتعا."),
("He made a cake for us.", "صنع لنا كعكة."),
("We came late to class.", "جئنا متأخرين إلى القسم.")]},
{
"en": "go/went, see/saw, eat/ate, drink/drank",
"ar": "أربعة أسس: ذهب، رأى، أكل، شرب",
"expl_ar": "أربعة أفعال يومية جداً: go→went (ذهب)، see→saw (رأى)، eat→ate (أكل)، drink→drank (شرب).\nأمثلة: I went (ذهبت)، He saw (رأى)، We ate (أكلنا)، She drank (شربت).",
"expl_en": "Four daily verbs: go→went, see→saw, eat→ate, drink→drank.",
"formula": "go→went • see→saw • eat→ate • drink→drank",
"examples": [
("I drank a glass of milk.", "شربت كأس حليب."),
("We saw the new film.", "رأينا الفيلم الجديد."),
("She ate an apple after lunch.", "أكلت تفاحة بعد الغداء.")]},
{
"en": "write/wrote, read/read, speak/spoke",
"ar": "كتب، قرأ، تحدث",
"expl_ar": "أفعال الدراسة: write→wrote (كتب)، read→read (قرأ، نفس الكتابة)، speak→spoke (تحدث).\nلاحظ: read في الماضي ينطق /red/.",
"expl_en": "Study verbs: write→wrote, read→read (/red/), speak→spoke.",
"formula": "write→wrote • read→read (pronounced 'red') • speak→spoke",
"examples": [
("I wrote a long letter.", "كتبت رسالة طويلة."),
("He read the poem to the class.", "قرأ القصيدة على القسم."),
("We spoke about the future.", "تحدثنا عن المستقبل.")]},
{
"en": "give/gave, take/took, meet/met, leave/left",
"ar": "أعطى، أخذ، قابل، غادر",
"expl_ar": "مجموعة شائعة: give→gave (أعطى)، take→took (أخذ)، meet→met (قابل)، leave→left (غادر).\nأمثلة: She gave me a gift (أعطتني هدية)، We met in Oran (تقابلنا في وهران)، They left early (غادروا مبكراً).",
"expl_en": "Common set: give→gave, take→took, meet→met, leave→left.",
"formula": "give→gave • take→took • meet→met • leave→left",
"examples": [
("She gave me this pen.", "أعطتني هذا القلم."),
("I took the bus to the city.", "أخذت الحافلة إلى المدينة."),
("We met our cousins at the airport.", "قابلنا أبناء عمنا في المطار.")]},
{
"en": "sleep/slept, run/ran, swim/swam, sing/sang",
"ar": "نام، ركض، سبح، غنى",
"expl_ar": "أفعال النشاط: sleep→slept (نام)، run→ran (ركض)، swim→swam (سبح)، sing→sang (غنى).\nأمثلة: He slept well (نام جيداً)، They swam in the sea (سبحوا في البحر).",
"expl_en": "Activity verbs: sleep→slept, run→ran, swim→swam, sing→sang.",
"formula": "sleep→slept • run→ran • swim→swam • sing→sang",
"examples": [
("I slept deeply last night.", "نم بعمق الليلة الماضية."),
("He ran to catch the train.", "ركض ليلحق بالقطار."),
("We sang songs around the fire.", "غنينا أغاني حول النار.")]},
{
"en": "buy/bought, bring/brought, think/thought",
"ar": "اشترى، أحضر، فكر",
"expl_ar": "مجموعة فيها «augh/ought»: buy→bought (اشترى)، bring→brought (أحضر)، think→thought (فكر)، teach→taught (درّس)، catch→caught (أمسك).\nنطقها متشابه.",
"expl_en": "The 'ought' family: buy→bought, bring→brought, think→thought, teach→taught.",
"formula": "buy→bought • bring→brought • think→thought",
"examples": [
("I bought a new phone.", "اشتريت هاتفا جديدا."),
("She brought some dates for us.", "أحضرت لنا بعض التمر."),
("He thought about the question.", "فكر في السؤال.")]},
{
"en": "The past is the same for all subjects",
"ar": "الماضي واحد لكل الفاعلين",
"expl_ar": "ميزة رائعة: الماضي لا يتغير مع الفاعل: I went، You went، He went، We went، They went.\nلا نضيف s أبداً.",
"expl_en": "Past is the same for all subjects: I went, he went, they went.",
"formula": "all subjects + same past form",
"examples": [
("I went home early.", "ذهبت إلى البيت مبكرا."),
("She went to the mosque.", "ذهبت إلى المسجد."),
("They went camping last summer.", "ذهبوا للتخييم الصيف الماضي.")]},
{
"en": "Irregular pairs to memorize daily",
"ar": "أزواج شاذة احفظها يومياً",
"expl_ar": "قسّمها لمجموعات: (1) تغيير العلة: drink/drank (شرب)، sing/sang (غنى)؛ (2) تغيير كامل: go/went (ذهب)، be/was (كان)؛ (3) نهاية t: sleep/slept (نام)، keep/kept (حافظ).\nراجعها يومياً.",
"expl_en": "Group irregulars: vowel change, full change, ending in t.",
"formula": "groups: drink/drank • go/went • sleep/slept",
"examples": [
("keep → kept (I kept my promise)", "وفيت بوعدي."),
("sell → sold (He sold his car)", "باع سيارته."),
("send → sent (She sent me a letter)", "أرسلت لي رسالة.")]},
{ 
"en": "Rewrite the story in the past",
"ar": "أعد كتابة القصة في الماضي",
"expl_ar": "حول جمل الحاضر إلى الماضي:\nI wake up → I woke up (أستيقظ → استيقظت)، I eat → I ate (آكل → أكلت)، I see → I saw (أرى → رأيت)، I go → I went (أذهب → ذهبت).\nهذه أفضل طريقة لتثبيت الأشكال الشاذة.",
"expl_en": "Change present sentences to past using irregular verbs: wake→woke, eat→ate.",
"formula": "present verb → past irregular form",
"examples": [
("I wake up at six. → I woke up at six.", "استيقظت في السادسة."),
("We have lunch. → We had lunch.", "تناولنا الغداء."),
("She goes to school. → She went to school.", "ذهبت إلى المدرسة.")]},
]
},
# ============================ NIVEAU 29 ============================
{
"num": 29, "cefr": "A1",
"category": "Past Simple: Negatives and Questions",
"category_ar": "نفي وسؤال الماضي البسيط",
"title_en": "Past Simple: Negatives and Questions (did)",
"title_ar": "نفي الماضي البسيط وسؤاله (did)",
"ideas": [
{
"en": "Auxiliary 'did' for the past",
"ar": "المساعد did للماضي",
"expl_ar": "للسؤال والنفي في الماضي نستعمل did (فعل مساعد بمعنى الماضي من do).\nيحمل علامة الماضي فالفعل الرئيسي يبقى في أصله: I didn't go وليس didn't went.",
"expl_en": "Use 'did' for past questions and negatives. The main verb stays base: I didn't go.",
"formula": "did + subject + base verb? | didn't + base verb",
"examples": [
("Did you watch the match?", "هل شاهدت المباراة؟"),
("I didn't see him yesterday.", "لم أره أمس."),
("She didn't come to the lesson.", "لم تأت إلى الحصة.")]},
{
"en": "Negative: didn't + base verb",
"ar": "النفي: didn't + فعل أصلي",
"expl_ar": "النفي بـ didn't (لم) ثم الفعل في أصله: I didn't play (لم ألعب)، He didn't eat (لم يأكل)، We didn't sleep (لم ننم).\nلا نستعمل الشكل الماضي مع didn't.",
"expl_en": "Negative: didn't + base verb. NOT 'didn't went'.",
"formula": "subject + didn't + base verb",
"examples": [
("I didn't play football yesterday.", "لم ألعب كرة القدم أمس."),
("He didn't eat breakfast today.", "لم يتناول الفطور اليوم."),
("They didn't sleep well last night.", "لم يناموا جيدا الليلة الماضية.")]},
{
"en": "didn't = did not",
"ar": "didn't = did not",
"expl_ar": "في الكتابة الرسمية: did not، والاختصار: didn't.\nالمعنى واحد: I did not understand = I didn't understand (لم أفهم).",
"expl_en": "didn't = did not. Same meaning.",
"formula": "didn't = did not",
"examples": [
("I did not understand the question.", "لم أفهم السؤال."),
("We did not watch TV last night.", "لم نشاهد التلفاز الليلة الماضية."),
("She did not like the film.", "لم يعجبها الفيلم.")]},
{
"en": "Questions: Did you...?",
"ar": "السؤال: هل فعلت...؟",
"expl_ar": "نبدأ بـ Did ثم الفاعل ثم الفعل الأصلي:\nDid you play? (هل لعبت؟)، Did he go? (هل ذهب؟)، Did they see? (هل رأوا؟).\nليس Did she went.",
"expl_en": "Question: Did + subject + base verb? Did you go?",
"formula": "Did + subject + base verb + rest?",
"examples": [
("Did you eat breakfast?", "هل تناولت الفطور؟"),
("Did he finish his homework?", "هل أنجز واجبه؟"),
("Did they visit Medina?", "هل زاروا المدينة؟")]},
{
"en": "Short answers: Yes, I did / No, I didn't",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I did. / No, I didn't.\nولا نكرر الفعل: Did you play? Yes, I did (هل لعبت؟ نعم).",
"expl_en": "Short answers: Yes, I did. No, I didn't.",
"formula": "Yes, + pronoun + did | No, + pronoun + didn't",
"examples": [
("Did you watch the film? Yes, I did.", "هل شاهدت الفيلم؟ نعم."),
("Did she call you? No, she didn't.", "هل اتصلت بك؟ لا."),
("Did they enjoy the trip? Yes, they did.", "هل استمتعوا بالرحلة؟ نعم.")]},
{
"en": "did or the past form?",
"ar": "did أم صيغة الماضي؟",
"expl_ar": "في الجملة المثبتة نستعمل صيغة الماضي: I went (ذهبت).\nفي النفي والسؤال نستعمل did + أصلي: I didn't go (لم أذهب)، Did you go? (هل ذهبت؟).\nعلامة الماضي تظهر مرة واحدة فقط.",
"expl_en": "Positive: past form (I went). Negative/Question: did + base (Did you go?). Only one past marker.",
"formula": "affirmative: went | negative/question: did + go",
"examples": [
("She came. → She didn't come.", "جاءت. ← لم تأت."),
("We saw it. → Did you see it?", "رأيناه. ← هل رأيته؟"),
("He wrote it. → He didn't write it.", "كتبه. ← لم يكتبه.")]},
{
"en": "Wh- questions in the past",
"ar": "أسئلة بأدوات الاستفهام في الماضي",
"expl_ar": "قبل Did نضع أداة الاستفهام:\nWhere did you go? (أين ذهبت؟)، When did she arrive? (متى وصلت؟)، Why did he leave? (لماذا غادر؟)، What did you eat? (ماذا أكلت؟).",
"expl_en": "Wh- + did + subject + verb: Where did you go?",
"formula": "Wh + did + subject + base verb?",
"examples": [
("Where did you go last weekend?", "إلى أين ذهبت عطلة الأسبوع الماضي؟"),
("What did you eat for dinner?", "ماذا أكلت على العشاء؟"),
("Why did he leave early?", "لماذا غادر مبكرا؟")]},
{
"en": "Past questions about ages, time",
"ar": "أسئلة الماضي عن الأعمار والأوقات",
"expl_ar": "أسئلة شائعة: What time did you wake up? (متى استيقظت؟)،\nHow old were you in 2010? (كم كان عمرك عام 2010؟ — يبقى مع be في الماضي كان).",
"expl_en": "Ask about the past: What time did you wake up? (be past: How old were you?).",
"formula": "What time/How old + did/be-past + subject?",
"examples": [
("What time did the bus leave?", "متى غادرت الحافلة؟"),
("How was the weather yesterday?", "كيف كان الجو أمس؟"),
("Where were you at noon?", "أين كنت ظهرا؟")]},
{
"en": "Common mistakes to avoid",
"ar": "أخطاء شائعة تجنبها",
"expl_ar": "خمسة أخطاء: (1) I didn't went ✗ → didn't go. (2) Did you went? ✗ → Did you go?\n(3) I no go ✗ → I didn't go. (4) She don't go ✗ → didn't. (5) قصر الماضي في النفي.",
"expl_en": "Avoid: didn't + past, Did + past, 'no' + verb. Always did + base.",
"formula": "DIDN'T + go (base)",
"examples": [
("I didn't go to bed early. ✓", "لم أنم مبكرا. صحيح."),
("Did you see the show? ✓", "هل رأيت العرض؟ صحيح."),
("We didn't know the answer. ✓", "لم نعرف الجواب. صحيح.")]},
{ 
"en": "Ask your classmate about yesterday",
"ar": "اسأل زميلك عن أمس",
"expl_ar": "تدريب: Did you wake up early? (هل استيقظت مبكراً؟)، Did you eat at school? (هل أكلت في المدرسة؟)، Did you watch TV? (هل شاهدت التلفاز؟)، Did you help at home? (هل ساعدت في البيت؟)\nثم أجب بنفسك بالشكلين.",
"expl_en": "Practise questions and answers about yesterday with did.",
"formula": "Did you + verb? → Yes, I did / No, I didn't",
"examples": [
("Did you study last night?", "هل ذاكرت الليلة الماضية؟"),
("Yes, I did, but I didn't finish.", "نعم، لكنني لم أنتهِ."),
("Did your brother help you? No, he didn't.", "هل ساعدك أخوك؟ لا.")]},
]
},
# ============================ NIVEAU 30 ============================
{
"num": 30, "cefr": "A1",
"category": "Future: Going To",
"category_ar": "المستقبل: going to",
"title_en": "Future with 'be going to'",
"title_ar": "المستقبل القريب: going to",
"ideas": [
{
"en": "Be going to + base verb",
"ar": "be going to + فعل أصلي",
"expl_ar": "نعبّر عن المستقبل بـ be going to + فعل: I am going to study (سأدرس)، She is going to travel (ستسافر).\nنقصد قراراً أو خطة مسبقة.",
"expl_en": "Future plans/decisions: be going to + base verb.",
"formula": "subject + am/is/are + going to + base verb",
"examples": [
("I am going to visit my grandparents.", "سأزور أجدادي."),
("She is going to buy a new dress.", "ستشتري فستانا جديدا."),
("We are going to watch a match tonight.", "سنشاهد مباراة الليلة.")]},
{
"en": "Plans already made",
"ar": "خطط مقررة مسبقاً",
"expl_ar": "going to يستعمل للخطط التي اتخذناها قبل الكلام: I'm going to study medicine (قررت ذلك منذ مدة).\nليست قراراً لحظياً.",
"expl_en": "Use 'going to' for plans made before speaking: decisions already taken.",
"formula": "I have decided → I'm going to + verb",
"examples": [
("He is going to be a doctor.", "سيصبح طبيبا."),
("We are going to move to a new house.", "سننتقل إلى بيت جديد."),
("They are going to start a business.", "سيؤسسون شركة.")]},
{
"en": "Predictions with evidence",
"ar": "توقعات مع دليل",
"expl_ar": "نستعمل going to للتوقع الذي نرى دليله الآن:\nLook at the clouds! It is going to rain (انظر للسحب! ستمطر).\nالسحب دليل.",
"expl_en": "Going to for predictions we can see: Look at the clouds! It's going to rain.",
"formula": "evidence → be going to + verb",
"examples": [
("Look! He is going to fall.", "انظر! على وشك السقوط."),
("The sky is dark. It's going to storm.", "السماء معتمة. ستهب عاصفة."),
("She is going to win; she is so fast.", "ستفوز؛ إنها سريعة جدا.")]},
{
"en": "Negative: am not / isn't / aren't going to",
"ar": "النفي: لن",
"expl_ar": "النفي بإضافة not بعد be:\nI'm not going to come (لن آتي)، It isn't going to snow (لن تثلج)، They aren't going to play (لن يلعبوا).",
"expl_en": "Negative: be + not + going to + verb.",
"formula": "subject + be + not + going to + base verb",
"examples": [
("I am not going to watch that film.", "لن أشاهد ذلك الفيلم."),
("He isn't going to accept the offer.", "لن يقبل العرض."),
("We aren't going to give up.", "لن نستسلم.")]},
{
"en": "Questions: Are you going to...?",
"ar": "السؤال: هل ستفعل؟",
"expl_ar": "نبدأ بفعل الكينونة:\nAre you going to come? (هل ستأتي؟)، Is she going to travel? (هل ستسافر؟)، What are you going to do? (ماذا ستفعل؟).",
"expl_en": "Question: be + subject + going to + verb?",
"formula": "Am/Is/Are + subject + going to + base verb?",
"examples": [
("Are you going to attend the meeting?", "هل ستحضر الاجتماع؟"),
("Is he going to come with us?", "هل سيأتي معنا؟"),
("What are you going to do this summer?", "ماذا ستفعل هذا الصيف؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I am. / No, I'm not. / Yes, she is. / No, they aren't.\nنكرر فعل الكينونة وليس going to.",
"expl_en": "Short answers: Yes, I am. No, I'm not. Yes, she is. No, they aren't.",
"formula": "Yes/No + pronoun + be (or be+n't)",
"examples": [
("Are you going to help? Yes, I am.", "هل ستساعد؟ نعم."),
("Is he going to join? No, he isn't.", "هل سينضم؟ لا."),
("Are they going to wait? Yes, they are.", "هل سينتظرون؟ نعم.")]},
{
"en": "Going to vs will (preview)",
"ar": "لمحة: going to مقابل will",
"expl_ar": "going to للخطط المقررة والتوقع بدليل، بينما will للقرارات اللحظية والوعود والتنبؤ العام.\nقارن: I'm going to travel (خطة: سأسافر) مقابل Okay, I'll help you (قرار لحظي: حسناً، سأساعدك).",
"expl_en": "Going to: plans/evidence. Will: sudden decisions, promises, general predictions.",
"formula": "plan → going to | sudden decision → will",
"examples": [
("I'm going to travel next month.", "سأسافر الشهر القادم (خطة)."),
("Don't worry, I'll help you.", "لا تقلق، سأساعدك (قرار لحظي)."),
("It's going to be a lovely day.", "سيكون يوما جميلا (توقع).")]},
{
"en": "Going to with time expressions",
"ar": "going to مع تعبيرات الزمن",
"expl_ar": "نستعمل معها:\ntomorrow (غداً)، next week (الأسبوع القادم)، next summer (الصيف القادم)، tonight (الليلة)، in the future (في المستقبل).\nمثال: I'm going to start a course next week (سأبدأ دورة الأسبوع القادم).",
"expl_en": "With future times: tomorrow, next week, tonight, next summer.",
"formula": "be going to + verb + future time",
"examples": [
("We are going to visit the museum tomorrow.", "سنزور المتحف غدا."),
("I'm going to learn cooking next month.", "سأتعلم الطبخ الشهر القادم."),
("They are going to plant trees this year.", "سيغرسون الأشجار هذه السنة.")]},
{ 
"en": "Talk about intentions",
"ar": "تحدث عن نواياك",
"expl_ar": "اكتب ثلاث خطط: I'm going to... (سوف...) وثلاث توقعات بدليل: Look! (انظر!) ... is going to... وثلاث نفي: I'm not going to...\nهذا يغطي كل أشكال القاعدة.",
"expl_en": "Make plans, predictions and negatives with going to.",
"formula": "plan: I'm going to... | evidence: ... is going to... | negative: I'm not going to...",
"examples": [
("I'm going to memorize a new surah.", "سأحفظ سورة جديدة."),
("Look at the sun! It's going to be hot.", "انظر للشمس! سيكون الجو حارا."),
("I'm not going to waste my time.", "لن أضيع وقتي.")]},
{
"en": "Going to vs present continuous (arrangements)",
"ar": "going to مقابل المضارع المستمر للتخطيط",
"expl_ar": "كلاهما للمستقبل المقرر: العزم والنية: I'm going to study (قررت بنية)، ولقاءات مرتبة: I'm meeting the doctor at 5 (ترتيب بموعد) أو I'm going to meet him at 5 (سأقابله في الخامسة).\nالفرق دقيق: المستمر يحسس بالترتيب الرسمي.",
"expl_en": "Going to = intention. Present continuous = fixed arrangements.",
"formula": "going to + verb (intention) | be + verb-ing (arrangement)",
"examples": [
("I'm going to call him later.", "سأتصل به لاحقا (نية)."),
("I'm seeing the dentist at four.", "أرى طبيب الأسنان في الرابعة (موعد)."),
("We're going to start a course soon.", "سنبدأ دورة قريبا.")]},
]
},
]