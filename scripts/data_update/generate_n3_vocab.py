import os
import json
import re
import pdfplumber
import requests
from bs4 import BeautifulSoup
import urllib.parse
import sys
import codecs
import unicodedata

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Paths
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
REF_DIR = os.path.join(BASE_DIR, 'refdoc')
KANJI_DIR = os.path.join(BASE_DIR, 'data', 'kanji')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'n3')

PDF_FILES = [
    {"file": "JLPT N3 필수 동사 정리.pdf", "type": "verb"},
    {"file": "JLPT N3 필수 명사 정리.pdf", "type": "noun"},
    {"file": "JLPT N3 핵심 명사 정리 (い형용사).pdf", "type": "i-adj"},
    {"file": "JLPT N3 핵심 명사 정리 (な형용사).pdf", "type": "na-adj"}
]

def load_existing_kanji():
    kanji_dict = {}
    for i in range(1, 7):
        file_path = os.path.join(KANJI_DIR, f'kanji_grade{i}.json')
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    k = item.get('kanji')
                    if k:
                        kanji_dict[k] = {
                            "kor_meaning": item.get('kor_meaning', ''),
                            "kor_sound": item.get('kor_sound', '')
                        }
    return kanji_dict

FALLBACK_KANJI = {
    '壊': ('무너질', '괴'), '誘': ('꾈', '유'), '戻': ('어그러질', '려'), '命': ('목숨', '명'), 
    '柔': ('부드러울', '유'), '怒': ('성낼', '노'), '込': ('담을', '곡'), '超': ('뛰어넘을', '초'), 
    '濃': ('짙을', '농'), '薄': ('엷을', '박'), '粋': ('순수할', '수'), '沸': ('끓을', '비'), 
    '裕': ('넉넉할', '유'), '倒': ('넘어질', '도'), '紹': ('이을', '소'), '渡': ('건널', '도'), 
    '違': ('어긋날', '위'), '丁': ('고무래', '정'), '介': ('끼일', '개'), '褒': ('기릴', '포'), 
    '鈍': ('둔할', '둔'), '遅': ('늦을', '지'), '硬': ('굳을', '경'), '環': ('고리', '환'), 
    '眩': ('아찔할', '현'), '翻': ('날릴', '번'), '駄': ('짐실을', '타'), '諦': ('체념할', '체'), 
    '狭': ('좁을', '협'), '絡': ('이을', '락'), '剣': ('칼', '검'), '鮮': ('고울', '선'), 
    '面': ('얼굴', '면'), '頃': ('잠깐', '경'), '詳': ('자세할', '상'), '逃': ('도망할', '도'), 
    '偉': ('훌륭할', '위'), '慮': ('생각할', '려'), '恥': ('부끄러울', '치'), '尋': ('찾을', '심'), 
    '較': ('견줄', '교'), '譲': ('사양할', '양'), '寂': ('고요할', '적'), '羨': ('부러워할', '선'), 
    '頼': ('의지할', '뢰'), '販': ('팔', '판'), '恐': ('두려울', '공'), '寧': ('편안할', '녕'), 
    '騒': ('떠들', '소'), '屈': ('굽힐', '굴'), '璧': ('구슬', '벽'), '悔': ('뉘우칠', '회'), 
    '普': ('넓을', '보'), '突': ('갑자기', '돌'), '鋭': ('날카로울', '예'), '臭': ('냄새', '취'), 
    '汚': ('더러울', '오'), '発': ('필', '발'), '齢': ('나이', '령'), '懸': ('달', '현'), '贈': ('줄', '증')
}

def crawl_hanja(kanji):
    """
    네이버 사전(또는 대체 사전) 크롤링하여 한자의 뜻/음 추출
    웹 크롤링이 실패하는 경우가 많아 하드코딩된 폴백 사전 사용
    """
    if kanji in FALLBACK_KANJI:
        return {"kor_meaning": FALLBACK_KANJI[kanji][0], "kor_sound": FALLBACK_KANJI[kanji][1]}
    
    url = f"https://dic.daum.net/search.do?q={urllib.parse.quote(kanji)}&dic=hanja"
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 1순위: sub_read 클래스
            sub_read = soup.find('a', class_='sub_read')
            if sub_read:
                text = sub_read.text.strip().split(',')[0].strip() # "보낼 증, 줄 증" -> "보낼 증"
                parts = text.split()
                if len(parts) >= 2:
                    return {"kor_meaning": " ".join(parts[:-1]), "kor_sound": parts[-1]}
                else:
                    return {"kor_meaning": text, "kor_sound": text[-1] if text else ""}
            
            # 2순위: 기존 클래스
            clean_word = soup.find('a', class_='txt_cleansch')
            if clean_word:
                meaning_span = clean_word.find_next_sibling('span', class_='txt_search')
                if meaning_span:
                    text = meaning_span.text.strip()
                    parts = text.split()
                    if len(parts) >= 2:
                        return {"kor_meaning": " ".join(parts[:-1]), "kor_sound": parts[-1]}
                    else:
                        return {"kor_meaning": text, "kor_sound": text[-1] if text else ""}
    except Exception as e:
        print(f"Error crawling {kanji}: {e}")
    
    return {"kor_meaning": "", "kor_sound": ""}

def is_kanji(char):
    return re.match(r'[一-龥]', char)

def extract_vocab_from_pdfs():
    kanji_db = load_existing_kanji()
    all_vocab = []

    for pdf_info in PDF_FILES:
        pdf_path = os.path.join(REF_DIR, pdf_info['file'])
        if not os.path.exists(pdf_path):
            print(f"File not found: {pdf_path}")
            continue
        
        print(f"Processing {pdf_info['file']} ...")
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        if not row or not row[0] or row[0].strip() == '' or row[0].strip() == '#':
                            continue
                        # Remove newlines in cells
                        row = [str(cell).replace('\n', '') if cell else '' for cell in row]
                        
                        # Columns based on type
                        word = ""
                        reading = ""
                        meaning = ""
                        if pdf_info['type'] == 'verb':
                            # 번호, 동사, 히라가나, 그룹, 한국어 뜻
                            if len(row) >= 5:
                                word = row[1].strip()
                                reading = row[2].strip()
                                meaning = row[4].strip()
                        else:
                            # 번호, 명사/형용사, 히라가나, 한국어 뜻
                            if len(row) >= 4:
                                word = row[1].strip()
                                reading = row[2].strip()
                                meaning = row[3].strip()

                        if not word or word == '동사 (일본어)' or word.startswith('명사'):
                            continue

                        if '/' in word:
                            word = word.split('/')[0]

                        # Normalize Kangxi radicals and compatibility chars to standard CJK ideographs
                        word = unicodedata.normalize('NFKC', word)

                        kanji_breakdown = []
                        for char in word:
                            if is_kanji(char):
                                k_info = kanji_db.get(char)
                                if not k_info:
                                    print(f"Kanji {char} not in grades 1-6. Crawling...")
                                    k_info = crawl_hanja(char)
                                    kanji_db[char] = k_info # Cache it
                                
                                kanji_breakdown.append({
                                    "kanji": char,
                                    "kor_meaning": k_info.get("kor_meaning", ""),
                                    "kor_sound": k_info.get("kor_sound", "")
                                })
                        
                        all_vocab.append({
                            "word": word,
                            "reading": reading,
                            "meaning": meaning,
                            "type": pdf_info['type'],
                            "kanji_breakdown": kanji_breakdown
                        })

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    out_file = os.path.join(OUTPUT_DIR, 'n3_vocab.json')
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(all_vocab, f, ensure_ascii=False, indent=2)
    print(f"Generated {out_file} with {len(all_vocab)} words.")

if __name__ == '__main__':
    extract_vocab_from_pdfs()
