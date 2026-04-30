import json
import re

def normalize(s):
    return re.sub(r'[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', '', s)

with open('d:/ag_coding_ex/jphanja/kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    id = item['id']
    kanji = item['kanji']
    kana = item['kana']
    
    if normalize(kanji) != normalize(kana):
        print(f"ID {id} mismatch:")
        print(f"  Kanji Norm: {normalize(kanji)}")
        print(f"  Kana Norm:  {normalize(kana)}")
