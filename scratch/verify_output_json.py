import json
import os
import re

hangul_re = re.compile(r'[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318f]')
english_re = re.compile(r'[a-zA-Z]')

def verify_json(file_path, expected_count, expected_grade):
    print(f"Verifying {file_path}...")
    if not os.path.exists(file_path):
        print(f"FAIL: File does not exist: {file_path}")
        return False
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"FAIL: JSON parse error: {e}")
        return False
        
    if not isinstance(data, list):
        print("FAIL: JSON root is not a list")
        return False
        
    if len(data) != expected_count:
        print(f"FAIL: Count mismatch. Expected {expected_count}, got {len(data)}")
        return False
        
    required_keys = {
        "kanji", "grade", "strokes", "meanings", "kor_meaning",
        "kor_sound", "readings_on", "romaji_on", "readings_kun",
        "romaji_kun", "examples"
    }
    
    errors = 0
    for idx, item in enumerate(data):
        # check keys
        missing_keys = required_keys - item.keys()
        if missing_keys:
            print(f"  [Item {idx}] Missing keys: {missing_keys}")
            errors += 1
            continue
            
        # check grade
        if item["grade"] != expected_grade:
            print(f"  [Item {idx}] Grade mismatch: expected {expected_grade}, got {item['grade']}")
            errors += 1
            
        # check examples
        exs = item["examples"]
        if not isinstance(exs, list) or len(exs) != 2:
            print(f"  [Item {idx} Kanji '{item['kanji']}'] Expected 2 examples, got {len(exs) if isinstance(exs, list) else type(exs)}")
            errors += 1
            continue
            
        for ex_idx, ex in enumerate(exs):
            if not isinstance(ex, dict) or not all(k in ex for k in ["word", "meaning", "romaji"]):
                print(f"  [Item {idx} Kanji '{item['kanji']}'] Invalid example format: {ex}")
                errors += 1
                continue
                
            word = ex["word"]
            # Extract word_jp and reading_jp
            if '(' in word:
                word_jp = word.split('(')[0]
                reading_jp = word.split('(')[1].split(')')[0]
            else:
                word_jp = word
                reading_jp = ""
                print(f"  [Item {idx} Kanji '{item['kanji']}'] Example word '{word}' has no reading in parentheses!")
                errors += 1
                
            # Check for Hangul or English in Japanese word part
            if hangul_re.search(word_jp):
                print(f"  [Item {idx} Kanji '{item['kanji']}'] Hangul found in Japanese word '{word_jp}'!")
                errors += 1
            if english_re.search(word_jp):
                print(f"  [Item {idx} Kanji '{item['kanji']}'] English found in Japanese word '{word_jp}'!")
                errors += 1
                
            # Check for Hangul or English in Japanese reading part
            if hangul_re.search(reading_jp):
                print(f"  [Item {idx} Kanji '{item['kanji']}'] Hangul found in Japanese reading '{reading_jp}'!")
                errors += 1
            if english_re.search(reading_jp):
                print(f"  [Item {idx} Kanji '{item['kanji']}'] English found in Japanese reading '{reading_jp}'!")
                errors += 1

    if errors == 0:
        print(f"SUCCESS: {file_path} verified successfully! {len(data)} items validated.")
        return True
    else:
        print(f"FAIL: {file_path} contains {errors} validation errors.")
        return False

success = True
success &= verify_json("d:/ag_coding_ex/jphanja/kanji_grade5.json", 185, 5)
success &= verify_json("d:/ag_coding_ex/jphanja/kanji_grade6.json", 181, 6)

if success:
    print("\nALL VERIFICATIONS PASSED!")
else:
    print("\nVERIFICATION FAILED!")
