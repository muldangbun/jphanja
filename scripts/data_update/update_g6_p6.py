import json
import os

new_data = [
  {
    "kanji": "視",
    "reading_on": "シ",
    "reading_kun": "み(る)",
    "meaning": "볼",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "신이나 조상에게 보여준다는 뜻에서 드러내어 보인다는 의미입니다." },
      { "char": "見", "role": "볼 견 (요소)", "desc": "눈으로 쳐다보는 동작을 나타냅니다." }
    ],
    "story": "눈앞에 드러나 보인(示) 것을 눈(見)을 크게 뜨고 자세히 쳐다보며 '보다(시찰하다)' 혹은 살핀다는 의미입니다.",
    "example_words": [
      { "word": "視線", "reading": "しせん", "meaning": "시선", "description": "눈으로 보는(視) 선(線), 즉 눈길이나 시력입니다." },
      { "word": "監視", "reading": "かんし", "meaning": "감시", "description": "잘못을 저지르지 않는지 눈여겨보고(監) 살피는(視) 일입니다." }
    ]
  },
  {
    "kanji": "覧",
    "reading_on": "ラン",
    "reading_kun": "",
    "meaning": "볼",
    "components": [
      { "char": "監", "role": "살필 감 (요소)", "desc": "눈을 크게 뜨고 살펴본다는 뜻과 발음 '감/란'의 변형 역할을 합니다. (위쪽 부분)" },
      { "char": "見", "role": "볼 견 (부수)", "desc": "눈으로 보는 동작을 뜻합니다." }
    ],
    "story": "높은 곳에서 아래를 살피듯(監 변형), 눈(見)으로 두루두루 넓게 쳐다보며 '보다(관람하다)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "展覧会", "reading": "てんらんかい", "meaning": "전람회", "description": "여러 가지 물건을 펼쳐(展) 놓고 사람들이 보게(覧) 하는 모임(会)입니다." },
      { "word": "観覧", "reading": "かんらん", "meaning": "관람", "description": "연극이나 영화, 풍경 따위를 구경하며(観) 보는(覧) 것입니다." }
    ]
  },
  {
    "kanji": "討",
    "reading_on": "トウ",
    "reading_kun": "う(つ)",
    "meaning": "칠 (토벌할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "손으로 재거나 따진다는 뜻과 규칙(법도)이라는 의미를 줍니다." }
    ],
    "story": "말(言)로 상대방의 잘못된 점을 따져(寸) 묻고 무기로 공격하여 '치다(토벌하다)', 혹은 어떤 일에 대해 깊이 파고들어 묻는다는 뜻입니다.",
    "example_words": [
      { "word": "討つ", "reading": "うつ", "meaning": "치다, 베다", "description": "적이나 나쁜 사람을 무기로 쳐서 무찌르는 것입니다." },
      { "word": "討論", "reading": "とうろん", "meaning": "토론", "description": "어떤 문제에 대해 서로 옳고 그름을 따져(討) 논하는(論) 일입니다." }
    ]
  },
  {
    "kanji": "訪",
    "reading_on": "ホウ",
    "reading_kun": "おとず(れる)、たず(ねる)",
    "meaning": "찾을 (방문할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "方", "role": "모 방 (요소)", "desc": "사방이라는 뜻에서 여기저기 돌아다닌다는 의미와 발음 '방/호우'를 줍니다." }
    ],
    "story": "여기저기(方) 돌아다니며 사람들에게 말(言)로 물어물어 목적지나 사람을 '찾다(방문하다)' 혹은 찾아간다는 뜻입니다.",
    "example_words": [
      { "word": "訪れる", "reading": "おとずれる", "meaning": "방문하다, 찾아오다", "description": "사람을 찾아가거나 어떤 계절이나 시대가 다가오는 것입니다." },
      { "word": "訪問", "reading": "ほうもん", "meaning": "방문", "description": "어떤 사람이나 장소를 찾아가서(訪) 인사하거나 묻는(問) 일입니다." }
    ]
  },
  {
    "kanji": "訳",
    "reading_on": "ヤク",
    "reading_kun": "わけ",
    "meaning": "번역할 (까닭)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 의미합니다." },
      { "char": "尺", "role": "자 척 (요소)", "desc": "길이를 잰다는 뜻에서 따져 본다는 의미와 발음 '척/야쿠'의 변형 역할을 합니다." }
    ],
    "story": "알아듣기 힘든 말(言)을 자로 재듯(尺) 따져서 알기 쉬운 다른 말로 바꾸어 '번역하다', 혹은 일이 벌어진 사리나 '까닭'을 뜻합니다.",
    "example_words": [
      { "word": "訳", "reading": "わけ", "meaning": "까닭, 이유, 뜻", "description": "말의 뜻이나 어떤 일이 일어나게 된 이유입니다." },
      { "word": "翻訳", "reading": "ほんやく", "meaning": "번역", "description": "어떤 나라의 말을 다른 나라의 말로 뒤집어(翻) 바꾸는(訳) 일입니다." }
    ]
  },
  {
    "kanji": "詞",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "말씀 (글)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 글을 의미합니다." },
      { "char": "司", "role": "맡을 사 (요소)", "desc": "맡아서 한다는 뜻과 발음 '사/시'를 줍니다." }
    ],
    "story": "자기의 뜻을 윗사람이나 남에게 맡아서(司) 올리는 글이나 '말씀', 혹은 시나 노래의 가사인 '사'를 뜻합니다.",
    "example_words": [
      { "word": "作詞", "reading": "さくし", "meaning": "작사", "description": "노래에 맞추어 부를 가사나 말(詞)을 짓는(作) 일입니다." },
      { "word": "名詞", "reading": "めいし", "meaning": "명사", "description": "사물의 이름(名)을 나타내는 말(詞)이나 품사입니다." }
    ]
  },
  {
    "kanji": "誌",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "기록할 (잡지)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 글을 뜻합니다." },
      { "char": "志", "role": "뜻 지 (요소)", "desc": "마음이나 뜻이라는 의미와 발음 '지/시'를 줍니다." }
    ],
    "story": "마음속에 품은 뜻(志)을 잊지 않기 위해 글(言)로 남겨 '기록하다' 혹은 여러 가지 글을 모아 엮은 책인 '잡지'를 의미합니다.",
    "example_words": [
      { "word": "雑誌", "reading": "ざっし", "meaning": "잡지", "description": "여러 가지 섞인(雑) 글들을 모아 기록하여(誌) 펴내는 정기 간행물입니다." },
      { "word": "日誌", "reading": "にっし", "meaning": "일지", "description": "날(日)마다 겪은 일이나 업무를 기록한(誌) 장부입니다." }
    ]
  },
  {
    "kanji": "認",
    "reading_on": "ニン",
    "reading_kun": "みと(める)",
    "meaning": "알 (인정할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 의미합니다." },
      { "char": "忍", "role": "참을 인 (요소)", "desc": "참고 새긴다는 뜻과 발음 '인/닌'을 줍니다." }
    ],
    "story": "상대방의 말이나 행동을 참을성 있게(忍) 듣고(言) 사실을 똑똑히 알아차려 '알다(인식하다)' 혹은 '인정하다'는 뜻입니다.",
    "example_words": [
      { "word": "認める", "reading": "みとめる", "meaning": "인정하다, 알아보다", "description": "사실이 틀림없다고 받아들이거나, 눈으로 보아 알아채는 것입니다." },
      { "word": "確認", "reading": "かくにん", "meaning": "확인", "description": "틀림이 없는지 확실히(確) 알아보는(認) 일입니다." }
    ]
  },
  {
    "kanji": "誕",
    "reading_on": "タン",
    "reading_kun": "",
    "meaning": "낳을",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 소리를 뜻합니다." },
      { "char": "延", "role": "늘일 연 (요소)", "desc": "길게 이어진다는 뜻과 발음 '연/탄'의 변형 역할을 합니다." }
    ],
    "story": "어머니의 뱃속에서 생명이 길게 이어져(延) 큰 울음소리(言)를 내며 세상에 태어나는 '탄생(낳다)'을 의미합니다.",
    "example_words": [
      { "word": "誕生", "reading": "たんじょう", "meaning": "탄생", "description": "아이가 태어나서(誕) 생명(生)을 얻는 일이나, 사물이 새로 생겨나는 것입니다." },
      { "word": "誕生日", "reading": "たんじょうび", "meaning": "생일", "description": "세상에 태어난(誕生) 날(日)입니다." }
    ]
  },
  {
    "kanji": "誠",
    "reading_on": "セイ",
    "reading_kun": "まこと",
    "meaning": "정성 (참)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "成", "role": "이룰 성 (요소)", "desc": "완성하거나 이룬다는 뜻과 발음 '성/세이'를 줍니다." }
    ],
    "story": "자기가 뱉은 말(言)을 거짓 없이 꼭 이루어(成) 내는 진실한 마음, 즉 '정성'이나 '참(진실)'을 뜻합니다.",
    "example_words": [
      { "word": "誠", "reading": "まこと", "meaning": "진실, 정성", "description": "거짓이 없는 참된 마음이나 진실입니다." },
      { "word": "誠実", "reading": "せいじつ", "meaning": "성실", "description": "정성스럽고(誠) 참되어(実) 거짓이 없는 태도입니다." }
    ]
  },
  {
    "kanji": "誤",
    "reading_on": "ゴ",
    "reading_kun": "あやま(る)",
    "meaning": "그르칠 (잘못)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 행동을 뜻합니다." },
      { "char": "呉", "role": "나라 오 (요소)", "desc": "소리를 크게 낸다는 뜻이나, 여기서는 발음 '오/고'를 줍니다." }
    ],
    "story": "생각이 부족하여 엉뚱하게 큰 소리(呉)를 내며 말(言)을 실수하여, 일을 '그르치다' 혹은 '잘못'을 저지른다는 뜻입니다.",
    "example_words": [
      { "word": "誤る", "reading": "あやまる", "meaning": "그르치다, 틀리다", "description": "잘못하여 실수하거나 틀리는 것입니다." },
      { "word": "誤解", "reading": "ごかい", "meaning": "오해", "description": "사실과 다르게 잘못(誤) 풀어서 해석하는(解) 것입니다." }
    ]
  },
  {
    "kanji": "論",
    "reading_on": "ロン",
    "reading_kun": "",
    "meaning": "논할",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 주장하는 것을 뜻합니다." },
      { "char": "侖", "role": "둥글 륜 (요소)", "desc": "둥글게 모여서 생각의 조리를 세운다는 뜻과 발음 '륜/론'을 줍니다." }
    ],
    "story": "여러 사람이 둥글게 모여 앉아(侖) 어떤 문제에 대해 이치에 맞게 말(言)로 따져서 '논하다(토의하다)'는 뜻입니다.",
    "example_words": [
      { "word": "議論", "reading": "ぎろん", "meaning": "의논", "description": "어떤 문제에 대해 서로 의견을 말하며(議) 따져 논하는(論) 일입니다." },
      { "word": "論文", "reading": "ろんぶん", "meaning": "논문", "description": "연구한 내용이나 주장을 조리 있게 논하여(論) 적은 글(文)입니다." }
    ]
  },
  {
    "kanji": "諸",
    "reading_on": "ショ",
    "reading_kun": "",
    "meaning": "모든 (제)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "者", "role": "놈 자 (요소)", "desc": "여럿이 모여 있다는 뜻과 발음 '자/쇼'의 변형 역할을 합니다." }
    ],
    "story": "수많은 사람들(者)이 모여 여러 가지 말(言)을 한다는 데서, 여러 개가 모인 '모든'이나 '여러(제)'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "諸君", "reading": "しょくん", "meaning": "제군, 여러분", "description": "자신과 같거나 아랫사람인 여러(諸) 사람(君)들을 부르는 말입니다." },
      { "word": "諸国", "reading": "しょこく", "meaning": "제국, 여러 나라", "description": "세계의 여러(諸) 나라(国)들입니다." }
    ]
  },
  {
    "kanji": "警",
    "reading_on": "ケイ",
    "reading_kun": "",
    "meaning": "경계할",
    "components": [
      { "char": "敬", "role": "공경할 경 (요소)", "desc": "몸가짐을 삼가고 조심한다는 뜻과 발음 '경/케이'를 줍니다." },
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 소리를 뜻합니다." }
    ],
    "story": "몸가짐을 조심하며(敬) 남이 함부로 침범하지 못하도록 말이나 소리(言)로 훈계하고 미리 '경계하다'는 의미입니다.",
    "example_words": [
      { "word": "警察", "reading": "けいさつ", "meaning": "경찰", "description": "범죄를 경계하여(警) 살피고(察) 막는 기관이나 사람입니다." },
      { "word": "警告", "reading": "けいこく", "meaning": "경고", "description": "조심하고 경계하도록(警) 미리 알리는(告) 일입니다." }
    ]
  },
  {
    "kanji": "貴",
    "reading_on": "キ",
    "reading_kun": "たっと(い)、とうと(い)、たっと(ぶ)、とうと(ぶ)",
    "meaning": "귀할",
    "components": [
      { "char": "𠀐", "role": "두손으로받들 궤 변형 (요소)", "desc": "두 손으로 귀한 물건을 떠받드는 모양을 나타냅니다. (위쪽 부분)" },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "보물이나 재물을 뜻합니다." }
    ],
    "story": "두 손으로 소중하게 떠받들어야(𠀐 변형) 할 만큼 가치가 높은 조개나 재물(貝)처럼, 신분이나 물건이 '귀하다(소중하다)'는 뜻입니다.",
    "example_words": [
      { "word": "貴い", "reading": "とうとい", "meaning": "귀중하다, 훌륭하다", "description": "신분이나 가치가 높아서 매우 소중하고 훌륭한 상태입니다." },
      { "word": "貴重", "reading": "きちょう", "meaning": "귀중", "description": "매우 귀하고(貴) 소중한(重) 모양입니다." }
    ]
  },
  {
    "kanji": "賃",
    "reading_on": "チン",
    "reading_kun": "",
    "meaning": "품삯",
    "components": [
      { "char": "任", "role": "맡길 임 (요소)", "desc": "일을 맡아 한다는 뜻과 발음 '임/친'의 변형 역할을 합니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 뜻합니다." }
    ],
    "story": "남에게 일을 맡기고(任) 그 대가로 지불하는 돈(貝), 즉 노동의 대가인 '품삯'이나 삯을 의미합니다.",
    "example_words": [
      { "word": "家賃", "reading": "やちん", "meaning": "집세", "description": "남의 집(家)이나 방을 빌려 쓰는 대가로 내는 돈(賃)입니다." },
      { "word": "賃金", "reading": "ちんぎん", "meaning": "임금, 품삯", "description": "노동을 한 대가로 일한 사람에게 주는 돈(賃, 金)입니다." }
    ]
  },
  {
    "kanji": "遺",
    "reading_on": "イ、ユイ",
    "reading_kun": "",
    "meaning": "남길",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아감을 뜻합니다." },
      { "char": "貴", "role": "귀할 귀 (요소)", "desc": "귀중하다는 뜻과 발음 '귀/이'의 변형 역할을 합니다." }
    ],
    "story": "먼 길을 떠나거나(辶) 죽을 때 후손들을 위해 귀중한(貴) 물건을 뒤에 '남기다' 혹은 물려준다는 뜻을 가집니다.",
    "example_words": [
      { "word": "遺産", "reading": "いさん", "meaning": "유산", "description": "죽은 사람이 뒤에 남겨(遺) 놓은 재산(産)입니다." },
      { "word": "遺跡", "reading": "いせき", "meaning": "유적", "description": "옛사람들이 남긴(遺) 건물이나 삶의 자취(跡)입니다." }
    ]
  },
  {
    "kanji": "郵",
    "reading_on": "ユウ",
    "reading_kun": "",
    "meaning": "우편 (역참)",
    "components": [
      { "char": "垂", "role": "드리울 수 (요소)", "desc": "멀리 변방까지 내려간다는 뜻과 발음 '수/유우'의 변형 역할을 합니다." },
      { "char": "阝", "role": "우부방 (부수)", "desc": "고을이나 마을(역참)을 뜻합니다." }
    ],
    "story": "변방(垂)이나 먼 마을(阝)까지 물건이나 편지를 말을 타고 전달하던 옛날의 역참에서 유래하여, 지금은 '우편'이나 우체국을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "郵便", "reading": "ゆうびん", "meaning": "우편", "description": "편지나 소포 등을 역참(郵)을 통해 편리하게(便) 전달해 주는 제도입니다." },
      { "word": "郵便局", "reading": "ゆうびんきょく", "meaning": "우체국", "description": "우편(郵便) 업무를 맡아보는 곳(局)입니다." }
    ]
  },
  {
    "kanji": "郷",
    "reading_on": "キョウ、ゴウ",
    "reading_kun": "さと",
    "meaning": "시골 (고향)",
    "components": [
      { "char": "郷", "role": "고을 향 (부수)", "desc": "두 사람이 밥그릇을 마주하고 밥을 먹는 모양에서, 같은 고을에 모여 사는 사람들을 나타냅니다." }
    ],
    "story": "마을 사람들이 그릇을 마주 놓고 함께 밥을 먹을 정도로 가까이 모여 사는 친근한 동네, 즉 자기가 태어난 '고향'이나 '시골'을 의미합니다.",
    "example_words": [
      { "word": "故郷", "reading": "こきょう", "meaning": "고향", "description": "자기가 태어나서 자란 옛(故) 마을이나 시골(郷)입니다." },
      { "word": "郷土", "reading": "きょうど", "meaning": "향토", "description": "태어나서 자란 고향(郷)의 땅(土)이나 그 지방입니다." }
    ]
  },
  {
    "kanji": "針",
    "reading_on": "シン",
    "reading_kun": "はり",
    "meaning": "바늘",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 금속을 의미합니다." },
      { "char": "十", "role": "열 十 (요소)", "desc": "원래 뾰족하게 찌른다는 뜻을 가진 咸(다 함)의 변형으로, 끝이 뾰족함을 나타냅니다." }
    ],
    "story": "쇠(金)를 가늘게 깎고 끝을 열 십(十)자 모양처럼 뾰족하게 갈아서 옷을 꿰맬 때 쓰는 '바늘'이나 침을 뜻합니다.",
    "example_words": [
      { "word": "針", "reading": "はり", "meaning": "바늘, 침", "description": "옷을 꿰매거나 시계를 가리키는 뾰족한 물건입니다." },
      { "word": "方針", "reading": "ほうしん", "meaning": "방침", "description": "나아갈 방향(方)을 가리키는 나침반의 바늘(針)처럼, 일의 방향입니다." }
    ]
  },
  {
    "kanji": "鋼",
    "reading_on": "コウ",
    "reading_kun": "はがね",
    "meaning": "강철",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 금속을 뜻합니다." },
      { "char": "岡", "role": "산등성이 강 (요소)", "desc": "산등성이처럼 단단하고 굳세다는 뜻과 발음 '강/코우'를 줍니다." }
    ],
    "story": "산등성이(岡)처럼 몹시 굳세고 단단하게 제련한 쇠붙이(金)인 '강철'을 의미합니다.",
    "example_words": [
      { "word": "鋼", "reading": "はがね", "meaning": "강철", "description": "아주 단단하게 만든 쇠로, 칼이나 기계를 만드는 데 씁니다." },
      { "word": "鉄鋼", "reading": "てっこう", "meaning": "철강", "description": "단단한 쇠(鉄)와 강철(鋼)을 아울러 이르는 말입니다." }
    ]
  },
  {
    "kanji": "閉",
    "reading_on": "ヘイ",
    "reading_kun": "と(じる)、と(ざす)、し(める)、し(まる)",
    "meaning": "닫을",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "문이나 출입구를 뜻합니다." },
      { "char": "才", "role": "재주 재 (요소)", "desc": "여기서는 문을 잠그는 빗장의 모양(원래 𠂇의 변형)으로 꽉 막는다는 뜻을 줍니다." }
    ],
    "story": "문(門)을 나무 빗장이나 자물쇠(才 변형)로 꽉 걸어 잠가서 열리지 않게 '닫다' 혹은 막는다는 의미입니다.",
    "example_words": [
      { "word": "閉める", "reading": "しめる", "meaning": "닫다", "description": "열려 있는 문이나 창문 등을 막아 닫히게 하는 것입니다." },
      { "word": "閉じる", "reading": "とじる", "meaning": "닫다, 눈을 감다", "description": "문이나 눈, 뚜껑 등을 닫거나 덮는 것입니다." }
    ]
  },
  {
    "kanji": "閣",
    "reading_on": "カク",
    "reading_kun": "",
    "meaning": "문설주 (누각)",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "문이나 건물을 뜻합니다." },
      { "char": "各", "role": "각각 각 (요소)", "desc": "따로 떨어져 있다는 뜻과 발음 '각/카쿠'를 줍니다." }
    ],
    "story": "문의 양옆에 따로따로(各) 세워 둔 문(門)설주라는 뜻에서, 나중에는 높게 지어 사방을 볼 수 있게 만든 크고 화려한 집인 '누각'이나 정부의 내각을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "内閣", "reading": "ないかく", "meaning": "내각", "description": "국가의 행정을 맡아보는 정부의 우두머리들이 모인 기관(閣)입니다." },
      { "word": "金閣寺", "reading": "きんかくじ", "meaning": "금각사 (킨카쿠지)", "description": "일본 교토에 있는 금박을 입힌 누각(閣)이 있는 유명한 절입니다." }
    ]
  },
  {
    "kanji": "降",
    "reading_on": "コウ",
    "reading_kun": "お(りる)、お(ろす)、ふ(る)",
    "meaning": "내릴 (항복할)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 산을 뜻합니다." },
      { "char": "夅", "role": "내릴 강 (요소)", "desc": "두 발(舛)을 아래로 향해 걷는다는 뜻과 발음 '강/코우'를 줍니다." }
    ],
    "story": "가파른 언덕(阝)에서 두 발을 내디뎌 아래로 향해 걷는다(夅)는 데서, 위에서 아래로 떨어져 '내리다(눈/비가 오다)' 혹은 머리를 숙여 '항복하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "降りる", "reading": "おりる", "meaning": "내리다", "description": "차나 계단 등 높은 곳에서 아래쪽으로 옮겨 가는 것입니다." },
      { "word": "降る", "reading": "ふる", "meaning": "내리다, (비가) 오다", "description": "하늘에서 비나 눈 따위가 땅으로 떨어져 내리는 것입니다." }
    ]
  },
  {
    "kanji": "陛",
    "reading_on": "ヘイ",
    "reading_kun": "",
    "meaning": "섬돌",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 층계를 뜻합니다." },
      { "char": "坒", "role": "나란할 비 (요소)", "desc": "계단이 나란히 이어져 있다는 뜻과 발음 '비/헤이'의 변형 역할을 합니다." }
    ],
    "story": "언덕(阝)처럼 높이 나란히(坒) 쌓아 만든 궁궐의 '섬돌(계단)'을 뜻하며, 이 계단 위에 계신 분이라는 뜻에서 임금을 높여 부르는 말(폐하)로 쓰입니다.",
    "example_words": [
      { "word": "陛下", "reading": "へいか", "meaning": "폐하", "description": "섬돌(陛) 아래(下)에서 뵙는다는 뜻으로, 황제나 천황을 높여 부르는 말입니다." },
      { "word": "天皇陛下", "reading": "てんのうへいか", "meaning": "천황 폐하", "description": "일본의 천황을 아주 높여 부르는 말입니다." }
    ]
  },
  {
    "kanji": "除",
    "reading_on": "ジョ、ジ",
    "reading_kun": "のぞ(く)",
    "meaning": "덜 (없앨)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 계단을 뜻합니다." },
      { "char": "余", "role": "나 여 (요소)", "desc": "넉넉하여 남는다는 뜻과 발음 '여/조'를 줍니다." }
    ],
    "story": "언덕(阝)이나 밭에서 쓸데없이 남는(余) 흙이나 잡초를 깎아내어 '없애다', 혹은 수량에서 '덜다(빼다)'는 뜻입니다.",
    "example_words": [
      { "word": "除く", "reading": "のぞく", "meaning": "없애다, 빼다", "description": "불필요한 것을 치우거나, 전체에서 어떤 것을 빼내는 것입니다." },
      { "word": "掃除", "reading": "そうじ", "meaning": "청소", "description": "더러운 것을 쓸고(掃) 없애어(除) 깨끗하게 하는 일입니다." }
    ]
  },
  {
    "kanji": "障",
    "reading_on": "ショウ",
    "reading_kun": "さわ(る)",
    "meaning": "막을",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 장애물을 뜻합니다." },
      { "char": "章", "role": "글장 장 (요소)", "desc": "가리거나 덮는다는 뜻과 발음 '장/쇼우'를 줍니다." }
    ],
    "story": "언덕(阝)처럼 앞을 가로막아(章) 덮어서 나아가지 못하게 '막다', 혹은 일의 진행을 가로막는 '장애물'을 뜻합니다.",
    "example_words": [
      { "word": "障子", "reading": "しょうじ", "meaning": "장지문 (쇼지)", "description": "나무틀에 얇은 종이를 발라 방을 가리고 막는(障) 일본식 미닫이문입니다." },
      { "word": "障害", "reading": "しょうがい", "meaning": "장애", "description": "어떤 일을 하는 데 막히고(障) 방해가 되어 해(害)가 되는 것입니다." }
    ]
  },
  {
    "kanji": "難",
    "reading_on": "ナン",
    "reading_kun": "むずか(しい)、かた(い)",
    "meaning": "어려울",
    "components": [
      { "char": "𦰩", "role": "진흙 근 변형 (요소)", "desc": "진흙이나 불에 타서 가물었다는 뜻으로 고생스럽다는 의미를 줍니다." },
      { "char": "隹", "role": "새 추 (부수)", "desc": "새를 의미합니다." }
    ],
    "story": "가뭄이나 진흙(𦰩 변형) 속에서 새(隹)가 먹이를 구하려 날갯짓하기가 몹시 괴롭고 '어렵다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "難しい", "reading": "むずかしい", "meaning": "어렵다", "description": "일이나 문제 따위를 이해하거나 해결하기가 힘들고 까다로운 것입니다." },
      { "word": "困難", "reading": "こんなん", "meaning": "곤란", "description": "일이 꼬여서 괴롭고(困) 해내기 어려운(難) 상태입니다." }
    ]
  },
  {
    "kanji": "革",
    "reading_on": "カク",
    "reading_kun": "かわ",
    "meaning": "가죽",
    "components": [
      { "char": "革", "role": "가죽 혁 (부수)", "desc": "짐승의 털을 뽑고 가죽을 팽팽하게 벗겨 낸 모양을 본뜬 글자입니다." }
    ],
    "story": "짐승의 털을 벗겨 내고 다듬어서 만든 부드러운 '가죽'을 뜻하며, 낡은 것을 벗겨 내고 새롭게 '고치다(혁신하다)'는 의미도 가집니다.",
    "example_words": [
      { "word": "革", "reading": "かわ", "meaning": "가죽", "description": "동물의 피부를 다듬어 구두나 가방을 만들 수 있게 한 것입니다." },
      { "word": "革命", "reading": "かくめい", "meaning": "혁명", "description": "낡은 제도를 가죽을 벗기듯 완전히 고치고(革) 운명(命)을 뒤집는 일입니다." }
    ]
  },
  {
    "kanji": "頂",
    "reading_on": "チョウ",
    "reading_kun": "いただ(く)、いただき",
    "meaning": "정수리",
    "components": [
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "원래 못의 머리 모양으로 맨 위라는 뜻과 발음 '정/초우'를 줍니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "머리나 사람을 의미합니다." }
    ],
    "story": "사람의 머리(頁) 중 가장 윗부분에 있는 '정수리'나 산의 꼭대기를 뜻하며, 머리 위로 '받들다' 혹은 음식을 '받다(먹다)'는 뜻으로 쓰입니다.",
    "example_words": [
      { "word": "頂く", "reading": "いただく", "meaning": "받다, 먹다 (겸양어)", "description": "남에게서 물건이나 음식을 감사히 받거나 먹는 것을 낮추어 이르는 말입니다." },
      { "word": "頂点", "reading": "ちょうてん", "meaning": "정점", "description": "산이나 물건의 맨 꼭대기(頂)가 되는 점(点)이나 최고조입니다." }
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

print("Grade 6 Part 6 data appended successfully.")
