# -*- coding: utf-8 -*-
"""المستويات 41–50 : متوسط (B1) — المضارع التام، الماضي المستمر، modals، الشروط.""" 

LEVELS = [

# ============================ NIVEAU 41 ============================
{
"num": 41, "cefr": "B1",
"category": "Present Perfect",
"category_ar": "المضارع التام",
"title_en": "Present Perfect: Form and Use",
"title_ar": "المضارع التام: التشكيل والاستعمال",
"ideas": [
{
"en": "Form: have/has + past participle",
"ar": "التشكيل: have/has + التصريف الثالث",
"expl_ar": "المضارع التام يتكون من have/has + التصريف الثالث (past participle): I have finished، She has written.\nللأفعال الشاذة التصريف الثالث خاص (go-gone، see-seen، write-written).",
"expl_en": "Present perfect = have/has + past participle (I have finished, she has seen).",
"formula": "subject + have/has + past participle",
"examples": [
("I have finished my homework.", "لقد أنهيت واجبي المنزلي."),
("She has seen that film twice.", "لقد شاهدت ذلك الفيلم مرتين."),
("They have gone to the market.", "لقد ذهبوا إلى السوق.")]},
{
"en": "Present perfect vs past simple",
"ar": "المضارع التام مقابل الماضي البسيط",
"expl_ar": "نستعمل الماضي البسيط عندما نذكر زمناً محدداً انتهى (yesterday (أمس) و last week (الأسبوع الماضي))، والمضارع التام عندما نربط الماضي بالحاضر (النتيجة الآن):\nI lost my keys (عندماً) — I have lost my keys (لا أجدهن الآن).",
"expl_en": "Past simple = finished time. Present perfect = result now. I lost my keys / I have lost my keys.",
"formula": "past simple + finished time | present perfect + result now",
"examples": [
("I saw him yesterday.", "رأيته أمس."),
("I have already seen the film.", "لقد شاهدت الفيلم توا."),
("She lived in Oran in 2010.", "عاشت في وهران سنة 2010.")]},
{
"en": "Unfinished state (up to now)",
"ar": "حالة مستمرة حتى الآن",
"expl_ar": "المضارع التام يعبر عن شيء بدأ في الماضي وما زال إلى الحاضر: I have known him for ten years (أعرفه منذ عشر سنوات وما زلت أعرفه).\nلا نستعمله مع زمن منتهٍ.",
"expl_en": "For actions/states that started in the past and continue now.",
"formula": "have/has + pp (past -> now)",
"examples": [
("I have known her since 2015.", "أعرفها منذ سنة 2015."),
("We have lived here all our lives.", "عشنا هنا طوال حياتنا."),
("He has worked at the bank for years.", "يعمل في البنك منذ سنوات.")]},
{
"en": "Irregular past participles",
"ar": "التصريف الثالث الشاذ",
"expl_ar": "العديد من الأفعال لها تصريف ثالث شاذ نحفظه: go-gone، do-done، see-seen، eat-eaten، write-written، take-taken، give-given، come-come، buy-bought، bring-brought.",
"expl_en": "Common irregular participles: gone, done, seen, eaten, written, bought.",
"formula": "base → past → past participle",
"examples": [
("I have never seen the ocean.", "لم أر المحيط قط."),
("They have eaten all the cake.", "لقد أكلوا كل الكعكة."),
("She has written a long letter.", "لقد كتبت رسالة طويلة.")]},
{
"en": "Negative: haven't / hasn't",
"ar": "النفي: haven't / hasn't",
"expl_ar": "النفي بإضافة not بعد have/has: I have not seen (لم أَرَ)، She hasn't finished (لم تنتهِ).\nكثيرا ما نستعمل never في النفي القوي.",
"expl_en": "Negative: I haven't finished. She hasn't seen it. I have never been there.",
"formula": "subject + haven't/hasn't + past participle",
"examples": [
("I haven't finished my report.", "لم أنهِ تقريري بعد."),
("She hasn't visited us this year.", "لم تزرنا هذا العام."),
("We haven't eaten anything today.", "لم نأكل شيئا اليوم.")]},
{
"en": "Questions: Have you...?",
"ar": "السؤال: هل...؟",
"expl_ar": "نبدأ بالسؤال بـ Have/Has + الفاعل: Have you finished? (هل أنهيت؟)، Has she called? (هل اتصلت؟).\nثم نستعمل الأجوبة القصيرة.",
"expl_en": "Question: Have/Has + subject + past participle?",
"formula": "Have/Has + subject + past participle?",
"examples": [
("Have you finished your homework?", "هل أنهيت واجبك؟"),
("Has she called you today?", "هل اتصلت بك اليوم؟"),
("Have they arrived at the station?", "هل وصلوا إلى المحطة؟")]},
{
"en": "Short answers",
"ar": "الأجوبة القصيرة",
"expl_ar": "نجيب: Yes, I have. / No, I haven't. Yes, she has. / No, she hasn't.\nمثال: Have you seen it? Yes, I have.",
"expl_en": "Short answers: Yes, I have. No, he hasn't.",
"formula": "Yes/No + have/has or haven't/hasn't",
"examples": [
("Have you ever been abroad? Yes, I have.", "هل سافرت خارج البلاد؟ نعم."),
("Has she finished? Yes, she has.", "هل انتهت؟ نعم."),
("Have they arrived? No, they haven't.", "هل وصلوا؟ لا.")]},
{
"en": "Experience: ever / never",
"ar": "الخبرة: ever / never",
"expl_ar": "للتعبير عن الخبرات نستعمل ever (في السؤال: هل سبق لك؟) و never (لم أسبق أبداً):\nHave you ever eaten sushi? I have never tried it.",
"expl_en": "Experience: 'Have you ever...?' 'I have never...'",
"formula": "Have you ever + pp? | I have never + pp",
"examples": [
("Have you ever climbed a mountain?", "هل سبق لك أن تسلقت جبلا؟"),
("I have never ridden a horse.", "لم أركب حصانا قط."),
("She has never flown before.", "لم تسافر بالطائرة من قبل.")]},
{
"en": "Have been vs have gone",
"ar": "have been مقابل have gone",
"expl_ar": "have been = ذهب وعاد (عاد): She has been to London (زارت لندن ورجعت).\nhave gone = ذهب وما زال هناك: He has gone to the office (ذهب وليس هنا).",
"expl_en": "Have been = went and returned. Have gone = went and is still there.",
"formula": "has been to (visited) | has gone to (still away)",
"examples": [
("I have been to Tunis twice.", "زرت تونس مرتين."),
("Dad has gone to the mosque.", "ذهب أبي إلى المسجد (وما زال هناك)."),
("Have you ever been to Morocco?", "هل زرتَ المغرب من قبل؟")]},
{
"en": "Time words: already, just, yet",
"ar": "كلمات الزمن: already, just, yet",
"expl_ar": "already (تفاجأنا أنه تم) في الجملة المثبتة، just (حالا / للتوي) قبل التصريف الثالث، yet (حتى الآن) في النفي والسؤال:\nI've just eaten، I've already done it، I haven't finished yet.",
"expl_en": "already = sooner than expected, just = a moment ago, yet = up to now (neg/question).",
"formula": "have + already/just + pp | haven't + pp + yet",
"examples": [
("I have just arrived home.", "وصلت إلى البيت لتوي."),
("She has already booked the tickets.", "لقد حجزت التذاكر توا."),
("Have you finished yet?", "هل انتهيت بعد؟")]},
]
},
# ============================ NIVEAU 42 ============================
{
"num": 42, "cefr": "B1",
"category": "Present Perfect: Just, Already, Yet",
"category_ar": "المضارع التام: just, already, yet",
"title_en": "Present Perfect with just, already, yet",
"title_ar": "المضارع التام: just, already, yet",
"ideas": [
{
"en": "just (a moment ago)",
"ar": "just (لتوه / حالا)",
"expl_ar": "just توضع بين have والتصريف الثالث وتعني «التو»: I've just finished (انتهيت للتو).\nنتحدث عن حدث قريب جدا من اللحظة الحالية.",
"expl_en": "just = a very short time ago, between have and the participle.",
"formula": "subject + have/has + just + past participle",
"examples": [
("I have just eaten lunch.", "تناولت الغداء للتو."),
("She has just left the office.", "غادرت المكتب للتو."),
("We have just heard the news.", "سمعنا الخبر توا.")]},
{
"en": "already (sooner than expected)",
"ar": "already (قبل المتوقع)",
"expl_ar": "already تعني «بفعل / سلفا» وتوضع بين have والتصريف الثالث (أو في نهاية الجملة): I've already paid (دفعت بالفعل).\nنستعملها في المثبت، وغالبا للتعجب أن الأمر تم أسرع من المتوقع.",
"expl_en": "already = before expected, in positive sentences.",
"formula": "subject + have/has + already + pp | subject + have + pp + already",
"examples": [
("I've already bought the tickets.", "اشتريت التذاكر بالفعل."),
("She's already finished her work.", "أنهت عملها بالفعل."),
("We've already seen this film.", "شاهدنا هذا الفيلم من قبل.")]},
{
"en": "yet (up to now, in negatives and questions)",
"ar": "yet (حتى الآن) في النفي والسؤال",
"expl_ar": "yet توضع في نهاية النفي أو السؤال وتعني «حتى الآن، بعد»: I haven't finished yet (لم أنتهِ بعد)، Have you called him yet? (هل اتصلت به بعد؟).",
"expl_en": "yet = up to now, used at the end of negatives and questions.",
"formula": "haven't/hasn't + pp + yet | Have/Has + subject + pp + yet?",
"examples": [
("I haven't sent the email yet.", "لم أرسل البريد الإلكتروني بعد."),
("Has the train arrived yet?", "هل وصل القطار بعد؟"),
("They haven't decided yet.", "لم يقرروا بعد.")]},
{
"en": "Choosing between just, already, yet",
"ar": "الاختيار بين just, already, yet",
"expl_ar": "قاعدة بسيطة: just = حدث قريب جدا، already = تم قبل المتوقع (مثبت)، yet = حتى الآن (نفي/سؤال).\nلا نستعمل already عادة مع منفى، ولا yet مع مثبت.",
"expl_en": "just = recent, already = positive, yet = negative/question.",
"formula": "just/already (positive) — yet (negative/question)",
"examples": [
("I've just started the lesson.", "بدأت الدرس للتو."),
("We've already done the exercise.", "أنجزنا التمرين بالفعل."),
("I haven't started yet.", "لم أبدأ بعد.")]},
{
"en": "Placement in the sentence",
"ar": "مكانها في الجملة",
"expl_ar": "just و already تأتي بعد have/has وقبل التصريف الثالث (أو في آخر الجملة مع already)، بينما yet تأتي دائما في آخر الجملة عادة.",
"expl_en": "just/already after have, before participle. yet usually at the end.",
"formula": "have + just/already + pp | pp + yet",
"examples": [
("She has just bought a new car.", "اشترت سيارة جديدة لتوها."),
("I have already written the article.", "كتبت المقال بالفعل."),
("He hasn't arrived at the airport yet.", "لم يصل إلى المطار بعد.")]},
{
"en": "Participle with just/already/yet in questions",
"ar": "التصريف الثالث مع just, already, yet في السؤال",
"expl_ar": "في السؤال: Have you just eaten? (هل أكلت للتو؟)، Have you already told him? (هل أخبرته بالفعل؟)، Have you finished yet? (هل انتهيت بعد؟).",
"expl_en": "Questions: Have you just/already + pp? Have you + pp + yet?",
"formula": "Have + subject + just/already + pp? | Have + subject + pp + yet?",
"examples": [
("Have you just arrived from Algiers?", "هل وصلت للتو من الجزائر؟"),
("Has she already spoken to the doctor?", "هل تحدثت مع الطبيب بالفعل؟"),
("Have they paid the rent yet?", "هل دفعوا الإيجار بعد؟")]},
]
},
# ============================ NIVEAU 43 ============================
{
"num": 43, "cefr": "B1",
"category": "Present Perfect: For and Since",
"category_ar": "المضارع التام: for و since",
"title_en": "Present Perfect with for and since",
"title_ar": "المضارع التام: for و since",
"ideas": [
{
"en": "for + a period (duration)",
"ar": "for + مدة زمنية",
"expl_ar": "for تعني «لمدة» وتأتي مع مدة زمنية: for five years (لمدة خمس سنوات)، for two hours (لمدة ساعتين)، for a week (لمدة أسبوع).\nنستعملها مع المضارع التام للحديث عن مدة استمرار شيء إلى الآن.",
"expl_en": "for + a period of time (for 5 years, for a week).",
"formula": "have/has + pp + for + period",
"examples": [
("I have lived here for ten years.", "عشت هنا منذ عشر سنوات."),
("She has worked for this company for months.", "تعمل مع هذه الشركة منذ أشهر."),
("We have waited for an hour.", "انتظرنا لمدة ساعة.")]},
{
"en": "since + a point in time",
"ar": "since + نقطة زمنية",
"expl_ar": "since تعني «منذ» وتأتي مع نقطة بداية محددة: since 2010، since Monday، since I was a child (منذ كنت طفلا)، since last June.\nتحدد متى بدأ الشيء.",
"expl_en": "since + a point in time (since 2010, since Monday).",
"formula": "have/has + pp + since + starting point",
"examples": [
("I have known him since 2015.", "أعرفه منذ سنة 2015."),
("She has studied English since last year.", "تدرس الإنجليزية منذ السنة الماضية."),
("We have been friends since childhood.", "نحن أصدقاء منذ الطفولة.")]},
{
"en": "for vs since: the difference",
"ar": "الفرق بين for و since",
"expl_ar": "for تجيب عن السؤال How long? بمدة (من كم؟ لمدة)، بينما since تعطي نقطة البداية (من متى؟).\nلا نخلط: for three days (مدة) ⟷ since Tuesday (بداية).",
"expl_en": "for = duration, since = starting point. for 3 days ⟷ since Tuesday.",
"formula": "for + duration | since + starting point",
"examples": [
("I have known him for three years.", "أعرفه منذ ثلاث سنوات (مدة)."),
("I have known him since 2019.", "أعرفه منذ سنة 2019 (بداية)."),
("She has been ill since Monday.", "مريضة منذ الاثنين.")]},
{
"en": "How long...? with for/since",
"ar": "سؤال How long? مع for و since",
"expl_ar": "للسؤال عن المدة: How long have you lived here? (منذ متى تسكن هنا؟)\nثم نجيب بـ for أو since: For ten years / Since 2010.",
"expl_en": "'How long have you...?' answer with for or since.",
"formula": "How long + have/has + subject + pp?",
"examples": [
("How long have you studied English?", "منذ متى تدرس الإنجليزية؟"),
("How long has she been a teacher?", "منذ متى هي معلمة؟"),
("How long have they lived in Oran?", "منذ متى يسكنون في وهران؟")]},
{
"en": "Since + a clause",
"ar": "since + جملة",
"expl_ar": "since يمكن أن يتبعه جملة كاملة في الماضي البسيط: since I moved here (منذ أن انتقلت إلى هنا)، since we met (منذ أن التقينا).",
"expl_en": "since + a clause in the past simple: since I moved here.",
"formula": "have/has + pp + since + past simple clause",
"examples": [
("I have felt better since I started exercising.", "أشعر بتحسن منذ أن بدأت ممارسة الرياضة."),
("She has been happier since she changed her job.", "هي أسعد منذ أن غيّرت عملها."),
("We have known each other since we were children.", "نتعرف على بعضنا منذ الطفولة.")]},
{
"en": "Present perfect continuous with for/since",
"ar": "المضارع التام المستمر مع for و since",
"expl_ar": "نستعمل أحيانا المضارع التام المستمر مع for و since للتأكيد على استمرار الفعل: I have been studying for two hours (أدرس منذ ساعتين وما زلت).",
"expl_en": "For continuous emphasis: I have been studying for two hours.",
"formula": "have/has been + -ing + for/since",
"examples": [
("I have been studying for three hours.", "أدرس منذ ثلاث ساعات."),
("She has been waiting since morning.", "تنتظر منذ الصباح."),
("They have been working here for years.", "يعملون هنا منذ سنوات.")]},
]
},
# ============================ NIVEAU 44 ============================
{
"num": 44, "cefr": "B1",
"category": "Past Continuous",
"category_ar": "الماضي المستمر",
"title_en": "Past Continuous",
"title_ar": "الماضي المستمر",
"ideas": [
{
"en": "Form: was/were + -ing",
"ar": "التشكيل: was/were + -ing",
"expl_ar": "الماضي المستمر يتكون من was/were + الفعل + ing: I was watching TV، They were playing.\nنعبّر عن فعل كان مستمرا في الماضي في لحظة معينة.",
"expl_en": "Past continuous = was/were + -ing. I was watching TV.",
"formula": "subject + was/were + verb-ing",
"examples": [
("I was watching TV at nine.", "كنت أشاهد التلفاز في التاسعة."),
("She was cooking dinner.", "كانت تطبخ العشاء."),
("They were playing football.", "كانوا يلعبون كرة القدم.")]},
{
"en": "In progress at a specific time",
"ar": "في تقدم في وقت محدد",
"expl_ar": "نستعمله لفعل كان قيد التقدم في لحظة معينة في الماضي: At 8 p.m. I was doing my homework (في الثامنة كنت أنجز واجبي).",
"expl_en": "For an action in progress at a specific past time.",
"formula": "was/were + -ing + at a specific time",
"examples": [
("At midnight we were sleeping.", "في منتصف الليل كنا نائمين."),
("Yesterday at 5 o'clock she was driving home.", "أمس في الخامسة كانت تقود إلى المنزل."),
("This time last week I was on holiday.", "في مثل هذا الوقت الأسبوع الماضي كنت في عطلة.")]},
{
"en": "Two actions at the same time",
"ar": "فعلان في نفس الوقت",
"expl_ar": "عندما يحدث فعلان في نفس الوقت في الماضي نستعمل الماضي المستمر لكلاهما للتعبير عن التزامن: While I was cooking, he was watching TV.",
"expl_en": "For two simultaneous actions: While I was cooking, he was watching TV.",
"formula": "while + was/were -ing, was/were -ing",
"examples": [
("While I was cooking, he was watching TV.", "بينما كنت أطبخ، كان يشاهد التلفاز."),
("The children were playing while their mother was working.", "كان الأطفال يلعبون بينما كانت أمهم تعمل."),
("We were talking while the teacher was writing.", "كنا نتحدث بينما كان المعلم يكتب.")]},
{
"en": "Past continuous with while / when",
"ar": "الماضي المستمر مع while / when",
"expl_ar": "نستعمل past continuous للتعبير عن الفعل الطويل (الأساس)، و past simple للفعل القصير الذي قاطعه: While I was sleeping, the phone rang (بينما كنت نائما رن الهاتف).",
"expl_en": "Long action (past continuous) + short interrupting action (past simple).",
"formula": "while + past continuous, + past simple",
"examples": [
("While I was sleeping, the phone rang.", "بينما كنت نائما، رن الهاتف."),
("She was reading when the door opened.", "كانت تقرأ عندما فتح الباب."),
("We were walking when it started to rain.", "كنا نمشي عندما بدأ المطر.")]},
{
"en": "Negative: wasn't / weren't + -ing",
"ar": "النفي: wasn't / weren't + -ing",
"expl_ar": "النفي بإضافة not: I wasn't watching، They weren't playing.\nنستعمله لنقول أن شيئا لم يكن قيد التقدم.",
"expl_en": "Negative: I wasn't watching. They weren't playing.",
"formula": "subject + wasn't/weren't + verb-ing",
"examples": [
("I wasn't listening to the teacher.", "لم أكن أستمع إلى المعلم."),
("She wasn't sleeping at ten.", "لم تكن نائمة في العاشرة."),
("They weren't working yesterday.", "لم يكونوا يعملون بالأمس.")]},
{
"en": "Questions: Was/Were + subject + -ing?",
"ar": "السؤال: Was/Were + الفاعل + -ing؟",
"expl_ar": "للسؤال نضع was/were قبل الفاعل: Were you sleeping? (هل كنت نائما؟)، What was she doing? (ماذا كانت تفعل؟).",
"expl_en": "Question: Was/Were + subject + -ing? What were you doing?",
"formula": "Was/Were + subject + verb-ing?",
"examples": [
("Were you sleeping at midnight?", "هل كنت نائما في منتصف الليل؟"),
("What was he doing when you arrived?", "ماذا كان يفعل عندما وصلتَ؟"),
("Were they playing in the garden?", "هل كانوا يلعبون في الحديقة؟")]},
{
"en": "State verbs (not usually continuous)",
"ar": "أفعال الحالة (لا تكون مستمرة عادة)",
"expl_ar": "الأفعال التي تعبر عن حالة وليست فعل (know, want, like, believe, understand, love) لا تستعمل في المستمر عادة: I knew (وليس I was knowing).",
"expl_en": "State verbs (know, want, like) are not usually used in the continuous.",
"formula": "state verbs: know, want, like, believe, understand",
"examples": [
("I knew the answer.", "كنت أعرف الجواب."),
("She wanted a break.", "كانت تريد استراحة."),
("We understood the lesson.", "كنا نفهم الدرس.")]},
]
},
# ============================ NIVEAU 45 ============================
{
"num": 45, "cefr": "B1",
"category": "Past Simple vs Past Continuous",
"category_ar": "الماضي البسيط مقابل الماضي المستمر",
"title_en": "Past Simple vs Past Continuous",
"title_ar": "الماضي البسيط والماضي المستمر",
"ideas": [
{
"en": "Background action (continuous) + main event (simple)",
"ar": "فعل الخلفية (مستمر) + الحدث الرئيسي (بسيط)",
"expl_ar": "الماضي المستمر يعطينا الخلفية/الأجواء، والماضي البسيط يعطينا الحدث الرئيسي الذي قاطعها: I was having a shower when the doorbell rang.",
"expl_en": "Continuous = background; simple = the event that interrupted.",
"formula": "was/were -ing (background) + past simple (event)",
"examples": [
("I was having a shower when the phone rang.", "كنت أستحم عندما رن الهاتف."),
("She was cooking when the lights went out.", "كانت تطبخ عندما انطفأت الأضواء."),
("We were talking when the boss came in.", "كنا نتحدث عندما دخل المدير.")]},
{
"en": "Choice between simple and continuous",
"ar": "الاختيار بين البسيط والمستمر",
"expl_ar": "اختر الماضي البسيط للأحداث الكاملة القصيرة (He arrived)، والماضي المستمر للأفعال الطويلة غير المكتملة (He was arriving).\nغالبا الفعل الطويل + الحدث القصير.",
"expl_en": "Simple = short complete events; continuous = longer background actions.",
"formula": "short completed: past simple | longer: past continuous",
"examples": [
("He came in and sat down.", "دخل وجلس."),
("He was coming in when I saw him.", "كان يدخل عندما رأيته."),
("She opened the window and looked out.", "فتحت النافذة ونظرت إلى الخارج.")]},
{
"en": "Repeated vs temporary actions",
"ar": "أفعال متكررة مقابل مؤقتة",
"expl_ar": "الماضي البسيط للأفعال المتكررة العادية (I went to school every day)، والماضي المستمر للأفعال المؤقتة أو التي لم تكن معتادة (That year I was working hard).",
"expl_en": "Simple = repeated habits; continuous = temporary actions around a time.",
"formula": "habit: past simple | temporary: past continuous",
"examples": [
("When I was a child, I played every day.", "عندما كنت طفلا كنت ألعب كل يوم."),
("In 2019 I was working in a different city.", "في سنة 2019 كنت أعمل في مدينة أخرى."),
("She was still studying when I called.", "كانت ما تزال تدرس عندما اتصلت.")]},
]
},
# ============================ NIVEAU 46 ============================
{
"num": 46, "cefr": "B1",
"category": "Used To",
"category_ar": "used to",
"title_en": "Used to (Past Habits and States)",
"title_ar": "used to (العادات والحالات الماضية)",
"ideas": [
{
"en": "Form: used to + base verb",
"ar": "التشكيل: used to + فعل أصلي",
"expl_ar": "used to يعبر عن عادة أو حالة في الماضي لم تعد موجودة: I used to play football (كنت ألعب كرة القدم سابقا).\nيليه الفعل في أصله سواء للفاعل المفرد أو الجمع.",
"expl_en": "Used to + base verb for past habits/states that no longer exist.",
"formula": "subject + used to + base verb",
"examples": [
("I used to play football every day.", "كنت ألعب كرة القدم كل يوم."),
("She used to live in Algiers.", "كانت تسكن في الجزائر العاصمة."),
("We used to watch cartoons together.", "كنا نشاهد الرسوم المتحركة معا.")]},
{
"en": "Negative: didn't use to",
"ar": "النفي: didn't use to",
"expl_ar": "النفي يكون بـ didn't use to (لاحظ: بدون d في use): I didn't use to like coffee (لم أكن أحب القهوة سابقا).",
"expl_en": "Negative: didn't + use to + base verb (no 'd' on use).",
"formula": "subject + didn't + use to + base verb",
"examples": [
("I didn't use to like vegetables.", "لم أكن أحب الخضروات من قبل."),
("She didn't use to wake up early.", "لم تكن تستيقظ مبكرا سابقا."),
("They didn't use to have a car.", "لم تكن لديهم سيارة سابقا.")]},
{
"en": "Questions: Did you use to...?",
"ar": "السؤال: Did you use to...؟",
"expl_ar": "للسؤال: Did you use to smoke? (هل كنت تدخن؟)، Where did you use to live?\nوكثيرا ما نستعمل used to مع never و always.",
"expl_en": "Question: Did + subject + use to + base verb?",
"formula": "Did + subject + use to + base verb?",
"examples": [
("Did you use to live in the countryside?", "هل كنت تسكن في الريف؟"),
("Where did they use to go in summer?", "أين كانوا يذهبون صيفا؟"),
("Did she use to drive to work?", "هل كانت تقود إلى العمل؟")]},
{
"en": "Used to vs past simple",
"ar": "used to مقابل الماضي البسيط",
"expl_ar": "used to يركز على عادة ماضية منتهية (توقفنا عنها)، بينما الماضي البسيط يذكر الحدث ببساطة.\nكلاهما صحيح لكن used to أنسب لهذه العادات المنتهية.",
"expl_en": "Used to emphasizes a finished past habit; past simple states the fact.",
"formula": "used to + verb (finished habit)",
"examples": [
("I used to smoke, but now I don't.", "كنت أدخن، لكن الآن لا."),
("I smoked at university many times.", "دخنت في الجامعة مرات كثيرة."),
("We used to visit our grandparents every Friday.", "كنا نزور أجدادنا كل جمعة.")]},
{
"en": "Used to for past states",
"ar": "used to للحالات الماضية",
"expl_ar": "نستعمل used to أيضا للحالات في الماضي (غير العادات): I used to have long hair (كان شعري طويلا)، There used to be a cinema here (كانت هناك صالة سينما هنا).",
"expl_en": "Used to for past states too: I used to have long hair.",
"formula": "used to + verb/be for past states",
"examples": [
("I used to have a bicycle.", "كانت لدي دراجة هوائية."),
("There used to be a school here.", "كانت توجد مدرسة هنا."),
("He used to be very shy.", "كان خجولا جدا سابقا.")]},
{
"en": "Used to vs be/get used to",
"ar": "used to مقابل be/get used to",
"expl_ar": "انتبه للفرق: used to + فعل = عادة ماضية منتهية.\nأما be used to / get used to + ing (أو اسم) = معتاد على شيء الآن: I'm used to the cold (أنا معتاد على البرد).",
"expl_en": "used to + verb = past habit. be/get used to + -ing = accustomed now.",
"formula": "used to + verb (past) | be used to + -ing (accustomed)",
"examples": [
("I used to get up late.", "كنت أستيقظ متأخرا."),
("I'm not used to getting up early.", "لست معتادا على الاستيقاظ المبكر."),
("She got used to living in a big city.", "اعتادت العيش في مدينة كبيرة.")]},
]
},
# ============================ NIVEAU 47 ============================
{
"num": 47, "cefr": "B1",
"category": "Modals: Should",
"category_ar": "الأفعال الناقصة: should",
"title_en": "Modals: Should and Shouldn't (Advice)",
"title_ar": "الأفعال الناقصة: should (نصيحة)",
"ideas": [
{
"en": "Should + base verb (advice)",
"ar": "should + فعل أصلي (نصيحة)",
"expl_ar": "should يعبر عن النصيحة أو التوصية: You should drink water (يجب أن تشرب الماء).\nيليه الفعل في أصله ولا يتغير مع الفاعل.",
"expl_en": "Should + base verb = advice or recommendation.",
"formula": "subject + should + base verb",
"examples": [
("You should drink more water.", "يجب أن تشرب ماء أكثر."),
("She should see a doctor.", "يجب أن تذهب إلى الطبيب."),
("We should arrive early.", "يجب أن نصل مبكرا.")]},
{
"en": "Negative: shouldn't",
"ar": "النفي: shouldn't",
"expl_ar": "النفي: should not / shouldn't = «لا ينبغي»: You shouldn't smoke (لا ينبغي أن تدخن).\nننصح بعدم فعل شيء.",
"expl_en": "shouldn't = it is not a good idea / not advisable.",
"formula": "subject + shouldn't + base verb",
"examples": [
("You shouldn't eat too much sugar.", "لا ينبغي أن تأكل سكرا كثيرا."),
("He shouldn't drive so fast.", "لا ينبغي أن يقود بهذه السرعة."),
("We shouldn't waste water.", "لا ينبغي أن نهدر الماء.")]},
{
"en": "Questions: Should I...?",
"ar": "السؤال: Should I...؟",
"expl_ar": "لطلب النصيحة: Should I apply for the job? (هل يجب أن أتقدم للوظيفة؟)، Where should we go? بمعنى «برأيك؟».",
"expl_en": "Question: Should I...? = asking for advice.",
"formula": "Should + subject + base verb?",
"examples": [
("Should I tell him the truth?", "هل يجب أن أخبره الحقيقة؟"),
("What should we do now?", "ماذا يجب أن نفعل الآن؟"),
("Should she accept the invitation?", "هل يجب أن تقبل الدعوة؟")]},
{
"en": "Deduction: should be (expectation)",
"ar": "الاستنتاج: should be (توقع)",
"expl_ar": "should يستعمل أحيانا للتوقع المنطقي: He should be home by now (يفترض أن يكون في البيت الآن).\nالفرق عن must = توقع قوي.",
"expl_en": "Should can express expectation: He should be home by now.",
"formula": "should + be/arrive etc. (logical expectation)",
"examples": [
("The train should be here soon.", "يفترض أن يصل القطار قريبا."),
("She should know the answer.", "من المفترض أن تعرف الجواب."),
("The letter should arrive tomorrow.", "يفترض أن تصل الرسالة غدا.")]},
{
"en": "Giving strong advice: really should / must",
"ar": "نصيحة قوية: really should / must",
"expl_ar": "لنصيحة أقوى نضيف really: You really should see a doctor (حقا يجب أن تذهب للطبيب)، أو نستعمل must للالتزام القوي.",
"expl_en": "For stronger advice: You really should... (or must).",
"formula": "subject + really should + base verb",
"examples": [
("You really should take a break.", "حقا يجب أن تأخذ استراحة."),
("We really should book the hotel soon.", "حقا يجب أن نحجز الفندق قريبا."),
("You must see that new film!", "يجب أن تشاهد ذلك الفيلم الجديد!")]},
{
"en": "Giving advice: polite forms",
"ar": "تقديم النصيحة بأسلوب مهذب",
"expl_ar": "لتقديم النصيحة بلطف نقول: You could try...، If I were you, I would...، Why don't you...?\nكلها أسهل وألطف من should المباشر.",
"expl_en": "Polite advice: You could... / If I were you, I'd... / Why don't you...?",
"formula": "You could + verb | If I were you, I'd + verb",
"examples": [
("If I were you, I'd take this job.", "لو كنت مكانك، لقبلت هذه الوظيفة."),
("Why don't you talk to your teacher?", "لماذا لا تتحدث مع معلمك؟"),
("You could try a different method.", "يمكنك أن تجرب طريقة مختلفة.")]},
]
},
# ============================ NIVEAU 48 ============================
{
"num": 48, "cefr": "B1",
"category": "Modals: Must and Have To",
"category_ar": "الأفعال الناقصة: must و have to",
"title_en": "Modals: Must / Have to (Obligation and Prohibition)",
"title_ar": "must و have to (الوجوب والمنع)",
"ideas": [
{
"en": "Must + base verb (obligation)",
"ar": "must + فعل أصلي (وجوب)",
"expl_ar": "must يعبر عن الوجوب القوي (من المتكلم أو القواعد): You must wear a helmet (يجب أن ترتدي الخوذة).\nيليه الفعل في أصله.",
"expl_en": "Must = strong obligation (rules, orders).",
"formula": "subject + must + base verb",
"examples": [
("You must wear a seatbelt.", "يجب أن تضع حزام الأمان."),
("Students must arrive on time.", "يجب على الطلاب أن يصلوا في الوقت."),
("I must finish this work today.", "يجب أن أنهي هذا العمل اليوم.")]},
{
"en": "Have to + base verb (obligation)",
"ar": "have to + فعل أصلي (وجوب)",
"expl_ar": "have to يعبر عن الوجوب الخارجي (القوانين، الظروف): I have to be at work at 8 (يجب أن أكون في العمل في الثامنة — بسبب العمل).\nيتغير مع الفاعل: has to مع he/she/it.",
"expl_en": "Have to = external obligation. Has to with he/she/it.",
"formula": "subject + have/has to + base verb",
"examples": [
("I have to get up early for work.", "يجب أن أستيقظ مبكرا للعمل."),
("She has to wear a uniform at school.", "يجب أن ترتدي الزي المدرسي."),
("We have to pay the bill by Friday.", "يجب أن ندفع الفاتورة قبل الجمعة.")]},
{
"en": "Must vs have to: the difference",
"ar": "الفرق بين must و have to",
"expl_ar": "must = وجوب شخصي/رأي المتكلم، have to = وجوب خارجي/قاعدة.\nMust للمتحدث عن نفسه، have to لما يفرضه الآخرون أو الواقع.",
"expl_en": "Must = internal/personal; have to = external/rule.",
"formula": "must (personal) | have to (external)",
"examples": [
("I must study more. (my decision)", "يجب أن أدرس أكثر (قرار شخصي)."),
("I have to study more. (the rules)", "يجب أن أدرس أكثر (القواعد تقتضي ذلك)."),
("You must see a doctor. (my advice)", "يجب أن تذهب للطبيب.")]},
{
"en": "Negative: mustn't (prohibition)",
"ar": "النفي: mustn't (منع)",
"expl_ar": "mustn't = ممنوع تماما (prohibition): You mustn't smoke here (ممنوع التدخين هنا).\nأما don't have to = ليس عليك (أي غير إجباري).",
"expl_en": "mustn't = forbidden. don't have to = not necessary.",
"formula": "mustn't + verb (forbidden) | don't have to + verb (not necessary)",
"examples": [
("You mustn't enter the room.", "ممنوع دخول الغرفة."),
("You needn't / don't have to wait.", "ليس عليك الانتظار."),
("They mustn't make noise here.", "يجب ألا يحدثوا ضجيجا هنا.")]},
{
"en": "Have to in past and future",
"ar": "have to في الماضي والمستقبل",
"expl_ar": "not have to في الماضي = did not have to (لم يكن عليَّ)، في المستقبل = will have to (سيتوجب عليَّ).\nأما must ليس له ماضٍ فرمي، نستعمل had to.",
"expl_en": "Past: had to / didn't have to. Future: will have to.",
"formula": "had to / didn't have to + verb | will have to + verb",
"examples": [
("Yesterday I had to stay late.", "أمس كان عليَّ البقاء متأخرا."),
("I didn't have to pay for the ticket.", "لم يكن عليَّ دفع ثمن التذكرة."),
("You will have to renew your passport.", "سيتوجب عليك تجديد جواز سفرك.")]},
{
"en": "Questions: Do I have to...?",
"ar": "السؤال: Do I have to...؟",
"expl_ar": "السؤال عن الوجوب: Do I have to come? (هل يجب أن آتي؟)، Do we have to pay?\nلا نستعمل must عادة في السؤال.",
"expl_en": "Question: Do/Does + subject + have to + verb?",
"formula": "Do/Does + subject + have to + base verb?",
"examples": [
("Do I have to bring my books?", "هل يجب أن أحضر كتبي؟"),
("Does she have to work on Saturday?", "هل يجب أن تعمل يوم السبت؟"),
("Do we have to book a table?", "هل يجب أن نحجز طاولة؟")]},
]
},
# ============================ NIVEAU 49 ============================
{
"num": 49, "cefr": "B1",
"category": "Modals: May, Might, Could",
"category_ar": "الأفعال الناقصة: may, might, could",
"title_en": "Modals: May / Might / Could (Possibility)",
"title_ar": "may و might و could (إمكانية)",
"ideas": [
{
"en": "May + base verb (possibility)",
"ar": "may + فعل أصلي (احتمال)",
"expl_ar": "may يعبر عن احتمال في الحاضر أو المستقبل: She may come (قد تأتي).\nأحيانا بمعنى «ربما» وهو أكثر تأكيدا من might قليلا.",
"expl_en": "May = possibility. She may come = perhaps she will come.",
"formula": "subject + may + base verb",
"examples": [
("She may arrive late.", "قد تصل متأخرة."),
("It may rain tomorrow.", "قد تمطر غدا."),
("They may accept the offer.", "قد يقبلون العرض.")]},
{
"en": "Might + base verb (less certain)",
"ar": "might + فعل أصلي (أقل تأكيدا)",
"expl_ar": "might يعبر عن احتمال أضعف: He might be at home (ربما هو في البيت، لست متأكدا).\nكثيرا ما نستعمله مع maybe (ربما) و perhaps (ربما).",
"expl_en": "Might = weaker possibility. Could also be used.",
"formula": "subject + might + base verb",
"examples": [
("He might be sleeping now.", "ربما هو نائم الآن."),
("We might go camping this weekend.", "ربما نذهب للتخييم هذا الأسبوع."),
("She might not agree with us.", "ربما لا توافقنا الرأي.")]},
{
"en": "Could + base verb (general/future possibility)",
"ar": "could + فعل أصلي (إمكانية عامة)",
"expl_ar": "could يعبر عن إمكانية عامة: The test could be easy (قد يكون الاختبار سهلا).\nفي الماضي نستعمل could have: could have been (ربما كان).",
"expl_en": "Could = general possibility, present or future.",
"formula": "subject + could + base verb",
"examples": [
("The meeting could be delayed.", "قد يتأخر الاجتماع."),
("Prices could go up next year.", "قد ترتفع الأسعار السنة القادمة."),
("She could be at the library now.", "قد تكون في المكتبة الآن.")]},
{
"en": "Negative: may not / might not",
"ar": "النفي: may not / might not",
"expl_ar": "النفي: may not (قد لا) / might not (ربما لا): He may not come (قد لا يأتي)، She might not like it.\nانتبه: mustn't = منع، أما may not = احتمال عدم.",
"expl_en": "may not / might not = perhaps not. Not prohibition here.",
"formula": "subject + may/might not + base verb",
"examples": [
("He may not come to the party.", "قد لا يأتي إلى الحفلة."),
("They might not accept the price.", "ربما لا يقبلون السعر."),
("She may not have enough time.", "قد لا يكون لديها وقت كاف.")]},
{
"en": "Asking for/giving permission",
"ar": "طلب وإعطاء الإذن",
"expl_ar": "may للطلب المهذب الرسمي: May I come in? (أيمكنني الدخول؟)، May I use your phone? الرد: Yes, you may. / No, you might not (أو may not).",
"expl_en": "May I...? = asking permission (formal/polite).",
"formula": "May + subject + base verb?",
"examples": [
("May I open the window?", "أيمكنني فتح النافذة؟"),
("May I borrow your pen?", "أيمكنني استعارة قلمك؟"),
("May we leave early today?", "أيمكننا المغادرة مبكرا اليوم؟")]},
{
"en": "Polite requests: Could you...?",
"ar": "طلبات مهذبة: Could you...؟",
"expl_ar": "لطلب مهذب جدا: Could you help me? (أيمكنك مساعدتي؟)، Could you pass the salt? ألطف من can you.",
"expl_en": "Could you...? = very polite request.",
"formula": "Could + subject + base verb?",
"examples": [
("Could you help me with this bag?", "أيمكنك مساعدتي مع هذه الحقيبة؟"),
("Could you open the door for me?", "أيمكنك فتح الباب لي؟"),
("Could you repeat that, please?", "أيمكنك إعادة ذلك من فضلك؟")]},
]
},
# ============================ NIVEAU 50 ============================
{
"num": 50, "cefr": "B1",
"category": "First Conditional",
"category_ar": "الجملة الشرطية الأولى",
"title_en": "First Conditional",
"title_ar": "الجملة الشرطية الأولى",
"ideas": [
{
"en": "Structure: If + present, will + verb",
"ar": "التركيب: If + مضارع بسيط، will + فعل",
"expl_ar": "الجملة الشرطية الأولى تعبر عن نتيجة محتملة في المستقبل: If it rains, I will stay home (إذا أمطرت سأبقى في البيت).\nالماضي في العربية لا يضللنا، فالتركيب إنجليزي: if + present ⟶ will.",
"expl_en": "First conditional = probable future result: If + present + will.",
"formula": "If + present simple, + will + base verb",
"examples": [
("If it rains, I will stay home.", "إذا أمطرت، سأبقى في البيت."),
("If you study, you will pass.", "إذا درست، ستنجح."),
("If she calls, I will answer.", "إذا اتصلت، سأجيب.")]},
{
"en": "Reverse order (comma rules)",
"ar": "الترتيب المعكوس (قاعدة الفاصلة)",
"expl_ar": "إذا بدأنا بـ if نضع فاصلة: If you hurry, you will catch it.\nإذا بدأنا بالنتيجة لا فاصلة: You will catch it if you hurry.",
"expl_en": "Comma after the if-clause when it comes first.",
"formula": "If + clause, + will-clause | will-clause + if + clause",
"examples": [
("If you hurry, you will catch the bus.", "إذا أسرعت، ستلحق بالحافلة."),
("You will catch the bus if you hurry.", "ستلحق بالحافلة إذا أسرعت."),
("If he helps, we will finish early.", "إذا ساعد، سننهي مبكرا.")]},
{
"en": "First conditional with unless",
"ar": "الجملة الشرطية الأولى مع unless",
"expl_ar": "unless = if...not (إلا إذا): You will fail unless you study = if you don't study (ستفشل إلا إذا درست).",
"expl_en": "Unless = if...not. You'll fail unless you study.",
"formula": "will + verb + unless + present simple",
"examples": [
("You will miss the train unless you hurry.", "ستفوت القطار إلا إذا أسرعت."),
("I won't go unless she invites me.", "لن أذهب إلا إذا دعتني."),
("We can't start unless everyone is here.", "لا يمكننا البدء إلا إذا كان الجميع هنا.")]},
{
"en": "Use of imperative/other verbs in result",
"ar": "استعمال فعل الأمر وغيره في النتيجة",
"expl_ar": "في النتيجة نستعمل will، أو can، أو may، أو فعل أمر: If you finish, you can go (إن أنهيت يمكنك الذهاب)، If you need help, tell me (إن احتجت مساعدة قل لي).",
"expl_en": "Result can use will, can, may, or an imperative.",
"formula": "If + present, + will/can/may/imperative",
"examples": [
("If you need help, call me.", "إذا احتجت مساعدة، اتصل بي."),
("If you finish early, you can leave.", "إذا أنهيت مبكرا يمكنك المغادرة."),
("If she agrees, we may start.", "إذا وافقت، قد نبدأ.")]},
{
"en": "First conditional in warnings",
"ar": "الجملة الشرطية الأولى في التحذير",
"expl_ar": "كثيرا ما نستعملها للتحذير أو النصيحة: If you touch that, you will get hurt (إن لمست ذلك ستؤذى).",
"expl_en": "Used for warnings and promises.",
"formula": "If + present, + will + verb (warning)",
"examples": [
("If you drive fast, you will have an accident.", "إذا قدت بسرعة فستتعرض لحادث."),
("If you don't sleep, you will be tired.", "إذا لم تنم فستكون متعبا."),
("If you eat too much, you will feel sick.", "إذا أكلت كثيرا فستشعر بالمرض.")]},
{
"en": "First conditional with future time words",
"ar": "الجملة الشرطية الأولى مع كلمات المستقبل",
"expl_ar": "في شرط الجملة الأولى نستعمل المضارع البسيط وليس will: if it rains (وليس if it will rain)، حتى لو كانت الجملة عن المستقبل.\nالنتيجة هي التي تأخذ will.",
"expl_en": "Never use 'will' in the if-clause, only in the result.",
"formula": "If + present (even about future) + will + verb",
"examples": [
("If I have time, I'll visit you tomorrow.", "إذا كان لدي وقت، سأزورك غدا."),
("If they arrive early, we will start first.", "إذا وصلوا مبكرا، سنبدأ أولا."),
("If it snows this winter, we will ski.", "إذا ثلج هذا الشتاء، سنتزلج.")]},
]
},
]
