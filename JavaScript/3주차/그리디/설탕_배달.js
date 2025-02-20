let fs = require('fs');
let input = fs.readFileSync('io.txt').toString();

let n = Number(input);

let gram = [5, 3];

let answer = 0;

let temp = 0;

while (n > 0) {
  if (n >= 5) {
    n -= 5;
    answer += 1;
    continue;
  }
  if (n >= 3) {
    n -= 3;
    answer += 1;
    continue;
  }
  if (n < 3 && n !== 0) {
    answer = -1;
    break;
  }
}

// 최적해가 아님

console.log(answer);
