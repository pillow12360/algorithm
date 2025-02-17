let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let n = Number(input[0]);
let sunsoo = input.slice(1);

let count = {}; // 성의 첫 글자 개수 저장
sunsoo.forEach((name) => {
  let firstLetter = name[0];
  count[firstLetter] = (count[firstLetter] || 0) + 1;
});

// 5명 이상인 성의 첫 글자 추출
let answer = Object.keys(count).filter((key) => count[key] >= 5);

// 결과 출력
if (answer.length === 0) {
  console.log('PREDAJA');
} else {
  console.log(answer.sort().join(''));
}
