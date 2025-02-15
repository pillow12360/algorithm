let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [a, b, c] = input.map(Number);
let [as, bs, cs] = input;
console.log(a + b - c);
console.log(as + bs - cs);
