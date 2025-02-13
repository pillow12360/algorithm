let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, k] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

let maxVal = 0;

let window = arr.slice(0, k).reduce((arr, cur) => (arr += cur));
maxVal = window;

for (let i = 0; i < n - k; i++) {
  window -= arr[i];
  window += arr[i + k];
  maxVal = Math.max(window, maxVal);
}
console.log(maxVal);
