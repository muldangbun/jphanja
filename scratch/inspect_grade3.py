import json

with open('kanji_grade3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Index 32: {json.dumps(data[32], ensure_ascii=False)}")
print(f"Index 49: {json.dumps(data[49], ensure_ascii=False)}")
print(f"Index 64: {json.dumps(data[64], ensure_ascii=False)}")
print(f"Index 131: {json.dumps(data[131], ensure_ascii=False)}")
