let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let t = +input.shift() * 3;
let answer = [];

let dr = [-2, -1, 1, 2, 2, 1, -1, -2]; // 나이트의 이동 경로
let dc = [1, 2, 2, 1, -1, -2, -2, -1];

function is_range(r, c, l) {
  return 0 <= r && r < l && 0 <= c && c < l;
}

function bfs(start_r, start_c, target_r, target_c, l) {
  if (start_r === target_r && start_c === target_c) {
    answer.push(0);
    return;
  }

  let visited = Array.from({ length: l }, () => Array(l).fill(false));

  let q = [];
  let moves = 0;
  q.push([start_r, start_c, moves]);

  while (q.length) {
    let [cur_r, cur_c, cur_moves] = q.shift();

    for (let i = 0; i < 8; i++) {
      let n_r = cur_r + dr[i];
      let n_c = cur_c + dc[i];

      if (is_range(n_r, n_c, l) && !visited[n_r][n_c]) {
        if (n_r === target_r && n_c === target_c) {
          answer.push(cur_moves + 1);
          return;
        } else {
          q.push([n_r, n_c, cur_moves + 1]);
          visited[n_r][n_c] = true;
        }
      }
    }
  }
}

for (let c = 0; c < t; c += 3) {
  l = input[c];

  let [start_r, start_c] = input[c + 1].split(' ').map(Number);
  let [target_r, target_c] = input[c + 2].split(' ').map(Number);

  bfs(start_r, start_c, target_r, target_c, l);
}

console.log(answer.join('\n'));
