let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = input.shift();
let arr = input.map((i) => i.split(' ').map(Number));

console.log(n, arr);

arr = arr.map((a) => {
  return a.sort((a, b) => a - b);
});

console.log(arr);

// n은 N(1 ≤ N ≤ 1,500)
