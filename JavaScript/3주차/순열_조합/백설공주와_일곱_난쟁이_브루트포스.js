let fs = require('fs');

let input;
try {
  input = fs.readFileSync('io.txt', 'utf8').trim().split('\n').map(Number);
  if (input.length !== 9)
    throw new Error('입력 개수 오류: 9개의 숫자가 입력되어야 합니다.');
} catch (error) {
  console.error('파일 읽기 오류:', error.message);
  process.exit(1);
}

let totalSum = input.reduce((sum, v) => sum + v, 0);

for (let i = 0; i < 9; i++) {
  for (let j = i + 1; j < 9; j++) {
    if (totalSum - (input[i] + input[j]) === 100) {
      let result = input.filter((_, idx) => idx !== i && idx !== j);
      result.forEach((num) => console.log(num));
      process.exit(0); // 정답이 유일하므로 즉시 종료
    }
  }
}
