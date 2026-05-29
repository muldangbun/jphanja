import json
import os

new_data = [
  {
    "kanji": "河",
    "reading_on": "カ",
    "reading_kun": "かわ",
    "meaning": "물 (강)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "可", "role": "옳을 가 (요소)", "desc": "물길이 구부러져 이어진다는 뜻과 발음 '가/카'를 줍니다." }
    ],
    "story": "물이 이리저리 굽이쳐(可) 길게 흘러가는 큰 물줄기인 '강'이나 '하천'을 뜻합니다.",
    "example_words": [
      { "word": "河川", "reading": "かせん", "meaning": "하천", "description": "큰 강(河)과 작은 내(川)를 아울러 이르는 말입니다." },
      { "word": "運河", "reading": "うんが", "meaning": "운하", "description": "배로 물건을 나르기(運) 위해 사람이 파서 만든 강(河)입니다." }
    ]
  },
  {
    "kanji": "液",
    "reading_on": "エキ",
    "reading_kun": "",
    "meaning": "진액 (액체)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "夜", "role": "밤 야 (요소)", "desc": "밤에는 이슬이 맺힌다는 뜻에서 즙이나 진액의 의미와 발음 '액/에키'를 담당합니다." }
    ],
    "story": "밤(夜)에 나뭇잎에 맺히는 이슬이나 수액처럼 식물이나 물건에서 짜낸 '진액'이나 '액체'를 뜻합니다.",
    "example_words": [
      { "word": "液体", "reading": "えきたい", "meaning": "액체", "description": "물이나 기름처럼 모양이 없고 흐르는 성질을 가진 물질(体)입니다." },
      { "word": "血液", "reading": "けつえき", "meaning": "혈액", "description": "동물의 몸속을 흐르는 피(血) 성분의 액체(液)입니다." }
    ]
  },
  {
    "kanji": "混",
    "reading_on": "コン",
    "reading_kun": "ま(じる)、ま(ざる)、ま(ぜる)",
    "meaning": "섞을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "昆", "role": "맏 곤 (요소)", "desc": "사람들이 모여 무리 지어 있다는 뜻과 발음 '곤/콘'을 줍니다." }
    ],
    "story": "물이 여러 곳에서 흘러나와 한곳에 무리(昆) 지어 모이듯 여러 가지가 한데 '섞이다' 혹은 '혼잡하다'는 의미입니다.",
    "example_words": [
      { "word": "混ざる", "reading": "まざる", "meaning": "섞이다", "description": "여러 가지가 하나로 합쳐져 구별하기 어려워지는 것입니다." },
      { "word": "混乱", "reading": "こんらん", "meaning": "혼란", "description": "여러 가지가 뒤섞여(混) 어지러운(乱) 상태입니다." }
    ]
  },
  {
    "kanji": "減",
    "reading_on": "ゲン",
    "reading_kun": "へ(る)、へ(らす)",
    "meaning": "덜 (줄어들)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "咸", "role": "다 함 (요소)", "desc": "창(戌)으로 입(口)을 막아 입을 다물게 한다는 데서 모두라는 뜻과 발음 '감/겐'을 줍니다." }
    ],
    "story": "강물(氵)이 모두(咸) 말라 없어져서 양이 '줄어들다' 혹은 '덜다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "減る", "reading": "へる", "meaning": "줄다, 감소하다", "description": "수나 양이 적어지는 것입니다." },
      { "word": "減少", "reading": "げんしょう", "meaning": "감소", "description": "양이나 수가 줄어서(減) 적어지는(少) 것입니다." }
    ]
  },
  {
    "kanji": "測",
    "reading_on": "ソク",
    "reading_kun": "はか(る)",
    "meaning": "잴 (측정할)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "則", "role": "법칙 칙 (요소)", "desc": "기준이나 법칙을 뜻하며 발음 '측/소쿠'를 담당합니다." }
    ],
    "story": "물의 깊이를 일정한 기준(則)을 가진 자로 재어 '헤아리다' 혹은 '측정하다'는 뜻입니다.",
    "example_words": [
      { "word": "測る", "reading": "はかる", "meaning": "재다, 측량하다", "description": "기구를 사용하여 길이나 깊이, 면적 따위를 재는 것입니다." },
      { "word": "測定", "reading": "そくてい", "meaning": "측정", "description": "재어서(測) 수치나 분량을 정하는(定) 일입니다." }
    ]
  },
  {
    "kanji": "準",
    "reading_on": "ジュン",
    "reading_kun": "",
    "meaning": "준할 (기준)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물을 뜻합니다." },
      { "char": "隼", "role": "새 매 준 (요소)", "desc": "물수리가 물 위를 날아 목표물을 정확히 겨냥한다는 데서 평평함, 기준을 뜻하며 발음 '준/쥰'을 줍니다." }
    ],
    "story": "목수가 수평을 맞추기 위해 물(氵) 위에 띄워 기준을 잡는 도구처럼 평평하고 바른 '기준'이나, 그 기준에 '준하다(맞추다)'는 뜻입니다.",
    "example_words": [
      { "word": "準備", "reading": "じゅんび", "meaning": "준비", "description": "미리 기준에 맞추어(準) 필요한 것을 갖추는(備) 일입니다." },
      { "word": "基準", "reading": "きじゅん", "meaning": "기준", "description": "기본(基)이 되는 준칙(準)이나 표준입니다." }
    ]
  },
  {
    "kanji": "演",
    "reading_on": "エン",
    "reading_kun": "",
    "meaning": "펼 (연기할)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "寅", "role": "범 인 (요소)", "desc": "화살을 똑바로 펴는 모양에서 길게 뻗어 나간다는 뜻과 발음 '인/엔'을 담당합니다." }
    ],
    "story": "물(氵)이 굽이치며 길게 멀리 흘러가듯(寅), 무대 위에서 이야기나 몸짓을 길게 '펼치다' 혹은 '연기하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "演技", "reading": "えんぎ", "meaning": "연기", "description": "배우가 배역의 인물로 분장하여 무대에서 재주(技)를 펼치는(演) 것입니다." },
      { "word": "演説", "reading": "えんぜつ", "meaning": "연설", "description": "많은 사람 앞에서 자신의 생각이나 주장을 말(説)로 펼쳐(演) 보이는 일입니다." }
    ]
  },
  {
    "kanji": "潔",
    "reading_on": "ケツ",
    "reading_kun": "いさぎよ(い)",
    "meaning": "깨끗할",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 씻음을 뜻합니다." },
      { "char": "絜", "role": "헤아릴 혈 (요소)", "desc": "실(糸)을 칼(刀)로 끊어 고르게 한다는 데서 반듯하고 깨끗하다는 뜻과 발음 '결/케츠'를 줍니다." }
    ],
    "story": "물(氵)로 깨끗하게 씻어 때나 흠이 없고 말끔히 다듬어(絜) '깨끗하다' 혹은 행동이나 마음씨가 맑고 바르다는 뜻입니다.",
    "example_words": [
      { "word": "潔い", "reading": "いさぎよい", "meaning": "깨끗하다, 떳떳하다", "description": "미련이 없고 태도나 마음이 산뜻하며 떳떳한 모양입니다." },
      { "word": "清潔", "reading": "せいけつ", "meaning": "청결", "description": "더럽지 않고 맑으며(清) 깨끗한(潔) 상태입니다." }
    ]
  },
  {
    "kanji": "災",
    "reading_on": "サイ",
    "reading_kun": "わざわ(い)",
    "meaning": "재앙",
    "components": [
      { "char": "巛", "role": "개미허리 (요소)", "desc": "원래 강물이 넘쳐 흐르는 모양인 내 천(川)의 변형입니다." },
      { "char": "火", "role": "불 화 (부수)", "desc": "불이나 화재를 뜻합니다." }
    ],
    "story": "홍수로 물이 넘치거나(巛) 불(火)이 나서 집이나 재산을 잃게 되는 큰 '재앙'이나 '재난'을 의미합니다.",
    "example_words": [
      { "word": "災い", "reading": "わざわい", "meaning": "재앙, 화", "description": "뜻하지 않게 생긴 불행이나 재난입니다." },
      { "word": "火災", "reading": "かさい", "meaning": "화재", "description": "불(火)이 나서 일어나는 재앙(災)입니다." }
    ]
  },
  {
    "kanji": "燃",
    "reading_on": "ネン",
    "reading_kun": "も(える)、も(やす)、も(す)",
    "meaning": "탈",
    "components": [
      { "char": "火", "role": "불 화 (부수)", "desc": "불을 의미합니다." },
      { "char": "然", "role": "그럴 연 (요소)", "desc": "개(犬) 고기(月)를 불(灬)에 굽는다는 본래 뜻이 있어 '타다'는 의미와 발음 '연/넨'을 줍니다." }
    ],
    "story": "원래 然 자가 불에 고기를 굽는다는 뜻이었으나, 나중에 '그렇다'는 뜻으로 쓰이게 되자 다시 불(火)을 붙여 불이 활활 '타다'나 '태우다'는 뜻을 명확히 한 글자입니다.",
    "example_words": [
      { "word": "燃える", "reading": "もえる", "meaning": "타だ, 불타다", "description": "불이 붙어 타오르거나 정열이 솟아나는 것입니다." },
      { "word": "燃料", "reading": "ねんりょう", "meaning": "연료", "description": "불을 태우는(燃) 데 쓰는 재료(料)입니다." }
    ]
  },
  {
    "kanji": "版",
    "reading_on": "ハン",
    "reading_kun": "",
    "meaning": "판목 (출판할)",
    "components": [
      { "char": "片", "role": "조각 편 (부수)", "desc": "나무를 쪼갠 납작한 나뭇조각을 뜻합니다." },
      { "char": "反", "role": "돌이킬 반 (요소)", "desc": "뒤집는다는 뜻에서 종이를 뒤집어 찍어낸다는 의미와 발음 '반/한'을 줍니다." }
    ],
    "story": "납작한 나뭇조각(片)에 글씨를 거꾸로 새긴 다음 종이를 뒤집어(反) 덮어 책을 인쇄하는 '판목(인쇄판)'이나 '출판하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "出版", "reading": "しゅっぱん", "meaning": "출판", "description": "책이나 그림 따위를 인쇄판(版)으로 찍어서 세상에 내놓는(出) 일입니다." },
      { "word": "版画", "reading": "はんが", "meaning": "판화", "description": "나무판 등에 그림을 새겨 잉크를 칠한 뒤 종이에 찍어낸(版) 그림(画)입니다." }
    ]
  },
  {
    "kanji": "犯",
    "reading_on": "ハン",
    "reading_kun": "おか(す)",
    "meaning": "범할 (죄인)",
    "components": [
      { "char": "犭", "role": "개사슴록변 (부수)", "desc": "개나 들짐승을 뜻합니다." },
      { "char": "㔾", "role": "병부 절 (요소)", "desc": "사람이 웅크린 모양이나 구부러짐을 의미하며 발음 '범/한'을 줍니다." }
    ],
    "story": "개가 사람(㔾 변형)에게 사납게 달려들어 물어뜯듯 규칙이나 법을 '어기다(범하다)' 혹은 죄를 지은 '범인'을 뜻합니다.",
    "example_words": [
      { "word": "犯す", "reading": "おかす", "meaning": "범하다, 어기다", "description": "법이나 규칙을 어기거나 죄를 짓는 것입니다." },
      { "word": "犯人", "reading": "はんにん", "meaning": "범인", "description": "죄를 지어 법을 범한(犯) 사람(人)입니다." }
    ]
  },
  {
    "kanji": "状",
    "reading_on": "ジョウ",
    "reading_kun": "",
    "meaning": "문서 (모양)",
    "components": [
      { "char": "丬", "role": "장수 장 (요소)", "desc": "침상이나 널빤지 모양으로 문서나 편지를 뜻하며 발음 '장/조우'를 줍니다." },
      { "char": "犬", "role": "개 견 (부수)", "desc": "개나 짐승을 뜻합니다." }
    ],
    "story": "원래 개의 겉모습을 뜻하여 사물의 생김새나 '모양(형상)'을 의미했으나, 나중에 문서를 뜻하는 丬와 결합하여 편지나 '문서'라는 뜻으로도 널리 쓰이게 되었습니다.",
    "example_words": [
      { "word": "状態", "reading": "じょうたい", "meaning": "상태", "description": "사물이나 현상이 놓여 있는 모양(状)과 태도(態)입니다." },
      { "word": "招待状", "reading": "しょうたいじょう", "meaning": "초대장", "description": "손님을 초대(招待)하기 위해 보내는 편지(状)입니다." }
    ]
  },
  {
    "kanji": "独",
    "reading_on": "ドク",
    "reading_kun": "ひと(り)",
    "meaning": "홀로",
    "components": [
      { "char": "犭", "role": "개사슴록변 (부수)", "desc": "개나 짐승을 의미합니다." },
      { "char": "虫", "role": "벌레 충 (요소)", "desc": "원래 蜀(나비 애벌레 촉)의 약자로, 한 마리만 남는다는 뜻과 발음 '독/도쿠'를 줍니다." }
    ],
    "story": "개(犭)가 무리 지어 다니지 않고 애벌레(虫)처럼 혼자 동떨어져서 외롭게 '홀로(혼자)' 있다는 뜻입니다.",
    "example_words": [
      { "word": "独り", "reading": "ひとり", "meaning": "혼자, 홀로", "description": "다른 사람 없이 한 사람만 있는 상태입니다. (一人과 같은 뜻이나 고독함을 강조합니다)" },
      { "word": "独立", "reading": "どくりつ", "meaning": "독립", "description": "남에게 의지하지 않고 홀로(独) 서는(立) 것입니다." }
    ]
  },
  {
    "kanji": "率",
    "reading_on": "ソツ、リツ",
    "reading_kun": "ひき(いる)",
    "meaning": "거느릴 (비율)",
    "components": [
      { "char": "玄", "role": "검을 현 (부수)", "desc": "검다는 뜻 외에 여기서는 실타래나 그물을 의미합니다." },
      { "char": "十", "role": "열 십 (요소)", "desc": "사방이나 얽혀 있음을 나타냅니다." }
    ],
    "story": "새를 잡는 밧줄(玄) 그물코(십자 모양 무늬)의 모양에서 전체를 통솔하고 '거느리다(이끌다)'는 뜻이 되었으며, 전체에 대한 어떤 양의 크기인 '비율'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "率いる", "reading": "ひきいる", "meaning": "거느리다, 이끌다", "description": "무리를 통솔하여 앞장서서 이끄는 것입니다." },
      { "word": "確率", "reading": "かくりつ", "meaning": "확률", "description": "어떤 일이 일어날 확실성(確)이 있는 비율(率)입니다." }
    ]
  },
  {
    "kanji": "現",
    "reading_on": "ゲン",
    "reading_kun": "あらわ(れる)、あらわ(す)",
    "meaning": "나타날 (현재)",
    "components": [
      { "char": "王", "role": "구슬 옥 (부수)", "desc": "여기서는 玉(구슬 옥) 자의 획이 줄어든 형태로 보석을 뜻합니다." },
      { "char": "見", "role": "볼 견 (요소)", "desc": "눈으로 봄을 의미하며 발음 '견/겐'의 변형 역할을 합니다." }
    ],
    "story": "흙 속에 묻혀 있던 보석(玉)의 빛깔이 세상 밖으로 뚜렷하게 '나타나다' 혹은 눈앞(見)에 펼쳐진 '지금(현재)'을 의미합니다.",
    "example_words": [
      { "word": "現れる", "reading": "あらわれる", "meaning": "나타나다", "description": "보이지 않던 것이 겉으로 드러나는 것입니다." },
      { "word": "現在", "reading": "げんざい", "meaning": "현재", "description": "지금 눈앞에 나타나(現) 있는(在) 시간입니다." }
    ]
  },
  {
    "kanji": "留",
    "reading_on": "リュウ、ル",
    "reading_kun": "と(める)、と(まる)",
    "meaning": "머무를",
    "components": [
      { "char": "卯", "role": "토끼 묘 (요소)", "desc": "물이 양쪽으로 흩어지는 모양(戼)의 변형으로, 여기서는 멈추어 괸다는 뜻과 발음 '류'를 줍니다." },
      { "char": "田", "role": "밭 전 (부수)", "desc": "논이나 밭을 의미합니다." }
    ],
    "story": "물이 흘러가지 않고 논(田)이나 밭에 괴어서 오랫동안 '머무르다' 혹은 나가지 못하게 '만류하다'는 뜻입니다.",
    "example_words": [
      { "word": "留まる", "reading": "とまる", "meaning": "머물다, 고정되다", "description": "움직이지 않고 한곳에 머무르거나 남는 것입니다." },
      { "word": "留学", "reading": "りゅうがく", "meaning": "유학", "description": "외국에 머무르며(留) 공부(学)하는 일입니다." }
    ]
  },
  {
    "kanji": "略",
    "reading_on": "リャク",
    "reading_kun": "",
    "meaning": "간략할 (생략할)",
    "components": [
      { "char": "田", "role": "밭 전 (부수)", "desc": "논밭을 뜻합니다." },
      { "char": "各", "role": "각각 각 (요소)", "desc": "따로따로라는 뜻과 발음 '각/랴쿠'를 담당합니다." }
    ],
    "story": "여러 사람의 논밭(田)을 각각(各)의 경계를 돌아다니며 자세히 살핀 뒤, 세세한 부분은 '생략하고(간략하게)' 요점만 남긴다는 뜻을 지닙니다.",
    "example_words": [
      { "word": "省略", "reading": "しょうりゃく", "meaning": "생략", "description": "자세한(省) 부분을 줄여서 간략하게(略) 하는 것입니다." },
      { "word": "略字", "reading": "りゃくじ", "meaning": "약자", "description": "복잡한 글자를 간략하게(略) 줄여 쓴 글자(字)입니다." }
    ]
  },
  {
    "kanji": "益",
    "reading_on": "エキ、ヤク",
    "reading_kun": "",
    "meaning": "더할 (유익할)",
    "components": [
      { "char": "水", "role": "물 수 (요소)", "desc": "가로로 쓰인 물 수(水) 자의 변형으로, 넘쳐흐르는 물을 뜻합니다." },
      { "char": "皿", "role": "그릇 명 (부수)", "desc": "그릇을 의미합니다." }
    ],
    "story": "그릇(皿)에 물(水의 변형)을 붓고 또 부어서 가득 차 찰랑거릴 정도로 '더하다', 혹은 차고 넘치도록 '이익이 되다(유익하다)'는 뜻입니다.",
    "example_words": [
      { "word": "利益", "reading": "りえき", "meaning": "이익", "description": "이롭고(利) 더해져서 남는 장사나 좋은 점(益)입니다." },
      { "word": "有益", "reading": "ゆうえき", "meaning": "유익", "description": "이로움과 이익(益)이 있음(有)입니다." }
    ]
  },
  {
    "kanji": "眼",
    "reading_on": "ガン",
    "reading_kun": "まなこ",
    "meaning": "눈 (안목)",
    "components": [
      { "char": "目", "role": "눈 목 (부수)", "desc": "눈을 뜻합니다." },
      { "char": "艮", "role": "그칠 간 (요소)", "desc": "원래 눈을 부릅뜨고 돌아본다는 뜻(눈을 부릅뜰 은)과 발음 '간/간'을 줍니다." }
    ],
    "story": "사람의 '눈'을 뜻하며, 특히 사물을 깊이 있게 살펴보는 눈썰미나 '안목'을 의미합니다.",
    "example_words": [
      { "word": "眼科", "reading": "がんか", "meaning": "안과", "description": "눈(眼)의 병을 치료하는 의학의 갈래(科)입니다." },
      { "word": "眼鏡", "reading": "めがね", "meaning": "안경", "description": "눈(眼)이 잘 보이게 쓰거나 보호하는 거울(鏡, 렌즈)입니다." }
    ]
  },
  {
    "kanji": "破",
    "reading_on": "ハ",
    "reading_kun": "やぶ(る)、やぶ(れる)",
    "meaning": "깨뜨릴",
    "components": [
      { "char": "石", "role": "돌 석 (부수)", "desc": "돌을 뜻합니다." },
      { "char": "皮", "role": "가죽 피 (요소)", "desc": "가죽이나 껍질이 벗겨진다는 뜻과 발음 '파/하'를 줍니다." }
    ],
    "story": "단단한 돌(石)을 쳐서 그 겉껍질(皮)을 완전히 부수고 '깨뜨리다' 혹은 약속을 '어기다(파괴하다)'는 뜻입니다.",
    "example_words": [
      { "word": "破れる", "reading": "やぶれる", "meaning": "찢어じだ, 깨지다", "description": "종이나 천 따위가 찢어지거나 약속이 깨지는 것입니다." },
      { "word": "破壊", "reading": "はかい", "meaning": "파괴", "description": "때려 부수어(破) 무너뜨리는(壊) 일입니다." }
    ]
  },
  {
    "kanji": "確",
    "reading_on": "カク",
    "reading_kun": "たし(か)、たし(かめる)",
    "meaning": "굳을 (확실할)",
    "components": [
      { "char": "石", "role": "돌 석 (부수)", "desc": "돌이나 바위처럼 단단함을 뜻합니다." },
      { "char": "隺", "role": "두루미 학 (요소)", "desc": "새가 높이 날아 둥지를 짓는다는 데서 딱딱하게 굳어짐을 뜻하며 발음 '학/카쿠'의 변형 역할을 합니다." }
    ],
    "story": "바위(石)처럼 단단하게 굳어 있어 의심할 여지 없이 틀림없고 '확실하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "確か", "reading": "たしか", "meaning": "확실히, 아마", "description": "틀림없이 그러하거나, 기억을 더듬어 볼 때 분명히 그런 모양입니다." },
      { "word": "確認", "reading": "かくにん", "meaning": "확인", "description": "틀림없는지 확실하게(確) 살펴보고 인정하는(認) 것입니다." }
    ]
  },
  {
    "kanji": "示",
    "reading_on": "ジ、シ",
    "reading_kun": "しめ(す)",
    "meaning": "보일 (지시할)",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "조상에게 제사를 지내는 제단(상) 모양을 본뜬 글자입니다." }
    ],
    "story": "제단(示)에서 제사를 지낼 때 신이 사람들에게 징조나 길을 '보여주다', 혹은 남에게 의견이나 길을 '지시하다(나타내다)'는 뜻입니다.",
    "example_words": [
      { "word": "示す", "reading": "しめす", "meaning": "가리키다, 보여주다", "description": "남에게 어떤 뜻이나 물건을 꺼내어 알게 하는 것입니다." },
      { "word": "指示", "reading": "しじ", "meaning": "지시", "description": "어떤 행동을 하도록 손가락으로 가리켜(指) 보여주는(示) 일입니다." }
    ]
  },
  {
    "kanji": "祖",
    "reading_on": "ソ",
    "reading_kun": "",
    "meaning": "할아비 (조상)",
    "components": [
      { "char": "礻", "role": "보일 시 (부수)", "desc": "신령이나 제단을 뜻합니다." },
      { "char": "且", "role": "또 차 (요소)", "desc": "남성의 성기나 위패 모양을 본떠 생명의 근원이라는 뜻과 발음 '조/소'를 담당합니다." }
    ],
    "story": "신주나 위패(且)를 모신 제단(礻)에 제사를 지내는 대상인 윗대 어른, 즉 '할아버지'나 집안의 '조상'을 의미합니다.",
    "example_words": [
      { "word": "祖父", "reading": "そふ", "meaning": "할아버지", "description": "아버지(父)의 아버지(祖)입니다." },
      { "word": "祖先", "reading": "そせん", "meaning": "조상", "description": "자신의 집안에서 먼저(先) 태어나 살다 간 어른(祖)들입니다." }
    ]
  },
  {
    "kanji": "禁",
    "reading_on": "キン",
    "reading_kun": "",
    "meaning": "금할",
    "components": [
      { "char": "林", "role": "수풀 림 (요소)", "desc": "신성한 나무들이 늘어선 숲이라는 뜻과 발음 '금/킨'을 줍니다." },
      { "char": "示", "role": "보일 시 (부수)", "desc": "신령이나 제단을 뜻합니다." }
    ],
    "story": "신에게 제사를 지내는(示) 제단 앞의 신성한 숲(林)에는 함부로 들어가지 못하도록 출입을 '금지하다(금하다)'는 의미입니다.",
    "example_words": [
      { "word": "禁止", "reading": "きんし", "meaning": "금지", "description": "어떤 행동을 못하게 금하여(禁) 그치게 하는(止) 일입니다." },
      { "word": "禁煙", "reading": "きんえん", "meaning": "금연", "description": "담배 연기(煙)를 피우지 못하게 금지하는(禁) 것입니다." }
    ]
  },
  {
    "kanji": "移",
    "reading_on": "イ",
    "reading_kun": "うつ(る)、うつ(す)",
    "meaning": "옮길",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 모를 뜻합니다." },
      { "char": "多", "role": "많을 다 (요소)", "desc": "크고 많게 한다는 뜻과 발음 '이/이'를 담당합니다." }
    ],
    "story": "곡식(禾)을 더 많고(多) 크레 기르기 위해 모판에서 자란 모를 논으로 뽑아 '옮겨 심다(이앙하다)', 혹은 장소를 '이동하다'는 뜻입니다.",
    "example_words": [
      { "word": "移る", "reading": "うつる", "meaning": "옮겨가다, 이동하다", "description": "사람이나 사물이 있던 곳에서 다른 곳으로 자리를 바꾸는 것입니다." },
      { "word": "移動", "reading": "いどう", "meaning": "이동", "description": "자리를 옮겨(移) 움직여(動) 가는 것입니다." }
    ]
  },
  {
    "kanji": "程",
    "reading_on": "テイ",
    "reading_kun": "ほど",
    "meaning": "한도 (정도)",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식을 의미합니다." },
      { "char": "呈", "role": "드릴 정 (요소)", "desc": "물건을 저울에 달아 나타낸다는 뜻과 발음 '정/테이'를 줍니다." }
    ],
    "story": "곡식(禾)의 무게를 달아(呈) 일정한 양이나 규격을 정한 데서, 사물의 알맞은 분량이나 '한도', 또는 어느 '정도'를 의미합니다.",
    "example_words": [
      { "word": "程度", "reading": "ていど", "meaning": "정도", "description": "사물의 성질이나 수준이 이르는 한도(程)와 정도(度)입니다." },
      { "word": "日程", "reading": "にってい", "meaning": "일정", "description": "하루하루(日) 겪어 나가야 할 일의 순서나 정도(程)입니다." }
    ]
  },
  {
    "kanji": "税",
    "reading_on": "ゼイ",
    "reading_kun": "",
    "meaning": "세금",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식을 의미합니다." },
      { "char": "兌", "role": "바꿀 태 (요소)", "desc": "기뻐하다, 벗어난다는 뜻에서 조금 덜어낸다는 의미와 발음 '태/제이'를 줍니다." }
    ],
    "story": "농민이 거둔 곡식(禾) 중에서 일정한 양을 국가에 덜어내어(兌) 바치는 곡식, 즉 '세금'을 뜻합니다.",
    "example_words": [
      { "word": "税金", "reading": "ぜいきん", "meaning": "세금", "description": "국가나 사회를 운영하기 위해 국민이 바치는 세금(税)인 돈(金)입니다." },
      { "word": "消費税", "reading": "しょうひぜい", "meaning": "소비세", "description": "물건을 사서 쓸(消費) 때 매겨지는 세금(税)입니다." }
    ]
  },
  {
    "kanji": "築",
    "reading_on": "チク",
    "reading_kun": "きず(く)",
    "meaning": "쌓을 (건축할)",
    "components": [
      { "char": "筑", "role": "축 축 (요소)", "desc": "대나무(竹)로 만든 악기를 손에 들고(巩) 친다는 뜻에서 단단히 다진다는 의미와 발음 '축/치쿠'를 줍니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 목재를 뜻합니다." }
    ],
    "story": "나무(木) 기둥을 세우고 도구(筑)로 흙을 단단하게 다져 건물을 '쌓다' 혹은 집을 '건축하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "築く", "reading": "きずく", "meaning": "쌓다, 구축하다", "description": "돌이나 흙으로 기초를 다지거나 재산이나 세력을 쌓아 올리는 것입니다." },
      { "word": "建築", "reading": "けんちく", "meaning": "건축", "description": "집이나 다리 따위를 세우고(建) 쌓아 올리는(築) 일입니다." }
    ]
  },
  {
    "kanji": "精",
    "reading_on": "セイ、ショウ",
    "reading_kun": "",
    "meaning": "정할 (깨끗할)",
    "components": [
      { "char": "米", "role": "쌀 미 (부수)", "desc": "쌀이나 곡식을 뜻합니다." },
      { "char": "青", "role": "푸를 청 (요소)", "desc": "푸르고 맑다는 뜻과 발음 '청/세이'를 줍니다." }
    ],
    "story": "쌀(米)의 겉껍질을 깎아내어 희고 깨끗하게(青) 찧은 쌀인 '정미'에서 유래하여, 흠집이 없고 맑아 순수하고 '깨끗하다' 혹은 사람의 참된 기운(정신)을 의미합니다.",
    "example_words": [
      { "word": "精神", "reading": "せいしん", "meaning": "정신", "description": "마음이나 영혼의 맑고(精) 신령스러운(神) 기운입니다." },
      { "word": "精算", "reading": "せいさん", "meaning": "정산", "description": "돈의 계산을 자세하고(精) 틀림없게 하는(算) 일입니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade5.json'
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

print("Grade 5 Part 4 data appended successfully.")
