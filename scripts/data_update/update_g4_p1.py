import json
import os

new_data = [
  {
    "kanji": "愛",
    "reading_on": "アイ",
    "reading_kun": "いと(しい)",
    "meaning": "사랑",
    "components": [
      { "char": "爫", "role": "손톱 조 (요소)", "desc": "손으로 무언가를 부드럽게 감싸는 모습을 나타냅니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 감정을 뜻합니다." },
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "천천히 걷거나 머무는 모습, 혹은 두 발을 모으고 돌아보는 모습입니다." }
    ],
    "story": "사랑하는 사람이나 물건을 손(爫)으로 부드럽게 감싸고, 마음(心)이 쓰여 자꾸만 걸음(夂)을 멈추고 돌아보며 아끼는 '사랑'을 뜻합니다.",
    "example_words": [
      { "word": "愛", "reading": "あい", "meaning": "사랑", "description": "아끼고 위하는 따뜻한 마음입니다." },
      { "word": "愛情", "reading": "あいじょう", "meaning": "애정", "description": "사랑하는(愛) 마음(情)입니다." }
    ]
  },
  {
    "kanji": "案",
    "reading_on": "アン",
    "reading_kun": "",
    "meaning": "책상 (생각할 / 안건)",
    "components": [
      { "char": "安", "role": "편안할 안 (요소)", "desc": "편안하다는 뜻과 발음 '안'을 담당합니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무로 만든 물건을 뜻합니다." }
    ],
    "story": "사람이 편안하게(安) 앉아 글을 쓰거나 생각을 가다듬기 위해 나무(木)로 만든 '책상'을 뜻하며, 책상 위에서 여러 가지 '안건'이나 생각을 짜낸다는 뜻을 가집니다.",
    "example_words": [
      { "word": "案内", "reading": "あんない", "meaning": "안내", "description": "어떤 곳의 사정(内)을 알고 편안하게 이끌어(案) 주는 일입니다." },
      { "word": "名案", "reading": "めいあん", "meaning": "명안", "description": "아주 훌륭한(名) 생각이나 안건(案)입니다." }
    ]
  },
  {
    "kanji": "以",
    "reading_on": "イ",
    "reading_kun": "もっ(て)",
    "meaning": "써 (까닭 / 시작)",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "원래 쟁기(농기구)를 손으로 쥔 모습이 변형된 것입니다." }
    ],
    "story": "농기구를 손에 쥐고 밭을 간다는 데서, 어떤 도구를 '써서(사용하여)' 무언가를 한다는 뜻이 되었으며, 나중에는 기준이나 한계를 나타내는 말로도 쓰이게 되었습니다.",
    "example_words": [
      { "word": "以上", "reading": "いじょう", "meaning": "이상", "description": "어떤 기준을 포함하여(以) 그보다 위(上)인 것입니다." },
      { "word": "以下", "reading": "いか", "meaning": "이하", "description": "어떤 기준을 포함하여(以) 그보다 아래(下)인 것입니다." }
    ]
  },
  {
    "kanji": "衣",
    "reading_on": "イ",
    "reading_kun": "ころも",
    "meaning": "옷",
    "components": [
      { "char": "衣", "role": "옷 의 (부수)", "desc": "윗옷의 깃과 양 소매가 늘어진 모양을 본뜬 상형문자입니다." }
    ],
    "story": "사람이 몸에 걸쳐 입는 상의의 모양에서 '옷'이나 '의복'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "衣服", "reading": "いふく", "meaning": "의복", "description": "몸에 입는 옷(衣)과 복장(服)입니다." },
      { "word": "衣", "reading": "ころも", "meaning": "옷, 튀김옷", "description": "겉에 둘러입는 옷이나 튀김의 겉 반죽입니다." }
    ]
  },
  {
    "kanji": "位",
    "reading_on": "イ",
    "reading_kun": "くらい",
    "meaning": "자리 (지위)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "立", "role": "설 립 (요소)", "desc": "사람이 똑바로 선다는 뜻입니다." }
    ],
    "story": "조정에서 사람(亻)들이 직급에 따라 나란히 서(立) 있는 '자리'나 '지위', 혹은 '위치'를 뜻합니다.",
    "example_words": [
      { "word": "位置", "reading": "いち", "meaning": "위치", "description": "어떤 자리에(位) 놓여(置) 있는 곳입니다." },
      { "word": "地位", "reading": "ちい", "meaning": "지위", "description": "사회적인 바탕(地)이 되는 자리(位)나 신분입니다." }
    ]
  },
  {
    "kanji": "囲",
    "reading_on": "イ",
    "reading_kun": "かこ(む)、かこ(う)",
    "meaning": "에워쌀",
    "components": [
      { "char": "囗", "role": "큰입구 몸 (부수)", "desc": "사방을 둘러싼 울타리나 성벽을 뜻합니다." },
      { "char": "井", "role": "우물 정 (요소)", "desc": "우물이나 마을의 중심이라는 뜻과 발음 '위/이'를 담당합니다." }
    ],
    "story": "마을의 중심인 우물(井) 주변으로 둥글게 울타리나 담장(囗)을 쳐서 빙 '에워싸다(둘러싸다)'는 뜻입니다.",
    "example_words": [
      { "word": "囲む", "reading": "かこむ", "meaning": "둘러싸다", "description": "어떤 것의 둘레를 빙 에워싸는 것입니다." },
      { "word": "周囲", "reading": "しゅうい", "meaning": "주위", "description": "어떤 것의 바깥 둘레(周)나 에워싼(囲) 근처입니다." }
    ]
  },
  {
    "kanji": "胃",
    "reading_on": "イ",
    "reading_kun": "",
    "meaning": "위장 (위)",
    "components": [
      { "char": "田", "role": "밭 전 (요소)", "desc": "원래 밭이 아니라 음식물이 들어찬 동그란 밥통 모양에서 유래했습니다." },
      { "char": "月", "role": "육달월 (부수)", "desc": "사람의 신체나 고기를 뜻합니다." }
    ],
    "story": "몸(月) 속에서 우리가 먹은 음식물을 담아두고 소화시키는 동그란 주머니(田의 원래 형태), 즉 '위(위장)'를 뜻합니다.",
    "example_words": [
      { "word": "胃", "reading": "い", "meaning": "위, 위장", "description": "음식물을 소화하는 신체 기관입니다." },
      { "word": "胃腸", "reading": "いちょう", "meaning": "위장", "description": "위(胃)와 창자(腸)를 아울러 이르는 말입니다." }
    ]
  },
  {
    "kanji": "印",
    "reading_on": "イン",
    "reading_kun": "しるし",
    "meaning": "도장 (찍을)",
    "components": [
      { "char": "爪", "role": "손톱 조 (요소)", "desc": "위에서 아래로 누르는 손의 모양입니다." },
      { "char": "卩", "role": "병부 절 (부수)", "desc": "사람이 무릎을 꿇고 있는 모양입니다." }
    ],
    "story": "윗사람이 손(爪)으로 무릎 꿇은 사람(卩)을 내리눌러 굴복시키듯, 도장을 꾹 내리눌러 '찍다' 혹은 그 흔적인 '도장', '표시'를 뜻합니다.",
    "example_words": [
      { "word": "印刷", "reading": "いんさつ", "meaning": "인쇄", "description": "글자나 그림의 틀을 도장처럼 찍어내어(印) 종이에 박아내는(刷) 것입니다." },
      { "word": "目印", "reading": "めじるし", "meaning": "표시, 안표", "description": "눈(目)에 잘 띄게 해놓은 표시나 도장(印)입니다." }
    ]
  },
  {
    "kanji": "英",
    "reading_on": "エイ",
    "reading_kun": "",
    "meaning": "꽃부리 (뛰어날)",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 풀, 꽃을 뜻합니다." },
      { "char": "央", "role": "가운데 앙 (요소)", "desc": "가운데나 한가운데를 뜻하며 발음 '영/에이'를 줍니다." }
    ],
    "story": "식물(艹)의 가장 가운데(央)에 화려하게 피어난 아름다운 꽃송이(꽃부리)를 뜻하며, 꽃처럼 화려하고 다른 것보다 '뛰어나다'는 뜻으로 쓰입니다.",
    "example_words": [
      { "word": "英語", "reading": "えいご", "meaning": "영어", "description": "영국(英) 사람들의 언어(語)입니다." },
      { "word": "英雄", "reading": "えいゆう", "meaning": "영웅", "description": "지혜와 재능이 뛰어나고(英) 굳센(雄) 사람입니다." }
    ]
  },
  {
    "kanji": "栄",
    "reading_on": "エイ",
    "reading_kun": "さか(える)、は(える)",
    "meaning": "영화로울",
    "components": [
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "나무 가지가 무성하게 덮인 모양의 변형입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." }
    ],
    "story": "나무(木)에 꽃(冖, 원래 𤇾 형태)이 무성하고 아름답게 활짝 피어난 모습에서, 널리 번창하고 '영화롭다(영광스럽다)'는 뜻입니다.",
    "example_words": [
      { "word": "栄養", "reading": "えいよう", "meaning": "영양", "description": "몸을 영화롭게(栄) 하고 기르는(養) 성분입니다." },
      { "word": "栄える", "reading": "さかえる", "meaning": "번영하다, 번창하다", "description": "가문이나 사업이 성하고 융성하게 되는 것입니다." }
    ]
  },
  {
    "kanji": "塩",
    "reading_on": "エン",
    "reading_kun": "しお",
    "meaning": "소금",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "소금을 굽는 진흙 화로나 땅을 뜻합니다." },
      { "char": "𠂉", "role": "사람 인 (요소)", "desc": "사람의 동작을 나타냅니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "소금을 담는 그릇입니다." },
      { "char": "皿", "role": "그릇 명 (요소)", "desc": "바닷물을 끓여 소금을 담는 접시를 나타냅니다." }
    ],
    "story": "바닷물을 진흙 화로(土) 위에 올려놓은 그릇(皿)에 담고, 사람(𠂉)이 정성껏 끓여서 얻어낸 하얀 '소금'을 뜻합니다.",
    "example_words": [
      { "word": "塩", "reading": "しお", "meaning": "소금", "description": "짠맛을 내는 조미료입니다." },
      { "word": "食塩", "reading": "しょくえん", "meaning": "식염", "description": "먹는(食) 데 쓰는 소금(塩)입니다." }
    ]
  },
  {
    "kanji": "央",
    "reading_on": "オウ",
    "reading_kun": "",
    "meaning": "가운데",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "사람이 양팔과 다리를 크게 벌리고 선 모양입니다." },
      { "char": "冂", "role": "멀 경 (요소)", "desc": "사람의 목에 씌운 칼(형구)의 모양을 본뜬 것입니다." }
    ],
    "story": "죄인의 목 한가운데에 칼(冂)을 씌워 크게(大) 벌을 준다는 모습에서, 목의 한가운데, 나아가 사물의 '가운데(중앙)'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "中央", "reading": "ちゅうおう", "meaning": "중앙", "description": "어떤 것의 속(中)이자 정가운데(央)입니다." }
    ]
  },
  {
    "kanji": "億",
    "reading_on": "オク",
    "reading_kun": "",
    "meaning": "억",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "意", "role": "뜻 의 (요소)", "desc": "마음이나 생각, 헤아림을 뜻하며 발음 '의/오쿠'를 줍니다." }
    ],
    "story": "사람(亻)이 마음속(意)으로 깊이 헤아릴 수 없을 만큼 아주 큰 숫자인 만(萬)의 만 배, 즉 '억'을 의미합니다.",
    "example_words": [
      { "word": "一億", "reading": "いちおく", "meaning": "일억", "description": "천만의 열 배가 되는 큰 숫자입니다." },
      { "word": "億万長者", "reading": "おくまんちょうじゃ", "meaning": "억만장자", "description": "억(億), 만(万) 단위의 큰돈을 가진 부자(長者)입니다." }
    ]
  },
  {
    "kanji": "加",
    "reading_on": "カ",
    "reading_kun": "くわ(える)、くわ(わる)",
    "meaning": "더할",
    "components": [
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 의미합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입이나 말을 의미합니다." }
    ],
    "story": "입(口)으로 격려의 말을 더해주어 상대방의 힘(力)을 북돋워 '더해주다' 혹은 수량을 '늘리다'는 뜻입니다.",
    "example_words": [
      { "word": "加える", "reading": "くわえる", "meaning": "더하다, 보태다", "description": "원래 있던 것에 다른 것을 보태어 많게 하는 것입니다." },
      { "word": "参加", "reading": "さんか", "meaning": "참가", "description": "어떤 모임에 끼어들어(参) 뜻을 더하는(加) 일입니다." }
    ]
  },
  {
    "kanji": "果",
    "reading_on": "カ",
    "reading_kun": "は(たす)、は(てる)、は(て)",
    "meaning": "열매",
    "components": [
      { "char": "田", "role": "밭 전 (요소)", "desc": "여기서는 나무에 둥글게 열린 열매 모양을 본뜬 것입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." }
    ],
    "story": "나무(木) 위에 둥근 열매(田)가 주렁주렁 열려 있는 모양에서 '열매'나 일의 결과인 '성과'를 뜻합니다.",
    "example_words": [
      { "word": "果物", "reading": "くだもの", "meaning": "과일", "description": "나무의 열매(果)인 식물(物)입니다." },
      { "word": "結果", "reading": "けっか", "meaning": "결과", "description": "원인에 의하여 맺어진(結) 열매(果), 즉 결말입니다." }
    ]
  },
  {
    "kanji": "貨",
    "reading_on": "カ",
    "reading_kun": "",
    "meaning": "재물 (화물)",
    "components": [
      { "char": "化", "role": "될 화 (요소)", "desc": "모양이 바뀌다, 교환하다는 뜻과 발음 '화/카'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "옛날 돈으로 쓰이던 조개 껍데기, 즉 재물을 뜻합니다." }
    ],
    "story": "돈(貝)을 지불하고 다른 물건으로 모양을 바꾸거나(化) 교환하여 얻은 '재물'이나 '화물(물건)'을 뜻합니다.",
    "example_words": [
      { "word": "貨物", "reading": "かもつ", "meaning": "화물", "description": "배나 기차로 실어 나르는 물건(貨物)입니다." },
      { "word": "硬貨", "reading": "こうか", "meaning": "동전, 경화", "description": "금속으로 단단하게(硬) 만든 돈(貨)입니다." }
    ]
  },
  {
    "kanji": "課",
    "reading_on": "カ",
    "reading_kun": "",
    "meaning": "과정 (부서)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 시험, 조사하는 것을 뜻합니다." },
      { "char": "果", "role": "열매 과 (요소)", "desc": "결과, 끝을 맺는다는 뜻과 발음 '과/카'를 줍니다." }
    ],
    "story": "말(言)로 일의 성과(果)나 성적을 매겨서 부과하는 할당량, 혹은 그런 일을 처리하는 '부서(과)'나 공부의 '과정'을 뜻합니다.",
    "example_words": [
      { "word": "課題", "reading": "かだい", "meaning": "과제", "description": "부여받은(課) 문제나 제목(題)입니다." },
      { "word": "放課後", "reading": "ほうかご", "meaning": "방과 후", "description": "학교의 수업 과정(課)을 마쳐 놓아진(放) 뒤(後)입니다." }
    ]
  },
  {
    "kanji": "芽",
    "reading_on": "ガ",
    "reading_kun": "め",
    "meaning": "싹",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 풀을 의미합니다." },
      { "char": "牙", "role": "어금니 아 (요소)", "desc": "동물의 날카로운 어금니 모양으로 발음 '아/가'를 줍니다." }
    ],
    "story": "풀(艹)이나 식물이 새로 자라날 때 동물의 어금니(牙)처럼 뾰족하게 땅을 뚫고 나오는 어린 '싹'을 뜻합니다.",
    "example_words": [
      { "word": "芽", "reading": "め", "meaning": "싹", "description": "식물의 씨앗이나 줄기에서 처음 돋아나는 어린잎입니다." },
      { "word": "発芽", "reading": "はつが", "meaning": "발아", "description": "식물의 싹(芽)이 트는(発) 것입니다." }
    ]
  },
  {
    "kanji": "改",
    "reading_on": "カイ",
    "reading_kun": "あらた(める)、あらた(まる)",
    "meaning": "고칠",
    "components": [
      { "char": "己", "role": "몸 기 (요소)", "desc": "자기 자신을 뜻합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손으로 치거나 매질을 하는 등 강제적인 동작입니다." }
    ],
    "story": "잘못을 한 자기 자신(己)을 회초리로 치듯(攵) 반성하고 꾸짖어 바르게 '고치다'라는 뜻입니다.",
    "example_words": [
      { "word": "改める", "reading": "あらためる", "meaning": "고치다, 변경하다", "description": "잘못된 점이나 낡은 것을 새롭게 바꾸는 것입니다." },
      { "word": "改正", "reading": "かいせい", "meaning": "개정", "description": "잘못된 것을 고쳐서(改) 바르게(正) 하는 것입니다." }
    ]
  },
  {
    "kanji": "械",
    "reading_on": "カイ",
    "reading_kun": "",
    "meaning": "기계",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻하며 옛날 도구나 기구를 나타냅니다." },
      { "char": "戒", "role": "경계할 계 (요소)", "desc": "창을 들고 경계한다는 뜻과 발음 '계/카이'를 담당합니다." }
    ],
    "story": "옛날에 나무(木)로 만든 경계용(戒) 도구나 형틀에서 유래하여, 일정한 동작을 수행하는 정교한 도구인 '기계'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "機械", "reading": "きかい", "meaning": "기계", "description": "동력을 받아 움직이며 일을 하는 장치(機, 械)입니다." }
    ]
  },
  {
    "kanji": "害",
    "reading_on": "ガイ",
    "reading_kun": "",
    "meaning": "해칠",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 건물을 뜻합니다." },
      { "char": "丰", "role": "예쁠 봉 (요소)", "desc": "여기서는 어지럽게 널려 있거나 찌른다는 뜻의 상형에서 왔습니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입이나 방해를 뜻합니다." }
    ],
    "story": "집안(宀)에서 말다툼(口)이나 칼부림(丰의 변형)이 일어나 서로 다치거나 피해를 주어 '해치다'는 뜻입니다.",
    "example_words": [
      { "word": "被害", "reading": "ひがい", "meaning": "피해", "description": "생명이나 재산에 해(害)를 입는(被) 일입니다." },
      { "word": "公害", "reading": "こうがい", "meaning": "공해", "description": "산업 활동 등으로 대중(公)에게 돌아가는 해(害)입니다." }
    ]
  },
  {
    "kanji": "街",
    "reading_on": "ガイ、カイ",
    "reading_kun": "まち",
    "meaning": "거리",
    "components": [
      { "char": "行", "role": "다닐 행 (부수)", "desc": "사람들이 다니는 넓은 사거리나 길을 뜻합니다." },
      { "char": "圭", "role": "홀 규 (요소)", "desc": "반듯하게 깎은 옥의 모양이나 흙이 쌓여 반듯한 모양으로 발음 '규/가이'를 줍니다." }
    ],
    "story": "사람들이 다니는 사거리(行) 옆으로 반듯하고(圭) 번화하게 건물들이 늘어선 상점가나 큰 '거리(시가지)'를 뜻합니다.",
    "example_words": [
      { "word": "街", "reading": "まち", "meaning": "거리, 번화가", "description": "상점이나 집들이 많이 모여 있는 시내입니다." },
      { "word": "商店街", "reading": "しょうてんがい", "meaning": "상점가", "description": "상점(商店)들이 줄지어 있는 거리(街)입니다." }
    ]
  },
  {
    "kanji": "各",
    "reading_on": "カク",
    "reading_kun": "おのおの",
    "meaning": "각각",
    "components": [
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "발이 아래로 향한 모양, 즉 발걸음을 뜻합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "마을이나 목적지를 나타냅니다." }
    ],
    "story": "사람의 발(夂)이 저마다의 목적지나 마을(口)에 도착하는 모양에서, 따로따로 무언가를 한다는 뜻인 '각각'이나 '저마다'를 뜻합니다.",
    "example_words": [
      { "word": "各自", "reading": "かくじ", "meaning": "각자", "description": "각각(各)의 자기 자신(自)입니다." },
      { "word": "各地", "reading": "かくち", "meaning": "각지", "description": "각각(各)의 여러 지방이나 땅(地)입니다." }
    ]
  },
  {
    "kanji": "覚",
    "reading_on": "カク",
    "reading_kun": "おぼ(える)、さ(ます)、さ(める)",
    "meaning": "깨달을 (기억할)",
    "components": [
      { "char": "⺍", "role": "불똥 주 (요소)", "desc": "배울 학(學)의 머리 부분(양손)의 생략형으로, 배움이나 지식을 뜻합니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "집이나 덮개를 뜻합니다." },
      { "char": "見", "role": "볼 견 (부수)", "desc": "눈으로 똑똑히 본다는 뜻입니다." }
    ],
    "story": "가르침(⺍)을 받아 눈(見)을 번쩍 뜨고 어두움을 벗어나 무언가를 '깨닫다', 혹은 머릿속에 똑똑히 '기억하다'는 뜻입니다.",
    "example_words": [
      { "word": "覚える", "reading": "おぼえる", "meaning": "기억하다, 외우다", "description": "어떤 사실을 머릿속에 간직하는 것입니다." },
      { "word": "感覚", "reading": "かんかく", "meaning": "감각", "description": "눈, 코, 귀 등으로 자극을 느끼고(感) 깨닫는(覚) 것입니다." }
    ]
  },
  {
    "kanji": "完",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "완전할",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 건물을 뜻합니다." },
      { "char": "元", "role": "으뜸 원 (요소)", "desc": "사람의 머리나 시작점, 바탕을 뜻하며 발음 '원/칸'을 줍니다." }
    ],
    "story": "집(宀)을 짓기 위해 바탕(元)부터 튼튼하게 끝까지 마무리하여 흠집 없이 '완전하다' 혹은 '마치다'는 뜻입니다.",
    "example_words": [
      { "word": "完成", "reading": "かんせい", "meaning": "완성", "description": "건물이나 물건을 완전하게(完) 다 이루는(成) 것입니다." },
      { "word": "完全", "reading": "かんぜん", "meaning": "완전", "description": "모자람 없이 흠집이 없고(全) 완벽한(完) 상태입니다." }
    ]
  },
  {
    "kanji": "官",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "벼슬 (관청)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "건물이나 집을 뜻합니다." },
      { "char": "㠯", "role": "써 이 (요소)", "desc": "사람이 엎드린 모양이거나 관리들이 모인 모양을 나타냅니다." }
    ],
    "story": "임금의 건물(宀) 아래에 모여서 나랏일을 맡아보는 관리들의 모습에서 '벼슬'이나 '관청'을 의미합니다.",
    "example_words": [
      { "word": "警官", "reading": "けいかん", "meaning": "경찰관", "description": "치안을 경계하는(警) 관리(官)입니다." },
      { "word": "器官", "reading": "きかん", "meaning": "기관", "description": "생물의 몸에서 특정한 역할을 맡은(官) 부분(器)입니다." }
    ]
  },
  {
    "kanji": "管",
    "reading_on": "カン",
    "reading_kun": "くだ",
    "meaning": "대롱 (관리할)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 뜻합니다." },
      { "char": "官", "role": "벼슬 관 (요소)", "desc": "관청이나 공적인 일이라는 뜻과 발음 '관'을 담당합니다." }
    ],
    "story": "대나무(竹)의 속을 파내어 속이 텅 빈 원통형의 파이프, 즉 '대롱(관)'을 뜻하며, 나중에 나랏일(官)의 열쇠를 보관하는 대나무 통에서 파생되어 사물을 통제하고 '관리하다'는 뜻이 생겼습니다.",
    "example_words": [
      { "word": "管理", "reading": "かんり", "meaning": "관리", "description": "조직이나 물건을 통제하고(管) 다스리는(理) 일입니다." },
      { "word": "血管", "reading": "けっかん", "meaning": "혈관", "description": "피(血)가 흐르는 통로인 관(管)입니다." }
    ]
  },
  {
    "kanji": "関",
    "reading_on": "カン",
    "reading_kun": "せき、かか(わる)",
    "meaning": "빗장 (관계할)",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "대문을 뜻합니다." },
      { "char": "关", "role": "웃음 왈 (요소)", "desc": "문짝을 실로 연결한 모습의 간략화된 형태로, 연결하다는 뜻과 발음 '관'을 줍니다." }
    ],
    "story": "대문(門)을 닫아걸고 끈(关의 본래 뜻)으로 단단히 묶는 가로막대, 즉 '빗장(관문)'을 뜻하며, 문고리처럼 서로 이어져 '관계하다(관여하다)'는 뜻으로 쓰입니다.",
    "example_words": [
      { "word": "関係", "reading": "かんけい", "meaning": "관계", "description": "둘 이상의 사람이나 사물이 서로 걸려(係) 맺어지는(関) 것입니다." },
      { "word": "玄関", "reading": "げんかん", "meaning": "현관", "description": "집이나 건물의 출입구이자 관문(関)입니다." }
    ]
  },
  {
    "kanji": "観",
    "reading_on": "カン",
    "reading_kun": "み(る)",
    "meaning": "볼",
    "components": [
      { "char": "雚", "role": "황새 관 (요소)", "desc": "황새처럼 눈을 부릅뜨고 자세히 본다는 뜻과 발음 '관'을 줍니다. (현대자형에서는 艹+口+隹 등으로 간략화)" },
      { "char": "見", "role": "볼 견 (부수)", "desc": "눈으로 본다는 뜻입니다." }
    ],
    "story": "황새(雚)가 먹이를 찾을 때 눈을 크게 뜨고 살피듯, 대상의 모습이나 풍경을 유심히 자세히 살펴 '보다(관찰하다)'는 의미입니다.",
    "example_words": [
      { "word": "観光", "reading": "かんこう", "meaning": "관광", "description": "다른 지방의 풍경이나 빛나는(光) 것들을 구경하는(観) 일입니다." },
      { "word": "観察", "reading": "かんさつ", "meaning": "관찰", "description": "사물의 상태나 현상을 주의 깊게 살펴보고(観) 살피는(察) 것입니다." }
    ]
  },
  {
    "kanji": "願",
    "reading_on": "ガン",
    "reading_kun": "ねが(う)",
    "meaning": "원할",
    "components": [
      { "char": "原", "role": "근원 원 (요소)", "desc": "근본이나 평평한 들판을 뜻하며, 발음 '원/간'을 나타냅니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "사람의 머리나 얼굴을 의미합니다." }
    ],
    "story": "사람의 머리(頁) 속에 있는 가장 근본적(原)이고 간절한 생각이나 바람, 즉 어떤 일이 이루어지기를 '원하다' 혹은 '바라다'는 뜻입니다.",
    "example_words": [
      { "word": "願う", "reading": "ねがう", "meaning": "바라다, 원하다", "description": "어떤 일이 이루어지기를 간절히 희망하는 것입니다." },
      { "word": "お願い", "reading": "おねがい", "meaning": "부탁", "description": "상대방에게 무언가를 해달라고 청하고 바라는(願) 말입니다." }
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

print("Grade 4 Part 1 data appended successfully.")
