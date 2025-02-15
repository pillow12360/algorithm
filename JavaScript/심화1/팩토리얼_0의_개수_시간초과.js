let fs = require('fs');
let input = fs.readFileSync('io.txt').toString();
let n = +input;

if (n === 0) {
  console.log(0);
  process.exit();
}

function facto(n) {
  if (n === 1) {
    return 1;
  }
  return n * facto(n - 1);
}

let fac = facto(n);

fac = String(fac);
fac = fac.split('');

let i = fac.length - 1;
let answer = 0;

while (i > 0) {
  if (fac[i] === '0') {
    answer++;
  } else {
    break;
  }
  i--;
}

console.log(answer);
