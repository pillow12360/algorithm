`
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
`;

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

input = input.map(Number);

t = input[0];
input.shift();
// console.log(input);

// dp = [];
// dp[0] = (1, 0);
// dp[1] = (0, 1);
// dp[2] = (1, 1);
// dp[3] = (1, 2);
// dp[4] = (2, 3);

for (let cur = 0; cur < t; cur++) {
  let n = input[cur]; // 현재 테스트 케이스의 n 값

  // DP 배열 초기화 (각 요소는 [0, 0] 형태)
  let dp = new Array(n + 1).fill(null).map(() => [0, 0]);

  // 초기값 설정
  dp[0] = [1, 0];
  if (n > 0) dp[1] = [0, 1];

  // DP 테이블 채우기
  for (let i = 2; i <= n; i++) {
    dp[i] = [
      dp[i - 1][0] + dp[i - 2][0], // 0이 호출된 횟수
      dp[i - 1][1] + dp[i - 2][1], // 1이 호출된 횟수
    ];
  }
  console.log(dp[n][0] + ' ' + dp[n][1]);
}
