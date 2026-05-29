import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

with open('d:/ag_coding_ex/jphanja/scratch/g5_list.txt', encoding='utf-8') as f:
    text = f.read()
chars = text.split(',')
for idx, c in enumerate(chars):
    print(f"Index {idx}: {c} (hex={[hex(ord(x)) for x in c]})")
