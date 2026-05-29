import json
import os

new_data = [
  {
    "kanji": "欲",
    "reading_on": "ヨク",
    "reading_kun": "ほっ(する)、ほ(しい)",
    "meaning": "하고자 할 (바랄)",
    "components": [
      { "char": "谷", "role": "골 곡 (요소)", "desc": "속이 텅 빈 계곡처럼 텅 비어 있다는 뜻과 발음 '곡/요쿠'의 변형 역할을 합니다." },
      { "char": "欠", "role": "하품 흠 (부수)", "desc": "입을 크게 벌리고 하품을 하거나 부족하여 바라는 동작을 뜻합니다." }
    ],
    "story": "텅 빈 계곡(谷)처럼 마음이 허전하여 무언가 채워지기를 입을 벌려(欠) 간절히 '바라다' 혹은 '하고자 하다'는 의미입니다.",
    "example_words": [
      { "word": "欲しい", "reading": "ほしい", "meaning": "갖고 싶다, 원하다", "description": "어떤 물건이나 상태를 바라고 탐내는 마음입니다." },
      { "word": "食欲", "reading": "しょくよく", "meaning": "식욕", "description": "음식을 먹고(食) 싶어 하는 바램(欲)입니다." }
    ]
  },
  {
    "kanji": "段",
    "reading_on": "ダン",
    "reading_kun": "",
    "meaning": "층계 (단)",
    "components": [
      { "char": "叚", "role": "빌릴 가 변형 (요소)", "desc": "언덕처럼 층이 져 있다는 뜻을 줍니다." },
      { "char": "殳", "role": "갖은등글월문 (부수)", "desc": "손에 든 도구로 내리쳐서 깎아 만든다는 뜻입니다." }
    ],
    "story": "가파른 언덕에 손수 도구(殳)를 써서 사람이 오르내리기 쉽도록 층이 지게 깎아 만든 '층계'나 일의 '단계'를 뜻합니다.",
    "example_words": [
      { "word": "階段", "reading": "かいだん", "meaning": "계단", "description": "오르내리기 위해 층(階)이 지게 만든 단(段)입니다." },
      { "word": "段階", "reading": "だんかい", "meaning": "단계", "description": "일의 차례를 따라 나아가는 층계(段)와 차례(階)입니다." }
    ]
  },
  {
    "kanji": "沿",
    "reading_on": "エン",
    "reading_kun": "そ(う)",
    "meaning": "물따라갈 (따를)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "㕣", "role": "산늪 연 (요소)", "desc": "물이 흘러내려 가는 계곡이나 늪이라는 뜻과 발음 '연/엔'을 줍니다." }
    ],
    "story": "강물(氵)이 늪이나 계곡(㕣)을 따라 굽이굽이 흘러가듯, 길이나 물가를 '따라가다' 혹은 뜻에 '따르다'는 의미입니다.",
    "example_words": [
      { "word": "沿う", "reading": "そう", "meaning": "따르다", "description": "길이나 강가 등을 끼고 곁을 따라가는 것입니다." },
      { "word": "沿岸", "reading": "えんがん", "meaning": "연안", "description": "바다나 강 따위의 물가를 따라(沿) 이어진 기슭(岸)입니다." }
    ]
  },
  {
    "kanji": "泉",
    "reading_on": "セン",
    "reading_kun": "いずみ",
    "meaning": "샘",
    "components": [
      { "char": "白", "role": "흰 백 (요소)", "desc": "여기서는 원래 작은 구멍에서 맑은 물이 솟아나는 옹달샘 모양(𡄣)의 윗부분이 변형된 것입니다." },
      { "char": "水", "role": "물 수 (부수)", "desc": "물이나 흐르는 물을 뜻합니다." }
    ],
    "story": "땅의 구멍(白 변형)에서 맑은 물(水)이 퐁퐁 솟아오르는 옹달샘을 본뜬 글자로, 물이 솟아나는 '샘'을 의미합니다.",
    "example_words": [
      { "word": "泉", "reading": "いずみ", "meaning": "샘", "description": "땅속에서 물이 솟아 나오는 곳입니다." },
      { "word": "温泉", "reading": "おんせん", "meaning": "온천", "description": "땅속에서 따뜻한(温) 물이 솟아나는 샘(泉)입니다." }
    ]
  },
  {
    "kanji": "洗",
    "reading_on": "セン",
    "reading_kun": "あら(う)",
    "meaning": "씻을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물을 뜻합니다." },
      { "char": "先", "role": "먼저 선 (요소)", "desc": "발을 앞으로 내민다는 뜻에서 맨 끝부분, 발끝이라는 의미와 발음 '선/센'을 줍니다." }
    ],
    "story": "먼저(先) 맨 끝에 있는 발이나 몸의 때를 물(氵)로 깨끗하게 '씻다' 혹은 빨래하다는 뜻을 지닙니다.",
    "example_words": [
      { "word": "洗う", "reading": "あらう", "meaning": "씻다, 빨다", "description": "물로 때나 더러운 것을 없애어 깨끗하게 하는 것입니다." },
      { "word": "洗濯", "reading": "せんたく", "meaning": "세탁", "description": "더러워진 옷 따위를 물에 씻어(洗) 빠는(濯) 일입니다." }
    ]
  },
  {
    "kanji": "派",
    "reading_on": "ハ",
    "reading_kun": "",
    "meaning": "갈래 (파)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "강물이나 물줄기를 뜻합니다." },
      { "char": "𠂢", "role": "물갈래 파 (요소)", "desc": "물이 갈라져 흐른다는 뜻과 발음 '파/하'를 줍니다." }
    ],
    "story": "큰 강물(氵)이 이리저리 여러 갈래로 갈라져(𠂢) 흐르는 물줄기, 즉 나뉘어 갈라진 '갈래'나 뜻이 맞는 사람들의 무리인 '파'를 의미합니다.",
    "example_words": [
      { "word": "立派", "reading": "りっぱ", "meaning": "훌륭함, 멋짐", "description": "갈래(派)가 우뚝 서(立) 있을 정도로 눈에 띄게 훌륭한 모양입니다." },
      { "word": "派手", "reading": "はで", "meaning": "화려함", "description": "모습이나 차림새가 눈에 띄게 튀는(派) 수법(手)입니다." }
    ]
  },
  {
    "kanji": "済",
    "reading_on": "サイ、ザイ",
    "reading_kun": "す(む)、す(ます)",
    "meaning": "건널 (구제할)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "斉", "role": "가지런할 제 (요소)", "desc": "나란히 가지런하다는 뜻과 발음 '제/사이'를 줍니다." }
    ],
    "story": "사람들이 강물(氵)을 나란히(斉) 건너가서 위험에서 무사히 '건너다', 혹은 무사히 일을 '마치다(끝나다)'나 백성을 '구제하다'는 뜻입니다.",
    "example_words": [
      { "word": "済む", "reading": "すむ", "meaning": "끝나다, 해결되다", "description": "일이나 문제가 무사히 마무리되어 끝나는 것입니다." },
      { "word": "経済", "reading": "けいざい", "meaning": "경제", "description": "나라를 다스려(経) 백성을 구제하는(済) 재화에 관한 활동입니다." }
    ]
  },
  {
    "kanji": "源",
    "reading_on": "ゲン",
    "reading_kun": "みなもと",
    "meaning": "근원 (수원)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 뜻합니다." },
      { "char": "原", "role": "근원 원 (요소)", "desc": "언덕 아래 옹달샘이라는 뜻과 발음 '원/겐'을 줍니다." }
    ],
    "story": "산언덕 바위틈(原)에서 솟아나 강물(氵)이 처음 시작되는 '수원(물이 시작되는 곳)'이나 사물의 첫 바탕이 되는 '근원'을 뜻합니다.",
    "example_words": [
      { "word": "源", "reading": "みなもと", "meaning": "근원, 수원", "description": "물이 솟아 나오기 시작하는 곳이나 사물이 비롯되는 처음입니다." },
      { "word": "資源", "reading": "しげん", "meaning": "자원", "description": "자본(資)의 바탕과 바탕(源)이 되는 재료입니다." }
    ]
  },
  {
    "kanji": "潮",
    "reading_on": "チョウ",
    "reading_kun": "しお",
    "meaning": "조수 (밀물)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "바닷물이나 물을 뜻합니다." },
      { "char": "朝", "role": "아침 조 (요소)", "desc": "아침이라는 뜻과 발음 '조/초우'를 줍니다." }
    ],
    "story": "아침(朝)에 바닷물(氵)이 밀려들고 밀려 나가는 흐름인 '조수(밀물과 썰물)'나 바닷물을 뜻합니다.",
    "example_words": [
      { "word": "潮", "reading": "しお", "meaning": "조수, 썰물과 밀물", "description": "달과 태양의 힘으로 바닷물이 들어오고 나가는 현상이나 그 물입니다." },
      { "word": "満潮", "reading": "まんちょう", "meaning": "만조, 밀물", "description": "바닷물(潮)이 해안으로 가득 차(満) 들어온 때입니다." }
    ]
  },
  {
    "kanji": "激",
    "reading_on": "ゲキ",
    "reading_kun": "はげ(しい)",
    "meaning": "격할 (부딪칠)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 물결을 의미합니다." },
      { "char": "敫", "role": "노래할 교 (요소)", "desc": "빛이 밝게 퍼져 나간다는 뜻에서 사방으로 튄다는 의미와 발음 '교/게키'의 변형 역할을 합니다." }
    ],
    "story": "강물이나 파도(氵)가 바위에 세게 부딪쳐 물보라가 사방으로 희게 튀어 오르는(敫) 모양에서 물살이나 세력이 '격하다(심하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "激しい", "reading": "はげしい", "meaning": "격렬하다, 심하다", "description": "움직임이나 성질이 사납고 정도가 매우 센 것입니다." },
      { "word": "感激", "reading": "かんげき", "meaning": "감격", "description": "마음 깊이 느끼어(感) 격렬하게(激) 마음이 흔들리는 일입니다." }
    ]
  },
  {
    "kanji": "灰",
    "reading_on": "カイ",
    "reading_kun": "はい",
    "meaning": "재",
    "components": [
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "여기서는 손(𠂇의 변형)의 모양을 나타내어 물건을 만진다는 뜻입니다." },
      { "char": "火", "role": "불 화 (부수)", "desc": "불이나 타다 남은 것을 뜻합니다." }
    ],
    "story": "불(火)이 다 타고 난 뒤에 남은 것을 손(厂 변형)으로 만져 보아도 뜨겁지 않은 가루, 즉 '재'를 뜻합니다.",
    "example_words": [
      { "word": "灰", "reading": "はい", "meaning": "재", "description": "불에 다 타고 남은 가루입니다." },
      { "word": "灰皿", "reading": "はいざら", "meaning": "재떨이", "description": "담뱃재(灰)를 떨어 모으는 작은 접시(皿)입니다." }
    ]
  },
  {
    "kanji": "熟",
    "reading_on": "ジュク",
    "reading_kun": "う(れる)",
    "meaning": "익을 (숙련될)",
    "components": [
      { "char": "孰", "role": "누구 숙 (요소)", "desc": "아이나 제물을 바친다는 뜻과 발음 '숙/쥬쿠'를 줍니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불을 때어 익히는 모양을 뜻합니다." }
    ],
    "story": "제물로 쓸 고기를 불(灬) 위에 올려놓고 부드럽게 푹 삶아 '익히다' 혹은 과일이 '익다', 나아가 기술이 능숙하게 '숙련되다'는 의미입니다.",
    "example_words": [
      { "word": "熟れる", "reading": "うれる", "meaning": "익다, 성숙하다", "description": "과일 따위가 알맞게 여물어 먹기 좋게 된 상태입니다." },
      { "word": "未熟", "reading": "みじゅく", "meaning": "미숙", "description": "아직 충분히 익지(熟) 않음(未), 또는 솜씨가 서투른 상태입니다." }
    ]
  },
  {
    "kanji": "片",
    "reading_on": "ヘン",
    "reading_kun": "かた",
    "meaning": "조각 (한쪽)",
    "components": [
      { "char": "片", "role": "조각 편 (부수)", "desc": "통나무(木)를 세로로 반쪽으로 쪼갠 것 중 오른쪽 절반의 모양을 본뜬 글자입니다." }
    ],
    "story": "통나무를 도끼로 세로로 쫙 갈라놓은 오른쪽 절반의 모양에서, 물건의 쪼개진 '조각'이나 쌍을 이루는 것 중 '한쪽'을 뜻합니다.",
    "example_words": [
      { "word": "片方", "reading": "かたほう", "meaning": "한쪽", "description": "짝을 이룬 것 가운데 어느 하나이거나 한 방향입니다." },
      { "word": "破片", "reading": "はへん", "meaning": "파편", "description": "깨어져(破) 떨어져 나온 조각(片)입니다." }
    ]
  },
  {
    "kanji": "班",
    "reading_on": "ハン",
    "reading_kun": "",
    "meaning": "나눌 (조)",
    "components": [
      { "char": "王", "role": "구슬 옥 (부수)", "desc": "옥이나 구슬을 뜻합니다. (원래 玉 자)" },
      { "char": "刂", "role": "선칼도방 (요소)", "desc": "칼로 자른다는 뜻입니다." }
    ],
    "story": "하나의 큰 옥(王)을 칼(刂)로 똑같이 반으로 쪼개어(王 刂 王) 나눈다는 데서, 사람들을 똑같이 나눈 작은 무리인 '반(조)'이나 '나누다'는 뜻입니다.",
    "example_words": [
      { "word": "班", "reading": "はん", "meaning": "반, 조", "description": "학교나 군대 등에서 무리를 작게 나눈 집단입니다." },
      { "word": "班長", "reading": "はんちょう", "meaning": "반장", "description": "작은 무리(班)의 우두머리(長)나 대표입니다." }
    ]
  },
  {
    "kanji": "異",
    "reading_on": "イ",
    "reading_kun": "こと(なる)",
    "meaning": "다를 (기이할)",
    "components": [
      { "char": "田", "role": "밭 전 (부수)", "desc": "여기서는 귀신이나 탈을 쓴 사람의 머리 모양을 나타냅니다." },
      { "char": "共", "role": "함께 공 (요소)", "desc": "두 손으로 무언가를 받쳐 들고 있는 모양입니다." }
    ],
    "story": "탈(田 변형)을 쓴 무당이 두 손(共)을 들고 보통 사람들과는 다른 기이한 행동을 한다는 데서, 보통과 '다르다' 혹은 '기이하다'는 의미입니다.",
    "example_words": [
      { "word": "異なる", "reading": "ことなる", "meaning": "다르다", "description": "서로 같지 않거나 차이가 나는 것입니다." },
      { "word": "異常", "reading": "いじょう", "meaning": "이상", "description": "보통이나 정상(常)적인 상태와 다름(異)입니다." }
    ]
  },
  {
    "kanji": "疑",
    "reading_on": "ギ",
    "reading_kun": "うたが(う)",
    "meaning": "의심할",
    "components": [
      { "char": "匕", "role": "비수 비 (요소)", "desc": "사람이 멈춰서 뒤를 돌아보는 모양입니다." },
      { "char": "矢", "role": "화살 시 (요소)", "desc": "화살이나 길을 뜻합니다." },
      { "char": "疋", "role": "발 소 (부수)", "desc": "발걸음을 내딛는 모양을 뜻합니다." }
    ],
    "story": "길(矢)을 가던 사람이 어딘가 이상하여 발걸음(疋)을 멈추고 고개를 돌려(匕) 이리저리 살피며 맞는지 '의심하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "疑う", "reading": "うたがう", "meaning": "의심하다", "description": "사실인지 아닌지 못 믿어 미심쩍게 생각하는 것입니다." },
      { "word": "疑問", "reading": "ぎもん", "meaning": "의문", "description": "의심(疑)스럽게 여겨 묻거나(問) 생각하는 점입니다." }
    ]
  },
  {
    "kanji": "痛",
    "reading_on": "ツウ",
    "reading_kun": "いた(い)、いた(む)、いた(める)",
    "meaning": "아플",
    "components": [
      { "char": "疒", "role": "병질엄 (부수)", "desc": "병상에 누워 있는 모양으로 질병을 뜻합니다." },
      { "char": "甬", "role": "길 용 (요소)", "desc": "종처럼 속이 비었다는 뜻에서 발음 '용/츠우'의 변형을 줍니다." }
    ],
    "story": "병(疒)이 들어 뼛속이나 속이 뚫린 듯 욱신거리며 아픔이 파고들어 '아프다' 혹은 '고통'을 뜻합니다.",
    "example_words": [
      { "word": "痛い", "reading": "いたい", "meaning": "아프다", "description": "몸에 상처가 나거나 병이 들어 쓰리고 괴로운 느낌입니다." },
      { "word": "苦痛", "reading": "くつう", "meaning": "고통", "description": "몸이나 마음이 괴롭고(苦) 아픈(痛) 일입니다." }
    ]
  },
  {
    "kanji": "皇",
    "reading_on": "コウ、オウ",
    "reading_kun": "",
    "meaning": "임금 (황제)",
    "components": [
      { "char": "白", "role": "흰 백 (부수)", "desc": "여기서는 햇빛이 눈부시게 빛나는 왕관의 모양(自의 변형)을 뜻합니다." },
      { "char": "王", "role": "임금 왕 (요소)", "desc": "왕이나 최고 권력자를 의미합니다." }
    ],
    "story": "햇빛처럼 빛나는 훌륭한 왕관(白 변형)을 쓴 임금(王), 즉 온 세상을 다스리는 으뜸가는 '황제'나 '임금'을 뜻합니다.",
    "example_words": [
      { "word": "天皇", "reading": "てんのう", "meaning": "천황", "description": "일본에서 임금(皇)을 높여 부르는 칭호입니다." },
      { "word": "皇帝", "reading": "こうてい", "meaning": "황제", "description": "제국을 다스리는 최고 군주(皇, 帝)입니다." }
    ]
  },
  {
    "kanji": "盛",
    "reading_on": "セイ、ジョウ",
    "reading_kun": "も(る)、さか(ん)",
    "meaning": "성할 (담을)",
    "components": [
      { "char": "成", "role": "이룰 성 (요소)", "desc": "물건을 쌓아 올린다는 뜻과 발음 '성/세이'를 줍니다." },
      { "char": "皿", "role": "그릇 명 (부수)", "desc": "음식을 담는 그릇을 뜻합니다." }
    ],
    "story": "그릇(皿) 위에 음식을 높이 수북하게 쌓아(成) 넘칠 듯이 '담다', 그득히 쌓인 모양에서 기운이 가득 차고 '성하다(번성하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "盛ん", "reading": "さかん", "meaning": "번성하다, 활발하다", "description": "기세나 상태가 매우 활기차고 성대한 모양입니다." },
      { "word": "盛る", "reading": "もる", "meaning": "담다, 쌓아 올리다", "description": "그릇에 음식 따위를 수북하게 담는 것입니다." }
    ]
  },
  {
    "kanji": "盟",
    "reading_on": "メイ",
    "reading_kun": "",
    "meaning": "맹세할",
    "components": [
      { "char": "明", "role": "밝을 명 (요소)", "desc": "신 앞에서 밝게 다짐한다는 뜻과 발음 '명/메이'를 줍니다." },
      { "char": "皿", "role": "그릇 명 (부수)", "desc": "제사에 쓰는 피나 물을 담은 그릇을 뜻합니다." }
    ],
    "story": "옛날에 서로 굳게 약속할 때 그릇(皿)에 짐승의 피를 담아 신 앞에서 떳떳하고 밝게(明) 맹세하며 마신 데서 '맹세하다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "同盟", "reading": "どうめい", "meaning": "동맹", "description": "개인이나 나라가 뜻을 같이(同)하여 서로 굳게 약속하고 맹세하는(盟) 것입니다." },
      { "word": "連盟", "reading": "れんめい", "meaning": "연맹", "description": "여러 단체가 서로 이어져(連) 뜻을 맹세하고(盟) 뭉친 조직입니다." }
    ]
  },
  {
    "kanji": "看",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "볼 (간호할)",
    "components": [
      { "char": "手", "role": "손 수 (요소)", "desc": "손을 나타냅니다. (맨 위의 龵 모양)" },
      { "char": "目", "role": "눈 목 (부수)", "desc": "눈으로 보는 동작을 뜻합니다." }
    ],
    "story": "손(手 변형)을 이마나 눈썹 위에 얹어 햇빛을 가리고 눈(目)으로 먼 곳을 뚫어지게 '바라보다', 혹은 환자를 지켜보며 '간호하다'는 뜻입니다.",
    "example_words": [
      { "word": "看板", "reading": "かんばん", "meaning": "간판", "description": "사람들이 잘 보도록(看) 널빤지(板) 등에 글씨를 써서 걸어 놓은 표지입니다." },
      { "word": "看護", "reading": "かんご", "meaning": "간호", "description": "다친 사람이나 환자를 곁에서 보살피며(看) 지켜(護) 주는 일입니다." }
    ]
  },
  {
    "kanji": "砂",
    "reading_on": "サ、シャ",
    "reading_kun": "すな",
    "meaning": "모래",
    "components": [
      { "char": "石", "role": "돌 석 (부수)", "desc": "돌이나 바위를 뜻합니다." },
      { "char": "少", "role": "적을 소 (요소)", "desc": "크기가 작거나 적다는 뜻과 발음 '소/사'의 변형 역할을 합니다." }
    ],
    "story": "바위나 돌(石)이 부서져서 아주 작아진(少) 알갱이들, 즉 '모래'를 뜻합니다.",
    "example_words": [
      { "word": "砂", "reading": "すな", "meaning": "모래", "description": "바위나 돌이 잘게 부서져서 된 작은 알갱이들입니다." },
      { "word": "砂糖", "reading": "さとう", "meaning": "설탕", "description": "모래(砂)처럼 하얗고 고운 가루 모양의 단 엿(糖)입니다." }
    ]
  },
  {
    "kanji": "磁",
    "reading_on": "ジ",
    "reading_kun": "",
    "meaning": "자석 (자기)",
    "components": [
      { "char": "石", "role": "돌 석 (부수)", "desc": "돌이나 광물을 뜻합니다." },
      { "char": "慈", "role": "사랑할 자 (요소)", "desc": "끌어당기는 애정이라는 뜻과 발음 '자/지'를 줍니다. (위쪽 兹 모양)" }
    ],
    "story": "마치 부모가 자식을 사랑하여(慈) 끌어안듯, 쇠붙이를 끌어당기는 성질을 가진 신기한 돌(石)인 '자석'이나 '자기'를 의미합니다.",
    "example_words": [
      { "word": "磁石", "reading": "じしゃく", "meaning": "자석", "description": "쇠붙이를 끌어당기는 성질(磁)을 가진 돌(石)이나 물체입니다." },
      { "word": "磁気", "reading": "じき", "meaning": "자기", "description": "자석(磁)이 쇠붙이를 당기는 기운(気)이나 성질입니다." }
    ]
  },
  {
    "kanji": "私",
    "reading_on": "シ",
    "reading_kun": "わたし、わたくし",
    "meaning": "나 (사사로울)",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 벼를 뜻합니다." },
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "팔을 굽혀 자기 쪽으로 끌어당긴다는 뜻에서 사사롭다는 의미를 줍니다." }
    ],
    "story": "추수한 곡식(禾)을 자기 혼자 몰래 자기 쪽으로 끌어당겨(ム) 차지한다는 데서, 공평하지 않고 '사사롭다(개인적이다)' 혹은 '나'를 뜻합니다.",
    "example_words": [
      { "word": "私", "reading": "わたし", "meaning": "나", "description": "말하는 사람이 자기 자신을 일컫는 말입니다." },
      { "word": "私立", "reading": "しりつ", "meaning": "사립", "description": "개인이나 민간(私)에서 돈을 내어 학교 등을 세움(立)입니다." }
    ]
  },
  {
    "kanji": "秘",
    "reading_on": "ヒ",
    "reading_kun": "ひ(める)",
    "meaning": "숨길 (비밀)",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 귀한 것을 뜻합니다." },
      { "char": "必", "role": "반드시 필 (요소)", "desc": "가려진다는 뜻과 발음 '필/히'의 변형 역할을 합니다." }
    ],
    "story": "귀한 곡식(禾)을 창고 속에 보이지 않게 가려(必) 둔다는 데서, 남이 모르게 덮어 감추거나 '숨기다' 혹은 '비밀'을 뜻합니다.",
    "example_words": [
      { "word": "秘密", "reading": "ひみつ", "meaning": "비밀", "description": "남에게 알려지지 않게 숨기고(秘) 가리는(密) 사실입니다." },
      { "word": "秘める", "reading": "ひめる", "meaning": "숨기다, 간직하다", "description": "마음속 깊이 간직하여 밖으로 드러내지 않는 것입니다." }
    ]
  },
  {
    "kanji": "穀",
    "reading_on": "コク",
    "reading_kun": "",
    "meaning": "곡식",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "벼나 곡식을 뜻합니다." },
      { "char": "殻", "role": "껍질 각 (요소)", "desc": "단단한 껍데기라는 뜻과 발음 '각/코쿠'의 변형 역할을 합니다." }
    ],
    "story": "벼(禾)처럼 단단한 껍질(殻)에 알맹이가 싸여 있는 식물의 열매, 즉 사람이 먹는 여러 가지 '곡식(곡물)'을 통틀어 이르는 말입니다.",
    "example_words": [
      { "word": "穀物", "reading": "こくもつ", "meaning": "곡물", "description": "사람이 주식으로 먹는 쌀, 보리 등의 곡식(穀)입니다." },
      { "word": "米穀", "reading": "べいこく", "meaning": "미곡", "description": "쌀(米)과 잡다한 곡식(穀)을 함께 부르는 말입니다." }
    ]
  },
  {
    "kanji": "穴",
    "reading_on": "ケツ",
    "reading_kun": "あな",
    "meaning": "구멍",
    "components": [
      { "char": "穴", "role": "구멍 혈 (부수)", "desc": "지붕(宀) 아래에 양쪽으로 흙을 파내어 뚫린(八) 동굴의 모양입니다." }
    ],
    "story": "산이나 땅에 흙을 양쪽으로 파내어(八) 사람이 들어가 살 수 있도록 둥글게 지붕(宀)처럼 파인 동굴, 즉 움푹 파인 '구멍'을 뜻합니다.",
    "example_words": [
      { "word": "穴", "reading": "あな", "meaning": "구멍", "description": "땅이나 물건에 움푹 파이거나 뚫린 곳입니다." },
      { "word": "落とし穴", "reading": "おとしあな", "meaning": "함정", "description": "짐승이나 사람이 떨어지도록(落とし) 파 놓은 구멍(穴)입니다." }
    ]
  },
  {
    "kanji": "窓",
    "reading_on": "ソウ",
    "reading_kun": "まど",
    "meaning": "창문",
    "components": [
      { "char": "穴", "role": "구멍 혈 (부수)", "desc": "벽에 뚫린 구멍을 뜻합니다." },
      { "char": "厶", "role": "마늘 모 (요소)", "desc": "구멍 틈을 가리킵니다. (가운데 부분)" },
      { "char": "心", "role": "마음 심 (요소)", "desc": "원래 연기가 빠져나가는 통로라는 의미가 변형된 것입니다." }
    ],
    "story": "집의 벽이나 지붕에 구멍(穴)을 내어 바람이 통하고 연기가 빠져나가게 만든 틈, 즉 밖을 내다볼 수 있는 '창문'을 의미합니다.",
    "example_words": [
      { "word": "窓", "reading": "まど", "meaning": "창문", "description": "건물의 벽이나 지붕에 햇빛이나 공기가 들어오도록 뚫어 놓은 문입니다." },
      { "word": "同窓会", "reading": "どうそうかい", "meaning": "동창회", "description": "같은(同) 학교의 창문(窓) 아래서 배운 졸업생들이 모이는(会) 모임입니다." }
    ]
  },
  {
    "kanji": "筋",
    "reading_on": "キン",
    "reading_kun": "すじ",
    "meaning": "힘줄 (줄거리)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무처럼 뼈대가 되는 가느다란 줄기를 뜻합니다." },
      { "char": "肋", "role": "갈비대 륵 (요소)", "desc": "몸(月)의 갈비뼈 근육에 힘(力)을 쓴다는 뜻입니다." }
    ],
    "story": "몸(月)에서 힘(力)을 낼 때 겉으로 드러나는 대나무 핏대(竹)처럼 가느다란 가닥, 즉 몸의 '힘줄(근육)'이나 이야기의 '줄거리'를 의미합니다.",
    "example_words": [
      { "word": "筋肉", "reading": "きんにく", "meaning": "근육", "description": "몸의 힘줄(筋)과 살(肉)입니다." },
      { "word": "筋", "reading": "すじ", "meaning": "줄거리, 힘줄", "description": "몸의 힘줄이나, 일의 앞뒤가 이어지는 줄거리입니다." }
    ]
  },
  {
    "kanji": "策",
    "reading_on": "サク",
    "reading_kun": "",
    "meaning": "꾀 (채찍)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무로 만든 죽간(글을 적는 패)이나 채찍을 뜻합니다." },
      { "char": "朿", "role": "가시 자 (요소)", "desc": "가시가 뾰족하다는 뜻에서 찌른다는 의미와 발음 '자/사쿠'의 변형 역할을 합니다." }
    ],
    "story": "대나무(竹) 조각에 뾰족한 가시(朿)로 글이나 작전을 기록했다는 데서, 일을 이루기 위한 좋은 '꾀(계책)'나 말의 엉덩이를 때리는 '채찍'을 뜻합니다.",
    "example_words": [
      { "word": "対策", "reading": "たいさく", "meaning": "대책", "description": "어떤 상황에 대처(対)하여 세운 꾀(策)나 방법입니다." },
      { "word": "政策", "reading": "せいさく", "meaning": "정책", "description": "정치(政)적인 목적을 이루기 위해 세운 방법과 꾀(策)입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade6.json'
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

print("Grade 6 Part 4 data appended successfully.")
