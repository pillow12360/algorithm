let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [n, m] = input.shift().split(' ').map(Number);
let map = input.map((i) => i.replace(/\r/g, '').split(''));
let visited = Array.from({ length: n }, () => Array(m).fill(false));

// console.log(visited);
// console.log(n, m, map);

let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];
let cur_r = 0;
let cur_c = 0;
let q = [];
let start_r = 0;
let start_c = 0;
let cnt = 0;

function is_range(r, c) {
  return 0 <= r && r < n && 0 <= c && c < m;
}

// 헌내기 위치
for (let i = 0; i < n; i++) {
  for (let j = 0; j < m; j++) {
    if (map[i][j] === 'I') {
      start_r = i;
      start_c = j;
    }
  }
}

q.push([start_r, start_c]);

while (q.length > 0) {
  [cur_r, cur_c] = q.shift();

  if (map[cur_r][cur_c] === 'P') {
    cnt++;
  }

  for (let i = 0; i < 4; i++) {
    let next_r = cur_r + dr[i];
    let next_c = cur_c + dc[i];

    if (is_range(next_r, next_c)) {
      if (map[next_r][next_c] !== 'X') {
        if (visited[next_r][next_c] != true) {
          visited[next_r][next_c] = true;
          q.push([next_r, next_c]);
        }
      }
    }
  }
}

console.log(cnt === 0 ? 'TT' : cnt);
