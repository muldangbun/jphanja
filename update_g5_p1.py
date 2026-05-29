import json
import os

new_data = [
  {
    "kanji": "久",
    "reading_on": "キュウ、ク",
    "reading_kun": "ひさ(しい)",
    "meaning": "오랠",
    "components": [
      { "char": "久", "role": "오랠 구 (부수)", "desc": "사람의 등에 뜸을 뜨는 모양에서 유래하여 오랫동안 뜸을 뜬다는 뜻입니다." }
    ],
    "story": "사람의 등에 뜸을 뜰 때 아주 오랫동안 그 기운이 머문다는 데서 시간이 '오래다' 혹은 '길다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "久しぶり", "reading": "ひさしぶり", "meaning": "오랜만", "description": "오래(久)간만에 어떤 일이 일어나는 모양입니다." },
      { "word": "永久", "reading": "えいきゅう", "meaning": "영구", "description": "시간이 한없이 길고(永) 오램(久)을 뜻합니다." }
    ]
  },
  {
    "kanji": "仏",
    "reading_on": "ブツ",
    "reading_kun": "ほとけ",
    "meaning": "부처",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "ム", "role": "마늘 모 (요소)", "desc": "원래 弗(아닐 불)의 생략형으로 발음 '불/부츠'를 담당합니다." }
    ],
    "story": "사람(亻) 중에서 깨달음을 얻어 번뇌를 떨쳐버린(弗의 변형) '부처'나 죽은 사람의 넋을 의미합니다.",
    "example_words": [
      { "word": "仏", "reading": "ほとけ", "meaning": "부처", "description": "불교에서 깨달음을 얻은 사람이나 그 형상입니다." },
      { "word": "仏教", "reading": "ぶっきょう", "meaning": "불교", "description": "부처(仏)의 가르침(教)을 믿는 종교입니다." }
    ]
  },
  {
    "kanji": "仮",
    "reading_on": "カ、ケ",
    "reading_kun": "かり",
    "meaning": "거짓 (임시)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "反", "role": "돌이킬 반 (요소)", "desc": "거꾸로라는 의미를 가지며 여기서는 假(거짓 가)의 약자로 쓰입니다." }
    ],
    "story": "사람(亻)이 얼굴에 뒤집어쓰는(反) 가면처럼 진짜가 아닌 '거짓'이나 '임시'라는 뜻을 지닙니다.",
    "example_words": [
      { "word": "仮", "reading": "かり", "meaning": "임시, 가짜", "description": "잠시 동안만 그렇게 해 두거나 진짜가 아닌 것입니다." },
      { "word": "仮病", "reading": "けびょう", "meaning": "꾀병", "description": "거짓(仮)으로 병(病)이 난 체하는 것입니다." }
    ]
  },
  {
    "kanji": "件",
    "reading_on": "ケン",
    "reading_kun": "",
    "meaning": "물건 (사건)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "牛", "role": "소 우 (요소)", "desc": "소나 물건, 가축을 의미합니다." }
    ],
    "story": "사람(亻)이 키우는 소(牛) 한 마리, 두 마리 세듯 낱개의 물건이나 처리해야 할 '사건'을 세는 단위를 뜻합니다.",
    "example_words": [
      { "word": "事件", "reading": "じけん", "meaning": "사건", "description": "세상에서 일어나는 여러 가지 일(事)이나 일거리(件)입니다." },
      { "word": "条件", "reading": "じょうけん", "meaning": "조건", "description": "어떤 일을 이루기 위해 갖추어야 할 조목(条)과 요건(件)입니다." }
    ]
  },
  {
    "kanji": "任",
    "reading_on": "ニン",
    "reading_kun": "まか(せる)、まか(す)",
    "meaning": "맡길",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "壬", "role": "북방 임 (요소)", "desc": "베틀에서 베를 짜듯 실을 엮는 모양이나 책임을 지는 모습, 발음 '임/닌'을 줍니다." }
    ],
    "story": "사람(亻)이 어떤 일을 책임지고 지도록(壬) 권한을 '맡기다' 혹은 '부임하다'라는 뜻입니다.",
    "example_words": [
      { "word": "任せる", "reading": "まかせる", "meaning": "맡기다", "description": "어떤 일을 남에게 대신하도록 책임 지우는 일입니다." },
      { "word": "責任", "reading": "せきにん", "meaning": "책임", "description": "맡아서(任) 지게 된 꾸지람(責)이나 의무입니다." }
    ]
  },
  {
    "kanji": "似",
    "reading_on": "ジ",
    "reading_kun": "に(る)",
    "meaning": "닮을",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "以", "role": "써 이 (요소)", "desc": "무엇으로써라는 뜻도 있으나, 여기서는 농기구로 땅을 파는 모양이나 발음 '사/지'의 변형 역할을 합니다." }
    ],
    "story": "사람(亻)들의 얼굴이나 모습이 서로 비슷하여(以) 구별하기 어려울 정도로 '닮다'는 의미입니다.",
    "example_words": [
      { "word": "似る", "reading": "にる", "meaning": "닮다, 비슷하다", "description": "모양이나 성질 따위가 서로 비슷한 것입니다." },
      { "word": "似顔絵", "reading": "にがおえ", "meaning": "초상화, 캐리커처", "description": "얼굴(顔)의 특징을 닮게(似) 그린 그림(絵)입니다." }
    ]
  },
  {
    "kanji": "余",
    "reading_on": "ヨ",
    "reading_kun": "あま(る)、あま(す)",
    "meaning": "남을",
    "components": [
      { "char": "人", "role": "사람 인 (부수)", "desc": "여기서는 지붕을 뜻합니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "들보나 기둥을 뜻합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "원래 여덟 팔(八)과 나무 목(木)이 결합된 형태로 넉넉하다는 의미입니다." }
    ],
    "story": "본래 뾰족한 지붕(人)과 기둥(木)이 넉넉하게 지어진 큰 집을 뜻하여, 빈 공간이나 여유가 '남다' 혹은 '나머지'를 의미합니다.",
    "example_words": [
      { "word": "余る", "reading": "あまる", "meaning": "남다", "description": "다 쓰고 난 뒤에 나머지가 생기는 것입니다." },
      { "word": "余裕", "reading": "よゆう", "meaning": "여유", "description": "넉넉하여(裕) 남음(余)이 있는 상태입니다." }
    ]
  },
  {
    "kanji": "価",
    "reading_on": "カ",
    "reading_kun": "あたい",
    "meaning": "값",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 사람의 물건을 뜻합니다." },
      { "char": "西", "role": "서녘 서 (요소)", "desc": "여기서는 장사치가 물건을 팔기 위해 덮어둔 모양(賈의 변형)에서 유래했습니다." }
    ],
    "story": "상인(亻)이 덮어둔 짐(西의 변형)을 풀어 물건을 팔 때 매기는 '값(가격)'이나 '가치'를 뜻합니다.",
    "example_words": [
      { "word": "価格", "reading": "かかく", "meaning": "가격", "description": "물건이 가지는 값(価)이나 가치(格)입니다." },
      { "word": "価値", "reading": "かち", "meaning": "가치", "description": "사물이 지니고 있는 값어치(価, 値)입니다." }
    ]
  },
  {
    "kanji": "保",
    "reading_on": "ホ",
    "reading_kun": "たも(つ)",
    "meaning": "지킬 (보호할)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "呆", "role": "어리석을 매 (요소)", "desc": "원래 아기를 포대기로 싼 모양(𤓽)에서 변형되어 아기를 뜻합니다." }
    ],
    "story": "어른(亻)이 포대기에 싼 아기(呆 변형)를 등이나 가슴에 안고 안전하게 '지키다(보호하다)' 혹은 '유지하다'는 뜻입니다.",
    "example_words": [
      { "word": "保つ", "reading": "たもつ", "meaning": "지키다, 유지하다", "description": "상태가 나빠지지 않게 온전하게 간직하는 일입니다." },
      { "word": "保護", "reading": "ほご", "meaning": "보호", "description": "안전하게 지키고(保) 돌보아(護) 주는 것입니다." }
    ]
  },
  {
    "kanji": "修",
    "reading_on": "シュウ、シュ",
    "reading_kun": "おさ(める)、おさ(まる)",
    "meaning": "닦을",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 의미합니다." },
      { "char": "攸", "role": "바 유 (요소)", "desc": "사람이 물로 몸을 씻는 모양에서 갈고닦는다는 뜻과 발음 '수/슈ウ'를 줍니다." },
      { "char": "彡", "role": "터럭 삼 (요소)", "desc": "아름다운 털이나 장식을 나타냅니다." }
    ],
    "story": "사람(亻)이 물로 깨끗이 씻고(攸) 수염이나 털(彡)을 예쁘게 다듬어 자신의 몸과 마음을 '닦다' 혹은 학문을 갈고닦는다는 뜻입니다.",
    "example_words": [
      { "word": "修める", "reading": "おさめる", "meaning": "닦다, 수양하다", "description": "학문이나 마음을 배우고 갈고닦는 것입니다." },
      { "word": "修理", "reading": "しゅうり", "meaning": "수리", "description": "고장 난 것을 닦고(修) 다듬어(理) 고치는 것입니다." }
    ]
  },
  {
    "kanji": "俵",
    "reading_on": "ヒョウ",
    "reading_kun": "たわら",
    "meaning": "섬 (가마니)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "表", "role": "겉 표 (요소)", "desc": "겉에 옷을 입힌다는 뜻과 발음 '표/히ょう'를 줍니다." }
    ],
    "story": "사람(亻)이 곡식 따위를 짚으로 짠 겉옷(表) 같은 가마니에 담아 포장한 것, 즉 쌀 '섬'이나 '가마니'를 뜻합니다.",
    "example_words": [
      { "word": "俵", "reading": "たわら", "meaning": "가마니, 섬", "description": "짚으로 쳐서 곡식을 담도록 만든 용기입니다." },
      { "word": "土俵", "reading": "どひょう", "meaning": "도효, 씨름판", "description": "일본 씨름(스모)에서 흙을 담은 가마니(俵)를 둥글게 놓아 만든 경기장(土)입니다." }
    ]
  },
  {
    "kanji": "個",
    "reading_on": "コ",
    "reading_kun": "",
    "meaning": "낱 (개인)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 사람과 관련된 낱개를 뜻합니다." },
      { "char": "固", "role": "굳을 고 (요소)", "desc": "단단하고 굳게 뭉쳐진 하나라는 뜻과 발음 '고/코'를 담당합니다." }
    ],
    "story": "여럿이 모인 무리 속에서 단단히(固) 하나씩 떨어져 있는 낱낱의 사람(亻)이나 물건, 즉 '낱개'나 '개인'을 의미합니다.",
    "example_words": [
      { "word": "個人", "reading": "こじん", "meaning": "개인", "description": "단체에 속한 사람(人) 하나하나(個)입니다." },
      { "word": "一個", "reading": "いっこ", "meaning": "한 개", "description": "물건 한(一) 낱개(個)입니다." }
    ]
  },
  {
    "kanji": "備",
    "reading_on": "ビ",
    "reading_kun": "そな(える)、そな(わる)",
    "meaning": "갖출 (준비할)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "艹", "role": "초두머리 (요소)", "desc": "풀이나 채비를 의미합니다." },
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "집이나 창고입니다." },
      { "char": "用", "role": "쓸 용 (요소)", "desc": "쓰이는 도구를 뜻합니다." }
    ],
    "story": "사람(亻)이 활이나 도구(艹, 厂, 用의 결합형)를 미리 창고에 잘 정돈해 두고 쓰임새를 '갖추다' 혹은 '준비하다'는 뜻입니다.",
    "example_words": [
      { "word": "備える", "reading": "そなえる", "meaning": "준비하다, 갖추다", "description": "미리 마련하여 마련해 두는 것입니다." },
      { "word": "準備", "reading": "じゅんび", "meaning": "준비", "description": "필요한 것을 미리 모아(準) 갖추는(備) 일입니다." }
    ]
  },
  {
    "kanji": "像",
    "reading_on": "ゾウ",
    "reading_kun": "",
    "meaning": "형상 (모양)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 사람의 모습을 의미합니다." },
      { "char": "象", "role": "코끼리 상 (요소)", "desc": "코끼리 모양처럼 무언가를 본뜬 형태, 발음 '상/조우'를 줍니다." }
    ],
    "story": "사람(亻)의 모양이나 코끼리(象) 같은 사물의 형태를 본떠 깎아 만든 그림이나 조각상인 '형상'을 의미합니다.",
    "example_words": [
      { "word": "想像", "reading": "そうぞう", "meaning": "상상", "description": "마음속으로 사물의 모양(像)을 생각하여(想) 그려보는 일입니다." },
      { "word": "仏像", "reading": "ぶつぞう", "meaning": "불상", "description": "부처(仏)의 형상(像)을 나무나 돌 등으로 만든 조각입니다." }
    ]
  },
  {
    "kanji": "再",
    "reading_on": "サイ、サ",
    "reading_kun": "ふたた(び)",
    "meaning": "두 번 (다시)",
    "components": [
      { "char": "冂", "role": "멀 경 (부수)", "desc": "여기서는 건물의 틀이나 물건을 묶는 끈입니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "한 번 더라는 의미입니다." }
    ],
    "story": "원래 묶어둔 끈을 한 번(一) 더 묶거나 겹친다는 뜻에서, 어떤 일을 '다시' 하거나 '두 번' 거듭한다는 뜻이 되었습니다.",
    "example_words": [
      { "word": "再び", "reading": "ふたたび", "meaning": "다시, 두 번째", "description": "어떤 일을 거듭하여 다시 하는 모양입니다." },
      { "word": "再来週", "reading": "さくらいしゅう", "meaning": "다다음주", "description": "다음다음으로 다시(再) 오는(来) 주(週)입니다." }
    ]
  },
  {
    "kanji": "刊",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "책 펴낼",
    "components": [
      { "char": "干", "role": "방패 간 (요소)", "desc": "방패나 마른 나무판자를 의미하며 발음 '간/칸'을 줍니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 새기거나 깎는 동작을 뜻합니다." }
    ],
    "story": "나무판자(干) 위에 칼(刂)로 글자를 새겨 넣어 인쇄판을 만들어 책이나 신문을 '펴내다(간행하다)'는 뜻입니다.",
    "example_words": [
      { "word": "刊行", "reading": "かんこう", "meaning": "간행", "description": "책을 펴내어(刊) 세상에 널리 행하는(行) 것입니다." },
      { "word": "朝刊", "reading": "ちょうかん", "meaning": "조간(신문)", "description": "아침(朝)에 펴내는(刊) 신문입니다." }
    ]
  },
  {
    "kanji": "判",
    "reading_on": "ハン、バン",
    "reading_kun": "",
    "meaning": "판단할",
    "components": [
      { "char": "半", "role": "반 반 (요소)", "desc": "소(牛)를 둘로 나눈다는 뜻에서 반, 나눈다는 의미와 발음 '반/한'을 담당합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 자르거나 나눔을 뜻합니다." }
    ],
    "story": "칼(刂)로 사물을 반(半)으로 딱 잘라서 둘을 분명하게 나누듯, 옳고 그름을 명확하게 가르고 '판단하다'는 뜻입니다.",
    "example_words": [
      { "word": "判断", "reading": "はんだん", "meaning": "판단", "description": "사리를 분별하여 가르고(判) 끊어(断) 결정하는 일입니다." },
      { "word": "評判", "reading": "ひょうばん", "meaning": "평판", "description": "세상 사람들의 평가(評)와 판단(判), 즉 소문입니다." }
    ]
  },
  {
    "kanji": "制",
    "reading_on": "セイ",
    "reading_kun": "",
    "meaning": "마를 (억제할 / 제도)",
    "components": [
      { "char": "未", "role": "아닐 미 (요소)", "desc": "여기서는 나뭇가지를 본뜬 글자입니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 나무를 치거나 깎는 동작입니다." }
    ],
    "story": "칼(刂)로 나뭇가지(未의 변형)의 쓸데없는 부분을 깎고 잘라서 알맞게 '마름질하다', 나아가 남의 행동을 깎아 '억제하다'나 규칙인 '제도'를 뜻합니다.",
    "example_words": [
      { "word": "制度", "reading": "せいど", "meaning": "제도", "description": "국가나 사회가 지키도록 마름질하여(制) 법으로 정한 제도(度)입니다." },
      { "word": "制服", "reading": "せいふく", "meaning": "제복, 교복", "description": "규칙으로 입도록 정해진(制) 옷(服)입니다." }
    ]
  },
  {
    "kanji": "券",
    "reading_on": "ケン",
    "reading_kun": "",
    "meaning": "문서 (표)",
    "components": [
      { "char": "龹", "role": "말 권 (요소)", "desc": "손으로 무언가를 둥글게 만다는 의미와 발음 '권/켄'을 줍니다." },
      { "char": "刀", "role": "칼 도 (부수)", "desc": "칼로 나무쪽이나 종이를 자르는 것을 뜻합니다." }
    ],
    "story": "옛날에는 나무쪽에 칼(刀)로 글자를 새긴 뒤 둥글게 말아(龹) 반으로 갈라 나눠 가졌던 증서에서, 어떤 권리를 증명하는 '문서'나 '표(티켓)'를 뜻합니다.",
    "example_words": [
      { "word": "入場券", "reading": "にゅうじょうけん", "meaning": "입장권", "description": "어느 장소에 들어갈(入場) 수 있음을 증명하는 표(券)입니다." },
      { "word": "定期券", "reading": "ていきけん", "meaning": "정기권", "description": "정해진 기간(定期) 동안 탈 수 있는 기차 등의 표(券)입니다." }
    ]
  },
  {
    "kanji": "則",
    "reading_on": "ソク",
    "reading_kun": "",
    "meaning": "법칙",
    "components": [
      { "char": "貝", "role": "조개 패 (부수)", "desc": "솥이나 재물을 뜻합니다." },
      { "char": "刂", "role": "선칼도방 (요소)", "desc": "칼로 새기거나 기준을 잡는 동작입니다." }
    ],
    "story": "청동 솥(貝의 원형)의 겉면에 칼(刂)로 영원히 지켜야 할 법이나 규칙을 새겨 넣은 데서 '법칙'이나 '규칙'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "規則", "reading": "きそく", "meaning": "규칙", "description": "사람들이 다 같이 지키기로 법(規)과 법칙(則)으로 정한 것입니다." },
      { "word": "原則", "reading": "げんそく", "meaning": "원칙", "description": "여러 가지 경우에 두루 적용되는 근본적인(原) 법칙(則)입니다." }
    ]
  },
  {
    "kanji": "効",
    "reading_on": "コウ",
    "reading_kun": "き(く)",
    "meaning": "효험 (효과)",
    "components": [
      { "char": "交", "role": "사귈 교 (요소)", "desc": "사람이 다리를 꼬고 교차한다는 뜻과 발음 '교/코우'를 담당합니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 작용을 뜻합니다." }
    ],
    "story": "힘(力)이나 약 기운이 몸속 깊숙이 엇갈려(交) 들어가 긍정적인 결과를 가져온다는 데서 약의 '효험'이나 '효과가 있다'는 뜻입니다.",
    "example_words": [
      { "word": "効く", "reading": "きく", "meaning": "효과가 있다, 듣다", "description": "약이나 기능 따위가 좋은 작용을 나타내는 것입니다." },
      { "word": "効果", "reading": "こうか", "meaning": "효과", "description": "어떤 행동으로 인해 나타나는 효험(効) 있는 결과(果)입니다." }
    ]
  },
  {
    "kanji": "務",
    "reading_on": "ム",
    "reading_kun": "つと(める)",
    "meaning": "힘쓸 (업무)",
    "components": [
      { "char": "矛", "role": "창 모 (요소)", "desc": "창이나 무기, 힘든 일을 뜻합니다." },
      { "char": "攵", "role": "칠 복 (요소)", "desc": "손으로 무기를 잡거나 치는 동작입니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘을 들여 노력함을 뜻합니다." }
    ],
    "story": "한 손(攵)에 창(矛)을 들고 다른 곳에서 힘(力)을 합쳐 어렵고 힘든 일을 억지로 '힘쓰다(애쓰다)' 혹은 맡은 '업무'를 뜻합니다.",
    "example_words": [
      { "word": "務める", "reading": "つとめる", "meaning": "맡아 하다", "description": "어떤 직책이나 임무를 맡아서 힘쓰는 일입니다." },
      { "word": "事務所", "reading": "じむしょ", "meaning": "사무소, 사무실", "description": "사무(事務)를 보는 곳(所)입니다." }
    ]
  },
  {
    "kanji": "勢",
    "reading_on": "セイ",
    "reading_kun": "いきお(い)",
    "meaning": "형세 (기세)",
    "components": [
      { "char": "埶", "role": "심을 예 (요소)", "desc": "나무를 심거나 형세를 나타내며 발음 '예/세이'를 줍니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 기운을 뜻합니다." }
    ],
    "story": "크게 자란 나무(埶)가 땅에 튼튼하게 뿌리박고 있는 힘(力)차고 억센 기운인 '형세'나 '기세'를 의미합니다.",
    "example_words": [
      { "word": "勢い", "reading": "いきおい", "meaning": "기세, 힘", "description": "뻗어 나가는 힘이나 분위기의 기운입니다." },
      { "word": "大勢", "reading": "おおぜい", "meaning": "많은 사람, 대세", "description": "사람의 기세(勢)가 크고(大) 많은 무리입니다." }
    ]
  },
  {
    "kanji": "厚",
    "reading_on": "コウ",
    "reading_kun": "あつ(い)",
    "meaning": "두터울",
    "components": [
      { "char": "厂", "role": "기슭 엄 (부수)", "desc": "언덕이나 바위를 뜻합니다." },
      { "char": "日", "role": "날 일 (요소)", "desc": "여기서는 햇빛이 아니라 언덕 아래 겹겹이 쌓인 흙 모양을 의미합니다." },
      { "char": "子", "role": "아들 자 (요소)", "desc": "두껍게 쌓인 모양입니다." }
    ],
    "story": "가파른 언덕(厂) 아래에 흙이나 돌덩이가 겹겹이 많이 쌓여 있어서 물건이나 인정이 아주 두껍고 '두텁다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "厚い", "reading": "あつい", "meaning": "두껍다, 두텁다", "description": "물건의 두께가 크거나 사람의 정이 깊은 상태입니다." },
      { "word": "温厚", "reading": "おんこう", "meaning": "온후", "description": "성격이 따뜻하고(温) 정이 두터운(厚) 사람을 칭합니다." }
    ]
  },
  {
    "kanji": "句",
    "reading_on": "ク",
    "reading_kun": "",
    "meaning": "글귀",
    "components": [
      { "char": "勹", "role": "쌀 포 (부수)", "desc": "사람의 몸이나 무언가를 감싸는 모양입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입이나 말, 글귀를 의미합니다." }
    ],
    "story": "말이나 글(口)이 길어지지 않게 한곳에 구부려(勹) 묶어 놓은 짧은 마디인 '글귀'나 구절을 뜻합니다.",
    "example_words": [
      { "word": "句読点", "reading": "くとうてん", "meaning": "구두점", "description": "글귀(句)를 읽기(読) 쉽게 찍는 점(点)입니다." },
      { "word": "俳句", "reading": "はいく", "meaning": "하이쿠", "description": "5·7·5의 17음으로 이뤄진 일본 고유의 짧은 글귀(句) 시입니다." }
    ]
  },
  {
    "kanji": "可",
    "reading_on": "カ",
    "reading_kun": "",
    "meaning": "옳을 (가할)",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "입으로 내는 소리나 허락을 뜻합니다." },
      { "char": "丁", "role": "고무래 정 (요소)", "desc": "숨을 들이마시거나 막힘을 뜻하는 모양에서, 막힘없이 통과한다는 뜻을 줍니다." }
    ],
    "story": "입(口)으로 숨이 편안하게(丁) 나오듯, 어떤 일에 대해 좋다고 허락하거나 '옳다(가하다)'고 인정하는 뜻입니다.",
    "example_words": [
      { "word": "可能", "reading": "かのう", "meaning": "가능", "description": "어떤 일을 할 수 있음(可)과 능력(能)이 있는 것입니다." },
      { "word": "可愛い", "reading": "かわいい", "meaning": "귀엽다", "description": "사랑(愛)스럽고 옳게(可) 여겨지는 사랑스러운 모양입니다." }
    ]
  },
  {
    "kanji": "営",
    "reading_on": "エイ",
    "reading_kun": "いとな(む)",
    "meaning": "경영할",
    "components": [
      { "char": "⺍", "role": "불똥 주 (요소)", "desc": "불빛이나 등불을 의미합니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "천막이나 건물을 뜻합니다." },
      { "char": "呂", "role": "등뼈 려 (요소)", "desc": "척추뼈처럼 연결된 방들을 뜻합니다." }
    ],
    "story": "밤에 등불(⺍)을 켜고 여러 개의 방(呂)이 이어진 큰 천막(冖)을 짓거나 둘러치듯, 사업이나 일을 계획하고 '경영하다'는 의미입니다.",
    "example_words": [
      { "word": "営む", "reading": "いとなむ", "meaning": "경영하다, 종사하다", "description": "일을 계획하여 꾸려나가거나 사업을 하는 것입니다." },
      { "word": "営業", "reading": "えいぎょう", "meaning": "영업", "description": "이익을 목적으로 사업(業)을 경영하는(営) 일입니다." }
    ]
  },
  {
    "kanji": "因",
    "reading_on": "イン",
    "reading_kun": "よ(る)",
    "meaning": "인할",
    "components": [
      { "char": "囗", "role": "큰입구 몸 (부수)", "desc": "사방이 둘러싸인 담장이나 테두리를 뜻합니다." },
      { "char": "大", "role": "큰 대 (요소)", "desc": "사람(大)이 누워있는 모양입니다." }
    ],
    "story": "사람(大)이 담장(囗) 안에 갇혀 빠져나가지 못하고 묶여 있는 모습에서 어떤 일의 바탕이 되는 '원인'이나 까닭(인하다)을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "原因", "reading": "げんいん", "meaning": "원인", "description": "어떤 일을 일으킨 근원(原)과 까닭(因)입니다." },
      { "word": "因る", "reading": "よる", "meaning": "인하다, 말미암다", "description": "어떤 원인이나 까닭으로 인해 일어나는 것입니다." }
    ]
  },
  {
    "kanji": "団",
    "reading_on": "ダン、トン",
    "reading_kun": "",
    "meaning": "둥글 (모일)",
    "components": [
      { "char": "囗", "role": "큰입구 몸 (부수)", "desc": "둥글게 둘러싼 테두리를 의미합니다." },
      { "char": "寸", "role": "마디 촌 (요소)", "desc": "원래 물레를 돌려 실을 뽑는 專(오로지 전)의 약자로, 둥글게 돈다는 뜻입니다." }
    ],
    "story": "물레(寸의 원형)가 둥글게 돌아가듯 사람들이 하나의 테두리(囗) 안에 둥글게 모여 뭉친 모임이나 '단체'를 뜻합니다.",
    "example_words": [
      { "word": "団体", "reading": "だんたい", "meaning": "단체", "description": "같은 목적을 가진 사람들이 모인(団) 모임(体)입니다." },
      { "word": "団地", "reading": "だんち", "meaning": "단지", "description": "집이나 공장이 모여(団) 있는 땅(地)입니다." }
    ]
  },
  {
    "kanji": "圧",
    "reading_on": "アツ",
    "reading_kun": "",
    "meaning": "누를",
    "components": [
      { "char": "厂", "role": "기슭 엄 (부수)", "desc": "언덕이나 낭떠러지를 의미합니다." },
      { "char": "土", "role": "흙 토 (요소)", "desc": "원래 두려워할 염(猒)의 약자로, 위에서 흙더미가 무너져 내린다는 뜻입니다." }
    ],
    "story": "언덕(厂) 위에서 무거운 흙더미(土)가 무너져 내려 사람이나 물건을 꽉 '누르다' 혹은 억누른다는 뜻입니다.",
    "example_words": [
      { "word": "圧力", "reading": "あつりょく", "meaning": "압력", "description": "무거운 것으로 내리누르는(圧) 힘(力)입니다." },
      { "word": "血圧", "reading": "けつあつ", "meaning": "혈압", "description": "피(血)가 혈관을 누르는(圧) 압력입니다." }
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

print("Grade 5 Part 1 data appended successfully.")
