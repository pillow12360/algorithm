let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n').map(Number);

function Combinations(arr, n) {
  const result = [];

  function backtrack(temp, start) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(temp, i + 1);
      temp.pop();
    }
  }
  backtrack([], 0);

  return result;
}

let combi = Combinations(input, 7);

// console.log(combi);

for (let a of combi) {
  if (a.reduce((sum, v) => sum + v, 0) === 100) {
    // a.sort((x, y) => x - y);
    a.forEach((num) => console.log(num));
    process.exit(0);
  }
}
