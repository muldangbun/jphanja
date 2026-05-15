import json
import re

KOREAN_RE = re.compile(r'[\uac00-\ud7af]+')

def clean_japanese_part(title):
    # Get part before '('
    jp_part = title.split('(')[0].strip()
    return jp_part

with open('kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("Scanning kaninotokoya.JSON for mixed Korean in grammar titles...")
found_count = 0
for i, sentence in enumerate(data):
    if 'grammar' in sentence:
        for p_idx, p in enumerate(sentence['grammar'].get('points', [])):
            title = p['title']
            jp_part = clean_japanese_part(title)
            if KOREAN_RE.search(jp_part):
                print(f"[{i}].grammar.points[{p_idx}] FOUND: {title}")
                found_count += 1

print(f"Total found: {found_count}")
