import re

js_path = r"d:\ag_coding_ex\jphanja\radical\dist\assets\index-DRI4bMSa.js"

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("fe=[{original:")
if pos == -1:
    pos = content.find("fe=[")
    
if pos != -1:
    print(f"Found 'fe=[' at {pos}")
    array_start = content.find("[", pos)
    
    depth = 0
    array_end = -1
    for i in range(array_start, len(content)):
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                array_end = i
                break
                
    if array_end != -1:
        extracted = content[array_start:array_end+1]
        print(f"Extracted length: {len(extracted)}")
        
        # Decode only \uXXXX escape sequences using regex
        decoded = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), extracted)
        
        with open(r"d:\ag_coding_ex\jphanja\scratch\extracted_fe.js", "w", encoding="utf-8") as out_f:
            out_f.write(decoded)
        print("Decoded cleanly and saved to scratch/extracted_fe.js")
    else:
        print("Closing bracket not found.")
else:
    print("'fe=[' not found.")
