# -*- coding: utf-8 -*-
"""النطق العربي للجمل الإنجليزية — translittération anglais → arabe (approximation pédagogique)."""

PRON = {
"a":"آ","an":"آن","the":"ذا","this":"ذيس","that":"ذات","these":"ذيز","those":"ذوز",
"my":"ماي","your":"يور","yours":"يورز","his":"هيز","her":"هور","hers":"هورز","its":"إتس",
"our":"آور","ours":"آورز","their":"ذير","theirs":"ذيرز","mine":"ماين",
"i":"آي","you":"يو","he":"هي","she":"شي","it":"إت","we":"وي","they":"ذاي",
"me":"مي","him":"هيم","us":"آس","them":"ذيم","who":"هو","whose":"هوز",
"what":"وات","which":"ويتش","where":"وير","when":"وين","why":"واي","how":"هاو",
"is":"إيز","are":"آر","was":"واز","were":"وير","be":"بي","been":"بين","being":"بينغ",
"do":"دو","does":"داز","did":"ديد","doing":"دوينغ","done":"دان",
"have":"هاف","has":"هاز","had":"هاد","having":"هافينغ","will":"ويل","would":"وود",
"can":"كان","could":"كود","may":"ماي","might":"مايت","should":"شود","must":"ماست",
"no":"نو","not":"نوت","yes":"ييس","so":"سو","too":"تو","very":"فيري","really":"ريلي",
"don't":"دونت","doesn't":"دازنت","didn't":"ديدنت","isn't":"إيزنت","aren't":"آرنت",
"wasn't":"وازنت","weren't":"ويرنت","haven't":"هافنت","hasn't":"هازنت","won't":"وونت",
"can't":"كانت","wouldn't":"وودنت","couldn't":"كوودنت","shouldn't":"شودنت",
"in":"إين","on":"أون","at":"آت","to":"تو","of":"آف","from":"فروم","by":"باي","for":"فور",
"with":"ويذ","without":"ويذاوت","about":"أباوت","after":"أفتير","before":"بيفور",
"between":"بيتوين","under":"أندير","over":"أوفير","above":"أبوف","below":"بيلو",
"behind":"بيهيند","beside":"بيسايد","near":"نير","around":"أراوند","into":"إينتو",
"onto":"أونتو","up":"آب","down":"داون","out":"آوت","off":"أوف","away":"أواي",
"and":"آند","but":"بات","or":"أور","because":"بيكوز","if":"إيف","while":"وايل",
"then":"ذين","than":"ذان","as":"آز","also":"أولسو","now":"ناو","here":"هير","there":"ذير",
"again":"أغين","always":"أولويز","never":"نيفير","often":"أوفن","usually":"يوجوالي",
"sometimes":"سامتايمز","just":"جاست","even":"إيفن","only":"أونلي","once":"وانس",
"today":"توداي","tomorrow":"تومورو","yesterday":"يسترداي","tonight":"تونات","soon":"سون",
"later":"ليتير","early":"إيرلي","first":"فيرست","last":"لاست","next":"نايكست",
"every":"إيفري","everyone":"إيفريوان","everything":"إيفريثينغ","everywhere":"إيفريوير",
"someone":"ساموان","something":"سامثينغ","somewhere":"ساموير",
"anyone":"إينيوون","anything":"إينيثينغ","anywhere":"إينيوير",
"nothing":"ناثينغ","nobody":"نوبودي","each":"إيتش","all":"أول",
"both":"باوث","some":"سام","any":"إني","more":"مور","most":"ماوست","few":"فيو",
"many":"ماني","much":"ماتش","little":"ليتل","another":"أناذر","other":"أذير",
"hello":"هيلو","hi":"هاي","goodbye":"غودباي","bye":"باي","please":"بليز",
"sorry":"سوري","thanks":"ثانكس","thank":"ثانك","excuse":"إكسكوس","welcome":"ويلكام",
"good":"غود","nice":"نايس","fine":"فاين","well":"ويل","okay":"أوكاي","great":"غريت",
"better":"بيتر","best":"بست","bad":"باد","worst":"ورست","big":"بيغ","bigger":"بيغير",
"biggest":"بيغوست","small":"سمول","smaller":"سمولير","tall":"تول","taller":"تولير",
"tallest":"تولوست","short":"شورت","shorter":"شورتير","long":"لونغ","longer":"لونغير",
"longest":"لونغوست","old":"أولد","older":"أولدير","oldest":"أولدست","young":"يانغ",
"new":"نيو","newer":"نيوير","happy":"هابي","happier":"هابيير","happiest":"هابيست",
"sad":"ساد","hungry":"هانغري","thirsty":"ثيرستي","tired":"تايرد","hot":"هوت",
"hotter":"هوتير","hottest":"هوتست","cold":"كولد","colder":"كولدير","clever":"كليفير",
"easy":"إيزي","easier":"إيزيير","easiest":"إيزيست","hard":"هارد","harder":"هاردير",
"fast":"فاست","faster":"فاستير","fastest":"فاستست","important":"إمبورتن",
"beautiful":"بيوتيفول","pretty":"بريتي","interesting":"إنتيريستينغ","difficult":"ديفيكولت",
"expensive":"إكسبنسيف","cheap":"تشيب","cheaper":"تشيبر","cheapest":"تشيبست",
"clean":"كلين","cleaner":"كلينير","cleanest":"كلينست","light":"لايت","lighter":"لايتير",
"lightest":"لايتست","quiet":"كوايت","delicious":"ديليشس","special":"سبيشال",
"nearest":"نييست","favourite":"فيوفريت","cozy":"كوزي",
"one":"وان","two":"تو","three":"ثري","four":"فور","five":"فايف","six":"سيكس",
"seven":"سفن","eight":"إيت","nine":"ناين","ten":"تن","eleven":"إليفن","twelve":"تويلف",
"twenty":"توينتي","thirty":"ثيرتي","forty":"فورتي","fifty":"فيفتي","sixty":"سيكستي",
"seventy":"سفنتي","eighty":"إيتي","ninety":"ناينتي","hundred":"هاندراد",
"thousand":"ثاوزند",
"sunday":"سنداي","monday":"مانداي","tuesday":"تيوسداي","wednesday":"ونزداي","thursday":"ثالزداي",
"friday":"فرايداي","saturday":"ساترداي",
"january":"جانوياري","february":"فيبريواري","march":"مارتش","april":"إيبريل",
"june":"جون","july":"جولاي","august":"أوغست","september":"سيبتيمبر",
"october":"أكتوبر","november":"نوفيمبر","december":"ديسيمبر",
"summer":"سامير","winter":"وينتير","spring":"سبرينغ","autumn":"أوتوم",
"algeria":"ألجيريا","algiers":"ألجيرز","oran":"أوران","mostaganem":"موستاغنيم",
"madani":"مداني","oussama":"أوساما","islem":"إسلام","anes":"أنس","belacel":"بلاسل",
"student":"ستيودنت","students":"ستيودنتس","teacher":"تيتشر","teachers":"تيتشيرز",
"pupil":"بيوبيل","friend":"فريند","friends":"فريندز","family":"فاميلي","mother":"ماذر",
"father":"فاذر","brother":"براذر","sister":"سيستير","grandmother":"غراندماذر",
"grandfather":"غراندفاذر","parents":"بارنتس","child":"تشايلد","children":"تشيلدرن",
"man":"مان","men":"من","woman":"ومن","women":"ومن","boy":"بوي","boys":"بويز",
"girl":"غيرل","person":"بيرسون","people":"بيبل","name":"نيم","age":"إيج","town":"تاون",
"country":"كانتري","city":"سيتي","cities":"سيتيز","school":"سكول","class":"كلاس",
"classroom":"كلاسروم","book":"بوك","books":"بوكس","pen":"بن","pens":"بينز",
"pencil":"بنسل","pencils":"بنسلز","basket":"باسكيت","doctor":"داكتور",
"engineer":"إنجينير","farmer":"فارمير","nurse":"نورس","pilot":"بايلوت","manager":"ماناجير",
"actor":"أكتور","dentist":"دانتيست","cook":"كوك","driver":"درايفر","worker":"وركير",
"house":"هاوس","houses":"هاوزز","room":"روم","rooms":"رومز","door":"دور","doors":"دورز",
"window":"ويندو","windows":"ويندوز","table":"تيبل","chair":"تشير","chairs":"تشيرز",
"bed":"باد","bedroom":"بادروم","kitchen":"كيتشين","bathroom":"باتروم","garden":"غاردن",
"water":"ووتر","milk":"ميلك","bread":"بريد","cheese":"تشيز","eggs":"إغز","cake":"كيك",
"cakes":"كايكس","tea":"تي","coffee":"كوفي","sugar":"شوغر","salt":"سولت","fruit":"فروت",
"apple":"أبل","apples":"أبلز","banana":"بانانا","bananas":"باناناز","orange":"أورنج",
"oranges":"أورنجز","tomato":"توماتو","tomatoes":"توماتوز","potato":"بوتيتو",
"potatoes":"بوتيتوز","rice":"رايس","couscous":"كوسكوس","chicken":"تشيكن","fish":"فيش",
"meat":"ميت","carrot":"كاروت","onion":"أونيان","juice":"جوس","date":"ديت","dates":"ديتس",
"olive":"أوليف","honey":"هوني","walnut":"وولنوت",
"home":"هوم","homes":"هومز","work":"وورك","job":"جوب","jobs":"جوبز",
"office":"أوفيس","hospital":"هوسبيتل","market":"ماركيت","museum":"ميوزيوم",
"station":"ستيشين","airport":"إييربورت","restaurant":"ريستورانت","cafe":"كافي",
"shop":"شوب","shops":"شوبس","store":"ستور","library":"لايبراري","park":"بارك",
"zoo":"زو","hotel":"هوتيل","mosque":"موسك","bank":"بانك","office":"أوفيس",
"pharmacy":"فارماسي","supermarket":"سوبرماركيت",
"car":"كار","cars":"كارز","bus":"باس","busy":"بيزي","bike":"بايك","plane":"بلين",
"planes":"بلينز","train":"ترين","tram":"ترام","taxi":"تاكسي","sea":"سي","beach":"بيتش",
"mountain":"ماونتن","mountains":"ماونتنز","river":"ريفير","forest":"فوريست",
"desert":"ديزيرت","sky":"سكاي","sun":"سان","moon":"مون","star":"ستار","stars":"ستارز",
"rain":"رين","rains":"رينز","snow":"سنو","wind":"ويند","air":"إيير",
"flower":"فلاور","flowers":"فلاورز","tree":"تري","trees":"تريز",
"bird":"بيرد","birds":"بيردز","cat":"كات","cats":"كاتس","dog":"دوغ","horse":"هورس",
"sheep":"شيب","camel":"كاميل","wall":"وول",
"foot":"فوت","feet":"فيت","hand":"هاند","hands":"هاندز","head":"هيد","eyes":"آيز",
"hair":"هير","face":"فايس","arm":"أرم","red":"ريد","green":"غرين","blue":"بلو",
"white":"وايت","black":"بلاك","yellow":"يلو","grey":"غري","brown":"براون","pink":"بينك",
"purple":"بيربل","shirt":"شيرت","shirts":"شيرتس","shoes":"شوز","hat":"هات",
"jacket":"جاكيت","coat":"كوت","dress":"دريس","trousers":"تراوزرز","jeans":"جينز",
"scissors":"سيزورز","watch":"ووتش","watches":"ووتشز","phone":"فون","mobile":"موبايل",
"computer":"كومبيوتر","laptop":"لابتوپ","radio":"راديو","tv":"تي في","games":"غيمز",
"game":"غيم","ball":"بول","doll":"دول","toy":"توي","toys":"تويز","gift":"غيفت",
"gifts":"غيفتس","present":"بريزنت","presents":"بريزنتس","money":"ماني","kite":"كايت",
"puzzle":"بازل","puzzles":"بازلز","color":"كالور","colours":"كالورز",
"time":"تايم","times":"تايمز","day":"داي","days":"دايز","week":"ويك","weeks":"ويكس",
"year":"يير","years":"ييرز","month":"مانث","months":"مانثس","hour":"أور","hours":"أورز",
"minute":"مينيت","minutes":"مينيتس","morning":"مورنينغ","afternoon":"أفتيرنون",
"evening":"إيفنينغ","night":"نايت","noon":"نون","midday":"ميدداي","midnight":"ميدنايت",
"weekend":"ويكيند","weekdays":"ويكدايز","o'clock":"أوكلوك",
"alphabet":"ألفابيت","letter":"ليتر","letters":"ليتيرز","word":"وورد","words":"ووردز",
"vowel":"فاول","vowels":"فاولز","consonant":"كونسوننت","consonants":"كونسوننتس",
"sound":"ساوند","sounds":"ساوندز","verb":"فيرب","question":"كويسشن","questions":"كويسشنز",
"answer":"أنسير","answers":"أنسيرز","sentence":"سينتنس","sentences":"سينتنسز",
"correct":"كوريكت","wrong":"رونغ","spell":"سبيل","spelling":"سبيلينغ","read":"ريد",
"reading":"ريدينغ","write":"رايت","writing":"رايتينغ","listen":"ليسن",
"listening":"ليسنينغ","speak":"سبيك","speaking":"سبيكينغ","repeat":"ريبيت",
"translate":"ترانسلت","translation":"ترانسلشن",
"arrive":"أرايف","arrived":"أرايفد","remember":"ريميمبر","forget":"فورغيت",
"play":"بلاي","plays":"بلايز","played":"بلايد","playing":"بلايينغ",
"worked":"ووركد","working":"ووركينغ","sleep":"سليب","sleeps":"سليبس","slept":"سليبت",
"sleeping":"سليبينغ","wake":"ويك","wakes":"ويكس","woke":"ووك","waking":"ويكينغ",
"eat":"إيت","eats":"إيتس","ate":"إيت","eating":"إيتينغ","drink":"درينك","drinks":"درينكس",
"drank":"درانك","drinking":"درينكينغ","cooked":"كوكت","cooking":"كوكنغ","cooks":"كوكس",
"wash":"ووش","washes":"ووشز","washing":"ووشينغ","cleaned":"كليند","cleaning":"كلينينغ",
"walks":"ووكس","walked":"ووكت","walking":"ووكينغ","walk":"ووك","run":"ران","runs":"رانز",
"running":"رانينغ","swim":"سويم","swimming":"سويمينغ","fly":"فلاي","flies":"فلايز",
"flying":"فلايينغ","drive":"درايف","drives":"درايفز","driving":"درايفينغ","drove":"دروف",
"ride":"رايد","riding":"رايدينغ","travel":"ترافل","travelling":"ترافلينغ","go":"غو",
"goes":"غوز","going":"غوينغ","went":"وينت","come":"كام","comes":"كامز","came":"كايم",
"coming":"كامينغ","look":"لوك","looks":"لوكس","looked":"لوكت","looking":"لوكينغ",
"see":"سي","sees":"سيز","seeing":"سينغ","saw":"صو","seen":"سين","watched":"ووتشد",
"watching":"ووتشينغ","hear":"هير","hearing":"هيرينغ","smell":"سميل","taste":"تايسنت",
"feel":"فيل","wait":"ويت","waits":"ويتس","waiting":"ويتينغ","study":"ستادي",
"studies":"ستاديز","studied":"ستاديد","studying":"ستادينغ","learn":"ليرن",
"learning":"ليرنينغ","learned":"ليرند","teach":"تيتش","teaches":"تيتشز",
"teaching":"تيتشينغ","like":"لايك","likes":"لايكس","liked":"لايكت","liking":"لايكينغ",
"love":"لاف","loves":"لافز","loved":"لافد","loving":"لافينغ","hate":"هيت","hates":"هيتس",
"want":"وانت","wants":"وانتس","wanted":"وانتيد","need":"نيد","needs":"نيدز",
"needed":"نيديد","think":"ثينك","thinks":"ثينكس","thought":"ثوت","know":"نو","knows":"نوز",
"knew":"نيو","knowing":"نوينغ","believe":"بيليف","believes":"بيليفز","say":"ساي",
"says":"سيز","said":"ساد","saying":"سايينغ","tell":"تيل","tells":"تيلز","told":"تولد",
"ask":"آسك","asks":"آسكس","asked":"آسكت","asking":"آسكينغ","answered":"أنسيرد",
"give":"غيف","gives":"غيفز","gave":"جيف","giving":"غيفينغ","take":"تيك","takes":"تيكس",
"took":"توك","taking":"تيكينغ","get":"غيت","gets":"غيتس","got":"غوت","getting":"غيتينغ",
"make":"مايك","makes":"مايكس","made":"مايد","making":"مايكينغ","put":"بوت","puts":"بوتس",
"open":"أوبن","opens":"أوبنز","opened":"أوبند","opening":"أوبنينغ","close":"كلوز",
"closes":"كلوزز","closed":"كلوزد","closing":"كلوزينغ","buy":"باي","buys":"بايز",
"bought":"بوت","buying":"بايينغ","sell":"سيل","sells":"سيلز","sold":"سولد","pay":"باي",
"paid":"بايد","find":"فايند","finds":"فايندز","found":"فاوند","finding":"فايندينغ",
"lose":"لوز","loses":"لوزز","lost":"لوست","losing":"لوزينغ","win":"وين","wins":"وينز",
"won":"وان","winning":"وينينغ","finish":"فينيش","finishes":"فينيشز","finished":"فينيشد",
"start":"ستار","starts":"ستارز","started":"ستارتد","stop":"ستوب","stops":"ستوبس",
"helped":"هيلبد","helping":"هيلبينغ","help":"هيلب","helps":"هيلبس",
"try":"تراي","tries":"ترايز","tried":"ترايد","trying":"ترايينغ","practise":"براكتيس",
"practising":"براكتيسينغ","use":"يوز","uses":"يوزز","used":"يوزد","using":"يوزينغ",
"visit":"فيزيت","visits":"فيزيتس","visited":"فيزيتد","visiting":"فيزيتينغ",
"live":"ليف","lives":"ليفز","lived":"ليفد","living":"ليفينغ","stay":"ستاي","stays":"ستايز",
"stayed":"ستايد","staying":"ستايينغ","move":"موف","moves":"موفز","moved":"موفد",
"moving":"موفينغ","sit":"سيت","sits":"سيتس","sat":"سات","sitting":"سيتينغ",
"lie":"لاي","lies":"لايز","lying":"لايينغ","carry":"كاري","carries":"كاريز",
"carried":"كاريد","smile":"سمايل","smiled":"سمايلد","smiling":"سمايلينغ","cry":"كراي",
"crying":"كرايينغ","call":"كول","calls":"كولز","called":"كولد","calling":"كولينغ",
"talk":"توك","talks":"توكس","talked":"توكت","talking":"توكينغ","spoke":"سبوك",
"hardly":"هار دلي","slowly":"سلو لي","quickly":"كويكلي","carefully":"كيرفالي",
"finally":"فاينالي","news":"نيوز","homework":"هوموورك","sport":"سبورت","sports":"سبورتس",
"football":"فوتبول","match":"ماتش","matches":"ماتشز","team":"تيم","teams":"تيمز",
"player":"بلاير","players":"بلايرز","goal":"غول","goals":"غولز",
"practice":"براكتيس","training":"تراينينغ","pet":"بيت","pets":"بيتس",
"photo":"فوتو","photos":"فوتوز","picture":"بيكتشير","pictures":"بيكتشيرز",
"celebrations":"سيليبريشنز","party":"بارتي","parties":"بارتيز",
"birthday":"بيرثداي","wedding":"ويدينغ","festival":"فيستيفل","eid":"عيد",
"guests":"غيستس","guest":"غيست","invite":"إنفايت","invited":"إنفايتد",
"surprise":"سوربرايز","apartment":"أبارتمنت","flat":"فلات","building":"بيلدينغ",
"floor":"فلور","roof":"روف","street":"ستريت","road":"رود","avenue":"أفينيو","path":"بات",
"bridge":"بريدج","ocean":"أوشن","island":"آيلاند","world":"وورلد",
"map":"ماب","place":"بليس","places":"بليسز","village":"فيليدج",
"capital":"كابيتل","tomb":"توم","cinema":"سينيما","farm":"فارم","field":"فيلد",
"history":"هيستوري","geography":"جيوغرافي","science":"ساينس","maths":"ماتس",
"english":"إينغليش","arabic":"عربي","french":"فرينتش","exam":"إكزام","exams":"إكزامز",
"test":"تيست","tests":"تستس","lesson":"ليسن","lessons":"ليسنس",
"beloved":"بيلافد","dear":"دير","aunt":"آنت","aunt's":"أنتس","uncle":"أنكل",
"cousin":"كازن","cousins":"كازنز","husband":"هازبند","wife":"وايف","mum":"مام",
"mom":"مام","dad":"داد","son":"سان","daughter":"دوتير",
"breakfast":"بريكفاست","lunch":"لانتش","dinner":"دينير","supper":"سابر","meal":"ميل",
"meals":"ميلز","plate":"بليت","spoon":"سبون","fork":"فورك","knife":"نايف","knives":"نايفز",
"glass":"غلاس","cup":"كاب","bottle":"بوتل","box":"بوكس","bags":"باغز","bag":"باغ",
"pieces":"بييسز","piece":"بيس","bit":"بيت","slice":"سلايس","bowl":"بول",
"rainy":"رييني","cloudy":"كلاودي","sunny":"ساني","snowy":"سنوي","stormy":"ستورمي",
"weather":"ويذر","season":"سيزن","seasons":"سيزنز","climate":"كلايميت",
"degree":"ديغري","degrees":"ديغريز","temperature":"تيمبريتشر","warm":"وورن",
"cool":"كول","afraid":"أفريد","excited":"إكسايتد","scared":"سكيرد",
"eye":"آي","ear":"إير","ears":"إيرز","nose":"نوز","mouth":"ماوث","tooth":"توث",
"teeth":"تيث","tongue":"تانغ","neck":"ناك","shoulders":"شولدرز","knees":"نيز",
"fingers":"فينغرز","toes":"توز","leg":"ليغ","legs":"ليغز","bodies":"بوديز",
"body":"بودي","sick":"سيك","ill":"إيل","healthy":"هيلثي","strong":"سترونغ",
"weak":"ويك","thin":"ثين","thinner":"ثينير","thinnest":"ثينست","shy":"شاي",
"gentle":"جنتل","brave":"بريف","honest":"أونيست","kind":"كايند","polite":"بولايت",
"cheerful":"تشيرفول","calm":"كالم","funny":"فاني","friendly":"فريندلي",
"generous":"جينيروس","lazy":"لايزي","naughty":"نووتي","noisy":"نويزي",
"serious":"سيريوس","smart":"سمارت","ugly":"أغلي","handsome":"هانسم",
"ago":"أغو","past":"باست","exactly":"إكزاكتلي","ahead":"أهد","far":"فار",
"farther":"فارذير","farthest":"فارذست","further":"فيرذير","slow":"سلو","hurry":"هاري",
"quick":"كويك","north":"نورث","south":"ساوث","east":"إيست","west":"وست",
"together":"توغيتير","alone":"ألون","outside":"آوتسايد","abroad":"أبرود",
"front":"فرانت","gate":"غيت","gates":"غيتس","corner":"كورنير","side":"سايد",
"middle":"ميدل","right":"رايت","left":"ليفت","opposite":"أوبوزيت","inside":"إنسايد",
"stairs":"ستايرز","lift":"ليفت","escalator":"إسكاليتور","basement":"بايسمنت",
"ground":"غراوند","earth":"إيرث","story":"ستوري","stories":"ستوريز","novel":"نوفل",
"poem":"بويم","sheet":"شيت","paper":"بايبير","vocabulary":"فوكابيولاري",
"dictionary":"ديكشنري","grammar":"غرامار","librarian":"لايبراريان",
"bee":"بي","bees":"بيز","butterfly":"باترفلاي","ant":"أنت","ants":"أنتس",
"mosquito":"موسكيتو","spider":"سبايدر","snake":"سناك","frog":"فروغ",
"turtle":"تيرتل","lion":"لايون","tiger":"تايجير","wolf":"وولف","wolves":"وولفز",
"bear":"بير","fox":"فوكس","monkey":"مانكي","rabbit":"رابيت","mouse":"ماوس",
"mice":"مايس","rat":"رات","noise":"نويز","loud":"لاود","music":"ميوزيك",
"song":"سونغ","songs":"سونغز","sing":"سينغ","sings":"سينغز","sang":"سانغ",
"singing":"سينغينغ","band":"بان","dance":"دانس","dances":"دانسز","danced":"دانست",
"dancing":"دانسينغ","singer":"سينغر","piano":"بيانو","guitar":"غيتار","drums":"درامز",
"violin":"فيولين","idea":"أيديا","ideas":"أيديا\u200bز",
"telephone":"تيليفون","message":"ميساج","messages":"ميساجز","ringing":"رينغينغ",
"ring":"رينغ","rings":"رينغز","rang":"رانغ","conversation":"كونفيرسيشن","chat":"تشات",
"text":"تيكست","email":"إيميل","postcard":"بوستكارد",
"fully":"فولي","etc":"إيتزَيطرا","etcetera":"إيتسيتيرا",
}

import re


_FIXED = {
"accept":"أكسابت","africa":"أفريكا","agree":"أغري","algerians":"ألجيريانس","apply":"أبلاي",
"argue":"أرجيو","attend":"أتند","awake":"أويك","babies":"بابيز","baby":"بايبي","back":"باك",
"baker":"بايكر","bakery":"باكاري","beard":"بيرد","became":"بيكيم","become":"بيكام",
"bedrooms":"بيدرومز","begins":"بغينز","bicycle":"بايسكل","board":"بورد","bored":"بورد",
"borrowing":"بوروينغ","breathe":"بريذ","bring":"برينغ","brothers":"براذرز","brought":"بروت",
"brush":"براش","business":"بيزنس","button":"باتن","camping":"كامبينغ","card":"كارد",
"case":"كيس","catch":"كاتش","catches":"كاتشيز","cents":"سنتس","century":"سينتشوري",
"chance":"تشانس","cherries":"تشيريز","cherry":"تشيري","chess":"تشيس","chocolate":"تشوكلت",
"chose":"تشوز","clear":"كليار","clothes":"كلوذز","clouds":"كلاودز","club":"كلاب",
"coats":"كووتس","colleague":"كوليج","comfortable":"كامفتربل","cookie":"كوكي","cost":"كوست",
"cosy":"كوزي","count":"كاونت","course":"كورس","cream":"كريم","daily":"ديلي","dark":"دارك",
"dawn":"دون","decision":"ديسيجن","deep":"ديب","deer":"دير","desk":"ديسك","dinars":"دينارس",
"dirhams":"ديرهامز","dive":"دايف","double":"دابل","drawing":"دراينغ","drop":"دروب",
"during":"ديورينغ","education":"إيديوكيشن","egypt":"إيجيبت","end":"إند","ended":"إندد",
"enjoy":"إنجوي","entrance":"إنترنس","ever":"إفر","excellent":"إكسيلنت","exciting":"إكسايتينغ",
"exercise":"إكسرسايز","experience":"إكسبيريينس","factory":"فاكتوري","famous":"فيمس",
"film":"فيلم","films":"فيلمز","fire":"فاير","fix":"فيكس","food":"فود","forgive":"فورغيف",
"fourth":"فورث","france":"فرانس","free":"فري","fridge":"فريدج","fuel":"فيويل",
"glasses":"غلاسيز","grandparents":"غراندبارنتس","grass":"غراس","habit":"هابيت","hangs":"هانغس",
"headache":"هيديك","hides":"هايدز","high":"هاي","highest":"هايست","hobby":"هوبي",
"holiday":"هوليداي","horror":"هورر","ice":"آيس","information":"إنفورميشين","insert":"إنسرت",
"jogging":"جوغينغ","join":"جوين","kept":"كيب","keys":"كيز","kilo":"كيلو","kilos":"كيلوز",
"kindness":"كايندنيس","knocking":"نوكينغ","lamp":"لامب","languages":"لانغويجز","largest":"لارغست",
"leads":"ليدز","leaf":"ليف","leave":"ليف","leaves":"ليفز","leaving":"ليفينغ","less":"ليس",
"life":"لايف","line":"لاين","litre":"ليتر","litter":"ليتر","lot":"لوت","love":"لاف",
"louder":"لاؤدر","lovely":"لافلي","machine":"ماشين","mall":"مول","matter":"ماتر",
"maybe":"مايبي","mean":"مين","medina":"مادينا","meet":"ميت","memorize":"ميمورايز",
"met":"ميت","metro":"ميترو","mind":"مايند","miss":"ميس","moment":"مومننت","nile":"نايل",
"accepted":"أكسابتيد","boring":"بورينغ","careful":"كارفل","decide":"ديسايد",
"decided":"ديسايديد","decision":"ديسيجن","deeply":"ديبلي","discussed":"ديسكست",
"discussing":"ديسكسينغ","documentaries":"دوكيومنتيريز","enjoyed":"أنجويد","enjoys":"أنجويز",
"explains":"إكسبلينز","future":"فيوتشر","joking":"جوكينغ","keep":"كيب","makkah":"مكة",
"meeting":"ميتينغ","memorizes":"ميمورايزز","mount":"ماونت","muezzin":"موآذّن","nowhere":"نوهوير",
"passed":"باست","patient":"بيشنت","pizza":"بيتزا","planned":"بلاند","pleasure":"بليزر",
"posted":"بوستيد","prays":"بريز","prefers":"بريفيرز","prayers":"برييرز","quran":"قرآن",
"queues":"كيو","offer":"أوفير","oil":"أويل","omar":"عمار","opinion":"أوبينيون","option":"أوبشن",
"order":"أوردير","others":"أوذيرز","parking":"باركينغ","pass":"باس",
"plant":"بلانت","pocket":"بوكيت","prefer":"بريفير","president":"بريزيدنت","press":"بريس",
"problem":"بروبلم","project":"بروجكت","promise":"بروميس","proud":"براود","quite":"كوايت",
"reason":"ريزن","ready":"ريدي","region":"ريجون","rest":"ريست","rise":"رايز","rises":"رايزز",
"screen":"سكرين","secret":"سيكرت","send":"سند","sent":"سنت","shelf":"شيلف","shine":"شاين",
"ship":"شيب","show":"شو","shown":"شون","silent":"سايلنت","skip":"سكيب","smoke":"سموك",
"solve":"سولف","soup":"سوب","speaks":"سبيكس","speech":"سبيتش","spicy":"سبايسي","stadium":"ستاديوم",
"stopped":"ستوبت","storm":"ستورم","straight":"ستريت","strawberry":"ستروبري","sunset":"سنسيت",
"sweet":"سويت","taken":"تيكين","talented":"تالنتد","tasty":"تاستي","traffic":"ترافيك",
"trip":"تريب","trust":"تراست","turn":"تورن","understand":"أندرساند","university":"يونيفرسيتي",
"useful":"يوسفول","victory":"فيكتوري","waited":"ويتيد","waste":"ويست","wear":"وير","works":"وركس",
"worry":"ووري","worse":"ويرس","wrote":"روت","yet":"ييت",
"advice":"أدفايس","angry":"أنجري","borrow":"بورو","borrows":"بوروز","boxes":"بوكسز",
"bridges":"بريدجز","buses":"باسز","coldest":"كولدست","corridor":"كوريدور",
"dad":"داد","dad's":"دادز","dishes":"دشيز","dropped":"دروبت","dying":"دايينغ",
"everest":"إيفرست","fajr":"فجر","fall":"فول","father's":"فاذرز","feed":"فيد","he's":"هيز",
"i'll":"آيل","i'm":"آيم","i've":"آيف","independent":"إنديبندنت","islem's":"إسلامز","it's":"إيتس",
"kids":"كيدز","late":"ليت","let's":"ليتس","marks":"ماركس","matters":"ماترز","mother's":"ماذرز",
"neighbours":"نيبورز","number":"نمبر","oussama's":"أسامة","painting":"بينتينغ",
"parks":"باركس","patients":"بيشنتس","plan":"بلان","plant":"بلانت","planting":"بلانتينغ","post":"بوست","pray":"بري",
"problems":"بروبلمز","queues":"كيو","rained":"ريند","raining":"رينينغ","raised":"رايزد",
"ramadan":"رمضان","ran":"ران","rarely":"ريرلي","reads":"ريدز","revise":"ريفايز","rising":"رايزينغ",
"route":"روت","runner":"رانر","safer":"سيفر","sahara":"صحراء","seat":"سيت","seats":"سيتس",
"she'll":"شيل","she's":"شيز","showed":"شاود","sidi":"سيدي","sim":"سيم","sir":"سير","sister's":"سيسترز",
"sisters":"سيسترز","solving":"سولفينغ","sooner":"سونر","spelled":"سبيلد","spending":"سبندينغ",
"sundays":"صنديز","surah":"سورة","sweets":"سويتس","taraweeh":"تراويح","temouchent":"تموشنت",
"that's":"ذاتس","there's":"ذيرز","they're":"ذير","thing":"ثينغ","things":"ثينغز",
"tunisia":"تونسيا","twelfth":"توالفث","tying":"تايينغ","understood":"أندرستود",
"vegetable":"فجيتبل","vegetables":"فجيتبلز","video":"فيديو","we're":"وير","we've":"ويف",
"we'll":"ويل","you're":"يور","am":"آم","add":"أضف","born":"بورن","roofs":"روفز",
"till":"تيل","way":"واي","amel":"أمل","wrote":"روت","began":"بجان","heart":"هارت","separate":"سيباريت",
}

def _c_rule(w):
    i, n, out = 0, len(w), []
    silent_e = len(w) >= 3 and w[-1] == "e" and w[-2] not in "aeiouy" and w[-3] in "aeiou"
    while i < n:
        a = w[i]
        b = w[i + 1] if i + 1 < n else ""
        c = w[i + 2] if i + 2 < n else ""
        # silent final e
        if silent_e and i == n - 1:
            i += 1
            continue
        # long vowel before consonant + silent final e
        if silent_e and i == n - 3 and a in "aeiou" and b not in "aeiou" and c == "e":
            out.append({"a": "اي", "e": "ي", "i": "اي", "o": "و", "u": "يو"}[a])
            i += 1
            continue
        if a + b + c == "tion":
            out.append("شن"); i += 3; continue
        if a + b + c == "ture":
            out.append("تشر"); i += 4; continue
        if a + b + c == "ssion" or a + b + c == "sion":
            out.append("شن"); i += 4; continue
        if a + b == "ed" and i + 2 == n:
            out.append("اد" if w[i - 1:i] not in ("t", "d") else "د")
            i += 2
            continue
        if a + b == "er" and i + 2 == n:
            out.append("ر"); i += 2; continue
        if a == "l" and w[i:i + 2] == "le" and i + 2 == n and i + 3 == n:
            out.append("ل"); i += 2; continue
        if a + b == "ue" and i + 2 == n:
            out.append("يو"); i += 2; continue
        if a + b == "th":
            out.append("ث"); i += 2; continue
        if a + b + c == "tch":
            out.append("تش"); i += 3; continue
        if a + b == "ch":
            out.append("تش"); i += 2; continue
        if a + b == "sh":
            out.append("ش"); i += 2; continue
        if a + b == "ph":
            out.append("ف"); i += 2; continue
        if a + b == "wh" and i == 0:
            out.append("و"); i += 2; continue
        if a + b == "kn" and i == 0:
            out.append("ن"); i += 2; continue
        if a + b == "wr" and i == 0:
            out.append("ر"); i += 2; continue
        if a + b == "ck" or a + b == "cc":
            out.append("ك"); i += 2; continue
        if a + b == "ng":
            out.append("نغ"); i += 2; continue
        if a + b == "qu":
            out.append("كو"); i += 2; continue
        if a + b + c == "igh":
            out.append("اي"); i += 3; continue
        if a + b + c == "ght":
            out.append("ت"); i += 3; continue
        if a + b == "gh":
            i += 2; continue
        if a + b == "oo":
            out.append("و"); i += 2; continue
        if a + b == "ee" or a + b == "ea":
            out.append("ي"); i += 2; continue
        if a + b == "ai" or a + b == "ay":
            out.append("اي"); i += 2; continue
        if a + b == "ou":
            out.append("او"); i += 2; continue
        if a + b == "ow":
            out.append("او"); i += 2; continue
        if a + b == "oi" or a + b == "oy":
            out.append("وي"); i += 2; continue
        if a + b == "oa":
            out.append("و"); i += 2; continue
        if a + b == "ie" or a + b == "ei":
            out.append("ي"); i += 2; continue
        if a + b == "au":
            out.append("ا"); i += 2; continue
        if a + b == "ur":
            out.append("ور"); i += 2; continue
        if a in "aeiou":
            out.append({"a": "ا", "e": "ا", "i": "ي", "o": "و", "u": "ا"}[a])
            i += 1
            continue
        if a == "g":
            out.append("ج" if b in "ei" else "غ"); i += 1; continue
        if a == "c":
            out.append("س" if b in "eiy" else "ك"); i += 1; continue
        if a == "s" and i > 0 and b in "aeiou" and w[i - 1] in "aeiou":
            out.append("ز"); i += 1; continue
        if a == "y":
            out.append("ي"); i += 1; continue
        m = {"b": "ب", "d": "د", "f": "ف", "h": "ه", "j": "ج", "k": "ك",
             "l": "ل", "m": "م", "n": "ن", "p": "ب", "q": "ك", "r": "ر",
             "s": "س", "t": "ت", "v": "ف", "w": "و", "x": "كس", "z": "ز"}.get(a, "")
        if m and out and out[-1] == m and a not in "w":
            i += 1
            continue
        if m:
            out.append(m)
        i += 1
    return "".join(out)
def ar_pron(sentence):
    words = re.findall(r"[A-Za-z']+", sentence)
    parts = []
    for w in words:
        key = w.strip("'").lower()
        parts.append(PRON.get(key, _FIXED.get(key, _c_rule(key))))
    return " ".join(parts)