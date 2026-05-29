import json
import os

new_data = [
  {
    "kanji": "点",
    "reading_on": "テン",
    "reading_kun": "つ(く)、つ(ける)",
    "meaning": "점 / 불켜다",
    "components": [
      { "char": "占", "role": "점칠 점 (요소)", "desc": "차지하거나 점을 친다는 뜻이며, 여기서는 발음 '점/텐'을 나타냅니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불빛이나 불꽃이 점점이 타오르는 모양입니다." }
    ],
    "story": "점(占)을 치듯 불꽃(灬)을 조그맣게 켜놓은 작은 불씨에서 '점'이나 불을 '켜다'는 의미를 나타냅니다.",
    "example_words": [
      { "word": "点数", "reading": "てんすう", "meaning": "점수", "description": "평가나 시험 등에서 얻은 점(点)의 수(数)입니다." },
      { "word": "満点", "reading": "まんてん", "meaning": "만점", "description": "가득(満) 찬 점수(点)입니다." }
    ]
  },
  {
    "kanji": "電",
    "reading_on": "デン",
    "reading_kun": "",
    "meaning": "번개 / 전기",
    "components": [
      { "char": "雨", "role": "비 우 (부수)", "desc": "구름, 비 등 기상 현상을 나타냅니다." },
      { "char": "申", "role": "납 신 (요소)", "desc": "번개가 구불구불 치며 뻗어나가는 모양입니다." }
    ],
    "story": "비(雨) 구름 속에서 번개(申)가 찌릿찌릿 치는 모습에서 '번개'나 '전기'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "電車", "reading": "でんしゃ", "meaning": "전철", "description": "전기(電)의 힘으로 움직이는 차(車)입니다." },
      { "word": "電話", "reading": "でんわ", "meaning": "전화", "description": "전기(電) 신호를 통해 말(話)을 주고받는 기기입니다." }
    ]
  },
  {
    "kanji": "刀",
    "reading_on": "トウ",
    "reading_kun": "かたな",
    "meaning": "칼",
    "components": [
      { "char": "刀", "role": "칼 도 (부수)", "desc": "날이 휘어진 외날 칼의 모양을 본뜬 상형문자입니다." }
    ],
    "story": "물건을 베거나 자를 때 사용하는 휘어진 외날 '칼'의 모습을 본뜬 글자입니다.",
    "example_words": [
      { "word": "日本刀", "reading": "にほんとう", "meaning": "일본도", "description": "일본(日本) 특유의 방법으로 만든 칼(刀)입니다." },
      { "word": "短刀", "reading": "たんとう", "meaning": "단도", "description": "길이가 짧은(短) 칼(刀)입니다." }
    ]
  },
  {
    "kanji": "冬",
    "reading_on": "トウ",
    "reading_kun": "ふゆ",
    "meaning": "겨울",
    "components": [
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "여기서는 실의 끝이나 마지막을 뜻합니다." },
      { "char": "冫", "role": "이수변 (부수)", "desc": "얼음이나 차가운 기운을 나타냅니다." }
    ],
    "story": "한 해의 마지막(夂) 즈음에 얼음(冫)이 얼어붙는 가장 춥고 차가운 계절인 '겨울'을 뜻합니다.",
    "example_words": [
      { "word": "冬休み", "reading": "ふゆやすみ", "meaning": "겨울방학", "description": "겨울(冬)에 쉬는(休み) 기간입니다." },
      { "word": "春夏秋冬", "reading": "しゅんかしゅうとう", "meaning": "춘하추동 (사계절)", "description": "봄, 여름, 가을, 겨울 네 계절입니다." }
    ]
  },
  {
    "kanji": "当",
    "reading_on": "トウ",
    "reading_kun": "あ(たる)、あ(てる)",
    "meaning": "마땅 / 맞다",
    "components": [
      { "char": "小", "role": "작을 소 (부수)", "desc": "여기서는 신에게 바치는 물건이나 위쪽을 덮는 덮개의 간략형입니다." },
      { "char": "ヨ", "role": "돼지머리 계 (요소)", "desc": "손으로 덮거나 밭(田)의 변형으로, 가치가 상응하는 무언가를 뜻합니다." }
    ],
    "story": "원래 두 개의 물건이 그 가치나 무게가 서로 똑같이 '맞다' 혹은 '마땅하다'는 뜻을 가졌으며, 과녁에 딱 '적중하다'는 뜻으로도 쓰입니다.",
    "example_words": [
      { "word": "本当", "reading": "ほんとう", "meaning": "정말, 사실", "description": "근본적(本)으로 마땅하고(当) 틀림없는 사실이라는 뜻입니다." },
      { "word": "当たる", "reading": "あたる", "meaning": "맞다, 적중하다", "description": "과녁이나 목적하는 바에 들어맞는(当) 것을 뜻합니다." }
    ]
  },
  {
    "kanji": "東",
    "reading_on": "トウ",
    "reading_kun": "ひがし",
    "meaning": "동녘 (동쪽)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "日", "role": "날 일 (요소)", "desc": "태양입니다." }
    ],
    "story": "나무(木)들 사이로 해(日)가 막 떠오르는 방향, 즉 해가 뜨는 '동쪽'을 의미합니다.",
    "example_words": [
      { "word": "東京", "reading": "とうきょう", "meaning": "도쿄", "description": "동쪽(東)의 수도(京)라는 뜻입니다." },
      { "word": "東西", "reading": "とうざい", "meaning": "동서", "description": "동쪽(東)과 서쪽(西)입니다." }
    ]
  },
  {
    "kanji": "答",
    "reading_on": "トウ",
    "reading_kun": "こた(える)、こた(え)",
    "meaning": "대답",
    "components": [
      { "char": "竹", "role": "대 죽 (부수)", "desc": "대나무나 대나무로 만든 관(피리)을 뜻합니다." },
      { "char": "合", "role": "합할 합 (요소)", "desc": "딱 맞다, 일치하다는 뜻입니다." }
    ],
    "story": "상대방의 말이나 질문에 딱 들어맞게(合) 대나무 피리(竹)로 화답하여 '대답'하거나 '답'을 맞춘다는 뜻입니다.",
    "example_words": [
      { "word": "答え", "reading": "こたえ", "meaning": "대답, 정답", "description": "질문이나 문제에 대해 내놓는 답(答)입니다." },
      { "word": "解答", "reading": "かいとう", "meaning": "해답", "description": "문제를 풀어서(解) 답(答)을 냄." }
    ]
  },
  {
    "kanji": "頭",
    "reading_on": "トウ、ズ、ト",
    "reading_kun": "あたま",
    "meaning": "머리",
    "components": [
      { "char": "豆", "role": "콩 두 (요소)", "desc": "제기(그릇)의 모양이며, 둥글고 볼록한 모양을 뜻하고 '두/토우' 발음을 담당합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "사람의 머리와 얼굴을 뜻합니다." }
    ],
    "story": "사람의 둥글고 볼록한(豆) 머리통 부분(頁)으로, 짐승이나 사람의 으뜸이 되는 '머리'를 의미합니다.",
    "example_words": [
      { "word": "頭痛", "reading": "ずつう", "meaning": "두통", "description": "머리(頭)가 아픈(痛) 것입니다." },
      { "word": "先頭", "reading": "せんとう", "meaning": "선두", "description": "맨 앞(先)의 머리(頭)가 되는 자리입니다." }
    ]
  },
  {
    "kanji": "同",
    "reading_on": "ドウ",
    "reading_kun": "おな(じ)",
    "meaning": "한가지 / 같다",
    "components": [
      { "char": "冂", "role": "멀 경 (요소)", "desc": "공간이나 범위를 덮는 모양입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "하나, 혹은 한마음입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입에서 나오는 목소리나 사람을 뜻합니다." }
    ],
    "story": "한 공간(冂)에 모인 사람들의 입(口)에서 하나(一)로 모아진 똑같은 목소리가 나온다는 데서 서로 '같다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "同じ", "reading": "おなじ", "meaning": "같다", "description": "성질이나 상태가 서로 똑같은 것입니다." },
      { "word": "同時", "reading": "どうじ", "meaning": "동시", "description": "같은(同) 시간(時)을 의미합니다." }
    ]
  },
  {
    "kanji": "道",
    "reading_on": "ドウ",
    "reading_kun": "みち",
    "meaning": "길 / 도리",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "나아가다, 길을 가다는 뜻입니다." },
      { "char": "首", "role": "머리 수 (요소)", "desc": "머리, 또는 우두머리라는 뜻으로, 이끌어가는 가장 중요한 방향을 나타냅니다." }
    ],
    "story": "머리(首)가 향하는 대로 발을 내딛고 걸어가는(辶) '길'이나, 사람으로서 마땅히 가야 할 '도리'를 의미합니다.",
    "example_words": [
      { "word": "道路", "reading": "どうろ", "meaning": "도로", "description": "길(道)과 길(路)로, 사람이나 차가 다니는 길입니다." },
      { "word": "水道", "reading": "すいどう", "meaning": "수도", "description": "물(水)이 지나가는 길(道)입니다." }
    ]
  },
  {
    "kanji": "読",
    "reading_on": "ドク、トク",
    "reading_kun": "よ(む)",
    "meaning": "읽다",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 언어를 뜻합니다." },
      { "char": "売", "role": "팔 매 (요소)", "desc": "원래는 발음 '독'을 나타내는 글자였으나 간략화되어 팔 매 자가 되었습니다. 뜻을 하나하나 풀이한다는 의미를 담고 있습니다." }
    ],
    "story": "책에 쓰인 말(言)의 의미를 하나하나 소리 내어 풀이하며 눈으로 훑어 '읽다'라는 뜻을 지닙니다.",
    "example_words": [
      { "word": "読書", "reading": "どくしょ", "meaning": "독서", "description": "책(書)을 읽는(読) 일입니다." },
      { "word": "読み方", "reading": "よみかた", "meaning": "읽는 법", "description": "글자를 읽는(読み) 방법(方)입니다." }
    ]
  },
  {
    "kanji": "内",
    "reading_on": "ナイ、ダイ",
    "reading_kun": "うち",
    "meaning": "안 (내부)",
    "components": [
      { "char": "冂", "role": "멀 경 (요소)", "desc": "건물이나 공간의 바깥 테두리입니다." },
      { "char": "人", "role": "들 입 (부수)", "desc": "안으로 들어간다는 뜻의 입(入)이 변형된 형태입니다." }
    ],
    "story": "어떤 테두리나 집(冂)의 문을 통해 안쪽으로 들어가는(入) 모양에서 건물이나 범위의 '안쪽'을 뜻합니다.",
    "example_words": [
      { "word": "内容", "reading": "ないよう", "meaning": "내용", "description": "안(内)에 담긴(容) 뜻거리입니다." },
      { "word": "案内", "reading": "あんない", "meaning": "안내", "description": "자세한 안쪽(内) 사정을 살펴(案) 이끌어 주는 것입니다." }
    ]
  },
  {
    "kanji": "南",
    "reading_on": "ナン、ナ",
    "reading_kun": "みなみ",
    "meaning": "남녘 (남쪽)",
    "components": [
      { "char": "十", "role": "열 십 (부수)", "desc": "초목이 자라는 모양이나 덮개를 뜻합니다." },
      { "char": "冂", "role": "멀 경 (요소)", "desc": "공간을 두르는 테두리입니다." },
      { "char": "￥", "role": "양 양 (요소)", "desc": "따뜻한 기운이나 양(羊)의 뿔 모양의 변형입니다." }
    ],
    "story": "초목(十)을 따뜻한 온실(冂) 안에 가두어 기르는 풍요롭고 따뜻한 방향인 '남쪽'을 뜻하는 글자입니다.",
    "example_words": [
      { "word": "南口", "reading": "みなみぐち", "meaning": "남쪽 출구", "description": "남쪽(南)에 있는 출입구(口)입니다." },
      { "word": "南北", "reading": "なんぼく", "meaning": "남북", "description": "남쪽(南)과 북쪽(北)입니다." }
    ]
  },
  {
    "kanji": "肉",
    "reading_on": "ニク",
    "reading_kun": "",
    "meaning": "고기",
    "components": [
      { "char": "肉", "role": "고기 육 (부수)", "desc": "도마 위에 칼집을 낸 짐승의 살코기 모양을 본뜬 상형문자입니다." }
    ],
    "story": "동물의 살코기에 마블링 무늬나 힘줄이 그어져 있는 먹음직스러운 '고기' 덩어리의 모습을 나타냅니다.",
    "example_words": [
      { "word": "牛肉", "reading": "ぎゅうにく", "meaning": "쇠고기", "description": "소(牛)의 고기(肉)입니다." },
      { "word": "筋肉", "reading": "きんにく", "meaning": "근육", "description": "몸을 움직이는 힘줄(筋)과 살코기(肉)입니다." }
    ]
  },
  {
    "kanji": "馬",
    "reading_on": "バ",
    "reading_kun": "うま",
    "meaning": "말",
    "components": [
      { "char": "馬", "role": "말 마 (부수)", "desc": "갈기와 꼬리가 날리는 튼튼한 말의 모습을 본뜬 글자입니다." }
    ],
    "story": "바람을 가르며 달리는 긴 얼굴과 갈기, 그리고 다리와 꼬리(灬)를 가진 날쌘 '말'의 모양을 본떴습니다.",
    "example_words": [
      { "word": "乗馬", "reading": "じょうば", "meaning": "승마", "description": "말(馬)에 올라타는(乗) 것입니다." },
      { "word": "馬鹿", "reading": "ばか", "meaning": "바보", "description": "말(馬)과 사슴(鹿)을 구별 못할 정도로 어리석음을 뜻하는 관용어입니다." }
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

print("Grade 2 Part 5.2 data appended successfully.")
