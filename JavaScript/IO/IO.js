let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split(' ');

let n1 = parseInt(input[0]);

console.log(n1);

console.log(Number(input[0]) + Number(input[1]));
