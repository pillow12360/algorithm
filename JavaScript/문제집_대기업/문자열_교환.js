let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('');

n = input.length;
n2 = [...input, ...input];

let cntA = input.filter((a) => a === 'a').length;

let curBCount = [...n2.slice(0, cntA)].filter((a) => a === 'b').length;
let minSwap = curBCount;

for (let i = 0; i < n; i++) {
  if (n2[i] === 'b') curBCount--;
  if (n2[i + cntA] === 'b') curBCount++;
  minSwap = Math.min(minSwap, curBCount);
}

console.log(minSwap);
