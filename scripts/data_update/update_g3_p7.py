import json
import os

new_data = [
  {
    "kanji": "油",
    "reading_on": "ユ",
    "reading_kun": "あぶら",
    "meaning": "기름",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "由", "role": "말미암을 유 (요소)", "desc": "열매에서 뽑아낸다는 뜻과 발음 '유'를 줍니다." }
    ],
    "story": "열매(由)를 짜내어 얻은 끈적한 액체(氵)인 '기름'을 의미합니다.",
    "example_words": [
      { "word": "油", "reading": "あぶら", "meaning": "기름", "description": "물에 섞이지 않는 미끈한 액체입니다." },
      { "word": "石油", "reading": "せきゆ", "meaning": "석유", "description": "돌(石)이 있는 땅속에서 뽑아낸 기름(油)입니다." }
    ]
  },
  {
    "kanji": "有",
    "reading_on": "ユウ、ウ",
    "reading_kun": "あ(る)",
    "meaning": "있을",
    "components": [
      { "char": "𠂇", "role": "왼손 좌 (요소)", "desc": "손을 의미합니다." },
      { "char": "月", "role": "달 월 (부수)", "desc": "고기나 제물(肉의 변형)을 뜻합니다." }
    ],
    "story": "오른손(𠂇)에 고기(月)를 쥐고 있는 모습에서 고기를 쥐고 '있다' 혹은 소유하다는 의미가 되었습니다.",
    "example_words": [
      { "word": "有る", "reading": "ある", "meaning": "있다", "description": "물건이 존재하거나 손에 쥐고 있는 것입니다." },
      { "word": "有名", "reading": "ゆうめい", "meaning": "유명", "description": "이름(名)이 널리 알려져 있는(有) 상태입니다." }
    ]
  },
  {
    "kanji": "遊",
    "reading_on": "ユウ、ユ",
    "reading_kun": "あそ(ぶ)",
    "meaning": "놀",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "돌아다니거나 길을 감을 뜻합니다." },
      { "char": "斿", "role": "깃발 유 (요소)", "desc": "깃발이 펄럭이는 모양으로 이리저리 흔들린다는 뜻과 발음 '유/유우'를 줍니다." }
    ],
    "story": "깃발(斿)이 바람에 이리저리 펄럭이듯, 마음 내키는 대로 여기저기 돌아다니며(辶) 즐겁게 '놀다'라는 뜻입니다.",
    "example_words": [
      { "word": "遊ぶ", "reading": "あそぶ", "meaning": "놀다", "description": "즐겁게 놀거나 이리저리 돌아다니며 쉬는 것입니다." },
      { "word": "遊園地", "reading": "ゆうえんち", "meaning": "유원지, 놀이공원", "description": "가서 즐겁게 노는(遊) 동산(園)과 땅(地)입니다." }
    ]
  },
  {
    "kanji": "予",
    "reading_on": "ヨ",
    "reading_kun": "",
    "meaning": "미리 (나)",
    "components": [
      { "char": "予", "role": "나 여 (부수)", "desc": "베틀에서 씨줄을 북에 감아 서로 밀고 당기는 모양에서 유래했습니다." }
    ],
    "story": "베틀에서 씨줄을 좌우로 밀고 당기며 여유를 둔다는 데서, 시간적 여유를 두고 '미리' 한다는 뜻이나 자신을 가리키는 '나'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "予定", "reading": "よてい", "meaning": "예정", "description": "미리(予) 정해두는(定) 것입니다." },
      { "word": "予想", "reading": "よそう", "meaning": "예상", "description": "미리(予) 짐작하여 생각하는(想) 것입니다." }
    ]
  },
  {
    "kanji": "羊",
    "reading_on": "ヨウ",
    "reading_kun": "ひつじ",
    "meaning": "양",
    "components": [
      { "char": "羊", "role": "양 양 (부수)", "desc": "머리에 뿔이 나 있고 털이 북실북실한 양의 모양을 본뜬 글자입니다." }
    ],
    "story": "구부러진 두 개의 뿔과 북실북실한 털을 가진 순한 동물인 '양'을 그렸습니다.",
    "example_words": [
      { "word": "羊", "reading": "ひつじ", "meaning": "양", "description": "털을 얻거나 기르는 동물인 양입니다." },
      { "word": "羊毛", "reading": "ようもう", "meaning": "양모", "description": "양(羊)의 털(毛)입니다." }
    ]
  },
  {
    "kanji": "洋",
    "reading_on": "ヨウ",
    "reading_kun": "",
    "meaning": "큰 바다 (서양)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 바다를 뜻합니다." },
      { "char": "羊", "role": "양 양 (요소)", "desc": "크다, 멀리 뻗어 있다는 뜻(크고 아름답다는 의미에서 확장)과 발음 '양/요우'를 담당합니다." }
    ],
    "story": "넓고 크게(羊) 끝없이 펼쳐진 물(氵), 즉 '큰 바다'를 의미하며 먼 바다 건너의 '서양'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "洋服", "reading": "ようふく", "meaning": "양복", "description": "서양(洋)식으로 만든 옷(服)입니다." },
      { "word": "太平洋", "reading": "たいへいよう", "meaning": "태평양", "description": "가장 크고 태평한(太平) 큰 바다(洋)입니다." }
    ]
  },
  {
    "kanji": "葉",
    "reading_on": "ヨウ",
    "reading_kun": "は",
    "meaning": "잎",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 풀을 의미합니다." },
      { "char": "枼", "role": "나뭇잎 엽 (요소)", "desc": "나무(木) 위에 얇고 평평하게 달린 잎들을 뜻하며 발음 '엽/요우'를 줍니다." }
    ],
    "story": "나무(木)나 식물(艹)의 가지 끝에 얇고 평평하게 달려 있는 '잎'사귀를 뜻합니다.",
    "example_words": [
      { "word": "葉", "reading": "は", "meaning": "나뭇잎", "description": "식물의 잎사귀입니다." },
      { "word": "言葉", "reading": "ことば", "meaning": "말, 언어", "description": "말(言)이 나뭇잎(葉)처럼 무성하게 이어진 것, 즉 언어입니다." }
    ]
  },
  {
    "kanji": "陽",
    "reading_on": "ヨウ",
    "reading_kun": "ひ",
    "meaning": "볕",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "산이나 언덕을 뜻합니다." },
      { "char": "昜", "role": "볕 양 (요소)", "desc": "태양이 높이 떠서 빛이 환하게 비추는 모양과 발음 '양/요우'를 줍니다." }
    ],
    "story": "산언덕(阝) 위로 해가 높이 떠올라(昜) 따뜻하고 밝은 햇'볕'이 내리쬐는 곳을 뜻합니다.",
    "example_words": [
      { "word": "太陽", "reading": "たいよう", "meaning": "태양", "description": "크고(太) 밝은 볕(陽)을 내뿜는 별입니다." },
      { "word": "陽気", "reading": "ようき", "meaning": "명랑함, 날씨", "description": "볕(陽)처럼 밝은 기운(気)이나 성격입니다." }
    ]
  },
  {
    "kanji": "様",
    "reading_on": "ヨウ",
    "reading_kun": "さま",
    "meaning": "모양 / 님",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 틀을 뜻합니다." },
      { "char": "羕", "role": "길 영 (요소)", "desc": "양(羊)이 물(水)처럼 길게 이어진다는 데서 어떤 모양이나 패턴, 발음 '양/요우'를 뜻합니다." }
    ],
    "story": "나무(木)로 어떤 무늬나 패턴(羕)을 조각하여 만든 틀의 '모양'을 뜻하며, 나중에는 남을 높여 부르는 '님'이라는 뜻으로도 쓰이게 되었습니다.",
    "example_words": [
      { "word": "様子", "reading": "ようす", "meaning": "모양, 낌새", "description": "겉으로 드러난 모양(様)과 모습입니다." },
      { "word": "お客様", "reading": "おきゃくさま", "meaning": "손님 (극존칭)", "description": "손님(客)을 아주 높여 부르는 님(様)입니다." }
    ]
  },
  {
    "kanji": "落",
    "reading_on": "ラク",
    "reading_kun": "お(ちる)、お(とす)",
    "meaning": "떨어질",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 잎사귀를 뜻합니다." },
      { "char": "洛", "role": "물 이름 락 (요소)", "desc": "물이 위에서 아래로 흘러내린다는 뜻과 발음 '락/라쿠'를 줍니다." }
    ],
    "story": "가을이 되어 나뭇잎(艹)이 물(洛)이 흘러내리듯 바닥으로 '떨어지다'는 뜻입니다.",
    "example_words": [
      { "word": "落ちる", "reading": "おちる", "meaning": "떨어지다", "description": "위에서 아래로 내려지거나 시험에 불합격하는 것입니다." },
      { "word": "落し物", "reading": "おとしもの", "meaning": "분실물", "description": "실수로 떨어뜨린(落し) 물건(物)입니다." }
    ]
  },
  {
    "kanji": "流",
    "reading_on": "リュウ、ル",
    "reading_kun": "なが(れる)、なが(す)",
    "meaning": "흐를",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "㐬", "role": "아기 날 돌 (요소)", "desc": "어머니 뱃속에서 양수와 함께 태어나는 아이의 모습으로 물이 콸콸 쏟아진다는 뜻을 줍니다." }
    ],
    "story": "아기가 양수와 함께 나오듯(㐬), 강물(氵)이 거침없이 계속 이어져 아래로 '흐르다'라는 의미입니다.",
    "example_words": [
      { "word": "流れる", "reading": "ながれる", "meaning": "흐르다", "description": "물이 낮은 곳으로 이동하거나 시간이 지나가는 것입니다." },
      { "word": "流行", "reading": "りゅうこう", "meaning": "유행", "description": "어떤 현상이 흘러서(流) 퍼져 가는(行) 일입니다." }
    ]
  },
  {
    "kanji": "旅",
    "reading_on": "リョ",
    "reading_kun": "たび",
    "meaning": "나그네 (여행)",
    "components": [
      { "char": "方", "role": "모방 (부수)", "desc": "여기서는 군대나 사람들이 모여 펄럭이는 깃발(㫃)의 변형입니다." },
      { "char": "氏", "role": "성 씨 (요소)", "desc": "여러 사람들이 줄지어 따라가는 모양입니다." }
    ],
    "story": "깃발(方의 변형)을 든 대장을 따라 여러 사람(氏의 변형)이 줄지어 먼 길을 떠나는 모습에서, 집을 떠난 '나그네'나 '여행'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "旅行", "reading": "りょこう", "meaning": "여행", "description": "나그네(旅)가 되어 먼 길을 가는(行) 일입니다." },
      { "word": "旅", "reading": "たび", "meaning": "여행", "description": "집을 떠나 다른 곳으로 가는 일입니다." }
    ]
  },
  {
    "kanji": "両",
    "reading_on": "リョウ",
    "reading_kun": "",
    "meaning": "두 / 양",
    "components": [
      { "char": "一", "role": "한 일 (부수)", "desc": "저울의 저울대 모양입니다." },
      { "char": "入", "role": "들 입 (요소)", "desc": "여기서는 저울의 양쪽 끝에 걸린 두 개의 짐을 나타내는 상형입니다." }
    ],
    "story": "저울대(一)의 양쪽 끝에 똑같은 무게의 짐(入 두 개)을 매달아 놓은 모양에서, 어느 한쪽이 아닌 '둘' 혹은 '양쪽'을 의미합니다.",
    "example_words": [
      { "word": "両方", "reading": "りょうほう", "meaning": "양쪽", "description": "두(両) 방향(方) 모두를 뜻합니다." },
      { "word": "両親", "reading": "りょうしん", "meaning": "양친, 부모님", "description": "두(両) 분의 어버이(親)입니다." }
    ]
  },
  {
    "kanji": "緑",
    "reading_on": "リョク、ロク",
    "reading_kun": "みどり",
    "meaning": "초록빛 (녹색)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 옷감을 뜻합니다." },
      { "char": "彔", "role": "나무새길 록 (요소)", "desc": "나무를 깎아 벗길 때 나오는 푸른색의 진액을 뜻하며 발음 '록/료쿠'를 줍니다." }
    ],
    "story": "나무 진액(彔)에서 얻은 푸른빛 염료로 물들인 실(糸)이나 옷감, 즉 푸르고 신선한 '초록빛'을 의미합니다.",
    "example_words": [
      { "word": "緑", "reading": "みどり", "meaning": "초록색, 녹색", "description": "풀이나 나뭇잎과 같은 푸른색입니다." },
      { "word": "新緑", "reading": "しんりょく", "meaning": "신록", "description": "새로(新) 돋아난 초록빛(緑) 잎입니다." }
    ]
  },
  {
    "kanji": "礼",
    "reading_on": "レイ、ライ",
    "reading_kun": "",
    "meaning": "예도",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "신을 모시는 제단이나 의식을 뜻합니다." },
      { "char": "乙", "role": "새을 (요소)", "desc": "제단에 바치는 제물을 담은 그릇(豊의 간략화된 모양)을 나타냅니다." }
    ],
    "story": "신을 모시는 제단(示)에 예쁜 그릇(乙의 원래 형태)에 담은 제물을 바치며 정성껏 절하고 섬기는 '예의'나 '예도'를 의미합니다.",
    "example_words": [
      { "word": "お礼", "reading": "おれい", "meaning": "감사 인사, 답례", "description": "고마움을 나타내는 예의(礼)나 인사입니다." },
      { "word": "失礼", "reading": "しつれい", "meaning": "실례", "description": "예의(礼)를 잃거나(失) 어긋나는 행동입니다." }
    ]
  },
  {
    "kanji": "列",
    "reading_on": "レツ",
    "reading_kun": "",
    "meaning": "벌일 (줄)",
    "components": [
      { "char": "歹", "role": "부서진 뼈 알 (요소)", "desc": "죽은 짐승이나 뼈를 뜻합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 베거나 자른다는 뜻입니다." }
    ],
    "story": "죽은 짐승의 뼈나 고기(歹)를 칼(刂)로 반듯하게 잘라 보기 좋게 '벌려 놓다' 혹은 나란히 세운 '줄(대열)'을 뜻합니다.",
    "example_words": [
      { "word": "行列", "reading": "ぎょうれつ", "meaning": "행렬", "description": "줄(列)을 지어 가는(行) 사람이나 차입니다." },
      { "word": "列車", "reading": "れっしゃ", "meaning": "열차", "description": "길게 줄(列)을 지어 이어진 기차(車)입니다." }
    ]
  },
  {
    "kanji": "練",
    "reading_on": "レン",
    "reading_kun": "ね(る)",
    "meaning": "익힐 (단련할)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 의미합니다." },
      { "char": "東", "role": "동녘 동 (요소)", "desc": "여기서는 원래 柬(가릴 간) 자가 간략화된 것으로 무언가를 끓는 물에 넣어 고르는 과정을 뜻합니다." }
    ],
    "story": "거친 명주실(糸)을 끓는 물에 여러 번 삶고 골라내어(東의 원래 형태) 부드럽고 질기게 만드는 과정에서 유래하여, 기술을 반복해 갈고 닦아 '익히다(단련하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "練習", "reading": "れんしゅう", "meaning": "연습", "description": "실을 다듬듯 반복하여 익히고(練) 배우는(習) 일입니다." },
      { "word": "練る", "reading": "ねる", "meaning": "단련하다, 반죽하다", "description": "기술을 닦거나 가루를 치대어 부드럽게 만드는 것입니다." }
    ]
  },
  {
    "kanji": "路",
    "reading_on": "ロ",
    "reading_kun": "じ",
    "meaning": "길",
    "components": [
      { "char": "足", "role": "발 족 (부수)", "desc": "사람의 발이나 걷는 동작을 의미합니다." },
      { "char": "各", "role": "각각 각 (요소)", "desc": "발이 닿아 이르는 각각의 장소를 뜻하며 발음 '로/로'를 줍니다." }
    ],
    "story": "사람의 발(足)이 이르는(各) 곳으로 이어지는 커다란 '길'이나 통로를 의미합니다.",
    "example_words": [
      { "word": "道路", "reading": "どうろ", "meaning": "도로", "description": "사람이나 차가 다닐 수 있게 만든 길(道)과 통로(路)입니다." },
      { "word": "線路", "reading": "せんろ", "meaning": "선로", "description": "기차가 다니는 선(線)이 깔린 길(路)입니다." }
    ]
  },
  {
    "kanji": "労",
    "reading_on": "ロウ",
    "reading_kun": "",
    "meaning": "일할",
    "components": [
      { "char": "ツ", "role": "머리 (요소)", "desc": "원래 𤇾(형광 불꽃) 자가 간략화된 것으로, 불빛이나 등불을 뜻합니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "지붕이나 장소를 덮는 모양입니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘을 쓴다, 일한다는 뜻입니다." }
    ],
    "story": "지붕(冖) 아래에서 밤늦게까지 불(ツ의 원래 형태)을 밝혀 놓고 힘(力)을 다해 열심히 '일하다(수고하다)'는 뜻입니다.",
    "example_words": [
      { "word": "労働", "reading": "ろうどう", "meaning": "노동", "description": "힘써 일하고(労) 몸을 움직이는(動) 것입니다." },
      { "word": "苦労", "reading": "くろう", "meaning": "고생, 수고", "description": "괴롭고(苦) 힘들게 일하는(労) 것입니다." }
    ]
  },
  {
    "kanji": "和",
    "reading_on": "ワ、オ",
    "reading_kun": "やわ(らぐ)、やわ(らげる)、なご(む)、なご(やか)",
    "meaning": "화할 (화목하다)",
    "components": [
      { "char": "禾", "role": "벼 화 (요소)", "desc": "곡식이나 식량을 의미합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "사람의 입이나 먹는 것을 뜻합니다." }
    ],
    "story": "곡식(禾)을 여러 사람의 입(口)에 골고루 나누어 먹으며 서로 싸우지 않고 '화목하다' 혹은 부드럽고 '온화하다'는 뜻이 되었으며, 나중에 '일본'을 뜻하는 한자로도 쓰이게 되었습니다.",
    "example_words": [
      { "word": "平和", "reading": "へいわ", "meaning": "평화", "description": "평평하고(平) 화목하게(和) 다툼이 없는 상태입니다." },
      { "word": "和食", "reading": "わしょく", "meaning": "일식", "description": "일본(和)의 전통 음식(食)입니다." }
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

print("Grade 3 Part 7 data appended successfully.")
