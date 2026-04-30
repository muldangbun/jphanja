import json
import re

with open('d:/ag_coding_ex/jphanja/kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    data = json.load(f)

japanese_pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF\u3005\u3000-\u303F\uff01-\uff0f\uff1a-\uff1f\u0020-\u007E]')

for item in data:
    id = item['id']
    kanji = item['kanji']
    kana = item['kana']
    
    # Find any characters that are NOT Japanese, Punctuation, or ASCII
    bad_kanji = [c for c in kanji if not japanese_pattern.match(c)]
    bad_kana = [c for c in kana if not japanese_pattern.match(c)]
    
    if bad_kanji or bad_kana:
        print(f"ID {id}:")
        if bad_kanji: print(f"  Bad Kanji: {''.join(bad_kanji)} in '{kanji}'")
        if bad_kana: print(f"  Bad Kana: {''.join(bad_kana)} in '{kana}'")
