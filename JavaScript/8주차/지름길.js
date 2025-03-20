let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, d] = input[0].split(' ').map(Number);

let short = input.slice(1).map((i) => i.split(' ').map(Number));
let distance = Array(d + 1).fill(Infinity);
distance[0] = 0;

// console.log(n, d, short);

let load = new Map();

for (let i = 0; i <= d; i++) {
  load.set(i, [[i + 1, 1]]);
}

short = short.sort((a, b) => a[1] - a[0] - a[2] - (b[1] - b[0] - b[2]));

// console.log(short);
for (let [start, end, cost] of short) {
  if (end <= d) {
    // 도로 범위를 넘지 않는 경우만 추가
    if (!load.has(start)) {
      load.set(start, []);
    }
    load.get(start).push([end, cost]); // start → end 지름길 추가
  }
}

// console.log(load);
let queue = [[0, 0]]; // [현재 위치, 현재까지 거리]

while (queue.length) {
  let [pos, curDist] = queue.shift();

  if (pos > d) continue; // 도로 범위 초과 시 종료
  if (curDist > distance[pos]) continue; // 기존 최단 거리보다 크면 무시

  // 현재 위치에서 이동할 수 있는 모든 경로 탐색
  for (let [nextPos, cost] of load.get(pos) || []) {
    let newDist = curDist + cost;
    if (newDist < distance[nextPos]) {
      distance[nextPos] = newDist;
      queue.push([nextPos, newDist]);
    }
  }
}

// 출력
console.log(distance[d]);
