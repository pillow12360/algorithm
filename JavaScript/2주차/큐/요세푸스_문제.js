let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split(' ');
let [n, k] = input.map(Number);

let circle = new Array(n).fill(0);
let answer = [];
let cnt = 0;

circle = circle.map((_, i) => {
  return i + 1;
});
