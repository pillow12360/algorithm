let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = input[0];
let arr = input
  .slice(1)
  .map((i) => i.split(' '))
  .map((i) => [i[0], +i[1]]);

let cur = [];
let answer = new Set();
let all = Array.from({ length: 20 }).map((_, i) => i + 1);

while (arr.length > 1) {
  cur = arr.splice(0, 1)[0];

  if (cur[0] === 'add') {
    answer.add(cur[1]);
  } else if (cur[0] === 'remove') {
    answer.delete(cur[1]);
  } else if (cur[0] === 'toggle') {
    if (answer.has(cur[1]) === true) {
      answer.delete(cur[1]);
    } else {
      answer.add(cur[1]);
    }
  } else if (cur[0] === 'all') {
    answer = new Set(all);
  } else if (cur[0] === 'empty') {
    answer = new Set();
  } else if (cur[0] === 'check') {
    console.log(answer.has(cur[1]) ? 1 : 0);
  }
}
