const fs = require('fs');

const feText = fs.readFileSync('d:/ag_coding_ex/jphanja/scratch/extracted_fe.js', 'utf8');
const fe = eval(feText);

const toolRadicals = fe.filter(r => r.category === 'tool');

const formattedLines = toolRadicals.map(r => {
  return `  { original: "${r.original}", variant: "${r.variant}", name: "${r.name}", meaning: "${r.meaning}", category: "${r.category}", reading_on: "${r.reading_on}", reading_kun: "${r.reading_kun}" },`;
});

const radicalsDataPath = 'd:/ag_coding_ex/jphanja/radical/src/data/radicalsData.js';
let content = fs.readFileSync(radicalsDataPath, 'utf8');

const isCRLF = content.includes('\r\n');
const lines = content.split(isCRLF ? '\r\n' : '\n');

// Find the index of the comment '// 도구/행동 (20개)'
let commentIdx = lines.findIndex(l => l.includes('// 도구/행동 (20개)'));
if (commentIdx === -1) {
  // Try single quotes or slight variations just in case
  commentIdx = lines.findIndex(l => l.includes('도구/행동'));
}

if (commentIdx !== -1) {
  // Find the first '];' after the comment
  let endIdx = -1;
  for (let i = commentIdx; i < lines.length; i++) {
    if (lines[i].trim() === '];') {
      endIdx = i;
      break;
    }
  }
  
  if (endIdx !== -1) {
    // The lines to replace are from commentIdx + 1 to endIdx - 1
    console.log(`Replacing lines ${commentIdx + 1} to ${endIdx - 1}`);
    
    // We remove the old lines and insert the formattedLines
    lines.splice(commentIdx + 1, endIdx - (commentIdx + 1), ...formattedLines);
    
    fs.writeFileSync(radicalsDataPath, lines.join(isCRLF ? '\r\n' : '\n'), 'utf8');
    console.log('Successfully fixed radicalsData.js cleanly!');
  } else {
    console.error('Could not find closing ]; after comment');
  }
} else {
  console.error('Could not find comment // 도구/행동 (20개) in radicalsData.js');
}
