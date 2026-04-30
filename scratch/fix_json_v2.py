import json

path = 'd:/ag_coding_ex/jphanja/kaninotokoya.JSON'

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    if 6 <= item['id'] <= 20:
        # Correct kanji
        if 'kanji' in item:
            item['kanji'] = item['kanji'].replace('에는', 'には').replace('가', 'が').replace('네를', 'ねを').replace('네오', 'ねを').replace('과', 'と').replace('을', 'を').replace('야이지만', 'やですが').replace('야데모', 'やでも').replace('잘', 'よく').replace('니아타마오요쿠미마시타', 'のあたまをよくみました').replace('코데아리마시타', 'こでありました').replace('야입니다만', 'やですが').replace('데스카라', 'ですから').replace('해서', 'して').replace('로', 'で').replace('이케나이', 'いけない').replace('시는', 'しは').replace('에', 'に').replace('나', 'な').replace('과야', 'とこ야').replace('와', 'と')
        
        # Correct kana
        if 'kana' in item:
            item['kana'] = item['kana'].replace('에는', 'には').replace('가', '가').replace('코', 'こ').replace('네오', 'ねを').replace('산', 'さん').replace('야이지만', 'や이지만').replace('용은', 'ようは').replace('고란요', 'ごらんよ').replace('니아타마오요쿠미마시타', 'のあたまをよくみました').replace('코데아리마시타', 'こでありました').replace('야데모', 'やでも').replace('을', 'を').replace('는', 'は').replace('에', 'に').replace('네오하고있었습니다', 'ねをしていました').replace('해서', 'して').replace('와', 'と').replace('이이마시타', 'いいました').replace('이케나이', 'いけない').replace('로', 'で').replace('나', 'な').replace('과야', 'とこや')

# Final manual overrides for consistency with story
final_fixes = {
    6: ["そこには たこが ひるねを していました。", "そこ에는 たこが ひるねを していました。"], # wait
    10: ["「よくごらんよ。わたしの頭に毛があるかどうか。」", "「よくごらんよ。わたしのあたまにけがあるかどうか。」"],
    17: ["たぬきはめをさまして、「なんだ。」といいました。", "たぬきはめをさまして、「なんだ。」といいました。"],
    18: ["「とこやですが ごようはありませんか。」", "「とこや이지만 ごようはありませんか。」"],
}

for item in data:
    i = item['id']
    if i == 6:
        item['kanji'] = "そこには たこが ひるねを していました。"
        item['kana'] = "そこには たこが ひるねを していました。"
    elif i == 7:
        item['kanji'] = "「もしもし、たこさん。」と蟹はよびかけました。"
        item['kana'] = "「もしもし、たこさん。」とかにはよびかけました。"
    elif i == 8:
        item['kanji'] = "たこはめをさまして、「なんだ。」といいました。"
        item['kana'] = "た코하메오사마시테".replace('코', 'こ').replace('하', 'は').replace('메', 'め').replace('오', 'を').replace('사', 'さ').replace('마', 'ま').replace('시', 'し').replace('테', 'て') + "、「なんだ。」といいました。"
        item['kana'] = "たこはめをさまして、「なんだ。」といいました。"
    elif i == 9:
        item['kanji'] = "「とこやですが、ごようはありませんか。」"
        item['kana'] = "「とこやですが、ごようはありませんか。」"
    elif i == 10:
        item['kanji'] = "「よくごらんよ。わたしの頭에毛があるかどうか。」".replace('에', 'に').replace('시는', 'しは')
        item['kanji'] = "「よくごらんよ。わたしの頭に毛があるかどうか。」"
        item['kana'] = "「よくごらんよ。わたしのあたまにけがあるかどうか。」"
    elif i == 13:
        item['kanji'] = "いくら蟹がじょうずなとこやでも、毛のない頭をかることはできません。"
        item['kana'] = "いくらかにがじょうずなとこやでも、けのないあたまをかることはできません。"
    elif i == 15:
        item['kanji'] = "山には たぬきが ひるねを していました。"
        item['kana'] = "やまにはたぬき가ひ루네오하고있었습니다.".replace('가', 'が').replace('히루네오하고있었습니다', 'ひるねをしていました')
        item['kana'] = "やま에는たぬきがひるねをしていました。".replace('에는', 'には')
    elif i == 17:
        item['kanji'] = "たぬきはめをさまして、「なんだ。」といいました。"
        item['kana'] = "たぬきはめをさまして、「なんだ。」といいました。"
    elif i == 18:
        item['kanji'] = "「とこやですが ごようはありませんか。」"
        item['kana'] = "「とこやですが ごようはありませんか。」"
    elif i == 19:
        item['kanji'] = "たぬきは、いたずらがすきなけものですから、よくないことを考えました。"
        item['kana'] = "たぬきは、いたずらがすきなけものですから、よくないことをかんがえました。"
    elif i == 20:
        item['kanji'] = "「よろしい、かってもらおう。ところで、ひとつやくそくしてくれ나きゃいけない。」".replace('나', 'な')
        item['kanji'] = "「よろしい、かってもらおう。ところで、ひとつやくそくしてくれなきゃいけない。」"
        item['kana'] = "「よろしい、かってもらおう。ところで、ひとつやくそくしてくれなきゃいけない。」"

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
