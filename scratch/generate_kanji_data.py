import urllib.request
import json
import os
import time
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# 1. Kana to Romaji Map
KANA_MAP = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    '나': 'na', 'ni': 'ni', 'ぬ': 'nu', 'ne': 'ne', '의': 'no', # Note: 'の' maps to 'no'
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'di', 'づ': 'du', '데': 'de', 'ど': 'do', # 'で' maps to 'de'
    'ba': 'ba', 'bi': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n',
    'ガ': 'ga', 'ギ': 'gi', 'グ': 'gu', 'ゲ': 'ge', 'ゴ': 'go',
    'ザ': 'za', 'ジ': 'ji', 'ズ': 'zu', 'ゼ': 'ze', 'ゾ': 'zo',
    '다': 'da', 'ヂ': 'di', 'ヅ': 'du', 'デ': 'de', 'ド': 'do',
    'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
    'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po'
}

# Add missing mapping characters if any
KANA_MAP['の'] = 'no'
KANA_MAP['で'] = 'de'
KANA_MAP['に'] = 'ni'
KANA_MAP['ね'] = 'ne'

COMB_MAP = {
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'nie': 'nie', 'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'びゃ': 'bya', '비ゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
    'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
    'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
    'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
    'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
    'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
    'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
    'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',
    'ビャ': 'bya', 'ビュ': 'byu', '비ョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

def kana_to_romaji(text):
    text = text.replace('.', '')
    res = ""
    i = 0
    while i < len(text):
        if text[i] in ['っ', 'ッ']:
            if i + 1 < len(text):
                next_romaji = ""
                if i + 2 < len(text) and text[i+1:i+3] in COMB_MAP:
                    next_romaji = COMB_MAP[text[i+1:i+3]]
                    i += 3
                elif text[i+1] in KANA_MAP:
                    next_romaji = KANA_MAP[text[i+1]]
                    i += 2
                else:
                    next_romaji = text[i+1]
                    i += 2
                if next_romaji:
                    res += next_romaji[0] + next_romaji
            else:
                res += 'tsu'
                i += 1
            continue

        if i + 1 < len(text) and text[i:i+2] in COMB_MAP:
            res += COMB_MAP[text[i:i+2]]
            i += 2
            continue
            
        if text[i] in KANA_MAP:
            res += KANA_MAP[text[i]]
            i += 1
            continue
            
        res += text[i]
        i += 1
        
    cleaned_res = []
    for char in res:
        if char == 'ー':
            if cleaned_res:
                prev = cleaned_res[-1]
                if prev in 'aeiou':
                    cleaned_res.append(prev)
                else:
                    cleaned_res.append('o')
            else:
                cleaned_res.append('o')
        else:
            cleaned_res.append(char)
            
    return "".join(cleaned_res)

# 2. Ollama API Request helper
def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "gemma4:26b",
        "prompt": prompt,
        "stream": False
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode('utf-8'), headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=600) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get('response', '').strip()
    except Exception as e:
        print(f"Error querying Ollama: {e}")
        return ""

# 3. Fetch Hanja Dictionary from GitHub
def download_hanja_dict():
    print("Downloading hanja.txt from GitHub...")
    url = "https://raw.githubusercontent.com/myungcheol/hanja/master/hanja.txt"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
            
        hanja_map = {}
        for line in content.splitlines():
            if '=' in line:
                parts = line.split('=', 1)
                char = parts[0].strip()
                val_part = parts[1].split(',', 1)[0].strip()
                words = val_part.split()
                if len(words) >= 2:
                    sound = words[-1]
                    meaning = " ".join(words[:-1])
                    hanja_map[char] = (meaning, sound)
                elif len(words) == 1:
                    hanja_map[char] = ("", words[0])
        print(f"Successfully loaded {len(hanja_map)} Hanja mapping entries.")
        return hanja_map
    except Exception as e:
        print(f"Error loading Hanja dict: {e}")
        return {}

# 4. Fetch Kanji List from kanjiapi.dev
def get_kanji_list(grade):
    print(f"Fetching Grade {grade} kanji list from kanjiapi.dev...")
    url = f"https://kanjiapi.dev/v1/kanji/grade-{grade}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetching kanji list: {e}")
        return []

# 5. Fetch single Kanji details from kanjiapi.dev
def fetch_kanji_details(kanji):
    url = f"https://kanjiapi.dev/v1/kanji/{urllib.parse.quote(kanji)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            strokes = data.get('stroke_count', 0)
            meanings = data.get('meanings', [])
            readings_on = data.get('on_readings', [])
            readings_kun = data.get('kun_readings', [])
            
            romaji_on = [kana_to_romaji(r) for r in readings_on]
            romaji_kun = [kana_to_romaji(r) for r in readings_kun]
            
            return {
                "strokes": strokes,
                "meanings": meanings,
                "readings_on": readings_on,
                "romaji_on": romaji_on,
                "readings_kun": readings_kun,
                "romaji_kun": romaji_kun
            }
    except Exception as e:
        print(f"Error fetching details for {kanji}: {e}")
        return None

# 6. Parser for compact format
def parse_compact_response(response_text):
    result_map = {}
    for line in response_text.strip().split('\n'):
        line = line.strip()
        if not line or ':' not in line:
            continue
        try:
            kanji, rest = line.split(':', 1)
            kanji = kanji.strip()
            # Clean prefixes like "한자: " or similar
            kanji = kanji.replace("한자", "").replace(" ", "").strip()
            if len(kanji) > 1:
                kanji = kanji[-1]
            
            ex_parts = rest.split(';')
            examples = []
            for ex in ex_parts:
                ex = ex.strip()
                if not ex:
                    continue
                parts = ex.split(':')
                if len(parts) == 3:
                    word, meaning, romaji = parts
                    examples.append({
                        "word": word.strip(),
                        "meaning": meaning.strip(),
                        "romaji": romaji.strip()
                    })
            if len(examples) >= 2:
                result_map[kanji] = examples[:2]
        except Exception as e:
            print(f"Error parsing line '{line}': {e}")
    return result_map

# 7. Query Ollama for examples in batches of 5 (using compact format)
def get_examples_for_batch(kanji_batch, hanja_map):
    kanji_list_str = "\n".join(kanji_batch)
    prompt = f"""다음 {len(kanji_batch)}개의 한자에 대해 각각 대표적인 일본어 예시 단어 2개씩을 생성해줘.
출력은 어떠한 설명, 빈줄, 마크다운 코드블럭(```) 없이 오직 아래 형식의 행들로만 출력해줘:
한자:단어1(히라가나):뜻1:로마자1;단어2(히라가나):뜻2:로마자2

대상 한자:
{kanji_list_str}"""
    
    # Try batch generation once
    response_text = ask_ollama(prompt)
    if response_text:
        batch_map = parse_compact_response(response_text)
        # Check if all kanjis in the batch were successfully parsed
        success = True
        for k in kanji_batch:
            if k not in batch_map:
                success = False
                break
        if success:
            return batch_map
            
    # If batch fails or is incomplete, fallback to single query for each missing kanji
    print(f"Batch query failed or incomplete. Falling back to single queries for: {kanji_batch}")
    result_map = {}
    for k in kanji_batch:
        single_prompt = f"""다음 한자에 대해 예시 단어 2개를 "단어(히라가나):뜻:로마자;단어(히라가나):뜻:로마자" 형식으로만 출력해줘.
설명이나 마크다운 코드블럭(```)을 절대 포함하지 마.

{k}:"""
        # Retry up to 2 times for single kanji
        for attempt in range(2):
            res_text = ask_ollama(single_prompt)
            if res_text:
                full_line = f"{k}:{res_text.strip()}"
                single_map = parse_compact_response(full_line)
                if k in single_map:
                    result_map[k] = single_map[k]
                    break
            time.sleep(1)
        if k not in result_map:
            print(f"Failed to generate examples for kanji: {k}")
            
    return result_map

# 8. Fallback to get single kanji info from Ollama
def get_fallback_kor_meaning_sound(kanji):
    prompt = f"한자 '{kanji}'의 한국식 뜻(훈)과 음을 다음 JSON 형식으로만 알려줘. 다른 텍스트는 금지: {{\"meaning\": \"뜻\", \"sound\": \"음\"}}"
    response_text = ask_ollama(prompt)
    try:
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            data = json.loads(json_match.group(0))
            return data.get("meaning", ""), data.get("sound", "")
    except Exception as e:
        print(f"Fallback Hanja lookup failed: {e}")
    return "", ""

# 9. Main process function
def generate_grade_data(grade, hanja_map):
    output_path = f"d:/ag_coding_ex/jphanja/kanji_grade{grade}.json"
    
    # 1. Fetch kanji list
    kanji_list = get_kanji_list(grade)
    if not kanji_list:
        print(f"Error: Empty kanji list for Grade {grade}")
        return
        
    print(f"Grade {grade} has {len(kanji_list)} kanji characters.")
    
    # 2. Check existing progress
    processed_data = []
    processed_kanji = set()
    if os.path.exists(output_path):
        try:
            with open(output_path, "r", encoding="utf-8") as f:
                processed_data = json.load(f)
            processed_kanji = {item["kanji"] for item in processed_data}
            print(f"Loaded existing file. Already processed {len(processed_kanji)} kanji.")
        except Exception as e:
            print(f"Error loading existing JSON, starting fresh: {e}")
            
    remaining_kanji = [k for k in kanji_list if k not in processed_kanji]
    print(f"Remaining kanji to process: {len(remaining_kanji)}")
    
    if not remaining_kanji:
        print(f"Grade {grade} is already fully completed!")
        return
        
    # 3. Process in batches of 3
    batch_size = 3
    for start_idx in range(0, len(remaining_kanji), batch_size):
        batch = remaining_kanji[start_idx:start_idx + batch_size]
        print(f"Processing batch {start_idx // batch_size + 1}: {batch}", flush=True)
        
        # A. Fetch examples from Ollama
        examples_map = get_examples_for_batch(batch, hanja_map)
        
        # B. Assemble details for each kanji
        for k in batch:
            details = fetch_kanji_details(k)
            if not details:
                # Retry once
                time.sleep(2)
                details = fetch_kanji_details(k)
                
            if not details:
                print(f"Skipping {k} due to API fetch errors.")
                continue
                
            # Get Korean meaning and sound
            h_mean, h_sound = hanja_map.get(k, ("", ""))
            if not h_mean or not h_sound:
                # Query fallback
                h_mean_fallback, h_sound_fallback = get_fallback_kor_meaning_sound(k)
                h_mean = h_mean or h_mean_fallback
                h_sound = h_sound or h_sound_fallback
                
            # Get examples from our map, or create empty list
            examples = examples_map.get(k, [])
            if not examples:
                print(f"Warning: No examples generated for {k}")
                
            # Build final kanji object matching Grade 4 format
            kanji_obj = {
                "kanji": k,
                "grade": grade,
                "strokes": details["strokes"],
                "meanings": details["meanings"],
                "kor_meaning": h_mean,
                "kor_sound": h_sound,
                "readings_on": details["readings_on"],
                "romaji_on": details["romaji_on"],
                "readings_kun": details["readings_kun"],
                "romaji_kun": details["romaji_kun"],
                "examples": examples
            }
            
            processed_data.append(kanji_obj)
            
        # C. Save progress after each batch
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
        print(f"Saved batch progress. Total completed: {len(processed_data)} / {len(kanji_list)}", flush=True)
        
        # Short cooldown to prevent overloading Ollama
        time.sleep(1)

if __name__ == "__main__":
    hanja_map = download_hanja_dict()
    
    # Process Grade 5
    print("\n================= STARTING GRADE 5 =================\n", flush=True)
    generate_grade_data(5, hanja_map)
    
    # Process Grade 6
    print("\n================= STARTING GRADE 6 =================\n", flush=True)
    generate_grade_data(6, hanja_map)
    
    print("\nALL TASKS COMPLETED SUCCESSFULLY!", flush=True)
