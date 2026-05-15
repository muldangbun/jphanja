import json

with open('kanji_grade3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Index 32: {data[32]}")
