const fs = require('fs');
const input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number);
let words = input.slice(1);

let bitmask = 0b0000; // 초기값: 0 (0000)
bitmask |= 1 << 2; // 3번째 비트를 켜기
console.log(bitmask.toString(2)); // "100"

let wordMasks = words.map((word) => {
  let mask = 0;
  for (let char of word) {
    mask |= 1 << (char.charCodeAt(0) - 97);
  }
  return mask;
});

// K가 5 미만이면 기본 문자("antic")도 못 배우므로 0 출력
if (K < 5) {
  console.log(0);
  process.exit();
}

// 만약 K == 26이면 모든 알파벳을 배울 수 있으므로 전체 단어 개수 출력
if (K == 26) {
  console.log(N);
  process.exit();
}
