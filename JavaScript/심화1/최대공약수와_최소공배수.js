let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split(' ');

a1 = Number(input[0]);
b1 = Number(input[1]);

b = b1;
a = a1;

while (b !== 0) {
  let r = a % b;
  a = b;
  b = r;
}

lcm = (a1 * b1) / a;

console.log(a + ' ' + lcm);
