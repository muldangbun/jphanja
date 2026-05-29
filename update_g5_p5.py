import json
import os

new_data = [
  {
    "kanji": "素",
    "reading_on": "ソ、ス",
    "reading_kun": "もと",
    "meaning": "본디 (흴)",
    "components": [
      { "char": "丰", "role": "예쁠 봉 (요소)", "desc": "여기서는 베틀에 걸어놓은 생사(물들이지 않은 명주실)가 늘어진 모양을 뜻합니다." },
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 의미합니다." }
    ],
    "story": "베틀에서 막 짜내어 아직 물들이지 않은 하얀 바탕의 명주실(糸)처럼 순수하고 아무것도 더해지지 않은 '본디(본래)'나 '바탕'을 뜻합니다.",
    "example_words": [
      { "word": "素直", "reading": "すなお", "meaning": "순순함, 솔직함", "description": "꾸밈없이 본디(素) 성질 그대로 올곧은(直) 모양입니다." },
      { "word": "要素", "reading": "ようそ", "meaning": "요소", "description": "사물을 이루는 긴요하고(要) 바탕(素)이 되는 성분입니다." }
    ]
  },
  {
    "kanji": "経",
    "reading_on": "ケイ、キョウ",
    "reading_kun": "へ(る)",
    "meaning": "지날 (경영할)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "巠", "role": "물줄기 경 (요소)", "desc": "베틀의 날실이 위아래로 꼿꼿하게 뻗은 모양으로 발음 '경/케이'를 줍니다." }
    ],
    "story": "베틀에 세로로 길게 걸어놓은 날실(巠)처럼 변하지 않는 도리나 '글(경전)'을 뜻하며, 날실이 위아래로 길게 지나가듯 세월을 '지나다(거치다)'나 나라를 '경영하다'는 뜻도 가집니다.",
    "example_words": [
      { "word": "経験", "reading": "けいけん", "meaning": "경험", "description": "자신이 실제로 겪어(経) 보고 확인하는(験) 일입니다." },
      { "word": "経済", "reading": "けいざい", "meaning": "경제", "description": "세상을 다스려(経) 백성을 구제하는(済) 재화에 관한 활동입니다." }
    ]
  },
  {
    "kanji": "統",
    "reading_on": "トウ",
    "reading_kun": "す(べる)",
    "meaning": "거느릴 (합칠)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 뜻합니다." },
      { "char": "充", "role": "채울 충 (요소)", "desc": "가득 채운다는 뜻과 발음 '충/토우'의 변형 역할을 줍니다." }
    ],
    "story": "베틀에서 여러 가닥의 실(糸)을 하나로 합쳐서 베를 짜듯, 여러 사람이나 조직을 하나로 뭉치고 '합치다(통일하다)' 혹은 통솔하여 '거느리다'는 뜻입니다.",
    "example_words": [
      { "word": "統一", "reading": "とういつ", "meaning": "통일", "description": "나누어진 것들을 합쳐(統) 하나(一)로 뭉치는 일입니다." },
      { "word": "大統領", "reading": "だいとうりょう", "meaning": "대통령", "description": "크게(大) 나라를 거느리고(統) 다스리는(領) 국가 원수입니다." }
    ]
  },
  {
    "kanji": "絶",
    "reading_on": "ゼツ",
    "reading_kun": "た(える)、た(つ)",
    "meaning": "끊을 (끊어질)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실을 뜻합니다." },
      { "char": "色", "role": "빛 색 (요소)", "desc": "원래 칼(刀)과 사람(卩)이 합쳐져 칼로 자른다는 뜻을 줍니다. (현재는 色으로 형태가 바뀜)" }
    ],
    "story": "칼로 실(糸)을 싹둑 잘라서 둘로 나누듯, 얽혀 있던 관계나 숨결이 '끊어지다' 혹은 '끊다'는 의미입니다.",
    "example_words": [
      { "word": "絶える", "reading": "たえる", "meaning": "끊어지다, 없어지다", "description": "계속 이어지던 것이 중간에 끊어지는 것입니다." },
      { "word": "絶対", "reading": "ぜったい", "meaning": "절대", "description": "비교하거나 상대(対)할 만한 것이 완전히 끊어져(絶) 없는 것입니다." }
    ]
  },
  {
    "kanji": "綿",
    "reading_on": "メン",
    "reading_kun": "わた",
    "meaning": "솜",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 천을 뜻합니다." },
      { "char": "帛", "role": "비단 백 (요소)", "desc": "비단처럼 희고 부드럽다는 뜻과 발음 '면/멘'의 변형 역할을 합니다." }
    ],
    "story": "목화송이에서 뽑아낸 희고 부드러운(帛) 실(糸), 즉 푹신푹신한 '솜'이나 '면'을 의미합니다.",
    "example_words": [
      { "word": "綿", "reading": "わた", "meaning": "솜", "description": "목화 씨를 둘러싸고 있는 흰 털을 모아 놓은 것입니다." },
      { "word": "木綿", "reading": "もめん", "meaning": "무명, 면직물", "description": "목화(木)에서 딴 솜(綿)으로 뽑은 실로 짠 천입니다." }
    ]
  },
  {
    "kanji": "総",
    "reading_on": "ソウ",
    "reading_kun": "",
    "meaning": "다 (거느릴)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실을 의미합니다." },
      { "char": "公", "role": "공평할 공 (요소)", "desc": "여러 사람을 아우른다는 뜻과 발음 '공/소우'의 변형 역할을 합니다." },
      { "char": "心", "role": "마음 심 (요소)", "desc": "마음이나 중심을 뜻합니다." }
    ],
    "story": "여러 가닥의 실(糸)을 한데 모아 묶듯이, 마음(心)을 모아 여러 사람이나 물건을 모두 하나로 묶고 '거느리다' 혹은 '다(전체)'라는 의미입니다.",
    "example_words": [
      { "word": "総合", "reading": "そうごう", "meaning": "종합", "description": "여러 가지를 다(総) 모아서 하나로 합치는(合) 것입니다." },
      { "word": "総理", "reading": "そうり", "meaning": "총리", "description": "나라의 정치나 여러 일을 다(総) 묶어 다스리는(理) 최고 책임자입니다." }
    ]
  },
  {
    "kanji": "編",
    "reading_on": "ヘン",
    "reading_kun": "あ(む)",
    "meaning": "엮을",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 의미합니다." },
      { "char": "扁", "role": "작을 편 (요소)", "desc": "문(戶)과 책(冊) 모양이 합쳐져 납작한 죽간(대나무 조각)이라는 뜻과 발음 '편/헨'을 줍니다." }
    ],
    "story": "옛날에 대나무 조각(扁)에 글을 쓰고 실(糸)로 나란히 꿰어 책을 만들었듯, 실로 옷을 '짜다' 혹은 글을 모아 책을 '엮다(편집하다)'는 뜻입니다.",
    "example_words": [
      { "word": "編む", "reading": "あむ", "meaning": "짜다, 엮다", "description": "실이나 끈을 얽어 스웨터나 바구니 등을 만드는 것입니다." },
      { "word": "編集", "reading": "へんしゅう", "meaning": "편집", "description": "자료를 모아(集) 짜임새 있게 엮어(編) 책이나 신문을 만드는 일입니다." }
    ]
  },
  {
    "kanji": "績",
    "reading_on": "セキ",
    "reading_kun": "",
    "meaning": "길쌈할 (공적)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 옷감을 뜻합니다." },
      { "char": "責", "role": "꾸짖을 책 (요소)", "desc": "맡은 일을 이룬다는 뜻과 발음 '책/세키'를 줍니다." }
    ],
    "story": "실(糸)을 잣고 옷감을 짜는 힘든 일(責)을 열심히 해낸 결과에서 유래하여, 일을 이루어 낸 훌륭한 '성과'나 '공적(업적)'을 뜻합니다.",
    "example_words": [
      { "word": "成績", "reading": "せいせき", "meaning": "성적", "description": "일이나 시험을 하여 이루어(成) 낸 결과(績)나 점수입니다." },
      { "word": "業績", "reading": "ぎょうせき", "meaning": "업적", "description": "사업이나 연구 등의 일(業)에서 이룩한 공적(績)입니다." }
    ]
  },
  {
    "kanji": "織",
    "reading_on": "ショク、シキ",
    "reading_kun": "お(る)",
    "meaning": "짤 (조직할)",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실을 뜻합니다." },
      { "char": "戠", "role": "찰흙 시 (요소)", "desc": "창(戈)으로 진흙이나 천에 무늬를 새긴다는 뜻과 발음 '식/쇼쿠'를 줍니다." }
    ],
    "story": "베틀에서 세로실과 가로실(糸)을 교차시키고 무늬(戠)를 넣어 옷감을 예쁘게 '짜다' 혹은 사람들을 묶어 단체를 '조직하다'는 의미입니다.",
    "example_words": [
      { "word": "織る", "reading": "おる", "meaning": "짜다", "description": "실을 얽어서 피륙(천)이나 카펫 따위를 만드는 것입니다." },
      { "word": "組織", "reading": "そしき", "meaning": "조직", "description": "실을 짜서(織) 천을 짜듯(組) 여러 사람이 모여 단체를 이루는 것입니다." }
    ]
  },
  {
    "kanji": "罪",
    "reading_on": "ザイ",
    "reading_kun": "つみ",
    "meaning": "허물 (죄)",
    "components": [
      { "char": "罒", "role": "그물망 머리 (부수)", "desc": "새나 물고기를 잡는 그물이나 법망을 뜻합니다." },
      { "char": "非", "role": "아닐 비 (요소)", "desc": "나쁘다, 옳지 않다는 뜻입니다." }
    ],
    "story": "옳지 않은(非) 행동을 한 사람을 그물(罒) 같은 법망으로 잡아 가둔 데서, 법이나 도덕을 어긴 '허물'이나 '죄'를 뜻합니다.",
    "example_words": [
      { "word": "罪", "reading": "つみ", "meaning": "죄", "description": "법이나 도덕을 어기고 지은 나쁜 일입니다." },
      { "word": "犯罪", "reading": "はんざい", "meaning": "범죄", "description": "법규를 어겨(犯) 벌을 받을 만한 죄(罪)를 짓는 일입니다." }
    ]
  },
  {
    "kanji": "群",
    "reading_on": "グン",
    "reading_kun": "む(れ)、む(れる)、む(らがる)",
    "meaning": "무리",
    "components": [
      { "char": "君", "role": "임금 군 (요소)", "desc": "무리 지어 산다는 뜻과 발음 '군/군'을 담당합니다." },
      { "char": "羊", "role": "양 양 (부수)", "desc": "양 떼나 동물을 뜻합니다." }
    ],
    "story": "양(羊)이나 가축들이 우두머리(君)를 따라 여러 마리가 한데 모여 떼 지어 사는 '무리'를 뜻합니다.",
    "example_words": [
      { "word": "群れ", "reading": "むれ", "meaning": "무리, 떼", "description": "짐승이나 사람 등이 여럿이 모인 동아리입니다." },
      { "word": "群衆", "reading": "ぐんしゅう", "meaning": "군중", "description": "한곳에 모여 있는 많은 사람(衆)의 무리(群)입니다." }
    ]
  },
  {
    "kanji": "義",
    "reading_on": "ギ",
    "reading_kun": "",
    "meaning": "옳을 (의리)",
    "components": [
      { "char": "羊", "role": "양 양 (부수)", "desc": "양처럼 착하고 훌륭하다는 뜻을 줍니다." },
      { "char": "我", "role": "나 아 (요소)", "desc": "나 자신의 행동이나 뜻을 의미하며 톱니 모양의 흉기(무기)의 모양에서 옳다는 뜻을 가집니다." }
    ],
    "story": "나(我)의 행동이 양(羊)처럼 착하고 바르며 흠잡을 데 없이 '옳다'거나 사람으로서 마땅히 지켜야 할 바른 도리인 '의리'를 뜻합니다.",
    "example_words": [
      { "word": "正義", "reading": "せいぎ", "meaning": "정의", "description": "바르고(正) 옳은(義) 도리입니다." },
      { "word": "義務", "reading": "ぎむ", "meaning": "의무", "description": "사람으로서 마땅히 지키고(義) 힘써야 할 일(務)입니다." }
    ]
  },
  {
    "kanji": "耕",
    "reading_on": "コウ",
    "reading_kun": "たがや(す)",
    "meaning": "밭갈",
    "components": [
      { "char": "耒", "role": "가래 뢰 (부수)", "desc": "흙을 파는 농기구인 쟁기나 괭이를 뜻합니다." },
      { "char": "井", "role": "우물 정 (요소)", "desc": "우물이나 물을 퍼올린다는 뜻과 발음 '정/코우'의 변형 역할을 합니다." }
    ],
    "story": "농기구(耒)를 사용하여 단단한 흙을 파고 뒤집어서 물(井)을 대어 농사짓기 좋게 '밭을 갈다(경작하다)'는 뜻입니다.",
    "example_words": [
      { "word": "耕す", "reading": "たがやす", "meaning": "밭을 갈다, 경작하다", "description": "논밭의 흙을 파고 일구어 농사짓기 좋게 하는 것입니다." },
      { "word": "農耕", "reading": "のうこう", "meaning": "농경", "description": "밭을 갈고(耕) 농사(農)를 짓는 일입니다." }
    ]
  },
  {
    "kanji": "職",
    "reading_on": "ショク",
    "reading_kun": "",
    "meaning": "직분 (직업)",
    "components": [
      { "char": "耳", "role": "귀 이 (부수)", "desc": "귀나 소리를 듣는다는 뜻입니다." },
      { "char": "戠", "role": "찰흙 시 (요소)", "desc": "무기(戈)를 들고 새긴다는 뜻과 발음 '식/쇼쿠'를 줍니다." }
    ],
    "story": "옛날 전투에서 귀(耳)를 밝게 하여 적의 움직임을 살피고 무기(戈가 포함된 戠)로 막아내는 중요한 임무를 맡은 데서 자신이 맡은 '직분(임무)'이나 '직업'을 뜻합니다.",
    "example_words": [
      { "word": "職業", "reading": "しょくぎょう", "meaning": "직업", "description": "생계를 유지하기 위해 맡아서(職) 하는 일(業)입니다." },
      { "word": "就職", "reading": "しゅうしょく", "meaning": "취직", "description": "어떤 직업(職)을 잡아 나아가(就) 일자리를 얻는 것입니다." }
    ]
  },
  {
    "kanji": "肥",
    "reading_on": "ヒ",
    "reading_kun": "こ(える)、こ(やす)、こ(やし)",
    "meaning": "살찔",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "고기나 몸을 뜻합니다." },
      { "char": "巴", "role": "꼬리 파 (요소)", "desc": "여기서는 크고 둥글게 늘어난다는 뜻과 발음 '파/히'를 줍니다." }
    ],
    "story": "사람이나 동물의 몸(月)에 살이 붙어 둥글고(巴) 통통하게 커진 모양에서 '살찌다' 혹은 땅이 비옥해진다는 뜻입니다.",
    "example_words": [
      { "word": "肥える", "reading": "こえる", "meaning": "살찌다, 기름지다", "description": "몸에 살이 찌거나 땅이 농사짓기 좋게 기름지게 되는 것입니다." },
      { "word": "肥料", "reading": "ひりょう", "meaning": "비료", "description": "땅을 살찌우기(肥) 위해 주는 재료(料)나 거름입니다." }
    ]
  },
  {
    "kanji": "能",
    "reading_on": "ノウ",
    "reading_kun": "",
    "meaning": "능할 (능력)",
    "components": [
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "곰의 머리 부분을 나타냅니다." },
      { "char": "月", "role": "육달월 (부수)", "desc": "곰의 튼튼한 몸통과 살을 뜻합니다." },
      { "char": "匕", "role": "비수 비 (요소)", "desc": "곰의 날카로운 발톱을 뜻합니다." }
    ],
    "story": "튼튼한 몸(月)과 날카로운 발톱(匕)을 가진 곰의 모양을 본뜬 글자로, 곰처럼 힘이 세고 무슨 일이든 '능숙하게 해내다' 혹은 '능력'이 있다는 뜻입니다.",
    "example_words": [
      { "word": "能力", "reading": "のうりょく", "meaning": "능력", "description": "일을 해낼(能) 수 있는 힘(力)입니다." },
      { "word": "可能", "reading": "かのう", "meaning": "가능", "description": "어떤 일을 할 수 있게(可) 해내는 능력(能)이 있는 것입니다." }
    ]
  },
  {
    "kanji": "興",
    "reading_on": "コウ、キョウ",
    "reading_kun": "おこ(る)、おこ(す)",
    "meaning": "일 흥 (일으킬)",
    "components": [
      { "char": "同", "role": "한가지 동 (요소)", "desc": "사람들이 다 같이 힘을 모은다는 뜻입니다." },
      { "char": "臼", "role": "절구 구 (부수)", "desc": "무거운 물건이나 들어 올리는 모습을 뜻합니다." }
    ],
    "story": "여러 사람(同)이 마주 서서 무거운 절구(臼) 따위를 한꺼번에 위로 들어 올리는 모양에서 쇠퇴하던 것이 번성하여 '일어나다', 기분이 들떠 '흥겹다'는 뜻입니다.",
    "example_words": [
      { "word": "興味", "reading": "きょうみ", "meaning": "흥미", "description": "어떤 일에 재미와 흥(興)을 느끼는 맛(味)입니다." },
      { "word": "復興", "reading": "ふっこう", "meaning": "부흥", "description": "쇠퇴했던 것이 다시(復) 일어나는(興) 것입니다." }
    ]
  },
  {
    "kanji": "舌",
    "reading_on": "ゼツ",
    "reading_kun": "した",
    "meaning": "혀",
    "components": [
      { "char": "千", "role": "일천 천 (요소)", "desc": "여기서는 입 밖으로 내민 혀끝 모양을 본뜬 것입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입을 의미합니다." }
    ],
    "story": "입(口) 밖으로 날름거리며 내민 혀(千 변형)의 모양을 본떠 맛을 느끼고 말을 하는 기관인 '혀'를 의미합니다.",
    "example_words": [
      { "word": "舌", "reading": "した", "meaning": "혀", "description": "입안에서 음식의 맛을 느끼고 소리를 내는 데 쓰는 근육입니다." },
      { "word": "舌打ち", "reading": "したうち", "meaning": "혀를 참", "description": "못마땅하여 혀(舌)를 차며(打ち) 소리를 내는 행동입니다." }
    ]
  },
  {
    "kanji": "舎",
    "reading_on": "シャ",
    "reading_kun": "",
    "meaning": "집 (여관)",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "지붕이나 덮개를 뜻합니다." },
      { "char": "干", "role": "방패 간 (요소)", "desc": "기둥이나 건물의 틀을 의미합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "창문이나 건물의 토대를 의미합니다." }
    ],
    "story": "지붕(人)과 기둥(干), 토대(口)를 갖추어 임시로 머물 수 있도록 대강 지어 놓은 '집'이나 여관, 학교 같은 건물을 뜻합니다.",
    "example_words": [
      { "word": "宿舎", "reading": "しゅくしゃ", "meaning": "숙사, 숙소", "description": "잠을 자고(宿) 묵는 집(舎)입니다." },
      { "word": "田舎", "reading": "いなか", "meaning": "시골", "description": "도심에서 벗어난 들판(田)과 집(舎)이 있는 한적한 곳입니다. (예외적인 읽기)" }
    ]
  },
  {
    "kanji": "術",
    "reading_on": "ジュツ",
    "reading_kun": "",
    "meaning": "재주 (기술)",
    "components": [
      { "char": "行", "role": "다닐 행 (부수)", "desc": "네거리를 뜻하며 길을 의미합니다." },
      { "char": "朮", "role": "차조 출 (요소)", "desc": "차조(식물)처럼 끈끈하게 달라붙는다는 뜻에서 교묘하다는 의미와 발음 '출/쥬츠'를 줍니다." }
    ],
    "story": "길(行) 한가운데(朮)에서 끈질기고 교묘하게 솜씨를 부리는 모습에서 어떤 일을 능숙하게 하는 '재주'나 '기술', '방법'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "技術", "reading": "ぎじゅつ", "meaning": "기술", "description": "사물을 다루거나 만드는 교묘한 재주(技)와 솜씨(術)입니다." },
      { "word": "手術", "reading": "しゅじゅつ", "meaning": "수술", "description": "의사가 손(手)과 의료 기구를 써서 병을 고치는 재주(術)입니다." }
    ]
  },
  {
    "kanji": "衛",
    "reading_on": "エイ",
    "reading_kun": "",
    "meaning": "지킬 (위생)",
    "components": [
      { "char": "行", "role": "다닐 행 (부수)", "desc": "길이나 사람들이 다니는 곳을 뜻합니다." },
      { "char": "韋", "role": "가죽 위 (요소)", "desc": "성 주위를 빙빙 돌며 에워싼다는 뜻과 발음 '위/에이'를 줍니다." }
    ],
    "story": "성이나 마을의 둘레길(行)을 군사들이 빙빙 돌며(韋) 적이 쳐들어오지 못하게 '지키다(방위하다)'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "衛生", "reading": "えいせい", "meaning": "위생", "description": "몸의 건강을 지키고(衛) 생명(生)을 보전하는 일입니다." },
      { "word": "防衛", "reading": "ぼうえい", "meaning": "방위", "description": "적의 침략을 막아(防) 지키는(衛) 것입니다." }
    ]
  },
  {
    "kanji": "製",
    "reading_on": "セイ",
    "reading_kun": "",
    "meaning": "지을 (만들)",
    "components": [
      { "char": "制", "role": "마를 제 (요소)", "desc": "옷감을 알맞게 마름질하여 자른다는 뜻과 발음 '제/세이'를 줍니다." },
      { "char": "衣", "role": "옷 의 (부수)", "desc": "옷이나 천을 의미합니다." }
    ],
    "story": "옷감(衣)을 치수에 맞게 칼로 자르고 마름질하여(制) 옷을 '짓다', 나아가 물건을 솜씨 좋게 '만들다(제조하다)'는 뜻입니다.",
    "example_words": [
      { "word": "製品", "reading": "せいひん", "meaning": "제품", "description": "공장에서 원료를 써서 만들어(製) 낸 물건(品)입니다." },
      { "word": "製造", "reading": "せいぞう", "meaning": "제조", "description": "재료에 가공하여 물건을 만들고(製) 짓는(造) 일입니다." }
    ]
  },
  {
    "kanji": "複",
    "reading_on": "フク",
    "reading_kun": "",
    "meaning": "겹칠 (복잡할)",
    "components": [
      { "char": "衤", "role": "옷의변 (부수)", "desc": "옷이나 천을 의미합니다." },
      { "char": "复", "role": "돌아올 복 (요소)", "desc": "왔던 길을 되돌아간다는 데서 거듭(다시)한다는 의미와 발음 '복/후쿠'를 줍니다." }
    ],
    "story": "옷(衤)을 얇게 입지 않고 거듭(复) 겹쳐 입는다는 데서 사물이 여러 개 '겹치다', 얽혀서 '복잡하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "複雑", "reading": "ふくざつ", "meaning": "복잡", "description": "일이나 사물이 겹치고(複) 뒤섞여(雑) 얽혀 있는 상태입니다." },
      { "word": "複数", "reading": "ふくすう", "meaning": "복수", "description": "두 개 이상 겹친(複) 수(数)입니다." }
    ]
  },
  {
    "kanji": "規",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "법 (규칙)",
    "components": [
      { "char": "夫", "role": "지아비 부 (요소)", "desc": "여기서는 활을 당기는 사람이나 화살의 모양을 본뜬 것입니다." },
      { "char": "見", "role": "볼 견 (부수)", "desc": "눈으로 보아 잰다는 뜻입니다." }
    ],
    "story": "컴퍼스처럼 둥글게 원을 그리는 도구(夫 변형)를 눈(見)으로 보며 정확히 기준을 잡는다는 데서, 지켜야 할 기준인 '법'이나 '규칙'을 뜻합니다.",
    "example_words": [
      { "word": "規則", "reading": "きそく", "meaning": "규칙", "description": "사람들이 다 같이 지키기로 한 법(規)과 법칙(則)입니다." },
      { "word": "規模", "reading": "きぼ", "meaning": "규모", "description": "사물이나 조직의 겉으로 나타나는 법(規)과 크기(模)입니다." }
    ]
  },
  {
    "kanji": "解",
    "reading_on": "カイ、ゲ",
    "reading_kun": "と(く)、と(ける)",
    "meaning": "풀 (해석할)",
    "components": [
      { "char": "角", "role": "뿔 각 (부수)", "desc": "소의 뿔이나 동물의 뼈를 의미합니다." },
      { "char": "刀", "role": "칼 도 (요소)", "desc": "칼로 쪼개거나 가르는 동작을 뜻합니다." },
      { "char": "牛", "role": "소 우 (요소)", "desc": "소를 의미합니다." }
    ],
    "story": "푸줏간에서 칼(刀)을 써서 소(牛)의 뿔(角)과 살을 뼈에서 떼어내어 '풀다', 혹은 엉킨 실마리를 풀어 '해석하다(이해하다)'는 뜻입니다.",
    "example_words": [
      { "word": "解く", "reading": "とく", "meaning": "풀다", "description": "묶인 끈이나 매듭을 헤치거나 어려운 문제를 알아내는 것입니다." },
      { "word": "理解", "reading": "りかい", "meaning": "이해", "description": "사물의 이치(理)를 깨달아 아는(解) 것입니다." }
    ]
  },
  {
    "kanji": "設",
    "reading_on": "セツ",
    "reading_kun": "もう(ける)",
    "meaning": "베풀 (설치할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 명령을 의미합니다." },
      { "char": "殳", "role": "갖은등글월문 (요소)", "desc": "손에 도구를 쥐고 세우거나 치는 모양입니다." }
    ],
    "story": "사람들에게 말(言)로 알리고 명령하여 손수 도구(殳)를 써서 새로운 건물이나 제도를 널리 '베풀다' 혹은 '설치하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "設ける", "reading": "もうける", "meaning": "마련하다, 베풀다", "description": "없던 것을 새로 차리거나 제도를 만드는 것입니다." },
      { "word": "設定", "reading": "せってい", "meaning": "설정", "description": "규칙이나 목표 등을 새로 베풀어(設) 정하는(定) 일입니다." }
    ]
  },
  {
    "kanji": "許",
    "reading_on": "キョ",
    "reading_kun": "ゆる(す)",
    "meaning": "허락할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "午", "role": "낮 오 (요소)", "desc": "절굿공이가 교차하는 모양에서 맞물린다는 뜻과 발음 '오/쿄'의 변형 역할을 합니다." }
    ],
    "story": "상대방의 요청에 대해 말(言)로 서로 뜻이 맞아(午) 좋다고 '허락하다(용서하다)'는 의미입니다.",
    "example_words": [
      { "word": "許す", "reading": "ゆるす", "meaning": "허락하다, 용서하다", "description": "남이 바라는 것을 들어주거나 잘못을 꾸짖지 않는 것입니다." },
      { "word": "許可", "reading": "きょか", "meaning": "허가", "description": "행동이나 요구를 좋다고(可) 허락하는(許) 것입니다." }
    ]
  },
  {
    "kanji": "証",
    "reading_on": "ショウ",
    "reading_kun": "",
    "meaning": "증명할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 서류를 뜻합니다." },
      { "char": "正", "role": "바를 정 (요소)", "desc": "거짓 없이 똑바르다는 뜻과 발음 '정/쇼우'를 줍니다." }
    ],
    "story": "말(言)이나 문서를 통해 어떤 사실이 거짓 없이 올바름(正)을 명백히 밝혀내어 '증명하다' 혹은 그 '증거'를 뜻합니다.",
    "example_words": [
      { "word": "証明", "reading": "しょうめい", "meaning": "증명", "description": "어떤 사실이 참이라는 것을 증거(証)를 들어 밝히는(明) 일입니다." },
      { "word": "保証", "reading": "ほしょう", "meaning": "보증", "description": "어떤 사물이 틀림없다고 책임지고 지켜(保) 증명하는(証) 것입니다." }
    ]
  },
  {
    "kanji": "評",
    "reading_on": "ヒョウ",
    "reading_kun": "",
    "meaning": "평가할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "平", "role": "평평할 평 (요소)", "desc": "저울이 치우치지 않고 평평하다는 뜻과 발음 '평/히ょう'를 줍니다." }
    ],
    "story": "말(言)로 사람이나 사물의 가치를 어느 한쪽으로 치우치지 않게 공평하고(平) 바르게 따져서 '평가하다'는 뜻입니다.",
    "example_words": [
      { "word": "評価", "reading": "ひょうか", "meaning": "평가", "description": "사물의 가치나 값(価)을 따져서 평하는(評) 일입니다." },
      { "word": "評判", "reading": "ひょうばん", "meaning": "평판", "description": "세상 사람들의 평가(評)와 판단(判)입니다." }
    ]
  },
  {
    "kanji": "講",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "풀 (강론할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 의미합니다." },
      { "char": "冓", "role": "짤 구 (요소)", "desc": "나무가 서로 얽혀 교차한다는 뜻과 발음 '구/코우'를 줍니다." }
    ],
    "story": "복잡하게 얽혀 있는(冓) 학문이나 이치를 말(言)로 알기 쉽게 하나하나 풀어서 '설명하다(강론하다)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "講義", "reading": "こうぎ", "meaning": "강의", "description": "어려운 뜻이나 의리(義)를 풀어서(講) 설명하는 수업입니다." },
      { "word": "休講", "reading": "きゅうこう", "meaning": "휴강", "description": "학교 등에서 하던 강의(講)를 하루 쉬는(休) 것입니다." }
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

print("Grade 5 Part 5 data appended successfully.")
