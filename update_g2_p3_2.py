import json
import os

new_data = [
  {
    "kanji": "国",
    "reading_on": "コク",
    "reading_kun": "くに",
    "meaning": "나라",
    "components": [
      { "char": "囗", "role": "에운담 구 (부수)", "desc": "사방을 둘러싼 울타리나 국경을 뜻합니다." },
      { "char": "玉", "role": "구슬 옥 (요소)", "desc": "왕(王)이 가진 보물(玉)처럼 소중한 영토를 의미합니다." }
    ],
    "story": "국경(囗) 안에서 왕이 구슬(玉)처럼 소중하게 다스리는 영토, 즉 '나라'를 뜻합니다.",
    "example_words": [
      { "word": "外国", "reading": "がいこく", "meaning": "외국", "description": "바깥(外)의 나라(国)입니다." },
      { "word": "国家", "reading": "こっか", "meaning": "국가", "description": "나라(国)와 집안(家), 즉 한 나라 전체를 뜻합니다." }
    ]
  },
  {
    "kanji": "黒",
    "reading_on": "コク",
    "reading_kun": "くろ(い)",
    "meaning": "검다",
    "components": [
      { "char": "里", "role": "마을 리 (변형)", "desc": "여기서는 창문이 있는 연기를 피우는 아궁이를 나타냅니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "타오르는 불꽃을 의미합니다." }
    ],
    "story": "불(灬)을 때어 아궁이 위쪽 창문(里의 변형)에 그을음이 묻어 '검게' 된 모습을 나타냅니다.",
    "example_words": [
      { "word": "黒板", "reading": "こくばん", "meaning": "칠판", "description": "검은(黒) 널빤지(板)라는 뜻입니다." },
      { "word": "白黒", "reading": "しろくろ", "meaning": "흑백", "description": "흰색(白)과 검은색(黒)입니다." }
    ]
  },
  {
    "kanji": "今",
    "reading_on": "コン、キン",
    "reading_kun": "いま",
    "meaning": "이제 / 지금",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "여기서는 어떤 것을 덮어 누르는 뚜껑이나 덮개 모양입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "과거를 가두어두는 경계를 뜻합니다." }
    ],
    "story": "과거를 뚜껑(人)으로 덮어버리고 남은 바로 '지금', '현재'를 의미합니다.",
    "example_words": [
      { "word": "今日", "reading": "きょう", "meaning": "오늘", "description": "지금(今)의 날(日)입니다. (특별한 발음)" },
      { "word": "今週", "reading": "こんしゅう", "meaning": "이번 주", "description": "지금(今) 해당되는 주(週)입니다." }
    ]
  },
  {
    "kanji": "才",
    "reading_on": "サイ",
    "reading_kun": "",
    "meaning": "재주",
    "components": [
      { "char": "手", "role": "손 수 (부수)", "desc": "원래 땅에서 식물의 싹이 돋아나는 모습(손의 형태와 유사)에서 유래했습니다." }
    ],
    "story": "땅을 뚫고 힘차게 돋아나는 새싹의 모습에서 사람의 타고난 '재주'나 '재능'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "天才", "reading": "てんさい", "meaning": "천재", "description": "하늘(天)에서 타고난 재주(才)를 가진 사람입니다." },
      { "word": "才能", "reading": "さいのう", "meaning": "재능", "description": "재주(才)와 능력(能)입니다." }
    ]
  },
  {
    "kanji": "細",
    "reading_on": "サイ",
    "reading_kun": "ほそ(い)、こま(かい)",
    "meaning": "가늘다 / 자세하다",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "가느다란 실을 나타냅니다." },
      { "char": "田", "role": "밭 전 (요소)", "desc": "정수리나 밭을 뜻하며, 본래는 작다(신)는 뜻에서 왔습니다." }
    ],
    "story": "실(糸)처럼 아주 '가늘고' 작은 것, 혹은 작은 조각들이 모여 있어서 '자세하다'는 뜻입니다.",
    "example_words": [
      { "word": "細い", "reading": "ほそい", "meaning": "가늘다", "description": "물건의 두께나 굵기가 가느다란 것을 말합니다." },
      { "word": "細かい", "reading": "こまかい", "meaning": "자잘하다, 자세하다", "description": "크기가 자잘하거나 내용이 상세한 것을 뜻합니다." }
    ]
  },
  {
    "kanji": "作",
    "reading_on": "サク、サ",
    "reading_kun": "つく(る)",
    "meaning": "지을 / 만들다",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "乍", "role": "잠깐 사 (요소)", "desc": "칼로 나무를 깎는 모습을 본떠 '작업'을 의미합니다." }
    ],
    "story": "사람(亻)이 도구를 들고 뚝딱뚝딱 물건을 '만든다' 혹은 글을 '지어낸다'는 뜻입니다.",
    "example_words": [
      { "word": "作品", "reading": "さくひん", "meaning": "작품", "description": "만들어낸(作) 물품(品)이나 예술작품을 말합니다." },
      { "word": "作業", "reading": "さぎょう", "meaning": "작업", "description": "무언가를 만드는(作) 업무나 일(業)입니다." }
    ]
  },
  {
    "kanji": "算",
    "reading_on": "サン",
    "reading_kun": "",
    "meaning": "셈하다 / 계산하다",
    "components": [
      { "char": "竹", "role": "대 죽 (부수)", "desc": "대나무로 만든 계산용 도구(산가지)를 뜻합니다." },
      { "char": "目", "role": "눈 목 (요소)", "desc": "눈으로 세심히 살펴본다는 의미입니다." },
      { "char": "廾", "role": "스물 입 / 두 손 (요소)", "desc": "두 손으로 잡고 조작하는 모습입니다." }
    ],
    "story": "두 손(廾)으로 대나무 산가지(竹)를 쥐고 눈(目)으로 집중하며 숫자를 '계산하는' 모습을 나타냅니다.",
    "example_words": [
      { "word": "算数", "reading": "さんすう", "meaning": "산수", "description": "숫자(数)를 계산(算)하는 초급 수학입니다." },
      { "word": "計算", "reading": "けいさん", "meaning": "계산", "description": "숫자를 셈(計)하고 맞추는(算) 일입니다." }
    ]
  },
  {
    "kanji": "止",
    "reading_on": "シ",
    "reading_kun": "と(まる)、と(める)",
    "meaning": "그치다 / 멈추다",
    "components": [
      { "char": "止", "role": "그칠 지 (부수)", "desc": "사람의 발자국 모양을 본뜬 상형문자입니다." }
    ],
    "story": "사람이 걷다가 남긴 발자국의 모습을 그려, 발걸음을 '멈추다' 혹은 하던 일을 '그치다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "中止", "reading": "ちゅうし", "meaning": "중지", "description": "중간(中)에 하던 일을 멈추는(止) 것입니다." },
      { "word": "止まれ", "reading": "とまれ", "meaning": "정지 (표지판)", "description": "교통 표지판 등에서 '멈추라'는 명령을 나타냅니다." }
    ]
  },
  {
    "kanji": "市",
    "reading_on": "シ",
    "reading_kun": "いち",
    "meaning": "저자 (시장) / 도시",
    "components": [
      { "char": "亠", "role": "돼지해머리 (요소)", "desc": "사람들이 모이는 장소의 덮개나 표지판입니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "물건을 둘러싼 천이나 상점의 가판대를 뜻합니다." }
    ],
    "story": "천막이나 가판대(巾) 아래에 사람들이 물건을 교환하러 모이는 '시장', 나아가 사람이 많이 사는 '도시'를 뜻합니다.",
    "example_words": [
      { "word": "市場", "reading": "いちば", "meaning": "시장", "description": "물건을 파는 저자(市)가 열리는 장소(場)입니다." },
      { "word": "市民", "reading": "しみん", "meaning": "시민", "description": "도시(市)에 사는 백성(民)입니다." }
    ]
  },
  {
    "kanji": "矢",
    "reading_on": "シ",
    "reading_kun": "や",
    "meaning": "화살",
    "components": [
      { "char": "矢", "role": "화살 시 (부수)", "desc": "깃털과 화살촉이 달린 화살의 모양을 본뜬 글자입니다." }
    ],
    "story": "끝이 뾰족하고 뒤에는 깃이 달린 '화살'의 모양을 그대로 그려낸 상형문자입니다.",
    "example_words": [
      { "word": "弓矢", "reading": "ゆみや", "meaning": "활과 화살", "description": "활(弓)과 화살(矢)입니다." },
      { "word": "矢印", "reading": "やじるし", "meaning": "화살표", "description": "화살(矢) 모양의 표시(印)입니다." }
    ]
  },
  {
    "kanji": "姉",
    "reading_on": "シ",
    "reading_kun": "あね",
    "meaning": "누나 / 언니",
    "components": [
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." },
      { "char": "市", "role": "저자 시 (요소)", "desc": "발음 '시'를 나타내며, 장성하여 시장에 갈 수 있는 나이를 의미하기도 합니다." }
    ],
    "story": "여성(女) 중에서 나이가 많아 앞장서서 이끄는 사람인 '언니'나 '누나'를 뜻합니다.",
    "example_words": [
      { "word": "姉妹", "reading": "しまい", "meaning": "자매", "description": "언니(姉)와 여동생(妹)입니다." },
      { "word": "お姉さん", "reading": "おねえさん", "meaning": "언니, 누나", "description": "언니를 높이거나 친근하게 부르는 말입니다." }
    ]
  },
  {
    "kanji": "思",
    "reading_on": "シ",
    "reading_kun": "おも(う)",
    "meaning": "생각하다",
    "components": [
      { "char": "田", "role": "밭 전 (변형)", "desc": "본래 아이의 정수리나 뇌를 상징하는 신(囟)에서 변형되었습니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 감정과 마음을 뜻합니다." }
    ],
    "story": "머리(田/뇌)와 마음(心)을 모두 써서 깊이 '생각하고' 그리워한다는 뜻입니다.",
    "example_words": [
      { "word": "思い出す", "reading": "おもいだす", "meaning": "생각해내다", "description": "생각(思い)을 바깥으로 꺼내는(出す) 것, 즉 기억을 떠올리는 일입니다." },
      { "word": "思考", "reading": "しこう", "meaning": "사고", "description": "생각(思)하고 이치에 맞게 헤아리는(考) 것입니다." }
    ]
  },
  {
    "kanji": "紙",
    "reading_on": "シ",
    "reading_kun": "かみ",
    "meaning": "종이",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실, 섬유 등 재료를 의미합니다." },
      { "char": "氏", "role": "성씨 씨 (요소)", "desc": "발음 '지/시'를 나타내며, 평평하다는 의미를 가집니다." }
    ],
    "story": "섬유(糸)를 곱게 짓이겨 평평하게(氏) 펴서 만든 '종이'를 뜻하는 한자입니다.",
    "example_words": [
      { "word": "手紙", "reading": "てがみ", "meaning": "편지", "description": "손(手)으로 종이(紙)에 쓴 글, 즉 편지입니다." },
      { "word": "折り紙", "reading": "おりがみ", "meaning": "종이접기", "description": "종이(紙)를 이리저리 접는(折り) 놀이입니다." }
    ]
  },
  {
    "kanji": "寺",
    "reading_on": "ジ",
    "reading_kun": "てら",
    "meaning": "절 (사찰)",
    "components": [
      { "char": "土", "role": "흙 토 (요소)", "desc": "흙으로 쌓은 터나 땅을 의미합니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "규칙, 법도, 손을 의미합니다." }
    ],
    "story": "규칙과 법도(寸)를 엄격히 지키며 흙(土) 터 위에 세워진 관청에서 유래하여, 나중에는 불교의 '절(사찰)'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "お寺", "reading": "おてら", "meaning": "절", "description": "불교의 사원(寺)을 친근하고 정중하게 부르는 말입니다." },
      { "word": "寺院", "reading": "じいん", "meaning": "사원", "description": "절(寺)과 담장(院), 즉 종교적 건축물을 의미합니다." }
    ]
  },
  {
    "kanji": "自",
    "reading_on": "ジ、シ",
    "reading_kun": "みずか(ら)",
    "meaning": "스스로 / 자기",
    "components": [
      { "char": "自", "role": "스스로 자 (부수)", "desc": "사람의 코 모양을 본뜬 상형문자입니다." }
    ],
    "story": "사람이 자신을 가리킬 때 코를 가리키는 습관에서 유래하여 '자기 자신'이나 '스스로'라는 의미가 되었습니다.",
    "example_words": [
      { "word": "自分", "reading": "じぶん", "meaning": "자신, 나", "description": "스스로(自)의 몫(分)이나 자기 자신을 뜻합니다." },
      { "word": "自由", "reading": "じゆう", "meaning": "자유", "description": "스스로(自)를 원인(由)으로 삼아 남에게 얽매이지 않는 상태입니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade2.json'
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

print("Grade 2 Part 3.2 data appended successfully.")
