import sys
import re

sys.path.append('d:/ag_coding_ex/jphanja/scratch')
from generate_direct_data import VOCAB_DB

# regex for Japanese text in the word part (before the parenthesized reading)
# The word part should only contain Kanji, Hiragana, Katakana, and maybe middle dots or tildes, but NO English/Hangul letters.
# Allowed: Han, Hiragana, Katakana, and standard punctuation.
# Let's check for any characters that are NOT in:
# CJK Unified Ideographs: \u4e00-\u9fff
# Hiragana: \u3040-\u309f
# Katakana: \u30a0-\u30ff
# Kanji/Kana punctuation: \u3000-\u303f, \uff00-\uffef
# And allow parentheses for readings.
# Let's just find anything in the word part (before '(') that matches [a-zA-Z] or Hangul.

hangul_re = re.compile(r'[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318f]')
english_re = re.compile(r'[a-zA-Z]')

for k, val in VOCAB_DB.items():
    ex_parts = val.split(';')
    if len(ex_parts) != 2:
        print(f"Kanji '{k}': Has {len(ex_parts)} examples instead of 2! Value: '{val}'")
    
    for ex in ex_parts:
        parts = ex.split('|')
        if len(parts) == 3:
            word, meaning, romaji = parts
            
            # Extract the kanji word part (before the parenthesis)
            if '(' in word:
                word_jp = word.split('(')[0]
                reading_jp = word.split('(')[1].split(')')[0]
            else:
                word_jp = word
                reading_jp = ""
                print(f"Kanji '{k}': Word '{word}' has no reading in parenthesis!")
                
            # Check Japanese word part for Hangul or English
            if hangul_re.search(word_jp):
                print(f"Kanji '{k}': Hangul found in Japanese word '{word_jp}'!")
            if english_re.search(word_jp):
                print(f"Kanji '{k}': English found in Japanese word '{word_jp}'!")
                
            # Check Japanese reading part for Hangul or English
            if hangul_re.search(reading_jp):
                print(f"Kanji '{k}': Hangul found in Japanese reading '{reading_jp}'!")
            if english_re.search(reading_jp):
                print(f"Kanji '{k}': English found in Japanese reading '{reading_jp}'!")
        else:
            print(f"Kanji '{k}': Invalid format for example '{ex}'")
