import json
import os

base_dir = r"d:\ag_coding_ex\jphanja"
kanji_dir = os.path.join(base_dir, "data", "kanji")
radical_data_dir = os.path.join(base_dir, "radical", "src", "data")

for grade in range(2, 7):
    main_file = os.path.join(kanji_dir, f"kanji_grade{grade}.json")
    radical_file = os.path.join(radical_data_dir, f"kanjiDecomposerData_grade{grade}.json")
    
    if not os.path.exists(main_file) or not os.path.exists(radical_file):
        print(f"Skipping grade {grade} - files not found.")
        continue
        
    with open(main_file, "r", encoding="utf-8") as f:
        main_data = json.load(f)
        
    with open(radical_file, "r", encoding="utf-8") as f:
        radical_data = json.load(f)
        
    # Create a lookup dictionary for main data
    kanji_lookup = {}
    for item in main_data:
        kor_meaning = item.get("kor_meaning", "")
        kor_sound = item.get("kor_sound", "")
        if kor_meaning and kor_sound:
            kanji_lookup[item["kanji"]] = f"{kor_meaning} {kor_sound}"
            
    # Update radical data
    updated_count = 0
    for item in radical_data:
        kanji = item["kanji"]
        if kanji in kanji_lookup:
            item["meaning"] = kanji_lookup[kanji]
            updated_count += 1
            
    with open(radical_file, "w", encoding="utf-8") as f:
        json.dump(radical_data, f, ensure_ascii=False, indent=2)
        
    print(f"Grade {grade}: Updated {updated_count} items.")

print("Update complete.")
