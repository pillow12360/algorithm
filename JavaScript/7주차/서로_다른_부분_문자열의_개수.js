let fs = require('fs');
let input = fs.readFileSync(0, 'utf-8').split('');

let len = input.length;
let answer = new Set();

// i는 윈도우 크기
// j는 인덱스

for (let i = 1; i <= len; i++) {
  for (let j = 0; j <= len - i; j++) {
    if (input.slice(j, j + i).length === 0) continue;
    answer.add(input.slice(j, j + i).join(''));
  }
}

// console.log(answer);
// console.log(setAnswer);
console.log(answer.size);
