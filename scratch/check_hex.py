with open('d:/ag_coding_ex/jphanja/kaninotokoya.JSON', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(430, 465):
    line = lines[i].strip()
    if '"kanji":' in line or '"kana":' in line:
        print(f"Line {i+1}: {line}")
        for c in line:
            if ord(c) > 127:
                print(f"  {c}: {hex(ord(c))}")
