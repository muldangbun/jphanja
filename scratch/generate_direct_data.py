import json
import urllib.request
import urllib.parse
import time
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

# Kana to Romaji Map
KANA_MAP = {
    'あ': 'a', 'い': 'i', 'う': 'u', 'え': 'e', 'お': 'o',
    'か': 'ka', 'き': 'ki', 'く': 'ku', 'け': 'ke', 'こ': 'ko',
    'さ': 'sa', 'し': 'shi', 'す': 'su', 'せ': 'se', 'そ': 'so',
    'た': 'ta', 'ち': 'chi', 'つ': 'tsu', 'て': 'te', 'と': 'to',
    'な': 'na', 'に': 'ni', 'ぬ': 'nu', 'ね': 'ne', 'の': 'no',
    'は': 'ha', 'ひ': 'hi', 'ふ': 'fu', 'へ': 'he', 'ほ': 'ho',
    'ま': 'ma', 'み': 'mi', 'む': 'mu', 'め': 'me', 'も': 'mo',
    'や': 'ya', 'ゆ': 'yu', 'よ': 'yo',
    'ら': 'ra', 'り': 'ri', 'る': 'ru', 'れ': 're', 'ろ': 'ro',
    'わ': 'wa', 'を': 'wo', 'ん': 'n',
    'が': 'ga', 'ぎ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ざ': 'za', 'じ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'だ': 'da', 'ぢ': 'di', 'づ': 'du', 'で': 'de', 'ど': 'do',
    'ば': 'ba', 'び': 'bi', 'ぶ': 'bu', 'べ': 'be', 'ぼ': 'bo',
    'ぱ': 'pa', 'ぴ': 'pi', 'ぷ': 'pu', 'ぺ': 'pe', 'ぽ': 'po',
    'ア': 'a', 'イ': 'i', 'ウ': 'u', 'エ': 'e', 'オ': 'o',
    'カ': 'ka', 'キ': 'ki', 'ク': 'ku', 'ケ': 'ke', 'コ': 'ko',
    'サ': 'sa', 'シ': 'shi', 'ス': 'su', 'セ': 'se', 'ソ': 'so',
    'タ': 'ta', 'チ': 'chi', 'ツ': 'tsu', 'テ': 'te', 'ト': 'to',
    'ナ': 'na', 'ニ': 'ni', 'ヌ': 'nu', 'ネ': 'ne', 'ノ': 'no',
    'ハ': 'ha', 'ヒ': 'hi', 'フ': 'fu', 'ヘ': 'he', 'ホ': 'ho',
    'マ': 'ma', 'ミ': 'mi', 'ム': 'mu', 'メ': 'me', 'モ': 'mo',
    'ヤ': 'ya', 'ユ': 'yu', 'ヨ': 'yo',
    'ラ': 'ra', 'リ': 'ri', 'ル': 'ru', 'レ': 're', 'ロ': 'ro',
    'ワ': 'wa', 'ヲ': 'wo', 'ン': 'n',
    'ガ': 'ga', 'ギ': 'gi', 'ぐ': 'gu', 'げ': 'ge', 'ご': 'go',
    'ザ': 'za', 'ジ': 'ji', 'ず': 'zu', 'ぜ': 'ze', 'ぞ': 'zo',
    'ダ': 'da', 'ヂ': 'di', 'ヅ': 'du', 'デ': 'de', 'ド': 'do',
    'バ': 'ba', 'ビ': 'bi', 'ブ': 'bu', 'ベ': 'be', 'ボ': 'bo',
    'パ': 'pa', 'ピ': 'pi', 'プ': 'pu', 'ペ': 'pe', 'ポ': 'po'
}

COMB_MAP = {
    'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
    'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
    'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
    'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
    'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
    'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
    'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
    'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
    'じゃ': 'ja', 'じゅ': 'ju', 'じょ': 'jo',
    'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
    'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
    'キャ': 'kya', 'キュ': 'kyu', 'キョ': 'kyo',
    'シャ': 'sha', 'シュ': 'shu', 'ショ': 'sho',
    'チャ': 'cha', 'チュ': 'chu', 'チョ': 'cho',
    'ニャ': 'nya', 'ニュ': 'nyu', 'ニョ': 'nyo',
    'ヒャ': 'hya', 'ヒュ': 'hyu', 'ヒョ': 'hyo',
    'ミャ': 'mya', 'ミュ': 'myu', 'ミョ': 'myo',
    'リャ': 'rya', 'リュ': 'ryu', 'リョ': 'ryo',
    'ギャ': 'gya', 'ギュ': 'gyu', 'ギョ': 'gyo',
    'ジャ': 'ja', 'ジュ': 'ju', 'ジョ': 'jo',
    'ビャ': 'bya', 'ビュ': 'byu', 'ビョ': 'byo',
    'ピャ': 'pya', 'ピュ': 'pyu', 'ピョ': 'pyo'
}

def kana_to_romaji(text):
    text = text.replace('.', '')
    res = ""
    i = 0
    while i < len(text):
        if text[i] in ['っ', 'ッ']:
            if i + 1 < len(text):
                next_romaji = ""
                if i + 2 < len(text) and text[i+1:i+3] in COMB_MAP:
                    next_romaji = COMB_MAP[text[i+1:i+3]]
                    i += 3
                elif text[i+1] in KANA_MAP:
                    next_romaji = KANA_MAP[text[i+1]]
                    i += 2
                else:
                    next_romaji = text[i+1]
                    i += 2
                if next_romaji:
                    res += next_romaji[0] + next_romaji
            else:
                res += 'tsu'
                i += 1
            continue

        if i + 1 < len(text) and text[i:i+2] in COMB_MAP:
            res += COMB_MAP[text[i:i+2]]
            i += 2
            continue
            
        if text[i] in KANA_MAP:
            res += KANA_MAP[text[i]]
            i += 1
            continue
            
        res += text[i]
        i += 1
        
    cleaned_res = []
    for char in res:
        if char == 'ー':
            if cleaned_res:
                prev = cleaned_res[-1]
                if prev in 'aeiou':
                    cleaned_res.append(prev)
                else:
                    cleaned_res.append('o')
            else:
                cleaned_res.append('o')
        else:
            cleaned_res.append(char)
            
    return "".join(cleaned_res)

# Pre-compiled vocabulary database
VOCAB_DB = {
    # Grade 5
    "久": "永久(えいきゅう)|영구|eikyuu;久しぶり(ひさしぶり)|오랜만|hisashiburi",
    "仏": "仏教(ぶっきょう)|불교|bukkyou;大仏(だいぶつ)|대불|daibutsu",
    "仮": "仮定(かてい)|가정|katei;仮面(かめん)|가면|kamen",
    "件": "事件(じけん)|사건|jiken;条件(じょうけん)|조건|jouken",
    "任": "責任(せきにん)|책임|sekinin;担任(たんにん)|담임|tannin",
    "似": "類似(るいじ)|유사|ruiji;似顔絵(にがおえ)|초상화|nigaoe",
    "余": "余白(よはく)|여백|yohaku;余裕(よゆう)|여유|yoyuu",
    "価": "価格(かかく)|가격|kakaku;価値(かち)|가치|kachi",
    "保": "保存(ほぞん)|보존|hozon;保護(ほご)|보호|hogo",
    "修": "修理(しゅうり)|수리|shuuri;修行(しゅぎょう)|수행|shugyou",
    "俵": "土俵(どひょう)|씨름판|dohyou;米俵(こめだわら)|쌀가마니|komedawara",
    "個": "個人(こじん)|개인|kojin;個性(こせい)|개성|kosei",
    "備": "準備(じゅんび)|준비|junbi;設備(せつび)|설비|setsubi",
    "像": "映像(えいぞう)|영상|eizou;想像(そうぞう)|상상|souzou",
    "再": "再生(さいせい)|재생|saisei;再会(さいかい)|재회|saikai",
    "刊": "新刊(しんかん)|신간|shinkan;朝刊(ちょうかん)|조간|choukan",
    "判": "判断(はんだん)|판단|handan;審判(しんぱん)|심판|shinpan",
    "制": "制度(せいど)|제도|seido;制限(せいげん)|제한|seigen",
    "券": "乗車券(じょうしゃけん)|승차권|joushaken;旅券(りょけん)|여권|ryoken",
    "則": "規則(きそく)|규칙|kisoku;原則(げんそく)|원칙|gensoku",
    "効": "効果(こうか)|효과|kouka;有効(ゆうこう)|유효|yuukou",
    "務": "義務(ぎむ)|의무|gimu;公務員(こうむいん)|공무원|koumuin",
    "勢": "勢力(せいりょく)|세력|seiryoku;姿勢(しせい)|자세|shisei",
    "厚": "厚手(あつで)|두꺼움|atsude;濃厚(のうこう)|농후|noukou",
    "句": "俳句(はいく)|하이쿠|haiku;文句(もんく)|불평|monku",
    "可": "可能(かのう)|가능|kanou;許可(きょか)|허가|kyoka",
    "営": "営業(えいぎょう)|영업|eigyou;運営(うんえい)|운영|unei",
    "因": "原因(げんいん)|원인|genin;要因(よういん)|요인|youin",
    "団": "団体(だんたい)|단체|dantai;布団(ふとん)|이불|futon",
    "圧": "圧力(あつりょく)|압력|atsuryoku;圧迫(あっぱく)|압박|appaku",
    "在": "現在(げんざい)|현재|genzai;存在(そんざい)|존재|sonzai", # '현재' is '現在'
    "均": "平均(へいきん)|평균|heikin;均等(きんとう)|균등|kintou",
    "基": "基本(きほん)|기본|kihon;基準(きじゅん)|기준|kijun",
    "報": "報告(ほうこく)|보고|houkoku;情報(じょうほう)|정보|jouhou",
    "境": "国境(こっきょう)|국경|kokkyou;環境(かんきょう)|환경|kankyou",
    "墓": "墓地(ぼち)|묘지|bochi;お墓(おはか)|무덤|ohaka",
    "増": "増加(ぞうか)|증가|zouka;増大(ぞうだい)|증대|zoudai",
    "夢": "夢中(むちゅう)|열중|muchuu;悪夢(あくむ)|악몽|akumu",
    "妻": "妻(つま)|아내|tsuma;愛妻(あいさい)|애처|aisai",
    "婦": "婦人(ふじん)|부인|fujin;主婦(しゅふ)|주부|shufu",
    "容": "内容(ないよう)|내용|naiyou;容器(ようき)|용기|youki",
    "寄": "寄付(きふ)|기부|kifu;立ち寄る(たちよる)|들르다|tachiyoru",
    "富": "豊富(ほうふ)|풍부|houfu;富豪(ふごう)|부호|fugou",
    "導": "指導(しどう)|지도|shidou;導入(どうにゅう)|도입|dounyuu",
    "居": "居眠り(いねむり)|말뚝잠|inemuri;住居(じゅうきょ)|주거|juukyo",
    "属": "金属(きんぞく)|금속|kinzoku;所属(しょぞく)|소속|shozoku",
    "布": "毛布(もうふ)|담요|moufu;財布(さいふ)|지갑|saifu",
    "師": "教師(きょうし)|교사|kyoushi;医師(いし)|의사|ishi",
    "常": "日常(にちじょう)|일상|nichijou;非常(ひじょう)|비상|hijou",
    "幹": "新幹線(しんかんせん)|신칸센|shinkansen;幹部(かんぶ)|간부|kanbu",
    "序": "順序(じゅんじょ)|순서|junjo;秩序(ちつじょ)|질서|chitsujo",
    "弁": "弁当(べんとう)|도시락|bentou;弁護士(べんごし)|변호사|bengoshi",
    "張": "緊張(きんちょう)|긴장|kinchou;主張(しゅちょう)|주장|shuchou",
    "往": "往復(おうふく)|왕복|oufuku;往来(おうらい)|왕래|ourai",
    "復": "回復(かいふく)|회복|kaihuku;復習(ふくしゅう)|복습|fukushuu",
    "徳": "道徳(どうとく)|도덕|doutoku;美徳(びとく)|미덕|bitoku",
    "志": "意志(いし)|의지|ishi;志望(しぼう)|지망|shibou",
    "応": "反応(はんのう)|반응|hannou;応用(おうよう)|응용|ouyou",
    "快": "快適(かいてき)|쾌적|kaiteki;快感(かいかん)|쾌감|kaikan",
    "性": "性格(せいかく)|성격|seikaku;可能性(かのうせい)|가능성|kanousei",
    "恩": "恩恵(おんけい)|은혜|onkei;謝恩(しゃおん)|사은|shaon",
    "情": "感情(かんじょう)|감정|kanjou;情報(じょうほう)|정보|jouhou",
    "態": "状態(じょうたい)|상태|joutai;態度(たいど)|태도|taido",
    "慣": "習慣(しゅうかん)|습관|shuukan;慣れる(なれる)|익숙해지다|nareru",
    "承": "承諾(しょうだく)|승낙|shoudaku;了承(りょうしょう)|양해|ryoushou",
    "技": "技術(ぎじゅつ)|기술|gijutsu;特技(とくぎ)|특기|tokugi", # '기술' is '技術'
    "招": "招待(しょうたい)|초대|shoutai;招く(まねく)|초래하다|maneku",
    "授": "授業(じゅぎょう)|수업|jugyou;教授(きょうじゅ)|교수|kyouju",
    "採": "採用(さいよう)|채용|saiyou;採点(さいてん)|채점|saiten",
    "接": "接続(せつぞく)|접속|setsuzoku;直接(ちょくせつ)|직접|chokusetsu",
    "提": "提案(ていあん)|제안|teian;提供(ていきょう)|제공|teikyou",
    "損": "損失(そんしつ)|손실|sonshitsu;破損(はそん)|파손|hason",
    "支": "支持(しじ)|지지|shiji;支店(してん)|지점|shiten",
    "政": "政治(せいじ)|정치|seiji;政府(せいふ)|정부|seifu",
    "故": "事故(じこ)|사고|jiko;故障(こしょう)|고장|koshou",
    "敵": "敵対(てきたい)|적대|tekitai;強敵(きょうてき)|강적|kyouteki",
    "断": "判断(はんだん)|판단|handan;決断(けつだん)|결단|ketsudan",
    "旧": "旧正月(きゅうしょうがつ)|설날|kyuushougatsu;旧跡(きゅうせき)|유적|kyuuseki",
    "易": "容易(ようい)|용이|youi;貿易(ぼうえき)|무역|boueki",
    "暴": "暴力(ぼうりょく)|폭력|bouryoku;暴走(ぼうそう)|폭주|bousou",
    "条": "条件(じょうけん)|조건|jouken;条約(じょうやく)|조약|jouyaku",
    "枝": "小枝(こえだ)|잔가지|koeda;枝豆(えだまめ)|풋콩|edamame",
    "査": "調査(ちょうさ)|조사|chousa;検査(けんさ)|검사|kensa",
    "格": "性格(せいかく)|성격|seikaku;資格(しかく)|자격|shikaku",
    "桜": "桜の花(さくらのはな)|벚꽃|sakuranohana;桜前線(さくらぜんせん)|벚꽃개화전선|sakurazensen",
    "検": "検査(けんさ)|검사|kensa;検出(けんしゅつ)|검출|kenshutsu",
    "構": "構成(こうせい)|구성|kousei;構造(こうぞう)|구조|kouzou",
    "武": "武器(ぶき)|무기|buki;武道(ぶどう)|무도|budou",
    "比": "比較(ひかく)|비교|hikaku;比率(ひりつ)|비율|hiritsu",
    "永": "永久(えいきゅう)|영구|eikyuu;永遠(えいえん)|영원|eien",
    "河": "河川(かせん)|하천|kasen;運河(うんが)|운하|unga",
    "液": "液体(えきたい)|액체|ekitai;血液(けつえき)|혈액|ketsueki",
    "混": "混乱(こんらん)|혼란|konran;混雑(こんざつ)|혼잡|konzatsu",
    "減": "減少(げんしょう)|감소|genshou;軽減(けいげん)|경감|keigen",
    "測": "測定(そくてい)|측정|sokutei;予測(よそく)|예측|yosoku",
    "準": "準備(じゅんび)|준비|junbi;基準(きじゅん)|기준|kijun",
    "演": "演技(えんぎ)|연기|engi;講演(こうえん)|강연|kouen",
    "潔": "清潔(せいけつ)|청결|seiketsu;簡潔(かんけつ)|간결|kanketsu",
    "災": "災害(さいがい)|재해|saigai;火災(かさい)|화재|kasai",
    "燃": "燃料(ねんりょう)|연료|nenryou;燃焼(ねんしょう)|연소|nenshou",
    "版": "出版(しゅっぱん)|출판|shuppan;版画(はんが)|판화|hanga",
    "犯": "犯罪(はんざい)|범죄|hanzai;犯人(はんにん)|범인|hannin", # 'hanning' is 'hannin'
    "状": "状態(じょうたい)|상태|joutai;状況(じょうきょう)|상황|joukyou",
    "独": "独特(どくとく)|독특|dokutoku;独立(どくりつ)|독립|dokuritsu",
    "率": "比率(ひりつ)|비율|hiritsu;効率(こうりつ)|효율|kouritsu",
    "現": "現在(げんざい)|현재|genzai;表現(ひょうげん)|표현|hyougen",
    "留": "留学(りゅうがく)|유학|ryuugaku;留守(るす)|부재중|rusu",
    "略": "省略(しょうりゃく)|생략|shouryaku;戦略(せんりゃく)|전략|senryaku",
    "益": "利益(りえき)|이익|rieki;有益(ゆうえき)|유익|yuueki",
    "眼": "眼科(がんか)|안과|ganka;眼鏡(めがね)|안경|megane",
    "破": "破壊(はかい)|파괴|hakai;破片(はへん)|파편|hahen",
    "確": "確認(かくにん)|확인|kakunin;正確(せいかく)|정확|seikaku",
    "示": "指示(しじ)|지지|shiji;表示(ひょうじ)|표시|hyouji",
    "祖": "祖父(そふ)|할아버지|sofu;祖国(そこく)|조국|sokoku",
    "禁": "禁止(きんし)|금지|kinshi;禁煙(きんえん)|금연|kinen",
    "移": "移動(いどう)|이동|idou;移住(いじゅう)|이주|ijuu",
    "程": "程度(ていど)|정도|teido;日程(にってい)|일정|nittei",
    "税": "税金(ぜいきん)|세금|zeikin;消費税(しょうひぜい)|소비세|shouhizei",
    "築": "建築(けんちく)|건축|kenchiku;築く(きずく)|쌓다|kizuku",
    "精": "精神(せいしん)|정신|seishin;精密(せいみつ)|정밀|seimitsu",
    "素": "素材(そざい)|소재|sozai;素朴(そぼく)|소박|soboku",
    "経": "経済(けいざい)|경제|keizai;経験(けいけん)|경험|keiken",
    "統": "大統領(だいとうりょう)|대통령|daitouryou;統一(とういつ)|통일|touitsu",
    "絶": "絶対(ぜったい)|절대|zettai;絶望(ぜつぼう)|절망|zetsubou",
    "綿": "綿布(めんぷ)|면포|menpu;木綿(もめん)|무명|momen",
    "総": "総合(そうごう)|종합|sougou;総理(そうり)|총리|souri",
    "編": "編集(へんしゅう)|편집|henshuu;編み物(あみもの)|뜨개질|amimono",
    "績": "成績(せいせき)|성적|seiseki;実績(じっせき)|실적|jisseki",
    "織": "組織(そしき)|조직|soshiki;織物(おりもの)|직물|orimono",
    "罪": "犯罪(はんざい)|범죄|hanzai;有罪(ゆうざい)|유죄|yuuzai",
    "群": "群衆(ぐんしゅう)|군중|gunshuu;群れ(むれ)|무리|mure",
    "義": "義務(ぎむ)|의무|gimu;正義(せいぎ)|정의|seigi",
    "耕": "耕作(こうさく)|경작|kousaku;耕す(たがやす)|밭을 갈다|tagayasu",
    "職": "職業(しょくぎょう)|직업|shokugyou;職場(しょくば)|직장|shokuba",
    "肥": "肥満(ひまん)|비만|himan;肥料(ひりょう)|비료|hiryou",
    "能": "能力(のうりょく)|능력|nouryoku;機能(きのう)|기능|kinou",
    "興": "興味(きょうみ)|흥미|kyoumi;新興(しんこう)|신흥|shinkou",
    "舌": "毒舌(どくぜつ)|독설|dokuzetsu;舌先(したさき)|혀끝|shitasaki",
    "舎": "宿舎(しゅくしゃ)|숙소|shukusha;田舎(いなか)|시골|inaka",
    "術": "技術(ぎじゅつ)|기술|gijutsu;芸術(げいじゅつ)|예술|geijutsu",
    "衛": "衛生(えいせい)|위생|eisei;防衛(ぼうえい)|방위|bouei",
    "製": "製品(せいひん)|제품|seihin;製作(せいさく)|제작|seisaku",
    "複": "複雑(ふくざつ)|복잡|fukuzatsu;複数(ふくすう)|복수|fukusuu",
    "規": "規則(きそく)|규칙|kisoku;規模(きぼ)|규모|kibo",
    "解": "解決(かいけつ)|해결|kaiketsu;理解(りかい)|이해|rikai",
    "設": "設計(せっけい)|설계|sekkei;建設(けんせつ)|건설|kensetsu",
    "許": "許可(きょか)|허가|kyoka;許す(ゆるす)|허락하다|yurusu",
    "証": "証明(しょうめい)|증명|shoumei;証拠(しょうこ)|증거|shouko",
    "評": "評価(ひょうか)|평가|hyouka;評判(ひょうばん)|평판|hyouban",
    "講": "講義(こうぎ)|강의|kougi;講演(こうえん)|강연|kouen",
    "謝": "感謝(かんしゃ)|감사|kansha;謝罪(しゃざい)|사죄|shazai",
    "識": "知識(ちしき)|지식|chishiki;意識(いしき)|의식|ishiki",
    "護": "保護(ほご)|보호|hogo;看護(かんご)|간호|kango",
    "豊": "豊富(ほうふ)|풍부|houfu;豊作(ほうさく)|풍작|housaku",
    "財": "財布(さいふ)|지갑|saifu;財産(ざいさん)|재산|zaisan",
    "貧": "貧困(ひんこん)|빈곤|hinkon;貧しい(まずしい)|가난하다|mazushii",
    "責": "責任(せきにん)|책임|sekinin;責める(せめる)|비난하다|semeru",
    "貸": "貸出(かしだし)|대출|kashidashi;貸家(かしや)|셋집|kashiya",
    "貿": "貿易(ぼうえき)|무역|boueki;密貿易(みつぼうえき)|밀무역|mitsuboueki",
    "賀": "年賀状(ねんがじょう)|연하장|nengajou;賀詞(がし)|축하말|gashi",
    "資": "資料(しりょう)|자료|shiryou;資源(しげん)|자원|shigen",
    "賛": "賛成(さんせい)|찬성|sansei;賛美(さんび)|찬미|sanbi",
    "質": "質問(しつもん)|질문|shitsumon;品質(ひんしつ)|품질|hinshitsu",
    "輸": "輸入(ゆにゅう)|수입|yunyuu;輸出(ゆしゅつ)|수출|yushutsu",
    "述": "記述(きじゅつ)|기술|kijutsu;述べる(のべる)|진술하다|noberu",
    "迷": "迷子(まいご)|미아|maigo;迷惑(めいわく)|민폐|meiwaku",
    "退": "退職(たいしょく)|퇴직|taishoku;退学(たいがく)|퇴학|taigaku",
    "逆": "逆転(ぎゃくてん)|역전|gyakuten;逆風(ぎゃくふう)|역풍|gyakufuu",
    "造": "製造(せいぞう)|제조|seizou;木造(もくぞう)|목조|mokuzou",
    "過": "過去(かこ)|과거|kako;過半数(かはんすう)|과반수|kahansuu",
    "適": "適切(てきせつ)|적절|tekisetsu;適応(てきおう)|적응|tekiou",
    "酸": "酸素(さんそ)|산소|sanso;酸性(さんせい)|산성|sansei",
    "鉱": "鉱物(こうぶつ)|광물|koubutsu;炭鉱(たんこう)|탄광|tankou",
    "銅": "銅像(どうぞう)|동상|douzou;青銅(せいどう)|청동|seidou",
    "銭": "小銭(こぜに)|잔돈|kozeni;金銭(きんせん)|금전|kinsen",
    "防": "防止(ぼうし)|방지|boushi;予防(よぼう)|예방|yobou",
    "限": "制限(せいげん)|제한|seigen;限界(げんかい)|한계|genkai",
    "険": "危険(きけん)|위험|kiken;保険(ほけん)|보험|hoken",
    "際": "国際(こくさい)|국제|kokusai;交際(こうさい)|교제|kousai",
    "雑": "複雑(ふくざつ)|복잡|fukuzatsu;雑誌(ざっし)|잡지|zasshi",
    "非": "非常(ひじょう)|비상|hijou;非難(ひなん)|비난|hinan",
    "預": "預金(よきん)|예금|yokin;預ける(あずける)|맡기다|azukeru",
    "領": "領土(りょうど)|영토|ryoudo;大統領(だいとうりょう)|대통령|daitouryou",
    "額": "金額(きんがく)|금액|kingaku;額縁(がくぶち)|액자|gakubuchi",
    "飼": "飼育(しいく)|사육|shiiku;飼う(かう)|기르다|kau",

    # Grade 6
    "並": "並列(へいれつ)|병렬|heiretsu;並木(なみき)|가로수|namiki",
    "乱": "混乱(こんらん)|혼란|konran;乱暴(らんぼう)|난폭|ranbou",
    "乳": "牛乳(ぎゅうにゅう)|우유|gyuunyuu;乳児(にゅうじ)|영아|nyuuji",
    "亡": "死亡(しぼう)|사망|shibou;亡命(ぼうめい)|망명|boumei",
    "仁": "仁義(じんぎ)|의리|jingi;仁愛(じんあい)|자애|jinai",
    "供": "子供(こども)|아이|kodomo;提供(ていきょう)|제공|teikyou",
    "俳": "俳句(はいく)|하이쿠|haiku;俳優(はいゆう)|배우|haiyuu",
    "値": "価値(かち)|가치|kachi;値段(ねだん)|가격|nedan",
    "傷": "負傷(ふしょう)|부상|fushou;傷口(きずぐち)|상처자국|kizuguchi",
    "優": "優秀(ゆうしゅう)|우수|yuushuu;優しい(やさしい)|친절하다|yasashii",
    "党": "政党(せいとう)|정당|seitou;野党(やとう)|야당|yatou",
    "冊": "冊子(さっし)|책자|sasshi;別冊(べっさつ)|별책|bessatsu",
    "処": "処理(しょり)|처리|shori;処分(しょぶん)|처분|shobun",
    "刻": "時刻(じこく)|시각|jikoku;彫刻(ちょうこく)|조각|choukoku",
    "割": "割合(わりあい)|비율|wariai;割引(わりびき)|할인|waribiki",
    "創": "創造(そうぞう)|창조|souzou;創作(そうさく)|창작|sousaku",
    "劇": "演劇(えんげき)|연극|engeki;劇場(げきじょう)|극장|gekijou",
    "勤": "通勤(つうきん)|통근|tsuukin;勤務(きんむ)|근무|kinmu",
    "危": "危険(きけん)|위험|kiken;危機(きき)|위기|kiki",
    "卵": "卵白(らんぱく)|난백|ranpaku;卵黄(らんおう)|난황|ranou",
    "厳": "厳格(げんかく)|엄격|genkaku;厳しい(きびしい)|엄하다|kibishii",
    "収": "収集(しゅうしゅう)|수집|shuushuuu;収入(しゅうにゅう)|수입|shuunyuu",
    "后": "皇后(こうごう)|황후|kougou;午后(ごご)|오후|gogo",
    "否": "否定(ひてい)|부정|hitei;否認(ひにん)|부인|hinin",
    "吸": "呼吸(こきゅう)|호흡|kokyuu;吸収(きゅうしゅう)|흡수|kyuushuuu",
    "呼": "呼吸(こきゅう)|호흡|kokyuu;呼ぶ(よぶ)|부르다|yobu",
    "善": "改善(かいぜん)|개선|kaizen;善意(ぜんい)|선의|zenii",
    "困": "困難(こんなん)|곤란|konnan;困る(こまる)|곤란하다|komaru",
    "垂": "垂直(すいちょく)|수직|suichoku;垂れる(たれる)|처지다|tareru",
    "城": "城下町(じょうかまち)|성하지방|joukamachi;城壁(じょうへき)|성벽|jouheki",
    "域": "地域(ちいき)|지역|chiiki;区域(くいき)|구역|kuiki",
    "奏": "演奏(えんそう)|연주|ensou;奏者(そうしゃ)|연주자|sousha",
    "奮": "興奮(こうふん)|흥분|koufun;奮闘(ふんとう)|분투|funtou",
    "姿": "姿勢(しせい)|자세|shisei;姿態(したい)|자태|shitai",
    "存": "存在(そんざい)|존재|sonzai;保存(ほぞん)|보존|hozon",
    "孝": "親孝行(おやこうこう)|효도|oyakoukou;孝行(こうこう)|효행|koukou",
    "宅": "自宅(じたく)|자택|jitaku;住宅(じゅうたく)|주택|juutaku",
    "宇": "宇宙(うちゅう)|우주|uchuu;宇宙船(うちゅうせん)|우주선|uchuusen",
    "宗": "宗教(しゅうきょう)|종교|shuukyou;宗派(しゅうは)|종파|shuuha",
    "宙": "宇宙(うちゅう)|우주|uchuu;宙返り(ちゅうがえり)|공중제비|chuugaeri",
    "宝": "宝物(たからもの)|보물|takaramono;宝石(ほうせき)|보석|houseki",
    "宣": "宣言(せんげん)|선언|sengen;宣伝(せんでん)|선전|senden",
    "密": "秘密(ひみつ)|비밀|himitsu;精密(せいみつ)|정밀|seimitsu",
    "寸": "寸法(すんぽう)|치수|sunpou;一寸(いっすん)|한치|issun",
    "専": "専門(せんもん)|전문|senmon;専用(せんよう)|전용|senyou",
    "射": "放射(ほうしゃ)|방사|housha;注射(ちゅうしゃ)|주사|chuusha",
    "将": "将来(しょうらい)|장래|shourai;将軍(しょうぐん)|장군|shougun",
    "尊": "尊重(そんちょう)|존중|sonchou;尊敬(そんけい)|존경|sonkei",
    "就": "就職(しゅうしょく)|취업|shuushoku;就任(しゅうにん)|취임|shuunin",
    "尺": "尺度(しゃくど)|척도|shakudo;縮尺(しゅくしゃく)|축척|shukushaku",
    "届": "届出(とどけで)|신고|todokede;届く(とどく)|닿다|todoku",
    "展": "展示(てんじ)|전시|tenji;展覧会(てんらんかい)|전람회|tenrankai",
    "層": "階層(かいそう)|계층|kaisou;高層(こうそう)|고층|kousou",
    "己": "自己(じこ)|자기|jiko;利己的(りこてき)|이기적|rikoteki",
    "巻": "巻末(かんまつ)|책의끝|kanmatsu;巻く(まく)|감다|maku",
    "幕": "字幕(じまく)|자막|jimaku;開幕(かいまく)|개막|kaimaku",
    "干": "干渉(かんしょう)|간섭|kanshou;干す(ほす)|말리다|hosu",
    "幼": "幼児(ようじ)|유아|youji;幼稚(ようち)|유치|youchi",
    "庁": "官庁(かんちょう)|관청|kanchou;県庁(けんちょう)|현청|kenchou",
    "座": "座席(ざせき)|좌석|zaseki;星座(せいざ)|별자리|seiza",
    "延": "延長(えんちょう)|연장|enchou;延期(えんき)|연기|enki",
    "律": "法律(ほうりつ)|법률|houritsu;規律(きりつ)|규율|kiritsu",
    "従": "従事(じゅうじ)|종사|juuji;服従(ふくじゅう)|복종|fukujuu",
    "忘": "忘年会(ぼうねんかい)|망년회|bounenkai;忘れる(わすれる)|잊다|wasureru",
    "忠": "忠誠(ちゅうせい)|충성|chuusei;忠実(ちゅうじつ)|충실|chuujitsu",
    "憲": "憲法(けんぽう)|헌법|kenpou;違憲(いけん)|위헌|iken",
    "我": "自我(じが)|자아|jiga;我慢(がまん)|참음|gaman",
    "批": "批判(ひはん)|비판|hihan;批准(ひじゅん)|비준|hijun",
    "担": "担当(たんとう)|담당|tantou;担任(たんにん)|담임|tannin",
    "拝": "拝見(はいけん)|알현|haiken;拝む(おがむ)|빌다|ogamu",
    "拡": "拡大(かくだい)|확대|kakudai;拡張(かくちょう)|확장|kakuchou",
    "捨": "四捨五入(ししゃごにゅう)|사사오입|shishagonyuu;捨てる(すてる)|버리다|suteru",
    "探": "探検(たんけん)|탐험|tanken;探す(さがす)|찾다|sagasu",
    "推": "推薦(すいせん)|추천|suisen;推測(すいそく)|추측|suisoku",
    "揮": "発揮(はっき)|발휘|hakki;指揮(しき)|지휘|shiki",
    "操": "操作(そうさ)|조작|sousa;体操(たいそう)|체조|taisou",
    "敬": "敬意(けいい)|경의|keii;敬語(けいご)|경어|keigo",
    "映": "映画(えいが)|영화|eiga;上映(じょうえい)|상영|jouei",
    "晩": "晩餐(ばんさん)|만찬|bansan;今晩(こんばん)|오늘밤|konban",
    "暖": "温暖(おんだん)|온난|ondan;暖房(だんぼう)|난방|danbou",
    "暮": "日暮れ(ひぐれ)|황혼|higure;暮らす(くらす)|살아가다|kurasu",
    "朗": "朗読(ろうどく)|낭독|roudoku;明朗(めいろう)|명랑|meirou",
    "机": "学習机(がくしゅうづくえ)|책상|gakushuuzukue;机上(きじょう)|탁상|kijou",
    "枚": "枚数(まいすう)|매수|maisuu;大枚(たいまい)|거금|taimai",
    "染": "感染(かんせん)|감염|kansen;染める(そめる)|물들이다|someru",
    "株": "株式(かぶしき)|주식|kabushiki;株主(かぶぬし)|주주|kabunushi",
    "棒": "相棒(あいぼう)|파트너|aibou;鉄棒(てつぼう)|철봉|tetsubou",
    "模": "模様(もよう)|무늬|moyou;模型(もけい)|모형|mokei",
    "権": "権利(けんり)|권리|kenri;政権(せいけん)|정권|seiken",
    "樹": "樹木(じゅもく)|수목|jumoku;植樹(しょくじゅ)|식수|shokuju",
    "欲": "欲望(よくぼう)|욕망|yokubou;欲しい(ほしい)|원하다|hoshii",
    "段": "階段(かいだん)|계단|kaidan;手段(しゅだん)|수단|shudan",
    "沿": "沿線(えんせん)|노선변|ensen;沿う(そう)|따르다|sou",
    "泉": "温泉(おんせん)|온천|onsen;泉水(せんすい)|샘물|sensui",
    "洗": "洗濯(せんたく)|세탁|sentaku;洗面所(せんめんじょ)|세면장|senmenjo",
    "派": "派遣(はけん)|파견|haken;立派(りっぱ)|훌륭함|rippa",
    "済": "経済(けいざい)|경제|keizai;返済(へんさい)|변제|hensai",
    "源": "資源(しげん)|자원|shigen;起源(きげん)|기원|kigen",
    "潮": "満潮(まんちょう)|만조|manchou;潮干狩り(しおひがり)|조개잡이|shiohigari",
    "激": "感激(かんげき)|감격|kangeki;激しい(はげしい)|격렬하다|hageshii",
    "灰": "石灰(せっかい)|석회|sekkai;灰皿(はいざら)|재떨이|haizara", # 'seっかい' is 'せっかい'
    "熟": "成熟(せいじゅく)|성숙|seijuku;熟す(こなす)|해내다|konasu",
    "片": "破片(はへん)|파편|hahen;片道(かたみち)|편도|katamichi",
    "班": "班長(はんちょう)|조장|hanchou;救護班(きゅうごはん)|구호반|kyuugohan",
    "異": "異常(いじょう)|이상|ijou;異なる(ことなる)|다르다|kotonaru",
    "疑": "疑問(ぎもん)|의문|gimon;疑う(うたがう)|의심하다|utagau",
    "痛": "苦痛(くつう)|고통|kutsuu;痛む(いたむ)|아프다|itamu",
    "皇": "天皇(てんのう)|천황|tennou;皇帝(こうてい)|황제|koutei",
    "盛": "盛大(せいだい)|성대|seidai;盛る(もる)|그릇에담다|moru",
    "盟": "同盟(どうめい)|동맹|doumei;加盟(かめい)|가맹|kamei",
    "看": "看板(かんばん)|간판|kanban;看護師(かんごし)|간호사|kangoshi",
    "砂": "砂漠(さばく)|사막|sabaku;砂糖(さとう)|설탕|satou",
    "磁": "磁石(じしゃく)|자석|jishaku;電磁波(でんじは)|전자파|denjiha",
    "私": "私立(しりつ)|사립|shiritsu;私有(しゆう)|사유|shiyuu",
    "秘": "秘密(ひみつ)|비밀|himitsu;秘書(ひしょ)|비서|hisho",
    "穀": "穀物(こくもつ)|곡물|kokumotsu;穀類(こくるい)|곡류|kokurui",
    "穴": "墓穴(ぼけつ)|무덤|boketsu;穴場(あなば)|숨은명소|anaba",
    "窓": "窓口(まどぐち)|창구|madoguchi;同窓会(どうそうかい)|동창회|dousoukai",
    "筋": "筋肉(きんにく)|근육|kinniku;筋書き(すじがき)|줄거리|suzigaki",
    "策": "政策(せいさく)|정책|seisaku;対策(たいさく)|대책|taisaku",
    "簡": "簡単(かんたん)|간단|kantan;簡潔(かんけつ)|간결|kanketsu",
    "糖": "砂糖(さとう)|설탕|satou;糖尿(とうにょう)|당뇨|tounyou",
    "系": "系統(けいとう)|계통|keitou;系列(けいれつ)|계열|keiretsu",
    "紅": "紅茶(こうちゃ)|홍차|koucha;口紅(くちべに)|립스틱|kuchibeni",
    "納": "納得(なっとく)|납득|nattoku;納入(のうにゅう)|납입|nounyuu",
    "純": "単純(たんじゅん)|단순|tanjun;純粋(じゅんすい)|순수|junsui",
    "絹": "絹糸(きぬいと)|비단실|kinuito;絹織物(きぬおりもの)|견직물|kinuorimono",
    "縦": "縦横(じゅうおう)|종횡|juuou;縦書き(たてがき)|세로쓰기|tategaki",
    "縮": "縮小(しゅくしょう)|축소|shukushou;短縮(たんしゅく)|단축|tanshuku",
    "署": "署名(しょめい)|서명|shomei;警察署(けいさつしょ)|경찰서|keisatsusho",
    "翌": "翌日(よくじつ)|익일|yokujitsu;翌年(よくねん)|이듬해|yokunen",
    "聖": "聖書(せいしょ)|성경|seisho;神聖(しんせい)|신성|shinsei",
    "肺": "肺炎(はいえん)|폐렴|haien;肺活量(はいかつりょう)|폐활량|haikatsuryou",
    "背": "背景(はいけい)|배경|haikei;背中(せなか)|등|senaka",
    "胸": "胸中(きょうちゅう)|흉중|kyouchuu;胸騒ぎ(むなさわぎ)|불안함|munasawagi",
    "脳": "脳裏(のうり)|뇌리|nouri;頭脳(ずのう)|두뇌|zunou",
    "腹": "満腹(まんぷく)|만복|manpuku;腹立ち(はらだち)|분통|haradachi",
    "臓": "心臓(しんぞう)|심장|shinzou;内臓(ないぞう)|내장|naizou",
    "臨": "臨時(りんじ)|임시|rinji;臨海(りんかい)|임해|rinkai",
    "至": "至急(しきゅう)|시급|shikyuu;至る(いたる)|이르다|itaru",
    "若": "若者(わかもの)|젊은이|wakamono;若々しい(わかわかしい)|젊디젊다|wakawakashii",
    "著": "著名(ちょめい)|저명|chomei;著書(ちょしょ)|저서|chosho",
    "蒸": "蒸気(じょうき)|증기|jouki;蒸発(じょうはつ)|증발|jouhatsu",
    "蔵": "冷蔵庫(れいぞうこ)|냉장고|reizouko;貯蔵(ちょぞう)|저장|chozou",
    "蚕": "養蚕(ようさん)|양잠|yousan;蚕糸(さんし)|잠사|sanshi",
    "衆": "民衆(みんしゅう)|민중|minshuu;観衆(かんしゅう)|관중|kanshuu",
    "裁": "裁判(さいばん)|재판|saiban;裁断(さいだん)|재단|saidan",
    "装": "装置(そうち)|장치|souchi;衣装(いしょう)|의상|ishou",
    "裏": "裏口(うらぐち)|뒷문|uraguchi;裏切り(うらぎり)|배신|uragiri",
    "補": "補足(ほそく)|보속|hosoku;候補(こうほ)|후보|kouho",
    "視": "視界(しかい)|시야|shikai;重視(じゅうし)|중시|juushi",
    "覧": "一覧(いちらん)|일람|ichiran;閲覧(えつらん)|열람|etsuran",
    "討": "討論(とうろん)|토론|touron;検討(けんとう)|검토|kentou",
    "訪": "訪問(ほうもん)|방문|houmon;訪れる(おとずれる)|방문하다|otozureru",
    "訳": "翻訳(ほんやく)|번역|honyaku;言い訳(いいわけ)|변명|iiwake",
    "詞": "名詞(めいし)|명사|meishi;歌詞(かし)|가사|kashi",
    "誌": "雑誌(ざっし)|잡지|zasshi;日誌(にっし)|일지|nisshi",
    "認": "確認(かくにん)|확인|kakunin;認める(みとめる)|인정하다|mitomeru",
    "誕": "誕生日(たんじょうび)|생일|tanjoubi;誕生(たんじょう)|탄생|tanjou",
    "誠": "誠実(せいじつ)|성실|seijitsu;誠意(せいい)|성의|seii",
    "誤": "誤解(ごかい)|오해|gokai;誤り(あやまり)|실수|ayamari",
    "論": "論文(ろんぶん)|논문|ronbun;討論(とうろん)|토론|touron",
    "諸": "諸国(しょこく)|여러나라|shokoku;諸君(しょくん)|여러분|shokun",
    "警": "警察(けいさつ)|경찰|keisatsu;警告(けいこく)|경고|keikoku",
    "貴": "貴重(きちょう)|귀중|kichou;高貴(こうき)|고귀|kouki",
    "賃": "家賃(やちん)|집세|yachin;賃金(ちんぎん)|임금|chingin",
    "遺": "遺跡(いせき)|유적|iseki;遺言(ゆいごん)|유언|yuigon",
    "郵": "郵便(ゆうびん)|우편|yuubin;郵送(ゆうそう)|우송|yuusou",
    "郷": "故郷(こきょう)|고향|kokyou;郷土(きょうど)|향토|kyoudo",
    "針": "針路(しんろ)|침로|shinro;羅針盤(らしんばん)|나침반|rashinban",
    "鋼": "鉄鋼(てっこう)|철강|tekkou;鋼鉄(こうてつ)|강철|koutetsu",
    "閉": "閉鎖(へいさ)|폐쇄|heisa;閉める(しめる)|닫다|shimeru",
    "閣": "内閣(ないかく)|내각|naikaku;閣僚(かくりょう)|각료|kakuryou",
    "降": "降下(こうか)|강하|kouka;降りる(おりる)|내리다|oriru",
    "陛": "陛下(へいか)|폐하|heika;陛爵(へいしゃく)|작위수여|heishaku",
    "除": "除外(じょがい)|제외|jogai;削除(さくじょ)|삭제|sakujo",
    "障": "障害(しょうがい)|장해|shougai;故障(こしょう)|고장|koshou",
    "難": "困難(こんなん)|곤란|konnan;難しい(むずかしい)|어렵다|muzukashii",
    "革": "革命(かくめい)|혁명|kakumei;改革(かいかく)|개혁|kaikaku",
    "頂": "頂上(ちょうじょう)|정상|choujou;頂く(いただく)|받다|itadaku",
    "骨": "骨折(こっせつ)|골절|kossetsu;骨組み(ほねぐみ)|뼈대|honegumi"
}

# Fetch Hanja Dictionary from GitHub
def download_hanja_dict():
    print("Downloading hanja.txt from GitHub...")
    url = "https://raw.githubusercontent.com/myungcheol/hanja/master/hanja.txt"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as response:
                content = response.read().decode('utf-8')
                
            hanja_map = {}
            for line in content.splitlines():
                if '=' in line:
                    parts = line.split('=', 1)
                    char = parts[0].strip()
                    val_part = parts[1].split(',', 1)[0].strip()
                    words = val_part.split()
                    if len(words) >= 2:
                        sound = words[-1]
                        meaning = " ".join(words[:-1])
                        hanja_map[char] = (meaning, sound)
                    elif len(words) == 1:
                        hanja_map[char] = ("", words[0])
            print(f"Successfully loaded {len(hanja_map)} Hanja mapping entries.")
            return hanja_map
        except Exception as e:
            print(f"Error loading Hanja dict (attempt {attempt+1}/3): {e}")
            if attempt < 2:
                time.sleep(2)
    return {}

# Fetch single Kanji details from kanjiapi.dev
def fetch_kanji_details(kanji):
    url = f"https://kanjiapi.dev/v1/kanji/{urllib.parse.quote(kanji)}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode('utf-8'))
                
                strokes = data.get('stroke_count', 0)
                meanings = data.get('meanings', [])
                readings_on = data.get('on_readings', [])
                readings_kun = data.get('kun_readings', [])
                
                romaji_on = [kana_to_romaji(r) for r in readings_on]
                romaji_kun = [kana_to_romaji(r) for r in readings_kun]
                
                return {
                    "strokes": strokes,
                    "meanings": meanings,
                    "readings_on": readings_on,
                    "romaji_on": romaji_on,
                    "readings_kun": readings_kun,
                    "romaji_kun": romaji_kun
                }
        except Exception as e:
            print(f"Error fetching details for {kanji} (attempt {attempt+1}/3): {e}")
            if attempt < 2:
                time.sleep(2)
    return None

def process_grade(grade, kanji_list, hanja_map):
    output_path = f"d:/ag_coding_ex/jphanja/kanji_grade{grade}.json"
    print(f"\nProcessing Grade {grade}: {len(kanji_list)} kanjis...")
    
    results = []
    for idx, k in enumerate(kanji_list):
        print(f"[{idx+1}/{len(kanji_list)}] Processing {k}...")
        details = fetch_kanji_details(k)
        if not details:
            print(f"Failed to fetch details for {k}, skipping...")
            continue
            
        # Parse examples
        vocab_str = VOCAB_DB.get(k, "")
        examples = []
        if vocab_str:
            ex_parts = vocab_str.split(';')
            for ex in ex_parts:
                ex = ex.strip()
                if not ex:
                    continue
                parts = ex.split('|')
                if len(parts) == 3:
                    word, meaning, romaji = parts
                    examples.append({
                        "word": word.strip(),
                        "meaning": meaning.strip(),
                        "romaji": romaji.strip()
                    })
        
        # Get Hanja meaning/sound
        h_mean, h_sound = hanja_map.get(k, ("", ""))
        if not h_mean or not h_sound:
            # fallback if needed, or leave blank
            pass
            
        kanji_obj = {
            "kanji": k,
            "grade": grade,
            "strokes": details["strokes"],
            "meanings": details["meanings"],
            "kor_meaning": h_mean,
            "kor_sound": h_sound,
            "readings_on": details["readings_on"],
            "romaji_on": details["romaji_on"],
            "readings_kun": details["readings_kun"],
            "romaji_kun": details["romaji_kun"],
            "examples": examples
        }
        results.append(kanji_obj)
        time.sleep(0.1) # small rate limit safety delay
        
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(results)} kanji data to {output_path}")

if __name__ == "__main__":
    # Load kanji lists
    with open('d:/ag_coding_ex/jphanja/scratch/g5_list.txt', encoding='utf-8') as f:
        g5_kanji = f.read().strip().split(',')
        
    with open('d:/ag_coding_ex/jphanja/scratch/g6_list.txt', encoding='utf-8') as f:
        g6_kanji = f.read().strip().split(',')
        
    hanja_map = download_hanja_dict()
    
    process_grade(5, g5_kanji, hanja_map)
    process_grade(6, g6_kanji, hanja_map)
    
    print("\nALL GRADES COMPLETED SUCCESSFULLY!")
