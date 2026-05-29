import re

js_path = r"d:\ag_coding_ex\jphanja\radical\dist\assets\index-DRI4bMSa.js"

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

# Let's search for the pattern of coreRadicalsData.
# It starts with "人" and "사람 인".
# Let's search for "사람 인" and find its position, then print the surrounding area.
pos = content.find("사람 인")
if pos != -1:
    print(f"Found '사람 인' at position {pos}")
    # Print 2000 characters before and 10000 characters after
    start = max(0, pos - 500)
    end = min(len(content), pos + 10000)
    snippet = content[start:end]
    
    # Save the snippet to a text file in scratch
    out_path = r"d:\ag_coding_ex\jphanja\scratch\radicals_snippet.txt"
    with open(out_path, "w", encoding="utf-8") as out_f:
        out_f.write(snippet)
    print("Saved snippet to scratch/radicals_snippet.txt")
else:
    print("'사람 인' not found in JS bundle.")
