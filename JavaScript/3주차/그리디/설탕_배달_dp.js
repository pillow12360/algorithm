let fs = require('fs');
let input = fs.readFileSync('io.txt').toString();

let n = Number(input);

let dp = Array(n + 1).fill(-1);

// dp[n] = n개무게일때 최소 가지수

/*
dp[0] = -1;
dp[1] = -1;
dp[2] = -1;
dp[3] = 1;
dp[4] = -1;
dp[5] = 1;
dp[6] = 2;
dp[7] = -1;
dp[8] = 2; // 5 + 3
dp[9] = 3;
dp[10] = 2; // 5 + 5
dp[11] = 3;
dp[12] = 4; // 3 + 3 + 3 + 3
dp[13] = 3; // 5 + 5 + 3
*/

// n % 3 === 0 일때
// dp[n] = dp[n - 3] + 1;

// n % 5 === 0 일때
// dp[n] = dp[n - 5] + 1;

dp[0] = 0;
dp[1] = -1;
dp[2] = -1;
dp[3] = 1;
dp[4] = -1;
dp[5] = 1;

for (let i = 6; i <= n; i++) {
  if (dp[i - 3] !== -1 && dp[i - 5] !== -1) {
    dp[i] = Math.min(dp[i - 3], dp[i - 5]) + 1;
  } else if (dp[i - 3] !== -1) {
    dp[i] = dp[i - 3] + 1;
  } else if (dp[i - 5] !== -1) {
    dp[i] = dp[i - 5] + 1;
  }
}

console.log(dp[n]);
