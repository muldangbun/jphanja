import json
import os

new_data = [
  {
    "kanji": "売",
    "reading_on": "バイ",
    "reading_kun": "う(る)、う(れる)",
    "meaning": "팔다",
    "components": [
      { "char": "士", "role": "선비 사 (요소)", "desc": "원래는 날출(出) 자가 변형된 것으로, 물건을 바깥으로 내놓는다는 뜻입니다." },
      { "char": "冖", "role": "민갓머리 (요소)", "desc": "가게나 가판대의 덮개를 뜻합니다." },
      { "char": "儿", "role": "어진사람 인 (부수)", "desc": "사람의 다리나 사람을 의미합니다." }
    ],
    "story": "가게(冖)에서 물건을 바깥으로(士의 원형) 내어놓고 사람(儿)들에게 '팔다'라는 뜻입니다.",
    "example_words": [
      { "word": "売店", "reading": "ばいてん", "meaning": "매점", "description": "물건을 파는(売) 작은 가게(店)입니다." },
      { "word": "売り切れ", "reading": "うりきれ", "meaning": "품절", "description": "모두 다 팔려서(売り) 끊어진(切れ) 상태입니다." }
    ]
  },
  {
    "kanji": "買",
    "reading_on": "バイ",
    "reading_kun": "か(う)",
    "meaning": "사다",
    "components": [
      { "char": "罒", "role": "그물 망 (요소)", "desc": "물건을 담는 그물이나 덮개를 뜻합니다." },
      { "char": "貝", "role": "조개 패 (부수)", "desc": "옛날 돈으로 쓰이던 조개껍데기로, 재물이나 돈을 뜻합니다." }
    ],
    "story": "돈(貝)을 지불하고 그물망(罒)에 물건을 담아서 '사다'라는 뜻입니다.",
    "example_words": [
      { "word": "買い物", "reading": "かいもの", "meaning": "쇼핑, 장보기", "description": "물건(物)을 사는(買い) 것입니다." },
      { "word": "売買", "reading": "ばいばい", "meaning": "매매", "description": "물건을 팔고(売) 사는(買) 일입니다." }
    ]
  },
  {
    "kanji": "麦",
    "reading_on": "バク",
    "reading_kun": "むぎ",
    "meaning": "보리",
    "components": [
      { "char": "麦", "role": "보리 맥 (부수)", "desc": "뿌리를 내린 보리의 이삭과 줄기 모양을 본뜬 글자의 간략화된 형태입니다." }
    ],
    "story": "위에 이삭이 패고 아래로는 뿌리가 내린 '보리'의 모양을 그려낸 글자입니다.",
    "example_words": [
      { "word": "小麦", "reading": "こむぎ", "meaning": "밀", "description": "작은(小) 보리(麦)라는 뜻의 밀입니다." },
      { "word": "麦茶", "reading": "むぎちゃ", "meaning": "보리차", "description": "보리(麦)를 볶아 끓인 차(茶)입니다." }
    ]
  },
  {
    "kanji": "半",
    "reading_on": "ハン",
    "reading_kun": "なか(ば)",
    "meaning": "반",
    "components": [
      { "char": "八", "role": "여덟 팔 (요소)", "desc": "양쪽으로 나누어진다는 뜻입니다." },
      { "char": "牛", "role": "소 우 (부수)", "desc": "커다란 짐승인 소를 나타냅니다. (간략화된 형태)" }
    ],
    "story": "커다란 소(牛) 고기를 양쪽으로(八) 똑같이 자른 절'반'을 뜻합니다.",
    "example_words": [
      { "word": "半分", "reading": "はんぶん", "meaning": "절반", "description": "반(半)으로 나눈(分) 것입니다." },
      { "word": "後半", "reading": "こうはん", "meaning": "후반", "description": "뒤(後)쪽의 절반(半)을 뜻합니다." }
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
      { "word": "順番", "reading": "じゅんばん", "meaning": "순번", "description": "차례(順)와 순서(番)입니다." },
      { "word": "交番", "reading": "こうばん", "meaning": "파출소", "description": "경찰이 교대(交)로 번갈아(番) 가며 지키는 곳입니다." }
    ]
  },
  {
    "kanji": "父",
    "reading_on": "フ",
    "reading_kun": "ちち",
    "meaning": "아비",
    "components": [
      { "char": "父", "role": "아비 부 (부수)", "desc": "손에 도끼나 막대기를 들고 있는 사람의 모습입니다." }
    ],
    "story": "손에 도끼나 몽둥이를 들고 가족을 지키거나 권위를 내세우는 집안의 어른, '아버지'를 의미합니다.",
    "example_words": [
      { "word": "父親", "reading": "ちちおや", "meaning": "부친, 아버지", "description": "아버지(父)인 어버이(親)입니다." },
      { "word": "お父さん", "reading": "おとうさん", "meaning": "아빠, 아버지", "description": "아버지를 친근하고 높여 부르는 말입니다." }
    ]
  },
  {
    "kanji": "風",
    "reading_on": "フウ、フ",
    "reading_kun": "かぜ",
    "meaning": "바람",
    "components": [
      { "char": "几", "role": "안석 궤 (부수)", "desc": "하늘에서 넓게 퍼져 내려오는 기운(凡의 변형)을 뜻합니다." },
      { "char": "虫", "role": "벌레 충 (요소)", "desc": "바람이 불면 나타나는 벌레나 곤충입니다." }
    ],
    "story": "하늘에서 기운(几)이 넓게 퍼져 불어오면, 숨어있던 벌레(虫)들이 나타나는 현상인 '바람'을 의미합니다.",
    "example_words": [
      { "word": "台風", "reading": "たいふう", "meaning": "태풍", "description": "매우 큰(台) 바람(風)입니다." },
      { "word": "風邪", "reading": "かぜ", "meaning": "감기", "description": "바람(風)에 실려오는 나쁜 기운(邪)이라는 뜻입니다." }
    ]
  },
  {
    "kanji": "分",
    "reading_on": "ブン、フン、ブ",
    "reading_kun": "わ(ける)、わ(かる)",
    "meaning": "나눌 / 분",
    "components": [
      { "char": "八", "role": "여덟 팔 (부수)", "desc": "양쪽으로 갈라지거나 나뉘는 모양입니다." },
      { "char": "刀", "role": "칼 도 (요소)", "desc": "물건을 베거나 자르는 칼입니다." }
    ],
    "story": "칼(刀)을 사용하여 물건을 양쪽으로(八) 갈라서 '나눈다'는 뜻입니다.",
    "example_words": [
      { "word": "半分", "reading": "はんぶん", "meaning": "절반", "description": "반(半)으로 나눈(分) 몫입니다." },
      { "word": "分かる", "reading": "わかる", "meaning": "알다, 이해하다", "description": "이치가 나누어져(分) 명확하게 머릿속에 들어온다는 뜻입니다." }
    ]
  },
  {
    "kanji": "聞",
    "reading_on": "ブン、モン",
    "reading_kun": "き(く)、き(こえる)",
    "meaning": "들을",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "양쪽으로 열리는 큰 대문입니다." },
      { "char": "耳", "role": "귀 이 (요소)", "desc": "사람의 귀입니다." }
    ],
    "story": "대문(門) 틈에 귀(耳)를 대고 문 밖에서 나는 소리를 주의 깊게 '듣다'라는 뜻입니다.",
    "example_words": [
      { "word": "新聞", "reading": "しんぶん", "meaning": "신문", "description": "새로운(新) 소식을 듣는(聞) 종이입니다." },
      { "word": "聞こえる", "reading": "きこえる", "meaning": "들리다", "description": "소리가 귀에 들어와 들리는(聞) 것입니다." }
    ]
  },
  {
    "kanji": "米",
    "reading_on": "ベイ、マイ",
    "reading_kun": "こめ",
    "meaning": "쌀",
    "components": [
      { "char": "米", "role": "쌀 미 (부수)", "desc": "벼 이삭에 낟알들이 붙어있는 모양을 본뜬 글자입니다." }
    ],
    "story": "가로 세로 줄기 사방에 흩뿌려진 듯이 달린 곡식 낟알, 즉 '쌀'의 모습을 나타냅니다.",
    "example_words": [
      { "word": "白米", "reading": "はくまい", "meaning": "백미", "description": "도정하여 하얀(白) 쌀(米)입니다." },
      { "word": "米国", "reading": "べいこく", "meaning": "미국", "description": "America의 아(A) 소리에 쌀 미(米) 자를 빌려 쓴 국가 이름입니다." }
    ]
  },
  {
    "kanji": "歩",
    "reading_on": "ホ、ブ",
    "reading_kun": "ある(く)、あゆ(む)",
    "meaning": "걸음",
    "components": [
      { "char": "止", "role": "그칠 지 (부수)", "desc": "발자국 모양에서 유래한 발을 뜻합니다." },
      { "char": "少", "role": "작을 소 (요소)", "desc": "여기서는 발자국이 서로 교차하는 모양(본래 형태에서 변형됨)을 뜻합니다." }
    ],
    "story": "오른발과 왼발(止와 그 변형)을 서로 교대로 내딛으며 앞을 향해 '걷다' 혹은 '걸음'을 뜻합니다.",
    "example_words": [
      { "word": "歩く", "reading": "あるく", "meaning": "걷다", "description": "발을 내디뎌 걷는(歩) 것입니다." },
      { "word": "散歩", "reading": "さんぽ", "meaning": "산책", "description": "발길 가는 대로 흩어져(散) 걷는(歩) 것입니다." }
    ]
  },
  {
    "kanji": "母",
    "reading_on": "ボ",
    "reading_kun": "はは",
    "meaning": "어미",
    "components": [
      { "char": "母", "role": "어미 모 (부수)", "desc": "여자(女)의 가슴에 젖(점 두 개)이 있는 모습을 본뜬 상형문자입니다." }
    ],
    "story": "아기에게 젖을 먹이는 여성의 모습을 그려내어, 자식을 기르는 '어머니'를 의미합니다.",
    "example_words": [
      { "word": "母親", "reading": "ははおや", "meaning": "모친, 어머니", "description": "어머니(母)인 어버이(親)입니다." },
      { "word": "お母さん", "reading": "おかあさん", "meaning": "엄마, 어머니", "description": "어머니를 친근하게 부르는 말입니다." }
    ]
  },
  {
    "kanji": "方",
    "reading_on": "ホウ",
    "reading_kun": "かた",
    "meaning": "모 / 방향",
    "components": [
      { "char": "方", "role": "모방 (부수)", "desc": "쟁기나 배가 두 척 나란히 있는 모양으로, 일정한 방향이나 방법, 모서리를 뜻합니다." }
    ],
    "story": "쟁기가 한쪽을 향해 나아가는 모습에서 어떤 사물의 모서리, 올바른 길이나 '방향', '방법'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "方法", "reading": "ほうほう", "meaning": "방법", "description": "일을 처리하는 방향(方)과 법(法)입니다." },
      { "word": "夕方", "reading": "ゆうがた", "meaning": "저녁 무렵", "description": "저녁(夕)이 다 되어가는 즈음(方)입니다." }
    ]
  },
  {
    "kanji": "北",
    "reading_on": "ホク",
    "reading_kun": "きた",
    "meaning": "북녘 (북쪽)",
    "components": [
      { "char": "匕", "role": "비수 비 (부수)", "desc": "여기서는 사람이 서 있는 모습을 뜻합니다." }
    ],
    "story": "두 사람이 서로 등을 돌리고 있는(등질 배의 원형) 모습에서, 햇볕이 안 드는 등 쪽인 '북쪽'을 의미하게 되었습니다.",
    "example_words": [
      { "word": "北海道", "reading": "ほっかいどう", "meaning": "홋카이도", "description": "일본 북쪽(北)의 바다(海)에 있는 도(道)입니다." },
      { "word": "南北", "reading": "なんぼく", "meaning": "남북", "description": "남쪽(南)과 북쪽(北)입니다." }
    ]
  },
  {
    "kanji": "毎",
    "reading_on": "マイ",
    "reading_kun": "",
    "meaning": "매양 (매번)",
    "components": [
      { "char": "𠂉", "role": "비녀 (요소)", "desc": "머리를 묶은 비녀, 혹은 머리 장식을 뜻합니다." },
      { "char": "母", "role": "어미 모 (부수)", "desc": "어머니를 뜻합니다." }
    ],
    "story": "어머니(母)가 비녀(𠂉)를 꽂고 매일매일 쉬지 않고 부지런히 일한다는 데서 '늘', '매번'이라는 뜻을 가집니다.",
    "example_words": [
      { "word": "毎日", "reading": "まいにち", "meaning": "매일", "description": "매번(毎) 다가오는 하루하루(日)입니다." },
      { "word": "毎朝", "reading": "まいあさ", "meaning": "매일 아침", "description": "매일(毎) 아침(朝)입니다." }
    ]
  }
]

file_path = '../../radical/src/data/kanjiDecomposerData_grade2.json'
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

print("Grade 2 Part 6.1 data appended successfully.")
