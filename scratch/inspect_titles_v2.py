
import json
import re
import sys

# Ensure stdout is UTF-8
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

file_path = r'd:\ag_coding_ex\jphanja\kaninotokoya.JSON'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    with open(file_path, 'r', encoding='cp949') as f:
        data = json.load(f)

korean_particles = ["부터", "에서", "까지", "에게", "와", "과", "도", "만", "뿐"]

for item in data:
    if 'grammar' in item and 'points' in item['grammar']:
        for point in item['grammar']['points']:
            title = point['title']
            # split by parenthesis
            parts = title.split('(')
            jap_part = parts[0]
            
            found_issue = False
            for p in korean_particles:
                if p in jap_part:
                    print(f"Potential issue in title: {title}")
                    found_issue = True
                    break
            
            if not found_issue:
                # Check for any Korean character in jap_part
                if re.search(r'[\uac00-\ud7af]', jap_part):
                     print(f"Korean found in Japanese part: {title}")

