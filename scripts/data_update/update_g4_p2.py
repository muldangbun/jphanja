import json
import os

new_data = [
  {
    "kanji": "希",
    "reading_on": "キ",
    "reading_kun": "まれ",
    "meaning": "바랄 / 드물",
    "components": [
      { "char": "爻", "role": "점괘 효 (요소)", "desc": "실이 엇갈리거나 성긴 모양입니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "베나 천을 뜻합니다." }
    ],
    "story": "베(巾)를 짤 때 실의 간격이 성기어 '드물다'는 뜻에서, 드문 것을 간절히 '바라다'라는 의미가 되었습니다.",
    "example_words": [
      { "word": "希望", "reading": "きぼう", "meaning": "희망", "description": "앞날에 대해 좋은 결과를 바라는(希) 마음(望)입니다." },
      { "word": "希少", "reading": "きしょう", "meaning": "희소", "description": "매우 드물고(希) 적은(少) 상태입니다." }
    ]
  },
  {
    "kanji": "季",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "계절",
    "components": [
      { "char": "禾", "role": "벼 화 (요소)", "desc": "곡식이나 농작물을 의미합니다." },
      { "char": "子", "role": "아들 자 (부수)", "desc": "아이, 작다는 뜻을 줍니다." }
    ],
    "story": "어린(子) 벼(禾)가 자라서 열매를 맺기까지의 기간, 즉 농사를 짓는 한 철인 '계절'을 뜻합니다.",
    "example_words": [
      { "word": "季節", "reading": "きせつ", "meaning": "계절", "description": "일 년을 날씨에 따라 나눈 철(季)의 마디(節)입니다." },
      { "word": "四季", "reading": "しき", "meaning": "사계", "description": "봄, 여름, 가을, 겨울의 네(四) 계절(季)입니다." }
    ]
  },
  {
    "kanji": "紀",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "벼리",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 뜻합니다." },
      { "char": "己", "role": "몸 기 (요소)", "desc": "구분하거나 실을 감는 실패의 모양에서 유래하여 발음 '기/키'를 줍니다." }
    ],
    "story": "실(糸)을 차곡차곡 감아 정리하듯 사물을 질서 있게 구별하는 기준점이나 규칙인 '벼리(근본)' 혹은 '시대'를 뜻합니다.",
    "example_words": [
      { "word": "世紀", "reading": "せいき", "meaning": "세기", "description": "백 년을 한 단위로 묶은(紀) 시대(世)입니다." },
      { "word": "紀行", "reading": "きこう", "meaning": "기행", "description": "여행하며(行) 겪은 일을 기록한(紀) 글입니다." }
    ]
  },
  {
    "kanji": "喜",
    "reading_on": "キ",
    "reading_kun": "よろこ(ぶ)",
    "meaning": "기쁠",
    "components": [
      { "char": "吉", "role": "길할 길 (요소)", "desc": "좋은 일이 생겨 입(口)으로 길하다고 말하는 모습입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입을 크게 벌리고 웃는 모습을 나타냅니다." }
    ],
    "story": "좋은(吉) 일이나 경사가 생겨서 사람들이 입(口)을 모아 기뻐하며 빙그레 웃는다는 뜻입니다.",
    "example_words": [
      { "word": "喜ぶ", "reading": "よろこぶ", "meaning": "기뻐하다", "description": "마음이 즐겁고 흐뭇하여 어쩔 줄 몰라 하는 것입니다." },
      { "word": "喜劇", "reading": "きげき", "meaning": "희극", "description": "사람들을 기쁘게(喜) 하고 웃음을 주는 연극(劇)입니다." }
    ]
  },
  {
    "kanji": "旗",
    "reading_on": "キ",
    "reading_kun": "はた",
    "meaning": "깃발",
    "components": [
      { "char": "方", "role": "모방 (부수)", "desc": "여기서는 나부끼는 깃발(㫃)의 모습에서 변형된 것입니다." },
      { "char": "其", "role": "그 기 (요소)", "desc": "곡식을 까부르는 키 모양으로 발음 '기/키'를 줍니다." }
    ],
    "story": "긴 장대나 줄에 매달아(方의 원래 뜻) 바람에 나부끼게 만들어 표시를 하는 '깃발'을 뜻합니다.",
    "example_words": [
      { "word": "旗", "reading": "はた", "meaning": "깃발", "description": "천이나 종이로 만들어 장대에 달아 표시를 하는 물건입니다." },
      { "word": "国旗", "reading": "こっき", "meaning": "국기", "description": "한 나라(国)를 상징하는 깃발(旗)입니다." }
    ]
  },
  {
    "kanji": "器",
    "reading_on": "キ",
    "reading_kun": "うつわ",
    "meaning": "그릇",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "여기서는 여러 개의 그릇이나 입구를 의미합니다." },
      { "char": "犬", "role": "개 견 (요소)", "desc": "그릇을 지키는 짐승을 나타내거나 큰 그릇을 뜻합니다." }
    ],
    "story": "네 개의 그릇(口) 한가운데에 개(犬)가 앉아 그릇들을 잘 지키고 있는 모양에서, 물건을 담는 '그릇'이나 '기구'를 뜻합니다.",
    "example_words": [
      { "word": "器", "reading": "うつわ", "meaning": "그릇, 인물", "description": "물건을 담는 도구나 사람의 재능, 크기를 뜻합니다." },
      { "word": "楽器", "reading": "がっき", "meaning": "악기", "description": "음악(楽)을 연주하는 도구(器)입니다." }
    ]
  },
  {
    "kanji": "機",
    "reading_on": "キ",
    "reading_kun": "はた",
    "meaning": "틀 (기계 / 기회)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 목재를 뜻합니다." },
      { "char": "幾", "role": "몇 기 (요소)", "desc": "작고 미세한 부품들이 얽혀 있다는 뜻과 발음 '기/키'를 줍니다." }
    ],
    "story": "나무(木)로 만든 복잡하고 미세한(幾) 부품들이 얽힌 베틀이나 '기계', 혹은 어떤 일이 일어나는 중요한 '기회'를 뜻합니다.",
    "example_words": [
      { "word": "機械", "reading": "きかい", "meaning": "기계", "description": "동력을 받아 움직이는 틀(機)이나 장치(械)입니다." },
      { "word": "機会", "reading": "きかい", "meaning": "기회", "description": "어떤 일을 하기에 알맞은 때(機)나 모임(会)입니다." }
    ]
  },
  {
    "kanji": "議",
    "reading_on": "ギ",
    "reading_kun": "",
    "meaning": "의논할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "義", "role": "옳을 의 (요소)", "desc": "옳은 일이나 바른 뜻, 발음 '의/기'를 담당합니다." }
    ],
    "story": "옳고 그름(義)을 가리기 위해 여러 사람이 말(言)을 나누며 바르게 '의논하다'는 뜻입니다.",
    "example_words": [
      { "word": "会議", "reading": "かいぎ", "meaning": "회의", "description": "여러 사람이 모여서(会) 의논하는(議) 것입니다." },
      { "word": "不思議", "reading": "ふしぎ", "meaning": "불가사의, 신비함", "description": "생각(思)하거나 말로 의논할(議) 수 없음(不)을 뜻합니다." }
    ]
  },
  {
    "kanji": "求",
    "reading_on": "キュウ",
    "reading_kun": "もと(める)",
    "meaning": "구할",
    "components": [
      { "char": "水", "role": "물 수 (부수)", "desc": "원래 털가죽 옷의 상형이 점차 변형되어 물 수의 형태가 되었습니다." }
    ],
    "story": "원래 털가죽 옷을 구한다는 뜻에서 유래하여, 지금은 무언가를 간절히 찾고 '구하다' 혹은 '요구하다'는 뜻으로 널리 쓰입니다.",
    "example_words": [
      { "word": "求める", "reading": "もとめる", "meaning": "구하다, 바라다", "description": "원하는 것을 얻으려고 찾거나 요구하는 일입니다." },
      { "word": "要求", "reading": "ようきゅう", "meaning": "요구", "description": "필요하여 달라고 청하고(要) 구하는(求) 것입니다." }
    ]
  },
  {
    "kanji": "泣",
    "reading_on": "キュウ",
    "reading_kun": "な(く)",
    "meaning": "울 (소리 없이)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 눈물을 뜻합니다." },
      { "char": "立", "role": "설 립 (요소)", "desc": "사람이 우두커니 서 있는 모습이나 발음 '립/큐'를 줍니다." }
    ],
    "story": "눈물(氵)을 뚝뚝 흘리며 가만히 서서(立) 소리 없이 서글프게 '울다'는 뜻입니다.",
    "example_words": [
      { "word": "泣く", "reading": "なく", "meaning": "울다", "description": "슬프거나 아파서 눈물을 흘리는 것입니다." },
      { "word": "号泣", "reading": "ごうきゅう", "meaning": "호곡, 통곡", "description": "큰 소리(号)를 내며 슬프게 우는(泣) 일입니다." }
    ]
  },
  {
    "kanji": "救",
    "reading_on": "キュウ",
    "reading_kun": "すく(う)",
    "meaning": "구원할",
    "components": [
      { "char": "求", "role": "구할 구 (요소)", "desc": "무언가를 구하거나 바란다는 뜻과 발음 '구/큐'를 담당합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손으로 치거나 힘을 가하는 동작을 나타냅니다." }
    ],
    "story": "위험에 처해 도움을 구하는(求) 사람을 힘(攵)을 다해 이끌어내어 생명을 '구하다(구원하다)'는 뜻입니다.",
    "example_words": [
      { "word": "救う", "reading": "すくう", "meaning": "구하다", "description": "위험이나 곤란에 빠진 사람을 건져내는 것입니다." },
      { "word": "救急車", "reading": "きゅうきゅうしゃ", "meaning": "구급차", "description": "급한(急) 환자를 구하는(救) 자동차(車)입니다." }
    ]
  },
  {
    "kanji": "給",
    "reading_on": "キュウ",
    "reading_kun": "",
    "meaning": "줄 (공급할)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "合", "role": "합할 합 (요소)", "desc": "모으거나 합친다는 뜻과 발음 '합/큐'를 줍니다." }
    ],
    "story": "모자란 실(糸)을 합하여(合) 채워 준다는 데서 유래하여, 모자란 물건이나 돈을 넉넉하게 '주다' 혹은 '공급하다'는 의미입니다.",
    "example_words": [
      { "word": "給料", "reading": "きゅうりょう", "meaning": "급료, 월급", "description": "일한 대가로 주는(給) 돈(料)입니다." },
      { "word": "供給", "reading": "きょうきゅう", "meaning": "공급", "description": "필요한 것을 마련하여(供) 채워 주는(給) 일입니다." }
    ]
  },
  {
    "kanji": "挙",
    "reading_on": "キョ",
    "reading_kun": "あ(げる)、あ(がる)",
    "meaning": "들 (선거)",
    "components": [
      { "char": "⺍", "role": "불똥 주 (요소)", "desc": "두 손으로 무언가를 받드는 모양입니다." },
      { "char": "手", "role": "손 수 (부수)", "desc": "손의 동작을 뜻합니다." }
    ],
    "story": "두 손(⺍의 본래 뜻)과 아랫손(手)을 합심하여 물건을 위로 번쩍 '들어 올리다', 혹은 행동을 일으키다(거사)나 추천하다(선거)는 뜻입니다.",
    "example_words": [
      { "word": "挙げる", "reading": "あげる", "meaning": "들다, 거행하다", "description": "손을 위로 들거나, 이름이나 예를 내세우는 일입니다." },
      { "word": "選挙", "reading": "せんきょ", "meaning": "선거", "description": "적합한 사람을 골라(選) 내세우는(挙) 일입니다." }
    ]
  },
  {
    "kanji": "漁",
    "reading_on": "ギョ、リョウ",
    "reading_kun": "あさ(る)",
    "meaning": "고기 잡을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 바다를 뜻합니다." },
      { "char": "魚", "role": "고기 어 (요소)", "desc": "물고기를 의미하며 발음 '어/교'를 줍니다." }
    ],
    "story": "바다나 강물(氵)에 나가서 그물 등으로 물고기(魚)를 '잡다(어로)' 혹은 해산물을 구한다는 뜻입니다.",
    "example_words": [
      { "word": "漁業", "reading": "ぎょぎょう", "meaning": "어업", "description": "물고기를 잡는(漁) 산업이나 생업(業)입니다." },
      { "word": "漁師", "reading": "りょうし", "meaning": "어부", "description": "물고기를 잡는 일(漁)을 직업으로 삼는 사람(師)입니다." }
    ]
  },
  {
    "kanji": "共",
    "reading_on": "キョウ",
    "reading_kun": "とも",
    "meaning": "함께",
    "components": [
      { "char": "廿", "role": "스물 입 (요소)", "desc": "원래 두 손으로 물건을 맞잡은 모양을 뜻합니다." },
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "양쪽으로 갈라져서 함께 든다는 뜻입니다." }
    ],
    "story": "두 손으로 무거운 물건을 양쪽에서 '함께(같이)' 맞들어 올리는 모양에서 공통되거나 같이 한다는 뜻을 가집니다.",
    "example_words": [
      { "word": "共に", "reading": "ともに", "meaning": "함께, 같이", "description": "여럿이 다 같이 무언가를 하는 모양입니다." },
      { "word": "共通", "reading": "きょうつう", "meaning": "공통", "description": "여럿이 함께(共) 통하여(通) 쓰는 성질입니다." }
    ]
  },
  {
    "kanji": "協",
    "reading_on": "キョウ",
    "reading_kun": "",
    "meaning": "화합할",
    "components": [
      { "char": "十", "role": "열 십 (부수)", "desc": "여럿이 모인다는 뜻입니다." },
      { "char": "办", "role": "힘 력 세 개 (요소)", "desc": "힘 력(力) 자 세 개가 뭉친 형태(劦)의 약자로 힘을 합친다는 의미입니다." }
    ],
    "story": "열(十, 많음) 사람의 힘(力 세 개)을 하나로 합쳐서 서로 도와주고 사이좋게 '화합하다'는 뜻입니다.",
    "example_words": [
      { "word": "協力", "reading": "きょうりょく", "meaning": "협력", "description": "서로 마음을 화합하여(協) 힘(力)을 합치는 일입니다." },
      { "word": "協会", "reading": "きょうかい", "meaning": "협회", "description": "같은 목적을 가진 사람들이 협력하여(協) 모인 단체(会)입니다." }
    ]
  },
  {
    "kanji": "鏡",
    "reading_on": "キョウ",
    "reading_kun": "かがみ",
    "meaning": "거울",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "금속이나 쇠붙이를 뜻합니다." },
      { "char": "竟", "role": "마칠 경 (요소)", "desc": "끝에 다다른다, 빛이 난다는 뜻과 발음 '경/쿄우'를 줍니다." }
    ],
    "story": "옛날에는 금속(金)의 표면을 반들반들하게 끝까지(竟) 갈고닦아 얼굴을 비추어 보던 '거울'을 뜻합니다.",
    "example_words": [
      { "word": "鏡", "reading": "かがみ", "meaning": "거울", "description": "물체의 모양을 비추어 보는 도구입니다." },
      { "word": "望遠鏡", "reading": "ぼうえんきょう", "meaning": "망원경", "description": "멀리(遠) 떨어진 것을 당겨서 보는(望) 유리 거울(鏡) 장치입니다." }
    ]
  },
  {
    "kanji": "競",
    "reading_on": "キョウ、ケイ",
    "reading_kun": "きそ(う)、せ(る)",
    "meaning": "다툴 (겨룰)",
    "components": [
      { "char": "立", "role": "설 립 (부수)", "desc": "사람이 꼿꼿이 서 있는 모습입니다." },
      { "char": "兄", "role": "맏 형 (요소)", "desc": "말을 많이 하거나 기운이 센 사람을 의미합니다." }
    ],
    "story": "두 사람(立)이 나란히 서서 서로 자신이 형(兄)이라거나 뛰어나다고 우기며 엎치락뒤치락 '다투다' 혹은 '겨루다'는 뜻입니다.",
    "example_words": [
      { "word": "競争", "reading": "きょうそう", "meaning": "경쟁", "description": "이익이나 승리를 차지하기 위해 서로 다투고(競) 싸우는(争) 것입니다." },
      { "word": "競う", "reading": "きそう", "meaning": "겨루다, 경쟁하다", "description": "남과 앞서기를 다투는 일입니다." }
    ]
  },
  {
    "kanji": "極",
    "reading_on": "キョク、ゴク",
    "reading_kun": "きわ(める)、きわ(まる)",
    "meaning": "다할 (극)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "亟", "role": "빠를 극 (요소)", "desc": "급하다, 한계에 다다른다는 뜻과 발음 '극/쿄쿠'를 줍니다." }
    ],
    "story": "나무(木) 기둥 중에서도 가장 높고 한계(亟)에 다다른 제일 끝, 즉 '끝(극)'이나 사물의 최고조를 뜻합니다.",
    "example_words": [
      { "word": "極める", "reading": "きわめる", "meaning": "다하다, 끝까지 가다", "description": "어떤 상태나 한계의 끝까지 이르는 것입니다." },
      { "word": "南極", "reading": "なんきょく", "meaning": "남극", "description": "지구의 가장 남(南)쪽 끝(極)입니다." }
    ]
  },
  {
    "kanji": "訓",
    "reading_on": "クン",
    "reading_kun": "",
    "meaning": "가르칠 (뜻)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 가르치는 것을 뜻합니다." },
      { "char": "川", "role": "내 천 (요소)", "desc": "물이 흐르듯 순조롭게 이끈다는 뜻과 발음 '훈/쿤'을 담당합니다." }
    ],
    "story": "물이 물길(川)을 따라 흐르듯, 사람의 도리를 말(言)로 잘 타일러서 '가르치다' 혹은 한자의 고유한 '뜻(훈)'을 의미합니다.",
    "example_words": [
      { "word": "訓練", "reading": "くんれん", "meaning": "훈련", "description": "가르쳐서(訓) 익숙하게 익히는(練) 일입니다." },
      { "word": "訓読み", "reading": "くんよみ", "meaning": "훈독", "description": "한자의 뜻(訓)을 빌려 일본어 고유어로 읽는(読み) 방식입니다." }
    ]
  },
  {
    "kanji": "軍",
    "reading_on": "グン",
    "reading_kun": "",
    "meaning": "군사",
    "components": [
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "덮개나 포장을 뜻합니다." },
      { "char": "車", "role": "수레 거 (부수)", "desc": "수레나 전차를 뜻합니다." }
    ],
    "story": "덮개나 포장(冖)을 씌운 많은 전차(車)가 모여 진을 치고 있는 막강한 '군사'나 군대 조직을 뜻합니다.",
    "example_words": [
      { "word": "軍隊", "reading": "ぐんたい", "meaning": "군대", "description": "전투를 위해 조직된 군사(軍)의 무리(隊)입니다." },
      { "word": "将軍", "reading": "しょうぐん", "meaning": "장군, 쇼군", "description": "군대(軍)를 거느리는 장수(将)입니다." }
    ]
  },
  {
    "kanji": "郡",
    "reading_on": "グン",
    "reading_kun": "",
    "meaning": "고을",
    "components": [
      { "char": "君", "role": "임금 군 (요소)", "desc": "군주나 지배자를 뜻하며 발음 '군'을 담당합니다." },
      { "char": "阝", "role": "우부방 (부수)", "desc": "고을이나 행정 구역을 뜻합니다." }
    ],
    "story": "임금(君)이 다스리는 지방의 행정 구역, 즉 '고을(군)'이나 '마을'을 뜻합니다.",
    "example_words": [
      { "word": "郡", "reading": "ぐん", "meaning": "군", "description": "시나 도보다 작은 행정 구역 단위입니다." },
      { "word": "郡部", "reading": "ぐんぶ", "meaning": "군부", "description": "행정 구역상 군(郡)에 속하는 지역(部)입니다." }
    ]
  },
  {
    "kanji": "径",
    "reading_on": "ケイ",
    "reading_kun": "みち",
    "meaning": "지름길 (오솔길)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 작은 길을 뜻합니다." },
      { "char": "巠", "role": "물줄기 경 (요소)", "desc": "베틀에서 세로로 길게 뻗은 날실의 모양으로, 꼿꼿하다는 뜻과 발음 '경/케이'를 줍니다. (현대 자형은 圣으로 간략화됨)" }
    ],
    "story": "큰길이 아니라 날실처럼 꼿꼿하고 곧게 난 작은 길(彳), 즉 빨리 갈 수 있는 '지름길'이나 원의 '지름'을 뜻합니다.",
    "example_words": [
      { "word": "直径", "reading": "ちょっけい", "meaning": "직경, 지름", "description": "원의 중심을 지나 곧게(直) 그은 지름길(径)입니다." },
      { "word": "半径", "reading": "はんけい", "meaning": "반경, 반지름", "description": "원이나 구의 지름(径)의 반(半)입니다." }
    ]
  },
  {
    "kanji": "型",
    "reading_on": "ケイ",
    "reading_kun": "かた",
    "meaning": "모형 (틀)",
    "components": [
      { "char": "刑", "role": "형벌 형 (요소)", "desc": "칼로 깎아 반듯한 모양을 만든다는 뜻과 발음 '형/케이'를 담당합니다." },
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 찰흙을 뜻합니다." }
    ],
    "story": "칼로 다듬은(刑) 찰흙(土)으로 그릇이나 쇠붙이를 찍어내기 위해 만든 일정한 모양의 '틀'이나 '모형'을 뜻합니다.",
    "example_words": [
      { "word": "型", "reading": "かた", "meaning": "형, 틀, 타입", "description": "물건을 만들 때 쓰는 틀이나 전형적인 모양입니다." },
      { "word": "血液型", "reading": "けつえきがた", "meaning": "혈액형", "description": "사람의 피(血液)를 구분하는 틀(型)입니다." }
    ]
  },
  {
    "kanji": "景",
    "reading_on": "ケイ",
    "reading_kun": "",
    "meaning": "볕 (경치)",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 태양 빛을 의미합니다." },
      { "char": "京", "role": "서울 경 (요소)", "desc": "높은 언덕이나 건물을 뜻하며 발음 '경/케이'를 줍니다." }
    ],
    "story": "태양(日) 빛이 높은 언덕이나 누각(京) 위에 밝게 비치어 사물의 모습이 선명하게 드러나는 '경치'나 풍경을 뜻합니다.",
    "example_words": [
      { "word": "景色", "reading": "けしき", "meaning": "경치, 풍경", "description": "자연의 아름다운 볕(景)과 색(色)깔입니다." },
      { "word": "風景", "reading": "ふうけい", "meaning": "풍경", "description": "산이나 들의 바람(風)과 경치(景)입니다." }
    ]
  },
  {
    "kanji": "芸",
    "reading_on": "ゲイ",
    "reading_kun": "",
    "meaning": "재주",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 밭을 매는 모양에서 왔습니다." },
      { "char": "云", "role": "이를 운 (요소)", "desc": "원래 埶(심을 예) 자가 약자로 간략화된 것으로, 심거나 가꾸는 재능을 뜻합니다." }
    ],
    "story": "원래 밭에 식물(艹)을 심고(云의 본래 뜻) 가꾸는 재주에서 유래하여, 지금은 학문이나 기예 등 솜씨 좋은 '재주'나 '예술'을 뜻합니다.",
    "example_words": [
      { "word": "芸術", "reading": "げいじゅつ", "meaning": "예술", "description": "미적인 재주(芸)와 기술(術)입니다." },
      { "word": "芸能人", "reading": "げいのうじん", "meaning": "연예인", "description": "대중 앞에서 재주(芸)와 능력을 보여주는 사람(人)입니다." }
    ]
  },
  {
    "kanji": "欠",
    "reading_on": "ケツ",
    "reading_kun": "か(ける)、か(かす)",
    "meaning": "하품 (이지러질)",
    "components": [
      { "char": "欠", "role": "하품 흠 (부수)", "desc": "사람이 입을 크게 벌리고 하품하는 상형문자입니다." }
    ],
    "story": "입을 크게 벌리고 하품을 하는 모양에서 틈이 생겼다는 데서, 이가 빠지듯 일부분이 '떨어져 나가다(이지러지다)' 혹은 부족하다는 뜻이 되었습니다.",
    "example_words": [
      { "word": "欠ける", "reading": "かける", "meaning": "빠지다, 부족하다", "description": "일부분이 떨어져 나가거나 모자란 상태입니다." },
      { "word": "欠席", "reading": "けっせき", "meaning": "결석", "description": "마땅히 있어야 할 자리(席)에서 빠지는(欠) 것입니다." }
    ]
  },
  {
    "kanji": "結",
    "reading_on": "ケツ",
    "reading_kun": "むす(ぶ)、ゆ(う)",
    "meaning": "맺을",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "吉", "role": "길할 길 (요소)", "desc": "단단하고 꽉 차 있다는 뜻과 발음 '길/케츠'를 담당합니다." }
    ],
    "story": "끈이나 실(糸)을 풀리지 않게 단단히(吉) 묶어서 '맺다(매듭짓다)' 혹은 일의 끝을 내거나 결과를 낸다는 뜻입니다.",
    "example_words": [
      { "word": "結ぶ", "reading": "むすぶ", "meaning": "묶다, 맺다", "description": "끈 따위를 매듭지어 잇거나 관계를 맺는 것입니다." },
      { "word": "結婚", "reading": "けっこん", "meaning": "결혼", "description": "남녀가 혼인(婚) 관계를 맺는(結) 일입니다." }
    ]
  },
  {
    "kanji": "建",
    "reading_on": "ケン、コン",
    "reading_kun": "た(てる)、た(つ)",
    "meaning": "세울",
    "components": [
      { "char": "廴", "role": "민책받침 (부수)", "desc": "길을 걷거나 끌어당기는 모양입니다." },
      { "char": "聿", "role": "붓 율 (요소)", "desc": "붓을 똑바로 세워 법도를 정한다는 뜻입니다." }
    ],
    "story": "붓(聿)을 꼿꼿이 세워 법령을 써서 널리 행하게(廴) 한다는 데서 기초를 다져 나라나 건물을 '세우다'는 뜻입니다.",
    "example_words": [
      { "word": "建てる", "reading": "たてる", "meaning": "세우다, 짓다", "description": "건물이나 집을 기초부터 만들어 올리는 일입니다." },
      { "word": "建物", "reading": "たてもの", "meaning": "건물", "description": "땅 위에 세운(建) 구조물(物)입니다." }
    ]
  },
  {
    "kanji": "健",
    "reading_on": "ケン",
    "reading_kun": "すこ(やか)",
    "meaning": "굳셀 (건강할)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "建", "role": "세울 건 (요소)", "desc": "건물을 세우듯 똑바로 서서 튼튼하다는 뜻과 발음 '건/켄'을 줍니다." }
    ],
    "story": "사람(亻)이 막 지어 올린 건물(建)처럼 똑바르고 튼튼하게 서 있어 몸이 '건강하다' 혹은 '굳세다'는 뜻입니다.",
    "example_words": [
      { "word": "健康", "reading": "けんこう", "meaning": "건강", "description": "몸과 마음이 굳세고(健) 편안함(康)입니다." },
      { "word": "健やか", "reading": "すこやか", "meaning": "튼튼함, 건전함", "description": "병 없이 튼튼하고 건강한 모양입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade4.json'
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

print("Grade 4 Part 2 data appended successfully.")
