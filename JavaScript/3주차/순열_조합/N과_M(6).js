let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);
// console.log(n, m, arr);

arr.sort((a, b) => a - b);

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
      if (temp[temp.length - 1] > arr[i]) continue;
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
