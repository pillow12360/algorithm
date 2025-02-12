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
