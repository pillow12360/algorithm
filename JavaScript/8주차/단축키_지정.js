let fs = require('fs');
let input = fs.readFileSync(0, 'utf-8').trim().split('\n');

let n = +input[0];
let words = input.slice(1);

words = words.map((i) => i.split(' '));

let usedKeys = new Set(); // 단축키로 지정된 문자 저장
let result = [];

for (let word of words) {
  let shortcutAssigned = false; // 단축키가 등록되었는지 여부

  // 각 단어의 첫 번째 문자를 단축키로 할 수 있는지 확인
  for (let i = 0; i < word.length; i++) {
    let firstChar = word[i][0].toLowerCase();

    if (!usedKeys.has(firstChar)) {
      usedKeys.add(firstChar);
      word[i] = `[${word[i][0]}]` + word[i].slice(1);
      shortcutAssigned = true;
      break;
    }
  }

  // 첫 번째 문자 등록 실패 시, 단어 내 다른 문자에서 단축키 찾기
  if (!shortcutAssigned) {
    for (let i = 0; i < word.length; i++) {
      for (let j = 1; j < word[i].length; j++) {
        let char = word[i][j].toLowerCase();

        if (!usedKeys.has(char)) {
          usedKeys.add(char);
          word[i] =
            word[i].slice(0, j) + `[${word[i][j]}]` + word[i].slice(j + 1);
          shortcutAssigned = true;
          break;
        }
      }
      if (shortcutAssigned) break;
    }
  }

  // 그래도 단축키를 찾지 못했다면 그대로 둠
  result.push(word.join(' '));
}
console.log(result.join('\n'));
