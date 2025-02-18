let fs = require('fs');

let input = fs.readFileSync('io.txt').toString().split('\n');

let n = Number(input.shift());
let food = input.map((i) => i.split(' ').map(Number));

// console.log(`food : `, food);
// 모든 재료를 사용하여 요리
// 각 요리에 사용할 재료 수 는 상관없다.

// 일단 전체를 사용하는 경우의 수의 차이를 구해

// maxM = Math.abs(s - b);

// n요소 조합 백트래킹
function combi(arr, n) {
  const result = [];

  function backtrack(temp, start) {
    if (temp.length === n) {
      result.push([...temp]); // 원본 데이터 그대로 저장
      return;
    }

    for (let i = start; i < arr.length; i++) {
      backtrack([...temp, arr[i]], i + 1); // 원본 데이터 저장
    }
  }

  backtrack([], 0);
  return result;
}

let minM = Infinity;
// 1개부터 n개까지의 모든 조합
for (let i = 1; i <= n; i++) {
  let cur = combi(food, i);
  // console.log(`cur : `, cur);

  // 각 조합의 쓴맛 신맛의 차 구해
  for (let i of cur) {
    let cur_s = 1;
    let cur_b = 0;

    for (let ingredient of recipe) {
      cur_s *= ingredient[0]; // 신맛 곱하기
      cur_b += ingredient[1]; // 쓴맛 더하기
    }

    let curM = Math.abs(cur_s - cur_b);
    minM = Math.min(curM, minM);
  }
}

console.log(minM);
