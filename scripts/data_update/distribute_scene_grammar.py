import json
import re
import os
import glob

def clean_title(title):
    t = re.sub(r'\(.*?\)', '', title).strip()
    t = t.replace('～', '').replace('~', '').strip()
    # Remove common dictionary form endings to match conjugations
    t = re.sub(r'(する|ます|いる|ある|れる|られる|せる|させる|ない|だ|です|て|た|な|に|の|を|が|は|へ|も|や|と|で)$', '', t)
    t = re.sub(r'[いるむぶつうくぐす]$', '', t)
    return [p.strip() for p in t.split('/') if p.strip()]

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for scenario in data.get('scenarios', []):
        grammar = scenario.get('grammar', {})
        points = grammar.get('points', [])
        
        # Initialize empty grammar for each dialogue
        for d in scenario['dialogue']:
            d['grammar'] = {'points': [], 'summary': d['meaning']}
        
        for pt in points:
            title = pt['title']
            keywords = clean_title(title)
            
            # Find which dialogue line contains any of the keywords
            matched = False
            for d in scenario['dialogue']:
                text_to_search = d['kanji'] + d['kana']
                if any(kw in text_to_search for kw in keywords if kw):
                    d['grammar']['points'].append(pt)
                    matched = True
                    break # Only attach to the first appearance
            
            if not matched and scenario['dialogue']:
                # If no match, attach to the first line as fallback
                scenario['dialogue'][0]['grammar']['points'].append(pt)
                
        # Remove scenario-level grammar
        if 'grammar' in scenario:
            del scenario['grammar']

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print(f"Finished {filepath}")

def main():
    scene_files = glob.glob('data/scenes/*_scenesv1.JSON')
    if not scene_files:
        print("No scene files found.")
        return
        
    for filepath in scene_files:
        process_file(filepath)

if __name__ == '__main__':
    main()
