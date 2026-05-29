import re

js_path = r"d:\ag_coding_ex\jphanja\radical\dist\assets\index-DRI4bMSa.js"

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for "사람 인". We know it is inside the coreRadicalsData array.
# Let's find the start of that array.
# The array begins with [{original:"人" or similar.
# Let's find "사람 인" and trace backwards to the start of the array `[`
pos = content.find("사람 인")
if pos != -1:
    # Trace backwards to find the opening bracket of the array
    # Let's look for `original` key
    start_pos = pos
    bracket_count = 0
    # Let's search backwards for the start of the list
    # The list is likely preceded by an equals or a variable assignment like `const fe=[` or similar
    # We can just look for the first '[' before '사람 인' that corresponds to the array start.
    # Let's search backwards for 'original:"人"' or 'original:`人`'
    # Actually, let's look for the word "human" or the first element
    first_elem_pos = content.rfind("human", 0, pos)
    if first_elem_pos != -1:
        array_start = content.rfind("[", 0, first_elem_pos)
        print(f"Array start found at {array_start}")
        
        # Now find the closing ']' matching the opening '['
        # Since it's an array of objects, we can count brackets or look for the end pattern
        # The end pattern has "瓦", "기와 와", "category:"tool"... followed by "]" and maybe a variable declaration
        # Let's trace forward from array_start counting brackets
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
            full_array = content[array_start:array_end+1]
            print(f"Extracted array length: {len(full_array)}")
            with open(r"d:\ag_coding_ex\jphanja\scratch\extracted_array.txt", "w", encoding="utf-8") as out_f:
                out_f.write(full_array)
            print("Saved full array to scratch/extracted_array.txt")
        else:
            print("Could not find matching closing bracket")
    else:
        print("Could not find 'human' before '사람 인'")
else:
    print("'사람 인' not found")
