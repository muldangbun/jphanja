import re

file_path = r"d:\ag_coding_ex\jphanja\radical\src\data\radicalsData.js"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if 'original: "示"' in line:
        start_idx = i
    if 'original: "瓦"' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    print(f"Found '示' at index {start_idx} and '瓦' at index {end_idx}")
    
    # Complete list of replacement lines matching original data format
    replacement_lines = [
        '  { original: "示", variant: "礻", name: "보일 시", meaning: "신앙, 제사, 길흉화복", category: "tool", reading_on: "ジ, シ", reading_kun: "しめす" },\n',
        '  { original: "宀", variant: "宀", name: "갓머리 면", meaning: "집, 덮개, 머무는 처소", category: "tool", reading_on: "ベン, メン", reading_kun: "" },\n',
        '  { original: "广", variant: "广", name: "엄호 엄", meaning: "경사진 지붕, 창고, 넓은 건물", category: "tool", reading_on: "ゲン", reading_kun: "" },\n',
        '  { original: "弓", variant: "弓", name: "활 궁", meaning: "무기, 당기다, 구부러지다", category: "tool", reading_on: "キュ우", reading_kun: "유미" },\n', # wait, let's use the exact extracted values
        '  { original: "弓", variant: "弓", name: "활 궁", meaning: "무기, 당기다, 구부러지다", category: "tool", reading_on: "キュウ", reading_kun: "ゆみ" },\n',
        '  { original: "車", variant: "車", name: "수레 거", meaning: "탈것, 운송 수단, 기계", category: "tool", reading_on: "シャ", reading_kun: "くる마" },\n', # wait, let's use the exact extracted values
        '  { original: "車", variant: "車", name: "수레 거", meaning: "탈것, 운송 수단, 기계", category: "tool", reading_on: "シャ", reading_kun: "くるま" },\n',
        '  { original: "戈", variant: "戈", name: "창 과", meaning: "무기, 군사적 행동, 지키다", category: "tool", reading_on: "カ", reading_kun: "ほこ" },\n',
        '  { original: "斤", variant: "斤", name: "도끼 근", meaning: "도구, 베다, 무게의 단위", category: "tool", reading_on: "キン", reading_kun: "" },\n',
        '  { original: "彳", variant: "彳", name: "자축거릴 척", meaning: "조금씩 걷다, 행동", category: "tool", reading_on: "テキ", reading_kun: "" },\n',
        '  { original: "言", variant: "言", name: "말씀 언", meaning: "언어, 대화, 평가와 기록", category: "tool", reading_on: "ゲん, ゴン", reading_kun: "いう, こと" },\n', # wait, let's use the exact extracted values
        '  { original: "言", variant: "言", name: "말씀 언", meaning: "언어, 대화, 평가와 기록", category: "tool", reading_on: "ゲン, ゴン", reading_kun: "いう, こと" },\n',
        '  { original: "衣", variant: "衣", name: "옷 의", meaning: "의복, 싸개, 꾸밈", category: "tool", reading_on: "イ", reading_kun: "ころも" },\n',
        '  { original: "食", variant: "飠", name: "밥 식", meaning: "음식물, 먹는 행위, 양식", category: "tool", reading_on: "ショク, ジキ", reading_kun: "たべる, くう" },\n',
        '  { original: "走", variant: "走", name: "달릴 주", meaning: "빨리 가다, 도망치다", category: "tool", reading_on: "ソウ", reading_kun: "하siru" },\n', # wait, let's use the exact extracted values
        '  { original: "走", variant: "走", name: "달릴 주", meaning: "빨리 가다, 도망치다", category: "tool", reading_on: "ソウ", reading_kun: "はしる" },\n',
        '  { original: "里", variant: "里", name: "마을 리", meaning: "구역, 토지 단위, 고향", category: "tool", reading_on: "リ", reading_kun: "さと" },\n',
        '  { original: "革", variant: "革", name: "가죽 혁", meaning: "피혁, 단련, 신발과 가죽벨트", category: "tool", reading_on: "カク", reading_kun: "かわ" },\n',
        '  { original: "行", variant: "行", name: "갈 행", meaning: "도로, 행동하다, 단체", category: "tool", reading_on: "コウ, ギョウ", reading_kun: "いく, おこなう" },\n',
        '  { original: "瓦", variant: "瓦", name: "기와 와", meaning: "도자기, 점토로 구운 그릇", category: "tool", reading_on: "ガ", reading_kun: "かわら" }\n'
    ]
    
    # Wait, the list above has duplicate lines for 弓, 車, 言, 走 because of copy paste!
    # Let's write the clean list without duplicate lines.
    clean_replacement_lines = [
        '  { original: "示", variant: "礻", name: "보일 시", meaning: "신앙, 제사, 길흉화복", category: "tool", reading_on: "ジ, シ", reading_kun: "しめす" },\n',
        '  { original: "宀", variant: "宀", name: "갓머리 면", meaning: "집, 덮개, 머무는 처소", category: "tool", reading_on: "ベン, メン", reading_kun: "" },\n',
        '  { original: "广", variant: "广", name: "엄호 엄", meaning: "경사진 지붕, 창고, 넓은 건물", category: "tool", reading_on: "ゲン", reading_kun: "" },\n',
        '  { original: "弓", variant: "弓", name: "활 궁", meaning: "무기, 당기다, 구부러지다", category: "tool", reading_on: "キュ우", reading_kun: "유미" },\n', # wait, let's use the exact values from extracted_fe.js
    ]
    
    # Wait! Let's just look at the exact values in extracted_fe.js.
    # In extracted_fe.js:
    # 弓: reading_on: 'キュウ', reading_kun: '유미' -> wait, the file has reading_kun: '유미'? No, let's look at the power shell output again:
    # {original:`弓`,variant:`弓`,name:`활 궁`,meaning:`무기, 당기다, 구부러지다`,category:`tool`,reading_on:`キュウ`,reading_kun:`유미`}
    # Ah!!! Yes, it has "유미" and "호코", etc.! Why?
    # Oh! Maybe the original developer did translate some of them to Korean strings in the JS file or the compiled output has them like that.
    # Let's follow the EXACT compiled JS bundle values! E.g. "유미", "호코", "하시루", "이쿠, 오고나우" etc.
    # Wait, why did the compiled bundle have:
    # 弓: reading_kun: `유미`
    # 戈: reading_kun: `호코`
    # 衣: reading_kun: `ころ도`
    # 走: reading_kun: `하시루`
    # 行: reading_kun: `이쿠, 오고나우`
    # Wait! These are:
    # 유미 = yumi (ゆみ)
    # 호코 = hoko (ほこ)
    # 코로모 -> 코로도 = korodo (Wait, in Japanese, 衣's kunyomi is ころも, which in Korean pronunciation is 코로모. But here it says "ころ도"? No, it has `ころ도`. Wait, is it a typo from the original developer or `ころも`?)
    # Let's check `ころ도` vs `ころも` in the PowerShell output.
    # In the PowerShell output, it printed:
    # `reading_kun: \`ころも\`` (Yes, `ころ도` in Korean but in Japanese it is `ころも`!).
    # Wait, let's look at the raw UTF-8 decoded text:
    # `{original: '衣', variant: '衣', name: '옷 의', meaning: '의복, 싸개, 꾸밈', category: 'tool', reading_on: 'イ', reading_kun: 'ころも'}`
    # Wait! Let's check if it printed `ころ도` or `ころも`.
    # Let's check:
    # `é ©`,variant:`é ©`,name:`ê°€ì£½ í˜ `,meaning:`í”¼í˜ , ë‹¨ë ¨, ì‹ ë°œê³¼ ê°€ì£½ë²¨íŠ¸`,category:`tool`,reading_on:`ã‚«ã‚¯`,reading_kun:`ã ‹ã‚ `
    # And before that:
    # `è¡Œ`,variant:`è¡Œ`,name:`ê°ˆ í–‰`,meaning:`ë  ë¡œ, í–‰ë  í•˜ë‹¤, ë‹¨ì²´`,category:`tool`,reading_on:`ã‚³ã‚¦, ã‚®ãƒ§ã‚¦`,reading_kun:`ã „ã  , ã Šã “ã ªã  `
    # In the cleanly decoded PowerShell output, we had:
    # `{original: "衣", variant: "衣", name: "옷 의", meaning: "의복, 싸개, 꾸밈", category: "tool", reading_on: "イ", reading_kun: "ころも"}`
    # Oh! It was `ころも`!
    # Wait, let's check `弓`:
    # `{original: "弓", variant: "弓", name: "활 궁", meaning: "무기, 당기다, 구부러지다", category: "tool", reading_on: "キュウ", reading_kun: "ゆみ"}`
    # Yes, it is `ゆみ`!
    # And `戈`:
    # `{original: "戈", variant: "戈", name: "창 과", meaning: "무기, 군사적 행동, 지키다", category: "tool", reading_on: "カ", reading_kun: "ほこ"}`
    # Yes, it is `ほこ`!
    # And `走`:
    # `{original: "走", variant: "走", name: "달릴 주", meaning: "빨리 가다, 도망치다", category: "tool", reading_on: "ソウ", reading_kun: "はしる"}`
    # Yes, it is `はしる`!
    # And `行`:
    # `{original: "行", variant: "行", name: "갈 행", meaning: "도로, 행동하다, 단체", category: "tool", reading_on: "コウ, ギョウ", reading_kun: "いく, おこなう"}`
    # Yes, it is `いく, おこなう`!

    # So all readings in `extracted_fe.js` are in HIRAGANA and KATAKANA!
    # Ah! The previous output of `Get-Content d:\ag_coding_ex\jphanja\scratch\extracted_fe.js` printed `이쿠, 오고나우` in the description, but let's check what was printed:
    # Wait, `Get-Content` on the first run printed:
    # `reading_kun: "이쿠, 오고나우"`
    # But that was because the console encoding page CP949 and python unicode escape decoding got messed up!
    # When we used the regex-based `decode_unicode_escapes`, the clean output was:
    # `reading_kun: "いく, おこなう"}`!
    # YES! The clean output has `いく, おこなう`!
    # Oh! The first script had encoding issues, but the second script (the clean regex-based one) decoded it perfectly to Hiragana and Katakana!
    # E.g.
    # `弓`: `reading_on: "キュウ"`, `reading_kun: "ゆみ"`
    # `車`: `reading_on: "シャ"`, `reading_kun: "くるま"`
    # `戈`: `reading_on: "カ"`, `reading_kun: "ほこ"`
    # `言`: `reading_on: "ゲン, ゴン"`, `reading_kun: "いう, こと"`
    # `衣`: `reading_on: "イ"`, `reading_kun: "ころ도"`? Wait! In the clean output:
    # `reading_kun: "ころも"`!
    # YES!
    # So the clean output has 100% correct Hiragana/Katakana!

    # Let's write the python script to read `scratch/extracted_fe.js` directly, parse it, and construct the correct Javascript array element string dynamically!
    # That is the most elegant, error-proof way!
    # E.g. we read the JSON-like array from `extracted_fe.js` and generate the JavaScript text!
    # Let's write a python script to do this.
