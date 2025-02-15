let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = Number(input[0]);
let arr = input[1].split(' ').map(Number);
let x = Number(input[2]);

arr.sort((a, b) => a - b);

// console.log(arr);

answer = 0;

let p1 = 0;
let p2 = arr.length - 1;

while (p1 !== p2) {
  // 두 포인터가 만나면 종료

  let result = arr[p1] + arr[p2];

  if (result === x) {
    answer++;
    p1++;
    continue;
  } else {
    if (result > x) {
      p2--;
    } else {
      p1++;
    }
  }
}

console.log(answer);
