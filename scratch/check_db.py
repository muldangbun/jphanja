import sys
import re

sys.path.append('d:/ag_coding_ex/jphanja/scratch')
from generate_direct_data import VOCAB_DB

hangul_re = re.compile(r'[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318f]')

for k, val in VOCAB_DB.items():
    ex_parts = val.split(';')
    # Check count
    if len(ex_parts) != 2:
        print(f"Kanji '{k}': Has {len(ex_parts)} examples instead of 2! Value: '{val}'")
    
    for ex in ex_parts:
        parts = ex.split('|')
        if len(parts) == 3:
            word, meaning, romaji = parts
            # Check for hangul in Japanese word
            # Note: the Japanese word is the part before the parentheses, and the reading inside.
            # But we can just check the whole 'word' string for Hangul characters.
            match = hangul_re.search(word)
            if match:
                print(f"Kanji '{k}': Hangul found in Japanese word '{word}'!")
        else:
            print(f"Kanji '{k}': Invalid format for example '{ex}'")
