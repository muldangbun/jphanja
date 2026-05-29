import requests
import json
import os
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')

VOICEVOX_URL = "http://localhost:50021"
JSON_FILE = "../../data/scenes/convenience_scenesv1.JSON"

def generate_voice(text, speaker_id, filename):
    params = {"text": text, "speaker": speaker_id}
    res = requests.post(f"{VOICEVOX_URL}/audio_query", params=params)
    if res.status_code != 200:
        print(f"Failed to create query for: {text}")
        return False
    query = res.json()

    res = requests.post(f"{VOICEVOX_URL}/synthesis", params={"speaker": speaker_id}, data=json.dumps(query))
    if res.status_code != 200:
        print(f"Failed to synthesize for: {text}")
        return False

    with open(filename, "wb") as f:
        f.write(res.content)
    return True

def main():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return

    for scenario in data["scenarios"]:
        if scenario["id"] == "con-01-friends":
            continue
            
        output_dir = f"../../audio/{scenario['id']}"
        os.makedirs(output_dir, exist_ok=True)
        print(f"--- Processing {scenario['id']} ---")
        
        for i, item in enumerate(scenario["dialogue"]):
            text = item.get("kana", item.get("kanji", ""))
            speaker = item.get("speaker", "")
            
            # 캐릭터별 목소리 선택
            # 점원: 8 (카스가베 츠무기 - 차분하고 친절한 여성 톤)
            # 손님: 10 (아오야마 류세이 - 일반 남성 톤)
            if speaker == "손님":
                speaker_id = 10
            elif speaker == "점원":
                speaker_id = 8
            else:
                speaker_id = 8 # Default
            
            filename = os.path.join(output_dir, f"{i}.mp3")
            if os.path.exists(filename):
                print(f"[{i+1}] Skipping (already exists): {filename}")
                continue
                
            print(f"[{i+1}] Synthesizing ({speaker}): {text[:20]}...")
            success = generate_voice(text, speaker_id, filename)
            if success:
                time.sleep(0.2)
            else:
                print(f"Error on {text}")

if __name__ == "__main__":
    main()
