let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(' ').map(Number));

console.log(n, m, map);

function combi(arr, n) {
  const visited = Array(arr.length).fill(false);
  const result = [];

  function backtrack(temp) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (visited[i]) continue;

      visited[i] = true;
      temp.push(arr[i]);
      backtrack(temp);
      temp.pop();
      visited[i] = false;
    }
  }

  backtrack([]);

  return result;
}

let chiken = [];

for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (map[i][j] === 2) {
      chiken.push([i, j]);
    }
  }
}

// chiken.length - m, 삭제할 치킨집 수
console.log(`현재 치킨집 목록:`, chiken);

let del = combi(chiken, chiken.length - m);
// 삭제할 치킨집들의 조합
console.log(del);

let minValue = Infinity;

del.forEach((combo) => {
  combo.forEach(([x, y]) => {
    map[x][y] = 0;
  });
  minValue = Math.min(len_chiken(map), minValue);
});

console.log(del);
console.log(map);

// 집과 치킨집 거리 총합을 구해
function len_chiken(map) {}

// 조합중 가장 가까운 거리만 출력
console.log(minValue);
