let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = Number(input[0]);
if (n <= 5) {
  console.log('PREDAJA');
  process.exit();
}
let sunsoo = input.slice(1);
// console.log(sunsoo);

let first = sunsoo.map((i) => i[0]);
// console.log(first);

let answer = [];

first.forEach((a) => {
  if (first.filter((i) => i === a).length >= 5) {
    answer.push(a);
  }
});
answer = new Set(answer);
answer = [...answer];
if (answer.length === 0) {
  console.log('PREDAJA');
} else {
  answer = answer.sort((a, b) => a - b);
  console.log(answer.join(''));
}
