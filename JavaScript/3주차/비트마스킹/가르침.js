// antaic 는 무조건 배워야 함!
// 비트 마스킹 방식으로 이미 배운 문자 확인 및 정리

// 백트래킹 조합을 이용하여 배우는 경우의 수 구하기

// 5글자 이하면 아무것도 말할 수 없음
/*
  비트마스킹 활용
	•	각 문자를 비트마스크로 표현하여 K개의 문자 선택 여부를 체크.
	•	알파벳 26개를 26비트 비트마스크로 관리 (00000000000000000000000000).

  백트래킹을 이용하여 K-5개의 글자 선택
    •	“a, n, t, i, c”는 반드시 포함되므로,
  남은 K-5개의 글자를 선택하는 모든 조합을 탐색.
*/

const fs = require('fs');
const input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [N, K] = input[0].split(' ').map(Number);
let words = input.slice(1);

const BASE_MASK =
  (1 << ('a'.charCodeAt(0) - 97)) |
  (1 << ('n'.charCodeAt(0) - 97)) |
  (1 << ('t'.charCodeAt(0) - 97)) |
  (1 << ('i'.charCodeAt(0) - 97)) |
  (1 << ('c'.charCodeAt(0) - 97));

let wordMasks = words.map((word) => {
  let mask = 0;
  for (let char of word) {
    mask |= 1 << (char.charCodeAt(0) - 97);
  }
  return mask;
}); // 말하려는 각 단어를 비트로 저장

// K가 5 미만이면 기본 문자("antic")도 못 배우므로 0 출력
if (K < 5) {
  console.log(0);
  process.exit();
}

// 만약 K == 26이면 모든 알파벳을 배울 수 있으므로 전체 단어 개수 출력
if (K == 26) {
  console.log(N);
  process.exit();
}

let maxReadable = 0; //읽을 수 있는 단어 수 answer
let totalAlphabets = 26;
let learned = BASE_MASK; // 기본적으로 "antic" 포함

function countReadableWords(learned) {
  //읽을 수 있는 단어 수 세기
  let count = 0;
  for (let mask of wordMasks) {
    if ((mask & learned) === mask) count++; // 모든 글자가 포함되었는지 확인
    // 비트마스크 & 연산으로 배운 단어가 현재 단어에 모두 포함되어있는지 확인
  }
  return count;
}

function backtrack(start, learned, selectedCount) {
  if (selectedCount === K - 5) {
    // K-5개 선택 완료
    maxReadable = Math.max(maxReadable, countReadableWords(learned));
    return;
  }

  for (let i = start; i < totalAlphabets; i++) {
    if (!(BASE_MASK & (1 << i))) {
      // "antic"가 아닌 알파벳만 선택
      backtrack(i + 1, learned | (1 << i), selectedCount + 1);
    }
  }
}

backtrack(0, learned, 0);
console.log(maxReadable);
