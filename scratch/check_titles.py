import re
import json

KOREAN_REGEX = re.compile(r'[\uac00-\ud7af]')

def check_grammar_titles(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for i, line in enumerate(lines):
        if '"title":' in line:
            # Extract the string value
            match = re.search(r'"title":\s*"(.*?)"', line)
            if match:
                title_val = match.group(1)
                # Check part before '('
                parts = title_val.split('(')
                japanese_part = parts[0]
                if KOREAN_REGEX.search(japanese_part):
                    print(f"Line {i+1}: {line.strip()}")

check_grammar_titles('kaninotokoya.JSON')
