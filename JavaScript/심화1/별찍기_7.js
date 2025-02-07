let fs = require('fs');

let input = fs.readFileSync('io.txt').toString().trim();
input = Number(input);

star = 1;
answer = '';

for (let i = 1; i < input; i++) {
  answer += ' '.repeat(input - i);
  answer += '*'.repeat(star) + '\n';
  star += 2;
}

for (let i = input; i > 0; i--) {
  answer += ' '.repeat(input - i);
  answer += '*'.repeat(star) + '\n';
  star -= 2;
}

console.log(answer);
