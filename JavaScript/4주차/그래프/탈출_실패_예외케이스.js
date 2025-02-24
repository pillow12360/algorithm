/*
물 *
돌 X
비어있음 .

비버  D
고슴도치 S

S -> D 최단거리
*/

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [R, C] = input[0].split(' ');
let map = input.slice(1).map((i) => i.split(''));
let visited = Array.from({ length: R }, (i) =>
  Array.from({ length: C }).fill(false)
);
let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];

// 물의 경로와 고슴도치의 경로 모두를 구해야해

// 비어있는칸 -> 물이 찰 수 있는 칸

// 물의 경로를 먼저 구한 후 고슴도치의 경로를 구해야지

function isRange(r, c) {
  return 0 <= r && r < R && 0 <= c && c < C;
}

function water(waterQ) {
  let day = 1;
  let q = waterQ;
  let c_r = 0;
  let c_c = 0;
  while (q.length) {
    [c_r, c_c, day] = q.shift();

    for (let i = 0; i < 4; i++) {
      n_r = c_r + dr[i];
      n_c = c_c + dc[i];

      if (isRange(n_r, n_c)) {
        if (map[n_r][n_c] === '.') {
          q.push([n_r, n_c, day + 1]);
          map[n_r][n_c] = day;
        }
      }
    }
  }
}

let waterQ = [];
let answer_r = 0;
let answer_c = 0;
let s_r = 0;
let s_c = 0;

for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    if (map[i][j] === '*') {
      waterQ.push([i, j, 1]);
    } else if (map[i][j] === 'D') {
      answer_r = i;
      answer_c = j;
    } else if (map[i][j] === 'S') {
      s_r = i;
      s_c = j;
    }
  }
}

water(waterQ);

// console.log(map);

function goseam(r, c) {
  let day = 0;
  let q = [[r, c, day]];
  let c_r = 0;
  let c_c = 0;
  visited[r][c] = true;

  while (q.length) {
    [c_r, c_c, day] = q.shift();

    for (let i = 0; i < 4; i++) {
      n_r = c_r + dr[i];
      n_c = c_c + dc[i];

      if (isRange(n_r, n_c) && !visited[n_r][n_c]) {
        if (map[n_r][n_c] === 'D') {
          console.log(day + 1);
          process.exit();
        } else if (map[n_r][n_c] !== '*' && map[n_r][n_c] > day + 1) {
          q.push([n_r, n_c, day + 1]);
          visited[n_r][n_c] = true;
          map[n_r][n_c] = day + 1;
        }
      }
    }
  }
}

goseam(s_r, s_c);

console.log('KAKTUS');
// console.log(map);

// map[answer_r][answer_c] === 'D'
//   ? console.log('KAKTUS')
//   : console.log(map[answer_r][answer_c]);
