let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

function processInput(input) {
  let currentLine = 0;

  const totalCases = parseInt(input[currentLine++]);

  for (let t = 0; t < totalCases; t++) {
    const n = parseInt(input[currentLine++]);

    const items = {};

    let cnt = 0;

    for (let i = 0; i < n; i++) {
      // 입력: "아이템명 카테고리" 형태
      const [item, category] = input[currentLine++].split(' ');

      // items 객체에 category 라는 키가 없으면 배열로 초기화
      if (!items[category]) {
        items[category] = [];
      }

      // 해당 카테고리 배열에 새 item 추가
      items[category].push(item);

      // 아이템 개수를 세는 용도인 것 같으므로 cnt를 증가
      cnt++;
    }

    // 카테고리의 총 개수를 구하고 싶다면?

    console.log(getTotal(items));
  }
}

processInput(input);

function getTotal(items) {
  let totalCombi = 1; // 곱셈을 위해 초기값 1

  // 각 카테고리별로 (아이템 개수 + 1) 값을 곱해줌
  for (const category in items) {
    totalCombi *= items[category].length + 1;
  }

  // 모두 선택하지 않는 경우(1가지) 제외
  return totalCombi - 1;
}
