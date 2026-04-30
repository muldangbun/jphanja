import json
import re

# 원본 데이터를 읽어와서 특정 구간을 수정하고 다시 쓰는 안전한 방식
path = 'd:/ag_coding_ex/jphanja/kaninotokoya.JSON'

# 1. 텍스트 정제 함수
def clean_japanese(text):
    # 한국어 조사 및 불필요한 공백/부호 수정
    text = text.replace('는', 'は').replace('에는', 'には').replace('가', 'が').replace('를', 'を').replace('이갔습니다', 'いきました')
    text = text.replace(', ', '、').replace('. ', '。').replace('.', '。').replace(',', '、')
    return text

try:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 만약 JSON이 깨져서 로드가 안 된다면, 정규식을 사용하여 구조를 어느 정도 복구 시도
    # 여기서는 수동으로 문제가 된 9번~15번 구간을 집중 수정
    
    data = json.loads(content)
    
    # 데이터 수정
    for item in data:
        if item['id'] == 14:
            item['kanji'] = "蟹는, そこで, 山へやっていきました."
            item['kana'] = "か에는, そこで, やまへやっていきました."
        if item['id'] == 15:
            item['kanji'] = "山에는 たぬき가 ひる네를 していました."
            item['kana'] = "やまには たぬきが ひるねを していました。"
        
        # 전체적으로 한국어 잔재 청소
        item['kanji'] = clean_japanese(item['kanji'])
        item['kana'] = clean_japanese(item['kana'])

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("Successfully cleaned and repaired JSON.")

except Exception as e:
    print(f"Error during repair: {e}")
