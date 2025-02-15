let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim();

let num = Number(input);

let answer = [];
let answerNum = 0;

function hanoi(n, start, target, temp) {
  if (n === 1) {
    answerNum++;
    answer.push(`${start} ${target}`);
    return;
  }

  hanoi(n - 1, start, temp, target);
  answer.push(`${start} ${target}`);
  answerNum++;
  hanoi(n - 1, temp, target, start);
}

hanoi(num, 1, 3, 2);
console.log(answerNum);
console.log(answer.join('\n'));
