import json
import os

new_data = [
  {
    "kanji": "在",
    "reading_on": "ザイ",
    "reading_kun": "あ(る)",
    "meaning": "있을",
    "components": [
      { "char": "才", "role": "재주 재 (요소)", "desc": "여기서는 새싹이 돋아나는 모양으로 생명을 뜻합니다." },
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅을 뜻합니다." }
    ],
    "story": "땅(土) 위에 새싹(才의 원형)이 돋아나 생명을 가지고 살아 '있다(존재하다)'라는 뜻입니다.",
    "example_words": [
      { "word": "存在する", "reading": "そんざいする", "meaning": "존재하다", "description": "실제로 생명을 가지고 있거나(存) 살아 있는(在) 것입니다." },
      { "word": "現在", "reading": "げんざい", "meaning": "현재", "description": "지금 눈앞에 나타나(現) 있는(在) 시간입니다." }
    ]
  },
  {
    "kanji": "均",
    "reading_on": "キン",
    "reading_kun": "",
    "meaning": "고를",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅을 뜻합니다." },
      { "char": "匀", "role": "적을 윤 (요소)", "desc": "고르게 나눈다는 뜻과 발음 '윤/킨'을 줍니다." }
    ],
    "story": "거친 흙(土)이나 밭을 농사짓기 좋게 평평하고 고르게(匀) '고르다(균등하게 하다)'는 뜻입니다.",
    "example_words": [
      { "word": "平均", "reading": "へいきん", "meaning": "평균", "description": "여러 수치를 고르게(均) 평평하게(平) 맞춘 값입니다." },
      { "word": "均等", "reading": "きんとう", "meaning": "균등", "description": "고르고(均) 가지런하여 차별이 없는(等) 상태입니다." }
    ]
  },
  {
    "kanji": "基",
    "reading_on": "キ",
    "reading_kun": "もと、もとい",
    "meaning": "터 (기초)",
    "components": [
      { "char": "其", "role": "그 기 (요소)", "desc": "곡식을 까부르는 키 모양에서 사물의 바탕이라는 뜻과 발음 '기/키'를 줍니다." },
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅, 토대를 의미합니다." }
    ],
    "story": "건물을 짓기 위해 흙(土)을 단단하게 다져 놓은 밑바탕(其), 즉 건물의 '터(기초)'를 뜻합니다.",
    "example_words": [
      { "word": "基本", "reading": "きほん", "meaning": "기본", "description": "사물의 터(基)가 되고 근본(本)이 되는 것입니다." },
      { "word": "基礎", "reading": "きそ", "meaning": "기초", "description": "건물의 터(基)를 다지는 주춧돌(礎)처럼 일의 바탕이 되는 것입니다." }
    ]
  },
  {
    "kanji": "報",
    "reading_on": "ホウ",
    "reading_kun": "むく(いる)",
    "meaning": "갚을 (알릴)",
    "components": [
      { "char": "幸", "role": "다행 행 (요소)", "desc": "원래 수갑이나 죄인을 뜻하는 𡴯의 변형입니다." },
      { "char": "卩", "role": "병부 절 (요소)", "desc": "사람이 무릎을 꿇고 있는 모양입니다." },
      { "char": "又", "role": "또 우 (부수)", "desc": "손으로 행동을 취하는 모양입니다." }
    ],
    "story": "죄를 지어 무릎을 꿇은(卩) 죄인(幸 변형)에게 손(又)으로 벌을 주어 죗값을 '치르게 하다(갚다)', 또는 사실을 윗사람에게 '알리다(보고하다)'는 뜻입니다.",
    "example_words": [
      { "word": "報いる", "reading": "むくいる", "meaning": "갚다, 보답하다", "description": "받은 은혜나 원한에 대해 그에 맞게 갚아 주는 것입니다." },
      { "word": "報告", "reading": "ほうこく", "meaning": "보고", "description": "일의 결과를 위로 알려서(告) 갚는(報) 일입니다." }
    ]
  },
  {
    "kanji": "境",
    "reading_on": "キョウ、ケイ",
    "reading_kun": "さかい",
    "meaning": "지경 (경계)",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅을 뜻합니다." },
      { "char": "竟", "role": "마칠 경 (요소)", "desc": "끝에 다다른다는 뜻과 발음 '경/쿄우'를 줍니다." }
    ],
    "story": "어떤 땅(土)의 넓이가 끝나는(竟) 곳, 즉 나라나 지역의 '지경(가장자리)'이나 '경계'를 뜻합니다.",
    "example_words": [
      { "word": "境界", "reading": "きょうかい", "meaning": "경계", "description": "지역이 나뉘는 지경(境)과 한계(界)입니다." },
      { "word": "環境", "reading": "かんきょう", "meaning": "환경", "description": "생물을 둘러싸고(環) 있는 지경(境)이나 주위의 상태입니다." }
    ]
  },
  {
    "kanji": "墓",
    "reading_on": "ボ",
    "reading_kun": "はか",
    "meaning": "무덤",
    "components": [
      { "char": "莫", "role": "없을 막 (요소)", "desc": "해(日)가 풀숲(艹) 아래로 져서 보이지 않는다는 뜻과 발음 '막/보'를 담당합니다." },
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 흙더미를 뜻합니다." }
    ],
    "story": "죽은 사람을 보이지 않게(莫) 땅속 깊이 묻고 그 위에 흙(土)을 덮어 둥글게 쌓아 올린 '무덤'을 뜻합니다.",
    "example_words": [
      { "word": "墓", "reading": "はか", "meaning": "무덤", "description": "죽은 사람을 묻어 놓은 곳입니다." },
      { "word": "墓地", "reading": "ぼち", "meaning": "묘지", "description": "무덤(墓)을 만들어 놓은 땅(地)입니다." }
    ]
  },
  {
    "kanji": "増",
    "reading_on": "ゾウ",
    "reading_kun": "ま(す)、ふ(える)、ふ(やす)",
    "meaning": "더할",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙을 뜻합니다." },
      { "char": "曽", "role": "일찍 증 (요소)", "desc": "겹쳐 있다, 쌓인다는 뜻과 발음 '증/조우'를 줍니다." }
    ],
    "story": "가마솥을 걸기 위해 흙(土)을 층층이 거듭 쌓아 올려(曽) 높이를 '더하다' 혹은 수량이 '늘어나다'는 뜻입니다.",
    "example_words": [
      { "word": "増える", "reading": "ふえる", "meaning": "늘다, 증가하다", "description": "수나 양이 많아지는 것입니다." },
      { "word": "増加", "reading": "ぞうか", "meaning": "증가", "description": "수나 양이 많아져(増) 더해지는(加) 것입니다." }
    ]
  },
  {
    "kanji": "夢",
    "reading_on": "ム",
    "reading_kun": "ゆめ",
    "meaning": "꿈",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "여기서는 눈썹이나 눈을 가리는 덮개를 나타내는 모양(瞢의 변형)입니다." },
      { "char": "罒", "role": "그물망 머리 (요소)", "desc": "눈(目)이 덮여서 잘 보이지 않는다는 뜻입니다." },
      { "char": "夕", "role": "저녁 석 (요소)", "desc": "어두운 저녁이나 밤을 의미합니다." }
    ],
    "story": "어두운 밤(夕)에 잠을 자면서 눈(罒)이 가려진(艹 변형) 채로 꾸는 '꿈'이나 비몽사몽한 상태를 뜻합니다.",
    "example_words": [
      { "word": "夢", "reading": "ゆめ", "meaning": "꿈", "description": "잠자는 동안에 일어나는 착각이나 장래의 희망입니다." },
      { "word": "悪夢", "reading": "あくむ", "meaning": "악몽", "description": "불길하고 나쁜(悪) 꿈(夢)입니다." }
    ]
  },
  {
    "kanji": "妻",
    "reading_on": "サイ",
    "reading_kun": "つま",
    "meaning": "아내",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "원래 여자가 머리에 꽂은 비녀 모양(屮)의 변형입니다." },
      { "char": "⺕", "role": "터진가로왈 (요소)", "desc": "손으로 머리를 다듬는 모양이나 빗자루를 나타냅니다." },
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." }
    ],
    "story": "비녀(十)를 꽂고 머리를 다듬은(⺕) 성인 여성(女), 혹은 손에 빗자루를 들고 집안일을 하는 남편의 짝인 '아내(처)'를 뜻합니다.",
    "example_words": [
      { "word": "妻", "reading": "つま", "meaning": "아내, 처", "description": "결혼한 남자의 짝이 되는 여자입니다." },
      { "word": "夫婦", "reading": "ふうふ", "meaning": "부부", "description": "남편(夫)과 아내(婦)이나, 아내를 뜻하는 다른 한자인 妻로 부처(夫妻)라고도 합니다." }
    ]
  },
  {
    "kanji": "婦",
    "reading_on": "フ",
    "reading_kun": "",
    "meaning": "며느리 (부인)",
    "components": [
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." },
      { "char": "帚", "role": "빗자루 추 (요소)", "desc": "손(⺕)에 빗자루(巾)를 들고 청소하는 모양입니다. (현재 자형은 帰의 오른쪽 부분 ⺕+冖+巾의 형태이나 원래는 帚입니다.)" }
    ],
    "story": "결혼하여 손에 빗자루(帚의 변형)를 들고 집안일을 도맡아 하는 여성인 '부인(아내)'이나 '며느리'를 의미합니다.",
    "example_words": [
      { "word": "主婦", "reading": "しゅふ", "meaning": "주부", "description": "한 집안의 살림을 맡아보는(主) 부인(婦)입니다." },
      { "word": "婦人", "reading": "ふじん", "meaning": "부인, 여성", "description": "결혼한 여자나 성인 여성을 점잖게 부르는 말입니다." }
    ]
  },
  {
    "kanji": "容",
    "reading_on": "ヨウ",
    "reading_kun": "",
    "meaning": "얼굴 (담을)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 건물을 의미합니다." },
      { "char": "谷", "role": "골 곡 (요소)", "desc": "산골짜기처럼 텅 빈 공간이나 얼굴 모양을 뜻하며 발음 '용/요우'를 줍니다." }
    ],
    "story": "집(宀) 안의 골짜기(谷)처럼 텅 빈 넓은 공간에 물건을 넉넉히 '담다(수용하다)', 나아가 담겨 있는 사람의 모습인 '얼굴'을 뜻합니다.",
    "example_words": [
      { "word": "内容", "reading": "ないよう", "meaning": "내용", "description": "그릇이나 사물 안(内)에 담긴(容) 알맹이입니다." },
      { "word": "美容", "reading": "びよう", "meaning": "미용", "description": "얼굴(容)이나 몸매를 아름답게(美) 가꾸는 일입니다." }
    ]
  },
  {
    "kanji": "寄",
    "reading_on": "キ",
    "reading_kun": "よ(る)、よ(せる)",
    "meaning": "부칠 (기댈)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 덮개를 의미합니다." },
      { "char": "奇", "role": "기이할 기 (요소)", "desc": "기이하다는 뜻 외에 기대거나 의지한다는 뜻과 발음 '기/키'를 줍니다." }
    ],
    "story": "남의 집(宀)에 잠시 몸을 의지하여(奇) 신세를 지고 '기대다' 혹은 편지나 물건을 다른 곳으로 '부치다'는 뜻입니다.",
    "example_words": [
      { "word": "寄る", "reading": "よる", "meaning": "들르다, 다가가다", "description": "어떤 곳을 지나가다 잠시 몸을 의탁하거나 가까이 다가가는 것입니다." },
      { "word": "寄付", "reading": "きふ", "meaning": "기부", "description": "자선 사업 등에 돈이나 물건을 대가 없이 부쳐(寄) 주는(付) 일입니다." }
    ]
  },
  {
    "kanji": "富",
    "reading_on": "フ、フウ",
    "reading_kun": "とみ、と(む)",
    "meaning": "부유할",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집을 뜻합니다." },
      { "char": "畐", "role": "가득할 복 (요소)", "desc": "술항아리에 술이 꽉 차 있는 모양에서 넉넉하다는 뜻과 발음 '부/후'를 담당합니다." }
    ],
    "story": "집안(宀) 창고에 재물이 항아리에 술이 차듯 가득(畐) 차 있어서 생활이 넉넉하고 '부유하다(부자)'는 뜻입니다.",
    "example_words": [
      { "word": "豊富", "reading": "ほうふ", "meaning": "풍부", "description": "풍성하고(豊) 넉넉하여 부유함(富)입니다." },
      { "word": "富士山", "reading": "ふじさん", "meaning": "후지산", "description": "일본에서 가장 높은 산의 이름입니다. (富 자를 씁니다)" }
    ]
  },
  {
    "kanji": "導",
    "reading_on": "ドウ",
    "reading_kun": "みちび(く)",
    "meaning": "이끌",
    "components": [
      { "char": "道", "role": "길 도 (요소)", "desc": "길을 뜻하며 발음 '도/도우'를 줍니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손의 동작을 의미합니다." }
    ],
    "story": "손(寸)으로 사람을 잡아당겨 올바른 길(道)로 가도록 안내하고 '이끌다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "導く", "reading": "みちびく", "meaning": "이끌다, 인도하다", "description": "올바른 방향으로 나아가도록 이끌어 주는 것입니다." },
      { "word": "指導", "reading": "しどう", "meaning": "지도", "description": "가르쳐서(指) 어떤 목적이나 방향으로 이끄는(導) 일입니다." }
    ]
  },
  {
    "kanji": "居",
    "reading_on": "キョ",
    "reading_kun": "い(る)",
    "meaning": "살 (거주할)",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "여기서는 사람이 걸터앉아 있는 모양을 나타냅니다." },
      { "char": "古", "role": "예 고 (요소)", "desc": "오래되었다는 뜻과 발음 '고/쿄'를 줍니다." }
    ],
    "story": "사람이 걸터앉아(尸) 한 장소에 아주 오랫동안(古) 머무르며 '살다' 혹은 '거주하다(거처)'라는 뜻입니다.",
    "example_words": [
      { "word": "居る", "reading": "いる", "meaning": "있다", "description": "사람이나 동물이 어느 곳에 머물러 있는 것입니다." },
      { "word": "住居", "reading": "じゅうきょ", "meaning": "주거", "description": "사람이 머물러 살고(住) 거처하는(居) 집입니다." }
    ]
  },
  {
    "kanji": "属",
    "reading_on": "ゾク",
    "reading_kun": "",
    "meaning": "무리 (속할)",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "여기서는 동물의 꼬리를 뜻하는 尾(꼬리 미)의 변형으로 쓰였습니다." },
      { "char": "禹", "role": "하우씨 우 (요소)", "desc": "벌레를 본뜬 모양(촉)의 일부로, 벌레가 꼬리에 꼬리를 물고 이어진다는 뜻과 발음 '촉/조쿠'를 줍니다." }
    ],
    "story": "짐승이나 벌레들이 꼬리에 꼬리를 물고 이어져서(禹 변형) 모여 있는 한 패거리인 '무리'나 윗사람에게 '속하다'는 의미입니다.",
    "example_words": [
      { "word": "所属", "reading": "しょぞく", "meaning": "소속", "description": "어떤 곳(所)이나 단체에 속해(属) 있는 것입니다." },
      { "word": "金属", "reading": "きんぞく", "meaning": "금속", "description": "쇠(金)와 비슷한 무리(属)의 성질을 가진 물질입니다." }
    ]
  },
  {
    "kanji": "布",
    "reading_on": "フ",
    "reading_kun": "ぬの",
    "meaning": "베 (펼)",
    "components": [
      { "char": "𠂇", "role": "왼손 좌 (요소)", "desc": "손의 모양으로 물건을 편다는 뜻을 줍니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "천이나 옷감을 의미합니다." }
    ],
    "story": "손(𠂇)으로 천(巾)을 쫙 '펼치다(반포하다)' 혹은 실을 짜서 만든 옷감인 '베'나 '포'를 의미합니다.",
    "example_words": [
      { "word": "布", "reading": "ぬの", "meaning": "천, 직물", "description": "실로 짜서 옷 따위를 만드는 재료입니다." },
      { "word": "毛布", "reading": "もうふ", "meaning": "모포, 담요", "description": "털(毛)로 짠 두툼한 천(布)입니다." }
    ]
  },
  {
    "kanji": "師",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "스승",
    "components": [
      { "char": "𠂤", "role": "퇴적할 퇴 (요소)", "desc": "작은 언덕이나 흙더미를 뜻합니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "여기서는 여러 사람이 무리 지어 있는 모습을 감싼 장막을 의미합니다." }
    ],
    "story": "언덕(𠂤)에 장막(巾)을 치고 진을 친 군사의 무리나 무리의 우두머리를 뜻했으나, 나중에는 사람들을 가르치는 '스승'이나 전문가를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "教師", "reading": "きょうし", "meaning": "교사", "description": "학생들을 가르치는(教) 직업을 가진 사람(師)입니다." },
      { "word": "医師", "reading": "いし", "meaning": "의사", "description": "의술(医)을 전문으로 하는 전문가(師)입니다." }
    ]
  },
  {
    "kanji": "常",
    "reading_on": "ジョウ",
    "reading_kun": "つね、とこ",
    "meaning": "항상",
    "components": [
      { "char": "尚", "role": "오히려 상 (요소)", "desc": "높인다, 오래간다는 뜻과 발음 '상/조우'를 담당합니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "치마나 천을 뜻합니다." }
    ],
    "story": "치마(巾)를 오래 입어 변치 않는다는 데서, 오랫동안 변하지 않고 '항상' 그대로이거나 평범한 상태를 뜻합니다.",
    "example_words": [
      { "word": "常に", "reading": "つねに", "meaning": "항상, 늘", "description": "언제나 변함없이 그러한 상태입니다." },
      { "word": "日常", "reading": "にちじょう", "meaning": "일상", "description": "매일(日) 반복되는 평범한(常) 하루하루입니다." }
    ]
  },
  {
    "kanji": "幹",
    "reading_on": "カン",
    "reading_kun": "みき",
    "meaning": "줄기 (주관할)",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "나뭇가지를 뜻합니다." },
      { "char": "早", "role": "이를 조 (요소)", "desc": "아침 해 모양이나 여기서 발음 '조/칸'의 변형 역할을 합니다." },
      { "char": "干", "role": "방패 간 (부수)", "desc": "나뭇가지나 기둥을 지탱한다는 뜻과 발음 '간/칸'을 줍니다." }
    ],
    "story": "나뭇가지들이 뻗어 나갈 수 있도록 가운데서 단단히 버티고(干) 서 있는 굵은 '줄기'나 일의 핵심을 맡아 '주관하다'는 뜻입니다.",
    "example_words": [
      { "word": "幹", "reading": "みき", "meaning": "줄기", "description": "나무의 뿌리에서 뻗어 나와 가지가 돋는 중심 부분입니다." },
      { "word": "新幹線", "reading": "しんかんせん", "meaning": "신칸센", "description": "일본의 새로운(新) 굵은 줄기(幹) 같은 주요 철도선(線)입니다." }
    ]
  },
  {
    "kanji": "序",
    "reading_on": "ジョ",
    "reading_kun": "",
    "meaning": "차례 (머리말)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "건물이나 집을 뜻합니다." },
      { "char": "予", "role": "나 여 (요소)", "desc": "베틀에서 실을 밀어낸다는 뜻에서 미리(예)나 차례로 뺀다는 의미와 발음 '여/조'를 줍니다." }
    ],
    "story": "건물(广)의 본채 옆에 실을 짜듯 순서대로 길게 낸 담장이나 곁채의 모양에서, 일이 진행되는 순서인 '차례'나 책의 첫머리인 '서문'을 뜻합니다.",
    "example_words": [
      { "word": "順序", "reading": "じゅんじょ", "meaning": "순서", "description": "정해진 차례(順)나 단계(序)입니다." },
      { "word": "序文", "reading": "じょぶん", "meaning": "서문", "description": "책의 맨 앞 차례(序)에 적어 놓은 글(文)입니다." }
    ]
  },
  {
    "kanji": "弁",
    "reading_on": "ベン",
    "reading_kun": "",
    "meaning": "분별할",
    "components": [
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "원래 두 손(廾) 모양이 변형된 것입니다." },
      { "char": "廾", "role": "스물입발 (부수)", "desc": "두 손으로 무언가를 다루는 모양입니다." }
    ],
    "story": "원래 辨(분별할 변)과 辯(말씀 변) 등의 약자로 쓰이는 글자로, 칼로 쪼개듯 사리를 '분별하다' 혹은 말솜씨(변론)를 뜻합니다. 또 덮개(밸브)라는 뜻도 있습니다.",
    "example_words": [
      { "word": "弁当", "reading": "べんとう", "meaning": "도시락", "description": "바깥에서 간편하게 식사를 해결하기 위해(当) 구별하여(弁) 싸는 밥입니다." },
      { "word": "弁護士", "reading": "べんごし", "meaning": "변호사", "description": "법정에서 말을 잘 분별하여(弁) 피고를 보호해(護) 주는 사람(士)입니다." }
    ]
  },
  {
    "kanji": "張",
    "reading_on": "チョウ",
    "reading_kun": "は(る)",
    "meaning": "베풀 (당길)",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "활이나 활시위를 의미합니다." },
      { "char": "長", "role": "길 장 (요소)", "desc": "길다는 뜻과 발음 '장/쵸우'를 담당합니다." }
    ],
    "story": "활(弓)의 시위를 길게(長) 쭉 '당기다' 혹은 천을 팽팽하게 펴서 '베풀다(펼치다)'라는 의미를 지닙니다.",
    "example_words": [
      { "word": "張る", "reading": "はる", "meaning": "뻗다, 팽팽해지다", "description": "줄이 팽팽하게 당겨지거나 얼음이 어는 모양입니다." },
      { "word": "出張", "reading": "しゅっちょう", "meaning": "출장", "description": "일을 위해 멀리 밖으로 나가서(出) 활동을 펼치는(張) 것입니다." }
    ]
  },
  {
    "kanji": "往",
    "reading_on": "オウ",
    "reading_kun": "",
    "meaning": "갈 (왕)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "主", "role": "주인 주 (요소)", "desc": "등불 모양에서 발음 '주/오우'의 변형 역할을 하며, 여기서는 왕(王)과 결합하여 앞으로 뻗어간다는 의미를 줍니다." }
    ],
    "story": "사람이 한쪽 방향을 향해 길(彳)을 거침없이 나아가다, 즉 어디론가 '가다(왕)' 혹은 지난 옛날을 뜻합니다.",
    "example_words": [
      { "word": "往復", "reading": "おうふく", "meaning": "왕복", "description": "목적지에 갔다가(往) 다시 돌아오는(復) 일입니다." },
      { "word": "往来", "reading": "おうらい", "meaning": "왕래, 사람의 통행", "description": "가고(往) 오는(来) 일입니다." }
    ]
  },
  {
    "kanji": "復",
    "reading_on": "フク",
    "reading_kun": "",
    "meaning": "회복할",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "复", "role": "돌아올 복 (요소)", "desc": "왔던 길을 되돌아간다는 뜻과 발음 '복/후쿠'를 줍니다." }
    ],
    "story": "어디를 갔다가(彳) 왔던 길로 다시 되돌아와(复) 원래의 상태로 되돌리다, 즉 '회복하다' 혹은 다시 겹친다는 뜻입니다.",
    "example_words": [
      { "word": "往復", "reading": "おうふく", "meaning": "왕복", "description": "갔다가(往) 되돌아오는(復) 것입니다." },
      { "word": "回復", "reading": "かいふく", "meaning": "회복", "description": "나빠진 병이나 상태를 돌이켜(回) 원래대로 되돌리는(復) 일입니다." }
    ]
  },
  {
    "kanji": "徳",
    "reading_on": "トク",
    "reading_kun": "",
    "meaning": "큰 (덕)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 행동함을 뜻합니다." },
      { "char": "直", "role": "곧을 직 (요소)", "desc": "눈(目)으로 똑바로 본다는 뜻입니다." },
      { "char": "心", "role": "마음 심 (요소)", "desc": "마음을 뜻합니다." }
    ],
    "story": "마음(心)에 거짓이 없이 똑바르고(直), 행동(彳)이 바른 사람의 훌륭한 인품이나 은혜인 큰 '덕'을 의미합니다.",
    "example_words": [
      { "word": "道徳", "reading": "どうとく", "meaning": "도덕", "description": "사람이 마땅히 지켜야 할 도리(道)와 훌륭한 인품(徳)입니다." }
    ]
  },
  {
    "kanji": "志",
    "reading_on": "シ",
    "reading_kun": "こころざ(す)、こころざし",
    "meaning": "뜻",
    "components": [
      { "char": "士", "role": "선비 사 (요소)", "desc": "원래 갈 지(之)의 변형으로, 마음이 어떤 방향으로 향한다는 뜻과 발음 '지/시'를 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음을 뜻합니다." }
    ],
    "story": "마음(心)이 어떤 훌륭한 목표나 방향(士 변형)을 향해 쏠려 있는 상태, 즉 무언가를 해내려는 굳은 '뜻'이나 의지를 의미합니다.",
    "example_words": [
      { "word": "志す", "reading": "こころざす", "meaning": "뜻을 두다", "description": "어떤 목표를 향해 마음을 먹고 나아가려는 것입니다." },
      { "word": "意志", "reading": "いし", "meaning": "의지", "description": "무언가를 해내려는 생각(意)과 굳은 뜻(志)입니다." }
    ]
  },
  {
    "kanji": "応",
    "reading_on": "オウ",
    "reading_kun": "こた(える)",
    "meaning": "응할",
    "components": [
      { "char": "广", "role": "엄호 (요소)", "desc": "집이나 건물을 뜻합니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음을 의미합니다." }
    ],
    "story": "원래 응(應)의 약자로, 가슴속(广)에 품고 있던 마음(心)이 바깥의 자극이나 부름을 받아 대답하며 '응하다(반응하다)'는 뜻입니다.",
    "example_words": [
      { "word": "応じる", "reading": "おうじる", "meaning": "응하다", "description": "물음이나 요구에 맞게 답하거나 따르는 것입니다." },
      { "word": "応援", "reading": "おうえん", "meaning": "응원", "description": "옆에서 호응하여(応) 도와주는(援) 일입니다." }
    ]
  },
  {
    "kanji": "快",
    "reading_on": "カイ",
    "reading_kun": "こころよ(い)",
    "meaning": "쾌할",
    "components": [
      { "char": "忄", "role": "심방변 (부수)", "desc": "마음을 의미합니다." },
      { "char": "夬", "role": "터놓을 쾌 (요소)", "desc": "활시위를 당기는 손가락깍지 모양에서, 맺힌 것을 확 풀어버린다는 뜻과 발음 '쾌/카이'를 줍니다." }
    ],
    "story": "마음(忄)속에 막히거나 맺혀 있던 것이 확 풀려(夬) 시원하고 상쾌하여 기분이 '쾌하다(좋다)'는 뜻입니다.",
    "example_words": [
      { "word": "快い", "reading": "こころよい", "meaning": "기분 좋다, 상쾌하다", "description": "몸이나 마음의 느낌이 시원하고 좋은 상태입니다." },
      { "word": "快適", "reading": "かいてき", "meaning": "쾌적", "description": "기분이 좋고(快) 알맞게(適) 편안한 상태입니다." }
    ]
  },
  {
    "kanji": "性",
    "reading_on": "セイ、ショウ",
    "reading_kun": "",
    "meaning": "성품 (성질)",
    "components": [
      { "char": "忄", "role": "심방변 (부수)", "desc": "마음을 의미합니다." },
      { "char": "生", "role": "날 생 (요소)", "desc": "태어나면서부터 주어졌다는 뜻과 발음 '생/세이'를 담당합니다." }
    ],
    "story": "사람이나 사물이 태어날(生) 때부터 마음(忄)속에 가지고 있는 본래의 바탕인 '성품'이나 '성질', 혹은 성별을 뜻합니다.",
    "example_words": [
      { "word": "性格", "reading": "せいかく", "meaning": "성격", "description": "사람의 성품(性)과 격식(格), 즉 본래의 기질입니다." },
      { "word": "男性", "reading": "だんせい", "meaning": "남성", "description": "사내(男)의 성별(性)입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade5.json'
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except:
            data = []
else:
    data = []

# Update or append
existing_kanjis = {d['kanji'] for d in data}
for item in new_data:
    if item['kanji'] not in existing_kanjis:
        data.append(item)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Grade 5 Part 2 data appended successfully.")
