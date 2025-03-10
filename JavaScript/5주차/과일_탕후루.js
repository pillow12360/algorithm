let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let N = Number(input[0]);
let S = input[1].split(' ').map(Number);

function maxFruitsTteokbokki(N, S) {
  let left = 0;
  let right = 0;
  let count = new Map();
  let maxLen = 0;

  while (right < N) {
    // 현재 숫자 추가
    count.set(S[right], (count.get(S[right]) || 0) + 1);

    // 과일 종류가 3개 이상이라면, left를 이동하여 2개 이하가 되도록 조정
    while (count.size > 2) {
      count.set(S[left], count.get(S[left]) - 1);
      if (count.get(S[left]) === 0) {
        count.delete(S[left]);
      }
      left++;
    }

    // 최대 길이 갱신
    maxLen = Math.max(maxLen, right - left + 1);

    // 오른쪽 포인터 이동
    right++;
  }

  return maxLen;
}

console.log(maxFruitsTteokbokki(N, S));
