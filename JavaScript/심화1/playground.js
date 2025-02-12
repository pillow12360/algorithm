let li = new Array(5).fill(0);
li[0] = 3;
ls = li.map((a) => a + 1);

console.log(li);

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString();

let arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];

let arrMap = arr.map((a) => {
  return a + 1;
});

let arrFor = arr.forEach((a) => {
  process.stdout.write(a + ' ');
});

function factori(n) {
  if (n === 1) {
    return 1;
  } else {
    return factori(n - 1) * n;
  }
}

console.log(factori(5));

const arr3 = [
  { name: '사과', cat: '과일', price: 3000 },
  { name: '오이', cat: '채소', price: 1500 },
  { name: '당근', cat: '채소', price: 2000 },
  { name: '살구', cat: '과일', price: 2500 },
  { name: '피망', cat: '채소', price: 3500 },
  { name: '딸기', cat: '과일', price: 5000 },
];

console.log(
  '과일 목록:',
  arr3
    .filter(({ cat }) => cat === '과일')
    .map(({ name }) => name)
    .join(', ')
);

let ten = Array.from({ length: 10 })
  .fill(0)
  .map((_, a) => {
    return a + 1;
  });
console.log(ten);

const numbers = [1, 2, 3, 4, 5];

const modified = numbers.map((value, index, array) => {
  console.log(`현재 값: ${value}, 인덱스: ${index}, 원본 배열: ${array}`);
  return value * 2;
});

console.log(modified);
