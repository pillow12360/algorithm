let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let tops = input[1]
  .split(' ')
  .map(Number)
  .map((cur, index) => [index + 1, cur]);

console.log(tops);
let stack = [];
let answer = [];

for (let i = 0; i < tops.length - 2; i++) {
  let cur_i = tops[i][0];
  let cur_v = tops[i][1];
  stack.push(cur_v);

  for (let j = i + 1; j <= tops.length - 2; j++) {
    let next_v = tops[j][1];

    if (next_v > cur_v) {
      stack.pop();
      if (stack.length === 0) {
        answer.push(0);
        break;
      } else {
        answer.push(cur_i);
        break;
      }
    } else {
      stack.push(next_v);
    }
  }
}

console.log(answer.join(' '));
