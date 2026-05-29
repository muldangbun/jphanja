import requests
import json
import os
import time

# 설정
VOICEVOX_URL = "http://localhost:50021"
JSON_FILE = "../../data/stories/dendenmushikanashi.JSON"
OUTPUT_DIR = "audio/dendenmushikanashi"
SPEAKER_ID = 85  # 青山龍星 (Aoyama Ryusei) 6th style (かなしみ / Sadness)

# 폴더 생성
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
    print(f"Created directory: {OUTPUT_DIR}")

def generate_voice(text, filename):
    # 1. 오디오 쿼리 생성
    params = {"text": text, "speaker": SPEAKER_ID}
    res = requests.post(f"{VOICEVOX_URL}/audio_query", params=params)
    if res.status_code != 200:
        print(f"Failed to create query for: {text}")
        return False
    query = res.json()

    # 2. 음성 합성
    res = requests.post(
        f"{VOICEVOX_URL}/synthesis",
        params={"speaker": SPEAKER_ID},
        data=json.dumps(query)
    )
    
    if res.status_code != 200:
        print(f"Failed to synthesize for: {text}")
        return False

    with open(filename, "wb") as f:
        f.write(res.content)
    print(f"Successfully saved: {filename}")
    return True

def main():
    print(f"Starting audio generation using VOICEVOX at {VOICEVOX_URL}...")
    print(f"Speaker: Aoyama Ryusei 6th style (ID: {SPEAKER_ID})")
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_FILE} not found!")
        return

    print(f"Total sentences to generate: {len(data)}")

    for i, item in enumerate(data):
        # 'kana' 필드가 있으면 가나를, 없으면 'kanji' 필드를 사용합니다.
        text = item.get("kana", item.get("kanji", ""))
        if not text:
            continue

        filename = os.path.join(OUTPUT_DIR, f"{i}.mp3")
        
        if os.path.exists(filename):
            print(f"[{i+1}/{len(data)}] Skipping {filename} (already exists)")
            continue
            
        print(f"[{i+1}/{len(data)}] Processing: {text[:30]}...")
        success = generate_voice(text, filename)
        
        if success:
            time.sleep(0.2)
        else:
            print(f"Error occurred at index {i}. Stopping.")
            break

    print(f"\nAll done! Check the '{OUTPUT_DIR}' folder.")

if __name__ == "__main__":
    main()
