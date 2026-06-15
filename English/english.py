import subprocess, os, re

PASSAGES = [
    {
        "no": 1, "title": "Education and Technology", "kind": "Prose",
        "summary": "The passage deals with the advantages, disadvantages and challenges of implementing AI in the classrooms. AI has the potential to revolutionize the way of teaching-learning by providing personalized learning, automating repetitive tasks, assisting teachers in their works etc. Again, it has some disadvantages like the possibility of replacing the teachers, lacking human interaction, the expense of implementation etc. To address the downsides, Edtech companies can play significant role in reducing the cost of implementation, making AI more teacher-oriented and overcoming the ethical concerns etc.",
        "theme": "Promise and peril of AI in education; balancing technological efficiency with the irreplaceable human element of teaching.",
        "vocab": [("revolutionize","v.","বৈপ্লবিক পরিবর্তন আনা","transform","preserve"),("personalized","adj.","ব্যক্তিগতকৃত","customized","generic"),("automate","v.","স্বয়ংক্রিয় করা","mechanize","do manually"),("implementation","n.","বাস্তবায়ন","execution","abandonment"),("ethical","adj.","নৈতিক","moral","unethical"),("downside","n.","অসুবিধা","drawback","advantage"),("interaction","n.","মিথস্ক্রিয়া","engagement","isolation")],
        "characters": "No fixed characters; stakeholders: teachers, students, EdTech firms, policy makers.",
        "quotes": ["AI has the potential to revolutionize the way of teaching-learning.","Technology can never replace the human touch of a teacher.","EdTech companies can play a significant role in reducing the cost."],
        "board_q": ["What are the advantages of AI in classrooms?","Discuss the challenges of implementing AI in education.","How can EdTech companies make AI teacher-oriented?"],
        "grammar": "Gerunds as noun/adjective: providing personalized learning, automating tasks -- V+ing used in subject/object position.",
        "writing": "Balanced composition: state Advantage then Disadvantage then Solution. Use however, on the other hand, to address this.",
        "shortcut": "PAT-CHEC: Personalized, Automation, Teacher-assist | Cost, Human-interaction, Ethical, Cheating.",
    },
    {
        "no": 2, "title": "Civic Engagement", "kind": "Prose",
        "summary": "The passage talks about the main purpose of education and that is to bring about positive changes in the society through civic engagement. Civic engagement means to work voluntarily for the public welfare using the skills learnt in the classroom. When people of a particular community are engaged in public issues, change is a must for that community. Thus, the ultimate goal of education is served.",
        "theme": "Education is meaningful only when its skills are returned to society through voluntary civic action.",
        "vocab": [("civic","adj.","নাগরিক সম্পর্কিত","public","private"),("engagement","n.","সম্পৃক্ততা","participation","withdrawal"),("voluntarily","adv.","স্বেচ্ছায়","willingly","forcibly"),("welfare","n.","কল্যাণ","well-being","harm"),("community","n.","সমাজ","society","individual"),("inevitable","adj.","অনিবার্য","certain","avoidable"),("positive","adj.","ইতিবাচক","affirmative","negative")],
        "characters": "Active citizens, students, community workers, educators.",
        "quotes": ["The ultimate goal of education is to bring positive change in society.","When people are engaged, change is a must.","Civic engagement uses the skills learnt in the classroom."],
        "board_q": ["Define civic engagement.","How does civic engagement fulfil the goal of education?","Why should educated people work for the community?"],
        "grammar": "Infinitive of purpose: to work voluntarily for public welfare -- to+verb shows purpose.",
        "writing": "Paragraph structure: Define the concept then give example then state benefit then conclude with impact.",
        "shortcut": "E = C + C: Education = Classroom skill + Community service.",
    },
    {
        "no": 3, "title": "Folk Music", "kind": "Prose",
        "summary": "The passage talks about the definition, features and types of folk music. Folk music refers to a particular genre of music that generates from the heart of a community and is uninfluenced by any sophisticated musical rules. Folk songs are usually composed and sung by the illiterate or semi-literate people. Despite having a universal appeal, these songs are sung in local dialects. Besides, environment plays an important role in composing these songs.",
        "theme": "Folk music as the spontaneous, environment-rooted voice of common people that carries universal human feelings.",
        "vocab": [("folk","adj.","লোকজ","traditional","classical"),("genre","n.","ধরন / শ্রেণী","category","--"),("sophisticated","adj.","পরিশীলিত","refined","simple"),("dialect","n.","আঞ্চলিক ভাষা","regional speech","standard language"),("universal","adj.","সার্বজনীন","global","local"),("illiterate","adj.","নিরক্ষর","uneducated","literate"),("compose","v.","রচনা করা","create","destroy")],
        "characters": "Anonymous rural composers, peasants, boatmen, marriage singers.",
        "quotes": ["Folk music generates from the heart of a community.","Environment plays an important role in composing folk songs.","Folk songs are uninfluenced by sophisticated musical rules."],
        "board_q": ["What is folk music?","Mention the features of folk songs.","How does environment influence folk music?"],
        "grammar": "Despite + V-ing: Despite having a universal appeal -- concession clause without a subject.",
        "writing": "Definition essay: Define then give features then give examples then conclude. Use refers to, is characterized by.",
        "shortcut": "Folk = Free + Oral + Local + Kommunity.",
    },
    {
        "no": 4, "title": "Lalon Shah", "kind": "Prose / Biography",
        "summary": "The passage deals with a brief biography of Lalon Shah, an icon of Baul tradition of Bangladesh, and his philosophy of life. Though Lalon was a Hindu by birth, he preached religious tolerance throughout his life. As a social reformer, he rejected all differences based on caste and religion. He tried to preach his Shahajia philosophy through his mystic songs and people in search of salvation accepted Lalon's philosophy and initiated asceticism under Lalon.",
        "theme": "Universal humanism above caste and creed, expressed through mystic Baul song.",
        "vocab": [("mystic","adj.","রহস্যময় / আধ্যাত্মিক","spiritual","worldly"),("tolerance","n.","সহিষ্ণুতা","acceptance","intolerance"),("reformer","n.","সংস্কারক","innovator","traditionalist"),("asceticism","n.","তপস্যা / সন্ন্যাস","self-denial","indulgence"),("philosophy","n.","দর্শন","ideology","--"),("salvation","n.","মুক্তি","deliverance","damnation"),("reject","v.","প্রত্যাখ্যান করা","refuse","accept")],
        "characters": "Lalon Shah (Baul saint), his disciples, Siraj Sain (spiritual guide).",
        "quotes": ["Everybody asks what Lalon's faith is.","Caste and creed are man-made; humanity is divine.","He preached religious tolerance throughout his life."],
        "board_q": ["Why is Lalon called a social reformer?","What is Shahajia philosophy?","How did Lalon preach his philosophy?"],
        "grammar": "Though/Although concession: Though Lalon was a Hindu by birth, he preached tolerance -- contrast clause.",
        "writing": "Biography paragraph: Birth/background then challenges then achievement/philosophy then legacy/impact.",
        "shortcut": "Lalon = Love + Liberty + Logic above caste.",
    },
    {
        "no": 5, "title": "Art", "kind": "Prose",
        "summary": "The passage deals with the implication, functions, examples and types of art. It is an expression of creative skills through different activities like painting, sculpture, crafts etc. The goal of art is to knock people emotionally and intellectually. Traditional artistic objects can be used as daily necessities. But, modern art focuses on expressing the spirits of time and changes in human thought using colors, shapes and techniques.",
        "theme": "Art as the evolving expression of human creativity that affects both emotion and intellect.",
        "vocab": [("expression","n.","প্রকাশ","representation","concealment"),("intuitive","adj.","সহজাত","instinctive","calculated"),("sculpture","n.","ভাস্কর্য","carving","painting"),("aesthetic","adj.","নান্দনিক","beautiful","ugly"),("contemporary","adj.","সমসাময়িক","modern","ancient"),("implication","n.","তাৎপর্য","significance","--"),("intellectually","adv.","বুদ্ধিবৃত্তিকভাবে","rationally","emotionally")],
        "characters": "Artists, craftsmen, viewers, modern and traditional artists.",
        "quotes": ["Art is a diverse range of human activity.","Modern art is the expression of the spirit of time.","The goal of art is to knock people emotionally and intellectually."],
        "board_q": ["Define art.","Differentiate between traditional and modern art.","What is the function of art?"],
        "grammar": "Passive voice in definitions: Art is expressed through..., Objects can be used as... -- subject + be + V3.",
        "writing": "Compare-contrast essay: Traditional art vs. Modern art. Use whereas, on the contrary, in contrast.",
        "shortcut": "Art = E + I (Emotion + Intellect) through Colour, Shape, Technique.",
    },
    {
        "no": 6, "title": "S M Sultan", "kind": "Prose / Biography",
        "summary": "The extract is about a brief biography of a famous Bangladeshi artist S M Sultan, the features of his art and his worldwide recognition as a major artist. Despite facing many challenges in life, Sultan could establish himself as an artist of classic dimension through his passion and talent. He had captured rural Bangladesh with philosophical insights in his art pieces. In his later life, he got lots of national awards, a huge international media coverage and a wide recognition worldwide.",
        "theme": "The dignity, vigour and philosophical depth of rural Bengali life as immortalized through Sultan's brush.",
        "vocab": [("muscular","adj.","পেশীবহুল","strong","frail"),("dimension","n.","মাত্রা / বিস্তার","aspect","--"),("recognition","n.","স্বীকৃতি","acknowledgement","neglect"),("philosophical","adj.","দার্শনিক","thoughtful","superficial"),("eccentric","adj.","অদ্ভুত","unconventional","normal"),("passion","n.","আবেগ / অনুরাগ","devotion","indifference"),("immortalize","v.","অমর করা","eternalize","forget")],
        "characters": "Sheikh Mohammad Sultan (S M Sultan), his rural subjects, peasants of Bengal.",
        "quotes": ["Sultan painted the muscular peasants of Bengal.","He gave the soil of Bangladesh a voice on canvas.","He established himself as an artist of classic dimension."],
        "board_q": ["Why are Sultan's peasants muscular?","Discuss Sultan as a classic artist.","Mention his international recognitions."],
        "grammar": "Despite + noun/V-ing: Despite facing many challenges -- introduces a concessive idea.",
        "writing": "Descriptive biography: Set the scene then describe qualities then give achievements then state legacy.",
        "shortcut": "Sultan = Soil + Strength + Soul of Bengal.",
    },
    {
        "no": 7, "title": "Novera Ahmed", "kind": "Prose / Biography",
        "summary": "The passage is about a brief biography of the first Bangladeshi sculptor Novera Ahmed, the steps of her becoming a sculptor and her recognition as a major artist. Being from a culturally inclined family, Novera got inspired to become an artist from her childhood. Later, her education and experiences in the western countries helped her to become a successful sculptor. Though initially, she was underrepresented, later she got a huge recognition in our country and won the Ekushey Padak in 1997.",
        "theme": "A pioneer female sculptor's perseverance against neglect and the late but rightful recognition of her art.",
        "vocab": [("sculptor","n.","ভাস্কর","carver","painter"),("inclined","adj.","আগ্রহী","disposed","disinterested"),("underrepresented","adj.","অবমূল্যায়িত","neglected","celebrated"),("pioneer","n.","পথিকৃৎ","trailblazer","follower"),("perseverance","n.","অধ্যবসায়","persistence","giving up"),("recognition","n.","স্বীকৃতি","appreciation","neglect"),("inspiration","n.","অনুপ্রেরণা","motivation","discouragement")],
        "characters": "Novera Ahmed, Hamidur Rahman (collaborator), her culturally inclined family.",
        "quotes": ["Novera is the pioneer of modern sculpture in Bangladesh.","She was awarded the Ekushey Padak in 1997.","Her education in the West shaped her artistic career."],
        "board_q": ["Why is Novera called a pioneer?","How did the West shape her art?","Mention her major recognitions."],
        "grammar": "Participle clause: Being from a culturally inclined family, Novera got inspired -- present participle replaces because clause.",
        "writing": "Biography with contrast: early life then struggle/neglect then later success then award/legacy. Use though initially...later.",
        "shortcut": "Novera = New Era of sculpture in Bangladesh.",
    },
    {
        "no": 8, "title": "Craft", "kind": "Prose",
        "summary": "The passage talks about the definitions of art and craft and the differences between them. Art is visionary and intuitive but craft is the application of practical skills to produce daily useful objects. The value of an art piece like a painting is measured by the stature of the artist. But, a craftwork like pottery is very cheap in comparison to an art piece. Because of the wonderful motifs and designs of a craftwork, it can be considered as an art form. But an art piece cannot be considered as a craft because of the lack of its daily usefulness.",
        "theme": "The kinship and contrast between vision-based art and skill-based craft.",
        "vocab": [("craft","n.","হস্তশিল্প","skilled handwork","fine art"),("motif","n.","অলংকরণ নকশা","decorative pattern","--"),("stature","n.","মর্যাদা","standing","obscurity"),("intuitive","adj.","সহজাত","instinctive","learned"),("functional","adj.","ব্যবহারযোগ্য","useful","decorative"),("visionary","adj.","দূরদর্শী","imaginative","practical"),("comparison","n.","তুলনা","contrast","similarity")],
        "characters": "Artists and craftsmen (potters, weavers, painters).",
        "quotes": ["Art is visionary; craft is practical.","Every craft may be an art, but every art is not craft.","The value of an art piece is measured by the stature of the artist."],
        "board_q": ["Differentiate art and craft.","Why is craft cheaper than art?","Can craft be considered art? Explain."],
        "grammar": "Can/Cannot modal: A craftwork can be considered art vs. An art piece cannot be considered craft -- possibility modals.",
        "writing": "Comparison paragraph: State definition of both then give key difference then overlap then conclusion.",
        "shortcut": "Art = Vision; Craft = Use. Overlap when craft carries motif.",
    },
    {
        "no": 9, "title": "Behula", "kind": "Prose / Myth",
        "summary": "The passage is taken from a mythical story of Manasamangal referring to how the worship of the goddess Manasa was established on earth with the help of Behula. Behula's father-in-law, Chand Saodagar was disobedient to Manasa. As a result, Manasa killed his son Lakhindar by a snake-bite. Behula then reached heaven to restore her husband through a mythical journey. Manasa took pity on her and Behula assured Manasa of her worship by Chand Saoudagar. Thus, the worship of Manasa was established on earth.",
        "theme": "Female devotion, loyalty and courage that bridges the human and divine worlds.",
        "vocab": [("mythical","adj.","পৌরাণিক","legendary","real"),("worship","n.","উপাসনা / পূজা","adoration","blasphemy"),("disobedient","adj.","অবাধ্য","defiant","obedient"),("restore","v.","পুনরুদ্ধার করা","bring back","destroy"),("devotion","n.","ভক্তি","dedication","neglect"),("pity","n.","সমবেদনা","sympathy","cruelty"),("establish","v.","প্রতিষ্ঠা করা","found","abolish")],
        "characters": "Behula (devoted wife), Lakhindar (husband), Chand Saodagar (father-in-law), Manasa (goddess).",
        "quotes": ["Behula journeyed to heaven for the love of her husband.","Devotion can move even the gods.","Thus the worship of Manasa was established on earth."],
        "board_q": ["Why did Manasa kill Lakhindar?","How did Behula restore her husband?","How was Manasa's worship established?"],
        "grammar": "Cause-effect connectors: As a result, Manasa killed... and Thus, the worship was established -- linking cause to consequence.",
        "writing": "Narrative retelling: Set the conflict then show character action then give divine response then state resolution/moral.",
        "shortcut": "B-L-C-M chain: Behula saves Lakhindar, Chand worships Manasa.",
    },
    {
        "no": 10, "title": "Icarus", "kind": "Prose / Myth",
        "summary": "This is a story taken from the Greek mythology about the downfall of Icarus due to his disobedience to his father, Daedalus. Being trapped in an island by king Minos, Daedalus discovered a way to escape the sea by means of artificial wings made of feathers and wax. Though he taught Icarus to fly at a moderate height, Icarus forgot the warning and soared higher out of excitement. As a result, he had to face the tragic downfall. Though it was a wonderful invention to fly with artificial wings, Icarus could not survive due to his amateur use of the technology.",
        "theme": "Hubris, disobedience and the misuse of technology lead to tragic downfall.",
        "vocab": [("downfall","n.","পতন / বিনাশ","ruin","rise"),("disobedience","n.","অবাধ্যতা","defiance","obedience"),("moderate","adj.","পরিমিত","middling","extreme"),("amateur","adj.","অনভিজ্ঞ","unskilled","expert"),("artificial","adj.","কৃত্রিম","man-made","natural"),("soar","v.","উচ্চে উড়া","ascend","plummet"),("tragic","adj.","বিয়োগান্তক","catastrophic","fortunate")],
        "characters": "Daedalus (inventor father), Icarus (son), King Minos (captor).",
        "quotes": ["Fly neither too high nor too low.","Pride goes before a fall.","Icarus could not survive due to his amateur use of technology."],
        "board_q": ["Why was Daedalus trapped?","Why did Icarus fall?","What lesson does the story of Icarus teach us?"],
        "grammar": "Though + clause concession: Though he taught Icarus to fly at a moderate height, Icarus forgot the warning.",
        "writing": "Moral story: Background then warning then disobedience then consequence then moral.",
        "shortcut": "Icarus: Impulse + Carelessness Always Ruins yoUth + Soaring.",
    },
    {
        "no": 11, "title": "Gazi Pir", "kind": "Prose / Myth",
        "summary": "The passage is about a Muslim mythological story regarding Gazi Pir. Gazi Pir was a Muslim preacher who is believed to have supernatural powers like calming dangerous animals and making them docile. The story of Gazi Pir has been preserved in folk literature of our country. Besides, some paintings of this great saint are still a part of the collection of the British Museum.",
        "theme": "Folk Islam, miraculous power and harmony between humans and wild nature.",
        "vocab": [("supernatural","adj.","অলৌকিক","miraculous","natural"),("preacher","n.","ধর্মপ্রচারক","religious teacher","listener"),("docile","adj.","নিরীহ / বাধ্য","tame","wild"),("saint","n.","সাধু / পির","holy person","sinner"),("preserve","v.","সংরক্ষণ করা","keep safe","destroy"),("calming","v.","শান্ত করা","soothing","agitating"),("folk","adj.","লোকজ","traditional","modern")],
        "characters": "Gazi Pir (saint), his followers, wild animals (tigers, crocodiles).",
        "quotes": ["Gazi Pir could calm even tigers.","His memory survives in folk paintings.","Some paintings are a part of the British Museum collection."],
        "board_q": ["Who was Gazi Pir?","Mention his supernatural powers.","How is his story preserved?"],
        "grammar": "Passive for ongoing preservation: His story has been preserved in folk literature -- present perfect passive.",
        "writing": "Short profile: Who + what powers + how remembered. Use is believed to, is said to for reported characteristics.",
        "shortcut": "Gazi = Guardian Against Zealous wIlderness.",
    },
    {
        "no": 12, "title": "Khona", "kind": "Prose / Myth",
        "summary": "This is a story taken from Indian mythology about the incredible gift of Khona to predict the weather and environment and her tragic fate due to the jealousy of the ruling class. Khona was a born astrologer who could predict the weather for the coming season and thus helped the farmers of the land by her prediction through easy to remember rhymes. When her predictions surpassed the famous astrologers of the royal court, their ego was hurt and they punished Khona cruelly by cutting her tongue off. Though Khona was disabled, her words have still been benefitting people over 1500 years.",
        "theme": "Genius silenced by patriarchal envy; the lasting voice of folk wisdom across centuries.",
        "vocab": [("astrologer","n.","জ্যোতিষী","star-reader","scientist"),("predict","v.","পূর্বাভাস দেওয়া","foretell","--"),("jealousy","n.","ঈর্ষা / হিংসা","envy","admiration"),("rhyme","n.","ছড়া / কবিতা","verse","prose"),("surpass","v.","ছাড়িয়ে যাওয়া","exceed","fall short of"),("disable","v.","অক্ষম করা","incapacitate","enable"),("benefit","v.","উপকৃত করা","help","harm")],
        "characters": "Khona, Varahamihira (father-in-law), royal court astrologers, farmers.",
        "quotes": ["Khona's rhymes guide farmers even today.","They cut her tongue but not her wisdom.","Her words have been benefitting people over 1500 years."],
        "board_q": ["Why did Khona invent rhymes?","Why was her tongue cut off?","Why are her sayings still relevant?"],
        "grammar": "Present perfect for continuing relevance: Her words have been benefitting people -- action started in past, still ongoing.",
        "writing": "Injustice narrative: Introduce talent then show threat to power then punishment then enduring legacy.",
        "shortcut": "Khona = Knowledge Helping Over Noble Arrogance.",
    },
    {
        "no": 13, "title": "I Have a Dream", "kind": "Speech",
        "summary": "Here the speaker implies the racial discrimination inflicted on the black people of America. But he hopes that someday will come when everybody will live peacefully and harmoniously. Besides, people will not be judged by the color of the skin rather by the beauty of character. All their states will be free from all types of inequalities and injustice based on apartheid.",
        "theme": "Racial equality, dignity and the prophetic dream of a just, discrimination-free society.",
        "vocab": [("discrimination","n.","বৈষম্য","unjust distinction","equality"),("apartheid","n.","বর্ণবাদী বিচ্ছিন্নতা","racial segregation","integration"),("inequality","n.","অসাম্য","disparity","equality"),("harmoniously","adv.","সহানুভূতির সাথে","peacefully","discordantly"),("character","n.","চরিত্র","moral quality","appearance"),("inflict","v.","আরোপ করা","impose","spare"),("envision","v.","কল্পনায় দেখা","imagine","ignore")],
        "characters": "Martin Luther King Jr. (speaker), black Americans, oppressors, future generations.",
        "quotes": ["I have a dream that one day...","Judged not by the colour of their skin but by the content of their character.","All states will be free from all types of inequalities."],
        "board_q": ["What is King's dream?","Why does the speaker mention skin colour?","How does King envision America's future?"],
        "grammar": "Future tense for hope/vision: people will not be judged, everybody will live peacefully -- future simple expressing aspiration.",
        "writing": "Persuasive speech: Open with emotional appeal then state the problem then paint a hopeful vision then end with a call to action.",
        "shortcut": "DREAM = Dignity + Race-equality + Equity + America-future + Morality.",
    },
    {
        "no": 14, "title": "The Unforgettable History", "kind": "Speech",
        "summary": "The extract is taken from the English translation of Bangabandhu's 7th March speech in 1971. The text is about a brief history of exploitation by the Pakistanis inflicted on the Bangladeshis from 1947 to 1971 and an indirect call for the liberation war. In the speech, Bangabandhu has precisely described the picture of oppression and deprivation from 1947. Being unable to stop the oppression, he inspired the Bengalees for the liberation war by saying that time has come to protest against all types of oppression and deprivation and the Bengalees responded to his call.",
        "theme": "Resistance against colonial oppression, the declaration of liberation and the birth of a nation.",
        "vocab": [("exploitation","n.","শোষণ","unfair use","fair treatment"),("deprivation","n.","বঞ্চনা","loss","fulfilment"),("oppression","n.","নিপীড়ন","tyranny","freedom"),("liberation","n.","মুক্তি","freedom","enslavement"),("inspire","v.","অনুপ্রাণিত করা","motivate","discourage"),("precisely","adv.","সুনির্দিষ্টভাবে","exactly","vaguely"),("unforgettable","adj.","অবিস্মরণীয","memorable","forgettable")],
        "characters": "Bangabandhu Sheikh Mujibur Rahman (speaker), Bangalees, Pakistani rulers.",
        "quotes": ["This time the struggle is for our freedom.","Build forts in every house.","Time has come to protest against all types of oppression."],
        "board_q": ["When was the speech delivered?","Why is it called unforgettable?","What did Bangabandhu call for?"],
        "grammar": "Reported speech back-shift: He said that time had come to protest -- tense shifts back in indirect speech.",
        "writing": "Historical speech analysis: Context/date then key argument then emotional appeal then call to action.",
        "shortcut": "7M-71 = Seventy-one March Seven: Mukti (Freedom).",
    },
    {
        "no": 15, "title": "Wangari Maathai", "kind": "Prose / Biography",
        "summary": "The passage deals with the contribution of Wangari Maathai to protect the earth. As a conscious citizen of the planet, she thought it compulsory to protect the earth through planting trees. She started a green belt movement in Kenya and then spread it throughout Africa. Besides, she worked on women rights and democracy to establish peace in the society. As a harbinger of peace, she was awarded Nobel Peace Prize, Nelson Mandela award and so on. As an environmentalist, Maathai has been an inspiration for the people around the world.",
        "theme": "Environmental activism intertwined with women's rights and democratic peace.",
        "vocab": [("environmentalist","n.","পরিবেশবাদী","activist","polluter"),("harbinger","n.","অগ্রদূত","forerunner","follower"),("conscious","adj.","সচেতন","aware","ignorant"),("democracy","n.","গণতন্ত্র","people's rule","dictatorship"),("inspiration","n.","অনুপ্রেরণা","stimulus","discouragement"),("compulsory","adj.","বাধ্যতামূলক","obligatory","optional"),("contribution","n.","অবদান","input","withdrawal")],
        "characters": "Wangari Maathai, Kenyan women, world leaders, environmental campaigners.",
        "quotes": ["When we plant trees, we plant the seeds of peace.","Maathai has been an inspiration for people around the world.","She worked on women's rights and democracy."],
        "board_q": ["What is the Green Belt Movement?","Why did Maathai win the Nobel?","How is she an inspiration?"],
        "grammar": "Present perfect for ongoing legacy: Maathai has been an inspiration -- past action with present relevance.",
        "writing": "Inspirational biography: Background then key initiative then wider impact then awards then tribute.",
        "shortcut": "Maathai = Mother of trees, Activism, Awards, Themes of Healthy Africa, Inspiration.",
    },
    {
        "no": 16, "title": "Frederick Douglass", "kind": "Prose / Autobiography",
        "summary": "The extract is taken from an autobiography of Frederick Douglass, an Afro-American writer and it is about the struggles of slaves in America. The slaves in America were deprived of many basic human rights and their life was full of miseries. They were ignorant of their birthday, parental identity and even parents' affection for the whole life. It seemed that the only ambition of their life was only to serve the white. Besides, they had to go through hard labor and severe punishment. Actually, this text is a vivid representation of the unending miseries of the slaves in America.",
        "theme": "The dehumanizing horror of slavery and the silent yearning for identity and basic human dignity.",
        "vocab": [("slave","n.","দাস","bondsman","free person"),("deprived","adj.","বঞ্চিত","denied","privileged"),("miseries","n.","দুর্দশা","sufferings","comforts"),("identity","n.","পরিচয়","sense of self","anonymity"),("punishment","n.","শাস্তি","penalty","reward"),("vivid","adj.","প্রাণবন্ত / স্পষ্ট","clear","vague"),("ambition","n.","উচ্চাকাঙ্ক্ষা","aspiration","contentment")],
        "characters": "Frederick Douglass (narrator/slave), his unnamed mother, white masters.",
        "quotes": ["I was born, but I have no accurate knowledge of my age.","A slave's life is not his own.","This text is a vivid representation of the unending miseries of the slaves."],
        "board_q": ["Describe a slave's daily life.","Why was Douglass ignorant of his birthday?","How does the extract expose slavery?"],
        "grammar": "Past simple for narrated historical facts: They were deprived, They had to go through -- simple past for completed events.",
        "writing": "Autobiographical extract analysis: Identify narrator voice then describe conditions then state what is denied then state moral message.",
        "shortcut": "Slave = Stripped of Life, Affection, Voice, Existence.",
    },
    {
        "no": 17, "title": "What is a Dream?", "kind": "Prose",
        "summary": "The text is about the definition and features of a dream and some prominent theories of famous psychologists about it. We experience dreams during sleep. Dreams may be vivid, vague, joyful or frightening etc. About the purpose of a dream, there is always a disagreement among the psychologists. However, dreaming is essential to mental, physical and psychological well-being.",
        "theme": "The mystery, function and necessity of dreaming for complete human health.",
        "vocab": [("vivid","adj.","উজ্জ্বল / স্পষ্ট","clear","vague"),("vague","adj.","অস্পষ্ট","unclear","definite"),("psychologist","n.","মনোবিজ্ঞানী","mind scientist","--"),("subconscious","adj.","অবচেতন","below awareness","conscious"),("well-being","n.","সুস্থতা","good condition","ill-being"),("prominent","adj.","বিশিষ্ট","famous","unknown"),("disagreement","n.","মতবিরোধ","difference of opinion","consensus")],
        "characters": "Freud, Jung (psychologists referenced), the dreamer (any person).",
        "quotes": ["A dream is a succession of images during sleep.","Dreaming is essential to well-being.","There is always a disagreement among psychologists about dreams."],
        "board_q": ["Define a dream.","What do psychologists say about dreams?","Why is dreaming essential?"],
        "grammar": "Modal may for uncertain characteristics: Dreams may be vivid, vague, joyful or frightening -- possibility not certainty.",
        "writing": "Expository writing: Define then give features then present contrasting theories then state conclusion.",
        "shortcut": "Dream = Disorder + Reflection + Emotion + Adjustment + Memory.",
    },
    {
        "no": 18, "title": "Brojen Das", "kind": "Prose / Biography",
        "summary": "This is a story about a national hero, Brojen Das and his struggles to upright the name of Bangladesh by risking his own life. Despite failing five times, he took the risk for the sixth time to make the record of crossing the English Channel from France to England. His determination, bravery and patriotism helped him make the record and upright the name of the country in the global arena. As a result, Brojen Das and Bangladesh have been recorded in the Greenwich book for the record to cross the English Channel.",
        "theme": "Patriotic perseverance turning repeated failure into national glory.",
        "vocab": [("perseverance","n.","অধ্যবসায়","persistent effort","giving up"),("patriotism","n.","দেশপ্রেম","love of country","betrayal"),("determination","n.","দৃঢ়প্রতিজ্ঞা","firmness","indecision"),("bravery","n.","সাহসিকতা","courage","cowardice"),("global","adj.","বৈশ্বিক","worldwide","local"),("channel","n.","সংকীর্ণ সমুদ্রপথ","narrow sea passage","--"),("record","n.","নথিভুক্ত কৃতিত্ব","registered achievement","--")],
        "characters": "Brojen Das (swimmer), his coach, fellow swimmers, the nation of Bangladesh.",
        "quotes": ["Failure is the pillar of success.","Brojen carried the flag of Bangladesh across the Channel.","He made the record on his sixth attempt."],
        "board_q": ["Who was Brojen Das?","How many times did he attempt crossing the Channel?","Why is he a national hero?"],
        "grammar": "Despite + V-ing (repeated failure): Despite failing five times, he took the risk -- persistent effort despite adversity.",
        "writing": "Inspirational biography: State the goal then describe struggle/failures then show turning point then celebrate achievement.",
        "shortcut": "Brojen = Brave + Resolute + Outstanding + Jubilant + ENduring.",
    },
    {
        "no": 19, "title": "Nishat Mazumder", "kind": "Prose / Biography",
        "summary": "The passage is about a short biography and great achievement of Nishat Mazumder, a Bangladeshi sports icon. She has earned enormous fame to Bangladesh by becoming the first Bangladeshi to reach the highest mountain peak in the world. She was born in Lakshmipur in 1981 and completed her graduation from Dhaka City College. Later, she got admitted in M.A in Japan Studies in Dhaka University.",
        "theme": "Female determination scaling literal and figurative peaks for national honour.",
        "vocab": [("mountaineer","n.","পর্বতারোহী","mountain climber","--"),("peak","n.","শিখর / চূড়া","summit","base"),("graduation","n.","স্নাতক ডিগ্রি","degree completion","enrollment"),("icon","n.","প্রতীক / আদর্শ ব্যক্তিত্ব","symbol","nobody"),("achievement","n.","কৃতিত্ব","accomplishment","failure"),("enormous","adj.","বিশাল","huge","tiny"),("admitted","v.","ভর্তি হওয়া","enrolled","rejected")],
        "characters": "Nishat Mazumder, fellow climbers, her family and mentors.",
        "quotes": ["Nishat conquered Everest with the flag of Bangladesh.","She is the first Bangladeshi woman to reach the highest peak.","Heights bow before willing hearts."],
        "board_q": ["Who is Nishat Mazumder?","What is her great achievement?","Mention her academic background."],
        "grammar": "Present perfect for past achievement with present relevance: She has earned enormous fame -- the fame continues in the present.",
        "writing": "Achievement profile: Introduce person then state the achievement then background details then significance.",
        "shortcut": "Nishat = Nation + Ice + Summit + Heroism + Aspiration + Triumph.",
    },
    {
        "no": 20, "title": "The Unbeaten Girls", "kind": "Prose / Report",
        "summary": "The passage talks about the success of the girl footballers in the Kalsindur village of Bangladesh. The village Kalsindur has become a symbol of girl power because girls have illuminated it by their skills in the game of football. Nothing but the faith and determination have brought this success to these female footballers.",
        "theme": "Rural female empowerment through sport, overcoming socio-economic and gender barriers.",
        "vocab": [("unbeaten","adj.","অপরাজিত","not defeated","defeated"),("determination","n.","অদম্য মনোবল","resolve","hesitation"),("empowerment","n.","ক্ষমতায়ন","authority","disempowerment"),("illuminate","v.","আলোকিত করা","brighten","darken"),("symbol","n.","প্রতীক","sign","--"),("faith","n.","বিশ্বাস / আস্থা","trust","doubt"),("footballer","n.","ফুটবলার","football player","--")],
        "characters": "Kalsindur girl footballers, their coach Mofiz Uddin, supportive parents.",
        "quotes": ["Kalsindur is now a symbol of girl-power.","Faith and determination are the only goals.","They proved that girls too can fly with the ball."],
        "board_q": ["Why is Kalsindur famous?","What made the girls successful?","Discuss the report as a symbol of empowerment."],
        "grammar": "Emphatic structure: Nothing but the faith and determination have brought this success -- nothing but for strong emphasis.",
        "writing": "Report writing: Headline then who/what/where then key achievement then reason for success then significance.",
        "shortcut": "Kalsindur = Kicks + Aspiration + Liberation + Skill + Inspiration.",
    },
    {
        "no": 21, "title": "Family Relationship", "kind": "Prose",
        "summary": "The passage deals with the importance and types of relationship in human life. As a social being, man has to maintain relationship with others for physical and emotional support. Depending on its nature, relationship is divided into two types such as familial and social. Relation with others helps us share our joys and overcome our sorrows. However, to maintain an effective relationship we should have trust, respect and love for each other.",
        "theme": "Relationship as the emotional backbone of human existence, built on trust, respect and love.",
        "vocab": [("familial","adj.","পারিবারিক","relating to family","social"),("trust","n.","বিশ্বাস","firm belief","distrust"),("respect","n.","সম্মান","esteem","disrespect"),("sorrow","n.","দুঃখ / বেদনা","grief","joy"),("bondage","n.","বন্ধন","close tie","freedom"),("effective","adj.","কার্যকর","efficient","ineffective"),("social","adj.","সামাজিক","communal","antisocial")],
        "characters": "Family members, friends, the individual as a social being.",
        "quotes": ["Man is a social being.","Trust, respect and love sustain every bond.","Relation with others helps us share our joys."],
        "board_q": ["Why is relationship important?","Mention types of relationship.","What is needed for effective relationships?"],
        "grammar": "Classification structure: Depending on its nature, relationship is divided into two types -- partitive structure for categorization.",
        "writing": "Argumentative paragraph: State importance then classify types then give benefits then state conditions for success.",
        "shortcut": "TRL = Trust + Respect + Love (the relationship triangle).",
    },
    {
        "no": 22, "title": "A Mother in Manville", "kind": "Short Story",
        "summary": "The extract deals with some of the good qualities of an orphan named Jerry in the eye of a writer. The writer was introduced to the boy for a very short period of time and got impressed with him for his unique qualities like integrity, sincerity, graciousness, gratefulness etc. Thus, Jerry made a deep bondage with the writer despite being completely unknown to her earlier.",
        "theme": "Hidden depth of an orphan's character; integrity transcends brief acquaintance and reveals the irony of a motherless claim.",
        "vocab": [("orphan","n.","এতিম / অনাথ","parentless child","child with parents"),("integrity","n.","সততা","honesty","dishonesty"),("graciousness","n.","সৌজন্য","kindness","rudeness"),("gratefulness","n.","কৃতজ্ঞতা","thankfulness","ingratitude"),("sincerity","n.","আন্তরিকতা","genuineness","insincerity"),("bondage","n.","গভীর বন্ধন","deep connection","distance"),("matron","n.","মহিলা প্রশাসক","female administrator","--")],
        "characters": "Jerry (orphan boy), the writer/narrator, the matron of the orphanage.",
        "quotes": ["He had made his pile of chips small.","Integrity is a word that means more than the dictionary defines.","My mother lives in Manville."],
        "board_q": ["Describe Jerry's character.","Why is the title ironic?","How does Jerry impress the writer?"],
        "grammar": "Present participle for concurrent condition: despite being completely unknown to her earlier -- -ing form with despite.",
        "writing": "Character sketch: First impression then specific traits with examples then significance of those traits.",
        "shortcut": "Jerry = Just + Earnest + Reliable + Responsible + Yearning for family.",
    },
    {
        "no": 23, "title": "Butterfly Forever", "kind": "Short Story",
        "summary": "Butterfly Forever by Chen Qiyou is a short story that revolves around the theme of love and loss, narrated from the perspective of someone who has experienced the profound pain of losing a loved one. The story focuses on a quiet moment when the narrator reflects on the death of his beloved, capturing the enduring scar left by this loss. It also touches upon the symbolism of a butterfly, representing both the beauty and fragility of life and love, and the lasting impact of memories.",
        "theme": "Eternal love and remembrance; the butterfly as symbol of fragile beauty preserved forever in memory.",
        "vocab": [("fragility","n.","ভঙ্গুরতা","delicacy","strength"),("scar","n.","ক্ষত / গভীর দাগ","lasting mark","healing"),("symbolism","n.","প্রতীকবাদ","use of symbols","literalism"),("profound","adj.","গভীর","deep","shallow"),("enduring","adj.","দীর্ঘস্থায়ী","lasting","temporary"),("reflect","v.","চিন্তা করা / প্রতিফলিত করা","contemplate","ignore"),("beloved","n.","প্রিয়জন","loved one","enemy")],
        "characters": "The narrator (unnamed), his deceased beloved.",
        "quotes": ["Love does not die with the loved.","The butterfly remains, fragile yet forever.","The enduring scar of loss lingers."],
        "board_q": ["What does the butterfly symbolize?","Describe the narrator's mood.","Discuss the theme of love and loss."],
        "grammar": "Present participle modifying the main clause: capturing the enduring scar, representing beauty -- simultaneous actions.",
        "writing": "Symbolic story analysis: Identify the symbol then explain its dual meaning then connect to the theme then state emotional impact.",
        "shortcut": "Butterfly = Beauty + Brief life + Forever in memory.",
    },
    {
        "no": 24, "title": "Storms and Stresses of Adolescence", "kind": "Prose",
        "summary": "The passage deals with the definition, features and problems of adolescence in one's life span. Adolescence is a transitional stage in everyone's life with several key developments and pressures like physical and sexual maturation, acquisition of necessary skills, curiosity towards drugs etc. So, all concerned should be careful about the successful transition of the adolescents into adulthood.",
        "theme": "Adolescence as a turbulent yet crucial transitional stage requiring careful guidance.",
        "vocab": [("adolescence","n.","কৈশোর / বয়ঃসন্ধি","teen years","adulthood"),("transitional","adj.","অন্তর্বর্তীকালীন","intermediate","permanent"),("maturation","n.","পরিপক্কতা","becoming mature","immaturity"),("curiosity","n.","কৌতূহল","desire to know","indifference"),("vulnerable","adj.","ঝুঁকিপূর্ণ","exposed to harm","protected"),("acquisition","n.","অর্জন","gaining","losing"),("transition","n.","রূপান্তর","shift","stagnation")],
        "characters": "Adolescents, parents, teachers, guidance counselors.",
        "quotes": ["Adolescence is a storm-and-stress period.","Successful transition makes a sound adult.","All concerned should be careful about the adolescents."],
        "board_q": ["Define adolescence.","Mention its key features.","Why is adolescence called a storm-and-stress stage?"],
        "grammar": "Should modal for obligation: all concerned should be careful -- modal expressing recommended duty.",
        "writing": "Expository with definition: Define the term then list features/problems then give advice/solution then conclude.",
        "shortcut": "Adolescence = ASKED: Adjustment, Sex-maturation, Knowledge, Emotion, Drug-risk.",
    },
    {
        "no": 25, "title": "Adolescence and Related Problems", "kind": "Prose",
        "summary": "The passage discusses the harmful effects of early marriage on adolescent girls and the potentially harmful effects on adolescent boys during adolescence. As a result of early marriage, adolescent girls have to face different health related problems. On the other hand, adolescent boys remain vulnerable to different forms of abuse like addiction to drugs and sexual exploitation etc.",
        "theme": "Gendered vulnerabilities of adolescence and the urgent social need to prevent early marriage.",
        "vocab": [("vulnerable","adj.","ঝুঁকিপূর্ণ","easily harmed","protected"),("addiction","n.","আসক্তি","dependence","freedom"),("exploitation","n.","শোষণ / অপব্যবহার","unfair use","fair treatment"),("conception","n.","গর্ভধারণ","becoming pregnant","--"),("abuse","n.","অপব্যবহার / নির্যাতন","ill-treatment","care"),("harmful","adj.","ক্ষতিকর","damaging","beneficial"),("adolescent","adj.","কিশোর/কিশোরী","teenage","adult")],
        "characters": "Adolescent girls (victims of early marriage), adolescent boys, families, peers.",
        "quotes": ["Early marriage is a silent killer of girls.","Boys without guidance walk towards addiction.","Adolescent boys remain vulnerable to different forms of abuse."],
        "board_q": ["What are the effects of early marriage on girls?","What dangers do adolescent boys face?","Suggest remedies to protect adolescents."],
        "grammar": "On the other hand for contrast: contrasts the situation of girls vs. boys -- discourse connective.",
        "writing": "Problem-solution with gender perspective: Girls issues then boys issues then unified solution.",
        "shortcut": "Early Marriage = EMIL: Early illness, Maternity risk, Identity loss, Loss of education.",
    },
    {
        "no": 26, "title": "The Story of Shilpy", "kind": "Prose",
        "summary": "The passage talks about the struggle of Shilpy, a Bangladeshi teenage girl who is a victim of early marriage. As a cultural practice in rural Bangladesh, Shilpy was married earlier. But, soon she became conscious about the negative effects of early marriage and pregnancy and made her husband aware of the adolescent issues. Gradually, this couple brought a significant change in people's attitudes towards early marriage in their area.",
        "theme": "Awareness and dialogue can transform even the most deeply entrenched harmful cultural practices.",
        "vocab": [("victim","n.","শিকার / ভুক্তভোগী","sufferer","victor"),("conscious","adj.","সচেতন","aware","ignorant"),("attitude","n.","মনোভাব","mindset","action"),("rural","adj.","গ্রামীণ","of the countryside","urban"),("significant","adj.","উল্লেখযোগ্য","important","trivial"),("gradual","adj.","ধীরে ধীরে","step-by-step","sudden"),("cultural","adj.","সাংস্কৃতিক","relating to culture","natural")],
        "characters": "Shilpy (teenage bride), her husband, villagers of their area.",
        "quotes": ["Shilpy became the voice of unspoken pain.","A single aware girl can light a village.","Gradually this couple brought a significant change."],
        "board_q": ["Who is Shilpy?","How did she change attitudes in her area?","What lesson does her story teach?"],
        "grammar": "Past simple narrative sequence: she became conscious, she made her husband aware, they brought change -- sequence of past events.",
        "writing": "Inspirational narrative: Introduce the character and problem then show transformation then describe outward impact then moral.",
        "shortcut": "Shilpy = Speaks, Helps, Inspires, Leads, Protests Young marriage.",
    },
    {
        "no": 27, "title": "Bullying", "kind": "Prose / Report",
        "summary": "This is a report by UNICEF to show the case of bullying of the school aged children both in Bangladesh and in the global arena. A large number of students aged between 13 and 15 are the victims of physical and mental bullying in and around the educational institutions both by the peers and the teachers. Due to bullying, students' academic progress is seriously hampered in the short term. And, bullying can lead them to depression, anxiety and even suicide in the long term.",
        "theme": "Bullying as a global child-rights crisis requiring immediate educational and social intervention.",
        "vocab": [("bully","v.","ভয় দেখানো / হুমকি দেওয়া","intimidate","protect"),("peer","n.","সমবয়সী সহপাঠী","equal-aged person","elder"),("depression","n.","বিষণ্নতা","sadness","happiness"),("anxiety","n.","উদ্বেগ","worry","calm"),("hamper","v.","বাধাগ্রস্ত করা","hinder","assist"),("suicide","n.","আত্মহত্যা","self-killing","survival"),("institution","n.","প্রতিষ্ঠান","organization","--")],
        "characters": "Student victims, bullies, teachers, parents, UNICEF researchers.",
        "quotes": ["In Bangladesh, 35 percent of children face bullying.","Bullying scars the mind, not just the body.","Bullying can lead to depression, anxiety and even suicide."],
        "board_q": ["What is bullying?","Mention its short- and long-term effects.","How can bullying be stopped?"],
        "grammar": "Modal can for potential consequence: bullying can lead to depression -- expresses strong possibility rather than certainty.",
        "writing": "UNICEF report structure: Statistics then definition then cause then short-term effect then long-term effect then recommendation.",
        "shortcut": "Bullying = B + A + D: Body-harm, Anxiety, Depression.",
    },
    {
        "no": 28, "title": "Cyber Bullying", "kind": "Prose / Report",
        "summary": "The passage is about the definition of cyber bullying, the range of this bullying and possible remedies to the problem. Cyber bullying refers to any type of harassment to any person using electronic or social media like Email, Facebook, Whatsapp or Twitter. To prevent this crime, ICT Act 2006 has been introduced in Bangladesh. Besides, several helplines have been set up to provide immediate service to the victims. In short, criminals are warned against committing this type of crime and victims are encouraged to lodge a complaint without hesitation.",
        "theme": "Digital-age abuse, legal protection and victim empowerment through awareness.",
        "vocab": [("cyber","adj.","সাইবার / ইন্টারনেট-সংক্রান্ত","internet-related","offline"),("harassment","n.","হয়রানি","persistent annoyance","support"),("electronic","adj.","বৈদ্যুতিন","digital","manual"),("helpline","n.","সহায়তা ফোন লাইন","support line","--"),("hesitation","n.","দ্বিধা","reluctance","confidence"),("lodge","v.","অভিযোগ দায়ের করা","file a complaint","withdraw"),("remedy","n.","প্রতিকার / সমাধান","solution","problem")],
        "characters": "Victims, online bullies, law enforcement authorities, helpline workers.",
        "quotes": ["Cyber bullying is bullying without borders.","Silence is the bully's best friend.","Victims are encouraged to lodge a complaint without hesitation."],
        "board_q": ["Define cyber bullying.","Mention the laws against cyber bullying in Bangladesh.","How can a victim seek remedy?"],
        "grammar": "Passive for official actions: helplines have been set up, criminals are warned, victims are encouraged -- institutional passive.",
        "writing": "Problem-remedy report: Define the crime then give its range/media then state laws/helplines then advise victims.",
        "shortcut": "Cyber = Click-Yields-Bullying-Easily-on-Receivers.",
    },
    {
        "no": 29, "title": "Table Manners", "kind": "Prose",
        "summary": "The passage talks about the basic concept and necessities of table manners in our everyday life. Table manner means showing respect, politeness and consideration to the people around while dining with them. The passage implies that it is really important to learn how to take foods with others without making them disturbed.",
        "theme": "Decorum at the dining table as a marker of civilized social conduct and respect for others.",
        "vocab": [("manner","n.","শিষ্টাচার / আচরণ","social behaviour","rudeness"),("politeness","n.","ভদ্রতা","courteous conduct","impoliteness"),("consideration","n.","বিবেচনা","thoughtfulness","selfishness"),("dining","n.","ভোজন","eating formally","fasting"),("etiquette","n.","সামাজিক নিয়মাচার","formal manners","rudeness"),("disturb","v.","বিরক্ত করা","annoy","please"),("necessity","n.","প্রয়োজনীয়তা","need","luxury")],
        "characters": "Diners, hosts and guests at the dining table.",
        "quotes": ["Manners make the man.","The table is a small theatre of society.","Table manners mean showing respect and consideration."],
        "board_q": ["What are table manners?","Why are table manners important?","Mention some basic rules of table manners."],
        "grammar": "Gerund as subject: Showing respect, politeness and consideration as the meaning of table manners -- gerund phrase.",
        "writing": "Instructional writing: Define concept then state why important then list specific dos and don'ts.",
        "shortcut": "Table = Think + Adjust + Be-polite + Listen + Eat-quietly.",
    },
    {
        "no": 30, "title": "A Strange Man with a Machine", "kind": "Short Story",
        "summary": "This is a supernatural story about the importance of polite expressions in a society. A strange man snatched away the polite expressions from the people by his peculiar machine. As a result, people became rough and tough due to the lack of politeness. Fortunately, two children with speech difficulty were free from his attack and they restored those expressions with intelligence. Consequently, peace and harmony were restored with the restoration of those expressions.",
        "theme": "The civilising power of polite language and the unexpected value of those considered disabled.",
        "vocab": [("peculiar","adj.","অদ্ভুত / বিচিত্র","odd","ordinary"),("restore","v.","পুনরুদ্ধার করা","bring back","remove"),("supernatural","adj.","অলৌকিক","beyond nature","natural"),("harmony","n.","সম্প্রীতি","accord","discord"),("intelligence","n.","বুদ্ধিমত্তা","cleverness","stupidity"),("rough","adj.","রুক্ষ / কর্কশ","harsh","gentle"),("expression","n.","অভিব্যক্তি","phrase","silence")],
        "characters": "The strange man, two speech-impaired children, the villagers.",
        "quotes": ["A polite word is the cheapest gift on earth.","The mute children spoke louder than the rude.","Peace returned with please and thank you."],
        "board_q": ["Why did the man take away polite expressions?","How did the children restore them?","What is the moral of the story?"],
        "grammar": "Result connectors: As a result, people became rough and Consequently, peace was restored -- cause-effect linkage.",
        "writing": "Fable/moral story: Introduce conflict then escalation then unexpected hero then resolution then moral.",
        "shortcut": "Politeness = Peace + Love + Ease + Affection + Sweetness + Exchange.",
    },
    {
        "no": 31, "title": "Fitness", "kind": "Prose",
        "summary": "The passage deals with the process of meditation and the benefits of it in our daily life. We should start meditation with a straight back and focusing the breath to reach a state of flow. We should continue it for calming the mind and controlling the torrents of thoughts into our mental horizon. Moreover, meditation can provide instant vacations to us at any time and any place. Actually, it is an effective way to exercise our mental muscles and to live a longer and stress-free life.",
        "theme": "Meditation as an everyday mental gym delivering fitness, focus and a stress-free life.",
        "vocab": [("meditation","n.","ধ্যান","mental focus practice","distraction"),("torrent","n.","প্রবল স্রোত","violent stream","trickle"),("flow","n.","সুষম মনোযোগের অবস্থা","focused state","distraction"),("stress","n.","মানসিক চাপ","mental tension","relaxation"),("horizon","n.","মানসিক পরিধি","boundary of mind","center"),("effective","adj.","কার্যকর","efficient","ineffective"),("calming","adj.","প্রশান্তিদায়ক","soothing","agitating")],
        "characters": "The meditating practitioner (the reader).",
        "quotes": ["Meditation is a vacation for the mind.","Breathe in peace, breathe out stress.","Meditation can provide instant vacations at any time."],
        "board_q": ["How does one meditate?","What are the benefits of meditation?","Why is meditation called instant vacation?"],
        "grammar": "Modal should for advice: We should start meditation, We should continue it -- modal expressing recommended action.",
        "writing": "Process description: State starting position then describe steps then list benefits then recommend.",
        "shortcut": "M-Fit = Mind + Focus + Inhale + Tranquillity.",
    },
    {
        "no": 32, "title": "Consumerism", "kind": "Prose",
        "summary": "The extract discusses the reasons and types of spending in our daily life. Money is spent for buying essentials, entertainment and travelling etc. There are two types of spending: necessary and within one's limit and unnecessary and beyond one's limit. The first one makes our life smooth and happy. But the second type of spending makes life stressful and unhappy.",
        "theme": "Mindful spending within one's means as the foundation of personal well-being and contentment.",
        "vocab": [("consumerism","n.","ভোগবাদ / অতিরিক্ত ভোগ","excessive consumption","frugality"),("essential","n.","অপরিহার্য জিনিস","necessary thing","luxury"),("entertainment","n.","বিনোদন","amusement","boredom"),("budget","n.","বাজেট / ব্যয়সীমা","spending plan","overspending"),("unnecessary","adj.","অপ্রয়োজনীয়","not needed","essential"),("stressful","adj.","চাপযুক্ত","anxiety-inducing","relaxing"),("smooth","adj.","মসৃণ / নির্বিঘ্ন","easy","rough")],
        "characters": "Everyday consumers, spenders, families managing budgets.",
        "quotes": ["Spend within your means, dream above them.","A want disguised as need is the costliest item.","The second type of spending makes life stressful."],
        "board_q": ["Define consumerism.","Distinguish the two types of spending.","How does spending pattern affect happiness?"],
        "grammar": "There are two types of classification: There are two types of spending: necessary and unnecessary -- categorization structure.",
        "writing": "Classification: Define concept then classify into types with examples then state effect of each then recommend.",
        "shortcut": "Spending = NWL: Necessary, Within Limits = happiness.",
    },
    {
        "no": 33, "title": "Water, Water Everywhere", "kind": "Prose",
        "summary": "The text is about the disastrous effects of human actions against nature and the river Buriganga has been taken as a case study here. Once the river had a glorious past and Dhaka gained the prestige of being the capital due to its location beside the river. But, because of our inhuman and thoughtless treatments, the river has almost died. If we still remain careless about our cruel treatment towards the rivers, we will cry in want of drinking water in the immediate future.",
        "theme": "Ecological warning: the human cost of killing rivers, using Buriganga as a mirror to our collective failure.",
        "vocab": [("disastrous","adj.","বিধ্বংসী","catastrophic","beneficial"),("prestige","n.","মর্যাদা / গৌরব","high standing","disgrace"),("inhuman","adj.","অমানবিক","cruel","humane"),("thoughtless","adj.","অবিবেচক","careless","thoughtful"),("glorious","adj.","গৌরবময়","magnificent","inglorious"),("careless","adj.","অসতর্ক","negligent","careful"),("immediate","adj.","তাৎক্ষণিক","very near","distant")],
        "characters": "Citizens of Dhaka, factory owners (polluters), environmental activists.",
        "quotes": ["Water, water everywhere, nor any drop to drink.","A river dies when conscience dries.","We will cry in want of drinking water in the immediate future."],
        "board_q": ["How was Buriganga in the past?","Why is the river dying?","What warning does the passage give?"],
        "grammar": "First conditional for warning: If we still remain careless, we will cry in want of water -- real future consequence.",
        "writing": "Cause-effect essay: Describe the glorious past then narrate the decline then identify causes then predict consequences then call to action.",
        "shortcut": "RIVER = Resource + Identity + Vitality + Existence + Refuge.",
    },
    {
        "no": 34, "title": "The Greta Effect", "kind": "Prose / Biography",
        "summary": "The passage is about a brief biography of Greta Thunberg, an environmental activist from Sweden and her struggles to protest against climate change. Greta became aware of climate change from the early age and started strike to force politicians to make policies to stop global warming. She also took some initiatives like Fridays for Future and Global Strike for Climate to protest the climate change. Greta's anti-climate change activities and speeches had a profound effect all over the world and this effect is known as the Greta Effect.",
        "theme": "Youth-led climate activism reshaping global political discourse and inspiring worldwide action.",
        "vocab": [("activist","n.","কর্মী / আন্দোলনকারী","campaigner","bystander"),("climate","n.","জলবায়ু","long-term weather","weather"),("strike","n.","ধর্মঘট / প্রতিবাদ","protest","work"),("policy","n.","নীতি / পরিকল্পনা","plan of action","chaos"),("profound","adj.","গভীর / ব্যাপক","deep","superficial"),("initiative","n.","উদ্যোগ","scheme","inaction"),("global warming","n.","বৈশ্বিক উষ্ণতা","greenhouse effect","cooling")],
        "characters": "Greta Thunberg, world politicians, fellow youth activists (Fridays for Future).",
        "quotes": ["How dare you!","Our house is on fire.","Greta's effect was profound all over the world."],
        "board_q": ["Who is Greta Thunberg?","What is Fridays for Future?","Define the Greta Effect."],
        "grammar": "Passive for naming an effect: this effect is known as the Greta Effect -- passive with known as for formal labelling.",
        "writing": "Biography-argument: Introduce the person then describe key action then show impact then evaluate significance.",
        "shortcut": "Greta = Generation Raising Earth-Truth Activism.",
    },
]

POEMS = [
    {
        "no": 1, "title": "She Walks in Beauty", "poet": "Lord Byron",
        "summary": "Byron contemplates the harmonious beauty of a lady whose outward grace perfectly mirrors the goodness of her mind. The night-and-day balance in her features represents a perfect blend of dark and light, body and soul.",
        "theme": "The poem deals with the ideal beauty consisting of the harmony of mind and body. The poem implies that a person's outward appearance reflects his personality and morality. Here, a lady is presented as matching her outward beauty with inner goodness, creating a sense of harmony between body and mind. Thus, she is presented as equally aesthetically perfect and morally perfect.",
        "vocab": [("aspect","n.","চেহারা / দিক","appearance","interior"),("tender","adj.","কোমল / মৃদু","gentle","harsh"),("serenely","adv.","শান্তভাবে","calmly","agitatedly"),("eloquent","adj.","বাগ্মী / অভিব্যক্তিময়","expressive","mute"),("grace","n.","সৌন্দর্য / মনোমুগ্ধকর ভাব","elegance","clumsiness"),("harmonious","adj.","সুষম / সামঞ্জস্যপূর্ণ","balanced","discordant"),("morality","n.","নৈতিকতা","virtue","immorality")],
        "characters": "The unnamed beautiful lady, the speaker (admirer).",
        "quotes": ["She walks in beauty, like the night.","A mind at peace with all below.","All that's best of dark and bright / Meet in her aspect and her eyes."],
        "board_q": ["What does the poem suggest about ideal beauty?","Explain the night imagery in the poem.","How does the poet link body and mind?"],
        "grammar": "Simile: She walks in beauty, like the night -- comparison using like to evoke mood and appearance simultaneously.",
        "writing": "Descriptive composition: Use sensory imagery to portray a person. Balance physical description with inner qualities.",
        "shortcut": "Beauty = Body + Mind in Harmony (dark + bright = perfect).",
    },
    {
        "no": 2, "title": "I Died for Beauty", "poet": "Emily Dickinson",
        "summary": "Two strangers, one who died for beauty and another for truth, lie buried side by side and converse like kinsmen until moss covers their lips and names -- suggesting beauty and truth are one.",
        "theme": "The poem deals with the themes of beauty and truth. The poet portrays them as parallel in various ways. Both are presented by someone who died for them, both are buried in the same tomb near each other, and their names are covered by the same moss. Thus, the poem indicates that beauty and truth are like two parts of the same coin.",
        "vocab": [("kinsmen","n.","আত্মীয় / স্বজন","relatives","strangers"),("moss","n.","শ্যাওলা","plant covering","flower"),("tomb","n.","সমাধি","grave","cradle"),("brethren","n.","ভাই / সহোদর","brothers","enemies"),("adjusted","v.","মানিয়ে নেওয়া","settled","disturbed"),("scarce","adv.","সবে / কষ্টে","barely","easily"),("parallel","adj.","সমান্তরাল","similar","opposite")],
        "characters": "The dead speaker (who died for beauty), a stranger (who died for truth).",
        "quotes": ["I died for Beauty, but was scarce / Adjusted in the Tomb.","Themself are One -- We Brethren are.","And so, as Kinsmen, met a Night."],
        "board_q": ["Who lies near the speaker in the tomb?","How are beauty and truth linked in the poem?","What eventually silences both the voices?"],
        "grammar": "Metaphor: the tomb as a meeting place, moss as the silencer of all discourse -- extended metaphor.",
        "writing": "Thematic essay: Identify the central idea (beauty = truth) then show how the poet develops it through dialogue and setting.",
        "shortcut": "Beauty = Truth (Keats echoed by Dickinson: They are one).",
    },
    {
        "no": 3, "title": "Auld Lang Syne", "poet": "Robert Burns",
        "summary": "A Scottish song celebrating friendship and the remembrance of old times. The speaker and his old friend drink a toast to the past, cherishing memories while promoting goodwill for the future.",
        "theme": "The song focuses on the celebration of friendship and the remembrance of old times. It emphasizes cherishing past memories and old experiences. The song reflects nostalgia for the past while promoting goodwill and unity for the future. In short, it is about valuing relationships and remembering the good old days.",
        "vocab": [("auld","adj.","পুরনো (স্কটিশ)","old","new"),("syne","adv.","সেই থেকে (স্কটিশ)","since","--"),("acquaintance","n.","পরিচিত ব্যক্তি","known person","stranger"),("nostalgia","n.","অতীত স্মৃতির আকুলতা","longing for the past","indifference"),("cherish","v.","লালন করা / মূল্য দেওয়া","treasure","discard"),("goodwill","n.","সৌহার্দ্য / শুভেচ্ছা","benevolence","ill-will"),("kindness","n.","সদয়তা","goodness","cruelty")],
        "characters": "The speaker and his long-absent old friend.",
        "quotes": ["Should auld acquaintance be forgot...","We'll take a cup o' kindness yet.","For auld lang syne, my dear."],
        "board_q": ["What does Auld Lang Syne mean?","What does the cup symbolize?","Why is this song sung on New Year?"],
        "grammar": "Rhetorical question: Should auld acquaintance be forgot? -- not truly asking but implying it should never be forgotten.",
        "writing": "Song/poem analysis: Explain the title then identify the emotional tone (nostalgia) then discuss key imagery (cup, wandering).",
        "shortcut": "ALS = Always Love the Same (old) friends.",
    },
    {
        "no": 4, "title": "I Have Seen Bengal's Face", "poet": "Jibanananda Das",
        "summary": "The poet declares that having seen the timeless natural beauty of Bengal, he has no need to seek beauty elsewhere in the world. He expresses deep love and patriotism for his motherland.",
        "theme": "The theme of this poem is the timeless and everlasting natural beauty of Bengal and the speaker's patriotic zeal aroused at that. He sees how generous nature has been to his motherland. The speaker is in deep love with the beauty of his motherland. He feels that his thirst for beauty has been so quenched that he does not need to see the beauty of the world any more. Overall, it is a tribute to Bengal's identity, history, and emotional landscape.",
        "vocab": [("quench","v.","তৃষ্ণা মেটানো","satisfy","intensify"),("motherland","n.","মাতৃভূমি","native country","foreign land"),("everlasting","adj.","চিরস্থায়ী","endless","temporary"),("zeal","n.","উৎসাহ / নিষ্ঠা","enthusiasm","apathy"),("tribute","n.","শ্রদ্ধাঞ্জলি","praise","criticism"),("generous","adj.","উদার / দানশীল","bountiful","stingy"),("patriotic","adj.","দেশপ্রেমিক","nationalist","unpatriotic")],
        "characters": "The speaker (poet), Bengal's nature as a living presence.",
        "quotes": ["I have seen Bengal's face; therefore I shall not seek beauty elsewhere.","Bengal's beauty is the world's beauty.","How generous nature has been to my motherland."],
        "board_q": ["What has the speaker seen?","Why will he not seek beauty elsewhere?","Explain the patriotic tone of the poem."],
        "grammar": "Present perfect for life-changing experience: I have seen Bengal's face -- the experience that shapes all future choices.",
        "writing": "Patriotic composition: Describe natural beauty then express emotional response then state declaration of devotion.",
        "shortcut": "Bengal = Beauty + Identity + Patriotism (quenches all thirst).",
    },
    {
        "no": 5, "title": "Landscape with the Fall of Icarus", "poet": "William Carlos Williams",
        "summary": "The poem reflects on Brueghel's painting: Icarus falls into the sea unnoticed while the farmer ploughs and the sea sparkles. The world continues, indifferent to individual tragedy.",
        "theme": "The poem shows the indifference of the world to individual suffering. When Icarus falls, life goes unchanged. For example, farmers continue to work and nature thrives. The poem implies how great struggles often go unnoticed in the flow of everyday life.",
        "vocab": [("indifference","n.","উদাসীনতা","lack of concern","concern"),("pageantry","n.","জাঁকজমক","display","plainness"),("insignificantly","adv.","নগণ্যভাবে","unimportantly","significantly"),("tingling","adj.","শিহরণ জাগানো","slight stinging","numbing"),("splash","n.","ছপছপ শব্দ","noise in water","silence"),("concerned","adj.","উদ্বিগ্ন","troubled","indifferent"),("landscape","n.","দৃশ্যপট","scenery","--")],
        "characters": "Icarus (the fallen), the farmer (indifferent), the world as bystander.",
        "quotes": ["...unsignificantly / off the coast / there was / a splash...","The farmer was ploughing his field.","Life goes on, unmoved by tragedy."],
        "board_q": ["What does Brueghel's painting show?","How does the world react to Icarus's fall?","Discuss the theme of indifference in the poem."],
        "grammar": "Free verse enjambment: lines run on without punctuation to reflect the uninterrupted flow of the indifferent world.",
        "writing": "Art-based poem analysis: Describe the image then identify the emotional contrast then discuss the implied theme.",
        "shortcut": "Icarus = Ignored, Crashed, Almost Recorded by Universe Silently.",
    },
    {
        "no": 6, "title": "Dreams (D. H. Lawrence)", "poet": "D. H. Lawrence",
        "summary": "Lawrence distinguishes two kinds of dreams: the unconscious night dream of ordinary people which is hard to materialize, and the bold conscious daydream of ambitious people who strive relentlessly to realize it. The latter is the true dream.",
        "theme": "In this poem, the poet talks about two types of dream. One type of dream is dreamt by the people at night subconsciously. Another type is dreamt by the dangerous people consciously. The first one is merely a dream which is hard to materialize. On the other hand, the second type of dream is the real dream because the dreamer tries his level best to materialize it.",
        "vocab": [("subconscious","adj.","অবচেতন","below awareness","conscious"),("materialize","v.","বাস্তবে রূপ দেওয়া","make real","abandon"),("relentless","adj.","অদম্য / নিরলস","persistent","lazy"),("conscious","adj.","সচেতন / উদ্দেশ্যমূলক","aware","unaware"),("daydream","n.","দিবাস্বপ্ন","waking aspiration","night dream"),("dangerous","adj.","সাহসী / দুঃসাহসিক","bold/ambitious","timid"),("ordinary","adj.","সাধারণ","common","extraordinary")],
        "characters": "Ordinary dreamers (passive), bold day-dreamers (active).",
        "quotes": ["All men dream, but not equally.","The day-dreamers are dangerous men.","The real dream is the one you pursue by day."],
        "board_q": ["What two kinds of dreams does Lawrence mention?","Why are day-dreamers called dangerous?","Which dream is the real dream?"],
        "grammar": "Contrast connector: On the other hand, the second type of dream is the real dream -- presents the positive counterpart.",
        "writing": "Contrast poem essay: Identify two contrasting ideas then explain each then state the poet's preferred idea with reasons.",
        "shortcut": "Dream = D(ay) > N(ight): conscious beats unconscious.",
    },
    {
        "no": 7, "title": "Dreams (Langston Hughes)", "poet": "Langston Hughes",
        "summary": "Hughes urges everyone to hold fast to their dream. If a dream dies, life becomes a broken-winged bird or a barren, snow-covered field -- empty and motionless.",
        "theme": "The poem implies the importance of cherishing a dream in everyone's life. If dream is lost from one's life, his life will be motionless. Without dreams, life becomes meaningless and unproductive. So, everybody must hold fast to a particular dream and try to materialize it.",
        "vocab": [("barren","adj.","ঊষর / নিষ্ফল","empty","fertile"),("broken-winged","adj.","ভাঙা পাখা বিশিষ্ট","disabled/crippled","soaring"),("cherish","v.","লালন করা","hold dear","discard"),("cling","v.","আঁকড়ে ধরা","hold fast","release"),("frozen","adj.","জমে যাওয়া / স্থবির","stilled","flowing"),("meaningless","adj.","অর্থহীন","purposeless","meaningful"),("unproductive","adj.","অনুৎপাদনশীল","fruitless","productive")],
        "characters": "The speaker (Hughes/advisor), the reader/dreamers of all ages.",
        "quotes": ["Hold fast to dreams.","Life is a broken-winged bird that cannot fly.","For if dreams die / Life is a barren field / Frozen with snow."],
        "board_q": ["What happens if dreams die?","Explain the bird imagery in the poem.","Why must one cherish one's dream?"],
        "grammar": "Imperative for advice: Hold fast to dreams -- imperative mood used as a direct command/advice to the reader.",
        "writing": "Motivational paragraph: Start with the imperative (hold your dream) then use imagery to show what happens without it then close with encouragement.",
        "shortcut": "Hold-Fast-Dream = HFD: Hope-Fly-Drive.",
    },
    {
        "no": 8, "title": "Those Winter Sundays", "poet": "Robert Hayden",
        "summary": "A grown son recalls his father's silent labour on cold Sunday mornings -- making fire, polishing shoes -- a sacrifice never acknowledged. Only in adulthood does the speaker realize love's austere and lonely offices.",
        "theme": "Here the poet implies the selfless sacrifice of a father for his family despite not being appreciated properly. The father in the poem not only works outside for the whole week but also works on the holidays for the comfort of the family members. Yet, his sacrifice is not understood properly and he always remains lonely.",
        "vocab": [("blueblack","adj.","কালো-নীলাভ (তীব্র শীতের রং)","very dark cold","warm"),("austere","adj.","কঠোর / সংযত","stern","indulgent"),("office","n.","কর্তব্য / দায়িত্ব","duty","privilege"),("chronic","adj.","দীর্ঘস্থায়ী","constant","temporary"),("indifferently","adv.","উদাসীনভাবে","carelessly","attentively"),("sacrifice","n.","ত্যাগ","selflessness","selfishness"),("regret","n.","অনুতাপ","remorse","satisfaction")],
        "characters": "The speaker (grown son), the father (silent, selfless).",
        "quotes": ["Sundays too my father got up early.","What did I know of love's austere and lonely offices?","No one ever thanked him."],
        "board_q": ["What did the father do on cold Sunday mornings?","How is love described as austere?","Discuss the speaker's regret in the poem."],
        "grammar": "Rhetorical question for regret: What did I know of love's austere and lonely offices? -- expresses guilt, not a real inquiry.",
        "writing": "Reflective paragraph: Describe a childhood scene then show what was missed at the time then reflect with adult understanding.",
        "shortcut": "Father = Fire + Austerity + Tireless + Heat + Endurance + Regret.",
    },
    {
        "no": 9, "title": "How Do I Love Thee?", "poet": "E. B. Browning",
        "summary": "A sonnet enumerating the many ways the speaker loves her beloved -- in depth, breadth and height of soul, by sun and candlelight, freely and passionately -- and vows to love him even better after death.",
        "theme": "Here the poet expresses her deep and unconditional love for her beloved in different ways. She expresses that her love for her beloved occupies every sphere of her life, from daily needs to spiritual longings. She also implies that her love is pure and eternal that will be stronger in the afterlife. This poem is the reflection of a perfect and everlasting bondage of the speaker with her beloved.",
        "vocab": [("thee","pron.","তোমাকে (পুরনো ইংরেজি)","you (archaic)","--"),("depth","n.","গভীরতা","deep extent","shallowness"),("breadth","n.","প্রশস্ততা / বিস্তার","width","narrowness"),("passion","n.","তীব্র আবেগ","intense love","indifference"),("eternal","adj.","চিরন্তন","everlasting","temporary"),("spiritual","adj.","আধ্যাত্মিক","of the soul","physical"),("unconditional","adj.","নিঃশর্ত","absolute","conditional")],
        "characters": "The speaker (Elizabeth Barrett Browning), her beloved (Robert Browning).",
        "quotes": ["How do I love thee? Let me count the ways.","I shall but love thee better after death.","I love thee to the depth and breadth and height / My soul can reach."],
        "board_q": ["How does the poet count the ways of her love?","What is the source of her love?","Comment on the significance of the closing line."],
        "grammar": "Anaphora: I love thee... I love thee... I love thee -- repetition at the start of successive lines for emphasis.",
        "writing": "Love poem analysis: Identify the central declaration then list the different ways love is described then discuss the eternal dimension.",
        "shortcut": "Love = Depth + Breadth + Height + AfterLife.",
    },
    {
        "no": 10, "title": "From September 1, 1939", "poet": "W. H. Auden",
        "summary": "Auden voices the fear, uncertainty and moral exhaustion of ordinary people on the eve of World War II; the clever hopes of a dishonest decade have expired.",
        "theme": "Here the poet implies the tension and anxiety of the general people during the beginning of the second world war. People became uncertain of their future, worried about the violation of their private life and afraid of the smell of imminent death as all their hopes to avoid the war got expired. This poem is a clear indication to the stressed and depressed mental condition of the people on the very beginning of the second world war.",
        "vocab": [("clever","adj.","চালাক / কৌশলী","ingenious","foolish"),("dishonest","adj.","অসৎ","deceitful","honest"),("decade","n.","দশক","ten years","century"),("anxiety","n.","উদ্বেগ","worry","calmness"),("imminent","adj.","আসন্ন","about to happen","distant"),("expire","v.","শেষ হয়ে যাওয়া","end/die","renew"),("tension","n.","উত্তেজনা / চাপ","strain","ease")],
        "characters": "The speaker (Auden), common citizens, politicians/dictators.",
        "quotes": ["The clever hopes expire / Of a low dishonest decade.","We must love one another or die.","I sit in one of the dives / On Fifty-second Street."],
        "board_q": ["What is the overall mood of the poem?","Why is the decade called dishonest?","Which war does the poem refer to?"],
        "grammar": "Metaphor: clever hopes expire -- hopes are personified as living things that can die; low dishonest decade -- decade given moral attributes.",
        "writing": "Historical poem analysis: Identify the date/context then describe the collective mood then quote key lines then explain the social message.",
        "shortcut": "1.9.1939 = Imminent War + Anxious World + Dying Hope.",
    },
    {
        "no": 11, "title": "Alone", "poet": "Maya Angelou",
        "summary": "The speaker repeatedly declares that nobody can survive emotionally alone. Even billionaires suffer from loneliness; only solidarity and human connection can heal the soul.",
        "theme": "The poem implies the importance of solidarity and spiritual connection among the human beings to lead a peaceful life. Without emotional connection among the people, nobody can live peacefully on earth. However, money and wealth cannot cure emotional diseases. Only close relation with others can heal human sufferings in the society.",
        "vocab": [("solidarity","n.","সংহতি / ঐক্য","unity","isolation"),("loneliness","n.","একাকিত্ব","solitude","togetherness"),("billionaire","n.","কোটিপতি","very rich person","pauper"),("storm","n.","ঝড় / বিপদ","trouble","calm"),("cure","v.","নিরাময় করা","remedy","worsen"),("spiritual","adj.","আধ্যাত্মিক","of the soul","material"),("wealth","n.","সম্পদ","riches","poverty")],
        "characters": "The speaker (Angelou), the wealthy, humanity in general.",
        "quotes": ["Nobody, but nobody, can make it out here alone.","Their wives run round like banshees.","Alone, all alone -- nobody, but nobody can make it out here alone."],
        "board_q": ["Why can't anyone live alone according to Angelou?","What does money fail to cure?","Explain the concept of solidarity in the poem."],
        "grammar": "Repetition for emphasis: Nobody, but nobody and Alone, all alone -- repeated structures to reinforce the message.",
        "writing": "Persuasive essay: Use the poem's argument (money can't cure loneliness) then support with examples then call for human connection.",
        "shortcut": "Alone = A Life Of Naked Emptiness.",
    },
    {
        "no": 12, "title": "The Ghost of Tom Joad", "poet": "Bruce Springsteen",
        "summary": "Echoing Steinbeck's Tom Joad, the song spotlights the homeless, poor and marginalized who endure injustice and hardship; it calls for compassion and collective resistance.",
        "theme": "The poem highlights the struggles of the poor, homeless, and marginalized people who live with hardship, fear, and injustice. It shows how society often ignores these suffering individuals. Through the symbol of Tom Joad's ghost, the composer emphasizes the need for compassion, solidarity, and standing up against inequality.",
        "vocab": [("ghost","n.","অশরীরী / প্রতীক","spirit/symbol","living person"),("homeless","adj.","গৃহহীন","without home","housed"),("marginalized","adj.","প্রান্তিক / উপেক্ষিত","sidelined","central"),("injustice","n.","অন্যায় / বৈষম্য","unfairness","justice"),("compassion","n.","সহানুভূতি","sympathy","cruelty"),("solidarity","n.","সংহতি","unity","division"),("hardship","n.","কষ্ট / দুর্দশা","suffering","comfort")],
        "characters": "Tom Joad (symbolic ghost), the poor and homeless, the singer as witness.",
        "quotes": ["Wherever there's somebody fighting for a place to stand... I'll be there.","The highway is alive tonight.","Tom Joad's ghost will never rest."],
        "board_q": ["Who is Tom Joad?","Whose voice is heard in the poem?","What is the social message of the poem?"],
        "grammar": "Symbol: The Ghost of Tom Joad -- a literary allusion using a fictional character as a symbol for all the oppressed.",
        "writing": "Social protest song analysis: Identify the oppressed group then describe their conditions then explain the symbol then state the message.",
        "shortcut": "Joad = Justice Out of Adversity and Despair.",
    },
    {
        "no": 13, "title": "Peace", "poet": "Henry Vaughan",
        "summary": "The speaker tells his soul that true peace is not found in earthly beauty, wealth or knowledge but only in faith -- in a country far beyond the stars, guarded by one born in a manger (Christ).",
        "theme": "The poem explores the spiritual search for true peace. It shows that worldly beauty, wealth, or knowledge cannot bring long lasting peace. Real peace is found only through faith in religion which is symbolized in the poem by Jesus Christ and his twelve followers.",
        "vocab": [("soul","n.","আত্মা","spirit","body"),("sentry","n.","প্রহরী / সৈনিক","guard","prisoner"),("manger","n.","গোশালার খাবার পাত্র","feeding trough","throne"),("ranges","v.","বিস্তৃত হওয়া","extends","shrinks"),("eternal","adj.","চিরন্তন","everlasting","mortal"),("worldly","adj.","জাগতিক / পার্থিব","earthly","spiritual"),("faith","n.","বিশ্বাস / ধর্মীয় আস্থা","religious belief","doubt")],
        "characters": "The soul (addressed), Christ (the commander born in a manger), the twelve followers.",
        "quotes": ["My soul, there is a country far beyond the stars.","One born in a manger commands the beauteous files.","Real peace is found only through faith."],
        "board_q": ["Where is true peace to be found?","Who is the commander in the poem?","Explain the religious symbolism in the poem."],
        "grammar": "Apostrophe: My soul, there is a country -- direct address to an abstraction (the soul) as if it were a person.",
        "writing": "Spiritual poem analysis: Identify what is rejected (worldly things) then identify what is affirmed (faith) then explain the symbolism.",
        "shortcut": "Peace = Prayer + Eternity + Abode + Christ + Everlasting.",
    },
    {
        "no": 14, "title": "Blowin' in the Wind", "poet": "Bob Dylan",
        "summary": "A series of rhetorical questions about war, racism and oppression -- how many roads, how many deaths, how long? -- whose answers are obvious but ignored. True answers lie in the wind, meaning they depend on human will.",
        "theme": "Here the speaker raises some rhetorical questions before us regarding war, racism and oppression whose answers are known to everybody. He emphasizes that people should think again to sustain these evils. If we truly want to establish peace in the society, there should be an end to war, cruelty, oppression and racism.",
        "vocab": [("rhetorical","adj.","বাগাড়ম্বরপূর্ণ (উত্তর না চেয়ে)","not seeking answer","genuine"),("oppression","n.","নিপীড়ন","cruel rule","freedom"),("dove","n.","শান্তির প্রতীক পাখি","peace symbol","hawk"),("cannonball","n.","কামানের গোলা","weapon of war","peace"),("racism","n.","বর্ণবাদ","race-discrimination","equality"),("sustain","v.","বজায় রাখা","continue","abandon"),("conscience","n.","বিবেক","moral awareness","apathy")],
        "characters": "The speaker (Dylan), humanity (the listener), the oppressed.",
        "quotes": ["The answer, my friend, is blowin' in the wind.","How many roads must a man walk down?","How many deaths will it take till he knows that too many people have died?"],
        "board_q": ["What questions does Dylan raise in the song?","Why are the questions rhetorical?","Where does the speaker say the answers lie?"],
        "grammar": "Anaphora with How many...: repeated structure of rhetorical questions builds emotional urgency throughout the song.",
        "writing": "Protest song essay: Identify the injustices questioned then explain why the questions are rhetorical then state the implicit demand.",
        "shortcut": "Wind = War + Injustice + Neglect + Discrimination.",
    },
    {
        "no": 15, "title": "Endangered Species List Blues", "poet": "Ishmael Reed",
        "summary": "The poet warns that technology, war and pollution are destroying nature and driving species to extinction. What humans call progress is leading to self-destruction; immediate action is needed.",
        "theme": "The poet highlights how the rise of technology, war and pollution is destroying nature. Although humans think that they are progressing, they are actually leading themselves to destruction. The poet implies that we should take immediate action to save the world and the civilization.",
        "vocab": [("endangered","adj.","বিপন্ন / বিপদাপন্ন","at risk of extinction","safe"),("species","n.","প্রজাতি","kind of life","--"),("blues","n.","বিষণ্ন সুর / দুঃখ","sad song","happiness"),("pollution","n.","দূষণ","contamination","purity"),("extinction","n.","বিলুপ্তি","dying out","survival"),("civilization","n.","সভ্যতা","human development","barbarism"),("progress","n.","অগ্রগতি","advancement","regression")],
        "characters": "The earth, vanishing species, mankind (responsible party).",
        "quotes": ["We're on the endangered species list.","Progress is killing us softly.","Take immediate action to save the world."],
        "board_q": ["Why is the poem called blues?","List the threats the poem mentions.","What is the poet's central appeal?"],
        "grammar": "Irony: Although humans think they are progressing, they are actually leading themselves to destruction -- irony between belief and reality.",
        "writing": "Ecological argument: State the threat then list causes then show irony of progress then end with urgent appeal.",
        "shortcut": "List = Loss + Ignorance + Suicide by progress + Technology threat.",
    },
    {
        "no": 16, "title": "Deathbed", "poet": "Kazi Nazrul Islam (trans.)",
        "summary": "The speaker uses metaphors to contrast body and soul. The body is merely a garment for the real self; at death, the self is freed and ascends to its eternal heavenly home. Death is thus a blessing.",
        "theme": "Here the speaker implies the ultimate definition of the self by making a contrast between the body and the soul of human beings using different metaphors. He expresses that human body is nothing but a garment for the self in this earthly life. The real self becomes free and reaches its ultimate heavenly abode within the death of the person. So, death is a blessing for the self from the Almighty.",
        "vocab": [("garment","n.","পোশাক / বস্ত্র","clothing/covering","soul"),("abode","n.","আবাস / নিবাস","dwelling/home","exile"),("transient","adj.","ক্ষণস্থায়ী","passing","eternal"),("metaphor","n.","রূপক","figure of speech","literal"),("blessing","n.","আশীর্বাদ","grace","curse"),("ascend","v.","আরোহণ করা / উপরে যাওয়া","rise","descend"),("Almighty","n.","সর্বশক্তিমান (ঈশ্বর)","God","--")],
        "characters": "The dying self (speaker), the soul, the Almighty.",
        "quotes": ["The body is but a garment for the self.","Death is the gateway to the eternal abode.","The real self becomes free at death."],
        "board_q": ["How is the body described in the poem?","What is the real self?","Why is death called a blessing?"],
        "grammar": "Metaphor: The body is but a garment -- but meaning only/merely, reducing the body to clothing for the soul.",
        "writing": "Philosophical poem essay: Identify the key metaphor then explain body vs. soul contrast then discuss the poet's view of death.",
        "shortcut": "Death = Departure + Eternity + Ascent + True self + Home.",
    },
    {
        "no": 17, "title": "Bird", "poet": "Al Mahmud (trans.)",
        "summary": "The flight of a bird serves as an image of time passing, the transient nature of existence and nature's continuous cycle of change and renewal.",
        "theme": "The poem is about the fleeting beauty and transient nature of existence reflected in the flight of a bird. It shows how the passage of time is marked by the movements of nature. The imagery of bird, wind and sky suggests a harmonious cycle that highlights the idea of continuity and change portraying nature as a powerful force.",
        "vocab": [("fleeting","adj.","ক্ষণস্থায়ী / ক্ষণিক","brief","lasting"),("transient","adj.","অস্থায়ী","short-lived","permanent"),("harmonious","adj.","সুষম / ঐকতানময়","balanced","discordant"),("imagery","n.","চিত্রকল্প","mental picture","literal statement"),("continuity","n.","ধারাবাহিকতা","unbroken flow","discontinuity"),("renewal","n.","নবায়ন / পুনরুজ্জীবন","rejuvenation","decay"),("existence","n.","অস্তিত্ব","being","non-existence")],
        "characters": "The bird (as time and life symbol), the wind, the sky.",
        "quotes": ["The bird carries the hour on its wings.","Time flies as the bird flies.","Nature's harmonious cycle highlights continuity and change."],
        "board_q": ["What does the bird symbolize in the poem?","Discuss the imagery of bird, wind and sky.","How does nature express change in the poem?"],
        "grammar": "Symbolism as extended metaphor: the bird is used throughout to represent time, life and the fleeting nature of beauty.",
        "writing": "Nature poem analysis: Describe the central image (bird) then identify what it symbolizes then discuss the mood/tone.",
        "shortcut": "Bird = Brief + Image of time + Renewal + Dynamic change.",
    },
    {
        "no": 18, "title": "Hope Is the Thing with Feathers", "poet": "Emily Dickinson",
        "summary": "Hope is a bird perched in the soul, singing a tuneless but ceaseless tune. It survives the fiercest storms in the strangest lands and never asks anything in return.",
        "theme": "The speaker implies the importance of Hope in human life by comparing it to a bird. Hope resides deeper in our hearts to inspire us to go ahead facing the challenging situations of life. In return, it does not claim anything from us. This selfless hope is the most precious thing in everyone's life.",
        "vocab": [("perch","v.","বসা / আশ্রয় নেওয়া","sit/settle","fly away"),("abash","v.","লজ্জিত করা","embarrass","encourage"),("gale","n.","ঝড়ো হাওয়া","strong wind","calm"),("extremity","n.","চরম অবস্থা","farthest/hardest point","comfort"),("crumb","n.","ক্ষুদ্র অংশ / টুকরো","tiny piece","whole"),("selfless","adj.","নিঃস্বার্থ","unselfish","selfish"),("precious","adj.","মূল্যবান","invaluable","worthless")],
        "characters": "Hope (personified as a bird), the speaker, any human soul.",
        "quotes": ["Hope is the thing with feathers.","Yet, never, in extremity, / It asked a crumb of me.","Hope perches in the soul and sings the tune without the words."],
        "board_q": ["How does Dickinson describe hope?","Why is hope called selfless?","Discuss the bird symbolism in the poem."],
        "grammar": "Extended metaphor: Hope is compared to a bird throughout -- the bird's qualities (singing, endurance, selflessness) all represent hope.",
        "writing": "Metaphor poem essay: Identify the extended metaphor then list qualities attributed to hope via the bird image then discuss the message.",
        "shortcut": "Hope = Heart's Own Persistent Echo (never asks, always gives).",
    },
]


def esc(s):
    if s is None:
        return ""
    s = str(s)
    for a, b in [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"), ("%", r"\%"), ("$", r"\$"),
        ("#", r"\#"), ("_", r"\_"),
        ("{", r"\{"), ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
        ("\u2018", "`"), ("\u2019", "'"),
        ("\u201c", "``"), ("\u201d", "''"),
        ("\u2013", "--"), ("\u2014", "---"),
        ("\u2026", r"\ldots "),
    ]:
        s = s.replace(a, b)
    return s

def bn_wrap(s):
    return r"{\bn " + s + r"}"

def vocab_block(items):
    out = []
    for word, pos, bn_m, syn, ant in items:
        line = (r"\textbf{" + esc(word) + r"} \textit{" + esc(pos) + r"} "
                + bn_wrap(bn_m)
                + r" \textbullet{} Syn: \textit{" + esc(syn) + r"}"
                + r" \textbullet{} Ant: \textit{" + esc(ant) + r"}")
        out.append(line)
    return r"\par".join(out)

def quotes_block(qs):
    return r" \textbar{} ".join(
        r"``" + esc(q.strip().strip('"').strip("'")) + r"''" for q in qs)

def list_block(items):
    out = [r"\begin{itemize}[leftmargin=3.5mm,itemsep=0pt,topsep=0pt,parsep=0pt,label={\textbullet}]"]
    for it in items:
        out.append(r"\item " + esc(it))
    out.append(r"\end{itemize}")
    return "\n".join(out)

def subhead(label, body):
    return r"\noindent{\footnotesize\textbf{" + esc(label) + r":}} " + body + r"\par"

def item_block(it, kind):
    hc = "authband" if kind == "passage" else "poemband"
    right = esc(it.get("kind","")) if kind == "passage" else esc(it.get("poet",""))
    header = (r"\smallskip\noindent\colorbox{" + hc
              + r"}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize "
              + str(it["no"]) + r". " + esc(it["title"])
              + r" \hfill \textnormal{\scriptsize " + right + r"}}}\par")
    parts = [header]
    parts.append(subhead("Summary", esc(it["summary"])))
    parts.append(subhead("Theme", esc(it["theme"])))
    parts.append(subhead("Vocabulary", vocab_block(it["vocab"])))
    parts.append(subhead("Characters", esc(it["characters"])))
    parts.append(subhead("Key Quotes", quotes_block(it["quotes"])))
    parts.append(r"\noindent{\footnotesize\textbf{Board Questions:}}\par" + list_block(it["board_q"]))
    parts.append(subhead("Grammar", esc(it["grammar"])))
    parts.append(subhead("Writing", esc(it["writing"])))
    parts.append(subhead("Shortcut", esc(it["shortcut"])))
    parts.append(r"\vspace{1.5pt}")
    return "\n".join(parts)

WRITING_GUIDE = r"""

\vspace{3pt}
\noindent\colorbox{guideband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\color{white}\bfseries\footnotesize SMART GUIDE -- HOW TO WRITE SUMMARY \& THEME (Even Without Reading the Text)}}
\vspace{2pt}
\begin{multicols}{2}\scriptsize\justifying

\noindent\colorbox{summaryband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize SUMMARY WRITING -- 8 GOLDEN RULES}}\par
\noindent\textbf{1. Skeleton:} WHO + DID WHAT + WHY/HOW + RESULT/LESSON.\par
\noindent\textbf{2. Start with:} ``The passage/story/poem deals with...'' or ``The text is about...''\par
\noindent\textbf{3. Length:} 4--5 sentences only. No more, no less.\par
\noindent\textbf{4. Tense:} Always \textbf{Simple Present}. The author \textit{describes}, the speaker \textit{says}, the poet \textit{implies}.\par
\noindent\textbf{5. Person:} 3rd person only --- He/She/They/The speaker/The poet. Never write ``I''.\par
\noindent\textbf{6. Avoid:} Direct copy, your opinion, ``I think'', examples from outside the text.\par
\noindent\textbf{7. Title trick:} Never read the text? Use the title as your starting topic.\par
\noindent\textbf{8. Instant Template:}\par
\noindent\colorbox{tmplband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\scriptsize The \textit{[passage/poem/speech]} deals with \textit{[topic]}. \textit{[He/She/The author]} \textit{[main action]}. \textit{[As a result/Thus]}, \textit{[outcome/lesson]}.}}\par

\vspace{3pt}
\noindent\colorbox{themeband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize THEME WRITING -- 8 GOLDEN RULES}}\par
\noindent\textbf{1. Definition:} Theme = ONE central idea/message of the WHOLE text (2--3 sentences max).\par
\noindent\textbf{2. Formula:} \textbf{[Abstract noun]} + \textbf{[active verb phrase]} = theme.\par
\noindent\hspace*{4mm}\textit{e.g.} ``Devotion overcomes death.'' / ``Hope sustains life.''\par
\noindent\textbf{3. Start with:} ``The theme of the passage/poem is...'' or ``The central theme is...''\par
\noindent\textbf{4. NEVER} write a plot point as theme. Write an abstract idea, not a story summary.\par
\noindent\textbf{5. For PROSE:} Ask yourself -- ``What is the main lesson or moral of this text?''\par
\noindent\textbf{6. For POEM:} Ask yourself -- ``What does the poet want me to feel or understand?''\par
\noindent\textbf{7. Title trick:} Extract an abstract noun from the title and build from it.\par
\noindent\hspace*{4mm}\textit{I Have a Dream} $\to$ hope, freedom, justice, equality\par
\noindent\hspace*{4mm}\textit{Alone} $\to$ loneliness, solidarity, human connection\par
\noindent\textbf{8. Instant Template:}\par
\noindent\colorbox{tmplband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\scriptsize The \textit{[central]} theme of the \textit{[passage/poem]} is \textit{[abstract noun]}. The \textit{[author/poet]} implies/shows that \textit{[one-sentence message]}.}}\par

\columnbreak

\noindent\colorbox{vocabband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize KEY ABSTRACT NOUNS FOR THEMES}}\par
\noindent love \textbullet{} sacrifice \textbullet{} courage \textbullet{} hope \textbullet{} freedom \textbullet{} justice \textbullet{} patriotism \textbullet{} perseverance \textbullet{} devotion \textbullet{} friendship \textbullet{} beauty \textbullet{} truth \textbullet{} identity \textbullet{} solidarity \textbullet{} nature \textbullet{} death \textbullet{} equality \textbullet{} tolerance \textbullet{} unity \textbullet{} wisdom \textbullet{} injustice \textbullet{} resilience \textbullet{} innocence \textbullet{} nostalgia \textbullet{} cruelty \textbullet{} corruption\par

\vspace{3pt}
\noindent\colorbox{vocabband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize POWER VERBS FOR SUMMARY (avoid ``says'' or ``tells'')}}\par
\noindent deals with \textbullet{} discusses \textbullet{} describes \textbullet{} implies \textbullet{} portrays \textbullet{} emphasizes \textbullet{} highlights \textbullet{} illustrates \textbullet{} narrates \textbullet{} explores \textbullet{} warns \textbullet{} urges \textbullet{} reveals \textbullet{} depicts \textbullet{} suggests \textbullet{} focuses on \textbullet{} presents \textbullet{} captures \textbullet{} reflects on\par

\vspace{3pt}
\noindent\colorbox{vocabband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize LINKING WORDS FOR SUMMARY \& THEME}}\par
\noindent\textbf{Add idea:} moreover, besides, furthermore, additionally\par
\noindent\textbf{Contrast:} however, but, on the other hand, yet, although\par
\noindent\textbf{Result:} as a result, thus, therefore, consequently, so\par
\noindent\textbf{Conclude:} in short, in brief, overall, ultimately, finally\par

\vspace{3pt}
\noindent\colorbox{vocabband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\bfseries\footnotesize COMMON MISTAKES -- AVOID THESE}}\par
\noindent\textbf{Summary:} \ding{55} Never copy exact lines \ding{55} No personal opinion \ding{55} No first person (I, we, my) \ding{55} No more than 5 sentences\par
\noindent\textbf{Theme:} \ding{55} Do NOT write the story as theme \ding{55} Max 3 sentences \ding{55} No second person (you, your) \ding{55} No single quote as theme\par

\vspace{3pt}
\noindent\colorbox{tmplband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\bfseries\scriptsize PRO EXAM TIP: 2-min plan -- 8-min write -- 1-min check. Read the title + first and last sentence of each paragraph. That is enough to write a full summary and theme answer.}}\par

\end{multicols}
"""

PREAMBLE = r"""
\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage[margin=7mm,top=7mm,bottom=7mm,includefoot]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{ragged2e}
\usepackage{pifont}
\usepackage[hidelinks]{hyperref}
\usepackage[protrusion=false,expansion=false]{microtype}
\pagestyle{empty}
\setlength{\emergencystretch}{15pt}
\hbadness=10000 \tolerance=9999 \hyphenpenalty=100
\sloppy
\raggedbottom
\setmainfont{TeX Gyre Termes}[Ligatures=TeX]
\newfontfamily\hd{TeX Gyre Heros}[Ligatures=TeX]
\newfontfamily\bn{Noto Serif Bengali}[Script=Bengali]
\definecolor{authband}{RGB}{20,40,90}
\definecolor{poemband}{RGB}{120,30,60}
\definecolor{topband}{RGB}{10,10,10}
\definecolor{guideband}{RGB}{0,100,70}
\definecolor{summaryband}{RGB}{30,100,160}
\definecolor{themeband}{RGB}{140,40,100}
\definecolor{vocabband}{RGB}{60,100,40}
\definecolor{tmplband}{RGB}{230,245,220}
\setlength{\columnsep}{6pt}
\setlength{\columnseprule}{0.2pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.5pt}
\linespread{1.03}
\begin{document}
\begin{center}
\noindent\colorbox{topband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\color{white}\bfseries\large HSC English 1st Paper -- Master Note \textnormal{\small (Summary + Theme + Vocabulary + Characters + Quotes + Board Qs + Grammar + Writing + Shortcut)}}}
\end{center}
\vspace{2pt}
\noindent\colorbox{authband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\color{white}\bfseries\footnotesize PART A -- 34 TEXTUAL PASSAGES (Prose, Story, Speech, Biography, Myth)}}
\vspace{1pt}
\begin{multicols}{2}\scriptsize\justifying
__PASSAGES__
\end{multicols}
\vspace{2pt}
\noindent\colorbox{poemband}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\color{white}\bfseries\footnotesize PART B -- 18 TEXTUAL POEMS}}
\vspace{1pt}
\begin{multicols}{2}\scriptsize\justifying
__POEMS__
\end{multicols}
__GUIDE__
\end{document}
"""

passages_block = "\n".join(item_block(p, "passage") for p in PASSAGES)
poems_block = "\n".join(item_block(p, "poem") for p in POEMS)
tex = PREAMBLE.replace("__PASSAGES__", passages_block).replace("__POEMS__", poems_block).replace("__GUIDE__", WRITING_GUIDE)

with open("hsc_english.tex", "w", encoding="utf-8") as fout:
    fout.write(tex)

def run(cmd):
    return subprocess.run(cmd, shell=True).returncode

run("apt-get update -qq 2>/dev/null; apt-get install -y texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-fonts-extra fonts-texgyre fonts-noto-core fonts-noto-extra 2>/dev/null")
run("fc-cache -fv 2>/dev/null")
run("xelatex -interaction=nonstopmode hsc_english.tex")
run("xelatex -interaction=nonstopmode hsc_english.tex")
print("PDF ready:", os.path.exists("hsc_english.pdf"))
