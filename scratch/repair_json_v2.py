import json
import re

path = 'd:/ag_coding_ex/jphanja/kaninotokoya.JSON'

# 원본 데이터 구조 (유실된 9번 데이터 포함)
replacement_id_9 = {
    "id": 9,
    "kanji": "「とこやですが、ごようはありませんか。」",
    "kana": "「とこ야이지만, 고요은 없습니까?」",
    "romaji": "tokoya desu ga goyou wa arimasenn ka",
    "meaning": "“이발사입니다만, 볼일(깎을 머리)은 없으신가요?”",
    "grammar": {
        "points": [
            {
                "title": "とこや이지만 (명사 + 이지만)",
                "desc": [
                    "と코야: 이발소 / 이발사",
                    "이지만: ~입니다만 (자신을 소개하거나 용건을 꺼내기 전 서두를 뗄 때 사용)"
                ]
            },
            {
                "title": "ごよう은 없습니까? (미화어 + 명사 + 부정 의문형)",
                "desc": [
                    "고요(御用): 볼일, 용건 (명사 앞에 '고'를 붙여 정중하게 표현)",
                    "없습니까?: 없습니까? / 없으신가요?"
                ]
            }
        ],
        "summary": "자신이 이발사임을 밝히며 영업(머리를 깎을 것인지)을 시도하는 게의 정중한 질문입니다."
    }
}

def clean_japanese(text):
    text = text.replace('는', 'は').replace('에는', '에는').replace('가', '가').replace('를', '를').replace('이갔습니다', 'いきました')
    text = text.replace(', ', '、').replace('. ', '。').replace('.', '。').replace(',', '、')
    return text

try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # JSON이 깨졌으므로, 9번 문장 주변을 텍스트 기반으로 복구
    # id 8번의 끝과 id 10번의 시작 사이를 replacement_id_9로 교체
    
    # 8번의 끝 찾기
    match_8 = re.search(r'\"id\": 8,.*?}\n\s+},', content, re.DOTALL)
    # 10번의 시작 찾기
    match_10 = re.search(r'{\n\s+\"id\": 10,', content, re.DOTALL)
    
    if match_8 and match_10:
        new_content = content[:match_8.end()] + "\n    " + json.dumps(replacement_id_9, indent=4, ensure_ascii=False) + ",\n    " + content[match_10.start():]
        
        # 다시 로드 시도
        data = json.loads(new_content)
        
        # 전체 데이터 정제
        for item in data:
            item['kanji'] = clean_japanese(item['kanji'])
            item['kana'] = clean_japanese(item['kana'])
            
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print("Successfully repaired and cleaned JSON via script.")
    else:
        print("Could not find anchor points in JSON text.")

except Exception as e:
    print(f"Error during script repair: {e}")
