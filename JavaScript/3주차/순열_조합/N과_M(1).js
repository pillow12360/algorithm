let fs = require('fs');
let [n, m] = fs.readFileSync('io.txt').toString().split(' ').map(Number);

let arr = Array(n)
  .fill(0)
  .map((_, i) => i + 1);

console.log(n, m, arr);

function Permutation(arr, n) {
  let visited = Array(arr.length).fill(false);

  function backtrack(temp) {
    if (temp.length === n) {
      console.log(temp.join(' '));
      return;
    }

    let used = new Set();

    for (let i = 0; i < arr.length; i++) {
      if (visited[arr[i]] || used.has(arr[i])) continue;

      visited[arr[i]] = true;
      temp.push(arr[i]);
      used.add(arr[i]);
      backtrack(temp);
      visited[arr[i]] = false;
      temp.pop();
    }
  }

  backtrack([]);
}

Permutation(arr, m);
