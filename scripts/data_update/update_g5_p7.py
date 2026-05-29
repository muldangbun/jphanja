import json
import os

new_data = [
  {
    "kanji": "非",
    "reading_on": "ヒ",
    "reading_kun": "あら(ず)",
    "meaning": "아닐 (비)",
    "components": [
      { "char": "非", "role": "아닐 비 (부수)", "desc": "새의 양쪽 날개가 서로 등지고 벌어진 모양을 본뜬 글자입니다." }
    ],
    "story": "새의 날개가 서로 반대 방향으로 엇갈린 모양에서 서로 어긋나고 '아니다(그르다)' 혹은 어긋난 '잘못'을 뜻합니다.",
    "example_words": [
      { "word": "非常", "reading": "ひじょう", "meaning": "비상, 대단히", "description": "평범하고 항상(常) 있는 일이 아님(非), 즉 특별하거나 위급한 때입니다." },
      { "word": "非常口", "reading": "ひじょうぐち", "meaning": "비상구", "description": "위급할(非常) 때 피해서 나가는 문(口)입니다." }
    ]
  },
  {
    "kanji": "預",
    "reading_on": "ヨ",
    "reading_kun": "あず(ける)、あず(かる)",
    "meaning": "맡길",
    "components": [
      { "char": "予", "role": "나 여 (요소)", "desc": "밀어낸다는 뜻에서 미리라는 의미와 발음 '여/요'를 줍니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "머리나 사람을 의미합니다." }
    ],
    "story": "사람(頁)이 돈이나 물건을 미리(予) 다른 사람에게 내어주어 잠시 보관하도록 '맡기다(예금하다)'는 뜻입니다.",
    "example_words": [
      { "word": "預ける", "reading": "あずける", "meaning": "맡기다", "description": "물건이나 돈을 남에게 보관하게 하거나, 일을 부탁하는 것입니다." },
      { "word": "預金", "reading": "よきん", "meaning": "예금", "description": "은행 따위에 돈(金)을 맡겨(預) 두는 일입니다." }
    ]
  },
  {
    "kanji": "領",
    "reading_on": "リョウ",
    "reading_kun": "",
    "meaning": "거느릴 (영역)",
    "components": [
      { "char": "令", "role": "명령 령 (요소)", "desc": "명령을 내린다는 뜻과 발음 '령/료우'를 줍니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "머리나 목을 의미합니다." }
    ],
    "story": "원래 사람의 가장 중요한 부분인 '목'을 뜻했으나, 나중에는 명령(令)을 내리는 우두머리(頁)라는 뜻으로 바뀌어 조직이나 나라를 '거느리다', 다스리는 '영토(영역)'를 뜻하게 되었습니다.",
    "example_words": [
      { "word": "領収書", "reading": "りょうしゅうしょ", "meaning": "영수증", "description": "돈이나 물건을 거두어(収) 받아들였음을(領) 증명하는 서류(書)입니다." },
      { "word": "大統領", "reading": "だいとうりょう", "meaning": "대통령", "description": "크게(大) 나라를 거느리고(統) 다스리는(領) 사람입니다." }
    ]
  },
  {
    "kanji": "額",
    "reading_on": "ガク",
    "reading_kun": "ひたい",
    "meaning": "이마 (액수)",
    "components": [
      { "char": "客", "role": "손 객 (요소)", "desc": "손님을 뜻하나 여기서는 발음 '객/가쿠'의 변형 역할을 합니다." },
      { "char": "頁", "role": "머리 혈 (부수)", "desc": "머리나 얼굴을 뜻합니다." }
    ],
    "story": "사람의 얼굴(頁) 윗부분에 있는 '이마'를 뜻하며, 건물의 이마에 해당하는 '간판(현판)'이나 돈의 총량인 '액수'를 뜻하기도 합니다.",
    "example_words": [
      { "word": "額", "reading": "ひたい", "meaning": "이마", "description": "얼굴에서 눈썹 위부터 머리카락이 난 아래까지의 부분입니다." },
      { "word": "金額", "reading": "きんがく", "meaning": "금액", "description": "돈(金)의 많고 적은 액수(額)입니다." }
    ]
  },
  {
    "kanji": "飼",
    "reading_on": "シ",
    "reading_kun": "か(う)",
    "meaning": "기를 (먹일)",
    "components": [
      { "char": "食", "role": "밥 식 (부수)", "desc": "음식이나 먹이를 뜻합니다." },
      { "char": "司", "role": "맡을 사 (요소)", "desc": "일을 맡아본다는 뜻과 발음 '사/시'를 줍니다." }
    ],
    "story": "동물에게 먹이(食)를 주고 돌보는 일을 맡아(司) 가축이나 짐승을 '기르다' 혹은 '먹이다'는 의미입니다.",
    "example_words": [
      { "word": "飼う", "reading": "かう", "meaning": "기르다", "description": "집에서 짐승이나 새 따위에게 먹이를 주며 키우는 일입니다." },
      { "word": "飼育", "reading": "しいく", "meaning": "사육", "description": "가축 등을 먹이를 주고 먹여서(飼) 기르는(育) 일입니다." }
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

print("Grade 5 Part 7 data appended successfully.")
