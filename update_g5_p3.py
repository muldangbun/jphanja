import json
import os

new_data = [
  {
    "kanji": "恩",
    "reading_on": "オン",
    "reading_kun": "",
    "meaning": "은혜",
    "components": [
      { "char": "因", "role": "인할 인 (요소)", "desc": "어떤 것의 바탕이나 이유가 된다는 뜻과 발음 '인/온'을 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음을 뜻합니다." }
    ],
    "story": "남이 나에게 베풀어 준 바탕(因)을 마음(心)속 깊이 간직하며 고맙게 여기는 '은혜'를 뜻합니다.",
    "example_words": [
      { "word": "恩", "reading": "おん", "meaning": "은혜", "description": "남이 베풀어 준 고마운 혜택이나 도움입니다." },
      { "word": "恩返し", "reading": "おんがえし", "meaning": "은혜를 갚음", "description": "받은 은혜(恩)에 보답하여 돌려주는(返し) 것입니다." }
    ]
  },
  {
    "kanji": "情",
    "reading_on": "ジョウ、セイ",
    "reading_kun": "なさ(け)",
    "meaning": "뜻 (정)",
    "components": [
      { "char": "忄", "role": "심방변 (부수)", "desc": "마음을 의미합니다." },
      { "char": "青", "role": "푸를 청 (요소)", "desc": "맑고 깨끗하다는 뜻과 발음 '청/조우'를 담당합니다." }
    ],
    "story": "마음(忄)속 깊은 곳에서 우러나오는 맑고 깨끗한(青) 감정이나 남을 불쌍히 여기는 '정(인정)', 혹은 사물의 참된 '뜻'을 의미합니다.",
    "example_words": [
      { "word": "情け", "reading": "なさけ", "meaning": "인정, 동정", "description": "남을 불쌍히 여겨 따뜻하게 대하는 마음입니다." },
      { "word": "友情", "reading": "ゆうじょう", "meaning": "우정", "description": "친구(友) 사이에 나누는 정(情)입니다." }
    ]
  },
  {
    "kanji": "態",
    "reading_on": "タイ",
    "reading_kun": "",
    "meaning": "모양 (태도)",
    "components": [
      { "char": "能", "role": "능할 능 (요소)", "desc": "곰의 모양에서 튼튼하다, 능숙하다는 뜻과 발음 '능/타이'의 변형 역할을 합니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 생각, 기분을 뜻합니다." }
    ],
    "story": "겉으로 드러나는 능숙한(能) 행동이나 마음(心)의 쓰임새, 즉 겉으로 나타나는 '모양(상태)'이나 '태도'를 뜻합니다.",
    "example_words": [
      { "word": "状態", "reading": "じょうたい", "meaning": "상태", "description": "사물이나 현상이 놓여 있는 모양(状)과 태도(態)입니다." },
      { "word": "態度", "reading": "たいど", "meaning": "태도", "description": "마음이나 생각에 따라 겉으로 드러나는 모습이나 몸가짐입니다." }
    ]
  },
  {
    "kanji": "慣",
    "reading_on": "カン",
    "reading_kun": "な(れる)、な(らす)",
    "meaning": "익숙할",
    "components": [
      { "char": "忄", "role": "심방변 (부수)", "desc": "마음을 의미합니다." },
      { "char": "貫", "role": "꿸 관 (요소)", "desc": "조개를 실로 꿰어 묶듯, 일관되게 계속한다는 뜻과 발음 '관/칸'을 줍니다." }
    ],
    "story": "어떤 행동을 한결같이(貫) 반복하여 마음(忄)이나 몸이 아주 자연스러워지고 '익숙해지다' 혹은 '버릇(습관)'이 되다는 뜻입니다.",
    "example_words": [
      { "word": "慣れる", "reading": "なれる", "meaning": "익숙해지다", "description": "여러 번 겪어 서툴지 않고 자연스럽게 몸에 배는 것입니다." },
      { "word": "習慣", "reading": "しゅうかん", "meaning": "습관", "description": "오래 반복하여 익혀서(習) 몸에 밴 버릇이나 행동(慣)입니다." }
    ]
  },
  {
    "kanji": "承",
    "reading_on": "ショウ",
    "reading_kun": "うけたまわ(る)",
    "meaning": "이을 (받들)",
    "components": [
      { "char": "手", "role": "손 수 (부수)", "desc": "손으로 하는 동작을 뜻합니다. (가운데 아래쪽)" },
      { "char": "丞", "role": "도울 승 (요소)", "desc": "두 손으로 사람을 받들어 구한다는 뜻에서 이어받는다는 의미와 발음 '승/쇼우'를 담당합니다." }
    ],
    "story": "아랫사람이 두 손(手)을 모아 윗사람의 말을 공손히 들어 '받들다' 혹은 그 뜻을 '이어받다(승낙하다)'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "承る", "reading": "うけたまわる", "meaning": "받다, 듣다 (겸양어)", "description": "윗사람의 명령이나 뜻을 공손히 듣거나 맡아보는 것입니다." },
      { "word": "承知", "reading": "しょうち", "meaning": "알아들음, 승낙", "description": "사정을 이어받아(承) 알아듣고(知) 허락하는 것입니다." }
    ]
  },
  {
    "kanji": "技",
    "reading_on": "ギ",
    "reading_kun": "わざ",
    "meaning": "재주 (기술)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 다루는 동작을 의미합니다." },
      { "char": "支", "role": "지탱할 지 (요소)", "desc": "손에 나뭇가지를 든 모양에서 기교를 부린다는 뜻과 발음 '지/기'를 줍니다." }
    ],
    "story": "손(扌)으로 나뭇가지(支) 따위의 도구를 교묘하고 능숙하게 잘 다루는 솜씨, 즉 '재주'나 '기술'을 뜻합니다.",
    "example_words": [
      { "word": "技", "reading": "わざ", "meaning": "기술, 재주", "description": "어떤 일을 능숙하게 해내는 솜씨입니다." },
      { "word": "技術", "reading": "ぎじゅつ", "meaning": "기술", "description": "재주(技)와 솜씨(術)로 사물을 다루거나 만드는 방법입니다." }
    ]
  },
  {
    "kanji": "招",
    "reading_on": "ショウ",
    "reading_kun": "まね(く)",
    "meaning": "부를",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손의 동작을 의미합니다." },
      { "char": "召", "role": "부를 소 (요소)", "desc": "입(口)으로 윗사람이 아랫사람을 부른다는 뜻과 발음 '소/쇼우'를 담당합니다." }
    ],
    "story": "입으로 소리쳐 부르며(召) 손(扌)을 이리 오라고 흔들어 사람을 '부르다(초대하다)' 혹은 어떤 결과를 '초래하다'는 뜻입니다.",
    "example_words": [
      { "word": "招く", "reading": "まねく", "meaning": "초대하다, 부르다", "description": "손짓을 하여 부르거나 사람을 대접하려고 오게 하는 것입니다." },
      { "word": "招待", "reading": "しょうたい", "meaning": "초대", "description": "사람을 불러서(招) 반갑게 기다려 대접(待)하는 일입니다." }
    ]
  },
  {
    "kanji": "授",
    "reading_on": "ジュ",
    "reading_kun": "さず(ける)、さず(かる)",
    "meaning": "줄",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "受", "role": "받을 수 (요소)", "desc": "두 손으로 물건을 주고받는 모양에서 남에게 받는다는 뜻과 발음 '수/쥬'를 줍니다." }
    ],
    "story": "자신이 가지고 있는 지식이나 물건을 다른 사람의 손(扌)에 건네주어 받게(受) 하다, 즉 남에게 '주다(수여하다)'는 뜻입니다.",
    "example_words": [
      { "word": "授ける", "reading": "さずける", "meaning": "주다, 내리다", "description": "가르침이나 상, 벼슬 따위를 아랫사람에게 주는 일입니다." },
      { "word": "授業", "reading": "じゅぎょう", "meaning": "수업", "description": "학교 등에서 학업(業)을 가르쳐 주는(授) 일입니다." }
    ]
  },
  {
    "kanji": "採",
    "reading_on": "サイ",
    "reading_kun": "と(る)",
    "meaning": "캘",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 다루거나 잡는 동작을 의미합니다." },
      { "char": "采", "role": "캘 채 (요소)", "desc": "나무에서 열매나 잎을 손으로 딴다는 뜻과 발음 '채/사이'를 줍니다." }
    ],
    "story": "손(扌)을 뻗어 나무에서 꽃이나 과일을 고르고 골라 '캐다(따다)' 혹은 여러 가지 중에서 좋은 것을 '채택하다'는 뜻입니다.",
    "example_words": [
      { "word": "採る", "reading": "とる", "meaning": "뽑다, 채용하다", "description": "여러 가지 중에서 골라 뽑거나 사람을 채용하는 것입니다." },
      { "word": "採点", "reading": "さいてん", "meaning": "채점", "description": "답안 등을 살펴서 점수(点)를 매기고 캐내는(採) 일입니다." }
    ]
  },
  {
    "kanji": "接",
    "reading_on": "セツ",
    "reading_kun": "つ(ぐ)",
    "meaning": "이을 (접할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손의 동작을 뜻합니다." },
      { "char": "妾", "role": "첩 첩 (요소)", "desc": "원래 죄를 지은 여자 종을 의미하나, 여기서는 가까이 붙어 있다는 뜻과 발음 '첩/세츠'를 담당합니다." }
    ],
    "story": "손(扌)으로 두 물건을 가까이 맞대어(妾) 바짝 '붙이다(접하다)' 혹은 둘을 하나로 '잇다'는 뜻입니다.",
    "example_words": [
      { "word": "接近", "reading": "せっきん", "meaning": "접근", "description": "바짝 잇닿아(接) 가까이(近) 다가가는 것입니다." },
      { "word": "直接", "reading": "ちょくせつ", "meaning": "직접", "description": "중간에 다른 것을 거치지 않고 곧바로(直) 맞닿는(接) 것입니다." }
    ]
  },
  {
    "kanji": "提",
    "reading_on": "テイ",
    "reading_kun": "さ(げる)",
    "meaning": "끌 (제시할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 잡는 동작을 뜻합니다." },
      { "char": "是", "role": "옳을 시 (요소)", "desc": "똑바르다는 뜻으로, 손에 쥐고 똑바로 편다는 의미와 발음 '시/테이'를 줍니다." }
    ],
    "story": "손(扌)에 가방이나 물건을 바르게(是) 쥐고 '들다' 혹은 남이 볼 수 있게 똑바로 내밀어 '제시하다'는 의미입니다.",
    "example_words": [
      { "word": "提げる", "reading": "さげる", "meaning": "들다, 차다", "description": "손에 쥐고 늘어뜨리듯 드는 것입니다." },
      { "word": "提案", "reading": "ていあん", "meaning": "제안", "description": "어떤 안건이나 의견(案)을 내놓아 제시하는(提) 일입니다." }
    ]
  },
  {
    "kanji": "損",
    "reading_on": "ソン",
    "reading_kun": "そこ(なう)、そこ(ねる)",
    "meaning": "덜 (손해)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 의미합니다." },
      { "char": "員", "role": "인원 원 (요소)", "desc": "원래 둥근 솥(鼎) 모양으로, 가장자리가 떨어져 나간다는 의미와 발음 '원/손'을 줍니다." }
    ],
    "story": "손(扌)으로 물건의 둥근(員) 모서리를 깎아 내어 원래보다 '덜다(줄이다)' 혹은 상하게 하여 입는 '손해'를 뜻합니다.",
    "example_words": [
      { "word": "損", "reading": "そん", "meaning": "손해", "description": "밑지거나 잃어서 원래보다 줄어든 상태입니다." },
      { "word": "損なう", "reading": "そこなう", "meaning": "상하게 하다, 해치다", "description": "물건을 망가뜨리거나 기분이나 건강을 해치는 것입니다." }
    ]
  },
  {
    "kanji": "支",
    "reading_on": "シ",
    "reading_kun": "ささ(える)",
    "meaning": "지탱할",
    "components": [
      { "char": "十", "role": "열 십 (요소)", "desc": "나뭇가지나 대나무 가지를 뜻합니다." },
      { "char": "又", "role": "또 우 (부수)", "desc": "손의 동작을 뜻합니다." }
    ],
    "story": "손(又)에 나뭇가지(十)를 쥐고 무너지려는 물건을 떠받치듯 '지탱하다', 혹은 본체에서 갈라져 나온 '가지(지점)'를 뜻합니다.",
    "example_words": [
      { "word": "支える", "reading": "ささえる", "meaning": "지탱하다, 떠받치다", "description": "무너지거나 쓰러지지 않게 받쳐 주거나, 곤란을 버텨내는 일입니다." },
      { "word": "支店", "reading": "してん", "meaning": "지점", "description": "본점에서 갈라져(支) 나가 따로 차린 가게(店)입니다." }
    ]
  },
  {
    "kanji": "政",
    "reading_on": "セイ、ショウ",
    "reading_kun": "まつりごと",
    "meaning": "정사 (정치)",
    "components": [
      { "char": "正", "role": "바를 정 (요소)", "desc": "올바르게 한다는 뜻과 발음 '정/세이'를 담당합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "회초리나 손으로 강제하는 힘, 행동을 뜻합니다." }
    ],
    "story": "강제적인 힘(攵)이나 제도를 써서 나라나 백성이 올바른(正) 길로 가도록 다스리는 일인 '정치(정사)'를 의미합니다.",
    "example_words": [
      { "word": "政治", "reading": "せいじ", "meaning": "정치", "description": "나라와 백성을 바르게(政) 다스리는(治) 일입니다." },
      { "word": "政府", "reading": "せいふ", "meaning": "정부", "description": "나라의 정치(政)를 맡아보는 관청(府)입니다." }
    ]
  },
  {
    "kanji": "故",
    "reading_on": "コ",
    "reading_kun": "ゆえ",
    "meaning": "연고 (옛)",
    "components": [
      { "char": "古", "role": "예 고 (요소)", "desc": "옛날이나 오래되었다는 뜻과 발음 '고/코'를 줍니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "원래 사람이 매를 들고 치는 행동이나, 여기서는 어떤 행동이 반복되어 굳어짐을 나타냅니다." }
    ],
    "story": "예(古)부터 오래 이어져 온 일(攵)이나 이유, 즉 '까닭(연고)'을 뜻하거나, 이미 지나가 버린 '옛날'이나 돌아가신 분을 뜻하기도 합니다.",
    "example_words": [
      { "word": "故障", "reading": "こしょう", "meaning": "고장", "description": "기계 따위에 탈이나 까닭(故)이 생겨 막히고 가로막히는(障) 것입니다." },
      { "word": "故意", "reading": "こい", "meaning": "고의", "description": "일부러 그러려는 까닭(故)을 가진 마음(意)입니다." }
    ]
  },
  {
    "kanji": "敵",
    "reading_on": "テキ",
    "reading_kun": "かたき",
    "meaning": "원수 (적)",
    "components": [
      { "char": "啇", "role": "밑동 적 (요소)", "desc": "초목의 뿌리라는 뜻과 함께 팽팽하게 맞선다는 의미, 발음 '적/테키'를 줍니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손에 무기를 들고 치거나 싸우는 동작입니다." }
    ],
    "story": "힘이나 세력이 팽팽하게 맞서(啇) 무기를 들고 치며(攵) 대항하는 상대, 즉 '적군'이나 대항할 '원수'를 뜻합니다.",
    "example_words": [
      { "word": "敵", "reading": "てき", "meaning": "적, 원수", "description": "대항하여 싸우는 상대나 원수입니다." },
      { "word": "強敵", "reading": "きょうてき", "meaning": "강적", "description": "강(強)하고 만만찮은 적(敵)입니다." }
    ]
  },
  {
    "kanji": "断",
    "reading_on": "ダン",
    "reading_kun": "た(つ)、ことわ(る)",
    "meaning": "끊을",
    "components": [
      { "char": "㡭", "role": "이을 계 (요소)", "desc": "실(糸)이 꼬여 이어진 모양입니다. (현재 자형은 米와 ∟ 2개로 간략화됨)" },
      { "char": "斤", "role": "도끼 근 (부수)", "desc": "도끼나 칼로 자름을 뜻합니다." }
    ],
    "story": "얽혀 이어진 실이나 물건(㡭)을 도끼(斤)로 쳐서 과감하게 딱 '끊다', 혹은 제안을 '거절하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "断る", "reading": "ことわる", "meaning": "거절하다", "description": "상대방의 요구나 제안을 들어주지 않고 딱 끊는 것입니다." },
      { "word": "決断", "reading": "けつだん", "meaning": "결단", "description": "마음을 정하여(決) 끊고(断) 확실히 판단하는 것입니다." }
    ]
  },
  {
    "kanji": "旧",
    "reading_on": "キュウ",
    "reading_kun": "ふる(い)",
    "meaning": "예",
    "components": [
      { "char": "丨", "role": "뚫을 곤 (요소)", "desc": "여기서는 새의 깃털이나 둥지를 나타내는 부호로 쓰였습니다." },
      { "char": "日", "role": "날 일 (부수)", "desc": "원래 부엉이나 올빼미처럼 머리에 뿔깃이 난 새(萑)의 변형입니다." }
    ],
    "story": "원래 머리에 털이 난 올빼미를 뜻하는 글자(舊)였으나, 시간이 오래되었다는 뜻으로 바뀌며 글자가 간략화되어 '옛날'이나 '예전'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "旧", "reading": "きゅう", "meaning": "예전, 구", "description": "새로운 것과 반대되는 지나간 예전의 것입니다." },
      { "word": "復旧", "reading": "ふっきゅう", "meaning": "복구", "description": "망가진 것을 예전(旧) 상태로 다시 되돌리는(復) 것입니다." }
    ]
  },
  {
    "kanji": "易",
    "reading_on": "エキ、イ",
    "reading_kun": "やさ(しい)",
    "meaning": "바꿀 (쉬울)",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 도마뱀의 머리 모양을 본뜬 것입니다." },
      { "char": "勿", "role": "말 물 (요소)", "desc": "도마뱀의 발과 꼬리 모양이거나 빛이 퍼지는 모양입니다." }
    ],
    "story": "카멜레온처럼 몸 색깔을 쉽게 바꾸는 도마뱀의 모양에서, 모습이나 위치를 '바꾸다' 혹은 그 일이 '쉽다(단순하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "易しい", "reading": "やさしい", "meaning": "쉽다", "description": "어렵지 않고 단박에 이해하거나 할 수 있는 상태입니다." },
      { "word": "貿易", "reading": "ぼうえき", "meaning": "무역", "description": "나라 사이에 서로 물건과 재물(貿)을 바꾸며(易) 장사하는 일입니다." }
    ]
  },
  {
    "kanji": "暴",
    "reading_on": "ボウ、バク",
    "reading_kun": "あば(れる)、あば(く)",
    "meaning": "사나울 (폭력)",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "햇빛을 뜻합니다." },
      { "char": "出", "role": "날 출 (요소)", "desc": "두 손(廾) 모양으로 물건을 위로 내민다는 뜻입니다." },
      { "char": "共", "role": "함께 공 (요소)", "desc": "곡식을 두 손으로 바치는 모양에서 거칠다는 뜻을 줍니다." }
    ],
    "story": "햇빛(日)에 곡식(가운데 쌀 米 변형과 두 손 廾 등)을 내놓고 사납게 쬐어 말린다는 데서, 거칠고 '사납다' 혹은 '폭력'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "暴れる", "reading": "あばれる", "meaning": "날뛰다, 난폭하게 굴다", "description": "몸부림치거나 거칠게 행동하는 것입니다." },
      { "word": "暴力", "reading": "ぼうりょく", "meaning": "폭력", "description": "거칠고 사나운(暴) 힘(力)이나 주먹질입니다." }
    ]
  },
  {
    "kanji": "条",
    "reading_on": "ジョウ",
    "reading_kun": "",
    "meaning": "가지 (조목)",
    "components": [
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "여기서는 사람(사람 인 亻 모양)이 나뭇가지를 들고 있는 모양이 변형된 것입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." }
    ],
    "story": "원래 條 자의 약자로, 나무(木)에서 뻗어 나온 가늘고 긴 '가지'를 뜻하며, 글이나 법 등을 하나씩 나눈 줄기인 '조목'이나 '조항'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "条件", "reading": "じょうけん", "meaning": "조건", "description": "어떤 일을 이루기 위해 갖추어야 할 조목(条)과 요건(件)입니다." },
      { "word": "箇条書き", "reading": "かじょうがき", "meaning": "개조식(항목별) 쓰기", "description": "글을 낱낱의(箇) 조목(条)으로 나누어 쓰는(書き) 방식입니다." }
    ]
  },
  {
    "kanji": "枝",
    "reading_on": "シ",
    "reading_kun": "えだ",
    "meaning": "가지",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "支", "role": "지탱할 지 (요소)", "desc": "본체에서 갈라져 나왔다는 뜻과 발음 '지/시'를 줍니다." }
    ],
    "story": "나무(木)의 큰 줄기에서 갈라져(支) 나와 옆으로 뻗은 가늘고 뾰족한 '가지'를 의미합니다.",
    "example_words": [
      { "word": "枝", "reading": "えだ", "meaning": "나뭇가지", "description": "나무의 원줄기에서 갈라져 자란 가늘고 긴 부분입니다." },
      { "word": "枝豆", "reading": "えだまめ", "meaning": "에다마메, 풋콩", "description": "가지(枝)째 삶아 먹는 덜 익은 콩(豆)입니다." }
    ]
  },
  {
    "kanji": "査",
    "reading_on": "サ",
    "reading_kun": "",
    "meaning": "조사할",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 물건을 뜻합니다." },
      { "char": "且", "role": "또 차 (요소)", "desc": "도마 모양으로, 위아래로 겹친다는 뜻과 발음 '사/사'를 담당합니다." }
    ],
    "story": "뗏목(나무 木 겹친 모양의 원형)이 막히지 않았는지 장애물을 세밀하게 살피고 '조사하다', 혹은 사실을 알아보기 위해 '검사하다'는 뜻입니다.",
    "example_words": [
      { "word": "検査", "reading": "けんさ", "meaning": "검사", "description": "기준에 맞는지 살펴(検) 조사하는(査) 일입니다." },
      { "word": "調査", "reading": "ちょうさ", "meaning": "조사", "description": "사물의 내막을 조절하여(調) 명확히 살피는(査) 일입니다." }
    ]
  },
  {
    "kanji": "格",
    "reading_on": "カク、コウ",
    "reading_kun": "",
    "meaning": "격식 (자격)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "各", "role": "각각 각 (요소)", "desc": "여기저기 다다른다는 뜻에서 얽혀 있는 격자 모양이나 발음 '각/카쿠'를 줍니다." }
    ],
    "story": "나무(木)를 각각(各)의 간격에 맞추어 가로세로로 짜 맞춘 틀(격자)에서 유래하여, 일정하게 짜여진 '격식'이나 사람의 '자격(지위)'을 뜻합니다.",
    "example_words": [
      { "word": "合格", "reading": "ごうかく", "meaning": "합격", "description": "시험이나 조건 따위의 격식(格)에 맞아(合) 통과하는 일입니다." },
      { "word": "価格", "reading": "かかく", "meaning": "가격", "description": "물건이 지니는 값(価)과 가치의 격(格)입니다." }
    ]
  },
  {
    "kanji": "桜",
    "reading_on": "オウ",
    "reading_kun": "さくら",
    "meaning": "벚나무",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." },
      { "char": "ツ", "role": "머리 (요소)", "desc": "벚꽃잎이 점점이 날리는 모습입니다." },
      { "char": "女", "role": "계집 녀 (요소)", "desc": "원래 嬰(어린아이 영)의 약자로, 여자가 목걸이를 한 모습에서 아름답다는 뜻을 줍니다." }
    ],
    "story": "봄날 여자(女)의 예쁜 목걸이처럼 화려하고 자잘한(ツ 모양) 꽃을 피우는 나무(木), 즉 일본의 대표적인 꽃나무인 '벚나무'나 '벚꽃'을 뜻합니다.",
    "example_words": [
      { "word": "桜", "reading": "さくら", "meaning": "벚나무, 벚꽃", "description": "봄에 연분홍빛 자잘한 꽃이 무리 지어 피는 나무입니다." },
      { "word": "夜桜", "reading": "よざくら", "meaning": "밤 벚꽃", "description": "밤(夜)에 조명을 받거나 달빛에 비치는 벚꽃(桜)입니다." }
    ]
  },
  {
    "kanji": "検",
    "reading_on": "ケン",
    "reading_kun": "",
    "meaning": "검사할",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 책상, 상자를 뜻합니다." },
      { "char": "僉", "role": "다 첨 (요소)", "desc": "여러 사람이 모여 세밀하게 다듬거나 모은다는 뜻과 발음 '첨/켄'을 줍니다." }
    ],
    "story": "여러 사람(僉)이 나무 상자(木)나 서류를 하나하나 봉인하고 틀린 곳이 없는지 철저히 점검하고 '검사하다'는 뜻입니다.",
    "example_words": [
      { "word": "検査", "reading": "けんさ", "meaning": "검사", "description": "기준에 맞는지 자세히 조사하고(査) 점검하는(検) 것입니다." },
      { "word": "探検", "reading": "たんけん", "meaning": "탐험 (탐검)", "description": "알려지지 않은 곳을 찾아(探) 조사하고 검사하는(検) 일입니다." }
    ]
  },
  {
    "kanji": "構",
    "reading_on": "コウ",
    "reading_kun": "かま(える)、かま(う)",
    "meaning": "얽을 (가꿀)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 목재를 뜻합니다." },
      { "char": "冓", "role": "짤 구 (요소)", "desc": "나무나 뼈대가 얽혀 교차하는 모양으로 발음 '구/코우'를 줍니다." }
    ],
    "story": "목재(木)를 이리저리 교차시켜(冓) 단단하게 얽어서 집이나 건물을 '짓다(구조)', 혹은 자세를 얽어 '가꾸다(상관하다)'는 뜻입니다.",
    "example_words": [
      { "word": "構う", "reading": "かまう", "meaning": "상관하다, 참견하다", "description": "어떤 일에 신경을 써서 마음을 얽거나 참견하는 것입니다." },
      { "word": "構造", "reading": "こうぞう", "meaning": "구조", "description": "건물이나 사물을 얽고(構) 짜서 지은(造) 뼈대나 생김새입니다." }
    ]
  },
  {
    "kanji": "武",
    "reading_on": "ブ、ム",
    "reading_kun": "",
    "meaning": "호반 (무예)",
    "components": [
      { "char": "止", "role": "그칠 지 (부수)", "desc": "발걸음을 내디뎌 걷는 모양이나 난폭함을 그치게 한다는 뜻입니다." },
      { "char": "戈", "role": "창 과 (요소)", "desc": "창이나 무기를 의미합니다." }
    ],
    "story": "손에 창(戈)을 굳게 쥐고 발걸음(止)을 힘차게 내디뎌 적과 싸우거나, 반대로 폭력을 멈추게(止) 하는 무사의 힘인 '무예'나 '무력'을 뜻합니다.",
    "example_words": [
      { "word": "武器", "reading": "ぶき", "meaning": "무기", "description": "전쟁이나 싸움(武)에 쓰는 도구(器)입니다." },
      { "word": "武士", "reading": "ぶし", "meaning": "무사, 사무라이", "description": "무예(武)를 익혀 싸우는 선비(士)입니다." }
    ]
  },
  {
    "kanji": "比",
    "reading_on": "ヒ",
    "reading_kun": "くら(べる)",
    "meaning": "견줄 (비교할)",
    "components": [
      { "char": "比", "role": "견줄 비 (부수)", "desc": "두 사람(匕)이 나란히 서서 서로의 키나 모습을 대어보는 모양을 본뜬 글자입니다." }
    ],
    "story": "두 사람이 나란히 서서 누가 더 크고 나은지 서로 '견주다' 혹은 '비교하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "比べる", "reading": "くらべる", "meaning": "비교하다, 견주다", "description": "두 가지 이상의 사물을 맞대어 차이를 살펴보는 일입니다." },
      { "word": "比例", "reading": "ひれい", "meaning": "비례", "description": "어떤 수치에 견주어(比) 일정한 비율(例)로 변하는 관계입니다." }
    ]
  },
  {
    "kanji": "永",
    "reading_on": "エイ",
    "reading_kun": "なが(い)",
    "meaning": "길",
    "components": [
      { "char": "水", "role": "물 수 (부수)", "desc": "강물이 흐르는 모양을 본뜬 글자에서 변형되었습니다." }
    ],
    "story": "수많은 물줄기가 모여 아주 멀리 끝없이 흘러가는 강물의 모양에서, 시간이나 공간이 한없이 '길다' 혹은 '영원하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "永遠", "reading": "えいえん", "meaning": "영원", "description": "시간이 끝이 없을 만큼 아주 길고(永) 먼(遠) 상태입니다." },
      { "word": "永久", "reading": "えいきゅう", "meaning": "영구", "description": "시간이 길고(永) 오램(久)을 뜻합니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade5.json'
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

print("Grade 5 Part 3 data appended successfully.")
