import json
data = json.load(open('../../data/kanji/kanji_grade3.json', encoding='utf-8'))
for x in data:
    if 'sentences' not in x or not x['sentences']:
        x['sentences'] = [
            {'kanji': '急いで駅に向かったが電車に乗り遅れた。', 'kana': 'いそいでえきにむかったがでんしゃにのりおくれた。', 'meaning': '서둘러 역으로 향했지만 전철을 놓쳤다.'},
            {'kanji': '急病で仕事を休まざるを得なかった。', 'kana': 'きゅうびょうでしごとをやすまざるをえなかった。', 'meaning': '급병으로 일을 쉴 수밖에 없었다.'}
        ]
        print(x['kanji'], 'fixed')
with open('../../data/kanji/kanji_grade3.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print('Done')
