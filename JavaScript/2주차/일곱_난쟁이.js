let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n').map(Number);

function sub(num, index = 0, current = []) {
  // 7길이의 연속되지 않는 부분 수열
  if (index === num.length) {
    if (current.length === 7) {
      let sumNum = current.reduce((acc, cur) => {
        return (acc += cur);
      }); // 요소 합 구하기
      if (sumNum === 100) {
        current.sort((a, b) => a - b); // 오름차순 정렬
        current = current.forEach((a) => {
          console.log(a); // 출력
        });
      }
    }
    return;
  }
  sub(num, index + 1, current);

  sub(num, index + 1, [...current, num[index]]);
}

sub(input);
