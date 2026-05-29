import json
import os

new_data = [
  {
    "kanji": "客",
    "reading_on": "キャク、カク",
    "reading_kun": "",
    "meaning": "손님",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "건물이나 지붕을 뜻합니다." },
      { "char": "各", "role": "각각 각 (요소)", "desc": "각기 다른 곳에서 모여든다는 뜻과 '각/객' 발음을 담당합니다." }
    ],
    "story": "지붕(宀)이 있는 집에 각기 다른(各) 곳에서 모여 찾아온 '손님'을 뜻합니다.",
    "example_words": [
      { "word": "お客さん", "reading": "おきゃくさん", "meaning": "손님", "description": "손님을 친근하고 높여 부르는 말입니다." },
      { "word": "乗客", "reading": "じょうきゃく", "meaning": "승객", "description": "차나 배에 타고(乗) 있는 손님(客)입니다." }
    ]
  },
  {
    "kanji": "究",
    "reading_on": "キュウ",
    "reading_kun": "きわ(める)",
    "meaning": "연구할 / 다할",
    "components": [
      { "char": "穴", "role": "구멍 혈 (부수)", "desc": "동굴이나 구멍을 뜻합니다." },
      { "char": "九", "role": "아홉 구 (요소)", "desc": "끝까지 구부러진 길이나 발음 '구/큐'를 나타냅니다." }
    ],
    "story": "동굴이나 구멍(穴)의 맨 끝(九)까지 깊이 파고들어 사물의 이치를 '연구하다' 혹은 끝까지 '다하다'는 뜻입니다.",
    "example_words": [
      { "word": "研究", "reading": "けんきゅう", "meaning": "연구", "description": "돌을 갈듯 자세히 살피고(研) 끝까지 파고들어(究) 진리를 찾는 일입니다." },
      { "word": "探究", "reading": "たんきゅう", "meaning": "탐구", "description": "찾고(探) 연구하는(究) 것입니다." }
    ]
  },
  {
    "kanji": "急",
    "reading_on": "キュウ",
    "reading_kun": "いそ(ぐ)",
    "meaning": "급할 / 서두르다",
    "components": [
      { "char": "ク", "role": "안을 포 (요소)", "desc": "사람의 굽어진 모양입니다." },
      { "char": "ヨ", "role": "돼지머리 계 (요소)", "desc": "손으로 무언가를 다급히 쥐거나 당기는 모양입니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 마음을 뜻합니다." }
    ],
    "story": "사람이(ク) 물건을 급하게 잡아당기는(ヨ) 다급한 마음(心) 상태에서 유래하여 '급하다'나 '서두르다'를 뜻합니다.",
    "example_words": [
      { "word": "急ぐ", "reading": "いそぐ", "meaning": "서두르다", "description": "어떤 일을 빨리하려고 다급하게 움직이는 것입니다." },
      { "word": "急行", "reading": "きゅうこう", "meaning": "급행", "description": "급하게(急) 서둘러 가는(行) 기차나 일입니다." }
    ]
  },
  {
    "kanji": "級",
    "reading_on": "キュウ",
    "reading_kun": "",
    "meaning": "등급 / 급",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실, 이어짐을 뜻합니다." },
      { "char": "及", "role": "미칠 급 (요소)", "desc": "어떤 곳에 다다르다, 혹은 발음 '급/큐'를 줍니다." }
    ],
    "story": "실(糸)을 차례대로 매듭지어 이어가는 것처럼 어떤 기준에 다다르는(及) 단계나 '등급'을 의미합니다.",
    "example_words": [
      { "word": "階級", "reading": "かいきゅう", "meaning": "계급", "description": "계단(階)처럼 나누어진 신분이나 등급(級)입니다." },
      { "word": "高級", "reading": "こうきゅう", "meaning": "고급", "description": "높은(高) 등급(級)입니다." }
    ]
  },
  {
    "kanji": "宮",
    "reading_on": "キュウ、グウ、ク",
    "reading_kun": "みや",
    "meaning": "집 / 궁궐",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 건물을 의미합니다." },
      { "char": "呂", "role": "등뼈 려 (요소)", "desc": "방들이 등뼈처럼 길게 여러 개 이어져 있는 모습을 뜻합니다." }
    ],
    "story": "큰 지붕(宀) 아래에 방들이 등뼈(呂)처럼 여러 채 길게 이어져 있는 크고 화려한 집, 즉 '궁궐'이나 '신사'를 뜻합니다.",
    "example_words": [
      { "word": "王宮", "reading": "おうきゅう", "meaning": "왕궁", "description": "왕(王)이 머무는 궁궐(宮)입니다." },
      { "word": "お宮", "reading": "おみや", "meaning": "신사", "description": "일본에서 신을 모시는 사당을 높여 부르는 말입니다." }
    ]
  },
  {
    "kanji": "球",
    "reading_on": "キュウ",
    "reading_kun": "たま",
    "meaning": "공",
    "components": [
      { "char": "王", "role": "구슬 옥 (부수)", "desc": "보석이나 둥근 옥(玉)이 간략화된 것입니다." },
      { "char": "求", "role": "구할 구 (요소)", "desc": "발음 '구/큐'를 나타내며, 둥글게 뭉친 털 모양에서 유래했습니다." }
    ],
    "story": "아름다운 옥(王)을 둥글게 다듬어 놓은 모양에서 유래하여 둥근 '공'이나 '구슬'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "野球", "reading": "やきゅう", "meaning": "야구", "description": "들판(野)처럼 넓은 곳에서 공(球)을 치는 경기입니다." },
      { "word": "地球", "reading": "ちきゅう", "meaning": "지구", "description": "우리가 사는 둥근 땅(地) 모양의 공(球)입니다." }
    ]
  },
  {
    "kanji": "去",
    "reading_on": "キョ、コ",
    "reading_kun": "さ(る)",
    "meaning": "갈 / 떠나다",
    "components": [
      { "char": "土", "role": "흙 토 (요소)", "desc": "여기서는 큰 사람(大)의 모양이 변형된 것입니다." },
      { "char": "厶", "role": "마늘 모 (부수)", "desc": "여기서는 발을 덮거나 굽힌 모양을 나타내어 어떤 곳을 떠남을 뜻합니다." }
    ],
    "story": "사람(土)이 자신이 있던 곳을 떠나서 등지고 멀리 '가버리다' 혹은 '떠나다'는 의미를 가집니다.",
    "example_words": [
      { "word": "過去", "reading": "かこ", "meaning": "과거", "description": "이미 지나쳐(過) 가버린(去) 시간입니다." },
      { "word": "立ち去る", "reading": "たちさる", "meaning": "떠나다, 물러가다", "description": "서 있던(立ち) 곳에서 떠나가는(去る) 것입니다." }
    ]
  },
  {
    "kanji": "橋",
    "reading_on": "キョウ",
    "reading_kun": "はし",
    "meaning": "다리",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "喬", "role": "높을 교 (요소)", "desc": "높고 둥글게 휘어진 모양을 뜻하며 발음 '교/쿄'를 담당합니다." }
    ],
    "story": "나무(木)를 사용하여 물이나 계곡 위로 높이 둥글게(喬) 휘어지게 걸쳐놓은 '다리'를 뜻합니다.",
    "example_words": [
      { "word": "歩道橋", "reading": "ほどうきょう", "meaning": "육교", "description": "사람이 걸어(歩) 다니는 길(道) 위에 놓은 다리(橋)입니다." },
      { "word": "鉄橋", "reading": "てっきょう", "meaning": "철교", "description": "쇠(鉄)로 만든 다리(橋)입니다." }
    ]
  },
  {
    "kanji": "業",
    "reading_on": "ギョウ、ゴウ",
    "reading_kun": "わざ",
    "meaning": "업 (일)",
    "components": [
      { "char": "业", "role": "풀 더미 (요소)", "desc": "악기를 거는 나무 틀의 윗부분 혹은 복잡한 장식을 뜻합니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." }
    ],
    "story": "원래 종이나 악기를 매달기 위해 나무(木)로 복잡하게(业) 짠 큰 틀을 의미하다가, 복잡하고 중요한 '업무'나 '직업'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "仕事", "reading": "しごと", "meaning": "일", "description": "해야 할 업(業)이나 직업을 뜻합니다. (단어는 '사/일'을 씁니다. 주의!)" },
      { "word": "授業", "reading": "じゅぎょう", "meaning": "수업", "description": "지식이나 학업(業)을 받는(授) 시간입니다." },
      { "word": "職業", "reading": "しょくぎょう", "meaning": "직업", "description": "맡은 직분(職)과 일(業)입니다." }
    ]
  },
  {
    "kanji": "曲",
    "reading_on": "キョク",
    "reading_kun": "ま(がる)、ま(げる)",
    "meaning": "굽을",
    "components": [
      { "char": "曲", "role": "굽을 곡 (부수)", "desc": "대나무나 나뭇가지로 짠 굽은 바구니의 모양을 본뜬 상형문자입니다." }
    ],
    "story": "대나무를 둥글게 휘어서 만든 바구니의 모습에서 '굽다'나 '휘어지다'는 뜻이 되었으며, 노래의 굽이치는 가락인 '곡'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "曲がる", "reading": "まがる", "meaning": "굽다, 구부러지다", "description": "길이나 물건이 휘어져 굽는 것입니다." },
      { "word": "名曲", "reading": "めいきょく", "meaning": "명곡", "description": "이름난(名) 좋은 곡(曲)입니다." }
    ]
  },
  {
    "kanji": "局",
    "reading_on": "キョク",
    "reading_kun": "",
    "meaning": "판 / 국",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "집의 지붕이나 사람이 쭈그려 앉은 모양을 뜻합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "칸막이로 나누어진 공간이나 구역을 의미합니다." }
    ],
    "story": "지붕(尸) 아래 칸막이(口)로 구역이 나뉜 사무실의 모습에서, 부서나 부문을 뜻하는 '국' 혹은 바둑의 한 '판'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "郵便局", "reading": "ゆうびんきょく", "meaning": "우체국", "description": "우편(郵便) 업무를 맡아보는 관청(局)입니다." },
      { "word": "薬局", "reading": "やっきょく", "meaning": "약국", "description": "약(薬)을 짓고 파는 가게(局)입니다." }
    ]
  },
  {
    "kanji": "銀",
    "reading_on": "ギン",
    "reading_kun": "",
    "meaning": "은",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "금속을 뜻합니다." },
      { "char": "艮", "role": "어긋날 간 (요소)", "desc": "발음 '간/은'을 나타내며, 하얗게 빛나는 눈빛을 뜻하기도 합니다." }
    ],
    "story": "금속(金) 중에서 마치 눈빛(艮)처럼 하얗게 빛나는 귀금속인 '은'을 의미합니다.",
    "example_words": [
      { "word": "銀行", "reading": "ぎんこう", "meaning": "은행", "description": "돈(銀)을 다루고 거래하는 기관(行)입니다." },
      { "word": "銀色", "reading": "ぎんいろ", "meaning": "은색", "description": "은(銀)빛 색깔(色)입니다." }
    ]
  },
  {
    "kanji": "区",
    "reading_on": "ク",
    "reading_kun": "",
    "meaning": "구역",
    "components": [
      { "char": "匚", "role": "터진입구 (부수)", "desc": "상자나 물건을 담는 테두리를 뜻합니다." },
      { "char": "メ", "role": "벨 예 (요소)", "desc": "원래 품(品) 자가 간략화된 것으로, 여러 물건이 나뉘어 있는 모양을 뜻합니다." }
    ],
    "story": "상자(匚) 안을 가로세로로(メ) 칸막이를 쳐서 나누어 둔 특정한 '구역'이나 '지역'을 의미합니다.",
    "example_words": [
      { "word": "区別", "reading": "くべつ", "meaning": "구별", "description": "구역(区)을 나누어 다르게(別) 판단하는 것입니다." },
      { "word": "地区", "reading": "ちく", "meaning": "지구, 지역", "description": "땅(地)을 나눈 구역(区)입니다." }
    ]
  },
  {
    "kanji": "苦",
    "reading_on": "ク",
    "reading_kun": "くる(しい)、にが(い)",
    "meaning": "쓸 / 괴롭다",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 식물을 뜻합니다." },
      { "char": "古", "role": "예 고 (요소)", "desc": "오래되었다는 뜻이며 '고/쿠' 발음을 담당합니다." }
    ],
    "story": "오래되어(古) 말라비틀어진 풀(艹)이나 씀바귀처럼 맛이 아주 '쓰다'거나, 그 쓴맛처럼 견디기 '괴롭다'는 의미입니다.",
    "example_words": [
      { "word": "苦しい", "reading": "くるしい", "meaning": "괴롭다", "description": "몸이나 마음이 몹시 견디기 힘든 상태입니다." },
      { "word": "苦い", "reading": "にがい", "meaning": "쓰다", "description": "맛이 쓴 상태를 뜻합니다." }
    ]
  },
  {
    "kanji": "具",
    "reading_on": "グ",
    "reading_kun": "",
    "meaning": "갖출 (도구)",
    "components": [
      { "char": "貝", "role": "조개 패 (요소)", "desc": "여기서는 돈이나 귀중한 솥을 나타내는 鼎(솥 정) 자의 변형입니다." },
      { "char": "廾", "role": "두 손 멱 (부수)", "desc": "두 손으로 잡는 모양입니다." }
    ],
    "story": "두 손(廾)으로 커다란 솥(貝) 같은 중요한 도구를 갖추어 들고 있는 모습에서, 필요한 물건을 '갖추다' 혹은 '도구'를 뜻합니다.",
    "example_words": [
      { "word": "道具", "reading": "どうぐ", "meaning": "도구", "description": "어떤 길(道)이나 일에 갖추어(具) 쓰는 물건입니다." },
      { "word": "家具", "reading": "かぐ", "meaning": "가구", "description": "집안(家)에 갖추어(具) 두는 물건입니다." }
    ]
  },
  {
    "kanji": "君",
    "reading_on": "クン",
    "reading_kun": "きみ",
    "meaning": "임금 / 그대",
    "components": [
      { "char": "尹", "role": "다스릴 윤 (요소)", "desc": "손에 지휘봉이나 펜을 들고 다스리는 모습입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입으로 명령을 내리는 모양입니다." }
    ],
    "story": "손에 지휘봉을 들고(尹) 입(口)으로 명령을 내려 백성을 다스리는 '임금'을 뜻하며, 나중에는 친근하게 '그대(너)'를 부르는 말로도 쓰이게 되었습니다.",
    "example_words": [
      { "word": "君", "reading": "きみ", "meaning": "너, 자네", "description": "동년배나 아랫사람을 친근하게 부르는 대명사입니다." },
      { "word": "〜君", "reading": "〜くん", "meaning": "~군", "description": "주로 남자 이름 뒤에 붙이는 호칭입니다." }
    ]
  },
  {
    "kanji": "係",
    "reading_on": "ケイ",
    "reading_kun": "かか(る)、かかり",
    "meaning": "걸릴 / 담당자",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "系", "role": "이을 계 (요소)", "desc": "실타래가 계속 이어져 있는 모양으로, 묶이거나 연결된다는 뜻입니다." }
    ],
    "story": "사람(亻)이 어떤 일이나 조직에 실(系)처럼 연결되어 '관계'를 맺거나 그 일을 '담당하다'라는 뜻입니다.",
    "example_words": [
      { "word": "関係", "reading": "かんけい", "meaning": "관계", "description": "둘 이상의 사람이나 사물이 서로 얽혀(関) 이어진(係) 상태입니다." },
      { "word": "係員", "reading": "かかりいん", "meaning": "담당자", "description": "어떤 일을 담당하는(係) 인원(員)입니다." }
    ]
  },
  {
    "kanji": "軽",
    "reading_on": "ケイ",
    "reading_kun": "かる(い)",
    "meaning": "가벼울",
    "components": [
      { "char": "車", "role": "수레 거 (부수)", "desc": "수레나 차를 의미합니다." },
      { "char": "巠", "role": "물줄기 경 (요소)", "desc": "베틀에서 세로로 팽팽하게 쳐진 실줄기로, 곧게 뻗어 나가며 발음 '경/케이'를 줍니다." }
    ],
    "story": "수레(車)에 베틀의 실(巠)처럼 가볍고 곧게 뻗은 물건만 실어서 움직임이 빠르고 '가볍다'는 뜻입니다.",
    "example_words": [
      { "word": "軽い", "reading": "かるい", "meaning": "가볍다", "description": "무게가 적거나 마음이 편안한 상태입니다." },
      { "word": "軽食", "reading": "けいしょく", "meaning": "경식, 간식", "description": "가볍게(軽) 먹는 식사(食)입니다." }
    ]
  },
  {
    "kanji": "血",
    "reading_on": "ケツ",
    "reading_kun": "ち",
    "meaning": "피",
    "components": [
      { "char": "皿", "role": "그릇 명 (부수)", "desc": "제사에 쓰이는 그릇입니다." },
      { "char": "丿", "role": "삐침 (요소)", "desc": "그릇 안에 담긴 핏방울이나 덩어리를 나타냅니다." }
    ],
    "story": "제사를 지낼 때 그릇(皿) 안에 바쳐진 짐승의 '피' 방울(丿)이 담겨 있는 모습을 본뜬 글자입니다.",
    "example_words": [
      { "word": "血圧", "reading": "けつあつ", "meaning": "혈압", "description": "피(血)가 혈관에 미치는 압력(圧)입니다." },
      { "word": "鼻血", "reading": "はなぢ", "meaning": "코피", "description": "코(鼻)에서 나는 피(血)입니다." }
    ]
  },
  {
    "kanji": "決",
    "reading_on": "ケツ",
    "reading_kun": "き(める)、き(まる)",
    "meaning": "결단할 / 정하다",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "夬", "role": "깍지 결 (요소)", "desc": "활시위를 당길 때 엄지손가락에 끼우는 도구로, 활시위를 놓듯 툭 끊어낸다는 뜻과 발음 '결'을 줍니다." }
    ],
    "story": "막혀 있던 둑을 터서 물(氵)이 한꺼번에 활시위처럼 툭 끊어지며(夬) 쏟아지게 하여 물길을 확고히 '결정하다'는 뜻입니다.",
    "example_words": [
      { "word": "決める", "reading": "きめる", "meaning": "정하다", "description": "어떤 일을 확실하게 결정하는 것입니다." },
      { "word": "解決", "reading": "かいけつ", "meaning": "해결", "description": "얽힌 문제를 풀어서(解) 결단 내리는(決) 일입니다." }
    ]
  },
  {
    "kanji": "研",
    "reading_on": "ケン",
    "reading_kun": "と(ぐ)",
    "meaning": "갈 (연구할)",
    "components": [
      { "char": "石", "role": "돌 석 (부수)", "desc": "단단한 돌을 의미합니다." },
      { "char": "幵", "role": "평평할 견 (요소)", "desc": "두 물건이 평평하게 나란히 있는 모양으로 발음 '견/켄'을 줍니다." }
    ],
    "story": "돌(石) 표면을 반듯하고 평평하게(幵) '갈고 닦는' 모습에서, 학문이나 기술을 깊이 파고들어 '연구하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "研究", "reading": "けんきゅう", "meaning": "연구", "description": "학문을 갈고(研) 다하여 파고드는(究) 것입니다." },
      { "word": "研ぐ", "reading": "とぐ", "meaning": "갈다", "description": "칼이나 쌀 따위를 문질러서 갈거나 씻는 것입니다." }
    ]
  },
  {
    "kanji": "県",
    "reading_on": "ケン",
    "reading_kun": "",
    "meaning": "고을 (현)",
    "components": [
      { "char": "目", "role": "눈 목 (요소)", "desc": "여기서는 원래 거꾸로 매달린 머리 모양(首의 거꾸로 된 형태)이 변형된 것입니다." },
      { "char": "糸", "role": "실 사 (요소)", "desc": "실로 묶었다는 뜻입니다." },
      { "char": "小", "role": "작을 소 (부수)", "desc": "매달려 있는 작은 조각들입니다." }
    ],
    "story": "원래는 나무에 머리를 실(糸)로 매달아(県의 고어인 현) 놓은 모양에서 유래하여, 중앙정부에 매달려 관리되는 지방 행정 구역인 '고을(현)'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "県知事", "reading": "けんちじ", "meaning": "현지사 (도지사)", "description": "도도부현 중 하나인 현(県)의 일(事)을 아는(知) 우두머리입니다." },
      { "word": "都道府県", "reading": "とどうふけん", "meaning": "도도부현", "description": "일본의 광역 자치 단체를 묶어 부르는 말입니다." }
    ]
  },
  {
    "kanji": "庫",
    "reading_on": "コ",
    "reading_kun": "",
    "meaning": "곳집 (창고)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "지붕이나 넓은 건물을 뜻합니다." },
      { "char": "車", "role": "수레 거 (요소)", "desc": "전차나 수레 등 물건을 의미합니다." }
    ],
    "story": "큰 지붕(广)이 덮인 건물 안에 중요한 전차나 수레(車)를 넣어 보관해 두는 '창고(곳집)'를 뜻합니다.",
    "example_words": [
      { "word": "金庫", "reading": "きんこ", "meaning": "금고", "description": "돈(金)을 보관하는 튼튼한 창고(庫)입니다." },
      { "word": "冷蔵庫", "reading": "れいぞうこ", "meaning": "냉장고", "description": "차갑게(冷) 간직해 두는(蔵) 창고(庫) 역할을 하는 기계입니다." }
    ]
  },
  {
    "kanji": "湖",
    "reading_on": "コ",
    "reading_kun": "みずうみ",
    "meaning": "호수",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 수역을 뜻합니다." },
      { "char": "胡", "role": "오랑캐 호 (요소)", "desc": "소가 목살을 길게 늘어뜨린 모양으로, 아주 길고 크다는 뜻과 발음 '호/코'를 담당합니다." }
    ],
    "story": "물이 모여(氵) 목살이 늘어진 것처럼 아주 길고 넓게 퍼져 있는 큰 연못, 즉 '호수'를 의미합니다.",
    "example_words": [
      { "word": "湖畔", "reading": "こはん", "meaning": "호숫가", "description": "호수(湖)의 기슭(畔)입니다." },
      { "word": "山中湖", "reading": "やまなかこ", "meaning": "야마나카호 (고유명사)", "description": "산(山) 한가운데(中) 있는 호수(湖)입니다." }
    ]
  },
  {
    "kanji": "向",
    "reading_on": "コウ",
    "reading_kun": "む(かう)、む(こう)",
    "meaning": "향할",
    "components": [
      { "char": "宀", "role": "갓머리 (요소)", "desc": "원래는 지붕이 아니라 북쪽을 향한 창문 구멍의 덮개 모양입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "창문 구멍이나 입구를 뜻합니다." }
    ],
    "story": "집의 벽(宀의 변형)에 낸 창문(口)을 통해 바깥쪽 방향을 '향하다' 혹은 '마주보다'라는 의미를 나타냅니다.",
    "example_words": [
      { "word": "向かう", "reading": "むかう", "meaning": "향하다", "description": "목적지를 향하여 나아가거나 마주 보는 것입니다." },
      { "word": "方向", "reading": "ほうこう", "meaning": "방향", "description": "어떤 쪽이나 곳(方)을 향하는(向) 것입니다." }
    ]
  },
  {
    "kanji": "幸",
    "reading_on": "コウ",
    "reading_kun": "しあわ(せ)、さいわ(い)",
    "meaning": "다행 / 행복",
    "components": [
      { "char": "大", "role": "큰 대 (요소)", "desc": "크다, 혹은 사람을 나타냅니다. (간자체 변형)" },
      { "char": "干", "role": "방패 간 (부수)", "desc": "원래 夭(어릴 요)와 屰(거스를 역)이 합쳐진 형태로, 큰 형벌(수갑)을 피한다는 뜻에서 유래했습니다." }
    ],
    "story": "원래 죄수에게 채우는 형틀(수갑)의 모양에서, 큰 형벌을 면하게 되어 무척 '다행'이며 '행복하다'는 뜻을 가지게 되었습니다.",
    "example_words": [
      { "word": "幸せ", "reading": "しあわせ", "meaning": "행복", "description": "마음이 흡족하고 기쁜 행복한 상태입니다." },
      { "word": "不幸", "reading": "ふこう", "meaning": "불행", "description": "다행(幸)스럽지 않은(不) 상태입니다." }
    ]
  },
  {
    "kanji": "港",
    "reading_on": "コウ",
    "reading_kun": "みなと",
    "meaning": "항구",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물, 바다, 강을 뜻합니다." },
      { "char": "巷", "role": "거리 항 (요소)", "desc": "거리, 통로라는 뜻과 발음 '항/코우'를 담당합니다." }
    ],
    "story": "배가 물(氵)을 가르며 들어와 정박하고, 육지의 거리(巷)로 사람들이 지나다니는 '항구'를 뜻합니다.",
    "example_words": [
      { "word": "港町", "reading": "みなとまち", "meaning": "항구 도시", "description": "항구(港)가 있는 마을(町)입니다." },
      { "word": "空港", "reading": "くうこう", "meaning": "공항", "description": "하늘(空)을 나는 비행기들이 머무는 항구(港)입니다." }
    ]
  },
  {
    "kanji": "号",
    "reading_on": "ゴウ",
    "reading_kun": "",
    "meaning": "이름 / 부호",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 목소리를 뜻합니다." },
      { "char": "丂", "role": "숨막힐 고 (요소)", "desc": "숨을 길게 내쉬는 모습이나 지팡이를 뜻하며, 여기서는 소리가 멀리 퍼지는 모양입니다." }
    ],
    "story": "입(口)으로 숨을 길게 내쉬며(丂) 큰 소리로 부르짖는다는 뜻에서, 널리 알리는 '이름(호)'이나 '부호(기호)'를 의미하게 되었습니다.",
    "example_words": [
      { "word": "番号", "reading": "ばんごう", "meaning": "번호", "description": "차례(番)를 나타내는 기호나 이름(号)입니다." },
      { "word": "信号", "reading": "しんごう", "meaning": "신호", "description": "믿고(信) 따르는 기호(号)나 불빛입니다." }
    ]
  },
  {
    "kanji": "根",
    "reading_on": "コン",
    "reading_kun": "ね",
    "meaning": "뿌리",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 식물을 뜻합니다." },
      { "char": "艮", "role": "어긋날 간 (요소)", "desc": "완고하게 버티는 모양이나 한곳에 머무른다는 뜻으로, 발음 '근/콘'을 줍니다." }
    ],
    "story": "나무(木)가 땅속 깊이 단단히 버티고(艮) 서 있게 해주는 밑바탕인 '뿌리'를 뜻합니다.",
    "example_words": [
      { "word": "根本", "reading": "こんぽん", "meaning": "근본", "description": "사물의 뿌리(根)와 바탕(本)입니다." },
      { "word": "大根", "reading": "だいこん", "meaning": "무", "description": "큰(大) 뿌리(根)라는 뜻의 식물입니다." }
    ]
  },
  {
    "kanji": "祭",
    "reading_on": "サイ",
    "reading_kun": "まつ(る)、まつ(り)",
    "meaning": "제사",
    "components": [
      { "char": "月", "role": "육달월 (요소)", "desc": "제물로 쓰이는 살코기를 뜻합니다." },
      { "char": "又", "role": "또 우 (요소)", "desc": "손으로 고기를 들어 올리는 모습입니다." },
      { "char": "示", "role": "보일 시 (부수)", "desc": "제단을 뜻합니다." }
    ],
    "story": "손(又)으로 살코기(月) 제물을 정성스레 들어 제단(示) 위에 올려놓고 신에게 '제사(축제)'를 지내는 모습입니다.",
    "example_words": [
      { "word": "お祭り", "reading": "おまつり", "meaning": "축제", "description": "신에게 제사(祭) 지내며 즐기는 축제입니다." },
      { "word": "文化祭", "reading": "ぶんかさい", "meaning": "문화제", "description": "학교 등에서 문화를 발표하며 즐기는 제전(祭)입니다." }
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

print("Grade 3 Part 2 data appended successfully.")
