import json
import os

new_data = [
  {
    "kanji": "巣",
    "reading_on": "ソウ",
    "reading_kun": "す",
    "meaning": "새집 (둥지)",
    "components": [
      { "char": "ツ", "role": "머리 (요소)", "desc": "새들이 모여 있는 모습입니다." },
      { "char": "田", "role": "밭 전 (요소)", "desc": "새알이 담긴 둥근 둥지 모양입니다." },
      { "char": "木", "role": "나무 목 (부수)", "desc": "둥지를 짓는 나무입니다." }
    ],
    "story": "나무(木) 위에 새들이 모여(ツ) 알(田)을 품고 있는 '새집'이나 짐승의 '둥지'를 뜻합니다.",
    "example_words": [
      { "word": "巣", "reading": "す", "meaning": "둥지, 새집", "description": "새나 짐승이 알을 낳고 새끼를 기르는 곳입니다." },
      { "word": "巣箱", "reading": "すばこ", "meaning": "새장", "description": "새가 살도록 나무 등에 달아놓은 둥지 상자(箱)입니다." }
    ]
  },
  {
    "kanji": "束",
    "reading_on": "ソク",
    "reading_kun": "たば",
    "meaning": "묶을",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나뭇가지나 장작을 뜻합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "여기서는 나뭇가지를 동여맨 끈이나 밧줄을 본뜬 모양입니다." }
    ],
    "story": "나뭇가지(木) 여러 개를 하나로 모아 밧줄(口의 변형)로 칭칭 감아 '묶다' 혹은 하나로 묶은 '다발'을 의미합니다.",
    "example_words": [
      { "word": "花束", "reading": "はなたば", "meaning": "꽃다발", "description": "꽃(花)을 모아 한데 묶은 다발(束)입니다." },
      { "word": "約束", "reading": "やくそく", "meaning": "약속", "description": "서로 말을 맺고(約) 단단히 묶어(束) 지키기로 하는 일입니다." }
    ]
  },
  {
    "kanji": "側",
    "reading_on": "ソク",
    "reading_kun": "かわ、がわ、そば",
    "meaning": "곁 (측면)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "則", "role": "법칙 칙 (요소)", "desc": "칼로 새겨 기준을 정한다는 뜻으로, 곁에 둔다는 의미와 발음 '칙/소쿠'를 줍니다." }
    ],
    "story": "사람(亻)이 칼로 정해진 규칙(則)을 언제나 가까이에 두고 지킨다는 데서 사물이나 사람의 옆인 '곁'이나 '측면'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "側", "reading": "がわ", "meaning": "쪽, 편", "description": "어떤 사물이나 사람의 옆 방향이나 입장입니다." },
      { "word": "右側", "reading": "みぎがわ", "meaning": "오른쪽", "description": "오른(右) 방향의 편(側)입니다." }
    ]
  },
  {
    "kanji": "続",
    "reading_on": "ゾク",
    "reading_kun": "つづ(く)、つづ(ける)",
    "meaning": "이을",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실이나 끈을 뜻합니다." },
      { "char": "売", "role": "팔 매 (요소)", "desc": "물건을 내놓아 팔거나 넘겨준다는 뜻과 발음 '매/조쿠'를 담당합니다." }
    ],
    "story": "끊어진 실(糸)을 다른 사람에게 넘겨주듯(売) 끊임없이 하나로 '잇다' 혹은 '계속되다'는 의미입니다.",
    "example_words": [
      { "word": "続く", "reading": "つづく", "meaning": "계속되다, 이어지다", "description": "끊이지 않고 뒤를 이어서 나아가는 것입니다." },
      { "word": "連続", "reading": "れんぞく", "meaning": "연속", "description": "끊어지지 않고 연달아(連) 이어지는(続) 일입니다." }
    ]
  },
  {
    "kanji": "卒",
    "reading_on": "ソツ",
    "reading_kun": "",
    "meaning": "마칠",
    "components": [
      { "char": "衣", "role": "옷 의 (요소)", "desc": "여기서는 옷(衣)에 여러 개의 표시를 한 모양에서 유래했습니다." },
      { "char": "十", "role": "열 십 (부수)", "desc": "모인다는 뜻입니다." }
    ],
    "story": "같은 옷(衣의 변형)을 입고 모인(十) 병사들 무리인 '졸개'를 뜻하다가, 무리 지어 함께 학업을 '마치다(졸업하다)'는 뜻으로 주로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "卒業", "reading": "そつぎょう", "meaning": "졸업", "description": "정해진 학업(業)을 모두 마치는(卒) 일입니다." },
      { "word": "大卒", "reading": "だいそつ", "meaning": "대졸", "description": "대학교(大)를 졸업함(卒)의 줄임말입니다." }
    ]
  },
  {
    "kanji": "孫",
    "reading_on": "ソン",
    "reading_kun": "まご",
    "meaning": "손자",
    "components": [
      { "char": "子", "role": "아들 자 (부수)", "desc": "자식이나 어린아이를 뜻합니다." },
      { "char": "系", "role": "이을 계 (요소)", "desc": "실(糸)처럼 길게 이어진다는 뜻과 발음 '계/손'을 줍니다." }
    ],
    "story": "자식(子)에게서 태어나 핏줄이 실처럼 길게 이어져(系) 내려가는 후손인 '손자'나 자손을 뜻합니다.",
    "example_words": [
      { "word": "孫", "reading": "まご", "meaning": "손자, 손녀", "description": "아들이나 딸이 낳은 자식입니다." },
      { "word": "子孫", "reading": "しそん", "meaning": "자손", "description": "자식(子)과 손자(孫), 즉 핏줄을 이어갈 후대입니다." }
    ]
  },
  {
    "kanji": "帯",
    "reading_on": "タイ",
    "reading_kun": "おび、お(びる)",
    "meaning": "띠",
    "components": [
      { "char": "丗", "role": "스물 입 (요소)", "desc": "여러 개의 장식이나 끈을 나타냅니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "허리를 덮거나 감싸는 모양입니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "천이나 옷감을 의미합니다." }
    ],
    "story": "여러 개의 장식(丗)이 달린 천(巾)으로 사람의 허리를 덮어(冖) 묶는 긴 '띠'를 뜻하며, 무언가를 몸에 지니거나 띠는 것을 의미합니다.",
    "example_words": [
      { "word": "帯", "reading": "おび", "meaning": "띠, 허리띠", "description": "옷이 풀리지 않게 허리에 두르는 끈입니다." },
      { "word": "携帯", "reading": "けいたい", "meaning": "휴대", "description": "손에 들거나(携) 몸에 지니고(帯) 다니는 것입니다." }
    ]
  },
  {
    "kanji": "隊",
    "reading_on": "タイ",
    "reading_kun": "",
    "meaning": "무리 (부대)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 험한 지형을 뜻합니다." },
      { "char": "㒸", "role": "돼지 시 (요소)", "desc": "위에서 무언가가 쏟아져 내리거나 길을 따라간다는 의미와 발음 '수/타이'를 줍니다." }
    ],
    "story": "험한 언덕길(阝)을 무리 지어 줄을 서서 쏟아지듯(㒸) 나아가는 군사들이나 사람들의 '대열'이나 '부대(무리)'를 뜻합니다.",
    "example_words": [
      { "word": "軍隊", "reading": "ぐんたい", "meaning": "군대", "description": "전투를 위해 조직된 군사(軍)의 무리(隊)입니다." },
      { "word": "兵隊", "reading": "へいたい", "meaning": "군인, 병대", "description": "병사(兵)들로 이뤄진 무리(隊)입니다." }
    ]
  },
  {
    "kanji": "達",
    "reading_on": "タツ",
    "reading_kun": "たち",
    "meaning": "통달할",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "幸", "role": "다행 행 (요소)", "desc": "여기서는 원래 새끼 양(羊)의 변형으로, 새끼 양이 어미를 막힘없이 쑥 낳고 지나간다는 뜻을 줍니다." }
    ],
    "story": "새끼 양이 쑥 태어나듯 거침없이 길(辶)을 나아가 목적지에 막힘없이 '이르다' 혹은 사리에 밝게 '통달하다'는 뜻입니다.",
    "example_words": [
      { "word": "友達", "reading": "ともだち", "meaning": "친구", "description": "벗(友)들의 무리(~達)입니다." },
      { "word": "配達", "reading": "はいたつ", "meaning": "배달", "description": "물건을 나누어(配) 목적지에 이르게(達) 하는 것입니다." }
    ]
  },
  {
    "kanji": "単",
    "reading_on": "タン",
    "reading_kun": "",
    "meaning": "홑 (간단할)",
    "components": [
      { "char": "ツ", "role": "머리 (요소)", "desc": "원래 양쪽으로 갈라진 나뭇가지 모양을 나타냅니다." },
      { "char": "甲", "role": "갑옷 갑 (요소)", "desc": "방패처럼 넓은 나무판자를 뜻합니다." },
      { "char": "十", "role": "열 십 (부수)", "desc": "무기를 쥐는 손잡이 부분입니다." }
    ],
    "story": "원래 사냥할 때 쓰는 커다란 몽둥이(방패와 손잡이가 달린 무기)를 본뜬 모양이나, 나중에는 겹치지 않고 오직 하나뿐인 무기라는 데서 '홑'이나 '간단하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "簡単", "reading": "かんたん", "meaning": "간단", "description": "간략하고(簡) 홑치기(単)처럼 복잡하지 않은 상태입니다." },
      { "word": "単語", "reading": "たんご", "meaning": "단어", "description": "의미를 가지는 하나의 홑(単) 말(語)입니다." }
    ]
  },
  {
    "kanji": "置",
    "reading_on": "チ",
    "reading_kun": "お(く)",
    "meaning": "둘 (위치할)",
    "components": [
      { "char": "罒", "role": "그물망 머리 (부수)", "desc": "그물이나 함정을 뜻합니다." },
      { "char": "直", "role": "곧을 직 (요소)", "desc": "똑바로 세운다는 뜻과 발음 '직/치'를 줍니다." }
    ],
    "story": "새나 짐승을 잡기 위해 그물(罒)을 똑바로(直) 세워 한곳에 '두다(설치하다)' 혹은 '놓다'라는 뜻입니다.",
    "example_words": [
      { "word": "置く", "reading": "おく", "meaning": "두다, 놓다", "description": "물건을 어떤 장소에 위치시키는 것입니다." },
      { "word": "位置", "reading": "いち", "meaning": "위치", "description": "사물이 놓여(置) 있는 자리(位)입니다." }
    ]
  },
  {
    "kanji": "仲",
    "reading_on": "チュウ",
    "reading_kun": "なか",
    "meaning": "버금 (가운데 / 사이)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "中", "role": "가운데 중 (요소)", "desc": "가운데나 사이라는 뜻과 발음 '중/츄우'를 담당합니다." }
    ],
    "story": "형과 아우 사이의 가운데(中)에 있는 둘째(버금) 사람(亻)을 의미하며, 사람과 사람의 '사이(관계)'를 뜻하기도 합니다.",
    "example_words": [
      { "word": "仲", "reading": "なか", "meaning": "사이, 관계", "description": "사람과 사람 사이의 관계나 교분입니다." },
      { "word": "仲間", "reading": "なかま", "meaning": "동료, 한패", "description": "같은 무리나 한 무리 안의 사이(仲)를 뜻합니다." }
    ]
  },
  {
    "kanji": "貯",
    "reading_on": "チョ",
    "reading_kun": "た(める)、た(まる)",
    "meaning": "쌓을 (모을)",
    "components": [
      { "char": "貝", "role": "조개 패 (부수)", "desc": "재물이나 돈을 뜻합니다." },
      { "char": "宁", "role": "쌓을 저 (요소)", "desc": "그릇 안에 물건을 쌓아 둔다는 뜻과 발음 '저/쵸'를 줍니다." }
    ],
    "story": "돈이나 귀중한 재물(貝)을 그릇이나 창고에 차곡차곡 쌓아(宁) '모으다' 혹은 '저축하다'는 뜻입니다.",
    "example_words": [
      { "word": "貯金", "reading": "ちょきん", "meaning": "저금, 저축", "description": "돈(金)을 모아 쌓아두는(貯) 일입니다." },
      { "word": "貯める", "reading": "ためる", "meaning": "모으다, 저축하다", "description": "돈이나 물건을 한곳에 모아두는 것입니다." }
    ]
  },
  {
    "kanji": "兆",
    "reading_on": "チョウ",
    "reading_kun": "きざ(し)、きざ(す)",
    "meaning": "조짐 (조)",
    "components": [
      { "char": "儿", "role": "어진사람인발 (부수)", "desc": "거북이 등껍질이나 뼈의 갈라진 모양을 나타내는 부분입니다." },
      { "char": "冫", "role": "이수변 (요소)", "desc": "불에 구운 껍질이 툭툭 갈라진 선입니다." }
    ],
    "story": "점을 칠 때 불에 구운 거북이 등껍질이 쫙쫙 갈라지는 모양을 본뜬 글자로, 앞으로 일어날 일의 '조짐'이나 어마어마하게 많은 숫자 '조'를 뜻합니다.",
    "example_words": [
      { "word": "兆", "reading": "ちょう", "meaning": "조 (숫자)", "description": "억의 만 배가 되는 어마어마하게 큰 숫자입니다." },
      { "word": "兆し", "reading": "きざし", "meaning": "조짐, 징조", "description": "어떤 일이 일어날 듯한 낌새나 모양입니다." }
    ]
  },
  {
    "kanji": "腸",
    "reading_on": "チョウ",
    "reading_kun": "はらわた",
    "meaning": "창자",
    "components": [
      { "char": "月", "role": "육달월 (부수)", "desc": "사람의 신체나 장기를 뜻합니다." },
      { "char": "昜", "role": "볕 양 (요소)", "desc": "햇빛이 멀리 퍼져나간다는 데서, 몸속에서 길게 구불구불 이어져 있다는 뜻과 발음 '장/쵸우'를 줍니다." }
    ],
    "story": "몸속(月)에 햇빛이 퍼지듯 아주 길고 구불구불하게 이어져 있는 소화 기관인 '창자'를 의미합니다.",
    "example_words": [
      { "word": "胃腸", "reading": "いちょう", "meaning": "위장", "description": "소화를 담당하는 위(胃)와 창자(腸)입니다." },
      { "word": "大腸", "reading": "だいちょう", "meaning": "대장", "description": "소장 끝에서 항문까지 이어지는 큰(大) 창자(腸)입니다." }
    ]
  },
  {
    "kanji": "低",
    "reading_on": "テイ",
    "reading_kun": "ひく(い)、ひく(める)、ひく(まる)",
    "meaning": "낮을",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "氐", "role": "근본 저 (요소)", "desc": "뿌리가 땅 밑으로 뻗어 내려간다는 뜻과 발음 '저/테이'를 담당합니다." }
    ],
    "story": "사람(亻)이 허리를 굽혀 식물의 뿌리(氐)처럼 바닥을 향해 몸을 '낮추다' 혹은 키나 지위가 '낮다'는 뜻입니다.",
    "example_words": [
      { "word": "低い", "reading": "ひくい", "meaning": "낮다", "description": "높이나 지위, 온도 따위가 기준보다 아래에 있는 상태입니다." },
      { "word": "最低", "reading": "さいてい", "meaning": "최저, 최악", "description": "가장(最) 낮거나(低) 몹시 나쁜 상태입니다." }
    ]
  },
  {
    "kanji": "底",
    "reading_on": "テイ",
    "reading_kun": "そこ",
    "meaning": "밑 (바닥)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "건물이나 지붕 아래를 뜻합니다." },
      { "char": "氐", "role": "근본 저 (요소)", "desc": "식물 뿌리가 가장 밑바닥까지 내려간다는 뜻과 발음 '저/테이'를 줍니다." }
    ],
    "story": "건물(广)의 뿌리가 닿는 가장 아래쪽, 즉 사물의 맨 아래쪽인 '밑바닥'이나 '바닥'을 뜻합니다.",
    "example_words": [
      { "word": "底", "reading": "そこ", "meaning": "바닥, 밑", "description": "그릇이나 물건의 맨 아랫부분입니다." },
      { "word": "徹底", "reading": "てってい", "meaning": "철저", "description": "통하여서(徹) 바닥(底)까지 닿게 끝까지 하는 일입니다." }
    ]
  },
  {
    "kanji": "停",
    "reading_on": "テイ",
    "reading_kun": "と(まる)、と(める)",
    "meaning": "머무를",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "亭", "role": "정자 정 (요소)", "desc": "사람이 잠시 쉬어가는 정자나 쉼터, 발음 '정/테이'를 담당합니다." }
    ],
    "story": "길을 걷던 사람(亻)이 정자(亭)에 앉아 발걸음을 멈추고 잠시 '머무르다' 혹은 '정지하다'는 의미입니다.",
    "example_words": [
      { "word": "停止", "reading": "ていし", "meaning": "정지", "description": "머물러서(停) 움직임을 멈추는(止) 일입니다." },
      { "word": "停留所", "reading": "ていりゅうじょ", "meaning": "정류소, 버스정류장", "description": "버스 따위가 머물렀다(停) 가는(留) 곳(所)입니다." }
    ]
  },
  {
    "kanji": "的",
    "reading_on": "テキ",
    "reading_kun": "まと",
    "meaning": "과녁",
    "components": [
      { "char": "白", "role": "흰 백 (부수)", "desc": "하얗고 분명하다는 뜻을 줍니다." },
      { "char": "勺", "role": "구기 작 (요소)", "desc": "국자 모양으로 무언가를 뚜렷하게 떠낸다는 뜻과 발음 '작/테키'를 담당합니다." }
    ],
    "story": "하얗고(白) 선명하게 그려져 화살을 쏘기 좋게 만든 '과녁'을 뜻하며, 과녁을 맞히듯 확실하다는 뜻을 지닙니다.",
    "example_words": [
      { "word": "的", "reading": "まと", "meaning": "과녁, 표적", "description": "화살이나 총을 쏠 때 목표로 삼는 물건입니다." },
      { "word": "目的", "reading": "もくてき", "meaning": "목적", "description": "눈(目)으로 겨냥하는 과녁(的), 즉 실현하려는 목표입니다." }
    ]
  },
  {
    "kanji": "典",
    "reading_on": "テン",
    "reading_kun": "",
    "meaning": "법전 (책)",
    "components": [
      { "char": "曲", "role": "굽을 곡 (요소)", "desc": "원래 冊(책 책)의 변형으로, 여러 개의 대나무 죽간을 엮은 모양입니다." },
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "여기서는 두 손(廾)으로 책을 받쳐 든 모양의 생략형입니다." }
    ],
    "story": "두 손으로 소중한 책(曲의 본래 뜻)을 받들고 있는 모양에서, 법이나 기준으로 삼아야 할 훌륭한 '법전'이나 중요한 '책'을 뜻합니다.",
    "example_words": [
      { "word": "辞典", "reading": "じてん", "meaning": "사전", "description": "단어와 뜻(辞)을 모아 기준이 되게 엮은 책(典)입니다." },
      { "word": "古典", "reading": "こてん", "meaning": "고전", "description": "옛날(古)에 쓰인 훌륭한 책(典)이나 예술 작품입니다." }
    ]
  },
  {
    "kanji": "伝",
    "reading_on": "デン、テン",
    "reading_kun": "つた(わる)、つた(える)",
    "meaning": "전할",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "云", "role": "이를 운 (요소)", "desc": "원래 專(오로지 전)이 약자로 바뀐 것으로 수레바퀴가 돌듯 이어진다는 의미입니다." }
    ],
    "story": "사람(亻)이 다른 사람에게 물건이나 말을 수레바퀴 굴러가듯(云의 본뜻) 계속 이어 '전하다' 혹은 '전달하다'는 뜻입니다.",
    "example_words": [
      { "word": "伝える", "reading": "つたえる", "meaning": "전하다, 전달하다", "description": "말이나 물건을 다른 사람에게 이어받게 하는 일입니다." },
      { "word": "伝統", "reading": "でんとう", "meaning": "전통", "description": "예전부터 전해져(伝) 내려오는 계통(統)이나 문화입니다." }
    ]
  },
  {
    "kanji": "徒",
    "reading_on": "ト",
    "reading_kun": "いたずら",
    "meaning": "무리 (걸을)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "走", "role": "달릴 주 (요소)", "desc": "원래 발이나 걷는 모습을 본뜬 글자의 변형입니다." }
    ],
    "story": "수레를 타지 않고 발(走)로 직접 길(彳)을 걷는 사람, 혹은 스승을 따라 길을 걷는 제자들의 '무리(도당)'를 뜻합니다.",
    "example_words": [
      { "word": "生徒", "reading": "せいと", "meaning": "학생", "description": "학교에서 배우고 자라나는(生) 제자나 무리(徒)입니다." },
      { "word": "徒歩", "reading": "とほ", "meaning": "도보", "description": "탈것을 타지 않고 맨발(徒)로 걷는(歩) 일입니다." }
    ]
  },
  {
    "kanji": "努",
    "reading_on": "ド",
    "reading_kun": "つと(める)",
    "meaning": "힘쓸",
    "components": [
      { "char": "奴", "role": "종 노 (요소)", "desc": "노비나 종이 억지로 일한다는 뜻과 발음 '노/도'를 줍니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 의미합니다." }
    ],
    "story": "종(奴)이 억지로 땀을 뻘뻘 흘리며 온 힘(力)을 다해 열심히 일하듯, 목표를 향해 애써 '힘쓰다(노력하다)'는 의미입니다.",
    "example_words": [
      { "word": "努力", "reading": "どりょく", "meaning": "노력", "description": "애를 써서(努) 온 힘(力)을 다하는 것입니다." },
      { "word": "努める", "reading": "つとめる", "meaning": "애쓰다, 노력하다", "description": "어떤 일을 해내기 위해 마음과 힘을 다하는 것입니다." }
    ]
  },
  {
    "kanji": "灯",
    "reading_on": "トウ",
    "reading_kun": "ひ",
    "meaning": "등불",
    "components": [
      { "char": "火", "role": "불 화 (부수)", "desc": "불이나 열기를 뜻합니다." },
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "쇠못 모양으로, 불을 피워 올린 모습이나 발음 '정/토우'를 줍니다." }
    ],
    "story": "밤눈을 밝히기 위해 쇠못(丁)이나 받침대 위에 불(火)을 밝혀 놓은 '등불'을 뜻합니다.",
    "example_words": [
      { "word": "灯", "reading": "ひ", "meaning": "등불, 불빛", "description": "어둠을 밝히는 등잔불이나 조명입니다." },
      { "word": "電灯", "reading": "でんとう", "meaning": "전등", "description": "전기(電)로 밝히는 등불(灯)이나 조명 기구입니다." }
    ]
  },
  {
    "kanji": "堂",
    "reading_on": "ドウ",
    "reading_kun": "",
    "meaning": "집 (당)",
    "components": [
      { "char": "尚", "role": "오히려 상 (요소)", "desc": "높이 솟아 있다는 뜻과 발음 '상/도우'를 담당합니다." },
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅, 토대를 의미합니다." }
    ],
    "story": "흙(土)으로 토대를 높이 쌓아(尚) 크고 화려하게 지은 전당이나 번듯한 '집'을 뜻합니다.",
    "example_words": [
      { "word": "食堂", "reading": "しょくどう", "meaning": "식당", "description": "밥(食)을 먹도록 지은 집이나 방(堂)입니다." },
      { "word": "堂々と", "reading": "どうどうと", "meaning": "당당하게", "description": "큰 집(堂)처럼 의젓하고 떳떳한 모양입니다." }
    ]
  },
  {
    "kanji": "働",
    "reading_on": "ドウ",
    "reading_kun": "はたら(く)",
    "meaning": "일할",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "動", "role": "움직일 동 (요소)", "desc": "물건을 옮기거나 활동한다는 뜻과 발음 '동/도우'를 줍니다." }
    ],
    "story": "사람(亻)이 부지런히 몸을 움직여서(動) 직업을 가지고 쓸모 있게 '일하다'라는 뜻의 일본 고유 한자(국자)입니다.",
    "example_words": [
      { "word": "働く", "reading": "はたらく", "meaning": "일하다", "description": "직업을 가지고 몸을 써서 일을 하는 것입니다." },
      { "word": "労働", "reading": "ろうどう", "meaning": "노동", "description": "힘써서(労) 일하고(働) 몸을 움직이는 일입니다." }
    ]
  },
  {
    "kanji": "特",
    "reading_on": "トク",
    "reading_kun": "",
    "meaning": "특별할",
    "components": [
      { "char": "牛", "role": "소 우 (부수)", "desc": "소를 의미합니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "손으로 모신다는 뜻이나, 여기서는 다른 소들과 다르게 구별된다는 의미입니다." }
    ],
    "story": "여러 마리의 소(牛) 떼 속에서 유난히 눈에 띄게 우뚝 서(寺의 멈춰 서 있다는 뜻) 있는 빼어난 황소, 즉 무리에서 뛰어나고 '특별하다'는 뜻입니다.",
    "example_words": [
      { "word": "特別", "reading": "とくべつ", "meaning": "특별", "description": "보통과 다르게 뛰어나고(特) 구별됨(別)을 뜻합니다." },
      { "word": "特徴", "reading": "とくちょう", "meaning": "특징", "description": "다른 것과 뚜렷이 구별되는(特) 증표(徴)나 성질입니다." }
    ]
  },
  {
    "kanji": "得",
    "reading_on": "トク",
    "reading_kun": "え(る)、う(る)",
    "meaning": "얻을",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "旦", "role": "아침 단 (요소)", "desc": "원래 조개나 재물을 뜻하는 貝의 변형입니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "손을 뜻합니다." }
    ],
    "story": "길(彳)을 가다가 땅에 떨어진 재물이나 조개껍데기(旦)를 손(寸)으로 주워 내 것으로 '얻다'는 뜻입니다.",
    "example_words": [
      { "word": "得る", "reading": "える", "meaning": "얻다, 획득하다", "description": "원하는 물건이나 이익, 지식을 자기 것으로 만드는 일입니다." },
      { "word": "得意", "reading": "とくい", "meaning": "잘함, 득의양양", "description": "자신의 뜻(意)을 이루어 얻고(得) 뽐내거나 재주가 뛰어난 일입니다." }
    ]
  },
  {
    "kanji": "毒",
    "reading_on": "ドク",
    "reading_kun": "",
    "meaning": "독",
    "components": [
      { "char": "生", "role": "날 생 (요소)", "desc": "식물이나 풀이 자라나는 모습을 의미합니다." },
      { "char": "毋", "role": "말 무 (부수)", "desc": "먹지 말라는 금지의 뜻을 나타냅니다." }
    ],
    "story": "풀이나 식물(生) 중에서 몸을 상하게 하므로 절대 먹지 말아야(毋) 하는 해로운 성분인 '독'을 의미합니다.",
    "example_words": [
      { "word": "毒", "reading": "どく", "meaning": "독", "description": "생물이나 사람의 건강을 해치는 나쁜 물질입니다." },
      { "word": "中毒", "reading": "ちゅうどく", "meaning": "중독", "description": "독(毒)에 맞아서(中) 몸에 이상이 생기거나 어떤 것에 깊이 빠지는 일입니다." }
    ]
  },
  {
    "kanji": "熱",
    "reading_on": "ネツ",
    "reading_kun": "あつ(い)",
    "meaning": "더울 (뜨거울)",
    "components": [
      { "char": "埶", "role": "심을 예 (요소)", "desc": "나무를 심거나 무언가를 잡고 있다는 뜻과 발음 '예/네츠'를 줍니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불이나 열기를 뜻합니다." }
    ],
    "story": "나무를 잡고(埶) 거세게 타오르는 불(灬) 옆에 가까이 있어서 몸이 몹시 '뜨겁다' 혹은 '열(열기)'을 의미합니다.",
    "example_words": [
      { "word": "熱い", "reading": "あつい", "meaning": "뜨겁다", "description": "불이나 열기 때문에 물체의 온도가 아주 높은 상태입니다." },
      { "word": "熱心", "reading": "ねっしん", "meaning": "열심", "description": "어떤 일에 뜨거운(熱) 마음(心)을 쏟는 것입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade4.json'
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

print("Grade 4 Part 5 data appended successfully.")
