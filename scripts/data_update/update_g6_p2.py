import json
import os

new_data = [
  {
    "kanji": "域",
    "reading_on": "イキ",
    "reading_kun": "",
    "meaning": "지경 (지역)",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "땅이나 흙을 뜻합니다." },
      { "char": "或", "role": "혹 혹 (요소)", "desc": "무기를 들고 땅을 지킨다는 뜻에서 구역이라는 의미와 발음 '혹/이키'의 변형 역할을 합니다." }
    ],
    "story": "흙(土)으로 경계를 쌓고 무기(或)를 들고 지키는 땅의 '지경(경계)'이나 일정한 '지역'을 뜻합니다.",
    "example_words": [
      { "word": "地域", "reading": "ちいき", "meaning": "지역", "description": "일정하게 나뉜 땅(地)의 구역(域)입니다." },
      { "word": "区域", "reading": "くいき", "meaning": "구역", "description": "일정한 기준에 따라 갈라놓은(区) 지경(域)입니다." }
    ]
  },
  {
    "kanji": "奏",
    "reading_on": "ソウ",
    "reading_kun": "かな(でる)",
    "meaning": "아뢸 (연주할)",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "크다라는 뜻이나, 여기서는 두 손을 모아 받치는 모양(𠬞)의 변형입니다." },
      { "char": "𡗗", "role": "풀훼머리 변형 (요소)", "desc": "신에게 바치는 풀이나 나뭇가지를 뜻합니다." },
      { "char": "天", "role": "하늘 천 (요소)", "desc": "여기서는 머리 쪽으로 들어 올린다는 뜻입니다." }
    ],
    "story": "두 손(大 변형)으로 풀이나 제물(𡗗)을 높이 들어 올려 신이나 임금에게 '아뢰다', 혹은 그 과정에서 악기를 '연주하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "奏でる", "reading": "かなでる", "meaning": "연주하다", "description": "악기를 켜거나 타서 음악을 소리 내는 것입니다." },
      { "word": "演奏", "reading": "えんそう", "meaning": "연주", "description": "악기를 다루어(演) 음악을 아뢰는(奏) 것입니다." }
    ]
  },
  {
    "kanji": "奮",
    "reading_on": "フン",
    "reading_kun": "ふる(う)",
    "meaning": "떨칠 (분발할)",
    "components": [
      { "char": "大", "role": "큰 대 (부수)", "desc": "새가 날개를 크게 펼친 모양을 뜻합니다." },
      { "char": "隹", "role": "새 추 (요소)", "desc": "새를 뜻합니다." },
      { "char": "田", "role": "밭 전 (요소)", "desc": "밭이나 둥지를 뜻합니다." }
    ],
    "story": "새(隹)가 둥지나 밭(田)에서 크게(大) 날개를 치며 날아오르듯 기운이나 용기를 '떨치다' 혹은 '분발하다'는 뜻입니다.",
    "example_words": [
      { "word": "奮う", "reading": "ふるう", "meaning": "떨치다, 분발하다", "description": "용기나 기운을 내어 씩씩하게 일어나는 것입니다." },
      { "word": "興奮", "reading": "こうふん", "meaning": "흥분", "description": "감정이 일어(興) 기운이 몹시 떨쳐(奮) 오르는 것입니다." }
    ]
  },
  {
    "kanji": "姿",
    "reading_on": "シ",
    "reading_kun": "すがた",
    "meaning": "모양 (자태)",
    "components": [
      { "char": "次", "role": "버금 차 (요소)", "desc": "이어진다는 뜻과 발음 '차/시'를 줍니다." },
      { "char": "女", "role": "계집 녀 (부수)", "desc": "여자나 사람을 뜻합니다." }
    ],
    "story": "차례(次)로 걸어가는 여자(女)의 아름다운 뒷모습에서 사람의 '모양'이나 '자태(모습)'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "姿", "reading": "すがた", "meaning": "모습, 자태", "description": "겉으로 보이는 사람이나 사물의 생김새입니다." },
      { "word": "姿勢", "reading": "しせい", "meaning": "자세", "description": "몸을 움직이는 모양(姿)과 기세(勢)입니다." }
    ]
  },
  {
    "kanji": "存",
    "reading_on": "ソン、ゾン",
    "reading_kun": "",
    "meaning": "있을 (존재할)",
    "components": [
      { "char": "子", "role": "아들 자 (부수)", "desc": "아이를 뜻합니다." },
      { "char": "才", "role": "재주 재 (요소)", "desc": "원래 氵(물결)의 변형으로 쓰이기도 했으나 여기서는 굳건하게 있다는 뜻과 발음 '재/손'의 변형 역할을 합니다." }
    ],
    "story": "아이(子)가 태어나 굳건하게(才) 살아 '있다' 혹은 세상에 '존재하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "存在", "reading": "そんざい", "meaning": "존재", "description": "실제로 세상에 있고(存) 머무는(在) 것입니다." },
      { "word": "保存", "reading": "ほぞん", "meaning": "보존", "description": "잘 보호하고(保) 지켜서 그대로 있게(存) 하는 일입니다." }
    ]
  },
  {
    "kanji": "孝",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "효도",
    "components": [
      { "char": "老", "role": "늙을 로 (요소)", "desc": "늙은 부모나 노인을 뜻합니다. (아래 匕가 생략된 耂 형태)" },
      { "char": "子", "role": "아들 자 (부수)", "desc": "아이나 자식을 의미합니다." }
    ],
    "story": "자식(子)이 늙은(耂) 부모를 잘 받들어 모시고 공경하는 '효도'를 뜻합니다.",
    "example_words": [
      { "word": "親孝行", "reading": "おやこうこう", "meaning": "효도", "description": "부모(親)에게 효도(孝)를 행하는(行) 일입니다." },
      { "word": "孝行", "reading": "こうこう", "meaning": "효행", "description": "효도(孝)하는 행실(行)입니다." }
    ]
  },
  {
    "kanji": "宅",
    "reading_on": "タク",
    "reading_kun": "",
    "meaning": "집 (댁)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 집을 뜻합니다." },
      { "char": "乇", "role": "부탁할 탁 (요소)", "desc": "식물의 뿌리가 내린다는 뜻과 발음 '탁/타쿠'를 줍니다." }
    ],
    "story": "식물이 뿌리를 내리듯(乇) 사람이 한곳에 정착하여 짓고 사는 지붕(宀) 있는 '집'이나 남의 집을 높여 부르는 '댁'을 의미합니다.",
    "example_words": [
      { "word": "自宅", "reading": "じたく", "meaning": "자택", "description": "자기(自)가 살고 있는 집(宅)입니다." },
      { "word": "住宅", "reading": "じゅうたく", "meaning": "주택", "description": "사람이 살며 머무는(住) 집(宅)입니다." }
    ]
  },
  {
    "kanji": "宇",
    "reading_on": "ウ",
    "reading_kun": "",
    "meaning": "집 (우주)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 집을 의미합니다." },
      { "char": "于", "role": "어조사 우 (요소)", "desc": "크고 넓게 퍼진다는 뜻과 발음 '우/우'를 담당합니다." }
    ],
    "story": "처마(지붕 宀)가 크고 넓게 퍼져(于) 하늘을 덮을 만큼 거대한 '집' 혹은 끝없이 넓은 '우주(공간)'를 뜻합니다.",
    "example_words": [
      { "word": "宇宙", "reading": "うちゅう", "meaning": "우주", "description": "하늘과 땅 사이의 끝없이 넓은 집(宇, 宙) 같은 공간입니다." },
      { "word": "宇宙船", "reading": "うちゅうせん", "meaning": "우주선", "description": "우주(宇宙)로 날아가는 배(船)나 비행체입니다." }
    ]
  },
  {
    "kanji": "宗",
    "reading_on": "シュウ、ソウ",
    "reading_kun": "",
    "meaning": "마루 (근본)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 사당을 뜻합니다." },
      { "char": "示", "role": "보일 시 (요소)", "desc": "신이나 제사, 조상을 뜻합니다." }
    ],
    "story": "집(宀) 안에 조상(示)을 모셔 둔 사당이라는 데서, 집안의 '마루(으뜸, 기둥)'나 종교의 '근본'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "宗教", "reading": "しゅうきょう", "meaning": "종교", "description": "으뜸이 되고 근본(宗)이 되는 가르침(教)이나 믿음입니다." },
      { "word": "祖宗", "reading": "そそう", "meaning": "조종", "description": "가문의 처음이 되는 할아버지(祖)와 으뜸 조상(宗)입니다." }
    ]
  },
  {
    "kanji": "宙",
    "reading_on": "チュウ",
    "reading_kun": "",
    "meaning": "집 (우주)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 공간을 뜻합니다." },
      { "char": "由", "role": "말미암을 유 (요소)", "desc": "과거부터 이어져 온다는 뜻과 발음 '유/츄우'의 변형 역할을 합니다." }
    ],
    "story": "집(宀)처럼 넓은 곳에서 과거부터 지금까지 이어져(由) 온 무한한 시간이나 공간, 즉 '집' 혹은 하늘과 '우주'를 의미합니다.",
    "example_words": [
      { "word": "宇宙", "reading": "うちゅう", "meaning": "우주", "description": "모든 시간과 공간을 아우르는 무한한 세계(宇, 宙)입니다." },
      { "word": "宙返り", "reading": "ちゅうがえり", "meaning": "공중제비", "description": "허공(宙)에서 몸을 뒤집어 도는(返り) 일입니다." }
    ]
  },
  {
    "kanji": "宝",
    "reading_on": "ホウ",
    "reading_kun": "たから",
    "meaning": "보배",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집을 뜻합니다." },
      { "char": "玉", "role": "구슬 옥 (요소)", "desc": "보석이나 귀한 구슬을 의미합니다." }
    ],
    "story": "집(宀) 안에 잘 간직해 둔 귀한 옥구슬(玉)처럼 아주 소중한 물건인 '보배'나 '보물'을 뜻합니다.",
    "example_words": [
      { "word": "宝", "reading": "たから", "meaning": "보물", "description": "매우 귀중하고 값비싼 물건입니다." },
      { "word": "宝石", "reading": "ほうせき", "meaning": "보석", "description": "보배(宝)로운 돌(石)이나 장신구입니다." }
    ]
  },
  {
    "kanji": "宣",
    "reading_on": "セン",
    "reading_kun": "",
    "meaning": "베풀 (선포할)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집이나 궁궐을 뜻합니다." },
      { "char": "亘", "role": "뻗칠 긍 (요소)", "desc": "널리 뻗어나간다는 뜻과 발음 '선/센'의 변형 역할을 합니다. (원래 𠄢 형태)" }
    ],
    "story": "궁궐(宀)에서 임금이 백성들에게 명령이나 뜻을 널리 뻗어나가게(亘) '베풀다' 혹은 '선포하다'는 의미입니다.",
    "example_words": [
      { "word": "宣言", "reading": "せんげん", "meaning": "선언", "description": "자신의 뜻이나 방침을 널리 알리고(宣) 말하는(言) 것입니다." },
      { "word": "宣伝", "reading": "せんでん", "meaning": "선전", "description": "주의나 주장을 널리 펴서(宣) 전하는(伝) 일입니다." }
    ]
  },
  {
    "kanji": "密",
    "reading_on": "ミツ",
    "reading_kun": "",
    "meaning": "빽빽할 (비밀)",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "집을 뜻합니다." },
      { "char": "必", "role": "반드시 필 (요소)", "desc": "창자처럼 얽혀 있다는 뜻과 발음 '필/미츠'의 변형 역할을 합니다." },
      { "char": "山", "role": "뫼 산 (요소)", "desc": "산이나 숲을 의미합니다." }
    ],
    "story": "집(宀) 안이나 산(山)속의 나무들이 촘촘하게(必) 얽혀 있어 빈틈없이 '빽빽하다' 혹은 남이 모르게 촘촘히 숨긴 '비밀'을 뜻합니다.",
    "example_words": [
      { "word": "秘密", "reading": "ひみつ", "meaning": "비밀", "description": "남에게 알려지지 않게 숨기고(秘) 가리는(密) 일입니다." },
      { "word": "密集", "reading": "みっしゅう", "meaning": "밀집", "description": "빈틈없이 빽빽하게(密) 모이는(集) 것입니다." }
    ]
  },
  {
    "kanji": "寸",
    "reading_on": "スン",
    "reading_kun": "",
    "meaning": "마디 (촌)",
    "components": [
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손목에서 맥박이 뛰는 곳까지의 길이나 마디를 나타내는 모양입니다." }
    ],
    "story": "손목에서 맥이 뛰는 곳까지의 짧은 거리를 본떠 만든 글자로, 손가락 한 '마디' 정도의 길이 단위인 '촌'을 뜻합니다.",
    "example_words": [
      { "word": "寸法", "reading": "すんぽう", "meaning": "치수", "description": "물건의 길이나 크기(寸)를 재는 법(法)이나 그 결과입니다." },
      { "word": "一寸", "reading": "いっすん", "meaning": "일 촌, 조금", "description": "아주 짧은 길이(한 마디)나 아주 적은 양입니다." }
    ]
  },
  {
    "kanji": "専",
    "reading_on": "セン",
    "reading_kun": "もっぱ(ら)",
    "meaning": "오로지 (전념할)",
    "components": [
      { "char": "叀", "role": "물레 전 (요소)", "desc": "실을 감는 물레의 모양에서 둥글게 돈다는 뜻과 발음 '전/센'을 줍니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손을 뜻하여 손으로 조작하는 동작을 나타냅니다." }
    ],
    "story": "손(寸)으로 물레(叀)를 한 방향으로만 계속 돌리듯, 다른 데 마음을 쓰지 않고 '오로지' 한 가지 일에만 마음을 쏟아 '전념하다'는 뜻입니다.",
    "example_words": [
      { "word": "専門", "reading": "せんもん", "meaning": "전문", "description": "오로지(専) 한 가지 분야나 학문(門)만을 연구하거나 맡는 일입니다." },
      { "word": "専用", "reading": "せんよう", "meaning": "전용", "description": "특정한 사람이나 목적에만 오로지(専) 쓰는(用) 일입니다." }
    ]
  },
  {
    "kanji": "射",
    "reading_on": "シャ",
    "reading_kun": "い(る)",
    "meaning": "쏠",
    "components": [
      { "char": "身", "role": "몸 신 (요소)", "desc": "원래 활(弓) 모양이 잘못 변하여 쓰이게 되었습니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손을 뜻하여 손으로 당기는 동작을 의미합니다." }
    ],
    "story": "손(寸)으로 활(身 변형)을 당기어 화살을 멀리 '쏘다'는 의미를 가지며, 빛을 쏜다는 뜻도 지닙니다.",
    "example_words": [
      { "word": "射る", "reading": "いる", "meaning": "쏘다", "description": "활이나 총 따위를 겨누어 화살이나 총알을 날려 보내는 것입니다." },
      { "word": "注射", "reading": "ちゅうしゃ", "meaning": "주사", "description": "주사기를 통해 약물을 몸속으로 부어(注) 쏘아(射) 넣는 일입니다." }
    ]
  },
  {
    "kanji": "将",
    "reading_on": "ショウ",
    "reading_kun": "",
    "meaning": "장수 (장차)",
    "components": [
      { "char": "丬", "role": "널빤지 장 (요소)", "desc": "침상이나 평상을 뜻하며 발음 '장/쇼우'를 줍니다." },
      { "char": "肉", "role": "고기 육 (요소)", "desc": "고기나 몸을 뜻합니다. (月 모양)" },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손을 의미합니다." }
    ],
    "story": "평상(丬) 위에서 손(寸)에 든 고기(肉)를 다루듯 군사들을 잘 다루고 이끄는 우두머리인 '장수'를 뜻하며, 앞으로 나아간다는 뜻에서 '장차'라는 뜻도 가집니다.",
    "example_words": [
      { "word": "将来", "reading": "しょうらい", "meaning": "장래", "description": "장차(将) 앞으로 다가올(来) 미래입니다." },
      { "word": "将軍", "reading": "しょうぐん", "meaning": "장군", "description": "군대(軍)를 거느리는 장수(将)입니다." }
    ]
  },
  {
    "kanji": "尊",
    "reading_on": "ソン",
    "reading_kun": "とうと(い)、たっと(い)、とうと(ぶ)、たっと(ぶ)",
    "meaning": "높을 (귀할)",
    "components": [
      { "char": "酋", "role": "묵은술 추 (요소)", "desc": "향기로운 술이 담긴 술통을 뜻합니다." },
      { "char": "寸", "role": "마디 촌 (부수)", "desc": "손을 뜻하여 손으로 받쳐 드는 동작을 의미합니다." }
    ],
    "story": "향기롭고 귀한 술이 든 통(酋)을 두 손(寸)으로 공손하게 받들어 신이나 어른께 올린다는 데서, 신분이 '높다' 혹은 아주 '귀하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "尊い", "reading": "とうとい", "meaning": "귀중하다, 거룩하다", "description": "가치가 매우 높거나 소중하고 훌륭한 상태입니다." },
      { "word": "尊敬", "reading": "そんけい", "meaning": "존경", "description": "남의 인격이나 생각을 높이(尊) 사서 공경하는(敬) 마음입니다." }
    ]
  },
  {
    "kanji": "就",
    "reading_on": "シュウ、ジュ",
    "reading_kun": "つ(く)、つ(ける)",
    "meaning": "나아갈 (이룰)",
    "components": [
      { "char": "京", "role": "서울 경 (요소)", "desc": "높은 건물이나 언덕을 뜻합니다." },
      { "char": "尤", "role": "더욱 우 (부수)", "desc": "절름발이나 한쪽으로 기우는 모양에서 다가간다는 뜻을 줍니다." }
    ],
    "story": "높은 건물(京)이나 성곽을 향해 발걸음(尤)을 옮겨 가까이 '나아가다' 혹은 일자리에 '나아가' 목적을 '이루다'는 뜻입니다.",
    "example_words": [
      { "word": "就く", "reading": "つく", "meaning": "나아가다, 자리에 앉다", "description": "어떤 지위나 일자리를 얻어 일하기 시작하는 것입니다." },
      { "word": "就職", "reading": "しゅうしょく", "meaning": "취직", "description": "일정한 직업(職)을 얻어 그 자리에 나아가는(就) 일입니다." }
    ]
  },
  {
    "kanji": "尺",
    "reading_on": "シャク",
    "reading_kun": "",
    "meaning": "자 (길이)",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "사람의 몸통을 뜻합니다." },
      { "char": "乀", "role": "파임 불 (요소)", "desc": "엄지와 중지를 벌린 한 뼘을 나타내는 표시입니다." }
    ],
    "story": "사람(尸)이 손가락을 벌려 한 뼘(乀)을 재는 모양에서 유래하여, 길이를 재는 단위인 '자(약 30cm)'나 길이를 재는 도구를 뜻합니다.",
    "example_words": [
      { "word": "尺", "reading": "しゃく", "meaning": "자", "description": "길이를 재는 단위나 도구입니다. 한 자는 약 30.3cm입니다." },
      { "word": "巻尺", "reading": "まきじゃく", "meaning": "줄자", "description": "둘둘 감아(巻) 두었다가 풀어서 길이를 재는 자(尺)입니다." }
    ]
  },
  {
    "kanji": "届",
    "reading_on": "カイ",
    "reading_kun": "とど(く)、とど(ける)",
    "meaning": "이를",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "사람이나 사람의 몸을 뜻합니다." },
      { "char": "由", "role": "말미암을 유 (요소)", "desc": "길을 따라간다는 뜻을 줍니다. (원래 屆 자의 줄임말)" }
    ],
    "story": "사람(尸)이 먼 길을 따라 걸어가서 마침내 목적지에 '이르다(도착하다)' 혹은 물건을 '전하다(닿다)'는 뜻입니다.",
    "example_words": [
      { "word": "届く", "reading": "とどく", "meaning": "닿다, 이르다", "description": "보낸 물건이나 편지 따위가 목적지에 무사히 도착하는 것입니다." },
      { "word": "届ける", "reading": "とどける", "meaning": "보내어 주다, 신고하다", "description": "물건을 목적지에 전달하거나 서류를 제출하여 알리는 일입니다." }
    ]
  },
  {
    "kanji": "展",
    "reading_on": "テン",
    "reading_kun": "",
    "meaning": "펼",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "몸통이나 굴러가는 모양을 뜻합니다." },
      { "char": "衣", "role": "옷 의 (요소)", "desc": "옷을 의미합니다. (아래 𧘇 형태)" },
      { "char": "一", "role": "한 일 (요소)", "desc": "펼쳐진 상태를 뜻합니다." }
    ],
    "story": "몸통(尸) 아래로 둘둘 말려 있던 옷(衣)을 평평하게(一) 굴려 활짝 '펴다(펼치다)' 혹은 전시하다는 뜻입니다.",
    "example_words": [
      { "word": "展開", "reading": "てんかい", "meaning": "전개", "description": "말려 있던 것을 펼쳐(展) 열거나(開) 일을 벌여 나가는 것입니다." },
      { "word": "展示", "reading": "てんじ", "meaning": "전시", "description": "물건을 넓게 펼쳐놓고(展) 여러 사람에게 보이게(示) 하는 일입니다." }
    ]
  },
  {
    "kanji": "層",
    "reading_on": "ソウ",
    "reading_kun": "",
    "meaning": "층",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "지붕이나 덮개를 뜻합니다." },
      { "char": "曽", "role": "일찍 증 (요소)", "desc": "가마솥이나 시루 위에 물건을 차곡차곡 쌓는다는 뜻과 발음 '증/소우'를 줍니다." }
    ],
    "story": "지붕(尸) 아래 시루떡처럼 여러 겹을 켜켜이 겹쳐(曽) 쌓아 올린 모양에서 겹치거나 건물의 '층'을 의미합니다.",
    "example_words": [
      { "word": "地層", "reading": "ちそう", "meaning": "지층", "description": "오랜 세월 동안 흙이나 모래가 쌓여 이룬 땅(地)의 층(層)입니다." },
      { "word": "階層", "reading": "かいそう", "meaning": "계층", "description": "사회적인 지위나 등급(階)이 나뉘어 있는 층(層)입니다." }
    ]
  },
  {
    "kanji": "己",
    "reading_on": "コ、キ",
    "reading_kun": "おのれ",
    "meaning": "몸 (자기)",
    "components": [
      { "char": "己", "role": "몸 기 (부수)", "desc": "구불구불한 새끼줄이나 사람이 몸을 굽힌 모양을 본뜬 글자입니다." }
    ],
    "story": "사람이 몸을 굽힌 모양이나 기운이 굽어도는 모습을 본떠 나 자신을 나타내는 '몸'이나 '자기'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "己", "reading": "おのれ", "meaning": "자기, 자신", "description": "나 스스로나 자기 자신을 가리키는 말입니다." },
      { "word": "自己", "reading": "じこ", "meaning": "자기", "description": "스스로(自)의 몸(己)이나 자신입니다." }
    ]
  },
  {
    "kanji": "巻",
    "reading_on": "カン",
    "reading_kun": "ま(く)、ま(き)",
    "meaning": "말 (권)",
    "components": [
      { "char": "龹", "role": "두손으로말 권 (요소)", "desc": "손으로 물건을 돌돌 만다는 뜻과 발음 '권/칸'을 줍니다." },
      { "char": "己", "role": "몸 기 (부수)", "desc": "구부러지거나 몸을 굽히는 모양을 뜻합니다." }
    ],
    "story": "두 손(龹)으로 종이나 천을 구부려(己) 둥글게 '말다' 혹은 돌돌 말아놓은 책을 세는 단위인 '권'을 뜻합니다.",
    "example_words": [
      { "word": "巻く", "reading": "まく", "meaning": "말다, 감다", "description": "종이나 천 따위를 둥글게 둘러싸거나 감는 것입니다." },
      { "word": "全巻", "reading": "ぜんかん", "meaning": "전권", "description": "시리즈로 된 책 따위의 모든(全) 권(巻)입니다." }
    ]
  },
  {
    "kanji": "幕",
    "reading_on": "マク、バク",
    "reading_kun": "",
    "meaning": "막",
    "components": [
      { "char": "莫", "role": "없을 막 (요소)", "desc": "해가 풀숲 사이로 숨어 보이지 않게 덮는다는 뜻과 발음 '막/마쿠'를 줍니다." },
      { "char": "巾", "role": "수건 건 (부수)", "desc": "천이나 헝겊을 의미합니다." }
    ],
    "story": "해가 지듯 안을 보이지 않게(莫) 넓은 천(巾)으로 빙 둘러쳐서 가리는 '막(장막)'을 의미합니다.",
    "example_words": [
      { "word": "幕", "reading": "まく", "meaning": "막", "description": "무대나 군대 진영을 가리거나 둘러치는 넓은 천입니다." },
      { "word": "開幕", "reading": "かいまく", "meaning": "개막", "description": "연극이나 행사 따위가 막(幕)을 열어(開) 시작되는 것입니다." }
    ]
  },
  {
    "kanji": "干",
    "reading_on": "カン",
    "reading_kun": "ほ(す)、ひ(る)",
    "meaning": "방패 (마를)",
    "components": [
      { "char": "干", "role": "방패 간 (부수)", "desc": "나무를 엮어 만든 방패나 찌르는 무기의 모양입니다." }
    ],
    "story": "적을 막는 방패의 모양에서 유래했으나, 나중에는 물건을 넓게 펴서 햇볕에 쬐어 '말리다' 혹은 물기가 '마르다'는 뜻으로 더 자주 쓰이게 되었습니다.",
    "example_words": [
      { "word": "干す", "reading": "ほす", "meaning": "말리다", "description": "빨래나 물건을 볕이나 바람에 내놓아 물기를 없애는 것입니다." },
      { "word": "若干", "reading": "じゃっかん", "meaning": "약간", "description": "얼마 되지 않는 적은 수량이나 정도입니다. (干이 구한다는 뜻으로 쓰임)" }
    ]
  },
  {
    "kanji": "幼",
    "reading_on": "ヨウ",
    "reading_kun": "おさな(い)",
    "meaning": "어릴",
    "components": [
      { "char": "幺", "role": "작을 요 (부수)", "desc": "가느다란 실이나 아주 작다는 뜻입니다." },
      { "char": "力", "role": "힘 력 (요소)", "desc": "힘이나 움직임을 뜻합니다." }
    ],
    "story": "가느다란 실(幺)처럼 아주 작고 아직 힘(力)이 약하여 나이가 '어리다' 혹은 '어리석다'는 뜻입니다.",
    "example_words": [
      { "word": "幼い", "reading": "おさない", "meaning": "어리다", "description": "나이가 적거나 생각이 미숙한 상태입니다." },
      { "word": "幼稚園", "reading": "ようちえん", "meaning": "유치원", "description": "어린(幼)아이들(稚)을 교육하고 기르는 곳(園)입니다." }
    ]
  },
  {
    "kanji": "庁",
    "reading_on": "チョウ",
    "reading_kun": "",
    "meaning": "관청",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "지붕이나 넓은 집을 뜻합니다." },
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "원래 듣는다는 뜻의 聽(들을 청)이 간략화되어 발음 '청/초우'를 줍니다." }
    ],
    "story": "큰 지붕(广)이 있는 집에서 백성들의 말을 듣고 나랏일을 처리하는 공공 기관, 즉 '관청'을 뜻합니다.",
    "example_words": [
      { "word": "官庁", "reading": "かんちょう", "meaning": "관청", "description": "나라의 일(官)을 맡아보는 기관(庁)입니다." },
      { "word": "県庁", "reading": "けんちょう", "meaning": "현청", "description": "일본의 행정 구역인 현(県)의 일을 맡아보는 관청(庁)입니다." }
    ]
  },
  {
    "kanji": "座",
    "reading_on": "ザ",
    "reading_kun": "すわ(る)",
    "meaning": "자리 (앉을)",
    "components": [
      { "char": "广", "role": "엄호 (부수)", "desc": "지붕이나 건물을 뜻합니다." },
      { "char": "坐", "role": "앉을 좌 (요소)", "desc": "두 사람(人人)이 땅(土) 위에 앉아 있다는 뜻과 발음 '좌/자'를 줍니다." }
    ],
    "story": "지붕(广)이 있는 집 안이나 방에 두 사람 이상이 마주 보고 앉을(坐) 수 있도록 마련된 '자리'나, 자리에 '앉다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "座る", "reading": "すわる", "meaning": "앉다", "description": "서 있던 사람이 의자나 바닥에 엉덩이를 대고 자리를 잡는 것입니다." },
      { "word": "座席", "reading": "ざせき", "meaning": "좌석", "description": "극장이나 기차 따위에 앉도록(座) 마련된 자리(席)입니다." }
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

print("Grade 6 Part 2 data appended successfully.")
