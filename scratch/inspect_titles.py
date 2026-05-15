
import json
import re

file_path = r'd:\ag_coding_ex\jphanja\kaninotokoya.JSON'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
except Exception as e:
    with open(file_path, 'r', encoding='cp949') as f:
        data = json.load(f)

for item in data:
    if 'grammar' in item and 'points' in item['grammar']:
        for point in item['grammar']['points']:
            print(point['title'])
