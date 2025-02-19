function getCombinations(arr, r) {
  let n = arr.length;
  let result = [];

  for (let bitmask = 0; bitmask < 1 << n; bitmask++) {}
}

for (let bitmask = 0; bitmask < 1 << 3; bitmask++) {
  console.log(bitmask.toString(2).padStart(3, '0'));
}

//toString => 2진수 비트로 변경
// padStart(n,'0') n자리로 맞추고 빈자리는 '0'으로 채워줌

// 1<<i i번째 비트만 1로 만들어 버리고 나머지는 0으로 바꿈

// 결과가 0이면 원소 포함 안됨 0이아니면 해당 원소가 포함됨

// 특정 2개의 조합을 선택 -> 백트래킹
// 모든 부분집합을 구하는 방법 -> 비트마스킹

// 비트마스킹이 유리한건 n 이 20보다 작을때만, 더 크면 백트래킹이 유리함

/*
모든 부분집합(멱집합) → 비트마스크 (O(2^N * N))
r개의 조합(NCr) → 백트래킹 (O(NCr))
비트마스크는 N이 작을 때 (N ≤ 20), 백트래킹은 N이 클 때 (N > 20) 적절
*/
