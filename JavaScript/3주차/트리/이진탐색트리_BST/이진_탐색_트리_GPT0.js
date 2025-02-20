// 빠른 입출력을 위해 node.js 환경에서 가정한 예시입니다.
// 백준 환경: fs 모듈 등으로 입력 받아서 처리.
// 브라우저라면 로직만 잘 참고하세요.

const fs = require('fs');
const input = fs.readFileSync('io.txt').toString().trim().split('\n');
// const input = `4
// 1
// 2
// 3
// 4
// `.split('\n'); // 직접 테스트 시 예시

// Fenwick(BIT) 트리 구현
class Fenwicks {
  constructor(n) {
    this.n = n; // Fenwicks 트리의 크기
    this.tree = new Array(n + 1).fill(0); // 1 ~ n 인덱스 사용
  }

  // 부분합(prefix sum) 구하기: 1 ~ i
  sum(i) {
    let s = 0;
    while (i > 0) {
      s += this.tree[i];
      i -= i & -i;
    }
    return s;
  }

  // Fenwicks 트리에 업데이트
  update(i, delta) {
    while (i <= this.n) {
      this.tree[i] += delta;
      i += i & -i;
    }
  }

  // Fenwicks 트리의 누적합을 이용하여
  // "prefix sum == k"가 되는 위치(1-based)를 찾는 함수
  // (lowerBound 느낌. sum(pos) >= k를 만족하는 가장 작은 pos)
  // ※ 아래 구현은 'k 이하' 원소 갯수를 보고 pos를 찾는 전형적인 이진 탐색 기법
  findIndex(k) {
    // k번째 1이 들어있는 위치(=rank -> 실제 값)의 Fenwicks 인덱스를 찾는다.
    let pos = 0;
    // 최대 크기보다 작거나 같은 2의 거듭제곱 찾기
    // 예: n=300000이면 대략 2^18 = 262144 정도.
    let bitMask = 1 << 18;
    while (bitMask > 0) {
      let nextPos = pos + bitMask;
      if (nextPos <= this.n && this.tree[nextPos] < k) {
        // k보다 작다면 해당 구간 누적값을 빼고 pos 이동
        k -= this.tree[nextPos];
        pos = nextPos;
      }
      bitMask >>= 1;
    }
    return pos + 1;
  }
}

// 메인 풀이
function solve() {
  const N = +input[0];
  let idx = 1;

  // depth 배열: 문제에서 요구하는 각 값의 "트리 깊이"
  // 0과 N+1도 쓸 것이므로 길이는 N+2
  const depth = new Array(N + 2).fill(0);
  depth[0] = -1; // 문제 설명에 맞춤
  depth[N + 1] = -1; // 문제 설명에 맞춤

  // Fenwicks 트리 생성 (크기: N+2)
  // 문제의 값 0 → Fenwicks 인덱스 1
  // 문제의 값 N+1 → Fenwicks 인덱스 (N+1)+1 = N+2
  const fenwicks = new Fenwicks(N + 2);

  // 0, N+1을 미리 삽입
  fenwicks.update(1, 1); // 0 삽입
  fenwicks.update(N + 2, 1); // N+1 삽입

  let count = 0n; // 깊이 누적 합 (커질 수 있으니 BigInt)
  const output = [];

  for (let i = 0; i < N; i++) {
    const num = +input[idx++];

    // 현재 num 보다 작거나 같은 값이 Fenwicks 상 몇 개 있나?
    // => rank = fenwicks.sum(num+1)
    //    (문제 값 num -> Fenwicks 에선 num+1 위치)
    // 다만, "직접 lower/higher"를 구해야 하므로,
    //   - leftNeighbor = findIndex(rank) - 1
    //   - rightNeighbor = findIndex(rank+1) - 1
    //   여기서 rank는 "num 이하 원소가 몇 개?" 값.
    const rank = fenwicks.sum(num + 1);

    // 왼쪽 이웃 (lower(num))
    // rank번째로 작은 원소 => Fenwicks findIndex(rank)
    // 문제 인덱스로는 -1 해야 실제 값
    const leftFen = fenwicks.findIndex(rank);
    const leftVal = leftFen - 1;

    // 오른쪽 이웃 (higher(num))
    // (rank+1)번째 원소
    const rightFen = fenwicks.findIndex(rank + 1);
    const rightVal = rightFen - 1;

    // 깊이 계산
    depth[num] = Math.max(depth[leftVal], depth[rightVal]) + 1;

    // 누적
    count += BigInt(depth[num]);
    output.push(count.toString());

    // Fenwicks 트리에 삽입
    fenwicks.update(num + 1, 1);
  }

  console.log(output.join('\n'));
}

solve();
