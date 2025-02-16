let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split(' ');

let n = +input[0];
let k = +input[1];

let person = Array.from({ length: n }, (v, i) => n - i);

console.log(person);
let answer = [];
let cnt = 0;

while (person.length !== 0) {
  cnt++;
  let cur = person.pop();

  if (cnt === k) {
    answer.push(cur);
    cnt = 0;
  } else {
    person = [cur, ...person];
  }
}

console.log(`<${answer.join(', ')}>`);
