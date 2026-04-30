import json

path = 'd:/ag_coding_ex/jphanja/kaninotokoya.JSON'

# Correct data for the broken IDs
correct_data = {
    9: {
        "id": 9,
        "kanji": "「と코야데스가, 고요와 아리마센카?」",
        "kana": "「と코야데스가, 고요와 아리마센카?」",
        "romaji": "tokoya desu ga goyou wa arimasenn ka",
        "meaning": "“이발사입니다만, 볼일(깎을 머리)은 없으신가요?”",
        "grammar": {
            "points": [
                {
                    "title": "とこや입니다만 (명사 + 입니다만)",
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
    },
    13: {
        "id": 13,
        "kanji": "いくら蟹がじょうずなとこや에서도, 毛없는 頭를 かる것은 できません.",
        "kana": "いくらかにがじょうずなとこやでも, けのないあたまをかることはできません.",
        "romaji": "ikura kani ga jouzu na tokoya demo ke no nai atama o karu koto wa dekimasenn",
        "meaning": "아무리 게가 솜씨 좋은 이발사라도, 털이 없는 머리를 깎을 수는 없습니다.",
        "grammar": {
            "points": [
                {
                    "title": "いくら ~でも (부사 + 조사)",
                    "desc": [
                        "아무리 ~라도",
                        "조건이나 상황에 관계없이 결과가 변하지 않음을 강조할 때 사용합니다."
                    ]
                },
                {
                    "title": "かることは できません (동사 기본형 + こと + 부정 가능형)",
                    "desc": [
                        "かる(刈る): (머리나 풀 등을) 깎다",
                        "~ことは できません: ~할 수는 없습니다 (능력이나 가능성의 부정)"
                    ]
                }
            ],
            "summary": "솜씨가 아무리 좋아도 깎을 대상(털)이 없으면 이발할 수 없다는 논리적인 상황을 설명합니다."
        }
    },
    14: {
        "id": 14,
        "kanji": "蟹는, そこで, 山へやって이갔습니다.",
        "kana": "か에는, そこで, やまへやって이갔습니다.",
        "romaji": "kani wa sokode yama e yatte ikimashita",
        "meaning": "게는 그래서 산으로 갔습니다.",
        "grammar": {
            "points": [
                {
                    "title": "山(やま)へ (명사 + 조사)",
                    "desc": [
                        "へ: ~로 (이동의 방향을 나타내는 조사. '에'로 바꿀 수 있음)"
                    ]
                },
                {
                    "title": "やっていきました (복합 동사 과거형)",
                    "desc": [
                        "やっていく: (어떤 장소로) 가다, 찾아가다",
                        "바다에서 산으로 장소를 이동하는 동작을 나타냅니다."
                    ]
                }
            ],
            "summary": "바다에서는 손님을 찾지 못해 산으로 장소를 옮겨 새로운 기회를 찾아가는 장면입니다."
        }
    },
    15: {
        "id": 15,
        "kanji": "山에는 たぬき가 ひる네를 していました。",
        "kana": "やま에는 たぬ기카 히루네오 시테 이마시타。",
        "romaji": "yama ni wa tanuki ga hirune o shite imashita",
        "meaning": "산에는 너구리가 낮잠을 자고 있었습니다.",
        "grammar": {
            "points": [
                {
                    "title": "たぬき (명사)",
                    "desc": [
                        "너구리 (일본 설화에서 자주 장난꾸러기로 등장하는 동물)"
                    ]
                }
            ],
            "summary": "산에 도착한 게가 이번에는 낮잠을 자고 있는 너구리를 발견했음을 나타냅니다. 구조는 바닷가의 문어 장면과 유사합니다."
        }
    }
}

def clean_japanese(text):
    text = text.replace('는', 'は').replace('에는', 'には').replace('가', 'が').replace('를', 'を').replace('이갔습니다', 'いきました')
    text = text.replace(', ', '、').replace('. ', '。').replace('.', '。').replace(',', '、')
    return text

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Parse as much as possible to get a list of dicts
# Since it's broken, we use regex to extract valid objects and fix them
objects = []
import re
raw_objs = re.split(r'}\n\s*},', content) # This is risky but let's try a better regex

# Better: find all { "id": ... } and manually parse
starts = [m.start() for m in re.finditer(r'\{\s*\"id\":', content)]
for i, start in enumerate(starts):
    end = starts[i+1] if i+1 < len(starts) else content.rfind('}') + 1
    # Find the last closing brace for this object
    obj_content = content[start:end].strip()
    if i < len(starts) - 1:
        obj_content = obj_content.rstrip(',')
        # Fix: ensure it ends with }
        if not obj_content.endswith('}'):
            obj_content += '}'
    
    try:
        obj = json.loads(obj_content)
        if obj['id'] in correct_data:
            obj = correct_data[obj['id']]
        objects.append(obj)
    except:
        # If it failed to load, check if it's one we know how to fix
        id_match = re.search(r'\"id\":\s*(\d+)', obj_content)
        if id_match:
            id_val = int(id_match.group(1))
            if id_val in correct_data:
                objects.append(correct_data[id_val])
            else:
                print(f"Failed to load and no replacement for ID {id_val}")

# Final clean up and write
for obj in objects:
    obj['kanji'] = clean_japanese(obj['kanji'])
    obj['kana'] = clean_japanese(obj['kana'])

with open(path, 'w', encoding='utf-8') as f:
    json.dump(objects, f, indent=4, ensure_ascii=False)
print("Successfully repaired JSON.")
