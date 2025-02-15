let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('');

// console.log(input);

let alpha = Array(26);
alpha = alpha.fill(0);

const alpha2 = {
  a: 0,
  b: 1,
  c: 2,
  d: 3,
  e: 4,
  f: 5,
  g: 6,
  h: 7,
  i: 8,
  j: 9,
  k: 10,
  l: 11,
  m: 12,
  n: 13,
  o: 14,
  p: 15,
  q: 16,
  r: 17,
  s: 18,
  t: 19,
  u: 20,
  v: 21,
  w: 22,
  x: 23,
  y: 24,
  z: 25,
};

input.forEach((a) => {
  alpha[alpha2[a]] += 1;
});

alpha.forEach((a) => {
  process.stdout.write(a + ' ');
});
