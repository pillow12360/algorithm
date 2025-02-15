let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

n = +input[0];
inputNum = input[1].split(' ').map(Number);

function ocen(nums) {
  let maxNum = 0;
  let stack = [];

  for (let num of nums) {
    // while() {

    // }

    if (stack.length === 0) {
      process.stdin.write(stack[0]);
    } else {
      process.stdin.write(-1);
    }
  }
}
