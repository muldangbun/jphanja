import json
import os

new_data = [
  {
    "kanji": "帰",
    "reading_on": "キ",
    "reading_kun": "かえ(る)、かえ(す)",
    "meaning": "돌아가다",
    "components": [
      { "char": "刂", "role": "선칼도방 (변형)", "desc": "여기서는 발의 이동이나 발걸음을 상징하는 부수의 변형으로 쓰였습니다." },
      { "char": "帚", "role": "빗자루 추 (요소)", "desc": "집안을 청소하는 빗자루, 즉 아내나 집안 살림을 뜻합니다." }
    ],
    "story": "발걸음(刂)을 돌려 아내가 빗자루(帚)를 들고 기다리는 편안한 집으로 '돌아간다'는 뜻입니다.",
    "example_words": [
      { "word": "帰国", "reading": "きこく", "meaning": "귀국", "description": "자신의 나라(国)로 돌아가는(帰) 것입니다." },
      { "word": "日帰り", "reading": "ひがえり", "meaning": "당일치기", "description": "그 날(日) 하루 만에 다녀와서 돌아오는(帰り) 것입니다." }
    ]
  },
  {
    "kanji": "弓",
    "reading_on": "キュウ",
    "reading_kun": "ゆみ",
    "meaning": "활",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "시위가 걸려 있는 굽은 활의 모습을 본뜬 상형문자입니다." }
    ],
    "story": "화살을 쏘기 위해 나무를 구부려 시위를 매단 '활'의 형태를 그대로 그린 한자입니다.",
    "example_words": [
      { "word": "弓矢", "reading": "ゆみや", "meaning": "활과 화살", "description": "활(弓)과 화살(矢)을 뜻합니다." },
      { "word": "弓道", "reading": "きゅうどう", "meaning": "궁도", "description": "활(弓)을 쏘는 무술이나 도(道)를 의미합니다." }
    ]
  },
  {
    "kanji": "牛",
    "reading_on": "ギュウ",
    "reading_kun": "うし",
    "meaning": "소",
    "components": [
      { "char": "牛", "role": "소 우 (부수)", "desc": "뿔이 난 소의 머리 모양을 정면에서 본뜬 상형문자입니다." }
    ],
    "story": "두 개의 뿔이 솟아 있고 양옆으로 귀가 달린 듬직한 '소'의 머리를 정면에서 바라본 모습입니다.",
    "example_words": [
      { "word": "牛乳", "reading": "ぎゅうにゅう", "meaning": "우유", "description": "소(牛)에서 짠 젖(乳)입니다." },
      { "word": "牛肉", "reading": "ぎゅうにく", "meaning": "쇠고기", "description": "소(牛)의 고기(肉)를 의미합니다." }
    ]
  },
  {
    "kanji": "魚",
    "reading_on": "ギョ",
    "reading_kun": "うお、さかな",
    "meaning": "물고기",
    "components": [
      { "char": "魚", "role": "물고기 어 (부수)", "desc": "머리, 비늘(田), 꼬리(灬)를 갖춘 물고기의 모습을 본뜬 상형문자입니다." }
    ],
    "story": "위쪽은 뾰족한 물고기의 입과 머리, 가운데(田)는 비늘이 있는 몸통, 아래(灬)는 지느러미와 꼬리를 그려 '물고기'를 나타냈습니다.",
    "example_words": [
      { "word": "金魚", "reading": "きんぎょ", "meaning": "금붕어", "description": "금빛(金)이 나는 물고기(魚)를 뜻합니다." },
      { "word": "魚屋", "reading": "さかなや", "meaning": "생선 가게", "description": "물고기(魚)를 파는 상점이나 사람(屋)입니다." }
    ]
  },
  {
    "kanji": "京",
    "reading_on": "キョウ、ケイ",
    "reading_kun": "みやこ",
    "meaning": "서울 / 도읍",
    "components": [
      { "char": "亠", "role": "돼지해머리 (부수)", "desc": "건물의 지붕이나 높은 꼭대기를 뜻합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "여기서는 크고 번화한 건축물의 몸통입니다." },
      { "char": "小", "role": "작을 소 (요소)", "desc": "여기서는 건물을 튼튼하게 받치는 기둥이나 성벽의 뜻으로 쓰였습니다." }
    ],
    "story": "지붕(亠)이 높고 웅장한 건물(口)들이 튼튼하게(小) 늘어서 있는, 왕이 사는 도읍지 즉 '서울'을 뜻합니다.",
    "example_words": [
      { "word": "東京", "reading": "とうきょう", "meaning": "도쿄", "description": "동쪽(東)에 있는 도읍지(京)라는 뜻으로, 일본의 수도입니다." },
      { "word": "上京", "reading": "じょうきょう", "meaning": "상경", "description": "지방에서 서울(京)로 올라가는(上) 것을 뜻합니다." }
    ]
  },
  {
    "kanji": "強",
    "reading_on": "キョウ、ゴウ",
    "reading_kun": "つよ(い)、し(いる)",
    "meaning": "강하다",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "탄력이 굳센 활을 의미합니다." },
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "팔을 굽힌 모양이나 굳센 벌레(풍뎅이)의 머리를 나타냅니다." },
      { "char": "虫", "role": "벌레 충 (요소)", "desc": "단단한 껍질을 가진 벌레(풍뎅이 류)를 뜻합니다." }
    ],
    "story": "단단하고 굳센 활(弓)과 딱딱한 껍질을 가진 벌레(虫)의 모습에서, 굽히지 않는 '강하다'는 의미를 나타냅니다.",
    "example_words": [
      { "word": "強力", "reading": "きょうりょく", "meaning": "강력", "description": "힘(力)이 세고 강한(強) 상태입니다." },
      { "word": "勉強", "reading": "べんきょう", "meaning": "공부", "description": "어려운 것을 애써서(勉) 강제로(強) 익히고 노력한다는 뜻에서 유래했습니다." }
    ]
  },
  {
    "kanji": "教",
    "reading_on": "キョウ",
    "reading_kun": "おし(える)、おそ(わる)",
    "meaning": "가르치다",
    "components": [
      { "char": "孝", "role": "효도 효 (요소)", "desc": "늙은이를 업거나 공경하며 전통을 잇는 모습입니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손에 회초리나 막대기를 들고 가볍게 치며 독려하는 모습입니다." }
    ],
    "story": "어른 공경하는 법과 전통(孝)을 아이가 잘 익히도록, 손에 막대기를 들고(攵) 올바른 길로 '가르치는' 모습입니다.",
    "example_words": [
      { "word": "教室", "reading": "きょうしつ", "meaning": "교실", "description": "가르치는(教) 활동이 이루어지는 방(室)입니다." },
      { "word": "教育", "reading": "きょういく", "meaning": "교육", "description": "가르쳐서(教) 바르게 자라도록 기르는(育) 것입니다." }
    ]
  },
  {
    "kanji": "近",
    "reading_on": "キン",
    "reading_kun": "ちか(い)",
    "meaning": "가깝다",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아가는 등 이동의 의미를 가집니다." },
      { "char": "斤", "role": "도끼 근 (요소)", "desc": "나무를 베는 도끼로, 발음 '근/킨'을 나타내며 나무를 잘라 사이를 좁힌다는 의미도 줍니다." }
    ],
    "story": "길을 갈 때(辶) 도끼(斤)로 장해물을 치워내어 가야 할 거리가 좁혀져 '가깝다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "近所", "reading": "きんじょ", "meaning": "근처, 이웃", "description": "가까운(近) 장소(所)를 뜻합니다." },
      { "word": "最近", "reading": "さいきん", "meaning": "최근", "description": "가장(最) 가까운(近) 과거의 시간을 말합니다." }
    ]
  },
  {
    "kanji": "兄",
    "reading_on": "キョウ、ケイ",
    "reading_kun": "あに",
    "meaning": "형 / 오빠",
    "components": [
      { "char": "口", "role": "입 구 (요소)", "desc": "입을 크게 벌리고 말하는 모습을 뜻합니다." },
      { "char": "儿", "role": "어진사람 인 (부수)", "desc": "사람의 다리나 사람 자체를 뜻합니다." }
    ],
    "story": "제사나 큰일이 있을 때, 사람들(儿)을 대표하여 입(口)을 벌려 축문을 읽거나 지시를 내리는 맏이, 즉 '형'을 의미합니다.",
    "example_words": [
      { "word": "兄弟", "reading": "きょうだい", "meaning": "형제", "description": "형(兄)과 아우(弟)를 뜻합니다." },
      { "word": "お兄さん", "reading": "おにいさん", "meaning": "형님, 오빠", "description": "형(兄)을 친근하고 높여 부르는 말입니다." }
    ]
  },
  {
    "kanji": "形",
    "reading_on": "ケイ、ギョウ",
    "reading_kun": "かたち",
    "meaning": "모양 / 형태",
    "components": [
      { "char": "幵", "role": "평평할 견 (요소)", "desc": "사물이 평평하게 잘 정돈된 틀의 모습을 뜻합니다. (발음 '형/케이')" },
      { "char": "彡", "role": "터럭 삼 (부수)", "desc": "아름다운 무늬나 겉으로 드러나는 윤곽, 털의 모양을 뜻합니다." }
    ],
    "story": "어떤 사물이 뼈대(幵)를 갖추고 겉으로 무늬나 윤곽(彡)이 뚜렷하게 드러나는 '모양'이나 '형태'를 뜻합니다.",
    "example_words": [
      { "word": "人形", "reading": "にんぎょう", "meaning": "인형", "description": "사람(人)의 모양(形)을 본떠 만든 장난감입니다." },
      { "word": "図形", "reading": "ずけい", "meaning": "도형", "description": "점, 선, 면 등으로 이루어진 그림(図) 모양(形)입니다." }
    ]
  },
  {
    "kanji": "計",
    "reading_on": "ケイ",
    "reading_kun": "はか(る)、はか(らう)",
    "meaning": "셈하다 / 계획하다",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 숫자를 소리 내어 세는 것을 뜻합니다." },
      { "char": "十", "role": "열 十 (요소)", "desc": "숫자 열(10), 즉 구체적인 숫자를 모두 합한다는 의미입니다." }
    ],
    "story": "열(十)까지의 모든 숫자를 말로(言) 하나하나 세어보며 전체를 '셈하다', 미래를 '계획하다'는 의미입니다.",
    "example_words": [
      { "word": "時計", "reading": "とけい", "meaning": "시계", "description": "시간(時)을 셈하는(計) 도구입니다." },
      { "word": "合計", "reading": "ごうけい", "meaning": "합계", "description": "전체를 합하여(合) 셈한(計) 값입니다." }
    ]
  },
  {
    "kanji": "元",
    "reading_on": "ゲン、ガン",
    "reading_kun": "もと",
    "meaning": "으뜸 / 근원",
    "components": [
      { "char": "二", "role": "두 이 (요소)", "desc": "여기서는 사람의 머리 위쪽, 하늘이나 으뜸을 표시하는 선입니다." },
      { "char": "儿", "role": "어진사람 인 (부수)", "desc": "사람의 몸통과 다리를 나타냅니다." }
    ],
    "story": "사람(儿)의 몸통 위에서 가장 높고 중요한 부분인 머리(二)를 강조하여, 만물의 처음인 '으뜸'이나 '근원'을 뜻합니다.",
    "example_words": [
      { "word": "元気", "reading": "げんき", "meaning": "건강함, 원기", "description": "근원적(元)으로 타고난 생명의 기운(気)을 뜻합니다." },
      { "word": "元日", "reading": "がんじつ", "meaning": "원일 (새해 첫날)", "description": "일 년 중 첫 번째(元) 날(日)입니다." }
    ]
  },
  {
    "kanji": "言",
    "reading_on": "ゲン、ゴン",
    "reading_kun": "い(う)、こと",
    "meaning": "말씀 / 말하다",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "입(口) 위에 나팔이나 피리 부는 모습을 얹어, 소리를 내어 말을 하는 모습을 본뜬 글자입니다." }
    ],
    "story": "입술(口) 위로 여러 가지 소리 굴곡이 나오며 다른 사람에게 내 뜻을 '말하다'라는 뜻을 지닌 부수이자 한자입니다.",
    "example_words": [
      { "word": "言葉", "reading": "ことば", "meaning": "말, 단어", "description": "사람의 입에서 나오는 말(言)의 이파리(葉)들, 즉 언어를 뜻합니다." },
      { "word": "伝言", "reading": "でんごん", "meaning": "전언, 메시지", "description": "다른 사람에게 대신 전해(伝) 주는 말(言)입니다." }
    ]
  },
  {
    "kanji": "原",
    "reading_on": "ゲン",
    "reading_kun": "はら",
    "meaning": "근원 / 들판",
    "components": [
      { "char": "厂", "role": "기슭 엄 (부수)", "desc": "산기슭이나 벼랑, 바위의 모양입니다." },
      { "char": "泉", "role": "샘 천 (요소)", "desc": "바위틈에서 물이 퐁퐁 솟아오르는 맑은 샘물을 뜻합니다. (원래 모양에서 간략화됨)" }
    ],
    "story": "산기슭 벼랑(厂) 밑의 바위틈에서 맑은 샘물(泉)이 솟아나오는 강물의 '근원'이라는 뜻이며, 물이 흐르는 넓은 '들판'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "原因", "reading": "げんいん", "meaning": "원인", "description": "어떤 일이 일어나게 된 근본(原)적인 까닭(因)입니다." },
      { "word": "野原", "reading": "のはら", "meaning": "들판", "description": "넓게 펼쳐진 들(野)과 평야(原)입니다." }
    ]
  },
  {
    "kanji": "戸",
    "reading_on": "コ",
    "reading_kun": "と",
    "meaning": "문 / 집",
    "components": [
      { "char": "戸", "role": "지게 호 (부수)", "desc": "한쪽으로 열고 닫는 외짝 문의 모습을 본뜬 상형문자입니다." }
    ],
    "story": "양쪽으로 열리는 큰 대문(門)과 달리, 한쪽으로만 열리고 닫히는 단출한 외짝 '문'이나 한 가구의 '집'을 뜻합니다.",
    "example_words": [
      { "word": "戸棚", "reading": "とだな", "meaning": "찬장, 벽장", "description": "문(戸)이 달려 있는 선반(棚)이라는 뜻입니다." },
      { "word": "雨戸", "reading": "あまど", "meaning": "덧문", "description": "비(雨)나 바람을 막기 위해 바깥에 설치하는 문(戸)입니다." }
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

print("Grade 2 Part 2.2 data appended successfully.")
