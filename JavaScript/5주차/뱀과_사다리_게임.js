let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');
let [n, m] = input[0].split(' ').map(Number);
let arr = input.slice(1).map((i) => i.split(' ').map(Number));

const map = new Map();
for (let i = 1; i <= 100; i++) {
  map.set(i, i); // 뱀 및 사다리가 아니여도 상관없도록 자기 자신을 세팅
}
// 사다리와 뱀 정보 저장
for (let [start, end] of arr) {
  map.set(start, end);
}

// console.log(arr, map);

const q = [[1, 0]];
const visited = new Set();
visited.add(1);

while (q.length) {
  const [pos, moves] = q.shift();
  if (pos === 100) {
    console.log(moves);
    break;
  }

  for (let dice = 1; dice <= 6; dice++) {
    let nextPos = pos + dice;
    if (nextPos <= 100) {
      nextPos = map.get(nextPos); // 뱀/사다리 적용 후 이동
      if (!visited.has(nextPos)) {
        visited.add(nextPos);
        q.push([nextPos, moves + 1]);
      }
    }
  }
}
