let n = 6;
let cows = [5, 2, 4, 2, 6, 1];

// 명제가 어려우면 대우로 풀어라

// 내가 보는 소 수가 아닌,
// 나를 보는 소를 스택에 넣는다.

// 명제가 참이면 대우도 참이다.

// stack[n] == 나를 볼 수 있는 소

// 골드 이상의 문제는 시간복잡도를 무조건 고려하여 풀것
function countCows(heights) {
  let stack = [];
  let count = 0;

  for (let height of heights) {
    while (stack.length > 0 && stack[stack.length - 1] <= height) {
      stack.pop();
    }
    count += stack.length;
    stack.push(height);
  }
  return count;
}

console.log(countCows(cows));
