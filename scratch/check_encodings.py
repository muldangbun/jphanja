import chardet

def check_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
    result = chardet.detect(raw_data)
    print(f"File: {file_path}")
    print(f"Detected: {result}")
    
    # Try common Korean/Japanese encodings
    encodings = ['utf-8', 'cp949', 'euc-kr', 'shift_jis', 'cp932', 'euc-jp']
    for enc in encodings:
        try:
            raw_data.decode(enc)
            print(f"Decodable as {enc}: YES")
        except:
            print(f"Decodable as {enc}: NO")

check_encoding('kaninotokoya.JSON')
check_encoding('kanji_grade1.json')
check_encoding('kanji_grade2.json')
check_encoding('kanji_grade3.json')
