let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n').map(Number);

// console.log(input);

let result = input.reduce((acc, cur) => acc * cur, 1);
