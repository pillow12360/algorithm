let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [m, n, h] = input.shift().split(' ').map(Number);
let tomato = [];
let queue = [];
let unripeCount = 0;

// 3차원 배열로 변환
for (let k = 0; k < h; k++) {
  let layer = [];
  for (let i = 0; i < n; i++) {
    let row = input.shift().split(' ').map(Number);
    layer.push(row);
    for (let j = 0; j < m; j++) {
      if (row[j] === 1) {
        queue.push([k, i, j, 0]); // 익은 토마토를 초기 큐에 추가
      } else if (row[j] === 0) {
        unripeCount++;
      }
    }
  }
  tomato.push(layer);
}

// 방향 벡터 (상, 하, 좌, 우, 위층, 아래층)
let dz = [-1, 1, 0, 0, 0, 0];
let dx = [0, 0, -1, 1, 0, 0];
let dy = [0, 0, 0, 0, -1, 1];

let maxDay = 0;
let front = 0; // 큐에서 꺼낼 위치를 나타내는 포인터

// BFS
while (front < queue.length) {
  let [z, x, y, day] = queue[front++];
  maxDay = ㅋ(maxDay, day);

  for (let i = 0; i < 6; i++) {
    let nz = z + dz[i];
    let nx = x + dx[i];
    let ny = y + dy[i];

    if (nz >= 0 && nz < h && nx >= 0 && nx < n && ny >= 0 && ny < m) {
      if (tomato[nz][nx][ny] === 0) {
        tomato[nz][nx][ny] = 1;
        unripeCount--;
        queue.push([nz, nx, ny, day + 1]);
      }
    }
  }
}

// 결과 출력
console.log(unripeCount === 0 ? maxDay : -1);
