import requests
import json
import os
import time

# 설정
VOICEVOX_URL = "http://localhost:50021"
JSON_FILE = "../../data/stories/kaninotokoya.JSON"
OUTPUT_DIR = "audio/story"
SPEAKER_ID = 3  # 3: 즈다몬 (Zundamon), 2: 시코쿠 메탄 (Shikoku Metan) 등 원하는 ID로 변경 가능

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
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: {JSON_FILE} not found!")
        return

    for i, item in enumerate(data):
        # 'kana' 필드가 있으면 가나를, 없으면 'kanji' 필드를 사용합니다.
        # VOICEVOX는 가나(히라가나/가타카나) 입력 시 발음이 가장 정확합니다.
        text = item.get("kana", item.get("kanji", ""))
        if not text:
            continue

        filename = os.path.join(OUTPUT_DIR, f"{i}.mp3")
        
        if os.path.exists(filename):
            print(f"[{i+1}/{len(data)}] Skipping {filename} (already exists)")
            continue
            
        print(f"[{i+1}/{len(data)}] Processing: {text[:20]}...")
        success = generate_voice(text, filename)
        
        if success:
            # 서버 부하 방지를 위해 아주 잠깐 대기
            time.sleep(0.2)
        else:
            print(f"Error occurred at index {i}. Stopping.")
            break

    print("\nAll done! Check the 'audio/story' folder.")

if __name__ == "__main__":
    main()
