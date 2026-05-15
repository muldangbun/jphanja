import json

with open('kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, sentence in enumerate(data):
    if 'grammar' in sentence:
        for p in sentence['grammar'].get('points', []):
            if '까지' in p['title']:
                print(f"[{i}] {p['title']}")
