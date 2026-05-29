import json
import os

new_data = [
  {
    "kanji": "代",
    "reading_on": "ダイ、タイ",
    "reading_kun": "か(わる)、か(える)",
    "meaning": "대신할 / 시대",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "弋", "role": "주살 익 (요소)", "desc": "말뚝이나 푯말을 의미하며 여기서는 자리를 이어받는다는 뜻과 발음 '대/다이'를 줍니다." }
    ],
    "story": "한 사람(亻)이 물러나고 다른 사람이 말뚝(弋)처럼 굳게 그 자리를 이어받아 '대신하다' 혹은 이어지는 '시대'를 뜻합니다.",
    "example_words": [
      { "word": "代わる", "reading": "かわる", "meaning": "대신하다", "description": "원래 있던 것과 자리를 바꾸거나 대신하는 것입니다." },
      { "word": "時代", "reading": "じだい", "meaning": "시대", "description": "시간(時)이 지나며 이어지는(代) 세월의 구분입니다." }
    ]
  },
  {
    "kanji": "第",
    "reading_on": "ダイ",
    "reading_kun": "",
    "meaning": "차례",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 엮어 만든 옛날의 책(죽간)을 의미합니다." },
      { "char": "弟", "role": "아우 제 (요소)", "desc": "가죽끈으로 순서대로 엮는다는 뜻과 발음 '제/다이'를 줍니다." }
    ],
    "story": "대나무(竹) 조각을 가죽끈(弟)으로 차례차례 엮어 책을 만들듯, 순서나 '차례'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "第一", "reading": "だいいち", "meaning": "제일, 첫째", "description": "가장 첫 번째(一)가 되는 차례(第)입니다." },
      { "word": "次第", "reading": "しだい", "meaning": "순서, 차례", "description": "다음(次)으로 이어지는 차례(第)입니다." }
    ]
  },
  {
    "kanji": "題",
    "reading_on": "ダイ",
    "reading_kun": "",
    "meaning": "제목",
    "components": [
      { "char": "是", "role": "옳을 시 (요소)", "desc": "이것, 옳다는 뜻이며 여기서는 발음 '시/다이'를 담당합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "사람의 머리나 얼굴, 맨 윗부분을 뜻합니다." }
    ],
    "story": "책이나 글의 맨 앞머리(頁)에 쓰여 이 글이 이것(是)이라고 밝히는 '제목'이나 '주제'를 의미합니다.",
    "example_words": [
      { "word": "問題", "reading": "もんだい", "meaning": "문제", "description": "묻는(問) 제목(題)이나 해결해야 할 일입니다." },
      { "word": "話題", "reading": "わだい", "meaning": "화제", "description": "이야기(話)의 제목(題)이나 이야깃거리입니다." }
    ]
  },
  {
    "kanji": "炭",
    "reading_on": "タン",
    "reading_kun": "すみ",
    "meaning": "숯",
    "components": [
      { "char": "山", "role": "뫼 산 (요소)", "desc": "산이나 언덕을 뜻합니다." },
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "산비탈이나 기슭입니다." },
      { "char": "火", "role": "불 화 (부수)", "desc": "불이나 타는 것을 뜻합니다." }
    ],
    "story": "산비탈(山, 厂)에서 나무를 베어 불(火)에 구워 만든 까만 '숯'을 의미합니다.",
    "example_words": [
      { "word": "石炭", "reading": "せきたん", "meaning": "석탄", "description": "돌(石)처럼 단단한 숯(炭)입니다." },
      { "word": "炭", "reading": "すみ", "meaning": "숯", "description": "나무를 구워 만든 검은 연료입니다." }
    ]
  },
  {
    "kanji": "短",
    "reading_on": "タン",
    "reading_kun": "みじか(い)",
    "meaning": "짧을",
    "components": [
      { "char": "矢", "role": "화살 시 (부수)", "desc": "화살이나 길이를 재는 기준을 뜻합니다." },
      { "char": "豆", "role": "콩 두 (요소)", "desc": "제기(그릇) 혹은 작고 둥글다는 뜻을 줍니다." }
    ],
    "story": "화살(矢)처럼 곧고 작으며 콩(豆)처럼 길이가 뭉툭하고 '짧다'는 뜻입니다.",
    "example_words": [
      { "word": "短い", "reading": "みじかい", "meaning": "짧다", "description": "길이나 시간이 길지 않은 상태입니다." },
      { "word": "短所", "reading": "たんしょ", "meaning": "단점", "description": "짧고(短) 모자란 점이나 곳(所)입니다." }
    ]
  },
  {
    "kanji": "談",
    "reading_on": "ダン",
    "reading_kun": "",
    "meaning": "말씀 (이야기)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하는 것을 뜻합니다." },
      { "char": "炎", "role": "불꽃 염 (요소)", "desc": "불꽃이 타오르듯 열정적이라는 뜻과 발음 '담/단'을 담당합니다." }
    ],
    "story": "사람들이 모여 불꽃(炎)이 활활 타오르듯 열을 띠고 '이야기'를 나누는 모습입니다.",
    "example_words": [
      { "word": "相談", "reading": "そうだん", "meaning": "상담", "description": "서로(相) 마주 대하여 이야기(談)를 나누는 것입니다." },
      { "word": "対談", "reading": "たいだん", "meaning": "대담", "description": "마주(対) 대하고 이야기(談)하는 일입니다." }
    ]
  },
  {
    "kanji": "着",
    "reading_on": "チャク、ジャク",
    "reading_kun": "き(る)、き(せる)、つ(く)",
    "meaning": "입을 / 닿을",
    "components": [
      { "char": "羊", "role": "양 양 (요소)", "desc": "양털로 짠 따뜻한 옷이나 덮개를 뜻합니다." },
      { "char": "目", "role": "눈 목 (부수)", "desc": "원래 옷을 몸에 붙이는 모양이 간략화된 것입니다." }
    ],
    "story": "몸에 양털(羊) 옷을 '입다' 혹은 물건이 목표한 곳에 '닿다(도착하다)'는 두 가지 큰 뜻을 가집니다.",
    "example_words": [
      { "word": "着る", "reading": "きる", "meaning": "입다", "description": "옷을 몸에 걸치는 것입니다." },
      { "word": "到着", "reading": "とうちゃく", "meaning": "도착", "description": "목적지에 이르러(到) 닿는(着) 것입니다." }
    ]
  },
  {
    "kanji": "注",
    "reading_on": "チュウ",
    "reading_kun": "そそ(ぐ)",
    "meaning": "부을 (물 댈)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "主", "role": "주인 주 (요소)", "desc": "한곳에 머무르다, 집중하다는 뜻과 발음 '주/츄'를 담당합니다." }
    ],
    "story": "물(氵)을 한곳(主)에 집중적으로 흘려보내 '붓다' 혹은 마음을 한곳에 '기울이다'라는 뜻입니다.",
    "example_words": [
      { "word": "注意", "reading": "ちゅうい", "meaning": "주의", "description": "어떤 곳에 뜻(意)을 집중하여 붓는(注) 것입니다." },
      { "word": "注文", "reading": "ちゅうもん", "meaning": "주문", "description": "조건을 달아(注) 글(文)로 요구하는 일입니다." }
    ]
  },
  {
    "kanji": "柱",
    "reading_on": "チュウ",
    "reading_kun": "はしら",
    "meaning": "기둥",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "主", "role": "주인 주 (요소)", "desc": "가운데 버티고 선 주인이란 뜻과 발음 '주/츄'를 줍니다." }
    ],
    "story": "집 한가운데에서 주인(主)처럼 든든하게 버티고 있는 나무(木)인 '기둥'을 뜻합니다.",
    "example_words": [
      { "word": "柱", "reading": "はしら", "meaning": "기둥", "description": "건물을 받치는 긴 나무나 돌 기둥입니다." },
      { "word": "大黒柱", "reading": "だいこくばしら", "meaning": "대들보, 기둥", "description": "집이나 조직을 지탱하는 가장 큰(大) 중심 기둥(柱)입니다." }
    ]
  },
  {
    "kanji": "帳",
    "reading_on": "チョウ",
    "reading_kun": "",
    "meaning": "휘장 / 장부",
    "components": [
      { "char": "巾", "role": "수건 건 (부수)", "desc": "헝겊이나 천을 의미합니다." },
      { "char": "長", "role": "길 장 (요소)", "desc": "길다는 뜻과 발음 '장/쵸우'를 담당합니다." }
    ],
    "story": "방을 가리기 위해 길게(長) 늘어뜨린 천(巾)인 '휘장'을 뜻하며, 나중에는 종이를 엮어 만든 기록책인 '장부'나 '공책'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "手帳", "reading": "てちょう", "meaning": "수첩", "description": "손(手)에 들고 다니는 작은 기록책(帳)입니다." },
      { "word": "通帳", "reading": "つうちょう", "meaning": "통장", "description": "은행에 돈을 넣고 빼는 내역이 통(通)하는 장부(帳)입니다." }
    ]
  },
  {
    "kanji": "調",
    "reading_on": "チョウ",
    "reading_kun": "しら(べる)、ととの(う)",
    "meaning": "고를 / 조사할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "周", "role": "두루 주 (요소)", "desc": "구석구석 두루두루 미친다는 뜻과 발음 '주/쵸우'를 줍니다." }
    ],
    "story": "말(言)로 두루두루(周) 물어보며 사정을 '조사하다' 혹은 의견을 맞추어 고르게 '조절하다'는 뜻입니다.",
    "example_words": [
      { "word": "調べる", "reading": "しらべる", "meaning": "조사하다, 알아보다", "description": "자세히 찾아서 알아보는 일입니다." },
      { "word": "調査", "reading": "ちょうさ", "meaning": "조사", "description": "두루 알아보고(調) 사실을 검사하는(査) 것입니다." }
    ]
  },
  {
    "kanji": "追",
    "reading_on": "ツイ",
    "reading_kun": "お(う)",
    "meaning": "쫓을",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "𠂤", "role": "언덕 퇴 (요소)", "desc": "여기서는 발 뒤꿈치(엉덩이) 모양으로 뒤를 뜻하며 발음 '추/츠이'를 줍니다." }
    ],
    "story": "앞서가는 사람의 뒤(𠂤)를 바짝 따라가며(辶) 붙잡으려고 '쫓다' 혹은 '추격하다'는 의미입니다.",
    "example_words": [
      { "word": "追う", "reading": "おう", "meaning": "쫓다", "description": "앞서가는 대상을 따라가는 것입니다." },
      { "word": "追加", "reading": "ついか", "meaning": "추가", "description": "뒤쫓아(追) 가서 무언가를 더 더하는(加) 것입니다." }
    ]
  },
  {
    "kanji": "笛",
    "reading_on": "テキ",
    "reading_kun": "ふえ",
    "meaning": "피리",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 뜻합니다." },
      { "char": "由", "role": "말미암을 유 (요소)", "desc": "어딘가를 거쳐 나온다는 뜻과 발음 '유/테키'를 줍니다." }
    ],
    "story": "대나무(竹) 통에 구멍을 뚫고 입김을 불어 그 안을 거쳐(由) 소리가 나게 만든 악기인 '피리'를 뜻합니다.",
    "example_words": [
      { "word": "笛", "reading": "ふえ", "meaning": "피리", "description": "입으로 불어 소리를 내는 관악기입니다." },
      { "word": "警笛", "reading": "けいてき", "meaning": "경적", "description": "위험을 경고하기(警) 위해 울리는 피리(笛) 소리나 호각입니다." }
    ]
  },
  {
    "kanji": "鉄",
    "reading_on": "テツ",
    "reading_kun": "",
    "meaning": "쇠 (철)",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "금속을 의미합니다." },
      { "char": "失", "role": "잃을 실 (요소)", "desc": "본래 鐵(철)에서 간략화된 글자체로, 녹이 슬어 모양을 잃는 금속이라는 뜻을 암시합니다." }
    ],
    "story": "금속(金) 중에서도 단단하지만 녹이 슬면 본래의 모양을 잃어버리는(失) 검은 금속, 즉 '철(쇠)'을 의미합니다.",
    "example_words": [
      { "word": "鉄道", "reading": "てつどう", "meaning": "철도", "description": "쇠(鉄)로 만든 기차가 다니는 길(道)입니다." },
      { "word": "地下鉄", "reading": "ちかてつ", "meaning": "지하철", "description": "땅(地) 아래(下)로 다니는 철도(鉄)입니다." }
    ]
  },
  {
    "kanji": "転",
    "reading_on": "テン",
    "reading_kun": "ころ(がる)、ころ(ばす)",
    "meaning": "구를 / 구르다",
    "components": [
      { "char": "車", "role": "수레 거 (부수)", "desc": "수레나 바퀴를 뜻합니다." },
      { "char": "云", "role": "이를 운 (요소)", "desc": "원래 專(오로지 전)이 간략화된 것으로, 빙글빙글 둥글게 돈다는 뜻입니다." }
    ],
    "story": "수레(車)의 둥근 바퀴가 빙글빙글 굴러가듯이, 물건이 '구르다' 혹은 상태가 '바뀌다(회전하다)'는 뜻입니다.",
    "example_words": [
      { "word": "転ぶ", "reading": "ころぶ", "meaning": "구르다, 넘어지다", "description": "발을 헛디뎌 쓰러지거나 넘어지는 것입니다." },
      { "word": "運転", "reading": "うんてん", "meaning": "운전", "description": "수레를 움직여(運) 바퀴를 굴리며(転) 나아가는 일입니다." }
    ]
  },
  {
    "kanji": "都",
    "reading_on": "ト、ツ",
    "reading_kun": "みやこ",
    "meaning": "도읍 / 도시",
    "components": [
      { "char": "者", "role": "놈 자 (요소)", "desc": "많은 사람들이 모여 있다는 뜻과 발음 '자/토'를 나타냅니다." },
      { "char": "阝", "role": "우부방 (부수)", "desc": "고을이나 마을, 행정 구역을 뜻합니다." }
    ],
    "story": "수많은 사람(者)이 모여 살며 임금이 있는 큰 고을(阝), 즉 '도읍(수도)'이나 번화한 '도시'를 의미합니다.",
    "example_words": [
      { "word": "都会", "reading": "とかい", "meaning": "도시", "description": "사람들이 모여(会) 사는 도읍(都)입니다." },
      { "word": "京都", "reading": "きょうと", "meaning": "교토", "description": "일본의 옛 서울(京)이자 도읍(都)이었던 도시입니다." }
    ]
  },
  {
    "kanji": "度",
    "reading_on": "ド、ト、タク",
    "reading_kun": "たび",
    "meaning": "법도 / 번 (횟수)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "지붕이나 건물을 의미합니다." },
      { "char": "廿", "role": "스물 입 (요소)", "desc": "여러 번이라는 뜻입니다." },
      { "char": "又", "role": "또 우 (요소)", "desc": "손으로 세거나 잰다는 뜻입니다." }
    ],
    "story": "집안(广)에서 손(又)으로 길이나 양을 여러 번(廿) 자로 재어 정한 '법도'나 '정도', 혹은 일의 횟수인 '번'을 의미합니다.",
    "example_words": [
      { "word": "温度", "reading": "おんど", "meaning": "온도", "description": "따뜻하거나 차가운 정도(度)입니다." },
      { "word": "今度", "reading": "こんど", "meaning": "이번", "description": "지금(今) 닥친 차례나 번(度)입니다." }
    ]
  },
  {
    "kanji": "投",
    "reading_on": "トウ",
    "reading_kun": "な(げる)",
    "meaning": "던질",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "殳", "role": "창 수 (요소)", "desc": "창이나 무기, 혹은 창을 던지는 동작을 나타냅니다." }
    ],
    "story": "손(扌)에 창이나 무기(殳)를 쥐고 목표물을 향해 세게 '던지다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "投げる", "reading": "なげる", "meaning": "던지다", "description": "물건을 손으로 쥐고 목표를 향해 뿌리는 것입니다." },
      { "word": "投手", "reading": "とうしゅ", "meaning": "투수", "description": "야구에서 공을 던지는(投) 사람(手)입니다." }
    ]
  },
  {
    "kanji": "豆",
    "reading_on": "トウ、ズ",
    "reading_kun": "まめ",
    "meaning": "콩",
    "components": [
      { "char": "豆", "role": "콩 두 (부수)", "desc": "제사에 쓰는 굽이 높은 제기(그릇)의 모양을 본뜬 글자입니다." }
    ],
    "story": "본래 굽이 높은 제사 그릇을 그렸으나, 나중에 그릇에 담는 곡식 중 둥글고 작은 '콩'을 뜻하는 글자로 더 널리 쓰이게 되었습니다.",
    "example_words": [
      { "word": "豆", "reading": "まめ", "meaning": "콩", "description": "작고 둥근 식물의 열매입니다." },
      { "word": "豆腐", "reading": "とうふ", "meaning": "두부", "description": "콩(豆)을 갈아 부드럽게 썩힌(腐, 굳힌) 음식입니다." }
    ]
  },
  {
    "kanji": "島",
    "reading_on": "トウ",
    "reading_kun": "しま",
    "meaning": "섬",
    "components": [
      { "char": "鳥", "role": "새 조 (요소)", "desc": "새를 뜻합니다." },
      { "char": "山", "role": "뫼 산 (부수)", "desc": "산이나 땅이 솟은 모습을 뜻합니다." }
    ],
    "story": "물새(鳥)들이 날아가다가 쉬기 위해 내려앉는 바다 위로 솟아오른 작은 산(山) 같은 '섬'을 의미합니다.",
    "example_words": [
      { "word": "島", "reading": "しま", "meaning": "섬", "description": "바다나 물로 둘러싸인 땅입니다." },
      { "word": "半島", "reading": "はんとう", "meaning": "반도", "description": "반(半)쯤은 섬(島)처럼 물에 둘러싸인 육지입니다." }
    ]
  },
  {
    "kanji": "湯",
    "reading_on": "トウ",
    "reading_kun": "ゆ",
    "meaning": "끓일 (따뜻한 물)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "昜", "role": "볕 양 (요소)", "desc": "태양이 솟아올라 따뜻하게 햇볕이 내리쬔다는 뜻과 발음 '양/토우'를 줍니다." }
    ],
    "story": "물(氵)에 뜨거운 햇볕(昜)을 쬐거나 불을 지펴서 따뜻하게 데워진 '끓인 물'이나 '목욕물'을 뜻합니다.",
    "example_words": [
      { "word": "お湯", "reading": "おゆ", "meaning": "뜨거운 물", "description": "끓이거나 데운 따뜻한 물입니다." },
      { "word": "銭湯", "reading": "せんとう", "meaning": "대중목욕탕", "description": "돈(銭)을 내고 따뜻한 물(湯)에 목욕하는 곳입니다." }
    ]
  },
  {
    "kanji": "登",
    "reading_on": "トウ、ト",
    "reading_kun": "のぼ(る)",
    "meaning": "오를",
    "components": [
      { "char": "癶", "role": "필발머리 (부수)", "desc": "양발을 벌려 걷거나 오르는 모양입니다." },
      { "char": "豆", "role": "콩 두 (요소)", "desc": "제기(그릇)를 뜻하며, 제단이나 높은 곳을 상징합니다." }
    ],
    "story": "두 발(癶)을 벌려 내디디며 높은 제단이나 산(豆의 변형) 위로 한 걸음씩 '오르다'라는 뜻입니다.",
    "example_words": [
      { "word": "登る", "reading": "のぼる", "meaning": "오르다", "description": "산이나 높은 곳을 향해 위로 올라가는 것입니다." },
      { "word": "登山", "reading": "とざん", "meaning": "등산", "description": "산(山)에 오르는(登) 일입니다." }
    ]
  },
  {
    "kanji": "等",
    "reading_on": "トウ",
    "reading_kun": "ひと(しい)、など",
    "meaning": "무리 (같을 / 등급)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 뜻합니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "규칙적이고 가지런하다는 뜻과 발음 '사/토우'를 담당합니다." }
    ],
    "story": "대나무(竹)를 잘랐을 때 그 마디마디의 길이가 관청의 법도(寺)처럼 가지런하고 '같다'거나 똑같은 '등급(무리)'을 뜻합니다.",
    "example_words": [
      { "word": "等しい", "reading": "ひとしい", "meaning": "같다, 동등하다", "description": "크기나 수량, 가치 따위가 다르지 않고 같은 상태입니다." },
      { "word": "平等", "reading": "びょうどう", "meaning": "평등", "description": "차별 없이 평평하고(平) 같은(等) 상태입니다." }
    ]
  },
  {
    "kanji": "動",
    "reading_on": "ドウ",
    "reading_kun": "うご(く)、うご(かす)",
    "meaning": "움직일",
    "components": [
      { "char": "重", "role": "무거울 중 (요소)", "desc": "아주 무겁다는 뜻입니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 의미합니다." }
    ],
    "story": "무거운(重) 물건을 온 힘(力)을 다해 밀거나 끌어서 '움직이다'는 뜻을 나타냅니다.",
    "example_words": [
      { "word": "動く", "reading": "うごく", "meaning": "움직이다", "description": "정지해 있지 않고 자리를 옮기거나 흔들리는 것입니다." },
      { "word": "動物", "reading": "どうぶつ", "meaning": "동물", "description": "스스로 움직이는(動) 생물(物)입니다." }
    ]
  },
  {
    "kanji": "童",
    "reading_on": "ドウ",
    "reading_kun": "わらべ",
    "meaning": "아이",
    "components": [
      { "char": "立", "role": "설 립 (부수)", "desc": "원래 辛(매울 신, 형벌 도구)이 변형된 것으로 묶여 있음을 뜻합니다." },
      { "char": "里", "role": "마을 리 (요소)", "desc": "마을이나 눈(目)의 변형으로 쓰입니다." }
    ],
    "story": "고대에는 눈이 찔린(辛) 채 마을(里)에 붙잡힌 어린 노예를 뜻했으나, 나중에는 단지 나이가 어린 '아이'나 '아동'을 뜻하는 글자가 되었습니다.",
    "example_words": [
      { "word": "童話", "reading": "どうわ", "meaning": "동화", "description": "어린아이(童)를 위해 지은 재미있는 이야기(話)입니다." },
      { "word": "児童", "reading": "じどう", "meaning": "아동", "description": "나이가 어린(児) 아이(童)입니다." }
    ]
  },
  {
    "kanji": "毒",
    "reading_on": "ドク",
    "reading_kun": "",
    "meaning": "독",
    "components": [
      { "char": "生", "role": "날 생 (요소)", "desc": "식물이나 풀이 자라나는 모습을 의미합니다." },
      { "char": "毋", "role": "말 무 (부수)", "desc": "어미 모(母)의 변형이거나, 먹지 말라는 뜻을 줍니다." }
    ],
    "story": "풀이나 식물(生) 중에서 몸을 상하게 하므로 절대 먹지 말아야(毋) 하는 나쁜 성분, 즉 '독'을 뜻합니다.",
    "example_words": [
      { "word": "毒", "reading": "どく", "meaning": "독", "description": "건강을 해치거나 생명을 뺏는 나쁜 물질입니다." },
      { "word": "消毒", "reading": "しょうどく", "meaning": "소독", "description": "독(毒)이나 세균을 없애고 사라지게(消) 하는 것입니다." }
    ]
  },
  {
    "kanji": "独",
    "reading_on": "ドク",
    "reading_kun": "ひと(り)",
    "meaning": "홀로",
    "components": [
      { "char": "犭", "role": "개사슴록변 (부수)", "desc": "개나 짐승을 뜻합니다." },
      { "char": "虫", "role": "벌레 충 (요소)", "desc": "벌레나 혼자 있다는 뜻의 발음 '독'을 줍니다." }
    ],
    "story": "무리 지어 다니는 양과 달리, 개나 야생동물(犭)이 무리에서 떨어져 웅크리고(虫의 변형) '홀로' 있는 모습을 뜻합니다.",
    "example_words": [
      { "word": "独立", "reading": "どくりつ", "meaning": "독립", "description": "홀로(独) 당당하게 서는(立) 것입니다." },
      { "word": "独身", "reading": "どくしん", "meaning": "독신", "description": "결혼하지 않고 홀로(独) 있는 몸(身)입니다." }
    ]
  },
  {
    "kanji": "内",
    "reading_on": "ナイ",
    "reading_kun": "うち",
    "meaning": "안 (내부)",
    "components": [
      { "char": "冂", "role": "멀 경 (부수)", "desc": "성벽이나 집의 외부 테두리를 뜻합니다." },
      { "char": "入", "role": "들 입 (요소)", "desc": "안으로 들어감을 뜻합니다." }
    ],
    "story": "담장이나 집(冂) 바깥에서 건물 '안'으로 들어간다(入)는 데서 사물의 '내부'나 '안쪽'을 뜻합니다.",
    "example_words": [
      { "word": "内", "reading": "うち", "meaning": "안, 집", "description": "건물의 내부나 자기의 집, 속마음을 뜻합니다." },
      { "word": "案内", "reading": "あんない", "meaning": "안내", "description": "어떤 곳의 사정(内)을 알고 편안하게(安) 이끌어 주는 일입니다." }
    ]
  },
  {
    "kanji": "波",
    "reading_on": "ハ",
    "reading_kun": "なみ",
    "meaning": "물결 (파도)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 바다를 뜻합니다." },
      { "char": "皮", "role": "가죽 피 (요소)", "desc": "가죽의 표면이나 겉을 뜻하며 발음 '피/하'를 줍니다." }
    ],
    "story": "바다나 물(氵)의 겉 표면(皮)이 바람에 휩쓸려 일어나는 주름진 '물결'이나 '파도'를 뜻합니다.",
    "example_words": [
      { "word": "波", "reading": "なみ", "meaning": "파도, 물결", "description": "수면에 일어나는 물결입니다." },
      { "word": "電波", "reading": "でんぱ", "meaning": "전파", "description": "전기(電) 신호가 파도(波)처럼 진동하며 퍼져나가는 것입니다." }
    ]
  },
  {
    "kanji": "配",
    "reading_on": "ハイ",
    "reading_kun": "くば(る)",
    "meaning": "나눌 / 짝지을",
    "components": [
      { "char": "酉", "role": "닭 유 (부수)", "desc": "술이나 항아리를 의미합니다." },
      { "char": "己", "role": "몸 기 (요소)", "desc": "무릎을 꿇은 사람의 모습으로, 여기서는 사람에게 나누어 준다는 뜻입니다." }
    ],
    "story": "술항아리(酉)에서 술을 떠서 사람(己)들에게 골고루 '나누어 주다' 혹은 '짝지어 분배하다'는 뜻입니다.",
    "example_words": [
      { "word": "配る", "reading": "くばる", "meaning": "나누어 주다, 배부하다", "description": "여러 사람에게 물건을 골고루 나누어 주는 것입니다." },
      { "word": "心配", "reading": "しんぱい", "meaning": "걱정, 근심", "description": "마음(心)을 여러 곳으로 나누어(配) 쓰며 애태우는 것입니다." }
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

print("Grade 3 Part 5 data appended successfully.")
