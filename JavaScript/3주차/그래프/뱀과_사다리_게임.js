let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
input = input.splice(1).map((i) => i.split(' ').map(Number));

console.log(n, m, input);
