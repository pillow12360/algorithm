let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim();
let n = Number(input);

if (n === 0) {
  console.log(0);
  return;
}

// **팩토리얼을 직접 계산하지 않고 5의 배수 개수를 세는 방식**
let count = 0;
let divisor = 5;

while (n >= divisor) {
  count += Math.floor(n / divisor);
  divisor *= 5;
}

console.log(count);
