import urllib.request
import json

def fetch_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return json.loads(response.read().decode('utf-8'))

g5 = fetch_url('https://kanjiapi.dev/v1/kanji/grade-5')
g6 = fetch_url('https://kanjiapi.dev/v1/kanji/grade-6')

print("G5 count:", len(g5))
print("G6 count:", len(g6))

with open('d:/ag_coding_ex/jphanja/scratch/g5_list.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(g5))

with open('d:/ag_coding_ex/jphanja/scratch/g6_list.txt', 'w', encoding='utf-8') as f:
    f.write(','.join(g6))
