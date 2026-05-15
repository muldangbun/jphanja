import json
import re
import os

KOREAN_REGEX = re.compile(r'[\uac00-\ud7af]')

def check_json_file(file_path):
    print(f"\nChecking {file_path}...")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return

    def scan(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_path = f"{path}.{k}" if path else k
                if k in ['kanji', 'kana', 'word', 'readings_on', 'readings_kun', 'title']:
                    text = v if isinstance(v, str) else ""
                    if k == 'title':
                        text = text.split('(')[0]
                    
                    found = KOREAN_REGEX.findall(text)
                    if found:
                        hex_codes = [hex(ord(c)) for c in found]
                        print(f"FOUND KOREAN in {new_path}: {text} (Codes: {hex_codes})")
                
                scan(v, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                scan(item, f"{path}[{i}]")

    scan(data)

files = ['kaninotokoya.JSON', 'kanji_grade1.json', 'kanji_grade2.json', 'kanji_grade3.json']
for f in files:
    check_json_file(f)
