let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let n = Number(input[0]);
let words = input.slice(1).map((i) => i.trim()); // 개행문자 처리
// console.log(words);

let answer = 0;

for (let word of words) {
  let stack = [];
  for (let w of word) {
    if (stack.length !== 0 && w === stack[stack.length - 1]) {
      stack.pop();
    } else {
      stack.push(w);
    }
  }

  if (stack.length === 0) {
    answer += 1;
  }
}

console.log(answer);
