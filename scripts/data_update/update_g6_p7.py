import json
import os

new_data = [
  {
    "kanji": "骨",
    "reading_on": "コツ",
    "reading_kun": "ほね",
    "meaning": "뼈",
    "components": [
      { "char": "骨", "role": "뼈 골 (부수)", "desc": "살이 발라진 뼈와 관절 모양을 본뜬 글자로, 뼈대나 골격을 의미합니다." }
    ],
    "story": "위쪽은 뼈마디 모양이고 아래쪽(月)은 몸(살)을 뜻하여, 사람이나 동물의 몸을 지탱하는 단단한 '뼈'나 '골격'을 뜻합니다.",
    "example_words": [
      { "word": "骨", "reading": "ほね", "meaning": "뼈, 뼈대", "description": "사람이나 동물의 몸을 이루는 단단한 조직입니다." },
      { "word": "骨折", "reading": "こっせつ", "meaning": "골절", "description": "뼈(骨)가 부러지거나(折) 부서지는 상처입니다." }
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

print("Grade 6 Part 7 data appended successfully.")
