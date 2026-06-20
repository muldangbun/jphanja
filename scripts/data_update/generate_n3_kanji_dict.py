import os
import json
import glob
import re

def generate_kanji_dict():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
    radical_data_dir = os.path.join(base_dir, 'radical', 'src', 'data')
    output_dir = os.path.join(base_dir, 'n3_vocab', 'src', 'data')
    output_file = os.path.join(output_dir, 'kanji_dict.json')

    kanji_dict = {}

    pattern = os.path.join(radical_data_dir, 'kanjiDecomposerData*.json')
    files = glob.glob(pattern)
    
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                for item in data:
                    kanji = item.get('kanji')
                    if not kanji:
                        continue
                    
                    kanji_dict[kanji] = {
                        "reading_on": item.get('reading_on', ''),
                        "reading_kun": item.get('reading_kun', ''),
                        "meaning": item.get('meaning', ''),
                        "story": item.get('story', ''),
                        "components": item.get('components', [])
                    }
            except Exception as e:
                print(f"Error parsing {file}: {e}")

    os.makedirs(output_dir, exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(kanji_dict, f, ensure_ascii=False, indent=2)

    print(f"Generated {output_file} with {len(kanji_dict)} kanji entries.")

if __name__ == '__main__':
    generate_kanji_dict()
