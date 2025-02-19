const numbers = [1, 2, 3, 4, 5];

const answer = numbers.map((cur) => {
  return (cur = cur * cur);
});

console.log(answer);

const words = ['hello', 'world', 'javascript', 'higher-order'];

const answer2 = words.map((cur) => {
  return cur.toUpperCase();
});

console.log(answer2);

let arr = [1, 2, 3, 4, 5];

let obj = {
  a: 1,
  b: 2,
  c: 3,
  d: 4,
  e: 5,
};

for (let i of arr) {
  console.log(`of `, i);
} // 값

for (let i in arr) {
  console.log(`in `, i);
  console.log(`in arr[i]`, arr[i]);
} // 인덱스
