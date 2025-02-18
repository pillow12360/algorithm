let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('');

let upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
let lower = 'abcdefghijklmnopqrstuvwxyz';

// 공백도 string
// 숫자도 string

// 공백 및 숫자면 13뒤로 이동 하지말기

function isUpperCase(char) {
  return char === char.toUpperCase();
}

function isLowerCase(char) {
  return char === char.toLowerCase();
}

function isNumber(char) {
  return !isNaN(char);
}

input = input.map((v) => {
  if (isNumber(v)) {
    return v;
  } else if (isUpperCase(v)) {
    return upper[(upper.indexOf(v) + 13) % 26];
  } else if (isLowerCase(v)) {
    return lower[(lower.indexOf(v) + 13) % 26];
  } else {
    return v;
  }
});

console.log(input.join(''));
