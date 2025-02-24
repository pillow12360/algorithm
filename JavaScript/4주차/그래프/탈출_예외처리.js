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
R = +R;
C = +C;

// 지도 읽기
let map = input.slice(1).map((i) => i.split(''));

// 방문 배열
let visited = Array.from({ length: R }, () =>
  Array.from({ length: C }).fill(false)
);

let dr = [-1, 1, 0, 0];
let dc = [0, 0, -1, 1];

// 범위 체크 함수
function isRange(r, c) {
  return 0 <= r && r < R && 0 <= c && c < C;
}

/**
 * 물이 차는 시간을 지도에 표시하는 BFS
 * 물이 퍼진 칸은 `map[r][c] = day` (숫자) 형태로 기록
 * (이미 '*'로 표시된 곳에서 시작)
 */
function water(waterQ) {
  let q = waterQ; // 물의 시작 지점들을 담은 큐
  while (q.length) {
    let [c_r, c_c, day] = q.shift();

    for (let i = 0; i < 4; i++) {
      let n_r = c_r + dr[i];
      let n_c = c_c + dc[i];

      if (isRange(n_r, n_c)) {
        // 아직 물이 안 차있고, 돌(X)이나 비버 굴(D)이 아닌 곳만
        if (map[n_r][n_c] === '.') {
          // day+1 시간에 물이 찰 것
          q.push([n_r, n_c, day + 1]);
          // 물이 도달하는 시간을 지도에 숫자로 기록
          map[n_r][n_c] = day;
        }
      }
    }
  }
}

let waterQ = [];
// 고슴도치 위치 , BFS 시작 인덱스
let s_r = 0;
let s_c = 0;

// 초기 세팅: 물(*), 비버 굴(D), 고슴도치(S) 위치 파악
for (let i = 0; i < R; i++) {
  for (let j = 0; j < C; j++) {
    if (map[i][j] === '*') {
      // 물 BFS를 위해 큐에 넣을 때, 시간은 1분부터 시작
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

// 물 확산 BFS 실행
water(waterQ);

/**
 * 고슴도치 이동 BFS
 * - day: 현재까지 걸린 시간
 * - 물이 이미 차거나 곧 찰 칸( map[n_r][n_c] ≤ (day+1) )은 이동 불가능
 * - D를 찾으면 그 즉시 시간(day+1) 출력 후 종료
 */
function goseam(r, c) {
  let day = 0;
  let q = [[r, c, day]];
  visited[r][c] = true;

  while (q.length) {
    let [c_r, c_c, curDay] = q.shift();

    for (let i = 0; i < 4; i++) {
      let n_r = c_r + dr[i];
      let n_c = c_c + dc[i];

      if (!isRange(n_r, n_c)) continue;
      if (visited[n_r][n_c]) continue;

      // 비버 굴(D) 만나면 즉시 결과 출력
      if (map[n_r][n_c] === 'D') {
        console.log(curDay + 1);
        process.exit();
      }

      // 돌(X)이나 물(*) 칸은 못 감
      if (map[n_r][n_c] === 'X' || map[n_r][n_c] === '*') {
        continue;
      }

      /**
       * [수정된 조건 설명]
       * - 만약 물 BFS가 해당 칸에 도달했다면 => map[n_r][n_c] 는 숫자(물 도착 시간)
       *   => 그 값이 curDay+1 보다 작거나 같으면, 이미 물이 찼거나 곧 찰 칸이므로 이동 불가
       * - 아직 물이 도달하지 않은 칸('.') 이라면 -> 그냥 이동 가능
       */
      if (
        (typeof map[n_r][n_c] === 'number' && map[n_r][n_c] > curDay + 1) ||
        map[n_r][n_c] === '.' ||
        // 혹시 S를 다시 만나는 일은 없겠지만(시작 칸 제외) 예외 처리
        map[n_r][n_c] === 'S'
      ) {
        visited[n_r][n_c] = true;
        // 다음 이동 시간 = curDay + 1
        q.push([n_r, n_c, curDay + 1]);
        // 지도에 고슴도치가 도달한 시간을 덮어쓰는 로직(원래 코드와 동일)
        map[n_r][n_c] = curDay + 1;
      }
    }
  }
}

// 고슴도치 BFS 시도
goseam(s_r, s_c);

// 만약 BFS가 끝날 때까지 D에 도달 못했다면 “KAKTUS”
console.log('KAKTUS');

/*
1.	고슴도치 BFS에서 '.'인 칸도 이동 가능하도록 조건 분기
	•	기존에는 map[n_r][n_c] > day + 1 형태의 “숫자 비교”만 있어서, '.' 문자열과 숫자 사이의 비교가 제대로 동작하지 않는 문제가 있었습니다.

	•	수정 후, '.'인 경우 그냥 이동 가능하다고 처리하고, 만약 숫자인 경우엔 물의 도착 시간(map[n_r][n_c])과 비교해서 더 늦게 오면 이동 가능하다고 처리합니다.
	
  2.	비버 굴(D) 발견 시 즉시 종료
	•	기존 코드에 이미 process.exit()를 써서 바로 종료하도록 했는데, 이 로직은 유지하며, 확인 차원에서 주석만 덧붙였습니다.
	
  3.	돌(X)과 물(*) 칸은 이동 불가
	•	원본 코드와 마찬가지로, 고슴도치 BFS에서는 이 칸들을 스킵합니다.
	
  4.	맵에 물 도착 시간을 기록할 때 map[r][c] = day;로 숫자를 대입하고, 고슴도치는 이 
  값을 참조하여 이동 가능 여부를 판별
	•	이때 typeof map[r][c] === 'number'인지 확인 후 (물도착 시간 > 고슴도치 이동 시간)인지 비교합니다.
	•	물이 도달하지 않은 '.'은 그대로 '.'로 남으므로 “완전히 물이 못 오는 안전 구역”이라는 의미가 됩니다.
*/
