let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
input = input.splice(1).map((i) => i.split(' ').map(Number));

let map = Array.from({ length: 100 }, (v, i) => {
  return i + 1;
});

console.log(n, m, input, map);

for (let i = 0; i < n; i++) {
  map[input[i][0] + 1] = input[i][1];
}

console.log(map);
// 사다리와 뱀을 어떻게 처리할 것인가?
// 사다리의 처음 시작점을 끝점으로 처리해버리면
// 그곳으로 이동한 것으로 될것,

// 뱀은 마찬가지로

// 그래프 탐색을 통해 최단거리를 구할거야

// 1~6 가는 경우의 수를 모두 큐에 저장해도 될까?

// i + 1 ~ i + 6
