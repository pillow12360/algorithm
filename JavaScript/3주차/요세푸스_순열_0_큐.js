const fs = require('fs');
const input = fs.readFileSync('io.txt').toString().split(' ');

const N = +input[0];
const K = +input[1];

const queue = Array.from({ length: N }, (_, i) => i + 1); // 1~N 배열 생성
const result = [];

let index = 0;

while (queue.length) {
  index = (index + K - 1) % queue.length; // 제거할 인덱스 찾기
  result.push(queue.splice(index, 1)[0]); // O(1) (사실상 O(N) 안됨)
}

// splice 원본 배열 변경 splice(시작 인덱스, 자를 요소 개수, 추가할 요소)
// slice 원본 배열 변경 안함

console.log(`<${result.join(', ')}>`); // 정답 출력
