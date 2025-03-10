let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');
let n = +input[0];
let nums = input[1].split(' ').map(Number);

nums = nums.filter((i) => {
  if (i === 1) return false;
  let yack = [];
  for (let num = 1; num <= i; num++) {
    if (i % num === 0) {
      yack.push(num);
    }
  }
  return yack.length < 3 ? true : false;
});

console.log(nums.length);
