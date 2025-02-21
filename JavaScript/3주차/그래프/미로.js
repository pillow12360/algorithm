let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input.shift().split(' ').map(Number);
let graph = input.map((i) => i.split('').map(Number));

let visited = Array.from({ length: n }, () => Array(m).fill(false));

// console.log(n, m, graph, visited);

function isRange(r, c) {
  return 0 <= r && r < n && 0 <= c && c < m;
}
let c_r,
  c_c = 0;
let n_r,
  n_c = 0;

let dr = [1, -1, 0, 0];
let dc = [0, 0, -1, 1]; // 상하좌우

function bfs(r, c) {
  let q = [[0, 0]];
  visited[0][0] = true;

  while (q.length > 0) {
    [c_r, c_c] = q.shift();

    for (let i = 0; i < 4; i++) {
      n_r = c_r + dr[i];
      n_c = c_c + dc[i];

      if (isRange(n_r, n_c)) {
        if (!visited[n_r][n_c] && graph[n_r][n_c] === 1) {
          q.push([n_r, n_c]);
          visited[n_r][n_c] = true;
          graph[n_r][n_c] += graph[c_r][c_c];
        }
      }
    }
  }
}

bfs(0, 0);

console.log(graph[n - 1][m - 1]);
