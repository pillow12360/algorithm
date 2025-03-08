let fs = require('fs');

let [m, n] = fs.readFileSync('io.txt').toString().split(' ').map(Number);

let is_sosu = Array(n + 1).fill(true);
is_sosu[0] = is_sosu[1] = false; // 0과 1은 소수가 아님

for (let i = 2; i <= Math.sqrt(n); i++) {
  // 여기서 범위 수정
  if (is_sosu[i]) {
    for (let j = i * i; j <= n; j += i) {
      is_sosu[j] = false;
    }
  }
}

// M 이상 N 이하의 소수 출력
let result = [];
for (let i = m; i <= n; i++) {
  if (is_sosu[i]) {
    result.push(i);
  }
}

console.log(result.join('\n'));

// 0, 1 제외
// 소수일 경우에만 해당 수열의 마지막까지 해당 소수의 배수 제거
// 이경우를 마지막 수열의 제곱근 까지 반복하면된다.
