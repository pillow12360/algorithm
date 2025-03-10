// 한개의 모음과 // 최소 두개의 자음으로 구성
// 사전순 증가하는 순서

// 문자종류 c가지

// 그러면 저 조건을 만족하는 증가하는 수열

// 모음 체크 함수
function isVowel(ch) {
  return ['a', 'e', 'i', 'o', 'u'].includes(ch);
}

// 조건 체크 함수: 모음 최소 1개, 자음 최소 2개
function isValid(sequence) {
  let vowels = 0,
    consonants = 0;

  sequence.forEach((ch) => {
    if (isVowel(ch)) vowels++;
    else consonants++;
  });

  return vowels >= 1 && consonants >= 2;
}

// 백트래킹을 이용한 증가하는 부분 수열 탐색 함수
function findSequences(chars, targetLength) {
  chars.sort(); // 알파벳 순 정렬
  const result = [];

  function backtrack(start, path) {
    if (path.length === targetLength) {
      if (isValid(path)) result.push(path.join(''));
      return;
    }

    for (let i = start; i < chars.length; i++) {
      path.push(chars[i]);
      backtrack(i + 1, path);
      path.pop(); // 백트래킹: 마지막 요소 제거
    }
  }

  backtrack(0, []);
  return result;
}

// 사용 예제

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let [l, c] = input[0].split(' ').map(Number);
let chars = input[1].split(' ');
// console.log(chars);
const sequences = findSequences(chars, l);

console.log(sequences.join('\n'));
