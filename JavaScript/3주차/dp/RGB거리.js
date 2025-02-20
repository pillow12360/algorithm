let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');
let n = Number(input.shift());
let arr = input.map((i) => i.split(' ').map(Number));

const dp = Array.from({ length: n }, () => Array(3).fill(-1));

// rgb(n, color) = 현재 컬러를 선택 하였을 때 집을 1번부터 n번까지 칠하는데 드는 최소 비용을 구한것

function rgb(i, color) {
  if (i < 0) return 0;
  if (n === 0) return arr[0][color];
  if (dp[i][color] !== -1) return dp[i][color]; // 이미 계산된 값이면 반환

  if (color === 0) {
    dp[i][0] = arr[i][0] + Math.min(rgb(i - 1, 1), rgb(i - 1, 2));
  } else if (color === 1) {
    dp[i][1] = arr[i][1] + Math.min(rgb(i - 1, 0), rgb(i - 1, 2));
  } else {
    dp[i][2] = arr[i][2] + Math.min(rgb(i - 1, 0), rgb(i - 1, 1));
  }

  return dp[i][color];
}

console.log(Math.min(rgb(n - 1, 0), rgb(n - 1, 1), rgb(n - 1, 2)));
