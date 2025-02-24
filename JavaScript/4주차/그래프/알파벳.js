/*
지났던 모든 알파벳을 지날 수 없다.

해시 테이블 Map을 이용하여 O(1)의 접근으로 지나갈 수 있는지 판별 하기

지나갈 수 있으면 큐에 푸시 후 Map에 set 메서드로 추가하기
has 가 true 일 경우 큐에 넣지 않음

bfs 종료 후 max 값을 출력

max 값을 출력하지 말고 bfs 가 종료 일 때 지나간 횟수를 카운트 한것을 출력하기
+ 알파벳 개수는 26이므로 26 이상 가는것은 불가능 -> 26 출력 후 프로그램 종료

-> 접근 실패


*/

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [R, C] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(''));

let visited = Array.from({ length: R }, (i) =>
  Array.from({ length: C }).fill(false)
);

let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];

let dic = new Map();

dic.set(map[0][0], 1);
visited[0][0] = true;

console.log(dic);

const q = [[0, 0, 1]]; // 좌측 상단도 포함
let c_c = 0;
let c_r = 0;
let c_time = 1;

function isRange(r, c) {
  return 0 <= r && r < R && 0 <= c && c < C;
}

while (q.length && time <= 26) {
  [c_r, c_c, c_time] = q.shift();

  for (let i = 0; i < 4; i++) {
    n_r = c_r + dr[i];
    n_c = c_c + dc[i];

    if (isRange(n_r, n_c)) {
      if (dic.has(map[n_r][n_c]) && !visited[n_r][n_c]) {
        visited[n_r][n_c] = true;
        dic.set(map[n_r][n_c], 1);
        q.push([n_r, n_c, time + 1]);
      }
    }
  }
}

console.log(map);
