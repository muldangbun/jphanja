import re
import json

def check_mixed_grammar(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    corrections = []
    
    # Common Korean particles that might have leaked into Japanese text
    particles = ['부터', '까지', '은', '는', '이', '가', '을', '를', '도', '의']
    
    def scan(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                new_path = f"{path}.{k}" if path else k
                if k == 'title' and isinstance(v, str):
                    # Check text before '('
                    jp_part = v.split('(')[0]
                    for p in particles:
                        # Search for particle not surrounded by Korean characters
                        # (to avoid matching normal Korean words in the title explanation)
                        # Actually, title explanation is usually in parentheses.
                        # So we check if the Japanese part contains Korean characters at all.
                        if re.search(r'[\uac00-\ud7af]', jp_part):
                            print(f"MIXED in {new_path}: {v}")
                            break
                elif k == 'desc' and isinstance(v, list):
                    # Desc is usually all Korean, so that's fine.
                    pass
                scan(v, new_path)
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                scan(item, f"{path}[{i}]")

    scan(data)

check_mixed_grammar('kaninotokoya.JSON')
