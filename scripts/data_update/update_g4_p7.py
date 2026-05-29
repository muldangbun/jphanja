import json
import os

new_data = [
  {
    "kanji": "無",
    "reading_on": "ム、ブ",
    "reading_kun": "な(い)",
    "meaning": "없을",
    "components": [
      { "char": "舞", "role": "춤출 무 (요소)", "desc": "사람들이 소매를 길게 늘어뜨리고 춤추는 모습의 원래 글자입니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불(火)을 뜻하나 여기서는 원래 숲을 의미하는 글자나 장식의 변형입니다." }
    ],
    "story": "원래 숲속에서 춤을 춘다는 뜻이었으나, 나중에 불(灬)타 없어져서 아무것도 '없다(무)'는 뜻으로 주로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "無い", "reading": "ない", "meaning": "없다", "description": "어떤 사물이나 사실이 존재하지 않는 상태입니다." },
      { "word": "無料", "reading": "むりょう", "meaning": "무료", "description": "내야 할 요금(料)이 없음(無), 즉 공짜입니다." }
    ]
  },
  {
    "kanji": "約",
    "reading_on": "ヤク",
    "reading_kun": "",
    "meaning": "맺을 (약속할)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "勺", "role": "구기 작 (요소)", "desc": "국자 모양으로, 여기서는 하나로 모아 묶는다는 뜻과 발음 '작/야쿠'를 줍니다." }
    ],
    "story": "여러 가닥의 실(糸)을 한데 모아 단단히 묶듯이(勺), 서로 의견을 모아 굳게 '맺다' 혹은 '약속하다'는 뜻입니다.",
    "example_words": [
      { "word": "約束", "reading": "やくそく", "meaning": "약속", "description": "서로 말을 맺고(約) 단단히 묶어(束) 지키기로 하는 일입니다." },
      { "word": "予約", "reading": "よやく", "meaning": "예약", "description": "미리(予) 자리나 물건을 맡아두기로 맺은(約) 일입니다." }
    ]
  },
  {
    "kanji": "勇",
    "reading_on": "ユウ",
    "reading_kun": "いさ(む)、いさ(ましい)",
    "meaning": "날랠 (용감할)",
    "components": [
      { "char": "マ", "role": "마 (요소)", "desc": "여기서는 위로 솟아오르는 기운인 甬(길 용)의 윗부분이 변형된 것입니다." },
      { "char": "男", "role": "사내 남 (요소)", "desc": "밭에서 힘쓰는 굳센 남자입니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 용기를 뜻합니다." }
    ],
    "story": "힘센 사내(男)가 넘치는 힘(力)을 주체하지 못하고 위로 솟구치듯(マ 변형) 기운차고 '날래다' 혹은 '용감하다'는 뜻입니다.",
    "example_words": [
      { "word": "勇気", "reading": "ゆうき", "meaning": "용기", "description": "두려움을 모르는 날래고(勇) 씩씩한 기운(気)입니다." },
      { "word": "勇ましい", "reading": "いさましい", "meaning": "용감하다, 씩씩하다", "description": "기운이 뻗쳐서 씩씩하고 두려움이 없는 모양입니다." }
    ]
  },
  {
    "kanji": "要",
    "reading_on": "ヨウ",
    "reading_kun": "い(る)",
    "meaning": "요긴할 (중요할)",
    "components": [
      { "char": "覀", "role": "덮을 아 (요소)", "desc": "원래 양손이나 몸을 감싸는 옷의 깃을 의미합니다." },
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." }
    ],
    "story": "여성(女)이 허리춤(覀의 원래 뜻)에 꼭 두르는 허리띠처럼 아주 요긴하고 '중요하다', 혹은 꼭 '필요하다'는 뜻입니다.",
    "example_words": [
      { "word": "重要", "reading": "じゅうよう", "meaning": "중요", "description": "아주 무겁고(重) 요긴함(要)을 뜻합니다." },
      { "word": "要る", "reading": "いる", "meaning": "필요하다", "description": "어떤 물건이나 일이 꼭 있어야 하는 것입니다." }
    ]
  },
  {
    "kanji": "養",
    "reading_on": "ヨウ",
    "reading_kun": "やしな(う)",
    "meaning": "기를",
    "components": [
      { "char": "羊", "role": "양 양 (요소)", "desc": "양처럼 착하고 통통하다는 뜻과 발음 '양/요우'를 담당합니다." },
      { "char": "食", "role": "밥 식 (부수)", "desc": "음식이나 먹이는 것을 의미합니다." }
    ],
    "story": "양(羊)처럼 통통하고 건강하게 자라도록 좋은 음식(食)을 먹여 사람이나 동물을 훌륭하게 '기르다' 혹은 '양육하다'는 뜻입니다.",
    "example_words": [
      { "word": "養う", "reading": "やしなう", "meaning": "기르다, 부양하다", "description": "가족을 먹여 살리거나 동물, 체력을 잘 보살펴 자라게 하는 것입니다." },
      { "word": "栄養", "reading": "えいよう", "meaning": "영양", "description": "몸을 영화롭게(栄) 기르는(養) 성분입니다." }
    ]
  },
  {
    "kanji": "浴",
    "reading_on": "ヨク",
    "reading_kun": "あ(びる)、あ(びせる)",
    "meaning": "목욕할",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "谷", "role": "골 곡 (요소)", "desc": "산골짜기, 몸의 텅 빈 계곡을 뜻하며 발음 '곡/요쿠'를 줍니다." }
    ],
    "story": "산골짜기(谷)에서 흘러내리는 맑은 계곡물(氵)에 몸을 담그거나 물을 끼얹어 '목욕하다' 혹은 빛을 '뒤집어쓰다'는 뜻입니다.",
    "example_words": [
      { "word": "浴びる", "reading": "あびる", "meaning": "뒤집어쓰다, (물을) 끼얹다", "description": "몸 전체에 물이나 햇빛 따위를 맞거나 받는 것입니다." },
      { "word": "海水浴", "reading": "かいすいよく", "meaning": "해수욕", "description": "바닷물(海水)에 들어가서 목욕하듯(浴) 즐기는 일입니다." }
    ]
  },
  {
    "kanji": "利",
    "reading_on": "リ",
    "reading_kun": "き(く)",
    "meaning": "이로울",
    "components": [
      { "char": "禾", "role": "벼 화 (요소)", "desc": "곡식이나 볏단을 의미합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 자르거나 거둔다는 뜻입니다." }
    ],
    "story": "가을이 되어 다 익은 곡식(禾)을 낫(刂)으로 베어 거두어들이니 이익이 생겨 '이롭다' 혹은 날이 '날카롭다(잘 든다)'는 뜻입니다.",
    "example_words": [
      { "word": "便利", "reading": "べんり", "meaning": "편리", "description": "쓰기에 편하고(便) 이로운(利) 상태입니다." },
      { "word": "利益", "reading": "りえき", "meaning": "이익", "description": "이롭고(利) 더해져서(益) 남는 것, 즉 벌어들인 돈이나 좋은 점입니다." }
    ]
  },
  {
    "kanji": "陸",
    "reading_on": "リク",
    "reading_kun": "",
    "meaning": "뭍 (육지)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 흙더미를 뜻합니다." },
      { "char": "坴", "role": "흙덩이 륙 (요소)", "desc": "흙이 여러 겹 솟아오른 모양으로 발음 '륙/리쿠'를 줍니다." }
    ],
    "story": "흙이 겹겹이 쌓여(坴) 바다보다 높이 솟아오른 커다란 언덕(阝), 즉 물이 없는 넓은 땅인 '뭍'이나 '육지'를 뜻합니다.",
    "example_words": [
      { "word": "陸", "reading": "りく", "meaning": "뭍, 육지", "description": "지구 표면에서 바다나 호수가 아닌 땅 부분입니다." },
      { "word": "大陸", "reading": "たいりく", "meaning": "대륙", "description": "바다로 둘러싸인 아주 큰(大) 육지(陸)입니다." }
    ]
  },
  {
    "kanji": "良",
    "reading_on": "リョウ",
    "reading_kun": "よ(い)",
    "meaning": "어질 (좋을)",
    "components": [
      { "char": "艮", "role": "그칠 간 (부수)", "desc": "여기서는 원래 맑고 깨끗한 쌀알을 고르는 도구의 모양에서 유래했습니다." }
    ],
    "story": "원래 곡식에서 티끌을 빼고 깨끗하고 좋은 쌀만 골라내는 모양을 본떠, 품질이나 성질이 '좋다' 혹은 마음씨가 착하고 '어질다'는 뜻입니다.",
    "example_words": [
      { "word": "良い", "reading": "よい", "meaning": "좋다", "description": "훌륭하거나 마음에 들어 긍정적인 상태입니다. (いい와 같은 뜻이나 더 격식있는 표현입니다)" },
      { "word": "不良", "reading": "ふりょう", "meaning": "불량", "description": "상태나 행실이 좋지(良) 않은(不) 것입니다." }
    ]
  },
  {
    "kanji": "料",
    "reading_on": "リョウ",
    "reading_kun": "",
    "meaning": "헤아릴 (재료)",
    "components": [
      { "char": "米", "role": "쌀 미 (요소)", "desc": "쌀이나 곡식을 의미합니다." },
      { "char": "斗", "role": "말 두 (부수)", "desc": "곡식을 담아 양을 재는 국자나 말을 뜻합니다." }
    ],
    "story": "말(斗)로 쌀(米)의 양을 되어 '헤아리다'라는 뜻에서 유래하여, 일의 바탕이 되는 '재료'나 치러야 할 '요금'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "料理", "reading": "りょうり", "meaning": "요리", "description": "재료(料)를 알맞게 다스려(理) 음식을 만드는 일입니다." },
      { "word": "無料", "reading": "むりょう", "meaning": "무료", "description": "내야 할 요금(料)이 없음(無)입니다." }
    ]
  },
  {
    "kanji": "量",
    "reading_on": "リョウ",
    "reading_kun": "はか(る)",
    "meaning": "헤아릴 (양)",
    "components": [
      { "char": "日", "role": "날 일 (요소)", "desc": "원래는 곡식을 담는 자루 모양인 東의 변형입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "자루에 담긴 곡식의 선입니다." },
      { "char": "里", "role": "마을 리 (부수)", "desc": "원래 무겁다는 뜻인 重(무거울 중)의 변형으로 무게를 뜻합니다." }
    ],
    "story": "자루(日의 원형)에 곡식을 가득 담아 무게(里의 원형)를 저울로 달아 '헤아리다' 혹은 사물의 '분량(양)'을 뜻합니다.",
    "example_words": [
      { "word": "量る", "reading": "はかる", "meaning": "달다, 재다", "description": "저울 따위로 무게나 부피를 헤아리는 것입니다." },
      { "word": "大量", "reading": "たいりょう", "meaning": "대량", "description": "아주 큰(大) 분량(量)이나 수량입니다." }
    ]
  },
  {
    "kanji": "輪",
    "reading_on": "リン",
    "reading_kun": "わ",
    "meaning": "바퀴 (고리)",
    "components": [
      { "char": "車", "role": "수레 거 (부수)", "desc": "수레나 바퀴를 뜻합니다." },
      { "char": "侖", "role": "둥글 륜 (요소)", "desc": "둥글게 묶여 질서 정연하다는 뜻과 발음 '륜/린'을 줍니다." }
    ],
    "story": "수레(車) 아래에 달린 둥글고(侖) 잘 굴러가는 둥그런 물건인 '바퀴'나 둥근 '고리'를 뜻합니다.",
    "example_words": [
      { "word": "輪", "reading": "わ", "meaning": "고리, 바퀴", "description": "둥글게 된 모양이나 테두리입니다." },
      { "word": "指輪", "reading": "ゆびわ", "meaning": "반지", "description": "손가락(指)에 끼우는 둥근 고리(輪) 장신구입니다." }
    ]
  },
  {
    "kanji": "類",
    "reading_on": "ルイ",
    "reading_kun": "",
    "meaning": "무리 (종류)",
    "components": [
      { "char": "米", "role": "쌀 미 (요소)", "desc": "원래 개(犬)의 변형이거나 씨앗을 뜻합니다." },
      { "char": "大", "role": "큰 대 (요소)", "desc": "큰 짐승을 의미합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "머리나 모양을 뜻하여 생김새가 비슷한 것들을 뜻합니다." }
    ],
    "story": "씨앗(米)이나 큰(大) 짐승처럼 머리(頁) 모양이나 생김새가 비슷한 것들끼리 묶어 놓은 '무리'나 갈래인 '종류'를 뜻합니다.",
    "example_words": [
      { "word": "種類", "reading": "しゅるい", "meaning": "종류", "description": "비슷한 특징을 가진 것끼리 나눈 갈래(種)나 무리(類)입니다." },
      { "word": "人類", "reading": "じんるい", "meaning": "인류", "description": "사람(人)의 무리(類), 즉 세상의 모든 사람입니다." }
    ]
  },
  {
    "kanji": "令",
    "reading_on": "レイ",
    "reading_kun": "",
    "meaning": "하여금 (명령)",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "여기서는 모인다는 뜻의 삼합집머리(亼)입니다." },
      { "char": "卩", "role": "병부 절 (요소)", "desc": "사람이 무릎을 꿇고 있는 모양입니다." }
    ],
    "story": "사람들(亼)을 모아놓고 무릎을 꿇게(卩) 하여 윗사람이 법도나 분부를 내려 '~로 하여금 ~하게 하다' 혹은 '명령'이라는 뜻을 가집니다.",
    "example_words": [
      { "word": "命令", "reading": "めいれい", "meaning": "명령", "description": "웃어른이 목숨(命)처럼 지키라고 분부를 내리는(令) 일입니다." },
      { "word": "令嬢", "reading": "れいじょう", "meaning": "영애", "description": "남의 딸을 높여 부르는 훌륭한(令) 아가씨(嬢)라는 말입니다." }
    ]
  },
  {
    "kanji": "冷",
    "reading_on": "レイ",
    "reading_kun": "つめ(たい)、ひ(える)、ひ(や)、ひ(やす)、ひ(やかす)、さ(める)、さ(ます)",
    "meaning": "찰",
    "components": [
      { "char": "冫", "role": "이수변 (부수)", "desc": "얼음이나 차가움을 뜻합니다." },
      { "char": "令", "role": "명령 령 (요소)", "desc": "맑고 깨끗하다는 뜻과 발음 '령/레이'를 줍니다." }
    ],
    "story": "얼음(冫)처럼 맑고 깨끗하여(令) 만지면 서늘하고 '차갑다(차다)' 혹은 식는다는 뜻입니다.",
    "example_words": [
      { "word": "冷たい", "reading": "つめたい", "meaning": "차갑다", "description": "온도가 낮아 만졌을 때 찬 느낌이 드는 상태입니다." },
      { "word": "冷房", "reading": "れいぼう", "meaning": "냉방", "description": "방(房)의 온도를 차갑게(冷) 낮추는 장치나 일입니다." }
    ]
  },
  {
    "kanji": "例",
    "reading_on": "レイ",
    "reading_kun": "たと(える)",
    "meaning": "법식 (예시)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 규칙을 따르는 사람을 뜻합니다." },
      { "char": "列", "role": "벌일 렬 (요소)", "desc": "나란히 세운다는 뜻에서 앞서 늘어선 본보기라는 의미와 발음 '렬/레이'를 줍니다." }
    ],
    "story": "사람(亻)들이 나란히 줄(列)을 서듯 이전에 정해진 기준이나 본보기인 '법식', 혹은 그것을 들어 비교하여 '예시하다(비유하다)'는 뜻입니다.",
    "example_words": [
      { "word": "例えば", "reading": "たとえば", "meaning": "예를 들면", "description": "어떤 것을 설명하기 위해 본보기를 들어 말할 때 쓰는 말입니다." },
      { "word": "例外", "reading": "れいがい", "meaning": "예외", "description": "일반적인 법식이나 예(例)에서 벗어난(外) 것입니다." }
    ]
  },
  {
    "kanji": "歴",
    "reading_on": "レキ",
    "reading_kun": "",
    "meaning": "지낼 (역사)",
    "components": [
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "언덕이나 장소를 뜻합니다." },
      { "char": "林", "role": "수풀 림 (요소)", "desc": "나무가 빽빽하게 늘어선 모습입니다." },
      { "char": "止", "role": "그칠 지 (부수)", "desc": "발걸음이나 지나가는 동작을 의미합니다." }
    ],
    "story": "나무가 빽빽한(林) 험한 언덕길(厂)을 오랜 시간에 걸쳐 차례차례 한 걸음씩(止) 밟고 '지나가다' 혹은 겪어온 세월인 '역사(경력)'를 뜻합니다.",
    "example_words": [
      { "word": "歴史", "reading": "れきし", "meaning": "역사", "description": "지난 세월(歴) 동안 일어난 일을 기록한 문헌(史)입니다." },
      { "word": "履歴書", "reading": "りれきしょ", "meaning": "이력서", "description": "지금까지 지내오고(歴) 밟아온(履) 학업이나 직업을 적은 문서(書)입니다." }
    ]
  },
  {
    "kanji": "連",
    "reading_on": "レン",
    "reading_kun": "つら(なる)、つら(ねる)、つ(れる)",
    "meaning": "이을 (데릴)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "車", "role": "수레 거 (요소)", "desc": "수레가 꼬리에 꼬리를 물고 이어진다는 뜻입니다." }
    ],
    "story": "길(辶) 위에 여러 대의 수레(車)가 꼬리에 꼬리를 물고 줄줄이 '이어지다' 혹은 사람을 '데리다(동반하다)'는 의미입니다.",
    "example_words": [
      { "word": "連れる", "reading": "つれる", "meaning": "데리고 가다", "description": "다른 사람이나 동물을 함께 뒤따르게 하여 가는 것입니다." },
      { "word": "連続", "reading": "れんぞく", "meaning": "연속", "description": "끊어지지 않고 연달아(連) 이어지는(続) 일입니다." }
    ]
  },
  {
    "kanji": "老",
    "reading_on": "ロウ",
    "reading_kun": "お(いる)、ふ(ける)",
    "meaning": "늙을",
    "components": [
      { "char": "耂", "role": "늙을 로 (부수)", "desc": "머리칼이 길고 허리가 굽은 노인의 모습입니다." },
      { "char": "匕", "role": "비수 비 (요소)", "desc": "모양이 변한다는 뜻이나, 지팡이를 짚고 있는 모습을 나타냅니다." }
    ],
    "story": "머리카락이 하얗게 세고 허리가 굽은 노인(耂)이 지팡이(匕의 변형)를 짚고 서 있는 모습에서 나이가 들어 '늙다'는 뜻입니다.",
    "example_words": [
      { "word": "老いる", "reading": "おいる", "meaning": "늙다", "description": "나이가 들어 젊음과 기운이 없어지는 것입니다." },
      { "word": "老人", "reading": "ろうじん", "meaning": "노인", "description": "나이가 들어 늙은(老) 사람(人)입니다." }
    ]
  },
  {
    "kanji": "労",
    "reading_on": "ロウ",
    "reading_kun": "",
    "meaning": "일할 (수고할)",
    "components": [
      { "char": "⺍", "role": "불똥 주 (요소)", "desc": "원래 횃불 두 개가 겹친 모양인 𤇾(불꽃 형)의 약자로 밤새워 불을 밝힌다는 뜻입니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "건물이나 장소를 뜻합니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘을 쓰거나 노력함을 뜻합니다." }
    ],
    "story": "밤에 횃불(⺍ 변형)을 켜고 집안(冖)에서 힘(力)을 다해 열심히 '일하다' 혹은 애써서 '수고하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "労働", "reading": "ろうどう", "meaning": "노동", "description": "몸을 써서 애써 수고하며(労) 움직여 일하는(働) 것입니다." },
      { "word": "苦労", "reading": "くろう", "meaning": "고생, 수고", "description": "괴로움을(苦) 겪으며 수고롭게 일하는(労) 일입니다." }
    ]
  },
  {
    "kanji": "録",
    "reading_on": "ロク",
    "reading_kun": "",
    "meaning": "기록할",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 쇠로 만든 칼을 뜻합니다." },
      { "char": "彔", "role": "나무새길 록 (요소)", "desc": "나무를 칼로 깎아 글자를 새긴다는 뜻과 발음 '록/로쿠'를 줍니다." }
    ],
    "story": "칼이나 쇠붙이(金) 도구를 사용하여 나무판자나 쇠(彔)에 글자를 새겨 후세에 남기기 위해 '기록하다'는 뜻입니다.",
    "example_words": [
      { "word": "記録", "reading": "きろく", "meaning": "기록", "description": "잊지 않도록 사실을 적어서(記) 남겨두는(録) 것입니다." },
      { "word": "録音", "reading": "ろくおん", "meaning": "녹음", "description": "소리(音)나 말을 기계에 기록하여(録) 남기는 일입니다." }
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

print("Grade 4 Part 7 data appended successfully.")
