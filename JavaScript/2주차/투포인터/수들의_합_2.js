let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let num = input[1].split(' ').map(Number);

let left = 0,
  right = 0;
let sum = 0;
let answer = 0;

while (right < n) {
  sum += num[right]; // 오른쪽 포인터 값을 추가

  while (sum > m) {
    // 합이 M보다 크면 왼쪽 포인터 이동
    sum -= num[left];
    left++;
  }

  if (sum === m) {
    // 합이 M이면 경우의 수 증가
    answer++;
  }

  right++; // 오른쪽 포인터 이동
}

console.log(answer);
