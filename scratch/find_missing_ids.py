import re

with open('d:/ag_coding_ex/jphanja/kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    content = f.read()

ids = re.findall(r'\"id\":\s*(\d+)', content)
ids = [int(i) for i in ids]
print(f"Found IDs: {ids}")

missing = [i for i in range(1, 39) if i not in ids]
print(f"Missing IDs: {missing}")
