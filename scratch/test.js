const fs = require('fs');
const data = JSON.parse(fs.readFileSync('kaninotokoya.JSON', 'utf-8'));

function alignFurigana(kanjiStr, kanaStr) {
    let result = [];
    const isKanji = (c) => /[\u4E00-\u9FAF\u3005]/.test(c);
    
    let blocks = [];
    let currentBlock = "";
    if(kanjiStr.length === 0) return [];
    let currentIsKanji = isKanji(kanjiStr[0]);
    
    for (let c of kanjiStr) {
        if (isKanji(c) === currentIsKanji) {
            currentBlock += c;
        } else {
            blocks.push({text: currentBlock, isKanji: currentIsKanji});
            currentIsKanji = isKanji(c);
            currentBlock = c;
        }
    }
    if (currentBlock) blocks.push({text: currentBlock, isKanji: currentIsKanji});
    
    let kStrIdx = 0;
    for (let i = 0; i < blocks.length; i++) {
        let block = blocks[i];
        if (!block.isKanji) {
            let nextIdx = kanaStr.indexOf(block.text, kStrIdx);
            if (nextIdx > kStrIdx) {
                // Must be the gap from previous kanji
                result[result.length - 1].kana = kanaStr.substring(kStrIdx, nextIdx);
            }
            result.push({text: block.text});
            kStrIdx = nextIdx + block.text.length;
        } else {
            result.push({text: block.text, isKanji: true});
            if (i === blocks.length - 1) {
                result[result.length - 1].kana = kanaStr.substring(kStrIdx);
            }
        }
    }
    return result;
}

for (let item of data) {
   let segments = alignFurigana(item.kanji, item.kana);
   console.log(item.kanji);
   console.log(segments);
   console.log('---');
}
