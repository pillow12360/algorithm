let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

// console.log(n, m, arr);

// 조합, 순열 두개 동시에 사용

// n개의 조합을 구한후
// // 그 조합의 순열을 출력

// 사전순으로 증가하는 순서 (오름차순 출력해야함) 정렬 시 시간 초과

// n 10,000 이고 1초 n^2 까지 마지노선

/*
위 접근 방법 틀림

1. 순열만 구하면 됨
2. 사전순서를 보장하기 위해 정렬된 arr 전달

*/
function getCombinations(arr, selectNum) {
  let result = [];

  function backtrack(start, temp) {
    if (temp.length === selectNum) {
      result.push([...temp]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(i + 1, temp);
      temp.pop();
    }
  }

  backtrack(0, []);
  return result;
}

function getPermutations(arr, selectNum) {
  const result = [];
  const visited = Array.from({ length: arr.length }).fill(false);

  function backtrack(temp) {
    if (temp.length === selectNum) {
      result.push([...temp]);
      console.log(temp.join(' '));
      return;
    }

    for (let i = arr.length - 1; i >= 0; i--) {
      if (visited[i]) continue;
      visited[i] = true;
      temp.push(arr[i]);
      backtrack(temp);
      temp.pop();
      visited[i] = false;
    }
  }

  backtrack([]);
  return result;
}

let comb = getCombinations(arr, n);
let permu = getPermutations(comb[0], m);

// console.log(permu);
