import json
import os

new_data = [
  {
    "kanji": "引",
    "reading_on": "イン",
    "reading_kun": "ひ(く)、ひ(ける)",
    "meaning": "끌다",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "활의 모양을 본뜬 부수입니다." },
      { "char": "丨", "role": "뚫을 곤 (요소)", "desc": "활시위를 길게 당기는 모습을 선으로 나타냈습니다." }
    ],
    "story": "활(弓)의 시위를 팽팽하게 당겨서(丨) '끌어당기다'라는 의미를 만든 한자입니다.",
    "example_words": [
      { "word": "引力", "reading": "いんりょく", "meaning": "인력", "description": "물체가 서로 끌어당기는(引) 힘(力)을 말합니다." },
      { "word": "割引", "reading": "わりびき", "meaning": "할인", "description": "비율을 나누어(割) 가격을 깎아주는(引) 것을 의미합니다." }
    ]
  },
  {
    "kanji": "羽",
    "reading_on": "ウ",
    "reading_kun": "は、はね",
    "meaning": "깃털",
    "components": [
      { "char": "羽", "role": "깃 우 (부수)", "desc": "새의 양쪽 날개와 깃털 모양을 본뜬 상형문자입니다." }
    ],
    "story": "새의 양쪽 날개에 달린 깃털(羽)의 모습을 본떠 만든 한자로, 깃털이나 날개를 의미합니다. 그 자체로 부수이자 기본 한자입니다.",
    "example_words": [
      { "word": "羽毛", "reading": "うもう", "meaning": "우모 (깃털)", "description": "새의 깃털(羽)과 털(毛)을 합쳐 푹신한 새의 털을 의미합니다." },
      { "word": "白羽", "reading": "しらは", "meaning": "흰 깃털", "description": "하얀(白) 깃털(羽)을 의미하며, '백하의 화살이 꽂히다(지목되다)'라는 관용구에 쓰입니다." }
    ]
  },
  {
    "kanji": "雲",
    "reading_on": "ウン",
    "reading_kun": "くも",
    "meaning": "구름",
    "components": [
      { "char": "雨", "role": "비 우 (부수)", "desc": "하늘에서 비가 내리는 모양으로, 날씨나 기상과 관련된 한자에 쓰입니다." },
      { "char": "云", "role": "이를 운 (요소)", "desc": "구름이 뭉게뭉게 피어오르는 모양이자, '운'이라는 발음을 담당합니다." }
    ],
    "story": "하늘에서 비(雨)를 내리게 하는 뭉게뭉게 피어오르는 수증기(云)인 '구름'을 뜻하는 한자입니다.",
    "example_words": [
      { "word": "暗雲", "reading": "あんうん", "meaning": "암운 (먹구름)", "description": "어두운(暗) 구름(雲)이라는 뜻으로, 불길한 징조를 비유합니다." },
      { "word": "雨雲", "reading": "あまぐも", "meaning": "비구름", "description": "비(雨)를 머금고 있는 구름(雲)을 말합니다." }
    ]
  },
  {
    "kanji": "園",
    "reading_on": "エン",
    "reading_kun": "その",
    "meaning": "동산",
    "components": [
      { "char": "囗", "role": "에운담 구 (부수)", "desc": "울타리를 둘러쳐서 영역을 표시하는 모양입니다." },
      { "char": "袁", "role": "옷길 원 (요소)", "desc": "옷이 넉넉하다는 뜻이며, 여기서는 '원'이라는 발음과 함께 넓은 공간을 의미합니다." }
    ],
    "story": "울타리(囗)를 넓게(袁) 둘러쳐서 과일이나 꽃을 가꾸는 정원이나 '동산'을 의미하는 한자입니다.",
    "example_words": [
      { "word": "公園", "reading": "こうえん", "meaning": "공원", "description": "공공(公)을 위해 만들어진 넓은 동산(園)입니다." },
      { "word": "動物園", "reading": "どうぶつえん", "meaning": "동물원", "description": "동물(動物)들을 모아 놓고 기르며 보여주는 동산(園)입니다." }
    ]
  },
  {
    "kanji": "遠",
    "reading_on": "エン",
    "reading_kun": "とお(い)",
    "meaning": "멀다",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아가는 것, 이동과 관련된 의미를 더합니다." },
      { "char": "袁", "role": "옷길 원 (요소)", "desc": "크고 넓다는 의미와 함께 '원'이라는 발음을 나타냅니다." }
    ],
    "story": "길을 걸어서(辶) 가야 할 거리가 아주 길고 넓다(袁)는 뜻에서 거리가 '멀다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "永遠", "reading": "えいえん", "meaning": "영원", "description": "끝없이 길고(永) 먼(遠) 시간을 뜻합니다." },
      { "word": "遠慮", "reading": "えんりょ", "meaning": "사양, 조심", "description": "멀리(遠) 앞날까지 생각한다(慮)는 뜻에서, 조심하거나 사양하는 태도를 의미합니다." }
    ]
  },
  {
    "kanji": "何",
    "reading_on": "カ",
    "reading_kun": "なに、なん",
    "meaning": "무엇",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 나타내는 부수입니다." },
      { "char": "可", "role": "옳을 가 (요소)", "desc": "입에서 소리를 내어 허락하거나 따지는 모습을 나타냅니다." }
    ],
    "story": "사람(亻)이 입술을 벌리고 소리쳐(可) 상대를 향해 '무엇이냐?'고 꾸짖거나 묻는 상황에서 유래하여 '무엇'이라는 의문사가 되었습니다.",
    "example_words": [
      { "word": "何か", "reading": "なにか", "meaning": "무언가", "description": "무엇(何)인가 어떤 것을 막연히 가리킬 때 씁니다." },
      { "word": "幾何学", "reading": "きかがく", "meaning": "기하학", "description": "도형이나 공간의 성질을 연구하는 학문입니다. ('얼마나'를 뜻하는 한자어에서 유래)" }
    ]
  },
  {
    "kanji": "科",
    "reading_on": "カ",
    "reading_kun": "",
    "meaning": "과목",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 벼를 나타냅니다." },
      { "char": "斗", "role": "말 두 (요소)", "desc": "곡식의 양을 재는 국자 모양의 도구를 뜻합니다." }
    ],
    "story": "수확한 벼(禾)의 양을 도구(斗)로 되어서 질과 양에 따라 등급을 나눈다는 데서, 품목을 분류하는 '과목'이나 '부서'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "科学", "reading": "かがく", "meaning": "과학", "description": "체계적으로 분류된(科) 학문(学)을 의미합니다." },
      { "word": "教科書", "reading": "きょうかしょ", "meaning": "교과서", "description": "가르치는(教) 과목(科)의 내용을 담은 책(書)입니다." }
    ]
  },
  {
    "kanji": "夏",
    "reading_on": "カ、ゲ",
    "reading_kun": "なつ",
    "meaning": "여름",
    "components": [
      { "char": "頁", "role": "머리 혈 (변형)", "desc": "머리나 얼굴을 의미하는 부수(의 변형)입니다." },
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "발을 끌며 천천히 걷는 모습, 춤추는 사람의 발을 의미합니다." }
    ],
    "story": "화려한 탈을 쓴 사람(頁의 변형)이 발(夂)을 굴리며 풍년을 기원하는 제사에서 춤을 추는 계절인 '여름'을 뜻합니다.",
    "example_words": [
      { "word": "真夏", "reading": "まなつ", "meaning": "한여름", "description": "진짜(真) 여름(夏)이라는 뜻으로 가장 더운 한창때의 여름을 말합니다." },
      { "word": "春夏秋冬", "reading": "しゅんかしゅうとう", "meaning": "춘하추동", "description": "봄, 여름, 가을, 겨울의 사계절을 말합니다." }
    ]
  },
  {
    "kanji": "家",
    "reading_on": "カ、ケ",
    "reading_kun": "いえ、や",
    "meaning": "집",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕을 본뜬 모양으로, 집이나 건물을 뜻합니다." },
      { "char": "豕", "role": "돼지 시 (요소)", "desc": "돼지의 모양을 본뜬 한자입니다." }
    ],
    "story": "지붕(宀) 아래에서 돼지(豕)를 기르던 고대 중국의 가옥 형태에서 유래하여 사람이 사는 '집'이나 '가족'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "家族", "reading": "かぞく", "meaning": "가족", "description": "한 집(家)에서 사는 무리(族)를 의미합니다." },
      { "word": "作家", "reading": "さっか", "meaning": "작가", "description": "작품을 만드는(作) 것을 전문으로 하는 사람(家)을 의미합니다." }
    ]
  },
  {
    "kanji": "歌",
    "reading_on": "カ",
    "reading_kun": "うた、うた(う)",
    "meaning": "노래",
    "components": [
      { "char": "哥", "role": "노래 가 (요소)", "desc": "입(口)에서 숨을 길게 내쉬며 노래하는 뜻을 담고 있습니다." },
      { "char": "欠", "role": "하품 흠 (부수)", "desc": "사람이 입을 크게 벌려 숨을 내쉬는 모습을 뜻합니다." }
    ],
    "story": "입을 벌리고 소리(哥)를 내며, 숨을 크게 들이마시고 내쉬면서(欠) '노래'를 부르는 모습을 표현한 한자입니다.",
    "example_words": [
      { "word": "歌手", "reading": "かしゅ", "meaning": "가수", "description": "노래(歌) 부르는 것을 직업으로 삼는 사람(手)을 말합니다." },
      { "word": "校歌", "reading": "こうか", "meaning": "교가", "description": "학교(校)를 상징하는 노래(歌)입니다." }
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

print("Grade 2 Part 1 data appended successfully.")
