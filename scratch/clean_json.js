const fs = require('fs');
let data = fs.readFileSync('kaninoshoubai.JSON', 'utf8');

// Mapping specifically for the common errors in this file
const mapping = {
    '의': 'の',
    '상은': '상은', // This should be は in '오토상은' -> お父さんは
    '에는': 'には',
    '가': 'が',
    '에': 'に',
    '를': '를', // This should be を
    '는': 'は',
    '이': 'い',
    '마': 'ま',
    '라': 'ら',
    '좋은': 'いい',
    '입': 'で', // 어텐키입니다 -> お天気です
    '니': 'す',
    '다': '',
    '사본타마': 'さぼん玉',
    '하나': '하나', // This should be ひとつ
    '주세요': 'ください',
    '두 개': 'ふたつ',
    '세 개': 'みっつ'
};

// However, a simple regex replace is better for manual cleaning.
// I'll just write the full clean JSON here.
const cleanJson = [
    {
        "id": 1,
        "kanji": "かにの お父さんは、さぼん玉を 売っています。",
        "kana": "かにの おとうさんは、しゃぼんだまを うっています。",
        "romaji": "kani no otousan wa shabondama o utteimasu",
        "meaning": "아빠 게는 비눗방울을 팔고 있습니다."
    },
    {
        "id": 2,
        "kanji": "「さぼん玉、いかがですか。」",
        "kana": "「しゃぼんだま、いかがですか。」",
        "romaji": "shabondama ikaga desu ka",
        "meaning": "“비눗방울, 어떠신가요?”"
    },
    {
        "id": 3,
        "kanji": "お父さんは、口から ぷうぷう ふきます。",
        "kana": "おとうさんは、く치から ぷうぷう ふきます。", // Wait, I just typed 'chi' in Korean style... fixed
        "romaji": "otousan wa kuchi kara puupuu fukimasu",
        "meaning": "아빠 게는 입으로 푸푸 하고 (비눗방울을) 붑니다."
    },
    {
        "id": 4,
        "kanji": "さぼん玉は、青い お空へ 飛んで いきました。",
        "kana": "しゃぼんだまは、あおい おそらへ とんで いきました。",
        "romaji": "shabondama wa aoi osora e tonde ikimashita",
        "meaning": "비눗방울은 푸른 하늘로 날아갔습니다."
    },
    {
        "id": 5,
        "kanji": "一番目には、えびが 買いに きました。",
        "kana": "いちばんめには、えびが かいに きました。",
        "romaji": "ichibanme ni wa ebi ga kai ni kimashita",
        "meaning": "첫 번째로는 새우가 사러 왔습니다."
    },
    {
        "id": 6,
        "kanji": "「さぼん玉、一つ ください。」",
        "kana": "「しゃぼんだま、ひとつ ください。」",
        "romaji": "shabondama hitotsu kudasai",
        "meaning": "“비눗방울 하나 주세요.”"
    },
    {
        "id": 7,
        "kanji": "えびは、長い おひげを ぴんぴんさせて いきました。",
        "kana": "え비は, ながい おひげを ぴんぴんさせて いきました.", // Wait, え비.. fixed
        "romaji": "ebi wa nagai ohige o pinpinsasete ikimashita",
        "meaning": "새우는 긴 수염을 씰룩거리며 갔습니다."
    },
    {
        "id": 8,
        "kanji": "二番目には、お魚가 買いに きました。", // Wait, '가'... fixed
        "kana": "にばんめには, おさかなが かいに きました.",
        "romaji": "nibanme ni wa osakana ga kai ni kimashita",
        "meaning": "두 번째로는 물고기가 사러 왔습니다."
    },
    {
        "id": 9,
        "kanji": "「さぼん玉、二つ ください。」",
        "kana": "「しゃぼんだま、ふたつ ください。」",
        "romaji": "shabondama futatsu kudasai",
        "meaning": "“비눗방울 두 개 주세요.”"
    },
    {
        "id": 10,
        "kanji": "お魚は、赤い ひれを ひらひらさせて いきました。",
        "kana": "おさかなは、あかい ひれを ひらひらさせて いきました。",
        "romaji": "osakana wa akai hire o hirahirasete ikimashita",
        "meaning": "물고기는 빨간 지느러미를 살랑거리며 갔습니다."
    },
    {
        "id": 11,
        "kanji": "三番目には、たこが 買いに きました。",
        "kana": "さんばんめには、たこが かいに きました。",
        "romaji": "sanbanme ni wa tako ga kai ni kimashita",
        "meaning": "세 번째로는 문어가 사러 왔습니다."
    },
    {
        "id": 12,
        "kanji": "「さぼん玉、三つ ください。」",
        "kana": "「しゃぼんだま、みっつ ください。」",
        "romaji": "shabondama mittsu kudasai",
        "meaning": "“비눗방울 세 개 주세요.”"
    },
    {
        "id": 13,
        "kanji": "たこは、八つの 足を にょろにょろさせて いきました。",
        "kana": "たこは、やっつの あしを にょろにょろさせて いきました。",
        "romaji": "tako wa yattsu no ashi o nyoronyorosete ikimashita",
        "meaning": "문어는 여덟 개의 다리를 꿈틀거리며 갔습니다."
    },
    {
        "id": 14,
        "kanji": "お父さんは、にこにこ 笑いました。",
        "kana": "おとうさんは、にこにこ わらいました。",
        "romaji": "otousan wa nikoniko waraimashita",
        "meaning": "아빠 게는 싱글벙글 웃었습니다."
    },
    {
        "id": 15,
        "kanji": "오늘은, とても いい お天気です。", // Wait, '오늘은'... fixed
        "kana": "きょうは、とても いい おてんきです。",
        "romaji": "kyou wa totemo ii otenki desu",
        "meaning": "오늘은 날씨가 매우 좋습니다."
    }
];

// Final check for ID 3, 7, 8, 15
cleanJson[2].kana = "おとうさんは、くちから ぷうぷう ふきます。";
cleanJson[6].kanji = "えびは、長い おひげを ぴんぴんさせて いきました。";
cleanJson[6].kana = "えびは、ながい おひげを ぴんぴんさせて いきました。";
cleanJson[7].kanji = "二番目에는, お魚가 買い에 きました."; // Wait, STIILL!!
cleanJson[7].kanji = "二番目には、お魚が 買いに きました。";
cleanJson[14].kanji = "今日は、とても いい お天気です。";

fs.writeFileSync('kaninoshoubai.JSON', JSON.stringify(cleanJson, null, 4));
console.log('JSON cleaned successfully');
