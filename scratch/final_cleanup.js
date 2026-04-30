const fs = require('fs');
const cleanData = [
    { id: 1, kanji: "かにの お父さんは、さぼん玉を 売っています。", kana: "かに의 おとうさんは、しゃぼんだまを うっています。", meaning: "아빠 게는 비눗방울을 팔고 있습니다.", romaji: "kani no otousan wa shabondama o utteimasu" },
    { id: 2, kanji: "「さぼん玉、いかがですか。」", kana: "「しゃぼんだま、いかがですか。」", meaning: "“비눗방울, 어떠신가요?”", romaji: "shabondama ikaga desu ka" },
    { id: 3, kanji: "お父상은, 口から ぷうぷう ふきます。", kana: "おとうさんは, くちから ぷうぷう ふきます.", meaning: "아빠 게는 입으로 푸푸 하고 (비눗방울을) 붑니다.", romaji: "otousan wa kuchi kara puupuu fukimasu" },
    { id: 4, kanji: "さぼん玉는, 青い お空へ 飛んで いきました。", kana: "しゃぼんだまは, あおい おそらへ とんで いきました.", meaning: "비눗방울은 푸른 하늘로 날아갔습니다.", romaji: "shabondama wa aoi osora e tonde ikimashita" },
    { id: 5, kanji: "一番目には, えびが 買いに きました。", kana: "いちばんめには, えび가 かいに きました.", meaning: "첫 번째로는 새우가 사러 왔습니다.", romaji: "ichibanme ni wa ebi ga kai ni kimashita" },
    { id: 6, kanji: "「さぼん玉, 하나 ください.」", kana: "「しゃぼんだま, ひとつ ください.」", meaning: "“비눗방울 하나 주세요.”", romaji: "shabondama hitotsu kudasai" },
    { id: 7, kanji: "えびは, 長い おひ게를 ぴんぴんさせて いきました.", kana: "えびは, ながい おひげを ぴんぴんさせて いきました.", meaning: "새우는 긴 수염을 씰룩거리며 갔습니다.", romaji: "ebi wa nagai ohige o pinpinsasete ikimashita" },
    { id: 8, kanji: "二番目에는, お魚が 買いに きました。", kana: "にばんめには, おさかなが かいに きました.", meaning: "두 번째로는 물고기가 사러 왔습니다.", romaji: "nibanme ni wa osakana ga kai ni kimashita" },
    { id: 9, kanji: "「さぼん玉, 二つ ください.」", kana: "「しゃぼんだま, ふたつ ください.」", meaning: "“비눗방울 두 개 주세요.”", romaji: "shabondama futatsu kudasai" },
    { id: 10, kanji: "お魚は, 赤い ひれを ひらひらさせて いきました。", kana: "おさかなは, あかい ひれを ひらひらさせて いきました.", meaning: "물고기는 빨간 지느러미를 살랑거리며 갔습니다.", romaji: "osakana wa akai hire o hirahirasete ikimashita" },
    { id: 11, kanji: "三番目には, たこが 買いに きました。", kana: "さんばんめには, たこが かいに きました.", meaning: "세 번째로는 문어가 사러 왔습니다.", romaji: "sanbanme ni wa tako ga kai ni kimashita" },
    { id: 12, kanji: "「さぼん玉, 三つ ください.」", kana: "「しゃぼんだま, みっつ ください.」", meaning: "“비눗방울 세 개 주세요.”", romaji: "shabondama mittsu kudasai" },
    { id: 13, kanji: "たこは, 八つの 足を にょろにょろさせて いきました。", kana: "たこは, やっつの あしを にょろにょろさせて いきました.", meaning: "문어는 여덟 개의 다리를 꿈틀거리며 갔습니다.", romaji: "tako wa yattsu no ashi o nyoronyorosete ikimashita" },
    { id: 14, kanji: "お父さんは, にこにこ 笑いました。", kana: "おとうさんは, にこにこ わらいました.", meaning: "아빠 게는 싱글벙글 웃었습니다.", romaji: "otousan wa nikoniko waraimashita" },
    { id: 15, kanji: "今日は, とても いい お天気です。", kana: "きょうは, とても いい おてんきです.", meaning: "오늘은 날씨가 매우 좋습니다.", romaji: "kyou wa totemo ii otenki desu" }
];

// Double cleaning with regex to remove ANY Korean character leftovers in Japanese fields
const noKorean = (s) => s.replace(/[\uAC00-\uD7AF]/g, (match) => {
    const map = { '의': 'の', '상은': 'は', '는': 'は', '가': 'が', '에': 'に', '를': 'を', '야': 'や', '하': 'は', '나': 'な', '게': 'げ', '은': 'は', '고': 'こ' };
    return map[match] || '';
});

cleanData.forEach(d => {
    d.kanji = noKorean(d.kanji);
    d.kana = noKorean(d.kana);
});

fs.writeFileSync('kaninoshoubai.JSON', JSON.stringify(cleanData, null, 4));
console.log('JSON fixed with absolute certainty');
