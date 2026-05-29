import json
import os

new_data = [
  {
    "kanji": "簡",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "대쪽 (간단할)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무나 대나무로 만든 죽간을 뜻합니다." },
      { "char": "間", "role": "사이 간 (요소)", "desc": "사이(틈)라는 뜻과 발음 '간/칸'을 줍니다." }
    ],
    "story": "옛날 종이가 없을 때 글을 적던 대나무 조각(竹) 사이(間)의 틈처럼, 글을 짧고 알기 쉽게 줄여 써서 '간단하다' 혹은 '대쪽'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "簡単", "reading": "かんたん", "meaning": "간단", "description": "대나무 편지(簡)처럼 홀로(単) 있어서 복잡하지 않고 쉬운 상태입니다." },
      { "word": "書簡", "reading": "しょかん", "meaning": "서간", "description": "글(書)을 적어 보내는 대나무 편지(簡)입니다." }
    ]
  },
  {
    "kanji": "糖",
    "reading_on": "トウ",
    "reading_kun": "",
    "meaning": "엿 (사탕)",
    "components": [
      { "char": "米", "role": "쌀 미 (부수)", "desc": "쌀이나 곡식을 의미합니다." },
      { "char": "唐", "role": "당나라 당 (요소)", "desc": "말을 많이 한다는 뜻에서 발음 '당/토우'를 줍니다." }
    ],
    "story": "쌀(米)이나 곡식을 고아서 달콤한 맛이 나게 만든 '엿'이나 '설탕', 당분을 뜻합니다.",
    "example_words": [
      { "word": "砂糖", "reading": "さとう", "meaning": "설탕", "description": "모래(砂)처럼 하얗고 고운 가루 모양의 단 엿(糖)입니다." },
      { "word": "糖分", "reading": "とうぶん", "meaning": "당분", "description": "단맛이 나는 엿(糖)의 성분(分)입니다." }
    ]
  },
  {
    "kanji": "系",
    "reading_on": "ケイ",
    "reading_kun": "",
    "meaning": "이을",
    "components": [
      { "char": "丿", "role": "삐침 별 (요소)", "desc": "위에서 아래로 이어지는 모양을 뜻합니다." },
      { "char": "糸", "role": "실 사 (부수)", "desc": "실타래나 실을 뜻합니다." }
    ],
    "story": "가느다란 실(糸)이 위에서 아래로(丿) 길게 이어져 있듯이, 혈통이나 사물이 줄줄이 '이어지다' 혹은 혈통의 '계통'을 뜻합니다.",
    "example_words": [
      { "word": "系統", "reading": "けいとう", "meaning": "계통", "description": "이어져(系) 내려오는 하나의 줄기나 계열입니다." },
      { "word": "体系", "reading": "たいけい", "meaning": "체계", "description": "사물이 뼈대(体)를 갖추고 하나로 이어져(系) 있는 상태입니다." }
    ]
  },
  {
    "kanji": "紅",
    "reading_on": "コウ、ク",
    "reading_kun": "べに、くれない",
    "meaning": "붉을",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 뜻합니다." },
      { "char": "工", "role": "장인 공 (요소)", "desc": "만든다는 뜻과 발음 '공/코우'를 줍니다." }
    ],
    "story": "실(糸)에 잇꽃이나 붉은 염료를 들여(工) 만든 빛깔, 즉 짙고 '붉다' 혹은 '홍색'을 의미합니다.",
    "example_words": [
      { "word": "紅茶", "reading": "こうちゃ", "meaning": "홍차", "description": "발효시켜 붉은(紅) 빛이 나는 차(茶)입니다." },
      { "word": "口紅", "reading": "くちべに", "meaning": "립스틱, 연지", "description": "입술(口)에 바르는 붉은(紅) 화장품입니다." }
    ]
  },
  {
    "kanji": "納",
    "reading_on": "ノウ、ナッ、ナ、ナン、トウ",
    "reading_kun": "おさ(める)、おさ(まる)",
    "meaning": "들일 (바칠)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 옷감을 뜻합니다." },
      { "char": "内", "role": "안 내 (요소)", "desc": "안쪽이나 받아들인다는 뜻과 발음 '내/노우'의 변형 역할을 합니다." }
    ],
    "story": "실(糸)로 짠 고운 옷감이나 세금을 나라나 창고 안(内)으로 들이어 '바치다' 혹은 '거두어들이다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "納める", "reading": "おさめる", "meaning": "바치다, 납부하다", "description": "세금이나 돈 따위를 정해진 곳에 내거나 들여놓는 것입니다." },
      { "word": "納得", "reading": "なっとく", "meaning": "납득", "description": "남의 말이나 상황을 마음으로 받아들여(納) 깨달아 아는(得) 것입니다." }
    ]
  },
  {
    "kanji": "純",
    "reading_on": "ジュン",
    "reading_kun": "",
    "meaning": "순수할",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 의미합니다." },
      { "char": "屯", "role": "진칠 둔 (요소)", "desc": "어린 싹이 자라난다는 뜻에서 순수하다는 의미와 발음 '둔/쥰'의 변형 역할을 합니다." }
    ],
    "story": "다른 색깔로 물들이지 않은 원래의 실(糸)처럼, 티가 없고 깨끗하며 '순수하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "純粋", "reading": "じゅんすい", "meaning": "순수", "description": "잡것이 섞이지 않고(純) 맑고 깨끗한(粋) 모양입니다." },
      { "word": "単純", "reading": "たんじゅん", "meaning": "단순", "description": "홀로(単) 있어 복잡하지 않고 순수한(純) 상태입니다." }
    ]
  },
  {
    "kanji": "絹",
    "reading_on": "ケン",
    "reading_kun": "きぬ",
    "meaning": "명주 (비단)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 옷감을 뜻합니다." },
      { "char": "肙", "role": "장구벌레 연 (요소)", "desc": "작고 둥근 벌레(누에)라는 뜻과 발음 '연/켄'을 줍니다." }
    ],
    "story": "누에(肙) 고치에서 뽑아낸 가늘고 부드러운 실(糸)이나, 그 실로 짠 광택이 나는 옷감인 '명주'나 '비단'을 뜻합니다.",
    "example_words": [
      { "word": "絹", "reading": "きぬ", "meaning": "비단, 명주", "description": "누에고치에서 뽑은 실로 짠 곱고 부드러운 천입니다." },
      { "word": "絹糸", "reading": "きぬいと", "meaning": "명주실", "description": "비단(絹)을 짤 때 쓰는 실(糸)입니다." }
    ]
  },
  {
    "kanji": "縦",
    "reading_on": "ジュウ",
    "reading_kun": "たて",
    "meaning": "세로",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "従", "role": "좇을 종 (요소)", "desc": "앞사람을 따라 걷는다는 뜻에서 똑바로 앞을 향한다는 의미와 발음 '종/쥬우'를 줍니다." }
    ],
    "story": "베틀에서 실(糸)이 사람이 걷는 방향(従)처럼 앞뒤(위아래)로 길게 놓인 날실, 즉 '세로' 방향을 뜻합니다.",
    "example_words": [
      { "word": "縦", "reading": "たて", "meaning": "세로", "description": "위아래로 이어지는 방향이나 선입니다." },
      { "word": "操縦", "reading": "そうじゅう", "meaning": "조종", "description": "비행기나 기계 따위를 마음대로 잡고(操) 세로로(縦) 움직여 다루는 일입니다." }
    ]
  },
  {
    "kanji": "縮",
    "reading_on": "シュク",
    "reading_kun": "ちぢ(む)、ちぢ(まる)、ちぢ(める)、ちぢ(れる)、ちぢ(らす)",
    "meaning": "오그라들",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 뜻합니다." },
      { "char": "宿", "role": "잘 숙 (요소)", "desc": "숙소에 가만히 머문다는 뜻에서 작아진다는 의미와 발음 '숙/슈쿠'를 줍니다." }
    ],
    "story": "빨아 놓은 천이나 실(糸)이 물에 젖어 처음보다 작아지고 '오그라들다' 혹은 크기를 '줄이다'는 뜻입니다.",
    "example_words": [
      { "word": "縮む", "reading": "ちぢむ", "meaning": "오그라들だ, 줄어들다", "description": "길이나 부피 따위가 전보다 작아지는 것입니다." },
      { "word": "短縮", "reading": "たんしゅく", "meaning": "단축", "description": "시간이나 거리를 짧게(短) 줄이는(縮) 것입니다." }
    ]
  },
  {
    "kanji": "署",
    "reading_on": "ショ",
    "reading_kun": "",
    "meaning": "관청 (서명할)",
    "components": [
      { "char": "罒", "role": "그물망 머리 (부수)", "desc": "법망이나 그물을 뜻합니다." },
      { "char": "者", "role": "놈 자 (요소)", "desc": "사람이라는 뜻과 발음 '자/쇼'의 변형 역할을 합니다." }
    ],
    "story": "나라의 법망(罒)을 지키고 관리하는 사람(者)들이 모여 있는 곳, 즉 경찰서나 세무서 같은 '관청(서)'을 뜻하며 공문서에 '서명하다'는 뜻도 있습니다.",
    "example_words": [
      { "word": "警察署", "reading": "けいさつしょ", "meaning": "경찰서", "description": "경찰(警察)이 사무를 보는 관청(署)입니다." },
      { "word": "署名", "reading": "しょめい", "meaning": "서명", "description": "문서 등에 자기의 이름(名)을 서명하여 쓰는(署) 일입니다." }
    ]
  },
  {
    "kanji": "翌",
    "reading_on": "ヨク",
    "reading_kun": "",
    "meaning": "다음 날",
    "components": [
      { "char": "羽", "role": "깃 우 (부수)", "desc": "새의 날개나 나는 것을 뜻합니다." },
      { "char": "立", "role": "설 립 (요소)", "desc": "자리에 선다는 뜻과 발음 '립/요쿠'의 변형 역할을 합니다." }
    ],
    "story": "새가 날개(羽)를 펴고(立) 날아간 후 하루가 지나갔다는 데서, 어떤 날의 그 '다음 날(이튿날)'을 의미합니다.",
    "example_words": [
      { "word": "翌日", "reading": "よくじつ", "meaning": "다음 날, 이튿날", "description": "어떤 날을 기준으로 그 다음(翌)의 날(日)입니다." },
      { "word": "翌年", "reading": "よくねん", "meaning": "다음 해, 이듬해", "description": "어떤 해의 다음(翌) 해(年)입니다." }
    ]
  },
  {
    "kanji": "聖",
    "reading_on": "セイ",
    "reading_kun": "",
    "meaning": "성스러울",
    "components": [
      { "char": "耳", "role": "귀 이 (부수)", "desc": "귀로 잘 듣는다는 뜻입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입으로 바르게 말한다는 뜻입니다." },
      { "char": "王", "role": "임금 왕 (요소)", "desc": "원래 壬(지구)의 변형으로, 신의 뜻을 전한다는 의미와 발음 '정/세이'의 변형 역할을 합니다." }
    ],
    "story": "남의 말을 귀(耳) 담아듣고 입(口)으로 바르게 말하며, 세상(王)의 이치를 잘 아는 훌륭하고 '성스럽다'는 뜻입니다.",
    "example_words": [
      { "word": "神聖", "reading": "しんせい", "meaning": "신성", "description": "신(神)처럼 거룩하고 성스럽고(聖) 위대한 모양입니다." },
      { "word": "聖書", "reading": "せいしょ", "meaning": "성서, 성경", "description": "기독교에서 성스러운(聖) 하나님의 말씀이 담긴 책(書)입니다." }
    ]
  },
  {
    "kanji": "肺",
    "reading_on": "ハイ",
    "reading_kun": "",
    "meaning": "허파",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 사람의 몸통을 뜻합니다." },
      { "char": "市", "role": "저자 시 (요소)", "desc": "시장에 물건이 많이 모여 있다는 뜻에서 숨이 모인다는 의미와 발음 '시/하이'의 변형 역할을 합니다." }
    ],
    "story": "사람의 몸(月)에서 숨을 들이마시고 내쉬며 공기를 모아(市) 호흡하는 중요한 기관인 '허파(폐)'를 뜻합니다.",
    "example_words": [
      { "word": "肺", "reading": "はい", "meaning": "허파, 폐", "description": "가슴속에 있으며 숨을 쉬게 하는 호흡 기관입니다." },
      { "word": "肺炎", "reading": "はいえん", "meaning": "폐렴", "description": "허파(肺)에 세균이 들어가 염증(炎)이 생기는 병입니다." }
    ]
  },
  {
    "kanji": "背",
    "reading_on": "ハイ",
    "reading_kun": "せ、せい、そむ(く)、そむ(ける)",
    "meaning": "등 (배반할)",
    "components": [
      { "char": "北", "role": "북녘 북 (요소)", "desc": "두 사람이 등을 지고 앉은 모양에서 등진다는 뜻과 발음 '북/하이'의 변형 역할을 합니다." },
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 몸을 의미합니다." }
    ],
    "story": "사람의 몸(月)에서 등지고(北) 서로 안 보게 되는 뒷부분, 즉 사람의 '등'이나 키를 뜻하며, 등지고 돌아선다는 데서 '배반하다(등지다)'는 의미도 가집니다.",
    "example_words": [
      { "word": "背", "reading": "せ", "meaning": "등, 키", "description": "사람의 몸 뒤쪽 부분이나, 사람의 몸길이(키)입니다." },
      { "word": "背中", "reading": "せなか", "meaning": "등", "description": "사람의 목 아래부터 허리 위까지의 뒤쪽(背) 가운데(中) 부분입니다." }
    ]
  },
  {
    "kanji": "胸",
    "reading_on": "キョウ",
    "reading_kun": "むね、むな",
    "meaning": "가슴",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 몸을 의미합니다." },
      { "char": "匈", "role": "오랑캐 흉 (요소)", "desc": "가슴속이 답답하다는 뜻과 발음 '흉/쿄우'를 줍니다." }
    ],
    "story": "사람의 몸(月)에서 호흡을 하며 속이 답답하거나 마음을 느끼는 부분인 '가슴'을 의미합니다.",
    "example_words": [
      { "word": "胸", "reading": "むね", "meaning": "가슴", "description": "목의 아래쪽에서 배의 위쪽까지의 몸통 앞부분이나 마음속입니다." },
      { "word": "胸囲", "reading": "きょうい", "meaning": "흉위, 가슴둘레", "description": "가슴(胸)을 한 바퀴 빙 두른(囲) 길이입니다." }
    ]
  },
  {
    "kanji": "脳",
    "reading_on": "ノウ",
    "reading_kun": "",
    "meaning": "뇌",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 사람의 몸을 의미합니다." },
      { "char": "巛", "role": "개미허리 뇌 변형 (요소)", "desc": "머리털이나 뇌수가 꼬불꼬불 모여 있는 모양(𡿺)의 간략한 형태와 발음 '뇌/노우'를 줍니다." }
    ],
    "story": "사람의 몸(月) 중 머리뼈 속에 꼬불꼬불하게(巛) 얽혀 있어 생각과 신경을 조절하는 뇌수를 가리키며 '뇌(골)'를 뜻합니다.",
    "example_words": [
      { "word": "脳", "reading": "のう", "meaning": "뇌", "description": "머리뼈 속에 들어 있어 생각이나 감각을 조절하는 기관입니다." },
      { "word": "首脳", "reading": "しゅのう", "meaning": "수뇌", "description": "가장 중요한 머리(首)나 뇌(脳)처럼, 한 조직의 가장 높은 우두머리입니다." }
    ]
  },
  {
    "kanji": "腹",
    "reading_on": "フク",
    "reading_kun": "はら",
    "meaning": "배 (마음)",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 사람의 몸을 의미합니다." },
      { "char": "复", "role": "돌아올 복 (요소)", "desc": "부풀어 오르고 겹쳐 있다는 뜻과 발음 '복/후쿠'를 줍니다." }
    ],
    "story": "사람의 몸(月) 중 음식을 많이 먹어 겹겹이 겹치고 불룩하게 부풀어 오르는(复) 부분인 '배'나 배 속의 '마음'을 뜻합니다.",
    "example_words": [
      { "word": "腹", "reading": "はら", "meaning": "배", "description": "가슴 아래에서 다리 위까지의 위장이나 내장이 있는 부분입니다." },
      { "word": "空腹", "reading": "くうふく", "meaning": "공복", "description": "배(腹) 속이 텅 비어(空) 배가 고픈 상태입니다." }
    ]
  },
  {
    "kanji": "臓",
    "reading_on": "ゾウ",
    "reading_kun": "",
    "meaning": "오장",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "몸이나 신체의 기관을 의미합니다." },
      { "char": "蔵", "role": "감출 장 (요소)", "desc": "감추어 둔다는 뜻과 발음 '장/조우'를 줍니다." }
    ],
    "story": "사람의 몸(月) 속에 잘 감추어져(蔵) 있는 여러 가지 중요한 내장 기관인 '오장(내장)'을 뜻합니다.",
    "example_words": [
      { "word": "心臓", "reading": "しんぞう", "meaning": "심장", "description": "가슴속에서 피를 온몸으로 뿜어내는 마음(心)의 장기(臓)입니다." },
      { "word": "内臓", "reading": "ないぞう", "meaning": "내장", "description": "몸의 안(内)쪽에 들어 있는 장기(臓)들입니다." }
    ]
  },
  {
    "kanji": "臨",
    "reading_on": "リン",
    "reading_kun": "のぞ(む)",
    "meaning": "임할",
    "components": [
      { "char": "臣", "role": "신하 신 (부수)", "desc": "사람의 눈 모양이나 내려다본다는 뜻입니다." },
      { "char": "卧", "role": "엎드릴 와 (요소)", "desc": "원래 사람이 엎드려 내려다본다는 모양과 빗방울(물건)의 모습이 합쳐진 것입니다." }
    ],
    "story": "높은 곳에서 아래를 엎드려 내려다보듯(臣, 卧), 물건이나 어떤 상황에 바짝 다가가서 부딪치며 '임하다(마주하다)'는 뜻입니다.",
    "example_words": [
      { "word": "臨む", "reading": "のぞむ", "meaning": "임하다, 향하다", "description": "어떤 장소나 사태를 마주 대하거나 다가가는 것입니다." },
      { "word": "臨時", "reading": "りんじ", "meaning": "임시", "description": "정해진 때가 아니라 그때그때 일에 마주하여(臨) 정한 때(時)입니다." }
    ]
  },
  {
    "kanji": "至",
    "reading_on": "シ",
    "reading_kun": "いた(る)",
    "meaning": "이르를",
    "components": [
      { "char": "至", "role": "이를 지 (부수)", "desc": "화살이 날아가 과녁(땅)에 꽂힌 모양을 본뜬 글자입니다." }
    ],
    "story": "화살이 멀리 날아가서 마침내 목적지에 꽂히는 모양에서, 어떤 장소나 시간에 마침내 '이르다(도달하다)' 혹은 '지극하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "至る", "reading": "いたる", "meaning": "이르다, 도달하다", "description": "어떤 목적지나 정도, 시간에 마침내 다다르는 것입니다." },
      { "word": "至急", "reading": "しきゅう", "meaning": "지급, 시급", "description": "지극히(至) 급하게(急) 서둘러야 하는 것입니다." }
    ]
  },
  {
    "kanji": "若",
    "reading_on": "ジャク、ニャク",
    "reading_kun": "わか(い)、も(しくわ)",
    "meaning": "같을 (젊을)",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 식물을 뜻합니다." },
      { "char": "右", "role": "오른 우 (요소)", "desc": "원래 머리를 빗어넘기는 손의 모양에서, 부드럽고 잘 따르는 사람이라는 뜻을 줍니다." }
    ],
    "story": "새로 돋아난 연한 풀(艹)처럼 나이가 적어 신선하고 '젊다', 혹은 '어리다'는 의미를 가지며, 부드럽게 순종한다는 뜻에서 '~와 같다(만약)'라는 뜻도 있습니다.",
    "example_words": [
      { "word": "若い", "reading": "わかい", "meaning": "젊다, 어리다", "description": "나이가 적고 기운이 한창인 상태입니다." },
      { "word": "若者", "reading": "わかもの", "meaning": "젊은이", "description": "나이가 젊은(若) 사람(者)입니다." }
    ]
  },
  {
    "kanji": "著",
    "reading_on": "チョ",
    "reading_kun": "あらわ(す)",
    "meaning": "나타날 (지을)",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀을 뜻합니다." },
      { "char": "者", "role": "놈 자 (요소)", "desc": "여럿이 쌓여 있다는 뜻과 발음 '자/초'의 변형 역할을 합니다." }
    ],
    "story": "풀(艹) 더미가 눈에 띄게 드러나게 모여(者) 있다는 데서, 사물이 뚜렷이 '나타나다(분명하다)' 혹은 글을 눈에 띄게 묶어 '지으다(저술하다)'는 뜻입니다.",
    "example_words": [
      { "word": "著す", "reading": "あらわす", "meaning": "지으다, 저술하다", "description": "책이나 글을 써서 세상에 나타내는 것입니다." },
      { "word": "著者", "reading": "ちょしゃ", "meaning": "저자", "description": "책을 지어낸(著) 사람(者)입니다." }
    ]
  },
  {
    "kanji": "蒸",
    "reading_on": "ジョウ",
    "reading_kun": "む(す)",
    "meaning": "찔",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀을 뜻합니다." },
      { "char": "烝", "role": "찔 증 (요소)", "desc": "뜨거운 김이 위로 솟아오른다는 뜻과 발음 '증/조우'를 줍니다." }
    ],
    "story": "아래에서 솟아오르는 뜨거운 김(烝)으로 풀(艹)이나 음식을 푹 익도록 '찌다(무덥다)' 혹은 '증발하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "蒸す", "reading": "むす", "meaning": "찌다, 무덥다", "description": "음식을 뜨거운 김으로 익히거나, 날씨가 푹푹 찌듯이 몹시 더운 것입니다." },
      { "word": "蒸発", "reading": "じょうはつ", "meaning": "증발", "description": "액체가 기체가 되어 김으로(蒸) 흩어지는(発) 현상입니다." }
    ]
  },
  {
    "kanji": "蔵",
    "reading_on": "ゾウ",
    "reading_kun": "くら",
    "meaning": "감출 (곳집)",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 덮는 것을 의미합니다." },
      { "char": "臧", "role": "착할 장 (요소)", "desc": "도구를 단단히 간직한다는 뜻과 발음 '장/조우'를 줍니다." }
    ],
    "story": "풀(艹)이나 덮개로 귀한 물건(臧)을 덮어 남이 보지 못하게 '감추다' 혹은 그런 물건을 보관해 두는 창고인 '곳집'을 의미합니다.",
    "example_words": [
      { "word": "蔵", "reading": "くら", "meaning": "창고, 곳집", "description": "곡식이나 물건을 안전하게 넣어두는 집입니다." },
      { "word": "貯蔵", "reading": "ちょぞう", "meaning": "저장", "description": "물건을 한곳에 모아(貯) 안전하게 감추어 두는(蔵) 일입니다." }
    ]
  },
  {
    "kanji": "蚕",
    "reading_on": "サン",
    "reading_kun": "かいこ",
    "meaning": "누에",
    "components": [
      { "char": "天", "role": "하늘 천 (요소)", "desc": "원래 잠(朁) 자의 줄임 모양으로, 실을 토해낸다는 의미와 발음 '잠/산'을 줍니다." },
      { "char": "虫", "role": "벌레 훼 (부수)", "desc": "벌레나 곤충을 뜻합니다." }
    ],
    "story": "뽕잎을 먹고 실(天 변형의 의미)을 토해내어 고치를 짓는 유익한 곤충(虫), 즉 '누에'를 뜻합니다.",
    "example_words": [
      { "word": "蚕", "reading": "かいこ", "meaning": "누에", "description": "명주실을 얻기 위해 기르는 뽕잎을 먹는 곤충입니다." },
      { "word": "養蚕", "reading": "ようさん", "meaning": "양잠", "description": "비단을 짜기 위해 누에(蚕)를 기르는(養) 일입니다." }
    ]
  },
  {
    "kanji": "衆",
    "reading_on": "シュウ、シュ",
    "reading_kun": "",
    "meaning": "무리 (많을)",
    "components": [
      { "char": "血", "role": "피 혈 (부수)", "desc": "원래 해(日) 아래에서 피를 나누어 마신다는 뜻이나, 여기서는 눈(目)의 변형으로 여러 사람의 시선을 뜻합니다." },
      { "char": "乑", "role": "사람 인 셋 (요소)", "desc": "여러 사람을 뜻합니다." }
    ],
    "story": "해 아래나 한곳에 많은 사람(乑)이 떼 지어 모여 눈길(血 변형)을 끄는 백성들의 '무리'나 인원이 '많음(군중)'을 뜻합니다.",
    "example_words": [
      { "word": "群衆", "reading": "ぐんしゅう", "meaning": "군중", "description": "한곳에 모인 수많은(群) 사람들의 무리(衆)입니다." },
      { "word": "大衆", "reading": "たいしゅう", "meaning": "대중", "description": "수많고(大) 평범한 사람들의 무리(衆)입니다." }
    ]
  },
  {
    "kanji": "裁",
    "reading_on": "サイ",
    "reading_kun": "た(つ)",
    "meaning": "마름질할 (결단할)",
    "components": [
      { "char": "𢦏", "role": "다칠 재 (요소)", "desc": "무기(창 戈)를 사용하여 상처를 내거나 자른다는 의미와 발음 '재/사이'를 줍니다." },
      { "char": "衣", "role": "옷 의 (부수)", "desc": "옷이나 옷감을 뜻합니다." }
    ],
    "story": "옷감(衣)을 치수에 맞게 칼이나 도구(𢦏)로 잘라서 '마름질하다(자르다)' 혹은 옳고 그름을 딱 잘라 '결단하다(재판하다)'는 뜻입니다.",
    "example_words": [
      { "word": "裁つ", "reading": "たつ", "meaning": "자르다, 재단하다", "description": "옷을 짓기 위해 옷감을 치수에 맞게 베거나 자르는 것입니다." },
      { "word": "裁判", "reading": "さいばん", "meaning": "재판", "description": "법원에서 시시비비를 가려 결단(裁)하여 판단(判)하는 일입니다." }
    ]
  },
  {
    "kanji": "装",
    "reading_on": "ソウ、ショウ",
    "reading_kun": "よそお(う)",
    "meaning": "꾸밀",
    "components": [
      { "char": "壮", "role": "장할 장 (요소)", "desc": "장대하고 훌륭하게 늘어놓는다는 뜻과 발음 '장/소우'를 줍니다." },
      { "char": "衣", "role": "옷 의 (부수)", "desc": "옷이나 입는 것을 의미합니다." }
    ],
    "story": "옷(衣)을 훌륭하고 멋지게(壮) 갖추어 입어 겉모습을 아름답게 '꾸미다(단장하다)' 혹은 여행의 채비를 꾸린다는 뜻입니다.",
    "example_words": [
      { "word": "装う", "reading": "よそおう", "meaning": "꾸미다, 차려입다", "description": "옷이나 장신구로 몸을 예쁘게 꾸미거나 가식적으로 겉을 꾸미는 것입니다." },
      { "word": "服装", "reading": "ふくそう", "meaning": "복장", "description": "몸에 옷(服)을 갖추어 꾸며(装) 입은 맵시입니다." }
    ]
  },
  {
    "kanji": "裏",
    "reading_on": "リ",
    "reading_kun": "うら",
    "meaning": "속 (뒤)",
    "components": [
      { "char": "衣", "role": "옷 의 (부수)", "desc": "옷이나 옷감을 뜻합니다." },
      { "char": "里", "role": "마을 리 (요소)", "desc": "옷의 안감(안쪽)이라는 뜻과 발음 '리/리'를 줍니다." }
    ],
    "story": "옷(衣)의 안쪽에 대는 옷감(里)이라는 데서, 사물의 안쪽이나 '속(이면)', 겉과 반대되는 '뒤(뒷면)'를 의미합니다.",
    "example_words": [
      { "word": "裏", "reading": "うら", "meaning": "뒤, 뒷면, 겉과 다름", "description": "사물의 보이지 않는 안쪽이나 겉면의 반대쪽입니다." },
      { "word": "裏口", "reading": "うらぐち", "meaning": "뒷문", "description": "집의 뒤쪽(裏)이나 안쪽으로 통하는 문(口)입니다." }
    ]
  },
  {
    "kanji": "補",
    "reading_on": "ホ",
    "reading_kun": "おぎな(う)",
    "meaning": "기울 (도울)",
    "components": [
      { "char": "衤", "role": "옷의변 (부수)", "desc": "옷이나 천을 뜻합니다." },
      { "char": "甫", "role": "클 보 (요소)", "desc": "크게 만들거나 더한다는 뜻과 발음 '보/호'를 줍니다." }
    ],
    "story": "해진 옷(衤)에 새 천 조각(甫)을 덧대어 꿰매어 '기우다(수선하다)' 혹은 모자란 것을 더하여 '도와주다(보충하다)'는 의미입니다.",
    "example_words": [
      { "word": "補う", "reading": "おぎなう", "meaning": "보충하다, 깁다", "description": "부족한 것을 채워 넣거나 모자란 부분을 더해 주는 것입니다." },
      { "word": "補充", "reading": "ほじゅう", "meaning": "보충", "description": "모자라는 것을 채워서(充) 도와주는(補) 일입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade6.json'
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

print("Grade 6 Part 5 data appended successfully.")
