import json
import os

new_data = [
  {
    "kanji": "親",
    "reading_on": "シン",
    "reading_kun": "おや、した(しい)、した(しむ)",
    "meaning": "어버이 / 친하다",
    "components": [
      { "char": "立", "role": "설 립 (요소)", "desc": "사람이 똑바로 서 있는 모습입니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "땅에 심어진 나무를 뜻합니다." },
      { "char": "見", "role": "볼 견 (부수)", "desc": "눈을 크게 뜨고 살펴보는 것을 의미합니다." }
    ],
    "story": "자식을 기다리는 부모가 나무(木) 위에 높이 서서(立) 멀리까지 자식이 오는지를 애타게 바라보는(見) 모습에서 '어버이'나 깊이 '친하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "両親", "reading": "りょうしん", "meaning": "양친, 부모님", "description": "양쪽(両)의 어버이(親)를 뜻합니다." },
      { "word": "親友", "reading": "しんゆう", "meaning": "친한 친구", "description": "아주 친한(親) 벗(友)을 말합니다." }
    ]
  },
  {
    "kanji": "図",
    "reading_on": "ズ、ト",
    "reading_kun": "はか(る)",
    "meaning": "그림 / 도모하다",
    "components": [
      { "char": "囗", "role": "에운담 구 (부수)", "desc": "사방을 두른 경계나 구역을 나타냅니다." },
      { "char": "乂", "role": "벨 예 (요소)", "desc": "가위표, 선이 서로 교차하는 모양(본래 형태에서 간략화됨)입니다." },
      { "char": "丶", "role": "점 주 (요소)", "desc": "특정 위치나 지점을 표시합니다." }
    ],
    "story": "일정한 구역(囗) 안에 교차하는 선(乂)과 점(丶)을 그려 넣어 토지나 지역을 표시한 '그림(지도)'이나 그것을 보고 '계획하다'라는 뜻입니다.",
    "example_words": [
      { "word": "地図", "reading": "ちず", "meaning": "지도", "description": "땅(地)의 경계를 표시한 그림(図)입니다." },
      { "word": "図書館", "reading": "としょかん", "meaning": "도서관", "description": "그림(図)과 책(書)을 모아둔 건물(館)입니다." }
    ]
  },
  {
    "kanji": "数",
    "reading_on": "スウ、ス",
    "reading_kun": "かず、かぞ(える)",
    "meaning": "수 / 셀 수",
    "components": [
      { "char": "婁", "role": "별이름 루 (요소)", "desc": "여자가 머리에 물건을 이고 있는 모습으로, 여러 개가 겹쳐진 형태를 뜻합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손에 막대기를 들고 가볍게 치며 독려하는 모습입니다." }
    ],
    "story": "막대기(攵)를 들고 여러 개 겹쳐 있는 짐이나 물건(婁)들의 개수를 일일이 세어 확인하는 모습에서 '수'나 '세다'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "数字", "reading": "すうじ", "meaning": "숫자", "description": "수(数)를 나타내는 글자(字)입니다." },
      { "word": "算数", "reading": "さんすう", "meaning": "산수", "description": "수(数)를 계산(算)하는 학문입니다." }
    ]
  },
  {
    "kanji": "西",
    "reading_on": "セイ、サイ",
    "reading_kun": "にし",
    "meaning": "서녘 (서쪽)",
    "components": [
      { "char": "西", "role": "덮을 아 (부수)", "desc": "새가 둥지 위에 앉아 있는 모습을 본뜬 상형문자입니다." }
    ],
    "story": "해가 지는 무렵이 되면 새들이 둥지로 돌아가 쉰다는 데서, 해가 지는 방향인 '서쪽'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "西洋", "reading": "せいよう", "meaning": "서양", "description": "서쪽(西)의 큰 바다(洋) 건너에 있는 나라들입니다." },
      { "word": "東西", "reading": "とうざい", "meaning": "동서", "description": "동쪽(東)과 서쪽(西)입니다." }
    ]
  },
  {
    "kanji": "声",
    "reading_on": "セイ、ショウ",
    "reading_kun": "こえ",
    "meaning": "소리",
    "components": [
      { "char": "士", "role": "선비 사 (요소)", "desc": "돌이나 악기를 뜻하는 본래 형태에서 줄어든 모양입니다." },
      { "char": "尸", "role": "주검 시 (요소)", "desc": "귀(耳)의 형태가 간략화된 것입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "소리가 퍼져나가는 파장이나 악기를 치는 막대기를 상징합니다." }
    ],
    "story": "돌로 만든 경쇠 같은 악기(士)를 막대기(一)로 칠 때 나는 맑은 소리가 귀(尸의 원형)에 들리는, 즉 사람의 '목소리'나 물체의 '소리'를 뜻합니다.",
    "example_words": [
      { "word": "大声", "reading": "おおごえ", "meaning": "큰 소리", "description": "큰(大) 목소리(声)입니다." },
      { "word": "音声", "reading": "おんせい", "meaning": "음성", "description": "소리(音)와 사람의 목소리(声)를 통틀어 말합니다." }
    ]
  },
  {
    "kanji": "星",
    "reading_on": "セイ、ショウ",
    "reading_kun": "ほし",
    "meaning": "별",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "태양, 해, 빛나는 천체를 뜻합니다." },
      { "char": "生", "role": "날 생 (요소)", "desc": "땅에서 싹이 나는 모습이며, 여기서는 '성/세이' 발음을 나타냅니다." }
    ],
    "story": "밤하늘에 마치 만물이 돋아나듯(生) 맑은 빛(日)을 흩뿌리며 반짝이는 천체인 '별'을 의미합니다.",
    "example_words": [
      { "word": "流れ星", "reading": "ながれぼし", "meaning": "별똥별", "description": "하늘을 흘러가는(流れ) 별(星)입니다." },
      { "word": "火星", "reading": "かせい", "meaning": "화성", "description": "붉은 불(火)처럼 빛나는 별(星)인 태양계의 행성입니다." }
    ]
  },
  {
    "kanji": "晴",
    "reading_on": "セイ",
    "reading_kun": "は(れる)、は(れ)",
    "meaning": "맑다 / 개다",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "태양, 해를 뜻합니다." },
      { "char": "青", "role": "푸를 청 (요소)", "desc": "푸르고 맑은 색, 발음 '청/세이'를 나타냅니다." }
    ],
    "story": "하늘에 구름이 걷히고 해(日)가 쨍쨍하게 빛나며 푸르고(青) '맑은' 날씨를 뜻하는 한자입니다.",
    "example_words": [
      { "word": "晴れ", "reading": "はれ", "meaning": "맑음", "description": "구름 없이 맑게 갠 날씨입니다." },
      { "word": "素晴らしい", "reading": "すばらしい", "meaning": "훌륭하다, 멋지다", "description": "구름이 맑게(晴) 갠 것처럼 아주 훌륭한 상태를 뜻합니다." }
    ]
  },
  {
    "kanji": "切",
    "reading_on": "セツ、サイ",
    "reading_kun": "き(る)、き(れる)",
    "meaning": "끊을 / 베다",
    "components": [
      { "char": "七", "role": "일곱 칠 (요소)", "desc": "여기서는 발음 '칠/세츠'을 나타내며, 원래 끊는다는 의미를 가진 글자의 간략화된 형태입니다." },
      { "char": "刀", "role": "칼 도 (부수)", "desc": "물건을 베거나 자르는 칼입니다." }
    ],
    "story": "칼(刀)을 사용하여 물건을 조각조각(七)으로 '자르다' 혹은 '끊다'라는 뜻입니다.",
    "example_words": [
      { "word": "大切", "reading": "たいせつ", "meaning": "소중함", "description": "크게(大) 절실하게(切) 마음에 새기는 모양으로, 아주 중요함을 뜻합니다." },
      { "word": "切符", "reading": "きっぷ", "meaning": "표, 승차권", "description": "원래 잘라서(切) 나누어 가지던 부적(符)이나 증표에서 유래했습니다." }
    ]
  },
  {
    "kanji": "雪",
    "reading_on": "セツ",
    "reading_kun": "ゆき",
    "meaning": "눈",
    "components": [
      { "char": "雨", "role": "비 우 (부수)", "desc": "기상 현상 중 하늘에서 내리는 물을 나타냅니다." },
      { "char": "ヨ", "role": "돼지머리 계 (요소)", "desc": "본래 빗자루(彗)의 윗부분을 본뜬 것으로 쓸어낸다는 뜻을 담고 있습니다." }
    ],
    "story": "하늘에서 내리는 비(雨)가 얼어서 하얗게 쌓이면 빗자루(ヨ)로 쓸어내야 하는 '눈'을 뜻합니다.",
    "example_words": [
      { "word": "大雪", "reading": "おおゆき", "meaning": "폭설", "description": "아주 크게(大) 많이 내린 눈(雪)입니다." },
      { "word": "雪だるま", "reading": "ゆきだるま", "meaning": "눈사람", "description": "눈(雪)을 뭉쳐서 만든 달마대사 모양의 사람 인형입니다." }
    ]
  },
  {
    "kanji": "船",
    "reading_on": "セン",
    "reading_kun": "ふね、ふな",
    "meaning": "배",
    "components": [
      { "char": "舟", "role": "배 주 (부수)", "desc": "통나무를 파서 만든 작은 배의 상형문자입니다." },
      { "char": "八", "role": "여덟 팔 (요소)", "desc": "물이 양옆으로 갈라지는 모습입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "사람이나 화물이 들어가는 입구, 구멍을 뜻합니다." }
    ],
    "story": "작은 나룻배(舟)가 물을 가르며(八) 여러 사람(口)을 한꺼번에 많이 싣고 다닐 수 있는 큰 '배'를 의미합니다.",
    "example_words": [
      { "word": "船長", "reading": "せんちょう", "meaning": "선장", "description": "배(船)의 가장 높은 우두머리(長)입니다." },
      { "word": "風船", "reading": "ふうせん", "meaning": "풍선", "description": "바람(風)을 넣어 허공을 떠다니는 배(船) 같은 물건입니다." }
    ]
  },
  {
    "kanji": "線",
    "reading_on": "セン",
    "reading_kun": "",
    "meaning": "줄 / 선",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "가느다란 실이나 끈을 나타냅니다." },
      { "char": "泉", "role": "샘 천 (요소)", "desc": "물이 한줄기로 샘솟는 모습이며, 발음 '천/센'을 나타냅니다." }
    ],
    "story": "실(糸)을 물줄기(泉)처럼 길고 가늘게 늘어뜨려 연결한 '선'이나 '줄'을 뜻하는 한자입니다.",
    "example_words": [
      { "word": "新幹線", "reading": "しんかんせん", "meaning": "신칸센", "description": "새로운(新) 주요 간선(幹) 철로의 노선(線)이라는 뜻의 일본 고속철도입니다." },
      { "word": "直線", "reading": "ちょくせん", "meaning": "직선", "description": "곧게(直) 뻗은 선(線)입니다." }
    ]
  },
  {
    "kanji": "前",
    "reading_on": "ゼン",
    "reading_kun": "まえ",
    "meaning": "앞 / 전",
    "components": [
      { "char": "丷", "role": "여덟 팔 (요소)", "desc": "발이 멈춘 모습을 뜻하는 지(止)의 변형입니다." },
      { "char": "月", "role": "육달월 (요소)", "desc": "사람이나 동물의 몸(배)을 상징하는 배 주(舟)의 변형입니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "가위나 칼을 나타냅니다." }
    ],
    "story": "발(丷) 아래에 있는 고깃덩이(月)를 칼(刂)로 자르기 위해 몸 '앞'에 가져다 둔다는 데서 '앞'이나 '앞서다'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "名前", "reading": "なまえ", "meaning": "이름", "description": "그 사람을 가리키는 호칭(名)으로, 사람의 앞(前)에 세우는 간판 같은 것입니다." },
      { "word": "午前", "reading": "ごぜん", "meaning": "오전", "description": "낮(午)의 이전(前) 시간입니다." }
    ]
  },
  {
    "kanji": "組",
    "reading_on": "ソ",
    "reading_kun": "く(む)、くみ",
    "meaning": "짤 / 조(무리)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실을 뜻합니다." },
      { "char": "且", "role": "또 차 (요소)", "desc": "도마 위에 고기나 제물이 차곡차곡 쌓여 있는 모습입니다." }
    ],
    "story": "실(糸)을 차곡차곡 포개어(且) 엮어서 천이나 끈을 '짜다', 혹은 사람들을 하나로 엮어 묶은 '조(무리)'를 뜻합니다.",
    "example_words": [
      { "word": "組織", "reading": "そしき", "meaning": "조직", "description": "실을 엮어 짜듯이(組) 체계적으로 이룬(織) 무리입니다." },
      { "word": "番組", "reading": "ばんぐみ", "meaning": "방송 프로그램", "description": "순서(番)대로 편성하여 짠(組) 방송 내용입니다." }
    ]
  },
  {
    "kanji": "走",
    "reading_on": "ソウ",
    "reading_kun": "はし(る)",
    "meaning": "달리다",
    "components": [
      { "char": "土", "role": "흙 토 (요소)", "desc": "상반신을 크게 흔들며 뛰어가는 사람 모양(夭)의 변형입니다." },
      { "char": "止", "role": "그칠 지 (요소)", "desc": "여기서는 발을 뜻하며, 발을 딛고 있는 모습입니다." }
    ],
    "story": "사람(土)이 팔을 흔들며 양발(止)을 쉴 새 없이 움직여 빠르게 '달리는' 모습을 본뜬 글자입니다.",
    "example_words": [
      { "word": "走る", "reading": "はしる", "meaning": "달리다", "description": "빠르게 뛰어서 움직이는 것입니다." },
      { "word": "逃走", "reading": "とうそう", "meaning": "도주", "description": "도망쳐서(逃) 달아나는(走) 일입니다." }
    ]
  },
  {
    "kanji": "多",
    "reading_on": "タ",
    "reading_kun": "おお(い)",
    "meaning": "많다",
    "components": [
      { "char": "夕", "role": "저녁 석 (부수)", "desc": "해가 진 후의 달, 혹은 고깃덩어리 모양을 나타냅니다." }
    ],
    "story": "제사에 쓸 고깃덩어리(夕)가 겹겹이 쌓여 있는 모습에서 그 수량이 매우 '많다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "多分", "reading": "たぶん", "meaning": "아마도", "description": "가능성이 많고(多) 크다(分)는 뜻의 부사입니다." },
      { "word": "多数", "reading": "たすう", "meaning": "다수", "description": "많은(多) 수(数)를 뜻합니다." }
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

print("Grade 2 Part 4.2 data appended successfully.")
