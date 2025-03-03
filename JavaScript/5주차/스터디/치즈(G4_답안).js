let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(' ').map(Number));

let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];

function is_range(r, c) {
  return 0 <= r && r < n && 0 <= c && c < m;
}

function is_fuze(r, c) {
  for (let i = 0; i < 4; i++) {
    let n_r = r + dr[i];
    let n_c = c + dc[i];

    if (is_range(n_r, n_c) && map[n_r][n_c] === 0) {
      return true;
    }
  }
  return false;
}

// 치즈가 모두 녹을 때까지 BFS 실행
let day = 0;
let last_cheese = 0;

while (true) {
  let visited = Array.from({ length: n }, () => Array(m).fill(false));
  let melted = 0; // 이번에 녹은 치즈 개수
  let q = [];

  // 가장 바깥 공기를 먼저 탐색하여 큐에 추가
  q.push([0, 0]); // (0, 0)은 항상 외부 공기
  visited[0][0] = true;

  while (q.length) {
    let [r, c] = q.shift();

    for (let i = 0; i < 4; i++) {
      let n_r = r + dr[i];
      let n_c = c + dc[i];

      if (is_range(n_r, n_c) && !visited[n_r][n_c]) {
        if (map[n_r][n_c] === 0) {
          q.push([n_r, n_c]);
        } else if (map[n_r][n_c] === 1) {
          map[n_r][n_c] = 0; // 치즈 녹이기
          melted++; // 녹은 치즈 개수 증가
        }
        visited[n_r][n_c] = true;
      }
    }
  }

  if (melted === 0) break; // 더 이상 녹을 치즈가 없으면 종료

  last_cheese = melted; // 녹기 1시간 전의 치즈 개수 저장
  day++; // 시간 증가
}

console.log(day); // 모든 치즈가 녹는 시간
console.log(last_cheese); // 녹기 한 시간 전에 남아있던 치즈 개수
