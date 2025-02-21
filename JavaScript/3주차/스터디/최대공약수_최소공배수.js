let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split(' ').map(Number);

let [a, b] = input;
let a1 = a;
let b1 = b;

// console.log(a, b);

let gcd = 0;
let c = 0;
let temp = 0;

while (a % b !== 0) {
  temp = b;
  c = a % b;
  a = b;
  b = c;
}

gcd = b;

let lcd = (a1 * b1) / b;

console.log(gcd);
console.log(lcd);
