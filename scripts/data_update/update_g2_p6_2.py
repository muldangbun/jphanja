import json
import os

new_data = [
  {
    "kanji": "妹",
    "reading_on": "マイ",
    "reading_kun": "いもうと",
    "meaning": "누이동생",
    "components": [
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." },
      { "char": "未", "role": "아닐 미 (요소)", "desc": "아직 다 자라지 않았다는 뜻으로 '미/마이' 발음을 나타냅니다." }
    ],
    "story": "아직 어리고(未) 다 자라지 않은 여자(女) 아이, 즉 '여동생'을 뜻합니다.",
    "example_words": [
      { "word": "姉妹", "reading": "しまい", "meaning": "자매", "description": "언니(姉)와 여동생(妹)입니다." },
      { "word": "妹さん", "reading": "いもうとさん", "meaning": "여동생", "description": "남의 여동생을 정중하게 부르는 말입니다." }
    ]
  },
  {
    "kanji": "万",
    "reading_on": "マン、バン",
    "reading_kun": "",
    "meaning": "일만",
    "components": [
      { "char": "一", "role": "한 일 (부수)", "desc": "숫자나 선을 의미합니다." },
      { "char": "万", "role": "일만 만 (부수)", "desc": "본래 卍(만자)나 여러 다리가 달린 벌레(전갈) 모양에서 왔으나, 나중에 숫자 10,000을 뜻하게 되었습니다." }
    ],
    "story": "전갈처럼 다리가 아주 많다는 데서 유래하여, 숫자가 끝없이 많다는 뜻인 '10,000'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "一万", "reading": "いちまん", "meaning": "일만 (10,000)", "description": "숫자 만입니다." },
      { "word": "万歳", "reading": "ばんざい", "meaning": "만세", "description": "만(万) 년(歳)토록 오래오래 살거나 번영하라는 축하의 말입니다." }
    ]
  },
  {
    "kanji": "明",
    "reading_on": "メイ、ミョウ",
    "reading_kun": "あか(るい)",
    "meaning": "밝다",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "밝은 해(태양)입니다." },
      { "char": "月", "role": "달 월 (요소)", "desc": "밤을 밝히는 달입니다." }
    ],
    "story": "하늘의 밝은 해(日)와 달(月)이 함께 있으니, 그 빛이 매우 '밝다'는 뜻입니다.",
    "example_words": [
      { "word": "明るい", "reading": "あかるい", "meaning": "밝다", "description": "빛이 많거나 성격이 쾌활하다는 뜻입니다." },
      { "word": "明日", "reading": "あした", "meaning": "내일", "description": "밝아오는(明) 다음 날(日)입니다." }
    ]
  },
  {
    "kanji": "鳴",
    "reading_on": "メイ",
    "reading_kun": "な(く)、な(る)",
    "meaning": "울다",
    "components": [
      { "char": "口", "role": "입 구 (요소)", "desc": "입이나 소리를 내는 부위입니다." },
      { "char": "鳥", "role": "새 조 (부수)", "desc": "새를 뜻합니다." }
    ],
    "story": "새(鳥)가 부리(口)를 벌려 짹짹 소리 내어 '울다' 혹은 사물이 소리를 '내다(울리다)'라는 뜻입니다.",
    "example_words": [
      { "word": "鳴く", "reading": "なく", "meaning": "울다", "description": "동물이나 새가 소리를 내어 우는 것입니다." },
      { "word": "悲鳴", "reading": "ひめい", "meaning": "비명", "description": "슬프고(悲) 괴롭게 울부짖는(鳴) 소리입니다." }
    ]
  },
  {
    "kanji": "毛",
    "reading_on": "モウ",
    "reading_kun": "け",
    "meaning": "털",
    "components": [
      { "char": "毛", "role": "털 모 (부수)", "desc": "짐승이나 사람의 몸에 난 털이 구부러져 있는 모습을 본뜬 상형문자입니다." }
    ],
    "story": "구불구불하게 자라난 짐승의 꼬리털이나 사람의 털 모양을 본떠 '털'을 의미합니다.",
    "example_words": [
      { "word": "髪の毛", "reading": "かみのけ", "meaning": "머리카락", "description": "머리(髪)에 난 털(毛)입니다." },
      { "word": "毛布", "reading": "もうふ", "meaning": "담요", "description": "짐승의 털(毛)로 짠 덮개나 천(布)입니다." }
    ]
  },
  {
    "kanji": "門",
    "reading_on": "モン",
    "reading_kun": "かど",
    "meaning": "문",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "양쪽으로 열고 닫는 커다란 두 짝의 문 모양을 본뜬 상형문자입니다." }
    ],
    "story": "좌우 양쪽으로 활짝 열고 닫는 기둥이 있는 큰 대'문'을 본뜬 글자입니다.",
    "example_words": [
      { "word": "門限", "reading": "もんげん", "meaning": "문단속 시간, 통금", "description": "문(門)을 닫고 제한하는(限) 시간입니다." },
      { "word": "正門", "reading": "せいもん", "meaning": "정문", "description": "건물의 올바른(正) 정면 출입구(門)입니다." }
    ]
  },
  {
    "kanji": "野",
    "reading_on": "ヤ",
    "reading_kun": "の",
    "meaning": "들 / 들판",
    "components": [
      { "char": "里", "role": "마을 리 (부수)", "desc": "사람들이 모여 사는 마을이나 거리를 뜻합니다." },
      { "char": "予", "role": "나 여 (요소)", "desc": "여기서는 베틀의 씨줄이 교차하는 모양, 길게 뻗어 있다는 뜻의 '서/여' 발음을 줍니다." }
    ],
    "story": "사람이 사는 마을(里) 바깥으로 시야가 길게 뻗어(予) 탁 트인 넓은 '들판'을 의미합니다.",
    "example_words": [
      { "word": "野原", "reading": "のはら", "meaning": "들판", "description": "넓게 펼쳐진 들(野)과 평원(原)입니다." },
      { "word": "野球", "reading": "やきゅう", "meaning": "야구", "description": "들판(野)처럼 넓은 곳에서 공(球)을 치는 스포츠입니다." }
    ]
  },
  {
    "kanji": "夜",
    "reading_on": "ヤ",
    "reading_kun": "よる、よ",
    "meaning": "밤",
    "components": [
      { "char": "亠", "role": "돼지해머리 (부수)", "desc": "사람의 머리나 위를 덮은 모양입니다." },
      { "char": "亻", "role": "사람 인 (요소)", "desc": "사람입니다." },
      { "char": "夕", "role": "저녁 석 (요소)", "desc": "해가 지고 달이 뜬 저녁입니다." }
    ],
    "story": "어두운 저녁(夕)이 되어 사람이 겨드랑이(달의 변형)를 모으고 잠자리에 누워 쉬는 '밤'을 의미합니다.",
    "example_words": [
      { "word": "夜中", "reading": "よなか", "meaning": "한밤중", "description": "밤(夜)의 깊은 중간(中) 시간입니다." },
      { "word": "今夜", "reading": "こんや", "meaning": "오늘 밤", "description": "지금(今) 맞이하는 밤(夜)입니다." }
    ]
  },
  {
    "kanji": "友",
    "reading_on": "ユウ",
    "reading_kun": "とも",
    "meaning": "벗 / 친구",
    "components": [
      { "char": "𠂇", "role": "왼손 좌 (요소)", "desc": "왼손을 뜻합니다." },
      { "char": "又", "role": "또 우 (부수)", "desc": "오른손을 뜻합니다." }
    ],
    "story": "두 사람이 나란히 서서 서로의 왼손(𠂇)과 오른손(又)을 맞잡고 돕는 다정한 '친구'나 '벗'을 의미합니다.",
    "example_words": [
      { "word": "友達", "reading": "ともだち", "meaning": "친구", "description": "친한 벗(友)들의 복수형이나 친구 자체를 뜻합니다." },
      { "word": "親友", "reading": "しんゆう", "meaning": "친한 친구, 절친", "description": "아주 가깝고 친한(親) 벗(友)입니다." }
    ]
  },
  {
    "kanji": "用",
    "reading_on": "ヨウ",
    "reading_kun": "もち(いる)",
    "meaning": "쓸 / 볼일",
    "components": [
      { "char": "用", "role": "쓸 용 (부수)", "desc": "물건을 꿰뚫은 막대기나, 우물가에 걸어둔 두레박 등 실용적인 도구를 본뜬 상형문자입니다." }
    ],
    "story": "생활에 편리하게 '쓰는' 도구의 모습에서 유래하여 무언가를 '사용하다' 혹은 처리해야 할 '볼일'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "用事", "reading": "ようじ", "meaning": "볼일, 용건", "description": "처리해야 할 쓰임새(用)가 있는 일(事)입니다." },
      { "word": "用意", "reading": "ようい", "meaning": "준비", "description": "쓸(用) 것에 대비하여 마음(意)을 먹고 미리 갖추는 것입니다." }
    ]
  },
  {
    "kanji": "曜",
    "reading_on": "ヨウ",
    "reading_kun": "",
    "meaning": "빛날 / 요일",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 별 같은 천체를 의미합니다." },
      { "char": "翟", "role": "꿩 적 (요소)", "desc": "깃털이 화려한 새(꿩)가 날개를 푸드덕거리며 빛나는 모습을 뜻합니다." }
    ],
    "story": "해나 달, 그리고 오행성(수성, 금성, 화성, 목성, 토성)이 화려한 깃털(翟)처럼 맑고 밝게 '빛나는' 천체들의 운행 주기를 뜻하여 '요일'이 되었습니다.",
    "example_words": [
      { "word": "日曜日", "reading": "にちようび", "meaning": "일요일", "description": "해(日)를 상징하는 요일(曜)입니다." },
      { "word": "曜日", "reading": "ようび", "meaning": "요일", "description": "빛나는 천체의 주기에 따른 요일입니다." }
    ]
  },
  {
    "kanji": "来",
    "reading_on": "ライ",
    "reading_kun": "く(る)",
    "meaning": "오다",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "본래 나무가 아니라 보리(麥)의 까끄라기를 뜻하는 글자의 간략화된 형태입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "보리의 이삭을 표시합니다." }
    ],
    "story": "옛날 사람들은 주식이 되는 보리가 하늘에서 내려왔다고 믿어, 보리를 뜻하던 글자가 멀리서 무언가가 '오다'라는 뜻으로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "来る", "reading": "くる", "meaning": "오다", "description": "이쪽으로 이동해 오는 것입니다." },
      { "word": "来週", "reading": "らいしゅう", "meaning": "다음 주", "description": "앞으로 다가올(来) 주(週)입니다." }
    ]
  },
  {
    "kanji": "里",
    "reading_on": "リ",
    "reading_kun": "さと",
    "meaning": "마을",
    "components": [
      { "char": "田", "role": "밭 전 (요소)", "desc": "농사를 짓는 밭이나 농경지입니다." },
      { "char": "土", "role": "흙 토 (요소)", "desc": "토지나 땅을 뜻합니다." }
    ],
    "story": "농사를 짓는 밭(田)과 집을 짓고 살 수 있는 흙(土) 토지가 어우러진 곳, 즉 사람들이 모여 사는 '마을'을 의미합니다.",
    "example_words": [
      { "word": "里帰り", "reading": "さとがえり", "meaning": "고향에 다녀옴", "description": "고향 마을(里)로 돌아가는(帰り) 것입니다." },
      { "word": "古里", "reading": "ふるさと", "meaning": "고향", "description": "오래되고 낡은(古) 마을(里), 즉 자기가 태어난 고향입니다." }
    ]
  },
  {
    "kanji": "理",
    "reading_on": "リ",
    "reading_kun": "",
    "meaning": "다스릴 / 이치",
    "components": [
      { "char": "王", "role": "구슬 옥 (부수)", "desc": "원래 玉(구슬 옥)이 변형된 것으로 옥석을 의미합니다." },
      { "char": "里", "role": "마을 리 (요소)", "desc": "밭과 땅의 무늬나 결을 나타내며 발음 '리'를 담당합니다." }
    ],
    "story": "옥돌(玉)의 아름다운 결(里)에 따라 매끄럽게 다듬어 옥을 '다스리다'는 뜻이었으며, 나중에 사물의 마땅한 결인 '이치'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "理由", "reading": "りゆう", "meaning": "이유", "description": "어떤 일이 일어나게 된 이치(理)와 까닭(由)입니다." },
      { "word": "料理", "reading": "りょうり", "meaning": "요리", "description": "재료를 헤아려(料) 이치에 맞게 잘 다스려(理) 음식을 만드는 일입니다." }
    ]
  },
  {
    "kanji": "話",
    "reading_on": "ワ",
    "reading_kun": "はな(す)、はなし",
    "meaning": "말씀 / 이야기",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하는 것을 뜻합니다." },
      { "char": "舌", "role": "혀 설 (요소)", "desc": "입안에 있는 혀로, 혀를 굴려 말을 한다는 뜻입니다. 발음 '괄/와'에서 왔습니다." }
    ],
    "story": "말(言)을 할 때 혀(舌)를 유창하게 굴려서 길고 재미있게 이어 나가는 '이야기'나 '말'을 뜻합니다.",
    "example_words": [
      { "word": "話す", "reading": "はなす", "meaning": "말하다, 이야기하다", "description": "말을 소리 내어 하는 것입니다." },
      { "word": "電話", "reading": "でんわ", "meaning": "전화", "description": "전기(電) 신호를 통해 이야기(話)를 나누는 기계입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade2.json'
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

print("Grade 2 Part 6.2 data appended successfully.")
