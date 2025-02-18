let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [n, m] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(' ').map(Number));

// console.log(n, m, map);

function combi(arr, n) {
  const result = [];

  function backtrack(start, temp) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(i + 1, temp);
      temp.pop();
    }
  }

  backtrack(0, []);
  return result;
}

let chiken = [];
let houses = [];

// 치킨집과 집을 분리하여 저장
for (let i = 0; i < n; i++) {
  for (let j = 0; j < n; j++) {
    if (map[i][j] === 2) {
      chiken.push([i, j]); // 치킨집 좌표 저장
    } else if (map[i][j] === 1) {
      houses.push([i, j]); // 집 좌표 저장
    }
  }
}

// console.log(`현재 치킨집 목록:`, chiken);

let del = combi(chiken, m); // m개의 치킨집을 유지하는 모든 조합
// console.log(`치킨집 조합 목록:`, del);

let minValue = Infinity;

// 집과 치킨집 거리 총합을 계산하는 함수
function len_chiken(selectedChickens) {
  let totalDistance = 0;

  // 모든 집을 탐색
  houses.forEach(([hx, hy]) => {
    let minDistance = Infinity;

    // 각 집에서 가장 가까운 치킨집 찾기
    selectedChickens.forEach(([cx, cy]) => {
      let distance = Math.abs(hx - cx) + Math.abs(hy - cy);
      minDistance = Math.min(minDistance, distance);
    });

    totalDistance += minDistance;
  });

  return totalDistance;
}

// 조합별로 도시의 치킨 거리 계산
del.forEach((combo) => {
  minValue = Math.min(len_chiken(combo), minValue);
});

// 조합 중 가장 가까운 치킨 거리 출력
console.log(minValue);
