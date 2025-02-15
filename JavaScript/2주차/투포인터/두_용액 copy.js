let fs = require('fs');

let input = fs.readFileSync('io.txt').toString().split('\n');
let n = Number(input[0]);
let arr = input[1].split(' ').map(Number);

// 오름차순 정렬 (중요!)
arr.sort((a, b) => a - b);

let zeroValue = Infinity;
let answer = [0, 0];
let p1 = 0;
let p2 = arr.length - 1;

while (p1 < p2) {
  let curValue = arr[p1] + arr[p2];

  if (Math.abs(curValue) < Math.abs(zeroValue)) {
    zeroValue = curValue;
    answer = [arr[p1], arr[p2]];
  }

  if (curValue > 0) {
    p2--;
  } else if (curValue < 0) {
    p1++;
  } else {
    break; // 0이면 가장 가까운 값이므로 종료
  }
}

console.log(answer[0], answer[1]);
