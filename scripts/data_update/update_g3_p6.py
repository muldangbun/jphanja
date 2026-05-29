import json
import os

new_data = [
  {
    "kanji": "倍",
    "reading_on": "バイ",
    "reading_kun": "",
    "meaning": "곱 (배)",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "사람입니다." },
      { "char": "咅", "role": "침 부 (요소)", "desc": "침을 뱉거나 입을 벌리는 모양, 혹은 양쪽으로 갈라진다는 뜻과 발음 '부/바이'를 줍니다." }
    ],
    "story": "사람(亻)이 입(咅)으로 침을 튀기며 말하거나 사람이 두 무리로 갈라지듯 수량이 두 배, 세 배 '곱'으로 늘어난다는 뜻입니다.",
    "example_words": [
      { "word": "倍", "reading": "ばい", "meaning": "배, 곱절", "description": "원래 수량의 두 배 이상으로 늘어나는 단위입니다." },
      { "word": "倍増", "reading": "ばいぞう", "meaning": "배증", "description": "갑절(倍)로 늘어남(増)입니다." }
    ]
  },
  {
    "kanji": "箱",
    "reading_on": "ソウ",
    "reading_kun": "はこ",
    "meaning": "상자",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 뜻합니다." },
      { "char": "相", "role": "서로 상 (요소)", "desc": "서로 마주 보다, 모양을 뜻하며 발음 '상/소우'를 나타냅니다." }
    ],
    "story": "대나무(竹)를 엮어서 안을 들여다볼 수 있게 모양(相)을 짠 둥글거나 네모난 '상자'를 의미합니다.",
    "example_words": [
      { "word": "箱", "reading": "はこ", "meaning": "상자", "description": "물건을 담는 궤나 갑입니다." },
      { "word": "ゴミ箱", "reading": "ごみばこ", "meaning": "쓰레기통", "description": "쓰레기(ゴミ)를 버리는 상자(箱)입니다." }
    ]
  },
  {
    "kanji": "畑",
    "reading_on": "",
    "reading_kun": "はた、はたけ",
    "meaning": "밭",
    "components": [
      { "char": "火", "role": "불 화 (요소)", "desc": "불로 태우다를 뜻합니다." },
      { "char": "田", "role": "밭 전 (부수)", "desc": "농사를 짓는 농경지나 밭입니다." }
    ],
    "story": "논과 달리 물이 없어서, 불(火)을 질러 잡초를 태우고 농사를 짓는 마른 농경지인 '밭'을 뜻하는 일본 고유 한자(국자)입니다.",
    "example_words": [
      { "word": "畑", "reading": "はたけ", "meaning": "밭", "description": "물을 대지 않고 농작물을 심는 땅입니다." },
      { "word": "麦畑", "reading": "むぎばたけ", "meaning": "보리밭", "description": "보리(麦)를 심은 밭(畑)입니다." }
    ]
  },
  {
    "kanji": "反",
    "reading_on": "ハン、ホン",
    "reading_kun": "そ(る)、そ(らす)",
    "meaning": "돌이킬 / 거스를",
    "components": [
      { "char": "厂", "role": "기슭 엄 (부수)", "desc": "산기슭이나 벼랑을 뜻합니다." },
      { "char": "又", "role": "또 우 (요소)", "desc": "손으로 무언가를 쥐거나 뒤집는 모양입니다." }
    ],
    "story": "산기슭(厂)에서 손(又)으로 돌이나 흙을 거꾸로 뒤집어 엎는다는 데서, 원래 상태를 '뒤집다'나 흐름을 '거스르다'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "反対", "reading": "はんたい", "meaning": "반대", "description": "거스르고(反) 마주 대하는(対) 상태입니다." },
      { "word": "反る", "reading": "そる", "meaning": "휘다, 젖혀지다", "description": "몸이나 널빤지가 뒤로 굽어지는 것입니다." }
    ]
  },
  {
    "kanji": "坂",
    "reading_on": "ハン",
    "reading_kun": "さか",
    "meaning": "고개 (비탈)",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "흙이나 땅을 뜻합니다." },
      { "char": "反", "role": "돌이킬 반 (요소)", "desc": "거꾸로 거스른다는 뜻과 발음 '반/한'을 담당합니다." }
    ],
    "story": "땅(土)이 평평하지 않고 거꾸로 거슬러(反) 올라가게 만들어진 비탈진 '고개'나 '언덕'을 의미합니다.",
    "example_words": [
      { "word": "坂道", "reading": "さかみち", "meaning": "비탈길, 고갯길", "description": "오르막이나 내리막의 비탈진(坂) 길(道)입니다." },
      { "word": "上り坂", "reading": "のぼりざか", "meaning": "오르막길", "description": "위로 올라가는(上り) 고개(坂)입니다." }
    ]
  },
  {
    "kanji": "板",
    "reading_on": "ハン、バン",
    "reading_kun": "いた",
    "meaning": "널빤지",
    "components": [
      { "char": "木", "role": "나무 목 (부수)", "desc": "나무를 의미합니다." },
      { "char": "反", "role": "돌이킬 반 (요소)", "desc": "뒤집다, 거스르다는 뜻과 발음 '반/한'을 나타냅니다." }
    ],
    "story": "통나무(木)를 잘라 거꾸로 뒤집어(反) 평평하게 다듬어 놓은 '널빤지'나 '판자'를 뜻합니다.",
    "example_words": [
      { "word": "板", "reading": "いた", "meaning": "널빤지, 판자", "description": "평평하게 켠 나무 조각입니다." },
      { "word": "看板", "reading": "かんばん", "meaning": "간판", "description": "상점 등을 볼 수 있게(看) 내건 널빤지(板)입니다." }
    ]
  },
  {
    "kanji": "番",
    "reading_on": "バン",
    "reading_kun": "",
    "meaning": "차례",
    "components": [
      { "char": "釆", "role": "분별할 변 (요소)", "desc": "짐승의 발자국 모양으로, 남겨진 흔적을 의미합니다." },
      { "char": "田", "role": "밭 전 (부수)", "desc": "밭이나 경작지를 뜻합니다." }
    ],
    "story": "밭(田)에 찍힌 발자국(釆)을 따라 씨를 뿌리거나 파종할 '차례'를 정한다는 뜻에서 유래했습니다.",
    "example_words": [
      { "word": "一番", "reading": "いちばん", "meaning": "제일, 첫째", "description": "첫(一) 번째 차례(番)입니다." },
      { "word": "順番", "reading": "じゅんばん", "meaning": "순번", "description": "순서(順)와 차례(番)입니다." }
    ]
  },
  {
    "kanji": "皮",
    "reading_on": "ヒ",
    "reading_kun": "かわ",
    "meaning": "가죽 (껍질)",
    "components": [
      { "char": "皮", "role": "가죽 피 (부수)", "desc": "짐승의 가죽을 벗기는 도구와 가죽 모양을 본뜬 글자입니다." }
    ],
    "story": "손에 도구를 들고 짐승의 털이나 '가죽(껍질)'을 벗겨내는 모양에서 유래하여 껍질이나 표면을 뜻합니다.",
    "example_words": [
      { "word": "皮", "reading": "かわ", "meaning": "껍질, 가죽", "description": "동식물의 겉을 싸고 있는 질긴 꺼풀입니다." },
      { "word": "毛皮", "reading": "けがわ", "meaning": "모피", "description": "털(毛)이 붙은 채로 벗긴 짐승의 가죽(皮)입니다." }
    ]
  },
  {
    "kanji": "悲",
    "reading_on": "ヒ",
    "reading_kun": "かな(しい)、かな(しむ)",
    "meaning": "슬플",
    "components": [
      { "char": "非", "role": "아닐 비 (요소)", "desc": "새의 양 날개가 서로 어긋난 모양으로 '어긋나다'는 뜻과 발음 '비/히'를 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 감정을 뜻합니다." }
    ],
    "story": "마음(心)먹은 뜻대로 일이 풀리지 않고 어긋나(非) 마음이 몹시 '슬프다'는 뜻입니다.",
    "example_words": [
      { "word": "悲しい", "reading": "かなしい", "meaning": "슬프다", "description": "마음이 아프고 눈물이 날 만큼 괴로운 상태입니다." },
      { "word": "悲鳴", "reading": "ひめい", "meaning": "비명", "description": "슬프고(悲) 괴로워서 울부짖는(鳴) 소리입니다." }
    ]
  },
  {
    "kanji": "美",
    "reading_on": "ビ",
    "reading_kun": "うつく(しい)",
    "meaning": "아름다울",
    "components": [
      { "char": "羊", "role": "양 양 (부수)", "desc": "통통하게 살찐 양을 뜻합니다." },
      { "char": "大", "role": "큰 대 (요소)", "desc": "크다, 훌륭하다는 의미를 나타냅니다." }
    ],
    "story": "고대인들에게 제물로 바치는 양(羊)이 아주 크고(大) 살찐 모습이 훌륭하고 '아름답게' 보였다는 데서 유래했습니다.",
    "example_words": [
      { "word": "美しい", "reading": "うつくしい", "meaning": "아름답다", "description": "모양이나 마음씨가 보기 좋고 훌륭한 상태입니다." },
      { "word": "美人", "reading": "びじん", "meaning": "미인", "description": "얼굴이나 자태가 아름다운(美) 사람(人)입니다." }
    ]
  },
  {
    "kanji": "鼻",
    "reading_on": "ビ",
    "reading_kun": "はな",
    "meaning": "코",
    "components": [
      { "char": "自", "role": "스스로 자 (요소)", "desc": "원래 코의 모양을 본뜬 글자로 자기 자신을 가리키거나 숨을 쉼을 뜻합니다." },
      { "char": "田", "role": "밭 전 (요소)", "desc": "여기서는 발음 부호 畀(줄 비)의 윗부분입니다." },
      { "char": "廾", "role": "두 손 멱 (요소)", "desc": "발음 부호 畀(줄 비)의 아랫부분으로, 손을 뜻합니다." }
    ],
    "story": "숨을 쉬는 코(自)와 기식을 뿜어낸다는 뜻을 가진 글자(畀)가 합쳐져 얼굴 한가운데 솟은 '코'를 의미하게 되었습니다.",
    "example_words": [
      { "word": "鼻", "reading": "はな", "meaning": "코", "description": "얼굴 한가운데 솟아 냄새를 맡거나 숨을 쉬는 기관입니다." },
      { "word": "耳鼻科", "reading": "じびか", "meaning": "이비인후과", "description": "귀(耳)와 코(鼻)의 병을 치료하는 과(科)입니다." }
    ]
  },
  {
    "kanji": "筆",
    "reading_on": "ヒツ",
    "reading_kun": "ふで",
    "meaning": "붓",
    "components": [
      { "char": "竹", "role": "대죽머리 (부수)", "desc": "대나무를 뜻합니다." },
      { "char": "聿", "role": "붓 율 (요소)", "desc": "손으로 붓대를 쥐고 글씨를 쓰는 모양을 본뜬 글자입니다." }
    ],
    "story": "손에 쥐고 글(聿)을 쓰는 도구 중에서도 대나무(竹) 통에 동물의 털을 꽂아 만든 '붓'을 의미합니다.",
    "example_words": [
      { "word": "鉛筆", "reading": "えんぴつ", "meaning": "연필", "description": "납(鉛)이나 흑연 심을 넣어 만든 붓(筆, 필기도구)입니다." },
      { "word": "筆箱", "reading": "ふでばこ", "meaning": "필통", "description": "붓(筆)이나 연필을 담는 상자(箱)입니다." }
    ]
  },
  {
    "kanji": "氷",
    "reading_on": "ヒョウ",
    "reading_kun": "こおり",
    "meaning": "얼음",
    "components": [
      { "char": "水", "role": "물 수 (부수)", "desc": "물이나 액체를 뜻합니다." },
      { "char": "丶", "role": "점 주 (요소)", "desc": "물이 얼어서 생긴 결정을 나타내는 얼음 방울입니다." }
    ],
    "story": "흐르는 물(水)이 추운 날씨에 꽁꽁 얼어붙어 뾰족한 결정(丶)이 맺힌 '얼음'을 뜻합니다.",
    "example_words": [
      { "word": "氷", "reading": "こおり", "meaning": "얼음", "description": "물이 얼어서 굳어진 물질입니다." },
      { "word": "かき氷", "reading": "かきごおり", "meaning": "빙수", "description": "얼음(氷)을 긁어내서(かき) 시럽을 뿌린 디저트입니다." }
    ]
  },
  {
    "kanji": "表",
    "reading_on": "ヒョウ",
    "reading_kun": "おもて、あらわ(す)、あらわ(れる)",
    "meaning": "겉 / 나타낼",
    "components": [
      { "char": "毛", "role": "털 모 (요소)", "desc": "짐승의 털을 의미합니다." },
      { "char": "衣", "role": "옷 의 (부수)", "desc": "사람이 입는 옷입니다." }
    ],
    "story": "옷(衣) 중에서 털(毛) 장식이 밖으로 드러난 화려한 겉옷의 모습에서 사물의 '겉(표면)'이나 속마음을 밖으로 '나타내다'는 뜻입니다.",
    "example_words": [
      { "word": "表", "reading": "おもて", "meaning": "겉, 표면", "description": "사물의 바깥쪽이나 겉으로 드러난 면입니다." },
      { "word": "発表", "reading": "はっぴょう", "meaning": "발표", "description": "세상에 널리 펴서(発) 겉으로 드러내(表) 알리는 것입니다." }
    ]
  },
  {
    "kanji": "病",
    "reading_on": "ビョウ、ヘイ",
    "reading_kun": "やまい",
    "meaning": "병 (앓을)",
    "components": [
      { "char": "疒", "role": "병질엄 (부수)", "desc": "사람이 병상에 누워 땀을 흘리는 모양으로 질병을 뜻합니다." },
      { "char": "丙", "role": "남녘 병 (요소)", "desc": "불이나 열기를 뜻하며, 발음 '병/ビョウ'을 줍니다." }
    ],
    "story": "몸에 열(丙)이 심하게 나서 침상에 누워 앓고(疒) 있는 '병'을 의미합니다.",
    "example_words": [
      { "word": "病気", "reading": "びょうき", "meaning": "병", "description": "몸이나 마음에 앓는 병(病)이 든 기운(気)입니다." },
      { "word": "病院", "reading": "びょういん", "meaning": "병원", "description": "병(病)을 고치는 관청이나 집(院)입니다." }
    ]
  },
  {
    "kanji": "品",
    "reading_on": "ヒン",
    "reading_kun": "しな",
    "meaning": "물건 / 품격",
    "components": [
      { "char": "口", "role": "입 구 (부수)", "desc": "그릇이나 사람의 입, 무리를 뜻합니다." }
    ],
    "story": "그릇(口) 세 개가 나란히 놓여 있는 모습에서 묶음이나 등급이 나뉜 '물건'을 뜻하며, 사람의 '품격'을 의미하기도 합니다.",
    "example_words": [
      { "word": "品物", "reading": "しなもの", "meaning": "물건, 품목", "description": "팔거나 쓰는 여러 가지 물건(品物)입니다." },
      { "word": "上品", "reading": "じょうひん", "meaning": "고상함, 품위 있음", "description": "품격이나 질(品)이 아주 높고 좋은(上) 상태입니다." }
    ]
  },
  {
    "kanji": "負",
    "reading_on": "フ",
    "reading_kun": "ま(ける)、ま(かす)、お(う)",
    "meaning": "질 / 등에 질",
    "components": [
      { "char": "⺈", "role": "안을 포 (요소)", "desc": "사람이 등을 굽힌 모양(人의 변형)입니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "돈이나 귀중한 재물을 뜻합니다." }
    ],
    "story": "사람이 귀중한 재물이나 보따리(貝)를 등(⺈)에 짊어지고 가다 무거워 쓰러진다는 데서 짐을 '지다' 혹은 승부에서 '지다(패배하다)'는 뜻이 되었습니다.",
    "example_words": [
      { "word": "負ける", "reading": "まける", "meaning": "지다, 패하다", "description": "승부에서 상대에게 꺾여 지는 것입니다." },
      { "word": "勝負", "reading": "しょうぶ", "meaning": "승부", "description": "이기고(勝) 지는(負) 것을 겨루는 일입니다." }
    ]
  },
  {
    "kanji": "部",
    "reading_on": "ブ",
    "reading_kun": "",
    "meaning": "떼 / 부분",
    "components": [
      { "char": "咅", "role": "침 부 (요소)", "desc": "나눈다는 뜻과 발음 '부'를 담당합니다." },
      { "char": "阝", "role": "우부방 (부수)", "desc": "마을이나 행정 구역을 의미합니다." }
    ],
    "story": "큰 고을이나 조직(阝)을 역할에 따라 여러 갈래로 나눈(咅) '부서'나 '부분', '무리(떼)'를 의미합니다.",
    "example_words": [
      { "word": "部屋", "reading": "へや", "meaning": "방", "description": "집 안을 여러 구역으로 나눈 부분(部)이 되는 공간(屋)입니다." },
      { "word": "部分", "reading": "ぶぶん", "meaning": "부분", "description": "전체를 여러 갈래로 나눈(分) 무리(部)나 몫입니다." }
    ]
  },
  {
    "kanji": "服",
    "reading_on": "フク",
    "reading_kun": "",
    "meaning": "옷 / 복종할",
    "components": [
      { "char": "月", "role": "달 월 (부수)", "desc": "원래 舟(배 주)가 변형된 것으로, 몸이나 배를 나타냅니다." },
      { "char": "𠬝", "role": "복종할 복 (요소)", "desc": "손으로 무언가를 억누르는 모양으로 다스리거나 엎드림을 뜻합니다." }
    ],
    "story": "몸(月)을 착 감싸게 입는 '옷(의복)'을 뜻하며, 몸을 굽혀 엎드려 '복종하다'나 약을 '먹다(복용하다)'는 뜻으로도 쓰입니다.",
    "example_words": [
      { "word": "洋服", "reading": "ようふく", "meaning": "양복", "description": "서양(洋)식으로 만든 옷(服)입니다." },
      { "word": "制服", "reading": "せいふく", "meaning": "교복, 제복", "description": "제도나 규정에 맞게 지은(制) 옷(服)입니다." }
    ]
  },
  {
    "kanji": "福",
    "reading_on": "フク",
    "reading_kun": "",
    "meaning": "복",
    "components": [
      { "char": "示", "role": "보일 시 (부수)", "desc": "제단이나 신을 뜻합니다." },
      { "char": "畐", "role": "가득할 복 (요소)", "desc": "술이나 곡식이 가득 찬 항아리 모양으로, 풍요로움과 발음 '복/후쿠'를 뜻합니다." }
    ],
    "story": "제단(示) 앞에 곡식과 술이 가득 찬 항아리(畐)를 바치고 신에게 풍요로운 '복'을 비는 모습입니다.",
    "example_words": [
      { "word": "幸福", "reading": "こうふく", "meaning": "행복", "description": "다행스럽고(幸) 기쁜 복(福)입니다." },
      { "word": "祝福", "reading": "しゅくふく", "meaning": "축복", "description": "복(福)을 받기를 빌어(祝) 주는 것입니다." }
    ]
  },
  {
    "kanji": "物",
    "reading_on": "ブツ、モツ",
    "reading_kun": "もの",
    "meaning": "만물 (물건)",
    "components": [
      { "char": "牛", "role": "소 우 (부수)", "desc": "소를 뜻하며, 여기서는 소처럼 큰 제물이나 사물을 대표합니다." },
      { "char": "勿", "role": "말 물 (요소)", "desc": "원래 피가 떨어지는 모양이거나 얼룩을 뜻하여 여러 잡다한 것이라는 뜻을 줍니다." }
    ],
    "story": "소(牛)처럼 크고 여러 털 색깔이나 얼룩(勿)을 가진 다양한 생물에서 유래하여, 세상 만물이나 '물건'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "動物", "reading": "どうぶつ", "meaning": "동물", "description": "움직이는(動) 생물이나 물건(物)입니다." },
      { "word": "買い物", "reading": "かいもの", "meaning": "쇼핑, 장보기", "description": "물건(物)을 사는(買い) 행위입니다." }
    ]
  },
  {
    "kanji": "平",
    "reading_on": "ヘイ、ビョウ",
    "reading_kun": "たい(ら)、ひら",
    "meaning": "평평할",
    "components": [
      { "char": "干", "role": "방패 간 (부수)", "desc": "원래 물 위에 뜬 개구리 밥이 고르게 퍼진 모양이거나 저울대 모양에서 유래했습니다." },
      { "char": "八", "role": "여덟 팔 (요소)", "desc": "양쪽으로 갈라져서 고르게 나뉜 모습입니다." }
    ],
    "story": "수면 위로 물풀이 고르게 둥둥 떠 있는 모습이나 저울대가 수평을 이룬 모양에서 '평평하다' 혹은 고요하고 '평온하다'는 뜻을 가집니다.",
    "example_words": [
      { "word": "平和", "reading": "へいわ", "meaning": "평화", "description": "평평하고(平) 화목하게(和) 다툼이 없는 상태입니다." },
      { "word": "平ら", "reading": "たいら", "meaning": "평평함", "description": "바닥 따위가 울퉁불퉁하지 않고 고른 상태입니다." }
    ]
  },
  {
    "kanji": "兵",
    "reading_on": "ヘイ、ヒョウ",
    "reading_kun": "",
    "meaning": "군사 (병기)",
    "components": [
      { "char": "斤", "role": "도끼 근 (요소)", "desc": "도끼나 무기를 뜻합니다." },
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "여기서는 두 손(廾)이 무기를 받쳐 든 모양에서 변형되었습니다." }
    ],
    "story": "두 손(八의 변형)으로 무거운 도끼나 무기(斤)를 굳게 잡고 싸우는 '군사(병사)' 혹은 그 '무기'를 뜻합니다.",
    "example_words": [
      { "word": "兵士", "reading": "へいし", "meaning": "병사", "description": "무기를 든 군사(兵)인 선비(사내)(士)입니다." },
      { "word": "兵器", "reading": "へいき", "meaning": "병기, 무기", "description": "군사(兵)가 전쟁에서 쓰는 기구(器)입니다." }
    ]
  },
  {
    "kanji": "別",
    "reading_on": "ベツ",
    "reading_kun": "わか(れる)",
    "meaning": "나눌 / 다를",
    "components": [
      { "char": "口", "role": "입 구 (요소)", "desc": "원래 뼈나 관절을 의미하는 冎(뼈 발라낼 과)의 변형입니다." },
      { "char": "刀", "role": "칼 도 (부수)", "desc": "칼로 베거나 자른다는 뜻입니다." }
    ],
    "story": "짐승의 뼈(口의 원형)를 칼(刀)로 발라내어 살과 뼈를 '나누다' 혹은 이별하여 '헤어지다'는 의미입니다.",
    "example_words": [
      { "word": "別れる", "reading": "わかれる", "meaning": "헤어지다, 갈라지다", "description": "서로 나뉘어 다른 길로 가는 것입니다." },
      { "word": "特別", "reading": "とくべつ", "meaning": "특별", "description": "뛰어나게(特) 다르게 나뉜(別) 보통과 다른 상태입니다." }
    ]
  },
  {
    "kanji": "勉",
    "reading_on": "ベン",
    "reading_kun": "",
    "meaning": "힘쓸",
    "components": [
      { "char": "免", "role": "면할 면 (요소)", "desc": "투구를 쓴 사람이 몸을 빼내어 피한다는 뜻에서 힘들게 애쓴다는 의미와 발음 '면/벤'을 줍니다." },
      { "char": "力", "role": "힘 력 (부수)", "desc": "힘이나 노력을 뜻합니다." }
    ],
    "story": "힘든 상황(免)을 극복하기 위해 온 힘(力)을 다해 열심히 '힘쓰다(노력하다)'는 뜻입니다.",
    "example_words": [
      { "word": "勉強", "reading": "べんきょう", "meaning": "공부", "description": "어려운 것을 억지로(強) 힘써서(勉) 익히는 일입니다." },
      { "word": "勤勉", "reading": "きんべん", "meaning": "근면", "description": "부지런히 일하고(勤) 힘쓰는(勉) 것입니다." }
    ]
  },
  {
    "kanji": "放",
    "reading_on": "ホウ",
    "reading_kun": "はな(す)、はな(つ)、はな(れる)",
    "meaning": "놓을 / 풀어주다",
    "components": [
      { "char": "方", "role": "모방 (요소)", "desc": "사방팔방, 방향을 뜻하며 발음 '방/호우'를 줍니다." },
      { "char": "攵", "role": "칠 복 (부수)", "desc": "손으로 치거나 내쫓는 동작입니다." }
    ],
    "story": "손에 도구를 들고 짐승 등을 사방(方)으로 내쫓아(攵) 밖으로 '풀어주다' 혹은 얽매인 것을 '놓아주다'는 뜻입니다.",
    "example_words": [
      { "word": "放送", "reading": "ほうそう", "meaning": "방송", "description": "전파를 놓아서(放) 멀리 보내는(送) 일입니다." },
      { "word": "手放す", "reading": "てばなす", "meaning": "놓아주다, 손에서 놓다", "description": "쥐고 있던 손(手)을 놓는(放す) 것입니다." }
    ]
  },
  {
    "kanji": "問",
    "reading_on": "モン",
    "reading_kun": "と(う)、と(ん)",
    "meaning": "물을",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "대문을 뜻합니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "입이나 목소리입니다." }
    ],
    "story": "남의 집 대문(門) 앞에 서서 입(口)으로 소리를 내어 안에 누가 있는지, 길은 어딘지 '묻다(질문하다)'는 뜻입니다.",
    "example_words": [
      { "word": "質問", "reading": "しつもん", "meaning": "질문", "description": "바탕(質)을 알기 위해 묻는(問) 것입니다." },
      { "word": "問題", "reading": "もんだい", "meaning": "문제", "description": "묻는(問) 주제나 제목(題)입니다." }
    ]
  },
  {
    "kanji": "役",
    "reading_on": "ヤク、エキ",
    "reading_kun": "",
    "meaning": "부릴 (직분)",
    "components": [
      { "char": "彳", "role": "두인변 (부수)", "desc": "길을 걷거나 이동함을 뜻합니다." },
      { "char": "殳", "role": "창 수 (요소)", "desc": "창이나 무기를 들고 내리치는 모습으로 강제적인 힘을 의미합니다." }
    ],
    "story": "창(殳)을 들고 백성들을 길(彳)로 몰고 가며 강제로 일을 '부리다(부역)'라는 뜻에서, 훗날 맡은 임무나 '직분(역할)'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "役に立つ", "reading": "やくにたつ", "meaning": "도움이 되다", "description": "특정한 역할이나 직분(役)에 서게(立つ) 되어 유용하다는 뜻입니다." },
      { "word": "役割", "reading": "やくわり", "meaning": "역할", "description": "맡은 직분(役)을 나누어(割) 맡은 것입니다." }
    ]
  },
  {
    "kanji": "薬",
    "reading_on": "ヤク",
    "reading_kun": "くすり",
    "meaning": "약",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 식물, 허브를 뜻합니다." },
      { "char": "楽", "role": "즐길 락 (요소)", "desc": "병이 나아 몸이 편안하고 즐거워진다는 의미와 발음 '락/야쿠'를 나타냅니다." }
    ],
    "story": "아픈 몸을 낫게 하여 편안하고 즐겁게(楽) 해주는 특별한 풀(艹)이나 식물, 즉 '약'을 뜻합니다.",
    "example_words": [
      { "word": "薬", "reading": "くすり", "meaning": "약", "description": "병을 고치기 위해 먹거나 바르는 물질입니다." },
      { "word": "薬局", "reading": "やっきょく", "meaning": "약국", "description": "약(薬)을 짓고 파는 가게(局)입니다." }
    ]
  },
  {
    "kanji": "由",
    "reading_on": "ユ、ユウ、ユイ",
    "reading_kun": "よし",
    "meaning": "말미암을",
    "components": [
      { "char": "田", "role": "밭 전 (부수)", "desc": "원래 밭이 아니라 조롱박이나 열매가 주렁주렁 매달린 모양에서 유래했습니다." },
      { "char": "丨", "role": "뚫을 곤 (요소)", "desc": "조롱박의 꼭지를 나타냅니다." }
    ],
    "story": "조롱박 열매가 꼭지(丨)를 통해 넝쿨에 매달려 나오는 모습에서, 어떤 일의 원인이 되어 거기서부터 비롯되거나 '말미암다(이유)'는 뜻을 가집니다.",
    "example_words": [
      { "word": "理由", "reading": "りゆう", "meaning": "이유", "description": "어떤 일이 일어나게 된 이치(理)와 까닭(由)입니다." },
      { "word": "自由", "reading": "じゆう", "meaning": "자유", "description": "스스로(自)를 원인으로 말미암아(由) 마음대로 행동하는 상태입니다." }
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

print("Grade 3 Part 6 data appended successfully.")
