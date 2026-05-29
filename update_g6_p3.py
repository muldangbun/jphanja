import json
import os

new_data = [
  {
    "kanji": "延",
    "reading_on": "エン",
    "reading_kun": "の(びる)、の(べる)、の(ばす)",
    "meaning": "늘일",
    "components": [
      { "char": "廴", "role": "민책받침 (부수)", "desc": "길게 걸어가는 모습을 나타냅니다." },
      { "char": "正", "role": "바를 정 (요소)", "desc": "원래 止(그칠 지)에서 변형된 것으로, 발을 내디딘다는 뜻과 발음 '정/엔'의 변형 역할을 합니다." }
    ],
    "story": "발을 내디뎌(正 변형) 멀리 길게 걸어가는(廴) 모습에서 시간이나 거리를 '늘이다', '연장하다' 혹은 길게 '늘어지다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "延びる", "reading": "のびる", "meaning": "길어지다, 연기되다", "description": "길이나 시간이 본래보다 길게 늘어나거나 미루어지는 것입니다." },
      { "word": "延長", "reading": "えんちょう", "meaning": "연장", "description": "길이나 시간을 길게(長) 늘이는(延) 것입니다." }
    ]
  },
  {
    "kanji": "律",
    "reading_on": "リツ、リチ",
    "reading_kun": "",
    "meaning": "법칙",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "사람이 걷는 길이나 행동을 뜻합니다." },
      { "char": "聿", "role": "붓 율 (요소)", "desc": "손에 붓을 쥐고 글을 쓴다는 뜻과 발음 '율/리츠'를 줍니다." }
    ],
    "story": "사람이 길(彳)을 걷듯 지켜야 할 바른 행동을 붓(聿)으로 써서 정해 놓은 규칙, 즉 '법칙'이나 규율을 뜻합니다.",
    "example_words": [
      { "word": "法律", "reading": "ほうりつ", "meaning": "법률", "description": "국가나 사회에서 꼭 지키도록 정해 놓은 법(法)과 법칙(律)입니다." },
      { "word": "規律", "reading": "きりつ", "meaning": "규율", "description": "사람들이 행동하거나 생활할 때 따르는 규칙(規)과 법(律)입니다." }
    ]
  },
  {
    "kanji": "従",
    "reading_on": "ジュウ",
    "reading_kun": "したが(う)、したが(える)",
    "meaning": "좇을 (따를)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 나아가는 모양을 뜻합니다." },
      { "char": "从", "role": "좇을 종 (요소)", "desc": "두 사람(人人)이 앞뒤로 나란히 따라간다는 뜻을 줍니다." },
      { "char": "止", "role": "그칠 지 (요소)", "desc": "발걸음을 의미합니다." }
    ],
    "story": "길(彳) 위에서 앞사람의 발걸음(止)을 여러 사람(从)이 뒤따라간다는 데서, 남의 뒤를 좇아 '따르다' 혹은 지시에 순응하다는 뜻입니다.",
    "example_words": [
      { "word": "従う", "reading": "したがう", "meaning": "따르다, 좇다", "description": "남의 뒤를 따라가거나 명령이나 규칙에 순응하는 것입니다." },
      { "word": "従順", "reading": "じゅうじゅん", "meaning": "종순, 순종", "description": "남의 뜻을 고분고분하게 따르고(従) 순한(順) 성질입니다." }
    ]
  },
  {
    "kanji": "忘",
    "reading_on": "ボウ",
    "reading_kun": "わす(れる)",
    "meaning": "잊을",
    "components": [
      { "char": "亡", "role": "망할 망 (요소)", "desc": "없어진다는 뜻과 발음 '망/보우'를 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 기억을 뜻합니다." }
    ],
    "story": "마음(心)이나 머릿속에 기억해 둔 것이 사라져 없어져(亡) 버렸다는 데서 '잊다', '망각하다'는 의미입니다.",
    "example_words": [
      { "word": "忘れる", "reading": "わすれる", "meaning": "잊다", "description": "기억해 두었던 것을 머릿속에서 잃어버리거나 생각나지 않게 되는 것입니다." },
      { "word": "忘れ物", "reading": "わすれもの", "meaning": "분실물, 잊은 물건", "description": "어디에 두고 잊어버린(忘れ) 물건(物)입니다." }
    ]
  },
  {
    "kanji": "忠",
    "reading_on": "チュウ",
    "reading_kun": "",
    "meaning": "충성 (충실할)",
    "components": [
      { "char": "中", "role": "가운데 중 (요소)", "desc": "마음의 한가운데, 치우치지 않는다는 뜻과 발음 '중/츄우'를 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음을 의미합니다." }
    ],
    "story": "어느 한쪽으로 치우치지 않고 중심(中)을 잃지 않는 올곧은 마음(心)에서 '충성'이나 '충실하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "忠実", "reading": "ちゅうじつ", "meaning": "충실", "description": "마음이 곧고(忠) 참되어(実) 거짓이 없는 것입니다." },
      { "word": "忠告", "reading": "ちゅうこく", "meaning": "충고", "description": "진심으로(忠) 남의 잘못을 일깨워 알리는(告) 말입니다." }
    ]
  },
  {
    "kanji": "憲",
    "reading_on": "ケン",
    "reading_kun": "",
    "meaning": "법",
    "components": [
      { "char": "宀", "role": "갓머리 (요소)", "desc": "집이나 건물을 뜻합니다." },
      { "char": "目", "role": "눈 목 (요소)", "desc": "눈으로 세심히 살핀다는 뜻입니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 생각을 뜻합니다." }
    ],
    "story": "집(宀) 안에서 눈(目)을 크게 뜨고 마음(心)을 모아 세심하게 살피며 백성을 다스리는 근본 규범, 즉 나라의 으뜸가는 '법(헌법)'을 뜻합니다.",
    "example_words": [
      { "word": "憲法", "reading": "けんぽう", "meaning": "헌법", "description": "국가를 다스리는 가장 바탕이 되는 으뜸 법(憲, 法)입니다." },
      { "word": "違憲", "reading": "いけん", "meaning": "위헌", "description": "법률 따위가 헌법(憲)에 어긋나는(違) 일입니다." }
    ]
  },
  {
    "kanji": "我",
    "reading_on": "ガ",
    "reading_kun": "われ、わ",
    "meaning": "나",
    "components": [
      { "char": "戈", "role": "창 과 (부수)", "desc": "톱니 모양의 흉기나 무기를 의미합니다." }
    ],
    "story": "원래 톱니 모양의 날이 달린 무기를 뜻했으나, 자신을 지키는 무기라는 데서 자신을 뜻하는 '나(자아)'나 '우리'라는 뜻으로 쓰이게 되었습니다.",
    "example_words": [
      { "word": "我", "reading": "われ", "meaning": "나", "description": "말하는 자기 자신을 가리키는 말입니다." },
      { "word": "自我", "reading": "じが", "meaning": "자아", "description": "스스로(自)의 나(我), 즉 자기 자신에 대한 의식입니다." }
    ]
  },
  {
    "kanji": "批",
    "reading_on": "ヒ",
    "reading_kun": "",
    "meaning": "비판할",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 뜻합니다." },
      { "char": "比", "role": "견줄 비 (요소)", "desc": "두 개를 나란히 비교한다는 뜻과 발음 '비/히'를 줍니다." }
    ],
    "story": "손(扌)으로 두 개의 사물을 들고 나란히 비교해(比) 보면서 어느 것이 좋고 나쁜지 '비판하다' 혹은 바로잡는다는 뜻입니다.",
    "example_words": [
      { "word": "批判", "reading": "ひはん", "meaning": "비판", "description": "옳고 그름을 따져서(批) 판단하는(判) 것입니다." },
      { "word": "批評", "reading": "ひひょう", "meaning": "비평", "description": "사물의 좋고 나쁨을 들어(批) 평가하는(評) 일입니다." }
    ]
  },
  {
    "kanji": "担",
    "reading_on": "タン",
    "reading_kun": "にな(う)",
    "meaning": "멜 (담당할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 의미합니다." },
      { "char": "旦", "role": "아침 단 (요소)", "desc": "해가 지평선 위로 떠오르는 아침이라는 뜻과 발음 '단/탄'을 줍니다." }
    ],
    "story": "손(扌)으로 무거운 짐을 어깨에 메어 들어 올리듯(旦), 어떤 책임을 어깨에 '메다' 혹은 일을 '담당하다(떠맡다)'는 의미입니다.",
    "example_words": [
      { "word": "担う", "reading": "になう", "meaning": "메다, 짊어지다", "description": "물건을 어깨에 메거나 어떤 책임이나 임무를 떠맡는 것입니다." },
      { "word": "担当", "reading": "たんとう", "meaning": "담당", "description": "어떤 일을 떠맡아(担) 마땅히 하는(当) 것입니다." }
    ]
  },
  {
    "kanji": "拝",
    "reading_on": "ハイ",
    "reading_kun": "おが(む)",
    "meaning": "절할 (배례할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "𢆉", "role": "두 손으로 바칠 변형 (요소)", "desc": "두 손을 마주 잡거나 받드는 모양을 나타냅니다." }
    ],
    "story": "두 손(扌와 변형)을 앞으로 모아 공손히 받들며 윗사람이나 신에게 허리 굽혀 '절하다', 혹은 우러러보며 숭배한다는 뜻입니다.",
    "example_words": [
      { "word": "拝む", "reading": "おがむ", "meaning": "절하다, 배례하다", "description": "신이나 부처 등에게 두 손을 모아 절하며 비는 것입니다." },
      { "word": "参拝", "reading": "さんぱい", "meaning": "참배", "description": "신사나 절 등에 찾아가서(参) 절하는(拝) 일입니다." }
    ]
  },
  {
    "kanji": "拡",
    "reading_on": "カク",
    "reading_kun": "",
    "meaning": "넓힐",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 동작을 뜻합니다." },
      { "char": "広", "role": "넓을 광 (요소)", "desc": "넓다는 뜻과 발음 '광/카쿠'의 변형 역할을 합니다." }
    ],
    "story": "손(扌)으로 물건의 끝을 잡아당겨 크기나 범위를 널리(広) '넓히다(확장하다)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "拡大", "reading": "かくだい", "meaning": "확대", "description": "모양이나 규모를 넓혀서(拡) 크게(大) 하는 일입니다." },
      { "word": "拡張", "reading": "かくちょう", "meaning": "확장", "description": "세력이나 규모를 넓히고(拡) 늘려 펴는(張) 것입니다." }
    ]
  },
  {
    "kanji": "捨",
    "reading_on": "シャ",
    "reading_kun": "す(てる)",
    "meaning": "버릴",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 뜻합니다." },
      { "char": "舎", "role": "집 사 (요소)", "desc": "쉬어가는 여관이라는 뜻에서 그냥 두고 간다는 의미와 발음 '사/샤'를 줍니다." }
    ],
    "story": "여관(舎)에 머물다 떠날 때 쓸데없는 짐을 손(扌)으로 던져 내버려 두고 가듯, 필요 없는 것을 '버리다'는 뜻입니다.",
    "example_words": [
      { "word": "捨てる", "reading": "すてる", "meaning": "버り다", "description": "필요 없는 물건을 내버리거나 잊어버리는 것입니다." },
      { "word": "四捨五入", "reading": "ししゃごにゅう", "meaning": "사사오입, 반올림", "description": "4까지는 버리고(捨) 5부터는 하나로 올려 넣는(入) 계산법입니다." }
    ]
  },
  {
    "kanji": "探",
    "reading_on": "タン",
    "reading_kun": "さが(す)",
    "meaning": "찾을 (탐구할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 더듬거나 찾는 동작을 뜻합니다." },
      { "char": "罙", "role": "깊을 심 (요소)", "desc": "깊숙한 곳이라는 뜻에서 깊이 파고든다는 의미와 발음 '탐/탄'의 변형 역할을 합니다." }
    ],
    "story": "손(扌)으로 깊고 으슥한 곳(罙)까지 이리저리 더듬으며 숨겨진 물건이나 진리를 깊이 '찾다' 혹은 '탐구하다'는 뜻입니다.",
    "example_words": [
      { "word": "探す", "reading": "さがす", "meaning": "찾다", "description": "잃어버린 물건이나 보이지 않는 사람을 이리저리 뒤져 알아내는 것입니다." },
      { "word": "探検", "reading": "たんけん", "meaning": "탐험", "description": "위험을 무릅쓰고 잘 알려지지 않은 곳을 찾아(探) 조사하는(検) 것입니다." }
    ]
  },
  {
    "kanji": "推",
    "reading_on": "スイ",
    "reading_kun": "",
    "meaning": "밀 (추천할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 뜻합니다." },
      { "char": "隹", "role": "새 추 (요소)", "desc": "새가 날아간다는 뜻에서 앞으로 나아간다는 의미와 발음 '추/스이'를 줍니다." }
    ],
    "story": "손(扌)으로 새(隹)를 날려 보내듯 사람이나 물건을 앞으로 쑥 '밀다(밀어 올리다)', 혹은 좋은 사람을 앞으로 내세워 '추천하다'나 미루어 짐작한다는 뜻입니다.",
    "example_words": [
      { "word": "推薦", "reading": "すいせん", "meaning": "추천", "description": "어떤 사람이나 물건을 앞으로 밀어(推) 천거하는(薦) 일입니다." },
      { "word": "推理", "reading": "すいり", "meaning": "추리", "description": "알고 있는 사실을 바탕으로 미루어(推) 이치(理)를 짐작하는 것입니다." }
    ]
  },
  {
    "kanji": "揮",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "휘두를 (지휘할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 움직이는 동작을 뜻합니다." },
      { "char": "軍", "role": "군사 군 (요소)", "desc": "군대나 군사들이 둥글게 모인 진영이라는 뜻과 발음 '휘/키'의 변형 역할을 합니다." }
    ],
    "story": "장수가 군대(軍) 앞에서 손(扌)에 무기나 깃발을 쥐고 둥글게 '휘두르다' 혹은 군사들을 이끌며 '지휘하다(명령하다)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "指揮", "reading": "しき", "meaning": "지휘", "description": "손가락(指)으로 가리키거나 휘둘러(揮) 여러 사람이나 연주를 이끄는 일입니다." },
      { "word": "発揮", "reading": "はっき", "meaning": "발휘", "description": "가지고 있는 능력이나 기운을 밖으로 드러내어(発) 휘두르는(揮) 것입니다." }
    ]
  },
  {
    "kanji": "操",
    "reading_on": "ソウ",
    "reading_kun": "あやつ(る)",
    "meaning": "잡을 (조종할)",
    "components": [
      { "char": "扌", "role": "재방변 (부수)", "desc": "손으로 하는 행동을 뜻합니다." },
      { "char": "喿", "role": "새 떼지어울 조 (요소)", "desc": "나무(木) 위에 여러 새가 앉아 짹짹 운다(品)는 모양에서 다수라는 뜻과 발음 '조/소우'를 줍니다." }
    ],
    "story": "나무 위에서 시끄럽게 우는 여러 마리의 새(喿)를 다루듯, 손(扌)으로 여러 가지 기계나 사물을 마음대로 꼭 쥐고 '잡다' 혹은 '조종하다(다루다)'는 의미입니다.",
    "example_words": [
      { "word": "操る", "reading": "あやつる", "meaning": "조종하다, 다루다", "description": "기계나 인형, 남의 마음 따위를 자기 뜻대로 능숙하게 움직이는 것입니다." },
      { "word": "体操", "reading": "たいそう", "meaning": "체조", "description": "몸(体)을 단련하기 위해 일정한 동작으로 몸을 움직이고 조작하는(操) 운동입니다." }
    ]
  },
  {
    "kanji": "敬",
    "reading_on": "ケイ",
    "reading_kun": "うやま(う)",
    "meaning": "공경할",
    "components": [
      { "char": "苟", "role": "진실로 구 (요소)", "desc": "말을 삼가고 조심한다는 뜻을 줍니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손에 도구를 쥐고 가볍게 치거나 채찍질하는 동작으로, 행동을 다스린다는 뜻입니다." }
    ],
    "story": "스스로 말이나 행동을 함부로 하지 않게 조심하고(苟) 스스로를 다스리며(攵), 어른이나 훌륭한 사람을 우러러보고 '공경하다'는 뜻입니다.",
    "example_words": [
      { "word": "敬う", "reading": "うやまう", "meaning": "공경하다, 우러러보다", "description": "남을 높여 소중하게 대하고 예의를 갖추는 것입니다." },
      { "word": "尊敬", "reading": "そんけい", "meaning": "존경", "description": "남의 훌륭한 인격을 높이(尊) 받들어 공경하는(敬) 마음입니다." }
    ]
  },
  {
    "kanji": "映",
    "reading_on": "エイ",
    "reading_kun": "うつ(る)、うつ(す)、は(える)",
    "meaning": "비칠",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 빛을 뜻합니다." },
      { "char": "央", "role": "가운데 앙 (요소)", "desc": "한가운데라는 뜻과 발음 '앙/에이'의 변형 역할을 합니다." }
    ],
    "story": "밝은 햇빛(日)이 방 한가운데(央)로 똑바로 들어와 사물의 그림자나 모습이 또렷하게 '비치다' 혹은 물가에 어리다는 뜻을 지닙니다.",
    "example_words": [
      { "word": "映る", "reading": "うつる", "meaning": "비치다", "description": "거울이나 물 등 평평한 표면에 사물의 모습이나 그림자가 나타나는 것입니다." },
      { "word": "映画", "reading": "えいが", "meaning": "영화", "description": "스크린에 빛을 비추어(映) 움직이는 그림(画)을 보여주는 예술입니다." }
    ]
  },
  {
    "kanji": "晩",
    "reading_on": "バン",
    "reading_kun": "",
    "meaning": "늦을 (저녁)",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 시간을 뜻합니다." },
      { "char": "免", "role": "면할 면 (요소)", "desc": "벗어난다는 뜻에서 해가 진다는 의미와 발음 '만/반'을 줍니다." }
    ],
    "story": "해(日)가 서산 너머로 모습을 벗어나(免) 사라지는 때, 즉 하루가 저무는 '늦다' 혹은 '저녁'을 의미합니다.",
    "example_words": [
      { "word": "今晩", "reading": "こんばん", "meaning": "오늘 밤", "description": "오늘(今)의 저녁(晩)이나 밤입니다." },
      { "word": "晩御飯", "reading": "ばんごはん", "meaning": "저녁밥", "description": "저녁(晩)에 먹는 밥(御飯)입니다." }
    ]
  },
  {
    "kanji": "暖",
    "reading_on": "ダン",
    "reading_kun": "あたた(かい)、あたた(まる)、あたた(める)",
    "meaning": "따뜻할",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 햇볕을 의미합니다." },
      { "char": "爰", "role": "이에 원 (요소)", "desc": "원래 불길이나 햇빛이 느슨하게 퍼진다는 뜻과 발음 '원/단'의 변형 역할을 합니다." }
    ],
    "story": "봄날의 햇볕(日)이 온 세상에 느슨하게(爰) 퍼져서 춥지 않고 포근하게 '따뜻하다'는 의미입니다.",
    "example_words": [
      { "word": "暖かい", "reading": "あたたかい", "meaning": "따뜻하다", "description": "춥지도 덥지도 않고 기온이나 햇볕이 기분 좋게 포근한 상태입니다." },
      { "word": "温暖", "reading": "おんだん", "meaning": "온난", "description": "기후가 춥지 않고 온화하며(温) 따뜻한(暖) 모양입니다." }
    ]
  },
  {
    "kanji": "暮",
    "reading_on": "ボ",
    "reading_kun": "く(れる)、く(らす)",
    "meaning": "저물",
    "components": [
      { "char": "莫", "role": "없을 막 (요소)", "desc": "해가 풀숲(艹) 사이로 숨어 없어진다는 뜻과 발음 '막/보'를 줍니다." },
      { "char": "日", "role": "날 일 (부수)", "desc": "해나 날(하루)을 뜻합니다." }
    ],
    "story": "해(日)가 풀숲(莫) 속으로 숨어 사라지는 모습에서 하루해가 져서 날이 '저물다' 혹은 하루하루를 보내며 '살다(생활하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "暮れる", "reading": "くれる", "meaning": "저물だ, 해가 지다", "description": "해가 져서 날이 어두워지거나 한 해가 끝나는 것입니다." },
      { "word": "暮らし", "reading": "くらし", "meaning": "생활, 살림", "description": "날마다 저물기를 반복하며 살아가는 생활입니다." }
    ]
  },
  {
    "kanji": "朗",
    "reading_on": "ロウ",
    "reading_kun": "ほが(らか)",
    "meaning": "밝을",
    "components": [
      { "char": "良", "role": "어질 량 (요소)", "desc": "훌륭하고 좋다는 뜻과 발음 '량/로우'를 줍니다." },
      { "char": "月", "role": "달 월 (부수)", "desc": "달이나 빛을 뜻합니다." }
    ],
    "story": "티 없이 맑고 좋은(良) 밤하늘의 달빛(月)처럼 사방이 환하게 '밝다', 혹은 사람의 표정이나 성격이 구김살 없이 '명랑하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "朗らか", "reading": "ほがらか", "meaning": "명랑하다, 밝다", "description": "성격이나 표정이 구김살 없이 밝고 유쾌한 모양입니다." },
      { "word": "朗読", "reading": "ろうどく", "meaning": "낭독", "description": "소리를 밝고(朗) 크고 분명하게 내어 글을 읽는(読) 것입니다." }
    ]
  },
  {
    "kanji": "机",
    "reading_on": "キ",
    "reading_kun": "つくえ",
    "meaning": "책상 (안석)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 나무로 만든 물건을 뜻합니다." },
      { "char": "几", "role": "안석 궤 (요소)", "desc": "사람이 앉을 때 기대는 방석이나 작은 책상 모양입니다." }
    ],
    "story": "나무(木)로 다리를 만들어(几) 책을 읽거나 글씨를 쓸 때 앞에 두고 쓰는 '책상'이나 기대는 도구를 의미합니다.",
    "example_words": [
      { "word": "机", "reading": "つくえ", "meaning": "책상", "description": "글을 읽거나 쓸 때 앞에 놓고 쓰는 상입니다." },
      { "word": "机上", "reading": "きじょう", "meaning": "기상, 탁상", "description": "책상(机)의 위(上), 즉 실제가 아닌 이론뿐인 상태를 가리킬 때 씁니다." }
    ]
  },
  {
    "kanji": "枚",
    "reading_on": "マイ",
    "reading_kun": "",
    "meaning": "낱장 (매)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 나뭇가지를 뜻합니다." },
      { "char": "攴", "role": "칠 복 (요소)", "desc": "원래 작은 나무 막대기를 뜻하는 毎(매양 매)의 변형으로 쓰여, 얇은 것이라는 의미와 발음 '매/마이'를 줍니다." }
    ],
    "story": "원래는 나무(木)의 잔가지나 작은 나무 팻말을 뜻했으나, 팻말처럼 얇고 평평한 물건, 특히 종이나 널빤지를 세는 단위인 '낱장'이나 '매'로 뜻이 바뀌었습니다.",
    "example_words": [
      { "word": "一枚", "reading": "いちまい", "meaning": "한 장", "description": "종이나 천 등 얇고 평평한 물건의 한(一) 장(枚)을 말합니다." },
      { "word": "枚数", "reading": "まいすう", "meaning": "매수, 장수", "description": "종이나 천 따위의 낱장(枚)의 수(数)입니다." }
    ]
  },
  {
    "kanji": "染",
    "reading_on": "セン",
    "reading_kun": "そ(める)、そ(まる)、し(みる)",
    "meaning": "물들일 (염색할)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "九", "role": "아홉 구 (요소)", "desc": "여러 가지 빛깔을 뜻합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "염료를 짜내는 나무나 풀을 뜻합니다." }
    ],
    "story": "나무나 풀(木)에서 즙을 짜낸 물(氵)에 천을 담가 여러 번(九) 주물러서 색깔을 '물들이다' 혹은 '염색하다'는 뜻입니다.",
    "example_words": [
      { "word": "染める", "reading": "そめる", "meaning": "물들이다, 염색하다", "description": "천이나 머리카락 등에 색깔이 배어들게 하는 것입니다." },
      { "word": "感染", "reading": "かんせん", "meaning": "감염", "description": "세균이나 병이 몸에 옮아(感) 물드는(染) 것입니다." }
    ]
  },
  {
    "kanji": "株",
    "reading_on": "シュ",
    "reading_kun": "かぶ",
    "meaning": "그루 (주식)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무나 식물을 뜻합니다." },
      { "char": "朱", "role": "붉을 주 (요소)", "desc": "나무의 속이 붉다는 뜻에서 중심이라는 의미와 발음 '주/슈'를 줍니다." }
    ],
    "story": "줄기를 잘라낸 나무(木)의 밑동이나 붉은 뿌리(朱) 부분에서 식물을 세는 단위인 '포기(그루)'를 뜻하며, 기업의 권리를 나누는 단위인 '주식(주)'을 뜻하기도 합니다.",
    "example_words": [
      { "word": "株", "reading": "かぶ", "meaning": "포기, 주식", "description": "나무의 밑동이나, 주식회사의 자본을 똑같이 나눈 단위입니다." },
      { "word": "株式", "reading": "かぶしき", "meaning": "주식", "description": "주식회사에서 자본금을 일정한 격식(式)에 따라 똑같이 나눈 주(株)입니다." }
    ]
  },
  {
    "kanji": "棒",
    "reading_on": "ボウ",
    "reading_kun": "",
    "meaning": "막대",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "奉", "role": "받들 봉 (요소)", "desc": "손으로 받들어 쥔다는 뜻과 발음 '봉/보우'를 줍니다." }
    ],
    "story": "두 손으로 길게 받들어(奉) 쥐고 쓰는 나무(木)로 만든 자루나 '막대기'를 의미합니다.",
    "example_words": [
      { "word": "棒", "reading": "ぼう", "meaning": "막대기", "description": "나무나 쇠 등으로 가늘고 길게 만든 도구입니다." },
      { "word": "泥棒", "reading": "どろぼう", "meaning": "도둑", "description": "남의 물건을 훔치는 사람을 가리킵니다. (발음을 빌려 쓴 한자)" }
    ]
  },
  {
    "kanji": "模",
    "reading_on": "モ、ボ",
    "reading_kun": "",
    "meaning": "본뜰",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무로 만든 틀이나 거푸집을 뜻합니다." },
      { "char": "莫", "role": "없을 막 (요소)", "desc": "보이지 않는다는 뜻에서 덮거나 가린다는 의미와 발음 '막/모'를 줍니다." }
    ],
    "story": "진흙 같은 것이 보이지 않게(莫) 나무(木)로 만든 거푸집을 덮어씌워 똑같은 모양을 '본뜨다' 혹은 일정한 '틀(모양)'을 뜻합니다.",
    "example_words": [
      { "word": "模様", "reading": "もよう", "meaning": "무늬, 모양", "description": "사물의 겉에 나타난 본뜬(模) 모양(様)이나 얼룩입니다." },
      { "word": "規模", "reading": "きぼ", "meaning": "규모", "description": "조직이나 사물의 겉으로 나타난 크기나 틀(模)입니다." }
    ]
  },
  {
    "kanji": "権",
    "reading_on": "ケン、ゴン",
    "reading_kun": "",
    "meaning": "권세 (권리)",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." },
      { "char": "雚", "role": "황새 관 (요소)", "desc": "새가 높이 날아 세상을 살핀다는 뜻과 발음 '관/켄'의 변형 역할을 합니다." }
    ],
    "story": "원래는 무게를 다는 나무(木) 저울의 추를 뜻했으나, 저울이 어느 한쪽으로 기우는 것처럼 세상을 좌지우지하는 힘인 '권세'나 마땅히 누릴 '권리'로 뜻이 커졌습니다.",
    "example_words": [
      { "word": "権利", "reading": "けんり", "meaning": "권리", "description": "어떤 일을 마음대로 할 수 있는 힘(権)과 이익(利)입니다." },
      { "word": "権力", "reading": "けんりょく", "meaning": "권력", "description": "남을 강제로 따르게 하는 권세(権)와 힘(力)입니다." }
    ]
  },
  {
    "kanji": "樹",
    "reading_on": "ジュ",
    "reading_kun": "",
    "meaning": "나무",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 뜻합니다." },
      { "char": "尌", "role": "세울 주 (요소)", "desc": "북을 세워 놓는다는 뜻에서 단단히 심어 세운다는 의미와 발음 '주/쥬'를 줍니다." }
    ],
    "story": "흙에 단단히 심어서 꼿꼿하게 세워 둔(尌) 자라나는 '나무'나 숲을 뜻하며, 근본을 굳게 세운다는 뜻도 가집니다.",
    "example_words": [
      { "word": "樹木", "reading": "じゅもく", "meaning": "수목, 나무", "description": "살아서 자라고 있는 여러 나무(樹, 木)들입니다." },
      { "word": "果樹園", "reading": "かじゅえん", "meaning": "과수원", "description": "과일(果)이 열리는 나무(樹)를 심어 기르는 밭(園)입니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade6.json'
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

print("Grade 6 Part 3 data appended successfully.")
