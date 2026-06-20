import os
import json
import wave
import io
import time
import requests
import lameenc

# Configuration
VOICEVOX_URL = 'http://127.0.0.1:50021'
SPEAKER_ID = 2  # 시코쿠 메탄 (노멀)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
JSON_FILE = os.path.join(BASE_DIR, 'data', 'n3', 'n3_vocab.json')
AUDIO_DIR = os.path.join(BASE_DIR, 'n3_vocab', 'public', 'audio', 'n3_vocab')

os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio(text, speaker, output_path):
    try:
        # 1. Query creation
        res = requests.post(
            f"{VOICEVOX_URL}/audio_query",
            params={'text': text, 'speaker': speaker},
            timeout=10
        )
        res.raise_for_status()
        query = res.json()
        
        # 2. Synthesis
        res_syn = requests.post(
            f"{VOICEVOX_URL}/synthesis",
            params={'speaker': speaker},
            json=query,
            timeout=30
        )
        res_syn.raise_for_status()
        wav_data = res_syn.content
        
        # 3. Convert WAV to MP3 using lameenc
        with wave.open(io.BytesIO(wav_data), 'rb') as wf:
            n_channels = wf.getnchannels()
            sample_width = wf.getsampwidth()
            framerate = wf.getframerate()
            n_frames = wf.getnframes()
            pcm_data = wf.readframes(n_frames)
            
            encoder = lameenc.Encoder()
            encoder.set_bit_rate(64)
            encoder.set_in_sample_rate(framerate)
            encoder.set_channels(n_channels)
            encoder.set_quality(2) # 2 = high quality
            
            mp3_data = encoder.encode(pcm_data)
            mp3_data += encoder.flush()
            
            with open(output_path, 'wb') as f:
                f.write(mp3_data)
        
        return True
    except Exception as e:
        print(f"Error generating audio for '{text}': {e}")
        return False

def main():
    if not os.path.exists(JSON_FILE):
        print(f"JSON file not found: {JSON_FILE}")
        return
        
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    total = len(data)
    print(f"Starting audio generation for {total} N3 vocabularies...")
    
    success_count = 0
    for idx, item in enumerate(data):
        reading = item.get('reading', '')
        if not reading:
            reading = item.get('word', '')
            
        output_filename = os.path.join(AUDIO_DIR, f"{idx}.mp3")
        
        # Skip if already exists
        if os.path.exists(output_filename):
            print(f"[{idx+1}/{total}] Skipping {reading} (already exists)")
            success_count += 1
            continue
            
        print(f"[{idx+1}/{total}] Generating audio for: {reading}")
        if generate_audio(reading, SPEAKER_ID, output_filename):
            success_count += 1
        
        # Small delay to not overwhelm the engine
        time.sleep(0.1)

    print(f"\nCompleted! Generated {success_count}/{total} audio files.")

if __name__ == '__main__':
    main()
