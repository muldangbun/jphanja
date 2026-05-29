import json

def main():
    file_path = 'convenience_scenesv1.JSON'
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for scene in data['scenarios']:
        if scene['id'] == 'con-02':
            # Fix duplicate ID
            for i, line in enumerate(scene['dialogue']):
                line['id'] = i + 1
                
            scene['dialogue'].extend([
                {
                    "id": 7,
                    "speaker": "점원",
                    "kanji": "そうですか。では、割れ物注意のシールは貼りません。料金は千二百円になります。",
                    "kana": "そうですか。では、われものちゅういのシールははりません。りょうきんはせんにひゃくえんになります。",
                    "romaji": "sou desu ka. dewa, waremono chuui no shiiru wa harimasen. ryoukin wa sennihyakuen ni narimasu",
                    "meaning": "그렇군요. 그럼 파손 주의 스티커는 붙이지 않겠습니다. 요금은 1,200엔입니다."
                },
                {
                    "id": 8,
                    "speaker": "손님",
                    "kanji": "はい、千二百円ですね。よろしくお願いします。",
                    "kana": "はい、せんにひゃくえんですね。よろしくおねがいします。",
                    "romaji": "hai, sennihyakuen desu ne. yoroshiku onegaishimasu",
                    "meaning": "네, 여기 1,200엔입니다. 잘 부탁드립니다."
                },
                {
                    "id": 9,
                    "speaker": "점원",
                    "kanji": "千二百円ちょうど頂戴いたします。こちらが領収書とお客様控えになります。ありがとうございました。",
                    "kana": "せんにひゃくえんちょうどちょうだいたします。こちらがりょうしゅうしょとおきゃくさまひかえになります。ありがとうございました。",
                    "romaji": "sennihyakuen choudo choudaiitashimasu. kochira ga ryoushuusho to okyakusama hikae ni narimasu. arigatou gozaimashita",
                    "meaning": "1,200엔 정확히 받았습니다. 이쪽이 영수증과 고객 보관용 전표입니다. 감사합니다."
                }
            ])
            
            scene['grammar']['points'].extend([
                {
                    "title": "割れ物注意 (われものちゅうい)",
                    "desc": ["파손 주의 (택배 등의 스티커)"]
                },
                {
                    "title": "シール",
                    "desc": ["스티커"]
                },
                {
                    "title": "料金 (りょうきん)",
                    "desc": ["요금"]
                },
                {
                    "title": "控え (ひかえ)",
                    "desc": ["보관용 전표, 영수증 원부"]
                }
            ])

        elif scene['id'] == 'con-03':
            # Remove the last line (id: 4) which is abrupt
            scene['dialogue'] = scene['dialogue'][:3]
            
            scene['dialogue'].extend([
                {
                    "id": 4,
                    "speaker": "점원",
                    "kanji": "はい、確認いたしました。ガス代四千五百円と手数料百十円、合わせて四千六百十円になります。",
                    "kana": "はい、かくにんいたしました。ガスだいよんせんごひゃくえんとてすうりょうひゃくじゅうえん、あわせてよんせんろっぴゃくじゅうえんになります。",
                    "romaji": "hai, kakunin itashimashita. gasudai yonsengohyakuen to tesuuryou hyakujuuen, awasete yonsenroppyakujuuen ni narimasu",
                    "meaning": "네, 확인했습니다. 가스 요금 4,500엔과 수수료 110엔, 합해서 4,610엔입니다."
                },
                {
                    "id": 5,
                    "speaker": "손님",
                    "kanji": "カードで支払うことはできますか。",
                    "kana": "カードでしはらうことはできますか。",
                    "romaji": "kaado de shiharau koto wa dekimasu ka",
                    "meaning": "카드로 결제할 수 있나요?"
                },
                {
                    "id": 6,
                    "speaker": "점원",
                    "kanji": "申し訳ございません。公共料金は現金のみのお支払いとなっております。",
                    "kana": "もうしわけございません。こうきょうりょうきんはげんきんのみのおしはらいとなっております。",
                    "romaji": "moushiwake gozaimasen. koukyou ryoukin wa genkin nomi no oshiharai to natte orimasu",
                    "meaning": "죄송합니다만, 공공요금은 현금으로만 결제 가능합니다."
                },
                {
                    "id": 7,
                    "speaker": "손님",
                    "kanji": "あ、そうなんですね。じゃあ、五千円からお願いします。",
                    "kana": "あ、そうなんですね。じゃあ、ごせんえんからおねがいします。",
                    "romaji": "a, sou nan desu ne. jaa, gosenen kara onegaishimasu",
                    "meaning": "아, 그렇군요. 그럼 5,000엔으로 부탁합니다."
                },
                {
                    "id": 8,
                    "speaker": "점원",
                    "kanji": "五千円お預かりいたします。三百九十円のお返しと領収書になります。領収書は大切に保管しておいてください。",
                    "kana": "ごせんえんおあずかりいたします。さんびゃくきゅうじゅうえんのおかえしとりょうしゅうしょになります。りょうしゅうしょはたいせつにほかんしておいてください。",
                    "romaji": "gosenen oazukariitashimasu. sanbyakukyuujuuen no okaeshi to ryoushuusho ni narimasu. ryoushuusho wa taisetsu ni hokan shite oite kudasai",
                    "meaning": "5,000엔 받았습니다. 390엔 거스름돈과 영수증입니다. 영수증은 소중히 보관해 두세요."
                }
            ])

            scene['grammar']['points'].extend([
                {
                    "title": "手数料 (てすうりょう)",
                    "desc": ["수수료"]
                },
                {
                    "title": "現金 (げんきん)",
                    "desc": ["현금"]
                },
                {
                    "title": "お預かりいたします (おあずかりいたします)",
                    "desc": ["맡겠습니다 (계산할 때 돈을 받으며 하는 정중한 표현)"]
                },
                {
                    "title": "お返し (おかえし)",
                    "desc": ["거스름돈, 반환"]
                }
            ])

        elif scene['id'] == 'con-04':
            for i, line in enumerate(scene['dialogue']):
                line['id'] = i + 1
                
            scene['dialogue'].extend([
                {
                    "id": 5,
                    "speaker": "손님",
                    "kanji": "はい、わかりました。こちらで待たせていただきます。",
                    "kana": "はい、わかりました。こちらでまたせていただきます。",
                    "romaji": "hai, wakarimashita. kochira de matasete itadakimasu",
                    "meaning": "네, 알겠습니다. 여기서 기다릴게요."
                },
                {
                    "id": 6,
                    "speaker": "점원",
                    "kanji": "大変お待たせいたしました。掃除が終わりましたので、どうぞご利用ください。",
                    "kana": "たいへんおまたせいたしました。そうじがおわりましたので、どうぞごりようください。",
                    "romaji": "taihen omatase itashimashita. souji ga owarimashita node, douzo goriyou kudasai",
                    "meaning": "오래 기다리셨습니다. 청소가 끝났으니 이용해 주세요."
                },
                {
                    "id": 7,
                    "speaker": "손님",
                    "kanji": "ありがとうございます。",
                    "kana": "ありがとうございます。",
                    "romaji": "arigatou gozaimasu",
                    "meaning": "감사합니다."
                }
            ])

            scene['grammar']['points'].extend([
                {
                    "title": "お待たせいたしました (おまたせいたしました)",
                    "desc": ["기다리게 해서 죄송합니다, 오래 기다리셨습니다."]
                },
                {
                    "title": "利用 (りよう)",
                    "desc": ["이용"]
                }
            ])

        elif scene['id'] == 'con-05':
            for i, line in enumerate(scene['dialogue']):
                line['id'] = i + 1
                
            scene['dialogue'].extend([
                {
                    "id": 5,
                    "speaker": "손님",
                    "kanji": "それでは、一冊予約をお願いします。連絡先はこちらに書けばいいですか。",
                    "kana": "それでは、いっさつよやくをおねがいします。れんらくさきはこちらにかけばいいですか。",
                    "romaji": "sore dewa, issatsu yoyaku o onegaishimasu. renrakusaki wa kochira ni kakeba ii desu ka",
                    "meaning": "그러면 한 권 예약 부탁드립니다. 연락처는 여기에 적으면 되나요?"
                },
                {
                    "id": 6,
                    "speaker": "점원",
                    "kanji": "はい、こちらの用紙にお名前とお電話番号をご記入ください。",
                    "kana": "はい、こちらのようしにおなまえとおでんわばんごうをごきにゅうください。",
                    "romaji": "hai, kochira no youshi ni onamae to odenwabangou o gokinyuu kudasai",
                    "meaning": "네, 이쪽 용지에 성함과 전화번호를 기입해 주세요."
                },
                {
                    "id": 7,
                    "speaker": "손님",
                    "kanji": "書きました。いつ頃入ってきますか。",
                    "kana": "かきました。いつごろはいってきますか。",
                    "romaji": "kakimashita. itsugoro haitte kimasu ka",
                    "meaning": "다 적었습니다. 언제쯤 들어오나요?"
                },
                {
                    "id": 8,
                    "speaker": "점원",
                    "kanji": "明後日の午後には入荷する予定です。届き次第、お電話いたしますね。",
                    "kana": "あさってのごごにはにゅうかするよていです。とどきしだい、おでんわいたしますね。",
                    "romaji": "asatte no gogo niwa nyuukasuru yotei desu. todokishidai, odenwaitashimasu ne",
                    "meaning": "모레 오후에는 입고될 예정입니다. 도착하는 대로 전화드리겠습니다."
                },
                {
                    "id": 9,
                    "speaker": "손님",
                    "kanji": "わかりました。よろしくお願いします。",
                    "kana": "わかりました。よろしくおねがいします。",
                    "romaji": "wakarimashita. yoroshiku onegaishimasu",
                    "meaning": "알겠습니다. 잘 부탁드립니다."
                }
            ])

            scene['grammar']['points'].extend([
                {
                    "title": "～次第 (～しだい)",
                    "desc": ["~하는 대로 (조건이 충족되면 바로 행동함을 나타냄)"]
                },
                {
                    "title": "連絡先 (れんらくさき)",
                    "desc": ["연락처"]
                },
                {
                    "title": "用紙 (ようし)",
                    "desc": ["용지"]
                },
                {
                    "title": "明後日 (あさって)",
                    "desc": ["모레"]
                },
                {
                    "title": "予定 (よてい)",
                    "desc": ["예정"]
                }
            ])
            
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        
    print("Successfully updated convenience_scenesv1.JSON")

if __name__ == "__main__":
    main()
