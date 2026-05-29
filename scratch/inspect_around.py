js_path = r"d:\ag_coding_ex\jphanja\radical\dist\assets\index-DRI4bMSa.js"

with open(js_path, "r", encoding="utf-8") as f:
    content = f.read()

pos = content.find("사람 인")
if pos != -1:
    print(f"Index: {pos}")
    snippet = content[pos-400:pos+600]
    safe_str = snippet.encode('ascii', 'backslashreplace').decode('ascii')
    print("--- snippet ---")
    print(safe_str)
else:
    print("Not found")
