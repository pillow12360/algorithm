// 1 : 완전 탐색
// 2 : 투포인터

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let num = input[1].split(' ').map(Number);
let answer = 0;
// 부분 수열 구하기 길이 1~N 까지

numSub = [];

function sub(num, index = 0, current = []) {
  if (index === num.length) {
    if (current.length > 0) {
      numSub.push(current);
    }
    return;
  }
  sub(num, index + 1, current);

  sub(num, index + 1, [...current, num[index]]);
}
sub(num);

numSub.forEach((a) => {
  let sumNum = a.reduce((acc, cur) => {
    return acc + cur;
  }, 0);
  if (sumNum === m) {
    answer++;
  }
});

console.log(answer);
