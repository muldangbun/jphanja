import json

with open('kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, sentence in enumerate(data):
    s_str = json.dumps(sentence, ensure_ascii=False)
    if '부터' in s_str:
        print(f"FOUND '부터' in sentence {i}")
        print(s_str)
