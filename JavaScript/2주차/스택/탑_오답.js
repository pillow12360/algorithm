let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let heights = input[1].split(' ').map(Number);
let stack = [];
let answer = Array(n).fill(0); // 기본적으로 0을 넣어줌

for (let i = 0; i < n; i++) {
  while (stack.length > 0 && stack[stack.length - 1][1] <= heights[i]) {
    stack.pop(); // 현재 탑보다 작은 탑들은 볼 수 없으므로 제거
  }

  if (stack.length > 0) {
    answer[i] = stack[stack.length - 1][0]; // 수신할 수 있는 가장 가까운 탑의 번호 저장
  }

  stack.push([i + 1, heights[i]]); // 현재 탑을 스택에 추가 (1-based index)
}

console.log(answer.join(' '));
