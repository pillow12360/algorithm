let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

// arr 정렬
arr.sort((a, b) => a - b);

function getPermutations(arr, n) {
  let visited = Array(arr.length).fill(false);

  function backtrack(temp) {
    if (temp.length === n) {
      console.log(temp.join(' '));
      return;
    }

    let used = new Set();

    for (let i = 0; i < arr.length; i++) {
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
}

getPermutations(arr, m);
