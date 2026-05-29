import json
import os

new_data = [
  {
    "kanji": "借",
    "reading_on": "シャク",
    "reading_kun": "か(りる)",
    "meaning": "빌릴",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "昔", "role": "예 석 (요소)", "desc": "옛날이나 지나간 일이라는 뜻과 발음 '석/샤쿠'를 줍니다." }
    ],
    "story": "옛날(昔)부터 알고 지내던 친한 사람(亻)에게 물건이나 돈을 '빌리다(차용하다)'라는 의미입니다.",
    "example_words": [
      { "word": "借りる", "reading": "かりる", "meaning": "빌리다", "description": "남의 물건이나 돈을 나중에 돌려주기로 하고 가져다 쓰는 것입니다." },
      { "word": "借金", "reading": "しゃっきん", "meaning": "빚", "description": "남에게 빌린(借) 돈(金)입니다." }
    ]
  },
  {
    "kanji": "種",
    "reading_on": "シュ",
    "reading_kun": "たね",
    "meaning": "씨",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 식물을 의미합니다." },
      { "char": "重", "role": "무거울 중 (요소)", "desc": "무겁다, 크다는 뜻과 함께 겹겹이 쌓인다는 뜻을 줍니다." }
    ],
    "story": "곡식(禾) 중에서 무겁고(重) 튼실한 것을 잘 골라내어 다음 농사를 위해 남겨둔 '씨앗'이나 '종류'를 뜻합니다.",
    "example_words": [
      { "word": "種", "reading": "たね", "meaning": "씨앗, 종류", "description": "식물이 싹을 틔우기 위한 씨앗이나 사물의 원인입니다." },
      { "word": "種類", "reading": "しゅるい", "meaning": "종류", "description": "비슷한 특징을 가진 것끼리 나눈 갈래(種)나 무리(類)입니다." }
    ]
  },
  {
    "kanji": "周",
    "reading_on": "シュウ",
    "reading_kun": "まわ(り)",
    "meaning": "두루",
    "components": [
      { "char": "冂", "role": "멀 경 (요소)", "desc": "사방을 둘러싼 경계나 테두리를 뜻합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 구멍, 밭을 의미합니다." },
      { "char": "土", "role": "흙 토 (요소)", "desc": "가운데 있는 흙이나 밭두둑을 뜻합니다." }
    ],
    "story": "밭(口와 土) 주변으로 경계선(冂)을 빙 둘러친 모습에서, 빈틈없이 '두루 미치다' 혹은 둘레를 빙 도는 '주위'를 뜻합니다.",
    "example_words": [
      { "word": "周り", "reading": "まわり", "meaning": "주위, 둘레", "description": "사물의 바깥쪽 둘레나 근처입니다." },
      { "word": "周囲", "reading": "しゅうい", "meaning": "주위", "description": "어떤 것의 바깥 둘레(周)와 그것을 에워싼(囲) 곳입니다." }
    ]
  },
  {
    "kanji": "祝",
    "reading_on": "シュク",
    "reading_kun": "いわ(う)",
    "meaning": "빌 (축하할)",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "제단이나 신에게 비는 모습을 뜻합니다." },
      { "char": "兄", "role": "맏 형 (요소)", "desc": "사람이 입을 크게 벌리고 말하는 모습을 나타냅니다." }
    ],
    "story": "제단(示) 앞에 꿇어앉아 입을 열고(兄의 원뜻) 신에게 복을 내려달라고 '빌다' 혹은 기쁜 일을 '축하하다'는 뜻입니다.",
    "example_words": [
      { "word": "祝う", "reading": "いわう", "meaning": "축하하다", "description": "좋은 일을 기뻐하며 인사를 차리는 것입니다." },
      { "word": "祝福", "reading": "しゅくふく", "meaning": "축복", "description": "행복하기를 빌어(祝) 주고 복(福)을 내리는 일입니다." }
    ]
  },
  {
    "kanji": "順",
    "reading_on": "ジュン",
    "reading_kun": "",
    "meaning": "순할 (차례)",
    "components": [
      { "char": "川", "role": "내 천 (요소)", "desc": "물이 위에서 아래로 순리대로 흐르는 모습을 뜻합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "사람의 머리나 얼굴을 의미합니다." }
    ],
    "story": "사람(頁)이 흐르는 강물(川)을 거스르지 않고 자연의 이치에 순응하여 따른다는 데서 성격이 '순하다' 혹은 차례대로 이어지는 '순서'를 뜻합니다.",
    "example_words": [
      { "word": "順番", "reading": "じゅんばん", "meaning": "순번, 차례", "description": "순서(順)대로 돌아오는 차례(番)입니다." },
      { "word": "順調", "reading": "じゅんちょう", "meaning": "순조", "description": "일이 아무 탈 없이 순순히(順) 잘 조절되어(調) 나아가는 상태입니다." }
    ]
  },
  {
    "kanji": "初",
    "reading_on": "ショ",
    "reading_kun": "はじ(め)、はじ(めて)、はつ、そ(める)",
    "meaning": "처음",
    "components": [
      { "char": "衤", "role": "옷의변 (부수)", "desc": "옷감이나 옷을 의미합니다." },
      { "char": "刀", "role": "칼 도 (요소)", "desc": "칼이나 가위로 자르는 동작을 뜻합니다." }
    ],
    "story": "옷(衤)을 짓기 위해 가장 먼저 가위(刀)로 천을 마름질하고 자르는 일에서, 일의 맨 '처음'이나 '시작'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "初めて", "reading": "はじめて", "meaning": "처음으로", "description": "이제까지 한 번도 없었던 일이 처음 일어나는 모양입니다." },
      { "word": "最初", "reading": "さいしょ", "meaning": "최초, 맨 처음", "description": "가장(最) 앞선 처음(初)입니다." }
    ]
  },
  {
    "kanji": "松",
    "reading_on": "ショウ",
    "reading_kun": "まつ",
    "meaning": "소나무",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "公", "role": "공평할 공 (요소)", "desc": "널리 드러나다, 공평하다는 뜻과 발음 '공/쇼우'를 줍니다." }
    ],
    "story": "항상 푸른 잎을 지니고 있어 누구에게나 널리(公) 훌륭한 자태를 드러내는 으뜸가는 나무(木), 즉 '소나무'를 의미합니다.",
    "example_words": [
      { "word": "松", "reading": "まつ", "meaning": "소나무", "description": "사철 푸른 바늘잎을 가진 소나뭇과의 식물입니다." },
      { "word": "門松", "reading": "かどまつ", "meaning": "카도마츠", "description": "새해에 복을 부르기 위해 대문(門) 앞에 장식하는 소나무(松)입니다." }
    ]
  },
  {
    "kanji": "笑",
    "reading_on": "ショウ",
    "reading_kun": "わら(う)、え(む)",
    "meaning": "웃을",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "원래 夭(어릴 요)가 변형된 것으로, 몸을 구부린 사람을 뜻합니다." },
      { "char": "夭", "role": "어릴 요 (요소)", "desc": "여기서는 개가 꼬리를 흔드는 모습이거나 사람의 머리 모양입니다." }
    ],
    "story": "사람이 기뻐서 허리를 굽히고(夭) 활짝 '웃는' 모습을 본뜬 글자로, 나중에 윗부분이 대죽(竹)으로 변형되었습니다.",
    "example_words": [
      { "word": "笑う", "reading": "わらう", "meaning": "웃다", "description": "기쁘거나 즐거워 얼굴에 미소를 띠고 소리를 내는 것입니다." },
      { "word": "笑顔", "reading": "えがお", "meaning": "웃는 얼굴", "description": "기뻐서 활짝 웃는(笑) 얼굴(顔)입니다." }
    ]
  },
  {
    "kanji": "唱",
    "reading_on": "ショウ",
    "reading_kun": "とな(える)",
    "meaning": "부를",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "입으로 소리를 내거나 노래하는 것을 뜻합니다." },
      { "char": "昌", "role": "창성할 창 (요소)", "desc": "해(日)처럼 밝고 분명하다는 뜻과 발음 '창/쇼우'를 줍니다." }
    ],
    "story": "여러 사람 앞에서 입(口)을 열고 의견이나 노래를 밝고 분명하게(昌) 소리 내어 '부르다' 혹은 주장한다는 뜻입니다.",
    "example_words": [
      { "word": "唱える", "reading": "となえる", "meaning": "소리 내어 읽다, 주장하다", "description": "큰 소리로 부르거나 자기 의견을 강하게 내세우는 것입니다." },
      { "word": "合唱", "reading": "がっしょう", "meaning": "합창", "description": "여러 사람이 함께 호흡을 합쳐(合) 노래를 부르는(唱) 일입니다." }
    ]
  },
  {
    "kanji": "焼",
    "reading_on": "ショウ",
    "reading_kun": "や(く)、や(ける)",
    "meaning": "태울 / 구울",
    "components": [
      { "char": "火", "role": "불 화 (부수)", "desc": "불이나 열기를 뜻합니다." },
      { "char": "尭", "role": "요임금 요 (요소)", "desc": "높이 솟아오른다는 뜻과 발음 '요/쇼우'를 담당합니다." }
    ],
    "story": "불(火)이 높이(尭) 솟아오르며 물건을 활활 '태우다' 혹은 음식을 '굽다'는 의미입니다.",
    "example_words": [
      { "word": "焼く", "reading": "やく", "meaning": "굽다, 태う다", "description": "불에 익혀 먹거나 불을 붙여 타게 하는 것입니다." },
      { "word": "夕焼け", "reading": "ゆうやけ", "meaning": "저녁놀", "description": "해 질 녘(夕) 하늘이 불타듯(焼け) 붉게 물드는 현상입니다." }
    ]
  },
  {
    "kanji": "象",
    "reading_on": "ショウ、ゾウ",
    "reading_kun": "",
    "meaning": "코끼리 / 모양",
    "components": [
      { "char": "象", "role": "코끼리 상 (부수)", "desc": "긴 코와 큰 귀, 굵은 다리를 가진 코끼리의 옆모습을 본뜬 글자입니다." }
    ],
    "story": "살아있는 거대한 짐승인 '코끼리'를 본떠 만들었으나, 나중에는 보이지 않는 것을 본뜬 모습이나 사물의 형태인 '모양(상)'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "象", "reading": "ぞう", "meaning": "코끼리", "description": "코가 길고 덩치가 큰 포유동물입니다." },
      { "word": "印象", "reading": "いんしょう", "meaning": "인상", "description": "마음속에 새겨진(印) 어떤 대상의 모양(象)이나 느낌입니다." }
    ]
  },
  {
    "kanji": "照",
    "reading_on": "ショウ",
    "reading_kun": "て(る)、て(らす)、て(れる)",
    "meaning": "비칠",
    "components": [
      { "char": "昭", "role": "밝을 소 (요소)", "desc": "햇빛이 밝게 퍼진다는 뜻과 발음 '소/쇼우'를 줍니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불이나 열기를 뜻합니다." }
    ],
    "story": "불(灬)을 피워 주위를 환하고 밝게(昭) '비추다' 혹은 빛이 사물에 '반사되다'는 의미입니다.",
    "example_words": [
      { "word": "照らす", "reading": "てらす", "meaning": "비추다", "description": "빛을 내어 어두운 곳을 밝게 하는 것입니다." },
      { "word": "照明", "reading": "しょうめい", "meaning": "조명", "description": "빛을 비추어(照) 밝게(明) 하는 장치입니다." }
    ]
  },
  {
    "kanji": "賞",
    "reading_on": "ショウ",
    "reading_kun": "",
    "meaning": "상줄",
    "components": [
      { "char": "尚", "role": "오히려 상 (요소)", "desc": "높이다, 더한다는 뜻과 발음 '상/쇼우'를 담당합니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "재물이나 돈을 뜻합니다." }
    ],
    "story": "공을 세운 사람에게 그 가치를 높이 사서(尚) 재물이나 상금(貝)을 내려 '상 주다' 혹은 '기리다'는 뜻입니다.",
    "example_words": [
      { "word": "賞品", "reading": "しょうひん", "meaning": "상품", "description": "상(賞)으로 주는 물건(品)입니다." },
      { "word": "受賞", "reading": "じゅしょう", "meaning": "수상", "description": "뛰어난 업적으로 상(賞)을 받는(受) 일입니다." }
    ]
  },
  {
    "kanji": "臣",
    "reading_on": "シン、ジン",
    "reading_kun": "",
    "meaning": "신하",
    "components": [
      { "char": "臣", "role": "신하 신 (부수)", "desc": "사람이 엎드려 머리를 조아릴 때 눈을 치켜뜨고 임금을 우러러보는 눈 모양을 본뜬 글자입니다." }
    ],
    "story": "고개를 숙이고 눈만 치켜떠서 조심스럽게 임금을 우러러보는 사람, 즉 충성스러운 '신하'를 뜻합니다.",
    "example_words": [
      { "word": "大臣", "reading": "だいじん", "meaning": "대신, 장관", "description": "국가를 다스리는 부서의 우두머리가 되는 큰(大) 신하(臣)입니다." },
      { "word": "家臣", "reading": "かしん", "meaning": "가신", "description": "한 집안이나 무사를 모시는 신하(臣)입니다." }
    ]
  },
  {
    "kanji": "信",
    "reading_on": "シン",
    "reading_kun": "",
    "meaning": "믿을",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "言", "role": "말씀 언 (요소)", "desc": "말이나 약속을 뜻합니다." }
    ],
    "story": "사람(亻)이 한 말(言)이나 약속은 겉과 속이 일치하여 참되어야 하므로 '믿다' 혹은 믿음을 주는 '편지(소식)'라는 뜻이 되었습니다.",
    "example_words": [
      { "word": "信用", "reading": "しんよう", "meaning": "신용", "description": "사람이나 사물을 믿고(信) 쓰는(用) 마음입니다." },
      { "word": "自信", "reading": "じしん", "meaning": "자신", "description": "자기 자신(自)의 능력이나 가치를 믿는(信) 마음입니다." }
    ]
  },
  {
    "kanji": "成",
    "reading_on": "セイ、ジョウ",
    "reading_kun": "な(る)、な(す)",
    "meaning": "이룰",
    "components": [
      { "char": "戊", "role": "창 모 (요소)", "desc": "창이나 무기를 뜻합니다." },
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "못을 뜻하며 여기서는 물건을 단단히 고정함을 의미합니다." }
    ],
    "story": "무기(戊)를 들고 적을 평정하거나, 무기를 완성하여 못(丁)을 박아 단단히 고정함으로써 일을 끝까지 '이루다(완성하다)'는 뜻입니다.",
    "example_words": [
      { "word": "成功", "reading": "せいこう", "meaning": "성공", "description": "목적한 바를 이루어(成) 공(功)을 세우는 일입니다." },
      { "word": "成長", "reading": "せいちょう", "meaning": "성장", "description": "사람이나 동식물이 이루어지고(成) 자라나는(長) 것입니다." }
    ]
  },
  {
    "kanji": "省",
    "reading_on": "セイ、ショウ",
    "reading_kun": "かえり(みる)、はぶ(く)",
    "meaning": "살필 (관청)",
    "components": [
      { "char": "少", "role": "적을 소 (요소)", "desc": "여기서는 눈을 가늘게 뜨고 본다는 의미나 발음 '소/쇼우'를 줍니다." },
      { "char": "目", "role": "눈 목 (부수)", "desc": "눈으로 자세히 살펴봄을 뜻합니다." }
    ],
    "story": "눈(目)을 가늘게(少) 뜨고 작은 것까지 세심하게 '살피다(반성하다)' 혹은 덜어내어 '생략하다'는 뜻이 되며, 나랏일을 살피는 '관청'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "反省", "reading": "はんせい", "meaning": "반성", "description": "자기의 언행을 뒤집어(反) 스스로 살피는(省) 것입니다." },
      { "word": "省く", "reading": "はぶく", "meaning": "생략하다, 줄이다", "description": "필요 없는 부분을 덜어내어 간단하게 하는 일입니다." }
    ]
  },
  {
    "kanji": "清",
    "reading_on": "セイ、ショウ",
    "reading_kun": "きよ(い)、きよ(まる)、きよ(める)",
    "meaning": "맑을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "青", "role": "푸를 청 (요소)", "desc": "푸르다는 뜻과 발음 '청/세이'를 담당합니다." }
    ],
    "story": "바닥이 투명하게 다 보일 정도로 강물(氵)이 푸르고(青) 깨끗하여 '맑다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "清い", "reading": "きよい", "meaning": "맑다, 깨끗하다", "description": "때나 잡티가 없이 투명하고 맑은 상태입니다." },
      { "word": "清潔", "reading": "せいけつ", "meaning": "청결", "description": "더러움 없이 맑고(清) 깨끗한(潔) 상태입니다." }
    ]
  },
  {
    "kanji": "静",
    "reading_on": "セイ、ジョウ",
    "reading_kun": "しず(か)、しず(まる)、しず(める)",
    "meaning": "고요할",
    "components": [
      { "char": "青", "role": "푸를 청 (부수)", "desc": "푸르다는 뜻과 발음 '청/세이'를 줍니다." },
      { "char": "争", "role": "다툴 쟁 (요소)", "desc": "다투거나 시끄러움을 뜻하나, 이 글자에서는 다툼이 그쳐 평온해짐을 의미합니다." }
    ],
    "story": "푸르고(青) 맑은 하늘 아래 사람들이 다투던(争) 일을 멈추고 평화를 되찾아 아주 '고요하다' 혹은 조용해졌다는 뜻입니다.",
    "example_words": [
      { "word": "静か", "reading": "しずか", "meaning": "조용함, 고요함", "description": "시끄러운 소리나 움직임이 없이 평온한 상태입니다." },
      { "word": "安静", "reading": "あんせい", "meaning": "안정", "description": "몸과 마음을 편안하고(安) 고요하게(静) 하는 일입니다." }
    ]
  },
  {
    "kanji": "席",
    "reading_on": "セキ",
    "reading_kun": "",
    "meaning": "자리",
    "components": [
      { "char": "广", "role": "엄호 (요소)", "desc": "건물이나 지붕 아래의 넓은 장소입니다." },
      { "char": "廿", "role": "스물 입 (요소)", "desc": "여러 개가 모여 있다는 뜻입니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "천이나 깔개를 의미합니다." }
    ],
    "story": "집 안(广)의 넓은 방바닥에 사람들이 앉기 편하도록 여러(廿) 개의 천이나 돗자리(巾)를 깔아놓은 '자리'나 좌석을 뜻합니다.",
    "example_words": [
      { "word": "席", "reading": "せき", "meaning": "자리, 좌석", "description": "사람이 앉도록 마련된 자리입니다." },
      { "word": "出席", "reading": "しゅっせき", "meaning": "출석", "description": "모임이나 수업 등의 자리(席)에 나가는(出) 것입니다." }
    ]
  },
  {
    "kanji": "積",
    "reading_on": "セキ",
    "reading_kun": "つ(む)、つ(もる)",
    "meaning": "쌓을",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 볏짚을 의미합니다." },
      { "char": "責", "role": "꾸짖을 책 (요소)", "desc": "빚을 진다는 뜻에서 유래하여 겹겹이 포개진다는 뜻과 발음 '책/세키'를 줍니다." }
    ],
    "story": "가을에 거둬들인 곡식이나 볏단(禾)을 창고에 포개어(責) 층층이 '쌓다' 혹은 눈이 '쌓이다'는 뜻입니다.",
    "example_words": [
      { "word": "積む", "reading": "つむ", "meaning": "쌓다", "description": "물건을 차곡차곡 위로 겹쳐 올리는 일입니다." },
      { "word": "面積", "reading": "めんせき", "meaning": "면적", "description": "어떤 평면(面)이 넓게 쌓여서(積) 이루는 크기입니다." }
    ]
  },
  {
    "kanji": "折",
    "reading_on": "セツ",
    "reading_kun": "お(る)、お(れる)",
    "meaning": "꺾을",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "斤", "role": "도끼 근 (요소)", "desc": "도끼나 칼로 자른다는 뜻을 의미합니다." }
    ],
    "story": "손(扌)에 도끼(斤)를 들고 나뭇가지 등을 내려쳐서 뚝 '꺾다' 혹은 반으로 '접다'는 의미를 나타냅니다.",
    "example_words": [
      { "word": "折る", "reading": "おる", "meaning": "접다, 꺾다", "description": "종이를 반으로 접거나 길쭉한 물건을 꺾어 부러뜨리는 것입니다." },
      { "word": "骨折", "reading": "こっせつ", "meaning": "골절", "description": "뼈(骨)가 부러지거나 꺾이는(折) 상처입니다." }
    ]
  },
  {
    "kanji": "節",
    "reading_on": "セツ、セチ",
    "reading_kun": "ふし",
    "meaning": "마디 (명절)",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 의미합니다." },
      { "char": "即", "role": "곧 즉 (요소)", "desc": "음식에 다가간다는 뜻에서 나아가 두 가지가 맞닿는 곳이라는 뜻을 줍니다." }
    ],
    "story": "대나무(竹)의 속이 비어 있다가 꽉 차게 맞닿은 톡 불거진 곳인 '마디'를 뜻하며, 계절의 갈라지는 마디인 '명절'이나 '철'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "季節", "reading": "きせつ", "meaning": "계절", "description": "일 년을 기후에 따라 나눈 철(季)의 마디(節)입니다." },
      { "word": "節約", "reading": "せつやく", "meaning": "절약", "description": "씀씀이를 알맞게 마디를 주어(節) 줄이고 맺는(約) 일입니다." }
    ]
  },
  {
    "kanji": "説",
    "reading_on": "セツ",
    "reading_kun": "と(く)",
    "meaning": "말씀 (설명할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 하거나 설명함을 뜻합니다." },
      { "char": "兌", "role": "바꿀 태 (요소)", "desc": "사람의 입술이 기뻐서 열리는 모양으로, 기쁘다 혹은 풀린다는 뜻을 줍니다." }
    ],
    "story": "어렵게 꼬인 문제를 말(言)로 속 시원히 풀어서(兌) 상대방을 알아듣게 '설명하다' 혹은 '타일러 설득하다'는 뜻입니다.",
    "example_words": [
      { "word": "説明", "reading": "せつめい", "meaning": "설명", "description": "어떤 일을 잘 말해서(説) 밝게(明) 알리는 일입니다." },
      { "word": "小説", "reading": "しょうせつ", "meaning": "소설", "description": "작가가 상상력을 더해 꾸며낸 작은(小) 이야기(説)입니다." }
    ]
  },
  {
    "kanji": "浅",
    "reading_on": "セン",
    "reading_kun": "あさ(い)",
    "meaning": "얕을",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 바다, 강을 의미합니다." },
      { "char": "戔", "role": "상할 잔 (요소)", "desc": "창이 부딪쳐 상처가 나거나 작게 부서진다는 뜻에서 물결이 조금 일렁인다는 뜻을 줍니다." }
    ],
    "story": "강물(氵)의 깊이가 얼마 되지 않아 물결이 잘게(戔) 부서지며 바닥이 다 보일 정도로 '얕다'는 뜻입니다.",
    "example_words": [
      { "word": "浅い", "reading": "あさい", "meaning": "얕다", "description": "물이나 생각의 깊이가 깊지 않은 상태입니다." },
      { "word": "浅草", "reading": "あさくさ", "meaning": "아사쿠사", "description": "일본 도쿄에 있는 유명한 관광지 지명입니다." }
    ]
  },
  {
    "kanji": "戦",
    "reading_on": "セン",
    "reading_kun": "いくさ、たたか(う)",
    "meaning": "싸움",
    "components": [
      { "char": "単", "role": "홑 단 (요소)", "desc": "원래 끝이 갈라진 무기인 몽둥이를 뜻합니다." },
      { "char": "戈", "role": "창 과 (부수)", "desc": "창이나 무기, 전쟁을 상징합니다." }
    ],
    "story": "손에 몽둥이(単의 원래 뜻)와 창(戈) 같은 무기를 들고 적과 치열하게 '싸우다' 혹은 서로 죽이는 '전쟁'을 뜻합니다.",
    "example_words": [
      { "word": "戦う", "reading": "たたかう", "meaning": "싸우다", "description": "적과 맞서 무력으로 승부를 겨루거나 어려움을 이겨내는 것입니다." },
      { "word": "戦争", "reading": "せんそう", "meaning": "전쟁", "description": "국가나 무리끼리 무력을 써서 싸우고(戦) 다투는(争) 큰일입니다." }
    ]
  },
  {
    "kanji": "選",
    "reading_on": "セン",
    "reading_kun": "えら(ぶ)",
    "meaning": "가릴 (선택할)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "이동이나 길을 가는 것을 뜻합니다." },
      { "char": "巽", "role": "손괘 손 (요소)", "desc": "무릎을 꿇고 공손히 물건을 올리는 모습에서 여러 개를 고른다는 뜻을 줍니다." }
    ],
    "story": "길(辶)을 가다가 여러 갈래 길 앞에서 어디로 갈지 이리저리 공손하게 따져보고(巽의 변형) 좋은 곳을 '가르다(선택하다)'는 뜻입니다.",
    "example_words": [
      { "word": "選ぶ", "reading": "えらぶ", "meaning": "고르다, 선택하다", "description": "여럿 가운데서 목적에 맞는 것을 골라내는 것입니다." },
      { "word": "選手", "reading": "せんしゅ", "meaning": "선수", "description": "운동 경기에 나갈 사람으로 뽑힌(選) 사람(手)입니다." }
    ]
  },
  {
    "kanji": "然",
    "reading_on": "ゼン、ネン",
    "reading_kun": "",
    "meaning": "그럴 (태울)",
    "components": [
      { "char": "肙", "role": "개고기 연 (요소)", "desc": "개고기나 짐승 고기를 뜻합니다." },
      { "char": "犬", "role": "개 견 (요소)", "desc": "개나 동물을 의미합니다." },
      { "char": "灬", "role": "연화발 (부수)", "desc": "불을 의미합니다." }
    ],
    "story": "원래 제사 때 불(灬)에 개고기(肙, 犬)를 활활 '태우다'는 뜻이었으나, 나중에는 '그렇다'라는 긍정의 의미나 어조사로 널리 쓰이게 되었습니다.",
    "example_words": [
      { "word": "自然", "reading": "しぜん", "meaning": "자연", "description": "사람의 힘을 더하지 않은, 스스로(自) 그러한(然) 세상 만물입니다." },
      { "word": "全然", "reading": "ぜんぜん", "meaning": "전혀", "description": "온전히(全) 그렇다(然)는 뜻에서, 부정어와 함께 쓰여 '아주'라는 뜻이 되었습니다." }
    ]
  },
  {
    "kanji": "争",
    "reading_on": "ソウ",
    "reading_kun": "あらそ(う)",
    "meaning": "다툴",
    "components": [
      { "char": "爫", "role": "손톱 조 (부수)", "desc": "위에서 물건을 잡으려는 손의 모양입니다." },
      { "char": "彐", "role": "튼가로왈 (요소)", "desc": "아래에서 물건을 당기려는 또 다른 손의 모양입니다." },
      { "char": "亅", "role": "갈고리 궐 (요소)", "desc": "가운데 있는 막대기나 물건입니다." }
    ],
    "story": "위아래의 두 손(爫, 彐)이 하나의 막대기(亅)를 차지하려고 서로 뺏고 뺏기며 서로 '다투다' 혹은 '싸우다'라는 의미입니다.",
    "example_words": [
      { "word": "争う", "reading": "あらそう", "meaning": "다투다, 겨루다", "description": "서로 이기려고 싸우거나 승부를 겨루는 것입니다." },
      { "word": "戦争", "reading": "せんそう", "meaning": "전쟁", "description": "국가나 무리끼리 싸우고(戦) 다투는(争) 큰 무력 충돌입니다." }
    ]
  },
  {
    "kanji": "倉",
    "reading_on": "ソウ",
    "reading_kun": "くら",
    "meaning": "곳집 (창고)",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "여기서는 지붕을 덮은 모양을 의미합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "건물의 내부나 창문을 뜻합니다." }
    ],
    "story": "커다란 지붕(人 모양)을 덮고, 환기가 되도록 문(口)을 만들어 곡식이나 물건을 오래도록 보관하는 '창고(곳간)'를 뜻합니다.",
    "example_words": [
      { "word": "倉", "reading": "くら", "meaning": "곳간, 창고", "description": "곡식이나 물건을 보관하기 위해 지은 건물입니다." },
      { "word": "倉庫", "reading": "そうこ", "meaning": "창고", "description": "물건을 쌓아두는 곳집(倉)과 차고(庫)입니다." }
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

print("Grade 4 Part 4 data appended successfully.")
