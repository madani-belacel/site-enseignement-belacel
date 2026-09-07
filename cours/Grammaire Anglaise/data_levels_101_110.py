# -*- coding: utf-8 -*-
"""المستوى 101 : قواعد نطق الحروف المركبة وأصواتها في الإنجليزية (English Sounds & Rules).
مأخوذة من كتاب: جميع قواعد النطق في اللغة الإنجليزية.
المحتوى معروض في شكل جدول مقسّم إلى أقسام (table + sections)."""

LEVELS = [

# ============================ NIVEAU 101 ============================
{
"num": 101, "cefr": "A1",
"category": "Digraphs & Compound Letter Sounds",
"category_ar": "أصوات الحروف المركبة في اللغة الإنجليزية",
"title_en": "Sounds & Pronunciation Rules",
"title_ar": "قواعد نطق الحروف المركبة في اللغة الإنجليزية (Digraphs & Rules)",
"layout": "table",
"audio_col": 2,
"audio_prefix_col": 0,
"table_columns": ["الحرف/الصوت", "النطق بالعربية", "أمثلة بالإنجليزية", "المعنى بالعربية", "ملاحظات"],
"table_rows": [

# ======================== القسم 1 : الحروف المركبة الساكنة ========================
["SECTION", "قسم 1 : الحروف المركبة الساكنة (Consonant Digraphs & Trigraphs)"],

["CH", "تش", "chair, cheese, choose, church, child, teacher, lunch", "كرسي, جبن, يختار, كنيسة, طفل, معلم, غداء", "حرفان = صوت تش في أغلب الكلمات (الأصل الأنجلوسكسوني)"],
["CH", "ك", "school, chemistry, character, stomach, echo, chaos", "مدرسة, كيمياء, شخصية, معدة, صدى, فوضى", "CH = ك في كلمات من أصل يوناني - مثال: chemistry = كيمياء تُلفظ «كيمستري» وليس «شيمستري»"],
["CH", "ش", "chef, machine, mustache, Chicago", "طاهٍ, آلة, شارب (نوع شعر), شيكاغو", "CH = ش في الكلمات من أصل فرنسي"],
["SH", "ش", "she, shop, sheep, ship, fish, wish, shadow", "هي, محل, خروف, سفينة, سمكة, أمنية, ظل", "SH = ش دائماً بلا استثناء"],
["WH", "و", "what, where, when, why, white, which", "ماذا, أين, متى, لماذا, أبيض, أيّ", "WH = و غالباً ويظهر في كلمات الأسئلة"],
["PH", "ف", "phone, photo, elephant, dolphin, graph, alphabet", "هاتف, صورة, فيل, دلفين, رسم بياني, أبجدية", "PH = ف دائماً (أصل يوناني)"],
["TH", "ذ", "the, this, that, there, these, they, mother, father", "ال, هذا, ذلك, هناك, هؤلاء, هم, أم, أب", "TH مجهورة = ذ في الكلمات الوظيفية والضمائر وأسماء الأقارب"],
["TH", "ث", "think, three, thank, thin, thumb, bath, tooth, math", "يفكر, ثلاثة, شكراً, نحيف, إبهام, حمام, سن, رياضيات", "TH مهموسة = ث في الأسماء والأفعال"],
["GH", "ج", "ghost, ghetto", "شبح, حي فقير (جيتو)", "GH = ج فقط في بداية الكلمة (حالات نادرة)"],
["GH", "صامتة", "light, night, right, high, through, eight, daughter", "ضوء, ليل, صحيح, مرتفع, عبر, ثمانية, ابنة", "GH صامتة بعد حرف متحرك (أكثر الحالات)"],
["GH", "ف", "laugh, cough, enough, rough, tough", "يضحك, يسعل, يكفي, خشن, صعب", "GH = ف بعد ou في نهاية الكلمة (مجموعة صغيرة تُحفظ)"],
["CK", "ك", "back, duck, neck, lock, kick, quick, rock", "ظهر, بطة, رقبة, قفل, يركل, سريع, صخرة", "CK = ك دائماً بعد حرف متحرك قصير"],
["NG", "نغ", "sing, king, long, song, ring, thing, morning", "يغني, ملك, طويل, أغنية, خاتم, شيء, صباح", "NG = صوت أنفي واحد نغ يُنطق من الأنف"],
["TCH", "تش", "match, watch, kitchen, catch, switch", "مباراة, يشاهد, مطبخ, يمسك, مفتاح كهربائي", "TCH = تش بعد حرف متحرك قصير"],
["DGE", "ج", "bridge, badge, edge, judge, fridge", "جسر, شارة, حافة, قاضٍ, ثلاجة", "DGE = ج بعد حرف متحرك قصير"],
["QU", "كو", "quick, queen, quiet, question, quarter, quantity", "سريع, ملكة, هادئ, سؤال, ربع, كمية", "Q يتبعها دائماً U وتُنطقان كو"],
["GU", "غ", "guess, guest, guide, guitar, guard", "يخمّن, ضيف, مرشد, قيثارة, حارس", "GU = غ في بداية الكلمة"],
["SC", "س", "science, scissors, scene, scenery", "علم, مقص, مشهد, منظر طبيعي", "SC = س قبل e أو i"],
["SC", "سك", "school, score, scream, screen, Scotland", "مدرسة, نتيجة, يصرخ, شاشة, اسكتلندا", "SC = سك قبل a/o/u أو ساكن"],

# ======================== القسم 2 : C و G القاسية واللينة ========================
["SECTION", "قسم 2 : C و G — هل هي قاسية أم لينة؟ (Soft & Hard C / G)"],

["CE/CI/CY", "س", "face, city, cinema, bicycle, center, cycle, nice", "وجه, مدينة, سينما, دراجة, مركز, دورة, لطيف", "C لينة = س قبل e أو i أو y"],
["C + a/o/u", "ك", "cat, cup, carrot, coffee, come, cold, candy", "قطة, كوب, جزرة, قهوة, يأتي, بارد, حلوى", "C قاسية = ك قبل a/o/u أو حرف ساكن"],
["GE/GI/GY", "ج", "change, orange, page, giant, giraffe, magic, gym", "تغيير, برتقالة, صفحة, عملاق, زرافة, سحر, صالة رياضة", "G لينة = ج قبل e أو i أو y"],
["G + a/o/u", "غ", "go, game, garden, gold, good, got", "يذهب, لعبة, حديقة, ذهب, جيد, نال", "G قاسية = غ قبل a/o/u أو في نهاية الكلمة (استثناء قبل i: give, get, girl)"],

# ======================== القسم 3 : الحروف الصامتة ========================
["SECTION", "قسم 3 : الحروف الصامتة (Silent Letters)"],

["KN", "ن", "knee, know, knife, knock, knit, knowledge", "ركبة, يعرف, سكين, يطرق, يحيك, معرفة", "K صامتة في بداية الكلمة قبل N"],
["WR", "ر", "write, wrong, wrist, wrap, wreck, wrestle", "يكتب, خطأ, معصم, يلف, حطام, مصارعة", "W صامتة في بداية الكلمة قبل R"],
["MB/BT", "م / ت", "comb, lamb, thumb, climb, debt, doubt", "مشط, خروف صغير, إبهام, يتسلق, دَين, شك", "B صامتة بعد M أو قبل T"],
["PS", "س", "psychology, psalm, pseudonym", "علم النفس, مزمور, اسم مستعار", "P صامتة في بداية الكلمات (أصل يوناني)"],
["MN", "ن", "autumn, column, condemn, hymn", "خريف, عمود, يدين, ترنيمة", "N صامتة بعد M في نهاية الكلمة"],
["Silent L", "لا تنطق", "talk, walk, half, calm, could, should, would", "يتحدث, يمشي, نصف, هادئ, استطاع, يجب, سوف", "L صامتة قبل K/F/M وفي could/should/would"],
["Silent H", "لا تنطق", "hour, honest, honor, heir", "ساعة, صادق, شرف, وريث", "H صامتة في بداية بعض الكلمات (من أصل فرنسي)"],

# ======================== القسم 4 : مقاطع -ion وغيرها ========================
["SECTION", "قسم 4 : نطق المقاطع المركبة الشائعة (-tion، -sion، -ture...)"],

["TION", "شن", "station, nation, action, information, education, position", "محطة, أمة, عمل, معلومات, تعليم, وظيفة", "TION = شن وتُحوّل الأفعال إلى أسماء"],
["TIAN", "شن", "Egyptian, Martian, Venetian", "مصري, مريخي, سكان البندقية", "TIAN = شن وتدل على النسبة"],
["SION", "شن", "tension, expression, mission, passion, discussion", "توتر, تعبير, مهمة, شغف, نقاش", "SION = شن بعد حرف ساكن"],
["SION", "جن", "vision, decision, television, conclusion, confusion", "رؤية, قرار, تلفاز, استنتاج, ارتباك", "SION = جن (صوت zh) بعد حرف متحرك"],
["STION", "تشن", "question, suggestion, digestion, exhaustion", "سؤال, اقتراح, هضم, إرهاق", "STION = تشن دائماً"],
["CIAN", "شن", "musician, electrician, politician, magician, technician", "موسيقي, كهربائي, سياسي, ساحر, تقني", "CIAN = شن وتدل على المهنة"],
["CI/CIA/CIO", "ش", "social, special, official, delicious, precious", "اجتماعي, خاص, رسمي, لذيذ, ثمين", "C = ش إذا جاء بعده i أو a"],
["CEA", "شا", "ocean", "محيط", "CEA = شا"],
["TI/TIA/TIO", "ش", "action, nation, patient, essential, initial", "عمل, أمة, مريض, أساسي, أولي", "TI = ش إذا جاء بعده a أو o"],
["TURE", "شر", "nature, picture, future, culture, furniture, temperature", "طبيعة, صورة, مستقبل, ثقافة, أثاث, حرارة", "TURE = شر (تشور) في نهاية الكلمة"],
["SURE", "جن", "measure, treasure, pleasure, leisure", "قياس, كنز, متعة, وقت الفراغ", "SURE = جن (صوت zh) ما عدا sure = شور"],
["SUA", "جا", "usually, casual", "عادةً, عادي/غير رسمي", "SUA = جا (صوت zh)"],

# ======================== القسم 5 : الحروف الصوتية المركبة ========================
["SECTION", "قسم 5 : الحروف الصوتية المركبة (Vowel Digraphs)"],

["AI/AY", "إي", "rain, wait, train, day, play, say, today", "مطر, ينتظر, قطار, يوم, يلعب, يقول, اليوم", "AI في منتصف الكلمة و AY في نهايتها"],
["EA", "إي", "eat, tea, read, sea, teacher, clean, speak", "يأكل, شاي, يقرأ, بحر, معلم, نظيف, يتكلم", "EA = إي طويل في أغلب الكلمات"],
["EA", "إِ", "bread, head, dead, breakfast, health, weather", "خبز, رأس, ميت, فطور, صحة, طقس", "EA = إِ قصيرة في مجموعة تُحفظ"],
["EE", "إي", "see, tree, green, week, feet, sleep", "يرى, شجرة, أخضر, أسبوع, أقدام, ينام", "EE = إي طويل دائماً"],
["IE", "إي", "field, piece, chief, believe, thief, achieve", "حقل, قطعة, زعيم, يعتقد, لص, يحقق", "IE في منتصف الكلمة = إي"],
["IE", "آي", "pie, tie, die, lie, cried, tried", "فطيرة, ربطة عنق, يموت, يكذب, بكى, حاول", "IE في نهاية الكلمة = آي"],
["EI/EIGH", "إي", "receive, ceiling, eight, weight, neighbor", "يستلم, سقف, ثمانية, وزن, جار", "EI = إي بعد C، و EIGH = إي"],
["IGH", "آي", "light, night, right, high, bright, fight", "ضوء, ليل, صحيح, مرتفع, ساطع, يقاتل", "IGH = آي في عدد كبير من الكلمات"],
["OA", "أو", "boat, coat, road, soap, goat, float", "قارب, معطف, طريق, صابون, ماعز, يطفو", "OA = أو في منتصف الكلمة"],
["OO", "و", "book, look, good, foot, cook, wood", "كتاب, ينظر, جيد, قدم, يطبخ, خشب", "OO قصيرة = و"],
["OO", "أوو", "moon, food, zoo, room, soon, cool, spoon", "قمر, طعام, حديقة حيوان, غرفة, قريباً, بارد, ملعقة", "OO طويلة = أوو (استثناء: flood, blood = أ)"],
["OI/OY", "واي", "coin, point, voice, boy, toy, joy", "عملة, نقطة, صوت, ولد, لعبة, فرح", "OI في المنتصف و OY في النهاية"],
["OW", "آو", "cow, town, brown, down, flower", "بقرة, مدينة, بني, أسفل, زهرة", "OW = آو في كلمات مثل cow"],
["OW", "أو", "show, snow, yellow, window, bowl", "يعرض, ثلج, أصفر, نافذة, وعاء", "OW = أو طويل في كلمات مثل snow"],
["OU", "آو", "out, house, mouse, cloud, sound, round", "خارج, بيت, فأر, سحابة, صوت, دائري", "OU = آو في أغلب الكلمات"],
["OU", "أ", "young, country, trouble, double, touch", "شاب, بلد, مشكلة, مزدوج, يلمس", "OU = أ في مجموعة تُحفظ"],
["OU", "أوو", "you, group, soup, youth", "أنت, مجموعة, حساء, شباب", "OU = أوو في كلمات قليلة"],
["AU/AW", "أو", "sauce, August, autumn, because, saw, law, draw", "صلصة, أغسطس, خريف, لأن, منشار, قانون, يرسم", "AU و AW = أو"],
["EW", "يو/أو", "new, few, knew, grew, drew, flew", "جديد, قليل, عرف, كبر, رسم, طار", "EW = يو (new) أو أو بعد g/r"],
["UE/UI", "أو", "blue, true, glue, fruit, juice, suit", "أزرق, صحيح, غراء, فاكهة, عصير, بدلة", "UE و UI = أو"],
["UY", "آي", "buy, guy, disguise", "يشتري, رجل, تنكّر", "UY = آي"],
["Y (نهاية)", "إي", "happy, city, story, baby, very, sunny", "سعيد, مدينة, قصة, طفل, جداً, مشمس", "Y في نهاية كلمة متعددة المقاطع = إي"],
["Y (قصيرة)", "آي", "my, fly, try, sky, cry, why", "لي, يطير, يحاول, سماء, يبكي, لماذا", "Y في نهاية كلمة قصيرة = آي"],
["Y (منتصف)", "إِ", "gym, myth, symbol, system", "صالة رياضة, أسطورة, رمز, نظام", "Y في منتصف الكلمة = إِ مثل الحرف i"],
["WA", "و", "want, watch, wash, water, was, what", "يريد, يشاهد, يغسل, ماء, كان, ماذا", "WA = و وكأن A تختفي"],
["AL", "أو", "all, ball, small, tall, call, wall", "كل, كرة, صغير, طويل, يتصل, جدار", "AL = أو ولها l صامتة في كلمات مثل talk و walk"],

# ======================== القسم 6 : النطق مع R ========================
["SECTION", "قسم 6 : النطق مع R (R-Controlled Vowels)"],

["AR", "آر", "car, star, far, hard, park, garden, market", "سيارة, نجمة, بعيد, صعب, حديقة عامة, حديقة, سوق", "AR = آر (تُنطق r بوضوح)"],
["ER", "أَرْ", "her, sister, teacher, water, winter, father", "هي (ضمير), أخت, معلم, ماء, شتاء, أب", "ER في نهاية الكلمة = أَرْ خفيفة"],
["IR", "أَرْ", "bird, girl, first, shirt, third, dirty", "طائر, فتاة, أول, قميص, ثالث, متسخ", "IR = أَرْ ويُنطق مثل ER و UR"],
["UR", "أَرْ", "turn, hurt, nurse, purple, return, surface", "يدور, يؤلم, ممرضة, بنفسجي, يعود, سطح", "UR = أَرْ وبنفس صوت IR و ER"],
["OR", "أور", "for, short, morning, horse, sport, corner", "لـ, قصير, صباح, حصان, رياضة, زاوية", "OR = أور (بعد W تُنطق أَرْ: word, work, world)"],
["AIR/EIR/ARE", "إير", "hair, chair, fair, air, their, where, care, share", "شعر, كرسي, عادل, هواء, ملكهم, أين, يعتني, يشارك", "AIR و EIR و ARE = إير"],
["EAR", "إير", "ear, hear, near, clear, year, dear, here", "أذن, يسمع, قريب, واضح, سنة, عزيز, هنا", "EAR = إير"],
["OOR/OAR/OUR", "أور", "door, floor, poor, board, four, your, pour", "باب, أرضية, فقير, لوح, أربعة, لك, يسكب", "OOR و OAR و OUR = أور"],

# ======================== القسم 7 : لواحق النهاية وقواعد خاصة ========================
["SECTION", "قسم 7 : لواحق النهاية وقواعد خاصة (Endings & Special Rules)"],

["Silent E", "يطوّل المتحرك", "cake, name, time, home, use, hope, make", "كعكة, اسم, وقت, منزل, يستعمل, يأمل, يصنع", "حرف E في نهاية الكلمة صامت لكنه يطوّل المتحرك قبله"],
["-ED", "د", "played, opened, cleaned, lived, loved", "لعب, فتح, نظّف, عاش, أحب", "ED = د بعد حرف مجهور أو متحرك"],
["-ED", "ت", "walked, helped, stopped, cooked, washed", "مشى, ساعد, توقف, طبخ, غسل", "ED = ت بعد حرف مهموس (غير مجهور)"],
["-ED", "إد", "wanted, needed, visited, decided, started", "أراد, احتاج, زار, قرر, بدأ", "ED = إد بعد حرفي t أو d"],
["-S/-ES", "س/ز/إز", "boys (ز), dogs (ز), cats (س), books (س), boxes (إز), watches (إز)", "أولاد, كلاب, قطط, كتب, صناديق, ساعات", "الجمع: ز بعد مجهور، س بعد مهموس، إز بعد s/sh/ch/x"],
["OUGH", "متعددة", "though (أو), through (أوو), cough (أوف), rough (أف), bough (آو)", "رغم أن, عبر, يسعل, خشن, غصن", "OUGH لها 5 نطقات مختلفة يجب حفظها"],

# ======================== القسم 8 : حروف لها أكثر من نطق ========================
["SECTION", "قسم 8 : حروف لها أكثر من نطق (Special Sounds: X و S)"],

["X (أول الكلمة)", "ز", "xylophone, xenon, Xerox, xenophobia", "إكسيليفون (آلة موسيقية), زينون (غاز), زيروكس (نسخ), رهاب الأجانب", "X في بداية الكلمة = ز (كلمات نادرة من أصل يوناني)"],
["X (في ex-)", "كز", "exam, example, exact, exist", "امتحان, مثال, دقيق, يوجد", "X في ex- قبل حرف متحرك مشدد = كز/غز"],
["X (منتصف/نهاية)", "كس", "box, six, taxi, next, text", "صندوق, ستة, سيارة أجرة, التالي, نص", "X في باقي المواضع = كس"],
["S (بين متحركين)", "ز", "music, president, easy, visit, season, rose", "موسيقى, رئيس, سهل, زيارة, فصل, وردة", "S بين حرفين متحركين غالباً = ز"],
],
},

# ============================ NIVEAU 102 ============================
{
"num": 102, "cefr": "A2",
"category": "English Alphabet",
"category_ar": "أبجدية اللغة الإنجليزية من A إلى Z",
"title_en": "The English Alphabet — Letters & Names",
"title_ar": "الحروف الأبجدية الإنجليزية A–Z مع طريقة نطق اسمها",
"layout": "table",
"audio_col": 3,
"table_columns": ["الحرف", "الاسم بالإنجليزية", "النطق بالعربية", "مثال", "المعنى"],
"table_rows": [

["SECTION", "الحروف A إلى M"],

["Aa", "ey", "آي", "apple", "تفاحة"],
["Bb", "bee", "بي", "book", "كتاب"],
["Cc", "see", "سي", "cat", "قطة"],
["Dd", "dee", "دي", "dog", "كلب"],
["Ee", "ee", "إي", "egg", "بيضة"],
["Ff", "ef", "إف", "fish", "سمكة"],
["Gg", "jee", "جي", "go", "يذهب"],
["Hh", "eych", "إيتش", "hat", "قبعة"],
["Ii", "ay", "آي", "in", "في"],
["Jj", "jey", "جي", "jump", "يقفز"],
["Kk", "key", "كي", "key", "مفتاح"],
["Ll", "el", "إل", "like", "يحب"],
["Mm", "em", "إم", "man", "رجل"],

["SECTION", "الحروف N إلى Z"],

["Nn", "en", "إن", "no", "لا"],
["Oo", "ow", "أو", "on", "على"],
["Pp", "pee", "بي", "pen", "قلم"],
["Qq", "kyuo", "كيو", "quick", "سريع"],
["Rr", "aar", "آر", "red", "أحمر"],
["Ss", "es", "إس", "sun", "شمس"],
["Tt", "tee", "تي", "ten", "عشرة"],
["Uu", "yoo", "يو", "up", "فوق"],
["Vv", "vee", "في", "very", "جداً"],
["Ww", "dabalyoo", "دبليو", "water", "ماء"],
["Xx", "eks", "إكس", "box", "صندوق"],
["Yy", "way", "واي", "yes", "نعم"],
["Zz", "zee", "زد", "zoo", "حديقة حيوان"],
],
},

# ============================ NIVEAU 103 ============================
{
"num": 103, "cefr": "A2",
"category": "Vowel Sounds",
"category_ar": "أصوات الحروف المتحركة المفردة",
"title_en": "The Vowels A, E, I, O, U — Sound Rules",
"title_ar": "قواعد نطق الحروف المتحركة A–E–I–O–U (قصير وطويل)",
"layout": "table",
"audio_col": 3,
"table_columns": ["الحرف", "القاعدة", "النطق", "أمثلة بالإنجليزية", "المعنى", "ملاحظات"],
"table_rows": [

["SECTION", "حرف A"],

["A", "في كلمة من ثلاثة أحرف", "أ (فتحة قصيرة)", "bad, sad, rat, cat, hat, fat", "رديء, حزين, فأر, قطة, قبعة, سمين", "تُلفظ كالألف العادية في العربية"],
["A", "قبل LL أو LT أو LD", "أو o", "all, tall, call, ball, salt, bald", "كل, طويل, يدعو, كرة, ملح, أصلع", "A قبل L المكرر تتحول إلى صوت O"],
["A", "بين ساكنين ثم e نهائية", "إي (ey)", "name, came, gate, late, fate", "اسم, أتى, بوابة, متأخر, مصير", "E في النهاية صامتة لكنها تطوّل A"],
["A", "قبل i", "آي (ay)", "train, air, fair, hair", "قطار, هواء, جميل, شعر", "A مع I يُنطقان معاً"],
["A", "استثناء شاذ", "أ", "have", "يملك", "كلمة have تكسر القاعدة"],

["SECTION", "حرف E"],

["E", "في منتصف الكلمة", "إِ (فتحة)", "bed, red, pen, men, fed", "سرير, أحمر, قلم, رجال, أطعم", "شرط ألا يكون هناك حرف صوتي آخر"],
["E", "مكرر EE أو قبله A", "إي (ياء)", "see, tree, free, eat, meat, meet", "يرى, شجرة, حر, يأكل, لحم, يجتمع", "EE و EA = إي طويلة"],
["E", "EA في بعض الكلمات", "إِ (بين الفتح والكسر)", "head, bread, death, deaf", "رأس, خبز, موت, أصم", "مجموعة تُحفظ: تُلفظ إِ وليس إي"],

["SECTION", "حرف I"],

["I", "كسرة", "إِ (كسرة)", "is, it, in, pin, tin, sit, win", "يكون, هو, في, دبوس, صفيح, يجلس, يكسب", "اللفظ الطبيعي للحرف I"],
["I", "استثناء شاذ", "أَ", "girl, bird, first", "فتاة, عصفور, أول", "I بعد r تُلفظ أَ"],
["I", "بين ساكنين ثم e نهائية", "آي (ay)", "line, fine, mine, ride, time", "خط, جميل, خاصتي, يركب, وقت", "E في النهاية تطوّل I"],

["SECTION", "حرف O"],

["O", "قبل a أو w", "أو", "broad, board, low, flow", "عريض, لوح, منخفض, يتدفق", "O يُنطق منفصلاً"],
["O", "OW في بعض الكلمات", "أو (aw)", "town, brown, down, crown", "مدينة, بني, أسفل, تاج", "مثل down = داون"],
["O", "OW في كلمات أخرى", "أو طويل (ou)", "snow, show, yellow, window", "ثلج, يعرض, أصفر, نافذة", "مثل snow = سنو"],

["SECTION", "حرف U"],

["U", "أول الكلمة أو بين ساكنين", "أَ (فتحة)", "cut, but, up, rub, hut", "قطع, لكن, فوق, يفرك, كوخ", "تلفظ مفتوحة"],
["U", "قبل LL", "ضمة (u)", "full, pull", "مليء, يسحب", "L الثانية لا تُنطق"],
["U", "بعد O", "أو (aw)", "out, shout, loud, stout", "خارج, يصيح, عالٍ, بدين", "OU = أو"],

["SECTION", "حرف Y (كحرف صوتي)"],

["Y", "نهاية كلمة متعددة المقاطع", "إي", "happy, city, baby, story", "سعيد, مدينة, رضيع, قصة", "Y النهائية = إي"],
["Y", "نهاية كلمة قصيرة", "آي", "my, fly, try, sky, cry", "لي, يطير, يحاول, سماء, يبكي", "Y النهائية القصيرة = آي"],
["Y", "منتصف الكلمة", "إِ", "gym, myth, symbol, system", "ناد رياضي, أسطورة, رمز, نظام", "Y الوسطى تُنطق مثل I"],
],
},

# ============================ NIVEAU 104 ============================
{
"num": 104, "cefr": "A2",
"category": "Plural Rules",
"category_ar": "قواعد جمع الأسماء ونطق -s / -es",
"title_en": "Making Plurals & Pronouncing -s / -es",
"title_ar": "تكوين الجمع في الإنجليزية ونطق لاحقة الجمع s / es",
"layout": "table",
"audio_col": 3,
"table_columns": ["القاعدة", "التحويل", "النطق", "مثال مفرد ← جمع", "المعنى", "ملاحظات"],
"table_rows": [

["SECTION", "الجمع الشائع"],

["جمع عادي", "+ s", "س أو ز", "cat → cats, cup → cups, hat → hats, girl → girls", "قط, كوب, قبعة, بنت", "إضافة s في نهاية الكلمة"],
["نهايات o, x, ch, sh, s", "+ es", "إز", "dress → dresses, box → boxes, bus → buses, match → matches, potato → potatoes", "فستان, صندوق, حافلة, مباراة, بطاطس", "الكلمات المنتهية بـ o/x/ch/sh/s تُضاف لها es"],

["SECTION", "التحويلات الخاصة"],

["نهاية is", "is → es", "إز", "analysis → analyses, oasis → oases", "تحليل, واحة", "استبدال is بـ es"],
["نهاية f أو fe", "f/fe → ves", "فز", "thief → thieves, wife → wives, knife → knives", "لص, زوجة, سكين", "تحوّل f أو fe إلى ves"],
["نهاية y بعد ساكن", "y → ies", "إيز", "family → families, city → cities", "عائلة, مدينة", "y بعد حرف ساكن → ies"],
["نهاية y بعد متحرك", "+ s فقط", "ز", "donkey → donkeys, key → keys, day → days", "حمار, مفتاح, يوم", "y بعد حرف متحرك (a-e-i-o-u) تبقى + s"],

["SECTION", "نطق لاحقة الجمع"],

["بعد f, k, p, t", "s تُنطق س", "س", "roof → roofs, mark → marks, trip → trips, cat → cats", "سقف, علامة, رحلة, قطة", "s = س بعد الحروف المهموسة f/k/p/t"],
["مع باقي الحروف", "s تُنطق ز", "ز", "boy → boys, car → cars, tour → tours", "ولد, سيارة, جولة", "s = ز بعد الحروف المجهورة"],
["نهاية es", "es تُنطق إز", "إز", "box → boxes, bus → buses", "صندوق, حافلة", "es تُنطق إز دائماً"],

["SECTION", "جموع شاذة (تُحفظ)"],

["شاذ", "تغيّر جذري", "—", "man → men, woman → women, foot → feet, tooth → teeth, child → children, mouse → mice, louse → lice", "رجل, امرأة, قدم, سن, طفل, فأر, قملة", "كلمات لا تتبع قاعدة ثابتة"],
],
},

# ============================ NIVEAU 105 ============================
{
"num": 105, "cefr": "B1",
"category": "Silent Letters",
"category_ar": "الحروف الصامتة في الإنجليزية",
"title_en": "Silent Letters — Master the Invisible Sounds",
"title_ar": "الحروف التي لا تُنطق (Silent Letters) وقواعدها",
"layout": "table",
"audio_col": 2,
"table_columns": ["النمط", "القاعدة", "مثال بالإنجليزية", "المعنى", "ملاحظات"],
"table_rows": [

["SECTION", "حروف صامتة في بداية الكلمة"],

["KN", "K لا تُنطق قبل N", "knee, know, knife, knock", "ركبة, يعرف, سكين, يطرق", "K صامتة في البداية قبل N"],
["WR", "W لا تُنطق قبل R", "write, wrong, wrist, wrap, wreck", "يكتب, خطأ, معصم, يلف, حطام", "W صامتة قبل R في بداية الكلمة"],
["WH", "H لا تُنطق بعد W", "what, when, where, why, which", "ماذا, متى, أين, لماذا, أيّ", "H صامتة بعد W في أدوات الاستفهام"],
["PS", "P لا تُنطق قبل S", "psychology, psalm, pseudonym", "علم النفس, مزمور, اسم مستعار", "كلمات من أصل يوناني تبدأ بـ Ps"],
["Silent H", "H صامتة في بداية بعض الكلمات", "hour, honest, honor, heir", "ساعة, صادق, شرف, وريث", "من أصل فرنسي: H لا تُنطق"],

["SECTION", "حروف صامتة في وسط ونهاية الكلمة"],

["MB / BT", "B صامتة", "comb, lamb, thumb, climb, debt, doubt", "مشط, حمل, إبهام, يتسلق, دَين, شك", "B صامتة بعد M أو قبل T"],
["MN", "N صامتة", "autumn, column, condemn, hymn", "خريف, عمود, يدين, ترنيمة", "N صامتة بعد M في نهاية الكلمة"],
["LK / LF / LM", "L صامتة", "talk, walk, half, calm, could, should, would", "يتحدث, يمشي, نصف, هادئ, استطاع, يجب, سوف", "L صامتة قبل K/F/M وفي could/should/would"],
["GH", "GH صامتة", "light, night, right, high, through, eight, daughter", "ضوء, ليل, صحيح, مرتفع, عبر, ثمانية, ابنة", "GH صامتة بعد حرف متحرك"],
["ST", "T صامتة", "castle, listen, whistle, Christmas", "قلعة, يستمع, صافرة, عيد الميلاد", "T صامتة قبل -le"],
["PT", "P صامتة في PT", "prompt, receipt", "سريع/يحرّض, إيصال", "حالات نادرة تُحفظ"],

["SECTION", "حرف E الصامت و قواعد أخرى"],

["Silent E", "E في نهاية الكلمة صامتة لكنها تطوّل المتحرك", "cake, name, time, home, use, make, hope", "كعكة, اسم, وقت, منزل, يستعمل, يصنع, يأمل", "أشهر قاعدة: حرف متحرك + ساكن + e"],
["Silent E (قصيرة)", "E صامتة في بعض الكلمات النهائية", "plane, favourite, take, have", "طائرة, مفضل, يأخذ, يملك", "من الفيديوهات: e لا تُنطق في آخر الكلمة"],
["AUGHT / OUGHT", "UGH صامتة بين A و T", "taught, daughter, caught", "درّس, ابنة, أمسك", "UGH لا تُنطق في AUGHT و OUGHT"],
],
},
]