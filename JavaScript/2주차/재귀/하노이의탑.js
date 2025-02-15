let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim();
let num = Number(input);

// 이동 횟수 계산 (2^num - 1)
let answer = 2n ** BigInt(num) - 1n; // N이 100까지 가능하므로 BigInt 사용
console.log(answer.toString());

// N이 20보다 크면 과정 생략
if (num > 20) {
  process.exit(0);
}

let result = [];

function hanoi(n, from, target, temp) {
  if (n === 1) {
    result.push(`${n}번 원판을 ${from}에서 ${target}로 이동`);
    return;
  }
  hanoi(n - 1, from, temp, target);
  result.push(`${n}번 원판을 ${from}에서 ${target}로 이동`);
  hanoi(n - 1, temp, target, from);
}

hanoi(num, 'A', 'C', 'B');
console.log(result.join('\n'));
