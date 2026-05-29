import json
import os

new_data = [
  {
    "kanji": "古",
    "reading_on": "コ",
    "reading_kun": "ふる(い)",
    "meaning": "옛 / 낡다",
    "components": [
      { "char": "十", "role": "열 십 (부수)", "desc": "열, 즉 많은 세대를 의미합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입에서 입으로 전해지는 말이나 이야기를 뜻합니다." }
    ],
    "story": "열(十) 세대를 거치며 입(口)에서 입으로 오랫동안 전해져 내려온 '옛날' 이야기나 '낡은' 것을 뜻합니다.",
    "example_words": [
      { "word": "古着", "reading": "ふるぎ", "meaning": "헌옷", "description": "낡고(古) 오래된 옷(着)입니다." },
      { "word": "中古", "reading": "ちゅうこ", "meaning": "중고", "description": "가운데(中) 정도로 낡은(古) 상태, 즉 누군가 쓰던 물건을 뜻합니다." }
    ]
  },
  {
    "kanji": "午",
    "reading_on": "ゴ",
    "reading_kun": "",
    "meaning": "낮 / 일곱째 지지",
    "components": [
      { "char": "十", "role": "열 십 (부수)", "desc": "십자가 모양의 절굿공이를 의미합니다." },
      { "char": "干", "role": "방패 간 (요소)", "desc": "가운데를 가로지르는 모습에서 파생되었습니다." }
    ],
    "story": "절굿공이(위아래로 찧는 도구)의 모습을 본뜬 것으로, 태양이 가장 높이 솟아 찧듯이 내리쬐는 '정오'나 '낮'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "午前", "reading": "ごぜん", "meaning": "오전", "description": "낮(午)의 이전(前) 시간입니다." },
      { "word": "午後", "reading": "ごご", "meaning": "오후", "description": "낮(午)의 이후(後) 시간입니다." }
    ]
  },
  {
    "kanji": "後",
    "reading_on": "ゴ、コウ",
    "reading_kun": "のち、うし(ろ)、あと",
    "meaning": "뒤 / 나중",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "조금씩 걷거나 길을 가는 모습입니다." },
      { "char": "幺", "role": "작을 요 (요소)", "desc": "작고 희미한 실타래 모양입니다." },
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "발을 끌며 뒤처져서 천천히 걷는 모습입니다." }
    ],
    "story": "길을 갈 때(彳) 발을 끌며(夂) 작게(幺) 뒤처져서 따라간다는 데서 '뒤'나 '나중'을 의미합니다.",
    "example_words": [
      { "word": "後ろ", "reading": "うしろ", "meaning": "뒤", "description": "사물이나 사람의 뒤쪽(後)을 말합니다." },
      { "word": "後半", "reading": "こうはん", "meaning": "후반", "description": "전체의 나중(後) 절반(半)을 뜻합니다." }
    ]
  },
  {
    "kanji": "語",
    "reading_on": "ゴ",
    "reading_kun": "かた(る)、かた(らう)",
    "meaning": "말씀 / 말하다",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 언어를 뜻합니다." },
      { "char": "吾", "role": "나 오 (요소)", "desc": "나 자신을 뜻하며, '오/고'라는 발음을 담당합니다." }
    ],
    "story": "자신(吾)의 생각을 말로(言) 조리 있게 풀어내어 '말하다' 혹은 '언어'를 의미합니다.",
    "example_words": [
      { "word": "単語", "reading": "たんご", "meaning": "단어", "description": "낱개(単)로 된 말(語)입니다." },
      { "word": "言語", "reading": "げんご", "meaning": "언어", "description": "말로(言) 표현하는 수단(語)입니다." }
    ]
  },
  {
    "kanji": "工",
    "reading_on": "コウ、ク",
    "reading_kun": "",
    "meaning": "장인 / 만들다",
    "components": [
      { "char": "工", "role": "장인 공 (부수)", "desc": "목수가 흙이나 나무를 다질 때 쓰는 도구(곱자)의 모양을 본뜬 글자입니다." }
    ],
    "story": "물건을 만드는 데 사용하는 도구를 그려내어, 기술을 가진 '장인'이나 무언가를 '만드는' 공사를 의미합니다.",
    "example_words": [
      { "word": "工場", "reading": "こうじょう", "meaning": "공장", "description": "물건을 만드는(工) 장소(場)입니다." },
      { "word": "人工", "reading": "じんこう", "meaning": "인공", "description": "사람(人)이 인위적으로 만든(工) 것입니다." }
    ]
  },
  {
    "kanji": "公",
    "reading_on": "コウ",
    "reading_kun": "おおやけ",
    "meaning": "공평하다 / 공공",
    "components": [
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "물건을 똑같이 나눈다는 의미를 가집니다." },
      { "char": "厶", "role": "마늘 모 (요소)", "desc": "사사로움(개인)을 뜻하는 형태입니다." }
    ],
    "story": "개인적인 사사로움(厶)을 반으로 나누어(八) 감추지 않고 드러내어 '공평하다' 혹은 '공공'의 뜻을 나타냅니다.",
    "example_words": [
      { "word": "公園", "reading": "こうえん", "meaning": "공원", "description": "공공(公)을 위해 만들어진 넓은 동산(園)입니다." },
      { "word": "公平", "reading": "こうへい", "meaning": "공평", "description": "어느 쪽으로도 치우치지 않고 공공(公)연하며 평평한(平) 상태입니다." }
    ]
  },
  {
    "kanji": "広",
    "reading_on": "コウ",
    "reading_kun": "ひろ(い)",
    "meaning": "넓다",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "벽이 없이 한쪽만 막힌 지붕이 있는 집이나 넓은 공간을 뜻합니다." },
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "크게 팔을 벌린 사람의 모습에서 변형되었습니다." }
    ],
    "story": "큰 지붕(广) 아래에서 팔을 벌릴(ム) 만큼 공간이 '넓다'는 의미를 나타내는 한자입니다.",
    "example_words": [
      { "word": "広場", "reading": "ひろば", "meaning": "광장", "description": "넓은(広) 장소(場)입니다." },
      { "word": "広告", "reading": "こうこく", "meaning": "광고", "description": "넓게(広) 세상에 알리는(告) 것입니다." }
    ]
  },
  {
    "kanji": "交",
    "reading_on": "コウ",
    "reading_kun": "まじ(わる)、ま(ぜる)",
    "meaning": "사귀다 / 엇갈리다",
    "components": [
      { "char": "亠", "role": "돼지해머리 (부수)", "desc": "사람의 머리 부분을 나타냅니다." },
      { "char": "父", "role": "아비 부 (요소)", "desc": "다리를 꼬고 서 있는 사람의 모습에서 유래했습니다." }
    ],
    "story": "사람이 두 다리를 '엇갈리게' 꼬고 있는 모습에서, 서로 교차하거나 '사귀는' 관계를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "交通", "reading": "こうつう", "meaning": "교통", "description": "서로 엇갈리며(交) 통과하는(通) 것을 의미합니다." },
      { "word": "交差点", "reading": "こうさてん", "meaning": "교차점", "description": "길이 엇갈려(交) 어긋나는(差) 지점(点)입니다." }
    ]
  },
  {
    "kanji": "光",
    "reading_on": "コウ",
    "reading_kun": "ひか(る)、ひかり",
    "meaning": "빛 / 빛나다",
    "components": [
      { "char": "⺌", "role": "작을 소 (변형)", "desc": "위쪽에서 타오르는 불꽃의 모양입니다." },
      { "char": "儿", "role": "어진사람 인 (부수)", "desc": "사람의 몸을 나타냅니다." }
    ],
    "story": "사람(儿)이 머리 위로 횃불(⺌)을 들고 주변을 '빛나게' 밝히는 모습입니다.",
    "example_words": [
      { "word": "日光", "reading": "にっこう", "meaning": "일광 (햇빛)", "description": "해(日)에서 나오는 빛(光)입니다." },
      { "word": "光景", "reading": "こうけい", "meaning": "광경", "description": "빛(光)이 비추어 보이는 경치나 모습(景)입니다." }
    ]
  },
  {
    "kanji": "考",
    "reading_on": "コウ",
    "reading_kun": "かんが(える)",
    "meaning": "생각하다",
    "components": [
      { "char": "耂", "role": "늙을 노 (부수)", "desc": "허리가 굽은 노인을 뜻합니다." },
      { "char": "丂", "role": "숨막힐 고 (요소)", "desc": "지팡이를 짚고 생각에 잠긴 모습이거나, 막혀서 나아가지 못하는 모습입니다." }
    ],
    "story": "경험이 많은 노인(耂)이 지팡이를 짚고(丂) 깊이 고민하며 '생각하는' 모습을 나타냅니다.",
    "example_words": [
      { "word": "参考", "reading": "さんこう", "meaning": "참고", "description": "다른 것을 살펴(参) 생각(考)에 도움을 주는 것입니다." },
      { "word": "思考", "reading": "しこう", "meaning": "사고", "description": "뜻을 품고(思) 깊이 생각하는(考) 것입니다." }
    ]
  },
  {
    "kanji": "行",
    "reading_on": "コウ、ギョウ",
    "reading_kun": "い(く)、ゆ(く)、おこな(う)",
    "meaning": "가다 / 행하다",
    "components": [
      { "char": "彳", "role": "두인변 (요소)", "desc": "사거리의 왼쪽 길 모양입니다." },
      { "char": "亍", "role": "자축거릴 촉 (요소)", "desc": "사거리의 오른쪽 길 모양입니다." }
    ],
    "story": "사방으로 통하는 교차로(彳+亍)의 모양을 본떠, 사람들이 길을 '가다' 혹은 일을 '행하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "旅行", "reading": "りょこう", "meaning": "여행", "description": "나그네(旅)가 되어 길을 가는(行) 것입니다." },
      { "word": "行動", "reading": "こうどう", "meaning": "행동", "description": "몸을 움직여(動) 행하는(行) 일입니다." }
    ]
  },
  {
    "kanji": "高",
    "reading_on": "コウ",
    "reading_kun": "たか(い)",
    "meaning": "높다",
    "components": [
      { "char": "亠", "role": "돼지해머리 (부수)", "desc": "건물의 지붕을 의미합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "건물의 창문이나 층을 나타냅니다." },
      { "char": "冂", "role": "멀 경 (요소)", "desc": "건물의 기둥이나 높은 구조물입니다." }
    ],
    "story": "지붕(亠)과 창문(口), 그리고 기둥(冂)을 층층이 높게 쌓아올린 성루의 모습을 본떠 '높다'는 의미입니다.",
    "example_words": [
      { "word": "高校", "reading": "こうこう", "meaning": "고교", "description": "높은(高) 수준의 학교(校)입니다." },
      { "word": "最高", "reading": "さいこう", "meaning": "최고", "description": "가장(最) 높은(高) 상태입니다." }
    ]
  },
  {
    "kanji": "黄",
    "reading_on": "コウ、オウ",
    "reading_kun": "き",
    "meaning": "누르다 (노랗다)",
    "components": [
      { "char": "廿", "role": "스물 입 (요소)", "desc": "두 손으로 무언가를 잡거나 불을 켜는 모습입니다." },
      { "char": "由", "role": "말미암을 유 (요소)", "desc": "불씨가 들어있는 화로나 흙을 뜻합니다." },
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "빛이 퍼지는 모양입니다." }
    ],
    "story": "흙바닥에 화로(由)를 놓고 불을 켜서 빛(八)이 번지는 노르스름한 색깔에서 '노랗다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "黄色", "reading": "きいろ", "meaning": "노란색", "description": "노란(黄) 빛깔(色)을 뜻합니다." },
      { "word": "黄金", "reading": "おうごん", "meaning": "황금", "description": "노란(黄) 쇠(金), 즉 금을 뜻합니다." }
    ]
  },
  {
    "kanji": "合",
    "reading_on": "ゴウ、ガッ",
    "reading_kun": "あ(う)、あ(わせる)",
    "meaning": "합하다 / 맞다",
    "components": [
      { "char": "亼", "role": "모일 집 (요소)", "desc": "뚜껑을 덮어 모아놓은 모습입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "그릇이나 입을 뜻합니다." }
    ],
    "story": "그릇(口)에 뚜껑(亼)을 꼭 덮어서 틈 없이 '합치다' 혹은 서로 딱 '맞다'라는 뜻입니다.",
    "example_words": [
      { "word": "合計", "reading": "ごうけい", "meaning": "합계", "description": "모두 합하여(合) 셈한(計) 수량입니다." },
      { "word": "試合", "reading": "しあい", "meaning": "시합", "description": "서로 기술을 시험(試)하며 맞붙는(合) 것입니다." }
    ]
  },
  {
    "kanji": "谷",
    "reading_on": "コク",
    "reading_kun": "たに",
    "meaning": "골짜기",
    "components": [
      { "char": "八", "role": "여덟 팔 (요소)", "desc": "물이 양쪽으로 갈라져 흐르는 모습입니다." },
      { "char": "人口", "role": "계곡 모양 (부수)", "desc": "위가 좁고 아래가 넓은 계곡의 모습을 단순화한 형태입니다." }
    ],
    "story": "물이 갈라져(八) 흐르는 깊고 움푹한(人口) 산속의 '골짜기'를 그린 상형문자입니다.",
    "example_words": [
      { "word": "谷間", "reading": "たにま", "meaning": "골짜기 사이", "description": "산골짜기(谷)의 사이(間) 공간을 뜻합니다." },
      { "word": "渓谷", "reading": "けいこく", "meaning": "계곡", "description": "물이 흐르는 시내(渓)와 골짜기(谷)입니다." }
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

print("Grade 2 Part 3 (first half) data appended successfully.")
