let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('');

const Combinatorics = require('js-combinatorics');

const elements = [...input];

const cmb = Combinatorics.combination(elements, 7);
const combinations = [...cmb];

console.log(combinations);
