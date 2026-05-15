
import json
import re

file_path = r'd:\ag_coding_ex\jphanja\kaninotokoya.JSON'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    print(f"Error loading UTF-8: {e}")
    with open(file_path, 'r', encoding='cp949') as f:
        data = json.load(f)

# Search for Korean particles in Japanese parts of grammar titles
# We are looking for "부터" -> "から", "까지" -> "まで", etc.
# The user specifically mentioned "부터"

def check_grammar(item):
    if 'grammar' in item and 'points' in item['grammar']:
        for point in item['grammar']['points']:
            title = point['title']
            # Regex to find Korean characters inside what should be Japanese text (before the parenthesis)
            match = re.search(r'^([^\(]+)', title)
            if match:
                jap_part = match.group(1)
                if re.search(r'[\uac00-\ud7af]', jap_part):
                    print(f"Found Korean in title: {title}")
                    # Replace "부터" with "から"
                    if "부터" in jap_part:
                        new_jap_part = jap_part.replace("부터", "から")
                        point['title'] = title.replace(jap_part, new_jap_part)
                        print(f"Fixed: {point['title']}")

for item in data:
    check_grammar(item)

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
