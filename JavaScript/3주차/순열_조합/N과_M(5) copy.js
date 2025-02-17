let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

// 사전순 정렬
arr.sort((a, b) => a - b);

function getPermutations(arr, selectNum) {
  let result = [];
  let visited = Array(arr.length).fill(false);

  function backtrack(temp) {
    if (temp.length === selectNum) {
      console.log(temp.join(' ')); // 즉시 출력
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (visited[i]) continue;
      visited[i] = true;
      temp.push(arr[i]);
      backtrack(temp);
      temp.pop();
      visited[i] = false;
    }
  }

  backtrack([]);
}

// 사전순 출력을 위해 정렬된 arr를 전달
getPermutations(arr, m);
