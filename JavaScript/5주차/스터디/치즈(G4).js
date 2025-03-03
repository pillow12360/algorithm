let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(' ').map(Number));

console.log(n, m, map);

let dr = [-1, 1, 0, 0, -1, 1, 1, 1];
let dc = [0, 0, -1, 1, -1, 1, -1, 1]; // 상하좌우 + 좌상, 우상, 좌하, 우하

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
let day = 1;

function bfs(r, c) {
  if (!is_fuze(r, c)) return false;
  let num = 1;
  let q = [[r, c, num]];
  let visited = Array.from({ length: n }, () => Array(m).fill(false));
  visited[r][c] = true;
  map[r][c] = 0;

  while (q.length) {
    let [c_r, c_c, c_num] = q.shift();

    for (let i = 0; i < 4; i++) {
      let n_r = c_r + dr[i];
      let n_c = c_c + dc[i];

      if (
        is_range(n_r, n_c) &&
        !visited[n_r][n_c] &&
        map[n_r][n_c] === 1 &&
        is_fuze(n_r, n_c)
      ) {
        map[n_r][n_c] = 0;
        visited[n_r][n_c] = true;
        num++;
        q.push([n_r, n_c]);
      }
    }
  }
  return num;
}
let answer = 0;
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (map[i][j] === 1) {
      answer = bfs(i, j);
      day++;
    }
  }
}

console.log(day);
console.log(answer);
