import json
import re
import os

# Korean character range
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
                # Fields that should be Japanese only (no Korean)
                # Note: 'title' often has (Korean) at the end, so we check only the part before '('
                if k in ['kanji', 'kana', 'word', 'readings_on', 'readings_kun']:
                    if isinstance(v, str) and KOREAN_REGEX.search(v):
                        print(f"FOUND KOREAN in {new_path}: {v}")
                    elif isinstance(v, list):
                        for i, item in enumerate(v):
                            if isinstance(item, str) and KOREAN_REGEX.search(item):
                                print(f"FOUND KOREAN in {new_path}[{i}]: {item}")
                elif k == 'title':
                    if isinstance(v, str):
                        # Check text before the first parenthesis
                        parts = v.split('(')
                        japanese_part = parts[0]
                        if KOREAN_REGEX.search(japanese_part):
                            print(f"FOUND KOREAN in title {new_path}: {v}")
                
                scan(v, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                scan(item, f"{path}[{i}]")

    scan(data)

files = ['kaninotokoya.JSON', 'kanji_grade1.json', 'kanji_grade2.json', 'kanji_grade3.json']
for f in files:
    check_json_file(f)
