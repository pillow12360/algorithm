let fs = require('fs');

// 파일 입력 처리
let input;
try {
  input = fs.readFileSync('io.txt', 'utf8').trim().split('\n').map(Number);
  if (input.length !== 9)
    throw new Error('입력 개수 오류: 9개의 숫자가 입력되어야 합니다.');
} catch (error) {
  console.error('파일 읽기 오류:', error.message);
  process.exit(1);
}

function Combinations(arr, n) {
  const result = [];

  function backtrack(temp, start) {
    if (temp.length === n) {
      result.push([...temp]); // 깊은 복사하여 추가
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(temp, i + 1);
      temp.pop();
    }
  }

  backtrack([], 0);
  return result;
}

let combi = Combinations(input, 2);

for (let [exclude1, exclude2] of combi) {
  let filtered = input.filter((num) => num !== exclude1 && num !== exclude2); // 두 요소를 제외한 배열

  if (filtered.reduce((sum, v) => sum + v, 0) === 100) {
    filtered.forEach((num) => console.log(num));
    process.exit(0);
  }
}
