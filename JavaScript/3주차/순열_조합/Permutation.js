let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

function Permutation(arr, n) {
  result = [];
  visited = Array(arr.length).fill(false);

  function backtrack(temp) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    let used = new Set();

    for (let i = 0; i < n; i++) {
      if (visited[i] || used.has(arr[i])) continue;

      visited[i] = true;
      temp.push(arr[i]);
      used.add(arr[i]);
      backtrack(temp);
      temp.pop();
      visited[i] = false;
    }
  }

  backtrack([]);

  return result;
}

console.log(Permutation(arr, m));
