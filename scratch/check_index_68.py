import json

with open('kanji_grade2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Index 68 kanji: {repr(data[68]['kanji'])}")
print(f"Index 68 word 1: {repr(data[68]['examples'][1]['word'])}")
