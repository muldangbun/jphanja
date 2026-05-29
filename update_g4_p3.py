import json
import os

new_data = [
  {
    "kanji": "験",
    "reading_on": "ケン、ゲン",
    "reading_kun": "",
    "meaning": "시험할",
    "components": [
      { "char": "馬", "role": "말 마 (부수)", "desc": "말을 뜻합니다." },
      { "char": "僉", "role": "다 첨 (요소)", "desc": "여러 사람이 모여 의논하거나 검사한다는 뜻과 발음 '첨/켄'을 줍니다." }
    ],
    "story": "말(馬)의 상태가 좋은지 여러 사람(僉)이 모여 요리조리 타보고 검사하며 '시험하다' 혹은 겪어본 '경험'을 뜻합니다.",
    "example_words": [
      { "word": "試験", "reading": "しけん", "meaning": "시험", "description": "실력을 시험해(試) 보고 검사하는(験) 일입니다." },
      { "word": "経験", "reading": "けいけん", "meaning": "경험", "description": "직접 거치고(経) 시험해(験) 보며 겪은 일입니다." }
    ]
  },
  {
    "kanji": "固",
    "reading_on": "コ",
    "reading_kun": "かた(める)、かた(まる)、かた(い)",
    "meaning": "굳을",
    "components": [
      { "char": "囗", "role": "큰입구 몸 (부수)", "desc": "사방이 막힌 울타리나 성벽을 뜻합니다." },
      { "char": "古", "role": "예 고 (요소)", "desc": "오래되었다는 뜻과 발음 '고/코'를 담당합니다." }
    ],
    "story": "사방을 둘러싼 울타리(囗)가 시간이 오래(古) 지나도 무너지지 않고 단단하게 '굳다'라는 뜻입니다.",
    "example_words": [
      { "word": "固い", "reading": "かたい", "meaning": "단단하다, 굳다", "description": "물건이 야무지고 단단한 상태입니다." },
      { "word": "固定", "reading": "こてい", "meaning": "고정", "description": "단단하게(固) 정하여(定) 움직이지 않게 하는 것입니다." }
    ]
  },
  {
    "kanji": "功",
    "reading_on": "コウ、ク",
    "reading_kun": "",
    "meaning": "공로",
    "components": [
      { "char": "工", "role": "장인 공 (요소)", "desc": "물건을 만드는 기술이나 도구, 발음 '공/코우'를 줍니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 의미합니다." }
    ],
    "story": "훌륭한 기술(工)과 엄청난 힘(力)을 들여 이룩해 낸 훌륭한 성과나 업적인 '공로(공)'를 뜻합니다.",
    "example_words": [
      { "word": "成功", "reading": "せいこう", "meaning": "성공", "description": "목적하는 바를 이루어(成) 공(功)을 세우는 것입니다." },
      { "word": "功績", "reading": "こうせき", "meaning": "공적", "description": "훌륭하게 이룩한 공로(功)와 업적(績)입니다." }
    ]
  },
  {
    "kanji": "好",
    "reading_on": "コウ",
    "reading_kun": "この(む)、す(く)",
    "meaning": "좋을",
    "components": [
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성이나 어머니를 의미합니다." },
      { "char": "子", "role": "아들 자 (요소)", "desc": "아이를 뜻합니다." }
    ],
    "story": "어머니(女)가 자기 아이(子)를 안고 예뻐하듯, 서로 아끼고 '좋아하다' 혹은 '좋다'라는 뜻입니다.",
    "example_words": [
      { "word": "好き", "reading": "すき", "meaning": "좋아함", "description": "마음에 들어 호감을 가지는 상태입니다." },
      { "word": "好物", "reading": "こうぶつ", "meaning": "좋아하는 음식", "description": "입맛에 맞아 좋아하는(好) 음식(物)입니다." }
    ]
  },
  {
    "kanji": "候",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "기후 (기다릴 / 철)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "矦", "role": "과녁 후 (요소)", "desc": "활시위를 당겨 과녁을 겨눈다는 뜻으로 여기서는 과녁을 응시하며 살핀다는 뜻과 발음 '후/코우'를 줍니다." }
    ],
    "story": "사람(亻)이 활을 들고 적의 동태나 과녁(矦)을 눈여겨보며 살피듯, 날씨의 변화를 살피거나 '기다리다'는 데서 날씨나 '기후(철)'를 뜻합니다.",
    "example_words": [
      { "word": "気候", "reading": "きこう", "meaning": "기후", "description": "일정한 지역의 날씨나 기운(気)의 상태(候)입니다." },
      { "word": "天候", "reading": "てんこう", "meaning": "날씨", "description": "하늘(天)의 상태나 기후(候)입니다." }
    ]
  },
  {
    "kanji": "航",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "배 다닐 (항해할)",
    "components": [
      { "char": "舟", "role": "배 주 (부수)", "desc": "배나 선박을 뜻합니다." },
      { "char": "亢", "role": "목항아리 항 (요소)", "desc": "사람의 목이나 곧게 뻗어나간다는 뜻과 발음 '항/코우'를 줍니다." }
    ],
    "story": "배(舟)가 목줄기처럼 곧게(亢) 뻗어 있는 넓은 물길을 따라 앞으로 나아간다, 즉 '항해하다(배가 다니다)'는 뜻입니다.",
    "example_words": [
      { "word": "航空", "reading": "こうくう", "meaning": "항공", "description": "하늘(空)을 배처럼 날아다니는(航) 일입니다." },
      { "word": "航海", "reading": "こうかい", "meaning": "항해", "description": "배를 타고 바다(海) 위를 다니는(航) 일입니다." }
    ]
  },
  {
    "kanji": "康",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "편안할",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "건물이나 집, 넓은 장소를 뜻합니다." },
      { "char": "隶", "role": "미칠 이 (요소)", "desc": "여기서는 곡식을 까부르는 키(도구)와 양손을 본뜬 庚(별 경)의 변형으로, 풍년이 들어 평온하다는 뜻을 줍니다." }
    ],
    "story": "집안(广)에 곡식이 가득하여 사람들이 배부르고 근심 없이 몸과 마음이 '편안하다' 혹은 건강하다는 뜻입니다.",
    "example_words": [
      { "word": "健康", "reading": "けんこう", "meaning": "건강", "description": "몸이 굳세고(健) 편안한(康) 상태입니다." }
    ]
  },
  {
    "kanji": "告",
    "reading_on": "コク",
    "reading_kun": "つ(げる)",
    "meaning": "알릴",
    "components": [
      { "char": "牛", "role": "소 우 (요소)", "desc": "제물로 바치는 소를 의미합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 말하는 것을 뜻합니다." }
    ],
    "story": "소(牛)를 제물로 바치고 신에게 입(口)으로 축문을 읽어 소원을 '알리다' 혹은 '고하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "告げる", "reading": "つげる", "meaning": "알리다, 고하다", "description": "어떤 사실이나 뜻을 말로 전해 알리는 것입니다." },
      { "word": "報告", "reading": "ほうこく", "meaning": "보고", "description": "일의 결과에 대해 갚아(報) 알리는(告) 일입니다." }
    ]
  },
  {
    "kanji": "差",
    "reading_on": "サ",
    "reading_kun": "さ(す)",
    "meaning": "어긋날 (차이)",
    "components": [
      { "char": "羊", "role": "양 양 (요소)", "desc": "여기서는 본래 늘어뜨린다는 뜻의 𠂹(늘어질 수)의 변형입니다." },
      { "char": "工", "role": "장인 공 (부수)", "desc": "도구나 손의 동작을 뜻합니다." }
    ],
    "story": "손에 도구(工)를 들고 가지가 늘어진(羊의 변형) 나무를 비스듬히 자른다는 데서, 높낮이가 달라서 생기는 '차이'나 '어긋남'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "差", "reading": "さ", "meaning": "차이", "description": "서로 어긋나거나 같지 않은 정도입니다." },
      { "word": "交差点", "reading": "こうさてん", "meaning": "교차점, 교차로", "description": "두 개 이상의 길이 엇갈려(交差) 만나는 지점(点)입니다." }
    ]
  },
  {
    "kanji": "菜",
    "reading_on": "サイ",
    "reading_kun": "な",
    "meaning": "나물 (채소)",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "식물이나 풀을 의미합니다." },
      { "char": "采", "role": "캘 채 (요소)", "desc": "손으로 나무의 열매나 잎을 캔다는 뜻과 발음 '채/사이'를 줍니다." }
    ],
    "story": "사람이 밭에 가서 손으로 캐어(采) 반찬으로 먹는 식물(艹), 즉 '나물'이나 '채소'를 뜻합니다.",
    "example_words": [
      { "word": "野菜", "reading": "やさい", "meaning": "채소, 야채", "description": "들(野)에서 나는 나물(菜)이나 밭에서 기른 채소입니다." },
      { "word": "菜っ葉", "reading": "なっぱ", "meaning": "푸른 채소 잎", "description": "잎을 먹는 잎채소입니다." }
    ]
  },
  {
    "kanji": "最",
    "reading_on": "サイ",
    "reading_kun": "もっと(も)",
    "meaning": "가장",
    "components": [
      { "char": "曰", "role": "가로 왈 (부수)", "desc": "여기서는 원래 冃(모자 모)의 변형으로 덮거나 위에 있다는 뜻입니다." },
      { "char": "取", "role": "취할 취 (요소)", "desc": "손으로 귀를 잡아 취하다는 뜻으로, 물건을 빼앗거나 모은다는 뜻을 줍니다." }
    ],
    "story": "여러 가지 취해서(取) 모아놓은 것 중에서 제일 위(曰의 원래 형태)에 있는 으뜸가는 것, 즉 '가장' 뛰어나거나 맨 처음이라는 뜻입니다.",
    "example_words": [
      { "word": "最も", "reading": "もっとも", "meaning": "가장, 제일", "description": "여럿 가운데 으뜸가는 정도입니다." },
      { "word": "最近", "reading": "さいきん", "meaning": "최근", "description": "가장(最) 가까운(近) 얼마 전부터 지금까지의 무렵입니다." }
    ]
  },
  {
    "kanji": "材",
    "reading_on": "ザイ",
    "reading_kun": "",
    "meaning": "재목",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "才", "role": "재주 재 (요소)", "desc": "원래 싹이 트는 모양으로 재능이나 자질을 뜻하며 발음 '재/자이'를 담당합니다." }
    ],
    "story": "건물이나 물건을 만드는 데 바탕(자질: 才)이 되는 좋은 나무(木), 즉 '재목'이나 '재료'를 의미합니다.",
    "example_words": [
      { "word": "材料", "reading": "ざいりょう", "meaning": "재료", "description": "물건을 만드는 데 바탕이 되는 재목(材)이나 원료(料)입니다." },
      { "word": "木材", "reading": "もくざい", "meaning": "목재", "description": "나무(木)로 된 재목(材)입니다." }
    ]
  },
  {
    "kanji": "昨",
    "reading_on": "サク",
    "reading_kun": "",
    "meaning": "어제",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 날짜, 시간을 뜻합니다." },
      { "char": "乍", "role": "잠깐 사 (요소)", "desc": "도끼로 나무를 깎는 모양에서 잠깐이나 비로소라는 뜻과 발음 '작/사쿠'를 줍니다." }
    ],
    "story": "오늘이라는 날(日)에서 바로 하루 전으로 떨어져 나간 날, 즉 '어제'나 지난날을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "昨日", "reading": "きのう", "meaning": "어제", "description": "오늘의 바로 하루 전날입니다. (특별한 읽기로 きのう라고 읽습니다.)" },
      { "word": "昨年", "reading": "さくねん", "meaning": "작년", "description": "지난(昨) 해(年)입니다." }
    ]
  },
  {
    "kanji": "札",
    "reading_on": "サツ",
    "reading_kun": "ふだ",
    "meaning": "조각 (패)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "乚", "role": "새을 (요소)", "desc": "여기서는 구부러진 갈고리 모양으로, 새기거나 쓴다는 의미를 암시합니다." }
    ],
    "story": "종이가 없던 옛날에 얇게 깎은 나무(木) 조각에 글씨를 써서 남기던 '팻말'이나 '패(조각)', 현대에는 지폐를 뜻하기도 합니다.",
    "example_words": [
      { "word": "札", "reading": "ふだ", "meaning": "팻말, 꼬리표", "description": "글자를 적은 나무 조각이나 종이표입니다." },
      { "word": "お札", "reading": "おさつ", "meaning": "지폐", "description": "종이로 만든 돈입니다." }
    ]
  },
  {
    "kanji": "刷",
    "reading_on": "サツ",
    "reading_kun": "す(る)",
    "meaning": "인쇄할 (쓸)",
    "components": [
      { "char": "尸", "role": "주검 시 (요소)", "desc": "원래 巾(수건 건)의 변형으로 수건이나 천을 의미합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 문지르거나 깎는 동작을 나타냅니다." }
    ],
    "story": "글자를 새긴 판 위에 잉크를 묻힌 수건이나 솔(尸의 변형)을 대고 칼(刂)처럼 도구로 문질러 종이에 글자를 '찍어내다(인쇄하다)'는 뜻입니다.",
    "example_words": [
      { "word": "印刷", "reading": "いんさつ", "meaning": "인쇄", "description": "글자나 그림을 도장 찍듯(印) 찍어내는(刷) 것입니다." },
      { "word": "刷る", "reading": "する", "meaning": "찍다, 인쇄하다", "description": "판에 잉크를 발라 종이에 찍어내는 일입니다." }
    ]
  },
  {
    "kanji": "殺",
    "reading_on": "サツ、サイ、セツ",
    "reading_kun": "ころ(す)",
    "meaning": "죽일",
    "components": [
      { "char": "乂", "role": "벨 예 (요소)", "desc": "가위표 모양으로 베어내거나 자른다는 뜻입니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "나무나 무기를 상징합니다." },
      { "char": "殳", "role": "창 수 (부수)", "desc": "창이나 무기를 들고 치는 동작입니다." }
    ],
    "story": "손에 창(殳) 같은 무기를 들고 덤불이나 나무(木)를 베어내듯(乂), 적을 강하게 쳐서 생명을 뺏고 '죽이다'는 뜻입니다.",
    "example_words": [
      { "word": "殺す", "reading": "ころす", "meaning": "죽이다", "description": "생명을 끊어지게 하는 일입니다." },
      { "word": "殺人", "reading": "さつじん", "meaning": "살인", "description": "사람(人)을 죽이는(殺) 것입니다." }
    ]
  },
  {
    "kanji": "察",
    "reading_on": "サツ",
    "reading_kun": "",
    "meaning": "살필",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 건물을 뜻합니다." },
      { "char": "祭", "role": "제사 제 (요소)", "desc": "손으로 고기를 제단에 바치며 신의 뜻을 살핀다는 의미와 발음 '찰/사츠'를 줍니다." }
    ],
    "story": "집(宀) 안의 제단에서 제사(祭)를 지내며 신의 마음이 어떤지 세심하게 '살피다(관찰하다)'라는 뜻입니다.",
    "example_words": [
      { "word": "警察", "reading": "けいさつ", "meaning": "경찰", "description": "법을 어기는 사람이 있는지 경계하며(警) 살피는(察) 조직입니다." },
      { "word": "観察", "reading": "かんさつ", "meaning": "관찰", "description": "눈으로 보고(観) 주의 깊게 살피는(察) 것입니다." }
    ]
  },
  {
    "kanji": "参",
    "reading_on": "サン",
    "reading_kun": "まい(る)",
    "meaning": "참여할 / 석 (숫자)",
    "components": [
      { "char": "厶", "role": "마늘 모 (부수)", "desc": "원래 별 삼(參) 자의 윗부분으로 3개의 별을 나타냈습니다." },
      { "char": "大", "role": "큰 대 (요소)", "desc": "사람의 모습을 나타냅니다." },
      { "char": "彡", "role": "터럭 삼 (요소)", "desc": "빛나는 별빛이나 머리장식을 의미합니다." }
    ],
    "story": "본래 밤하늘에 빛나는(彡) 별 세 개(별자리)를 뜻하여 숫자 '3'을 의미했으나, 나중에는 높은 사람의 부름을 받고 무리에 '참여하다(가다)'는 뜻으로 주로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "参る", "reading": "まいる", "meaning": "가다, 오다 (겸양어)", "description": "가거나 오는 것을 낮추어 정중하게 표현하는 말입니다." },
      { "word": "参加", "reading": "さんか", "meaning": "참가", "description": "어떤 모임에 끼어들어(参) 뜻을 더하는(加) 것입니다." }
    ]
  },
  {
    "kanji": "産",
    "reading_on": "サン",
    "reading_kun": "う(む)、う(まれる)",
    "meaning": "낳을 (생산할)",
    "components": [
      { "char": "文", "role": "글월 문 (요소)", "desc": "여기서는 이마에 난 주름이나 무늬를 뜻하는 彦(선비 언)의 변형입니다." },
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "이마의 모양을 나타냅니다." },
      { "char": "生", "role": "날 생 (부수)", "desc": "아기가 태어난다는 뜻입니다." }
    ],
    "story": "사람의 이마(문과 엄의 결합 형태)에 주름이 질 정도로 땀을 뻘뻘 흘리며 새 생명을 '낳다(출산하다)' 혹은 물건을 '생산하다'는 뜻입니다.",
    "example_words": [
      { "word": "産む", "reading": "うむ", "meaning": "낳다", "description": "새끼나 알을 낳거나, 새로운 것을 만들어내는 것입니다." },
      { "word": "生産", "reading": "せいさん", "meaning": "생산", "description": "물건을 새로 만들어(生) 내는(産) 일입니다." }
    ]
  },
  {
    "kanji": "散",
    "reading_on": "サン",
    "reading_kun": "ち(る)、ち(らす)、ち(らかる)",
    "meaning": "흩을",
    "components": [
      { "char": "艹", "role": "초두머리 (요소)", "desc": "원래 고기를 나타내는 肉의 변형이거나 흩어지는 나뭇잎입니다." },
      { "char": "月", "role": "육달월 (요소)", "desc": "여기서는 고기나 사물을 의미합니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손으로 치거나 두드려 부순다는 의미입니다." }
    ],
    "story": "고기나 물건을 몽둥이(攵)로 때려 부수어 사방으로 조각조각 '흩어지게 하다(흩어지다)'는 뜻입니다.",
    "example_words": [
      { "word": "散る", "reading": "ちる", "meaning": "지다, 흩어지다", "description": "꽃잎이 떨어지거나 사람들이 뿔뿔이 흩어지는 것입니다." },
      { "word": "散歩", "reading": "さんぽ", "meaning": "산책", "description": "기분 전환을 위해 발걸음(歩)을 흩날리듯(散) 걷는 것입니다." }
    ]
  },
  {
    "kanji": "残",
    "reading_on": "ザン",
    "reading_kun": "のこ(る)、のこ(す)",
    "meaning": "남을",
    "components": [
      { "char": "歹", "role": "부서진뼈 알 (부수)", "desc": "죽은 짐승이나 뼈만 남은 시체를 뜻합니다." },
      { "char": "戔", "role": "상할 잔 (요소)", "desc": "창(戈)이 두 개 겹쳐 찌르고 다친다는 뜻과 발음 '잔/잔'을 줍니다." }
    ],
    "story": "창에 찔려 상처를 입고 뼈(歹)만 앙상하게 '남다', 혹은 목숨이 간신히 붙어 '남아 있다'는 뜻입니다.",
    "example_words": [
      { "word": "残る", "reading": "のこる", "meaning": "남다", "description": "다 없어지지 않고 뒷부분이 남아 있는 상태입니다." },
      { "word": "残念", "reading": "ざんねん", "meaning": "유감, 아쉬움", "description": "생각이나 미련(念)이 아직 남아 있는(残) 아쉬운 상태입니다." }
    ]
  },
  {
    "kanji": "士",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "선비",
    "components": [
      { "char": "士", "role": "선비 사 (부수)", "desc": "남자의 성기나 무기를 본뜬 글자로 건장한 남성을 뜻합니다." }
    ],
    "story": "학문과 무예를 익혀 도끼 같은 무기(士의 원형)를 들고 나랏일을 하거나 군사가 된 어엿한 남성인 '선비'나 '관리'를 의미합니다.",
    "example_words": [
      { "word": "武士", "reading": "ぶし", "meaning": "무사, 사무라이", "description": "무예(武)를 익혀 싸우는 선비(士)입니다." },
      { "word": "消防士", "reading": "しょうぼうし", "meaning": "소방관", "description": "불을 끄는(消防) 일을 맡은 직업인(士)입니다." }
    ]
  },
  {
    "kanji": "氏",
    "reading_on": "シ",
    "reading_kun": "うじ",
    "meaning": "성씨",
    "components": [
      { "char": "氏", "role": "성씨 씨 (부수)", "desc": "조상의 위패 모양이나 숟가락 모양, 혹은 땅 밑으로 뿌리를 내린 모양을 본뜬 글자입니다." }
    ],
    "story": "같은 조상(위패)을 모시며 혈연으로 맺어진 한 핏줄인 '성씨(가문)'를 뜻하며, 나중에 사람을 높여 부르는 '씨'로도 쓰입니다.",
    "example_words": [
      { "word": "氏名", "reading": "しめい", "meaning": "성명", "description": "가문의 성(氏)과 이름(名)입니다." },
      { "word": "氏", "reading": "うじ", "meaning": "가문, 씨", "description": "같은 성을 쓰는 집안이나 사람을 높여 부르는 말입니다." }
    ]
  },
  {
    "kanji": "史",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "역사",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "여기서는 문서나 책이 담긴 상자를 의미합니다." },
      { "char": "乂", "role": "벨 예 (요소)", "desc": "손으로 붓이나 칼을 쥐고 있는 모양(又)의 변형입니다." }
    ],
    "story": "손(乂의 변형)에 붓을 들고 책(口의 변형)에 나라의 일이나 지난 과거의 사실을 기록하는 사람, 혹은 그 기록인 '역사'를 뜻합니다.",
    "example_words": [
      { "word": "歴史", "reading": "れきし", "meaning": "역사", "description": "지난 세월(歴) 동안 일어난 일을 기록한 문헌(史)입니다." },
      { "word": "日本史", "reading": "にほんし", "meaning": "일본사", "description": "일본(日本)의 역사(史)입니다." }
    ]
  },
  {
    "kanji": "司",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "맡을",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "명령을 내리는 입이나 관청을 뜻합니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "명령이나 깃발 모양을 나타내는 司의 윗부분(후에 변형)입니다." }
    ],
    "story": "사람의 뒤에서 입(口)으로 명령을 내려 일을 시키고 '맡아보다' 혹은 어떤 일을 지휘하는 사람(벼슬)을 의미합니다.",
    "example_words": [
      { "word": "司会", "reading": "しかい", "meaning": "사회", "description": "모임이나 회의(会)를 맡아(司) 진행하는 사람이나 그 일입니다." },
      { "word": "上司", "reading": "じょうし", "meaning": "상사", "description": "회사 등에서 나보다 위(上)에서 일을 지휘하고 맡아보는(司) 사람입니다." }
    ]
  },
  {
    "kanji": "試",
    "reading_on": "シ",
    "reading_kun": "こころ(みる)、ため(す)",
    "meaning": "시험할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말로 묻거나 조사하는 것을 뜻합니다." },
      { "char": "式", "role": "법 식 (요소)", "desc": "정해진 법이나 규칙, 발음 '식/시'를 담당합니다." }
    ],
    "story": "말(言)로 질문하여 상대가 정해진 법도(式)나 지식을 잘 아는지 '시험하다' 혹은 '시도해 보다'라는 뜻입니다.",
    "example_words": [
      { "word": "試す", "reading": "ためす", "meaning": "시험하다, 시도하다", "description": "실력이나 상태를 알아보기 위해 실제로 해보는 것입니다." },
      { "word": "試験", "reading": "しけん", "meaning": "시험", "description": "실력을 알아보고(試) 검사하는(験) 일입니다." }
    ]
  },
  {
    "kanji": "児",
    "reading_on": "ジ、ニ",
    "reading_kun": "",
    "meaning": "아이",
    "components": [
      { "char": "臼", "role": "절구 구 (요소)", "desc": "원래 어린아이의 이빨이 난 벌어진 입술 모양입니다." },
      { "char": "儿", "role": "어진사람인발 (부수)", "desc": "사람의 다리나 아이를 뜻합니다." }
    ],
    "story": "유치가 듬성듬성 난 입(臼의 변형)을 벌리고 웃고 있는 어린아이(儿)를 뜻하여 '아동'이나 어린 '아이'를 뜻합니다.",
    "example_words": [
      { "word": "児童", "reading": "じどう", "meaning": "아동", "description": "나이가 어린(児) 아이(童)입니다." },
      { "word": "幼児", "reading": "ようじ", "meaning": "유아", "description": "나이가 아주 어린(幼) 아이(児)입니다." }
    ]
  },
  {
    "kanji": "治",
    "reading_on": "ジ、チ",
    "reading_kun": "おさ(める)、おさ(まる)、なお(る)、なお(す)",
    "meaning": "다스릴",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "台", "role": "별 태 (요소)", "desc": "높은 곳에서 말하다는 뜻과 함께 발음 '태/치'를 줍니다." }
    ],
    "story": "높은 곳(台)에서 명령을 내려 강물(氵)이 넘치지 않게 치수를 잘하여 백성을 평안하게 '다스리다', 혹은 아픈 몸을 '고치다'는 뜻입니다.",
    "example_words": [
      { "word": "治る", "reading": "なおる", "meaning": "낫다", "description": "병이나 상처가 고쳐져서 본래대로 회복되는 것입니다." },
      { "word": "政治", "reading": "せいじ", "meaning": "정치", "description": "나라의 일이나 백성을 바르게(政) 다스리는(治) 일입니다." }
    ]
  },
  {
    "kanji": "辞",
    "reading_on": "ジ",
    "reading_kun": "や(める)",
    "meaning": "말씀 (사양할)",
    "components": [
      { "char": "舌", "role": "혀 설 (요소)", "desc": "원래 얽힌 실타래 모양인 𤔔(어지러울 란)이 간략화된 것입니다." },
      { "char": "辛", "role": "매울 신 (부수)", "desc": "형벌 도구로 침을 찌르듯 맵고 단호하다는 뜻입니다." }
    ],
    "story": "복잡하게 얽힌 문제(舌의 원래 뜻)를 단호하게(辛) 판결하여 내리는 '말씀(글)'이나, 벼슬이나 자리를 단호히 '사양하고 물러나다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "辞める", "reading": "やめる", "meaning": "그만두다, 사임하다", "description": "맡고 있던 직위나 일을 스스로 물러나 그만두는 것입니다." },
      { "word": "辞典", "reading": "じてん", "meaning": "사전", "description": "단어와 뜻(辞)을 모아놓은 책(典)입니다." }
    ]
  },
  {
    "kanji": "失",
    "reading_on": "シツ",
    "reading_kun": "うしな(う)",
    "meaning": "잃을",
    "components": [
      { "char": "手", "role": "손 수 (요소)", "desc": "손의 모양입니다." },
      { "char": "丿", "role": "삐침 (요소)", "desc": "물건이 손에서 미끄러져 빠져나가는 모습을 나타냅니다." }
    ],
    "story": "손(手)에 쥐고 있던 물건이 스르르 미끄러져(丿) 빠져나가는 모습에서 소중한 것을 '잃어버리다(상실하다)' 혹은 실수를 한다는 의미입니다.",
    "example_words": [
      { "word": "失う", "reading": "うしなう", "meaning": "잃다", "description": "가지고 있던 것이 떨어져 나가거나 놓치는 것입니다." },
      { "word": "失敗", "reading": "しっぱい", "meaning": "실패", "description": "일을 잘못하여 잃어버리고(失) 무너져 지는(敗) 것입니다." }
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

print("Grade 4 Part 3 data appended successfully.")
