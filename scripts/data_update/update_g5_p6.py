import json
import os

new_data = [
  {
    "kanji": "謝",
    "reading_on": "シャ",
    "reading_kun": "あやま(る)",
    "meaning": "사례할 (사과할)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "射", "role": "쏠 사 (요소)", "desc": "활(弓)을 당겨 화살을 쏘듯, 긴장이 탁 풀린다는 뜻과 발음 '사/샤'를 줍니다." }
    ],
    "story": "활시위가 풀려 화살이 날아가듯, 긴장을 풀고 말(言)로 상대에게 잘못을 뉘우치며 '사과하다' 혹은 고마움을 '사례하다(사의를 표하다)'는 뜻입니다.",
    "example_words": [
      { "word": "謝る", "reading": "あやまる", "meaning": "사과하다", "description": "잘못을 인정하고 용서를 비는 말이나 행동을 하는 것입니다." },
      { "word": "感謝", "reading": "かんしゃ", "meaning": "감사", "description": "고마움을 느끼고(感) 그 뜻을 나타내어 사례하는(謝) 일입니다." }
    ]
  },
  {
    "kanji": "識",
    "reading_on": "シキ",
    "reading_kun": "",
    "meaning": "알 (식견)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 뜻합니다." },
      { "char": "戠", "role": "찰흙 시 (요소)", "desc": "무기(戈)를 들고 표시를 새겨 넣는다는 뜻과 발음 '식/시키'를 줍니다." }
    ],
    "story": "무기나 물건에 자기 것임을 표시(戠)해 두고, 나중에 남에게 말(言)로 분명히 설명하여 알아볼 수 있도록 '알다(식별하다)'는 뜻입니다.",
    "example_words": [
      { "word": "知識", "reading": "ちしき", "meaning": "지식", "description": "배워서 알고(知) 사물을 분별해 아는(識) 내용이나 깨달음입니다." },
      { "word": "意識", "reading": "いしき", "meaning": "의식", "description": "마음이나 뜻(意)으로 느끼고 아는(識) 감각입니다." }
    ]
  },
  {
    "kanji": "護",
    "reading_on": "ゴ",
    "reading_kun": "",
    "meaning": "보호할 (도울)",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말을 의미합니다." },
      { "char": "蒦", "role": "잴 확 (요소)", "desc": "새를 손으로 잡는다는 뜻에서 지킨다는 의미와 발음 '확/고'의 변형 역할을 합니다." }
    ],
    "story": "주변에 있는 사람이 다치지 않게 말(言)로 타이르고 위협으로부터 감싸 안아(蒦) 안전하게 '보호하다' 혹은 '지키다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "保護", "reading": "ほご", "meaning": "보호", "description": "안전하게 감싸(保) 지켜(護) 주는 일입니다." },
      { "word": "看護", "reading": "かんご", "meaning": "간호", "description": "환자 등을 보살피고(看) 돌보아 주는(護) 일입니다." }
    ]
  },
  {
    "kanji": "豊",
    "reading_on": "ホウ",
    "reading_kun": "ゆた(か)",
    "meaning": "풍성할",
    "components": [
      { "char": "豆", "role": "콩 두 (부수)", "desc": "원래 굽이 높은 굽다리 접시나 제기(제사 그릇)를 뜻합니다." },
      { "char": "曲", "role": "굽을 곡 (요소)", "desc": "제기 위에 곡식을 가득 쌓아 올린 모양(𧯮의 윗부분)의 변형입니다." }
    ],
    "story": "높은 그릇(豆) 위에 제물로 쓸 음식을 가득 수북하게(曲 변형) 쌓아 올려 넘칠 듯이 많고 '풍성하다(풍요롭다)'는 뜻입니다.",
    "example_words": [
      { "word": "豊か", "reading": "ゆたか", "meaning": "풍요롭다, 넉넉하다", "description": "모자람이 없이 아주 많고 넉넉한 상태입니다." },
      { "word": "豊富", "reading": "ほうふ", "meaning": "풍부", "description": "아주 풍성하고(豊) 넉넉하며 많은(富) 상태입니다." }
    ]
  },
  {
    "kanji": "財",
    "reading_on": "ザイ、サイ",
    "reading_kun": "",
    "meaning": "재물",
    "components": [
      { "char": "貝", "role": "조개 패 (부수)", "desc": "조개껍데기로, 옛날에 돈이나 재물로 쓰였습니다." },
      { "char": "才", "role": "재주 재 (요소)", "desc": "원래 강물이 막히지 않고 흐른다는 뜻이나 여기서는 재주나 바탕, 그리고 발음 '재/자이'를 줍니다." }
    ],
    "story": "사람이 살아가는 데 바탕(才)이 되는 돈이나 소중한 조개(貝), 즉 값어치가 있는 '재물'이나 '재산'을 뜻합니다.",
    "example_words": [
      { "word": "財産", "reading": "ざいさん", "meaning": "재산", "description": "돈이나 집 따위의 재물(財)과 생산물(産)입니다." },
      { "word": "財布", "reading": "さいふ", "meaning": "지갑", "description": "재물(財)인 돈을 넣기 위해 헝겊(布)이나 가죽으로 만든 주머니입니다." }
    ]
  },
  {
    "kanji": "貧",
    "reading_on": "ヒン、ビン",
    "reading_kun": "まず(しい)",
    "meaning": "가난할",
    "components": [
      { "char": "分", "role": "나눌 분 (요소)", "desc": "사물을 쪼개고 나눈다는 뜻과 발음 '분/힌'을 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 의미합니다." }
    ],
    "story": "가지고 있던 돈이나 재물(貝)을 여럿으로 작게 나누어(分) 버려 결국 재산이 쪼들리고 '가난하다' 혹은 '빈약하다'는 뜻입니다.",
    "example_words": [
      { "word": "貧しい", "reading": "まずしい", "meaning": "가난하다, 빈약하다", "description": "돈이나 재물이 부족하여 생활이 어렵거나 내용이 보잘것없는 상태입니다." },
      { "word": "貧乏", "reading": "びんぼう", "meaning": "가난, 빈보", "description": "재물이 가난하여(貧) 없는(乏) 궁핍한 상태입니다." }
    ]
  },
  {
    "kanji": "責",
    "reading_on": "セキ",
    "reading_kun": "せ(める)",
    "meaning": "꾸짖을 (책임)",
    "components": [
      { "char": "龶", "role": "가시 자 (요소)", "desc": "원래 가시나무를 뜻하여 날카롭고 따끔하다는 의미입니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 의미합니다." }
    ],
    "story": "빌려 간 돈(貝)을 갚으라고 따끔하게(龶) 독촉하며 남의 잘못을 '꾸짖다' 혹은 갚아야 할 의무인 '책임'을 뜻합니다.",
    "example_words": [
      { "word": "責める", "reading": "せめる", "meaning": "나무라다, 꾸짖다", "description": "남의 잘못이나 책임을 따져서 강하게 비난하는 것입니다." },
      { "word": "責任", "reading": "せきにん", "meaning": "책임", "description": "맡아서(任) 져야 할 꾸지람(責)이나 임무입니다." }
    ]
  },
  {
    "kanji": "貸",
    "reading_on": "タイ",
    "reading_kun": "か(す)",
    "meaning": "빌려줄",
    "components": [
      { "char": "代", "role": "대신할 대 (요소)", "desc": "대신하거나 바꾼다는 뜻과 발음 '대/타이'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 뜻합니다." }
    ],
    "story": "나중에 대신(代) 같은 것으로 돌려받기로 약속하고 남에게 돈(貝)이나 물건을 '빌려주다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "貸す", "reading": "かす", "meaning": "빌려주다", "description": "자신의 물건이나 돈을 남이 임시로 쓰도록 내주는 것입니다." },
      { "word": "賃貸", "reading": "ちんたい", "meaning": "임대", "description": "삯(賃)을 받고 물건 등을 빌려주는(貸) 일입니다." }
    ]
  },
  {
    "kanji": "貿",
    "reading_on": "ボウ",
    "reading_kun": "",
    "meaning": "무역할 (바꿀)",
    "components": [
      { "char": "卯", "role": "토끼 묘 (요소)", "desc": "물이 갈라진다는 뜻에서 서로 물건을 나눈다는 의미와 발음 '묘/보우'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 뜻합니다." }
    ],
    "story": "재물이나 돈(貝)을 주고받으며 서로 가진 물건을 '바꾸다' 혹은 사고파는 장사인 '무역하다'는 뜻입니다.",
    "example_words": [
      { "word": "貿易", "reading": "ぼうえき", "meaning": "무역", "description": "나라 사이에 서로 물건과 재물을 바꾸며(貿, 易) 장사하는 일입니다." }
    ]
  },
  {
    "kanji": "賀",
    "reading_on": "ガ",
    "reading_kun": "",
    "meaning": "하례할 (축하할)",
    "components": [
      { "char": "加", "role": "더할 가 (요소)", "desc": "보탠다는 뜻과 발음 '가/가'를 담당합니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 귀한 재물을 의미합니다." }
    ],
    "story": "축하하는 마음을 담아 좋은 말이나 칭찬을 더하고(加), 그에 맞게 귀한 선물(貝)을 바치며 축복하고 '하례하다(축하하다)'는 뜻입니다.",
    "example_words": [
      { "word": "年賀状", "reading": "ねんがじょう", "meaning": "연하장", "description": "새해(年)를 축하하기(賀) 위해 보내는 편지(状)입니다." },
      { "word": "祝賀", "reading": "しゅくが", "meaning": "축하", "description": "기쁜 일을 빌어주고(祝) 하례하는(賀) 일입니다." }
    ]
  },
  {
    "kanji": "資",
    "reading_on": "シ",
    "reading_kun": "",
    "meaning": "재물 (바탕)",
    "components": [
      { "char": "次", "role": "버금 차 (요소)", "desc": "차례로 모인다는 뜻과 발음 '차/시'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "재물이나 돈을 뜻합니다." }
    ],
    "story": "사업이나 장사를 하기 위해 차례로(次) 모아둔 밑천인 '재물'이나 '자본', 혹은 일의 '바탕(자료)'을 의미합니다.",
    "example_words": [
      { "word": "資料", "reading": "しりょう", "meaning": "자료", "description": "연구나 조사 등의 바탕(資)이 되는 재료(料)입니다." },
      { "word": "資格", "reading": "しかく", "meaning": "자격", "description": "어떤 일을 할 수 있는 바탕(資)과 격식(格)입니다." }
    ]
  },
  {
    "kanji": "賛",
    "reading_on": "サン",
    "reading_kun": "",
    "meaning": "도울 (찬성할)",
    "components": [
      { "char": "兟", "role": "나아갈 신 (요소)", "desc": "사람들이 앞으로 나아가며 뜻을 모은다는 의미와 발음 '신/산'의 변형 역할을 합니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "재물이나 돈을 뜻합니다." }
    ],
    "story": "다른 사람의 의견에 뜻을 모아(兟) 재물(貝)을 내어주며 적극적으로 '돕다' 혹은 그 의견에 '찬성하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "賛成", "reading": "さんせい", "meaning": "찬성", "description": "남의 의견을 도와(賛) 이루어(成) 주거나 뜻을 같이하는 것입니다." },
      { "word": "絶賛", "reading": "ぜっさん", "meaning": "절찬", "description": "더할 나위 없이 아주 훌륭하다고 극구 칭찬(賛)하는 것입니다." }
    ]
  },
  {
    "kanji": "質",
    "reading_on": "シツ、シチ",
    "reading_kun": "",
    "meaning": "바탕 (질)",
    "components": [
      { "char": "斦", "role": "은 냥 (요소)", "desc": "도끼 두 개를 맞대고 잰다는 뜻에서 무게를 다는 단위를 뜻하며 발음 '은/시츠'를 줍니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 재물을 뜻합니다." }
    ],
    "story": "재물(貝)의 무게(斦)나 가치를 저울로 재어 보는 데서, 사물이 본디 가지고 있는 '바탕(질)'이나 가치를 뜻하거나 돈을 빌릴 때 맡기는 '저당물'을 뜻합니다.",
    "example_words": [
      { "word": "質問", "reading": "しつもん", "meaning": "질문", "description": "모르는 것을 알기 위해 사실의 바탕(質)을 묻는(問) 것입니다." },
      { "word": "品質", "reading": "ひんしつ", "meaning": "품질", "description": "물건(品)이 지니고 있는 고유한 바탕과 성질(質)입니다." }
    ]
  },
  {
    "kanji": "輸",
    "reading_on": "ユ",
    "reading_kun": "",
    "meaning": "보낼 (나를)",
    "components": [
      { "char": "車", "role": "수레 거 (부수)", "desc": "수레나 탈것을 의미합니다." },
      { "char": "兪", "role": "점점 유 (요소)", "desc": "배를 타고 물을 건넌다는 뜻에서 통과한다는 의미와 발음 '유'를 담당합니다." }
    ],
    "story": "사람이나 물건을 수레(車)나 배(兪)에 싣고 다른 곳으로 '나르다(수송하다)' 혹은 '보내다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "輸入", "reading": "ゆにゅう", "meaning": "수입", "description": "외국에서 물건을 실어(輸) 들여오는(入) 일입니다." },
      { "word": "輸出", "reading": "ゆしゅつ", "meaning": "수출", "description": "자기 나라의 물건을 실어(輸) 외국으로 내보내는(出) 일입니다." }
    ]
  },
  {
    "kanji": "述",
    "reading_on": "ジュツ",
    "reading_kun": "の(べる)",
    "meaning": "지을 (서술할)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 나아가며 행동함을 뜻합니다." },
      { "char": "朮", "role": "차조 출 (요소)", "desc": "끈적끈적하게 따라다닌다는 뜻에서 이어서 붙인다는 의미와 발음 '출/쥬츠'를 줍니다." }
    ],
    "story": "자신의 생각이나 일어난 일들을 차례차례 길(辶)을 따라가듯 이어서(朮) 끈기 있게 말하거나 글로 '서술하다' 혹은 '말하다'는 뜻입니다.",
    "example_words": [
      { "word": "述べる", "reading": "のべる", "meaning": "말하다, 진술하다", "description": "생각이나 사실을 순서에 따라 조리 있게 말하거나 적어 나타내는 것입니다." },
      { "word": "記述", "reading": "きじゅつ", "meaning": "기술", "description": "사실을 있는 그대로 순서대로 적어(記) 서술하는(述) 일입니다." }
    ]
  },
  {
    "kanji": "迷",
    "reading_on": "メイ",
    "reading_kun": "まよ(う)",
    "meaning": "미혹할 (헤맬)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷는 것을 뜻합니다." },
      { "char": "米", "role": "쌀 미 (요소)", "desc": "여기서는 사방으로 흩어지는 작은 낟알처럼 갈피를 잡지 못한다는 뜻과 발음 '미/메이'를 줍니다." }
    ],
    "story": "쌀알(米)이 사방으로 흩어지듯 걷는 길(辶)이 헷갈려 갈피를 잡지 못하고 '헤매다', 혹은 마음이 '미혹되다(어지럽다)'는 뜻입니다.",
    "example_words": [
      { "word": "迷う", "reading": "まよう", "meaning": "헤매다, 망설いだ", "description": "길을 잃고 갈 바를 모르거나, 결정을 내리지 못해 이리저리 생각하는 것입니다." },
      { "word": "迷惑", "reading": "めいわく", "meaning": "민폐, 성가심", "description": "남의 일로 인해 마음이 어지럽고(迷) 홀리는(惑) 등 괴롭고 귀찮은 일입니다." }
    ]
  },
  {
    "kanji": "退",
    "reading_on": "タイ",
    "reading_kun": "しりぞ(く)、しりぞ(ける)",
    "meaning": "물러날",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 이동함을 뜻합니다." },
      { "char": "艮", "role": "그칠 간 (요소)", "desc": "눈을 부릅뜨고 뒤를 돌아본다는 뜻으로, 멈추어 선다는 의미와 발음 '간/타이'의 변형 역할을 합니다." }
    ],
    "story": "길을 가다가(辶) 발걸음을 멈추고 뒤를 돌아보며(艮) 뒷걸음질 쳐서 뒤로 '물러나다' 혹은 자리에서 '물러서다'는 뜻입니다.",
    "example_words": [
      { "word": "退く", "reading": "しりぞく", "meaning": "물러나다, 후퇴하다", "description": "자리나 지위에서 뒤로 물러나거나 그만두는 것입니다." },
      { "word": "退院", "reading": "たいいん", "meaning": "퇴원", "description": "병이 나아서 병원(院)에서 물러나는(退) 일입니다." }
    ]
  },
  {
    "kanji": "逆",
    "reading_on": "ギャク",
    "reading_kun": "さか、さか(らう)",
    "meaning": "거스를 (역)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "나아감을 의미합니다." },
      { "char": "屰", "role": "거스를 역 (요소)", "desc": "사람이 거꾸로 서 있는 모양으로 발음 '역/갸쿠'를 줍니다." }
    ],
    "story": "사람이 거꾸로 된(屰) 모양으로 길을 걷거나(辶), 순리에 맞지 않게 반대 방향으로 향하여 '거스르다' 혹은 '반대(역)'를 의미합니다.",
    "example_words": [
      { "word": "逆", "reading": "さか", "meaning": "거꾸로, 반대", "description": "정해진 방향이나 순서와 반대가 되는 상태입니다." },
      { "word": "逆らう", "reading": "さからう", "meaning": "거스르다, 반항하다", "description": "명령이나 흐름에 따르지 않고 거꾸로 맞서는 것입니다." }
    ]
  },
  {
    "kanji": "造",
    "reading_on": "ゾウ",
    "reading_kun": "つく(る)",
    "meaning": "지을",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 가거나 진행하는 것을 뜻합니다." },
      { "char": "告", "role": "알릴 고 (요소)", "desc": "제단에 소를 바치며 신에게 고한다는 뜻에서 완성했다는 의미와 발음 '고/조우'를 줍니다." }
    ],
    "story": "어떤 일을 진행하여(辶) 마침내 뜻한 바를 신에게 알릴(告) 정도로 훌륭하게 물건이나 건물을 '만들다' 혹은 '짓다(조성하다)'는 의미입니다.",
    "example_words": [
      { "word": "造る", "reading": "つくる", "meaning": "만들다, 짓다", "description": "큰 규모의 건물이나 배 따위를 설계하여 만들어 내는 것입니다." },
      { "word": "改造", "reading": "かいぞう", "meaning": "개조", "description": "원래 있던 것을 고쳐서(改) 새롭게 다시 만드는(造) 것입니다." }
    ]
  },
  {
    "kanji": "過",
    "reading_on": "カ",
    "reading_kun": "す(ぎる)、す(ごす)、あやま(つ)",
    "meaning": "지날",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 지나감을 의미합니다." },
      { "char": "咼", "role": "입비뚤어질 과 (요소)", "desc": "뼈가 어긋난 모양으로 엇나간다는 뜻과 발음 '과/카'를 담당합니다." }
    ],
    "story": "목적지를 어긋나게(咼) 치우쳐서 길(辶)을 그냥 '지나가 버리다' 혹은 정도가 '지나치다(너무하다)'나 '허물(잘못)'을 뜻합니다.",
    "example_words": [
      { "word": "過ぎる", "reading": "すぎる", "meaning": "지나다, 통과하다", "description": "어떤 시간이나 장소를 지나쳐 가거나, 정도가 보통을 넘는 것입니다." },
      { "word": "過去", "reading": "かこ", "meaning": "과거", "description": "이미 지나가고(過) 떠나버린(去) 옛날입니다." }
    ]
  },
  {
    "kanji": "適",
    "reading_on": "テキ",
    "reading_kun": "",
    "meaning": "맞을 (적당할)",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "가거나 나아감을 뜻합니다." },
      { "char": "啇", "role": "밑동 적 (요소)", "desc": "초목의 뿌리라는 뜻에서 딱 들어맞는다는 의미와 발음 '적/테키'를 줍니다." }
    ],
    "story": "자신이 가고자 하는(辶) 목적지와 딱 들어맞게(啇) 다다르다, 즉 조건이나 형편에 알맞게 딱 '맞다' 혹은 '적당하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "適当", "reading": "てきとう", "meaning": "적당", "description": "조건이나 성질에 꼭 들어맞는(適, 当) 일, 또는 요령껏 대충 넘기는 모양입니다." },
      { "word": "適切", "reading": "てきせつ", "meaning": "적절", "description": "상황에 알맞고(適) 꼭 맞아떨어지는(切) 것입니다." }
    ]
  },
  {
    "kanji": "酸",
    "reading_on": "サン",
    "reading_kun": "す(い)",
    "meaning": "실 (산성)",
    "components": [
      { "char": "酉", "role": "닭 유 (부수)", "desc": "술이나 발효된 음식 등을 뜻하는 닭(술)을 의미합니다." },
      { "char": "夋", "role": "천천히 걷는 모양 준 (요소)", "desc": "날카롭거나 찌른다는 뜻과 발음 '준/산'의 변형 역할을 합니다." }
    ],
    "story": "오래 발효된 술(酉)이 식초로 변하여 혀를 찌를(夋) 만큼 맛이 시큼하고 '시다', 혹은 화학에서의 '산(산성)'을 뜻합니다.",
    "example_words": [
      { "word": "酸っぱい", "reading": "すっぱい", "meaning": "시다, 시큼하다", "description": "식초나 레몬처럼 시큼한 맛이 나는 상태입니다." },
      { "word": "酸素", "reading": "さんそ", "meaning": "산소", "description": "산(酸)을 만드는 바탕(素)이 되는 기체 원소입니다." }
    ]
  },
  {
    "kanji": "鉱",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "쇳돌 (광석)",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 광물을 뜻합니다." },
      { "char": "広", "role": "넓을 광 (요소)", "desc": "넓다는 뜻과 발음 '광/코우'를 담당합니다." }
    ],
    "story": "넓은(広) 산속이나 땅 밑에 널리 묻혀 있는 쇠붙이(金)가 섞인 돌, 즉 금속을 캐낼 수 있는 '쇳돌'이나 '광물'을 의미합니다.",
    "example_words": [
      { "word": "鉱山", "reading": "こうざん", "meaning": "광산", "description": "유용한 광물(鉱)을 캐내는 산(山)이나 땅입니다." },
      { "word": "炭鉱", "reading": "たんこう", "meaning": "탄광", "description": "석탄(炭)을 캐내는 쇳돌 구덩이(鉱)입니다." }
    ]
  },
  {
    "kanji": "銅",
    "reading_on": "ドウ",
    "reading_kun": "",
    "meaning": "구리",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 금속을 의미합니다." },
      { "char": "同", "role": "한가지 동 (요소)", "desc": "비슷하다는 뜻과 발음 '동/도우'를 줍니다." }
    ],
    "story": "금과 빛깔이 비슷하여(同) 값어치가 높은 붉은색의 금속(金)인 '구리(동)'를 의미합니다.",
    "example_words": [
      { "word": "銅", "reading": "どう", "meaning": "구리", "description": "붉은빛을 띠고 전기가 잘 통하는 금속 원소입니다." },
      { "word": "銅メダル", "reading": "どうめだる", "meaning": "동메달", "description": "구리(銅)로 만들어 3등에게 주는 메달입니다." }
    ]
  },
  {
    "kanji": "銭",
    "reading_on": "セン",
    "reading_kun": "ぜに",
    "meaning": "돈 (전)",
    "components": [
      { "char": "金", "role": "쇠 금 (부수)", "desc": "쇠붙이나 돈을 뜻합니다." },
      { "char": "戔", "role": "적을 전 (요소)", "desc": "창(戈)이 거듭되어 자잘하게 나눈다는 뜻과 발음 '전/센'을 줍니다." }
    ],
    "story": "쇠(金)를 작고 자잘하게(戔) 나누어 둥글게 만들어 엽전으로 쓰던 가치가 작은 쇠붙이, 즉 '돈'이나 화폐 단위를 뜻합니다.",
    "example_words": [
      { "word": "銭", "reading": "ぜに", "meaning": "돈, 푼돈", "description": "물건을 살 때 쓰는 잔돈이나 엽전입니다." },
      { "word": "小銭", "reading": "こぜに", "meaning": "잔돈", "description": "지폐가 아닌 자잘한(小) 동전(銭)입니다." }
    ]
  },
  {
    "kanji": "防",
    "reading_on": "ボウ",
    "reading_kun": "ふせ(ぐ)",
    "meaning": "막을",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 둑을 뜻합니다." },
      { "char": "方", "role": "모 방 (요소)", "desc": "사방이라는 뜻이나, 여기서는 넓게 퍼진다는 의미와 발음 '방/보우'를 담당합니다." }
    ],
    "story": "물이 넓게 사방(方)으로 넘쳐흐르지 못하도록 흙을 높이 쌓아 올린 둑(阝)을 만들어 물을 '막다(방어하다)'는 의미입니다.",
    "example_words": [
      { "word": "防ぐ", "reading": "ふせぐ", "meaning": "막다, 방어하다", "description": "적이 쳐들어오거나 재난이 닥치는 것을 미리 막아 내는 일입니다." },
      { "word": "予防", "reading": "よぼう", "meaning": "예방", "description": "병이나 사고가 나기 전 미리(予) 막는(防) 일입니다." }
    ]
  },
  {
    "kanji": "限",
    "reading_on": "ゲン",
    "reading_kun": "かぎ(る)",
    "meaning": "한할 (한계)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 둑을 뜻합니다." },
      { "char": "艮", "role": "그칠 간 (요소)", "desc": "가다 멈춘다는 뜻과 함께 어긋난다는 의미, 발음 '간/겐'의 변형을 줍니다." }
    ],
    "story": "가파른 언덕(阝)에 가로막혀 발걸음을 멈추게(艮) 되는 끝부분, 즉 사물이 다다른 '한계'나 범위를 정하여 '제한하다'는 뜻입니다.",
    "example_words": [
      { "word": "限る", "reading": "かぎる", "meaning": "제한하다, 한정하다", "description": "시간이나 범위 따위를 일정한 선까지로 못 박아 정하는 것입니다." },
      { "word": "限界", "reading": "げんかい", "meaning": "한계", "description": "더 이상 나아갈 수 없는 한정된(限) 지경이나 경계(界)입니다." }
    ]
  },
  {
    "kanji": "険",
    "reading_on": "ケン",
    "reading_kun": "けわ(しい)",
    "meaning": "험할",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 산을 뜻합니다." },
      { "char": "僉", "role": "다 첨 (요소)", "desc": "여러 사람이 모여 의견을 낸다는 뜻이나, 여기서는 날카롭다는 의미와 발음 '첨/켄'을 줍니다." }
    ],
    "story": "산이나 언덕(阝)의 모양이 여러 갈래(僉)로 날카롭게 깎아지른 듯 가파르고 다가가기 위험하여 '험하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "険しい", "reading": "けわしい", "meaning": "험하다, 가파르다", "description": "산이나 비탈이 오르기 힘들거나 사람의 표정이 매서운 모양입니다." },
      { "word": "危険", "reading": "きけん", "meaning": "위험", "description": "안전하지 못하고 위태로우며(危) 험한(険) 상태입니다." }
    ]
  },
  {
    "kanji": "際",
    "reading_on": "サイ",
    "reading_kun": "きわ",
    "meaning": "즈음 (사이)",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 둑을 뜻합니다." },
      { "char": "祭", "role": "제사 제 (요소)", "desc": "제사를 지낸다는 뜻에서 손이 닿는 가까운 곳이라는 의미와 발음 '제/사이'를 줍니다." }
    ],
    "story": "언덕(阝)과 평지가 만나는 맞닿은 곳(祭 변형의 의미), 즉 물건의 가장자리나 두 사물 간의 '사이', 어떤 일이 일어나는 '즈음(때)'을 뜻합니다.",
    "example_words": [
      { "word": "際", "reading": "きわ", "meaning": "가장자리, 즈음", "description": "어떤 물건의 끝이 되는 가장자리나 어떤 일이 일어나는 무렵입니다." },
      { "word": "国際", "reading": "こくさい", "meaning": "국제", "description": "여러 나라(国) 사이(際)에 걸치는 관계입니다." }
    ]
  },
  {
    "kanji": "雑",
    "reading_on": "ザツ、ゾウ",
    "reading_kun": "",
    "meaning": "섞일",
    "components": [
      { "char": "九", "role": "아홉 구 (요소)", "desc": "여기서는 나무(木)와 여러 가지 색을 뜻하는 글자(衣)의 결합형(雜)의 변형으로, 여럿을 뜻합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "나뭇가지들이 얽힌 모양을 나타냅니다." },
      { "char": "隹", "role": "새 추 (부수)", "desc": "작은 새가 여럿 모인 것을 의미합니다." }
    ],
    "story": "여러 마리의 새(隹)들이 나뭇가지(木) 위에 모여들어 다양한 색깔의 깃털이 어지럽게 뒤엉켜 '섞이다(잡다하다)'는 뜻을 의미합니다.",
    "example_words": [
      { "word": "雑草", "reading": "ざっそう", "meaning": "잡초", "description": "이름 모를 여러 가지(雑) 풀(草)들이 마구 자라난 것입니다." },
      { "word": "複雑", "reading": "ふくざつ", "meaning": "복잡", "description": "여러 가지가 겹치고(複) 뒤섞여서(雑) 얽힌 상태입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade5.json'
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

print("Grade 5 Part 6 data appended successfully.")
