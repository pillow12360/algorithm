let fs = require('fs');
let input = fs.readFileSync(0, 'utf-8').trim().split('\n').map(Number).slice(1);

console.log(
  input
    .sort((a, b) => a - b)
    .join('\n')
    .trim()
);
