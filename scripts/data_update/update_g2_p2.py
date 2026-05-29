import json
import os

new_data = [
  {
    "kanji": "画",
    "reading_on": "ガ、カク",
    "reading_kun": "",
    "meaning": "그림 / 그을 획",
    "components": [
      { "char": "一", "role": "한 일 (부수/요소)", "desc": "붓을 그어 선을 나타냅니다." },
      { "char": "田", "role": "밭 전 (요소)", "desc": "경계가 나뉜 밭의 모습입니다." },
      { "char": "凵", "role": "위터진입구 몸 (부수)", "desc": "그림의 테두리나 액자를 상징합니다." }
    ],
    "story": "붓(一)으로 밭(田)의 경계처럼 선을 그어 테두리(凵) 안에 '그림'을 그리거나 '획'을 긋는다는 뜻입니다.",
    "example_words": [
      { "word": "映画", "reading": "えいが", "meaning": "영화", "description": "빛이 비추어(映) 움직이는 그림(画)을 의미합니다." },
      { "word": "計画", "reading": "けいかく", "meaning": "계획", "description": "미래의 일을 셈하고(計) 선을 그어(画) 준비하는 것입니다." }
    ]
  },
  {
    "kanji": "回",
    "reading_on": "カイ",
    "reading_kun": "まわ(る)",
    "meaning": "돌다 / 횟수",
    "components": [
      { "char": "囗", "role": "에운담 구 (부수)", "desc": "바깥쪽에서 한 바퀴 둘러싼 모양입니다." },
      { "char": "口", "role": "입 구 (요소)", "desc": "안쪽에서 한 바퀴를 그리는 모양입니다." }
    ],
    "story": "소용돌이 치듯 안팎(囗, 口)으로 둥글게 빙빙 '도는' 모습을 본떠 횟수나 도는 것을 뜻합니다.",
    "example_words": [
      { "word": "一回", "reading": "いっかい", "meaning": "일회 (한 번)", "description": "한(一) 번(回)이라는 뜻입니다." },
      { "word": "回り道", "reading": "まわりみち", "meaning": "우회로", "description": "빙 돌아서(回り) 가는 길(道)을 말합니다." }
    ]
  },
  {
    "kanji": "会",
    "reading_on": "カイ、エ",
    "reading_kun": "あ(う)",
    "meaning": "모이다 / 만나다",
    "components": [
      { "char": "人", "role": "사람 인 (변형)", "desc": "사람들이 위에 모여 있는 지붕 형태(亼)입니다." },
      { "char": "云", "role": "이를 운 (요소)", "desc": "말을 하며 뜻을 나누는 것을 뜻합니다." }
    ],
    "story": "한곳(亼)에 사람들이 모여서 말(云)을 나누며 '만난다'는 의미입니다.",
    "example_words": [
      { "word": "会社", "reading": "かいしゃ", "meaning": "회사", "description": "사람들이 모인(会) 모임(社)이라는 뜻입니다." },
      { "word": "出会い", "reading": "であい", "meaning": "만남", "description": "나가서(出) 누군가를 우연히 만나는(会い) 것을 말합니다." }
    ]
  },
  {
    "kanji": "海",
    "reading_on": "カイ",
    "reading_kun": "うみ",
    "meaning": "바다",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이 모여 있는 것을 나타냅니다." },
      { "char": "毎", "role": "매양 매 (요소)", "desc": "어머니가 머리를 땋은 모습에서, 넓고 크다(어머니의 사랑처럼) 혹은 발음 '매/해'를 나타냅니다." }
    ],
    "story": "물(氵)이 끝없이 넓게(毎) 펼쳐져 있는 '바다'를 의미합니다.",
    "example_words": [
      { "word": "海外", "reading": "かいがい", "meaning": "해외", "description": "바다(海) 밖(外)의 외국을 의미합니다." },
      { "word": "海草", "reading": "かいそう", "meaning": "해초", "description": "바다(海)에서 자라는 풀(草)입니다." }
    ]
  },
  {
    "kanji": "絵",
    "reading_on": "カイ、エ",
    "reading_kun": "",
    "meaning": "그림",
    "components": [
      { "char": "糸", "role": "실 사 (부수)", "desc": "실, 천, 엮인 색깔 등 텍스타일을 뜻합니다." },
      { "char": "会", "role": "모일 회 (요소)", "desc": "색깔을 모은다(会)는 의미와 '회/에'라는 발음을 담당합니다." }
    ],
    "story": "색색의 실(糸)을 짜 모아서(会) 만든 무늬나 '그림'을 뜻하는 한자입니다.",
    "example_words": [
      { "word": "絵本", "reading": "えほん", "meaning": "그림책", "description": "그림(絵)이 그려진 책(本)을 말합니다." },
      { "word": "絵画", "reading": "かいが", "meaning": "회화", "description": "붓으로 그린 그림(絵, 画)을 통틀어 말합니다." }
    ]
  },
  {
    "kanji": "外",
    "reading_on": "ガイ、ゲ",
    "reading_kun": "そと、はず(れる)",
    "meaning": "바깥",
    "components": [
      { "char": "夕", "role": "저녁 석 (부수)", "desc": "해가 지고 달이 뜬 저녁 무렵을 뜻합니다." },
      { "char": "卜", "role": "점 복 (요소)", "desc": "점을 치는 모습입니다." }
    ],
    "story": "어두운 저녁(夕)에는 점(卜)을 치기 어려워 규정 '밖'의 일로 여겼다는 데서 '바깥'이라는 뜻이 되었습니다.",
    "example_words": [
      { "word": "外国", "reading": "がいこく", "meaning": "외국", "description": "우리나라 밖(外)의 나라(国)를 뜻합니다." },
      { "word": "外す", "reading": "はずす", "meaning": "떼다, 벗기다", "description": "원래 있던 자리에서 바깥(外)으로 분리한다는 뜻입니다." }
    ]
  },
  {
    "kanji": "角",
    "reading_on": "カク",
    "reading_kun": "かど、つの",
    "meaning": "뿔 / 모서리",
    "components": [
      { "char": "角", "role": "뿔 각 (부수)", "desc": "짐승의 뾰족한 뿔과 그 아래 주름을 본뜬 상형문자입니다." }
    ],
    "story": "짐승의 단단하고 뾰족한 뿔의 모습을 그대로 그렸으며, 뿔처럼 튀어나온 '모서리'나 '각도'를 뜻합니다.",
    "example_words": [
      { "word": "角度", "reading": "かくど", "meaning": "각도", "description": "모서리(角)가 벌어진 정도(度)를 말합니다." },
      { "word": "四つ角", "reading": "よつかど", "meaning": "네거리", "description": "네 개(四)의 모서리(角)가 만나는 교차로입니다." }
    ]
  },
  {
    "kanji": "楽",
    "reading_on": "ガク、ラク",
    "reading_kun": "たの(しい)",
    "meaning": "즐겁다 / 음악",
    "components": [
      { "char": "白", "role": "흰 백 (부수)", "desc": "나무 틀 위에 올려진 북의 둥근 통 부분을 뜻합니다. (원래는 둥글다는 의미)" },
      { "char": "木", "role": "나무 목 (요소)", "desc": "악기를 받치는 나무 받침대입니다." },
      { "char": "幺", "role": "작을 요 (요소)", "desc": "악기에 달린 방울이나 장식을 뜻합니다. (좌우의 점들)" }
    ],
    "story": "나무(木) 틀 위에 올려진 북(白)과 방울 장식(幺)을 두드리며 연주하는 '음악'이 사람을 '즐겁게' 한다는 의미입니다.",
    "example_words": [
      { "word": "音楽", "reading": "おんがく", "meaning": "음악", "description": "소리(音)로 즐거움(楽)을 표현하는 예술입니다." },
      { "word": "気楽", "reading": "きらく", "meaning": "편안함", "description": "마음(気)이 편안하고 즐거운(楽) 상태입니다." }
    ]
  },
  {
    "kanji": "活",
    "reading_on": "カツ",
    "reading_kun": "い(きる)",
    "meaning": "살다 / 활동하다",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "생명을 유지하게 하는 물을 뜻합니다." },
      { "char": "舌", "role": "혀 설 (요소)", "desc": "침이 도는 혀를 뜻하며, 발음 '괄/활'을 나타냅니다." }
    ],
    "story": "물(氵)이 흐르듯 혀(舌)에 침이 마르지 않는 것이 생기가 넘쳐 '살아 움직임'을 뜻합니다.",
    "example_words": [
      { "word": "生活", "reading": "せいかつ", "meaning": "생활", "description": "살아가면서(生) 활동하는(活) 것을 뜻합니다." },
      { "word": "活発", "reading": "かっぱつ", "meaning": "활발", "description": "살아(活) 움직이는 기운이 일어난다(発)는 뜻입니다." }
    ]
  },
  {
    "kanji": "間",
    "reading_on": "カン、ケン",
    "reading_kun": "あいだ、ま",
    "meaning": "사이",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "양쪽으로 열리는 두 짝의 문입니다." },
      { "char": "日", "role": "날 일 (요소)", "desc": "태양이나 빛을 뜻합니다." }
    ],
    "story": "문(門)틈 사이로 쏟아져 들어오는 햇빛(日)을 나타내어 사물과 사물의 '사이'나 시간적 '간격'을 뜻합니다.",
    "example_words": [
      { "word": "時間", "reading": "じかん", "meaning": "시간", "description": "때(時)와 때의 사이(間)를 뜻합니다." },
      { "word": "間違い", "reading": "まちがい", "meaning": "틀림, 실수", "description": "간격(間)이 어긋난다(違い)는 뜻에서 실수를 의미합니다." }
    ]
  },
  {
    "kanji": "丸",
    "reading_on": "ガン",
    "reading_kun": "まる(い)",
    "meaning": "둥글다",
    "components": [
      { "char": "丶", "role": "점 주 (부수)", "desc": "모서리가 깎여 나간 것을 표시하는 점입니다." },
      { "char": "九", "role": "아홉 구 (요소)", "desc": "여기서는 구부러진 사람이나 물건의 모습에서 파생되었습니다." }
    ],
    "story": "사람이나 물건이 몸을 굽혀서(九) 뾰족한 곳 없이(丶) '둥글게' 말린 모습을 뜻합니다.",
    "example_words": [
      { "word": "丸薬", "reading": "がんやく", "meaning": "환약", "description": "둥글게(丸) 빚은 약(薬)을 뜻합니다." },
      { "word": "丸見え", "reading": "まるみえ", "meaning": "훤히 다 보임", "description": "전체(丸)가 숨김없이 모두 보인다(見え)는 의미입니다." }
    ]
  },
  {
    "kanji": "岩",
    "reading_on": "ガン",
    "reading_kun": "いわ",
    "meaning": "바위",
    "components": [
      { "char": "山", "role": "뫼 산 (부수)", "desc": "산이나 융기한 지형을 뜻합니다." },
      { "char": "石", "role": "돌 석 (요소)", "desc": "단단한 돌을 의미합니다." }
    ],
    "story": "산(山)을 구성하고 있는 거대하고 단단한 돌(石)인 '바위'를 의미하는 한자입니다.",
    "example_words": [
      { "word": "岩石", "reading": "がんせき", "meaning": "암석", "description": "바위(岩)와 돌(石)을 통틀어 이르는 말입니다." },
      { "word": "一枚岩", "reading": "いちまいいわ", "meaning": "한 덩어리의 바위", "description": "갈라지지 않은 한(一) 장(枚)의 바위(岩)처럼, 조직이 단결된 모습을 비유합니다." }
    ]
  },
  {
    "kanji": "顔",
    "reading_on": "ガン",
    "reading_kun": "かお",
    "meaning": "얼굴",
    "components": [
      { "char": "彦", "role": "선비 언 (요소)", "desc": "이마가 아름다운 남자를 뜻하며, 발음 '안/간'과 형태를 제공합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "사람의 머리나 얼굴을 뜻합니다." }
    ],
    "story": "사람의 머리(頁) 중에서 특히 이마나 눈, 코 등이 반듯하게 자리 잡은 앞면, 즉 '얼굴'을 뜻하는 한자입니다.",
    "example_words": [
      { "word": "笑顔", "reading": "えがお", "meaning": "웃는 얼굴", "description": "활짝 웃는(笑) 얼굴(顔)을 뜻합니다." },
      { "word": "顔色", "reading": "かおいろ", "meaning": "안색", "description": "얼굴(顔)에 나타나는 혈색이나 표정(色)입니다." }
    ]
  },
  {
    "kanji": "汽",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "증기",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물과 관련됨을 나타냅니다." },
      { "char": "气", "role": "기운 기 (요소)", "desc": "수증기나 구름이 피어오르는 기운입니다." }
    ],
    "story": "물(氵)이 끓어올라 기운(气)처럼 퍼져나가는 '증기'를 의미합니다.",
    "example_words": [
      { "word": "汽車", "reading": "きしゃ", "meaning": "기차", "description": "증기(汽)의 힘으로 달리는 차(車)를 뜻합니다." },
      { "word": "汽船", "reading": "きせん", "meaning": "기선", "description": "증기(汽) 기관으로 추진하는 배(船)입니다." }
    ]
  },
  {
    "kanji": "記",
    "reading_on": "キ",
    "reading_kun": "しる(す)",
    "meaning": "기록하다",
    "components": [
      { "char": "言", "role": "말씀 언 (부수)", "desc": "말이나 글, 언어 활동을 뜻합니다." },
      { "char": "己", "role": "몸 기 (요소)", "desc": "자기 자신을 뜻하며, '기'라는 발음을 담당합니다." }
    ],
    "story": "자신(己)이 겪은 일이나 생각한 말(言)을 잊지 않기 위해 글로 '기록하다'라는 뜻의 한자입니다.",
    "example_words": [
      { "word": "日記", "reading": "にっき", "meaning": "일기", "description": "매일(日) 일어난 일을 기록한(記) 글입니다." },
      { "word": "記憶", "reading": "きおく", "meaning": "기억", "description": "기록(記)하고 뜻을 생각하여(憶) 머릿속에 담아두는 것입니다." }
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

print("Grade 2 Part 2 data appended successfully.")
