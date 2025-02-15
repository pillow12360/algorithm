const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let n = +input[0];
let arr = input[1].split(' ').map(Number).reverse(); // 원본 배열을 뒤집음

function snack(arr) {
  let stack = [];
  let cur = 1;

  while (arr.length > 0 || stack.length > 0) {
    // 간식을 받을 차례라면 바로 pop()
    if (arr.length > 0 && arr[arr.length - 1] === cur) {
      arr.pop();
      cur++;
    }
    // 보조 스택에서 받을 수 있으면 pop()
    else if (stack.length > 0 && stack[stack.length - 1] === cur) {
      stack.pop();
      cur++;
    }
    // 대기열에서 보조 스택으로 이동
    else if (arr.length > 0) {
      stack.push(arr.pop());
    }
    // 받을 수 없는 경우
    else {
      return 'Sad';
    }
  }

  return 'Nice';
}

console.log(snack(arr));
