let fs = require('fs');
let [a, b, c] = fs.readFileSync('io.txt').toString().split(' ').map(Number);
// console.log(a, b, c);

function modExp(a, b, c) {
  if (b === 0) return 1;
  let half = modExp(a, Math.floor(b / 2), c);
  let result = (half * half) % c;
  if (b % 2 === 1) {
    result = (result * a) % c;
  }
  return result;
}

console.log(modExp(a, b, c));
