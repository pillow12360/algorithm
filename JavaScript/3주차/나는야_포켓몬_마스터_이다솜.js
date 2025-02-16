let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let pocketmon = input.slice(1, n + 1);
let k = input.slice(n + 1);

k = k.map((i) => {
  return !isNaN(i) && typeof i === 'string' ? Number(i) : i;
});

pocketmon = pocketmon.map((v, i) => [v, i + 1]);
let pocketmonMap = new Map(pocketmon);

// console.log(pocketmon);

for (let cur of k) {
  typeof cur === 'number'
    ? console.log(pocketmon[cur - 1][0])
    : console.log(pocketmonMap.get(cur));
}
