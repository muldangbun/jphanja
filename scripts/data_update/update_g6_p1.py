import json
import os

new_data = [
  {
    "kanji": "並",
    "reading_on": "ヘイ",
    "reading_kun": "なみ、なら(べる)、なら(ぶ)、なら(びに)",
    "meaning": "나란할",
    "components": [
      { "char": "立", "role": "설 립 (요소)", "desc": "사람이 똑바로 서 있는 모양입니다. (원래 竝이 변형됨)" },
      { "char": "一", "role": "한 일 (부수)", "desc": "하나로 줄을 맞춘다는 뜻입니다." }
    ],
    "story": "두 사람이 똑같이 나란히(竝) 서 있는 모양에서 한 줄로 똑바르게 '나란하다' 혹은 쭉 '늘어서다'는 뜻입니다.",
    "example_words": [
      { "word": "並ぶ", "reading": "ならぶ", "meaning": "늘어서다, 나란히 서다", "description": "여럿이 줄을 지어 나란하게 서는 것입니다." },
      { "word": "並行", "reading": "へいこう", "meaning": "병행", "description": "나란히(並) 줄지어 나아가는(行) 일입니다." }
    ]
  },
  {
    "kanji": "乱",
    "reading_on": "ラン",
    "reading_kun": "みだ(れる)、みだ(す)",
    "meaning": "어지러울",
    "components": [
      { "char": "舌", "role": "혀 설 (요소)", "desc": "여기서는 원래 실패에 엉킨 실(𤔔) 모양이 간략화된 것입니다." },
      { "char": "乙", "role": "새 을 (부수)", "desc": "굽은 끈이나 갈고리 모양을 뜻하여 얽힌 것을 푸는 도구입니다." }
    ],
    "story": "실패에 이리저리 엉킨 실(舌 변형)을 손(乙)으로 풀려고 애쓰는 모양에서 몹시 뒤엉켜 '어지럽다' 혹은 '문란하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "乱れる", "reading": "みだれる", "meaning": "어지러워지다, 흐트러지다", "description": "질서나 마음이 뒤죽박죽으로 어지럽게 되는 것입니다." },
      { "word": "混乱", "reading": "こんらん", "meaning": "혼란", "description": "여러 가지가 뒤섞여(混) 어지러운(乱) 상태입니다." }
    ]
  },
  {
    "kanji": "乳",
    "reading_on": "ニュウ",
    "reading_kun": "ちち、ち",
    "meaning": "젖",
    "components": [
      { "char": "孚", "role": "미쁠 부 (요소)", "desc": "손으로 아이를 감싸 안은 모양을 뜻합니다." },
      { "char": "乙", "role": "새 을 (부수)", "desc": "여기서는 새나 제비 모양으로 젖가슴을 나타냅니다. (원래 乚의 형태)" }
    ],
    "story": "어머니가 아기(孚)를 안고 젖가슴(乙)을 물려 '젖'을 먹이는 모양을 본뜬 글자입니다.",
    "example_words": [
      { "word": "牛乳", "reading": "ぎゅうにゅう", "meaning": "우유", "description": "소(牛)의 젖(乳)입니다." },
      { "word": "乳", "reading": "ちち", "meaning": "젖", "description": "어머니나 동물의 암컷 가슴에서 나는 하얀 액체입니다." }
    ]
  },
  {
    "kanji": "亡",
    "reading_on": "ボウ、モウ",
    "reading_kun": "な(い)",
    "meaning": "망할 (없을)",
    "components": [
      { "char": "亠", "role": "돼지해머리 (부수)", "desc": "어떤 물건을 덮거나 감춘다는 뜻입니다." },
      { "char": "𠃊", "role": "숨을 은 (요소)", "desc": "보이지 않게 숨어 버린다는 뜻입니다." }
    ],
    "story": "어떤 물건이나 사람이 보이지 않게(亠) 훌쩍 숨어(𠃊) 버려 완전히 '없어지다' 혹은 사람이 죽어 '망하다(죽다)'는 뜻입니다.",
    "example_words": [
      { "word": "亡くなる", "reading": "なくなる", "meaning": "돌아가시다, 죽다", "description": "세상을 떠나서 이 세상에 없게 되는 것입니다." },
      { "word": "死亡", "reading": "しぼう", "meaning": "사망", "description": "목숨이 끊어져 죽어서(死) 없어지는(亡) 것입니다." }
    ]
  },
  {
    "kanji": "仁",
    "reading_on": "ジン、ニ",
    "reading_kun": "",
    "meaning": "어질",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "二", "role": "두 이 (요소)", "desc": "두 사람 사이의 관계라는 뜻과 발음 '이/니'를 줍니다." }
    ],
    "story": "두(二) 사람(亻) 이상이 모여 살 때 서로 아끼고 친하게 지내는 착한 마음, 즉 '어질다' 혹은 '어짊'을 뜻합니다.",
    "example_words": [
      { "word": "仁愛", "reading": "じんあい", "meaning": "인애", "description": "어질고(仁) 자애롭게 사랑하는(愛) 마음입니다." },
      { "word": "仁義", "reading": "じんぎ", "meaning": "인의", "description": "어질고(仁) 의로운(義) 사람의 도리입니다." }
    ]
  },
  {
    "kanji": "供",
    "reading_on": "キョウ、ク",
    "reading_kun": "そな(える)、とも",
    "meaning": "이바지할 (바칠)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "共", "role": "함께 공 (요소)", "desc": "두 손으로 물건을 함께 받쳐 든다는 뜻과 발음 '공/쿄우'를 줍니다." }
    ],
    "story": "사람(亻)이 윗사람이나 신에게 물건을 두 손으로 받쳐 들어(共) 정성껏 '바치다' 혹은 함께 따라다니는 '동반자(아이)'를 뜻합니다.",
    "example_words": [
      { "word": "子供", "reading": "こども", "meaning": "아이", "description": "나이가 어린 아이(子)나 자식입니다. (供는 복수나 동반의 의미로 쓰임)" },
      { "word": "提供", "reading": "ていきょう", "meaning": "제공", "description": "물건이나 의견을 내놓아(提) 남에게 바치고 이바지하는(供) 일입니다." }
    ]
  },
  {
    "kanji": "俳",
    "reading_on": "ハイ",
    "reading_kun": "",
    "meaning": "배우",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 사람의 직업을 뜻합니다." },
      { "char": "非", "role": "아닐 비 (요소)", "desc": "진짜가 아니라는 뜻에서 가짜 역할을 한다는 의미와 발음 '비/하이'를 줍니다." }
    ],
    "story": "자신의 진짜 모습이 아닌(非) 가짜 인물을 흉내 내는 사람(亻), 즉 연기하는 광대나 '배우'를 뜻합니다.",
    "example_words": [
      { "word": "俳優", "reading": "はいゆう", "meaning": "배우", "description": "연극이나 영화 등에서 광대(俳)나 훌륭한 인물(優)의 역을 맡아 연기하는 사람입니다." },
      { "word": "俳句", "reading": "はいく", "meaning": "하이쿠", "description": "일본 고유의 짧고 재미있는(俳) 시구(句)입니다." }
    ]
  },
  {
    "kanji": "値",
    "reading_on": "チ",
    "reading_kun": "ね、あたい",
    "meaning": "값 (가치)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람이나 사람의 물건을 뜻합니다." },
      { "char": "直", "role": "곧을 직 (요소)", "desc": "가치를 똑바로 매긴다는 뜻과 발음 '치/치'를 줍니다." }
    ],
    "story": "사람(亻)이 사고파는 물건의 올바른(直) 가격을 매긴 '값'이나 '가치'를 의미합니다.",
    "example_words": [
      { "word": "価値", "reading": "かち", "meaning": "가치", "description": "사물이 지니고 있는 값(価)어치나 값(値)입니다." },
      { "word": "値段", "reading": "ねだん", "meaning": "값, 가격", "description": "물건의 값(値)을 매겨 놓은 단계(段)입니다." }
    ]
  },
  {
    "kanji": "傷",
    "reading_on": "ショウ",
    "reading_kun": "きず、いた(む)、いた(める)",
    "meaning": "상할 (다칠)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "𠂉", "role": "사람 인 엎드린 모양 (요소)", "desc": "화살이나 무기를 뜻합니다." },
      { "char": "昜", "role": "볕 양 (요소)", "desc": "태양 아래 드러난다는 뜻과 발음 '양/쇼우'의 변형 역할을 합니다." }
    ],
    "story": "사람(亻)이 날카로운 무기(𠂉)에 맞아 몸에 피가 날 정도로 크게 '다치다(상하다)' 혹은 몸의 '상처'를 의미합니다.",
    "example_words": [
      { "word": "傷", "reading": "きず", "meaning": "상처, 흠", "description": "다쳐서 찢어지거나 흠집이 난 곳입니다." },
      { "word": "負傷", "reading": "ふしょう", "meaning": "부상", "description": "다쳐서 상처(傷)를 입는(負) 것입니다." }
    ]
  },
  {
    "kanji": "優",
    "reading_on": "ユウ",
    "reading_kun": "やさ(しい)、すぐ(れる)",
    "meaning": "넉넉할 (뛰어날)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람을 뜻합니다." },
      { "char": "憂", "role": "근심 우 (요소)", "desc": "근심하거나 부드럽게 생각한다는 뜻과 발음 '우/유우'를 줍니다." }
    ],
    "story": "사람(亻)이 남의 근심(憂)을 함께 걱정해 줄 만큼 마음이 착하고 '다정하다(상냥하다)' 혹은 남보다 재주가 '뛰어나다'는 뜻입니다.",
    "example_words": [
      { "word": "優しい", "reading": "やさしい", "meaning": "다정하다, 상냥하다", "description": "마음씨가 부드럽고 친절한 것입니다." },
      { "word": "優秀", "reading": "ゆうしゅう", "meaning": "우수", "description": "남보다 넉넉하게 뛰어나고(優) 훌륭한(秀) 것입니다." }
    ]
  },
  {
    "kanji": "党",
    "reading_on": "トウ",
    "reading_kun": "",
    "meaning": "무리 (당)",
    "components": [
      { "char": "尚", "role": "오히려 상 (요소)", "desc": "우러른다는 뜻과 발음 '상/토우'의 변형 역할을 합니다. (원래 黨 자의 줄임말)" },
      { "char": "儿", "role": "어진사람 인 (부수)", "desc": "사람을 뜻합니다." }
    ],
    "story": "뜻이 같거나 한 사람을 우러러보는(尚) 사람들(儿)이 한데 모여 이룬 '무리'나 정치적인 '당'을 의미합니다.",
    "example_words": [
      { "word": "政党", "reading": "せいとう", "meaning": "정당", "description": "정치(政)에 뜻을 같이하는 사람들의 무리(党)입니다." },
      { "word": "悪党", "reading": "あくとう", "meaning": "악당", "description": "나쁜(悪) 짓을 일삼는 무리(党)입니다." }
    ]
  },
  {
    "kanji": "冊",
    "reading_on": "サツ、サク",
    "reading_kun": "",
    "meaning": "책 (권)",
    "components": [
      { "char": "冂", "role": "멀 경 (부수)", "desc": "여기서는 대나무 조각들을 나란히 묶은 끈을 뜻합니다." },
      { "char": "冊", "role": "책 책 (요소)", "desc": "대나무 조각(죽간)을 가죽끈으로 나란히 묶어놓은 옛날 책 모양입니다." }
    ],
    "story": "글을 적은 여러 개의 얇은 대나무 조각을 끈(冂)으로 나란히 엮어 만든 옛날의 '책'이나 책을 세는 단위인 '권'을 뜻합니다.",
    "example_words": [
      { "word": "冊子", "reading": "さっし", "meaning": "책자, 팸플릿", "description": "글을 엮어 만든 작고 얇은 책(冊)입니다." },
      { "word": "一冊", "reading": "いっさつ", "meaning": "한 권", "description": "책 한(一) 권(冊)을 세는 말입니다." }
    ]
  },
  {
    "kanji": "処",
    "reading_on": "ショ",
    "reading_kun": "",
    "meaning": "곳 (처리할)",
    "components": [
      { "char": "夂", "role": "뒤져올 치 (요소)", "desc": "발걸음을 늦춘다는 뜻에서 멈춘다는 의미를 줍니다." },
      { "char": "几", "role": "안석 궤 (부수)", "desc": "기대어 앉는 방석이나 자리(곳)를 뜻합니다." }
    ],
    "story": "걸어가던 발걸음을 멈추고(夂) 자리(几)에 앉아 쉬는 '곳(장소)'이거나, 한곳에 머무르며 일을 알맞게 '처리하다'는 뜻입니다.",
    "example_words": [
      { "word": "処理", "reading": "しょり", "meaning": "처리", "description": "일을 사리에 맞게 다스려(理) 마무리(処)하는 일입니다." },
      { "word": "処罰", "reading": "しょばつ", "meaning": "처벌", "description": "죄를 지은 사람에게 벌(罰)을 주는(処) 일입니다." }
    ]
  },
  {
    "kanji": "刻",
    "reading_on": "コク",
    "reading_kun": "きざ(む)",
    "meaning": "새길",
    "components": [
      { "char": "亥", "role": "돼지 해 (요소)", "desc": "동물의 뼈대나 뿌리라는 뜻과 발음 '해/코쿠'의 변형 역할을 합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 깎거나 파는 동작을 의미합니다." }
    ],
    "story": "단단한 뼈나 나무(亥)에 칼(刂)로 글자나 무늬를 깊이 파서 '새기다', 혹은 시간을 잘게 쪼개어 새긴다는 데서 '시각'을 뜻합니다.",
    "example_words": [
      { "word": "刻む", "reading": "きざむ", "meaning": "새ぎ다, 잘게 썰다", "description": "글씨를 파서 새기거나 채소 등을 칼로 잘게 자르는 것입니다." },
      { "word": "遅刻", "reading": "ちこく", "meaning": "지각", "description": "정해진 시각(刻)보다 늦게(遅) 도착하는 것입니다." }
    ]
  },
  {
    "kanji": "割",
    "reading_on": "カツ",
    "reading_kun": "わ(る)、わ(れる)、わ(り)、さ(く)",
    "meaning": "나눌 (벨)",
    "components": [
      { "char": "害", "role": "해할 해 (요소)", "desc": "상처를 낸다는 뜻과 발음 '해/카츠'의 변형 역할을 줍니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 자르거나 나누는 동작입니다." }
    ],
    "story": "사물에 칼(刂)을 대어 틈을 내어(害) 여러 조각으로 쪼개고 '나누다(할당하다)' 혹은 깨뜨린다는 의미입니다.",
    "example_words": [
      { "word": "割る", "reading": "わる", "meaning": "나누다, 깨뜨리다", "description": "하나를 여러 몫으로 나누거나 유리 따위를 깨는 것입니다." },
      { "word": "割引", "reading": "わりびき", "meaning": "할인", "description": "원래 값에서 일정한 몫(割)을 빼고(引) 싸게 파는 일입니다." }
    ]
  },
  {
    "kanji": "創",
    "reading_on": "ソウ",
    "reading_kun": "",
    "meaning": "비롯할 (창조할)",
    "components": [
      { "char": "倉", "role": "곳집 창 (요소)", "desc": "창고를 뜻하며 발음 '창/소우'를 줍니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 무언가를 베어 처음 시작한다는 뜻을 줍니다." }
    ],
    "story": "칼(刂)로 나무를 베어 창고(倉) 같은 집을 처음 짓기 시작한다는 데서, 없던 것을 처음 '비롯하다(만들다)' 혹은 '창조하다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "創造", "reading": "そうぞう", "meaning": "창조", "description": "새로운 것을 처음으로 비롯하여(創) 만들어(造) 내는 일입니다." },
      { "word": "創立", "reading": "そうりつ", "meaning": "창립", "description": "조직이나 기관을 처음으로 세우는(立) 것입니다." }
    ]
  },
  {
    "kanji": "劇",
    "reading_on": "ゲキ",
    "reading_kun": "",
    "meaning": "심할 (연극)",
    "components": [
      { "char": "虍", "role": "범호엄 (요소)", "desc": "호랑이처럼 호랑이의 거세고 심한 동작을 뜻합니다." },
      { "char": "豕", "role": "돼지 시 (요소)", "desc": "멧돼지처럼 사나운 짐승을 뜻합니다." },
      { "char": "刂", "role": "선칼도방 (부수)", "desc": "칼로 무언가를 자르듯 치열한 다툼을 뜻합니다." }
    ],
    "story": "호랑이(虍)와 멧돼지(豕)가 날카로운 발톱(칼 刂)을 세우고 치열하게 다투는 모양에서 '심하다'는 뜻이 되었고, 나중에는 배우들이 무대 위에서 치열하게 연기하는 '연극'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "演劇", "reading": "えんげき", "meaning": "연극", "description": "배우가 무대 위에서 이야기의 배역을 맡아 연기(演)하는 일(劇)입니다." },
      { "word": "劇的", "reading": "げきてき", "meaning": "극적", "description": "일의 상황이 연극(劇)처럼 몹시 놀랍고 심한 모양입니다." }
    ]
  },
  {
    "kanji": "勤",
    "reading_on": "キン、ゴン",
    "reading_kun": "つと(める)、つと(まる)",
    "meaning": "부지런할 (근무할)",
    "components": [
      { "char": "菫", "role": "진흙 근 (요소)", "desc": "진흙처럼 끈기가 있다는 뜻과 발음 '근/킨'을 줍니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘을 쓰거나 애쓰는 동작입니다." }
    ],
    "story": "어떤 일을 할 때 진흙(菫)처럼 끈기 있게 힘(力)을 다하여 '부지런하다' 혹은 애써 일하며 '근무하다'는 의미입니다.",
    "example_words": [
      { "word": "勤める", "reading": "つとめる", "meaning": "근무하다", "description": "직장에 소속되어 일정한 시간 동안 일을 맡아 하는 것입니다." },
      { "word": "通勤", "reading": "つうきん", "meaning": "통근", "description": "일하러(勤) 직장에 다니는(通) 것입니다." }
    ]
  },
  {
    "kanji": "危",
    "reading_on": "キ",
    "reading_kun": "あぶ(ない)、あや(うい)",
    "meaning": "위태할",
    "components": [
      { "char": "厄", "role": "액 액 (요소)", "desc": "언덕(厂) 위에서 무릎을 꿇고 있는 모양으로 위험한 상태를 뜻합니다." },
      { "char": "卩", "role": "병부 절 (부수)", "desc": "사람이 잔뜩 웅크리고 있는 모습을 뜻합니다." }
    ],
    "story": "높고 험한 벼랑 끝(厄)에서 사람이 떨어질까 두려워 몸을 웅크리고(卩) 있는 아슬아슬하고 '위태하다(위험하다)'는 뜻입니다.",
    "example_words": [
      { "word": "危ない", "reading": "あぶない", "meaning": "위험하다, 위태롭다", "description": "안전하지 않아 다치거나 해를 입을 것 같은 상태입니다." },
      { "word": "危険", "reading": "きけん", "meaning": "위험", "description": "위태롭고(危) 험하여(険) 안전하지 못한 일이나 상태입니다." }
    ]
  },
  {
    "kanji": "卵",
    "reading_on": "ラン",
    "reading_kun": "たまご",
    "meaning": "알",
    "components": [
      { "char": "卩", "role": "병부 절 (부수)", "desc": "여기서는 개구리나 벌레 따위가 낳은 알들이 뭉쳐 있는 모양(알 란)을 뜻합니다." }
    ],
    "story": "물고기나 벌레, 개구리 등이 한가득 낳아 뭉쳐 놓은 '알'의 모양을 본뜬 글자입니다.",
    "example_words": [
      { "word": "卵", "reading": "たまご", "meaning": "알, 계란", "description": "새나 물고기 따위가 낳은 둥근 알입니다." },
      { "word": "卵焼き", "reading": "たまごやき", "meaning": "달걀부침, 계란말이", "description": "달걀(卵)을 풀어서 불에 구운(焼き) 요리입니다." }
    ]
  },
  {
    "kanji": "厳",
    "reading_on": "ゲン、ゴン",
    "reading_kun": "きび(しい)",
    "meaning": "엄할",
    "components": [
      { "char": "ツ", "role": "머리 (요소)", "desc": "원래 바위 언덕(厂)에 튀어나온 험악한 돌무더기의 모양(吅)이 변형된 것입니다." },
      { "char": "厂", "role": "기슭 엄 (부수)", "desc": "언덕이나 바위를 뜻합니다." },
      { "char": "敢", "role": "감히 감 (요소)", "desc": "억세게 감행한다는 뜻으로 두렵고 강하다는 의미와 발음 '감/겐'의 변형을 줍니다." }
    ],
    "story": "크고 험상궂은 바위 언덕(厂)처럼 굳세고 두려우며(敢), 규칙이나 성격이 매우 맵짜고 '엄격하다'는 뜻입니다.",
    "example_words": [
      { "word": "厳しい", "reading": "きびしい", "meaning": "엄하다, 엄격하다", "description": "규칙이나 성격이 몹시 엄격하고 철저한 상태입니다." },
      { "word": "厳格", "reading": "げんかく", "meaning": "엄격", "description": "기준이나 격식(格)이 조금도 용서 없이 엄한(厳) 것입니다." }
    ]
  },
  {
    "kanji": "収",
    "reading_on": "シュウ",
    "reading_kun": "おさ(める)、おさ(まる)",
    "meaning": "거둘",
    "components": [
      { "char": "丩", "role": "얽힐 구 (요소)", "desc": "실이 엉켜 있는 모양에서 얽는다는 뜻입니다." },
      { "char": "又", "role": "또 우 (부수)", "desc": "손으로 하는 행동을 의미합니다." }
    ],
    "story": "가을이 되어 밭에서 농작물(丩 변형)을 손(又)으로 얽어 잡아당겨 한곳에 모아 '거두다(수확하다)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "収める", "reading": "おさめる", "meaning": "거두다, 얻다", "description": "이익이나 결과를 거두어들이거나 속에 집어넣는 것입니다." },
      { "word": "吸収", "reading": "きゅうしゅう", "meaning": "흡수", "description": "물기나 기운을 빨아(吸) 거두어들이는(収) 일입니다." }
    ]
  },
  {
    "kanji": "后",
    "reading_on": "コウ",
    "reading_kun": "",
    "meaning": "왕후 (뒤)",
    "components": [
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "원래 웅크린 사람이나 덮개 모양입니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입으로 명령을 내리는 모양입니다." }
    ],
    "story": "웅크리고 앉아(厂) 입(口)으로 아랫사람에게 명령을 내리는 높은 사람, 즉 임금이나 '왕후'를 뜻하며, 나중에 '뒤'를 뜻하는 後 자와 통용되기도 했습니다.",
    "example_words": [
      { "word": "皇后", "reading": "こうごう", "meaning": "황후", "description": "황제(皇)의 정실 아내(后)입니다." },
      { "word": "母后", "reading": "ぼこう", "meaning": "모후", "description": "임금의 어머니(母)인 왕대비입니다." }
    ]
  },
  {
    "kanji": "否",
    "reading_on": "ヒ",
    "reading_kun": "いな",
    "meaning": "아닐 (부정할)",
    "components": [
      { "char": "不", "role": "아닐 불 (요소)", "desc": "아니다라는 부정을 뜻하며 발음 '불/히'의 변형 역할을 합니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 말하는 것을 뜻합니다." }
    ],
    "story": "남의 제안이나 말에 대해 입(口)으로 '아니다(不)'라고 말하여 딱 잘라 '부정하다'는 뜻을 지닙니다.",
    "example_words": [
      { "word": "否定", "reading": "ひてい", "meaning": "부정", "description": "그렇지 아니하다고(否) 딱 잘라 정하여(定) 말하는 것입니다." },
      { "word": "賛否", "reading": "さんぴ", "meaning": "찬부 (찬반)", "description": "어떤 일에 찬성(賛)함과 그렇지 않음(否)입니다." }
    ]
  },
  {
    "kanji": "吸",
    "reading_on": "キュウ",
    "reading_kun": "す(う)",
    "meaning": "마실 (숨쉴)",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 호흡을 뜻합니다." },
      { "char": "及", "role": "미칠 급 (요소)", "desc": "뒤쫓아가 미친다(다다른다)는 뜻과 발음 '급/큐우'를 줍니다." }
    ],
    "story": "몸 바깥의 공기나 물이 폐 속까지 다다르도록(及) 입(口)으로 들이마셔 '숨 쉬다' 혹은 '빨아들이다'는 뜻입니다.",
    "example_words": [
      { "word": "吸う", "reading": "すう", "meaning": "들이마시다, 피우다", "description": "숨이나 물기, 담배 연기 따위를 입으로 빨아들이는 것입니다." },
      { "word": "呼吸", "reading": "こきゅう", "meaning": "호흡", "description": "숨을 내쉬고(呼) 들이마시는(吸) 일입니다." }
    ]
  },
  {
    "kanji": "呼",
    "reading_on": "コ",
    "reading_kun": "よ(ぶ)",
    "meaning": "부를",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 소리를 내는 동작을 의미합니다." },
      { "char": "乎", "role": "어조사 호 (요소)", "desc": "소리가 길게 울려 퍼진다는 뜻과 발음 '호/코'를 담당합니다." }
    ],
    "story": "입(口)을 크게 벌리고 멀리 있는 사람이 듣도록 소리를 길게 뽑아 큰 소리로 '부르다' 혹은 숨을 내쉰다는 뜻입니다.",
    "example_words": [
      { "word": "呼ぶ", "reading": "よぶ", "meaning": "부르다", "description": "소리 내어 남을 오라고 하거나 이름을 일컫는 것입니다." },
      { "word": "呼吸", "reading": "こきゅう", "meaning": "호흡", "description": "숨을 내쉬고(呼) 들이마시는(吸) 일입니다." }
    ]
  },
  {
    "kanji": "善",
    "reading_on": "ゼン",
    "reading_kun": "よ(い)",
    "meaning": "착할 (좋을)",
    "components": [
      { "char": "羊", "role": "양 양 (요소)", "desc": "양처럼 착하고 상서롭다는 뜻을 줍니다." },
      { "char": "口", "role": "입 구 (부수)", "desc": "입이나 말함을 뜻합니다." }
    ],
    "story": "양(羊)처럼 순하고 좋은 성품으로 사람들과 다투지 않고 입(口)으로 좋은 말만 한다는 데서 '착하다' 혹은 '선하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "善い", "reading": "よい", "meaning": "착하다, 선하다", "description": "행동이나 마음씨가 훌륭하고 착한 모양입니다." },
      { "word": "親善", "reading": "しんぜん", "meaning": "친선", "description": "서로 친근하게 지내며(親) 착하고(善) 사이좋게 지내는 일입니다." }
    ]
  },
  {
    "kanji": "困",
    "reading_on": "コン",
    "reading_kun": "こま(る)",
    "meaning": "곤할 (곤란할)",
    "components": [
      { "char": "囗", "role": "큰입구 몸 (부수)", "desc": "사방이 둘러싸인 담장이나 울타리를 뜻합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "나무를 뜻하며 여기서는 갇혀 있다는 의미를 줍니다." }
    ],
    "story": "크게 자라야 할 나무(木)가 사방이 꽉 막힌 담장(囗) 안에 갇혀 더 자라지 못하고 옴짝달싹 못해 몹시 '괴롭다(곤란하다)'는 뜻입니다.",
    "example_words": [
      { "word": "困る", "reading": "こまる", "meaning": "곤란하다, 난처하다", "description": "일이 뜻대로 되지 않아 괴롭거나 어찌할 바를 모르는 상태입니다." },
      { "word": "困難", "reading": "こんなん", "meaning": "곤란", "description": "일이 막혀 괴롭고(困) 헤쳐 나가기 어려운(難) 상황입니다." }
    ]
  },
  {
    "kanji": "垂",
    "reading_on": "スイ",
    "reading_kun": "た(れる)、た(らす)",
    "meaning": "드리울 (늘어질)",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "땅이나 흙을 뜻합니다." },
      { "char": "千", "role": "일천 천 (요소)", "desc": "여기서는 나뭇가지나 꽃잎이 아래로 축 처진 모양을 나타냅니다." }
    ],
    "story": "식물의 잎이나 가지가 무게를 이기지 못하고 땅(土)을 향해 아래로 길게 '드리우다' 혹은 축 '늘어지다'는 의미입니다.",
    "example_words": [
      { "word": "垂れる", "reading": "たれる", "meaning": "늘어지다, 떨어지다", "description": "물방울이나 가지가 아래로 축 늘어져 떨어지는 것입니다." },
      { "word": "垂直", "reading": "すいちょく", "meaning": "수직", "description": "위에서 똑바로(直) 내려뜨린(垂) 선처럼 똑바른 모양입니다." }
    ]
  },
  {
    "kanji": "城",
    "reading_on": "ジョウ",
    "reading_kun": "しろ",
    "meaning": "성 (성곽)",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅을 의미합니다." },
      { "char": "成", "role": "이룰 성 (요소)", "desc": "이룩하여 지어낸다는 뜻과 발음 '성/ジョウ'을 줍니다." }
    ],
    "story": "적의 침입을 막기 위해 흙(土)과 돌을 높이 쌓아 이룩한(成) 크고 튼튼한 요새, 즉 '성(성곽)'을 뜻합니다.",
    "example_words": [
      { "word": "城", "reading": "しろ", "meaning": "성", "description": "외적을 막기 위해 흙이나 돌로 높이 쌓아 올린 큰 건물입니다." },
      { "word": "大阪城", "reading": "おおさかじょう", "meaning": "오사카성", "description": "일본 오사카에 있는 유명한 성(城) 이름입니다." }
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

print("Grade 6 Part 1 data appended successfully.")
