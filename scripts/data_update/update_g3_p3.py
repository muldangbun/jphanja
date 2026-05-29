import json
import os

new_data = [
  {
    "kanji": "皿",
    "reading_on": "ベイ",
    "reading_kun": "さら",
    "meaning": "그릇 / 접시",
    "components": [
      { "char": "皿", "role": "그릇 명 (부수)", "desc": "음식을 담는 오목한 그릇이나 넓적한 접시의 모양을 본뜬 글자입니다." }
    ],
    "story": "위가 넓고 바닥이 평평한 모양의 밥그릇이나 '접시'의 형태를 그대로 그린 한자입니다.",
    "example_words": [
      { "word": "灰皿", "reading": "はいざら", "meaning": "재떨이", "description": "재(灰)를 담는 접시(皿)입니다." },
      { "word": "お皿", "reading": "おさら", "meaning": "접시", "description": "음식을 담는 둥글고 납작한 그릇입니다." }
    ]
  },
  {
    "kanji": "仕",
    "reading_on": "シ、ジ",
    "reading_kun": "つか(える)",
    "meaning": "섬길",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "士", "role": "선비 사 (요소)", "desc": "학식과 능력을 갖춘 선비나 관리를 의미합니다." }
    ],
    "story": "사람(亻)이 선비(士)처럼 능력을 갖추고 관직에 나아가 윗사람이나 국가를 '섬긴다'는 뜻입니다.",
    "example_words": [
      { "word": "仕事", "reading": "しごと", "meaning": "일, 직업", "description": "맡아서 섬기는(仕) 일(事)입니다." },
      { "word": "仕方", "reading": "しかた", "meaning": "방법, 방도", "description": "어떤 일을 하는(仕) 방법(方)입니다." }
    ]
  },
  {
    "kanji": "死",
    "reading_on": "シ",
    "reading_kun": "し(ぬ)",
    "meaning": "죽을",
    "components": [
      { "char": "歹", "role": "부서진 뼈 알 (부수)", "desc": "사람의 뼈가 흩어져 있는 모양으로 죽음을 뜻합니다." },
      { "char": "匕", "role": "비수 비 (요소)", "desc": "여기서는 사람이 뒤집혀 있거나 땅에 쓰러져 있는 모양입니다." }
    ],
    "story": "사람이 거꾸로 쓰러져(匕) 백골(歹)이 되어 '죽다'라는 뜻을 적나라하게 나타내는 한자입니다.",
    "example_words": [
      { "word": "死ぬ", "reading": "しぬ", "meaning": "죽다", "description": "생명이 끝나는 것입니다." },
      { "word": "必死", "reading": "ひっし", "meaning": "필사", "description": "반드시(必) 죽기(死) 살기로 온 힘을 다하는 것입니다." }
    ]
  },
  {
    "kanji": "使",
    "reading_on": "シ",
    "reading_kun": "つか(う)",
    "meaning": "부릴 / 사용하다",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "吏", "role": "벼슬아치 리 (요소)", "desc": "도구를 들고 문서를 처리하는 관리로, 어떤 일을 시키거나 맡기는 모양입니다." }
    ],
    "story": "사람(亻)을 관리(吏)처럼 어떤 일에 맡겨서 심부름을 '부리다' 혹은 도구를 '사용하다'라는 뜻입니다.",
    "example_words": [
      { "word": "使う", "reading": "つかう", "meaning": "사용하다", "description": "도구나 사람을 부려서 목적에 맞게 쓰는 것입니다." },
      { "word": "大使", "reading": "たいし", "meaning": "대사", "description": "나라의 명을 받아 부름을 받은(使) 큰(大) 대표자입니다." }
    ]
  },
  {
    "kanji": "始",
    "reading_on": "シ",
    "reading_kun": "はじ(める)、はじ(まる)",
    "meaning": "비로소 / 시작하다",
    "components": [
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여성이나 생명의 탄생을 의미합니다." },
      { "char": "台", "role": "별 태 (요소)", "desc": "아기가 태어나는 모습이거나, '태/시' 발음을 줍니다." }
    ],
    "story": "여자(女)가 잉태하여 아이(台)를 낳으면서 모든 생명과 생애가 '처음'으로 '시작된다'는 뜻입니다.",
    "example_words": [
      { "word": "始める", "reading": "はじめる", "meaning": "시작하다", "description": "새로운 일을 처음으로 시작하는 것입니다." },
      { "word": "開始", "reading": "かいし", "meaning": "개시", "description": "문을 열고(開) 처음으로 일을 시작(始)하는 것입니다." }
    ]
  },
  {
    "kanji": "指",
    "reading_on": "シ",
    "reading_kun": "ゆび、さ(す)",
    "meaning": "손가락 / 가리키다",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손의 동작과 관련됨을 나타냅니다." },
      { "char": "旨", "role": "맛있을 지 (요소)", "desc": "맛있는 음식을 의미하며, 발음 '지/시'를 담당합니다." }
    ],
    "story": "맛있는(旨) 음식을 손(扌)으로 집어 먹던 도구인 '손가락', 혹은 그 손가락으로 특정 방향을 '가리키다'는 뜻입니다.",
    "example_words": [
      { "word": "指", "reading": "ゆび", "meaning": "손가락", "description": "손끝에 갈라진 다섯 개의 부분입니다." },
      { "word": "指定", "reading": "してい", "meaning": "지정", "description": "손가락으로 가리켜서(指) 확실하게 정하는(定) 것입니다." }
    ]
  },
  {
    "kanji": "止",
    "reading_on": "シ",
    "reading_kun": "と(まる)、と(める)",
    "meaning": "그칠 / 멈추다",
    "components": [
      { "char": "止", "role": "그칠 지 (부수)", "desc": "사람의 발자국 모양에서 유래했습니다." }
    ],
    "story": "걷던 발자국을 땅에 단단히 디디고 서서 움직임을 '멈추다' 혹은 하던 일을 '그치다'는 의미입니다.",
    "example_words": [
      { "word": "止まる", "reading": "とまる", "meaning": "멈추다", "description": "움직임이나 흐름이 멈춰 서는 것입니다." },
      { "word": "中止", "reading": "ちゅうし", "meaning": "중지", "description": "중간(中)에 하던 일을 멈추는(止) 것입니다." }
    ]
  },
  {
    "kanji": "詩",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "시",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 언어, 글을 뜻합니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "원래 志(뜻 지)에서 변형된 것으로, 마음속의 뜻과 발음 '지/시'를 줍니다." }
    ],
    "story": "마음속 깊은 곳에 품고 있는 뜻이나 감정(寺의 원래 의미)을 압축된 말이나 글(言)로 표현한 문학인 '시'를 뜻합니다.",
    "example_words": [
      { "word": "詩人", "reading": "しじん", "meaning": "시인", "description": "시(詩)를 짓는 사람(人)입니다." },
      { "word": "詩集", "reading": "ししゅう", "meaning": "시집", "description": "여러 시(詩)를 모아 엮은(集) 책입니다." }
    ]
  },
  {
    "kanji": "歯",
    "reading_on": "シ",
    "reading_kun": "は",
    "meaning": "이 (치아)",
    "components": [
      { "char": "止", "role": "그칠 지 (부수)", "desc": "입을 멈추고 다문 모양의 윗입술 부분을 나타냅니다." },
      { "char": "米", "role": "쌀 미 (요소)", "desc": "입안에 하얗게 늘어선 치아들의 모양(원래 齒에서 간략화됨)을 쌀알에 빗대었습니다." }
    ],
    "story": "입(止) 안에 쌀알(米)처럼 하얗고 가지런하게 늘어서 있는 '이(치아)'를 뜻하는 상형문자의 간자체입니다.",
    "example_words": [
      { "word": "歯医者", "reading": "はいしゃ", "meaning": "치과 의사", "description": "이(歯)를 고치는 의사(医者)입니다." },
      { "word": "虫歯", "reading": "むしば", "meaning": "충치", "description": "벌레(虫)가 먹어 썩은 이(歯)입니다." }
    ]
  },
  {
    "kanji": "事",
    "reading_on": "ジ、ズ",
    "reading_kun": "こと",
    "meaning": "일",
    "components": [
      { "char": "一", "role": "한 일 (요소)", "desc": "문서를 묶은 끈의 모양입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입으로 명령을 내리거나 묶여진 서류를 나타냅니다." },
      { "char": "⺕", "role": "가로왈 (요소)", "desc": "손으로 붓이나 깃발을 쥐고 있는 모습입니다." }
    ],
    "story": "손으로 붓이나 지휘봉을 쥐고 서류나 업무를 처리하는 관리의 모습에서, 다루어야 할 '일'이나 '사건'을 의미합니다.",
    "example_words": [
      { "word": "仕事", "reading": "しごと", "meaning": "일, 직업", "description": "맡아서 섬기는(仕) 일(事)입니다." },
      { "word": "食事", "reading": "しょくじ", "meaning": "식사", "description": "밥(食)을 먹는 일(事)입니다." }
    ]
  },
  {
    "kanji": "次",
    "reading_on": "ジ、シ",
    "reading_kun": "つぎ、つ(ぐ)",
    "meaning": "버금 (다음)",
    "components": [
      { "char": "冫", "role": "이수변 (요소)", "desc": "두 개라는 의미나, 얼음처럼 뒤처진다는 뜻입니다." },
      { "char": "欠", "role": "하품 흠 (부수)", "desc": "사람이 숨을 들이마시거나 침을 흘리는 모습입니다." }
    ],
    "story": "어떤 일을 하다가 숨을 돌리고(欠) 두 번째(冫)로 이어서 하는 일, 즉 첫째 다음인 '다음'이나 '버금'을 뜻합니다.",
    "example_words": [
      { "word": "次", "reading": "つぎ", "meaning": "다음", "description": "현재의 바로 뒤를 잇는 차례입니다." },
      { "word": "次回", "reading": "じかい", "meaning": "다음 회", "description": "다음(次)으로 돌아오는 차례(回)입니다." }
    ]
  },
  {
    "kanji": "持",
    "reading_on": "ジ",
    "reading_kun": "も(つ)",
    "meaning": "가질 / 쥐다",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손과 관련된 동작을 뜻합니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "관청의 법도처럼 단단히 지킨다는 의미와 '지' 발음을 줍니다." }
    ],
    "story": "손(扌)으로 어떤 물건을 관청(寺)의 법도처럼 흔들림 없이 꽉 쥐고 '가지다'라는 뜻입니다.",
    "example_words": [
      { "word": "持つ", "reading": "もつ", "meaning": "가지다, 쥐다", "description": "물건을 손에 쥐거나 상태를 유지하는 것입니다." },
      { "word": "気持ち", "reading": "きもち", "meaning": "기분", "description": "마음이나 기(気)를 가지고(持ち) 있는 상태, 즉 기분입니다." }
    ]
  },
  {
    "kanji": "式",
    "reading_on": "シキ",
    "reading_kun": "",
    "meaning": "법 / 의식",
    "components": [
      { "char": "弋", "role": "주살 익 (부수)", "desc": "말뚝이나 나무 푯말을 의미합니다." },
      { "char": "工", "role": "장인 공 (요소)", "desc": "정교하게 다듬는 도구(곱자)를 의미합니다." }
    ],
    "story": "말뚝(弋)을 기준 삼아 도구(工)를 대고 목수가 정확한 규격에 맞춰 나무를 자르는 데서 일정한 '규칙', '법도'나 '의식'을 뜻합니다.",
    "example_words": [
      { "word": "洋式", "reading": "ようしき", "meaning": "양식 (서양식)", "description": "서양(洋)의 방식이나 규칙(式)입니다." },
      { "word": "入学式", "reading": "にゅうがくしき", "meaning": "입학식", "description": "학교에 입학(入学)할 때 치르는 의식(式)입니다." }
    ]
  },
  {
    "kanji": "実",
    "reading_on": "ジツ",
    "reading_kun": "み、みの(る)",
    "meaning": "열매 / 참되다",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 건물을 뜻합니다." },
      { "char": "三", "role": "석 삼 (요소)", "desc": "가득 차 있음을 상징하는 장식(원래 貫에서 변형)입니다." },
      { "char": "大", "role": "큰 대 (요소)", "desc": "아래쪽을 받쳐주는 크고 무거운 물건을 의미합니다." }
    ],
    "story": "집(宀) 안에 재물이 가득(三) 차서 든든하게(大) 채워져 있는 모양에서, 속이 꽉 찬 '열매'나 내용이 충실한 '사실'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "事実", "reading": "じじつ", "meaning": "사실", "description": "일(事)의 참된(実) 알맹이입니다." },
      { "word": "実る", "reading": "みのる", "meaning": "열매 맺다", "description": "식물이 자라 과실이나 알맹이가 생기는 것입니다." }
    ]
  },
  {
    "kanji": "写",
    "reading_on": "シャ",
    "reading_kun": "うつ(す)、うつ(る)",
    "meaning": "베낄",
    "components": [
      { "char": "冖", "role": "민갓머리 (부수)", "desc": "덮개나 천막을 뜻합니다." },
      { "char": "与", "role": "줄 여 (요소)", "desc": "물건을 주거나 한곳에서 다른 곳으로 옮긴다는 의미(원래 모양 舄에서 간략화됨)입니다." }
    ],
    "story": "물건을 덮개(冖)로 덮어 옮기듯이(与), 그림이나 글씨를 그대로 다른 종이에 옮겨 '베끼다'는 뜻입니다.",
    "example_words": [
      { "word": "写真", "reading": "しゃしん", "meaning": "사진", "description": "참된(真) 모습을 기계로 그대로 베껴(写) 낸 그림입니다." },
      { "word": "写す", "reading": "うつす", "meaning": "베끼다, 찍다", "description": "글을 베끼거나 사진을 찍는 일입니다." }
    ]
  },
  {
    "kanji": "者",
    "reading_on": "シャ",
    "reading_kun": "もの",
    "meaning": "사람 / 놈",
    "components": [
      { "char": "耂", "role": "늙을 노 (부수)", "desc": "나이가 많은 사람을 뜻합니다." },
      { "char": "日", "role": "날 일 (요소)", "desc": "원래 白(아래로 말하다)에서 변형된 것으로, 말을 하거나 지목하는 대상을 뜻합니다." }
    ],
    "story": "나이가 많은 어른(耂)이 아랫사람(日의 원형)에게 지시를 내리거나 특정 대상을 가리킬 때 쓰는 말로, 특정한 일을 하는 '사람'을 가리키는 대명사가 되었습니다.",
    "example_words": [
      { "word": "医者", "reading": "いしゃ", "meaning": "의사", "description": "의술(医)을 행하는 사람(者)입니다." },
      { "word": "若者", "reading": "わかもの", "meaning": "젊은이", "description": "나이가 젊은(若) 사람(者)입니다." }
    ]
  },
  {
    "kanji": "主",
    "reading_on": "シュ",
    "reading_kun": "ぬし、おも",
    "meaning": "주인 / 주된",
    "components": [
      { "char": "丶", "role": "점 주 (부수)", "desc": "타오르는 촛불의 불꽃 모양을 나타냅니다." },
      { "char": "王", "role": "구슬 옥 (요소)", "desc": "여기서는 촛대의 받침을 모양을 본뜬 촛대 전체의 모습(원래 主의 몸통)입니다." }
    ],
    "story": "방 한가운데를 밝히는 촛대(王의 변형)와 타오르는 불꽃(丶)처럼, 한가운데에서 중심 역할을 하는 '주인'이나 '주된' 것을 의미합니다.",
    "example_words": [
      { "word": "主人", "reading": "しゅじん", "meaning": "남편, 주인", "description": "가정이나 가게의 중심(主)이 되는 사람(人)입니다." },
      { "word": "主な", "reading": "おもな", "meaning": "주된, 주요한", "description": "여럿 중에서 가장 중심이나 으뜸이 되는 성질입니다." }
    ]
  },
  {
    "kanji": "守",
    "reading_on": "シュ、ス",
    "reading_kun": "まも(る)",
    "meaning": "지킬",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "관청, 건물, 지붕을 뜻합니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "법도, 규칙, 혹은 손을 의미합니다." }
    ],
    "story": "손(寸)을 모아 법도를 따르며 관청이나 집(宀)을 굳게 '지키다'라는 뜻입니다.",
    "example_words": [
      { "word": "守る", "reading": "まもる", "meaning": "지키다", "description": "위험으로부터 보호하거나 약속을 어기지 않는 것입니다." },
      { "word": "留守", "reading": "るす", "meaning": "부재중", "description": "집에 머물러(留) 지키는(守) 사람이 없다는 뜻에서, 집을 비웠음을 의미합니다." }
    ]
  },
  {
    "kanji": "取",
    "reading_on": "シュ",
    "reading_kun": "と(る)",
    "meaning": "취할 / 가지다",
    "components": [
      { "char": "耳", "role": "귀 이 (부수)", "desc": "사람이나 짐승의 귀입니다." },
      { "char": "又", "role": "또 우 (요소)", "desc": "손으로 잡는 모양을 뜻합니다." }
    ],
    "story": "고대 전쟁터에서 적을 쓰러뜨린 후 그 증거로 귀(耳)를 손(又)으로 베어 '가져가다(취하다)'라는 살벌한 유래에서 유래했습니다.",
    "example_words": [
      { "word": "取る", "reading": "とる", "meaning": "잡다, 가지다", "description": "손으로 물건을 집거나 어떤 것을 자신의 것으로 만드는 것입니다." },
      { "word": "受け取る", "reading": "うけとる", "meaning": "받다, 수취하다", "description": "남이 주는 것을 받아서(受け) 가지는(取る) 일입니다." }
    ]
  },
  {
    "kanji": "酒",
    "reading_on": "シュ",
    "reading_kun": "さけ、さか",
    "meaning": "술",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 의미합니다." },
      { "char": "酉", "role": "닭 유 (요소)", "desc": "술이나 발효 식품을 담그는 밑이 뾰족한 항아리 모양을 본뜬 글자입니다." }
    ],
    "story": "항아리(酉) 안에 담겨서 향기롭게 발효되어 물(氵)처럼 찰랑거리는 액체인 '술'을 뜻합니다.",
    "example_words": [
      { "word": "お酒", "reading": "おさけ", "meaning": "술", "description": "마시는 알코올 음료를 친근하게 부르는 말입니다." },
      { "word": "日本酒", "reading": "にほんしゅ", "meaning": "사케, 일본주", "description": "일본(日本)의 전통 방식으로 빚은 술(酒)입니다." }
    ]
  },
  {
    "kanji": "受",
    "reading_on": "ジュ",
    "reading_kun": "う(ける)、う(かる)",
    "meaning": "받을",
    "components": [
      { "char": "爫", "role": "손톱 조 (요소)", "desc": "위에서 아래로 물건을 내밀어 건네주는 손의 모양입니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "물건을 건네받는 쟁반이나 덮개를 뜻합니다." },
      { "char": "又", "role": "또 우 (부수)", "desc": "아래에서 위로 물건을 받는 손의 모양입니다." }
    ],
    "story": "위에서 건네주는(爫) 물건을 쟁반(冖)에 담아 아래쪽 손(又)으로 공손하게 '받는다'는 뜻입니다.",
    "example_words": [
      { "word": "受ける", "reading": "うける", "meaning": "받다", "description": "물건이나 허락, 시험 따위를 치르거나 받아들이는 일입니다." },
      { "word": "受付", "reading": "うけつけ", "meaning": "접수처", "description": "사람이나 서류를 받아(受け) 덧붙이는(付) 곳입니다." }
    ]
  },
  {
    "kanji": "州",
    "reading_on": "シュウ",
    "reading_kun": "す",
    "meaning": "고을 / 모래톱",
    "components": [
      { "char": "川", "role": "내 천 (부수)", "desc": "물이 흐르는 강이나 시내의 모양입니다." },
      { "char": "丶", "role": "점 주 (요소)", "desc": "강물 중간중간에 솟아오른 흙이나 모래톱을 나타내는 점들입니다." }
    ],
    "story": "강물(川)이 흐르는 중간중간에 모래나 흙이 점(丶)처럼 솟아오른 모래톱을 뜻하며, 나중에 사람들이 사는 큰 행정 구역인 '고을(주)'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "本州", "reading": "ほんしゅう", "meaning": "혼슈", "description": "일본의 가장 크고 중심(本)이 되는 고을(州)이자 섬입니다." },
      { "word": "九州", "reading": "きゅうしゅう", "meaning": "규슈", "description": "과거 아홉(九) 개의 고을(州)로 나뉘었던 일본 남쪽의 큰 섬입니다." }
    ]
  },
  {
    "kanji": "拾",
    "reading_on": "シュウ、ジュウ",
    "reading_kun": "ひろ(う)",
    "meaning": "주울",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "合", "role": "합할 합 (요소)", "desc": "모으다, 합치다는 뜻을 지니고 있습니다." }
    ],
    "story": "바닥에 흩어져 있는 물건들을 손(扌)으로 여러 번 모아서(合) 한데 '줍다'는 의미입니다.",
    "example_words": [
      { "word": "拾う", "reading": "ひろう", "meaning": "줍다", "description": "떨어진 물건을 주워서 가지는 것입니다." },
      { "word": "落し物拾い", "reading": "おとしものひろい", "meaning": "분실물 습득", "description": "떨어진(落し) 물건(物)을 줍는(拾い) 일입니다." }
    ]
  },
  {
    "kanji": "終",
    "reading_on": "シュウ",
    "reading_kun": "お(わる)、お(える)",
    "meaning": "끝날",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실타래나 묶음을 의미합니다." },
      { "char": "冬", "role": "겨울 동 (요소)", "desc": "한 해의 마지막인 겨울을 뜻하며, 무언가의 끝과 발음 '동/슈우'를 줍니다." }
    ],
    "story": "실타래(糸)를 풀다가 사계절의 끝인 겨울(冬)처럼 실의 맨 끝부분에 도달하여 일이 모두 '끝났다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "終わる", "reading": "おわる", "meaning": "끝나다", "description": "어떤 일이나 동작이 모두 마쳐진 상태입니다." },
      { "word": "最終", "reading": "さいしゅう", "meaning": "최종", "description": "가장(最) 마지막으로 끝나는(終) 차례입니다." }
    ]
  },
  {
    "kanji": "習",
    "reading_on": "シュウ",
    "reading_kun": "なら(う)",
    "meaning": "익힐",
    "components": [
      { "char": "羽", "role": "깃 우 (부수)", "desc": "새의 두 날개를 본뜬 글자입니다." },
      { "char": "白", "role": "흰 백 (요소)", "desc": "원래 日(해 일) 자나 둥지를 뜻하는 글자에서 변형되어 아침 햇빛을 상징합니다." }
    ],
    "story": "어린 새가 둥지(白의 원형) 밖으로 나와 밝은 날 하늘을 날기 위해 깃발(羽)을 퍼덕이며 나는 연습을 반복해서 '익히다'는 뜻입니다.",
    "example_words": [
      { "word": "習う", "reading": "ならう", "meaning": "배우다, 익히다", "description": "남에게 가르침을 받아 기술이나 지식을 몸에 익히는 것입니다." },
      { "word": "練習", "reading": "れんしゅう", "meaning": "연습", "description": "실이나 쇠를 벼르듯(練) 반복하여 익히는(習) 일입니다." }
    ]
  },
  {
    "kanji": "集",
    "reading_on": "シュウ",
    "reading_kun": "あつ(まる)、あつ(める)",
    "meaning": "모일",
    "components": [
      { "char": "隹", "role": "새 추 (부수)", "desc": "꼬리가 짧은 통통한 새를 뜻합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "나무를 뜻합니다." }
    ],
    "story": "저녁 무렵, 숲속의 꼬리 짧은 새(隹)들이 쉴 곳을 찾아 나무(木) 위로 떼 지어 '모여드는' 모습을 본뜬 글자입니다.",
    "example_words": [
      { "word": "集まる", "reading": "あつまる", "meaning": "모이다", "description": "사람이나 물건이 한곳으로 여럿 모이는 것입니다." },
      { "word": "集中", "reading": "しゅうちゅう", "meaning": "집중", "description": "한가운데(中)로 마음이나 힘을 모으는(集) 것입니다." }
    ]
  },
  {
    "kanji": "住",
    "reading_on": "ジュウ",
    "reading_kun": "す(む)",
    "meaning": "살 / 머무를",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "主", "role": "주인 주 (요소)", "desc": "주인으로 자리 잡는다는 뜻과 발음 '주'를 담당합니다." }
    ],
    "story": "사람(亻)이 어떤 곳에 주인(主)처럼 터전을 잡고 정착하여 '살다' 혹은 '머무르다'는 뜻입니다.",
    "example_words": [
      { "word": "住む", "reading": "すむ", "meaning": "살다", "description": "어떤 장소에 집을 두고 정착하는 것입니다." },
      { "word": "住所", "reading": "じゅうしょ", "meaning": "주소", "description": "살고(住) 있는 장소(所)입니다." }
    ]
  },
  {
    "kanji": "重",
    "reading_on": "ジュウ、チョウ",
    "reading_kun": "おも(い)、かさ(ねる)",
    "meaning": "무거울 / 거듭",
    "components": [
      { "char": "千", "role": "일천 천 (요소)", "desc": "원래 사람(人)이 짐을 진 모양의 윗부분에서 변형되었습니다." },
      { "char": "里", "role": "마을 리 (부수)", "desc": "여기서는 발을 구부린 사람과 짐 보따리가 결합한 모양의 아랫부분입니다." }
    ],
    "story": "사람이 커다란 짐 꾸러미를 등에 지고 땀을 뻘뻘 흘리며 서 있는 모습에서 짐이 아주 '무겁다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "重い", "reading": "おもい", "meaning": "무겁다", "description": "무게가 많이 나가거나 병이 깊은 상태입니다." },
      { "word": "貴重品", "reading": "きちょうひん", "meaning": "귀중품", "description": "귀하고(貴) 무게가 나갈(重) 정도로 중요한 물품(品)입니다." }
    ]
  },
  {
    "kanji": "宿",
    "reading_on": "シュク",
    "reading_kun": "やど、やど(る)",
    "meaning": "묵을 / 여관",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 건물을 뜻합니다." },
      { "char": "亻", "role": "사람 인 (요소)", "desc": "사람을 뜻합니다." },
      { "char": "百", "role": "일백 백 (요소)", "desc": "여기서는 일백 백이 아니라 자리(돗자리 陌)의 변형으로, 사람이 눕는 자리를 나타냅니다." }
    ],
    "story": "지붕(宀)이 있는 집 안에서 사람(亻)이 돗자리(百의 원형)를 펴고 편안하게 하룻밤 '묵어가다'는 뜻입니다.",
    "example_words": [
      { "word": "宿題", "reading": "しゅくだい", "meaning": "숙제", "description": "집(宿)에서 풀어오도록 내준 문제(題)입니다." },
      { "word": "新宿", "reading": "しんじゅく", "meaning": "신주쿠 (지명)", "description": "도쿄의 번화가로, 새롭게(新) 생긴 여관(宿) 거리라는 뜻에서 유래했습니다." }
    ]
  },
  {
    "kanji": "所",
    "reading_on": "ショ",
    "reading_kun": "ところ",
    "meaning": "곳 (장소)",
    "components": [
      { "char": "戸", "role": "지게 호 (부수)", "desc": "외짝 문이나 방의 입구를 뜻합니다." },
      { "char": "斤", "role": "도끼 근 (요소)", "desc": "도끼로 나무를 다듬거나 장소를 고르는 도구입니다." }
    ],
    "story": "도끼(斤)를 사용하여 나무 문(戸)을 짜 맞추고 집을 지을 만한 터를 잡는다는 데서 특정한 '곳'이나 '장소'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "場所", "reading": "ばしょ", "meaning": "장소", "description": "활동하는 마당(場)과 곳(所)입니다." },
      { "word": "近所", "reading": "きんじょ", "meaning": "근처, 이웃", "description": "가까운(近) 곳(所)입니다." }
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

print("Grade 3 Part 3 data appended successfully.")
