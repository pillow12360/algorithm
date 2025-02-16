let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [n, m, b] = input[0].split(' ').map(Number);
let map = input.slice(1).map((i) => i.split(' ').map(Number));

let minTime = Infinity;
let min_h = 0;

// 현재 땅의 최소 높이와 최대 높이 계산
let h_min = Math.min(...map.flat()); // 가장 낮은 높이
let h_max = Math.max(...map.flat()); // 가장 높은 높이

// 가능한 모든 높이 탐색 (h_min ~ h_max 범위)
for (let h = h_min; h <= h_max; h++) {
  let removeBlocks = 0; // 제거해야 하는 블록 개수
  let addBlocks = 0; // 추가해야 하는 블록 개수

  for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
      let diff = map[i][j] - h; // 현재 높이와 목표 높이 차이

      if (diff > 0) {
        removeBlocks += diff; // 높이를 낮추기 위해 제거해야 하는 블록 개수
      } else if (diff < 0) {
        addBlocks += -diff; // 높이를 높이기 위해 추가해야 하는 블록 개수
      }
    }
  }

  // 인벤토리 블록으로 추가할 블록을 커버할 수 있는지 확인
  if (removeBlocks + b >= addBlocks) {
    let cur_time = removeBlocks * 2 + addBlocks * 1; // 제거는 2초, 추가는 1초

    // 최소 시간 업데이트 및 높이 결정
    if (cur_time < minTime) {
      minTime = cur_time;
      min_h = h;
    } else if (cur_time === minTime) {
      min_h = Math.max(min_h, h); // 같은 시간이라면 더 높은 높이 선택
    }
  }
}

console.log(`${minTime} ${min_h}`);
