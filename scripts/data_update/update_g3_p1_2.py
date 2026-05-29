import json
import os

new_data = [
  {
    "kanji": "屋",
    "reading_on": "オク",
    "reading_kun": "や",
    "meaning": "집 / 가게",
    "components": [
      { "char": "尸", "role": "주검 시 (부수)", "desc": "사람이 앉아 있는 모습이거나, 여기서는 지붕을 덮은 집 모양을 뜻합니다." },
      { "char": "至", "role": "이를 지 (요소)", "desc": "화살이 꽂힌 모양에서 유래하여 어떤 장소에 이르는 것을 뜻합니다." }
    ],
    "story": "지붕(尸) 아래 사람들이 다다르고(至) 쉴 수 있는 장소인 '집'을 뜻하며, 사람들이 모이는 상점인 '가게'를 의미하기도 합니다.",
    "example_words": [
      { "word": "屋上", "reading": "おくじょう", "meaning": "옥상", "description": "집(屋)의 맨 위(上)입니다." },
      { "word": "本屋", "reading": "ほんや", "meaning": "서점", "description": "책(本)을 파는 가게(屋)입니다." }
    ]
  },
  {
    "kanji": "温",
    "reading_on": "オン",
    "reading_kun": "あたた(かい)、あたた(まる)",
    "meaning": "따뜻할",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물과 관련된 것을 의미합니다." },
      { "char": "囚", "role": "가둘 수 (요소)", "desc": "본래 皿(그릇 명) 위에 담긴 음식을 뜻하는 글자의 변형입니다." },
      { "char": "皿", "role": "그릇 명 (요소)", "desc": "음식을 담는 그릇을 뜻합니다." }
    ],
    "story": "그릇(皿) 안에 물(氵)이나 국을 담아 두어 김이 모락모락 나며 '따뜻하다'는 뜻을 지니게 되었습니다.",
    "example_words": [
      { "word": "温度", "reading": "おんど", "meaning": "온도", "description": "따뜻하고(温) 차가운 정도(度)를 나타냅니다." },
      { "word": "温かい", "reading": "あたたかい", "meaning": "따뜻하다", "description": "마음이나 온도가 포근하고 따뜻한 상태입니다." }
    ]
  },
  {
    "kanji": "化",
    "reading_on": "カ、ケ",
    "reading_kun": "ば(ける)",
    "meaning": "될 / 모양이 변하다",
    "components": [
      { "char": "亻", "role": "사람 인 (부수)", "desc": "똑바로 서 있는 사람을 나타냅니다." },
      { "char": "匕", "role": "비수 비 (요소)", "desc": "여기서는 사람이 거꾸로 뒤집힌 모양으로 쓰였습니다." }
    ],
    "story": "똑바로 선 사람(亻)이 뒤집힌 모양(匕)으로 바뀌는 모습에서 유래하여, 본래의 형태에서 휙 '모양이 변하다' 혹은 다른 것으로 '되다'는 의미입니다.",
    "example_words": [
      { "word": "変化", "reading": "へんか", "meaning": "변화", "description": "다른 모양으로 바뀌어(変) 다르게 되는(化) 것입니다." },
      { "word": "お化け", "reading": "おばけ", "meaning": "도깨비, 귀신", "description": "모양이 변하여(化け) 놀라게 하는 존재입니다." }
    ]
  },
  {
    "kanji": "荷",
    "reading_on": "カ",
    "reading_kun": "に",
    "meaning": "짐",
    "components": [
      { "char": "艹", "role": "초두머리 (부수)", "desc": "풀이나 식물을 뜻합니다." },
      { "char": "何", "role": "어찌 하 (요소)", "desc": "사람이 어깨에 짐을 멘 모양에서 유래하였으며 '카/하' 발음을 줍니다." }
    ],
    "story": "원래는 어깨에 멘 연잎(艹)이나 짐을 뜻하다가, 사람(何)이 짊어지고 다니는 무거운 식물 줄기나 풀 더미 같은 '짐' 자체를 의미하게 되었습니다.",
    "example_words": [
      { "word": "荷物", "reading": "にもつ", "meaning": "짐, 수화물", "description": "어깨에 메는 짐(荷)과 물건(物)입니다." },
      { "word": "重荷", "reading": "おもに", "meaning": "무거운 짐", "description": "무게가 무거운(重) 짐(荷)입니다." }
    ]
  },
  {
    "kanji": "界",
    "reading_on": "カイ",
    "reading_kun": "",
    "meaning": "지경 / 세계",
    "components": [
      { "char": "田", "role": "밭 전 (부수)", "desc": "나누어진 밭이나 땅을 의미합니다." },
      { "char": "介", "role": "낄 개 (요소)", "desc": "사람(人) 사이에 끼어 있는 경계선(八)을 나타냅니다." }
    ],
    "story": "사람들 사이에(介) 구역을 나누어 밭(田)의 경계선을 그었다는 뜻으로, '지경(경계)' 혹은 특정한 구역이나 '세계'를 뜻합니다.",
    "example_words": [
      { "word": "世界", "reading": "せかい", "meaning": "세계", "description": "우리가 사는 인간 세상(世)의 전체 구역(界)입니다." },
      { "word": "限界", "reading": "げんかい", "meaning": "한계", "description": "더 이상 나아갈 수 없는 한정된(限) 경계(界)입니다." }
    ]
  },
  {
    "kanji": "開",
    "reading_on": "カイ",
    "reading_kun": "あ(く)、ひら(く)",
    "meaning": "열 / 열리다",
    "components": [
      { "char": "門", "role": "문 문 (부수)", "desc": "양쪽으로 닫힌 큰 대문을 뜻합니다." },
      { "char": "廾", "role": "두 손 멱 (요소)", "desc": "두 손으로 무언가를 쥐거나 여는 동작을 나타냅니다." },
      { "char": "一", "role": "한 일 (요소)", "desc": "빗장을 의미합니다." }
    ],
    "story": "대문(門)의 빗장(一)을 두 손(廾)으로 잡고 활짝 '열다' 혹은 저절로 문이 '열리다'는 뜻입니다.",
    "example_words": [
      { "word": "開く", "reading": "あく", "meaning": "열리다", "description": "문이나 가게가 닫혀있지 않고 열리는 것입니다." },
      { "word": "開始", "reading": "かいし", "meaning": "개시, 시작", "description": "문을 열어(開) 일을 처음 시작(始)하는 것입니다." }
    ]
  },
  {
    "kanji": "階",
    "reading_on": "カイ",
    "reading_kun": "",
    "meaning": "섬돌 (계단) / 층",
    "components": [
      { "char": "阝", "role": "좌부변 (부수)", "desc": "언덕이나 흙으로 쌓은 담장을 의미합니다." },
      { "char": "皆", "role": "다 개 (요소)", "desc": "사람들이 여럿 모여서 한꺼번에 소리친다는 데서 '모두', 발음 '카이/개'를 줍니다." }
    ],
    "story": "언덕(阝)을 오르기 위해 사람들이 다 함께(皆) 차곡차곡 줄지어 밟고 올라가는 '계단'이나 건물의 '층'을 의미합니다.",
    "example_words": [
      { "word": "階段", "reading": "かいだん", "meaning": "계단", "description": "오르내리기 위해 만든 층계(階)와 단(段)입니다." },
      { "word": "二階", "reading": "にかい", "meaning": "2층", "description": "건물의 두(二) 번째 층(階)입니다." }
    ]
  },
  {
    "kanji": "貝",
    "reading_on": "バイ",
    "reading_kun": "かい",
    "meaning": "조개",
    "components": [
      { "char": "貝", "role": "조개 패 (부수)", "desc": "조개의 껍데기 모양을 본뜬 상형문자입니다." }
    ],
    "story": "조개의 껍데기를 그린 한자로, 고대에는 둥글고 예쁜 조개껍데기가 돈으로 쓰여 '재물'이나 '돈'을 뜻하는 부수로 많이 쓰입니다.",
    "example_words": [
      { "word": "貝殻", "reading": "かいがら", "meaning": "조개껍데기", "description": "조개(貝)의 단단한 껍질(殻)입니다." },
      { "word": "巻き貝", "reading": "まきがい", "meaning": "고둥", "description": "껍질이 돌돌 말린(巻き) 조개(貝)입니다." }
    ]
  },
  {
    "kanji": "寒",
    "reading_on": "カン",
    "reading_kun": "さむ(い)",
    "meaning": "찰 / 춥다",
    "components": [
      { "char": "宀", "role": "갓머리 (부수)", "desc": "건물이나 지붕을 뜻합니다." },
      { "char": "艹", "role": "초두머리 (요소)", "desc": "풀이나 짚단입니다." },
      { "char": "人", "role": "사람 인 (요소)", "desc": "사람입니다." },
      { "char": "冫", "role": "이수변 (요소)", "desc": "얼음이나 차가운 기운입니다." }
    ],
    "story": "집(宀) 안에서 풀과 짚단(艹)으로 몸을 덮은 사람(人)이 바닥의 얼음(冫) 기운 때문에 몸을 떨며 '춥다'고 느끼는 모습입니다.",
    "example_words": [
      { "word": "寒い", "reading": "さむい", "meaning": "춥다", "description": "날씨나 기온이 차가운 상태입니다." },
      { "word": "寒気", "reading": "さむけ", "meaning": "오한", "description": "몸이 으스스하게 춥고(寒) 떨리는 기운(気)입니다." }
    ]
  },
  {
    "kanji": "感",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "느낄",
    "components": [
      { "char": "咸", "role": "다 함 (요소)", "desc": "무기로 상처를 내다라는 원래 뜻에서 모두 닫다, 혹은 꽉 채우다로 쓰이며 발음 '칸'을 줍니다." },
      { "char": "心", "role": "마음 심 (부수)", "desc": "마음이나 감정입니다." }
    ],
    "story": "바늘로 찌르는 듯한 깊은 자극이 마음(心)속에 모두(咸) 퍼져들어 강하게 무언가를 '느끼다'는 뜻입니다.",
    "example_words": [
      { "word": "感動", "reading": "かんどう", "meaning": "감동", "description": "깊이 느껴서(感) 마음이 움직이는(動) 일입니다." },
      { "word": "感情", "reading": "かんじょう", "meaning": "감정", "description": "마음속에서 느껴서(感) 일어나는 뜻과 정(情)입니다." }
    ]
  },
  {
    "kanji": "漢",
    "reading_on": "カン",
    "reading_kun": "",
    "meaning": "한나라 (한수)",
    "components": [
      { "char": "氵", "role": "삼수변 (부수)", "desc": "물이나 강을 의미합니다." },
      { "char": "廿", "role": "스물 입 (요소)", "desc": "여기서는 황토밭이나 진흙을 상징하는 글자의 변형입니다." },
      { "char": "夫", "role": "사내 부 (요소)", "desc": "진흙탕에서 일하는 성인 남자의 모양입니다." }
    ],
    "story": "강(氵)에서 진흙(廿)을 퍼내며 일하는 남자(夫)들이 있는 중국의 '한(漢)수'라는 강 이름에서 유래하여 나중에는 중국의 '한나라'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "漢字", "reading": "かんじ", "meaning": "한자", "description": "한나라(漢) 때부터 쓰이던 중국의 글자(字)입니다." },
      { "word": "漢方薬", "reading": "かんぽうやく", "meaning": "한약", "description": "한나라(漢)의 방법(方)대로 지은 약(薬)입니다." }
    ]
  },
  {
    "kanji": "館",
    "reading_on": "カン",
    "reading_kun": "やかた",
    "meaning": "집 / 여관",
    "components": [
      { "char": "食", "role": "밥 식 (부수)", "desc": "밥, 식사, 음식을 의미합니다." },
      { "char": "官", "role": "벼슬 관 (요소)", "desc": "관리들이 일하는 관청이나 집을 뜻하며 발음 '관/칸'을 줍니다." }
    ],
    "story": "관리(官)들이 묵으면서 밥(食)을 먹고 쉴 수 있도록 만들어진 큰 '집'이나 '여관(숙소)'을 의미합니다.",
    "example_words": [
      { "word": "図書館", "reading": "としょかん", "meaning": "도서관", "description": "그림(図)과 책(書)을 모아둔 큰 집(館)입니다." },
      { "word": "水族館", "reading": "すいぞくかん", "meaning": "수족관", "description": "물(水)속 생물 족속(族)을 전시해 놓은 집(館)입니다." }
    ]
  },
  {
    "kanji": "岸",
    "reading_on": "ガン",
    "reading_kun": "きし",
    "meaning": "언덕 (기슭)",
    "components": [
      { "char": "山", "role": "뫼 산 (부수)", "desc": "높은 산을 뜻합니다." },
      { "char": "厂", "role": "기슭 엄 (요소)", "desc": "바위 벼랑이나 산기슭을 뜻합니다." },
      { "char": "干", "role": "방패 간 (요소)", "desc": "절구공이나 무기를 든 모습으로 깎아지른 듯한 모양과 '간/간' 발음을 줍니다." }
    ],
    "story": "높은 산(山)에서 가파르게 깎아지른 바위 벼랑(厂)처럼 물가로 이어진 '언덕'이나 물'기슭'을 뜻합니다.",
    "example_words": [
      { "word": "海岸", "reading": "かいがん", "meaning": "해안", "description": "바다(海)와 맞닿은 기슭(岸)입니다." },
      { "word": "川岸", "reading": "かわぎし", "meaning": "강기슭", "description": "강(川)이 흐르는 둑과 기슭(岸)입니다." }
    ]
  },
  {
    "kanji": "起",
    "reading_on": "キ",
    "reading_kun": "お(きる)、お(こす)",
    "meaning": "일어날",
    "components": [
      { "char": "走", "role": "달릴 주 (부수)", "desc": "사람이 달리기 위해 발을 딛고 움직이는 모습입니다." },
      { "char": "己", "role": "몸 기 (요소)", "desc": "자기 자신을 뜻하거나 굽어 있던 것이 펴진다는 발음 '기/키'를 나타냅니다." }
    ],
    "story": "구부리고 있던 몸(己)을 쫙 펴고 달릴(走) 준비를 하며 자리에서 '일어나다' 혹은 사건을 '일으키다'는 뜻입니다.",
    "example_words": [
      { "word": "起きる", "reading": "おきる", "meaning": "일어나다", "description": "아침에 잠자리에서 일어나거나 사건이 일어나는 일입니다." },
      { "word": "早起き", "reading": "はやおき", "meaning": "일찍 일어남", "description": "아침 일찍(早) 일어나는(起き) 것입니다." }
    ]
  },
  {
    "kanji": "期",
    "reading_on": "キ",
    "reading_kun": "",
    "meaning": "기약할 (기간)",
    "components": [
      { "char": "其", "role": "그 기 (요소)", "desc": "키(곡식을 까부르는 도구)의 모양에서 유래하여 어떤 정해진 시기나 발음 '기/키'를 나타냅니다." },
      { "char": "月", "role": "달 월 (부수)", "desc": "달의 움직임, 즉 시간이나 기간을 뜻합니다." }
    ],
    "story": "달(月)이 차고 기우는 것을 보고, 정해진 어떤 시기(其)가 다시 돌아오기를 '기약하다' 혹은 일정한 '기간'을 뜻하게 되었습니다.",
    "example_words": [
      { "word": "期間", "reading": "きかん", "meaning": "기간", "description": "기약된(期) 시간의 사이(間)입니다." },
      { "word": "期待", "reading": "きたい", "meaning": "기대", "description": "어떤 일이 이루어질 기간(期)을 정해놓고 기다리는(待) 일입니다." }
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

print("Grade 3 Part 1.2 data appended successfully.")
