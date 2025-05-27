let fs = require('fs');
let input = fs.readFileSync(0, 'utf-8').trim().split('\n').map(Number);

// console.log(input);

let result = input.reduce((acc, cur) => acc * cur, 1);

// console.log(result);

result = String(result);

let arr = result.split('').map(Number);

// console.log(arr);

let answer = new Map();

for (let i of arr) {
  if (answer.has(i)) {
    answer.set(i, answer.get(i) + 1);
  } else {
    answer.set(i, 1);
  }
}

// console.log(answer);

for (let i = 0; i < 10; i++) {
  if (answer.has(i)) {
    console.log(answer.get(i));
  } else {
    console.log(0);
  }
}
