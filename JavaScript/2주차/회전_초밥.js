const fs = require('fs');

let input = fs.readFileSync('io.txt').toString().trim().split('\n');
let [n, d, k, c] = input[0].split(' ').map(Number);
let belt = input.slice(1).map(Number);

// 2️원형 테이블 고려 (배열 2배 확장)
let chobab = [...belt, ...belt];

// 3️ 슬라이딩 윈도우 알고리즘
let maxTypes = 0;
let window = new Map(); // 현재 윈도우 내 초밥 개수를 저장할 Map

// 초기 윈도우 구성
for (let i = 0; i < k; i++) {
  window.set(chobab[i], (window.get(chobab[i]) || 0) + 1);
}

// 4초기 상태에서 최대 가짓수 설정
let uniqueCount = window.size;

// 쿠폰 초밥이 윈도우 내부에 없으면 추가 가능
if (!window.has(c)) {
  uniqueCount++; // 쿠폰 초밥 추가
}

maxTypes = uniqueCount;

// 5️슬라이딩 윈도우 이동
for (let i = 0; i < n; i++) {
  // 앞쪽 초밥 제거
  let removeSushi = chobab[i];
  window.set(removeSushi, window.get(removeSushi) - 1);
  if (window.get(removeSushi) === 0) {
    window.delete(removeSushi);
  }

  // 뒤쪽 초밥 추가
  let addSushi = chobab[i + k];
  window.set(addSushi, (window.get(addSushi) || 0) + 1);

  // 새로운 초밥 종류 개수 계산
  let uniqueCount = window.size;

  // 쿠폰 초밥이 윈도우 내부에 없으면 추가
  if (!window.has(c)) {
    uniqueCount++;
  }

  // 최대 초밥 가짓수 업데이트
  maxTypes = Math.max(maxTypes, uniqueCount);
}

console.log(maxTypes);
