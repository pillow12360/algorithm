let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [m, n, h] = input.shift().split(' ').map(Number);
let tomato = input.map((i) => i.split(' ').map(Number));
// console.log(n, m, h, tomato);

// 3차원 그래프
// 위, 아래, 왼쪽, 오른쪽, 앞, 뒤
// 하루 뒤

// -1 빈 곳
// 0 안익은 토마토
// 1 익은 토마토

// 모두 익지 못하는 상황 -> 1익은토마토가 -1로 가로 막혀 있을경우 -1 출력

//

//일단 모두 익어있는 상태면 0 출력
let set = new Set();
set.add(tomato);

// for (let i of tomato) {
//   for (let j of i) {
//     set.add(j);
//   }
// }

// console.log(set);

// if (!set.has(0) && set.size() === 2) {
//   console.log(0);
//   process.exit();
// }

/*
// 위 ->+n
// 아래 -> -n
*/

function isRage(c_r, c_c) {
  if (h < c_r) {
    c_h = Math.floor((n * h) / c_r);
  }
  return n - c_h <= c_r && c_r < c_h + n && 0 <= c_c && c_c < m;
}

visited = Array.from({ length: n }, () =>
  Array.from({ length: m }).fill(false)
);

for (let i = 0; i < h - 1; i++) {
  visited = [...visited, ...visited];
}

console.log(visited);

let dr = [-1, 1, 0, 0, n, -n]; // 위 상자 아래 상자 이동 추가
let dc = [0, 0, -1, 1, 0, 0];
let day = 0;

function bfs(r, c, h) {
  let q = [[r, c]];

  while (q.length > 0) {
    let [c_r, c_c] = q.shift();
    day += 1;

    for (let i = 0; i < 4; i++) {
      n_r = c_r + dr[i];
      n_c = c_c + dc[i];
      if (isRage(n_r, n_c, h)) {
        if (
          !visited[n_r][n_c] &&
          tomato[n_r][n_c] !== -1 &&
          tomato[n_r][n_c] === 0
        ) {
          tomato[n_r][n_c] = day;
          visited[n_r][n_c] = true;
          q.push([n_r, n_c]);
        }
      }
    }
  }
}

let wellto = [];

console.log(tomato);

for (let i = 0; i < n * h; i++) {
  for (let j = 0; j < m * h; j++) {
    if (tomato[i][j] === 1) {
      c_h = Math.floor(i / h);
      wellto.push([i, j, c_h]);
    }
  }
}

console.log(wellto);

while (wellto.length) {
  let [cur_r, cur_c] = wellto.shift();
  bfs(cur_r, cur_c);
}

console.log(tomato);
console.log(visited);
