# -*- coding: utf-8 -*-
"""المستويات 1–10 : المبتدئ (A1) — أساسيات اللغة.""" 

LEVELS = [

# ============================ NIVEAU 1 ============================
{
"num": 1, "cefr": "A1",
"category": "Alphabet and Sounds",
"category_ar": "الحروف الأبجدية والأصوات",
"title_en": "The Alphabet, Letters and Sounds",
"title_ar": "الحروف الأبجدية والأصوات",
"ideas": [
{
"en": "The English alphabet has 26 letters",
"ar": "تحتوي الأبجدية الإنجليزية على 26 حرفاً",
"expl_ar": "الأبجدية الإنجليزية تتكون من 26 حرفاً، نبدأ بحرف A وننتهي بحرف Z.\nحفظ ترتيب هذه الحروف يساعدنا عندما نبحث في القاموس أو نكتب القوائم.",
"expl_en": "English has 26 letters, from A to Z. We memorize their order for the dictionary and for lists.",
"formula": "a b c d e f g h i j k l m n o p q r s t u v w x y z",
"examples": [
("A is the first letter.", "A هو أول حرف."),
("Z is the last letter.", "Z هو آخر حرف."),
("There are 26 letters in English.", "يوجد 26 حرفاً في الإنجليزية.")]},
{
"en": "Vowels: A, E, I, O, U",
"ar": "حروف العلة: A, E, I, O, U",
"expl_ar": "حروف العلة (Vowels) هي خمسة أحرف: A, E, I, O, U.\nبقية الحروف تسمى ساكنة (Consonants).\nكل كلمة إنجليزية تقريباً تحتوي على حرف علة واحد على الأقل.",
"expl_en": "The vowels are A, E, I, O and U. The other letters are consonants. Almost every word has a vowel.",
"formula": "Vowels = A, E, I, O, U",
"examples": [
("cat → a is a vowel.", "cat → حرف a علة."),
("dog → o is a vowel.", "dog → حرف o علة."),
("The vowels are A E I O U.", "حروف العلة هي A E I O U.")]},
{
"en": "Consonants",
"ar": "الحروف الساكنة",
"expl_ar": "الحروف الساكنة هي كل الحروف ما عدا حروف العلة: مثل B, C, D, F, G... وهي 21 حرفاً. معظم الحروف في الكلمة تكون ساكنة.",
"expl_en": "Consonants are the 21 non-vowel letters, like B, C, D, and F. Most letters in a word are consonants.",
"formula": "Consonants = 26 − 5 vowels = 21",
"examples": [
("B, C, D are consonants.", "B, C, D حروف ساكنة."),
("Yes begins with y (consonant).", "كلمة Yes تبدأ بحرف y الساكن."),
("Book has 4 letters and 4 sounds.", "كلمة Book فيها 4 حروف و4 أصوات.")]},
{
"en": "Capital letters and small letters",
"ar": "الحروف الكبيرة والحروف الصغيرة",
"expl_ar": "كل حرف له شكلان: كبير (CAPITAL) وصغير (small). نستعمل الحرف الكبير في بداية الجملة، ومع أسماء العلم (الأشخاص، المدن، الدول، الأيام، الشهور).",
"expl_en": "Each letter has a big (capital) and a small form. We use capital letters at the start of a sentence and for names.",
"formula": "Aa Bb Cc ... Zz  |  Start of sentence + names",
"examples": [
("My name is Oussama.", "اسمي أسامة."),
("We live in Algeria.", "نعيش في الجزائر."),
("Today is Sunday.", "اليوم هو الأحد.")]},
{
"en": "Spelling your name",
"ar": "تهجئة الاسم",
"expl_ar": "عندما نذكر اسمنا لشخص لا يعرفه، ننطق الحروف واحداً واحداً. هذا مفيد جداً عند ملء الاستمارات أو التحدث في الهاتف.",
"expl_en": "When we say our name to someone who does not know it, we say the letters one by one. This helps on the phone and in forms.",
"formula": "My name is ____ . It is spelled S-A-L-I-M.",
"examples": [
("How do you spell your name?", "كيف تهجئ اسمك؟"),
("M-A-D-A-N-I. That is my name.", "M-A-D-A-N-I. هذا هو اسمي."),
("Can you spell that, please?", "هل يمكنك تهجئة ذلك من فضلك؟")]},
{
"en": "Sounds: the alphabet vs phonics",
"ar": "أصوات الحروف: الاسم مقابل النطق",
"expl_ar": "لكل حرف «اسم» (مثل: bee لحرف B) وصوت مختلف في الكلمة (مثل: صوت /b/ في كلمة ball (كرة)).\nننتبه إلى أن بعض الحروف تنطق بصوت مختلف حسب الكلمة.",
"expl_en": "Each letter has a name (like 'bee' for B) and a sound (like /b/ in ball). The sound can change in different words.",
"formula": "Letter name ≠ letter sound",
"examples": [
("letter B: name /bee/, sound /b/.", "حرف B: اسمه بي، وصوته ب."),
("letter C can sound /k/ or /s/.", "حرف C قد ينطق ك أو س."),
("letter G can sound /g/ or /j/.", "حرف G قد ينطق ج أو جيم أخرى.")]},
{
"en": "Common letter pairs: ch, sh, th",
"ar": "أزواج حروف شائعة: ch, sh, th",
"expl_ar": "بعض الحروف تتجمع معاً لإنتاج صوت جديد. مثلاً ch تنطق «تش»، sh تنطق «ش»، وth لها نطقان: ذ أو ث.",
"expl_en": "Some letters work together to make a new sound. ch says 'ch' (chair), sh says 'sh' (ship), th says 'th' (three).",
"formula": "ch → /tʃ/ • sh → /ʃ/ • th → /θ/ or /ð/",
"examples": [
("Chair, cheese ← ch.", "كرسي، جبن ← ch."),
("Ship, fish ← sh.", "سفينة، سمك ← sh."),
("Three, this ← th.", "ثلاثة، هذا ← th.")]},
{
"en": "The letter Y is special",
"ar": "حرف Y حرف خاص",
"expl_ar": "حرف Y يمكن أن يكون ساكناً في بداية الكلمة (yes) أو علة في نهاية الكلمة مثل happy (سعيد) و fly (يطير).\nهذا يجعله حرفاً مميزاً.",
"expl_en": "Y is special: it is a consonant in 'yes' but a vowel in 'happy' and 'fly'.",
"formula": "Y = consonant (yes) or vowel (baby)",
"examples": [
("Yellow ← Y consonant.", "أصفر ← Y ساكن."),
("Happy ← y vowel sound.", "سعيد ← y علة."),
("My fly cry ← y as a vowel.", "في كلمات مثل fly وcry.")]},
{
"en": "Memorizing the alphabet order",
"ar": "حفظ ترتيب الحروف",
"expl_ar": "ترتيب الحروف مهم جداً في القواميس والهواتف والفهارس. نستعمل «الأغنية الأبجدية» لمساعدتنا على الحفظ. تكرار الترتيب يومياً يجعل الحفظ أسهل.",
"expl_en": "Alphabet order helps us in dictionaries and indexes. Singing the ABC song helps us memorize it.",
"formula": "A B C D / E F G / H I J K / L M N O P ...",
"examples": [
("The dictionary is in alphabet order.", "القاموس مرتب بالترتيب الأبجدي."),
("Apple comes before banana.", "Apple تأتي قبل banana."),
("Fruit comes before vegetable.", "Fruit قبل vegetable.")]},
{
"en": "Reading the alphabet in words",
"ar": "قراءة الحروف داخل الكلمات",
"expl_ar": "عند القراءة نقرأ الكلمة كلها كمقاطع، لا نقرأ كل حرف على حدة. مثلاً كلمة cat تقرأ في صوت واحد وليس c-a-t. هذا هو أساس القراءة الصحيحة.",
"expl_en": "When we read, we blend the letters into one word. We do not read c-a-t; we read 'cat'.",
"formula": "c + a + t → /kæt/",
"examples": [
("Dog → one sound /dɒg/.", "Dog تنطق كصوت واحد."),
("Sun → one sound /sʌn/.", "Sun تنطق كصوت واحد."),
("Blend the letters to read.", "امزج الحروف لتقرأ الكلمة.")]},
{
"en": "Nice, new sounds: the alphabet practice",
"ar": "تدريب عملي على الحروف",
"expl_ar": "أفضل طريقة لتعلم الحروف هي الممارسة: انطق كل حرف بصوت عالٍ، واكتبه، وابحث عن كلمات تبدأ به. كل دقيقة تدريب تقوّي ذاكرتك.",
"expl_en": "The best way to learn the alphabet is practice: say each letter aloud, write it, and find words that start with it.",
"formula": "Learn = say + write + find examples",
"examples": [
("A: apple, ant, arm.", "A: تفاحة، نملة، ذراع."),
("B: book, boy, box.", "B: كتاب، ولد، صندوق."),
("Practice five letters every day.", "درّب خمسة حروف كل يوم.")]},
{
"en": "Alphabet for classroom use",
"ar": "الأبجدية في القسم",
"expl_ar": "في القسم نستعمل الأبجدية كثيراً: لتهجئة الكلمات الجديدة، وللإشارة إلى الحروف، ولمعرفة أسماء الحروف بالضبط. انتبه إلى نطق الحروف بالطريقة الإنجليزية لا الفرنسية.",
"expl_en": "In class we use the alphabet to spell new words and to name letters. Pronounce letters the English way.",
"formula": "Q = /kjuː/ • W = /ˈdʌbəljuː/",
"examples": [
("How is that word spelled?", "كيف تُهجأ تلك الكلمة؟"),
("Spell 'house': H-O-U-S-E.", "هجِّئ كلمة house: H-O-U-S-E."),
("Say the letter H, please.", "انطق حرف H من فضلك.")]},
]},
# ============================ NIVEAU 2 ============================
{
"num": 2, "cefr": "A1",
"category": "Greetings and Politeness",
"category_ar": "التحية والمجاملة",
"title_en": "Greetings and Basic Expressions",
"title_ar": "التحية والتعابير الأساسية",
"ideas": [
{
"en": "Hello and Hi",
"ar": "مرحباً / أهلاً",
"expl_ar": "نستعمل Hello و Hi للتحية في أي وقت. Hello رسمية قليلاً، أما Hi فهي غير رسمية وللأصدقاء. كلاهما يعني «مرحباً».",
"expl_en": "We use 'Hello' and 'Hi' to greet people any time. 'Hello' is a little more formal; 'Hi' is friendly.",
"formula": "Hello! / Hi!",
"examples": [
("Hello, how are you?", "مرحباً، كيف حالك؟"),
("Hi, my name is Islem.", "أهلاً، اسمي إسلام."),
("Hello, nice to see you.", "مرحباً، سعيد برؤيتك.")]},
{
"en": "Good morning / afternoon / evening / night",
"ar": "صباح الخير / مساء الخير / ليلة سعيدة",
"expl_ar": "نختار التحية حسب وقت اليوم:\nGood morning (حتى الظهر)، Good afternoon (بعد الظهر)، Good evening (في المساء)، و Good night نقولها عند النوم أو الوداع ليلاً.",
"expl_en": "We choose the greeting by the time: Good morning (till noon), Good afternoon, Good evening, and Good night (to say goodbye at night).",
"formula": "Good morning (before 12) • Good afternoon (12–18) • Good evening (18–22) • Good night (sleep/leave)",
"examples": [
("Good morning, everyone!", "صباح الخير جميعاً!"),
("Good afternoon, teacher.", "مساء الخير أيها الأستاذ."),
("Good night, Mom.", "ليلة سعيدة يا أمي.")]},
{
"en": "How are you? — and answers",
"ar": "كيف حالك؟ — والجواب",
"expl_ar": "السؤال الشائع «كيف حالك؟». الأجوبة الشائعة: I am fine (أنا بخير)، I am good (أنا بخير)، Not bad (ليس سيئاً)، Very well (جيد جداً).\nأضف دائماً سؤال: And you? (وأنت؟) للمجاملة.",
"expl_en": "People often ask 'How are you?'. Common answers: I am fine, I am good, Not bad, Very well. Add 'And you?' to be polite.",
"formula": "How are you? → I am fine / good / not bad, and you?",
"examples": [
("How are you today?", "كيف حالك اليوم؟"),
("I am fine, thank you. And you?", "أنا بخير شكراً. وأنت؟"),
("I am very well, thanks.", "أنا بخير جداً، شكراً.")]},
{
"en": "Introducing yourself: I am ...",
"ar": "التعريف بالنفس: أنا ...",
"expl_ar": "لتعريف نفسك قل: My name is ... (اسمي هو ...) أو I am ... (أنا ...). يمكنك إضافة عمرك وسكنك وبلدك.",
"expl_en": "To introduce yourself say: My name is ... or I am .... You can add your age, your town and your country.",
"formula": "My name is ____. | I am ____ years old. | I am from ____.",
"examples": [
("My name is Anes.", "اسمي أنس."),
("I am ten years old.", "عمري عشر سنوات."),
("I am from Oran, Algeria.", "أنا من وهران، الجزائر.")]},
{
"en": "Introducing others: This is ...",
"ar": "التعريف بالآخرين: هذا/هذه ...",
"expl_ar": "لتقديم شخص لشخص آخر نقول: This is my friend (هذا صديقي) أو This is my teacher (هذه أستاذتي). نستعمل This is مع شخص قريب منا.",
"expl_en": "To introduce someone, say: This is my friend / my teacher / my mother.",
"formula": "This is my ____.",
"examples": [
("This is my brother Oussama.", "هذا أخي أسامة."),
("This is my mother.", "هذه أمي."),
("This is our teacher.", "هذا أستاذنا.")]},
{
"en": "Nice to meet you",
"ar": "تشرفت بلقائك",
"expl_ar": "عندما يتعرف شخصان لأول مرة، يقول أحدهما: Nice to meet you (تشرفت بلقائك)، والآخر يجيب: Nice to meet you too (وأنا أيضاً).",
"expl_en": "When people meet for the first time, one says 'Nice to meet you' and the other answers 'Nice to meet you too'.",
"formula": "Nice to meet you! → Nice to meet you too!",
"examples": [
("Nice to meet you, Sir.", "تشرفت بلقائك سيدي."),
("Nice to meet you too.", "وأنا أيضاً تشرفت."),
("It is a pleasure to meet you.", "من دواعي سروري لقاؤك.")]},
{
"en": "Thank you and You are welcome",
"ar": "شكراً وعلى الرحب",
"expl_ar": "نقول Thank you (شكراً) أو Thanks عندما نشكر، والجواب الشائع: You are welcome (على الرحب والسعة) أو No problem (لا مشكلة) أو My pleasure (بكل سرور).",
"expl_en": "We say 'Thank you' or 'Thanks' to say thanks. Answers: 'You are welcome', 'No problem', 'My pleasure'.",
"formula": "Thank you → You are welcome / No problem",
"examples": [
("Thank you very much.", "شكراً جزيلاً."),
("You are welcome.", "على الرحب والسعة."),
("Thanks for your help.", "شكراً لمساعدتك.")]},
{
"en": "Please — the magic word",
"ar": "من فضلك — الكلمة السحرية",
"expl_ar": "كلمة Please (من فضلك) تجعل الطلب مهذباً. نضعها في نهاية الجملة.\nمثال: Can I have some water, please?\nمن يستعمل Please يتحدث بأدب والجميع يحترمه.",
"expl_en": "'Please' makes a request polite. Put it at the end of the sentence.",
"formula": "Can I + verb, please?",
"examples": [
("Can I open the window, please?", "هل يمكنني فتح النافذة من فضلك؟"),
("A cup of tea, please.", "فنجان شاي من فضلك."),
("Please, sit down.", "اجلس من فضلك.")]},
{
"en": "Excuse me / Sorry",
"ar": "المعذرة / آسف",
"expl_ar": "نقول Excuse me (المعذرة/بإذنكم) قبل طلب مساعدة أو عند المرور، و Sorry (آسف) بعد الخطأ أو عند الاعتذار.",
"expl_en": "'Excuse me' is for asking help or passing. 'Sorry' is for apologizing after a mistake.",
"formula": "Excuse me + request | Sorry + apology",
"examples": [
("Excuse me, where is the station?", "المعذرة، أين المحطة؟"),
("Sorry, I am late.", "آسف، لقد تأخرت."),
("Excuse me, can you help me?", "المعذرة، هل يمكنك مساعدتي؟")]},
{
"en": "Goodbye and Bye",
"ar": "إلى اللقاء / وداعاً",
"expl_ar": "عند الوداع نقول Goodbye أو Bye أو See you later (أراك لاحقاً) أو See you tomorrow (أراك غداً). إضافة اسم الشخص تجعلها ألطف: Bye, Sam!",
"expl_en": "To say goodbye: Goodbye, Bye, See you later, See you tomorrow.",
"formula": "Goodbye! / See you later! / Bye!",
"examples": [
("Goodbye, sir.", "وداعاً سيدي."),
("See you tomorrow!", "أراك غداً!"),
("Bye, see you later!", "وداعاً، أراك لاحقاً!")]},
{
"en": "Classroom expressions",
"ar": "عبارات القسم",
"expl_ar": "عبارات مفيدة في القسم: Open your books (افتحوا كتبكم)، Close the door (أغلق الباب)، I have a question (لدي سؤال)، Repeat, please (أعد من فضلك)، I do not understand (لا أفهم).",
"expl_en": "Useful classroom phrases: Open your books, Close the door, I have a question, Repeat please, I do not understand.",
"formula": "Come in • Sit down • Listen • Repeat • Write",
"examples": [
("Open your books, please.", "افتحوا كتبكم من فضلك."),
("I have a question.", "لدي سؤال."),
("Repeat after me.", "كرروا بعدي.")]},
]
},
# ============================ NIVEAU 3 ============================
{
"num": 3, "cefr": "A1",
"category": "Pronouns and To Be",
"category_ar": "الضمائر وفعل الكينونة",
"title_en": "Subject Pronouns and the Verb To Be",
"title_ar": "ضمائر الفاعل وفعل الكينونة (am, is, are)",
"ideas": [
{
"en": "Subject pronouns",
"ar": "ضمائر الفاعل",
"expl_ar": "ضمائر الفاعل هي التي تقوم بالفعل: I (أنا)، You (أنت)، He (هو)، She (هي)، It (هو/هي لغير العاقل)، We (نحن)، They (هم). نستعملها قبل الفعل في الجملة.",
"expl_en": "Subject pronouns do the action: I, you, he, she, it, we, they. They come before the verb.",
"formula": "I • you • he • she • it • we • they",
"examples": [
("I am a student.", "أنا طالب."),
("She is my sister.", "هي أختي."),
("They are happy.", "هم سعداء.")]},
{
"en": "To be: am, is, are",
"ar": "فعل الكينونة: am, is, are",
"expl_ar": "فعل To be معناه «يكون / هو».\nله ثلاثة أشكال في الحاضر: am مع I، is مع he/she/it أو اسم مفرد، و are مع you/we/they أو اسم جمع.",
"expl_en": "'To be' means to exist. Its present forms are am (with I), is (with he, she, it, singular), are (with you, we, they, plural).",
"formula": "I am • he/she/it is • you/we/they are",
"examples": [
("I am happy.", "أنا سعيد."),
("He is a doctor.", "هو طبيب."),
("They are teachers.", "هم معلمون.")]},
{
"en": "Contractions: I'm, you're, he's...",
"ar": "الاختصارات: I'm, you're, he's...",
"expl_ar": "في الكلام اليومي نختصر الفعل مع الضمير: I am ← I'm، you are ← you're، he is ← he's، we are ← we're، they are ← they're. النطق يصبح أسرع وأسهل.",
"expl_en": "In speaking we join pronoun + verb: I'm, you're, he's, she's, it's, we're, they're.",
"formula": "I am = I'm • you are = you're • he is = he's",
"examples": [
("I'm fine, thanks.", "أنا بخير شكراً."),
("You're very kind.", "أنت لطيف جداً."),
("She's my friend.", "هي صديقتي.")]},
{
"en": "Negative with to be",
"ar": "النفي مع فعل الكينونة",
"expl_ar": "للنفي نضيف not بعد الفعل: is not، are not، am not.\nالاختصارات الشائعة: isn't لـ is not، aren't لـ are not.\nلاحظ أننا لا نختصر am not في الإنجليزية القياسية إلا في السؤال (aren't I).",
"expl_en": "For the negative, add 'not' after the verb: is not, are not. Short forms: isn't, aren't.",
"formula": "am/is/are + not",
"examples": [
("It is not cold.", "الجو ليس باردا."),
("They aren't at home.", "هم ليسوا في المنزل."),
("I am not tired.", "أنا لست متعبا.")]},
{
"en": "Questions with to be",
"ar": "السؤال مع فعل الكينونة",
"expl_ar": "لجعل الجملة سؤالاً، نضع الفعل قبل الفاعل: You are → Are you? الفعل (am/is/are) في البداية يرفع نبرة السؤال.",
"expl_en": "To make a question, put the verb first: Are you? Is he?",
"formula": "Am/Is/Are + subject + rest ?",
"examples": [
("Are you ready?", "هل أنت مستعد؟"),
("Is he your brother?", "هل هو أخوك؟"),
("Are they English teachers?", "هل هم أساتذة إنجليزية؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "عند السؤال بـ Yes/No نجيب بإيجاز: Yes, I am. أو No, he isn't.\nنكرر الضمير مع فعل to be، ولا نستعمل الاختصار في الجواب الإيجابي القصير (لا نقول Yes, I'm).",
"expl_en": "Answer Yes/No questions briefly: Yes, I am. No, he isn't. We do not use a contraction in a short Yes answer.",
"formula": "Yes, + pronoun + am/is/are | No, + pronoun + am/is/are + not",
"examples": [
("Are you a pupil? Yes, I am.", "هل أنت تلميذ؟ نعم."),
("Is she at school? No, she isn't.", "هل هي في المدرسة؟ لا."),
("Are they here? Yes, they are.", "هل هم هنا؟ نعم.")]},
{
"en": "It is ... — special uses",
"ar": "استعمالات خاصة لـ It is",
"expl_ar": "نستعمل It مثلاً للزمن والطقس والأشياء: It is a book (إنه كتاب)، It is sunny (الجو مشمس)، It is seven o'clock (إنها الساعة السابعة).",
"expl_en": "We use 'it' for weather, time and things: It's a book, It's sunny, It's seven o'clock.",
"formula": "It is + noun / weather / time",
"examples": [
("It is raining now.", "إنها تمطر الآن."),
("It is six o'clock.", "إنها الساعة السادسة."),
("It is a beautiful day.", "إنه يوم جميل.")]},
{
"en": "To be + feelings and states",
"ar": "فعل الكينونة مع المشاعر والحالات",
"expl_ar": "نصف المشاعر والحالة بالصفة بعد الفعل: happy (سعيد)، sad (حزين)، hungry (جائع)، thirsty (عطشان)، cold (بارد)، hot (حار)، tired (متعب).\nالمثال: He is thirsty (هو عطشان).",
"expl_en": "Describe feelings with to be + adjective: happy, sad, hungry, thirsty, tired.",
"formula": "Subject + am/is/are + adjective (happy, sad...)",
"examples": [
("I am hungry.", "أنا جائع."),
("She is thirsty.", "هي عطشانة."),
("We are tired.", "نحن متعبون.")]},
{
"en": "To be + nationality and place",
"ar": "فعل الكينونة مع الجنسية والمكان",
"expl_ar": "نقول الجنسية أو المكان بعد الفعل: I am Algerian (أنا جزائري)، He is from France (هو من فرنسا)، They are in the classroom (هم في القسم).",
"expl_en": "Use to be with nationalities and places: I am Algerian, He is from France, They are in class.",
"formula": "Subject + be + nationality | be + in/from + place",
"examples": [
("We are Algerians.", "نحن جزائريون."),
("She is from Tunisia.", "هي من تونس."),
("The bag is on the table.", "الحقيبة على الطاولة.")]},
{
"en": "Who is it? What is it?",
"ar": "من هذا؟ ما هذا؟",
"expl_ar": "نستعمل Who مع الأشخاص (Who is he? من هو؟) و What مع الأشياء (What is this? ما هذا؟).\nالجواب يبدأ بـ It is ... أو He/She is ... .",
"expl_en": "'Who' is for people and 'What' is for things.",
"formula": "Who is he? → He is my father. | What is this? → It is a pen.",
"examples": [
("Who is that man?", "من هذا الرجل؟"),
("What is that?", "ما ذلك؟"),
("It is a mobile phone.", "إنه هاتف نقال.")]},
]
},
# ============================ NIVEAU 4 ============================
{
"num": 4, "cefr": "A1",
"category": "Articles",
"category_ar": "أدوات التعريف والتنكير",
"title_en": "Articles: a, an, the",
"title_ar": "أدوات النكرة والمعرفة: a, an, the",
"ideas": [
{
"en": "What is an article?",
"ar": "ما هي أداة التعريف والتنكير؟",
"expl_ar": "الأداة كلمة صغيرة تأتي قبل الاسم. هناك أداتان للنكرة: a و an، وأداة واحدة للمعرفة: the. مثال: a book (كتاب ما)، the book (الكتاب المعيَّن).",
"expl_en": "An article is a small word before a noun. 'a/an' = non-specific, 'the' = specific.",
"formula": "a / an + singular noun | the + any noun",
"examples": [
("I have a cat.", "لدي قط."),
("The cat is black.", "القط أسود."),
("Give me a pen, please.", "أعطني قلما من فضلك.")]},
{
"en": "a vs an",
"ar": "الفرق بين a و an",
"expl_ar": "نستعمل a قبل الكلمة التي تبدأ بصوت ساكن (a book، a car)، و an قبل الكلمة التي تبدأ بصوت علة (an apple، an hour). النطق هو المهم لا الكتابة.",
"expl_en": "Use 'a' before consonant sounds (a book) and 'an' before vowel sounds (an apple). Sound matters, not spelling.",
"formula": "a + consonant sound | an + vowel sound",
"examples": [
("an apple", "تفاحة."),
("an hour (h silent)", "ساعة (حرف h لا ينطق)."),
("a university (y sound)", "جامعة (صوت y ساكن).")]},
{
"en": "When we use 'the'",
"ar": "متى نستعمل the",
"expl_ar": "نستعمل the عندما يعرف المتكلم والمستمع الشيء المقصود بدقة: الشيء الوحيد (the sun الشمس)، الشيء المذكور سابقاً، أو الشيء المعروف في السياق.",
"expl_en": "We use 'the' when everyone knows which thing we mean: the sun, the moon, or something already mentioned.",
"formula": "the + specific/near/unique thing",
"examples": [
("The sun is hot.", "الشمس حارة."),
("Close the door, please.", "أغلق الباب من فضلك."),
("I read a book. The book was good.", "قرأت كتابا. كان الكتاب جيدا.")]},
{
"en": "First mention: a, second mention: the",
"ar": "الذكر الأول بـ a والثاني بـ the",
"expl_ar": "عندما نذكر شيئاً لأول مرة نستعمل a، وعندما نعيد ذكره نستعمل the لأنه أصبح معروفاً للمستمع.",
"expl_en": "First time we say 'a'; second time we say 'the' because we both know it now.",
"formula": "a + noun ... then ... the + noun",
"examples": [
("I saw a dog. The dog was brown.", "رأيت كلبا. كان الكلب بنيا."),
("She bought a dress. The dress is red.", "اشترت فستانا. الفستان أحمر."),
("There is a cat on the roof. The cat is sleeping.", "هناك قط على السطح. القط نائم.")]},
{
"en": "Jobs with a/an",
"ar": "المهن مع a / an",
"expl_ar": "عند ذكر المهنة بعد فعل to be نستعمل دائماً أداة النكرة: He is a doctor (هو طبيب)، She is an engineer (هي مهندسة). لا نقول He is doctor.",
"expl_en": "Always use a/an with jobs after to be: He is a doctor. NOT 'He is doctor'.",
"formula": "Subject + be + a/an + job",
"examples": [
("My father is a farmer.", "أبي فلاح."),
("She is an engineer.", "هي مهندسة."),
("I want to be a teacher.", "أريد أن أصبح معلما.")]},
{
"en": "When we do NOT use an article",
"ar": "متى لا نستعمل أداة",
"expl_ar": "لا نستعمل أداة قبل الجموع العامة (Cats are animals) أو الأسماء غير المعدودة العامة (Water is life).\nولا نستعملها قبل البلدان والقارات (Algeria، Africa) أو الأيام والشهور (Sunday، January).",
"expl_en": "No article with general plurals, general uncountables, countries, continents, days and months.",
"formula": "no article + general plural/noun + time names",
"examples": [
("Cats like milk.", "القطط تحب الحليب."),
("I live in Algeria.", "أعيش في الجزائر."),
("We eat breakfast on Friday.", "نتناول الفطور يوم الجمعة.")]},
{
"en": "a/an for one unit",
"ar": "a / an بمعنى «واحدة»",
"expl_ar": "a و an تعنيان «واحد/واحدة» كالرقم one: a week (أسبوع واحد)، an hour (ساعة واحدة)، a hundred (مئة).",
"expl_en": "'a' and 'an' can mean 'one': a week (one week), a hundred (one hundred).",
"formula": "a/an = one unit",
"examples": [
("I sleep eight hours a night.", "أنام ثماني ساعات في الليلة."),
("He visits us once a month.", "يزورنا مرة في الشهر."),
("A hundred years = a century.", "مئة سنة = قرن.")]},
{
"en": "'The' with unique things",
"ar": "the مع الأشياء الوحيدة",
"expl_ar": "الأشياء الوحيدة في الوجود تأخذ the دائماً: the sun (الشمس)، the moon (القمر)، the sky (السماء)، the sea (البحر)، the earth (الأرض).\nلأنه لا يوجد سوى واحدة فلا حاجة للسؤال عنها.",
"expl_en": "For unique things we use 'the': the sun, the moon, the sky, the sea.",
"formula": "the + sun/moon/sky/world/sea/earth",
"examples": [
("The sky is blue.", "السماء زرقاء."),
("The sea is deep.", "البحر عميق."),
("The world is big.", "العالم كبير.")]},
{
"en": "Examples with a, an, the",
"ar": "أمثلة مقارنة",
"expl_ar": "قارن: I bought a phone (لم نعرفه بعد)،\nThe phone is new (نعرفه الآن).\na للجديد والمجهول،\nthe للمعلوم والخاص.",
"expl_en": "Compare: 'a phone' (new, unknown) → 'the phone' (now known to all).",
"formula": "a/an = general • the = specific",
"examples": [
("Give me a glass.", "أعطني كأسا (أيا كان)."),
("Give me the glass.", "أعطني الكأس (المعينة)."),
("He drives a car. The car is white.", "يسوق سيارة. السيارة بيضاء.")]},
{
"en": "'The' with names of places (orientations)",
"ar": "the مع أسماء الأماكن والجهات",
"expl_ar": "نستعمل the مع أسماء البحار والمحيطات والأنهار والجهات: the Mediterranean، the Nile، the north (الشمال).\nولا نستعملها عموماً مع أسماء المدن والدول.",
"expl_en": "We use 'the' with seas, oceans, rivers and directions: the Nile, the north. Not with city/country names.",
"formula": "the + Nile/Mountains/East | no article + cities/countries",
"examples": [
("The Nile is in Egypt.", "نهر النيل في مصر."),
("Algeria is in the north of Africa.", "الجزائر في شمال إفريقيا."),
("The Sahara is very hot.", "الصحراء الكبرى حارة جدا.")]},
]
},
# ============================ NIVEAU 5 ============================
{
"num": 5, "cefr": "A1",
"category": "Plural Nouns",
"category_ar": "جمع الأسماء",
"title_en": "Plural Nouns",
"title_ar": "جمع الأسماء",
"ideas": [
{
"en": "Regular plural: + s",
"ar": "الجمع المنتظم: إضافة s",
"expl_ar": "معظم الأسماء تتحول إلى جمع بإضافة s في النهاية: book → books (كتاب/كتب)، pen → pens (قلم/أقلام)، car → cars (سيارة/سيارات).",
"expl_en": "Most nouns form the plural by adding 's': book → books, pen → pens.",
"formula": "noun + s",
"examples": [
("one book → three books", "كتاب واحد ← ثلاثة كتب."),
("two pens, five doors", "قلمان، خمسة أبواب."),
("Cats are nice pets.", "القطط حيوانات أليفة لطيفة.")]},
{
"en": "Plural with + es: s, ss, ch, sh, x, o",
"ar": "الجمع بإضافة es",
"expl_ar": "إذا انتهى الاسم بـ s أو ss أو ch أو sh أو x أو o، نضيف es: bus → buses، box → boxes، watch → watches، dish → dishes.",
"expl_en": "Add 'es' after s, ss, ch, sh, x, o endings: bus → buses, box → boxes.",
"formula": "noun ending in s/ss/ch/sh/x/o + es",
"examples": [
("bus → buses", "حافلة ← حافلات."),
("box → boxes", "صندوق ← صناديق."),
("watch → watches", "ساعة يد ← ساعات.")]},
{
"en": "Nouns ending in -y",
"ar": "الأسماء المنتهية بـ y",
"expl_ar": "إذا كان قبل y حرفا ساكنا، نحول y إلى ies: baby → babies (رضيع/أطفال)، city → cities (مدينة/مدن).\nأما إذا كان قبل y حرف علة فنضيف s فقط: boy → boys، day → days.",
"expl_en": "Consonant + y → ies (baby→babies). Vowel + y → add s (boy→boys).",
"formula": "consonant+y → ies | vowel+y → ys",
"examples": [
("baby → babies", "رضيع ← أطفال."),
("city → cities", "مدينة ← مدن."),
("boy → boys", "ولد ← أولاد.")]},
{
"en": "Nouns ending in -f / -fe",
"ar": "الأسماء المنتهية بـ f أو fe",
"expl_ar": "بعض الأسماء المنتهية بـ f/fe تحول إلى ves: leaf → leaves (ورقة/أوراق)، knife → knives (سكين/سكاكين)، life → lives (حياة/حياة).\nانتبه: بعضها يأخذ s فقط مثل roof → roofs.",
"expl_en": "Some -f/-fe nouns change to -ves: leaf→leaves, knife→knives. But some just add s: roof→roofs.",
"formula": "mostly f/fe → ves",
"examples": [
("leaf → leaves", "ورقة ← أوراق."),
("knife → knives", "سكين ← سكاكين."),
("roof → roofs", "سطح ← أسطح.")]},
{
"en": "Irregular plurals",
"ar": "الجموع الشاذة",
"expl_ar": "هناك أسماء لا تتبع القاعدة وتتغير تماماً في الجمع: man → men (رجل/رجال)، woman → women (امرأة/نساء)، child → children (طفل/أطفال)، tooth → teeth (سن/أسنان)، foot → feet (قدم/أقدام).",
"expl_en": "Some plurals are irregular: man→men, woman→women, child→children, tooth→teeth, foot→feet.",
"formula": "man→men • woman→women • child→children • tooth→teeth • foot→feet",
"examples": [
("One man, two men.", "رجل واحد، رجلان."),
("My children are at school.", "أطفالي في المدرسة."),
("Brush your teeth every day.", "نظف أسنانك كل يوم.")]},
{
"en": "Plurals with the same form",
"ar": "أسماء لا تتغير في الجمع",
"expl_ar": "بعض الأسماء تبقى كما هي في المفرد والجمع: sheep (خروف/خراف)، fish (سمكة/سمك)، deer (غزال/غزلان).\nنقول one sheep و two sheep.",
"expl_en": "Some nouns keep the same form: sheep, fish, deer. One sheep, two sheep.",
"formula": "singular = plural (sheep, fish, deer)",
"examples": [
("I see three sheep.", "أرى ثلاثة خراف."),
("There are many fish in the sea.", "هناك سمك كثير في البحر."),
("Deer live in the forest.", "تعيش الغزلان في الغابة.")]},
{
"en": "Plurals ending in -o",
"ar": "الجمع للأسماء المنتهية بـ o",
"expl_ar": "معظم الأسماء المنتهية بـ o تأخذ es: potato → potatoes (بطاطا)، tomato → tomatoes (طماطم)، hero → heroes.\nلكن كلمات مختصرة تأخذ s فقط: photo → photos، piano → pianos، radio → radios.",
"expl_en": "Most -o nouns take es (potatoes, tomatoes). Shortened words take s (photos, pianos, radios).",
"formula": "tomato→tomatoes | photo→photos",
"examples": [
("tomato → tomatoes", "طماطم ← طماطم."),
("photo → photos", "صورة ← صور."),
("potato → potatoes", "بطاطا ← بطاطا.")]},
{
"en": "Plural of countable words with names",
"ar": "جمع الأسماء مع أدوات أخرى",
"expl_ar": "بعد الجمع نستعمل أرقاما وتعبيرات عد: two books، three children، many pens.\nيبقى الاسم الجمع دائما بدون أداة a (لا نقول a books).",
"expl_en": "Plurals go with numbers and 'many': two books, many pens. Never use 'a' with a plural.",
"formula": "number/many + plural noun",
"examples": [
("four books", "أربعة كتب."),
("many students", "طلاب كثيرون."),
("few cars", "سيارات قليلة.")]},
{
"en": "Only plural nouns",
"ar": "أسماء تستعمل في الجمع فقط",
"expl_ar": "بعض الأشياء المزدوجة تستعمل بالجمع فقط: glasses (نظارة)، trousers (سروال)، scissors (مقص)، jeans (جينز). نقول these glasses (هذه هي).",
"expl_en": "Some things come in pairs and stay plural: glasses, trousers, scissors, jeans.",
"formula": "these/my + plural pair words",
"examples": [
("Where are my glasses?", "أين نظارتي؟"),
("These trousers are new.", "هذا السروال جديد."),
("The scissors are on the desk.", "المقص على المكتب.")]},
{
"en": "Make plurals: quick practice",
"ar": "تمرين سريع على الجمع",
"expl_ar": "أعد جدول الجمع لكل كلمة جديدة تتعلمها: ضع قبلها a/an إن أمكن، ثم حولها إلى الجمع.\nراجع اليوم القواعد الخمس الرئيسية: s، es، ies، ves، والشاذة.",
"expl_en": "For every new noun, practise: singular with a/an, then the plural. Check the 5 rules: s, es, ies, ves, irregular.",
"formula": "rule 1: +s • rule 2: +es • rule 3: y→ies • rule 4: f→ves • rule 5: irregular",
"examples": [
("a house → houses", "بيت ← بيوت."),
("a cherry → cherries", "كرزة ← كرز."),
("a wolf → wolves", "ذئب ← ذئاب.")]},
]
},
# ============================ NIVEAU 6 ============================
{
"num": 6, "cefr": "A1",
"category": "Demonstratives",
"category_ar": "أسماء الإشارة",
"title_en": "This, That, These, Those",
"title_ar": "أسماء الإشارة: هذا، تلك، هؤلاء، أولئك",
"ideas": [
{
"en": "This = here, one thing",
"ar": "This للمفرد القريب",
"expl_ar": "نستعمل This للإشارة إلى شيء واحد قريب منا: this book (هذا الكتاب)، this pen (هذا القلم). ننطقها بصوت /ض/ مفخم.",
"expl_en": "Use 'this' for one thing near you: this book, this pen.",
"formula": "this + singular noun (near)",
"examples": [
("This is my phone.", "هذا هاتفي."),
("This book is interesting.", "هذا الكتاب ممتع."),
("Take this bag.", "خذ هذه الحقيبة.")]},
{
"en": "That = there, one thing",
"ar": "That للمفرد البعيد",
"expl_ar": "نستعمل That للإشارة إلى شيء واحد بعيد عنا: that car (تلك السيارة)، that house (ذلك البيت).",
"expl_en": "Use 'that' for one thing far from you: that car, that house.",
"formula": "that + singular noun (far)",
"examples": [
("That is my school.", "تلك مدرستي."),
("Look at that mountain.", "انظر إلى ذلك الجبل."),
("That man is my uncle.", "ذلك الرجل عمي.")]},
{
"en": "These = here, many things",
"ar": "These للجمع القريب",
"expl_ar": "نستعمل These مع أشياء قريبة متعددة: these flowers (هذه الأزهار)، these shoes (هذه الأحذية).",
"expl_en": "Use 'these' for many things near you: these flowers, these shoes.",
"formula": "these + plural noun (near)",
"examples": [
("These are my keys.", "هذه مفاتيحي."),
("These apples are sweet.", "هذه التفاحات حلوة."),
("I like these pictures.", "أحب هذه الصور.")]},
{
"en": "Those = there, many things",
"ar": "Those للجمع البعيد",
"expl_ar": "نستعمل Those مع أشياء بعيدة متعددة: those children (أولئك الأطفال)، those trees (تلك الأشجار).",
"expl_en": "Use 'those' for many things far away: those children, those trees.",
"formula": "those + plural noun (far)",
"examples": [
("Those birds are flying.", "تلك الطيور تحلق."),
("Who are those people?", "من أولئك الناس؟"),
("Those are my neighbours.", "أولئك هم جيراني.")]},
{
"en": "Making questions: Is this...? Are these...?",
"ar": "السؤال: هل هذا...؟ هل هذه...؟",
"expl_ar": "نكون السؤال بقلب الفعل: This is → Is this? (هل هذا...؟)، These are → Are these? (هل هذه...؟) مع that: Is that? ومع those: Are those?",
"expl_en": "Questions: Is this...? Is that...? Are these...? Are those...?",
"formula": "Is this/that + noun? | Are these/those + noun?",
"examples": [
("Is this your book?", "هل هذا كتابك؟"),
("Are these your pens?", "هل هذه أقلامك؟"),
("Are those your friends?", "هل أولئك أصدقاؤك؟")]},
{
"en": "Short answers with is/are",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, it is. / No, it is not. أو Yes, they are. / No, they are not.\nنستعمل it مع المفرد و they مع الجمع حتى لو كانت الإشارة بـ this أو that.",
"expl_en": "Yes/No answers: Yes, it is. No, it isn't. Yes, they are. No, they aren't.",
"formula": "Yes, it is. | No, they aren't.",
"examples": [
("Are these your keys? Yes, they are.", "هل هذه مفاتيحك؟ نعم."),
("Is that your school? No, it isn't.", "هل تلك مدرستك؟ لا."),
("Are those new? Yes, they are.", "هل أولئك/تلك جديدة؟ نعم.")]},
{
"en": "This is + introducing people",
"ar": "This is للتعريف بالأشخاص",
"expl_ar": "عند تقديم شخص أمامنا نقول: This is my friend (هذا صديقي). وبالنسبة للجمع: These are my friends (هؤلاء أصدقائي).",
"expl_en": "To introduce people: This is my friend. These are my friends.",
"formula": "This is + person | These are + people",
"examples": [
("This is my mother.", "هذه أمي."),
("These are my brothers.", "هؤلاء إخوتي."),
("This is my teacher.", "هذا أستاذي.")]},
{
"en": "On the phone: This is ...",
"ar": "في الهاتف: This is ...",
"expl_ar": "في الهاتف نقدّم أنفسنا بـ This is ... (معي...). مثال: Hello, this is Islem (مرحباً، معي إسلام).\nأما في المقابلة وجها لوجه فنقول I am أو My name is.",
"expl_en": "On the phone we say 'This is...'. Face to face we say 'I am' or 'My name is'.",
"formula": "Hello, this is + name.",
"examples": [
("Hello, this is Anes.", "مرحبا، معي أنس."),
("Is this the manager?", "هل هذا هو المدير؟"),
("This is Dr. Belacel speaking.", "معي الأستاذ بلا عسل.")]},
{
"en": "These/those + be + adjective",
"ar": "هذه/تلك + فعل الكينونة + صفة",
"expl_ar": "نصف الأشياء بعد أسماء الإشارة: This book is heavy (ثقيل)، These shoes are old (قديمة)، Those clouds are dark (داكنة).\nالصفة تأتي بعد الفعل.",
"expl_en": "Describe after the demonstrative: This book is heavy. These shoes are old.",
"formula": "This/That + noun + is + adjective | These/Those + noun + are + adjective",
"examples": [
("This soup is hot.", "هذا الحساء ساخن."),
("Those mountains are high.", "تلك الجبال عالية."),
("These shoes are comfortable.", "هذه الأحذية مريحة.")]},
{
"en": "Practice: choose this/that/these/those",
"ar": "تمرين: اختر أداة الإشارة الصحيحة",
"expl_ar": "القاعدة: قريب مفرد ← this، بعيد مفرد ← that، قريب جمع ← these، بعيد جمع ← those. ألق نظرة على بعد الشيء وعدده ثم اختر.",
"expl_en": "Rule: near+one=this, far+one=that, near+many=these, far+many=those.",
"formula": "this (near,sing) • that (far,sing) • these (near,plur) • those (far,plur)",
"examples": [
("This bag is mine.", "هذه الحقيبة لي."),
("Those stars are far away.", "تلك النجوم بعيدة."),
("These children are happy.", "هؤلاء الأطفال سعداء.")]},
]
},
# ============================ NIVEAU 7 ============================
{
"num": 7, "cefr": "A1",
"category": "Possessives",
"category_ar": "الملكية",
"title_en": "Possessive Adjectives and 's",
"title_ar": "صفات الملكية وإضافة الملكية 's",
"ideas": [
{
"en": "What are possessive adjectives?",
"ar": "ما هي صفات الملكية؟",
"expl_ar": "صفات الملكية تدل على أن شيئاً ملكاً لشخص: my (لي)، your (لك)، his (له)، her (لها)، its (له لغير العاقل)، our (لنا)، their (لهم).",
"expl_en": "Possessive adjectives show ownership: my, your, his, her, its, our, their.",
"formula": "my • your • his • her • its • our • their",
"examples": [
("My house is big.", "بيتي كبير."),
("His name is Omar.", "اسمه عمر."),
("Our school is new.", "مدرستنا جديدة.")]},
{
"en": "Always followed by a noun",
"ar": "تأتي دائماً قبل الاسم",
"expl_ar": "صفة الملكية لا تقف وحدها بل تتبعها اسماً: my book، your pen، our teacher. لا نقول This is my بل نضيف الاسم.",
"expl_en": "A possessive adjective always comes before a noun: my book, your pen.",
"formula": "possessive adjective + noun",
"examples": [
("my book", "كتابي."),
("her mother", "أمها."),
("their house", "بيتهم.")]},
{
"en": "No plural form for possessive adjectives",
"ar": "لا جمع لصفات الملكية",
"expl_ar": "صفات الملكية لا تتغير مع الجمع: my books ليست «مياس» بل my books. نفس الصفة مع المفرد والجمع.",
"expl_en": "Possessive adjectives do not change for plural: my book / my books.",
"formula": "my + singular = my + plural (same word)",
"examples": [
("my car → my cars", "سيارتي ← سياراتي."),
("their child → their children", "طفلهم ← أطفالهم."),
("your pen → your pens", "قلمك ← أقلامك.")]},
{
"en": "Its vs It's",
"ar": "الفرق بين Its و It's",
"expl_ar": "Its (بدون فاصلة علوية) = ملك لغير العاقل: The cat drinks its milk (القط يشرب حليبه). أما It's = اختصار It is: It's a cat (إنه قط).",
"expl_en": "'Its' = ownership for things/animals. 'It's' = it is.",
"formula": "its = of it | it's = it is",
"examples": [
("The dog eats its food.", "الكلب يأكل طعامه."),
("It's a beautiful day.", "إنه يوم جميل."),
("The tree loses its leaves.", "الشجرة تفقد أوراقها.")]},
{
"en": "His vs Her",
"ar": "His هيس / Her هير",
"expl_ar": "نستعمل his للمذكر (له): His name (اسمه). و her للمؤنث (لها): Her name (اسمها).\nانتبه: his للملكية قد يخص رجلا أو وطنا أو حيوانا ذكرا.",
"expl_en": "'His' = for men, 'her' = for women.",
"formula": "his + noun (male) | her + noun (female)",
"examples": [
("His father is a doctor.", "أبوه طبيب."),
("Her hair is long.", "شعرها طويل."),
("She loves her family.", "هي تحب عائلتها.")]},
{
"en": "Whose...? questions",
"ar": "السؤال بـ Whose (لمن؟)",
"expl_ar": "نستعمل Whose للسؤال عن ملكية: Whose book is this? (لمن هذا الكتاب؟). الجواب: It is Oussama's / It is mine.",
"expl_en": "'Whose' asks about possession: Whose book is this? Answer: It's Oussama's.",
"formula": "Whose + noun + is/are + ...?",
"examples": [
("Whose car is that?", "لمن تلك السيارة؟"),
("Whose pen is this? It's mine.", "لمن هذا القلم؟ إنه لي."),
("Whose keys are these?", "لمن هذه المفاتيح؟")]},
{
"en": "The 's possessive: Oussama's book",
"ar": "الملكية بـ 's: كتاب أسامة",
"expl_ar": "للملكية مع الأشخاص نضيف فاصلة علوية و s: Oussama's book (كتاب أسامة)، my mother's car (سيارة أمي).\nوللجمع المختوم بـ s نضيف فاصلة فقط: my parents' house (بيت والديّ).",
"expl_en": "Add 's for possession: Oussama's book, my mother's car. Plural ending in s → just ': my parents' house.",
"formula": "name/owner + 's + thing | plural-s + ' + thing",
"examples": [
("Oussama's bicycle", "دراجة أسامة."),
("my sister's bag", "حقيبة أختي."),
("the students' books", "كتب الطلاب.")]},
{
"en": "The 's with the last owner",
"ar": "الحرف 's مع آخر المالك",
"expl_ar": "عند الملكية المشتركة نضيف 's لآخر اسم فقط: Oussama and Islem's room (غرفة أسامة وإسلام معاً).\nأما إذا لكل منهما شيء فأضف 's للاثنين: Oussama's and Islem's rooms.",
"expl_en": "Shared ownership: put 's on the last name only (Oussama and Islem's room).",
"formula": "A + B + 's + thing (shared)",
"examples": [
("Anes and Islem's toys", "ألعاب أنس وإسلام."),
("my uncle and aunt's house", "بيت عمي وعمتي (معاً)."),
("Mom and Dad's wedding", "زواج أمي وأبي.")]},
{
"en": "Possessive adjectives vs possessive pronouns (intro)",
"ar": "صفات الملكية مقابل ضمائر الملكية",
"expl_ar": "صفة الملكية قبل الاسم (my book)، وضمير الملكية يحل محل الاسم (mine بمعنى «لي»).\nسنفصله في مستوى لاحق لكن تذكر: his و its كما هما.",
"expl_en": "Possessive adjective + noun (my book). Possessive pronoun replaces the noun (mine).",
"formula": "my→mine • your→yours • her→hers • our→ours • their→theirs",
"examples": [
("This is my pen. It is mine.", "هذا قلمي. إنه لي."),
("Her bag is red. Hers is new.", "حقيبتها حمراء. حقيبتها (لها) جديدة."),
("Our house is here. Yours is there.", "بيتنا هنا. بيتكم هناك.")]},
{
"en": "Practice: possessive sentences",
"ar": "تمارين على الملكية",
"expl_ar": "تدرب على تحويل: I have a brother → My brother ...؟ لا، بل: my brother. استعمل صفات الملكية مع أفراد العائلة والأشياء الشخصية كل يوم.",
"expl_en": "Practise: say these daily — my father, your mother, his bike, her school, our class, their city.",
"formula": "subject → possessive: I → my, you → your, he → his ...",
"examples": [
("We love our city.", "نحب مدينتنا."),
("They play in their garden.", "يلعبون في حديقتهم."),
("You must finish your homework.", "يجب أن تنجز واجبك.")]},
]
},
# ============================ NIVEAU 8 ============================
{
"num": 8, "cefr": "A1",
"category": "Numbers, Days, Months",
"category_ar": "الأرقام والأيام والشهور",
"title_en": "Numbers, Days, Months and Seasons",
"title_ar": "الأرقام والأيام والشهور والفصول",
"ideas": [
{
"en": "Cardinal numbers: 1 to 20",
"ar": "الأعداد الأساسية: من 1 إلى 20",
"expl_ar": "الأعداد من 1 إلى 20 يجب حفظها: one، two، three، four، five، six، seven، eight، nine، ten، eleven، twelve، ثم thirteen... twenty.",
"expl_en": "Memorize 1 to 20: one, two, three ... nineteen, twenty.",
"formula": "1 one • 2 two • 3 three • ... • 10 ten • 11 eleven • 12 twelve ...",
"examples": [
("I have ten fingers.", "لدي عشرة أصابع."),
("She is twelve years old.", "عمرها اثنتي عشرة سنة."),
("Seven days in a week.", "سبعة أيام في الأسبوع.")]},
{
"en": "Tens and numbers 20-100",
"ar": "العشرات والأعداد من 20 إلى 100",
"expl_ar": "نبدأ من العشرات: twenty (20)، thirty (30)، forty (40)، fifty (50)، sixty (60)، seventy (70)، eighty (80)، ninety (90)، a hundred (100).\nنربط بالواصلة: twenty-five (25)، thirty-one (31).",
"expl_en": "Tens: twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety, a hundred. Join with a hyphen: twenty-five.",
"formula": "twenty + - + five = twenty-five (25)",
"examples": [
("thirty-five books", "خمسة وثلاثون كتابا."),
("a hundred dirhams/cents", "مئة."),
("forty students are here.", "أربعون طالبا هنا.")]},
{
"en": "Numbers 100 to 1000",
"ar": "الأعداد من 100 إلى 1000",
"expl_ar": "نكوّن الأعداد الكبيرة بسهولة: a hundred (100)، two hundred (200)، ثلاث مئة، وهكذا حتى a thousand (1000).\nنضيف الرقم بعد المئة: 350 = three hundred and fifty.",
"expl_en": "Make big numbers easily: a hundred, two hundred, a thousand. 350 = three hundred and fifty.",
"formula": "hundred + and + tens/units (350 = three hundred and fifty)",
"examples": [
("a hundred ... = 100", "مئة = 100."),
("nine hundred ninety-nine = 999", "999."),
("two thousand ... = 2000", "ألفان = 2000.")]},
{
"en": "Days of the week",
"ar": "أيام الأسبوع",
"expl_ar": "الأيام السبعة: Monday، Tuesday، Wednesday، Thursday، Friday، Saturday، Sunday.\nفي الجزائر عطلة نهاية الأسبوع: الجمعة والسبت.\nنكتب الأيام بحرف كبير دائماً، ونستعمل on + اليوم: on Friday.",
"expl_en": "Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Use 'on' with days: on Friday.",
"formula": "on + Monday/Sunday...",
"examples": [
("We rest on Friday.", "نستريح يوم الجمعة."),
("School starts on Sunday.", "تبدأ المدرسة يوم الأحد."),
("Today is Saturday.", "اليوم هو السبت.")]},
{
"en": "Months of the year",
"ar": "شهور السنة",
"expl_ar": "الشهور الاثنا عشر: January، February، March، April، May، June، July، August، September، October، November، December.\nنستعمل in مع الشهر: in September.",
"expl_en": "Months: January to December. Use 'in' with months: in May.",
"formula": "in + January/December...",
"examples": [
("Ramadan was in March this year.", "كان رمضان في مارس هذه السنة."),
("School starts in September.", "تبدأ المدرسة في سبتمبر."),
("My birthday is in July.", "عيد ميلادي في يوليو.")]},
{
"en": "Seasons",
"ar": "الفصول",
"expl_ar": "الفصول الأربعة: spring (الربيع)، summer (الصيف)، autumn/fall (الخريف)، winter (الشتاء).\nنستعمل in مع الفصل: in winter.\nلكل فصل صفاته: hot (حار)، cold (بارد)، sunny (مشمس)، rainy (ممطر).",
"expl_en": "Seasons: spring, summer, autumn, winter. Use 'in' with a season: in winter.",
"formula": "in + spring/summer/autumn/winter",
"examples": [
("It is hot in summer.", "الجو حار في الصيف."),
("Leaves fall in autumn.", "تسقط الأوراق في الخريف."),
("We wear coats in winter.", "نلبس المعاطف في الشتاء.")]},
{
"en": "Ordinal numbers: first, second, third...",
"ar": "الأعداد الترتيبية: الأول، الثاني، الثالث...",
"expl_ar": "للترتيب نستخدم: first (الأول)، second (الثاني)، third (الثالث)، fourth (الرابع)...\nنشكلها بإضافة th للعدد: six → sixth.\nالاستثناءات: 1st، 2nd، 3rd، و 5th (fifth).",
"expl_en": "Ordinals: first, second, third, fourth... Add th: six→sixth. Exceptions: 1st, 2nd, 3rd, 5th.",
"formula": "4th fourth • 5th fifth • 11th eleventh • 21st twenty-first",
"examples": [
("April is the fourth month.", "أبريل هو الشهر الرابع."),
("He is the first in class.", "هو الأول في القسم."),
("December is the twelfth month.", "ديسمبر هو الشهر الثاني عشر.")]},
{
"en": "Saying dates",
"ar": "قراءة التاريخ",
"expl_ar": "الترتيب الإنجليزي: اليوم ثم الشهر ثم السنة.\nنقرأ بـ the + ترتيبي + of: the first of March (الأول من مارس).\nالتعبير المكتوب: March 1st أو 1st March.",
"expl_en": "British order: day, month, year. Read: the first of March. Write: 1st March.",
"formula": "the + ordinal + of + month (1st March / March 1st)",
"examples": [
("Today is the 29th of August.", "اليوم هو 29 أغسطس."),
("My birthday is on the 3rd of May.", "عيد ميلادي في 3 مايو."),
("We start on September 1st.", "نبدأ في أول سبتمبر.")]},
{
"en": "Saying years",
"ar": "قراءة السنوات",
"expl_ar": "سنوات قديمة نقسمها نصفين: 1990 = nineteen ninety.\nالسنوات الحديثة: 2000 = two thousand، 2024 = twenty twenty-four.",
"expl_en": "Old years divide in two halves: 1990 = nineteen ninety. New years: 2024 = twenty twenty-four.",
"formula": "1962 = nineteen sixty-two • 2025 = twenty twenty-five",
"examples": [
("I was born in 2010.", "ولدت في 2010."),
("Algeria became independent in 1962.", "استقلت الجزائر عام 1962."),
("It is the year 2026.", "نحن في سنة 2026.")]},
{
"en": "Practice numbers in real life",
"ar": "استعمال الأرقام في الحياة",
"expl_ar": "استعمل الأرقام دائماً: لتاريخ الميلاد، رقم الهاتف، السعر، الوقت، التاريخ. كل ما تتحدث عنه بالأرقام يثبت حفظك لها.",
"expl_en": "Use numbers everywhere: age, dates, prices, phone numbers, time.",
"formula": "age + years old • price + dinars • date + on/in",
"examples": [
("How much is it? It is 200 dinars.", "كم سعرها؟ 200 دينار."),
("My phone number is 0550...", "رقم هاتفي 0550..."),
("When is your birthday?", "متى عيد ميلادك؟")]},
]
},
# ============================ NIVEAU 9 ============================
{
"num": 9, "cefr": "A1",
"category": "There is / There are",
"category_ar": "يوجد / توجد",
"title_en": "There is / There are",
"title_ar": "There is / There are (يوجد)",
"ideas": [
{
"en": "There is + singular",
"ar": "There is + مفرد",
"expl_ar": "نستعمل There is (يوجد/هناك) مع الاسم المفرد: There is a book on the table (يوجد كتاب على الطاولة). الاختصار: There's.",
"expl_en": "Use 'There is' with a singular noun: There is a book on the table. Short form: There's.",
"formula": "There is + a/an + singular noun + place",
"examples": [
("There is a cat in the garden.", "يوجد قطة في الحديقة."),
("There's a phone in my bag.", "يوجد هاتف في حقيبتي."),
("Is there a bank near here?", "هل يوجد بنك قريب من هنا؟")]},
{
"en": "There are + plural",
"ar": "There are + جمع",
"expl_ar": "نستعمل There are مع الاسم الجمع: There are two windows in the room (يوجد نافذتان في الغرفة). لا نقول There is مع الجمع.",
"expl_en": "Use 'There are' with plural nouns: There are two windows.",
"formula": "There are + plural noun + place",
"examples": [
("There are four chairs here.", "توجد أربعة كراسي هنا."),
("There are many students.", "يوجد طلاب كثيرون."),
("There are apples in the basket.", "يوجد تفاح في السلة.")]},
{
"en": "Negative: There isn't / There aren't",
"ar": "النفي: ليس هناك",
"expl_ar": "النفي: There isn't (مع مفرد) و There aren't (مع جمع): There isn't any sugar (لا يوجد سكر)، There aren't any pencils (لا توجد أقلام).",
"expl_en": "Negatives: There isn't (singular), There aren't (plural).",
"formula": "There isn't + a/an/any + singular | There aren't + any + plural",
"examples": [
("There isn't a TV in my room.", "لا يوجد تلفاز في غرفتي."),
("There aren't any chairs.", "لا توجد كراسي."),
("There's no milk in the fridge.", "لا يوجد حليب في الثلاجة.")]},
{
"en": "Questions: Is there...? Are there...?",
"ar": "السؤال: هل يوجد...؟",
"expl_ar": "نقلب الفعل للسؤال: Is there a bank? (هل يوجد بنك؟)، Are there any shops? (هل توجد محلات؟). نستعمل any في السؤال مع الجمع و بعض المفرادات.",
"expl_en": "Questions: Is there...? (singular), Are there...? (plural). Use 'any' in questions.",
"formula": "Is there + a/an + noun? | Are there + any + plural noun?",
"examples": [
("Is there a mosque near here?", "هل يوجد مسجد قريب؟"),
("Are there any parks in town?", "هل توجد حدائق في المدينة؟"),
("Is there a problem?", "هل توجد مشكلة؟")]},
{
"en": "Short answers: Yes, there is / No, there isn't",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب باختصار: Yes, there is. أو No, there isn't. للجمع: Yes, there are. أو No, there aren't.\nلا نكرر الاسم في الجواب المختصر.",
"expl_en": "Short answers: Yes, there is. No, there isn't. (plural: there are / there aren't).",
"formula": "Yes, there is/are. | No, there isn't/aren't.",
"examples": [
("Is there a library? Yes, there is.", "هل توجد مكتبة؟ نعم."),
("Are there any buses? No, there aren't.", "هل توجد حافلات؟ لا."),
("Is there any water? Yes, there is.", "هل يوجد ماء؟ نعم.")]},
{
"en": "There is vs It is",
"ar": "الفرق بين There is و It is",
"expl_ar": "There is يُقدم شيئاً جديداً لأول مرة (يوجد...)، أما It is فيحدد شيئاً معروفاً (إنه...).\nمثال: There is a dog in the street. It is brown.",
"expl_en": "'There is' introduces something new. 'It is' describes known things.",
"formula": "There is + new noun → then → It is + description",
"examples": [
("There is a bird on the tree. It is singing.", "يوجد طائر على الشجرة. إنه يغرد."),
("There is a school near here. It is new.", "يوجد مركز قريب. إنه جديد."),
("Is there a doctor? It is Dr. Madani.", "هل يوجد طبيب؟ إنه الدكتور مداني.")]},
{
"en": "There are + some",
"ar": "There are + some (بعض)",
"expl_ar": "مع الجمع نستعمل some في الجملة المثبتة: There are some books (يوجد بعض الكتب). أما في النفي والسؤال فنستعمل any.",
"expl_en": "Use 'some' in positive plurals: There are some books. Use 'any' in negatives and questions.",
"formula": "positive: There are some + plural | question/negative: any",
"examples": [
("There are some chairs.", "توجد بعض الكراسي."),
("Are there any problems?", "هل توجد مشاكل؟"),
("There aren't any eggs.", "لا توجد بيضات.")]},
{
"en": "There is + some + uncountable",
"ar": "There is + some + غير معدود",
"expl_ar": "مع الأسماء غير المعدودة (ماء، حليب، سكر، خبز) نستعمل There is وليس There are: There is some water (يوجد بعض الماء).",
"expl_en": "With uncountable nouns (water, milk) use 'There is': There is some water.",
"formula": "There is + some + uncountable noun",
"examples": [
("There is some bread.", "يوجد بعض الخبز."),
("There is some juice in the fridge.", "يوجد بعض العصير في الثلاجة."),
("Is there any rice? Yes, there is.", "هل يوجد أرز؟ نعم.")]},
{
"en": "Describing rooms and places",
"ar": "وصف الغرف والأماكن",
"expl_ar": "لوصف مكان نستعمل There is/are مع حروف الجر المكانية: in، on، under، next to، between.\nمثال: There is a bed next to the window (توجد سرير بجانب النافذة).",
"expl_en": "Describe places with There is/are + place prepositions (in, on, under, next to).",
"formula": "There is/are + noun + preposition + place",
"examples": [
("There is a lamp on the desk.", "يوجد مصباح على المكتب."),
("There is a table in the kitchen.", "توجد طاولة في المطبخ."),
("There are pictures on the wall.", "توجد صور على الجدار.")]},
{
"en": "Practice: your town and home",
"ar": "تمرين: مدينتك ومنزلك",
"expl_ar": "تحدث عن مدينتك: There is a market (سوق)...، There are two mosques (مساجد)...، There isn't a cinema (سينما).\nوعن منزلك: There is a garden (حديقة) behind the house.",
"expl_en": "Talk about your town and home with There is/are. Say what exists and what does not.",
"formula": "In my town, there is/are ... There isn't/aren't ...",
"examples": [
("There is a stadium in our city.", "يوجد ملعب في مدينتنا."),
("There aren't any bridges here.", "لا توجد جسور هنا."),
("There is a big kitchen in my house.", "يوجد مطبخ كبير في منزلي.")]},
]
},
# ============================ NIVEAU 10 ============================
{
"num": 10, "cefr": "A1",
"category": "Have Got / Has Got",
"category_ar": "الملكية: have got / has got",
"title_en": "Have got / Has got",
"title_ar": "have got / has got (الملكية)",
"ideas": [
{
"en": "Have got: possession",
"ar": "have got: الملكية",
"expl_ar": "نستعمل have got للتعبير عن الملكية.\nمع I/you/we/they: have got، ومع he/she/it: has got.\nالمثال: I have got a bike (لدي دراجة).",
"expl_en": "Use 'have got' to show possession. I/you/we/they → have got. He/she/it → has got.",
"formula": "I/you/we/they + have got | he/she/it + has got",
"examples": [
("I have got one brother.", "لدي أخ واحد."),
("You have got two eyes.", "لديك عينان."),
("They have got a new car.", "لديهم سيارة جديدة.")]},
{
"en": "Has got with he/she/it",
"ar": "has got مع هو/هي",
"expl_ar": "المفرد الغائب (he, she, it) يأخذ has got: She has got long hair (لديها شعر طويل)، The house has got three rooms (للبيت ثلاث غرف).",
"expl_en": "Has got is for he, she, it: She has got long hair.",
"formula": "He/She/It + has got + noun",
"examples": [
("She has got a dog.", "لديها كلب."),
("He has got blue eyes.", "لديه عينان زرقاوان."),
("It (the phone) has got a big screen.", "لها شاشة كبيرة.")]},
{
"en": "Short forms: 've got / 's got",
"ar": "الاختصارات: 've got / 's got",
"expl_ar": "نختصر: I have got ← I've got، He has got ← He's got، They have got ← They've got.\nتحذف have/has وتُستبدل بفاصلة علوية.",
"expl_en": "Contractions: I've got, He's got, They've got.",
"formula": "have→'ve | has→'s",
"examples": [
("I've got a cold.", "لدي زكام."),
("She's got two sisters.", "لديها أختان."),
("We've got time.", "لدينا وقت.")]},
{
"en": "Negative: haven't got / hasn't got",
"ar": "النفي: ليس لدي",
"expl_ar": "النفي بإضافة not بين have/has و got: I haven't got (ليس لدي)، She hasn't got (ليس لديها). لا نستعمل do في النفي هنا.",
"expl_en": "Negative: haven't got / hasn't got. Do not use 'do' with got.",
"formula": "I/you/we/they + haven't got | he/she/it + hasn't got",
"examples": [
("I haven't got a laptop.", "ليس لدي حاسوب محمول."),
("He hasn't got any money.", "ليس لديه مال."),
("We haven't got homework today.", "ليس لدينا واجب اليوم.")]},
{
"en": "Questions: Have you got...?",
"ar": "السؤال: هل لديك...؟",
"expl_ar": "نبدأ السؤال بالفعل: Have you got a car? (هل لديك سيارة؟)، Has she got a sister? (هل لديها أخت؟).",
"expl_en": "Questions start with the verb: Have you got...? Has she got...?",
"formula": "Have/Has + subject + got + noun?",
"examples": [
("Have you got a pen?", "هل لديك قلم؟"),
("Has he got a phone?", "هل لديه هاتف؟"),
("Have they got any children?", "هل لديهم أطفال؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب بـ Yes/No مع الفاعل: Yes, I have. / No, I haven't. مع المفرد الغائب: Yes, she has. / No, he hasn't.",
"expl_en": "Short answers: Yes, I have. No, I haven't. Yes, she has. No, he hasn't.",
"formula": "Yes, + subject + have/has | No, + subject + haven't/hasn't",
"examples": [
("Have you got a bike? Yes, I have.", "هل لديك دراجة؟ نعم."),
("Has she got a cat? No, she hasn't.", "هل لديها قطة؟ لا."),
("Have we got time? Yes, we have.", "هل لدينا وقت؟ نعم.")]},
{
"en": "Uses: family, things, feelings",
"ar": "الاستعمالات: العائلة والأشياء والمشاعر",
"expl_ar": "نستعمل have got مع: العائلة (I have got a big family)، الأشياء المادية (a house)، وحتى بعض الحالات (I've got a headache).",
"expl_en": "Have got is used for family, possessions, and some conditions like a headache.",
"formula": "have got + family member / possession / illness",
"examples": [
("I've got three cousins.", "لدي ثلاثة أبناء عم."),
("He's got a very big house.", "لديه منزل كبير جدا."),
("I've got a bad headache.", "لدي صداع شديد.")]},
{
"en": "Have got vs Have",
"ar": "have got مقابل have",
"expl_ar": "have got و have بمعنى واحد للملكية في الإنجليزية البريطانية: I have a car = I have got a car.\nلكن للسؤال والنفي نماذج مختلفة: Do you have a car? = Have you got a car?",
"expl_en": "Have = Have got for possession. Questions: Do you have...? = Have you got...?",
"formula": "I have ... = I've got ... | Do you have? = Have you got?",
"examples": [
("I have two brothers. = I've got two brothers.", "لدي أخوان."),
("Do you have a car? = Have you got a car?", "هل لديك سيارة؟"),
("I don't have a computer. = I haven't got one.", "ليس لدي حاسوب.")]},
{
"en": "Never use double forms",
"ar": "لا تجمع الصيغتين",
"expl_ar": "لا تقل «I have got a car» مع do: لا نقول Do you have got؟ ولا He doesn't has got.\nاختر صيغة واحدة: has got أو have.",
"expl_en": "Never mix: 'Do you have got?' is wrong. Choose one form: have got or have.",
"formula": "WRONG: Do you have got? | RIGHT: Have you got? / Do you have?",
"examples": [
("Have you got a pen? ✓", "هل لديك قلم؟ صحيح."),
("Do you have a pen? ✓", "هل تملك قلما؟ صحيح."),
("Do you have got a pen? ✗", "جملة خاطئة.")]},
{
"en": "Describe yourself and your family",
"ar": "صف نفسك وعائلتك",
"expl_ar": "تحدث عما تملكه: I've got brown eyes (لدي عيون بنية)، my brother has got short hair (لأخي شعر قصير)، we've got a small garden (لدينا حديقة صغيرة).\nاستعمل have/has got لوصف أفراد عائلتك.",
"expl_en": "Describe yourself: I've got brown eyes. Describe your family with has/have got.",
"formula": "I've got ... • My brother has got ... • We've got ...",
"examples": [
("I've got long hair.", "لدي شعر طويل."),
("My father has got a grey beard.", "لأبي لحية رمادية."),
("We've got a small, cosy house.", "لدينا بيت صغير ومريح.")]},
]
},
]