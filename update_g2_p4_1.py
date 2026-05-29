import json
import os

new_data = [
  {
    "kanji": "時",
    "reading_on": "ジ",
    "reading_kun": "とき",
    "meaning": "때 / 시간",
    "components": [
      { "char": "日", "role": "날 일 (부수)", "desc": "태양의 움직임을 뜻하며, 옛날에는 해시계로 쓰였습니다." },
      { "char": "寺", "role": "절 사 (요소)", "desc": "관청이나 절을 의미하며, 규칙적으로 정해진 것을 나타내고 '시/지' 발음을 줍니다." }
    ],
    "story": "해(日)가 움직이는 것을 보고 관청(寺)에서 규칙적으로 백성들에게 '시간'을 알려주던 데서 유래했습니다.",
    "example_words": [
      { "word": "時間", "reading": "じかん", "meaning": "시간", "description": "때(時)와 때의 사이(間)입니다." },
      { "word": "時計", "reading": "とけい", "meaning": "시계", "description": "시간(時)을 셈하는(計) 기계입니다." }
    ]
  },
  {
    "kanji": "室",
    "reading_on": "シツ",
    "reading_kun": "むろ",
    "meaning": "방",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "지붕이나 건물을 뜻합니다." },
      { "char": "至", "role": "이를 지 (요소)", "desc": "화살이 꽂힌 모양에서 유래하여, 깊숙하게 이르다, 닿다라는 뜻입니다." }
    ],
    "story": "지붕(宀) 아래 건물의 가장 깊숙한 곳까지 이르러(至) 있는 개인적인 공간인 '방'을 뜻합니다.",
    "example_words": [
      { "word": "教室", "reading": "きょうしつ", "meaning": "교실", "description": "가르치는(教) 방(室)입니다." },
      { "word": "室内", "reading": "しつない", "meaning": "실내", "description": "방(室)의 안쪽(内)입니다." }
    ]
  },
  {
    "kanji": "社",
    "reading_on": "シャ",
    "reading_kun": "やしろ",
    "meaning": "모일 / 토지신",
    "components": [
      { "char": "礻", "role": "보일 시 (부수)", "desc": "제단이나 신에게 제사를 지내는 것을 뜻합니다." },
      { "char": "土", "role": "흙 토 (요소)", "desc": "땅이나 토지를 의미합니다." }
    ],
    "story": "토지(土)의 신에게 제사(礻)를 지내기 위해 마을 사람들이 '모이는' 장소를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "会社", "reading": "かいしゃ", "meaning": "회사", "description": "사람들이 만나(会) 모인 곳(社)입니다." },
      { "word": "社会", "reading": "しゃかい", "meaning": "사회", "description": "사람들이 모여서(社) 만나는(会) 공동체입니다." }
    ]
  },
  {
    "kanji": "弱",
    "reading_on": "ジャク",
    "reading_kun": "よわ(い)",
    "meaning": "약하다",
    "components": [
      { "char": "弓", "role": "활 궁 (부수)", "desc": "탄력 있는 활을 뜻합니다." },
      { "char": "彡", "role": "터럭 삼 (요소)", "desc": "가늘고 부드러운 털 장식이나 연약한 깃털을 의미합니다." }
    ],
    "story": "활(弓)에 부드러운 깃털 장식(彡)을 달아놓은 것처럼, 탄력이 적고 구부러지기 쉬워 '약하다'는 뜻을 나타냅니다. (이 글자가 양옆에 두 개 있습니다)",
    "example_words": [
      { "word": "弱い", "reading": "よわい", "meaning": "약하다", "description": "힘이나 체력이 부족한 상태입니다." },
      { "word": "弱点", "reading": "じゃくてん", "meaning": "약점", "description": "약한(弱) 부분이나 점(点)입니다." }
    ]
  },
  {
    "kanji": "首",
    "reading_on": "シュ",
    "reading_kun": "くび",
    "meaning": "목 / 우두머리",
    "components": [
      { "char": "首", "role": "머리 수 (부수)", "desc": "머리카락(위의 획들)이 있는 사람의 머리와 눈을 강조한 상형문자입니다." }
    ],
    "story": "사람의 머리와 목 부분을 본뜬 모양으로, 신체 부위인 '목'이나 무리의 꼭대기인 '우두머리'를 의미합니다.",
    "example_words": [
      { "word": "手首", "reading": "てくび", "meaning": "손목", "description": "손(手)과 팔이 이어지는 목(首)처럼 잘록한 부분입니다." },
      { "word": "首都", "reading": "しゅと", "meaning": "수도", "description": "나라의 우두머리(首)가 되는 큰 도읍(都)입니다." }
    ]
  },
  {
    "kanji": "秋",
    "reading_on": "シュウ",
    "reading_kun": "あき",
    "meaning": "가을",
    "components": [
      { "char": "禾", "role": "벼 화 (부수)", "desc": "곡식이나 벼를 나타냅니다." },
      { "char": "火", "role": "불 화 (요소)", "desc": "뜨거운 불이나 메뚜기 같은 해충을 불로 태우는 모습에서 유래했습니다." }
    ],
    "story": "익은 벼(禾)를 수확한 후 들판에 불(火)을 질러 해충을 잡는 계절인 '가을'을 뜻합니다. (또는 벼가 불타듯 붉게 익는 가을)",
    "example_words": [
      { "word": "秋晴れ", "reading": "あきばれ", "meaning": "가을의 맑은 날씨", "description": "가을(秋)에 맑게 갠(晴れ) 날입니다." },
      { "word": "春秋", "reading": "しゅんじゅう", "meaning": "춘추 (봄과 가을, 혹은 나이)", "description": "봄(春)과 가을(秋)을 아울러 이르는 말입니다." }
    ]
  },
  {
    "kanji": "週",
    "reading_on": "シュウ",
    "reading_kun": "",
    "meaning": "주일 / 돌다",
    "components": [
      { "char": "辶", "role": "쉬엄쉬엄 갈 착 (부수)", "desc": "길을 걷거나 나아가는 등 이동의 의미를 가집니다." },
      { "char": "周", "role": "두루 주 (요소)", "desc": "밭 둘레를 빙 두른다는 뜻으로 둥글게 도는 것을 의미합니다." }
    ],
    "story": "시간이나 길이 빙 돌아서(周) 다시 원래 자리로 진행해(辶) 오는 주기, 즉 7일을 단위로 하는 '주일'을 뜻합니다.",
    "example_words": [
      { "word": "週末", "reading": "しゅうまつ", "meaning": "주말", "description": "한 주(週)의 끝(末) 부분입니다." },
      { "word": "今週", "reading": "こんしゅう", "meaning": "이번 주", "description": "지금(今)의 주(週)입니다." }
    ]
  },
  {
    "kanji": "春",
    "reading_on": "シュン",
    "reading_kun": "はる",
    "meaning": "봄",
    "components": [
      { "char": "𡗗", "role": "풀밭 (요소)", "desc": "햇볕을 받아 풀(艹)이 싹트는 둔덕의 변형입니다." },
      { "char": "日", "role": "날 일 (부수)", "desc": "따뜻한 태양을 뜻합니다." }
    ],
    "story": "따뜻한 태양(日) 빛을 받아 땅 위로 풀과 새싹이 돋아나는 생명력 넘치는 계절인 '봄'을 의미합니다.",
    "example_words": [
      { "word": "青春", "reading": "せいしゅん", "meaning": "청춘", "description": "푸른(青) 봄(春)처럼 만물이 푸른 봄철, 즉 젊은 시절을 뜻합니다." },
      { "word": "春休み", "reading": "はるやすみ", "meaning": "봄방학", "description": "봄(春)에 쉬는(休み) 기간입니다." }
    ]
  },
  {
    "kanji": "書",
    "reading_on": "ショ",
    "reading_kun": "か(く)",
    "meaning": "글 / 쓰다",
    "components": [
      { "char": "聿", "role": "붓 율 (요소)", "desc": "손으로 붓을 쥐고 있는 모습입니다." },
      { "char": "曰", "role": "가로 왈 (부수)", "desc": "말을 하거나 입에서 나오는 뜻을 담고 있습니다." }
    ],
    "story": "손에 붓(聿)을 쥐고 말(曰)로 전달하려는 내용을 먹으로 찍어 '쓰다', 또는 그렇게 쓴 '글'이나 '책'을 뜻합니다.",
    "example_words": [
      { "word": "辞書", "reading": "じしょ", "meaning": "사전", "description": "말이나 단어(辞)를 모아 놓은 책(書)입니다." },
      { "word": "図書館", "reading": "としょかん", "meaning": "도서관", "description": "그림(図)과 책(書)을 모아 둔 건물(館)입니다." }
    ]
  },
  {
    "kanji": "少",
    "reading_on": "ショウ",
    "reading_kun": "すく(ない)、すこ(し)",
    "meaning": "적다 / 젊다",
    "components": [
      { "char": "小", "role": "작을 소 (부수)", "desc": "크기가 작은 것을 나타냅니다." },
      { "char": "丿", "role": "삐침 (요소)", "desc": "작은 것에서 한 조각이 더 떨어져 나가는 모습입니다." }
    ],
    "story": "크기가 작은(小) 것에서 부스러기마저 떨어져 나가(丿) 수량이 매우 '적다'는 의미를 나타내며, 나이가 적은 '젊다'는 뜻으로도 쓰입니다.",
    "example_words": [
      { "word": "少年", "reading": "しょうねん", "meaning": "소년", "description": "나이가 적은(少) 나이(年)의 남자아이입니다." },
      { "word": "少し", "reading": "すこし", "meaning": "조금", "description": "분량이나 정도가 적은(少) 상태입니다." }
    ]
  },
  {
    "kanji": "場",
    "reading_on": "ジョウ",
    "reading_kun": "ば",
    "meaning": "마당 / 장소",
    "components": [
      { "char": "土", "role": "흙 토 (부수)", "desc": "땅이나 토지를 의미합니다." },
      { "char": "昜", "role": "볕 양 (요소)", "desc": "제단 위로 해가 비치는 모습으로, 평평하게 펴지거나 넓다는 뜻입니다." }
    ],
    "story": "햇빛이 잘 비치는(昜) 평평하고 널찍한 땅(土)을 의미하여, 사람들이 활동하는 '마당'이나 '장소'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "場所", "reading": "ばしょ", "meaning": "장소", "description": "활동하는 마당(場)과 곳(所)입니다." },
      { "word": "立場", "reading": "たちば", "meaning": "입장", "description": "서 있는(立) 장소나 처지(場)를 뜻합니다." }
    ]
  },
  {
    "kanji": "色",
    "reading_on": "ショク、シキ",
    "reading_kun": "いろ",
    "meaning": "빛 / 색",
    "components": [
      { "char": "⺈", "role": "안을 포 (변형)", "desc": "사람의 윗부분을 뜻합니다." },
      { "char": "巴", "role": "꼬리 파 (요소)", "desc": "사람이 몸을 구부린 모습이거나, 다른 사람이 뒤에서 껴안는 모습입니다." }
    ],
    "story": "원래는 사람의 몸이 포개진 모습에서 유래했으나, 얼굴이나 몸에 나타나는 안색이나 안면의 감정 변화를 통해 '빛깔'이나 '색'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "景色", "reading": "けしき", "meaning": "경치", "description": "햇볕에 빛나는 풍경(景)과 그 빛깔(色)입니다." },
      { "word": "色々", "reading": "いろいろ", "meaning": "여러 가지", "description": "색(色)과 종류가 아주 많다는 뜻입니다." }
    ]
  },
  {
    "kanji": "食",
    "reading_on": "ショク",
    "reading_kun": "た(べる)",
    "meaning": "밥 / 먹다",
    "components": [
      { "char": "亼", "role": "모일 집 (요소)", "desc": "음식을 담은 그릇의 뚜껑 모양입니다." },
      { "char": "皀", "role": "고소할 급 (요소)", "desc": "음식이 고소하게 담긴 굽이 있는 그릇 모양입니다." }
    ],
    "story": "뚜껑(亼)이 덮여 있고 맛있는 음식이 듬뿍 담긴 고소한 그릇(皀)을 본떠, '음식'이나 그것을 '먹다'라는 뜻입니다.",
    "example_words": [
      { "word": "食事", "reading": "しょくじ", "meaning": "식사", "description": "음식을 먹는(食) 일(事)입니다." },
      { "word": "食べ物", "reading": "たべもの", "meaning": "음식", "description": "먹는(食べ) 물건(物)입니다." }
    ]
  },
  {
    "kanji": "心",
    "reading_on": "シン",
    "reading_kun": "こころ",
    "meaning": "마음",
    "components": [
      { "char": "心", "role": "마음 심 (부수)", "desc": "사람의 심장(염통) 모양을 본뜬 상형문자입니다." }
    ],
    "story": "피를 뿜어내는 심장의 모습을 본뜬 글자로, 옛 사람들은 심장에 감정과 생각이 깃들어 있다고 믿어 '마음'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "安心", "reading": "あんしん", "meaning": "안심", "description": "마음(心)이 편안한(安) 상태입니다." },
      { "word": "関心", "reading": "かんしん", "meaning": "관심", "description": "어떤 것에 마음(心)이 관계되어(関) 끌리는 것입니다." }
    ]
  },
  {
    "kanji": "新",
    "reading_on": "シン",
    "reading_kun": "あたら(しい)、あら(た)",
    "meaning": "새롭다",
    "components": [
      { "char": "辛", "role": "매울 신 (요소)", "desc": "손잡이가 있는 뾰족한 칼이나 도구를 의미합니다." },
      { "char": "木", "role": "나무 목 (요소)", "desc": "벨 수 있는 나무를 뜻합니다." },
      { "char": "斤", "role": "도끼 근 (부수)", "desc": "도끼의 모습을 나타냅니다." }
    ],
    "story": "칼(辛)과 도끼(斤)를 사용해 나무(木)를 갓 베어내어 결이 생생한 상태에서, 처음 만들어진 '새롭다'는 의미가 되었습니다.",
    "example_words": [
      { "word": "新聞", "reading": "しんぶん", "meaning": "신문", "description": "새롭게(新) 세상의 소식을 듣는(聞) 매체입니다." },
      { "word": "新鮮", "reading": "しんせん", "meaning": "신선", "description": "갓 잡은 물고기처럼 새롭고(新) 생생한(鮮) 것입니다." }
    ]
  }
]

file_path = 'radical/src/data/kanjiDecomposerData_grade2.json'
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

print("Grade 2 Part 4.1 data appended successfully.")
