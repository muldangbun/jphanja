import json
import os

new_data = [
  {
    "kanji": "太",
    "reading_on": "タイ、タ",
    "reading_kun": "ふと(い)、ふと(る)",
    "meaning": "클 / 굵다",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "사람이 두 팔과 다리를 크게 벌린 모양입니다." },
      { "char": "丶", "role": "점 주 (요소)", "desc": "크고 중요한 부분, 혹은 덧붙여진 무언가를 강조합니다." }
    ],
    "story": "큰(大) 몸에 살집이나 점(丶)이 더 붙어서 덩치가 아주 '크고', '굵다'는 의미입니다.",
    "example_words": [
      { "word": "太陽", "reading": "たいよう", "meaning": "태양", "description": "우주에서 가장 크고(太) 빛나는 볕(陽)입니다." },
      { "word": "太る", "reading": "ふとる", "meaning": "살찌다", "description": "몸집이 크고 굵어지는 것입니다." }
    ]
  },
  {
    "kanji": "体",
    "reading_on": "タイ、テイ",
    "reading_kun": "からだ",
    "meaning": "몸",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "本", "role": "근본 본 (요소)", "desc": "사물의 뿌리나 근본을 뜻하며, 발음 '본/혼'이 변형되어 쓰입니다." }
    ],
    "story": "사람(亻)이 살아가는 데 있어 가장 근본(本)이 되는 중요한 바탕, 즉 '몸'을 뜻합니다.",
    "example_words": [
      { "word": "体育", "reading": "たいいく", "meaning": "체육", "description": "몸(体)을 건강하게 기르는(育) 것입니다." },
      { "word": "体力", "reading": "たいりょく", "meaning": "체력", "description": "몸(体)에서 나오는 힘(力)입니다." }
    ]
  },
  {
    "kanji": "台",
    "reading_on": "ダイ、タイ",
    "reading_kun": "",
    "meaning": "대 / 돈대",
    "components": [
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "위로 솟아오른 모양이나 어떤 물건의 윗부분을 뜻합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "토대나 튼튼한 기반을 뜻합니다." }
    ],
    "story": "튼튼한 기반(口) 위에 어떤 물건이 높이 솟아(ム) 올려져 있는 평평한 '받침대'나 '단'을 의미합니다.",
    "example_words": [
      { "word": "台風", "reading": "たいふう", "meaning": "태풍", "description": "대만(台湾) 쪽에서 불어오는 큰 바람(風)이라는 뜻에서 유래했습니다." },
      { "word": "舞台", "reading": "ぶたい", "meaning": "무대", "description": "춤을 추기(舞) 위해 높이 만들어진 대(台)입니다." }
    ]
  },
  {
    "kanji": "地",
    "reading_on": "チ、ジ",
    "reading_kun": "",
    "meaning": "땅",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 대지를 의미합니다." },
      { "char": "也", "role": "어조사 야 (요소)", "desc": "뱀이 몸을 틀고 있는 모양으로, 구불구불 이어짐을 나타냅니다." }
    ],
    "story": "흙(土)이 구불구불하게(也) 끝없이 넓게 이어져 있는 '땅'이나 '대지'를 의미합니다.",
    "example_words": [
      { "word": "地球", "reading": "ちきゅう", "meaning": "지구", "description": "우리가 사는 땅(地)으로 된 둥근 공(球)입니다." },
      { "word": "地下", "reading": "ちか", "meaning": "지하", "description": "땅(地)의 아래(下)입니다." }
    ]
  },
  {
    "kanji": "池",
    "reading_on": "チ",
    "reading_kun": "いけ",
    "meaning": "못",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물과 관련됨을 뜻합니다." },
      { "char": "也", "role": "어조사 야 (요소)", "desc": "구불구불한 둘레나 모양을 뜻하며 발음 '야/지'를 담당합니다." }
    ],
    "story": "구불구불한(也) 둑을 쌓아 물(氵)을 가두어 놓은 '연못'을 뜻합니다.",
    "example_words": [
      { "word": "電池", "reading": "でんち", "meaning": "전지, 배터리", "description": "전기(電)를 모아두는 연못(池)이라는 뜻입니다." },
      { "word": "ため池", "reading": "ためいけ", "meaning": "저수지", "description": "물을 모아(ため) 두는 연못(池)입니다." }
    ]
  },
  {
    "kanji": "知",
    "reading_on": "チ",
    "reading_kun": "し(る)",
    "meaning": "알다",
    "components": [
      { "char": "矢", "role": "화살 시 (부수)", "desc": "과녁을 향해 빠르게 날아가는 화살입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "말로 표현하는 것을 의미합니다." }
    ],
    "story": "어떤 사물에 대한 지식이 마치 화살(矢)처럼 빠르고 명확하게 입(口) 밖으로 튀어나올 정도로 잘 '안다'는 뜻입니다.",
    "example_words": [
      { "word": "知識", "reading": "ちしき", "meaning": "지식", "description": "알고(知) 분별하는(識) 내용입니다." },
      { "word": "知り合い", "reading": "しりあい", "meaning": "지인, 아는 사람", "description": "서로 아는(知り) 사이(合い)입니다." }
    ]
  },
  {
    "kanji": "茶",
    "reading_on": "チャ、サ",
    "reading_kun": "",
    "meaning": "차",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 식물을 뜻합니다." },
      { "char": "人", "role": "사람 인 (요소)", "desc": "사람이 채집하는 모습을 나타냅니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "차나무를 뜻합니다." }
    ],
    "story": "사람(人)이 차나무(木)에서 돋아난 어린 잎이나 풀(艹)을 따서 달여 마시는 '차'를 뜻합니다.",
    "example_words": [
      { "word": "お茶", "reading": "おちゃ", "meaning": "차 (음료)", "description": "마시는 차(茶)를 친근하고 높여 부르는 말입니다." },
      { "word": "茶色", "reading": "ちゃいろ", "meaning": "갈색", "description": "차(茶)를 우려낸 빛깔(色)입니다." }
    ]
  },
  {
    "kanji": "昼",
    "reading_on": "チュウ",
    "reading_kun": "ひる",
    "meaning": "낮",
    "components": [
      { "char": "尺", "role": "자 척 (요소)", "desc": "길이를 재는 잣대나, 한계를 뜻합니다." },
      { "char": "旦", "role": "아침 단 (요소)", "desc": "지평선 위로 해가 뜬 아침부터 해가 지기 전까지를 뜻합니다." }
    ],
    "story": "지평선 위로 해가 솟은(旦) 후부터 해가 지기 전까지 일정한 길이(尺)를 가진 밝은 시간인 '낮'을 뜻합니다.",
    "example_words": [
      { "word": "昼休み", "reading": "ひるやすみ", "meaning": "점심시간", "description": "낮(昼)에 쉬는(休み) 시간입니다." },
      { "word": "昼食", "reading": "ちゅうしょく", "meaning": "중식, 점심", "description": "낮(昼)에 먹는 밥(食)입니다." }
    ]
  },
  {
    "kanji": "長",
    "reading_on": "チョウ",
    "reading_kun": "なが(い)",
    "meaning": "길다 / 어른",
    "components": [
      { "char": "長", "role": "길 장 (부수)", "desc": "머리카락이 길게 늘어진 지팡이를 짚은 노인의 모습입니다." }
    ],
    "story": "나이가 많아 머리카락이 길게 자란 노인의 모습에서 시간이 '길다'거나, 무리의 '어른(우두머리)'이라는 뜻이 되었습니다.",
    "example_words": [
      { "word": "長い", "reading": "ながい", "meaning": "길다", "description": "거리나 시간이 긴 상태입니다." },
      { "word": "社長", "reading": "しゃちょう", "meaning": "사장", "description": "회사(社)의 가장 높은 어른(長)입니다." }
    ]
  },
  {
    "kanji": "鳥",
    "reading_on": "チョウ",
    "reading_kun": "とり",
    "meaning": "새",
    "components": [
      { "char": "鳥", "role": "새 조 (부수)", "desc": "부리, 눈, 날개, 그리고 발톱(灬)을 가진 새의 상형문자입니다." }
    ],
    "story": "부리와 날개를 가지고 하늘을 나는 꼬리가 긴 '새'의 모양을 그대로 그린 글자입니다.",
    "example_words": [
      { "word": "小鳥", "reading": "ことり", "meaning": "작은 새", "description": "크기가 작은(小) 새(鳥)입니다." },
      { "word": "白鳥", "reading": "はくちょう", "meaning": "백조", "description": "흰색(白) 깃털을 가진 새(鳥)입니다." }
    ]
  },
  {
    "kanji": "朝",
    "reading_on": "チョウ",
    "reading_kun": "あさ",
    "meaning": "아침",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "풀숲을 나타내는 두 개의 십자(++=艹)의 변형입니다." },
      { "char": "日", "role": "날 일 (요소)", "desc": "태양입니다." },
      { "char": "月", "role": "달 월 (부수)", "desc": "달을 뜻합니다." }
    ],
    "story": "풀숲(十, 十) 사이로 해(日)가 막 떠오르고 아직 달(月)이 지지 않고 희미하게 남아 있는 시간, 즉 '아침'을 뜻합니다.",
    "example_words": [
      { "word": "朝食", "reading": "ちょうしょく", "meaning": "조식, 아침 식사", "description": "아침(朝)에 먹는 밥(食)입니다." },
      { "word": "毎朝", "reading": "まいあさ", "meaning": "매일 아침", "description": "매일(毎) 맞이하는 아침(朝)입니다." }
    ]
  },
  {
    "kanji": "直",
    "reading_on": "チョク、ジキ",
    "reading_kun": "ただ(ちに)、なお(す)",
    "meaning": "곧다 / 고치다",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "눈 위를 가리는 무언가 혹은 올바름을 뜻합니다." },
      { "char": "目", "role": "눈 목 (부수)", "desc": "사람의 눈입니다." },
      { "char": "乚", "role": "숨을 은 (요소)", "desc": "숨겨진 모서리, 즉 숨김없는 상태를 나타냅니다." }
    ],
    "story": "열(十) 개의 눈(目)이 지켜보듯 시선을 감추지 않고 올곧게 바로 보는 모습에서 '곧다'나 잘못을 '고치다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "直線", "reading": "ちょくせん", "meaning": "직선", "description": "곧게(直) 뻗은 선(線)입니다." },
      { "word": "見直す", "reading": "みなおす", "meaning": "다시 보다", "description": "보고(見) 잘못된 것을 고치는(直す) 것입니다." }
    ]
  },
  {
    "kanji": "通",
    "reading_on": "ツウ",
    "reading_kun": "とお(る)、かよ(う)",
    "meaning": "통하다",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아가는 것, 이동을 뜻합니다." },
      { "char": "甬", "role": "길 용 (요소)", "desc": "대롱이나 종처럼 텅 비어서 소리가 통하는 모양입니다. 발음 '용/통'을 줍니다." }
    ],
    "story": "막힌 곳이 없는 대롱(甬)처럼, 길(辶)이 뚫려 있어 막힘없이 나아가고 '통한다'는 뜻입니다.",
    "example_words": [
      { "word": "交通", "reading": "こうつう", "meaning": "교통", "description": "서로 엇갈리며(交) 통과하는(通) 일입니다." },
      { "word": "通勤", "reading": "つうきん", "meaning": "통근", "description": "근무처(勤)로 다니는(通) 일입니다." }
    ]
  },
  {
    "kanji": "弟",
    "reading_on": "テイ、ダイ",
    "reading_kun": "おとうと",
    "meaning": "아우",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "여기서는 가죽 끈을 휘감은 모양의 간략화된 형태입니다." },
      { "char": "丿", "role": "삐침 (요소)", "desc": "순서대로 차례를 나타내는 표시입니다." }
    ],
    "story": "원래는 막대에 가죽 끈을 차례대로 감은 모습에서, 형 다음의 순서를 뜻하게 되어 '아우(남동생)'를 의미합니다.",
    "example_words": [
      { "word": "兄弟", "reading": "きょうだい", "meaning": "형제", "description": "형(兄)과 아우(弟)입니다." },
      { "word": "弟子", "reading": "でし", "meaning": "제자", "description": "아우(弟)처럼 가르침을 받는 아이(子), 즉 제자입니다." }
    ]
  },
  {
    "kanji": "店",
    "reading_on": "テン",
    "reading_kun": "みせ",
    "meaning": "가게",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "지붕이나 한쪽 벽이 터진 집무실, 점포를 뜻합니다." },
      { "char": "占", "role": "점칠 점 (요소)", "desc": "자리를 차지하다는 의미와 '점/텐' 발음을 담당합니다." }
    ],
    "story": "지붕(广)이 덮인 건물 안에서 어떤 자리를 차지하고(占) 물건을 늘어놓고 파는 '가게'를 뜻합니다.",
    "example_words": [
      { "word": "書店", "reading": "しょてん", "meaning": "서점", "description": "책(書)을 파는 가게(店)입니다." },
      { "word": "店員", "reading": "てんいん", "meaning": "점원", "description": "가게(店)에서 일하는 직원(員)입니다." }
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

print("Grade 2 Part 5.1 data appended successfully.")
