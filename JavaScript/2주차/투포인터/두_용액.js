let fs = require('fs');

let input = fs.readFileSync('io.txt').toString().split('\n');

let n = Number(input[0]);

let arr = input[1].split(' ').map(Number);

arr.sort((a, b) => a - b);
// console.log(arr);
zeroValue = Infinity;

let answer = new Map();
let curValue = 0;
let p1 = 0;
let p2 = arr.length - 1;

while (p1 < p2) {
  curValue = arr[p1] + arr[p2];

  if (curValue === 0) {
    answer.set('p1', arr[p1]);
    answer.set('p2', arr[p2]);
    break;
  }

  if (Math.abs(curValue) < Math.abs(zeroValue)) {
    zeroValue = Math.abs(curValue);
    answer.set('p1', arr[p1]);
    answer.set('p2', arr[p2]);
  }

  if (curValue > 0) {
    p2--;
  } else {
    p1++;
  }
}

console.log(`${answer.get('p1')} ${answer.get('p2')}`);
