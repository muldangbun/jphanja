import json
import os

new_data = [
  {
    "kanji": "悪",
    "reading_on": "アク、オ",
    "reading_kun": "わる(い)",
    "meaning": "악할 / 나쁘다",
    "components": [
      { "char": "亜", "role": "버금 아 (요소)", "desc": "무덤 속 십자형 구조나 건물의 기초를 뜻하며, 둘째 간다는 뜻으로 '아/악' 발음을 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 마음을 뜻합니다." }
    ],
    "story": "버금가게(亜) 억눌려 있거나 굽은 마음(心)에서 유래하여, 성질이 삐뚤어지고 '나쁘다', '악하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "悪い", "reading": "わるい", "meaning": "나쁘다", "description": "좋지 않거나 성질이 악한 상태를 뜻합니다." },
      { "word": "悪者", "reading": "わるもの", "meaning": "악당", "description": "나쁜(悪) 짓을 하는 사람(者)입니다." }
    ]
  },
  {
    "kanji": "安",
    "reading_on": "アン",
    "reading_kun": "やす(い)",
    "meaning": "편안할 / 싸다",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "건물이나 지붕을 뜻하여 안락한 공간을 의미합니다." },
      { "char": "女", "role": "계집 녀 (요소)", "desc": "여성을 뜻합니다." }
    ],
    "story": "지붕(宀) 아래에 여자(女)가 편안하게 앉아 있는 모습에서 '편안하다'는 뜻이 되었고, 마음이 편안할 만큼 가격이 '싸다'는 뜻으로도 쓰입니다.",
    "example_words": [
      { "word": "安心", "reading": "あんしん", "meaning": "안심", "description": "마음(心)이 편안한(安) 상태입니다." },
      { "word": "安い", "reading": "やすい", "meaning": "싸다", "description": "가격이 저렴하고 싼 것을 뜻합니다." }
    ]
  },
  {
    "kanji": "暗",
    "reading_on": "アン",
    "reading_kun": "くら(い)",
    "meaning": "어두울",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 햇빛을 뜻합니다." },
      { "char": "音", "role": "소리 음 (요소)", "desc": "발음 '음/안'을 나타내며, 원래 빛이 가려진다는 뜻을 내포하고 있습니다." }
    ],
    "story": "태양(日) 빛이 무언가에 가려져 소리(音)만 들리고 주변은 '어둡다'는 뜻을 나타냅니다.",
    "example_words": [
      { "word": "暗い", "reading": "くらい", "meaning": "어둡다", "description": "빛이 없어 어두운 상태입니다." },
      { "word": "暗記", "reading": "あんき", "meaning": "암기", "description": "책을 안 보고 어두운(暗) 상태에서 외워 기억하는(記) 일입니다." }
    ]
  },
  {
    "kanji": "医",
    "reading_on": "イ",
    "reading_kun": "",
    "meaning": "의원",
    "components": [
      { "char": "匚", "role": "터진입구 (부수)", "desc": "상자나 그릇 등 기구를 담아두는 곳을 뜻합니다." },
      { "char": "矢", "role": "화살 시 (요소)", "desc": "상처를 입힌 화살이나, 찌르는 침 등 의료 도구를 나타냅니다." }
    ],
    "story": "상자(匚) 속에 침이나 칼, 뽑아낸 화살(矢) 같은 수술 도구들을 담아두고 사람을 고치는 '의사(의원)'를 뜻합니다.",
    "example_words": [
      { "word": "医者", "reading": "いしゃ", "meaning": "의사", "description": "의술(医)을 행하는 사람(者)입니다." },
      { "word": "医学", "reading": "いがく", "meaning": "의학", "description": "병을 고치는(医) 학문(学)입니다." }
    ]
  },
  {
    "kanji": "委",
    "reading_on": "イ",
    "reading_kun": "ゆだ(ねる)",
    "meaning": "맡길",
    "components": [
      { "char": "禾", "role": "벼 화 (요소)", "desc": "벼나 곡식을 뜻하며, 구부러진 이삭 모양입니다." },
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성을 뜻합니다." }
    ],
    "story": "벼(禾) 이삭이 여물어 고개를 숙이듯, 여자(女)가 다소곳이 숙이고 시키는 대로 물건을 '맡다' 혹은 남에게 '맡기다'는 뜻입니다.",
    "example_words": [
      { "word": "委員", "reading": "いいん", "meaning": "위원", "description": "어떤 일을 맡은(委) 인원(員)입니다." },
      { "word": "委せる", "reading": "まかせる", "meaning": "맡기다", "description": "남에게 일이나 책임을 맡기는 것입니다." }
    ]
  },
  {
    "kanji": "意",
    "reading_on": "イ",
    "reading_kun": "",
    "meaning": "뜻",
    "components": [
      { "char": "音", "role": "소리 음 (요소)", "desc": "마음속에서 울리는 소리나 생각을 뜻합니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 마음을 뜻합니다." }
    ],
    "story": "마음(心) 속에서 생각의 소리(音)가 울려나와 겉으로 드러나는 '뜻'이나 '생각'을 의미합니다.",
    "example_words": [
      { "word": "意味", "reading": "いみ", "meaning": "의미", "description": "뜻(意)이 담고 있는 맛(味), 즉 의의입니다." },
      { "word": "注意", "reading": "ちゅうい", "meaning": "주의", "description": "뜻(意)을 어떤 곳에 붓거나(注) 쏟아 집중하는 것입니다." }
    ]
  },
  {
    "kanji": "育",
    "reading_on": "イク",
    "reading_kun": "そだ(つ)、そだ(てる)",
    "meaning": "기를",
    "components": [
      { "char": "㐬", "role": "아기 날 돌 (요소)", "desc": "어머니 몸에서 태어나는 아이의 모습을 뒤집어 놓은 형태입니다." },
      { "char": "月", "role": "육달월 (부수)", "desc": "사람의 몸, 살코기를 뜻합니다." }
    ],
    "story": "거꾸로 태어난 아기(㐬)를 살(月)이 통통하게 오르도록 튼튼하게 '기른다'는 뜻입니다.",
    "example_words": [
      { "word": "教育", "reading": "きょういく", "meaning": "교육", "description": "바르게 가르쳐서(教) 기르는(育) 일입니다." },
      { "word": "育てる", "reading": "そだてる", "meaning": "기르다", "description": "아이를 보살펴서 키우는 것을 뜻합니다." }
    ]
  },
  {
    "kanji": "員",
    "reading_on": "イン",
    "reading_kun": "",
    "meaning": "인원",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "둥근 솥이나 입을 뜻하며 사람의 머릿수를 의미합니다." },
      { "char": "貝", "role": "조개 패 (요소)", "desc": "돈이나 둥근 청동솥을 뜻하여 관직을 받은 사람을 의미하기도 합니다." }
    ],
    "story": "둥근 입구(口)를 가진 솥(貝)의 모습에서 '둥글다'는 뜻이었다가, 관청에서 녹봉을 받는 '인원(사람)'을 가리키게 되었습니다.",
    "example_words": [
      { "word": "店員", "reading": "てんいん", "meaning": "점원", "description": "가게(店)에서 일하는 인원(員)입니다." },
      { "word": "会員", "reading": "かいいん", "meaning": "회원", "description": "모임(会)에 속한 인원(員)입니다." }
    ]
  },
  {
    "kanji": "院",
    "reading_on": "イン",
    "reading_kun": "",
    "meaning": "집 (담장)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 흙으로 쌓은 담장을 뜻합니다." },
      { "char": "完", "role": "완전할 완 (요소)", "desc": "빙 둘러서 튼튼하고 완전하다는 뜻으로, '완/인' 발음을 담당합니다." }
    ],
    "story": "담장(阝)을 튼튼하고 완전하게(完) 빙 둘러친 관청, 혹은 커다란 '집'을 뜻합니다.",
    "example_words": [
      { "word": "病院", "reading": "びょういん", "meaning": "병원", "description": "병(病)을 고치는 관청(집)(院)입니다." },
      { "word": "入院", "reading": "にゅういん", "meaning": "입원", "description": "병원(院)에 들어가는(入) 것입니다." }
    ]
  },
  {
    "kanji": "飲",
    "reading_on": "イン",
    "reading_kun": "の(む)",
    "meaning": "마실",
    "components": [
      { "char": "食", "role": "밥 식 (부수)", "desc": "음식, 밥을 뜻합니다." },
      { "char": "欠", "role": "하품 흠 (요소)", "desc": "입을 크게 벌리고 하품을 하거나 숨을 들이마시는 모양입니다." }
    ],
    "story": "음식(食) 중에서도 물이나 액체를 입을 크게 벌려(欠) 목구멍으로 '마시는' 동작을 나타냅니다.",
    "example_words": [
      { "word": "飲む", "reading": "のむ", "meaning": "마し다", "description": "물이나 약 등을 입안에 넣고 삼키는 것입니다." },
      { "word": "飲み物", "reading": "のみもの", "meaning": "음료, 마실 것", "description": "마시는(飲み) 액체 물건(物)입니다." }
    ]
  },
  {
    "kanji": "運",
    "reading_on": "ウン",
    "reading_kun": "はこ(ぶ)",
    "meaning": "운전할 / 나르다",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "이동하다, 길을 가다는 뜻입니다." },
      { "char": "軍", "role": "군사 군 (요소)", "desc": "군대나 수레(車)를 뜻하여 무거운 짐을 나타냅니다." }
    ],
    "story": "무거운 수레나 짐(軍)을 길을 따라 이동(辶)하며 '나르다' 혹은 스스로 나아가는 '운수'를 뜻합니다.",
    "example_words": [
      { "word": "運ぶ", "reading": "はこぶ", "meaning": "나르다, 운반하다", "description": "물건을 다른 곳으로 옮기는 것입니다." },
      { "word": "運転", "reading": "うんてん", "meaning": "운전", "description": "바퀴를 굴려(転) 나아가게 이끄는(運) 것입니다." }
    ]
  },
  {
    "kanji": "泳",
    "reading_on": "エイ",
    "reading_kun": "およ(ぐ)",
    "meaning": "헤엄칠",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물과 관련됨을 뜻합니다." },
      { "char": "永", "role": "길 영 (요소)", "desc": "물줄기가 끝없이 길게 흘러가는 모양으로, 헤엄을 치며 계속 뻗어나감을 뜻합니다." }
    ],
    "story": "물(氵) 속에서 손과 발을 길게 뻗어가며(永) 앞으로 '헤엄쳐' 나아가는 것을 나타냅니다.",
    "example_words": [
      { "word": "泳ぐ", "reading": "およぐ", "meaning": "헤엄치다", "description": "물속을 나아가는 것입니다." },
      { "word": "水泳", "reading": "すいえい", "meaning": "수영", "description": "물(水)에서 헤엄치는(泳) 운동입니다." }
    ]
  },
  {
    "kanji": "駅",
    "reading_on": "エキ",
    "reading_kun": "",
    "meaning": "정거장 (역)",
    "components": [
      { "char": "馬", "role": "말 마 (부수)", "desc": "달리는 말을 뜻합니다." },
      { "char": "尺", "role": "자 척 (요소)", "desc": "여기서는 여러 말을 교대시키기 위해 잇대어 늘어놓은 모양(역)이 변형된 것입니다." }
    ],
    "story": "옛날에 짐을 나르던 말(馬)들을 길 중간중간(尺의 변형)에서 갈아탈 수 있게 마련해 놓은 '정거장' 혹은 '역'을 뜻합니다.",
    "example_words": [
      { "word": "駅員", "reading": "えきいん", "meaning": "역무원", "description": "역(駅)에서 일하는 인원(員)입니다." },
      { "word": "駅前", "reading": "えきまえ", "meaning": "역 앞", "description": "정거장(駅)의 앞(前)쪽 공간입니다." }
    ]
  },
  {
    "kanji": "央",
    "reading_on": "オウ",
    "reading_kun": "",
    "meaning": "가운데",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "팔다리를 벌리고 서 있는 사람의 모양입니다." },
      { "char": "冂", "role": "멀 경 (요소)", "desc": "사람의 목에 씌워진 칼(형구) 모양입니다." }
    ],
    "story": "사람(大)의 목 '한가운데'에 둥근 칼(冂)이 씌워진 모습에서, 어떤 사물의 한가운데나 '중앙'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "中央", "reading": "ちゅうおう", "meaning": "중앙", "description": "가운데(中) 중에서도 가장 복판(央)입니다." },
      { "word": "震央", "reading": "しんおう", "meaning": "진앙", "description": "지진이 일어난 한가운데(央) 지점입니다." }
    ]
  },
  {
    "kanji": "横",
    "reading_on": "オウ",
    "reading_kun": "よこ",
    "meaning": "가로 (옆)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "黄", "role": "누를 황 (요소)", "desc": "노란 빛, 넓게 퍼진다는 의미와 '황/오우' 발음을 가집니다." }
    ],
    "story": "문이나 창문을 단단히 잠그기 위해 나무(木)를 넓게 가로질러(黄) 질러놓은 빗장에서 유래하여, '가로'나 '옆'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "横断", "reading": "おうだん", "meaning": "횡단", "description": "길을 가로(横) 질러서 건너는(断) 것입니다." },
      { "word": "横顔", "reading": "よこがお", "meaning": "옆얼굴", "description": "옆(横)에서 본 얼굴(顔) 모습입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade3.json'
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

print("Grade 3 Part 1.1 data appended successfully.")
