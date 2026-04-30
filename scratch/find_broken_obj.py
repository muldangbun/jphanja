import json
import re

with open('d:/ag_coding_ex/jphanja/kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    content = f.read()

start_indices = [m.start() for m in re.finditer(r'\{\s*\"id\":', content)]

for i in range(len(start_indices)):
    start = start_indices[i]
    if i+1 < len(start_indices):
        end = start_indices[i+1]
        # Find the last } before the next {
        last_brace = content.rfind('}', start, end)
        end = last_brace + 1
    else:
        end = content.rfind('}') + 1
    
    obj_str = content[start:end].strip()
    try:
        json.loads(obj_str)
    except Exception as e:
        print(f"Object at index {i} is broken: {e}")
        print(f"Content:\n{obj_str}")
