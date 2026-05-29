import json
import os

new_data = [
  {
    "kanji": "念",
    "reading_on": "ネン",
    "reading_kun": "",
    "meaning": "생각할",
    "components": [
      { "char": "今", "role": "이제 금 (요소)", "desc": "지금, 현재라는 뜻과 발음 '금/넨'을 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 생각을 뜻합니다." }
    ],
    "story": "지금(今) 당장 마음(心)속에 품고 있는 깊은 '생각'이나 염원을 뜻합니다.",
    "example_words": [
      { "word": "念のため", "reading": "ねんのため", "meaning": "만일을 위해, 다짐을 위해", "description": "확실히 해두려는 생각(念)에서 하는 일입니다." },
      { "word": "残念", "reading": "ざんねん", "meaning": "유감, 분함", "description": "아쉬운 생각이나 미련(念)이 아직 남아 있는(残) 것입니다." }
    ]
  },
  {
    "kanji": "敗",
    "reading_on": "ハイ",
    "reading_kun": "やぶ(れる)",
    "meaning": "패할",
    "components": [
      { "char": "貝", "role": "조개 패 (요소)", "desc": "솥이나 재물(정鼎의 생략형)을 뜻합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "몽둥이로 치거나 부순다는 의미입니다." }
    ],
    "story": "커다란 솥(貝의 원래 형태)을 몽둥이(攵)로 때려 부수듯, 싸움에서 지고 무너져 '패하다'는 뜻입니다.",
    "example_words": [
      { "word": "敗れる", "reading": "やぶれる", "meaning": "패배하다, 지다", "description": "싸움이나 경기에서 져서 무너지는 것입니다." },
      { "word": "失敗", "reading": "しっぱい", "meaning": "실패", "description": "일을 잘못하여 잃어버리고(失) 무너져 지는(敗) 것입니다." }
    ]
  },
  {
    "kanji": "梅",
    "reading_on": "バイ",
    "reading_kun": "うめ",
    "meaning": "매화나무",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "毎", "role": "매양 매 (요소)", "desc": "매번, 어머니(母)라는 뜻과 발음 '매/바이'를 줍니다. (신맛 때문에 아이를 밴 어머니가 즐겨 찾는 열매라는 뜻도 내포)" }
    ],
    "story": "이른 봄마다(毎) 아름다운 꽃을 피우고 신맛이 나는 둥근 열매를 맺는 나무(木), 즉 '매화나무'나 '매실'을 의미합니다.",
    "example_words": [
      { "word": "梅", "reading": "うめ", "meaning": "매화, 매실", "description": "봄에 피는 벚나무과의 꽃나무나 그 열매입니다." },
      { "word": "梅雨", "reading": "つゆ", "meaning": "장마", "description": "매실(梅)이 익을 무렵에 내리는 긴 비(雨)입니다. (특별한 읽기)" }
    ]
  },
  {
    "kanji": "博",
    "reading_on": "ハク、バク",
    "reading_kun": "",
    "meaning": "넓을",
    "components": [
      { "char": "十", "role": "열 십 (부수)", "desc": "많거나 모든 방향을 뜻합니다." },
      { "char": "甫", "role": "클 보 (요소)", "desc": "크다, 넓게 퍼진다는 뜻입니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "손의 동작을 뜻합니다." }
    ],
    "story": "손(寸)으로 큰 밭(甫의 변형)을 사방(十)으로 고르게 펴듯, 지식이나 사물이 크고 '넓다(해박하다)'는 뜻입니다.",
    "example_words": [
      { "word": "博士", "reading": "はかせ", "meaning": "박사", "description": "학식이 아주 넓고(博) 뛰어난 선비(士), 즉 최고 학위를 가진 사람입니다." },
      { "word": "博物館", "reading": "はくぶつかん", "meaning": "박물관", "description": "여러 가지 다양한 사물(物)을 널리(博) 모아 전시하는 집(館)입니다." }
    ]
  },
  {
    "kanji": "飯",
    "reading_on": "ハン",
    "reading_kun": "めし",
    "meaning": "밥",
    "components": [
      { "char": "食", "role": "밥 식 (부수)", "desc": "음식이나 먹는 것을 뜻합니다." },
      { "char": "反", "role": "돌이킬 반 (요소)", "desc": "뒤집다, 돌려준다는 뜻과 발음 '반/한'을 담당합니다." }
    ],
    "story": "배가 고플 때 먹고(食) 나면 몸의 기운을 원래대로 든든하게 뒤집어 돌려주는(反) 음식, 즉 '밥'을 의미합니다.",
    "example_words": [
      { "word": "ご飯", "reading": "ごはん", "meaning": "밥, 식사", "description": "쌀 따위를 끓여서 익힌 음식이나 식사입니다." },
      { "word": "昼飯", "reading": "ひるめし", "meaning": "점심밥", "description": "낮(昼)에 먹는 밥(飯)입니다." }
    ]
  },
  {
    "kanji": "飛",
    "reading_on": "ヒ",
    "reading_kun": "と(ぶ)、と(ばす)",
    "meaning": "날 (비행할)",
    "components": [
      { "char": "飛", "role": "날 비 (부수)", "desc": "새가 두 날개를 쫙 펴고 힘차게 하늘을 나는 모양을 본뜬 글자입니다." }
    ],
    "story": "새가 날개를 활짝 펴고 높이 '날아오르다' 혹은 '날다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "飛ぶ", "reading": "とぶ", "meaning": "날다", "description": "새나 비행기가 공중으로 떠서 이동하는 것입니다." },
      { "word": "飛行機", "reading": "ひこうき", "meaning": "비행기", "description": "하늘을 날아(飛) 다니는(行) 기계(機)입니다." }
    ]
  },
  {
    "kanji": "費",
    "reading_on": "ヒ",
    "reading_kun": "つい(やす)、つい(える)",
    "meaning": "쓸 (소비할)",
    "components": [
      { "char": "弗", "role": "아닐 불 (요소)", "desc": "두 막대기를 끈으로 묶은 모양에서 풀어 없앤다는 뜻과 발음 '비/히'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "재물이나 돈을 뜻합니다." }
    ],
    "story": "재물이나 돈(貝)을 묶어둔 끈을 풀어서(弗) 여기저기 흩어지게 '쓰다' 혹은 '소비하다'는 뜻입니다.",
    "example_words": [
      { "word": "費やす", "reading": "ついやす", "meaning": "쓰다, 소비하다", "description": "돈이나 시간, 기운 따위를 들여서 없애는 것입니다." },
      { "word": "食費", "reading": "しょくひ", "meaning": "식비", "description": "밥을 먹는(食) 데에 쓰는(費) 돈이나 비용입니다." }
    ]
  },
  {
    "kanji": "必",
    "reading_on": "ヒツ",
    "reading_kun": "かなら(ず)",
    "meaning": "반드시",
    "components": [
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음을 뜻합니다." },
      { "char": "丿", "role": "삐침 (요소)", "desc": "마음을 가로지르는 칼이나 막대를 뜻하여 나눌 수 없다는 의미를 줍니다." }
    ],
    "story": "칼이 마음(心) 한가운데를 꿰뚫고 지나가는(丿) 모양에서, 흔들림 없이 확고하고 '반드시' 꼭 이루어져야 함을 뜻합니다.",
    "example_words": [
      { "word": "必ず", "reading": "かならず", "meaning": "반드시, 꼭", "description": "틀림없이 그렇게 됨을 나타냅니다." },
      { "word": "必要", "reading": "ひつよう", "meaning": "필요", "description": "반드시(必) 원하고 쓰여야(要) 하는 상태입니다." }
    ]
  },
  {
    "kanji": "票",
    "reading_on": "ヒョウ",
    "reading_kun": "",
    "meaning": "표 (쪽지)",
    "components": [
      { "char": "覀", "role": "덮을 아 (요소)", "desc": "불(火)이 타오르며 위로 오르는 모양입니다." },
      { "char": "示", "role": "보일 시 (부수)", "desc": "여기서는 제단이나 신에게 무언가를 보여 알린다는 의미입니다." }
    ],
    "story": "불(覀)이 타오를 때 연기가 위로 올라가듯 흩날리는 가벼운 종이나, 자기의 뜻을 써서 알리는(示) 쪽지인 '표(투표용지 등)'를 뜻합니다.",
    "example_words": [
      { "word": "投票", "reading": "とうひょう", "meaning": "투표", "description": "의견이나 찬반을 적은 표(票)를 상자에 던져(投) 넣는 일입니다." },
      { "word": "伝票", "reading": "でんぴょう", "meaning": "전표", "description": "돈의 출납이나 내역을 적어 전하는(伝) 종이쪽지(票)입니다." }
    ]
  },
  {
    "kanji": "標",
    "reading_on": "ヒョウ",
    "reading_kun": "",
    "meaning": "표적 (표시)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "票", "role": "표 표 (요소)", "desc": "불꽃이 솟아 눈에 띈다는 뜻과 발음 '표/히ょう'를 담당합니다." }
    ],
    "story": "나무(木) 막대기 끝에 눈에 잘 띄게 불꽃이나 표시(票)를 매달아 놓아 사람들이 보고 알아볼 수 있게 세운 '표시'나 '목표물'을 뜻합니다.",
    "example_words": [
      { "word": "目標", "reading": "もくひょう", "meaning": "목표", "description": "눈(目)으로 보고 나아갈 방향이나 표적(標)입니다." },
      { "word": "標識", "reading": "ひょうしき", "meaning": "표지(판)", "description": "길이나 규칙을 알리도록 표시(標)하여 알게(識) 한 물건입니다." }
    ]
  },
  {
    "kanji": "不",
    "reading_on": "フ、ブ",
    "reading_kun": "",
    "meaning": "아닐 (불)",
    "components": [
      { "char": "一", "role": "한 일 (부수)", "desc": "하늘이나 땅, 경계를 의미합니다." },
      { "char": "个", "role": "낱 개 (요소)", "desc": "새가 위로 날아올라가는 모양의 간략화된 형태입니다." }
    ],
    "story": "새가 하늘 위(一)로 멀리 날아가 버려 다시 돌아오지 '않는다' 혹은 '아니다'라는 부정의 뜻을 가집니다.",
    "example_words": [
      { "word": "不安", "reading": "ふあん", "meaning": "불안", "description": "마음이 편안하지(安) 않은(不) 상태입니다." },
      { "word": "不足", "reading": "ふそく", "meaning": "부족", "description": "충분하거나 족하지(足) 않은(不) 즉, 모자란 상태입니다." }
    ]
  },
  {
    "kanji": "夫",
    "reading_on": "フ、フウ",
    "reading_kun": "おっと",
    "meaning": "지아비 (남편)",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "어른이 된 큰 남자의 모양입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "어른이 되었음을 나타내는 비녀(상투) 모양입니다." }
    ],
    "story": "머리에 상투(一)를 튼 늠름한 어른 남자(大)를 그려, 다 큰 사내나 아내의 짝인 '남편(지아비)'을 뜻합니다.",
    "example_words": [
      { "word": "夫", "reading": "おっと", "meaning": "남편", "description": "결혼한 여자의 짝이 되는 사내입니다." },
      { "word": "夫婦", "reading": "ふうふ", "meaning": "부부", "description": "남편(夫)과 아내(婦)를 아울러 이르는 말입니다." }
    ]
  },
  {
    "kanji": "付",
    "reading_on": "フ",
    "reading_kun": "つ(く)、つ(ける)",
    "meaning": "붙을 (줄)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "손의 모양이나 가까이 댄다는 뜻을 나타냅니다." }
    ],
    "story": "사람(亻)에게 손(寸)으로 물건을 가까이 대어 건네주거나 '붙이다', 나아가 무언가를 내어준다는 뜻입니다.",
    "example_words": [
      { "word": "付く", "reading": "つく", "meaning": "붙다", "description": "어떤 물건이 다른 물건에 착 달라붙는 것입니다." },
      { "word": "受付", "reading": "うけつけ", "meaning": "접수(처)", "description": "사람이나 서류를 받아(受) 붙이는(付) 일이나 그 장소입니다." }
    ]
  },
  {
    "kanji": "府",
    "reading_on": "フ",
    "reading_kun": "",
    "meaning": "마을 (관청 / 창고)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "건물이나 지붕 아래를 의미합니다." },
      { "char": "付", "role": "붙을 부 (요소)", "desc": "물건을 주거나 맡긴다는 뜻과 발음 '부/후'를 담당합니다." }
    ],
    "story": "건물(广) 안에 중요한 문서나 재물을 맡겨(付) 보관하는 큰 창고나 '관청', 혹은 그런 관청이 있는 큰 '마을(행정 구역)'을 뜻합니다.",
    "example_words": [
      { "word": "政府", "reading": "せいふ", "meaning": "정부", "description": "나라의 정치(政)를 맡아보는 국가의 관청(府) 조직입니다." },
      { "word": "京都府", "reading": "きょうとふ", "meaning": "교토부", "description": "일본의 광역 행정 구역 중 하나인 교토(京都) 부(府)입니다." }
    ]
  },
  {
    "kanji": "副",
    "reading_on": "フク",
    "reading_kun": "",
    "meaning": "버금",
    "components": [
      { "char": "畐", "role": "가득할 복 (요소)", "desc": "배가 불룩한 항아리로, 물건이 꽉 차 있다는 뜻과 발음 '복/후쿠'를 줍니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 나누거나 자르는 것을 의미합니다." }
    ],
    "story": "항아리에 가득 찬(畐) 물건을 칼(刂)로 둘로 나누어, 본래의 으뜸가는 것 외에 그것을 돕는 두 번째인 '버금(부)'이나 곁딸린 것을 뜻합니다.",
    "example_words": [
      { "word": "副社長", "reading": "ふくしゃちょう", "meaning": "부사장", "description": "사장 다음으로 버금가며(副) 회사를 다스리는 사람입니다." },
      { "word": "副作用", "reading": "ふくさよう", "meaning": "부작용", "description": "원래 작용 외에 부수적으로(副) 일어나는 작용(作用)입니다." }
    ]
  },
  {
    "kanji": "粉",
    "reading_on": "フン",
    "reading_kun": "こ、こな",
    "meaning": "가루",
    "components": [
      { "char": "米", "role": "쌀 미 (부수)", "desc": "쌀이나 곡식을 뜻합니다." },
      { "char": "分", "role": "나눌 분 (요소)", "desc": "작게 나눈다는 뜻과 발음 '분/훈'을 담당합니다." }
    ],
    "story": "쌀(米)이나 곡식을 빻아서 아주 작게 나눈(分) 미세한 조각, 즉 '가루'를 뜻합니다.",
    "example_words": [
      { "word": "粉", "reading": "こな", "meaning": "가루", "description": "어떤 물질을 빻거나 갈아서 만든 아주 작은 부스러기입니다." },
      { "word": "花粉", "reading": "かふん", "meaning": "꽃가루", "description": "꽃(花)에서 날리는 가루(粉)입니다." }
    ]
  },
  {
    "kanji": "兵",
    "reading_on": "ヘイ、ヒョウ",
    "reading_kun": "",
    "meaning": "군사",
    "components": [
      { "char": "斤", "role": "도끼 근 (요소)", "desc": "도끼나 무기를 뜻합니다." },
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "여기서는 두 손(廾)이 무기를 굳게 받쳐 든 모양에서 변형되었습니다." }
    ],
    "story": "두 손(八의 변형)으로 무거운 도끼나 무기(斤)를 굳게 잡고 싸우는 '군사(병사)' 혹은 '병기(무기)'를 뜻합니다.",
    "example_words": [
      { "word": "兵士", "reading": "へいし", "meaning": "병사", "description": "무기를 든 군사(兵)인 사람(士)입니다." },
      { "word": "兵器", "reading": "へいき", "meaning": "병기, 무기", "description": "전쟁에서 군사(兵)가 쓰는 기구(器)입니다." }
    ]
  },
  {
    "kanji": "別",
    "reading_on": "ベツ",
    "reading_kun": "わか(れる)",
    "meaning": "나눌 (다를)",
    "components": [
      { "char": "口", "role": "입 구 (요소)", "desc": "원래 뼈를 의미하는 冎의 변형입니다." },
      { "char": "刀", "role": "선칼도방 (부수)", "desc": "칼로 베거나 자르는 동작을 뜻합니다." }
    ],
    "story": "짐승의 뼈(口의 원형)를 칼(刀)로 발라내어 살과 뼈를 서로 '나누다', 혹은 둘이 떨어져서 '다르다', '헤어지다'는 의미입니다.",
    "example_words": [
      { "word": "別れる", "reading": "わかれる", "meaning": "헤어지다", "description": "만나던 사람과 떨어져서 각자 다른 길로 가는 것입니다." },
      { "word": "特別", "reading": "とくべつ", "meaning": "특별", "description": "뛰어나고(特) 다른 것과 구별되는(別) 보통이 아닌 상태입니다." }
    ]
  },
  {
    "kanji": "辺",
    "reading_on": "ヘン",
    "reading_kun": "あたり、べ",
    "meaning": "가 (근처)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 이동함을 의미합니다." },
      { "char": "刀", "role": "칼 도 (요소)", "desc": "여기서는 刀 모양의 변형으로 칼로 끊은 가장자리라는 뜻을 줍니다." }
    ],
    "story": "길(辶)을 따라 가다 보면 닿게 되는 변두리나 가장자리(刀의 깎인 모습)에서 유래하여 어떤 곳의 '근처'나 '가장자리'를 뜻합니다.",
    "example_words": [
      { "word": "辺り", "reading": "あたり", "meaning": "근처, 주변", "description": "어떤 곳을 중심으로 한 가까운 둘레나 부근입니다." },
      { "word": "海辺", "reading": "うみべ", "meaning": "해변, 바닷가", "description": "바다(海)가 있는 가장자리나 근처(辺)입니다." }
    ]
  },
  {
    "kanji": "変",
    "reading_on": "ヘン",
    "reading_kun": "か(わる)、か(える)",
    "meaning": "변할 (이상할)",
    "components": [
      { "char": "亦", "role": "또 역 (요소)", "desc": "여기서는 실타래가 얽힌 모양(䜌)의 간략화된 형태로 얽혀 있음을 뜻합니다." },
      { "char": "夂", "role": "뒤져올 치 (부수)", "desc": "발걸음이나 동작을 뜻하여 치거나 푸는 동작을 나타냅니다." }
    ],
    "story": "복잡하게 얽혀 있는 실타래(亦의 원래 형태)를 손으로 쳐서(夂) 풀거나 모양을 다른 것으로 '변하게 하다(바꾸다)' 혹은 상태가 '이상하다'는 뜻입니다.",
    "example_words": [
      { "word": "変わる", "reading": "かわる", "meaning": "변하다, 바뀌다", "description": "원래의 모양이나 성질이 다른 것으로 달라지는 것입니다." },
      { "word": "大変", "reading": "たいへん", "meaning": "매우, 큰일, 몹시 힘듦", "description": "크게(大) 변할(変) 만큼 몹시 심한 모양입니다." }
    ]
  },
  {
    "kanji": "便",
    "reading_on": "ベン、ビン",
    "reading_kun": "たよ(り)",
    "meaning": "편할 (소식)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "更", "role": "고칠 경 (요소)", "desc": "번갈아 가며 바꾼다는 뜻에서 사람 사이를 오간다는 뜻과 발음 '편/벤'을 줍니다." }
    ],
    "story": "사람(亻)들이 이리저리 오가며(更) 소식을 전해 주는 '우편(소식)'이나, 그렇게 해 주어 일이 '편리하다'는 뜻입니다.",
    "example_words": [
      { "word": "便利", "reading": "べんり", "meaning": "편리", "description": "쓰기에 편하고(便) 이로운(利) 상태입니다." },
      { "word": "郵便", "reading": "ゆうびん", "meaning": "우편", "description": "역참(郵)을 통해 편지나 소식(便)을 전하는 제도입니다." }
    ]
  },
  {
    "kanji": "包",
    "reading_on": "ホウ",
    "reading_kun": "つつ(む)",
    "meaning": "쌀",
    "components": [
      { "char": "勹", "role": "쌀 포 (부수)", "desc": "사람이 몸을 굽혀 무언가를 감싸 안는 모양입니다." },
      { "char": "巳", "role": "뱀 사 (요소)", "desc": "여기서는 어머니 배 속에 들어 있는 태아의 모양을 나타냅니다." }
    ],
    "story": "어머니가 배 속(勹)에 든 아기(巳)를 안전하게 보호하듯, 물건을 밖으로 드러나지 않게 덮어 '싸다(포장하다)'는 뜻입니다.",
    "example_words": [
      { "word": "包む", "reading": "つつむ", "meaning": "싸다, 포장하다", "description": "물건이 보이지 않게 천이나 종이 따위로 겉을 감싸는 것입니다." },
      { "word": "小包", "reading": "こづつみ", "meaning": "소포", "description": "작게(小) 싸서(包) 우편으로 보내는 물건입니다." }
    ]
  },
  {
    "kanji": "法",
    "reading_on": "ホウ、ハッ、ホッ",
    "reading_kun": "",
    "meaning": "법",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강물이 흘러가는 것을 뜻합니다." },
      { "char": "去", "role": "갈 거 (요소)", "desc": "악한 것을 버리거나 떠나보낸다는 뜻입니다. (옛 글자에서는 외뿔 달린 해태 모양도 있었습니다.)" }
    ],
    "story": "강물(氵)이 위에서 아래로 순리대로 흘러가듯, 악한 것은 쫓아내고(去) 공평하게 사회의 규칙을 지키는 '법도(법)'나 '방법'을 뜻합니다.",
    "example_words": [
      { "word": "法律", "reading": "ほうりつ", "meaning": "법률", "description": "나라에서 정하여 모두가 지켜야 할 법(法)과 규칙(律)입니다." },
      { "word": "方法", "reading": "ほうほう", "meaning": "방법", "description": "어떤 목적을 이루기 위한 수단이나 방향(方)과 법도(法)입니다." }
    ]
  },
  {
    "kanji": "望",
    "reading_on": "ボウ、モウ",
    "reading_kun": "のぞ(む)",
    "meaning": "바랄",
    "components": [
      { "char": "亡", "role": "망할 망 (요소)", "desc": "먼 곳이나 눈에 보이지 않게 숨는다는 뜻과 발음 '망/보우'를 줍니다." },
      { "char": "月", "role": "달 월 (부수)", "desc": "하늘에 떠 있는 달을 의미합니다." },
      { "char": "王", "role": "구슬 옥 (요소)", "desc": "여기서는 壬(사람이 서 있는 모양)의 변형으로 사람이 발돋움하고 서 있는 모양입니다." }
    ],
    "story": "사람이 발돋움하고(王의 원형) 까마득히 먼(亡) 밤하늘의 보름달(月)을 쳐다보며 소원을 간절히 '바라다' 혹은 먼 곳을 '바라보다'는 뜻입니다.",
    "example_words": [
      { "word": "希望", "reading": "きぼう", "meaning": "희망", "description": "앞날이 좋게 되기를 간절히 바라는(望) 마음입니다." },
      { "word": "望む", "reading": "のぞむ", "meaning": "바라다", "description": "어떤 일이 이루어지기를 기대하거나 먼 곳을 바라보는 것입니다." }
    ]
  },
  {
    "kanji": "牧",
    "reading_on": "ボク",
    "reading_kun": "まき",
    "meaning": "칠 (목장)",
    "components": [
      { "char": "牛", "role": "소 우 (부수)", "desc": "소나 가축을 의미합니다." },
      { "char": "攵", "role": "칠 복 (요소)", "desc": "손에 회초리를 들고 가축을 몰거나 치는 동작입니다." }
    ],
    "story": "손에 채찍(攵)을 들고 들판에서 소나 가축(牛) 떼를 쫓으며 기르고 '치다(먹이다)'는 뜻에서 소를 기르는 곳(목장)을 의미합니다.",
    "example_words": [
      { "word": "牧場", "reading": "ぼくじょう", "meaning": "목장", "description": "가축을 치며(牧) 기르는 넓은 장소(場)입니다." },
      { "word": "遊牧", "reading": "ゆうぼく", "meaning": "유목", "description": "가축 떼를 치기(牧) 위해 물과 풀을 찾아 이리저리 돌아다니는(遊) 일입니다." }
    ]
  },
  {
    "kanji": "末",
    "reading_on": "マツ、バツ",
    "reading_kun": "すえ",
    "meaning": "끝",
    "components": [
      { "char": "一", "role": "한 일 (요소)", "desc": "가느다란 끝부분이나 지시선입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." }
    ],
    "story": "나무(木)의 가지 맨 위쪽에 선(一)을 그어, 나무의 꼭대기나 사물의 가장 나중인 '끝(마지막)'을 가리키는 글자입니다.",
    "example_words": [
      { "word": "週末", "reading": "しゅうまつ", "meaning": "주말", "description": "한 주(週)의 끝(末)인 토요일과 일요일 무렵입니다." },
      { "word": "月末", "reading": "げつまつ", "meaning": "월말", "description": "어떤 달(月)의 끝(末) 무렵입니다." }
    ]
  },
  {
    "kanji": "満",
    "reading_on": "マン",
    "reading_kun": "み(ちる)、み(たす)",
    "meaning": "찰 (가득할)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "廿", "role": "스물 입 (요소)", "desc": "여기서는 두 손으로 가득 잡고 있다는 뜻의 변형입니다." },
      { "char": "両", "role": "두 량 (요소)", "desc": "두 개, 양쪽이 다 찼다는 뜻을 줍니다." }
    ],
    "story": "그릇의 양쪽(両) 끝까지 빈틈없이 물(氵)이 꽉 '차다' 혹은 마음이 만족하여 '가득하다'는 뜻입니다.",
    "example_words": [
      { "word": "満ちる", "reading": "みちる", "meaning": "가득 차다", "description": "달이 둥글어지거나 물이나 감정이 꽉 찬 상태가 되는 것입니다." },
      { "word": "満足", "reading": "まんぞく", "meaning": "만족", "description": "모자람 없이 꽉 차서(満) 넉넉하고 족한(足) 마음입니다." }
    ]
  },
  {
    "kanji": "未",
    "reading_on": "ミ",
    "reading_kun": "いま(だ)",
    "meaning": "아닐 (아직)",
    "components": [
      { "char": "一", "role": "한 일 (요소)", "desc": "아직 덜 자란 가지를 가리키는 짧은 선입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." }
    ],
    "story": "나무(木)의 윗부분에 짧은 가지(一)를 그려 넣어 잎사귀나 가지가 '아직' 무성하게 자라지 않았음을 나타내어 '아직 ~하지 않다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "未来", "reading": "みらい", "meaning": "미래", "description": "아직(未) 오지 않은(来) 앞날입니다." },
      { "word": "未満", "reading": "みまん", "meaning": "미만", "description": "정한 수량에 아직(未) 차지(満) 않은 적은 수입니다." }
    ]
  },
  {
    "kanji": "脈",
    "reading_on": "ミャク",
    "reading_kun": "",
    "meaning": "맥 (줄기)",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "사람의 신체나 장기를 뜻합니다." },
      { "char": "永", "role": "길 영 (요소)", "desc": "원래 피가 갈라져 나간다는 뜻인 派(갈래 파)의 변형으로, 길게 뻗어 있다는 의미입니다." }
    ],
    "story": "사람의 몸(月) 속에서 피가 나뭇가지처럼 길게(永의 변형) 뻗어나가며 뛰는 핏줄, 즉 '맥박'이나 산맥의 '줄기'를 뜻합니다.",
    "example_words": [
      { "word": "脈", "reading": "みゃく", "meaning": "맥, 맥박", "description": "혈관에서 피가 돌 때 느껴지는 박동이나 이어지는 줄기입니다." },
      { "word": "山脈", "reading": "さんみゃく", "meaning": "산맥", "description": "산(山)들이 맥(脈)처럼 길게 줄지어 이어진 띠입니다." }
    ]
  },
  {
    "kanji": "民",
    "reading_on": "ミン",
    "reading_kun": "たみ",
    "meaning": "백성",
    "components": [
      { "char": "氏", "role": "성씨 씨 (부수)", "desc": "본래 눈(目)의 상형이 氏 형태로 바뀐 것입니다." }
    ],
    "story": "옛날 포로로 잡힌 사람의 한쪽 눈(氏 모양의 원형)을 바늘로 멀게 하여 노예로 부린 데서 유래했으나, 나중에는 나라에 속한 평범한 '백성'이나 '국민'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "国民", "reading": "こくみん", "meaning": "국민", "description": "한 나라(国)에 속한 백성(民)입니다." },
      { "word": "市民", "reading": "しみん", "meaning": "시민", "description": "시(市)라는 행정 구역 안에 사는 백성(民)입니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade4.json'
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

print("Grade 4 Part 6 data appended successfully.")
