# -*- coding: utf-8 -*-
"""المستويات 31–40 : ابتدائي (A2) — المستقبل، المقارنات، الكمية.""" 

LEVELS = [

# ============================ NIVEAU 31 ============================
{
"num": 31, "cefr": "A1",
"category": "Future: Will",
"category_ar": "المستقبل: will",
"title_en": "Future with 'will'",
"title_ar": "المستقبل البسيط: will",
"ideas": [
{
"en": "Will + base verb",
"ar": "will + فعل أصلي",
"expl_ar": "نعبّر عن المستقبل بـ will + الفعل في أصله: I will travel (سأسافر)، He will come (سيأتي).\nلا نغير الفعل مهما كان الفاعل.",
"expl_en": "Future with will + base verb: I will travel.",
"formula": "subject + will + base verb",
"examples": [
("I will call you tomorrow.", "سأتصل بك غدا."),
("She will be very happy.", "ستكون سعيدة جدا."),
("We will see each other soon.", "سنجتمع قريبا.")]},
{
"en": "Contractions: I'll, you'll, he'll...",
"ar": "الاختصارات: I'll, you'll...",
"expl_ar": "فِي الكلام نختصر will مع الفاعل: I will ← I'll، you will ← you'll، he will ← he'll، she'll، it'll، we'll، they'll.",
"expl_en": "Contractions: I'll, you'll, we'll, they'll.",
"formula": "will = 'll (I'll, she'll)",
"examples": [
("I'll help you with that.", "سأساعدك في ذلك."),
("She'll arrive at eight.", "ستصل في الثامنة."),
("We'll wait for you.", "سننتظرك.")]},
{
"en": "Sudden decisions (at the moment of speaking)",
"ar": "قرارات لحظية",
"expl_ar": "will للقرارات التي نتخذها في لحظة الكلام: الهاتف يرن: I'll answer it (سأجيب)، أو الباب: I'll open the door (سأفتح الباب).\nلم تكن في الخطة.",
"expl_en": "Will for decisions made now: 'I'll answer the phone.'",
"formula": "sudden: I'll + verb",
"examples": [
("The phone is ringing. I'll answer it.", "الهاتف يرن. سأجيب عليه."),
("I'll have the chicken, please.", "سآخذ الدجاج من فضلك."),
("Okay, I'll buy it!", "حسنا، سأشتريه!")]},
{
"en": "Predictions",
"ar": "التنبؤات",
"expl_ar": "will للتنبؤ العام بالمستقبل: I think it will rain (أظن أنها ستمطر)، Prices will go up (ستسعر الأسعار).\nنستخدم في التنبؤ دون دليل لحظي.",
"expl_en": "Will for general predictions: I think it will rain.",
"formula": "I think/Maybe + will + verb",
"examples": [
("I think Algeria will win the match.", "أظن أن الجزائر ستفوز في المباراة."),
("Maybe he will come later.", "ربما سيأتي لاحقا."),
("It will be cold this winter.", "سيكون الجو باردا هذا الشتاء.")]},
{
"en": "Promises and offers",
"ar": "الوعود والعروض",
"expl_ar": "will للوعود (I promise I won't tell) وللعروض: I'll carry your bag (سأحمل حقيبتك).\nالمواد والخدمات: Will you help me? نعم.",
"expl_en": "Will for promises and offers: I'll help you. I won't tell anyone.",
"formula": "promise: I won't + verb | offer: I'll + verb",
"examples": [
("I promise I'll be careful.", "أعدك أني سأكون حذرا."),
("I won't tell anyone your secret.", "لن أخبر أحدا بسرك."),
("I'll carry those bags for you.", "سأحمل تلك الحقائب لك.")]},
{
"en": "Negative: won't",
"ar": "النفي: won't (لن)",
"expl_ar": "النفي بـ will not والاختصار won't: I won't come (لن آتي)، He won't listen (لن يستمع).\nانتبه للاختصار الغريب: will not ← won't.",
"expl_en": "Negative: won't (will not). I won't come.",
"formula": "subject + won't + base verb",
"examples": [
("I won't forget your kindness.", "لن أنسى لطفك."),
("He won't accept the offer.", "لن يقبل العرض."),
("They won't believe us.", "لن يصدقونا.")]},
{
"en": "Questions: Will you...?",
"ar": "السؤال: هل ست...؟",
"expl_ar": "نبدأ السؤال بـ Will ثم الفاعل: Will you come? (هل ستأتي؟)، What will you do? (ماذا ستفعل؟).\nWill يستعمل أيضاً للطلبات المهذبة.",
"expl_en": "Question: Will + subject + verb? Will you come?",
"formula": "Will + subject + base verb?",
"examples": [
("Will you come to my party?", "هل ستأتي إلى حفلتي؟"),
("Will she agree with us?", "هل ستوافقنا؟"),
("Where will we meet?", "أين سنلتقي؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I will. / No, I won't. مثال: Will you help? Yes, I will.",
"expl_en": "Short answers: Yes, I will. No, I won't.",
"formula": "Yes/No + pronoun + will / won't",
"examples": [
("Will you join us? Yes, I will.", "هل ستنضم إلينا؟ نعم."),
("Will he call? No, he won't.", "هل سيتصل؟ لا."),
("Will they come early? Yes, they will.", "هل سيأتون مبكرا؟ نعم.")]},
{
"en": "Time words with will",
"ar": "كلمات الزمن مع will",
"expl_ar": "نستعمل مع will: tomorrow، next week، next year، soon، later، in the future، tonight.\nمثال: I will travel next summer (سأسافر الصيف القادم).",
"expl_en": "Future words: tomorrow, next week, soon, later.",
"formula": "will + verb + tomorrow/next/soon",
"examples": [
("We will start a new project next month.", "سنبدأ مشروعا جديدا الشهر القادم."),
("She will finish the work soon.", "ستنهي العمل قريبا."),
("They will visit us again in the future.", "سيزوروننا مستقبلا.")]},
{
"en": "Will in polite requests",
"ar": "will في الطلبات المهذبة",
"expl_ar": "للطلب المؤدب نقول: Will you open the window, please? (هل من فضلك تفتح النافذة؟)، أو Won't you sit down? أقرب إلى الدعوة.",
"expl_en": "Polite requests: Will you open the window, please?",
"formula": "Will you + verb, please?",
"examples": [
("Will you pass the salt, please?", "هل تمرر الملح من فضلك؟"),
("Will you wait a moment?", "هل تنتظر لحظة؟"),
("Will you show me the way?", "هل تريني الطريق؟")]},
]
},
# ============================ NIVEAU 32 ============================
{
"num": 32, "cefr": "A2",
"category": "Will vs Going To",
"category_ar": "will مقابل going to",
"title_en": "Will vs Going to",
"title_ar": "الفرق بين will و going to",
"ideas": [
{
"en": "Going to = plan, Will = decision now",
"ar": "going to = خطة، will = قرار لحظي",
"expl_ar": "going to للخطط المقررة قبل الكلام: I'm going to study medicine (سأدرس الطب، قررت منذ زمن).\nwill للقرارات في لحظة الكلام: It's hot (الجو حار). I'll open a window (سأفتح نافذة).",
"expl_en": "Going to: a plan made before. Will: a decision made now.",
"formula": "plan → going to | now → will",
"examples": [
("I'm going to travel next Friday.", "سأسافر يوم الجمعة القادم (خطة)."),
("This seat is free. I'll take it.", "هذا المقعد فارغ. سآخذه (قرار الآن)."),
("She's going to buy a car this year.", "ستشتري سيارة هذه السنة (خطة).")]},
{
"en": "Going to = evidence, Will = opinion",
"ar": "going to = دليل، will = رأي",
"expl_ar": "التوقع بدليل نراه نستعمل فيه going to: Look! (انظر!) It's going to rain (ستمطر).\nالتنبؤ بالرأي العام نستعمل will: I think it will rain (أظن أنها ستمطر).",
"expl_en": "Evidence → going to. General opinion → will.",
"formula": "evidence: Look! ... is going to... | opinion: I think ... will...",
"examples": [
("Look at those clouds! It's going to rain.", "انظر لتلك السحب! ستمطر (دليل)."),
("I think it will be sunny tomorrow.", "أظن أن الجو سيكون مشمسا غدا."),
("The car has no fuel. We're going to walk.", "السيارة بلا وقود. سنمشي (دليل).")]},
{
"en": "Going to with arrangements, will with willingness",
"ar": "going to مع الترتيبات، will مع الرغبة",
"expl_ar": "going to لخطة مركبة بترتيبات، will لعرض المساعدة أو الموافقة اللحظية.\nI'm going to meet them at 6 (سألتقي بهم السادسة) مقابل I will wait for you here (سأنتظرك هنا).",
"expl_en": "going to = plan. will = offer/willingness.",
"formula": "going to + plan | will + offer",
"examples": [
("We're going to have dinner at their house.", "سنتناول العشاء عندهم (ترتيب)."),
("I'll help you with your homework.", "سأساعدك في واجبك (عرض)."),
("He's going to apply for the job.", "سيقدم طلبا للوظيفة.")]},
{
"en": "Question forms comparison",
"ar": "مقارنة صيغ السؤال",
"expl_ar": "الأسئلة مختلفة: Are you going to travel? (هل خططت أن تسافر؟)، Will you travel? (هل تسافر؟ قرار/سؤال عام).\nالفرق يظهر في المعنى.",
"expl_en": "Questions: 'Are you going to travel?' (plan) vs 'Will you travel?' (offer/predict).",
"formula": "Are you going to + verb? | Will you + verb?",
"examples": [
("Are you going to attend the wedding?", "هل ستشهد حفل الزواج (مقبلا)؟"),
("Will you attend the meeting?", "هل ستحضر الاجتماع (سؤال)؟"),
("What are you going to wear tonight?", "ماذا سترتدي الليلة؟")]},
{
"en": "Both wrong uses",
"ar": "استعمالات خاطئة",
"expl_ar": "لا نقول: I'm going to will go ✗. ولا نستخدم going to مع to: I'm going to to travel ✗.\nبيكون الأمر: going to + فعل أصلي، و will + فعل أصلي.",
"expl_en": "Never: 'going to will'. Never 'going to to'. One marker only.",
"formula": "going to + verb | will + verb",
"examples": [
("I'm going to stay home. ✓", "سأبقى في البيت. صحيح."),
("I'll stay home. ✓", "سأبقى في البيت. صحيح."),
("I'm going to will stay. ✗", "جملة خاطئة.")]},
{
"en": "Choosing between the two",
"ar": "اختيار بين الاثنين",
"expl_ar": "اسأل نفسك: هل كانت الخطة موجودة قبل؟ نعم ← going to. هل قررتُ الآن لأول مرة؟ نعم ← will.\nمثال: (مخطط) I'm going to start diet (سأبدأ نظاما غذائيا). (لحظي) Okay, I'll try it (حسنا، سأجربه).",
"expl_en": "Was it planned before? → going to. Decided now? → will.",
"formula": "already decided → going to | deciding now → will",
"examples": [
("I'm going to revise for the exam tonight.", "سأراجع من أجل الامتحان الليلة (خطة)."),
("I'll help you right now.", "سأساعدك الآن (عرض)."),
("She's going to open a bakery.", "ستفتح مخبزة.")]},
{
"en": "Forms of 'be' with going to",
"ar": "تصاريف be مع going to",
"expl_ar": "going to يُسبق دائماً بـ am/is/are حسب الفاعل: I am going to، She is going to، They are going to.\nلا تقل أبداً: I going to ✗.",
"expl_en": "Always use be before going to: I am / she is / they are going to.",
"formula": "am / is / are + going to + verb",
"examples": [
("I am going to visit my grandparents.", "سأزور أجدادي."),
("She is going to study abroad.", "ستدرس في الخارج."),
("We are going to buy a new fridge.", "سنشتري برادا جديدا.")]},
{
"en": "Negative: isn't / won't",
"ar": "النفي: Isn't going to و won't",
"expl_ar": "نفي going to يكون بنفي الفعل be: I'm not going to come (لن آتي). نفي will: I won't come (لن آتي).\nالأولى تنكر وجود خطة، والثانية رفض أو امتناع عن الفعل.",
"expl_en": "'Not going to' denies a plan; 'won't' = refusal or strong intention.",
"formula": "am/is/are not going to | won't + verb",
"examples": [
("I'm not going to stay long.", "لن أطيل البقاء (ليس في الخطة)."),
("She isn't going to attend the party.", "لن تحضر الحفلة (لا خطة)."),
("He won't listen to advice.", "لن يستمع للنصيحة (رفض).")]},
{
"en": "Time words with both forms",
"ar": "كلمات الزمن مع الاثنين معا",
"expl_ar": "كلمات مثل tomorrow، next week، tonight، this summer، soon، later تصح مع going to ومع will معاً.\nالاختيار يعتمد على المعنى لا على الكلمة.",
"expl_en": "Tomorrow, next week, soon, later work with both; the choice depends on meaning.",
"formula": "going to / will + verb + tomorrow / next / soon",
"examples": [
("We are going to meet tonight.", "سنجتمع الليلة (خطة)."),
("She will call you later.", "ستتصل بك لاحقا (وعد)."),
("I'm going to fix the car this weekend.", "سأصلح السيارة هذا الأسبوع (خطة).")]},
{
"en": "Will: statements, Going to: plans",
"ar": "will للأقوال الرسمية و going to للخطط الشخصية",
"expl_ar": "في الإعلانات والتصريحات الرسمية نستعمل will: The new school will open in September (المدرسة الجديدة ستفتح في سبتمبر).\nفي الخطط الشخصية نستعمل going to: I'm going to move next year (سأنتقل في العام القادم).",
"expl_en": "Official statements use will; personal intentions use going to.",
"formula": "statement → will | intention → going to",
"examples": [
("The new metro line will open in May.", "من المقرر افتتاح خط المترو الجديد في ماي."),
("I'm going to move to a new flat.", "سأنتقل إلى شقة جديدة (خطة)."),
("The president will give a speech tonight.", "سيُدلي الرئيس بخطاب الليلة.")]},
]
},
# ============================ NIVEAU 33 ============================
{
"num": 33, "cefr": "A2",
"category": "Comparatives",
"category_ar": "صيغة المقارنة",
"title_en": "Comparatives: -er / more",
"title_ar": "صيغة المقارنة: أطول، أفضل، أكثر",
"ideas": [
{
"en": "Short adjectives + er",
"ar": "الصفات القصيرة + er",
"expl_ar": "الصفات القصيرة (مقطع واحد) تقارن بإضافة er: old → older (أكبر سنا)، tall → taller (أطول)، cold → colder (أبرد).\nونستخدم than (من).",
"expl_en": "Short adjectives add -er and use 'than': taller than.",
"formula": "adjective + er + than",
"examples": [
("My brother is taller than me.", "أخي أطول مني."),
("Today is colder than yesterday.", "اليوم أبرد من أمس."),
("This story is shorter than that one.", "هذه القصة أقصر من تلك.")]},
{
"en": "Long adjectives + more",
"ar": "الصفات الطويلة + more",
"expl_ar": "الصفات الطويلة (مقطعين فأكثر) نستعمل معها more: beautiful → more beautiful (أجمل)، interesting → more interesting (أكثر إثارة).",
"expl_en": "Long adjectives use 'more': more beautiful, more interesting.",
"formula": "more + long adjective + than",
"examples": [
("English is more interesting than French for me.", "الإنجليزية أكثر إثارة من الفرنسية بالنسبة لي."),
("This film is more boring than the book.", "هذا الفيلم أكثر مملة من الكتاب."),
("Her answer is more correct than mine.", "إجابتها أصح من إجابتي.")]},
{
"en": "Spelling: -y → -ier, -e → -er",
"ar": "إملاء المقارنة: y و e",
"expl_ar": "الصفة المنتهية بـ y نحولها إلى ier: happy → happier • easy → easier.\nالمنتهية بـ e نضيف r: nice → nicer • safe → safer.",
"expl_en": "happy→happier, easy→easier; nice→nicer, safe→safer.",
"formula": "happy→happier • easy→easier | nice→nicer • safe→safer",
"examples": [
("She is happier now than before.", "إنها أسعد الآن مما مضى."),
("This exercise is easier than that one.", "هذا التمرين أسهل من ذلك."),
("The sea is safer today than yesterday.", "البحر أأمن اليوم من أمس.")]},
{
"en": "Double the consonant: big → bigger",
"ar": "مضاعفة الساكن: big → bigger",
"expl_ar": "الصفات القصيرة بنمط ساكن + علة + ساكن نضاعف الحرف الأخير: big → bigger، hot → hotter، thin → thinner، wet → wetter.",
"expl_en": "CVC short adjectives double the last letter: big→bigger, hot→hotter.",
"formula": "big→bigger • hot→hotter • thin→thinner",
"examples": [
("My house is bigger than yours.", "بيتي أكبر من بيتك."),
("Oran is hotter than Algiers in summer.", "وهران أحر من الجزائر صيفا."),
("He is thinner than his brother.", "أوهف من أخيه.")]},
{
"en": "Irregular comparatives: good, bad, far",
"ar": "مقارنات شاذة: جيد، سيئ، بعيد",
"expl_ar": "ثلاث صفات شاذة: good → better (أفضل)، bad → worse (أسوأ)، far → farther/further (أبعد).\nلا نقول gooder ولا more good.",
"expl_en": "Irregular: good→better, bad→worse, far→farther.",
"formula": "good→better • bad→worse • far→farther/further",
"examples": [
("Your marks are better than mine.", "علاماتك أفضل من علاماتي."),
("The traffic is worse this morning.", "حركة المرور أسوأ هذا الصباح."),
("The mosque is farther than the shop.", "المسجد أبعد من المتجر.")]},
{
"en": "Not as ... as / less",
"ar": "ليس بنفس الدرجة: as...as",
"expl_ar": "للمساواة: as old as (بالسن نفس). للنفي: not as big as (ليس بالحجم نفسه).\nولتفضيل أقل: less expensive (أقل كلفة).",
"expl_en": "Equality: as...as. Not equal: not as...as. Less: less expensive.",
"formula": "as + adjective + as | not as + adjective + as",
"examples": [
("He is as tall as his father.", "هو بنفس طول والده."),
("This phone is not as expensive as that one.", "هذا الهاتف ليس بنفس كلفة ذلك."),
("The new car is less noisy.", "السيارة الجديدة أقل ضجيجا.")]},
{
"en": "Much / far + comparative",
"ar": "much / far لتقوية المقارنة",
"expl_ar": "لتقوية معنى المقارنة نستعمل much أو far أو a lot قبل الصفة المقارنة: much better (أفضل بكثير)، far more expensive (أغلى بكثير)، a lot taller (أطول بكثير).",
"expl_en": "Intensify with much / far / a lot: much better, far more expensive.",
"formula": "much / far + comparative",
"examples": [
("Oran is much hotter than Algiers in July.", "وهران أحن بكثير من الجزائر في جويلية."),
("This phone is far more expensive than that one.", "هذا الهاتف أغلى بكثير من ذلك."),
("Islem is a lot smaller than Oussama.", "إسلام أصغر بكثير من أسامة.")]},
{
"en": "Even + comparative",
"ar": "even + المقارنة (أكثر حتى)",
"expl_ar": "even تضيف مقارنة فوق مقارنة: It's cold, but the mountains (الجبال) are even colder (أبرد حتى).\nMy phone (هاتفي) is new, yours (هاتفك) is even newer.",
"expl_en": "'Even' adds to a comparison: even colder, even better.",
"formula": "even + comparative",
"examples": [
("Islem is good at reading, but Oussama is even better.", "إسلام جيد في القراءة، لكن أسامة أفضل حتى."),
("This test is even harder than the last one.", "هذا الاختبار أصعب حتى من السابق."),
("Your idea is even more interesting.", "فكرتك أكثر إثارة حتى.")]},
{
"en": "The + comparative, the + comparative",
"ar": "كلما... كلما (the + المقارنة)",
"expl_ar": "للربط بين تطورين متوازيين: The more you read, the better you write (كلما قرأت أكثر كتبت أفضل).\nThe sooner we start, the sooner we finish (كلما بدأنا أبكر أنجزنا أبكر).",
"expl_en": "Parallel change: The more you practise, the better you get.",
"formula": "The + comparative, the + comparative",
"examples": [
("The more you practise, the better you become.", "كلما تدربت أكثر، أصبحت أفضل."),
("The louder he speaks, the less I understand.", "كلما زاد ارتفاع صوته، قل فهمي."),
("The sooner we start, the sooner we finish.", "كلما بدأنا أبكر، انتهينا أبكر.")]},
{
"en": "More + uncountable nouns",
"ar": "more + الأسماء غير المعدودة",
"expl_ar": "المقارنة بين الكميات غير المعدودة بـ more: more time (وقت أطول)، more money (مال أكثر)، more water (ماء أكثر).",
"expl_en": "Compare quantities: more time, more money, more water.",
"formula": "more + uncountable noun",
"examples": [
("I need more time to finish my homework.", "أحتاج وقتا أطول لإنجاز واجبي."),
("They have more money than us.", "لديهم مال أكثر منا."),
("Drink more water in summer.", "اشرب ماء أكثر في الصيف.")]},
]
},
# ============================ NIVEAU 34 ============================
{
"num": 34, "cefr": "A2",
"category": "Superlatives",
"category_ar": "صيغة التفضيل",
"title_en": "Superlatives: -est / the most",
"title_ar": "صيغة التفضيل: الأطول، الأفضل",
"ideas": [
{
"en": "Short adjectives + est",
"ar": "الصفات القصيرة + est",
"expl_ar": "للتفضيل (الأفضل من مجموعة) نضيف est للصفات القصيرة مع the: the tallest (الأطول)، the oldest (الأقدم)، the coldest (الأبرد).",
"expl_en": "Short adjectives: the + adjective + est: the tallest.",
"formula": "the + adjective + est",
"examples": [
("Mount Everest is the highest mountain.", "إيفرست هو أعلى جبل."),
("Oussama is the oldest in the family.", "أسامة هو الأكبر في العائلة."),
("Winter is the coldest season.", "الشتاء أبرد فصل.")]},
{
"en": "Long adjectives + the most",
"ar": "الصفات الطويلة + the most",
"expl_ar": "مع الصفات الطويلة نستعمل the most: the most beautiful (الأجمل)، the most interesting (الأكثر إثارة)، the most expensive (الأغلى).",
"expl_en": "Long adjectives: the most + adjective: the most beautiful.",
"formula": "the most + long adjective",
"examples": [
("She is the most talented student.", "هي الطالبة الأكثر موهبة."),
("This is the most expensive restaurant in town.", "هذا أغلى مطعم في المدينة."),
("It was the most exciting match ever.", "كانت المباراة الأكثر إثارة إطلاقا.")]},
{
"en": "Spelling: y → iest, nice → nicest",
"ar": "إملاء التفضيل: y و e",
"expl_ar": "y → iest: happy → happiest، easy→easier→easiest.\nالصفة المنتهية بـ e: nice → nicest، large → largest.",
"expl_en": "happy→happiest, easy→easiest; nice→nicest, large→largest.",
"formula": "happy→the happiest • nice→the nicest",
"examples": [
("Today is the happiest day of my life.", "اليوم أسعد يوم في حياتي."),
("This is the easiest exercise.", "هذا أسهل تمرين."),
("She chose the largest piece.", "اختارت أكبر قطعة.")]},
{
"en": "Double consonant: big → the biggest",
"ar": "مضاعفة الساكن: the biggest",
"expl_ar": "نمط ساكن+علة+ساكن نضاعف: big → the biggest، hot → the hottest، thin → the thinnest، sad → the saddest.",
"expl_en": "CVC: the biggest, the hottest, the thinnest.",
"formula": "big→the biggest • hot→the hottest",
"examples": [
("Sahara is the biggest desert.", "الصحراء الكبرى أكبر صحراء."),
("July is the hottest month here.", "يوليو أحر شهر هنا."),
("He got the thinnest slice.", "حصل على أنحف شريحة.")]},
{
"en": "Irregular superlatives: the best, the worst",
"ar": "تفضيلات شاذة: الأفضل، الأسوأ",
"expl_ar": "good → the best (الأفضل)، bad → the worst (الأسوأ)، far → the farthest (الأبعد).\nلا نقول the goodest ولا the most good.",
"expl_en": "Irregular: the best, the worst, the farthest.",
"formula": "good→the best • bad→the worst • far→the farthest",
"examples": [
("He is the best player on the team.", "هو أفضل لاعب في الفريق."),
("That was the worst meal I ever had.", "كانت أسوأ وجبة أكلتها."),
("This is the farthest village in the region.", "هذه أبعد قرية في المنطقة.")]},
{
"en": "The + superlative + in/of",
"ar": "the + تفضيل + in / of",
"expl_ar": "نحدد مجال التفضيل: in مع أماكن ومجموعة عامة: the tallest in the class، of مع مجموعة: the best of all.\nلا نستعمل than مع التفضيل.",
"expl_en": "Use 'in' for places/groups, 'of' for specific ones. Never 'than' with superlatives.",
"formula": "the + superlative + in + group/place",
"examples": [
("She is the fastest runner in the school.", "هي أسرع عداءة في المدرسة."),
("This is the best film of the year.", "هذا أفضل فيلم في السنة."),
("He is the tallest of the three brothers.", "هو الأطول بين الإخوة الثلاثة.")]},
{
"en": "Common superlative phrases",
"ar": "عبارات تفضيل شائعة",
"expl_ar": "عبارات يومية: the most important (الأهم)، the most delicious (الألذ)، the easiest (الأسهل)، the youngest (الأصغر)، the nearest (الأقرب)، the cheapest (الأرخص)، the highest (الأعلى).\nاحفظها بسياقها.",
"expl_en": "Useful: the most important, the youngest, the nearest, the cheapest.",
"formula": "the + best/easiest/cheapest/nearest...",
"examples": [
("Education is the most important thing.", "التعليم أهم شيء."),
("This is the nearest pharmacy.", "هذه أقرب صيدلية."),
("That's the cheapest option.", "هذا أرخص خيار.")]},
]
},
# ============================ NIVEAU 35 ============================
{
"num": 35, "cefr": "A2",
"category": "Comparatives vs Superlatives",
"category_ar": "المقارنة مقابل التفضيل",
"title_en": "Comparative vs Superlative: review",
"title_ar": "مراجعة: المقارنة والتفضيل",
"ideas": [
{
"en": "Comparing two vs three or more",
"ar": "مقارنة اثنين مقابل تفضيل ثلاثة",
"expl_ar": "المقارنة بين اثنين نستعمل -er أو more: Oussama is taller than Islem.\nالتفضيل بين ثلاثة فأكثر نستعمل -est أو the most: Oussama is the tallest.",
"expl_en": "Two things: comparative. Three or more: superlative.",
"formula": "2 → -er/more + than | 3+ → the -est/the most",
"examples": [
("Oran is bigger than Sidi Bel Abbès.", "وهران أكبر من سيدي بلعباس."),
("Oran is the biggest city in the west.", "وهران أكبر مدينة في الغرب."),
("This route is shorter than that one.", "هذا الطريق أقصر من ذلك.")]},
{
"en": "The pattern with than and in",
"ar": "النمط مع than و in",
"expl_ar": "المقارنة: A + verb + comparative + than + B. التفضيل: the + superlative + in/of.\nلن نخلط أحدهما.",
"expl_en": "Comparative + than + B. The + superlative + in + group.",
"formula": "X is bigger than Y | X is the biggest in Z",
"examples": [
("My room is cleaner than yours.", "غرفتي أنظف من غرفتك."),
("This is the cleanest kitchen I have seen.", "هذا أنظف مطبخ رأيته."),
("She is more patient than her husband.", "هي أكثر صبرا من زوجها.")]},
{
"en": "No 'than' with superlatives, no 'the' with comparatives (alone)",
"ar": "لا than مع التفضيل، ولا the مع المقارنة فقط",
"expl_ar": "مع التفضيل نستعمل the: the best، ولا نضيف than: أعلى من في المدرسة = the best in school.\nمع المقارنة نستعمل than ولا نضع عادة the: أنا أفضل = I am better، لا I am the better.",
"expl_en": "Superlative: the + -est (no than). Comparative: -er + than (no the in general use).",
"formula": "the best (no than) | better than (no the)",
"examples": [
("She is the best. Here, 'the' is needed.", "هي الأفضل. نحتاج the."),
("He is better than me at chess.", "هو أفضل مني في الشطرنج."),
("That is the highest building here.", "ذلك أطول مبنى هنا.")]},
{
"en": "Practice: compare and choose",
"ar": "تمرين: قارن واختر",
"expl_ar": "تدرب على تبديل: Of the two shirts (من القميصين)، this is cheaper. Of all the shirts (من بين كل القمصان)، this is the cheapest.\nأكمل الجمل بنفس الفكرة في مفردتين.",
"expl_en": "Practise: two → cheaper; many → the cheapest.",
"formula": "of two: cheaper | of many: the cheapest",
"examples": [
("Of the two bags, this one is lighter.", "من الحقيبتين، هذه أخف."),
("Of all the toys, this is the lightest.", "من بين كل الألعاب، هذه الأخف."),
("Ramadan is the most special month.", "رمضان هو أكثر الشهور خصوصية.")]},
]
},
# ============================ NIVEAU 36 ============================
{
"num": 36, "cefr": "A2",
"category": "Countable / Uncountable",
"category_ar": "المعدود وغير المعدود",
"title_en": "Countable and Uncountable Nouns",
"title_ar": "الأسماء المعدودة وغير المعدودة",
"ideas": [
{
"en": "Countable nouns: can count one by one",
"ar": "المعدود: يمكن عده",
"expl_ar": "المعدودة أسماء نعدها واحداً، اثنين: apple (تفاحة)، book (كتاب)، chair (كرسي)، house (منزل).\nلها جمع: an apple, two apples. نستعمل معها a/an والجمع.",
"expl_en": "Countable nouns have singular/plural and work with a/an and numbers.",
"formula": "a/an + singular count noun | plural + s",
"examples": [
("I have one apple.", "لدي تفاحة واحدة."),
("She bought three books.", "اشترت ثلاثة كتب."),
("There are five chairs in the room.", "توجد خمسة كراسي في الغرفة.")]},
{
"en": "Uncountable nouns: cannot count",
"ar": "غير المعدود: لا يعد",
"expl_ar": "غير المعدودة أسماء لا فاصل بين وحداتها: water (ماء)، milk (حليب)، rice (أرز)، sugar (سكر)، bread (خبز)، money (مال)، music (موسيقى)، information (معلومات).\nلا جمع ولا a/an معها.",
"expl_en": "Uncountable nouns: water, rice, money. No plural, no a/an.",
"formula": "uncountable: no a/an, no plural",
"examples": [
("Water is life.", "الماء حياة."),
("I need some money.", "أحتاج بعض المال."),
("She gave me good advice.", "أعطتني نصيحة جيدة.")]},
{
"en": "Quantify with containers and units",
"ar": "التعبير عن الكمية بالمقاييس",
"expl_ar": "لعدّ غير المعدود نستخدم وحدات: a glass of water (كأس ماء)، a cup of tea (كوب شاي)، a piece of bread (قطعة خبز)، a kilo of sugar (كيلو سكر)، a loaf of bread (رغيف خبز)، a bottle of milk (قنينة حليب).",
"expl_en": "Use units: a glass of water, a piece of bread, a kilo of sugar.",
"formula": "a + container/unit + of + uncountable",
"examples": [
("I drink a glass of milk daily.", "أشرب كأس حليب يوميا."),
("Buy a kilo of tomatoes, please.", "اشتر كيلو طماطم من فضلك."),
("He ate two pieces of cake.", "أكل قطعتين من الكعكة.")]},
{
"en": "Common uncountable mistakes",
"ar": "أخطاء شائعة مع غير المعدود",
"expl_ar": "انتبه: معلومات (information) وليس informations، وثقافة advise، و homework (واجب منزلي): pieces of homework.\nلا نقول an information ولا advices.",
"expl_en": "No 'informations', no 'advices'. Use 'some information/advice'.",
"formula": "some information • some advice • no plural",
"examples": [
("This is useful information.", "هذه معلومات مفيدة."),
("Can you give me some advice?", "هل يمكنك أن تعطيني نصيحة؟"),
("I have to do my homework.", "علي إنجاز واجبي.")]},
{
"en": "Verbs with count/uncount",
"ar": "الأفعال مع المعدود وغير المعدود",
"expl_ar": "مع غير المعدود نستخدم مفرد الفعل: Water is، Money is، Sugar is.\nمع المعدود الجمع: Books are. 'is' للوحدة وإما جمع المعدودة",
"expl_en": "Uncountable → singular verb (is). Plural countables → are.",
"formula": "uncountable + is | plural countable + are",
"examples": [
("Sugar is sweet.", "السكر حلو."),
("The news is good.", "الأخبار جيدة (غير معدود)."),
("Her ideas are excellent.", "أفكارها ممتازة (جمع).")]},
]
},
# ============================ NIVEAU 37 ============================
{
"num": 37, "cefr": "A2",
"category": "Some / Any / No",
"category_ar": "some / any / no",
"title_en": "Some, Any, No",
"title_ar": "بعض، أي، لا",
"ideas": [
{
"en": "Some = positive, Any = question/negative",
"ar": "some للمثبت، any للسؤال والنفي",
"expl_ar": "some في الجمل المثبتة (بعض): I have some money (لدي بعض المال).\nany في الأسئلة والنفي: Do you have any money? (هل لديك مال؟) I don't have any.",
"expl_en": "Some in positives. Any in questions and negatives.",
"formula": "positive: some | question/negative: any",
"examples": [
("I have some money in my pocket.", "لدي بعض المال في جيبي."),
("Do you have any questions?", "هل لديك أي سؤال؟"),
("I don't have any time today.", "ليس لدي أي وقت اليوم.")]},
{
"en": "Some in offers and requests",
"ar": "some في العروض والطلبات",
"expl_ar": "في الأسئلة التي تشبه العروض والطلبات نستعمل some وليس any: Would you like some tea (هل تود بعض الشاي)؟ Can I have some water (هل يمكنني الحصول على ماء)؟",
"expl_en": "Offers/requests use some: Would you like some tea?",
"formula": "offer/request: some (any rarely)",
"examples": [
("Would you like some coffee?", "هل تود بعض القهوة؟"),
("Can I have some sugar, please?", "هل يمكنني أخذ بعض السكر؟"),
("Do you want some dates?", "هل تريد بعض التمر؟")]},
{
"en": "Any in positives = 'it doesn't matter which'",
"ar": "any في المثبت = أياً كان",
"expl_ar": "في الجمل المثبتة، any تعني «أياً كان، مهما كان»: You can come any day (في أي يوم). Take any seat (خذ أي مقعد).",
"expl_en": "Any in positives means 'no matter which': any day, any seat.",
"formula": "positive + any = whichever",
"examples": [
("You can ask any question.", "يمكنك طرح أي سؤال."),
("Come back any time you want.", "عد متى شئت."),
("Any student can join the club.", "أي طالب يمكنه الانضمام للنادي.")]},
{
"en": "No = not any",
"ar": "no = لا (نفي)",
"expl_ar": "no تعني «لا يوجد أي» وتعمل نفي المفرد: I have no time (ليس لدي وقت) (= I don't have any time)، There is no milk (لا يوجد حليب) (= There isn't any milk).\nلا نجمع نفيين.",
"expl_en": "No = not any: I have no time. Don't use double negatives.",
"formula": "No + noun (nobody, nothing...)",
"examples": [
("I have no money today.", "ليس لدي مال اليوم."),
("There is no school on Friday.", "لا توجد مدرسة يوم الجمعة."),
("We have no homework tonight.", "لا واجب لدينا الليلة.")]},
{
"en": "Compounds: something/anything/nothing",
"ar": "المركبات: شيء/أي شيء/لا شيء",
"expl_ar": "نفس القاعدة مع المركبات: something (شيء ما - مثبت)، anything (أي شيء - سؤال/نفي)، nothing (لا شيء).\nI want something، Is there anything?، I need nothing.",
"expl_en": "Compounds: something, anything, nothing (same rule as some/any).",
"formula": "+ something | ? anything | − nothing",
"examples": [
("I want something sweet.", "أريد شيئا حلوا."),
("Is there anything in the fridge?", "هل يوجد شيء في الثلاجة؟"),
("There is nothing to worry about.", "لا شيء يدعو للقلق.")]},
{
"en": "Someone/anyone/no one",
"ar": "شخص/أي شخص/لا أحد",
"expl_ar": "بالنسبة للأشخاص: someone (شخص ما)، anyone (أي شخص)، no one / nobody (لا أحد).\nمثال: Is anyone here? (هل يوجد أحد هنا؟) No one came (لم يأت أحد).",
"expl_en": "People: someone, anyone, no one/nobody.",
"formula": "+ someone | ? anyone | − no one/nobody",
"examples": [
("Someone is knocking at the door.", "شخص ما يطرق الباب."),
("Did anyone call me?", "هل اتصل بي أحد؟"),
("No one knows the answer.", "لا أحد يعرف الجواب.")]},
{
"en": "Somewhere/anywhere/nowhere",
"ar": "مكان ما/أي مكان/لا مكان",
"expl_ar": "للأماكن: somewhere (مكان ما)، anywhere (أي مكان)، nowhere (لا مكان).\nLet's go somewhere quiet (لنذهب إلى مكان هادئ)، I can't find it anywhere (لا أجده في أي مكان).",
"expl_en": "Places: somewhere, anywhere, nowhere.",
"formula": "+ somewhere | ? anywhere | − nowhere",
"examples": [
("We need to go somewhere cool.", "نحتاج الذهاب لمكان بارد."),
("Have you seen my keys anywhere?", "هل رأيت مفاتيحي في أي مكان؟"),
("There is nowhere to sit.", "لا يوجد مكان للجلوس.")]},
]
},
# ============================ NIVEAU 38 ============================
{
"num": 38, "cefr": "A2",
"category": "Much / Many / A lot of",
"category_ar": "much / many / a lot of",
"title_en": "Much, Many, A lot of",
"title_ar": "الكثرة: much, many, a lot of",
"ideas": [
{
"en": "Many + countable plural",
"ar": "many + معدود جمع",
"expl_ar": "many (كثير) مع الأسماء المعدودة الجمع: many books (كتب كثيرة)، many students (طلاب كثيرون)، many problems (مشاكل كثيرة).\nنستعملها خاصة في النفي والسؤال.",
"expl_en": "Many + plural countable nouns: many books, many students.",
"formula": "many + plural countable",
"examples": [
("How many books do you have?", "كم كتابا لديك؟"),
("There aren't many chairs here.", "لا توجد كراسي كثيرة هنا."),
("Many people visit this beach in summer.", "كثير من الناس يزورون هذا الشاطئ صيفا.")]},
{
"en": "Much + uncountable",
"ar": "much + غير معدود",
"expl_ar": "much (كثير) مع الأسماء غير المعدودة: much water (ماء كثير)، much time (وقت كثير)، much money (مال كثير).\nخاصة في النفي والسؤال.",
"expl_en": "Much + uncountable nouns: much water, much time.",
"formula": "much + uncountable",
"examples": [
("I don't have much time.", "ليس لدي وقت كثير."),
("How much sugar do we need?", "كم سكر نحتاج؟"),
("There isn't much milk left.", "لا توجد حليب كثير متبقٍ.")]},
{
"en": "A lot of / lots of + both",
"ar": "a lot of مع الاثنين معاً",
"expl_ar": "a lot of تناسب المعدود وغير المعدود في الجمل المثبتة: a lot of people (ناس كثيرون)، a lot of water (ماء كثير).\nفي الكلام الشائع: lots of.",
"expl_en": "A lot of/lots of works with both types, mainly in positives.",
"formula": "a lot of + count/uncount",
"examples": [
("We have a lot of homework.", "لدينا واجب كثير."),
("There are a lot of cars here.", "هناك سيارات كثيرة هنا."),
("He drinks a lot of water.", "يشرب ماء كثيرا.")]},
{
"en": "Which one to choose?",
"ar": "كيف تختار؟",
"expl_ar": "في الواقع: هل الاسم معدود؟ → many / a lot of. غير معدود؟ → much / a lot of.\nكثيراً ما الإنجليزية الحديثة تفضل a lot of في المثبت.",
"expl_en": "Countable → many/lots. Uncountable → much/lots. Use a lot of generally.",
"formula": "countable → many | uncountable → much",
"examples": [
("How many eggs are in the basket?", "كم بيضة في السلة؟"),
("How much rice do we have?", "كم أرزا لدينا؟"),
("We used a lot of oil.", "استعملنا زيتا كثيرا.")]},
{
"en": "So much / so many",
"ar": "so much / so many (كثير جداً)",
"expl_ar": "so تقوي: so much (كثير جداً مع غير المعدود)، so many (كثير جداً مع المعدود).\nThere was so much noise (كان هناك ضجيج كثير)، She has so many friends (لديها أصدقاء كثيرون).",
"expl_en": "Intensity: so much (uncountable), so many (countable).",
"formula": "so much + uncount | so many + plural",
"examples": [
("You eat so much sugar.", "تأكل سكرا كثيرا جدا."),
("I have so many things to do.", "لدي أشياء كثيرة جدا لأفعلها."),
("It rained so much last night.", "أمطرت بكثرة الليلة الماضية.")]},
]
},
# ============================ NIVEAU 39 ============================
{
"num": 39, "cefr": "A2",
"category": "A Little / A Few",
"category_ar": "a little / a few (قليل)",
"title_en": "A little, A few",
"title_ar": "a little / a few",
"ideas": [
{
"en": "A few + countable",
"ar": "a few + معدود",
"expl_ar": "a few (قليل) مع الأسماء المعدودة الجمع: a few books (قليل من الكتب)، a few minutes (دقائق قليلة)، a few friends (بعض الأصدقاء).",
"expl_en": "A few + plural countable: a few books.",
"formula": "a few + plural countable",
"examples": [
("I have a few questions.", "لدي بضعة أسئلة."),
("Wait a few minutes, please.", "انتظر بضع دقائق من فضلك."),
("She made a few mobile calls.", "أجرت بضع مكالمات هاتفية.")]},
{
"en": "A little + uncountable",
"ar": "a little + غير معدود",
"expl_ar": "a little (قليل) مع الأسماء غير المعدودة: a little sugar (سكر قليل)، a little time (وقت قليل)، a little water (ماء قليل).",
"expl_en": "A little + uncountable: a little sugar.",
"formula": "a little + uncountable",
"examples": [
("Add a little salt to the soup.", "أضف قليلا من الملح إلى الحساء."),
("I speak a little English.", "أتحدث القليل من الإنجليزية."),
("We have a little time before the bus.", "لدينا القليل من الوقت قبل الحافلة.")]},
{
"en": "A few = some (positive), Few = not many",
"ar": "a few = بعض، few = ليس كثيراً",
"expl_ar": "الفرق الدقيق: a few (بعض/ما يكفي): I have a few friends (بعض الأصدقاء).\nfew بدون a (قلة/ليس كثيراً): Few people came (قلة من الناس حضروا).",
"expl_en": "A few = some (positive). Few = not many (negative idea).",
"formula": "a few = some | few = not many",
"examples": [
("I have a few days free.", "لدي بضعة أيام فارغة."),
("Few students understood the lesson.", "قليل من الطلاب فهموا الدرس."),
("A few people raised their hands.", "رفع بعض الناس أيديهم.")]},
{
"en": "A little = some, Little = not much",
"ar": "a little = بعض، little = ليس كثيراً",
"expl_ar": "a little (بعض/قدر): I have a little money (لدي القليل من المال). little (قليل جداً): There is little hope (أمل ضئيل).\nنفس الفرق الدقيق.",
"expl_en": "A little = some. Little = very small amount.",
"formula": "a little = some | little = hardly any",
"examples": [
("I know a little Arabic.", "أعرف القليل من العربية."),
("There is little chance of rain.", "هناك فرصة ضئيلة للمطر."),
("She has a little experience.", "لديها بعض الخبرة.")]},
{
"en": "Quite a few / quite a little",
"ar": "تأكيد: quite a few",
"expl_ar": "quite a few تعني حقاً كثير (المفاجأة بالعكس): quite a few people = عدد لا بأس به.\nمع غير المعدود: quite a lot of.",
"expl_en": "Quite a few = quite many (surprise positive).",
"formula": "quite a few + plural | a lot of + uncount",
"examples": [
("Quite a few cars passed by.", "مرت سيارات كثيرة نوعا ما."),
("We have quite a lot of time.", "لدينا متسع من الوقت."),
("Quite a few students passed the exam.", "نجح عدد لا بأس به من الطلاب.")]},
]
},
# ============================ NIVEAU 40 ============================
{
"num": 40, "cefr": "A2",
"category": "How much / How many",
"category_ar": "السؤال عن الكمية",
"title_en": "How much? / How many?",
"title_ar": "كم؟ (How much / How many)",
"ideas": [
{
"en": "How many + countable",
"ar": "How many + معدود",
"expl_ar": "للسؤال عن عدد الأشياء المعدودة: How many brothers do you have? (كم أخاً لديك؟)، How many days (كم يوما)؟",
"expl_en": "How many + countable: How many brothers do you have?",
"formula": "How many + plural countable + verb?",
"examples": [
("How many students are in your class?", "كم طالبا في قسمك؟"),
("How many hours do you sleep?", "كم ساعة تنام؟"),
("How many languages does she speak?", "كم لغة تتحدث؟")]},
{
"en": "How much + uncountable",
"ar": "How much + غير معدود",
"expl_ar": "للسؤال عن مقدار غير المعدود: How much water do you drink? (كم ماء تشرب؟)، How much money (كم من المال)؟",
"expl_en": "How much + uncountable: How much water do you drink?",
"formula": "How much + uncountable + verb?",
"examples": [
("How much sugar is in this tea?", "كم سكر في هذا الشاي؟"),
("How much time do we have?", "كم لدينا من الوقت؟"),
("How much homework did the teacher give?", "كم واجب أعطى المعلم؟")]},
{
"en": "How much = price too",
"ar": "How much = كم (ثمن) أيضاً",
"expl_ar": "بمعنى الثمن: How much is it? (كم ثمنها؟)، How much are these shoes? (بكم هذه الأحذية؟).",
"expl_en": "'How much is it?' = What's the price?",
"formula": "How much + is/are + noun?",
"examples": [
("How much is this phone?", "بكم هذا الهاتف؟"),
("How much are the bananas?", "بكم الموز؟"),
("How much does it cost?", "كم يكلف؟")]},
{
"en": "Answers: with numbers or quantity words",
"ar": "الأجوبة: أرقام أو كلمات كمية",
"expl_ar": "الجواب عن How many: أعداد أو a few / many: Three. / A few.\nعن How much: قياسات أو a little / some: A litre (لتر) / Not much.",
"expl_en": "Answers: numbers + a few/many, or units + a little/some.",
"formula": "How many → number/a few | How much → a litre/a little",
"examples": [
("How many apples? About ten.", "كم تفاحة؟ حوالي عشرة."),
("How much milk? A litre.", "كم حليبا؟ لتر واحد."),
("How much homework? Not much.", "كم واجبا؟ ليس كثيرا.")]},
{
"en": "Common shopping questions",
"ar": "أسئلة التسوق الشائعة",
"expl_ar": "في السوق: How much are the tomatoes? (بكم الطماطم؟)، How many do you want? (كم تريد؟)\nوهنا الفرق واضح بين الثمن والعدد.",
"expl_en": "Shopping: How much are...? (price) How many do you want? (count).",
"formula": "How much are + plural? | How many + noun + do you want?",
"examples": [
("How much is a kilo of oranges?", "بكم كيلو البرتقال؟"),
("How many kilos do you need?", "كم كيلو تحتاج؟"),
("I want two kilos, please.", "أريد كيلوين من فضلك.")]},
{
"en": "Not much / not many in answers",
"ar": "not much / not many في الجواب",
"expl_ar": "اجابات قصيرة: Not much (قليل - غير معدود)، Not many (قليل - معدود)، A lot (كثير).",
"expl_en": "Short answers: Not much (uncount), Not many (count), A lot.",
"formula": "answers: Not much / Not many / A lot",
"examples": [
("How much money do you have? Not much.", "كم لديك من المال؟ ليس كثيرا."),
("How many brothers? Not many, just two.", "كم أخا؟ اثنان فقط."),
("How much time? A lot.", "كم وقتا؟ كثيرا.")]},
]
},
]