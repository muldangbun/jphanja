import urllib.request
import json
import time
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "gemma4:26b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 150,
            "temperature": 0.2
        }
    }
    req = urllib.request.Request(
        url, 
        data=json.dumps(data).encode('utf-8'), 
        headers={'Content-Type': 'application/json'}
    )
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            print(f"Time taken: {time.time() - t0:.2f}s", flush=True)
            return res_data.get('response', '')
    except Exception as e:
        print(f"Error querying Ollama: {e}", flush=True)
        return ""

prompt = """다음 한자에 대해 예시 단어 2개를 "단어(히라가나):뜻:로마자;단어(히라가나):뜻:로마자" 형식으로만 출력해줘.
설명이나 마크다운 코드블럭(```)을 절대 포함하지 마.

圧:"""

res = ask_ollama(prompt)
print("Response representation:", repr(res), flush=True)
