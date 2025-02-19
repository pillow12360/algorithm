let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, k] = input.shift().split(' ').map(Number);
let word = input;

// antic 는 무조건 배워야해

let base_mask =
  (1 << ('a'.charCodeAt(0) - 97)) |
  (1 << ('n'.charCodeAt(0) - 97)) |
  (1 << ('t'.charCodeAt(0) - 97)) |
  (1 << ('i'.charCodeAt(0) - 97)) |
  (1 << ('c'.charCodeAt(0) - 97));

console.log(base_mask.toString(2).padEnd(26, '0'));

let wordMasks = word.map((a) => {
  let result = 0;
  for (let i of a) {
    result |= 1 << (i.charCodeAt(0) - 97);
  }
  return result;
});

console.log(wordMasks);
